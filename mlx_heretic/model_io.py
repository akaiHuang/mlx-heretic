"""MLX-LM model loading + forward-with-hidden-states helper for Qwen3.5."""
from __future__ import annotations

from typing import List, Tuple

import mlx.core as mx
from mlx_lm import load
from mlx_lm.models.base import create_attention_mask, create_ssm_mask


def load_model(path: str):
    """Load Qwen3.5 model via mlx-lm."""
    return load(path)


def forward_with_hidden_states(model, ids: mx.array) -> Tuple[mx.array, List[mx.array]]:
    """Run forward and return (logits, [h_0=embed, h_1=after_layer0, ...]).

    Mirrors Qwen3_5TextModel.__call__ but collects per-layer outputs.

    ids: (B, S) int tokens
    Returns:
        logits: (B, S, vocab)
        hidden_states: list of (B, S, hidden) with length n_layers+1
    """
    tm = model.language_model.model  # Qwen3_5TextModel
    text_model = model.language_model  # TextModel wrapper

    h = tm.embed_tokens(ids)
    hidden_states = [h]

    cache = [None] * len(tm.layers)
    fa_mask = create_attention_mask(h, None)
    ssm_mask = create_ssm_mask(h, None)

    for layer, c in zip(tm.layers, cache):
        mask = ssm_mask if layer.is_linear else fa_mask
        h = layer(h, mask=mask, cache=c)
        hidden_states.append(h)

    h_norm = tm.norm(h)
    if text_model.args.tie_word_embeddings:
        logits = tm.embed_tokens.as_linear(h_norm)
    else:
        logits = text_model.lm_head(h_norm)

    return logits, hidden_states


def get_residuals_last_token(model, ids: mx.array) -> mx.array:
    """Hidden states at the last non-pad position, for each layer.

    Returns: (B, n_layers+1, hidden) in float32.
    """
    _, hs = forward_with_hidden_states(model, ids)
    # Take last token across each layer
    # h shape: (B, S, H). We just take h[:, -1, :] (no padding expected here since
    # we pass each prompt individually, S is its real length).
    stacked = mx.stack([h[:, -1, :] for h in hs], axis=1)  # (B, n_layers+1, H)
    return stacked.astype(mx.float32)


def get_first_token_logprobs(model, ids: mx.array) -> mx.array:
    """Log-softmax over vocab at last input position. Shape (B, vocab)."""
    logits, _ = forward_with_hidden_states(model, ids)
    logits = logits[:, -1, :].astype(mx.float32)
    logprobs = mx.log(mx.softmax(logits, axis=-1) + 1e-30)
    return logprobs
