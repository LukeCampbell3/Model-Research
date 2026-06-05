"""PVR-EC Full Model: integrates with existing experiment/benchmark infrastructure.

This is a decoder-only transformer that uses PVR-EC MoE blocks instead of
the standard MoE FFN. It implements the same interface as SparseLoopMoEModel
and DenseTransformer so it can be used in the benchmark runner.
"""

from __future__ import annotations

from dataclasses import dataclass
import math

import torch
import torch.nn as nn
import torch.nn.functional as F

from sparse_loop_moe.models.pvr_ec.pvr_ec_moe import PVRECMoEFFN


@dataclass
class PVRECModelConfig:
    """Configuration for PVR-EC model variant."""
    vocab_size: int = 256
    d_model: int = 128
    max_seq_len: int = 256
    n_layers: int = 2
    n_heads: int = 4
    d_ff: int = 256
    num_experts: int = 4
    num_prototypes: int = 16
    max_k: int = 4
    d_expert: int = 128  # Expert delta hidden dim (smaller than d_ff)
    dropout: float = 0.1
    tie_weights: bool = True
    load_bias_cap: float = 0.20
    pvr_execution_mode: str = "variable_k_pack_by_expert"
    pvr_expert_type: str = "delta_rank_medium"
    pvr_training_dispatch_mode: str | None = None
    pvr_inference_dispatch_mode: str | None = None
    target_avg_k: float = 2.0
    expert_capacity: int | None = None
    branch_ticket_shadow_mode: bool = True


class PVRECBlock(nn.Module):
    """Single PVR-EC transformer block: attention + PVR-EC MoE."""

    def __init__(self, config: PVRECModelConfig):
        super().__init__()
        self.attn_ln = nn.LayerNorm(config.d_model)
        self.attn = nn.MultiheadAttention(
            config.d_model, config.n_heads, dropout=config.dropout, batch_first=True
        )
        self.attn_dropout = nn.Dropout(config.dropout)

        self.moe_ln = nn.LayerNorm(config.d_model)
        self.moe = PVRECMoEFFN(
            d_model=config.d_model,
            d_ff=config.d_ff,
            num_experts=config.num_experts,
            d_expert=config.d_expert,
            num_prototypes=config.num_prototypes,
            max_k=config.max_k,
            dropout=config.dropout,
            load_bias_cap=config.load_bias_cap,
            execution_mode=config.pvr_execution_mode,
            expert_type=config.pvr_expert_type,
            pvr_training_dispatch_mode=config.pvr_training_dispatch_mode,
            pvr_inference_dispatch_mode=config.pvr_inference_dispatch_mode,
            target_avg_k=config.target_avg_k,
            expert_capacity=config.expert_capacity,
            branch_ticket_shadow_mode=config.branch_ticket_shadow_mode,
        )

    def forward(self, x: torch.Tensor) -> tuple[torch.Tensor, dict]:
        # Self-attention
        attn_in = self.attn_ln(x)
        attn_out, _ = self.attn(attn_in, attn_in, attn_in, need_weights=False)
        x = x + self.attn_dropout(attn_out)

        # PVR-EC MoE FFN
        moe_in = self.moe_ln(x)
        moe_out, aux = self.moe(moe_in)
        x = x + moe_out

        return x, aux


class PVRECModel(nn.Module):
    """Full PVR-EC model for benchmarking.

    Same interface as DenseTransformer and SparseLoopMoEModel:
    forward(input_ids, targets) -> {"logits", "loss", "hidden_states", ...}
    """

    def __init__(self, config: PVRECModelConfig):
        super().__init__()
        self.config = config

        # Embeddings
        self.token_emb = nn.Embedding(config.vocab_size, config.d_model)
        self.pos_emb = nn.Embedding(config.max_seq_len, config.d_model)
        self.dropout = nn.Dropout(config.dropout)

        # PVR-EC blocks
        self.blocks = nn.ModuleList([
            PVRECBlock(config) for _ in range(config.n_layers)
        ])

        # Output
        self.ln_f = nn.LayerNorm(config.d_model)
        self.head = nn.Linear(config.d_model, config.vocab_size, bias=False)

        if config.tie_weights:
            self.head.weight = self.token_emb.weight

        self._init_weights()

    def _init_weights(self):
        for module in self.modules():
            if isinstance(module, nn.Linear):
                nn.init.normal_(module.weight, mean=0.0, std=0.02)
                if module.bias is not None:
                    nn.init.zeros_(module.bias)
            elif isinstance(module, nn.Embedding):
                nn.init.normal_(module.weight, mean=0.0, std=0.02)

    def forward(
        self,
        input_ids: torch.Tensor,
        targets: torch.Tensor = None,
    ) -> dict:
        """Forward pass compatible with benchmark infrastructure.

        Args:
            input_ids: [batch, seq_len]
            targets: [batch, seq_len] optional

        Returns:
            dict with logits, loss, hidden_states, loop_stats, aux_losses
        """
        batch_size, seq_len = input_ids.shape
        device = input_ids.device

        positions = torch.arange(seq_len, device=device).unsqueeze(0)
        x = self.dropout(self.token_emb(input_ids) + self.pos_emb(positions))

        all_aux = []
        for block in self.blocks:
            x, aux = block(x)
            all_aux.append(aux)

        x = self.ln_f(x)
        logits = self.head(x)

        result = {
            "logits": logits,
            "hidden_states": x,
            "loop_stats": [],  # No loops in PVR-EC base (compatible interface)
            "aux_losses": {},
        }

        # Aggregate aux losses
        if all_aux:
            lb_losses = [a["load_balance_loss"] for a in all_aux if "load_balance_loss" in a]
            if lb_losses:
                result["aux_losses"]["load_balance_loss"] = torch.stack(lb_losses).mean()

        # Task loss
        if targets is not None:
            loss = F.cross_entropy(
                logits.view(-1, self.config.vocab_size), targets.view(-1)
            )
            result["loss"] = loss

        return result

    def count_parameters(self) -> int:
        return sum(p.numel() for p in self.parameters() if p.requires_grad)
