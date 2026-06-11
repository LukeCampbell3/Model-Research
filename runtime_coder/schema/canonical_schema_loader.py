"""Canonical schema loader for RuntimeCoder.

Loads BranchTicket schema from cognitive_microkernel, computes schema_hash,
and validates compatibility between runtime_coder's expected schema and the
canonical source.
"""

import hashlib
import json
from typing import Dict, Any, Tuple


# BranchTicket canonical schema definition (mirrors cognitive_microkernel)
BRANCH_TICKET_SCHEMA = {
    "schema_name": "BranchTicket",
    "schema_version": "1.0",
    "required_fields": [
        "ticket_id",
        "branch_type",
        "privilege_level",
        "description",
        "read_set",
        "write_set",
    ],
    "optional_fields": [
        "verifier_targets",
        "constraints",
        "parent_ticket_id",
        "metadata",
        "schema_hash",
        "runtime_contract_version",
        "target_kind",
    ],
    "field_types": {
        "ticket_id": "str",
        "branch_type": "str",
        "privilege_level": "str",
        "description": "str",
        "read_set": "List[str]",
        "write_set": "List[str]",
        "verifier_targets": "List[str]",
        "constraints": "List[str]",
        "parent_ticket_id": "Optional[str]",
        "metadata": "Dict[str, Any]",
        "schema_hash": "str",
        "runtime_contract_version": "str",
        "target_kind": "str",
    },
    "allowed_branch_types": [
        "patch", "refactor", "test", "documentation",
        "exploration", "fix", "bug_fix", "type_fix",
        "import_fix", "test_gen",
    ],
    "allowed_privilege_levels": [
        "read_only", "read_write", "admin", "sandboxed",
    ],
    "runtime_contract_version": "1.0",
    "target_kind": "python",
}


def load_branch_ticket_schema() -> Dict[str, Any]:
    """Load the canonical BranchTicket schema definition.

    Returns:
        Schema dictionary with fields, types, and constraints.
    """
    return BRANCH_TICKET_SCHEMA.copy()


def compute_schema_hash(schema: Dict[str, Any] = None) -> str:
    """Compute a deterministic hash of the schema for versioning.

    Args:
        schema: Schema dict to hash. Uses canonical if None.

    Returns:
        SHA-256 hex digest (first 16 chars) of the schema.
    """
    if schema is None:
        schema = BRANCH_TICKET_SCHEMA

    # Deterministic serialization: sorted keys, no whitespace
    canonical_json = json.dumps(schema, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical_json.encode()).hexdigest()[:16]


def check_schema_compatibility(
    expected_hash: str = None,
    expected_version: str = "1.0",
) -> Tuple[bool, str]:
    """Check schema compatibility between expected and canonical.

    Args:
        expected_hash: Expected schema hash. If None, always passes.
        expected_version: Expected runtime contract version.

    Returns:
        Tuple of (is_compatible, message).
    """
    schema = load_branch_ticket_schema()
    current_hash = compute_schema_hash(schema)
    current_version = schema.get("runtime_contract_version", "unknown")

    if expected_hash is not None and expected_hash != current_hash:
        return False, (
            f"Schema hash mismatch: expected={expected_hash}, "
            f"current={current_hash}"
        )

    if expected_version != current_version:
        return False, (
            f"Version mismatch: expected={expected_version}, "
            f"current={current_version}"
        )

    return True, f"Compatible: hash={current_hash}, version={current_version}"
