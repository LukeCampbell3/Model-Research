"""Cognitive Kernel: immutable invariants and safety rules.

Analogous to OS kernel space — must not be modified by ordinary learning,
reflection, or task adaptation.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class KernelConstraints:
    """Immutable constraints that govern the system."""

    # Loop safety
    max_loop_depth: int = 16
    max_experts_per_token: int = 6
    min_utility_threshold: float = 0.01
    max_compute_budget_multiplier: float = 4.0

    # Anti-spinlock
    oscillation_window: int = 3
    oscillation_threshold: float = 0.02
    max_consecutive_rollbacks: int = 3

    # Reflection safety
    max_reflection_depth: int = 4
    reflection_must_improve: bool = True
    min_reflection_improvement: float = 0.005

    # Memory safety
    max_fast_memory_slots: int = 64
    max_episodic_entries: int = 1024
    consolidation_threshold: int = 5
    regression_test_required: bool = True

    # Modification safety
    sandbox_required_for_modification: bool = True
    kernel_modification_forbidden: bool = True


class CognitiveKernel:
    """Immutable cognitive kernel — the system's invariant layer.

    Contains base invariants, safety rules, reasoning constraints,
    and architectural assumptions. Cannot be modified by ordinary
    learning, reflection, or task adaptation.
    """

    def __init__(self, constraints: KernelConstraints | None = None):
        self._constraints = constraints or KernelConstraints()
        self._frozen = True

    @property
    def constraints(self) -> KernelConstraints:
        return self._constraints

    def validate_loop_count(self, loop_count: int) -> bool:
        """Check if loop count is within kernel bounds."""
        return loop_count <= self._constraints.max_loop_depth

    def validate_expert_count(self, k: int) -> bool:
        """Check if expert count is within kernel bounds."""
        return 1 <= k <= self._constraints.max_experts_per_token

    def validate_compute_budget(self, used: float, baseline: float) -> bool:
        """Check if compute budget is within kernel bounds."""
        return used <= baseline * self._constraints.max_compute_budget_multiplier

    def check_oscillation(self, deltas: list[float]) -> bool:
        """Detect oscillation in recent loop deltas."""
        window = self._constraints.oscillation_window
        if len(deltas) < window:
            return False
        recent = deltas[-window:]
        # Oscillation: alternating signs with small magnitude
        sign_changes = sum(
            1 for i in range(1, len(recent)) if recent[i] * recent[i - 1] < 0
        )
        avg_magnitude = sum(abs(d) for d in recent) / len(recent)
        return (
            sign_changes >= window - 1
            and avg_magnitude < self._constraints.oscillation_threshold
        )

    def validate_reflection_improvement(
        self, before: float, after: float
    ) -> bool:
        """Check if reflection actually improved the state."""
        if not self._constraints.reflection_must_improve:
            return True
        return (after - before) >= self._constraints.min_reflection_improvement

    def validate_modification(self, target: str) -> bool:
        """Check if a modification target is allowed."""
        forbidden_targets = {
            "cognitive_kernel",
            "base_safety_rules",
            "core_invariants",
            "permanent_priors",
        }
        return target not in forbidden_targets

    def __setattr__(self, name: str, value: Any) -> None:
        if hasattr(self, "_frozen") and self._frozen and name != "_frozen":
            raise AttributeError(
                f"CognitiveKernel is immutable. Cannot modify '{name}'."
            )
        super().__setattr__(name, value)
