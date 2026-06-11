"""ClaimLedger schema - tracks claims made during execution."""

import dataclasses
from typing import List, Dict, Any

from runtime_coder.schemas.base import BaseSchema


@dataclasses.dataclass
class ClaimEntry:
    """A single claim entry in the ledger."""
    claim_id: str = ""
    claim_text: str = ""
    confidence: float = 0.0
    evidence_refs: List[str] = dataclasses.field(default_factory=list)
    verified: bool = False
    timestamp: str = ""


@dataclasses.dataclass
class ClaimLedger(BaseSchema):
    """Ledger tracking all claims made during branch execution."""

    ledger_id: str = ""
    ticket_id: str = ""
    claims: List[Dict[str, Any]] = dataclasses.field(default_factory=list)
    total_claims: int = 0
    verified_claims: int = 0
    rejected_claims: int = 0
    metadata: Dict[str, Any] = dataclasses.field(default_factory=dict)

    def validate(self) -> list:
        errors = super().validate()
        if not self.ledger_id:
            errors.append("ledger_id must not be empty")
        if not self.ticket_id:
            errors.append("ticket_id must not be empty")
        if self.verified_claims > self.total_claims:
            errors.append("verified_claims cannot exceed total_claims")
        if self.rejected_claims > self.total_claims:
            errors.append("rejected_claims cannot exceed total_claims")
        return errors
