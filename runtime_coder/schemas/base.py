"""Base schema with serialization and validation support."""

import json
import dataclasses
from typing import Any, Dict


class BaseSchema:
    """Mixin providing to_dict, from_dict, to_json, from_json, validate."""

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to dictionary."""
        return dataclasses.asdict(self)

    @classmethod
    def from_dict(cls, d: Dict[str, Any]):
        """Deserialize from dictionary."""
        field_names = {f.name for f in dataclasses.fields(cls)}
        filtered = {k: v for k, v in d.items() if k in field_names}
        return cls(**filtered)

    def to_json(self) -> str:
        """Serialize to JSON string."""
        return json.dumps(self.to_dict(), indent=2)

    @classmethod
    def from_json(cls, s: str):
        """Deserialize from JSON string."""
        return cls.from_dict(json.loads(s))

    def validate(self) -> list:
        """Validate fields. Returns list of error strings (empty = valid)."""
        errors = []
        for f in dataclasses.fields(self):
            val = getattr(self, f.name)
            if val is None and f.default is dataclasses.MISSING and f.default_factory is dataclasses.MISSING:
                errors.append(f"Field '{f.name}' is required but None")
        return errors
