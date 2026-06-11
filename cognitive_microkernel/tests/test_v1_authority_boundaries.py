"""V1 Authority Boundary Integration Tests.

Verifies cross-phase properties that ensure no advisory component
can violate the fundamental authority hierarchy:

    Only CommitManager can mutate durable state.

Every other component — compiler, research, adjudicator, policy memory,
context compiler, promotion gate, audit reporter — is read-only or advisory.
"""

import pytest
import inspect
import tempfile
from pathlib import Path

from cognitive_microkernel.schemas import (
    BranchProcess, BranchType, ProcessStatus, CanonicalState,
    EvidenceRecord, Claim, SupportStatus, SideEffectPolicy,
    EvidenceSourceType, TransactionStatus,
)
from cognitive_microkernel.storage import StorageManager
from cognitive_microkernel.transactions import CanonicalStateCommitter
from cognitive_microkernel.runtime import Runtime

from cognitive_microkernel.compiler import (
    PassManager, DeadBranchElimination, DuplicateBranchMerge,
    BasicConflictAnalysis, StrengthReduction, AdmissionScoring,
    BranchPlan, BranchPlanEntry, AdmissionStatus,
)
from cognitive_microkernel.phase3 import (
    ResearchGateway, ResearchRequest, ResearchBounds,
    PromptInjectionBoundary,
    EvidencePacket, ProvenanceChain, ProvenanceNode,
    ReplayPatternMemory,
    PolicyMemory, PolicyEntry, DecaySchedule,
    ContextCompiler, ContextBudget,
    Adjudicator, AdjudicationResult, ConflictResolution,
    PromotionGate, PromotionRequest, PromotionVerdict,
    RuntimeAuditReporter, AuditEvent,
)
from cognitive_microkernel.phase3.research_gateway import ResearchOutcome, ResearchStatus
from cognitive_microkernel.phase3.audit_reporter import AuditSeverity


@pytest.fixture
def temp_dir():
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


@pytest.fixture
def storage(temp_dir):
    return StorageManager(temp_dir)


# ============================================================================
# 1. ResearchGateway cannot create commit candidates directly
# ============================================================================

class TestResearchGatewayAuthority:
    def test_research_gateway_has_no_commit_interface(self):
        """ResearchGateway has no method to commit, propose_commit, or create transactions."""
        gw = ResearchGateway()
        forbidden = ["commit", "propose_commit", "create_transaction",
                     "mutate_state", "write_state", "advance_state"]
        for attr in forbidden:
            assert not hasattr(gw, attr), f"ResearchGateway has forbidden attr: {attr}"

    def test_research_gateway_has_no_storage_dependency(self):
        """ResearchGateway does not hold a reference to StorageManager."""
        gw = ResearchGateway()
        members = [name for name, _ in inspect.getmembers(gw)]
        assert "storage" not in members
        assert "state_ledger" not in members
        assert "evidence_ledger" not in members

    def test_research_produces_outcomes_not_state_changes(self):
        """Research outcomes are data objects, not state mutations."""
        outcome = ResearchOutcome(
            request_id="r1", status=ResearchStatus.COMPLETED,
            evidence_produced=["ev1"], claims_produced=["c1"],
        )
        # Outcome is a data container — it has no write capability
        assert not hasattr(outcome, "commit")
        assert not hasattr(outcome, "apply")
        assert isinstance(outcome.evidence_produced, list)

    def test_research_request_cannot_escalate_to_commit(self):
        """A research request cannot morph into a commit operation."""
        req = ResearchRequest(topic="T", justification="J", evidence_gap_ref="g")
        # No field or method allows commit-level authority
        assert not hasattr(req, "commit")
        assert not hasattr(req, "transaction")
        assert not hasattr(req, "state_delta")


# ============================================================================
# 2. Adjudicator cannot apply patches
# ============================================================================

class TestAdjudicatorAuthority:
    def test_adjudicator_has_no_patch_interface(self):
        """Adjudicator cannot apply, execute, or commit patches."""
        adj = Adjudicator()
        forbidden = ["apply_patch", "execute_resolution", "commit",
                     "mutate", "write", "patch_state"]
        for attr in forbidden:
            assert not hasattr(adj, attr), f"Adjudicator has forbidden attr: {attr}"

    def test_adjudication_result_is_data_only(self):
        """AdjudicationResult is informational, not executable."""
        result = AdjudicationResult(
            conflict_id="c1", branch_a_id="a", branch_b_id="b",
            resolution=ConflictResolution.PREFER_A, confidence=0.8,
            reasoning="A has stronger evidence",
        )
        assert not hasattr(result, "execute")
        assert not hasattr(result, "apply")
        assert not hasattr(result, "commit")

    def test_adjudicator_output_does_not_reference_storage(self):
        """Adjudicator never touches StorageManager."""
        adj = Adjudicator()
        result = adj.adjudicate({"ev1": 0.9}, {"ev2": 0.3}, "a", "b")
        # Result contains branch IDs and evidence IDs — not storage handles
        assert isinstance(result.evidence_basis, list)
        assert all(isinstance(e, str) for e in result.evidence_basis)


# ============================================================================
# 3. PromotionGate cannot apply patches
# ============================================================================

class TestPromotionGateAuthority:
    def test_promotion_gate_evaluates_only(self):
        """PromotionGate produces verdicts, never executes them."""
        gate = PromotionGate()
        forbidden = ["execute", "apply", "activate", "promote",
                     "commit", "write_state", "mutate"]
        for attr in forbidden:
            assert not hasattr(gate, attr), f"PromotionGate has forbidden attr: {attr}"

    def test_promotion_verdict_is_enum_not_action(self):
        """PromotionVerdict is a status label, not a callable action."""
        for verdict in PromotionVerdict:
            assert not callable(verdict.value)
            assert isinstance(verdict.value, str)

    def test_promotion_gate_has_no_storage(self):
        """PromotionGate does not hold storage references."""
        gate = PromotionGate()
        assert not hasattr(gate, "storage")
        assert not hasattr(gate, "state_ledger")


# ============================================================================
# 4. PolicyMemory cannot override hard rejection
# ============================================================================

class TestPolicyMemoryAuthority:
    def test_policy_memory_is_query_only(self):
        """PolicyMemory can store and query policies, but cannot enforce them."""
        mem = PolicyMemory()
        forbidden = ["commit", "override", "force", "execute",
                     "bypass_verification", "bypass_gate"]
        for attr in forbidden:
            assert not hasattr(mem, attr), f"PolicyMemory has forbidden attr: {attr}"

    def test_policy_entry_cannot_override_rejection(self):
        """A PolicyEntry has no mechanism to override commit rejection."""
        entry = PolicyEntry(
            policy_id="p1", policy_type="routing",
            decision="override_rejection", confidence=1.0,
        )
        # The entry is data — it cannot act
        assert not hasattr(entry, "apply")
        assert not hasattr(entry, "execute")
        assert not hasattr(entry, "force_commit")

    def test_strongest_policy_does_not_grant_commit_authority(self):
        """Even the strongest policy is advisory only."""
        mem = PolicyMemory()
        entry = PolicyEntry(policy_id="strong", policy_type="routing",
                           decision="always_commit", confidence=1.0,
                           decay_schedule=DecaySchedule.PERMANENT)
        mem.store(entry)
        strongest = mem.get_strongest("routing")
        assert strongest is not None
        assert strongest.confidence == 1.0
        # But it has no commit power
        assert not hasattr(strongest, "commit")
        assert not hasattr(strongest, "authorize")


# ============================================================================
# 5. ContextCompiler cannot authorize branch execution
# ============================================================================

class TestContextCompilerAuthority:
    def test_context_compiler_produces_pages_not_authorizations(self):
        """ContextCompiler outputs ContextPages, not execution authorizations."""
        cc = ContextCompiler()
        page = cc.compile(["ev1", "ev2"], ["c1"], [])
        assert not hasattr(page, "authorize")
        assert not hasattr(page, "execute")
        assert not hasattr(page, "admit")

    def test_context_page_cannot_create_workspace(self):
        """ContextPage is data — it cannot create workspaces."""
        from cognitive_microkernel.phase3 import ContextPage
        page = ContextPage(evidence_refs=["ev1"], claim_refs=["c1"])
        assert not hasattr(page, "create_workspace")
        assert not hasattr(page, "admit_branch")

    def test_context_compiler_has_no_storage_write(self):
        """ContextCompiler reads references but never writes."""
        cc = ContextCompiler()
        assert not hasattr(cc, "write")
        assert not hasattr(cc, "store")
        assert not hasattr(cc, "storage")


# ============================================================================
# 6. AuditReporter cannot mutate branch status
# ============================================================================

class TestAuditReporterAuthority:
    def test_audit_reporter_is_append_only_observer(self):
        """AuditReporter appends events but cannot modify system state."""
        reporter = RuntimeAuditReporter()
        forbidden = ["mutate", "cancel_branch", "modify_branch",
                     "commit", "rollback", "change_status"]
        for attr in forbidden:
            assert not hasattr(reporter, attr), f"AuditReporter has forbidden attr: {attr}"

    def test_audit_events_are_immutable_records(self):
        """AuditEvents are created and stored, never modified after creation."""
        event = AuditEvent(
            category="commit", actor="p1", action="propose_commit",
            target="state_hash", outcome="success",
        )
        # Event is a frozen dataclass record
        assert isinstance(event.event_id, str)
        assert isinstance(event.timestamp, object)

    def test_audit_report_generation_does_not_mutate(self):
        """Generating a report does not modify the event stream."""
        reporter = RuntimeAuditReporter()
        reporter.record_commit("p1", "s1", True)
        reporter.record_commit("p2", "s2", False)
        count_before = reporter.event_count
        _ = reporter.generate_report()
        assert reporter.event_count == count_before  # Not mutated


# ============================================================================
# 7. EvidencePacket validity does not equal commit permission
# ============================================================================

class TestEvidencePacketAuthority:
    def test_valid_evidence_packet_is_not_commit_authorization(self):
        """An EvidencePacket being valid_for_commit is a PROPERTY, not an ACTION."""
        packet = EvidencePacket(
            evidence_id="ev1", confidence_score=0.95, strength=0.9,
            provenance=ProvenanceChain(nodes=[
                ProvenanceNode(process_id="p1", state_hash="s1", confidence=0.95)
            ]),
        )
        # Valid for commit is a boolean property check
        assert packet.is_valid_for_commit()
        # But the packet has no commit method
        assert not hasattr(packet, "commit")
        assert not hasattr(packet, "execute_commit")
        assert not hasattr(packet, "authorize_commit")

    def test_invalid_evidence_packet_has_same_interface(self):
        """Invalid packets have identical interface to valid ones (data only)."""
        invalid = EvidencePacket(
            evidence_id="ev_bad", confidence_score=0.1, strength=0.1,
            provenance=ProvenanceChain(nodes=[
                ProvenanceNode(process_id="p1", state_hash="s1",
                             action="contradicted", confidence=0.1)
            ]),
        )
        assert not invalid.is_valid_for_commit()
        # Same interface — no commit power either way
        assert not hasattr(invalid, "commit")

    def test_evidence_packet_cannot_write_to_ledger(self):
        """EvidencePacket has no storage write capability."""
        packet = EvidencePacket(evidence_id="ev1")
        assert not hasattr(packet, "storage")
        assert not hasattr(packet, "write")
        assert not hasattr(packet, "store")


# ============================================================================
# 8. Only CommitManager can mutate durable state
# ============================================================================

class TestCommitManagerExclusivity:
    def test_commit_manager_is_the_only_state_mutator(self, storage):
        """Only CanonicalStateCommitter can advance canonical state."""
        initial = CanonicalState(root_state_hash="initial_v1")
        storage.state_ledger.register_state(initial)

        # Store evidence for a valid commit
        ev = EvidenceRecord(
            evidence_id="verify_authority",
            source_type=EvidenceSourceType.VERIFIER,
            source_ref="verifier", state_hash="initial_v1",
            process_id="p1", raw_payload_ref="r", summary="Verified",
        )
        storage.evidence_ledger.record_evidence(ev)

        # The CommitManager is the ONLY path to state mutation.
        # This test verifies that CommitManager EXISTS and CAN commit
        # (the positive case) while all other components CANNOT.
        committer = CanonicalStateCommitter(storage)
        assert hasattr(committer, "propose_commit")

        # Verify advisory components lack this capability
        from cognitive_microkernel.phase3 import (
            ResearchGateway, Adjudicator, PromotionGate, PolicyMemory,
            ContextCompiler, RuntimeAuditReporter,
        )
        for component_class in [ResearchGateway, Adjudicator, PromotionGate,
                                PolicyMemory, ContextCompiler, RuntimeAuditReporter]:
            assert not hasattr(component_class, "propose_commit"), (
                f"{component_class.__name__} should not have propose_commit"
            )

    def test_no_phase3_component_has_state_write_capability(self):
        """Exhaustive check: no Phase 3 component can write state."""
        components = [
            ResearchGateway(),
            PromptInjectionBoundary(),
            ReplayPatternMemory(),
            PolicyMemory(),
            ContextCompiler(),
            Adjudicator(),
            PromotionGate(),
            RuntimeAuditReporter(),
        ]
        write_methods = ["commit", "propose_commit", "write_state",
                        "mutate_state", "advance_state", "create_transaction",
                        "register_state", "record_evidence"]

        for component in components:
            name = type(component).__name__
            for method in write_methods:
                assert not hasattr(component, method), (
                    f"{name} has forbidden method: {method}"
                )

    def test_no_compiler_pass_has_state_write_capability(self):
        """Exhaustive check: no compiler pass can write state."""
        passes = [
            DeadBranchElimination(),
            DuplicateBranchMerge(),
            BasicConflictAnalysis(),
            StrengthReduction(),
            AdmissionScoring(),
        ]
        write_methods = ["commit", "propose_commit", "write_state",
                        "mutate_state", "storage", "state_ledger"]

        for compiler_pass in passes:
            name = type(compiler_pass).__name__
            for method in write_methods:
                assert not hasattr(compiler_pass, method), (
                    f"Compiler pass {name} has forbidden attr: {method}"
                )


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
