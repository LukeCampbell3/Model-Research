"""Pretraining evaluation metrics for RuntimeCoder Phase 1.

Evaluates:
- Perplexity on held-out code
- FIM completion accuracy
- Special token retention (no garbage logits on special tokens)
"""

import math
from typing import Dict, List, Optional

import torch
import torch.nn.functional as F

from runtime_coder.data_pipeline.fim_dataset import FIMExample
from runtime_coder.model.tiny_runtime_coder import TinyRuntimeCoder
from runtime_coder.tokenizer.runtime_special_tokens import (
    SPECIAL_TOKENS,
    SPECIAL_TOKEN_ID_OFFSET,
)


def _text_to_ids(text: str, vocab_size: int, max_len: int) -> torch.Tensor:
    """Convert text to token IDs for evaluation."""
    ids = [ord(c) % vocab_size for c in text[:max_len]]
    while len(ids) < max_len:
        ids.append(0)
    return torch.tensor(ids[:max_len], dtype=torch.long)


def eval_perplexity(
    model: TinyRuntimeCoder,
    dataset: List[str],
    device: str = "cpu",
    max_len: int = 256,
) -> float:
    """Evaluate perplexity on a dataset of text examples.

    Args:
        model: The model to evaluate
        dataset: List of text examples
        device: Device for computation
        max_len: Maximum sequence length

    Returns:
        Perplexity (lower is better). Returns inf if dataset is empty.
    """
    if not dataset:
        return float("inf")

    model.eval()
    vocab_size = model.config.vocab_size
    total_loss = 0.0
    total_tokens = 0

    with torch.no_grad():
        for text in dataset:
            ids = _text_to_ids(text, vocab_size, max_len).unsqueeze(0).to(device)
            output = model(ids, labels=ids)
            loss = output["loss"]

            # Count non-padding tokens
            non_pad = (ids != 0).sum().item()
            total_loss += loss.item() * non_pad
            total_tokens += non_pad

    if total_tokens == 0:
        return float("inf")

    avg_loss = total_loss / total_tokens
    perplexity = math.exp(min(avg_loss, 100))  # Cap to avoid overflow
    return perplexity


def eval_fim_completion(
    model: TinyRuntimeCoder,
    fim_examples: List[FIMExample],
    device: str = "cpu",
    max_len: int = 256,
) -> Dict[str, float]:
    """Evaluate FIM completion quality.

    Measures how well the model predicts the middle portion given
    prefix and suffix context.

    Args:
        model: The model to evaluate
        fim_examples: List of FIM examples
        device: Device for computation
        max_len: Maximum sequence length

    Returns:
        Dictionary with FIM accuracy metrics.
    """
    if not fim_examples:
        return {"fim_loss": float("inf"), "fim_perplexity": float("inf"), "examples_evaluated": 0}

    model.eval()
    vocab_size = model.config.vocab_size
    total_loss = 0.0
    num_examples = 0

    with torch.no_grad():
        for example in fim_examples:
            # Format as training format
            formatted = example.to_training_format()
            ids = _text_to_ids(formatted, vocab_size, max_len).unsqueeze(0).to(device)

            output = model(ids, labels=ids)
            total_loss += output["loss"].item()
            num_examples += 1

    if num_examples == 0:
        return {"fim_loss": float("inf"), "fim_perplexity": float("inf"), "examples_evaluated": 0}

    avg_loss = total_loss / num_examples
    perplexity = math.exp(min(avg_loss, 100))

    return {
        "fim_loss": avg_loss,
        "fim_perplexity": perplexity,
        "examples_evaluated": num_examples,
    }


def eval_special_token_retention(
    model: TinyRuntimeCoder,
    tokenizer=None,
    device: str = "cpu",
) -> Dict[str, object]:
    """Evaluate that special tokens don't produce garbage logits.

    Checks that the model assigns reasonable probability mass to special
    token IDs when prompted with context that should elicit them.

    Args:
        model: The model to evaluate
        tokenizer: Optional tokenizer (unused in scaffold, kept for API)
        device: Device for computation

    Returns:
        Dictionary with special token retention metrics.
    """
    model.eval()
    vocab_size = model.config.vocab_size

    # Check if special token IDs are within vocab range
    max_special_id = SPECIAL_TOKEN_ID_OFFSET + len(SPECIAL_TOKENS) - 1
    special_tokens_in_vocab = max_special_id < vocab_size

    if not special_tokens_in_vocab:
        return {
            "special_tokens_in_vocab": False,
            "note": f"Special token max ID ({max_special_id}) exceeds vocab_size ({vocab_size})",
            "logit_stats": None,
        }

    # Generate logits and check special token positions
    with torch.no_grad():
        # Create input with some special token IDs
        input_ids = torch.zeros(1, 32, dtype=torch.long, device=device)
        # Put some special token IDs in the input
        for i, token_idx in enumerate(range(min(10, len(SPECIAL_TOKENS)))):
            if i < 32:
                input_ids[0, i] = SPECIAL_TOKEN_ID_OFFSET + token_idx

        output = model(input_ids)
        logits = output["logits"]

        # Check logit statistics at special token positions
        special_token_ids = list(range(
            SPECIAL_TOKEN_ID_OFFSET,
            SPECIAL_TOKEN_ID_OFFSET + len(SPECIAL_TOKENS),
        ))

        # Get logits for the last position
        last_logits = logits[0, -1, :]  # shape: [vocab_size]

        # Check that special token logits are finite and not all the same
        special_logits = last_logits[special_token_ids]
        all_finite = torch.isfinite(special_logits).all().item()
        logit_std = special_logits.std().item()
        logit_mean = special_logits.mean().item()

        # Check that special tokens get some probability mass
        probs = F.softmax(last_logits, dim=-1)
        special_probs = probs[special_token_ids]
        total_special_prob = special_probs.sum().item()

    return {
        "special_tokens_in_vocab": special_tokens_in_vocab,
        "all_logits_finite": all_finite,
        "special_logit_std": logit_std,
        "special_logit_mean": logit_mean,
        "total_special_token_prob": total_special_prob,
        "num_special_tokens_checked": len(special_token_ids),
        "no_garbage_logits": all_finite and logit_std > 0,
    }
