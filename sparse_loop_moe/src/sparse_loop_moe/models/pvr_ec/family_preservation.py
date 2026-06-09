"""Family Preservation Observatory for PVR-EC-O.

Measures whether single-owner Top1 routing preserves the latent family/prototype
structure that produced each state.

Key insight: A state may belong to multiple latent families (60% syntax, 30% semantic,
10% structural) while deployment still executes owner=expert_7. The question is whether
that owner preserves the latent family evidence.

This module provides:
- Family membership computation (soft, from prototype neighborhoods)
- Family preservation scoring (does the final owner preserve family structure?)
- Shadow family-preservation bias (tensor-backed, GPU-resident, never active in first pass)
- Family-aware oracle gap computation
- Overlap/boundary detection
- Owner churn tracking
- Family preservation gate logic
"""

from __future__ import annotations

from dataclasses import dataclass, field, asdict
from typing import Any, Optional
import math

import torch
import torch.nn.functional as F


# =============================================================================
# Family Preservation Failure Modes
# =============================================================================

FAMILY_PRESERVATION_FAILURE_MODES = (
    "PVR_EC_FAILURE_FAMILY_PRESERVATION_LOSS",
    "PVR_EC_FAILURE_OVERLAP_BOUNDARY_MISROUTE",
    "PVR_EC_FAILURE_NOISY_REGION_OWNERSHIP",
    "PVR_EC_FAILURE_FAMILY_OWNER_CHURN",
    "PVR_EC_FAILURE_PROTOTYPE_FAMILY_COLLAPSE",
    "PVR_EC_FAILURE_BALANCE_BIAS_FAMILY_OVERRIDE",
    "PVR_EC_FAILURE_FAMILY_AWARE_ORACLE_GAP_HIGH",
    "PVR_EC_FAILURE_SOFT_FAMILY_EVIDENCE_DROPPED",
    "PVR_EC_FAILURE_FAMILY_LABEL_PROXY_DISAGREEMENT",
    "PVR_EC_FAILURE_NLP_AMBIGUOUS_TOKEN_OWNERSHIP",
    "PVR_EC_FAILURE_NLP_CONTEXT_INSENSITIVE_ROUTING",
    "PVR_EC_FAILURE_NLP_LENGTH_GENERALIZATION_COLLAPSE",
    "PVR_EC_FAILURE_NLP_OBSERVATORY_TAXONOMY_GAP",
)

# Gate verdicts
FAMILY_PRESERVATION_VERDICTS = (
    "PVR_EC_FAMILY_PRESERVATION_PASSED",
    "PVR_EC_FAMILY_PRESERVATION_PASSED_WITH_BLOCKERS",
    "PVR_EC_FAMILY_PRESERVATION_BLOCKED",
    "PVR_EC_FAMILY_PRESERVATION_OBSERVATORY_EXPANSION_REQUIRED",
)

NLP_STAGE1_VERDICTS = (
    "PVR_EC_NLP_STAGE1_RESEARCH_ALLOWED",
    "PVR_EC_NLP_STAGE1_RESEARCH_ALLOWED_WITH_BLOCKERS",
    "PVR_EC_NLP_STAGE1_OBSERVATORY_EXPANSION_REQUIRED",
    "PVR_EC_NLP_STAGE1_DO_NOT_EXPAND",
)


# =============================================================================
# Family Membership Computation
# =============================================================================


@dataclass
class FamilyMembership:
    """Soft family membership for a batch of states."""
    # [N, num_prototypes] - distance to each prototype
    prototype_distances: torch.Tensor
    # [N, num_prototypes] - soft membership (normalized)
    soft_membership: torch.Tensor
    # [N] - entropy of membership distribution
    membership_entropy: torch.Tensor
    # [N] - margin between top-1 and top-2 prototype
    membership_margin: torch.Tensor
    # [N] - whether state is near a boundary (low margin)
    is_boundary: torch.Tensor
    # [N] - nearest prototype id
    nearest_prototype: torch.Tensor


def compute_family_membership(
    routing_space_embeddings: torch.Tensor,
    prototypes: torch.Tensor,
    temperature: float = 1.0,
    boundary_threshold: float = 0.15,
) -> FamilyMembership:
    """Compute soft family membership from prototype distances.

    Args:
        routing_space_embeddings: [N, d_route] - states projected to routing space
        prototypes: [num_prototypes, d_route] - prototype embeddings
        temperature: softmax temperature for membership
        boundary_threshold: margin below which a state is "boundary"

    Returns:
        FamilyMembership with all computed fields
    """
    # [N, num_prototypes]
    distances = torch.cdist(
        routing_space_embeddings.unsqueeze(0),
        prototypes.unsqueeze(0),
    ).squeeze(0)

    # Convert distances to similarities (negative distance / temperature)
    similarities = -distances / max(temperature, 1e-8)
    soft_membership = F.softmax(similarities, dim=-1)

    # Entropy of membership distribution
    log_probs = torch.log(soft_membership + 1e-8)
    entropy = -(soft_membership * log_probs).sum(dim=-1)

    # Margin between top-1 and top-2
    top2_vals, top2_ids = soft_membership.topk(2, dim=-1)
    margin = top2_vals[:, 0] - top2_vals[:, 1]

    # Boundary detection
    is_boundary = margin < boundary_threshold

    # Nearest prototype
    nearest = distances.argmin(dim=-1)

    return FamilyMembership(
        prototype_distances=distances,
        soft_membership=soft_membership,
        membership_entropy=entropy,
        membership_margin=margin,
        is_boundary=is_boundary,
        nearest_prototype=nearest,
    )


# =============================================================================
# Family Preservation Score
# =============================================================================


def compute_family_preservation_score(
    soft_membership: torch.Tensor,
    owner_ids: torch.Tensor,
    owner_prototype_affinity: torch.Tensor,
) -> torch.Tensor:
    """Compute per-token family preservation score.

    Measures how well the assigned owner preserves the state's family structure.

    Args:
        soft_membership: [N, num_prototypes] - soft family membership
        owner_ids: [N] - assigned owner expert id per token
        owner_prototype_affinity: [num_experts, num_prototypes] - how well each
            expert serves each prototype/family (learned from history)

    Returns:
        [N] preservation score in [0, 1] where 1 = perfect preservation
    """
    N = soft_membership.shape[0]
    # Get the affinity of the assigned owner for each prototype
    # owner_affinity[i] = owner_prototype_affinity[owner_ids[i]]  -> [N, num_prototypes]
    owner_affinity = owner_prototype_affinity[owner_ids]

    # Preservation = dot product of soft_membership and owner_affinity
    # (how much does this owner cover the state's family distribution?)
    # Normalize owner_affinity to [0, 1] range per expert
    owner_affinity_norm = torch.sigmoid(owner_affinity)

    # Weighted sum: how much of the state's family membership is served by this owner
    preservation = (soft_membership * owner_affinity_norm).sum(dim=-1)

    return preservation.clamp(0.0, 1.0)


# =============================================================================
# Family-Aware Oracle Gap
# =============================================================================


def compute_family_oracle_gap(
    losses_per_expert: torch.Tensor,
    owner_ids: torch.Tensor,
) -> tuple[torch.Tensor, torch.Tensor]:
    """Compute family-aware oracle gap per token.

    Args:
        losses_per_expert: [N, num_experts] - loss if each expert were the owner
        owner_ids: [N] - currently assigned owner

    Returns:
        (oracle_gap, best_expert_ids) where:
        oracle_gap[i] = loss(current_owner) - loss(best_expert)
        best_expert_ids[i] = argmin expert loss
    """
    N = losses_per_expert.shape[0]
    device = losses_per_expert.device

    # Current owner loss
    current_loss = losses_per_expert[torch.arange(N, device=device), owner_ids]

    # Best available expert loss
    best_loss, best_ids = losses_per_expert.min(dim=-1)

    # Gap (positive = current owner is worse than best)
    oracle_gap = current_loss - best_loss

    return oracle_gap, best_ids


# =============================================================================
# Owner Churn Tracking
# =============================================================================


@dataclass
class OwnerChurnState:
    """Tracks owner changes across checkpoints/seeds for churn detection."""
    # [num_prototypes, num_experts] - count of times each expert owned each prototype
    ownership_counts: torch.Tensor
    # Number of snapshots recorded
    num_snapshots: int = 0

    def record_snapshot(self, owner_ids: torch.Tensor, prototype_ids: torch.Tensor):
        """Record ownership assignments from one run/seed."""
        for p_id, o_id in zip(prototype_ids.tolist(), owner_ids.tolist()):
            self.ownership_counts[p_id, o_id] += 1
        self.num_snapshots += 1

    def churn_rate(self) -> torch.Tensor:
        """Per-prototype churn rate: 1 - (max_count / total_count)."""
        totals = self.ownership_counts.sum(dim=-1).clamp(min=1)
        max_counts = self.ownership_counts.max(dim=-1).values
        stability = max_counts / totals
        return 1.0 - stability


# =============================================================================
# Shadow Family-Preservation Bias
# =============================================================================


@dataclass
class FamilyPreservationBiasConfig:
    """Configuration for shadow family-preservation bias."""
    family_bias_weight: float = 0.25
    family_bias_cap: float = 0.25
    semantic_family_margin_guard: float = 0.10
    num_prototypes: int = 16
    num_experts: int = 4


class ShadowFamilyPreservationBias:
    """Shadow-mode family-preservation bias.

    Tensor-backed, GPU-resident, clipped, compatible-mask constrained.
    Never active in the first diagnostic pass.
    Computes what the bias *would* do without changing actual routing.
    """

    def __init__(self, config: FamilyPreservationBiasConfig):
        self.config = config
        # Reliability: how often expert e succeeds for prototype/family f
        self.family_owner_reliability = torch.zeros(
            config.num_prototypes, config.num_experts
        )
        # Failure: how often expert e fails for prototype/family f
        self.family_owner_failure = torch.zeros(
            config.num_prototypes, config.num_experts
        )
        self._active = False  # Never active in first pass

    @property
    def is_shadow_only(self) -> bool:
        """Always shadow in diagnostic pass."""
        return not self._active

    def raw_bias(self) -> torch.Tensor:
        """[num_prototypes, num_experts] raw family bias."""
        return self.family_owner_reliability - self.family_owner_failure

    def clipped_bias(self) -> torch.Tensor:
        """[num_prototypes, num_experts] clipped family bias."""
        raw = self.raw_bias()
        scaled = self.config.family_bias_weight * raw
        return scaled.clamp(-self.config.family_bias_cap, self.config.family_bias_cap)

    def compute_shadow_scores(
        self,
        current_scores: torch.Tensor,
        prototype_ids: torch.Tensor,
        compatible_mask: torch.Tensor,
    ) -> dict[str, Any]:
        """Compute what family bias would do (shadow only).

        Args:
            current_scores: [N, num_experts] current routing scores
            prototype_ids: [N] nearest prototype per token
            compatible_mask: [N, num_experts] binary compatibility

        Returns:
            Dict with shadow analysis (would_change_owner, etc.)
        """
        N = current_scores.shape[0]
        device = current_scores.device

        # Move bias to device if needed
        bias = self.clipped_bias().to(device)

        # Get per-token family bias
        token_bias = bias[prototype_ids]  # [N, num_experts]

        # Shadow scores
        shadow_scores = current_scores + token_bias
        # Mask incompatible
        shadow_scores = shadow_scores.masked_fill(compatible_mask == 0, -float("inf"))

        # Current owner
        current_owner = current_scores.masked_fill(
            compatible_mask == 0, -float("inf")
        ).argmax(dim=-1)
        # Shadow owner
        shadow_owner = shadow_scores.argmax(dim=-1)

        # Would change?
        would_change = (current_owner != shadow_owner)

        return {
            "shadow_owner": shadow_owner,
            "current_owner": current_owner,
            "would_change_owner": would_change,
            "change_rate": would_change.float().mean().item(),
            "family_bias_applied": token_bias,
            "shadow_scores": shadow_scores,
        }

    def update_from_evidence(
        self,
        prototype_ids: torch.Tensor,
        expert_ids: torch.Tensor,
        success: torch.Tensor,
    ):
        """Update reliability/failure from offline evidence.

        Args:
            prototype_ids: [N] prototype assignments
            expert_ids: [N] expert assignments
            success: [N] boolean - did this expert succeed?
        """
        for p, e, s in zip(
            prototype_ids.tolist(), expert_ids.tolist(), success.tolist()
        ):
            if s:
                self.family_owner_reliability[p, e] += 1.0
            else:
                self.family_owner_failure[p, e] += 1.0


# =============================================================================
# Family Preservation Metrics
# =============================================================================


def compute_family_metrics(
    soft_membership: torch.Tensor,
    owner_ids: torch.Tensor,
    prototype_ids: torch.Tensor,
    num_experts: int,
    family_labels: Optional[torch.Tensor] = None,
) -> dict[str, float]:
    """Compute all family preservation metrics for a batch.

    Args:
        soft_membership: [N, num_prototypes]
        owner_ids: [N]
        prototype_ids: [N]
        num_experts: int
        family_labels: [N] optional external family labels

    Returns:
        Dict of metric name -> value
    """
    N = soft_membership.shape[0]
    num_prototypes = soft_membership.shape[1]

    # Expert family purity: for each expert, what fraction of its tokens
    # share the same dominant prototype?
    expert_purity_values = []
    expert_coverage_values = []
    for e in range(num_experts):
        mask = owner_ids == e
        if mask.sum() == 0:
            continue
        protos_for_expert = prototype_ids[mask]
        if protos_for_expert.numel() == 0:
            continue
        counts = torch.bincount(protos_for_expert, minlength=num_prototypes).float()
        total = counts.sum()
        purity = (counts.max() / total).item() if total > 0 else 0.0
        coverage = (counts > 0).sum().item() / max(num_prototypes, 1)
        expert_purity_values.append(purity)
        expert_coverage_values.append(coverage)

    # Prototype-family-owner consistency: for each prototype, is there
    # a dominant owner that is consistent?
    proto_owner_consistency = []
    proto_monopoly_rates = []
    for p in range(num_prototypes):
        mask = prototype_ids == p
        if mask.sum() == 0:
            continue
        owners_for_proto = owner_ids[mask]
        counts = torch.bincount(owners_for_proto, minlength=num_experts).float()
        total = counts.sum()
        if total > 0:
            consistency = (counts.max() / total).item()
            proto_owner_consistency.append(consistency)
            proto_monopoly_rates.append(1.0 if consistency > 0.9 else 0.0)

    # Owner entropy
    owner_counts = torch.bincount(owner_ids, minlength=num_experts).float()
    owner_probs = owner_counts / max(owner_counts.sum().item(), 1.0)
    owner_entropy = -(owner_probs * torch.log(owner_probs + 1e-8)).sum().item()

    # Family label proxy disagreement
    label_proxy_disagreement = 0.0
    if family_labels is not None:
        # Compare external labels with prototype assignments
        for p in range(num_prototypes):
            mask = prototype_ids == p
            if mask.sum() < 2:
                continue
            labels_in_proto = family_labels[mask]
            unique_labels = labels_in_proto.unique()
            if len(unique_labels) > 1:
                label_proxy_disagreement += 1.0
        label_proxy_disagreement /= max(num_prototypes, 1)

    metrics = {
        "expert_family_purity": float(sum(expert_purity_values) / max(len(expert_purity_values), 1)),
        "expert_family_coverage": float(sum(expert_coverage_values) / max(len(expert_coverage_values), 1)),
        "expert_family_entropy": owner_entropy,
        "prototype_family_owner_consistency": float(sum(proto_owner_consistency) / max(len(proto_owner_consistency), 1)),
        "prototype_local_monopoly_rate": float(sum(proto_monopoly_rates) / max(len(proto_monopoly_rates), 1)),
        "owner_entropy": owner_entropy,
        "family_label_proxy_disagreement_rate": label_proxy_disagreement,
    }
    return metrics


# =============================================================================
# Family Preservation Gate
# =============================================================================


def family_preservation_gate(
    metrics: dict[str, float],
    baseline_metrics: Optional[dict[str, float]] = None,
    owners_per_token: float = 1.0,
    top2_executions: int = 0,
    top4_executions: int = 0,
    unknown_failures: int = 0,
) -> dict[str, Any]:
    """Evaluate family preservation gate.

    Returns verdict and evidence.
    """
    # Hard invariants
    if owners_per_token != 1.0:
        return {"verdict": "PVR_EC_FAMILY_PRESERVATION_BLOCKED",
                "reason": f"owners_per_token={owners_per_token}, must be 1.0"}
    if top2_executions > 0:
        return {"verdict": "PVR_EC_FAMILY_PRESERVATION_BLOCKED",
                "reason": f"Top2_executions={top2_executions}, must be 0"}
    if top4_executions > 0:
        return {"verdict": "PVR_EC_FAMILY_PRESERVATION_BLOCKED",
                "reason": f"Top4_executions={top4_executions}, must be 0"}
    if unknown_failures > 0:
        return {"verdict": "PVR_EC_FAMILY_PRESERVATION_OBSERVATORY_EXPANSION_REQUIRED",
                "reason": f"unknown_failures={unknown_failures}"}

    blockers = []
    monopoly = metrics.get("prototype_local_monopoly_rate", 0.0)
    if monopoly > 0.5:
        blockers.append(f"prototype_local_monopoly_rate={monopoly:.3f} > 0.5")

    purity = metrics.get("expert_family_purity", 0.0)
    entropy = metrics.get("expert_family_entropy", 0.0)
    if purity > 0.95 and entropy < 0.5:
        blockers.append(f"high purity ({purity:.3f}) with low entropy ({entropy:.3f}) suggests collapse")

    if blockers:
        return {
            "verdict": "PVR_EC_FAMILY_PRESERVATION_PASSED_WITH_BLOCKERS",
            "blockers": blockers,
            "metrics": metrics,
        }

    return {
        "verdict": "PVR_EC_FAMILY_PRESERVATION_PASSED",
        "metrics": metrics,
    }
