"""Tests for canonical schema loader."""

import pytest

from runtime_coder.schema.canonical_schema_loader import (
    load_branch_ticket_schema,
    compute_schema_hash,
    check_schema_compatibility,
)


class TestSchemaLoader:
    """Tests for schema loading and hashing."""

    def test_schema_loads(self):
        """Schema loads successfully with expected structure."""
        schema = load_branch_ticket_schema()
        assert isinstance(schema, dict)
        assert "schema_name" in schema
        assert schema["schema_name"] == "BranchTicket"

    def test_schema_has_required_fields(self):
        """Schema defines required fields."""
        schema = load_branch_ticket_schema()
        required = schema["required_fields"]
        assert "ticket_id" in required
        assert "branch_type" in required
        assert "read_set" in required
        assert "write_set" in required

    def test_schema_has_runtime_fields(self):
        """Schema includes runtime contract fields."""
        schema = load_branch_ticket_schema()
        optional = schema["optional_fields"]
        assert "schema_hash" in optional
        assert "runtime_contract_version" in optional
        assert "target_kind" in optional

    def test_schema_hash_computed(self):
        """Schema hash is a non-empty hex string."""
        h = compute_schema_hash()
        assert isinstance(h, str)
        assert len(h) == 16
        # Should be valid hex
        int(h, 16)

    def test_schema_hash_deterministic(self):
        """Same schema produces same hash."""
        h1 = compute_schema_hash()
        h2 = compute_schema_hash()
        assert h1 == h2

    def test_schema_hash_changes_on_modification(self):
        """Modified schema produces different hash."""
        schema = load_branch_ticket_schema()
        h1 = compute_schema_hash(schema)

        modified = schema.copy()
        modified["new_field"] = "test"
        h2 = compute_schema_hash(modified)

        assert h1 != h2

    def test_compatibility_check_passes(self):
        """Compatibility check passes with correct version."""
        compatible, msg = check_schema_compatibility(expected_version="1.0")
        assert compatible
        assert "Compatible" in msg

    def test_compatibility_check_fails_on_wrong_version(self):
        """Compatibility check fails with wrong version."""
        compatible, msg = check_schema_compatibility(expected_version="2.0")
        assert not compatible
        assert "mismatch" in msg.lower()

    def test_compatibility_check_fails_on_wrong_hash(self):
        """Compatibility check fails with wrong hash."""
        compatible, msg = check_schema_compatibility(expected_hash="wrong_hash")
        assert not compatible
        assert "mismatch" in msg.lower()

    def test_compatibility_with_correct_hash(self):
        """Compatibility passes with correct hash."""
        correct_hash = compute_schema_hash()
        compatible, msg = check_schema_compatibility(expected_hash=correct_hash)
        assert compatible
