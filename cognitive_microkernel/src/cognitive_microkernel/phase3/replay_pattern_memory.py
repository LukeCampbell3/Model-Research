"""ReplayPatternMemory: learn patterns from successful replay traces.

Extracts reusable patterns from completed process chains:
- Which branch hypotheses led to successful commits
- Which expert routing paths were efficient
- Which evidence types were most reliable
- Which conflict resolutions worked

Patterns are read-only advisors — they inform scoring but don't control commits.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any
from datetime import datetime


@dataclass
class ReplayPattern:
    """A learned pattern from replay traces."""
    pattern_id: str
    pattern_type: str  # "branch_success", "routing_efficiency", "evidence_reliability"
    hypothesis_keywords: list[str] = field(default_factory=list)
    success_rate: float = 0.0
    sample_count: int = 0
    avg_cost: float = 0.0
    avg_depth: int = 0
    last_observed: datetime = field(default_factory=datetime.utcnow)
    confidence: float = 0.0

    @property
    def is_reliable(self) -> bool:
        """Pattern is reliable if enough samples and high success rate."""
        return self.sample_count >= 5 and self.success_rate >= 0.6


class ReplayPatternMemory:
    """Accumulate and query patterns from replay traces.

    This memory is ADVISORY only — it informs branch scoring and context
    selection but cannot commit state or override verification gates.
    """

    def __init__(self, max_patterns: int = 1000, min_samples_for_confidence: int = 5):
        self._patterns: dict[str, ReplayPattern] = {}
        self._max_patterns = max_patterns
        self._min_samples = min_samples_for_confidence

    @property
    def pattern_count(self) -> int:
        return len(self._patterns)

    def record_outcome(self, hypothesis_keywords: list[str], success: bool,
                       cost: float = 0.0, depth: int = 0, pattern_type: str = "branch_success") -> None:
        """Record an outcome from a completed replay trace."""
        key = self._make_key(hypothesis_keywords, pattern_type)

        if key not in self._patterns:
            if len(self._patterns) >= self._max_patterns:
                self._evict_oldest()
            self._patterns[key] = ReplayPattern(
                pattern_id=key, pattern_type=pattern_type,
                hypothesis_keywords=hypothesis_keywords,
            )

        pattern = self._patterns[key]
        # Update running stats
        n = pattern.sample_count
        pattern.success_rate = (pattern.success_rate * n + (1.0 if success else 0.0)) / (n + 1)
        pattern.avg_cost = (pattern.avg_cost * n + cost) / (n + 1)
        pattern.avg_depth = int((pattern.avg_depth * n + depth) / (n + 1))
        pattern.sample_count = n + 1
        pattern.last_observed = datetime.utcnow()
        pattern.confidence = min(pattern.sample_count / self._min_samples, 1.0)

    def query_relevance(self, hypothesis_keywords: list[str], pattern_type: str = "branch_success") -> ReplayPattern | None:
        """Query for a relevant pattern."""
        key = self._make_key(hypothesis_keywords, pattern_type)
        return self._patterns.get(key)

    def get_top_patterns(self, n: int = 10) -> list[ReplayPattern]:
        """Get top N patterns by success rate (with min samples)."""
        reliable = [p for p in self._patterns.values() if p.is_reliable]
        reliable.sort(key=lambda p: p.success_rate, reverse=True)
        return reliable[:n]

    def _make_key(self, keywords: list[str], pattern_type: str) -> str:
        sorted_kw = sorted(set(k.lower() for k in keywords))
        return f"{pattern_type}:{'_'.join(sorted_kw[:5])}"

    def _evict_oldest(self) -> None:
        if not self._patterns:
            return
        oldest_key = min(self._patterns, key=lambda k: self._patterns[k].last_observed)
        del self._patterns[oldest_key]
