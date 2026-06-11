"""ContextPacket schema - represents context provided to a coding task."""

import dataclasses
from typing import List, Dict, Any

from runtime_coder.schemas.base import BaseSchema


@dataclasses.dataclass
class ContextPacket(BaseSchema):
    """Context information for task execution."""

    context_id: str = ""
    source_type: str = "file"  # file, symbol, snippet, documentation
    content: str = ""
    file_path: str = ""
    language: str = ""
    symbols: List[str] = dataclasses.field(default_factory=list)
    dependencies: List[str] = dataclasses.field(default_factory=list)
    metadata: Dict[str, Any] = dataclasses.field(default_factory=dict)

    def validate(self) -> list:
        errors = super().validate()
        if not self.context_id:
            errors.append("context_id must not be empty")
        if not self.content:
            errors.append("content must not be empty")
        allowed_sources = {"file", "symbol", "snippet", "documentation", "runtime"}
        if self.source_type not in allowed_sources:
            errors.append(f"source_type must be one of {allowed_sources}")
        return errors
