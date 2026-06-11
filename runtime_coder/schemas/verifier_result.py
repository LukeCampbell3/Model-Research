"""VerifierResult schema - result from a verification step."""

import dataclasses
from typing import List, Dict, Any

from runtime_coder.schemas.base import BaseSchema


@dataclasses.dataclass
class VerifierResult(BaseSchema):
    """Result from running a verifier on branch output."""

    result_id: str = ""
    ticket_id: str = ""
    verifier_type: str = "syntax"  # syntax, semantic, test, runtime, type_check
    passed: bool = False
    score: float = 0.0
    errors: List[str] = dataclasses.field(default_factory=list)
    warnings: List[str] = dataclasses.field(default_factory=list)
    evidence_refs: List[str] = dataclasses.field(default_factory=list)
    metadata: Dict[str, Any] = dataclasses.field(default_factory=dict)

    def validate(self) -> list:
        errors_list = super().validate()
        if not self.result_id:
            errors_list.append("result_id must not be empty")
        if not self.ticket_id:
            errors_list.append("ticket_id must not be empty")
        if not 0.0 <= self.score <= 1.0:
            errors_list.append("score must be between 0.0 and 1.0")
        allowed_types = {"syntax", "semantic", "test", "runtime", "type_check", "lint"}
        if self.verifier_type not in allowed_types:
            errors_list.append(f"verifier_type must be one of {allowed_types}")
        return errors_list
