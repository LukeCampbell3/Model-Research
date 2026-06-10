Below is a robust **Phase 2 implementation plan**.

Phase 1 built the **safety microkernel**:

```text
TaskPacket
BranchTicket
BranchIR
SnapshotManager
WorkspaceManager
PermissionValidator
ContractResourceRegistry
VerifierRunner
ClaimLedger
CommitManager
ReplayWriter
RuntimeEventLog
```

Phase 2 adds the first real intelligence layer around the microkernel: a **basic compiler-style branch handler**.

The goal is not advanced autonomy. The goal is to optimize branch plans **before execution** so the runtime wastes less compute and admits safer, better-scoped branches.

---

# Phase 2 Goal

Build the **Basic Compiler Branch Handler**.

It should take candidate branches and run them through a deterministic pass pipeline:

```text
BranchTicket
  ↓
BranchIR
  ↓
PassManager
  ↓
safety passes
  ↓
waste-reduction passes
  ↓
conflict analysis
  ↓
strength reduction
  ↓
admission scoring
  ↓
admitted / rejected / downgraded / quarantined
```

Phase 2 proves this doctrine:

```text
Do not execute every branch the model proposes.
Lower branches into IR.
Reject invalid work early.
Merge duplicates.
Detect basic conflicts.
Reduce expensive branches into cheaper probes.
Admit only useful, bounded, verifier-ready branches.
```

---

# 1. Phase 2 Scope

## Build in Phase 2

```text
PassManager
PassResult schema
BranchPlan schema
AdmissionDecision schema
BranchOptimizer
DeadBranchEliminationPass
DuplicateBranchMergePass
BasicConflictAnalysisPass
StrengthReductionPass
AdmissionScoringPass
Mode-aware pass execution
Branch status transitions
Branch plan artifacts
Branch optimization event logging
Tests for each pass
End-to-end optimized branch demo
```

## Do not build in Phase 2

```text
live web research
learned policy
semantic alias inference beyond declared contracts
parallel execution
full Pareto frontier adjudication
advanced benchmark scheduling
profile-guided optimization
distributed workers
background branch daemon
database replay
```

Phase 2 remains local, deterministic, JSON-based, and agent-implementable.

---

# 2. Phase 2 Core Invariants

Phase 1 invariants still apply. Phase 2 adds optimizer invariants.

```text
Invariant 1:
No optimization pass may weaken Phase 1 safety gates.

Invariant 2:
No optimization pass may remove required verifier targets.

Invariant 3:
No optimization pass may remove required evidence obligations.

Invariant 4:
No optimization pass may increase branch privilege.

Invariant 5:
No optimization pass may expand write_set beyond declared bounds.

Invariant 6:
No optimization pass may convert a non-commit-eligible mode into commit-eligible.

Invariant 7:
Strength reduction may reduce depth, patch radius, verifier cost, or execution scope, but may not hide uncertainty.

Invariant 8:
Duplicate merging must preserve all evidence and verifier requirements from merged branches.

Invariant 9:
Admission scoring may prioritize branches, but cannot override hard rejection.

Invariant 10:
Every pass decision must be written to the runtime event log.
```

The key rule:

```text
Optimization may reduce cost.
Optimization may not reduce safety.
```

---

# 3. Phase 2 Runtime Flow

Phase 1 flow:

```text
create task
→ create branch
→ lower to BranchIR
→ validate
→ workspace
→ execute
→ verify
→ commit/reject
→ replay
```

Phase 2 flow:

```text
create task
→ create candidate branches
→ lower candidates to BranchIR
→ run PassManager
→ produce optimized BranchPlan
→ admit selected branches
→ create workspaces only for admitted branches
→ execute
→ verify
→ commit/reject
→ replay
```

The important improvement:

```text
Workspace creation and execution happen only after branch optimization.
```

---

# 4. New Phase 2 Artifacts

Add these files under each branch directory:

```text
.runtime/
  branches/
    branch_<id>/
      branch_ticket.json
      branch_ir.json
      pass_results.json
      admission_decision.json
      optimized_branch_ir.json
      branch_plan.json
      events.jsonl
```

Add task-level optimization artifacts:

```text
.runtime/
  tasks/
    task_<id>/
      candidate_branches.json
      branch_plan.json
      conflict_report.json
      duplicate_report.json
      admission_report.json
```

---

# 5. New Schemas

## 5.1 PassResult

Each pass should produce a structured result.

```python
class PassResult:
    pass_id: str
    pass_name: str
    task_id: str
    branch_id: str | None

    status: str
    decision: str
    reason: str

    input_refs: list[str]
    output_refs: list[str]

    warnings: list[str]
    errors: list[str]

    changed_fields: dict
    hard_reject: bool
    requires_quarantine: bool
```

Statuses:

```text
pass
modified
rejected
quarantined
skipped
error
```

Example:

```json
{
  "pass_name": "DeadBranchEliminationPass",
  "branch_id": "branch_002",
  "status": "rejected",
  "decision": "reject",
  "reason": "Branch has no verifier targets and no expected evidence.",
  "hard_reject": true,
  "requires_quarantine": false
}
```

---

## 5.2 AdmissionDecision

```python
class AdmissionDecision:
    task_id: str
    branch_id: str

    decision: str
    score: float

    normalized_terms: dict

    admitted_depth: int
    admitted_mode: str

    reasons: list[str]
    blockers: list[str]
    required_followups: list[str]
```

Decision values:

```text
admit
reject
quarantine
downgrade
merge_duplicate
defer
```

Example:

```json
{
  "branch_id": "branch_003",
  "decision": "downgrade",
  "score": 0.62,
  "admitted_depth": 1,
  "admitted_mode": "O1",
  "reasons": [
    "High information value but requested depth exceeds O1 contract.",
    "Strength reduction lowered branch from patch to diagnostic."
  ],
  "blockers": [],
  "required_followups": ["Run diagnostic before patch admission."]
}
```

---

## 5.3 BranchPlan

Task-level optimized branch plan.

```python
class BranchPlan:
    task_id: str
    created_at: str

    candidate_branch_ids: list[str]
    admitted_branch_ids: list[str]
    rejected_branch_ids: list[str]
    quarantined_branch_ids: list[str]
    deferred_branch_ids: list[str]
    merged_branch_ids: dict[str, list[str]]

    execution_order: list[str]

    shared_diagnostics: list[str]
    conflict_groups: list[list[str]]

    plan_summary: str
    risks: list[str]
    required_verifiers: list[str]
```

This is the output of Phase 2 optimization.

---

## 5.4 ConflictReport

```python
class Conflict:
    conflict_id: str
    conflict_type: str

    branch_a: str
    branch_b: str

    resource_type: str
    resource_id: str

    severity: str
    resolution: str
    reason: str
```

Conflict types:

```text
file_write_write
file_write_read_invalidation
contract_write_write
contract_write_read_invalidation
forbidden_write
mode_contract_violation
verifier_contract_violation
metric_self_gaming
```

Severity:

```text
low
medium
high
fatal
```

Resolution:

```text
allow
order_required
rerun_required
quarantine
reject
```

---

# 6. Phase 2 Modules

Add or extend these modules:

```text
spec_runtime/
  optimizer/
    branch_optimizer.py
    pass_manager.py
    scoring.py
    normalization.py
    branch_plan_builder.py

  passes/
    base.py
    permission_pass.py
    forbidden_write_pass.py
    snapshot_binding_pass.py
    verifier_requirement_pass.py
    evidence_requirement_pass.py
    contract_validation_pass.py
    dead_branch_elimination.py
    duplicate_branch_merge.py
    basic_conflict_analysis.py
    strength_reduction.py
    admission_scoring.py

  schemas/
    pass_result.py
    admission_decision.py
    branch_plan.py
    conflict_report.py
```

Phase 1 modules remain the authority for execution and commit. Phase 2 only prepares better branches.

---

# 7. PassManager

The `PassManager` orchestrates deterministic passes.

```python
class PassManager:
    def __init__(self, passes: list[BranchPass]):
        self.passes = passes

    def run(self, branch_irs: list[BranchIR], context: OptimizationContext) -> BranchPlan:
        ...
```

## OptimizationContext

```python
class OptimizationContext:
    task_packet: TaskPacket
    mode_contracts: dict[str, ModeContract]
    contract_registry: ContractResourceRegistry
    snapshot_id: str

    existing_branches: list[BranchIR]
    committed_records: list[ReplayRecord]

    runtime_root: str
    event_log: RuntimeEventLog
```

## Required pass order

```text
1. PermissionValidationPass
2. ForbiddenWriteSetPass
3. SnapshotBindingPass
4. VerifierRequirementPass
5. EvidenceRequirementPass
6. ContractValidationPass
7. DeadBranchEliminationPass
8. DuplicateBranchMergePass
9. BasicConflictAnalysisPass
10. StrengthReductionPass
11. AdmissionScoringPass
12. BranchPlanBuilder
```

This order matters.

Safety first.
Waste reduction second.
Admission last.

---

# 8. Safety Passes

Phase 2 should reuse Phase 1 validators as passes.

## 8.1 PermissionValidationPass

Rejects branches that violate type/privilege rules.

Examples:

```text
observe_only writing source
test_generation editing production logic
metric_patch claiming metric improvement
verifier_patch self-validating
promotion_candidate doing new risky work
```

Output:

```text
pass / rejected / quarantined
```

---

## 8.2 ForbiddenWriteSetPass

Checks:

```text
write_set ∩ forbidden_write_set == empty
expected_write_set does not include forbidden paths
branch type cannot write protected paths
mode patch radius not exceeded
```

Rejects hard violations.

---

## 8.3 SnapshotBindingPass

Ensures every branch is tied to the current base snapshot.

Checks:

```text
BranchIR.base_snapshot_id exists
base snapshot exists in .runtime/snapshots/
base snapshot matches current task snapshot
```

If snapshot mismatch exists before execution:

```text
reject or re-lower branch
```

---

## 8.4 VerifierRequirementPass

Ensures every branch has verifier targets.

Rules:

```text
minimal_patch requires at least one executable verifier
config_patch requires config verifier or test verifier
metric_patch requires metric-definition verifier
verifier_patch requires meta-verifier or golden fixture
promotion_candidate requires previous verifier result refs
observe/research may use artifact verifier instead of test verifier
```

Rejects branches with no verifier path.

---

## 8.5 EvidenceRequirementPass

Ensures branch has expected evidence.

Rules:

```text
claims require expected evidence
diagnostic branches require artifact output
metric claims require metric evidence
research claims require evidence packet, but Phase 2 live research is disabled
```

---

## 8.6 ContractValidationPass

Checks that declared contracts exist.

```text
every contract_read_set ID exists
every contract_write_set ID exists
branch_type is allowed to write that contract type
contract verifier_requirements are added to verifier targets
```

Example:

```text
branch writes MetricContract:QPM
→ add metric_definition_diff verifier
→ add metric_regression_control verifier
```

---

# 9. Waste-Reduction Passes

## 9.1 DeadBranchEliminationPass

Reject branches that are structurally useless.

Reject if:

```text
missing hypothesis
missing verifier target
missing expected evidence
write_set intersects forbidden_write_set
branch exceeds mode max_patch_radius
branch exceeds mode max_depth
branch has no path to output
branch has no effect on task objective
branch is promotion_candidate but has no prior verified artifact
branch is O3 commit-eligible without promotion gate
```

Do not execute these.

---

## 9.2 DuplicateBranchMergePass

Detect duplicate or near-duplicate branches using deterministic fields first.

A branch is duplicate if these match:

```text
branch_family
hypothesis normalized string
read_set
write_set
contract_read_set
contract_write_set
verifier_targets
expected_evidence
```

Merge rule:

```text
Keep the branch with:
1. lower risk
2. smaller patch radius
3. stronger verifier targets
4. lower mode cost
5. earlier creation time
```

Merged branch must preserve:

```text
union of verifier targets
union of expected evidence
union of assumptions
union of event references
```

Record duplicate report.

Do not rely on embeddings in Phase 2.

---

## 9.3 BasicConflictAnalysisPass

Detect simple conflicts before execution.

Conflict classes:

```text
file write/write
file write/read invalidation
contract write/write
contract write/read invalidation
forbidden write
metric self-gaming
verifier self-validation risk
```

Resolution rules:

```text
write/write same file:
  conflict group; only one can be admitted foreground

write/read:
  reader branch invalidated if writer commits first

contract write/write:
  conflict group; require ordering or reject one

contract write/read:
  reader requires rerun if writer commits

metric self-gaming:
  reject

verifier self-validation:
  quarantine unless meta-verifier exists
```

Output:

```text
conflict_report.json
```

---

## 9.4 StrengthReductionPass

Converts expensive or risky branch requests into cheaper staged probes.

This is one of the most important Phase 2 additions.

Examples:

```text
minimal_patch with high uncertainty
→ diagnostic first

O3 patch branch with commit eligibility
→ background diagnostic/probe, commit_eligible false

large patch_radius > mode max
→ clamp if safe, otherwise reject

full benchmark request
→ benchmark slice request

metric_patch claiming improvement
→ split into metric_definition branch and later evaluation branch

refactor_candidate
→ observe/test branch proving local repair is insufficient
```

Phase 2 strength reduction should be conservative and deterministic.

Allowed transformations:

```text
reduce execution_depth
reduce patch_radius
change commit_policy to quarantine
change branch_type from minimal_patch to diagnostic only when patch is not yet justified
add required verifier target
add required evidence obligation
set commit_eligible false
```

Not allowed:

```text
increase privilege
expand write_set
remove verifier targets
remove evidence obligations
turn failed branch into commit candidate
```

---

## 9.5 AdmissionScoringPass

Scores branches after safety and waste passes.

All terms must be normalized to `0.0–1.0`.

```text
admission_score =
    1.4 * expected_information_gain
  + 1.2 * expected_failure_reduction
  + 1.0 * expected_future_value
  + 0.8 * reversibility
  + 0.6 * hypothesis_diversity
  - 1.2 * compute_cost
  - 1.3 * patch_radius
  - 1.2 * conflict_risk
  - 1.0 * verification_cost
  - 1.5 * rewrite_penalty
```

Phase 2 should not overfit this. Treat it as a transparent heuristic.

## Required normalized terms

```text
expected_information_gain
expected_failure_reduction
expected_future_value
reversibility
hypothesis_diversity
compute_cost
patch_radius
conflict_risk
verification_cost
rewrite_penalty
```

## Admission thresholds

Suggested defaults:

```text
score >= 0.65:
  admit

0.45 <= score < 0.65:
  defer or downgrade

0.25 <= score < 0.45:
  quarantine

score < 0.25:
  reject
```

Hard rejections override scores.

---

# 10. Mode-Aware Admission

Admission must respect O-modes.

## Os

```text
max admitted branches: 1
only depth 0–1
no research
no background
smallest safe branch wins
```

## O1

```text
max admitted branches: 2
depth <= 2
cached/internal evidence only
prefer one observe/test branch and one minimal patch
```

## O2

```text
max admitted branches: 3–4
depth <= 3
allow targeted trusted-source research later, but Phase 2 disables live research
preserve small diverse frontier
```

## O3

```text
background allowed
commit_eligible false unless promotion_candidate
prefer probes, benchmarks, and validation branches
do not directly commit broad branch
```

## Og

```text
prefer observe, test_only, diagnostic
trace preservation required
commit unlikely
research-native later, but Phase 2 uses cached/local evidence only
```

---

# 11. BranchPlanBuilder

After passes, build a task-level plan.

The plan should include:

```text
admitted branches
rejected branches
quarantined branches
deferred branches
merged duplicates
conflict groups
execution order
shared diagnostics
required verifier targets
risk summary
```

## Execution order rules

Phase 2 can be simple:

```text
1. observe/test/diagnostic branches first
2. minimal patches second
3. config/metric/verifier patches third
4. promotion candidates last
5. quarantined branches not executed
```

Conflict groups should not run together in Phase 2.

---

# 12. Branch Status Transitions

Add optimizer statuses:

```text
candidate
lowered
optimization_started
optimization_rejected
optimization_modified
optimization_quarantined
optimization_admitted
optimization_deferred
workspace_ready
```

A valid Phase 2 transition:

```text
candidate
→ lowered
→ optimization_started
→ optimization_modified
→ optimization_admitted
→ workspace_created
→ executing
```

Rejected branch:

```text
candidate
→ lowered
→ optimization_started
→ optimization_rejected
→ replay_written
```

Even rejected branches should get replay records.

---

# 13. Event Logging Requirements

Add event types:

```text
optimization_started
pass_started
pass_finished
branch_modified_by_pass
branch_rejected_by_pass
branch_quarantined_by_pass
branch_merged_duplicate
conflict_detected
strength_reduction_applied
admission_scored
admission_decided
branch_plan_written
```

Every pass should emit events.

Example event:

```json
{
  "event_type": "strength_reduction_applied",
  "task_id": "task_001",
  "branch_id": "branch_003",
  "actor": "StrengthReductionPass",
  "decision": "downgrade",
  "reason": "Requested depth 5 exceeds O1 max_depth 2; lowered to diagnostic depth 1.",
  "input_refs": ["branch_ir.json"],
  "output_refs": ["optimized_branch_ir.json"]
}
```

---

# 14. CLI Additions

Extend `specctl`.

```text
specctl optimize --task <task_id>
specctl optimize-branch --branch <branch_id>
specctl plan show --task <task_id>
specctl conflicts show --task <task_id>
specctl admissions show --task <task_id>
specctl passes show --branch <branch_id>
```

Example flow:

```text
specctl create-task --objective "Fix app bug"
specctl snapshot create
specctl branch create --task task_001 --ticket branch_a.json
specctl branch create --task task_001 --ticket branch_b.json
specctl optimize --task task_001
specctl plan show --task task_001
specctl workspace create --branch branch_admitted_001
specctl branch execute --branch branch_admitted_001 --command "..."
specctl verify --branch branch_admitted_001
specctl commit attempt --branch branch_admitted_001
```

---

# 15. Demo Scenario for Phase 2

Use the Phase 1 demo project, but add multiple candidates.

## Candidate branches

### Branch A: observe-only diagnostic

```text
branch_type: observe
privilege: observe_only
mode: O1
verifier_targets: artifact_exists
```

Expected:

```text
admitted
runs first
```

### Branch B: minimal patch

```text
branch_type: minimal_patch
privilege: local_patch
mode: O1
write_set: app.py
verifier_targets: pytest
```

Expected:

```text
admitted
runs after observe/test
```

### Branch C: duplicate minimal patch

Same hypothesis/read/write/verifier as Branch B.

Expected:

```text
merged into Branch B
duplicate recorded
```

### Branch D: broad rewrite

```text
branch_type: refactor_candidate
mode: O1
patch_radius: 5
write_set: many files
```

Expected:

```text
rejected or downgraded to diagnostic
reason: exceeds O1 mode contract
```

### Branch E: metric self-gaming

```text
branch_type: metric_patch
contract_write_set: MetricContract:QPM
claim: QPM improved
```

Expected:

```text
hard rejected
```

### Branch F: verifier self-validation risk

```text
branch_type: verifier_patch
contract_write_set: VerifierContract:unit_tests
no meta-verifier
```

Expected:

```text
quarantined or rejected
```

### Branch G: O3 patch candidate

```text
mode: O3
branch_type: minimal_patch
commit_policy: merge
```

Expected:

```text
commit_policy changed to quarantine unless promotion_candidate
```

Phase 2 is successful if the runtime produces a valid `branch_plan.json` and only admitted branches can proceed to workspace creation.

---

# 16. Required Tests

## PassManager tests

```text
passes execute in required order
hard reject stops later passes for branch
pass results are written
events are emitted for each pass
```

## DeadBranchElimination tests

```text
rejects branch with no verifier targets
rejects branch with no expected evidence
rejects branch exceeding mode max_patch_radius
rejects promotion_candidate without verified artifact
rejects O3 direct commit candidate
```

## DuplicateBranchMerge tests

```text
merges exact duplicate branches
preserves union of verifier targets
preserves union of expected evidence
records duplicate branch replay
does not merge branches with different write_set
does not merge branches with different contract_write_set
```

## BasicConflictAnalysis tests

```text
detects file write/write conflict
detects file write/read invalidation
detects contract write/write conflict
detects contract write/read invalidation
detects MetricContract self-gaming
detects VerifierContract self-validation risk
```

## StrengthReduction tests

```text
clamps depth to mode max_depth
clamps or rejects patch_radius above mode contract
downgrades broad O1 patch to diagnostic
marks O3 patch commit_policy quarantine
adds required verifier targets for contract writes
does not increase privilege
does not expand write_set
does not remove evidence requirements
```

## AdmissionScoring tests

```text
normalizes all terms to 0.0–1.0
hard rejected branches cannot be admitted
high score branch is admitted
medium score branch is deferred/downgraded
low score branch is rejected/quarantined
mode max branch count is respected
```

## BranchPlan tests

```text
plan includes admitted/rejected/quarantined branches
execution order puts observe/test/diagnostic first
conflict groups are included
duplicate groups are included
shared diagnostics are included
plan written to .runtime/tasks/<task_id>/branch_plan.json
```

## CLI tests

```text
specctl optimize produces branch_plan.json
specctl plan show prints plan
specctl conflicts show prints conflicts
specctl admissions show prints decisions
workspace creation is blocked for non-admitted branches
```

---

# 17. Acceptance Criteria

Phase 2 is complete when:

```text
1. Multiple candidate branches can be optimized as a task group.
2. PassManager runs deterministic pass order.
3. Pass results are persisted per branch.
4. Invalid branches are rejected before workspace creation.
5. Duplicate branches are merged before execution.
6. Basic file conflicts are detected.
7. Basic contract conflicts are detected.
8. Strength reduction downgrades or clamps overbroad branches.
9. Admission scoring produces transparent normalized terms.
10. O-mode limits are enforced during optimization.
11. BranchPlan is produced for the task.
12. Only admitted branches can create workspaces.
13. Every pass decision is written to the event log.
14. Rejected/quarantined/merged branches still produce replay records.
15. Phase 1 commit gates remain unchanged and authoritative.
16. Full test suite passes.
```

---

# 18. Implementation Sequence for an Agent

## Step 1 — Add new schemas

Implement:

```text
PassResult
AdmissionDecision
BranchPlan
ConflictReport
OptimizationContext
```

Add schema tests.

---

## Step 2 — Add optimizer package

Create:

```text
optimizer/pass_manager.py
optimizer/branch_optimizer.py
optimizer/scoring.py
optimizer/normalization.py
optimizer/branch_plan_builder.py
```

---

## Step 3 — Convert Phase 1 validators into passes

Wrap existing validators:

```text
PermissionValidationPass
ForbiddenWriteSetPass
SnapshotBindingPass
VerifierRequirementPass
EvidenceRequirementPass
ContractValidationPass
```

These should call the same underlying validation logic Phase 1 uses.

---

## Step 4 — Implement DeadBranchEliminationPass

Start with deterministic hard rules.

Do not use model calls.

---

## Step 5 — Implement DuplicateBranchMergePass

Use exact normalized field matching.

No semantic embeddings yet.

---

## Step 6 — Implement BasicConflictAnalysisPass

Use declared file and contract read/write sets.

No inferred semantic aliasing yet.

---

## Step 7 — Implement StrengthReductionPass

Implement safe transformations only:

```text
depth reduction
patch radius clamp/reject
commit_policy downgrade to quarantine
branch_type downgrade to diagnostic when justified
required verifier target addition
```

---

## Step 8 — Implement AdmissionScoringPass

Normalize terms.

Apply thresholds.

Respect hard rejections and mode branch limits.

---

## Step 9 — Implement BranchPlanBuilder

Generate task-level `branch_plan.json`.

---

## Step 10 — Add CLI commands

Implement:

```text
specctl optimize
specctl plan show
specctl conflicts show
specctl admissions show
specctl passes show
```

---

## Step 11 — Enforce admitted-only workspace creation

Modify `WorkspaceManager` or CLI guard:

```text
workspace create fails unless branch status == optimization_admitted
```

This is key.

Phase 2 optimization must actually control execution.

---

## Step 12 — Add tests and demo

Build the demo branch set and verify optimization behavior.

---

# 19. Agent Handoff Prompt for Phase 2

```text
You are implementing Phase 2 of a microkernel-first speculative process runtime.

Phase 1 already provides:
- TaskPacket
- BranchTicket
- BranchIR
- SnapshotManager
- WorkspaceManager
- PermissionValidator
- ContractResourceRegistry
- VerifierRunner
- ClaimLedger
- CommitManager
- ReplayWriter
- RuntimeEventLog

Do not implement live web research.
Do not implement learned policy.
Do not implement distributed workers.
Do not implement parallel execution.
Do not implement advanced semantic alias inference.
Do not weaken any Phase 1 safety invariant.

Your task is to build the Basic Compiler Branch Handler.

Implement:
1. PassResult, AdmissionDecision, BranchPlan, ConflictReport, OptimizationContext schemas.
2. PassManager with deterministic pass order.
3. Safety passes wrapping existing Phase 1 validators.
4. DeadBranchEliminationPass.
5. DuplicateBranchMergePass using exact normalized fields.
6. BasicConflictAnalysisPass using file and contract read/write sets.
7. StrengthReductionPass for depth reduction, patch-radius clamping/rejection, commit-policy downgrade, and verifier-target additions.
8. AdmissionScoringPass with normalized 0.0–1.0 terms.
9. BranchPlanBuilder.
10. CLI commands:
   - specctl optimize
   - specctl plan show
   - specctl conflicts show
   - specctl admissions show
   - specctl passes show
11. Enforce that only optimization_admitted branches may create workspaces.

Hard requirements:
- No optimization pass may increase privilege.
- No optimization pass may expand write_set.
- No optimization pass may remove required verifier targets.
- No optimization pass may remove evidence obligations.
- No optimization pass may make O3 branches commit eligible unless they are promotion_candidate branches.
- Every pass decision must be logged as a RuntimeEvent.
- Rejected, duplicated, deferred, and quarantined branches must still write replay records.
- Phase 1 CommitManager remains the only component allowed to apply changes to durable state.

Phase 2 is complete when the test suite proves:
- invalid branches are rejected before workspace creation,
- duplicates are merged,
- basic file and contract conflicts are detected,
- overbroad branches are downgraded or rejected,
- admission scoring is transparent and mode-aware,
- BranchPlan is written,
- only admitted branches can execute,
- all pass decisions are event-logged,
- Phase 1 safety gates remain authoritative.
```

---

# 20. Final Phase 2 Deliverable

The Phase 2 deliverable is a **compiler-style branch optimizer**.

At the end of Phase 2, the runtime should be able to say:

```text
The model proposed several branches.
The runtime lowered them into BranchIR.
The pass manager rejected invalid branches.
The duplicate pass merged redundant branches.
The conflict pass found file and contract hazards.
The strength reduction pass downgraded overbroad work into cheaper probes.
The admission scorer admitted only useful, mode-valid branches.
Only admitted branches were allowed to execute.
Every decision was replayed.
```

That is the correct next step after the Phase 1 microkernel.
