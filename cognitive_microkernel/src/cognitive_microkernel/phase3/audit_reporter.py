"""RuntimeAuditReporter: structured audit trail generation.

Produces machine-readable audit events for every significant
runtime decision. Enables post-hoc analysis and compliance.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any
from datetime import datetime
from enum import Enum


class AuditSeverity(Enum):
    INFO = "info"
    WARNING = "warning"
    CRITICAL = "critical"
    SECURITY = "security"


@dataclass
class AuditEvent:
    """A single audit event."""
    event_id: str = field(default_factory=lambda: f"audit_{datetime.utcnow().isoformat()}")
    timestamp: datetime = field(default_factory=datetime.utcnow)
    severity: AuditSeverity = AuditSeverity.INFO
    category: str = ""  # "commit", "research", "promotion", "injection", "rollback"
    actor: str = ""  # process_id or system component
    action: str = ""
    target: str = ""
    outcome: str = ""  # "success", "blocked", "failed"
    evidence_refs: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class AuditReport:
    """A collection of audit events with summary."""
    events: list[AuditEvent] = field(default_factory=list)
    start_time: datetime = field(default_factory=datetime.utcnow)
    end_time: datetime | None = None

    @property
    def event_count(self) -> int:
        return len(self.events)

    @property
    def security_events(self) -> list[AuditEvent]:
        return [e for e in self.events if e.severity == AuditSeverity.SECURITY]

    @property
    def critical_events(self) -> list[AuditEvent]:
        return [e for e in self.events if e.severity == AuditSeverity.CRITICAL]

    def summary(self) -> dict[str, Any]:
        severity_counts = {}
        category_counts = {}
        for e in self.events:
            severity_counts[e.severity.value] = severity_counts.get(e.severity.value, 0) + 1
            category_counts[e.category] = category_counts.get(e.category, 0) + 1
        return {
            "total_events": self.event_count,
            "severity_distribution": severity_counts,
            "category_distribution": category_counts,
            "security_event_count": len(self.security_events),
            "critical_event_count": len(self.critical_events),
        }


class RuntimeAuditReporter:
    """Collect and report audit events.

    Read-only observer — does not affect execution flow.
    """

    def __init__(self, max_events: int = 10000):
        self._events: list[AuditEvent] = []
        self._max_events = max_events

    def record(self, event: AuditEvent) -> None:
        """Record an audit event."""
        if len(self._events) >= self._max_events:
            self._events.pop(0)  # FIFO eviction
        self._events.append(event)

    def record_commit(self, process_id: str, state_hash: str, success: bool) -> None:
        self.record(AuditEvent(
            category="commit", actor=process_id,
            action="propose_commit", target=state_hash,
            outcome="success" if success else "blocked",
        ))

    def record_injection_attempt(self, source: str, injection_types: list[str]) -> None:
        self.record(AuditEvent(
            severity=AuditSeverity.SECURITY, category="injection",
            actor=source, action="prompt_injection_detected",
            outcome="blocked", metadata={"types": injection_types},
        ))

    def record_research_initiation(self, request_id: str, topic: str, approved: bool) -> None:
        self.record(AuditEvent(
            category="research", actor=request_id,
            action="research_requested", target=topic,
            outcome="approved" if approved else "rejected",
        ))

    def record_promotion(self, capability_id: str, verdict: str) -> None:
        self.record(AuditEvent(
            category="promotion", actor=capability_id,
            action="promotion_evaluated", outcome=verdict,
        ))

    def generate_report(self, since: datetime | None = None) -> AuditReport:
        """Generate audit report, optionally filtered by time."""
        if since:
            events = [e for e in self._events if e.timestamp >= since]
        else:
            events = list(self._events)
        return AuditReport(events=events)

    @property
    def event_count(self) -> int:
        return len(self._events)
