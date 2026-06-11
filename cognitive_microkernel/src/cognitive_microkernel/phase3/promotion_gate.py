"""PromotionGate: evidence-gated capability upgrades.

Controls when policies, memory, or experts can be promoted from
shadow/candidate to active. Requires evidence of improvement.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any
from enum import Enum
from datetime import datetime


class PromotionVerdict(Enum):
    APPROVED = "approved"
    REJECTED_INSUFFICIENT_EVIDENCE = "rejected_insufficient_evidence"
    REJECTED_REGRESSION = "rejected_regression"
    REJECTED_TOO_EARLY = "rejected_too_early"
    DEFERRED = "deferred"


@dataclass
class PromotionRequest:
    """Request to promote a capability."""
    request_id: str = ""
    capability_type: str = ""  # "policy", "memory", "expert", "research"
    capability_id: str = ""
    evidence_refs: list[str] = field(default_factory=list)
    improvement_metric: float = 0.0
    baseline_metric: float = 0.0
    sample_count: int = 0
    created_at: datetime = field(default_factory=datetime.utcnow)


class PromotionGate:
    """Gate evidence-backed promotions.

    Does NOT mutate state. Produces verdicts that the runtime
    can choose to act on (or not).
    """

    def __init__(self, min_samples: int = 50, min_improvement: float = 0.05,
                 min_age_hours: float = 24.0, require_no_regression: bool = True):
        self._min_samples = min_samples
        self._min_improvement = min_improvement
        self._min_age_hours = min_age_hours
        self._require_no_regression = require_no_regression
        self._history: list[tuple[PromotionRequest, PromotionVerdict]] = []

    def evaluate(self, request: PromotionRequest) -> PromotionVerdict:
        """Evaluate a promotion request."""
        # Check sample count
        if request.sample_count < self._min_samples:
            verdict = PromotionVerdict.REJECTED_INSUFFICIENT_EVIDENCE
        # Check age
        elif (datetime.utcnow() - request.created_at).total_seconds() < self._min_age_hours * 3600:
            verdict = PromotionVerdict.REJECTED_TOO_EARLY
        # Check regression
        elif self._require_no_regression and request.improvement_metric < request.baseline_metric:
            verdict = PromotionVerdict.REJECTED_REGRESSION
        # Check improvement threshold
        elif (request.improvement_metric - request.baseline_metric) < self._min_improvement:
            verdict = PromotionVerdict.DEFERRED
        else:
            verdict = PromotionVerdict.APPROVED

        self._history.append((request, verdict))
        return verdict

    @property
    def approval_count(self) -> int:
        return sum(1 for _, v in self._history if v == PromotionVerdict.APPROVED)

    @property
    def rejection_count(self) -> int:
        return sum(1 for _, v in self._history if v != PromotionVerdict.APPROVED)
