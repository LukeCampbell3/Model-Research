"""Generate synthetic fixtures for all schema types."""

from typing import Dict, Any

from runtime_coder.schemas.task_packet import TaskPacket
from runtime_coder.schemas.context_packet import ContextPacket
from runtime_coder.schemas.branch_ticket import BranchTicket
from runtime_coder.schemas.branch_ir import BranchIR
from runtime_coder.schemas.evidence_packet import EvidencePacket
from runtime_coder.schemas.verifier_result import VerifierResult
from runtime_coder.schemas.replay_record import ReplayRecord
from runtime_coder.schemas.commit_result import CommitResult
from runtime_coder.schemas.claim_ledger import ClaimLedger


def generate_task_packet() -> TaskPacket:
    """Generate a valid TaskPacket fixture."""
    return TaskPacket(
        task_id="task_001",
        task_type="code_generation",
        description="Implement a binary search function",
        constraints=["O(log n) time complexity", "handle empty arrays"],
        context_refs=["ctx_001", "ctx_002"],
        priority=1,
        metadata={"source": "fixture"},
    )


def generate_context_packet() -> ContextPacket:
    """Generate a valid ContextPacket fixture."""
    return ContextPacket(
        context_id="ctx_001",
        source_type="file",
        content="def existing_sort(arr): return sorted(arr)",
        file_path="src/utils.py",
        language="python",
        symbols=["existing_sort"],
        dependencies=["typing"],
        metadata={"line_start": 1, "line_end": 5},
    )


def generate_branch_ticket() -> BranchTicket:
    """Generate a valid BranchTicket fixture."""
    return BranchTicket(
        ticket_id="branch_001",
        branch_type="patch",
        privilege_level="read_write",
        description="Add binary search implementation",
        read_set=["src/utils.py", "tests/test_utils.py"],
        write_set=["src/search.py"],
        verifier_targets=["tests/test_search.py::test_binary_search"],
        constraints=["must not modify existing functions"],
        parent_ticket_id=None,
        metadata={"estimated_tokens": 500},
    )


def generate_branch_ir() -> BranchIR:
    """Generate a valid BranchIR fixture."""
    return BranchIR(
        ir_id="ir_001",
        ticket_id="branch_001",
        steps=[
            {"action": "read", "target": "src/utils.py"},
            {"action": "generate", "target": "src/search.py", "template": "function"},
            {"action": "verify", "target": "tests/test_search.py"},
        ],
        dependencies=["ctx_001"],
        estimated_tokens=450,
        optimization_hints={"cache_context": True},
        status="pending",
        metadata={},
    )


def generate_evidence_packet() -> EvidencePacket:
    """Generate a valid EvidencePacket fixture."""
    return EvidencePacket(
        evidence_id="ev_001",
        ticket_id="branch_001",
        evidence_type="test_result",
        content="All 5 tests passed",
        confidence=0.95,
        source_step=2,
        supporting_data={"tests_passed": 5, "tests_failed": 0},
        timestamp="2024-01-01T00:00:00Z",
        metadata={},
    )


def generate_verifier_result() -> VerifierResult:
    """Generate a valid VerifierResult fixture."""
    return VerifierResult(
        result_id="vr_001",
        ticket_id="branch_001",
        verifier_type="test",
        passed=True,
        score=0.95,
        errors=[],
        warnings=["unused import detected"],
        evidence_refs=["ev_001"],
        metadata={"duration_ms": 120},
    )


def generate_replay_record() -> ReplayRecord:
    """Generate a valid ReplayRecord fixture."""
    return ReplayRecord(
        record_id="replay_001",
        ticket_id="branch_001",
        sequence_number=0,
        action_type="generate",
        inputs={"context": "ctx_001", "prompt": "implement binary search"},
        outputs={"code": "def binary_search(arr, target): ..."},
        token_budget_used=200,
        timestamp="2024-01-01T00:00:01Z",
        metadata={},
    )


def generate_commit_result() -> CommitResult:
    """Generate a valid CommitResult fixture."""
    return CommitResult(
        commit_id="commit_001",
        ticket_id="branch_001",
        committed=True,
        files_modified=[],
        files_created=["src/search.py"],
        files_deleted=[],
        rollback_available=True,
        verifier_summary={"passed": True, "score": 0.95},
        metadata={},
    )


def generate_claim_ledger() -> ClaimLedger:
    """Generate a valid ClaimLedger fixture."""
    return ClaimLedger(
        ledger_id="ledger_001",
        ticket_id="branch_001",
        claims=[
            {"claim_id": "c1", "text": "function is O(log n)", "verified": True},
            {"claim_id": "c2", "text": "handles empty arrays", "verified": True},
        ],
        total_claims=2,
        verified_claims=2,
        rejected_claims=0,
        metadata={},
    )


def generate_all_fixtures() -> Dict[str, Any]:
    """Generate all synthetic fixtures and return as a dictionary."""
    return {
        "task_packet": generate_task_packet(),
        "context_packet": generate_context_packet(),
        "branch_ticket": generate_branch_ticket(),
        "branch_ir": generate_branch_ir(),
        "evidence_packet": generate_evidence_packet(),
        "verifier_result": generate_verifier_result(),
        "replay_record": generate_replay_record(),
        "commit_result": generate_commit_result(),
        "claim_ledger": generate_claim_ledger(),
    }
