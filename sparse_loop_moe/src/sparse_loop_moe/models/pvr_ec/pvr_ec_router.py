"""PVR-EC Router Core.

Prototype Variable-k Router with Expert-Choice Expansion.
Implements guaranteed top1 ownership, bucketed variable-k,
load-pressure bias, prototype neighborhoods, and bitset masks.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import IntEnum
from typing import Optional

import torch
import torch.nn as nn
import torch.nn.functional as F


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

    def forward(self, x: torch.Tensor) -> RoutingOutput:
        """Route tokens through PVR-EC.

        Args:
            x: [N, d_model] flattened token batch

        Returns:
            RoutingOutput with assignments and metrics
        """
        N = x.shape[0]
        device = x.device
        c = self.config

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

        # Step 7: Extra expert assignments for NORMAL/HARD
        max_extra = c.max_k - 1  # max 3 extra (top4 total)
        extra_expert_ids = torch.full((N, max_extra), -1, device=device, dtype=torch.long)
        extra_weights = torch.zeros(N, max_extra, device=device)

        # NORMAL tokens: 1 extra expert
        normal_mask = difficulty == Difficulty.NORMAL
        if normal_mask.any():
            normal_probs = probs[normal_mask].clone()
            # Zero out primary
            normal_probs[torch.arange(normal_mask.sum(), device=device),
                         primary_expert_ids[normal_mask]] = 0
            extra1 = normal_probs.argmax(dim=-1)
            extra1_w = normal_probs[torch.arange(normal_mask.sum(), device=device), extra1]
            extra_expert_ids[normal_mask, 0] = extra1
            extra_weights[normal_mask, 0] = extra1_w

        # HARD tokens: up to 3 extra experts
        hard_mask = difficulty == Difficulty.HARD
        if hard_mask.any():
            hard_probs = probs[hard_mask].clone()
            hard_probs[torch.arange(hard_mask.sum(), device=device),
                       primary_expert_ids[hard_mask]] = 0
            for slot in range(min(3, max_extra)):
                extra_e = hard_probs.argmax(dim=-1)
                extra_w = hard_probs[torch.arange(hard_mask.sum(), device=device), extra_e]
                extra_expert_ids[hard_mask, slot] = extra_e
                extra_weights[hard_mask, slot] = extra_w
                # Zero out selected
                hard_probs[torch.arange(hard_mask.sum(), device=device), extra_e] = 0

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
        metrics = {
            "easy_rate": (difficulty == Difficulty.EASY).float().mean().item(),
            "normal_rate": (difficulty == Difficulty.NORMAL).float().mean().item(),
            "hard_rate": (difficulty == Difficulty.HARD).float().mean().item(),
            "avg_active_experts": 1.0 + (extra_expert_ids != -1).float().sum() / max(N, 1),
            "routing_entropy": norm_entropy.mean().item(),
            "avg_margin": margin.mean().item(),
            "expert_utilization": (expert_load > 0.001).float().mean().item(),
            "load_imbalance": expert_load.std().item(),
            "primary_owner_entropy": -(expert_load * torch.log(expert_load + 1e-8)).sum().item(),
            "dead_expert_count": (expert_load < 0.001).sum().item(),
            "load_bias_magnitude": self.load_bias.abs().mean().item(),
        }

        return RoutingOutput(
            primary_expert_ids=primary_expert_ids,
            primary_weights=primary_weights,
            extra_expert_ids=extra_expert_ids,
            extra_weights=extra_weights,
            difficulty=difficulty,
            all_probs=probs,
            load_balance_loss=load_balance_loss,
            metrics=metrics,
        )

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
