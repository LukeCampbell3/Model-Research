"""EvidencePacket v2: structured evidence with provenance chains.

Extends the flat EvidenceRecord with:
- Full provenance chain (which process produced which evidence)
- Confidence decay over time
- Cross-reference integrity
- Strength-of-evidence scoring
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any
from datetime import datetime


@dataclass
class ProvenanceNode:
    """Single node in a provenance chain."""
    process_id: str
    state_hash: str
    timestamp: datetime = field(default_factory=datetime.utcnow)
    action: str = "produced"  # produced, verified, contradicted, extended
    confidence: float = 1.0


@dataclass
class ProvenanceChain:
    """Full provenance chain for a piece of evidence."""
    nodes: list[ProvenanceNode] = field(default_factory=list)

    @property
    def origin_process(self) -> str | None:
        return self.nodes[0].process_id if self.nodes else None

    @property
    def latest_verifier(self) -> str | None:
        for node in reversed(self.nodes):
            if node.action == "verified":
                return node.process_id
        return None

    @property
    def chain_length(self) -> int:
        return len(self.nodes)

    @property
    def min_confidence(self) -> float:
        if not self.nodes:
            return 0.0
        return min(n.confidence for n in self.nodes)

    def add_node(self, node: ProvenanceNode) -> None:
        self.nodes.append(node)

    @property
    def is_contradicted(self) -> bool:
        return any(n.action == "contradicted" for n in self.nodes)


@dataclass
class EvidencePacket:
    """Structured evidence with provenance, confidence, and cross-references.

    EvidencePacket wraps an evidence_id and adds rich metadata without
    replacing the underlying EvidenceLedger entry.
    """
    evidence_id: str
    provenance: ProvenanceChain = field(default_factory=ProvenanceChain)
    confidence_score: float = 1.0
    strength: float = 1.0  # How strong this evidence is (0-1)
    cross_references: list[str] = field(default_factory=list)  # Other evidence_ids
    supporting_claims: list[str] = field(default_factory=list)
    contradicting_claims: list[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.utcnow)
    last_accessed: datetime = field(default_factory=datetime.utcnow)
    access_count: int = 0

    @property
    def is_stale(self) -> bool:
        """Evidence older than 24h without access is stale."""
        from datetime import timedelta
        return (datetime.utcnow() - self.last_accessed) > timedelta(hours=24)

    @property
    def effective_confidence(self) -> float:
        """Confidence after considering provenance chain."""
        return self.confidence_score * self.provenance.min_confidence

    def record_access(self) -> None:
        self.access_count += 1
        self.last_accessed = datetime.utcnow()

    def is_valid_for_commit(self) -> bool:
        """Check if this evidence is strong enough to support a commit."""
        return (
            self.effective_confidence >= 0.5 and
            not self.provenance.is_contradicted and
            self.strength >= 0.3
        )
