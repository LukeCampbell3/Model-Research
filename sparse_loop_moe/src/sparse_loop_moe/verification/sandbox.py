"""Sandboxed Modification Layer.

Any self-modification must happen outside the kernel.
All modifications follow: propose → sandbox → evaluate → rollback or commit.
Only validated changes can be promoted into long-term memory.

Allowed to modify:
- fast memory
- task-local state
- temporary adapters
- expert routing preferences
- loop depth
- branch selection
- active assumptions

NOT allowed to modify:
- cognitive kernel
- base safety rules
- core invariants
- permanent priors from a single task
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable
from copy import deepcopy

import torch

from sparse_loop_moe.core.cognitive_kernel import CognitiveKernel
from sparse_loop_moe.core.cognitive_state import CognitiveState


@dataclass
class ModificationProposal:
    """A proposed modification to the system state."""

    target: str  # What to modify
    description: str  # Human-readable description
    old_value: Any = None
    new_value: Any = None
    confidence: float = 0.0
    risk_score: float = 0.0


@dataclass
class SandboxResult:
    """Result of evaluating a modification in sandbox."""

    proposal: ModificationProposal
    approved: bool
    score_before: float = 0.0
    score_after: float = 0.0
    improvement: float = 0.0
    side_effects: list[str] = field(default_factory=list)
    regression_passed: bool = True


class SandboxedModification:
    """Sandboxed modification layer.

    Ensures all modifications are:
    1. Proposed explicitly
    2. Evaluated in isolation
    3. Checked against kernel constraints
    4. Rolled back if harmful
    5. Only committed if validated
    """

    # Targets that are NEVER modifiable
    FORBIDDEN_TARGETS = frozenset(
        {
            "cognitive_kernel",
            "base_safety_rules",
            "core_invariants",
            "permanent_priors",
        }
    )

    # Targets that are allowed
    ALLOWED_TARGETS = frozenset(
        {
            "fast_memory",
            "task_local_state",
            "temporary_adapters",
            "expert_routing_preferences",
            "loop_depth",
            "branch_selection",
            "active_assumptions",
            "cognitive_state",
        }
    )

    def __init__(self, kernel: CognitiveKernel):
        self.kernel = kernel
        self.pending_proposals: list[ModificationProposal] = []
        self.committed_modifications: list[SandboxResult] = []
        self.rollback_stack: list[tuple[str, Any]] = []
        self._evaluators: dict[str, Callable] = {}

    def propose(self, proposal: ModificationProposal) -> bool:
        """Propose a modification. Returns False if immediately rejected."""
        # Check kernel constraints
        if not self.kernel.validate_modification(proposal.target):
            return False

        if proposal.target in self.FORBIDDEN_TARGETS:
            return False

        if proposal.target not in self.ALLOWED_TARGETS:
            return False

        self.pending_proposals.append(proposal)
        return True

    def evaluate_in_sandbox(
        self,
        proposal: ModificationProposal,
        state: CognitiveState,
        score_fn: Callable[[CognitiveState], float],
    ) -> SandboxResult:
        """Evaluate a proposed modification in a sandboxed copy.

        Args:
            proposal: The modification to evaluate
            state: Current cognitive state
            score_fn: Function to score the state quality

        Returns:
            SandboxResult with evaluation outcome
        """
        # Score before
        score_before = score_fn(state)

        # Create sandboxed copy
        sandbox_state = deepcopy(state)

        # Apply modification in sandbox
        try:
            self._apply_modification(sandbox_state, proposal)
        except Exception as e:
            return SandboxResult(
                proposal=proposal,
                approved=False,
                score_before=score_before,
                score_after=score_before,
                improvement=0.0,
                side_effects=[f"Application failed: {str(e)}"],
                regression_passed=False,
            )

        # Score after
        score_after = score_fn(sandbox_state)
        improvement = score_after - score_before

        # Check for regressions
        regression_passed = self._check_regressions(sandbox_state, proposal)

        # Determine approval
        approved = improvement > 0 and regression_passed

        return SandboxResult(
            proposal=proposal,
            approved=approved,
            score_before=score_before,
            score_after=score_after,
            improvement=improvement,
            regression_passed=regression_passed,
        )

    def commit(
        self,
        result: SandboxResult,
        state: CognitiveState,
    ) -> bool:
        """Commit an approved modification to the actual state.

        Returns True if committed, False if rejected.
        """
        if not result.approved:
            return False

        # Save rollback point
        old_value = self._get_current_value(state, result.proposal.target)
        self.rollback_stack.append((result.proposal.target, old_value))

        # Apply to real state
        try:
            self._apply_modification(state, result.proposal)
            self.committed_modifications.append(result)
            return True
        except Exception:
            # Rollback on failure
            self.rollback_last(state)
            return False

    def rollback_last(self, state: CognitiveState) -> bool:
        """Rollback the last committed modification."""
        if not self.rollback_stack:
            return False

        target, old_value = self.rollback_stack.pop()
        self._set_value(state, target, old_value)
        if self.committed_modifications:
            self.committed_modifications.pop()
        return True

    def _apply_modification(
        self, state: CognitiveState, proposal: ModificationProposal
    ) -> None:
        """Apply a modification to a state object."""
        target = proposal.target

        if target == "cognitive_state":
            # Update specific fields
            if isinstance(proposal.new_value, dict):
                for key, val in proposal.new_value.items():
                    if hasattr(state, key):
                        setattr(state, key, val)
        elif target == "active_assumptions":
            state.active_assumptions = proposal.new_value
        elif target == "loop_depth":
            state.max_loops = proposal.new_value
        elif target == "branch_selection":
            state.selected_path = proposal.new_value
        else:
            # Generic attribute setting
            if hasattr(state, target):
                setattr(state, target, proposal.new_value)

    def _get_current_value(self, state: CognitiveState, target: str) -> Any:
        """Get the current value of a target from state."""
        if target == "active_assumptions":
            return deepcopy(state.active_assumptions)
        elif target == "loop_depth":
            return state.max_loops
        elif target == "branch_selection":
            return state.selected_path
        elif hasattr(state, target):
            return deepcopy(getattr(state, target))
        return None

    def _set_value(self, state: CognitiveState, target: str, value: Any) -> None:
        """Set a value on the state."""
        if target == "active_assumptions":
            state.active_assumptions = value
        elif target == "loop_depth":
            state.max_loops = value
        elif target == "branch_selection":
            state.selected_path = value
        elif hasattr(state, target):
            setattr(state, target, value)

    def _check_regressions(
        self, state: CognitiveState, proposal: ModificationProposal
    ) -> bool:
        """Check if a modification causes regressions."""
        # Basic checks
        if state.uncertainty > 0.95:
            return False  # Modification made things too uncertain
        if state.contradiction_score > 0.8:
            return False  # Introduced contradictions

        # Run registered evaluators
        target = proposal.target
        if target in self._evaluators:
            return self._evaluators[target](state)

        return True

    def register_evaluator(
        self, target: str, evaluator: Callable[[CognitiveState], bool]
    ) -> None:
        """Register a custom evaluator for a modification target."""
        self._evaluators[target] = evaluator
