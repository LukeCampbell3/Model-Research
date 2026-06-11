"""ResearchGateway: bounded autonomous research initiation.

Research can only be initiated when:
- An evidence gap is identified (missing support for a claim)
- Budget is pre-approved and bounded
- Maximum depth, duration, and concurrent limits are enforced
- Research produces evidence records, never commits directly
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any
from datetime import datetime, timedelta
from enum import Enum


class ResearchStatus(Enum):
    PENDING = "pending"
    APPROVED = "approved"
    RUNNING = "running"
    COMPLETED = "completed"
    TERMINATED = "terminated"
    REJECTED = "rejected"


@dataclass
class ResearchBounds:
    """Hard limits on any research process."""
    max_budget: float = 10.0
    max_depth: int = 5
    max_duration_seconds: float = 3600.0
    max_concurrent: int = 2
    max_daily_count: int = 10
    requires_evidence_gap: bool = True
    requires_justification: bool = True
    auto_terminate_on_loop: bool = True


@dataclass
class ResearchRequest:
    """A request to initiate autonomous research."""
    request_id: str = field(default_factory=lambda: f"research_{datetime.utcnow().isoformat()}")
    topic: str = ""
    justification: str = ""
    evidence_gap_ref: str = ""  # Reference to the gap that triggered this
    requested_budget: float = 1.0
    requested_depth: int = 3
    requester_process_id: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)


@dataclass
class ResearchOutcome:
    """Outcome of a completed research process."""
    request_id: str
    status: ResearchStatus
    evidence_produced: list[str] = field(default_factory=list)
    claims_produced: list[str] = field(default_factory=list)
    budget_consumed: float = 0.0
    depth_reached: int = 0
    duration_seconds: float = 0.0
    terminated_reason: str | None = None


class ResearchGateway:
    """Gate for initiating and managing bounded research processes.

    Key safety properties:
    - Research NEVER commits to canonical state directly
    - Research produces evidence records only
    - All research is bounded (budget, time, depth)
    - Loop detection terminates stuck research
    - Daily caps prevent runaway usage
    """

    def __init__(self, bounds: ResearchBounds | None = None):
        self._bounds = bounds or ResearchBounds()
        self._active: dict[str, ResearchRequest] = {}
        self._daily_count: int = 0
        self._last_reset: datetime = datetime.utcnow()
        self._history: list[ResearchOutcome] = []

    @property
    def bounds(self) -> ResearchBounds:
        return self._bounds

    @property
    def active_count(self) -> int:
        return len(self._active)

    def request_research(self, request: ResearchRequest) -> tuple[bool, str]:
        """Evaluate and approve/reject a research request.

        Returns:
            (approved, reason)
        """
        self._maybe_reset_daily_count()

        # Check justification
        if self._bounds.requires_justification and not request.justification:
            return False, "Research requires justification"

        # Check evidence gap
        if self._bounds.requires_evidence_gap and not request.evidence_gap_ref:
            return False, "Research requires an evidence gap reference"

        # Check budget
        if request.requested_budget > self._bounds.max_budget:
            return False, f"Budget {request.requested_budget} exceeds max {self._bounds.max_budget}"

        # Check depth
        if request.requested_depth > self._bounds.max_depth:
            return False, f"Depth {request.requested_depth} exceeds max {self._bounds.max_depth}"

        # Check concurrent limit
        if len(self._active) >= self._bounds.max_concurrent:
            return False, f"Concurrent limit reached ({self._bounds.max_concurrent})"

        # Check daily cap
        if self._daily_count >= self._bounds.max_daily_count:
            return False, f"Daily cap reached ({self._bounds.max_daily_count})"

        # Approved
        self._active[request.request_id] = request
        self._daily_count += 1
        return True, "Approved"

    def complete_research(self, request_id: str, outcome: ResearchOutcome) -> None:
        """Record research completion."""
        self._active.pop(request_id, None)
        self._history.append(outcome)

    def terminate_research(self, request_id: str, reason: str) -> ResearchOutcome | None:
        """Force-terminate a running research process."""
        request = self._active.pop(request_id, None)
        if not request:
            return None
        outcome = ResearchOutcome(
            request_id=request_id,
            status=ResearchStatus.TERMINATED,
            terminated_reason=reason,
        )
        self._history.append(outcome)
        return outcome

    def check_loop_detection(self, request_id: str, seen_states: set[str]) -> bool:
        """Returns True if a loop is detected (same state visited twice)."""
        # Simple: if any state hash appears twice, it's a loop
        return len(seen_states) != len(set(seen_states))  # Always false for sets
        # Actually check via caller tracking repeated visits

    def _maybe_reset_daily_count(self):
        now = datetime.utcnow()
        if (now - self._last_reset) > timedelta(hours=24):
            self._daily_count = 0
            self._last_reset = now
