"""Ablation: subtract refusal direction from output-projection weights.

Original Heretic update (for full-rank, no row-norm preservation):
    W <- W - alpha * v v^T W
where v is unit-norm refusal direction in output space (hidden_size),
W is (out_features=hidden_size, in_features).

For MLX nn.Linear, weight shape is (out_features, in_features). So:
    v: (hidden,)
    v @ W -> (in_features,)
    outer(v, v @ W) -> (hidden, in_features)
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Tuple

import mlx.core as mx


@dataclass
class AbliterationParameters:
    max_weight: float
    max_weight_position: float
    min_weight: float
    min_weight_distance: float


def get_target_modules(model) -> List[Tuple[int, str, object]]:
    """List (layer_index, component, module) for each abliterable Linear.

    component is one of 'attn.o_proj' or 'mlp.down_proj'.
    """
    out = []
    for i, layer in enumerate(model.language_model.model.layers):
        # attn output
        if layer.is_linear:
            out.append((i, "attn.o_proj", layer.linear_attn.out_proj))
        else:
            out.append((i, "attn.o_proj", layer.self_attn.o_proj))
        # mlp down
        out.append((i, "mlp.down_proj", layer.mlp.down_proj))
    return out


def snapshot_weights(model) -> Dict[Tuple[int, str], mx.array]:
    """Save original weights so we can reset per trial."""
    snap = {}
    for i, comp, mod in get_target_modules(model):
        snap[(i, comp)] = mx.array(mod.weight)  # copy
    return snap


def restore_weights(model, snap: Dict[Tuple[int, str], mx.array]):
    """Restore weights from snapshot."""
    for i, comp, mod in get_target_modules(model):
        mod.weight = mx.array(snap[(i, comp)])


def _alpha_for_layer(layer_idx: int, params: AbliterationParameters) -> float:
    distance = abs(layer_idx - params.max_weight_position)
    if distance > params.min_weight_distance:
        return 0.0
    # Linear interp from max_weight at center to min_weight at min_weight_distance
    return params.max_weight + (distance / params.min_weight_distance) * (
        params.min_weight - params.max_weight
    )


def abliterate(
    model,
    refusal_directions: mx.array,  # (n_layers+1, hidden) fp32, L2-normalized
    direction_index: float | None,
    params_per_component: Dict[str, AbliterationParameters],
):
    """Apply abliteration to all target modules. Mutates model in place."""
    n_layers = len(model.language_model.model.layers)

    if direction_index is None:
        global_direction = None
    else:
        # Interpolate between two adjacent layer directions, shifted by +1
        # (refusal_directions[0] is embedding-level).
        import math

        weight_frac, idx_f = math.modf(direction_index + 1)
        idx = int(idx_f)
        idx = max(0, min(n_layers - 1, idx))
        d0 = refusal_directions[idx]
        d1 = refusal_directions[min(idx + 1, n_layers)]
        d = (1 - weight_frac) * d0 + weight_frac * d1
        d = d / (mx.linalg.norm(d) + 1e-12)
        global_direction = d

    for layer_idx, comp, mod in get_target_modules(model):
        params = params_per_component[comp]
        alpha = _alpha_for_layer(layer_idx, params)
        if alpha == 0.0:
            continue

        if global_direction is None:
            v = refusal_directions[layer_idx + 1]  # +1 shift
        else:
            v = global_direction

        v = v.astype(mod.weight.dtype)  # cast to bf16 to match weight
        W = mod.weight  # (out=hidden, in)
        # v @ W: (in,)
        vW = v @ W  # uses broadcasting: (hidden,) @ (hidden, in) -> (in,)
        update = alpha * mx.outer(v, vW)  # (hidden, in)
        mod.weight = W - update


def compute_refusal_directions(
    good_residuals_mean: mx.array,  # (n_layers+1, hidden), fp32
    bad_residuals_mean: mx.array,  # same
    orthogonalize: bool = True,
) -> mx.array:
    """Compute refusal direction per layer.

    Returns: (n_layers+1, hidden) fp32, L2-normalized rows.
    """
    d = bad_residuals_mean - good_residuals_mean  # (L, H)
    d_norm = mx.linalg.norm(d, axis=-1, keepdims=True) + 1e-12
    d = d / d_norm

    if orthogonalize:
        g = good_residuals_mean
        g_norm = mx.linalg.norm(g, axis=-1, keepdims=True) + 1e-12
        g_unit = g / g_norm
        proj = mx.sum(d * g_unit, axis=-1, keepdims=True)
        d = d - proj * g_unit
        d_norm = mx.linalg.norm(d, axis=-1, keepdims=True) + 1e-12
        d = d / d_norm

    return d
