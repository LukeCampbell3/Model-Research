"""Cognitive Microkernel Runtime.

Step 7: The minimal end-to-end loop:
  observe → branch → expert → claim → evidence → verify → transaction → commit/rollback → archive → replay trace
"""

import hashlib
import json
from typing import Optional, Any
from pathlib import Path
from datetime import datetime

from .schemas import (
    ProcessDescriptor, ProcessNode, CanonicalState, EvidenceRecord, Claim,
    Transaction, ExpertInput, ExpertOutput, BranchProcess, ReplayTrace,
    ProcessStatus, SupportStatus, SideEffectPolicy, EvidenceSourceType,
    BranchType, TransactionStatus, ArtifactType,
)
from .storage import StorageManager
from .transactions import (
    StateDeltaBuilder, TransactionManager, RollbackManager,
    CanonicalStateCommitter, SideEffectPolicyEnforcer,
)
from .experts import ExpertRouter, ExpertABIValidator, SupportTagValidator
from .branching import (
    BranchSeedGenerator, BranchDeduplicator, BranchCheapScorer,
    BranchArchive, BranchCommitController,
)
from .scheduler import (
    ProcessQueueManager, PriorityScheduler, BudgetManager,
    TimingCollector, RuntimeProfiler, QueueType,
)


class Runtime:
    """Cognitive Microkernel Runtime.

    Orchestrates the full pipeline:
    1. observe input
    2. create root process descriptor
    3. page required context
    4. extract initial claims
    5. generate branch seeds
    6. deduplicate branch seeds
    7. cheap-score branches
    8. expand best branch sketches
    9. route selected process to compatible expert
    10. collect expert output
    11. extract claims
    12. write evidence records
    13. verify commit candidate
    14. create transaction
    15. commit or rollback
    16. archive losing branches
    17. store useful speculation
    18. write replay trace
    19. report timing and cost metrics
    """

    def __init__(self, base_dir: Path):
        self.base_dir = base_dir
        self.storage = StorageManager(base_dir)

        # Core components
        self.state_delta_builder = StateDeltaBuilder(self.storage)
        self.state_committer = CanonicalStateCommitter(self.storage)
        self.expert_router = ExpertRouter()
        self.branch_seed_generator = BranchSeedGenerator(self.storage)
        self.branch_deduplicator = BranchDeduplicator()
        self.branch_scorer = BranchCheapScorer()
        self.branch_archive = BranchArchive(self.storage)
        self.branch_commit_controller = BranchCommitController(self.storage)

        # Scheduling
        self.queue_manager = ProcessQueueManager()
        self.scheduler = PriorityScheduler(self.queue_manager)
        self.budget_manager = BudgetManager()
        self.timing_collector = TimingCollector()
        self.profiler = RuntimeProfiler()

        # Initial state
        self.current_state = self._initialize_state()

    def _initialize_state(self) -> CanonicalState:
        """Initialize or load canonical state."""
        latest_state = self.storage.state_ledger.get_latest_state()
        if latest_state:
            return latest_state

        initial_state = CanonicalState(
            root_state_hash=hashlib.sha256(b"initial_state").hexdigest(),
        )
        self.storage.state_ledger.register_state(initial_state)
        return initial_state

    # =========================================================================
    # Pipeline steps
    # =========================================================================

    def execute_minimal_loop(self, observation: str) -> dict[str, Any]:
        """Execute the minimal end-to-end loop for a single observation.

        Returns a result dict with all outputs from each stage.
        """
        results: dict[str, Any] = {
            "root_process": None,
            "branch_seeds": [],
            "expanded_branches": [],
            "claims_extracted": [],
            "evidence_created": [],
            "verification_results": [],
            "transaction": None,
            "new_state": None,
            "archived_branches": [],
            "replay_trace": None,
            "error": None,
        }

        try:
            # Step 1-2: Observe and create root process
            root_process = self._step_create_root_process(observation)
            results["root_process"] = root_process

            # Step 3: Extract initial claims
            initial_claims = self._step_extract_initial_claims(observation, root_process)
            results["claims_extracted"].extend(initial_claims)

            # Step 4-6: Generate, deduplicate, score branch seeds
            branch_seeds = self._step_generate_branches(observation, root_process)
            results["branch_seeds"] = branch_seeds

            # Step 7: Select top branches for expansion
            top_branches = self.branch_scorer.select_top_branches(branch_seeds, max_select=2)

            # Step 8-11: Expand branch sketches via expert
            for branch in top_branches:
                expert_output, claims, evidence = self._step_expand_branch(branch, root_process)
                if expert_output:
                    results["expanded_branches"].append({
                        "branch": branch,
                        "expert_output": expert_output,
                    })
                    results["claims_extracted"].extend(claims)
                    results["evidence_created"].extend(evidence)

            # Step 12-15: Verify and commit/rollback
            if results["expanded_branches"]:
                commit_result = self._step_verify_and_commit(
                    results["expanded_branches"][0]["branch"],
                    results["evidence_created"],
                    results["claims_extracted"],
                    root_process,
                )
                results["verification_results"] = commit_result.get("verification", [])
                results["transaction"] = commit_result.get("transaction")
                results["new_state"] = commit_result.get("new_state")

            # Step 16-17: Archive losing branches
            winning_id = top_branches[0].branch_id if top_branches else None
            for branch in branch_seeds:
                if branch not in top_branches:
                    spec = self.branch_archive.archive_branch(
                        branch, prune_reason="Not selected for expansion",
                        winning_branch_id=winning_id,
                    )
                    if spec:
                        results["archived_branches"].append(spec)
                        self.profiler.increment("speculations_retained")

            # Step 18: Create replay trace
            results["replay_trace"] = self._step_build_replay_trace(results, root_process)

            # Step 19: Record metrics
            root_process.status = ProcessStatus.COMPLETED
            root_process.updated_at = datetime.utcnow()
            self.storage.process_registry.register_process(root_process)
            self.profiler.increment("processes_completed")

        except Exception as e:
            results["error"] = str(e)
            if results["root_process"]:
                results["root_process"].status = ProcessStatus.FAILED
                self.storage.process_registry.register_process(results["root_process"])
            self.profiler.increment("processes_cancelled")

        return results

    # =========================================================================
    # Internal pipeline helpers
    # =========================================================================

    def _step_create_root_process(self, observation: str) -> ProcessDescriptor:
        """Step 1-2: Observe and create root process descriptor."""
        cache_key = hashlib.sha256(
            f"root:{observation}:{self.current_state.root_state_hash}".encode()
        ).hexdigest()[:32]

        # Check cache
        cached = self.storage.process_registry.find_by_cache_key(cache_key)
        if cached:
            self.profiler.record_cache_hit(True)
            return cached

        self.profiler.record_cache_hit(False)

        root_process = ProcessDescriptor(
            process_type="observe_and_plan",
            parent_state_hash=self.current_state.root_state_hash,
            expected_output_schema="branch_seeds",
            cache_key=cache_key,
            side_effect_policy=SideEffectPolicy.TRANSACTIONAL_WRITE,
            max_tokens=2000,
            budget_remaining=1.0,
        )

        self.storage.process_registry.register_process(root_process)
        self.profiler.increment("processes_created")
        return root_process

    def _step_extract_initial_claims(
        self, observation: str, process: ProcessDescriptor
    ) -> list[Claim]:
        """Step 3: Extract initial claims from observation."""
        claim = Claim(
            text=f"Task observed: {observation[:200]}",
            support_status=SupportStatus.SUPPORTED,
            scope="observation",
            source_processes=[process.process_id],
            evidence_refs=[],
        )
        self.storage.claim_registry.register_claim(claim)
        self.profiler.record_claim_support(has_evidence=True)
        return [claim]

    def _step_generate_branches(
        self, observation: str, process: ProcessDescriptor
    ) -> list[BranchProcess]:
        """Steps 4-6: Generate, deduplicate, and score branch seeds."""
        seeds = self.branch_seed_generator.generate_seeds(
            parent_state_hash=process.parent_state_hash,
            observation=observation,
            created_by_process=process.process_id,
            max_seeds=5,
        )
        unique_seeds = self.branch_deduplicator.deduplicate(seeds)
        self.profiler.increment("branch_seeds_generated", len(unique_seeds))
        return unique_seeds

    def _step_expand_branch(
        self, branch: BranchProcess, process: ProcessDescriptor
    ) -> tuple[Optional[ExpertOutput], list[Claim], list[EvidenceRecord]]:
        """Steps 8-11: Expand a branch sketch using experts."""
        expert_input = ExpertInput(
            task_state_slice=branch.hypothesis,
            required_output_schema="branch_expansion",
            budget=process.budget_remaining,
        )

        # Route to expert
        expert_id, routing_result = self.expert_router.route(process, [])
        if not expert_id:
            return None, [], []

        expert = self.expert_router.experts[expert_id]
        expert_output = expert.execute(expert_input)

        # Validate output
        valid, errors = ExpertABIValidator.validate_output(expert_output)
        if not valid:
            err_evidence = EvidenceRecord(
                source_type=EvidenceSourceType.RUNTIME_METRIC,
                source_ref=process.process_id,
                state_hash=process.parent_state_hash,
                process_id=process.process_id,
                raw_payload_ref="",
                summary=f"Expert output validation failed: {errors}",
            )
            self.storage.evidence_ledger.record_evidence(err_evidence)
            return None, [], [err_evidence]

        # Extract claims
        claims: list[Claim] = []
        for claim_text in expert_output.claims:
            support_status = SupportTagValidator.get_claim_support_status(expert_output.support_tags)
            claim = Claim(
                text=claim_text,
                support_status=support_status,
                scope=branch.hypothesis[:50],
                source_processes=[process.process_id],
                source_branch=branch.branch_id,
            )
            claims.append(claim)
            self.storage.claim_registry.register_claim(claim)
            self.profiler.record_claim_support(support_status != SupportStatus.UNSUPPORTED)

        # Create evidence
        evidence = EvidenceRecord(
            source_type=EvidenceSourceType.MODEL_OUTPUT,
            source_ref=expert_id,
            state_hash=process.parent_state_hash,
            process_id=process.process_id,
            branch_id=branch.branch_id,
            claim_supported=[c.claim_id for c in claims],
            raw_payload_ref=expert_output.raw_output_ref or "",
            summary=f"Expert output for branch: {branch.hypothesis[:100]}",
        )
        self.storage.evidence_ledger.record_evidence(evidence)
        self.profiler.increment("evidence_records_created")
        self.profiler.increment("branches_expanded")

        return expert_output, claims, [evidence]

    def _step_verify_and_commit(
        self,
        branch: BranchProcess,
        evidence_list: list[EvidenceRecord],
        claims: list[Claim],
        process: ProcessDescriptor,
    ) -> dict[str, Any]:
        """Steps 12-15: Verify commit candidate and commit or rollback."""
        result: dict[str, Any] = {"verification": [], "transaction": None, "new_state": None}

        # Create commit candidate from branch
        commit_candidate = self.branch_commit_controller.create_commit_candidate(
            sketch_branch=branch,
            supporting_evidence=[e.evidence_id for e in evidence_list],
            validation_condition="Evidence supports hypothesis",
        )

        # Verify
        can_commit, reason = self.branch_commit_controller.can_commit_branch(commit_candidate)
        if not can_commit:
            result["verification"].append({"verified": False, "reason": reason})
            return result

        # Create verification evidence
        verify_evidence = EvidenceRecord(
            source_type=EvidenceSourceType.VERIFIER,
            source_ref=process.process_id,
            state_hash=process.parent_state_hash,
            process_id=process.process_id,
            raw_payload_ref="",
            summary=f"Branch verified: {branch.hypothesis[:100]}",
            claim_supported=[c.claim_id for c in claims],
        )
        self.storage.evidence_ledger.record_evidence(verify_evidence)
        result["verification"].append({"verified": True, "evidence": verify_evidence})

        # Build state delta
        delta_changes = {
            "add_claim_refs": [c.claim_id for c in claims],
            "add_evidence_refs": [e.evidence_id for e in evidence_list] + [verify_evidence.evidence_id],
        }
        delta_json = json.dumps({
            "previous_state_hash": self.current_state.root_state_hash,
            "changes": delta_changes,
            "timestamp": datetime.utcnow().isoformat(),
        }, sort_keys=True)
        delta_hash = hashlib.sha256(delta_json.encode()).hexdigest()

        # Store delta as artifact so apply_delta can find it
        self.storage.artifact_store.store_artifact(
            delta_json.encode(),
            artifact_type="state_delta",
            created_by_process=process.process_id,
        )

        # Propose commit
        new_state, transaction = self.state_committer.propose_commit(
            process=process,
            delta_hash=delta_hash,
            verification_evidence=[verify_evidence.evidence_id],
        )

        result["transaction"] = transaction
        if new_state:
            result["new_state"] = new_state
            self.current_state = new_state
            self.profiler.increment("branches_committed")
        else:
            self.profiler.increment("rollback_count")

        return result

    def _step_build_replay_trace(
        self, results: dict[str, Any], root_process: ProcessDescriptor
    ) -> ReplayTrace:
        """Step 18: Build replay trace from collected artifacts."""
        trace = ReplayTrace(
            root_process_id=root_process.process_id,
            process_path=[root_process.process_id],
            artifact_refs=[],
            evidence_refs=[e.evidence_id for e in results.get("evidence_created", [])],
            claim_refs=[c.claim_id for c in results.get("claims_extracted", [])],
            transaction_refs=(
                [results["transaction"].transaction_id] if results.get("transaction") else []
            ),
            state_hash_sequence=[self.current_state.root_state_hash],
        )

        # Also add to DAG
        node = ProcessNode(
            process_id=root_process.process_id,
            state_hash_before=root_process.parent_state_hash,
            state_hash_after=self.current_state.root_state_hash,
            status=ProcessStatus.COMPLETED,
            start_time=root_process.created_at,
            end_time=datetime.utcnow(),
            replayable=True,
        )
        self.storage.process_dag.add_node(node)

        return trace

    # =========================================================================
    # Utility
    # =========================================================================

    def get_current_state_hash(self) -> str:
        return self.current_state.root_state_hash

    def get_metrics(self) -> dict[str, Any]:
        return self.profiler.get_metrics()
