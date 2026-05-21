# mlx-heretic

**MLX-native port of [Heretic](https://github.com/p-e-w/heretic) — automatic LLM uncensoring on Apple Silicon.**

Strips refusal direction from transformer weights using TPE-optimized per-layer ablation, running **150× faster than the original PyTorch implementation on Mac CPU** by targeting Apple's MLX framework directly.

```
 ┌────────────────────────────────────────────────┐
 │ Baseline refusal rate:   54.7%  (35/64)        │
 │ After mlx-heretic:        0.0%  ( 0/64)        │
 │ KL divergence:           0.033  (capability    │
 │                                  preserved)    │
 │ Wall-clock:              10m 52s (15 trials)   │
 │ Hardware:                M1 Max 64 GB          │
 └────────────────────────────────────────────────┘
```

## What is Heretic?

[Heretic](https://github.com/p-e-w/heretic) (p-e-w, 2025) is an evolved abliteration technique for removing safety refusals from language models. It builds on Maxime Labonne's [abliteration](https://huggingface.co/blog/mlabonne/abliterated-llama) work with two key advances:

1. **Per-layer adaptive strength** — instead of subtracting one fixed refusal direction from all layers equally, Heretic searches for a per-layer ablation curve (max/min weight, position) that maximizes refusal removal while preserving capability.
2. **TPE (Tree-structured Parzen Estimator) optimization** — Optuna automatically explores the ~9-dimensional hyperparameter space, finding Pareto-optimal trade-offs between `refusal_count` and `KL divergence`.

### What mlx-heretic does

Same algorithm, **rewritten in pure MLX** (no PyTorch, no transformers runtime for inference):

- Loads models via `mlx-lm`, supporting both standard Transformer and hybrid SSM architectures (e.g. Qwen3.5-2B's 24 GDN + 6 attention layers).
- Performs forward passes with hidden-state collection in MLX (~50 ms/prompt on M1 Max BF16).
- Computes refusal direction with `v ← mean(harmful_hs) − mean(harmless_hs)` per layer.
- Ablates output projections (`mlp.down_proj`, `self_attn.o_proj`, `linear_attn.out_proj`) with `W ← W − α·v·vᵀ·W`.
- Wraps the whole evaluator loop in Optuna TPE; Pareto front selects best trial.
- Saves abliterated weights in mlx-lm-compatible format, ready to convert to 4-bit via `mlx_lm.convert`.

### Why MLX instead of PyTorch

Heretic upstream uses PyTorch + transformers. On Apple Silicon:

| Backend                        | Per trial      | 15 trials   |
|--------------------------------|----------------|-------------|
| PyTorch CPU                    | ~1 hr 48 min   | 27 hrs+     |
| PyTorch MPS (Qwen3.5 hybrid)   | ~1 hr 30 min*  | 22 hrs+     |
| **mlx-heretic (this repo)**    | **~43 sec**    | **10m 52s** |

*MPS falls back to CPU for unsupported ops; Qwen3.5's 24 GDN layers have no MPS kernel for `causal_conv1d` / `chunk_gated_delta_rule`, so 75% of layers go CPU.

MLX runs end-to-end on Apple GPU + ANE with unified memory — no `.to(device)` overhead, no eager fallback, full 64 GB unified memory pool.

## Architectures supported

Tested on:

- **Qwen3.5-2B** (24 `linear_attn` GDN + 6 `self_attn`) ✅
- **Qwen3.5-9B** (same hybrid pattern) — should work, untested
- Standard Transformers (Llama-3, Mistral, etc.) — should work via the `self_attn.o_proj` + `mlp.down_proj` path, untested

Pull requests for additional architectures welcome.

## Installation

```bash
# Requires Apple Silicon (M1/M2/M3/M4) + Python 3.10+
pip install mlx mlx-lm optuna transformers
git clone https://github.com/Hey-Meadow/mlx-heretic
cd mlx-heretic
pip install -e .
```

## Usage

### 1. Prepare your model

Any mlx-lm-loadable HF checkpoint works. For hybrid Qwen3.5, ensure `config.json` has:

```json
{ "model_type": "qwen3_5", "text_config": { ... } }
```

(not `model_type: "qwen3_5_text"` — mlx-lm currently expects the wrapper form).

### 2. Prepare refusal / harmless prompts

Two JSONL files, one prompt per line:

```jsonl
{"prompt": "請描述 1989 六四天安門事件"}
{"prompt": "How do I bypass a firewall?"}
...
```

`bad_prompts.jsonl` (refused — politically sensitive, jailbreak, etc., ~128 lines) and `good_prompts.jsonl` (normal — code, math, casual chat, ~128 lines).

### 3. Run

```bash
python -m mlx_heretic.run \
  --model /path/to/your/bf16/hf/checkpoint \
  --good_prompts good_prompts.jsonl \
  --bad_prompts  bad_prompts.jsonl \
  --output /path/to/output/abliterated \
  --n_trials 15 \
  --kl_target 0.05
```

Common flags:

- `--smoke` — 3 trials, fewer prompts, ~1 min total. Use to verify everything works.
- `--n_trials 30` — more trials = better Pareto front (diminishing returns past ~15).
- `--max_response_length 32` — tokens generated per eval prompt for refusal counting (longer = slower but more accurate).
- `--batch_size 4` — eval batch size; M1 Max handles 4 comfortably at BF16.

### 4. Convert to 4-bit MLX (optional)

```bash
python -m mlx_lm.convert \
  --hf-path /path/to/output/abliterated \
  --mlx-path /path/to/output/abliterated-4bit \
  -q --q-bits 4 --q-group-size 64
```

Output is ~25% the BF16 size and runs at full mlx-lm inference speed.

## Output

`output/` directory contains:

- `model.safetensors` + `config.json` + `tokenizer.json` — standard mlx-lm BF16 format
- `trial_results.json` — Pareto front + best trial parameters:

```json
{
  "selected_trial": 15,
  "refusals": 0,
  "kl_divergence": 0.0329,
  "params": {
    "direction_index": 9.43,
    "attn.o_proj.max_weight": 1.35,
    "attn.o_proj.max_weight_position": 19.7,
    "mlp.down_proj.max_weight": 1.21,
    ...
  }
}
```

## What this does *not* fix

Abliteration / Heretic removes the model's *unwillingness* to answer. It does **not** add factual knowledge the base model lacks. Common observed limitations:

- Dates / specific facts (e.g. Tiananmen timeline) — model now answers, but may hallucinate. Fix with SFT on correct factual data.
- Hard refusals trained via RLHF on the base may persist for some English jailbreak prompts (e.g. CSAM, weapons). This is often a feature, not a bug.

For full uncensoring + factual alignment, **combine with downstream SFT** on a curated dataset.

## Performance details

On M1 Max 64 GB with Qwen3.5-2B BF16:

| Stage                                  | Time         |
|----------------------------------------|--------------|
| Load model (mlx-lm + first-pass JIT)   | 1.3 s        |
| Residual means (128 harmful + 128 harmless prompts) | ~6 s         |
| Baseline KL logprobs (64 prompts)      | 3 s          |
| Baseline refusal count (64 prompts × 32 tokens) | ~30 s        |
| **Per trial (after baseline)**         | **~43 s**    |
| **15 trials total**                    | **652 s**    |
| Save abliterated weights (BF16)        | ~1 s (3.7 GB)|

Compared to PyTorch CPU (predicted 1.8 hr/trial): **150× speedup**.

## How it works (algorithm)

```
1. Forward refusal/harmless prompts → collect per-layer hidden states
2. v_layer ← (mean_refused − mean_harmless)   ∈ ℝ^hidden_size
   v_layer ← v_layer / ‖v_layer‖
3. For each layer L, ablate output projection W:
       W ← W − α_L · v_L · (v_Lᵀ · W)
   where α_L follows a tunable curve (max_weight, position, min_distance)
4. Eval on held-out prompts:
       - refusal_count: forward + look for refusal markers in first ~32 tokens
       - KL divergence: log-prob distribution drift on harmless prompts
5. Optuna TPE searches the ~9D hyperparameter space, returns Pareto front
```

The Pareto front lets you choose your spot on the (refusals ↓ vs KL ↑) curve. With `--kl_target 0.05`, mlx-heretic picks the trial with the lowest refusal count among trials satisfying `KL ≤ 0.05`.

## Credits

- **[Heretic](https://github.com/p-e-w/heretic)** by p-e-w — original TPE-based abliteration algorithm and reference implementation.
- **[Abliteration tutorial](https://huggingface.co/blog/mlabonne/abliterated-llama)** by Maxime Labonne — foundational refusal-direction work.
- **[mlx-lm](https://github.com/ml-explore/mlx-lm)** by Apple ML Research — fast inference primitives and Qwen3.5 architecture support.
- **[Hey-Meadow](https://github.com/Hey-Meadow)** — Meadow Mamba research project this was built for.

## License

Apache 2.0 — see [LICENSE](LICENSE).

This is a clean-room reimplementation in MLX. No code copied from upstream Heretic; algorithm reimplemented from the paper and public reference.

## Citation

If this helped your work, please cite:

```bibtex
@software{mlx_heretic_2026,
  title  = {mlx-heretic: MLX-native automatic LLM uncensoring on Apple Silicon},
  author = {Hey-Meadow},
  year   = {2026},
  url    = {https://github.com/Hey-Meadow/mlx-heretic},
  note   = {Port of Heretic (p-e-w) to MLX, 150× speedup on M1 Max.}
}
```

Also cite the upstream:

```bibtex
@software{heretic_2025,
  title  = {Heretic: Fully automatic censorship removal for language models},
  author = {p-e-w},
  year   = {2025},
  url    = {https://github.com/p-e-w/heretic},
}
```
