"""Cognitive State: structured internal representation for each task.

The model reflects on this representation, not only on the final answer.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Optional

import torch


@dataclass
class CognitiveState:
    """Structured internal state object for each task.

    This is the Representation State Layer — maintains all the structured
    information the model uses for metacognitive reasoning.
    """

    # Task understanding
    task_goal: str = ""
    known_constraints: list[str] = field(default_factory=list)
    unknown_constraints: list[str] = field(default_factory=list)
    active_assumptions: list[str] = field(default_factory=list)

    # Path selection
    candidate_paths: list[str] = field(default_factory=list)
    selected_path: str = ""

    # Uncertainty and risk signals (scalar scores 0-1)
    uncertainty: float = 0.5
    ambiguity: float = 0.5
    expected_risk: float = 0.5
    missing_context_score: float = 0.5
    contradiction_score: float = 0.0
    abstraction_gap: float = 0.5
    route_regret: float = 0.0

    # Control signals
    validation_required: bool = False
    confidence_surface: float = 0.5

    # Memory links
    memory_links: list[str] = field(default_factory=list)

    # Internal tensor state (hidden representation)
    hidden_state: Optional[torch.Tensor] = None
    best_hidden_state: Optional[torch.Tensor] = None
    best_state_score: float = float("-inf")

    # Loop tracking
    loop_count: int = 0
    max_loops: int = 8

    def compute_need(
        self,
        alpha: float = 0.3,
        beta: float = 0.25,
        gamma: float = 0.2,
        delta: float = 0.15,
        epsilon: float = 0.1,
    ) -> float:
        """Compute the adaptive compute need score.

        compute_need = alpha * uncertainty + beta * ambiguity
                     + gamma * expected_risk + delta * missing_context_score
                     + epsilon * abstraction_gap
        """
        return (
            alpha * self.uncertainty
            + beta * self.ambiguity
            + gamma * self.expected_risk
            + delta * self.missing_context_score
            + epsilon * self.abstraction_gap
        )

    def to_tensor(self) -> torch.Tensor:
        """Convert scalar state signals to a tensor for neural processing."""
        return torch.tensor(
            [
                self.uncertainty,
                self.ambiguity,
                self.expected_risk,
                self.missing_context_score,
                self.contradiction_score,
                self.abstraction_gap,
                self.route_regret,
                self.confidence_surface,
                float(self.validation_required),
                self.loop_count / max(self.max_loops, 1),
            ],
            dtype=torch.float32,
        )

    def update_from_tensor(self, t: torch.Tensor) -> None:
        """Update scalar state signals from a tensor."""
        values = t.detach().cpu().tolist()
        self.uncertainty = values[0]
        self.ambiguity = values[1]
        self.expected_risk = values[2]
        self.missing_context_score = values[3]
        self.contradiction_score = values[4]
        self.abstraction_gap = values[5]
        self.route_regret = values[6]
        self.confidence_surface = values[7]
        self.validation_required = values[8] > 0.5

    def snapshot(self) -> dict[str, Any]:
        """Create a serializable snapshot of the state."""
        return {
            "uncertainty": self.uncertainty,
            "ambiguity": self.ambiguity,
            "expected_risk": self.expected_risk,
            "missing_context_score": self.missing_context_score,
            "contradiction_score": self.contradiction_score,
            "abstraction_gap": self.abstraction_gap,
            "route_regret": self.route_regret,
            "confidence_surface": self.confidence_surface,
            "validation_required": self.validation_required,
            "loop_count": self.loop_count,
        }
