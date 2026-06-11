"""Test runtime schemas: round-trip, validation, edge cases."""

import json
import pytest

from runtime_coder.schemas import (
    TaskPacket,
    ContextPacket,
    BranchTicket,
    BranchIR,
    EvidencePacket,
    VerifierResult,
    ReplayRecord,
    CommitResult,
    ClaimLedger,
)
from runtime_coder.data_pipeline.fixtures import generate_all_fixtures


class TestSchemaRoundTrip:
    """Test to_dict/from_dict/to_json/from_json round-trip for all schemas."""

    @pytest.fixture
    def fixtures(self):
        return generate_all_fixtures()

    def test_task_packet_round_trip(self, fixtures):
        original = fixtures["task_packet"]
        restored = TaskPacket.from_json(original.to_json())
        assert original.to_dict() == restored.to_dict()

    def test_context_packet_round_trip(self, fixtures):
        original = fixtures["context_packet"]
        restored = ContextPacket.from_json(original.to_json())
        assert original.to_dict() == restored.to_dict()

    def test_branch_ticket_round_trip(self, fixtures):
        original = fixtures["branch_ticket"]
        restored = BranchTicket.from_json(original.to_json())
        assert original.to_dict() == restored.to_dict()

    def test_branch_ir_round_trip(self, fixtures):
        original = fixtures["branch_ir"]
        restored = BranchIR.from_json(original.to_json())
        assert original.to_dict() == restored.to_dict()

    def test_evidence_packet_round_trip(self, fixtures):
        original = fixtures["evidence_packet"]
        restored = EvidencePacket.from_json(original.to_json())
        assert original.to_dict() == restored.to_dict()

    def test_verifier_result_round_trip(self, fixtures):
        original = fixtures["verifier_result"]
        restored = VerifierResult.from_json(original.to_json())
        assert original.to_dict() == restored.to_dict()

    def test_replay_record_round_trip(self, fixtures):
        original = fixtures["replay_record"]
        restored = ReplayRecord.from_json(original.to_json())
        assert original.to_dict() == restored.to_dict()

    def test_commit_result_round_trip(self, fixtures):
        original = fixtures["commit_result"]
        restored = CommitResult.from_json(original.to_json())
        assert original.to_dict() == restored.to_dict()

    def test_claim_ledger_round_trip(self, fixtures):
        original = fixtures["claim_ledger"]
        restored = ClaimLedger.from_json(original.to_json())
        assert original.to_dict() == restored.to_dict()


class TestSchemaValidation:
    """Test schema validation logic."""

    def test_valid_branch_ticket_passes(self):
        ticket = BranchTicket(
            ticket_id="t1",
            branch_type="patch",
            privilege_level="read_write",
            read_set=["file.py"],
            write_set=["out.py"],
            verifier_targets=["test.py"],
        )
        assert ticket.validate() == []

    def test_branch_ticket_invalid_type(self):
        ticket = BranchTicket(
            ticket_id="t1",
            branch_type="invalid_type",
            privilege_level="read_write",
        )
        errors = ticket.validate()
        assert any("branch_type" in e for e in errors)

    def test_branch_ticket_invalid_privilege(self):
        ticket = BranchTicket(
            ticket_id="t1",
            branch_type="exploration",
            privilege_level="superuser",
        )
        errors = ticket.validate()
        assert any("privilege_level" in e for e in errors)

    def test_patch_requires_read_set(self):
        ticket = BranchTicket(
            ticket_id="t1",
            branch_type="patch",
            privilege_level="read_write",
            read_set=[],
            write_set=["out.py"],
            verifier_targets=["test.py"],
        )
        errors = ticket.validate()
        assert any("read_set" in e for e in errors)

    def test_patch_requires_write_set(self):
        ticket = BranchTicket(
            ticket_id="t1",
            branch_type="patch",
            privilege_level="read_write",
            read_set=["file.py"],
            write_set=[],
            verifier_targets=["test.py"],
        )
        errors = ticket.validate()
        assert any("write_set" in e for e in errors)

    def test_patch_requires_verifier_targets(self):
        ticket = BranchTicket(
            ticket_id="t1",
            branch_type="patch",
            privilege_level="read_write",
            read_set=["file.py"],
            write_set=["out.py"],
            verifier_targets=[],
        )
        errors = ticket.validate()
        assert any("verifier_targets" in e for e in errors)

    def test_non_patch_no_extra_requirements(self):
        ticket = BranchTicket(
            ticket_id="t1",
            branch_type="exploration",
            privilege_level="read_only",
            read_set=[],
            write_set=[],
            verifier_targets=[],
        )
        errors = ticket.validate()
        assert errors == []

    def test_empty_ticket_id_fails(self):
        ticket = BranchTicket(ticket_id="", branch_type="exploration", privilege_level="read_only")
        errors = ticket.validate()
        assert any("ticket_id" in e for e in errors)

    def test_branch_ir_requires_steps(self):
        ir = BranchIR(ir_id="ir1", ticket_id="t1", steps=[])
        errors = ir.validate()
        assert any("steps" in e for e in errors)

    def test_verifier_result_score_bounds(self):
        vr = VerifierResult(result_id="v1", ticket_id="t1", score=1.5)
        errors = vr.validate()
        assert any("score" in e for e in errors)

    def test_claim_ledger_verified_exceeds_total(self):
        cl = ClaimLedger(
            ledger_id="l1", ticket_id="t1",
            total_claims=2, verified_claims=5
        )
        errors = cl.validate()
        assert any("verified_claims" in e for e in errors)


class TestAllFixturesValid:
    """All generated fixtures should pass validation."""

    def test_all_fixtures_validate(self):
        fixtures = generate_all_fixtures()
        for name, fixture in fixtures.items():
            errors = fixture.validate()
            assert errors == [], f"Fixture '{name}' failed validation: {errors}"
