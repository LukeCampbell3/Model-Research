"""Core type definitions for the Sparse Loop-MoE system."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Optional

import torch


class ReflectionAction(Enum):
    """Actions the reflection controller can take."""

    HALT = auto()
    CONTINUE = auto()
    ADD_EXPERT = auto()
    SWITCH_EXPERT = auto()
    RUN_PROBE = auto()
    RUN_COUNTERFACTUAL = auto()
    CHECK_ASSUMPTIONS = auto()
    REQUEST_RETRIEVAL = auto()
    VALIDATE = auto()
    REVISE_STATE = auto()
    ROLLBACK = auto()


@dataclass
class ProbeSignals:
    """Signals from latent probe heads."""

    failure_risk: float = 0.0
    missing_context: float = 0.0
    coverage_gap: float = 0.0
    validation_fail_probability: float = 0.0
    route_confidence: float = 0.0
    hidden_constraint_probability: float = 0.0
    false_commitment_risk: float = 0.0
    representation_drift: float = 0.0
    novelty_score: float = 0.0
    memory_relevance: float = 0.0

    def to_tensor(self) -> torch.Tensor:
        """Convert probe signals to a tensor."""
        return torch.tensor(
            [
                self.failure_risk,
                self.missing_context,
                self.coverage_gap,
                self.validation_fail_probability,
                self.route_confidence,
                self.hidden_constraint_probability,
                self.false_commitment_risk,
                self.representation_drift,
                self.novelty_score,
                self.memory_relevance,
            ],
            dtype=torch.float32,
        )

    @classmethod
    def from_tensor(cls, t: torch.Tensor) -> "ProbeSignals":
        """Create ProbeSignals from a tensor."""
        values = t.detach().cpu().tolist()
        return cls(
            failure_risk=values[0],
            missing_context=values[1],
            coverage_gap=values[2],
            validation_fail_probability=values[3],
            route_confidence=values[4],
            hidden_constraint_probability=values[5],
            false_commitment_risk=values[6],
            representation_drift=values[7],
            novelty_score=values[8],
            memory_relevance=values[9],
        )


@dataclass
class LoopStats:
    """Statistics from a single loop execution."""

    loops_used: int = 0
    halted_early: bool = False
    halt_reason: str = ""
    experts_used_per_loop: list[int] = field(default_factory=list)
    delta_per_loop: list[float] = field(default_factory=list)
    probe_signals_per_loop: list[ProbeSignals] = field(default_factory=list)
    actions_taken: list[ReflectionAction] = field(default_factory=list)
    rollback_count: int = 0
    oscillation_detected: bool = False
    compute_budget_exhausted: bool = False
    best_state_loop: int = 0
    utility_per_loop: list[float] = field(default_factory=list)


@dataclass
class RouterMetrics:
    """Metrics from the expert router."""

    routing_entropy: float = 0.0
    expert_utilization: list[float] = field(default_factory=list)
    dead_expert_count: int = 0
    load_imbalance: float = 0.0
    expert_overlap: float = 0.0
    route_regret: float = 0.0
    selected_k: int = 0


@dataclass
class ComputeMetrics:
    """Compute cost metrics."""

    flops_estimate: float = 0.0
    active_experts_per_token: float = 0.0
    loops_per_sample: float = 0.0
    quality_per_compute: float = 0.0
