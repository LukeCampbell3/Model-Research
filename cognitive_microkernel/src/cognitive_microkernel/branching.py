"""Branch lifecycle management.

Step 5: Implement branch generation, deduplication, scoring, archiving, and commit control.
"""

import hashlib
import json
from typing import Optional, Any
from datetime import datetime

from .schemas import (
    ProcessDescriptor, BranchProcess, BranchType, ProcessStatus,
    SpeculationLedgerEntry, SpeculationStatus,
)
from .storage import StorageManager


class BranchSeedGenerator:
    """Generate branch seeds (Level 0) from initial observations."""
    
    def __init__(self, storage: StorageManager):
        self.storage = storage
    
    def generate_seeds(
        self,
        parent_state_hash: str,
        observation: str,
        created_by_process: str,
        max_seeds: int = 10,
    ) -> list[BranchProcess]:
        """Generate initial branch seeds from observation."""
        
        # Simple heuristic: generate variations based on observation keywords
        seeds = []
        
        # Parse observation for key concepts
        words = observation.lower().split()
        key_concepts = [w for w in words if len(w) > 3][:5]
        
        # Generate hypothesis variations (always at least 3)
        base_hypotheses = [f"Focus on {concept}" for concept in key_concepts]
        
        # Ensure minimum 3 hypotheses
        fallback_hypotheses = [
            "Direct approach",
            "Alternative approach",
            "Conservative approach",
            "Incremental approach",
            "Exhaustive approach",
        ]
        while len(base_hypotheses) < 3:
            base_hypotheses.append(fallback_hypotheses[len(base_hypotheses)])
        
        # Create branch seeds
        for i, hypothesis in enumerate(base_hypotheses[:max_seeds]):
            seed = BranchProcess(
                parent_state_hash=parent_state_hash,
                branch_type=BranchType.BRANCH_SEED,
                hypothesis=hypothesis,
                expected_upside=0.3 + (i * 0.1),  # Simple heuristic
                primary_risk="Incomplete information",
                estimated_token_cost=500,
                estimated_verification_cost=100,
                reversibility=True,
                validation_condition="Sufficient evidence collected",
                priority_score=0.5 - (i * 0.1),  # First seeds have higher priority
                expansion_level=0,
                created_by_process=created_by_process,
                status=ProcessStatus.PENDING,
            )
            seeds.append(seed)
        
        return seeds


class BranchDeduplicator:
    """Deduplicate similar branches."""
    
    @staticmethod
    def compute_branch_fingerprint(branch: BranchProcess) -> str:
        """Compute fingerprint for branch deduplication."""
        fingerprint_data = {
            "parent_state_hash": branch.parent_state_hash,
            "hypothesis_keywords": " ".join(sorted(set(branch.hypothesis.lower().split()))),
            "evidence_needed": sorted(branch.evidence_needed),
            "context_refs_needed": sorted(branch.context_refs_needed),
        }
        fingerprint_json = json.dumps(fingerprint_data, sort_keys=True)
        return hashlib.sha256(fingerprint_json.encode()).hexdigest()[:16]
    
    def deduplicate(self, branches: list[BranchProcess]) -> list[BranchProcess]:
        """Remove duplicate branches."""
        seen_fingerprints = set()
        unique_branches = []
        
        for branch in branches:
            fingerprint = self.compute_branch_fingerprint(branch)
            if fingerprint not in seen_fingerprints:
                seen_fingerprints.add(fingerprint)
                unique_branches.append(branch)
            else:
                # Mark as duplicate in metadata
                branch.hypothesis = f"[DUPLICATE] {branch.hypothesis}"
        
        return unique_branches


class BranchCheapScorer:
    """Score branches cheaply before expensive expansion."""
    
    @staticmethod
    def score_branch(branch: BranchProcess, context: dict[str, Any]) -> float:
        """Score a branch using cheap heuristics."""
        score = 0.0
        
        # Hypothesis length heuristic (moderate is good)
        hyp_len = len(branch.hypothesis.split())
        if 5 <= hyp_len <= 20:
            score += 0.2
        elif hyp_len > 50:
            score -= 0.1
        
        # Evidence needed heuristic (less is better)
        evidence_needed = len(branch.evidence_needed)
        if evidence_needed == 0:
            score += 0.1
        elif evidence_needed > 5:
            score -= 0.1
        
        # Context needed heuristic (less is better)
        context_needed = len(branch.context_refs_needed)
        if context_needed == 0:
            score += 0.1
        elif context_needed > 3:
            score -= 0.1
        
        # Cost heuristic (cheaper is better)
        total_cost = branch.estimated_token_cost + branch.estimated_tool_cost
        if total_cost < 1000:
            score += 0.2
        elif total_cost > 5000:
            score -= 0.2
        
        # Reversibility bonus
        if branch.reversibility:
            score += 0.1
        
        # Expected upside (direct from branch)
        score += branch.expected_upside * 0.3
        
        # Priority score adjustment
        score += branch.priority_score * 0.2
        
        # Clamp to [0, 1]
        return max(0.0, min(1.0, score))
    
    def select_top_branches(
        self,
        branches: list[BranchProcess],
        max_select: int = 3,
        min_score: float = 0.2,
    ) -> list[BranchProcess]:
        """Select top-scoring branches for expansion."""
        scored_branches = []
        
        for branch in branches:
            score = self.score_branch(branch, {})
            if score >= min_score:
                scored_branches.append((score, branch))
        
        # Sort by score descending
        scored_branches.sort(key=lambda x: x[0], reverse=True)
        
        # Return top branches
        return [branch for _, branch in scored_branches[:max_select]]


class BranchArchive:
    """Archive losing branches and create speculation entries."""
    
    def __init__(self, storage: StorageManager):
        self.storage = storage
    
    def archive_branch(
        self,
        branch: BranchProcess,
        prune_reason: str,
        winning_branch_id: Optional[str] = None,
    ) -> Optional[SpeculationLedgerEntry]:
        """Archive a losing branch as speculation."""
        
        # Don't archive completed or already archived branches
        if branch.status in [ProcessStatus.COMPLETED, ProcessStatus.CANCELLED]:
            return None
        
        # Create speculation entry
        speculation = SpeculationLedgerEntry(
            parent_state_hash=branch.parent_state_hash,
            branch_id=branch.branch_id,
            hypothesis=branch.hypothesis,
            branch_type=branch.branch_type,
            expected_upside=branch.expected_upside,
            primary_risk=branch.primary_risk,
            reason_not_selected=prune_reason,
            required_evidence_to_reopen=branch.evidence_needed.copy(),
            trigger_conditions=[
                f"New evidence about {branch.primary_risk.lower()}",
                f"Changed context for {branch.hypothesis[:50]}...",
            ],
            confidence=branch.expected_upside,
            uncertainty=1.0 - branch.expected_upside,
            support_tags=["speculative"],
            evidence_refs=[],
            related_claims=[],
            cost_to_resume=branch.estimated_token_cost / 2,  # Resume cheaper than fresh
            last_reviewed_step=datetime.utcnow(),
            status=SpeculationStatus.DORMANT,
            usable_for_learning=True,
        )
        
        # Store speculation
        self.storage.speculation_ledger.record_speculation(speculation)
        
        # Update branch status
        branch.status = ProcessStatus.CANCELLED
        
        return speculation
    
    def archive_contradicted_branch(
        self,
        branch: BranchProcess,
        contradiction_evidence_ref: str,
    ) -> SpeculationLedgerEntry:
        """Archive a contradicted branch as negative knowledge."""
        
        speculation = SpeculationLedgerEntry(
            parent_state_hash=branch.parent_state_hash,
            branch_id=branch.branch_id,
            hypothesis=branch.hypothesis,
            branch_type=branch.branch_type,
            expected_upside=0.0,  # Contradicted
            primary_risk="Contradicted by evidence",
            reason_not_selected="Contradicted by evidence",
            required_evidence_to_reopen=[],  # Cannot be reopened
            trigger_conditions=[],
            confidence=0.0,
            uncertainty=1.0,
            support_tags=["contradicted"],
            evidence_refs=[contradiction_evidence_ref],
            related_claims=[],
            cost_to_resume=0.0,
            last_reviewed_step=datetime.utcnow(),
            status=SpeculationStatus.CONTRADICTED,
            usable_for_learning=True,  # Useful as negative training data
        )
        
        # Store as contradicted speculation
        self.storage.speculation_ledger.record_speculation(speculation)
        
        # Update branch status
        branch.status = ProcessStatus.FAILED
        
        return speculation


class BranchCommitController:
    """Control branch commitment and validation."""
    
    def __init__(self, storage: StorageManager):
        self.storage = storage
    
    def can_commit_branch(self, branch: BranchProcess) -> tuple[bool, str]:
        """Check if a branch can be committed."""
        
        # Must be a commit candidate
        if branch.branch_type != BranchType.COMMIT_CANDIDATE:
            return False, f"Not a commit candidate: {branch.branch_type}"
        
        # Must have validation condition
        if not branch.validation_condition:
            return False, "Missing validation condition"
        
        # Must not be in terminal state
        if branch.status in [ProcessStatus.COMPLETED, ProcessStatus.CANCELLED, ProcessStatus.FAILED]:
            return False, f"Branch in terminal state: {branch.status}"
        
        # Must have transaction ID if side-effecting
        if not branch.transaction_id and branch.reversibility is False:
            return False, "Missing transaction ID for irreversible branch"
        
        return True, "Can commit"
    
    def prepare_for_commit(
        self,
        branch: BranchProcess,
        evidence_refs: list[str],
        claim_refs: list[str],
    ) -> BranchProcess:
        """Prepare branch for commit by updating references."""
        
        # Update branch with commit preparation
        branch.evidence_needed = []  # All evidence collected
        branch.context_refs_needed = []  # All context retrieved
        branch.status = ProcessStatus.COMPLETED
        
        # Note: In a real implementation, we would update the branch object
        # and store it. For v1, we return the updated object.
        
        return branch
    
    def create_commit_candidate(
        self,
        sketch_branch: BranchProcess,
        supporting_evidence: list[str],
        validation_condition: str,
    ) -> BranchProcess:
        """Create a commit candidate from a branch sketch."""
        
        commit_candidate = BranchProcess(
            parent_state_hash=sketch_branch.parent_state_hash,
            branch_type=BranchType.COMMIT_CANDIDATE,
            hypothesis=sketch_branch.hypothesis,
            expected_upside=sketch_branch.expected_upside,
            primary_risk=sketch_branch.primary_risk,
            evidence_needed=[],  # Already collected
            context_refs_needed=[],  # Already retrieved
            estimated_token_cost=sketch_branch.estimated_token_cost,
            estimated_tool_cost=sketch_branch.estimated_tool_cost,
            estimated_verification_cost=sketch_branch.estimated_verification_cost,
            reversibility=sketch_branch.reversibility,
            validation_condition=validation_condition,
            priority_score=sketch_branch.priority_score + 0.3,  # Boost for commit
            expansion_level=2,  # Commit candidate level
            created_by_process=sketch_branch.created_by_process,
            status=ProcessStatus.PENDING,
        )
        
        return commit_candidate
