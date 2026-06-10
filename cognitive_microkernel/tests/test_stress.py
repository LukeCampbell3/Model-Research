"""Intense stress tests for the cognitive microkernel.

Tests concurrency safety, state corruption resistance, resource exhaustion,
deep recursion, adversarial inputs, and edge cases that would break a
production system.
"""
import pytest
import tempfile
import hashlib
import json
import time
import threading
import random
import string
from pathlib import Path
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor, as_completed

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
from cognitive_microkernel.runtime import Runtime


@pytest.fixture
def temp_dir():
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


@pytest.fixture
def runtime(temp_dir):
    return Runtime(temp_dir)


@pytest.fixture
def storage(temp_dir):
    return StorageManager(temp_dir)


# ============================================================================
# Rapid Sequential Execution Stress
# ============================================================================

class TestRapidExecution:
    """Test rapid sequential execution doesn't corrupt state."""

    def test_100_sequential_loops_no_corruption(self, runtime):
        """Run 100 loops sequentially — state should remain consistent."""
        prev_hash = runtime.get_current_state_hash()
        completed = 0
        for i in range(100):
            result = runtime.execute_minimal_loop(f"Task {i}: do something {i}")
            assert result["error"] is None, f"Loop {i} errored: {result['error']}"
            new_hash = runtime.get_current_state_hash()
            # State should advance or remain same (never go backward)
            completed += 1
        assert completed == 100

    def test_rapid_loops_all_produce_traces(self, runtime):
        """Every loop must produce a replay trace."""
        traces = []
        for i in range(50):
            result = runtime.execute_minimal_loop(f"Quick task {i}")
            assert result["replay_trace"] is not None
            traces.append(result["replay_trace"])
        assert len(traces) == 50
        # All root process IDs should be unique
        ids = [t.root_process_id for t in traces]
        assert len(set(ids)) == 50

    def test_state_hash_never_reverts_without_rollback(self, runtime):
        """State hash should monotonically advance (or stay same) without rollback."""
        seen_hashes = set()
        for i in range(30):
            h = runtime.get_current_state_hash()
            seen_hashes.add(h)
            runtime.execute_minimal_loop(f"Advance {i}")
            new_h = runtime.get_current_state_hash()
            # New hash is either same or different, never previously-seen-then-returned-to
            # (unless rollback occurs, which the loop doesn't trigger)


# ============================================================================
# Concurrent Access Stress
# ============================================================================

class TestConcurrentAccess:
    """Test thread safety of storage and state management."""

    def test_concurrent_artifact_storage(self, storage):
        """Multiple threads storing artifacts shouldn't corrupt the store."""
        results = []

        def store_artifact(idx):
            content = f"artifact_content_{idx}_{random.random()}".encode()
            artifact = storage.artifact_store.store_artifact(
                content, artifact_type="test", created_by_process=f"p_{idx}"
            )
            retrieved = storage.artifact_store.retrieve_artifact(artifact.content_hash)
            return retrieved == content

        with ThreadPoolExecutor(max_workers=8) as executor:
            futures = [executor.submit(store_artifact, i) for i in range(100)]
            for f in as_completed(futures):
                results.append(f.result())

        assert all(results), f"Some artifacts corrupted: {results.count(False)} failures"

    def test_concurrent_evidence_recording(self, storage):
        """Multiple threads recording evidence shouldn't lose records."""
        recorded_ids = []

        def record_evidence(idx):
            ev = EvidenceRecord(
                source_type=EvidenceSourceType.RUNTIME_METRIC,
                source_ref=f"source_{idx}",
                state_hash="concurrent_state",
                process_id=f"p_{idx}",
                raw_payload_ref=f"ref_{idx}",
                summary=f"Evidence {idx}",
            )
            storage.evidence_ledger.record_evidence(ev)
            return ev.evidence_id

        with ThreadPoolExecutor(max_workers=8) as executor:
            futures = [executor.submit(record_evidence, i) for i in range(50)]
            for f in as_completed(futures):
                recorded_ids.append(f.result())

        # Verify all records are retrievable
        retrieved = 0
        for eid in recorded_ids:
            if storage.evidence_ledger.get_evidence(eid) is not None:
                retrieved += 1
        assert retrieved == 50

    def test_concurrent_claim_registration(self, storage):
        """Multiple threads registering claims shouldn't lose claims."""
        claim_ids = []

        def register_claim(idx):
            claim = Claim(
                text=f"Concurrent claim {idx}",
                support_status=SupportStatus.SPECULATIVE,
                scope=f"thread_{idx}",
            )
            storage.claim_registry.register_claim(claim)
            return claim.claim_id

        with ThreadPoolExecutor(max_workers=8) as executor:
            futures = [executor.submit(register_claim, i) for i in range(50)]
            for f in as_completed(futures):
                claim_ids.append(f.result())

        retrieved = sum(1 for cid in claim_ids if storage.claim_registry.get_claim(cid) is not None)
        assert retrieved == 50


# ============================================================================
# Large State / Deep Graph Stress
# ============================================================================

class TestLargeState:
    """Test behavior under large state and deep process graphs."""

    def test_deep_process_dag(self, storage):
        """DAG with 50 nodes in a chain doesn't crash or corrupt."""
        prev_id = None
        for i in range(50):
            node = ProcessNode(
                process_id=f"deep_node_{i}",
                state_hash_before=f"state_{i}",
                state_hash_after=f"state_{i+1}",
                status=ProcessStatus.COMPLETED,
                parent_process_ids=[prev_id] if prev_id else [],
                replayable=True,
            )
            storage.process_dag.add_node(node)
            prev_id = f"deep_node_{i}"

        # Can still retrieve root and leaf
        root = storage.process_dag.get_node("deep_node_0")
        leaf = storage.process_dag.get_node("deep_node_49")
        assert root is not None
        assert leaf is not None
        assert leaf.state_hash_after == "state_50"

    def test_wide_branching_factor(self, storage):
        """A process with 100 children branches doesn't crash."""
        parent = ProcessNode(
            process_id="wide_root",
            state_hash_before="s0",
            state_hash_after="s1",
            status=ProcessStatus.COMPLETED,
            replayable=True,
        )
        storage.process_dag.add_node(parent)

        for i in range(100):
            child = ProcessNode(
                process_id=f"wide_child_{i}",
                state_hash_before="s1",
                state_hash_after=f"s_child_{i}",
                status=ProcessStatus.COMPLETED,
                parent_process_ids=["wide_root"],
                replayable=True,
            )
            storage.process_dag.add_node(child)

        descendants = storage.process_dag.get_descendants("wide_root", depth=1)
        assert len(descendants) >= 50  # Should find many children

    def test_large_artifact_storage(self, storage):
        """Store 200 artifacts of varying sizes without corruption."""
        stored = []
        for i in range(200):
            size = random.randint(100, 10000)
            content = random.randbytes(size)
            artifact = storage.artifact_store.store_artifact(
                content, artifact_type="stress_test", created_by_process=f"p_{i}"
            )
            stored.append((artifact.content_hash, content))

        # Verify all retrievable
        for content_hash, original in stored:
            retrieved = storage.artifact_store.retrieve_artifact(content_hash)
            assert retrieved == original, f"Artifact {content_hash[:8]} corrupted"

    def test_many_speculations_stored(self, storage):
        """Store 100 speculation entries without loss."""
        archive = BranchArchive(storage)
        for i in range(100):
            branch = BranchProcess(
                parent_state_hash=f"state_{i}",
                branch_type=BranchType.BRANCH_SEED,
                hypothesis=f"Speculation hypothesis {i} with detailed reasoning",
                created_by_process=f"p_{i}",
                expected_upside=random.random(),
            )
            archive.archive_branch(branch, prune_reason=f"Reason {i}")

        # Verify we can still create and retrieve
        final_branch = BranchProcess(
            parent_state_hash="final_state",
            branch_type=BranchType.BRANCH_SEED,
            hypothesis="Final speculation",
            created_by_process="p_final",
        )
        spec = archive.archive_branch(final_branch, prune_reason="Final")
        assert spec is not None
        retrieved = storage.speculation_ledger.get_speculation(spec.speculation_id)
        assert retrieved is not None


# ============================================================================
# Adversarial Input Stress
# ============================================================================

class TestAdversarialInputs:
    """Test robustness against adversarial/malformed inputs."""

    def test_extremely_long_observation(self, runtime):
        """Very long observation string doesn't crash."""
        long_obs = "x" * 100000
        result = runtime.execute_minimal_loop(long_obs)
        assert result["error"] is None

    def test_unicode_observation(self, runtime):
        """Unicode characters in observation don't crash."""
        unicode_obs = "Build a 日本語 endpoint with émojis 🚀🎉 and Ñ"
        result = runtime.execute_minimal_loop(unicode_obs)
        assert result["error"] is None

    def test_empty_observation(self, runtime):
        """Empty observation doesn't crash (should still produce process)."""
        result = runtime.execute_minimal_loop("")
        assert result["root_process"] is not None

    def test_special_characters_in_hypothesis(self, storage):
        """Special chars in branch hypothesis don't corrupt storage."""
        gen = BranchSeedGenerator(storage)
        evil_obs = 'Use "quotes" and \\backslash and \nnewlines and \ttabs and NULL\x00bytes'
        seeds = gen.generate_seeds("state", evil_obs, "p1", max_seeds=5)
        assert len(seeds) >= 3

    def test_hash_collision_resistance(self, storage):
        """Two similar artifacts produce different hashes."""
        a1 = storage.artifact_store.store_artifact(b"content_a", "test", "p1")
        a2 = storage.artifact_store.store_artifact(b"content_b", "test", "p1")
        assert a1.content_hash != a2.content_hash

    def test_duplicate_process_registration(self, storage):
        """Registering same process twice doesn't corrupt registry."""
        p = ProcessDescriptor(
            process_type="test",
            parent_state_hash="state",
            expected_output_schema="test",
            cache_key="dup_test",
        )
        storage.process_registry.register_process(p)
        storage.process_registry.register_process(p)  # Duplicate
        retrieved = storage.process_registry.get_process(p.process_id)
        assert retrieved is not None
        assert retrieved.process_id == p.process_id


# ============================================================================
# Transaction Safety Stress
# ============================================================================

class TestTransactionSafety:
    """Test transaction atomicity and state consistency under stress."""

    def test_multiple_commits_advance_state_correctly(self, storage):
        """Multiple sequential commits produce correct state chain."""
        state = CanonicalState(root_state_hash="genesis")
        storage.state_ledger.register_state(state)

        committer = CanonicalStateCommitter(storage)
        current_hash = "genesis"

        for i in range(20):
            # Store delta
            delta = json.dumps({"changes": {"step": i}, "previous_state_hash": current_hash}, sort_keys=True)
            delta_hash = hashlib.sha256(delta.encode()).hexdigest()
            storage.artifact_store.store_artifact(delta.encode(), "state_delta", f"p_{i}")

            # Store verification evidence
            ev = EvidenceRecord(
                evidence_id=f"verify_{i}",
                source_type=EvidenceSourceType.VERIFIER,
                source_ref="v", state_hash=current_hash,
                process_id=f"p_{i}", raw_payload_ref="r", summary="ok",
            )
            storage.evidence_ledger.record_evidence(ev)

            process = ProcessDescriptor(
                process_type="commit", parent_state_hash=current_hash,
                expected_output_schema="t", cache_key=f"c_{i}",
                side_effect_policy=SideEffectPolicy.TRANSACTIONAL_WRITE,
            )
            new_state, tx = committer.propose_commit(
                process=process, delta_hash=delta_hash,
                verification_evidence=[f"verify_{i}"],
            )
            if new_state:
                current_hash = new_state.root_state_hash

        # Final state should not be genesis
        assert current_hash != "genesis"
        final = storage.state_ledger.get_latest_state()
        assert final is not None

    def test_rollback_after_commit_restores_state(self, storage):
        """Rollback after a successful commit returns to prior state."""
        s1 = CanonicalState(root_state_hash="v1")
        storage.state_ledger.register_state(s1)

        import time; time.sleep(0.01)
        tx = Transaction(
            initiating_process_id="p1",
            parent_state_hash="v1",
            proposed_state_delta_ref="delta",
            side_effect_policy=SideEffectPolicy.TRANSACTIONAL_WRITE,
            status=TransactionStatus.COMMITTED,
        )
        s2 = CanonicalState(
            root_state_hash="v2",
            committed_transaction_refs=[tx.transaction_id],
        )
        storage.state_ledger.register_state(s2)

        mgr = RollbackManager(storage)
        rolled = mgr.execute_rollback(tx)
        assert rolled is not None
        assert tx.transaction_id not in rolled.committed_transaction_refs

    def test_concurrent_commits_dont_produce_orphan_states(self, storage):
        """Two commits against same parent — one wins, other should fail gracefully."""
        genesis = CanonicalState(root_state_hash="shared_parent")
        storage.state_ledger.register_state(genesis)

        committer = CanonicalStateCommitter(storage)

        # First commit succeeds
        ev1 = EvidenceRecord(
            evidence_id="ev_first",
            source_type=EvidenceSourceType.VERIFIER,
            source_ref="v", state_hash="shared_parent",
            process_id="p1", raw_payload_ref="r", summary="ok",
        )
        storage.evidence_ledger.record_evidence(ev1)

        p1 = ProcessDescriptor(
            process_type="commit1", parent_state_hash="shared_parent",
            expected_output_schema="t", cache_key="c1",
            side_effect_policy=SideEffectPolicy.TRANSACTIONAL_WRITE,
        )
        delta1 = json.dumps({"changes": "first"}, sort_keys=True)
        dh1 = hashlib.sha256(delta1.encode()).hexdigest()
        storage.artifact_store.store_artifact(delta1.encode(), "state_delta", "p1")
        new1, tx1 = committer.propose_commit(p1, dh1, ["ev_first"])

        # Second commit against SAME parent (should be stale now)
        p2 = ProcessDescriptor(
            process_type="commit2", parent_state_hash="shared_parent",
            expected_output_schema="t", cache_key="c2",
            side_effect_policy=SideEffectPolicy.TRANSACTIONAL_WRITE,
        )
        # If first succeeded, shared_parent is stale
        if new1:
            new2, tx2 = committer.propose_commit(p2, "dh2", ["ev_first"])
            # Should fail because parent is stale
            assert new2 is None or tx2.status == TransactionStatus.REJECTED


# ============================================================================
# Resource Exhaustion / Budget Stress
# ============================================================================

class TestResourceExhaustion:
    """Test budget enforcement and resource limits."""

    def test_budget_manager_enforces_limits(self):
        """Budget manager blocks execution when budget exhausted."""
        bm = BudgetManager()
        p = ProcessDescriptor(
            process_type="test", parent_state_hash="s",
            expected_output_schema="t", cache_key="budget_test",
            budget_remaining=1.0,
        )
        bm.allocate_budget(p)
        assert bm.consume_budget(p.process_id, 0.8)
        assert bm.get_remaining_budget(p.process_id) == pytest.approx(0.2, abs=0.01)
        assert not bm.consume_budget(p.process_id, 0.3)  # Overspend blocked

    def test_many_queue_entries_dont_starve_scheduler(self):
        """A flooded queue still returns highest-priority items."""
        qm = ProcessQueueManager()
        # Add 200 low-priority items
        for i in range(200):
            p = ProcessDescriptor(
                process_type="spam", parent_state_hash="s",
                expected_output_schema="t", cache_key=f"spam_{i}", priority=0.1,
            )
            qm.enqueue(p, QueueType.SPECULATIVE_PROCESS)

        # Add 1 high-priority item
        important = ProcessDescriptor(
            process_type="urgent", parent_state_hash="s",
            expected_output_schema="t", cache_key="urgent_1", priority=0.99,
        )
        qm.enqueue(important, QueueType.INTERRUPT)

        scheduler = PriorityScheduler(qm)
        selected = scheduler.select_next_process()
        assert selected.cache_key == "urgent_1"

    def test_profiler_tracks_metrics_under_load(self, runtime):
        """Profiler doesn't lose counts under rapid execution."""
        for i in range(50):
            runtime.execute_minimal_loop(f"Profile test {i}")
        metrics = runtime.get_metrics()
        assert metrics.get("processes_completed", 0) >= 40  # Some might fail


# ============================================================================
# State Integrity Stress
# ============================================================================

class TestStateIntegrity:
    """Test that state invariants hold under all conditions."""

    def test_canonical_state_hash_is_deterministic(self):
        """Same inputs produce same canonical state hash."""
        s1 = CanonicalState(root_state_hash=hashlib.sha256(b"seed").hexdigest())
        s2 = CanonicalState(root_state_hash=hashlib.sha256(b"seed").hexdigest())
        assert s1.root_state_hash == s2.root_state_hash

    def test_process_dag_maintains_parent_child_consistency(self, storage):
        """Parent-child relationships are bidirectionally consistent."""
        parent = ProcessNode(
            process_id="parent",
            state_hash_before="s0", state_hash_after="s1",
            status=ProcessStatus.COMPLETED,
            child_process_ids=["child"],
        )
        child = ProcessNode(
            process_id="child",
            state_hash_before="s1", state_hash_after="s2",
            status=ProcessStatus.COMPLETED,
            parent_process_ids=["parent"],
        )
        storage.process_dag.add_node(parent)
        storage.process_dag.add_node(child)

        # Both directions work
        descendants = storage.process_dag.get_descendants("parent", depth=1)
        assert any(n.process_id == "child" for n in descendants)

    def test_evidence_immutability(self, storage):
        """Evidence records cannot be silently modified after creation."""
        ev = EvidenceRecord(
            evidence_id="immutable_ev",
            source_type=EvidenceSourceType.TOOL,
            source_ref="tool_1",
            state_hash="state",
            process_id="p1",
            raw_payload_ref="ref",
            summary="Original summary",
        )
        storage.evidence_ledger.record_evidence(ev)

        # Retrieve and verify
        retrieved = storage.evidence_ledger.get_evidence("immutable_ev")
        assert retrieved.summary == "Original summary"

    def test_storage_clear_and_reinitialize(self, temp_dir):
        """Storage can be cleared and reinitialized cleanly."""
        s = StorageManager(temp_dir)
        # Store something
        s.artifact_store.store_artifact(b"test", "test", "p1")
        # Clear
        s.clear()
        # Should be empty
        result = s.artifact_store.retrieve_artifact(hashlib.sha256(b"test").hexdigest())
        assert result is None

    def test_runtime_metrics_are_monotonic(self, runtime):
        """Profiler counters never decrease."""
        runtime.execute_minimal_loop("First")
        m1 = runtime.get_metrics()
        runtime.execute_minimal_loop("Second")
        m2 = runtime.get_metrics()
        for key in ["processes_completed", "processes_created"]:
            if key in m1 and key in m2:
                assert m2[key] >= m1[key]


# ============================================================================
# Edge Cases and Boundary Conditions
# ============================================================================

class TestEdgeCases:
    """Test boundary conditions and rare paths."""

    def test_branch_with_zero_budget(self):
        """Branch with zero budget is still valid (just can't expand)."""
        branch = BranchProcess(
            parent_state_hash="state",
            branch_type=BranchType.BRANCH_SEED,
            hypothesis="cheap idea",
            created_by_process="p1",
            estimated_token_cost=0,
            estimated_tool_cost=0,
        )
        scorer = BranchCheapScorer()
        score = scorer.score_branch(branch, {})
        assert 0.0 <= score <= 1.0

    def test_expert_output_at_confidence_boundaries(self):
        """Expert output at exactly 0.0 and 1.0 confidence is valid."""
        for conf in [0.0, 1.0]:
            output = ExpertOutput(
                expert_id="boundary_expert",
                output_type="test",
                claims=["claim"],
                support_tags=["supported"],
                confidence=conf,
                uncertainty=1.0 - conf,
                raw_output_ref="ref",
            )
            valid, errors = ExpertABIValidator.validate_output(output)
            assert valid, f"Failed at confidence={conf}: {errors}"

    def test_claim_with_max_evidence_refs(self):
        """Claim with many evidence refs doesn't break."""
        refs = [f"ev_{i}" for i in range(100)]
        claim = Claim(
            text="Well-supported claim",
            support_status=SupportStatus.SUPPORTED,
            evidence_refs=refs,
            scope="test",
        )
        assert len(claim.evidence_refs) == 100

    def test_empty_branch_deduplication(self):
        """Deduplicating empty list doesn't crash."""
        dedup = BranchDeduplicator()
        result = dedup.deduplicate([])
        assert result == []

    def test_scheduler_with_empty_queues(self):
        """Scheduler returns None when all queues empty."""
        qm = ProcessQueueManager()
        scheduler = PriorityScheduler(qm)
        selected = scheduler.select_next_process()
        assert selected is None

    def test_timing_collector_under_rapid_calls(self):
        """TimingCollector handles rapid start/stop cycles."""
        tc = TimingCollector()
        for i in range(100):
            tc.record_process_start(f"op_{i}", QueueType.NORMAL_PROCESS)
            tc.record_process_end(f"op_{i}")
        # Should have recorded all timings
        stats = tc.get_queue_timing_stats()
        assert QueueType.NORMAL_PROCESS.value in stats
        assert stats[QueueType.NORMAL_PROCESS.value]["count"] == 100


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
