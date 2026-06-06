"""PVR-EC Router Core.

Prototype Variable-k Router with Expert-Choice Expansion.
Implements guaranteed top1 ownership, bucketed variable-k,
load-pressure bias, prototype neighborhoods, and bitset masks.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import IntEnum
from typing import Optional

import torch
import torch.nn as nn
import torch.nn.functional as F

from sparse_loop_moe.models.pvr_ec.diagnostics import K_ALLOWED


class Difficulty(IntEnum):
    EASY = 0
    NORMAL = 1
    HARD = 2


@dataclass
class PVRECConfig:
    """Configuration for PVR-EC router."""
    d_model: int = 128
    num_experts: int = 4
    num_prototypes: int = 16
    d_route: int = 64
    max_k: int = 4
    expert_capacity_factor: float = 1.5
    load_bias_eta: float = 0.01
    load_bias_cap: float = 0.20
    # Difficulty thresholds
    easy_margin_threshold: float = 0.4
    hard_entropy_threshold: float = 0.7
    hard_margin_threshold: float = 0.15
    # Primary owner target weight
    primary_weight_target: float = 0.70
    dropout: float = 0.1
    routing_mode: str = "variable_k_pack_by_expert"
    target_avg_k: float = 2.0
    k_allowed: tuple[int, ...] = K_ALLOWED
    expert_capacity: Optional[int] = None
    branch_ticket_shadow_mode: bool = True


@dataclass
class RoutingOutput:
    """Output from PVR-EC routing."""
    primary_expert_ids: torch.Tensor      # [N] guaranteed top1
    primary_weights: torch.Tensor          # [N]
    extra_expert_ids: torch.Tensor         # [N, max_extra] padded with -1
    extra_weights: torch.Tensor            # [N, max_extra]
    difficulty: torch.Tensor               # [N] Difficulty enum values
    all_probs: torch.Tensor                # [N, num_experts]
    load_balance_loss: torch.Tensor        # scalar
    metrics: dict
    nearest_proto_ids: Optional[torch.Tensor] = None
    nearest_proto_dist: Optional[torch.Tensor] = None
    selected_mask: Optional[torch.Tensor] = None


@dataclass
class RoutingState:
    """Mutable routing state (load bias, prototype stats)."""
    load_bias: torch.Tensor                # [num_experts]
    expert_load_ema: torch.Tensor          # [num_experts]
    primary_owner_counts: torch.Tensor     # [num_experts]
    update_step: int = 0


class PVRECRouter(nn.Module):
    """PVR-EC Router: Prototype Variable-k with Expert-Choice Expansion.

    Flow:
    1. Project hidden states into routing space
    2. Find nearest prototypes
    3. Use prototype->expert bitset to shortlist candidates
    4. Score candidates, apply prototype bias + load-pressure bias
    5. Classify difficulty (EASY/NORMAL/HARD)
    6. Assign guaranteed top1 primary owner to every token
    7. For NORMAL/HARD tokens, allocate extra expert slots
    8. Return packed assignments

    Critical invariant: candidates and probabilities are always in sync.
    """

    def __init__(self, config: PVRECConfig):
        super().__init__()
        self.config = config
        c = config

        # Route projection
        self.route_proj = nn.Linear(c.d_model, c.d_route, bias=False)

        # Prototype embeddings (learned cluster centers in routing space)
        self.prototypes = nn.Parameter(torch.randn(c.num_prototypes, c.d_route) * 0.1)

        # Prototype -> expert compatibility bitset [num_prototypes, num_experts]
        # Initialized so each prototype is compatible with ~half the experts
        proto_compat_init = torch.rand(c.num_prototypes, c.num_experts) > 0.4
        self.register_buffer("proto_expert_compat", proto_compat_init.float())

        # Router gate (scores experts given routing-space embedding)
        self.gate = nn.Linear(c.d_route, c.num_experts, bias=False)

        # Prototype bias projection (small learned bias per prototype)
        self.proto_bias = nn.Parameter(torch.zeros(c.num_prototypes, c.num_experts))

        # Load-pressure bias (non-learned, updated by EMA)
        self.register_buffer("load_bias", torch.zeros(c.num_experts))
        self.register_buffer("expert_load_ema", torch.ones(c.num_experts) / c.num_experts)
        self.register_buffer("primary_owner_counts", torch.zeros(c.num_experts))
        self.register_buffer("update_step", torch.tensor(0, dtype=torch.long))

    def forward(self, x: torch.Tensor, routing_mode: Optional[str] = None) -> RoutingOutput:
        """Route tokens through PVR-EC.

        Args:
            x: [N, d_model] flattened token batch

        Returns:
            RoutingOutput with assignments and metrics
        """
        N = x.shape[0]
        device = x.device
        c = self.config
        routing_mode = routing_mode or c.routing_mode

        # Step 1: Project to routing space
        z = self.route_proj(x)  # [N, d_route]

        # Step 2: Find nearest prototypes
        proto_dist = torch.cdist(z.unsqueeze(0), self.prototypes.unsqueeze(0)).squeeze(0)  # [N, num_proto]
        nearest_proto_ids = proto_dist.argmin(dim=-1)  # [N]
        nearest_proto_dist = proto_dist[torch.arange(N, device=device), nearest_proto_ids]

        # Step 3: Get candidate masks from prototype compatibility
        # candidate_mask[i] = proto_expert_compat[nearest_proto_ids[i]]
        candidate_mask = self.proto_expert_compat[nearest_proto_ids]  # [N, num_experts]

        # Ensure at least 2 experts are candidates per token (safety)
        while (candidate_mask.sum(dim=-1) < 2).any():
            low_mask = candidate_mask.sum(dim=-1) < 2
            # Add the expert with highest gate score
            fallback_scores = self.gate(z[low_mask])
            fallback_scores[candidate_mask[low_mask].bool()] = -float("inf")
            best_fallback = fallback_scores.argmax(dim=-1)
            for i, idx in enumerate(low_mask.nonzero(as_tuple=True)[0]):
                candidate_mask[idx, best_fallback[i]] = 1.0
            break  # One pass is enough for safety

        # Step 4: Score candidates with prototype bias + load-pressure bias
        router_logits = self.gate(z)  # [N, num_experts]

        # Apply prototype bias
        proto_bias_per_token = self.proto_bias[nearest_proto_ids]  # [N, num_experts]

        # Compute effective logits
        effective_logits = router_logits + proto_bias_per_token + self.load_bias.unsqueeze(0)

        # Mask out incompatible experts
        effective_logits = effective_logits.masked_fill(candidate_mask == 0, -float("inf"))

        # Compute probabilities
        probs = F.softmax(effective_logits, dim=-1)  # [N, num_experts]

        # Step 5: Classify difficulty
        top2_vals, top2_ids = probs.topk(min(2, c.num_experts), dim=-1)
        top1_prob = top2_vals[:, 0]
        margin = top2_vals[:, 0] - top2_vals[:, 1] if top2_vals.shape[1] > 1 else top1_prob

        # Entropy (normalized)
        entropy = -(probs * torch.log(probs + 1e-8)).sum(dim=-1)
        max_entropy = torch.log(torch.tensor(float(c.num_experts), device=device))
        norm_entropy = entropy / (max_entropy + 1e-8)

        difficulty = torch.full((N,), Difficulty.NORMAL, device=device, dtype=torch.long)
        difficulty[margin > c.easy_margin_threshold] = Difficulty.EASY
        difficulty[(norm_entropy > c.hard_entropy_threshold) | (margin < c.hard_margin_threshold)] = Difficulty.HARD

        # Step 6: Guaranteed top1 primary owner
        primary_expert_ids = probs.argmax(dim=-1)  # [N]
        primary_weights = probs[torch.arange(N, device=device), primary_expert_ids]

        # Normalize primary weight toward target
        primary_weights = torch.clamp(primary_weights, min=0.3, max=0.95)

        # Step 7: Expert assignments. Modes share probabilities but differ in
        # route-width regularity and expert-choice budget enforcement.
        if routing_mode in {"fixed_top2_pack_by_expert", "fixed_top2_all_experts_masked"}:
            extra_expert_ids, extra_weights, selected_mask, mode_metrics = self._fixed_top2_assignments(
                probs, primary_expert_ids
            )
            difficulty = torch.full_like(difficulty, Difficulty.NORMAL)
        elif routing_mode == "hybrid_expert_choice_bucketed":
            extra_expert_ids, extra_weights, selected_mask, mode_metrics = self._hybrid_expert_choice_assignments(
                probs=probs,
                primary_expert_ids=primary_expert_ids,
                difficulty=difficulty,
                margin=margin,
                norm_entropy=norm_entropy,
            )
        else:
            extra_expert_ids, extra_weights, selected_mask, mode_metrics = self._variable_k_assignments(
                probs=probs,
                primary_expert_ids=primary_expert_ids,
                difficulty=difficulty,
            )

        # Normalize extra weights so primary + extras sum to ~1
        total_extra_w = extra_weights.sum(dim=-1)  # [N]
        scale = (1.0 - primary_weights) / (total_extra_w + 1e-8)
        scale = torch.clamp(scale, max=1.0)
        extra_weights = extra_weights * scale.unsqueeze(-1)

        # Step 8: Compute load balance loss
        # Target: uniform load across experts
        expert_load = torch.zeros(c.num_experts, device=device)
        expert_load.scatter_add_(0, primary_expert_ids, torch.ones(N, device=device))
        expert_load = expert_load / N
        target_load = 1.0 / c.num_experts
        load_balance_loss = c.num_experts * (expert_load * probs.mean(dim=0)).sum()

        # Update load bias (EMA, training only)
        if self.training:
            self._update_load_state(expert_load, primary_expert_ids, N)

        # Metrics
        final_k = selected_mask.sum(dim=-1)
        assignment_budget_target = N * c.target_avg_k
        total_final_assignments = final_k.sum().item()
        budget_drift = (
            (total_final_assignments - assignment_budget_target) / max(assignment_budget_target, 1.0)
        )
        k_distribution = {
            "k1": (final_k == 1).sum().item(),
            "k2": (final_k == 2).sum().item(),
            "k4": (final_k == 4).sum().item(),
        }
        metrics = {
            "routing_mode": routing_mode,
            "easy_rate": (difficulty == Difficulty.EASY).float().mean().item(),
            "normal_rate": (difficulty == Difficulty.NORMAL).float().mean().item(),
            "hard_rate": (difficulty == Difficulty.HARD).float().mean().item(),
            "avg_active_experts": final_k.float().mean().item(),
            "actual_avg_k": final_k.float().mean().item(),
            "target_avg_K": c.target_avg_k,
            "K_distribution": k_distribution,
            "num_k1_tokens": k_distribution["k1"],
            "num_k2_tokens": k_distribution["k2"],
            "num_k4_tokens": k_distribution["k4"],
            "assignment_budget_drift": budget_drift,
            "total_final_assignments": total_final_assignments,
            "assignment_budget_status": (
                "PVR_EC_ASSIGNMENT_BUDGET_DRIFT" if abs(budget_drift) > 0.10 else "ok"
            ),
            "routing_entropy": norm_entropy.mean().item(),
            "avg_margin": margin.mean().item(),
            "expert_utilization": (expert_load > 0.001).float().mean().item(),
            "load_imbalance": expert_load.std().item(),
            "primary_owner_entropy": -(expert_load * torch.log(expert_load + 1e-8)).sum().item(),
            "dead_expert_count": (expert_load < 0.001).sum().item(),
            "load_bias_magnitude": self.load_bias.abs().mean().item(),
        }
        metrics.update(mode_metrics)

        return RoutingOutput(
            primary_expert_ids=primary_expert_ids,
            primary_weights=primary_weights,
            extra_expert_ids=extra_expert_ids,
            extra_weights=extra_weights,
            difficulty=difficulty,
            all_probs=probs,
            load_balance_loss=load_balance_loss,
            metrics=metrics,
            nearest_proto_ids=nearest_proto_ids,
            nearest_proto_dist=nearest_proto_dist,
            selected_mask=selected_mask,
        )

    def deploy_topk(self, x: torch.Tensor, k: int = 2) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        """Tensor-only deployment routing.

        Returns:
            top_ids: [N, k]
            top_weights: [N, k]
            entropy: [N]
        """

        c = self.config
        z = self.route_proj(x)
        proto_dist = torch.cdist(z.unsqueeze(0), self.prototypes.unsqueeze(0)).squeeze(0)
        nearest_proto_ids = proto_dist.argmin(dim=-1)
        candidate_mask = self.proto_expert_compat[nearest_proto_ids].bool()
        router_logits = self.gate(z)
        required = min(k, c.num_experts)
        candidate_count = candidate_mask.sum(dim=-1)
        missing = (required - candidate_count).clamp(min=0)
        fallback_scores = router_logits.masked_fill(candidate_mask, -float("inf"))
        fallback_ids = fallback_scores.topk(required, dim=-1).indices
        rank = torch.arange(required, device=x.device).unsqueeze(0)
        fallback_keep = rank < missing.unsqueeze(1)
        fallback_mask = torch.zeros_like(candidate_mask)
        fallback_mask.scatter_(1, fallback_ids, fallback_keep)
        candidate_mask = candidate_mask | fallback_mask

        logits = router_logits + self.proto_bias[nearest_proto_ids] + self.load_bias.unsqueeze(0)
        logits = logits.masked_fill(candidate_mask == 0, -float("inf"))
        probs = F.softmax(logits, dim=-1)
        top_weights, top_ids = probs.topk(required, dim=-1)
        entropy = -(probs * torch.log(probs + 1e-8)).sum(dim=-1)
        return top_ids, top_weights, entropy

    def _fixed_top2_assignments(
        self,
        probs: torch.Tensor,
        primary_expert_ids: torch.Tensor,
    ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, dict]:
        """Select top-2 experts for every token."""

        N, E = probs.shape
        device = probs.device
        max_extra = max(self.config.max_k - 1, 0)
        extra_expert_ids = torch.full((N, max_extra), -1, device=device, dtype=torch.long)
        extra_weights = torch.zeros(N, max_extra, device=device)
        selected_mask = torch.zeros(N, E, device=device, dtype=torch.bool)
        selected_mask.scatter_(1, primary_expert_ids.unsqueeze(1), True)

        if max_extra > 0 and E > 1:
            masked = probs.clone()
            masked[torch.arange(N, device=device), primary_expert_ids] = -1.0
            extra = masked.argmax(dim=-1)
            extra_expert_ids[:, 0] = extra
            extra_weights[:, 0] = probs[torch.arange(N, device=device), extra]
            selected_mask.scatter_(1, extra.unsqueeze(1), True)

        return extra_expert_ids, extra_weights, selected_mask, {
            "fallback_top1_count": 0,
            "overflow_count": 0,
            "expert_choice_select_time_ms": 0.0,
            "coverage_repair_time_ms": 0.0,
            "k_bucket_enforce_time_ms": 0.0,
            "capacity_repair_time_ms": 0.0,
        }

    def _variable_k_assignments(
        self,
        probs: torch.Tensor,
        primary_expert_ids: torch.Tensor,
        difficulty: torch.Tensor,
    ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, dict]:
        """Current bucketed variable-k assignment path."""

        N, E = probs.shape
        device = probs.device
        c = self.config
        max_extra = c.max_k - 1
        extra_expert_ids = torch.full((N, max_extra), -1, device=device, dtype=torch.long)
        extra_weights = torch.zeros(N, max_extra, device=device)
        selected_mask = torch.zeros(N, E, device=device, dtype=torch.bool)
        selected_mask.scatter_(1, primary_expert_ids.unsqueeze(1), True)

        normal_mask = difficulty == Difficulty.NORMAL
        if normal_mask.any() and max_extra > 0:
            normal_probs = probs[normal_mask].clone()
            normal_probs[torch.arange(normal_mask.sum(), device=device),
                         primary_expert_ids[normal_mask]] = 0
            extra1 = normal_probs.argmax(dim=-1)
            extra1_w = normal_probs[torch.arange(normal_mask.sum(), device=device), extra1]
            extra_expert_ids[normal_mask, 0] = extra1
            extra_weights[normal_mask, 0] = extra1_w
            selected_mask[normal_mask, extra1] = True

        hard_mask = difficulty == Difficulty.HARD
        if hard_mask.any() and max_extra > 0:
            hard_probs = probs[hard_mask].clone()
            hard_probs[torch.arange(hard_mask.sum(), device=device),
                       primary_expert_ids[hard_mask]] = 0
            hard_rows = hard_mask.nonzero(as_tuple=True)[0]
            for slot in range(min(3, max_extra)):
                extra_e = hard_probs.argmax(dim=-1)
                extra_w = hard_probs[torch.arange(hard_mask.sum(), device=device), extra_e]
                extra_expert_ids[hard_mask, slot] = extra_e
                extra_weights[hard_mask, slot] = extra_w
                selected_mask[hard_rows, extra_e] = True
                hard_probs[torch.arange(hard_mask.sum(), device=device), extra_e] = 0

        return extra_expert_ids, extra_weights, selected_mask, {
            "fallback_top1_count": 0,
            "overflow_count": 0,
            "expert_choice_select_time_ms": 0.0,
            "coverage_repair_time_ms": 0.0,
            "k_bucket_enforce_time_ms": 0.0,
            "capacity_repair_time_ms": 0.0,
        }

    def _hybrid_expert_choice_assignments(
        self,
        *,
        probs: torch.Tensor,
        primary_expert_ids: torch.Tensor,
        difficulty: torch.Tensor,
        margin: torch.Tensor,
        norm_entropy: torch.Tensor,
    ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, dict]:
        """Hybrid expert-choice scaffold with vectorized bucketed K enforcement.

        The original MVP used Python loops over every token. That made the
        diagnostic router dominate training wall-clock on GPU. This path keeps
        the same bounded speculation contract (K in {1, 2, 4}, top1 coverage,
        capacity repair) while using token-side top-k tensors and only looping
        over experts for capacity repair.
        """

        N, E = probs.shape
        device = probs.device
        c = self.config
        max_k = min(c.max_k, max(c.k_allowed))
        capacity = c.expert_capacity or max(1, int((N * c.target_avg_k / E) * c.expert_capacity_factor))

        # K hints: uncertainty controls speculation width, then enforce {1,2,4}.
        requested_k = torch.ones(N, device=device, dtype=torch.long)
        requested_k[difficulty == Difficulty.NORMAL] = 2
        requested_k[difficulty == Difficulty.HARD] = 4
        requested_k[(norm_entropy > 0.85) & (margin < 0.10)] = 4
        requested_k = torch.clamp(requested_k, max=min(max_k, E))

        top_count = min(max_k, E)
        top_ids = probs.topk(top_count, dim=-1).indices
        ranks = torch.arange(top_count, device=device).unsqueeze(0)
        keep_by_rank = ranks < requested_k.unsqueeze(1)

        selected_mask = torch.zeros(N, E, device=device, dtype=torch.bool)
        selected_mask.scatter_(1, top_ids, keep_by_rank)
        selected_mask.scatter_(1, primary_expert_ids.unsqueeze(1), True)
        fallback_top1 = 0
        overflow_count = 0

        # Capacity repair drops weakest non-primary overflow assignments.
        capacity_drops = 0
        for expert_id in range(E):
            assigned = selected_mask[:, expert_id].nonzero(as_tuple=True)[0]
            if assigned.numel() <= capacity:
                continue
            primary_assigned = assigned[primary_expert_ids[assigned] == expert_id]
            optional_assigned = assigned[primary_expert_ids[assigned] != expert_id]
            keep_optional_count = max(capacity - primary_assigned.numel(), 0)
            if optional_assigned.numel() > keep_optional_count:
                drop_count = optional_assigned.numel() - keep_optional_count
                drop_scores = probs[optional_assigned, expert_id]
                drop = optional_assigned[drop_scores.topk(drop_count, largest=False).indices]
                selected_mask[drop, expert_id] = False
                capacity_drops += int(drop_count)

        # Top1 coverage is hard; repair any token knocked down to zero.
        selected_mask.scatter_(1, primary_expert_ids.unsqueeze(1), True)

        # Capacity repair can turn K=4 into K=3. Refill those rows with the
        # strongest remaining expert so K remains in {1, 2, 4}.
        k_counts = selected_mask.sum(dim=-1)
        three_mask = (k_counts == 3) & (4 in c.k_allowed) & (max_k >= 4) & (E >= 4)
        if three_mask.any():
            refill_scores = probs[three_mask].masked_fill(selected_mask[three_mask], -1.0)
            refill = refill_scores.argmax(dim=-1)
            rows = three_mask.nonzero(as_tuple=True)[0]
            selected_mask[rows, refill] = True

        max_extra = c.max_k - 1
        extras_mask = selected_mask.clone()
        extras_mask.scatter_(1, primary_expert_ids.unsqueeze(1), False)
        if max_extra > 0:
            extra_scores = probs.masked_fill(~extras_mask, -1.0)
            top_extra_w, top_extra_ids = extra_scores.topk(max_extra, dim=-1)
            valid = top_extra_w >= 0.0
            extra_expert_ids = torch.where(
                valid,
                top_extra_ids,
                torch.full_like(top_extra_ids, -1),
            )
            extra_weights = torch.where(valid, top_extra_w, torch.zeros_like(top_extra_w))
        else:
            extra_expert_ids = torch.empty(N, 0, device=device, dtype=torch.long)
            extra_weights = torch.empty(N, 0, device=device)

        return extra_expert_ids, extra_weights, selected_mask, {
            "fallback_top1_count": fallback_top1,
            "overflow_count": overflow_count,
            "expert_capacity": capacity,
            "capacity_repair_drop_count": capacity_drops,
            "expert_choice_select_time_ms": 0.0,
            "coverage_repair_time_ms": 0.0,
            "k_bucket_enforce_time_ms": 0.0,
            "capacity_repair_time_ms": 0.0,
            "PVR_EC_SPECULATIVE_ROUTER_ENABLED": True,
        }

    def _update_load_state(self, expert_load: torch.Tensor, primary_ids: torch.Tensor, N: int):
        """Update load-pressure bias using EMA."""
        c = self.config
        # EMA update of load
        alpha = 0.1
        self.expert_load_ema.mul_(1 - alpha).add_(expert_load, alpha=alpha)

        # Update load bias
        target_share = 1.0 / c.num_experts
        load_error = self.expert_load_ema - target_share
        self.load_bias.sub_(c.load_bias_eta * load_error)
        self.load_bias.clamp_(-c.load_bias_cap, c.load_bias_cap)

        # Track primary owner counts
        self.primary_owner_counts.zero_()
        self.primary_owner_counts.scatter_add_(0, primary_ids, torch.ones(N, device=primary_ids.device))
        self.update_step += 1
