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
import time
from typing import Optional

import torch
import torch.nn as nn
import torch.nn.functional as F

from sparse_loop_moe.models.pvr_ec.diagnostics import (
    DEPLOY_MODES,
    EXECUTION_MODES,
    ExpertDeltaScaleSchedule,
    EXPERT_TYPES,
    MergeabilityState,
    choose_merge_type,
    make_branch_ticket,
    normalized_entropy,
    post_expert_mergeability,
    pre_expert_mergeability,
    weighted_hidden_merge,
)
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
    forward_total_ms: float = 0.0
    forward_router_score_ms: float = 0.0
    forward_prototype_shortlist_ms: float = 0.0
    forward_assignment_build_ms: float = 0.0
    forward_pack_ms: float = 0.0
    forward_expert_compute_ms: float = 0.0
    forward_scatter_ms: float = 0.0
    backward_total_ms: float = 0.0
    backward_dispatch_related_ms: float = 0.0
    backward_pack_related_ms: float = 0.0
    backward_scatter_related_ms: float = 0.0
    expert_backward_time_ms: float = 0.0
    optimizer_time_ms: float = 0.0


class LowRankExpertDelta(nn.Module):
    """Low-rank residual expert delta."""

    def __init__(self, d_model: int, d_expert: int, dropout: float = 0.1):
        super().__init__()
        self.expert_architecture_id = f"delta_rank_{d_expert}"
        self.expert_inner_dim = d_expert
        self.delta_rank = d_expert
        self.w1 = nn.Linear(d_model, d_expert)
        self.w2 = nn.Linear(d_expert, d_model)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return x + self.w2(self.dropout(F.gelu(self.w1(x))))


class MicroFFNExpertDelta(nn.Module):
    """Residual micro-FFN expert delta."""

    def __init__(self, d_model: int, d_expert: int, dropout: float = 0.1):
        super().__init__()
        self.expert_architecture_id = f"micro_ffn_{d_expert}"
        self.expert_inner_dim = d_expert
        self.delta_rank = 0
        self.w1 = nn.Linear(d_model, d_expert)
        self.w2 = nn.Linear(d_expert, d_model)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return x + self.w2(self.dropout(F.gelu(self.w1(x))))


class FullExpertFFN(nn.Module):
    """Full non-residual FFN expert control comparable to fixed MoE experts."""

    def __init__(self, d_model: int, d_expert: int, dropout: float = 0.1):
        super().__init__()
        self.expert_architecture_id = "full_expert_ffn"
        self.expert_inner_dim = d_expert
        self.delta_rank = 0
        self.w1 = nn.Linear(d_model, d_expert)
        self.w2 = nn.Linear(d_expert, d_model)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.w2(self.dropout(F.gelu(self.w1(x))))


ExpertDelta = MicroFFNExpertDelta


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
        execution_mode: str = "variable_k_pack_by_expert",
        expert_type: str = "delta_rank_medium",
        pvr_training_dispatch_mode: Optional[str] = None,
        pvr_inference_dispatch_mode: Optional[str] = None,
        target_avg_k: float = 2.0,
        expert_capacity: Optional[int] = None,
        branch_ticket_shadow_mode: bool = True,
        emit_branch_tickets_during_training: bool = False,
        max_shadow_branch_tickets: int = 64,
        pvr_deploy_mode: str = "off",
        pvr_aux_alpha: float = 0.5,
        pvr_shared_scale: float = 1.0,
        pvr_expert_delta_scale: float = 1.0,
        pvr_expert_delta_scale_schedule: str = "constant",
        pvr_expert_delta_scale_start: Optional[float] = None,
        pvr_expert_delta_scale_end: Optional[float] = None,
        pvr_expert_delta_scale_warmup_steps: int = 0,
        pvr_expert_delta_scale_hold_steps: int = 0,
        pvr_expert_delta_scale_decay: Optional[float] = None,
        pvr_debug_force_expert_id: Optional[int] = None,
        pvr_debug_owner_mode: str = "",
        profile: bool = False,
        collect_debug: bool = False,
        emit_branch_tickets: bool = False,
        mergeability_mode: str = "disabled",
        runtime_branching: bool = False,
    ):
        super().__init__()
        if execution_mode not in EXECUTION_MODES:
            raise ValueError(f"Unknown PVR-EC execution mode: {execution_mode}")
        if expert_type not in EXPERT_TYPES:
            raise ValueError(f"Unknown PVR-EC expert type: {expert_type}")
        if pvr_deploy_mode not in DEPLOY_MODES:
            raise ValueError(f"Unknown PVR-EC deploy mode: {pvr_deploy_mode}")
        self.d_model = d_model
        self.num_experts = num_experts
        self.execution_mode = execution_mode
        self.expert_type = expert_type
        self.pvr_deploy_mode = pvr_deploy_mode
        self.pvr_aux_alpha = pvr_aux_alpha
        self.pvr_shared_scale = float(pvr_shared_scale)
        self.pvr_expert_delta_scale = float(pvr_expert_delta_scale)
        schedule_start = self.pvr_expert_delta_scale if pvr_expert_delta_scale_start is None else float(pvr_expert_delta_scale_start)
        schedule_end = self.pvr_expert_delta_scale if pvr_expert_delta_scale_end is None else float(pvr_expert_delta_scale_end)
        self.pvr_expert_delta_scale_schedule = ExpertDeltaScaleSchedule(
            schedule=pvr_expert_delta_scale_schedule,
            start=schedule_start,
            end=schedule_end,
            warmup_steps=pvr_expert_delta_scale_warmup_steps,
            hold_steps=pvr_expert_delta_scale_hold_steps,
            decay=pvr_expert_delta_scale_decay,
        )
        self.pvr_expert_delta_scale_t = self.pvr_expert_delta_scale_schedule.value(0)
        self.pvr_debug_force_expert_id = pvr_debug_force_expert_id
        self.pvr_debug_owner_mode = pvr_debug_owner_mode
        self.profile = profile
        self.collect_debug = collect_debug
        self.emit_branch_tickets = emit_branch_tickets
        self.mergeability_mode = mergeability_mode
        self.runtime_branching = runtime_branching
        self.pvr_training_dispatch_mode = pvr_training_dispatch_mode
        self.pvr_inference_dispatch_mode = pvr_inference_dispatch_mode
        self.branch_ticket_shadow_mode = branch_ticket_shadow_mode
        self.emit_branch_tickets_during_training = emit_branch_tickets_during_training
        self.max_shadow_branch_tickets = max_shadow_branch_tickets
        self.mergeability_state = MergeabilityState()
        d_expert = self._resolve_expert_inner_dim(d_model, d_ff, expert_type, d_expert)
        self.d_expert = d_expert
        self.expert_architecture_id = self._architecture_id_for_type(expert_type, d_expert)

        # Shared base FFN (always active)
        self.shared_base = nn.Sequential(
            nn.Linear(d_model, d_ff),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(d_ff, d_model),
        )

        expert_cls = self._expert_class_for_type(expert_type)
        self.expert_deltas = nn.ModuleList([
            expert_cls(d_model, d_expert, dropout) for _ in range(num_experts)
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
            routing_mode=execution_mode,
            target_avg_k=target_avg_k,
            expert_capacity=expert_capacity,
            branch_ticket_shadow_mode=branch_ticket_shadow_mode,
        )
        self.router = PVRECRouter(router_config)

        # Shared gate (scales shared base contribution)
        self.shared_gate = nn.Linear(d_model, 1)

    def set_training_step(self, step: int) -> float:
        """Update the active expert delta scale for the current training step."""

        self.pvr_expert_delta_scale_t = self.pvr_expert_delta_scale_schedule.value(step)
        self.pvr_expert_delta_scale = float(self.pvr_expert_delta_scale_t)
        return self.pvr_expert_delta_scale_t

    def get_expert_delta_scale(self) -> float:
        return float(self.pvr_expert_delta_scale_t)

    @staticmethod
    def _resolve_expert_inner_dim(
        d_model: int,
        d_ff: int,
        expert_type: str,
        requested: Optional[int],
    ) -> int:
        if requested is not None:
            return max(1, int(requested))
        rank_map = {
            "delta_rank_8": 8,
            "delta_rank_16": 16,
            "delta_rank_32": 32,
            "delta_rank_64": 64,
            "delta_rank_128": 128,
            "delta_rank_small": max(1, d_model // 4),
            "delta_rank_medium": max(1, d_model // 2),
            "delta_rank_large": d_model,
            "delta_small": max(1, d_model // 4),
            "delta_medium": max(1, d_model // 2),
            "delta_large": d_model,
        }
        if expert_type in rank_map:
            return rank_map[expert_type]
        if expert_type == "micro_ffn_0_25x":
            return max(1, int(round(d_ff * 0.25)))
        if expert_type == "micro_ffn_0_5x":
            return max(1, int(round(d_ff * 0.5)))
        if expert_type in {"micro_ffn_1_0x", "full_expert_ffn", "full_expert_ffn_control"}:
            return d_ff
        return max(1, d_model // 2)

    @staticmethod
    def _expert_class_for_type(expert_type: str) -> type[nn.Module]:
        if expert_type in {"full_expert_ffn", "full_expert_ffn_control"}:
            return FullExpertFFN
        if expert_type.startswith("micro_ffn_"):
            return MicroFFNExpertDelta
        return LowRankExpertDelta

    @staticmethod
    def _architecture_id_for_type(expert_type: str, d_expert: int) -> str:
        if expert_type in {"full_expert_ffn", "full_expert_ffn_control"}:
            return "full_expert_ffn"
        if expert_type.startswith("micro_ffn_"):
            return expert_type
        return f"delta_rank_{d_expert}"

    def forward(
        self,
        x: torch.Tensor,
        fixed_k: Optional[int] = None,
        execution_mode: Optional[str] = None,
    ) -> tuple[torch.Tensor, dict]:
        """Forward pass with pack-by-expert execution.

        Args:
            x: [batch, seq_len, d_model]
            fixed_k: Override routing width (for ablation)

        Returns:
            output: [batch, seq_len, d_model]
            aux: Dictionary with losses and metrics
        """
        if self.pvr_deploy_mode != "off":
            return self._deploy_forward(x)

        batch_size, seq_len, d_model = x.shape
        device = x.device
        forward_start = self._now_ms(device)
        timing = self._empty_timing()
        mode = self._resolve_execution_mode(execution_mode, fixed_k)

        # Flatten tokens
        flat_x = x.view(-1, d_model)  # [N, d_model]
        N = flat_x.shape[0]

        # Step 1: Shared base (always runs, dense)
        t0 = self._now_ms(device)
        shared_out = self.shared_base(flat_x)  # [N, d_model]
        shared_weight = torch.sigmoid(self.shared_gate(flat_x))  # [N, 1]
        timing["shared_base_ms"] = self._elapsed_ms(t0, device)

        if self.expert_type == "shared_base_only":
            sparse_out = torch.zeros_like(shared_out)
            routing = self.router(flat_x, routing_mode="fixed_top2_pack_by_expert")
            expert_outputs_for_merge = None
        else:
            # Step 2: Route via PVR-EC
            t0 = self._now_ms(device)
            routing_mode = self._routing_mode_for_execution(mode)
            routing = self.router(flat_x, routing_mode=routing_mode)
            timing["forward_router_score_ms"] = self._elapsed_ms(t0, device)

            if mode in {"dense_all_experts", "fixed_top2_all_experts_masked"}:
                sparse_out, dense_metrics, expert_outputs_for_merge = self._dense_all_experts_execute(
                    flat_x, routing, mode, device
                )
                timing.update(dense_metrics)
            else:
                sparse_out, sparse_metrics = self._pack_execute_scatter(flat_x, routing, N, device)
                timing.update(sparse_metrics)
                expert_outputs_for_merge = None

        # Step 6: Combine shared + sparse
        scaled_shared_out = self.pvr_shared_scale * shared_weight * shared_out
        scale_t = self.get_expert_delta_scale()
        scaled_sparse_out = scale_t * sparse_out
        output = scaled_shared_out + scaled_sparse_out
        shared_norm = scaled_shared_out.detach().float().norm(dim=-1).mean()
        sparse_norm = scaled_sparse_out.detach().float().norm(dim=-1).mean()

        # Unflatten
        output = output.view(batch_size, seq_len, d_model)
        shared_hidden = scaled_shared_out.view(batch_size, seq_len, d_model)
        sparse_delta = scaled_sparse_out.view(batch_size, seq_len, d_model)
        timing["forward_total_ms"] = self._elapsed_ms(forward_start, device)
        timing.update(self._derived_timing(timing, N))
        mergeability, branch_tickets = self._shadow_mergeability_and_tickets(
            routing=routing,
            expert_outputs=expert_outputs_for_merge,
            timing=timing,
        )

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
            "pvr_execution_mode": mode,
            "pvr_expert_type": self.expert_type,
            "expert_architecture_id": self.expert_architecture_id,
            "expert_inner_dim": self.d_expert,
            "routing_metrics": routing.metrics,
            "contribution_metrics": {
                "shared_output_norm": shared_norm,
                "sparse_output_norm": sparse_norm,
                "shared_sparse_ratio": shared_norm / (sparse_norm + 1e-8),
                "pvr_shared_scale": float(self.pvr_shared_scale),
                "pvr_expert_delta_scale": float(scale_t),
                "pvr_expert_delta_scale_t": float(scale_t),
                "pvr_expert_delta_scale_schedule": self.pvr_expert_delta_scale_schedule.schedule,
            },
            "shared_hidden": shared_hidden,
            "sparse_delta": sparse_delta,
            "combined_hidden": output,
            "timing": timing,
            "mergeability": mergeability,
            "branch_tickets": branch_tickets,
            "statuses": [
                "PVR_EC_SOFT_SPECULATION_ONLY",
                "PVR_EC_BRANCH_TICKETS_SHADOW_ONLY",
                "PVR_EC_RUNTIME_BRANCHING_DISABLED",
                "PVR_EC_FORMULAIC_MERGEABILITY_ENABLED",
                "PVR_EC_MERGEABILITY_FORMULA_SHADOW_MODE",
            ],
        }

        return output, aux

    def _deploy_forward(self, x: torch.Tensor) -> tuple[torch.Tensor, dict]:
        """Low-overhead deployment forward path.

        This path avoids branch tickets, mergeability objects, JSON/report
        construction, CUDA sync, and per-token Python work.
        """

        batch_size, seq_len, d_model = x.shape
        flat_x = x.reshape(-1, d_model)
        shared_out = self.shared_base(flat_x)

        mode = self.pvr_deploy_mode
        if mode == "top1":
            top_ids, top_weights = self._debug_or_router_top1(flat_x)
            expert_out = self._vectorized_expert_deltas(flat_x, top_ids)
            sparse_out = top_weights[:, :1].unsqueeze(-1).mul(expert_out).sum(dim=1)
            actual_k = 1.0
            actual_expert_slots = 1.0
            dense_all_experts_executed = False
        elif mode == "top2":
            top_ids, top_weights, _ = self.router.deploy_topk(flat_x, k=2)
            expert_out = self._vectorized_expert_deltas(flat_x, top_ids)
            primary = top_weights[:, :1].unsqueeze(-1) * expert_out[:, :1]
            aux = self.pvr_aux_alpha * top_weights[:, 1:2].unsqueeze(-1) * expert_out[:, 1:2]
            sparse_out = (primary + aux).sum(dim=1)
            actual_k = 2.0
            actual_expert_slots = 2.0
            dense_all_experts_executed = False
        elif mode == "bucketed":
            top_ids, top_weights, entropy = self.router.deploy_topk(flat_x, k=4)
            k4 = entropy > 0.70
            k2 = (entropy > 0.40) & ~k4
            rank = torch.arange(top_ids.shape[1], device=top_ids.device).unsqueeze(0)
            keep_k = torch.ones_like(entropy, dtype=torch.long)
            keep_k = torch.where(k2, torch.full_like(keep_k, 2), keep_k)
            keep_k = torch.where(k4, torch.full_like(keep_k, 4), keep_k)
            keep = rank < keep_k.unsqueeze(1)
            expert_out = self._vectorized_expert_deltas(flat_x, top_ids)
            weights = top_weights * keep.to(top_weights.dtype)
            sparse_out = (weights.unsqueeze(-1) * expert_out).sum(dim=1)
            actual_k = keep.to(top_weights.dtype).sum(dim=-1).float().mean()
            actual_expert_slots = 4.0
            dense_all_experts_executed = False
        elif mode == "dense_masked_control":
            top_ids, top_weights, _ = self.router.deploy_topk(flat_x, k=2)
            all_ids = torch.arange(self.num_experts, device=flat_x.device).unsqueeze(0).expand(flat_x.shape[0], -1)
            expert_out = self._vectorized_expert_deltas(flat_x, all_ids)
            weights = torch.zeros(flat_x.shape[0], self.num_experts, device=flat_x.device, dtype=flat_x.dtype)
            weights.scatter_(1, top_ids, top_weights)
            sparse_out = (weights.unsqueeze(-1) * expert_out).sum(dim=1)
            actual_k = 2.0
            actual_expert_slots = float(self.num_experts)
            dense_all_experts_executed = True
        else:
            raise ValueError(f"Unsupported deploy mode: {mode}")

        scaled_shared_out = self.pvr_shared_scale * shared_out
        scale_t = self.get_expert_delta_scale()
        scaled_sparse_out = scale_t * sparse_out
        output = (scaled_shared_out + scaled_sparse_out).view(batch_size, seq_len, d_model)
        shared_hidden = scaled_shared_out.view(batch_size, seq_len, d_model)
        sparse_delta = scaled_sparse_out.view(batch_size, seq_len, d_model)
        shared_norm = scaled_shared_out.detach().float().norm(dim=-1).mean()
        sparse_norm = scaled_sparse_out.detach().float().norm(dim=-1).mean()
        avg_k_tensor = torch.as_tensor(actual_k, device=x.device, dtype=x.dtype)
        expert_slots_tensor = torch.as_tensor(actual_expert_slots, device=x.device, dtype=x.dtype)
        # Expose primary expert ids for diagnostics (detached, no grad cost)
        primary_expert_ids_diag = top_ids[:, 0].detach() if top_ids.dim() == 2 else top_ids.detach()
        status = "PVR_EC_DEPLOY_TOP2_IMPLEMENTED"
        if mode == "top1":
            status = "PVR_EC_DEPLOY_TOP1_IMPLEMENTED"
        elif mode == "bucketed":
            status = "PVR_EC_DEPLOY_BUCKETED_IMPLEMENTED"
        aux = {
            "load_balance_loss": torch.zeros((), device=x.device, dtype=x.dtype),
            "pvr_execution_mode": f"pvr_ec_deploy_{mode}",
            "pvr_expert_type": self.expert_type,
            "expert_architecture_id": self.expert_architecture_id,
            "expert_inner_dim": self.d_expert,
            "deploy_mode": mode,
            "expert_execution_mode": "FULLY_VECTORIZED",
            "branch_tickets": [],
            "branch_tickets_enabled": False,
            "runtime_branching_enabled": False,
            "mergeability_mode": self.mergeability_mode,
            "primary_expert_ids": primary_expert_ids_diag,
            "routing_metrics": {
                "actual_avg_k": avg_k_tensor,
                "actual_owner_count_per_token": avg_k_tensor,
                "actual_experts_executed": expert_slots_tensor,
                "actual_expert_slots_per_token": expert_slots_tensor,
                "dense_all_experts_executed": dense_all_experts_executed,
                "oracle_owner_used": False,
                "forced_action_path_used": False,
                "replay_probe_labels_used": False,
                "target_avg_K": avg_k_tensor,
                "assignment_budget_drift": 0.0,
                "expert_utilization": 1.0,
                "load_imbalance": 0.0,
                "routing_entropy": 0.0,
                "num_k1_tokens": 0.0,
                "num_k2_tokens": 0.0,
                "num_k4_tokens": 0.0,
                "assignment_budget_status": "deploy",
            },
            "contribution_metrics": {
                "shared_output_norm": shared_norm,
                "sparse_output_norm": sparse_norm,
                "shared_sparse_ratio": shared_norm / (sparse_norm + 1e-8),
                "pvr_shared_scale": float(self.pvr_shared_scale),
                "pvr_expert_delta_scale": float(scale_t),
                "pvr_expert_delta_scale_t": float(scale_t),
                "pvr_expert_delta_scale_schedule": self.pvr_expert_delta_scale_schedule.schedule,
            },
            "shared_hidden": shared_hidden,
            "sparse_delta": sparse_delta,
            "combined_hidden": output,
            "timing": self._empty_timing(),
            "mergeability": {
                "mergeability_score_mean": 0.0,
                "mergeability_score_std": 0.0,
                "expert_disagreement_mean": 0.0,
            },
            "statuses": [
                status,
                "PVR_EC_RUNTIME_BRANCHING_DISABLED",
            ],
        }
        return output, aux

    def _debug_or_router_top1(self, flat_x: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
        if self.pvr_debug_force_expert_id is not None:
            expert_id = int(self.pvr_debug_force_expert_id) % max(self.num_experts, 1)
            ids = torch.full((flat_x.shape[0], 1), expert_id, device=flat_x.device, dtype=torch.long)
            weights = torch.ones(flat_x.shape[0], 1, device=flat_x.device, dtype=flat_x.dtype)
            return ids, weights
        if self.pvr_debug_owner_mode in {"round_robin", "uniform"}:
            ids = (torch.arange(flat_x.shape[0], device=flat_x.device) % self.num_experts).view(-1, 1)
            weights = torch.ones(flat_x.shape[0], 1, device=flat_x.device, dtype=flat_x.dtype)
            return ids, weights
        top_ids, top_weights, _ = self.router.deploy_topk(flat_x, k=1)
        return top_ids, top_weights

    def _stacked_expert_weights(self) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
        w1 = torch.stack([expert.w1.weight.transpose(0, 1) for expert in self.expert_deltas], dim=0)
        b1 = torch.stack([expert.w1.bias for expert in self.expert_deltas], dim=0)
        w2 = torch.stack([expert.w2.weight.transpose(0, 1) for expert in self.expert_deltas], dim=0)
        b2 = torch.stack([expert.w2.bias for expert in self.expert_deltas], dim=0)
        return w1, b1, w2, b2

    def _vectorized_expert_deltas(self, flat_x: torch.Tensor, expert_ids: torch.Tensor) -> torch.Tensor:
        w1, b1, w2, b2 = self._stacked_expert_weights()
        selected_w1 = w1[expert_ids]
        selected_b1 = b1[expert_ids]
        selected_w2 = w2[expert_ids]
        selected_b2 = b2[expert_ids]
        hidden = torch.einsum("nh,nkhr->nkr", flat_x, selected_w1) + selected_b1
        hidden = F.gelu(hidden)
        out = torch.einsum("nkr,nkrh->nkh", hidden, selected_w2) + selected_b2
        if self.expert_architecture_id != "full_expert_ffn":
            out = flat_x.unsqueeze(1) + out
        return out

    def _resolve_execution_mode(self, requested: Optional[str], fixed_k: Optional[int]) -> str:
        if requested:
            mode = requested
        elif self.training and self.pvr_training_dispatch_mode == "dense":
            mode = "dense_all_experts"
        elif (not self.training) and self.pvr_inference_dispatch_mode == "sparse":
            mode = "variable_k_pack_by_expert"
        else:
            mode = self.execution_mode
        if fixed_k == 2 and mode == "variable_k_pack_by_expert":
            mode = "fixed_top2_pack_by_expert"
        if mode not in EXECUTION_MODES:
            raise ValueError(f"Unknown PVR-EC execution mode: {mode}")
        return mode

    def _routing_mode_for_execution(self, mode: str) -> str:
        if mode == "dense_all_experts":
            return "variable_k_pack_by_expert"
        return mode

    @staticmethod
    def _now_ms(device: torch.device) -> float:
        # Synchronizing CUDA at every instrumentation boundary is far more
        # expensive than the tiny experts in this prototype. These timings are
        # diagnostic estimates; full synchronized profiling belongs in a
        # dedicated profiler run, not the training hot path.
        return time.perf_counter() * 1000.0

    def _elapsed_ms(self, start_ms: float, device: torch.device) -> float:
        return self._now_ms(device) - start_ms

    @staticmethod
    def _empty_timing() -> dict:
        return {
            "total_step_time_ms": 0.0,
            "router_score_time_ms": 0.0,
            "prototype_shortlist_time_ms": 0.0,
            "bitset_mask_time_ms": 0.0,
            "assignment_build_time_ms": 0.0,
            "pack_time_ms": 0.0,
            "expert_compute_time_ms": 0.0,
            "small_expert_execution_time_ms": 0.0,
            "scatter_time_ms": 0.0,
            "loss_compute_time_ms": 0.0,
            "backward_time_ms": 0.0,
            "optimizer_time_ms": 0.0,
            "tokens_per_second": 0.0,
            "quality_per_ms": 0.0,
            "quality_per_param": 0.0,
            "quality_per_active_param": 0.0,
            "expert_utilization": 0.0,
            "avg_tokens_per_active_expert": 0.0,
            "small_expert_batch_rate": 0.0,
            "avg_k": 0.0,
            "route_entropy": 0.0,
            "expert_load_cv": 0.0,
            "dispatch_overhead_ratio": 0.0,
            "compute_to_dispatch_ratio": 0.0,
            "forward_total_ms": 0.0,
            "forward_router_score_ms": 0.0,
            "forward_prototype_shortlist_ms": 0.0,
            "forward_assignment_build_ms": 0.0,
            "forward_pack_ms": 0.0,
            "forward_expert_compute_ms": 0.0,
            "forward_scatter_ms": 0.0,
            "backward_total_ms": 0.0,
            "backward_dispatch_related_ms": 0.0,
            "backward_pack_related_ms": 0.0,
            "backward_scatter_related_ms": 0.0,
            "expert_backward_time_ms": 0.0,
            "training_compute_to_dispatch_ratio": 0.0,
        }

    @staticmethod
    def _derived_timing(timing: dict, token_count: int) -> dict:
        total = max(timing["forward_total_ms"], 1e-8)
        dispatch = (
            timing["forward_router_score_ms"]
            + timing["forward_assignment_build_ms"]
            + timing["forward_pack_ms"]
            + timing["forward_scatter_ms"]
        )
        sparse_dispatch = (
            timing["forward_assignment_build_ms"]
            + timing["forward_pack_ms"]
            + timing["forward_scatter_ms"]
        )
        compute = timing["forward_expert_compute_ms"]
        backward_total = max(timing["backward_total_ms"], 1e-8)
        backward_dispatch = (
            timing["backward_dispatch_related_ms"]
            + timing["backward_pack_related_ms"]
            + timing["backward_scatter_related_ms"]
        )
        return {
            "total_step_time_ms": timing["forward_total_ms"],
            "router_score_time_ms": timing["forward_router_score_ms"],
            "assignment_build_time_ms": timing["forward_assignment_build_ms"],
            "pack_time_ms": timing["forward_pack_ms"],
            "expert_compute_time_ms": timing["forward_expert_compute_ms"],
            "small_expert_execution_time_ms": timing["forward_expert_compute_ms"],
            "scatter_time_ms": timing["forward_scatter_ms"],
            "tokens_per_second": 1000.0 * token_count / total,
            "dispatch_overhead_ratio": dispatch / total,
            "compute_to_dispatch_ratio": compute / max(sparse_dispatch, 1e-8),
            "forward_dispatch_overhead_ratio": dispatch / total,
            "backward_dispatch_overhead_ratio": backward_dispatch / backward_total,
            "training_compute_to_dispatch_ratio": (
                (compute + timing["expert_backward_time_ms"])
                / max(sparse_dispatch + backward_dispatch, 1e-8)
            ),
        }

    def _dense_all_experts_execute(
        self,
        flat_x: torch.Tensor,
        routing: RoutingOutput,
        mode: str,
        device: torch.device,
    ) -> tuple[torch.Tensor, dict, torch.Tensor]:
        t0 = self._now_ms(device)
        expert_outputs = torch.stack([expert(flat_x) for expert in self.expert_deltas], dim=1)
        expert_compute_ms = self._elapsed_ms(t0, device)

        probs = routing.all_probs
        if mode == "fixed_top2_all_experts_masked":
            top2 = probs.topk(min(2, probs.shape[-1]), dim=-1).indices
            weights = torch.zeros_like(probs)
            weights.scatter_(1, top2, probs.gather(1, top2))
        else:
            weights = probs
        sparse_out = weighted_hidden_merge(expert_outputs, weights)
        return sparse_out, {
            "forward_assignment_build_ms": 0.0,
            "forward_pack_ms": 0.0,
            "forward_expert_compute_ms": expert_compute_ms,
            "forward_scatter_ms": 0.0,
            "avg_tokens_per_active_expert": float(flat_x.shape[0]),
            "small_expert_batch_rate": 0.0,
        }, expert_outputs

    def _pack_execute_scatter(
        self,
        flat_x: torch.Tensor,
        routing: RoutingOutput,
        N: int,
        device: torch.device,
    ) -> tuple[torch.Tensor, dict]:
        """Pack assignments by expert, execute batched, scatter-add back.

        Tier 1 MVP: one expert call per active expert, not per token.
        Vectorized assignment building, sorted packing.
        """
        sparse_out = torch.zeros(N, self.d_model, device=device)

        # Build all assignments as tensors (vectorized, no Python loops over tokens)
        t0 = self._now_ms(device)
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
        assignment_ms = self._elapsed_ms(t0, device)

        # Sort by expert_id for cache-friendly execution
        t0 = self._now_ms(device)
        sort_idx = expert_ids.argsort()
        token_ids = token_ids[sort_idx]
        expert_ids = expert_ids[sort_idx]
        weights = weights[sort_idx]

        # Find expert boundaries (vectorized, no Python loop for finding masks)
        # Use unique_consecutive for sorted tensor
        unique_experts, counts = expert_ids.unique_consecutive(return_counts=True)
        pack_ms = self._elapsed_ms(t0, device)

        # Execute per-expert batches
        offset = 0
        expert_compute_ms = 0.0
        scatter_ms = 0.0
        small_batches = 0
        for i in range(unique_experts.shape[0]):
            expert_idx = unique_experts[i].item()
            count = counts[i].item()
            if count < 8:
                small_batches += 1

            expert_token_ids = token_ids[offset:offset + count]
            expert_weights = weights[offset:offset + count]

            # Batched expert call
            expert_input = flat_x[expert_token_ids]
            t0 = self._now_ms(device)
            expert_output = self.expert_deltas[expert_idx](expert_input)
            expert_compute_ms += self._elapsed_ms(t0, device)

            # Weighted scatter-add
            weighted_output = expert_output * expert_weights.unsqueeze(-1)
            t0 = self._now_ms(device)
            sparse_out.scatter_add_(
                0,
                expert_token_ids.unsqueeze(-1).expand_as(weighted_output),
                weighted_output,
            )
            scatter_ms += self._elapsed_ms(t0, device)
            offset += count

        active = max(unique_experts.shape[0], 1)
        return sparse_out, {
            "forward_assignment_build_ms": assignment_ms,
            "forward_pack_ms": pack_ms,
            "forward_expert_compute_ms": expert_compute_ms,
            "forward_scatter_ms": scatter_ms,
            "avg_tokens_per_active_expert": float(token_ids.numel()) / active,
            "small_expert_batch_rate": small_batches / active,
        }

    def _shadow_mergeability_and_tickets(
        self,
        *,
        routing: RoutingOutput,
        expert_outputs: Optional[torch.Tensor],
        timing: dict,
    ) -> tuple[dict, list[dict]]:
        selected_mask = routing.selected_mask
        if selected_mask is None:
            selected_mask = torch.zeros_like(routing.all_probs, dtype=torch.bool)
            selected_mask.scatter_(1, routing.primary_expert_ids.unsqueeze(1), True)
        risk = torch.zeros(routing.all_probs.shape[0], device=routing.all_probs.device)
        pre_scores = pre_expert_mergeability(
            routing.all_probs,
            selected_mask,
            risk=risk,
            weights=self.mergeability_state.current_weights,
        )
        if expert_outputs is not None:
            selected_counts = selected_mask.sum(dim=-1).clamp(min=1)
            disagreement = torch.zeros_like(pre_scores)
            multi = selected_counts > 1
            if multi.any():
                # Dense modes have all expert outputs available, so compute a cheap
                # disagreement proxy against the primary expert output.
                primary_outputs = expert_outputs[
                    torch.arange(expert_outputs.shape[0], device=expert_outputs.device),
                    routing.primary_expert_ids,
                ]
                diff = torch.linalg.norm(expert_outputs - primary_outputs.unsqueeze(1), dim=-1)
                disagreement = (diff * selected_mask.to(diff.dtype)).sum(dim=-1) / selected_counts
                disagreement = disagreement / (torch.linalg.norm(primary_outputs, dim=-1) + 1e-8)
            post_scores = post_expert_mergeability(
                routing.all_probs,
                selected_mask,
                disagreement=disagreement,
                risk=risk,
                weights=self.mergeability_state.current_weights,
            )
        else:
            disagreement = torch.zeros_like(pre_scores)
            post_scores = pre_scores

        tickets = []
        entropy = normalized_entropy(routing.all_probs)
        should_emit_tickets = (
            self.branch_ticket_shadow_mode
            and (not self.training or self.emit_branch_tickets_during_training)
            and self.max_shadow_branch_tickets > 0
        )
        if should_emit_tickets:
            emitted = 0
            for state_id in range(routing.all_probs.shape[0]):
                selected = selected_mask[state_id].nonzero(as_tuple=True)[0].tolist()
                if len(selected) <= 1:
                    continue
                score = float(post_scores[state_id].detach().cpu())
                merge_type = choose_merge_type(score)
                branch_value = float(
                    entropy[state_id].detach().cpu()
                    + routing.all_probs[state_id, selected].sum().detach().cpu()
                    - 0.05 * len(selected)
                    - (1.0 - score)
                )
                tickets.append(make_branch_ticket(
                    state_id=state_id,
                    primary_expert=int(routing.primary_expert_ids[state_id].detach().cpu()),
                    selected_experts=[int(x) for x in selected],
                    uncertainty=float(entropy[state_id].detach().cpu()),
                    mergeability_score=score,
                    branch_value=branch_value,
                    affinity=[float(v) for v in routing.all_probs[state_id].detach().cpu().tolist()],
                    prototype_ids=(
                        [int(routing.nearest_proto_ids[state_id].detach().cpu())]
                        if routing.nearest_proto_ids is not None else []
                    ),
                    prototype_distance=(
                        float(routing.nearest_proto_dist[state_id].detach().cpu())
                        if routing.nearest_proto_dist is not None else 0.0
                    ),
                    difficulty_bucket=Difficulty(int(routing.difficulty[state_id])).name.lower(),
                    merge_type=merge_type,
                ))
                emitted += 1
                if emitted >= self.max_shadow_branch_tickets:
                    break

        score_by_k = {}
        k_vals = selected_mask.sum(dim=-1)
        for k in [1, 2, 4]:
            mask = k_vals == k
            if mask.any():
                score_by_k[f"k{k}"] = float(post_scores[mask].mean().detach().cpu())
        return {
            "mergeability_score_mean": float(post_scores.mean().detach().cpu()),
            "mergeability_score_std": float(post_scores.std(unbiased=False).detach().cpu()),
            "mergeability_score_by_K": score_by_k,
            "mergeability_score_by_task_family": {},
            "merge_success_rate_by_score_bucket": {},
            "merge_failure_rate_by_score_bucket": {},
            "delayed_correction_rate_by_score_bucket": {},
            "mergeability_brier_score": None,
            "mergeability_ece": None,
            "mergeability_prediction_correlation": None,
            "pre_expert_score_mean": float(pre_scores.mean().detach().cpu()),
            "post_expert_score_mean": float(post_scores.mean().detach().cpu()),
            "expert_disagreement_mean": float(disagreement.mean().detach().cpu()),
            "mergeability_score_time_ms": timing.get("forward_total_ms", 0.0) * 0.0,
            "active_or_shadow_mode": "shadow",
        }, tickets

    def get_routing_metrics(self) -> dict:
        """Get current routing state metrics."""
        return {
            "load_bias": self.router.load_bias.detach().cpu().tolist(),
            "expert_load_ema": self.router.expert_load_ema.detach().cpu().tolist(),
            "primary_owner_counts": self.router.primary_owner_counts.detach().cpu().tolist(),
            "update_step": self.router.update_step.item(),
        }
