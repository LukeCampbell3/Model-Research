"""PVR-EC MoE FFN: Pack-by-expert batched execution.

Implements:
- Shared base FFN (always runs on all tokens)
- Lightweight expert deltas (specialized per-expert)
- Pack-by-expert execution (no per-token expert calls)
- Scatter-add back to token positions
- Bucketed variable-k via PVR-EC router
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import torch
import torch.nn as nn
import torch.nn.functional as F

from sparse_loop_moe.models.pvr_ec.pvr_ec_router import (
    PVRECRouter, PVRECConfig, RoutingOutput, Difficulty,
)


@dataclass
class PVRECMetrics:
    """Metrics from PVR-EC MoE execution."""
    load_balance_loss: torch.Tensor
    routing_metrics: dict
    # Batching metrics
    avg_tokens_per_active_expert: float = 0.0
    small_expert_batch_count: int = 0
    expert_pack_efficiency: float = 0.0
    packing_overhead_ms: float = 0.0
    scatter_overhead_ms: float = 0.0
    shared_base_ms: float = 0.0
    expert_compute_ms: float = 0.0


class ExpertDelta(nn.Module):
    """Lightweight expert delta module.

    A small FFN that produces a specialized correction to the shared base output.
    Uses smaller hidden dimension than the shared base for efficiency.
    """

    def __init__(self, d_model: int, d_expert: int, dropout: float = 0.1):
        super().__init__()
        self.w1 = nn.Linear(d_model, d_expert)
        self.w2 = nn.Linear(d_expert, d_model)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.w2(self.dropout(F.gelu(self.w1(x))))


class PVRECMoEFFN(nn.Module):
    """PVR-EC Mixture-of-Experts FFN with pack-by-expert execution.

    Architecture:
        output = shared_base(x) + weighted_sum(expert_delta_i(x))

    Execution flow:
    1. Run shared base on all tokens (dense, always active)
    2. Route tokens via PVR-EC router (prototype + bucketed k)
    3. Pack assignments by expert id
    4. Run expert deltas on packed batches (one call per expert, not per token)
    5. Scatter-add weighted deltas back to token positions
    6. Combine shared + sparse
    """

    def __init__(
        self,
        d_model: int,
        d_ff: int,
        num_experts: int = 4,
        d_expert: Optional[int] = None,
        num_prototypes: int = 16,
        max_k: int = 4,
        dropout: float = 0.1,
        load_bias_cap: float = 0.20,
    ):
        super().__init__()
        self.d_model = d_model
        self.num_experts = num_experts
        d_expert = d_expert or d_ff // 2  # Expert deltas are smaller than shared

        # Shared base FFN (always active)
        self.shared_base = nn.Sequential(
            nn.Linear(d_model, d_ff),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(d_ff, d_model),
        )

        # Expert delta modules (lightweight)
        self.expert_deltas = nn.ModuleList([
            ExpertDelta(d_model, d_expert, dropout) for _ in range(num_experts)
        ])

        # PVR-EC Router
        router_config = PVRECConfig(
            d_model=d_model,
            num_experts=num_experts,
            num_prototypes=num_prototypes,
            d_route=min(64, d_model),
            max_k=max_k,
            load_bias_cap=load_bias_cap,
            dropout=dropout,
        )
        self.router = PVRECRouter(router_config)

        # Shared gate (scales shared base contribution)
        self.shared_gate = nn.Linear(d_model, 1)

    def forward(self, x: torch.Tensor, fixed_k: Optional[int] = None) -> tuple[torch.Tensor, dict]:
        """Forward pass with pack-by-expert execution.

        Args:
            x: [batch, seq_len, d_model]
            fixed_k: Override routing width (for ablation)

        Returns:
            output: [batch, seq_len, d_model]
            aux: Dictionary with losses and metrics
        """
        batch_size, seq_len, d_model = x.shape
        device = x.device

        # Flatten tokens
        flat_x = x.view(-1, d_model)  # [N, d_model]
        N = flat_x.shape[0]

        # Step 1: Shared base (always runs, dense)
        shared_out = self.shared_base(flat_x)  # [N, d_model]
        shared_weight = torch.sigmoid(self.shared_gate(flat_x))  # [N, 1]

        # Step 2: Route via PVR-EC
        routing = self.router(flat_x)

        # Step 3-5: Pack-by-expert execution and scatter-add
        sparse_out = self._pack_execute_scatter(
            flat_x, routing, N, device
        )

        # Step 6: Combine shared + sparse
        output = shared_weight * shared_out + sparse_out

        # Unflatten
        output = output.view(batch_size, seq_len, d_model)

        # Aux losses and metrics
        aux = {
            "load_balance_loss": routing.load_balance_loss,
            "routing_entropy": torch.tensor(routing.metrics["routing_entropy"]),
            "expert_utilization": torch.tensor(routing.metrics["expert_utilization"]),
            "dead_expert_count": torch.tensor(float(routing.metrics["dead_expert_count"])),
            "load_imbalance": torch.tensor(routing.metrics["load_imbalance"]),
            "easy_rate": routing.metrics["easy_rate"],
            "normal_rate": routing.metrics["normal_rate"],
            "hard_rate": routing.metrics["hard_rate"],
            "avg_active_experts": routing.metrics["avg_active_experts"],
        }

        return output, aux

    def _pack_execute_scatter(
        self,
        flat_x: torch.Tensor,
        routing: RoutingOutput,
        N: int,
        device: torch.device,
    ) -> torch.Tensor:
        """Pack assignments by expert, execute batched, scatter-add back.

        Tier 1 MVP: one expert call per active expert, not per token.
        Vectorized assignment building, sorted packing.
        """
        sparse_out = torch.zeros(N, self.d_model, device=device)

        # Build all assignments as tensors (vectorized, no Python loops over tokens)
        all_token_ids = [torch.arange(N, device=device)]
        all_expert_ids = [routing.primary_expert_ids]
        all_weights = [routing.primary_weights]

        # Extra assignments (vectorized extraction)
        max_extra = routing.extra_expert_ids.shape[1]
        for slot in range(max_extra):
            valid = routing.extra_expert_ids[:, slot] != -1
            if valid.any():
                all_token_ids.append(valid.nonzero(as_tuple=True)[0])
                all_expert_ids.append(routing.extra_expert_ids[valid, slot])
                all_weights.append(routing.extra_weights[valid, slot])

        # Single concatenation
        token_ids = torch.cat(all_token_ids)
        expert_ids = torch.cat(all_expert_ids)
        weights = torch.cat(all_weights)

        # Sort by expert_id for cache-friendly execution
        sort_idx = expert_ids.argsort()
        token_ids = token_ids[sort_idx]
        expert_ids = expert_ids[sort_idx]
        weights = weights[sort_idx]

        # Find expert boundaries (vectorized, no Python loop for finding masks)
        # Use unique_consecutive for sorted tensor
        unique_experts, counts = expert_ids.unique_consecutive(return_counts=True)

        # Execute per-expert batches
        offset = 0
        for i in range(unique_experts.shape[0]):
            expert_idx = unique_experts[i].item()
            count = counts[i].item()

            expert_token_ids = token_ids[offset:offset + count]
            expert_weights = weights[offset:offset + count]

            # Batched expert call
            expert_input = flat_x[expert_token_ids]
            expert_output = self.expert_deltas[expert_idx](expert_input)

            # Weighted scatter-add
            weighted_output = expert_output * expert_weights.unsqueeze(-1)
            sparse_out.scatter_add_(
                0,
                expert_token_ids.unsqueeze(-1).expand_as(weighted_output),
                weighted_output,
            )
            offset += count

        return sparse_out

    def get_routing_metrics(self) -> dict:
        """Get current routing state metrics."""
        return {
            "load_bias": self.router.load_bias.detach().cpu().tolist(),
            "expert_load_ema": self.router.expert_load_ema.detach().cpu().tolist(),
            "primary_owner_counts": self.router.primary_owner_counts.detach().cpu().tolist(),
            "update_step": self.router.update_step.item(),
        }
