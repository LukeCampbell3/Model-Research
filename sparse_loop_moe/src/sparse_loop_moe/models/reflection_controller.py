"""Phase 6: Self-Reflection Controller.

Metacognitive controller that evaluates internal state quality and
decides whether to halt, continue, add experts, rollback, etc.

This is NOT merely an answer critic — it evaluates the internal
task representation itself.
"""

from __future__ import annotations

import torch
import torch.nn as nn
import torch.nn.functional as F

from sparse_loop_moe.core.types import ProbeSignals, ReflectionAction
from sparse_loop_moe.core.cognitive_state import CognitiveState


class ReflectionHeads(nn.Module):
    """Individual reflection assessment heads.

    Each head evaluates a specific metacognitive dimension:
    - state_completeness: Is the internal task representation complete?
    - assumption_risk: Are active assumptions risky?
    - early_commitment: Did the model commit too early?
    - contradiction: Is there a contradiction in current state?
    - domain_mismatch: Are the active experts appropriate?
    - abstraction_gap: Is the abstraction level appropriate?
    - route_regret: Should a different route have been taken?
    - revision_need: Is revision likely to help?
    - validation_need: Should output be validated before committing?
    """

    NUM_HEADS = 9

    def __init__(self, d_input: int, d_hidden: int = 64):
        super().__init__()
        self.shared = nn.Sequential(
            nn.Linear(d_input, d_hidden),
            nn.GELU(),
        )
        self.state_completeness = nn.Linear(d_hidden, 1)
        self.assumption_risk = nn.Linear(d_hidden, 1)
        self.early_commitment = nn.Linear(d_hidden, 1)
        self.contradiction = nn.Linear(d_hidden, 1)
        self.domain_mismatch = nn.Linear(d_hidden, 1)
        self.abstraction_gap = nn.Linear(d_hidden, 1)
        self.route_regret = nn.Linear(d_hidden, 1)
        self.revision_need = nn.Linear(d_hidden, 1)
        self.validation_need = nn.Linear(d_hidden, 1)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Compute reflection head outputs.

        Args:
            x: Combined state vector [d_input]

        Returns:
            Reflection scores [9] (each in [0, 1])
        """
        features = self.shared(x)
        return torch.cat(
            [
                torch.sigmoid(self.state_completeness(features)),
                torch.sigmoid(self.assumption_risk(features)),
                torch.sigmoid(self.early_commitment(features)),
                torch.sigmoid(self.contradiction(features)),
                torch.sigmoid(self.domain_mismatch(features)),
                torch.sigmoid(self.abstraction_gap(features)),
                torch.sigmoid(self.route_regret(features)),
                torch.sigmoid(self.revision_need(features)),
                torch.sigmoid(self.validation_need(features)),
            ],
            dim=-1,
        )


class ReflectionController(nn.Module):
    """Self-reflection metacognitive controller.

    Combines:
    - Hidden state information
    - Cognitive state signals
    - Probe signals
    - Reflection head assessments
    - Loop history

    To decide an action from ReflectionAction enum.
    """

    NUM_ACTIONS = len(ReflectionAction)

    def __init__(
        self,
        d_model: int,
        num_probe_signals: int = 10,
        num_cognitive_signals: int = 10,
        d_hidden: int = 128,
    ):
        super().__init__()
        self.d_model = d_model

        # Input: pooled hidden state + probe signals + cognitive state + loop info
        d_input = d_model + num_probe_signals + num_cognitive_signals + 4  # +4 for loop stats

        # Reflection heads
        self.reflection_heads = ReflectionHeads(d_input, d_hidden)

        # Action policy network
        # Input: reflection head outputs + probe signals + cognitive state
        d_policy_input = ReflectionHeads.NUM_HEADS + num_probe_signals + num_cognitive_signals + 4
        self.action_policy = nn.Sequential(
            nn.Linear(d_policy_input, d_hidden),
            nn.GELU(),
            nn.Linear(d_hidden, d_hidden // 2),
            nn.GELU(),
            nn.Linear(d_hidden // 2, self.NUM_ACTIONS),
        )

        # Halting head (separate, for direct halt probability)
        self.halt_head = nn.Sequential(
            nn.Linear(d_policy_input, d_hidden // 2),
            nn.GELU(),
            nn.Linear(d_hidden // 2, 1),
            nn.Sigmoid(),
        )

        # Utility estimator (predicts marginal utility of continuing)
        self.utility_head = nn.Sequential(
            nn.Linear(d_policy_input, d_hidden // 2),
            nn.GELU(),
            nn.Linear(d_hidden // 2, 1),
        )

    def forward(
        self,
        hidden_state: torch.Tensor,
        probe_signals: ProbeSignals,
        cognitive_state: CognitiveState,
        loop_count: int,
        max_loops: int,
        recent_deltas: list[float],
    ) -> tuple[ReflectionAction, float, float, torch.Tensor]:
        """Decide the next action based on all available signals.

        Args:
            hidden_state: Current hidden state [batch, seq, d_model] or [d_model]
            probe_signals: Current probe signals
            cognitive_state: Current cognitive state
            loop_count: Current loop iteration
            max_loops: Maximum allowed loops
            recent_deltas: Recent improvement deltas

        Returns:
            action: Selected ReflectionAction
            halt_prob: Probability of halting
            utility: Estimated marginal utility of continuing
            reflection_scores: Raw reflection head outputs [9]
        """
        # Pool hidden state
        if hidden_state.dim() == 3:
            pooled_hidden = hidden_state.mean(dim=(0, 1))  # [d_model]
        elif hidden_state.dim() == 2:
            pooled_hidden = hidden_state.mean(dim=0)  # [d_model]
        else:
            pooled_hidden = hidden_state  # [d_model]

        # Build combined input
        probe_tensor = probe_signals.to_tensor().to(pooled_hidden.device)
        cognitive_tensor = cognitive_state.to_tensor().to(pooled_hidden.device)
        loop_info = torch.tensor(
            [
                loop_count / max(max_loops, 1),
                len(recent_deltas) / max(max_loops, 1),
                sum(recent_deltas[-3:]) / max(len(recent_deltas[-3:]), 1) if recent_deltas else 0.0,
                1.0 if loop_count >= max_loops - 1 else 0.0,
            ],
            device=pooled_hidden.device,
            dtype=torch.float32,
        )

        combined_input = torch.cat(
            [pooled_hidden, probe_tensor, cognitive_tensor, loop_info], dim=-1
        )

        # Compute reflection head assessments
        reflection_scores = self.reflection_heads(combined_input)

        # Build policy input
        policy_input = torch.cat(
            [reflection_scores, probe_tensor, cognitive_tensor, loop_info], dim=-1
        )

        # Compute action logits, halt probability, and utility
        action_logits = self.action_policy(policy_input)
        halt_prob = self.halt_head(policy_input).squeeze(-1)
        utility = self.utility_head(policy_input).squeeze(-1)

        # Select action
        action_idx = action_logits.argmax().item()
        action = list(ReflectionAction)[action_idx]

        # Override with HALT if halt probability is high
        if halt_prob.item() > 0.8:
            action = ReflectionAction.HALT

        return action, halt_prob.item(), utility.item(), reflection_scores

    def compute_reflection_loss(
        self,
        action_logits: torch.Tensor,
        target_action: ReflectionAction,
        halt_prob: torch.Tensor,
        should_halt: bool,
        utility: torch.Tensor,
        actual_utility: float,
    ) -> torch.Tensor:
        """Compute reflection training loss.

        Only rewards reflection when it improves outcome.
        """
        # Action classification loss
        target_idx = list(ReflectionAction).index(target_action)
        action_loss = F.cross_entropy(
            action_logits.unsqueeze(0),
            torch.tensor([target_idx], device=action_logits.device),
        )

        # Halt prediction loss
        halt_target = torch.tensor(
            [1.0 if should_halt else 0.0], device=halt_prob.device
        )
        halt_loss = F.binary_cross_entropy(halt_prob.unsqueeze(0), halt_target)

        # Utility prediction loss
        utility_target = torch.tensor([actual_utility], device=utility.device)
        utility_loss = F.mse_loss(utility.unsqueeze(0), utility_target)

        return action_loss + halt_loss + utility_loss
