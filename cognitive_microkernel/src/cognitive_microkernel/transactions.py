"""Transaction and rollback management.

Step 3: Implement transaction manager, rollback manager, and side-effect policy enforcement.
"""

import json
import hashlib
from datetime import datetime
from pathlib import Path
from typing import Optional, Any

from .schemas import (
    ProcessDescriptor, CanonicalState, Transaction, EvidenceRecord, Claim,
    SupportStatus, SideEffectPolicy, TransactionStatus, ProcessStatus,
)
from .storage import StorageManager


class StateDeltaBuilder:
    """Build state deltas for transactional commits."""
    
    def __init__(self, storage: StorageManager):
        self.storage = storage
    
    def build_delta(self, current_state: CanonicalState, changes: dict[str, Any]) -> tuple[str, dict[str, Any]]:
        """Build a state delta from current state and changes.
        
        Returns:
            Tuple of (content_hash, delta_dict)
        """
        delta = {
            "previous_state_hash": current_state.root_state_hash,
            "changes": changes,
            "timestamp": datetime.utcnow().isoformat(),
        }
        
        # Serialize and hash
        delta_json = json.dumps(delta, sort_keys=True)
        content_hash = hashlib.sha256(delta_json.encode()).hexdigest()
        
        return content_hash, delta
    
    def apply_delta(self, current_state: CanonicalState, delta_hash: str) -> Optional[CanonicalState]:
        """Apply a delta to create new canonical state."""
        # Retrieve delta artifact
        delta_content = self.storage.artifact_store.retrieve_artifact(delta_hash)
        if not delta_content:
            return None
        
        delta = json.loads(delta_content.decode())
        
        # Validate delta references current state
        if delta.get("previous_state_hash") != current_state.root_state_hash:
            return None
        
        # Create new canonical state
        changes = delta.get("changes", {})
        
        # Merge active references
        active_artifact_refs = current_state.active_artifact_refs.copy()
        active_claim_refs = current_state.active_claim_refs.copy()
        active_evidence_refs = current_state.active_evidence_refs.copy()
        active_branch_refs = current_state.active_branch_refs.copy()
        active_speculation_refs = current_state.active_speculation_refs.copy()
        committed_transaction_refs = current_state.committed_transaction_refs.copy()
        
        # Apply changes
        if "add_artifact_refs" in changes:
            active_artifact_refs.extend(changes["add_artifact_refs"])
        if "remove_artifact_refs" in changes:
            active_artifact_refs = [r for r in active_artifact_refs if r not in changes["remove_artifact_refs"]]
        
        if "add_claim_refs" in changes:
            active_claim_refs.extend(changes["add_claim_refs"])
        if "remove_claim_refs" in changes:
            active_claim_refs = [r for r in active_claim_refs if r not in changes["remove_claim_refs"]]
        
        if "add_evidence_refs" in changes:
            active_evidence_refs.extend(changes["add_evidence_refs"])
        if "remove_evidence_refs" in changes:
            active_evidence_refs = [r for r in active_evidence_refs if r not in changes["remove_evidence_refs"]]
        
        # Create new state hash
        state_data = {
            "root_state_hash": hashlib.sha256(
                f"{current_state.root_state_hash}:{delta_hash}".encode()
            ).hexdigest(),
            "active_artifact_refs": sorted(set(active_artifact_refs)),
            "active_claim_refs": sorted(set(active_claim_refs)),
            "active_evidence_refs": sorted(set(active_evidence_refs)),
            "active_branch_refs": sorted(set(active_branch_refs)),
            "active_speculation_refs": sorted(set(active_speculation_refs)),
            "committed_transaction_refs": committed_transaction_refs,
        }
        new_state_hash = hashlib.sha256(json.dumps(state_data, sort_keys=True).encode()).hexdigest()
        
        return CanonicalState(
            root_state_hash=new_state_hash,
            active_artifact_refs=active_artifact_refs,
            active_claim_refs=active_claim_refs,
            active_evidence_refs=active_evidence_refs,
            active_branch_refs=active_branch_refs,
            active_speculation_refs=active_speculation_refs,
            committed_transaction_refs=committed_transaction_refs,
        )


class TransactionManager:
    """Manage transactions and state commits."""
    
    def __init__(self, storage: StorageManager):
        self.storage = storage
        self.delta_builder = StateDeltaBuilder(storage)
    
    def create_transaction(
        self,
        process: ProcessDescriptor,
        proposed_delta_hash: str,
        verification_refs: list[str],
        rollback_plan_ref: Optional[str] = None,
    ) -> Transaction:
        """Create a transaction for state changes."""
        
        # Validate process has transaction capability
        if process.side_effect_policy not in [
            SideEffectPolicy.TRANSACTIONAL_WRITE,
            SideEffectPolicy.REVERSIBLE_WRITE,
        ]:
            raise ValueError(f"Process cannot create transactions with side_effect_policy: {process.side_effect_policy}")
        
        transaction = Transaction(
            initiating_process_id=process.process_id,
            parent_state_hash=process.parent_state_hash,
            proposed_state_delta_ref=proposed_delta_hash,
            affected_claim_refs=process.claim_refs,
            affected_evidence_refs=process.evidence_refs,
            side_effect_policy=process.side_effect_policy,
            verification_refs=verification_refs,
            rollback_plan_ref=rollback_plan_ref,
        )
        
        # Store transaction metadata (in a real implementation, would use storage)
        return transaction
    
    def verify_transaction(self, transaction: Transaction, verification_evidence_refs: list[str]) -> bool:
        """Verify a transaction can be committed."""
        
        # Check parent state exists
        current_state = self.storage.state_ledger.get_state_by_hash(transaction.parent_state_hash)
        if not current_state:
            return False
        
        # Must have at least one verification evidence reference
        all_verification_refs = transaction.verification_refs + verification_evidence_refs
        if not all_verification_refs:
            return False
        
        # Check all verification evidence exists and is retrievable
        for evidence_ref in all_verification_refs:
            evidence = self.storage.evidence_ledger.get_evidence(evidence_ref)
            if not evidence:
                return False
        
        # Check claims are supported (if any)
        for claim_ref in transaction.affected_claim_refs:
            claim = self.storage.claim_registry.get_claim(claim_ref)
            if claim and claim.support_status in [SupportStatus.UNSUPPORTED, SupportStatus.CONTRADICTED]:
                return False
        
        # Side-effect policy validation
        if transaction.side_effect_policy == SideEffectPolicy.FORBIDDEN:
            return False
        if transaction.side_effect_policy == SideEffectPolicy.HUMAN_APPROVAL_REQUIRED:
            # In v1, human approval not implemented, so block
            return False
        
        return True
    
    def commit_transaction(self, transaction: Transaction) -> Optional[CanonicalState]:
        """Commit a transaction and return new canonical state."""
        
        # Get current state
        current_state = self.storage.state_ledger.get_state_by_hash(transaction.parent_state_hash)
        if not current_state:
            return None
        
        # Apply delta
        new_state = self.delta_builder.apply_delta(current_state, transaction.proposed_state_delta_ref)
        if not new_state:
            return None
        
        # Add transaction to committed list
        new_state.committed_transaction_refs.append(transaction.transaction_id)
        
        # Update transaction status
        transaction.status = TransactionStatus.COMMITTED
        transaction.committed_at = datetime.utcnow()
        
        # Store new state
        self.storage.state_ledger.register_state(new_state)
        
        return new_state
    
    def reject_transaction(self, transaction: Transaction, reason: str) -> Transaction:
        """Reject a transaction."""
        transaction.status = TransactionStatus.REJECTED
        
        # Create evidence for rejection
        rejection_evidence = EvidenceRecord(
            source_type="verifier",
            source_ref=transaction.transaction_id,
            state_hash=transaction.parent_state_hash,
            process_id=transaction.initiating_process_id,
            raw_payload_ref="",  # Would be actual rejection artifact in real impl
            summary=f"Transaction rejected: {reason}",
        )
        self.storage.evidence_ledger.record_evidence(rejection_evidence)
        
        return transaction


class RollbackManager:
    """Manage rollback of failed transactions."""
    
    def __init__(self, storage: StorageManager):
        self.storage = storage
    
    def create_rollback_plan(self, transaction: Transaction) -> str:
        """Create a rollback plan for a transaction.
        
        Returns:
            Artifact hash of the rollback plan
        """
        rollback_plan = {
            "transaction_id": transaction.transaction_id,
            "parent_state_hash": transaction.parent_state_hash,
            "affected_refs": {
                "claims": transaction.affected_claim_refs,
                "evidence": transaction.affected_evidence_refs,
            },
            "created_at": datetime.utcnow().isoformat(),
            "rollback_steps": [
                "Restore parent state hash",
                "Remove transaction from committed list",
                "Mark transaction as rolled_back",
            ],
        }
        
        plan_json = json.dumps(rollback_plan, sort_keys=True)
        content_hash = hashlib.sha256(plan_json.encode()).hexdigest()
        
        # Store rollback plan as artifact
        artifact = self.storage.artifact_store.store_artifact(
            plan_json.encode(),
            artifact_type="state_delta",
            created_by_process=transaction.initiating_process_id,
        )
        
        return artifact.content_hash
    
    def execute_rollback(self, transaction: Transaction) -> Optional[CanonicalState]:
        """Execute rollback to previous state."""
        
        # Get current state (which includes this transaction)
        current_state = self.storage.state_ledger.get_latest_state()
        if not current_state:
            return None
        
        # Verify this transaction is in the committed list
        if transaction.transaction_id not in current_state.committed_transaction_refs:
            return None
        
        # Find parent state
        parent_state = self.storage.state_ledger.get_state_by_hash(transaction.parent_state_hash)
        if not parent_state:
            return None
        
        # Create new state that's essentially the parent state but with rollback evidence
        rollback_state = CanonicalState(
            root_state_hash=hashlib.sha256(
                f"{parent_state.root_state_hash}:rollback:{transaction.transaction_id}".encode()
            ).hexdigest(),
            active_artifact_refs=parent_state.active_artifact_refs.copy(),
            active_claim_refs=parent_state.active_claim_refs.copy(),
            active_evidence_refs=parent_state.active_evidence_refs.copy(),
            active_branch_refs=parent_state.active_branch_refs.copy(),
            active_speculation_refs=parent_state.active_speculation_refs.copy(),
            committed_transaction_refs=[
                tx for tx in parent_state.committed_transaction_refs
                if tx != transaction.transaction_id
            ],
        )
        
        # Update transaction status
        transaction.status = TransactionStatus.ROLLED_BACK
        
        # Store rollback evidence
        rollback_evidence = EvidenceRecord(
            source_type="runtime_metric",
            source_ref=transaction.transaction_id,
            state_hash=rollback_state.root_state_hash,
            process_id=transaction.initiating_process_id,
            raw_payload_ref="",  # Would be actual rollback artifact in real impl
            summary="Transaction rolled back",
        )
        self.storage.evidence_ledger.record_evidence(rollback_evidence)
        
        # Store new state
        self.storage.state_ledger.register_state(rollback_state)
        
        return rollback_state


class CanonicalStateCommitter:
    """Facade for committing state changes."""
    
    def __init__(self, storage: StorageManager):
        self.storage = storage
        self.transaction_manager = TransactionManager(storage)
        self.rollback_manager = RollbackManager(storage)
    
    def propose_commit(
        self,
        process: ProcessDescriptor,
        delta_hash: str,
        verification_evidence: list[str],
    ) -> tuple[Optional[CanonicalState], Transaction]:
        """Propose and potentially commit state changes."""
        
        # Create transaction
        rollback_plan_ref = self.rollback_manager.create_rollback_plan(
            Transaction(
                initiating_process_id=process.process_id,
                parent_state_hash=process.parent_state_hash,
                proposed_state_delta_ref=delta_hash,
                side_effect_policy=process.side_effect_policy,
            )
        )
        
        transaction = self.transaction_manager.create_transaction(
            process=process,
            proposed_delta_hash=delta_hash,
            verification_refs=verification_evidence,
            rollback_plan_ref=rollback_plan_ref,
        )
        
        # Verify transaction
        if self.transaction_manager.verify_transaction(transaction, verification_evidence):
            # Commit
            new_state = self.transaction_manager.commit_transaction(transaction)
            return new_state, transaction
        else:
            # Reject
            rejected_transaction = self.transaction_manager.reject_transaction(
                transaction,
                reason="Verification failed",
            )
            return None, rejected_transaction


class SideEffectPolicyEnforcer:
    """Enforce side-effect policies on processes."""
    
    @staticmethod
    def can_execute(process: ProcessDescriptor, current_state_hash: str) -> bool:
        """Check if a process can execute given its side-effect policy."""
        
        # Check parent state hash matches
        if process.parent_state_hash != current_state_hash:
            return False
        
        # Policy-based checks
        if process.side_effect_policy == SideEffectPolicy.FORBIDDEN:
            return False
        
        if process.side_effect_policy == SideEffectPolicy.HUMAN_APPROVAL_REQUIRED:
            # In v1, human approval not implemented
            return False
        
        if process.side_effect_policy == SideEffectPolicy.EXTERNAL_IRREVERSIBLE_ACTION:
            # In v1, irreversible actions not allowed
            return False
        
        return True
    
    @staticmethod
    def requires_transaction(process: ProcessDescriptor) -> bool:
        """Check if a process requires a transaction for its side effects."""
        return process.side_effect_policy in [
            SideEffectPolicy.TRANSACTIONAL_WRITE,
            SideEffectPolicy.REVERSIBLE_WRITE,
            SideEffectPolicy.EXTERNAL_REVERSIBLE_ACTION,
        ]
    
    @staticmethod
    def is_read_only(process: ProcessDescriptor) -> bool:
        """Check if a process is read-only."""
        return process.side_effect_policy == SideEffectPolicy.READ_ONLY
