"""ContextCompiler: compile context pages for expert inputs.

Selects and organizes context (evidence, claims, artifacts) into a
budget-limited page for expert consumption. Prioritizes by relevance
and recency.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any


@dataclass
class ContextBudget:
    """Budget constraints for context compilation."""
    max_tokens: int = 2000
    max_evidence_refs: int = 10
    max_claim_refs: int = 10
    max_artifact_refs: int = 5
    prefer_recent: bool = True
    prefer_supported: bool = True


@dataclass
class ContextPage:
    """A compiled context page ready for expert consumption."""
    evidence_refs: list[str] = field(default_factory=list)
    claim_refs: list[str] = field(default_factory=list)
    artifact_refs: list[str] = field(default_factory=list)
    summary: str = ""
    estimated_tokens: int = 0
    budget_used_ratio: float = 0.0
    relevance_scores: dict[str, float] = field(default_factory=dict)

    @property
    def is_within_budget(self) -> bool:
        return self.budget_used_ratio <= 1.0

    @property
    def total_refs(self) -> int:
        return len(self.evidence_refs) + len(self.claim_refs) + len(self.artifact_refs)


class ContextCompiler:
    """Compile relevant context within budget for expert inputs.

    This is a read-only operation — it queries evidence/claims but
    does not modify state.
    """

    def __init__(self, budget: ContextBudget | None = None):
        self._budget = budget or ContextBudget()

    def compile(self, available_evidence: list[str], available_claims: list[str],
                available_artifacts: list[str], relevance_fn=None) -> ContextPage:
        """Compile a context page from available references.

        Args:
            available_evidence: Evidence IDs to consider
            available_claims: Claim IDs to consider
            available_artifacts: Artifact hashes to consider
            relevance_fn: Optional callable(ref_id) -> float for scoring
        """
        # Score and rank
        scored_ev = self._score_refs(available_evidence, relevance_fn)
        scored_claims = self._score_refs(available_claims, relevance_fn)
        scored_arts = self._score_refs(available_artifacts, relevance_fn)

        # Select within budget
        selected_ev = scored_ev[:self._budget.max_evidence_refs]
        selected_claims = scored_claims[:self._budget.max_claim_refs]
        selected_arts = scored_arts[:self._budget.max_artifact_refs]

        # Estimate tokens (rough: 50 tokens per reference)
        est_tokens = (len(selected_ev) + len(selected_claims) + len(selected_arts)) * 50

        page = ContextPage(
            evidence_refs=[ref for ref, _ in selected_ev],
            claim_refs=[ref for ref, _ in selected_claims],
            artifact_refs=[ref for ref, _ in selected_arts],
            estimated_tokens=est_tokens,
            budget_used_ratio=est_tokens / max(self._budget.max_tokens, 1),
            relevance_scores={ref: score for ref, score in scored_ev + scored_claims + scored_arts},
        )
        return page

    def _score_refs(self, refs: list[str], relevance_fn=None) -> list[tuple[str, float]]:
        """Score and sort references by relevance."""
        if relevance_fn:
            scored = [(ref, relevance_fn(ref)) for ref in refs]
        else:
            # Default: later refs are more recent = more relevant
            scored = [(ref, (i + 1) / len(refs)) for i, ref in enumerate(refs)] if refs else []
        scored.sort(key=lambda x: x[1], reverse=True)
        return scored
