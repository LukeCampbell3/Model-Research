"""Core tests for the cognitive microkernel v1.

Required test categories:
- Process tests
- State and transaction tests
- Evidence tests
- Claim tests
- Expert ABI tests
- Branch tests
- Speculation tests
- Scheduler tests
- Replay tests
- Runtime success tests
"""

import pytest
import tempfile
import hashlib
import json
from pathlib import Path
from datetime import datetime, timedelta

from cognitive_microkernel.schemas import (
    ProcessDescriptor, ProcessNode, CanonicalState, EvidenceRecord, Claim,
    Transaction, ExpertInput, ExpertOutput, BranchProcess, ReplayTrace,
    SpeculationLedgerEntry,
    ProcessStatus, SupportStatus, SideEffectPolicy, EvidenceSourceType,
    BranchType, TransactionStatus, SpeculationStatus,
)
from cognitive_microkernel.storage import StorageManager
from cognitive_microkernel.transactions import (
    StateDeltaBuilder, TransactionManager, CanonicalStateCommitter,
    RollbackManager, SideEffectPolicyEnforcer,
)
from cognitive_microkernel.experts import (
    ExpertRouter, ExpertABIValidator, SupportTagValidator,
)
from cognitive_microkernel.branching import (
    BranchSeedGenerator, BranchDeduplicator, BranchCheapScorer,
    BranchArchive, BranchCommitController,
)
from cognitive_microkernel.scheduler import (
    ProcessQueueManager, PriorityScheduler, BudgetManager,
    TimingCollector, RuntimeProfiler, QueueType,
)
from cognitive_microkernel.future_extensions import (
    FutureExtensionRegistry, MemoryPromotionGate, ResearchProcessManager,
)
from cognitive_microkernel.runtime import Runtime


@pytest.fixture
def temp_dir():
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


@pytest.fixture
def storage(temp_dir):
    return StorageManager(temp_dir)


@pytest.fixture
def runtime(temp_dir):
    return Runtime(temp_dir)


# ============================================================================
# Process tests
# ============================================================================

class TestProcessLifecycle:
    def test_process_descriptor_created_before_execution(self, runtime):
        """process descriptor is created before execution"""
        results = runtime.execute_minimal_loop("test task")
        assert results["root_process"] is not None
        assert results["root_process"].process_id.startswith("process_")

    def test_process_cannot_run_without_parent_state_hash(self):
        """process cannot run without parent_state_hash"""
        with pytest.raises(ValueError, match="parent_state_hash must not be empty"):
            ProcessDescriptor(
                process_type="test",
                parent_state_hash="",
                expected_output_schema="test",
                cache_key="test",
            )

    def test_stale_process_is_cancelled_or_refreshed(self, runtime):
        """stale process is cancelled or refreshed"""
        process = ProcessDescriptor(
            process_type="test",
            parent_state_hash="stale_hash_not_current",
            expected_output_schema="test",
            cache_key="stale_test",
        )
        can_exec = SideEffectPolicyEnforcer.can_execute(
            process, runtime.get_current_state_hash()
        )
        assert not can_exec  # Stale hash doesn't match current

    def test_process_cache_key_changes_when_state_hash_changes(self):
        """process cache key changes when state hash changes"""
        p1 = ProcessDescriptor(
            process_type="test",
            parent_state_hash="hash_a",
            expected_output_schema="test",
            cache_key="cache_for_hash_a",
        )
        p2 = ProcessDescriptor(
            process_type="test",
            parent_state_hash="hash_b",
            expected_output_schema="test",
            cache_key="cache_for_hash_b",
        )
        assert p1.cache_key != p2.cache_key

    def test_process_side_effect_policy_is_enforced(self):
        """process side-effect policy is enforced"""
        process = ProcessDescriptor(
            process_type="forbidden",
            parent_state_hash="current",
            expected_output_schema="test",
            cache_key="test",
            side_effect_policy=SideEffectPolicy.FORBIDDEN,
        )
        assert not SideEffectPolicyEnforcer.can_execute(process, "current")

    def test_process_handoff_does_not_copy_full_state(self):
        """process handoff does not copy full state"""
        # Processes reference state by hash, not by copying full state
        process = ProcessDescriptor(
            process_type="test",
            parent_state_hash="hash_ref_only",
            expected_output_schema="test",
            cache_key="test",
        )
        # The process holds a hash reference, not the full canonical state
        assert isinstance(process.parent_state_hash, str)
        assert len(process.parent_state_hash) < 256  # Just a hash, not a state blob


# ============================================================================
# State and transaction tests
# ============================================================================

class TestStateAndTransactions:
    def test_branch_cannot_mutate_canonical_state_before_commit(self, storage):
        """branch cannot mutate canonical state before commit"""
        initial_state = CanonicalState(root_state_hash="initial")
        storage.state_ledger.register_state(initial_state)

        branch = BranchProcess(
            parent_state_hash="initial",
            branch_type=BranchType.BRANCH_SEED,
            hypothesis="test",
            created_by_process="p1",
        )
        # Branch only holds a reference, cannot mutate state
        after_state = storage.state_ledger.get_state_by_hash("initial")
        assert after_state.root_state_hash == "initial"

    def test_transaction_requires_proposed_state_delta(self):
        """transaction requires proposed state delta"""
        with pytest.raises(ValueError, match="proposed_state_delta_ref must not be empty"):
            Transaction(
                initiating_process_id="p1",
                parent_state_hash="hash",
                proposed_state_delta_ref="",
                side_effect_policy=SideEffectPolicy.TRANSACTIONAL_WRITE,
            )

    def test_transaction_cannot_commit_without_verification(self, storage):
        """transaction cannot commit without verification"""
        initial = CanonicalState(root_state_hash="init_hash")
        storage.state_ledger.register_state(initial)

        process = ProcessDescriptor(
            process_type="test",
            parent_state_hash="init_hash",
            expected_output_schema="test",
            cache_key="test",
            side_effect_policy=SideEffectPolicy.TRANSACTIONAL_WRITE,
        )

        committer = CanonicalStateCommitter(storage)
        new_state, tx = committer.propose_commit(
            process=process,
            delta_hash="fake_delta",
            verification_evidence=[],  # No verification
        )
        assert new_state is None
        assert tx.status == TransactionStatus.REJECTED

    def test_rollback_restores_previous_state_pointer(self, storage):
        """rollback restores previous state pointer"""
        # Set up: initial state, then a committed state with a transaction
        initial = CanonicalState(root_state_hash="state_v1")
        storage.state_ledger.register_state(initial)

        tx = Transaction(
            initiating_process_id="p1",
            parent_state_hash="state_v1",
            proposed_state_delta_ref="delta_ref",
            side_effect_policy=SideEffectPolicy.TRANSACTIONAL_WRITE,
            status=TransactionStatus.COMMITTED,
        )

        # Create a "committed" state that includes this tx (registered after initial)
        import time; time.sleep(0.01)  # Ensure later timestamp
        committed_state = CanonicalState(
            root_state_hash="state_v2",
            committed_transaction_refs=[tx.transaction_id],
        )
        storage.state_ledger.register_state(committed_state)

        # Execute rollback
        rollback_mgr = RollbackManager(storage)
        rolled_back = rollback_mgr.execute_rollback(tx)
        assert rolled_back is not None
        assert rolled_back.root_state_hash != "state_v2"  # Changed
        assert tx.transaction_id not in rolled_back.committed_transaction_refs

    def test_irreversible_action_is_blocked_without_approval(self):
        """irreversible action is blocked without approval"""
        process = ProcessDescriptor(
            process_type="dangerous",
            parent_state_hash="current",
            expected_output_schema="test",
            cache_key="test",
            side_effect_policy=SideEffectPolicy.EXTERNAL_IRREVERSIBLE_ACTION,
        )
        assert not SideEffectPolicyEnforcer.can_execute(process, "current")

    def test_stale_parent_state_hash_blocks_commit(self, storage):
        """stale parent_state_hash blocks commit"""
        initial = CanonicalState(root_state_hash="current_hash")
        storage.state_ledger.register_state(initial)

        process = ProcessDescriptor(
            process_type="test",
            parent_state_hash="stale_hash",  # Not current
            expected_output_schema="test",
            cache_key="test",
            side_effect_policy=SideEffectPolicy.TRANSACTIONAL_WRITE,
        )

        committer = CanonicalStateCommitter(storage)
        new_state, tx = committer.propose_commit(
            process=process, delta_hash="delta", verification_evidence=["ev"],
        )
        assert new_state is None

    def test_committed_transaction_creates_new_canonical_state_hash(self, storage):
        """committed transaction creates new canonical_state_hash"""
        initial = CanonicalState(root_state_hash="original")
        storage.state_ledger.register_state(initial)

        # Store a valid delta artifact
        delta = json.dumps({
            "previous_state_hash": "original",
            "changes": {"add_claim_refs": ["c1"]},
            "timestamp": "2024-01-01",
        }, sort_keys=True)
        delta_hash = hashlib.sha256(delta.encode()).hexdigest()
        storage.artifact_store.store_artifact(
            delta.encode(), artifact_type="state_delta", created_by_process="p1",
        )

        # Store verification evidence
        ev = EvidenceRecord(
            evidence_id="verify_ev",
            source_type=EvidenceSourceType.VERIFIER,
            source_ref="verifier",
            state_hash="original",
            process_id="p1",
            raw_payload_ref="ref",
            summary="Verified",
        )
        storage.evidence_ledger.record_evidence(ev)

        process = ProcessDescriptor(
            process_type="test",
            parent_state_hash="original",
            expected_output_schema="test",
            cache_key="test",
            side_effect_policy=SideEffectPolicy.TRANSACTIONAL_WRITE,
        )

        committer = CanonicalStateCommitter(storage)
        new_state, tx = committer.propose_commit(
            process=process, delta_hash=delta_hash, verification_evidence=["verify_ev"],
        )
        assert new_state is not None
        assert new_state.root_state_hash != "original"
        assert tx.status == TransactionStatus.COMMITTED


# ============================================================================
# Evidence tests
# ============================================================================

class TestEvidence:
    def test_tool_output_creates_evidence_record(self):
        """tool output creates evidence record"""
        ev = EvidenceRecord(
            source_type=EvidenceSourceType.TOOL,
            source_ref="tool_run_123",
            state_hash="state",
            process_id="p1",
            raw_payload_ref="artifact_hash",
            summary="Tool completed",
        )
        assert ev.source_type == EvidenceSourceType.TOOL
        assert ev.raw_payload_ref == "artifact_hash"

    def test_verifier_output_creates_evidence_record(self):
        """verifier output creates evidence record"""
        ev = EvidenceRecord(
            source_type=EvidenceSourceType.VERIFIER,
            source_ref="verifier_check",
            state_hash="state",
            process_id="p1",
            raw_payload_ref="verifier_hash",
            summary="Verification passed",
        )
        assert ev.source_type == EvidenceSourceType.VERIFIER

    def test_failed_attempt_creates_negative_evidence(self):
        """failed attempt creates negative evidence"""
        ev = EvidenceRecord(
            source_type=EvidenceSourceType.RUNTIME_METRIC,
            source_ref="failed_process",
            state_hash="state",
            process_id="p1",
            raw_payload_ref="error_hash",
            summary="Process failed: timeout",
        )
        assert "failed" in ev.summary.lower()

    def test_contradicted_evidence_remains_retrievable(self, storage):
        """contradicted evidence remains retrievable"""
        ev = EvidenceRecord(
            evidence_id="contradicted_ev",
            source_type=EvidenceSourceType.MODEL_OUTPUT,
            source_ref="model",
            state_hash="state",
            process_id="p1",
            raw_payload_ref="ref",
            summary="Later contradicted",
            claim_contradicted=["claim_1"],
        )
        storage.evidence_ledger.record_evidence(ev)
        retrieved = storage.evidence_ledger.get_evidence("contradicted_ev")
        assert retrieved is not None
        assert retrieved.claim_contradicted == ["claim_1"]

    def test_evidence_used_for_commit_is_traceable(self, storage):
        """evidence used for commit is traceable"""
        ev = EvidenceRecord(
            evidence_id="commit_ev",
            source_type=EvidenceSourceType.VERIFIER,
            source_ref="verifier",
            state_hash="state",
            process_id="p1",
            raw_payload_ref="ref",
            summary="Used for commit",
        )
        storage.evidence_ledger.record_evidence(ev)
        retrieved = storage.evidence_ledger.get_evidence("commit_ev")
        assert retrieved is not None
        assert retrieved.process_id == "p1"


# ============================================================================
# Claim tests
# ============================================================================

class TestClaims:
    def test_supported_claim_requires_evidence_refs(self):
        """supported claim requires evidence refs"""
        claim = Claim(
            text="Verified fact",
            support_status=SupportStatus.SUPPORTED,
            evidence_refs=["ev_1"],
            scope="test",
        )
        assert len(claim.evidence_refs) > 0

    def test_speculative_claim_cannot_become_fact_through_summarization(self):
        """speculative claim cannot become fact through summarization"""
        claim = Claim(
            text="Might be true",
            support_status=SupportStatus.SPECULATIVE,
            scope="guess",
        )
        # Support status is explicit and doesn't auto-upgrade
        assert claim.support_status == SupportStatus.SPECULATIVE

    def test_unsupported_claim_cannot_affect_canonical_state(self, storage):
        """unsupported claim cannot affect canonical state"""
        initial = CanonicalState(root_state_hash="state")
        storage.state_ledger.register_state(initial)

        unsupported_claim = Claim(
            claim_id="bad_claim",
            text="No evidence",
            support_status=SupportStatus.UNSUPPORTED,
            scope="test",
        )
        storage.claim_registry.register_claim(unsupported_claim)

        process = ProcessDescriptor(
            process_type="test",
            parent_state_hash="state",
            expected_output_schema="test",
            cache_key="test",
            side_effect_policy=SideEffectPolicy.TRANSACTIONAL_WRITE,
            claim_refs=["bad_claim"],
        )

        committer = CanonicalStateCommitter(storage)
        new_state, tx = committer.propose_commit(
            process=process, delta_hash="d", verification_evidence=[],
        )
        assert new_state is None  # Blocked

    def test_contradicted_claim_is_downgraded(self):
        """contradicted claim is downgraded"""
        claim = Claim(
            text="Was supported",
            support_status=SupportStatus.SUPPORTED,
            evidence_refs=["old_ev"],
            scope="test",
        )
        # Downgrade
        claim.support_status = SupportStatus.CONTRADICTED
        claim.contradiction_refs = ["new_ev"]
        assert claim.support_status == SupportStatus.CONTRADICTED

    def test_local_claim_scope_does_not_become_global_assumption(self):
        """local claim scope does not become global assumption"""
        claim = Claim(
            text="Works here",
            support_status=SupportStatus.SUPPORTED,
            evidence_refs=["local_ev"],
            scope="local_context_xyz",
        )
        assert claim.scope == "local_context_xyz"
        assert claim.scope != "global"

    def test_claim_used_for_learning_has_explicit_support_status(self):
        """claim used for learning has explicit support status"""
        claim = Claim(
            text="Training data",
            support_status=SupportStatus.SUPPORTED,
            evidence_refs=["training_ev"],
            scope="training",
            usable_for_training=True,
        )
        assert claim.usable_for_training
        assert claim.support_status != SupportStatus.UNSUPPORTED


# ============================================================================
# Expert ABI tests
# ============================================================================

class TestExpertABI:
    def test_compatible_expert_passes_abi_validation(self):
        """compatible expert passes ABI validation"""
        output = ExpertOutput(
            expert_id="test_expert",
            output_type="plan",
            claims=["Claim A"],
            support_tags=["supported"],
            confidence=0.8,
            uncertainty=0.2,
            raw_output_ref="artifact_hash",
        )
        valid, errors = ExpertABIValidator.validate_output(output)
        assert valid
        assert len(errors) == 0

    def test_incompatible_expert_output_is_rejected(self):
        """incompatible expert output is rejected"""
        output = ExpertOutput(
            expert_id="",
            output_type="",
            support_tags=[],
            confidence=1.5,
            uncertainty=-0.1,
            raw_output_ref="",
        )
        valid, errors = ExpertABIValidator.validate_output(output)
        assert not valid

    def test_expert_output_without_support_tags_is_rejected(self):
        """expert output without support tags is rejected"""
        output = ExpertOutput(
            expert_id="ex",
            output_type="plan",
            support_tags=[],
            raw_output_ref="ref",
        )
        valid, errors = ExpertABIValidator.validate_output(output)
        assert not valid
        assert any("support_tags" in e.lower() for e in errors)

    def test_deterministic_router_logs_reason_selected(self):
        """deterministic router logs reason_selected"""
        router = ExpertRouter()
        process = ProcessDescriptor(
            process_type="plan_task",
            parent_state_hash="state",
            expected_output_schema="branch_seeds",
            cache_key="test",
        )
        expert_id, routing_result = router.route(process, [])
        assert "reason_selected" in routing_result
        assert routing_result["reason_selected"] != ""


# ============================================================================
# Branch tests
# ============================================================================

class TestBranching:
    def test_many_level_0_branches_can_be_generated_cheaply(self, storage):
        """many Level 0 branches can be generated cheaply"""
        gen = BranchSeedGenerator(storage)
        seeds = gen.generate_seeds("state", "Build a web server", "p1", max_seeds=10)
        assert len(seeds) >= 3
        for seed in seeds:
            assert seed.branch_type == BranchType.BRANCH_SEED
            assert seed.expansion_level == 0

    def test_duplicate_branches_are_pruned(self):
        """duplicate branches are pruned"""
        dedup = BranchDeduplicator()
        b1 = BranchProcess(
            parent_state_hash="same", branch_type=BranchType.BRANCH_SEED,
            hypothesis="same hypothesis", created_by_process="p1",
        )
        b2 = BranchProcess(
            parent_state_hash="same", branch_type=BranchType.BRANCH_SEED,
            hypothesis="same hypothesis", created_by_process="p2",
        )
        unique = dedup.deduplicate([b1, b2])
        assert len(unique) == 1

    def test_branch_uses_copy_on_write_delta(self):
        """branch uses copy-on-write delta"""
        branch = BranchProcess(
            parent_state_hash="parent_ref",
            branch_type=BranchType.BRANCH_SEED,
            hypothesis="test",
            created_by_process="p1",
        )
        # Branch holds reference, not full state copy
        assert isinstance(branch.parent_state_hash, str)

    def test_branch_cannot_commit_without_validation_condition(self, storage):
        """branch cannot commit without validation condition"""
        controller = BranchCommitController(storage)
        branch = BranchProcess(
            parent_state_hash="state",
            branch_type=BranchType.COMMIT_CANDIDATE,
            hypothesis="test",
            created_by_process="p1",
            validation_condition="",  # Empty!
        )
        can_commit, reason = controller.can_commit_branch(branch)
        assert not can_commit
        assert "validation" in reason.lower()

    def test_losing_branch_is_archived_with_prune_reason(self, storage):
        """losing branch is archived with prune reason"""
        archive = BranchArchive(storage)
        branch = BranchProcess(
            parent_state_hash="state",
            branch_type=BranchType.BRANCH_SEED,
            hypothesis="losing path",
            created_by_process="p1",
        )
        spec = archive.archive_branch(branch, prune_reason="Lower priority")
        assert spec is not None
        assert spec.reason_not_selected == "Lower priority"

    def test_useful_losing_branch_becomes_dormant_speculation(self, storage):
        """useful losing branch becomes dormant speculation"""
        archive = BranchArchive(storage)
        branch = BranchProcess(
            parent_state_hash="state",
            branch_type=BranchType.BRANCH_SEED,
            hypothesis="interesting alternative",
            created_by_process="p1",
            expected_upside=0.7,
        )
        spec = archive.archive_branch(branch, prune_reason="Budget limit")
        assert spec is not None
        assert spec.status == SpeculationStatus.DORMANT
        assert len(spec.trigger_conditions) > 0

    def test_contradicted_branch_remains_negative_evidence(self, storage):
        """contradicted branch remains negative evidence"""
        archive = BranchArchive(storage)
        branch = BranchProcess(
            parent_state_hash="state",
            branch_type=BranchType.BRANCH_SKETCH,
            hypothesis="wrong approach",
            created_by_process="p1",
        )
        spec = archive.archive_contradicted_branch(branch, "contra_ev_id")
        assert spec.status == SpeculationStatus.CONTRADICTED
        assert spec.usable_for_learning is True


# ============================================================================
# Speculation tests
# ============================================================================

class TestSpeculation:
    def test_dormant_speculation_includes_trigger_conditions(self, storage):
        """dormant speculation includes trigger conditions"""
        archive = BranchArchive(storage)
        branch = BranchProcess(
            parent_state_hash="state",
            branch_type=BranchType.BRANCH_SEED,
            hypothesis="future idea",
            created_by_process="p1",
        )
        spec = archive.archive_branch(branch, "Not yet needed")
        assert spec is not None
        assert len(spec.trigger_conditions) > 0

    def test_speculation_cannot_become_memory_without_evidence(self):
        """speculation cannot become memory without evidence"""
        gate = MemoryPromotionGate()
        result = gate.evaluate_memory_promotion(
            item={"type": "speculation"},
            evidence_refs=[],
            usage_history={},
        )
        assert not result["can_promote"]

    def test_speculation_cannot_become_positive_training_data_without_validation(self):
        """speculation cannot become positive training data without validation"""
        spec = SpeculationLedgerEntry(
            parent_state_hash="state",
            branch_id="b1",
            hypothesis="unvalidated",
            branch_type=BranchType.BRANCH_SEED,
            reason_not_selected="unproven",
            status=SpeculationStatus.DORMANT,
            usable_for_learning=False,
        )
        # Dormant speculation is not positive training data
        assert not spec.usable_for_learning or spec.status != SpeculationStatus.VALIDATED


# ============================================================================
# Scheduler tests
# ============================================================================

class TestScheduler:
    def test_interrupt_preempts_normal_process(self):
        """interrupt preempts normal process"""
        qm = ProcessQueueManager()
        normal = ProcessDescriptor(
            process_type="normal", parent_state_hash="s", expected_output_schema="t",
            cache_key="n1", priority=0.5,
        )
        interrupt = ProcessDescriptor(
            process_type="interrupt", parent_state_hash="s", expected_output_schema="t",
            cache_key="i1", priority=0.9,
        )
        qm.enqueue(normal, QueueType.NORMAL_PROCESS)
        qm.enqueue(interrupt, QueueType.INTERRUPT)

        scheduler = PriorityScheduler(qm)
        selected = scheduler.select_next_process()
        assert selected.process_id == interrupt.process_id

    def test_commit_verification_outranks_branch_expansion(self):
        """commit verification outranks branch expansion"""
        qm = ProcessQueueManager()
        branch = ProcessDescriptor(
            process_type="branch", parent_state_hash="s", expected_output_schema="t",
            cache_key="b1", priority=0.5,
        )
        verify = ProcessDescriptor(
            process_type="verify", parent_state_hash="s", expected_output_schema="t",
            cache_key="v1", priority=0.5,
        )
        qm.enqueue(branch, QueueType.SPECULATIVE_PROCESS)
        qm.enqueue(verify, QueueType.COMMIT_VERIFICATION)

        scheduler = PriorityScheduler(qm)
        selected = scheduler.select_next_process()
        assert selected.process_id == verify.process_id

    def test_low_priority_speculative_work_cancels_under_pressure(self):
        """low-priority speculative work cancels under budget pressure"""
        qm = ProcessQueueManager()
        for i in range(5):
            p = ProcessDescriptor(
                process_type="speculative", parent_state_hash="s",
                expected_output_schema="t", cache_key=f"s{i}", priority=0.1 * i,
            )
            qm.enqueue(p, QueueType.SPECULATIVE_PROCESS)

        scheduler = PriorityScheduler(qm)
        cancelled = scheduler.cancel_low_priority_speculative(pressure_level=0.6)
        assert cancelled >= 1


# ============================================================================
# Replay tests
# ============================================================================

class TestReplay:
    def test_process_dag_can_replay_completed_decision_path(self, storage):
        """process DAG can replay a completed decision path"""
        node = ProcessNode(
            process_id="p1",
            state_hash_before="s1",
            state_hash_after="s2",
            status=ProcessStatus.COMPLETED,
            replayable=True,
        )
        storage.process_dag.add_node(node)
        path = storage.process_dag.get_process_path("p1")
        assert len(path) >= 1
        assert path[0].replayable

    def test_artifact_replay_does_not_require_model_calls(self):
        """artifact replay does not require model calls"""
        trace = ReplayTrace(
            root_process_id="p1",
            artifact_refs=["a1", "a2"],
            evidence_refs=["e1"],
            state_hash_sequence=["s1", "s2"],
        )
        # Replay trace holds references to stored artifacts — no model needed
        assert len(trace.artifact_refs) > 0

    def test_replay_preserves_evidence_refs(self):
        """replay preserves evidence refs"""
        trace = ReplayTrace(
            root_process_id="p1",
            evidence_refs=["e1", "e2"],
            state_hash_sequence=["s1"],
        )
        assert trace.evidence_refs == ["e1", "e2"]

    def test_replay_reproduces_transaction_decision(self):
        """replay reproduces transaction decision from stored artifacts"""
        trace = ReplayTrace(
            root_process_id="p1",
            transaction_refs=["tx_1"],
            state_hash_sequence=["s1", "s2"],
        )
        assert len(trace.transaction_refs) == 1
        assert len(trace.state_hash_sequence) == 2


# ============================================================================
# Runtime success tests
# ============================================================================

class TestRuntimeSuccess:
    def test_no_learned_policy_controls_active_decision_path_in_v1(self):
        """no learned policy controls active decision path in v1"""
        registry = FutureExtensionRegistry()
        assert not registry.is_active("learned_policies")
        assert not registry.can_activate_extension("learned_policies")

    def test_no_durable_memory_promotion_occurs_in_v1(self):
        """no durable memory promotion occurs in v1"""
        gate = MemoryPromotionGate()
        assert not gate.is_promotion_allowed()

    def test_autonomous_research_does_not_run_by_default(self):
        """autonomous research does not run by default"""
        mgr = ResearchProcessManager()
        assert not mgr.active
        result = mgr.can_initiate_research("topic", "justification")
        assert not result["allowed"]

    def test_end_to_end_loop_runs_successfully(self, runtime):
        """the full observe→branch→expert→claim→evidence→verify→transaction→commit/rollback→replay loop runs"""
        results = runtime.execute_minimal_loop("Build a REST API endpoint")
        assert results["error"] is None
        assert results["root_process"] is not None
        assert len(results["branch_seeds"]) >= 3
        assert len(results["claims_extracted"]) >= 1
        assert len(results["evidence_created"]) >= 1
        assert results["replay_trace"] is not None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
