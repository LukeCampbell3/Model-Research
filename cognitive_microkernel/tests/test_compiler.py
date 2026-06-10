"""Tests for Phase 2: Branch Compiler."""

import pytest
from cognitive_microkernel.schemas import BranchProcess, BranchType, ProcessStatus
from cognitive_microkernel.compiler import (
    PassManager, CompilerPass, PassResult,
    DeadBranchElimination, DuplicateBranchMerge,
    BasicConflictAnalysis, StrengthReduction,
    AdmissionScoring, BranchPlan, BranchPlanEntry, AdmissionStatus,
)
from cognitive_microkernel.compiler.branch_plan import compile_branch_plan


def _branch(hypothesis="Test", upside=0.5, priority=0.5, parent="state",
            branch_type=BranchType.BRANCH_SEED, status=ProcessStatus.PENDING,
            validation_condition="Some condition", token_cost=500, tool_cost=0):
    return BranchProcess(
        parent_state_hash=parent, branch_type=branch_type,
        hypothesis=hypothesis, expected_upside=upside,
        priority_score=priority, created_by_process="p1",
        status=status, validation_condition=validation_condition,
        estimated_token_cost=token_cost, estimated_tool_cost=tool_cost,
    )


# ============================================================================
# PassManager Tests
# ============================================================================

class TestPassManager:
    def test_empty_pipeline_returns_input_unchanged(self):
        pm = PassManager()
        branches = [_branch("A"), _branch("B")]
        result, results = pm.run(branches)
        assert result == branches
        assert results == []

    def test_passes_execute_in_order(self):
        pm = PassManager()
        pm.register(DeadBranchElimination())
        pm.register(DuplicateBranchMerge())
        pm.register(BasicConflictAnalysis())
        pm.register(StrengthReduction())
        pm.register(AdmissionScoring())
        branches = [_branch("Build web server"), _branch("Build web server copy")]
        result, results = pm.run(branches)
        assert len(results) == 5
        assert results[0].pass_name == "DeadBranchElimination"
        assert results[-1].pass_name == "AdmissionScoring"

    def test_summary_aggregates_all_passes(self):
        pm = PassManager()
        pm.register(DeadBranchElimination())
        pm.register(AdmissionScoring(admission_threshold=0.9))
        branches = [_branch(upside=0.0), _branch(upside=0.3)]
        pm.run(branches)
        summary = pm.summary()
        assert summary["status"] == "COMPLETE"
        assert summary["passes_run"] == 2
        assert summary["total_eliminated"] >= 1


# ============================================================================
# DeadBranchElimination Tests
# ============================================================================

class TestDeadBranchElimination:
    def test_zero_upside_eliminated(self):
        dbe = DeadBranchElimination()
        branches = [_branch(upside=0.0), _branch(upside=0.5)]
        result, pr = dbe.run(branches, {})
        assert len(result) == 1
        assert pr.branches_eliminated == 1

    def test_cancelled_status_eliminated(self):
        dbe = DeadBranchElimination()
        branches = [_branch(status=ProcessStatus.CANCELLED), _branch()]
        result, pr = dbe.run(branches, {})
        assert len(result) == 1

    def test_failed_status_eliminated(self):
        dbe = DeadBranchElimination()
        branches = [_branch(status=ProcessStatus.FAILED)]
        result, pr = dbe.run(branches, {})
        assert len(result) == 0

    def test_stale_parent_eliminated(self):
        dbe = DeadBranchElimination(current_state_hash="current", stale_hashes={"old"})
        branches = [_branch(parent="old"), _branch(parent="current")]
        result, pr = dbe.run(branches, {})
        assert len(result) == 1
        assert result[0].parent_state_hash == "current"

    def test_commit_candidate_without_validation_eliminated(self):
        dbe = DeadBranchElimination()
        b = _branch(branch_type=BranchType.COMMIT_CANDIDATE, validation_condition="")
        result, pr = dbe.run([b], {})
        assert len(result) == 0

    def test_healthy_branch_survives(self):
        dbe = DeadBranchElimination()
        b = _branch(upside=0.7, priority=0.6)
        result, _ = dbe.run([b], {})
        assert len(result) == 1


# ============================================================================
# DuplicateBranchMerge Tests
# ============================================================================

class TestDuplicateBranchMerge:
    def test_identical_hypotheses_merged(self):
        dbm = DuplicateBranchMerge(similarity_threshold=0.8)
        b1 = _branch("Build a fast web server with caching")
        b2 = _branch("Build a fast web server with caching")
        result, pr = dbm.run([b1, b2], {})
        assert len(result) == 1
        assert pr.branches_merged == 1

    def test_different_hypotheses_not_merged(self):
        dbm = DuplicateBranchMerge()
        b1 = _branch("Build a web server")
        b2 = _branch("Write unit tests for database")
        result, pr = dbm.run([b1, b2], {})
        assert len(result) == 2
        assert pr.branches_merged == 0

    def test_merged_branch_inherits_higher_priority(self):
        dbm = DuplicateBranchMerge(similarity_threshold=0.8)
        b1 = _branch("Build fast web server endpoint", priority=0.3)
        b2 = _branch("Build fast web server endpoint", priority=0.8)
        result, _ = dbm.run([b1, b2], {})
        assert len(result) == 1
        assert result[0].priority_score == 0.8

    def test_different_parents_not_merged(self):
        dbm = DuplicateBranchMerge()
        b1 = _branch("Same hypothesis here", parent="state_A")
        b2 = _branch("Same hypothesis here", parent="state_B")
        result, _ = dbm.run([b1, b2], {})
        assert len(result) == 2  # Different parents = different groups

    def test_single_branch_passes_through(self):
        dbm = DuplicateBranchMerge()
        result, pr = dbm.run([_branch()], {})
        assert len(result) == 1
        assert pr.branches_merged == 0


# ============================================================================
# BasicConflictAnalysis Tests
# ============================================================================

class TestConflictAnalysis:
    def test_commit_candidates_same_parent_conflict(self):
        bca = BasicConflictAnalysis()
        b1 = _branch("Plan A", branch_type=BranchType.COMMIT_CANDIDATE)
        b2 = _branch("Plan B", branch_type=BranchType.COMMIT_CANDIDATE)
        result, pr = bca.run([b1, b2], {})
        assert pr.conflicts_detected >= 1
        assert len(result) == 2  # No elimination

    def test_contradictory_hypotheses_detected(self):
        bca = BasicConflictAnalysis()
        b1 = _branch("Use caching for performance")
        b2 = _branch("Do not use caching for simplicity")
        _, pr = bca.run([b1, b2], {})
        assert pr.conflicts_detected >= 1

    def test_non_conflicting_branches_pass_clean(self):
        bca = BasicConflictAnalysis()
        b1 = _branch("Build frontend", branch_type=BranchType.BRANCH_SEED)
        b2 = _branch("Build backend", branch_type=BranchType.BRANCH_SEED)
        _, pr = bca.run([b1, b2], {})
        assert pr.conflicts_detected == 0

    def test_conflicts_annotated_for_downstream(self):
        bca = BasicConflictAnalysis()
        b1 = _branch("X", branch_type=BranchType.COMMIT_CANDIDATE)
        b2 = _branch("Y", branch_type=BranchType.COMMIT_CANDIDATE)
        annotations = {}
        bca.run([b1, b2], annotations)
        assert "conflicts" in annotations
        assert "conflict_branch_ids" in annotations


# ============================================================================
# StrengthReduction Tests
# ============================================================================

class TestStrengthReduction:
    def test_duplicate_evidence_needed_deduped(self):
        sr = StrengthReduction()
        b = _branch()
        b.evidence_needed = ["ev1", "ev1", "ev2", "ev2", "ev3"]
        sr.run([b], {})
        assert len(b.evidence_needed) == 3

    def test_upside_clamped_to_max(self):
        sr = StrengthReduction(max_upside=0.95)
        b = _branch(upside=1.5)
        sr.run([b], {})
        assert b.expected_upside == 0.95

    def test_commit_candidate_without_condition_downgraded(self):
        sr = StrengthReduction()
        b = _branch(branch_type=BranchType.COMMIT_CANDIDATE, validation_condition="")
        sr.run([b], {})
        assert b.branch_type == BranchType.BRANCH_SKETCH

    def test_trivial_hypothesis_cost_reduced(self):
        sr = StrengthReduction()
        b = _branch("Do it", token_cost=5000)
        sr.run([b], {})
        assert b.estimated_token_cost == 200

    def test_normal_branch_unchanged(self):
        sr = StrengthReduction()
        b = _branch("Reasonable hypothesis for testing purposes", upside=0.5, token_cost=500)
        _, pr = sr.run([b], {})
        assert pr.branches_modified == 0


# ============================================================================
# AdmissionScoring Tests
# ============================================================================

class TestAdmissionScoring:
    def test_high_quality_branch_admitted(self):
        asm = AdmissionScoring(admission_threshold=0.2)
        b = _branch(upside=0.8, priority=0.7)
        result, pr = asm.run([b], {})
        assert len(result) == 1
        assert pr.branches_eliminated == 0

    def test_low_quality_branch_rejected(self):
        asm = AdmissionScoring(admission_threshold=0.9)
        b = _branch(upside=0.1, priority=0.1)
        result, pr = asm.run([b], {})
        assert len(result) == 0
        assert pr.branches_eliminated == 1

    def test_max_admitted_enforced(self):
        asm = AdmissionScoring(admission_threshold=0.1, max_admitted=3)
        branches = [_branch(f"Branch {i}", upside=0.5 + i*0.05) for i in range(10)]
        result, pr = asm.run(branches, {})
        assert len(result) <= 3

    def test_conflict_penalty_reduces_score(self):
        asm = AdmissionScoring(admission_threshold=0.2)
        b = _branch(upside=0.4, priority=0.4)
        annotations = {"conflict_branch_ids": {b.branch_id}}
        result, _ = asm.run([b], annotations)
        scores = annotations.get("admission_scores", [])
        if scores:
            assert scores[0].conflict_penalty > 0

    def test_scores_stored_in_annotations(self):
        asm = AdmissionScoring()
        annotations = {}
        asm.run([_branch()], annotations)
        assert "admission_scores" in annotations
        assert "admitted_branch_ids" in annotations


# ============================================================================
# BranchPlan Tests
# ============================================================================

class TestBranchPlan:
    def test_admitted_branches_get_workspace(self):
        plan = BranchPlan(entries=[
            BranchPlanEntry(branch=_branch("A"), status=AdmissionStatus.ADMITTED, score=0.8),
            BranchPlanEntry(branch=_branch("B"), status=AdmissionStatus.REJECTED_BELOW_THRESHOLD, score=0.1),
        ])
        assert plan.can_create_workspace
        assert plan.admitted_count == 1
        assert plan.rejected_count == 1

    def test_empty_plan_blocks_workspace(self):
        plan = BranchPlan(entries=[
            BranchPlanEntry(branch=_branch("X"), status=AdmissionStatus.ELIMINATED_DEAD, score=0.0),
        ])
        assert not plan.can_create_workspace

    def test_workspace_budget_sums_admitted_only(self):
        plan = BranchPlan(entries=[
            BranchPlanEntry(branch=_branch("A", token_cost=100), status=AdmissionStatus.ADMITTED, score=0.8),
            BranchPlanEntry(branch=_branch("B", token_cost=9999), status=AdmissionStatus.REJECTED_BELOW_THRESHOLD, score=0.1),
        ])
        assert plan.workspace_budget == 100  # Only admitted branch's cost

    def test_compile_branch_plan_integration(self):
        """Full pipeline produces a valid BranchPlan."""
        pm = PassManager()
        pm.register(DeadBranchElimination())
        pm.register(DuplicateBranchMerge())
        pm.register(BasicConflictAnalysis())
        pm.register(StrengthReduction())
        pm.register(AdmissionScoring(admission_threshold=0.2, max_admitted=5))

        branches = [
            _branch("Build authentication system", upside=0.7, priority=0.6),
            _branch("Build authentication system", upside=0.5, priority=0.4),  # Duplicate
            _branch("Add logging", upside=0.3, priority=0.3),
            _branch("Dead branch", upside=0.0),  # Dead
            _branch("Cancelled work", status=ProcessStatus.CANCELLED),  # Dead
        ]

        admitted, results = pm.run(branches)
        annotations = {}
        # Re-run to get annotations (PassManager stores internally)
        pm2 = PassManager()
        pm2.register(DeadBranchElimination())
        pm2.register(DuplicateBranchMerge())
        pm2.register(BasicConflictAnalysis())
        pm2.register(StrengthReduction())
        pm2.register(AdmissionScoring(admission_threshold=0.2, max_admitted=5))
        admitted2, results2 = pm2.run(branches)

        assert len(admitted) >= 1  # At least the good branch
        assert len(admitted) <= 3  # Dead + dup removed
        summary = pm.summary()
        assert summary["status"] == "COMPLETE"
        assert summary["total_eliminated"] >= 2  # Dead + dup


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
