"""EvidencePacket schema - evidence collected during branch execution."""

import dataclasses
from typing import List, Dict, Any, Optional

from runtime_coder.schemas.base import BaseSchema


@dataclasses.dataclass
class EvidencePacket(BaseSchema):
    """Evidence gathered during execution to support claims."""

    evidence_id: str = ""
    ticket_id: str = ""
    evidence_type: str = "test_result"  # test_result, trace, assertion, metric
    content: str = ""
    confidence: float = 0.0
    source_step: int = 0
    supporting_data: Dict[str, Any] = dataclasses.field(default_factory=dict)
    timestamp: str = ""
    metadata: Dict[str, Any] = dataclasses.field(default_factory=dict)

    def validate(self) -> list:
        errors = super().validate()
        if not self.evidence_id:
            errors.append("evidence_id must not be empty")
        if not self.ticket_id:
            errors.append("ticket_id must not be empty")
        if not 0.0 <= self.confidence <= 1.0:
            errors.append("confidence must be between 0.0 and 1.0")
        allowed_types = {"test_result", "trace", "assertion", "metric", "observation"}
        if self.evidence_type not in allowed_types:
            errors.append(f"evidence_type must be one of {allowed_types}")
        return errors
