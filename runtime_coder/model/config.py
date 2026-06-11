"""Configuration for the TinyRuntimeCoder model."""

import dataclasses
from typing import Optional


@dataclasses.dataclass
class TinyRuntimeCoderConfig:
    """Configuration for the tiny runtime coder transformer."""

    vocab_size: int = 50256 + 128  # base + special tokens headroom
    hidden_dim: int = 128
    num_heads: int = 4
    num_layers: int = 2
    max_seq_len: int = 512
    dropout: float = 0.1
    head_dim: int = 32  # hidden_dim // num_heads
    ff_dim: int = 512  # 4 * hidden_dim
    pad_token_id: int = 0
    special_token_offset: int = 50000

    def __post_init__(self):
        self.head_dim = self.hidden_dim // self.num_heads
        self.ff_dim = 4 * self.hidden_dim
