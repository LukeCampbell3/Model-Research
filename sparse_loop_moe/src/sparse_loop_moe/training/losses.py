"""Combined loss function for Sparse Loop-MoE training.

L_total = L_task
        + lambda_balance * L_balance
        + lambda_compute * L_compute
        + lambda_probe * L_probe
        + lambda_halt * L_halt
        + lambda_reflection * L_reflection
        + lambda_consistency * L_state_consistency
        + lambda_revision * L_revision_success

Important: Do not reward reflection for its own sake.
Reward reflection only when it improves outcome, reduces risk, or prevents failure.
"""

from __future__ import annotations

from dataclasses import dataclass

import torch
import torch.nn as nn
import torch.nn.functional as F

from sparse_loop_moe.core.types import LoopStats


@dataclass
class LossWeights:
    """Weights for the combined loss function."""

    lambda_balance: float = 0.01
    lambda_compute: float = 0.001
    lambda_probe: float = 0.1
    lambda_halt: float = 0.05
    lambda_reflection: float = 0.05
    lambda_consistency: float = 0.01
    lambda_revision: float = 0.05


class CombinedLoss(nn.Module):
    """Combined loss for Sparse Loop-MoE training.

    Combines task loss with auxiliary losses that train:
    - Load balancing (prevent expert collapse)
    - Compute efficiency (penalize unnecessary loops/experts)
    - Probe accuracy (train risk/failure prediction)
    - Halting behavior (train when to stop)
    - Reflection quality (train metacognitive evaluation)
    - State consistency (prevent contradictory internal states)
    - Revision success (reward useful revisions only)
    """

    def __init__(self, weights: LossWeights | None = None):
        super().__init__()
        self.weights = weights or LossWeights()

    def forward(
        self,
        task_loss: torch.Tensor,
        aux_losses: dict[str, torch.Tensor],
        loop_stats: list[LoopStats],
        probe_targets: torch.Tensor | None = None,
        probe_predictions: torch.Tensor | None = None,
        halt_targets: torch.Tensor | None = None,
        halt_predictions: torch.Tensor | None = None,
        pre_reflection_score: float | None = None,
        post_reflection_score: float | None = None,
    ) -> tuple[torch.Tensor, dict[str, torch.Tensor]]:
        """Compute combined loss.

        Args:
            task_loss: Base task prediction loss
            aux_losses: Auxiliary losses from model forward pass
            loop_stats: Loop statistics from each block
            probe_targets: Ground truth probe signals [N, 10]
            probe_predictions: Predicted probe signals [N, 10]
            halt_targets: Ground truth halt decisions
            halt_predictions: Predicted halt probabilities
            pre_reflection_score: Score before reflection
            post_reflection_score: Score after reflection

        Returns:
            total_loss: Combined scalar loss
            loss_components: Dictionary of individual loss components
        """
        w = self.weights
        components: dict[str, torch.Tensor] = {"task_loss": task_loss}
        total = task_loss.clone()

        # L_balance: load balancing loss (from MoE forward pass)
        if "load_balance_loss" in aux_losses:
            l_balance = aux_losses["load_balance_loss"]
            total = total + w.lambda_balance * l_balance
            components["balance_loss"] = l_balance

        # L_compute: penalize unnecessary compute
        l_compute = self._compute_loss(loop_stats)
        total = total + w.lambda_compute * l_compute
        components["compute_loss"] = l_compute

        # L_probe: train probe heads
        if probe_targets is not None and probe_predictions is not None:
            l_probe = F.binary_cross_entropy(probe_predictions, probe_targets)
            total = total + w.lambda_probe * l_probe
            components["probe_loss"] = l_probe

        # L_halt: train halting behavior
        if halt_targets is not None and halt_predictions is not None:
            l_halt = F.binary_cross_entropy(halt_predictions, halt_targets)
            total = total + w.lambda_halt * l_halt
            components["halt_loss"] = l_halt

        # L_reflection: reward reflection only when it helps
        if pre_reflection_score is not None and post_reflection_score is not None:
            l_reflection = self._reflection_loss(
                pre_reflection_score, post_reflection_score
            )
            total = total + w.lambda_reflection * l_reflection
            components["reflection_loss"] = l_reflection

        # L_state_consistency: penalize contradictory states
        l_consistency = self._consistency_loss(loop_stats)
        total = total + w.lambda_consistency * l_consistency
        components["consistency_loss"] = l_consistency

        components["total_loss"] = total
        return total, components

    def _compute_loss(self, loop_stats: list[LoopStats]) -> torch.Tensor:
        """Penalize unnecessary loops and expert usage.

        Compute cost = sum of (loops_used * avg_experts_per_loop) across blocks.
        Normalized by maximum possible compute.
        """
        total_compute = 0.0
        max_compute = 0.0

        for stats in loop_stats:
            loops = stats.loops_used
            if stats.experts_used_per_loop:
                avg_experts = sum(stats.experts_used_per_loop) / len(
                    stats.experts_used_per_loop
                )
            else:
                avg_experts = 1.0
            total_compute += loops * avg_experts
            max_compute += 8 * 4  # max_loops * max_k (upper bound)

        # Normalized compute cost
        compute_ratio = total_compute / max(max_compute, 1.0)
        return torch.tensor(compute_ratio, requires_grad=True)

    def _reflection_loss(
        self, pre_score: float, post_score: float
    ) -> torch.Tensor:
        """Penalize reflection that doesn't improve outcome.

        reflection_value = (post - pre) / compute_used
        If negative, penalize. If positive, reward.
        """
        improvement = post_score - pre_score
        # Penalize negative improvement (reflection made things worse)
        if improvement < 0:
            return torch.tensor(abs(improvement), requires_grad=True)
        else:
            # Small reward for useful reflection (negative loss)
            return torch.tensor(-improvement * 0.5, requires_grad=True)

    def _consistency_loss(self, loop_stats: list[LoopStats]) -> torch.Tensor:
        """Penalize oscillation and inconsistent state transitions."""
        oscillation_penalty = 0.0
        for stats in loop_stats:
            if stats.oscillation_detected:
                oscillation_penalty += 1.0
            # Penalize excessive rollbacks
            oscillation_penalty += stats.rollback_count * 0.1

        return torch.tensor(
            oscillation_penalty / max(len(loop_stats), 1), requires_grad=True
        )
