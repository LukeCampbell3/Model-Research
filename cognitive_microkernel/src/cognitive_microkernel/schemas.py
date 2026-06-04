"""Core data schemas for the cognitive microkernel.

Step 1: Implement all required schemas with schema_version and Pydantic validation.
"""

from __future__ import annotations

import uuid
from datetime import datetime
from enum import Enum
from typing import Any, Optional
from pydantic import BaseModel, Field, field_validator


class SideEffectPolicy(str, Enum):
    """Side effect policies for processes."""
    READ_ONLY = "read_only"
    REVERSIBLE_WRITE = "reversible_write"
    TRANSACTIONAL_WRITE = "transactional_write"
    EXTERNAL_REVERSIBLE_ACTION = "external_reversible_action"
    EXTERNAL_IRREVERSIBLE_ACTION = "external_irreversible_action"
    HUMAN_APPROVAL_REQUIRED = "human_approval_required"
    FORBIDDEN = "forbidden"


class SupportStatus(str, Enum):
    """Claim support statuses."""
    SUPPORTED = "supported"
    INFERRED = "inferred"
    SPECULATIVE = "speculative"
    UNSUPPORTED = "unsupported"
    CONTRADICTED = "contradicted"


class EvidenceSourceType(str, Enum):
    """Evidence source types."""
    TOOL = "tool"
    TEST = "test"
    MODEL_OUTPUT = "model_output"
    VERIFIER = "verifier"
    USER = "user"
    RUNTIME_METRIC = "runtime_metric"
    RESEARCH = "research"
    SHADOW_EVAL = "shadow_eval"
    PROMOTION_EVAL = "promotion_eval"
    LEARNING_EVAL = "learning_eval"
    CACHE_HIT = "cache_hit"
    REPLAY = "replay"


class ArtifactType(str, Enum):
    """Artifact types for content-addressed storage."""
    RAW_TOOL_OUTPUT = "raw_tool_output"
    MODEL_OUTPUT = "model_output"
    VERIFIER_OUTPUT = "verifier_output"
    CONTEXT_PAGE = "context_page"
    STATE_DELTA = "state_delta"
    BRANCH_SUMMARY = "branch_summary"
    EVIDENCE_PAYLOAD = "evidence_payload"
    CLAIM_PAYLOAD = "claim_payload"
    TEST_RESULT = "test_result"
    RUNTIME_METRIC = "runtime_metric"
    REPLAY_TRACE = "replay_trace"
    IMPORTED_RESEARCH_PAYLOAD = "imported_research_payload"
    EXPERT_OUTPUT_PAYLOAD = "expert_output_payload"


class BranchType(str, Enum):
    """Branch types for v1."""
    BRANCH_SEED = "branch_seed"
    BRANCH_SKETCH = "branch_sketch"
    COMMIT_CANDIDATE = "commit_candidate"


class ProcessStatus(str, Enum):
    """Process statuses."""
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    FAILED = "failed"
    ROLLED_BACK = "rolled_back"


class SpeculationStatus(str, Enum):
    """Speculation ledger entry statuses."""
    ACTIVE = "active"
    DORMANT = "dormant"
    VALIDATED = "validated"
    REJECTED = "rejected"
    CONTRADICTED = "contradicted"
    PROMOTED = "promoted"


class TransactionStatus(str, Enum):
    """Transaction statuses."""
    CREATED = "created"
    VERIFICATION_PENDING = "verification_pending"
    VERIFIED = "verified"
    COMMITTED = "committed"
    REJECTED = "rejected"
    ROLLED_BACK = "rolled_back"


# ============================================================================
# Core schemas with schema_version
# ============================================================================

class ProcessDescriptor(BaseModel):
    """Process descriptor with parent state hash and budget tracking.
    
    Mutable: status and updated_at change during lifecycle.
    """
    process_id: str = Field(default_factory=lambda: f"process_{uuid.uuid4().hex[:16]}")
    process_type: str
    parent_process_ids: list[str] = Field(default_factory=list)
    parent_state_hash: str
    input_state_refs: list[str] = Field(default_factory=list)
    required_context_refs: list[str] = Field(default_factory=list)
    state_delta_ref: Optional[str] = None
    artifact_refs: list[str] = Field(default_factory=list)
    evidence_refs: list[str] = Field(default_factory=list)
    claim_refs: list[str] = Field(default_factory=list)
    branch_refs: list[str] = Field(default_factory=list)
    speculation_refs: list[str] = Field(default_factory=list)
    expected_output_schema: str
    expert_requirements: dict[str, Any] = Field(default_factory=dict)
    max_tokens: int = 10000
    max_model_calls: int = 10
    max_tool_calls: int = 5
    max_runtime_ms: int = 30000
    budget_remaining: float = 1.0
    priority: float = 0.5
    side_effect_policy: SideEffectPolicy = SideEffectPolicy.READ_ONLY
    transaction_id: Optional[str] = None
    cache_key: str
    resume_pointer: Optional[str] = None
    status: ProcessStatus = ProcessStatus.PENDING
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    trace_enabled: bool = True
    schema_version: str = "v1"

    @field_validator("parent_state_hash")
    @classmethod
    def parent_state_hash_not_empty(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("parent_state_hash must not be empty")
        return v


class ProcessNode(BaseModel):
    """Process DAG node for replay and audit."""
    process_id: str
    parent_process_ids: list[str] = Field(default_factory=list)
    child_process_ids: list[str] = Field(default_factory=list)
    input_artifact_refs: list[str] = Field(default_factory=list)
    output_artifact_refs: list[str] = Field(default_factory=list)
    state_hash_before: str
    state_hash_after: Optional[str] = None
    status: ProcessStatus = ProcessStatus.PENDING
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    cost_used: float = 0.0
    error_refs: list[str] = Field(default_factory=list)
    replayable: bool = True
    schema_version: str = "v1"


class Artifact(BaseModel):
    """Content-addressed artifact."""
    artifact_id: str = Field(default_factory=lambda: f"artifact_{uuid.uuid4().hex[:16]}")
    content_hash: str
    artifact_type: str
    storage_uri: str
    created_by_process: str
    schema_version: str = "v1"
    compression_type: str = "none"
    privacy_level: str = "private"
    retention_policy: str = "permanent"
    created_at: datetime = Field(default_factory=datetime.utcnow)


class CanonicalState(BaseModel):
    """Canonical state root pointer. Mutable via transactions only."""
    canonical_state_id: str = Field(default_factory=lambda: f"state_{uuid.uuid4().hex[:16]}")
    root_state_hash: str
    active_artifact_refs: list[str] = Field(default_factory=list)
    active_claim_refs: list[str] = Field(default_factory=list)
    active_evidence_refs: list[str] = Field(default_factory=list)
    active_branch_refs: list[str] = Field(default_factory=list)
    active_speculation_refs: list[str] = Field(default_factory=list)
    committed_transaction_refs: list[str] = Field(default_factory=list)
    schema_version: str = "v1"
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class EvidenceRecord(BaseModel):
    """Evidence record with traceability."""
    evidence_id: str = Field(default_factory=lambda: f"evidence_{uuid.uuid4().hex[:16]}")
    source_type: EvidenceSourceType
    source_ref: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    state_hash: str
    process_id: str
    branch_id: Optional[str] = None
    claim_supported: list[str] = Field(default_factory=list)
    claim_contradicted: list[str] = Field(default_factory=list)
    raw_payload_ref: str
    summary: str
    reliability: float = 0.5
    freshness: float = 1.0
    reproducibility: float = 0.5
    downstream_uses: list[str] = Field(default_factory=list)
    usable_for_training: bool = False
    schema_version: str = "v1"


class Claim(BaseModel):
    """Claim with evidence linkage and support status."""
    claim_id: str = Field(default_factory=lambda: f"claim_{uuid.uuid4().hex[:16]}")
    text: str
    support_status: SupportStatus
    evidence_refs: list[str] = Field(default_factory=list)
    contradiction_refs: list[str] = Field(default_factory=list)
    confidence: float = 0.5
    freshness: float = 1.0
    scope: str
    source_processes: list[str] = Field(default_factory=list)
    source_branch: Optional[str] = None
    promoted_to_memory: bool = False
    reusable: bool = False
    usable_for_training: bool = False
    schema_version: str = "v1"


class BranchProcess(BaseModel):
    """Branch process for speculative work."""
    branch_id: str = Field(default_factory=lambda: f"branch_{uuid.uuid4().hex[:16]}")
    parent_state_hash: str
    branch_type: BranchType
    hypothesis: str
    expected_upside: float = 0.0
    primary_risk: str = ""
    evidence_needed: list[str] = Field(default_factory=list)
    context_refs_needed: list[str] = Field(default_factory=list)
    estimated_token_cost: int = 1000
    estimated_tool_cost: int = 0
    estimated_verification_cost: int = 100
    reversibility: bool = True
    validation_condition: str = ""
    priority_score: float = 0.0
    expansion_level: int = 0
    transaction_id: Optional[str] = None
    resume_pointer: Optional[str] = None
    status: ProcessStatus = ProcessStatus.PENDING
    created_by_process: str
    schema_version: str = "v1"


class SpeculationLedgerEntry(BaseModel):
    """Dormant speculation ledger entry."""
    speculation_id: str = Field(default_factory=lambda: f"speculation_{uuid.uuid4().hex[:16]}")
    parent_state_hash: str
    branch_id: str
    hypothesis: str
    branch_type: BranchType
    expected_upside: float = 0.0
    primary_risk: str = ""
    reason_not_selected: str
    required_evidence_to_reopen: list[str] = Field(default_factory=list)
    trigger_conditions: list[str] = Field(default_factory=list)
    confidence: float = 0.0
    uncertainty: float = 1.0
    support_tags: list[str] = Field(default_factory=list)
    evidence_refs: list[str] = Field(default_factory=list)
    related_claims: list[str] = Field(default_factory=list)
    cost_to_resume: float = 0.0
    last_reviewed_step: Optional[datetime] = None
    status: SpeculationStatus = SpeculationStatus.DORMANT
    usable_for_learning: bool = False
    schema_version: str = "v1"


class Transaction(BaseModel):
    """Transactional commit record. Mutable: status changes during lifecycle."""
    transaction_id: str = Field(default_factory=lambda: f"tx_{uuid.uuid4().hex[:16]}")
    initiating_process_id: str
    parent_state_hash: str
    proposed_state_delta_ref: str
    affected_claim_refs: list[str] = Field(default_factory=list)
    affected_evidence_refs: list[str] = Field(default_factory=list)
    side_effect_policy: SideEffectPolicy
    verification_refs: list[str] = Field(default_factory=list)
    rollback_plan_ref: Optional[str] = None
    status: TransactionStatus = TransactionStatus.CREATED
    created_at: datetime = Field(default_factory=datetime.utcnow)
    committed_at: Optional[datetime] = None
    schema_version: str = "v1"

    @field_validator("proposed_state_delta_ref")
    @classmethod
    def proposed_state_delta_ref_not_empty(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("proposed_state_delta_ref must not be empty")
        return v


class ReplayTrace(BaseModel):
    """Replay trace for artifact-based reconstruction."""
    replay_trace_id: str = Field(default_factory=lambda: f"replay_{uuid.uuid4().hex[:16]}")
    root_process_id: str
    process_path: list[str] = Field(default_factory=list)
    artifact_refs: list[str] = Field(default_factory=list)
    evidence_refs: list[str] = Field(default_factory=list)
    claim_refs: list[str] = Field(default_factory=list)
    transaction_refs: list[str] = Field(default_factory=list)
    state_hash_sequence: list[str] = Field(default_factory=list)
    schema_version: str = "v1"
    created_at: datetime = Field(default_factory=datetime.utcnow)


class ExpertInput(BaseModel):
    """Input to an interchangeable expert."""
    task_state_slice: str
    active_constraints: list[str] = Field(default_factory=list)
    evidence_refs: list[str] = Field(default_factory=list)
    claim_refs: list[str] = Field(default_factory=list)
    branch_context: str = ""
    required_output_schema: str
    budget: float = 1.0
    risk_level: str = "medium"
    support_policy: str = "strict"
    schema_version: str = "v1"


class ExpertOutput(BaseModel):
    """Output from an interchangeable expert."""
    expert_id: str
    expert_version: str = "v1"
    output_type: str
    claims: list[str] = Field(default_factory=list)
    proposed_actions: list[str] = Field(default_factory=list)
    confidence: float = 0.5
    uncertainty: float = 0.5
    evidence_refs_used: list[str] = Field(default_factory=list)
    claim_refs_used: list[str] = Field(default_factory=list)
    support_tags: list[str] = Field(default_factory=list)
    detected_risks: list[str] = Field(default_factory=list)
    expected_value_delta: float = 0.0
    cost_used: float = 0.0
    recommended_next_processes: list[str] = Field(default_factory=list)
    side_effects_requested: bool = False
    validation_required: bool = True
    raw_output_ref: str
    schema_version: str = "v1"


# ============================================================================
# Future extension stubs (inactive in v1)
# ============================================================================

class LearnedPolicy(BaseModel):
    """Learned policy interface (inactive in v1)."""
    policy_id: str = Field(default_factory=lambda: f"policy_{uuid.uuid4().hex[:16]}")
    policy_type: str
    feature_schema_version: str = "v1"
    training_data_refs: list[str] = Field(default_factory=list)
    target_definition: str = ""
    model_version: str = "v1"
    calibration_metrics: dict[str, float] = Field(default_factory=dict)
    shadow_metrics: dict[str, float] = Field(default_factory=dict)
    promotion_status: str = "shadow_only"
    rollback_pointer: Optional[str] = None
    schema_version: str = "v1"


class ExpertKnowledgeStore(BaseModel):
    """Expert knowledge store (inactive in v1)."""
    expert_id: str
    base_model_id: str = ""
    adapter_ids: list[str] = Field(default_factory=list)
    memory_bank_id: Optional[str] = None
    replay_buffer_id: Optional[str] = None
    validated_trace_refs: list[str] = Field(default_factory=list)
    domain_scope: str = ""
    supported_claim_refs: list[str] = Field(default_factory=list)
    negative_evidence_refs: list[str] = Field(default_factory=list)
    last_training_run_id: Optional[str] = None
    promotion_status: str = "inactive"
    rollback_pointer: Optional[str] = None
    schema_version: str = "v1"
