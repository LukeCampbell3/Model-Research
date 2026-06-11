"""RuntimeCoder-Micro model configuration and builder.

A scaled-up version of TinyRuntimeCoder for Phase 1 pretraining experiments.
Target: ~30-50M parameters with d_model=256, n_layers=6, n_heads=8.
"""

import dataclasses
from typing import Optional

import torch
import torch.nn as nn

from runtime_coder.model.config import TinyRuntimeCoderConfig
from runtime_coder.model.tiny_runtime_coder import TinyRuntimeCoder


@dataclasses.dataclass
class RuntimeCoderMicroConfig:
    """Configuration for RuntimeCoder-Micro (~30-50M params).

    This scales up TinyRuntimeCoder to a size suitable for
    pretraining experiments on code corpora.

    vocab_size is set to 50176 to accommodate both the base vocabulary
    (32K code tokens) and the reserved special token IDs (50000-50074).
    """

    vocab_size: int = 50176  # Must be > 50074 to hold special tokens
    d_model: int = 256
    n_layers: int = 6
    n_heads: int = 8
    max_seq_len: int = 2048
    d_ff: int = 1024
    dropout: float = 0.1
    pad_token_id: int = 0
    special_token_offset: int = 50000

    def to_tiny_config(self) -> TinyRuntimeCoderConfig:
        """Convert to TinyRuntimeCoderConfig for model construction."""
        config = TinyRuntimeCoderConfig(
            vocab_size=self.vocab_size,
            hidden_dim=self.d_model,
            num_heads=self.n_heads,
            num_layers=self.n_layers,
            max_seq_len=self.max_seq_len,
            dropout=self.dropout,
            pad_token_id=self.pad_token_id,
            special_token_offset=self.special_token_offset,
        )
        # Override ff_dim (default is 4*hidden_dim, we want explicit d_ff)
        config.ff_dim = self.d_ff
        return config


def build_micro_model(
    config: Optional[RuntimeCoderMicroConfig] = None,
    device: str = "cpu",
) -> TinyRuntimeCoder:
    """Build a RuntimeCoder-Micro model.

    Args:
        config: Model configuration. Uses defaults if None.
        device: Device to place model on ('cpu', 'cuda', etc.)

    Returns:
        TinyRuntimeCoder model at micro scale.
    """
    if config is None:
        config = RuntimeCoderMicroConfig()

    tiny_config = config.to_tiny_config()
    model = TinyRuntimeCoder(tiny_config)
    model = model.to(device)

    return model


def count_parameters(model: nn.Module) -> dict:
    """Count and categorize model parameters.

    Returns:
        Dictionary with parameter counts by component.
    """
    total = sum(p.numel() for p in model.parameters())
    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)

    # Break down by component
    breakdown = {}
    for name, param in model.named_parameters():
        component = name.split(".")[0]
        if component not in breakdown:
            breakdown[component] = 0
        breakdown[component] += param.numel()

    return {
        "total": total,
        "trainable": trainable,
        "breakdown": breakdown,
    }
