"""MLX-native Heretic CLI.

Usage:
    python -m mlx_heretic.run \
        --model /path/to/bf16 \
        --good_prompts good.jsonl --bad_prompts bad.jsonl \
        --n_trials 15 [--smoke]
"""
from __future__ import annotations

import argparse
import json
import math
import os
import random
import sys
import time
from dataclasses import asdict
from pathlib import Path

import mlx.core as mx
import optuna
from optuna import Trial
from optuna.samplers import TPESampler
from optuna.study import StudyDirection
from optuna.trial import TrialState

from .ablation import (
    AbliterationParameters,
    abliterate,
    compute_refusal_directions,
    restore_weights,
    snapshot_weights,
)
from .evaluator import (
    build_chat_ids,
    count_refusals,
    get_logprobs_for_prompts,
    is_refusal,
    kl_divergence,
)
from .model_io import get_residuals_last_token, load_model


def read_jsonl(path: str):
    out = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                out.append(json.loads(line)["text"])
    return out


def compute_residual_means(model, tokenizer, prompts, system_prompt, response_prefix):
    """Per-layer mean residual (last-token hidden state). Returns (n_layers+1, H) fp32."""
    acc = None
    n = 0
    for p in prompts:
        ids = build_chat_ids(tokenizer, p, system_prompt, response_prefix)
        h = get_residuals_last_token(model, ids)  # (1, L, H)
        mx.eval(h)
        h64 = h[0].astype(mx.float32)  # (L, H)
        if acc is None:
            acc = h64
        else:
            acc = acc + h64
        n += 1
    return acc / n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="/Users/akaihuangm1/Desktop/LLM/meadow-2b-v2/bf16_for_heretic")
    ap.add_argument("--output", default="/Users/akaihuangm1/Desktop/LLM/meadow-2b-v2/heretic_mlx")
    ap.add_argument("--good_prompts", default="/Users/akaihuangm1/Desktop/LLM/heretic/good_prompts.jsonl")
    ap.add_argument("--bad_prompts", default="/Users/akaihuangm1/Desktop/LLM/heretic/bad_prompts.jsonl")
    ap.add_argument("--system_prompt", default="你是 Meadow Mamba")
    ap.add_argument("--response_prefix", default="<think>\n\n</think>\n\n")
    ap.add_argument("--n_trials", type=int, default=15)
    ap.add_argument("--n_startup", type=int, default=5)
    ap.add_argument("--max_response_length", type=int, default=32)
    ap.add_argument("--n_eval_good", type=int, default=32, help="cap good prompts used for KL eval")
    ap.add_argument("--n_eval_bad", type=int, default=32, help="cap bad prompts used for refusal eval")
    ap.add_argument("--n_dir_good", type=int, default=64, help="cap good prompts for refusal-direction estimation")
    ap.add_argument("--n_dir_bad", type=int, default=64, help="cap bad prompts for refusal-direction estimation")
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--smoke", action="store_true", help="quick test: 3 trials, fewer prompts")
    ap.add_argument("--kl_target", type=float, default=0.01)
    ap.add_argument("--kl_scale", type=float, default=1.0)
    args = ap.parse_args()

    if args.smoke:
        args.n_trials = 3
        args.n_startup = 1
        args.n_eval_good = 16
        args.n_eval_bad = 16
        args.n_dir_good = 32
        args.n_dir_bad = 32

    random.seed(args.seed)
    mx.random.seed(args.seed)

    print(f"[mlx-heretic] Loading model from {args.model}")
    t_load = time.perf_counter()
    model, tokenizer = load_model(args.model)
    print(f"  loaded in {time.perf_counter()-t_load:.1f}s")
    n_layers = len(model.language_model.model.layers)
    print(f"  n_layers={n_layers}")

    print("[mlx-heretic] Loading prompts")
    good = read_jsonl(args.good_prompts)
    bad = read_jsonl(args.bad_prompts)
    print(f"  good: {len(good)}, bad: {len(bad)}")

    # Subsets
    dir_good = good[: args.n_dir_good]
    dir_bad = bad[: args.n_dir_bad]
    eval_good = good[: args.n_eval_good]
    eval_bad = bad[: args.n_eval_bad]

    print(f"[mlx-heretic] Computing residual means (good={len(dir_good)}, bad={len(dir_bad)})")
    t0 = time.perf_counter()
    good_means = compute_residual_means(model, tokenizer, dir_good, args.system_prompt, args.response_prefix)
    bad_means = compute_residual_means(model, tokenizer, dir_bad, args.system_prompt, args.response_prefix)
    mx.eval(good_means, bad_means)
    print(f"  residuals in {time.perf_counter()-t0:.1f}s, shape={good_means.shape}")

    refusal_directions = compute_refusal_directions(good_means, bad_means, orthogonalize=True)
    mx.eval(refusal_directions)
    print(f"  refusal_directions shape={refusal_directions.shape}")

    print("[mlx-heretic] Baseline first-token logprobs for eval_good")
    t0 = time.perf_counter()
    base_logprobs = get_logprobs_for_prompts(model, tokenizer, eval_good, args.system_prompt, args.response_prefix)
    mx.eval(base_logprobs)
    print(f"  {time.perf_counter()-t0:.1f}s, shape={base_logprobs.shape}")

    print("[mlx-heretic] Baseline refusal count on eval_bad")
    t0 = time.perf_counter()
    base_refusals = count_refusals(model, tokenizer, eval_bad, args.system_prompt, args.response_prefix, max_tokens=args.max_response_length)
    print(f"  base refusals: {base_refusals}/{len(eval_bad)}, {time.perf_counter()-t0:.1f}s")

    # Snapshot weights (so we can reset between trials).
    print("[mlx-heretic] Snapshotting weights for reset")
    t0 = time.perf_counter()
    snapshot = snapshot_weights(model)
    mx.eval(*list(snapshot.values()))
    print(f"  snapshotted {len(snapshot)} modules in {time.perf_counter()-t0:.1f}s")

    last_layer = n_layers - 1
    components = ["attn.o_proj", "mlp.down_proj"]

    start_time = time.perf_counter()
    trial_index = [0]
    results = []

    def objective(trial: Trial):
        trial_index[0] += 1
        idx = trial_index[0]
        trial.set_user_attr("index", idx)
        direction_scope = trial.suggest_categorical("direction_scope", ["global", "per layer"])
        direction_index = trial.suggest_float("direction_index", 0.4 * last_layer, 0.9 * last_layer)
        if direction_scope == "per layer":
            direction_index_eff = None
        else:
            direction_index_eff = direction_index

        params = {}
        for c in components:
            mw = trial.suggest_float(f"{c}.max_weight", 0.8, 1.5)
            mwp = trial.suggest_float(f"{c}.max_weight_position", 0.6 * last_layer, 1.0 * last_layer)
            mw_frac = trial.suggest_float(f"{c}.min_weight", 0.0, 1.0)
            mwd = trial.suggest_float(f"{c}.min_weight_distance", 1.0, 0.6 * last_layer)
            params[c] = AbliterationParameters(
                max_weight=mw,
                max_weight_position=mwp,
                min_weight=mw_frac * mw,
                min_weight_distance=mwd,
            )

        print(f"\n[Trial {idx}/{args.n_trials}]")
        print(f"  direction: {direction_scope} idx={direction_index:.2f}")
        for c, p in params.items():
            print(f"  {c}: mw={p.max_weight:.2f} pos={p.max_weight_position:.1f} min={p.min_weight:.2f} dist={p.min_weight_distance:.1f}")

        # Reset
        t_r = time.perf_counter()
        restore_weights(model, snapshot)
        # Apply abliteration
        abliterate(model, refusal_directions, direction_index_eff, params)
        # Force eval to materialize weights
        for _, _, mod in __import__("mlx_heretic.ablation", fromlist=["get_target_modules"]).get_target_modules(model):
            mx.eval(mod.weight)
        t_abl = time.perf_counter() - t_r

        # Eval KL
        t_e = time.perf_counter()
        ab_logprobs = get_logprobs_for_prompts(model, tokenizer, eval_good, args.system_prompt, args.response_prefix)
        mx.eval(ab_logprobs)
        kl = kl_divergence(ab_logprobs, base_logprobs)
        t_kl = time.perf_counter() - t_e

        t_g = time.perf_counter()
        refusals = count_refusals(model, tokenizer, eval_bad, args.system_prompt, args.response_prefix, max_tokens=args.max_response_length)
        t_gen = time.perf_counter() - t_g

        refusals_score = refusals / base_refusals if base_refusals > 0 else float(refusals)
        if kl >= args.kl_target:
            kld_score = kl / args.kl_scale
        else:
            kld_score = refusals_score * args.kl_target / args.kl_scale

        elapsed = time.perf_counter() - start_time
        print(f"  refusals={refusals}/{len(eval_bad)} (base {base_refusals})  KL={kl:.4f}  abl={t_abl:.1f}s kl={t_kl:.1f}s gen={t_gen:.1f}s  total_elapsed={elapsed:.0f}s")

        trial.set_user_attr("kl_divergence", kl)
        trial.set_user_attr("refusals", refusals)
        trial.set_user_attr("base_refusals", base_refusals)
        trial.set_user_attr("direction_index", direction_index_eff)
        trial.set_user_attr("parameters", {c: asdict(p) for c, p in params.items()})
        results.append({
            "trial": idx,
            "kl": kl,
            "refusals": refusals,
            "base_refusals": base_refusals,
            "direction_scope": direction_scope,
            "direction_index": direction_index_eff,
            "parameters": {c: asdict(p) for c, p in params.items()},
        })
        return kld_score, refusals_score

    optuna.logging.set_verbosity(optuna.logging.WARNING)
    study = optuna.create_study(
        sampler=TPESampler(n_startup_trials=args.n_startup, n_ei_candidates=128, multivariate=True, seed=args.seed),
        directions=[StudyDirection.MINIMIZE, StudyDirection.MINIMIZE],
        study_name="mlx_heretic",
    )

    try:
        study.optimize(objective, n_trials=args.n_trials)
    except KeyboardInterrupt:
        print("Interrupted.")

    completed = [t for t in study.trials if t.state == TrialState.COMPLETE]
    if not completed:
        print("No completed trials.")
        sys.exit(1)

    # Pareto
    sorted_trials = sorted(completed, key=lambda t: (t.user_attrs["refusals"], t.user_attrs["kl_divergence"]))
    min_div = math.inf
    pareto = []
    for t in sorted_trials:
        k = t.user_attrs["kl_divergence"]
        if k < min_div:
            min_div = k
            pareto.append(t)
    print("\n[mlx-heretic] Pareto front:")
    for t in pareto:
        print(f"  trial {t.user_attrs['index']}: refusals={t.user_attrs['refusals']}/{len(eval_bad)} KL={t.user_attrs['kl_divergence']:.4f}")

    best = pareto[0]
    print(f"\n[mlx-heretic] Selected trial {best.user_attrs['index']}: refusals={best.user_attrs['refusals']} KL={best.user_attrs['kl_divergence']:.4f}")

    # Apply best and save
    print("[mlx-heretic] Restoring and applying best params...")
    restore_weights(model, snapshot)
    best_params = {c: AbliterationParameters(**v) for c, v in best.user_attrs["parameters"].items()}
    abliterate(model, refusal_directions, best.user_attrs["direction_index"], best_params)
    for _, _, mod in __import__("mlx_heretic.ablation", fromlist=["get_target_modules"]).get_target_modules(model):
        mx.eval(mod.weight)

    out_dir = Path(args.output)
    out_dir.mkdir(parents=True, exist_ok=True)
    # Save MLX-format weights
    from mlx_lm.utils import save_model
    try:
        save_model(out_dir, model)
    except Exception as e:
        # Fallback manual save
        from mlx.utils import tree_flatten
        weights = dict(tree_flatten(model.parameters()))
        mx.save_safetensors(str(out_dir / "weights.safetensors"), weights)
    # Save tokenizer + config
    import shutil
    for fname in ("config.json", "tokenizer.json", "tokenizer_config.json", "chat_template.jinja", "generation_config.json"):
        src = Path(args.model) / fname
        if src.exists():
            shutil.copy(src, out_dir / fname)
    # Save results
    with open(out_dir / "trial_results.json", "w") as f:
        json.dump({
            "base_refusals": base_refusals,
            "selected_trial": best.user_attrs["index"],
            "trials": results,
        }, f, indent=2, ensure_ascii=False)
    print(f"[mlx-heretic] Saved abliterated model to {out_dir}")


if __name__ == "__main__":
    main()
