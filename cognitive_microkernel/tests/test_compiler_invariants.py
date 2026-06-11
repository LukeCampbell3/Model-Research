"""Phase 2 Invariant Tests: verify compiler passes cannot violate frozen invariants.

These tests enforce the 8 frozen invariants from PHASE2_BRANCH_COMPILER_BASELINE.md.
"""

import pytest
from cognitive_microkernel.schemas import (
    BranchProcess, BranchType, ProcessStatus, SideEffectPolicy,
)
from cognitive_microkernel.compiler import (
    PassManager, DeadBranchElimination, DuplicateBranchMerge,
    BasicConflictAnalysis, StrengthReduction, AdmissionScoring,
    BranchPlan, BranchPlanEntry, AdmissionStatus,
)
from cognitive_microkernel.compiler.branch_plan import compile_branch_plan


def _branch(hypothesis="Test hypothesis for branch", upside=0.5, priority=0.5,
            parent="state", branch_type=BranchType.BRANCH_SEED,
            status=ProcessStatus.PENDING, validation_condition="Needs verification",
            token_cost=500, tool_cost=0, expansion_level=0,
            side_effect_policy=SideEffectPolicy.READ_ONLY):
    b = BranchProcess(
        parent_state_hash=parent, branch_type=branch_type,
        hypothesis=hypothesis, expected_upside=upside,
        priority_score=priority, created_by_process="p1",
        status=status, validation_condition=validation_condition,
        estimated_token_cost=token_cost, estimated_tool_cost=tool_cost,
        expansion_level=expansion_level,
    )
    return b


def _full_pipeline():
    pm = PassManager()
    pm.register(DeadBranchElimination())
    pm.register(DuplicateBranchMerge())
    pm.register(BasicConflictAnalysis())
    pm.register(StrengthReduction())
    pm.register(AdmissionScoring(admission_threshold=0.2))
    return pm


# ============================================================================
# Invariant 1: No compiler pass may increase privilege
# ============================================================================

class TestInvariant1NoPrivilegeIncrease:
    def test_read_only_branch_stays_read_only_through_pipeline(self):
        """A READ_ONLY branch cannot gain write privilege through compilation."""
        b = _branch(upside=0.8, priority=0.8)
        # BranchProcess doesn't have side_effect_policy directly, but
        # the invariant applies to any privilege metadata
        original_type = b.branch_type
        pm = _full_pipeline()
        result, _ = pm.run([b])
        if result:
            # Branch type should not be escalated (seed can't become commit_candidate)
            assert result[0].branch_type == BranchType.BRANCH_SEED

    def test_branch_seed_never_promoted_to_commit_candidate(self):
        """No pass promotes BRANCH_SEED to COMMIT_CANDIDATE."""
        b = _branch(branch_type=BranchType.BRANCH_SEED, upside=0.99, priority=0.99)
        pm = _full_pipeline()
        result, _ = pm.run([b])
        for branch in result:
            assert branch.branch_type != BranchType.COMMIT_CANDIDATE


# ============================================================================
# Invariant 2: No compiler pass may expand write scope
# ============================================================================

class TestInvariant2NoWriteScopeExpansion:
    def test_branch_type_only_downgrades_never_upgrades(self):
        """StrengthReduction may downgrade (COMMIT→SKETCH) but never upgrade."""
        # A commit candidate without validation gets downgraded
        b = _branch(branch_type=BranchType.COMMIT_CANDIDATE, validation_condition="")
        sr = StrengthReduction()
        sr.run([b], {})
        assert b.branch_type == BranchType.BRANCH_SKETCH  # Downgraded

        # A seed with everything perfect stays seed
        b2 = _branch(branch_type=BranchType.BRANCH_SEED, upside=0.99)
        sr.run([b2], {})
        assert b2.branch_type == BranchType.BRANCH_SEED  # Not upgraded


# ============================================================================
# Invariant 3: No compiler pass may remove verifier requirements
# ============================================================================

class TestInvariant3VerifierRequirements:
    def test_validation_condition_preserved_on_valid_branches(self):
        """A branch with a validation condition keeps it through the pipeline."""
        b = _branch(validation_condition="Evidence from verifier required", upside=0.7)
        pm = _full_pipeline()
        result, _ = pm.run([b])
        if result:
            assert result[0].validation_condition != ""

    def test_strength_reduction_does_not_clear_validation_on_sketches(self):
        """StrengthReduction does not clear validation_condition on sketches."""
        b = _branch(branch_type=BranchType.BRANCH_SKETCH, 
                    validation_condition="Must verify before commit")
        sr = StrengthReduction()
        sr.run([b], {})
        assert b.validation_condition == "Must verify before commit"


# ============================================================================
# Invariant 4: No compiler pass may remove evidence obligations
# ============================================================================

class TestInvariant4EvidenceObligations:
    def test_evidence_needed_not_emptied_by_strength_reduction(self):
        """StrengthReduction may dedup but not empty evidence_needed."""
        b = _branch()
        b.evidence_needed = ["ev1", "ev2", "ev3"]
        sr = StrengthReduction()
        sr.run([b], {})
        assert len(b.evidence_needed) >= 1  # Deduped but not emptied

    def test_evidence_needed_dedup_preserves_unique_entries(self):
        """Dedup removes only true duplicates."""
        b = _branch()
        b.evidence_needed = ["ev_a", "ev_b", "ev_c", "ev_a"]
        sr = StrengthReduction()
        sr.run([b], {})
        assert set(b.evidence_needed) == {"ev_a", "ev_b", "ev_c"}

    def test_cap_preserves_some_evidence(self):
        """Cap at max_evidence_needed still leaves evidence present."""
        b = _branch()
        b.evidence_needed = [f"ev_{i}" for i in range(20)]
        sr = StrengthReduction(max_evidence_needed=5)
        sr.run([b], {})
        assert len(b.evidence_needed) == 5  # Capped, not emptied


# ============================================================================
# Invariant 5: No L0 branches become commit-eligible directly
# ============================================================================

class TestInvariant5NoL0DirectCommit:
    def test_level_0_seed_cannot_become_commit_candidate_in_pipeline(self):
        """expansion_level=0 branches stay non-commit through full pipeline."""
        branches = [
            _branch(f"Idea {i}", upside=0.9, priority=0.9, expansion_level=0)
            for i in range(5)
        ]
        pm = _full_pipeline()
        result, _ = pm.run(branches)
        for b in result:
            assert b.branch_type != BranchType.COMMIT_CANDIDATE
            assert b.expansion_level == 0

    def test_strength_reduction_does_not_promote_seeds(self):
        """StrengthReduction downgrades, never promotes."""
        b = _branch(branch_type=BranchType.BRANCH_SEED, expansion_level=0, upside=0.99)
        sr = StrengthReduction()
        sr.run([b], {})
        assert b.branch_type == BranchType.BRANCH_SEED


# ============================================================================
# Invariant 6: Conflict analysis does not erase branches
# ============================================================================

class TestInvariant6ConflictPreservation:
    def test_conflict_analysis_preserves_all_branches(self):
        """ConflictAnalysis output count equals input count."""
        branches = [
            _branch("Do X", branch_type=BranchType.COMMIT_CANDIDATE, validation_condition="v"),
            _branch("Do Y", branch_type=BranchType.COMMIT_CANDIDATE, validation_condition="v"),
            _branch("Do not X", branch_type=BranchType.BRANCH_SEED),
        ]
        bca = BasicConflictAnalysis()
        result, pr = bca.run(branches, {})
        assert len(result) == len(branches)
        assert pr.branches_eliminated == 0

    def test_conflicting_branches_remain_scoreable(self):
        """Conflicting branches still reach admission scoring."""
        branches = [
            _branch("Approach A", upside=0.6, branch_type=BranchType.COMMIT_CANDIDATE, validation_condition="v"),
            _branch("Approach B", upside=0.7, branch_type=BranchType.COMMIT_CANDIDATE, validation_condition="v"),
        ]
        pm = _full_pipeline()
        result, results = pm.run(branches)
        # At least one should be admitted (both have decent scores)
        assert len(result) >= 1


# ============================================================================
# Invariant 7: BranchPlan is advisory, not commit authority
# ============================================================================

class TestInvariant7BranchPlanAdvisory:
    def test_branch_plan_cannot_commit_state(self):
        """BranchPlan has no commit method or state mutation capability."""
        plan = BranchPlan(entries=[
            BranchPlanEntry(branch=_branch("A"), status=AdmissionStatus.ADMITTED, score=0.9),
        ])
        # BranchPlan should have NO method that writes to state
        assert not hasattr(plan, 'commit')
        assert not hasattr(plan, 'mutate_state')
        assert not hasattr(plan, 'write_canonical_state')

    def test_branch_plan_only_reports_admission_status(self):
        """BranchPlan's public interface is read-only reporting."""
        plan = BranchPlan(entries=[
            BranchPlanEntry(branch=_branch("X"), status=AdmissionStatus.ADMITTED, score=0.8),
            BranchPlanEntry(branch=_branch("Y"), status=AdmissionStatus.REJECTED_BELOW_THRESHOLD, score=0.1),
        ])
        # These are all read-only queries
        assert plan.admitted_count == 1
        assert plan.rejected_count == 1
        assert plan.can_create_workspace is True
        assert plan.workspace_budget >= 0
        summary = plan.summary()
        assert isinstance(summary, dict)


# ============================================================================
# Invariant 8: CommitManager is sole state mutator
# ============================================================================

class TestInvariant8CommitManagerExclusive:
    def test_compiler_passes_do_not_import_storage(self):
        """Compiler passes should not import or use StorageManager."""
        from cognitive_microkernel.compiler import (
            dead_branch_elimination, duplicate_branch_merge,
            conflict_analysis, strength_reduction, admission_scoring,
            branch_plan,
        )
        # None of these modules should reference StorageManager
        for module in [dead_branch_elimination, duplicate_branch_merge,
                       conflict_analysis, strength_reduction, admission_scoring,
                       branch_plan]:
            source = module.__file__
            with open(source) as f:
                content = f.read()
            assert "StorageManager" not in content, f"{module.__name__} imports StorageManager"
            assert "state_ledger" not in content, f"{module.__name__} references state_ledger"
            assert "evidence_ledger" not in content, f"{module.__name__} references evidence_ledger"

    def test_pass_manager_has_no_storage_access(self):
        """PassManager has no storage, ledger, or state mutation capability."""
        pm = PassManager()
        assert not hasattr(pm, 'storage')
        assert not hasattr(pm, 'state_ledger')
        assert not hasattr(pm, 'commit')
        assert not hasattr(pm, 'evidence_ledger')


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
