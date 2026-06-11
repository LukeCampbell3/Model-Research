"""Tests for the Python BranchTicket curriculum builder."""

import json
import pytest

from runtime_coder.data_pipeline.python_branch_ticket_curriculum import (
    build_curriculum,
    build_mixed_curriculum,
)
from runtime_coder.schema.canonical_schema_loader import compute_schema_hash


class TestCurriculumBuilder:
    """Tests for staged curriculum building."""

    def test_stage_a_builds(self):
        """Stage A (JSON warmup) builds successfully."""
        examples = build_curriculum("A", size=10)
        assert len(examples) == 10

    def test_stage_b_builds(self):
        """Stage B (minimal ticket) builds successfully."""
        examples = build_curriculum("B", size=10)
        assert len(examples) == 10

    def test_stage_c_builds(self):
        """Stage C (full ticket) builds successfully."""
        examples = build_curriculum("C", size=10)
        assert len(examples) == 10

    def test_invalid_stage_raises(self):
        """Invalid stage raises ValueError."""
        with pytest.raises(ValueError):
            build_curriculum("X", size=5)

    def test_stage_a_targets_are_valid_json(self):
        """Stage A targets parse as valid JSON."""
        for ex in build_curriculum("A", size=10):
            data = json.loads(ex["target"])
            assert "schema_hash" in data
            assert "runtime_contract_version" in data
            assert "target_kind" in data

    def test_stage_b_targets_have_required_fields(self):
        """Stage B targets have minimal BranchTicket fields."""
        schema_hash = compute_schema_hash()
        for ex in build_curriculum("B", size=10):
            data = json.loads(ex["target"])
            assert data["ticket_id"]
            assert data["branch_type"]
            assert data["schema_hash"] == schema_hash

    def test_stage_c_targets_have_full_fields(self):
        """Stage C targets have full BranchTicket with context."""
        for ex in build_curriculum("C", size=10):
            data = json.loads(ex["target"])
            assert "verifier_targets" in data
            assert "constraints" in data
            assert data["target_kind"] == "python"

    def test_stage_c_inputs_have_context(self):
        """Stage C inputs include context tokens."""
        for ex in build_curriculum("C", size=10):
            assert "<|context_start|>" in ex["input"]
            assert "<|context_end|>" in ex["input"]

    def test_mixed_curriculum_has_all_stages(self):
        """Mixed curriculum includes A, B, and C stages."""
        examples = build_mixed_curriculum(size=50)
        stages = {ex["stage"] for ex in examples}
        assert "A" in stages
        assert "B" in stages
        assert "C" in stages

    def test_curriculum_metadata_present(self):
        """All examples have curriculum_metadata."""
        for ex in build_curriculum("C", size=5):
            assert "curriculum_metadata" in ex
            assert "difficulty" in ex["curriculum_metadata"]

    def test_deterministic_with_seed(self):
        """Same seed produces same curriculum."""
        ex1 = build_curriculum("B", size=5, seed=123)
        ex2 = build_curriculum("B", size=5, seed=123)
        assert ex1 == ex2

    def test_different_seeds_differ(self):
        """Different seeds produce different curricula."""
        ex1 = build_curriculum("B", size=5, seed=1)
        ex2 = build_curriculum("B", size=5, seed=999)
        assert ex1 != ex2
