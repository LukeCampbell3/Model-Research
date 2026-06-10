Below is a robust **Phase 1 implementation plan** using the validation feedback. The goal is to build the smallest useful runtime that enforces the core safety invariants before adding research, replay priors, learned scheduling, or advanced compiler passes.

# Phase 1 Goal

Build a **local speculative process microkernel**.

It should prove this doctrine:

```text
The model proposes.
The runtime owns authority.
The verifier owns truth-testing.
The commit manager owns durable state.
Replay owns regret.
```

Phase 1 does **not** build the full cognitive runtime. It builds the safety kernel that makes unsafe agent behavior impossible to commit.

---

# 1. Phase 1 Scope

## Build in Phase 1

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
Basic mode contracts
Basic branch passes
CLI
Tests
```

## Do not build in Phase 1

```text
live web research
learned policy
distributed workers
parallel execution
database-backed replay
advanced semantic alias inference
full Pareto adjudication
multi-agent orchestration
complex benchmark scheduling
```

Phase 1 should be local, file-based, deterministic, and easy for an implementation agent to reason about.

---

# 2. Phase 1 Hard Invariants

These are non-negotiable. The runtime should fail closed if any invariant is violated.

```text
Invariant 1:
No branch can mutate durable state directly.

Invariant 2:
Every branch must run in an isolated workspace.

Invariant 3:
Every branch must have a TaskPacket, BranchTicket, and BranchIR.

Invariant 4:
Every branch must declare file read/write sets and contract read/write sets.

Invariant 5:
Forbidden write sets are enforced before execution and before commit.

Invariant 6:
No branch can commit without verifier output.

Invariant 7:
No claim can become durable knowledge without evidence status.

Invariant 8:
Metric-definition changes cannot claim metric improvement in the same branch.

Invariant 9:
A branch that modifies verifier logic cannot use the modified verifier as sole evidence for its own success.

Invariant 10:
External sources may update evidence, never authority.

Invariant 11:
If the base snapshot or evidence context changes, verification must rerun or the branch is quarantined.

Invariant 12:
Every meaningful runtime decision must be written to the append-only event log.
```

---

# 3. Recommended Repo Structure

```text
spec_runtime/
  __init__.py

  schemas/
    task_packet.py
    branch_ticket.py
    branch_ir.py
    claim_ledger.py
    evidence_packet.py
    replay_record.py
    contract_resource.py
    runtime_event.py
    verifier_result.py
    mode_contract.py

  core/
    snapshot_manager.py
    workspace_manager.py
    branch_decoder.py
    branch_ir_lowerer.py
    permission_validator.py
    contract_registry.py
    verifier_runner.py
    claim_validator.py
    commit_manager.py
    replay_writer.py
    event_log.py
    invalidation.py

  modes/
    optimization_modes.py
    mode_contracts.py

  passes/
    pass_manager.py
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

  cli/
    specctl.py

  tests/
    test_task_packet.py
    test_branch_ticket.py
    test_branch_ir.py
    test_workspace_isolation.py
    test_permission_validator.py
    test_contract_registry.py
    test_commit_gate.py
    test_claim_ledger.py
    test_verifier_self_validation.py
    test_branch_invalidation.py
    test_event_log.py
    test_replay_writer.py
```

Runtime artifacts should live outside the source modules:

```text
.runtime/
  snapshots/
  branches/
    branch_<id>/
      branch_ticket.json
      branch_ir.json
      patch.diff
      claims.json
      evidence.json
      verifier_result.json
      replay_record.json
      events.jsonl
      artifacts/
      workspace/
  replay/
    replay_log.jsonl
  contracts/
    contracts.json
  events/
    runtime_events.jsonl
```

Do not start with a database. JSON and JSONL are enough for Phase 1.

---

# 4. Core Schemas

## 4.1 TaskPacket

Purpose: define the task boundary.

```python
class TaskPacket:
    task_id: str
    task_objective: str
    task_type: str
    created_at: str

    affected_subsystems: list[str]
    risk_level: str

    required_outputs: list[str]
    forbidden_actions: list[str]

    max_branches: int
    max_patch_radius: int
    max_verifier_cost: str

    authority_notes: list[str]
    human_constraints: list[str]
```

Phase 1 validation:

```text
task_id is required
task_objective is required
risk_level is one of low/medium/high
forbidden_actions defaults to []
max_patch_radius must be >= 0
```

---

## 4.2 BranchTicket

Purpose: typed branch proposal.

```python
class BranchTicket:
    ticket_id: str
    parent_task_id: str
    state_snapshot_id: str

    task_objective: str
    hypothesis: str
    branch_family: str
    branch_type: str

    privilege_level: str
    optimization_mode: str

    patch_radius: int
    affected_subsystems: list[str]
    affected_files: list[str]

    read_set: list[str]
    expected_write_set: list[str]
    forbidden_write_set: list[str]

    contract_read_set: list[str]
    contract_write_set: list[str]

    allowed_tools: list[str]
    research_policy: str
    network_policy: str
    secret_policy: str
    artifact_policy: str

    verifier_targets: list[str]
    expected_evidence: list[str]
    merge_policy: str

    risk: float
    reversibility: float
    expected_information_gain: float
    expected_failure_reduction: float
    expected_metric_gain: float
    expected_future_value: float
    conflict_risk: float
```

Phase 1 branch types:

```text
observe
test_only
diagnostic
minimal_patch
config_patch
metric_patch
verifier_patch
promotion_candidate
rollback_candidate
```

`research` exists as a schema value, but live research is disabled in Phase 1.

---

## 4.3 BranchIR

Purpose: executable/optimizable runtime representation.

```python
class BranchIR:
    branch_id: str
    task_id: str
    objective: str
    hypothesis: str

    branch_type: str
    branch_family: str
    privilege_level: str
    optimization_mode: str

    inputs: list[str]
    outputs: list[str]

    read_set: list[str]
    write_set: list[str]
    forbidden_write_set: list[str]

    contract_read_set: list[str]
    contract_write_set: list[str]
    semantic_assumption_set: list[str]

    side_effects: list[str]
    dependencies: list[str]
    invariants: list[str]

    verifier_targets: list[str]
    expected_evidence: list[str]

    cost_estimate: float
    risk_estimate: float
    information_gain_estimate: float
    future_state_estimate: float

    execution_depth: int
    cache_requirements: list[str]
    commit_policy: str

    base_snapshot_id: str
    evidence_context_hash: str | None
```

Phase 1 rule:

```text
BranchIR is the only object passed into execution, verification, and commit.
```

The runtime should not execute raw model text or raw branch tickets.

---

## 4.4 ContractResource

Purpose: practical semantic conflict detection.

```python
class ContractResource:
    contract_id: str
    contract_type: str
    owner_subsystem: str

    read_claims: list[str]
    write_claims: list[str]

    verifier_requirements: list[str]
    invalidation_rules: list[str]

    description: str
```

Examples:

```json
{
  "contract_id": "MetricContract:QPM",
  "contract_type": "MetricContract",
  "owner_subsystem": "metrics",
  "read_claims": ["reads QPM definition", "claims QPM movement"],
  "write_claims": ["changes QPM definition"],
  "verifier_requirements": ["metric_definition_diff", "metric_regression_control"],
  "invalidation_rules": [
    "invalidate branches that claimed QPM improvement against previous definition"
  ],
  "description": "Quality-per-millisecond metric contract."
}
```

Phase 1 conflict rule:

```text
If one branch writes a contract another branch reads, the reader branch is invalidated or must rerun verification.
```

---

## 4.5 EvidencePacket

Phase 1 evidence can be local only. Live web evidence comes later.

```python
class EvidencePacket:
    evidence_id: str
    branch_id: str
    evidence_type: str

    source_kind: str
    source_ref: str

    claim_supported: str
    summary: str

    freshness_score: float
    directness_score: float
    reliability_score: float

    limitations: list[str]
    conflicts: list[str]

    evidence_context_hash: str
```

Allowed `source_kind` in Phase 1:

```text
local_file
test_output
verifier_output
runtime_artifact
manual_note
cached_evidence
```

Blocked in Phase 1:

```text
live_web_page
external_pdf
github_issue
forum_post
```

The schema can support them later, but Phase 1 should not fetch them.

---

## 4.6 ClaimLedger

Purpose: prevent unsupported conclusions from becoming durable memory.

```python
class Claim:
    claim_id: str
    claim: str
    claim_type: str

    evidence_ids: list[str]
    counterevidence_ids: list[str]

    assumptions: list[str]
    unknowns: list[str]

    confidence: float
    status: str
```

Statuses:

```text
supported
weakly_supported
unsupported
conflicted
stale
not_checked
```

`ClaimLedger`:

```python
class ClaimLedger:
    branch_id: str
    claims: list[Claim]
    unsupported_claims: list[str]
    unknowns: list[str]
```

Phase 1 commit rule:

```text
A branch with claims marked unsupported, conflicted, stale, or not_checked cannot commit those claims as durable knowledge.
```

---

## 4.7 VerifierResult

```python
class VerifierResult:
    verifier_result_id: str
    branch_id: str
    verifier_id: str

    started_at: str
    finished_at: str

    status: str
    command: str
    exit_code: int

    stdout_ref: str
    stderr_ref: str

    metrics: dict
    artifacts: list[str]

    verifier_version_hash: str
    evidence_context_hash: str
```

Statuses:

```text
pass
fail
partial
inconclusive
quarantine
requires_rerun
requires_human_review
```

---

## 4.8 RuntimeEvent

This is the minimal append-only event log schema.

```python
class RuntimeEvent:
    event_id: str
    timestamp: str

    task_id: str | None
    branch_id: str | None

    event_type: str
    snapshot_id: str | None

    actor: str

    input_refs: list[str]
    output_refs: list[str]

    decision: str | None
    reason: str | None
```

Required event types:

```text
task_created
snapshot_created
branch_fetched
branch_decoded
branch_lowered
branch_rejected
branch_admitted
workspace_created
branch_execution_started
branch_execution_finished
verifier_started
verifier_finished
claim_recorded
commit_attempted
commit_succeeded
commit_rejected
branch_invalidated
rollback_created
replay_written
```

The event log should be append-only JSONL.

---

# 5. Enforceable O-Modes for Phase 1

Phase 1 should include mode contracts even if advanced scheduling is deferred.

```python
class ModeContract:
    mode: str
    max_depth: int
    max_patch_radius: int
    max_branches: int
    max_model_calls: int | None
    research_default_level: str
    research_max_level: str
    background_allowed: bool
    commit_eligible: bool
    trace_preservation_required: bool
```

## Os

```text
max_depth: 1
max_patch_radius: 1
max_branches: 1
research_default_level: R0
research_max_level: R0
background_allowed: false
commit_eligible: true
trace_preservation_required: false
```

## O1

```text
max_depth: 2
max_patch_radius: 2
max_branches: 2
research_default_level: R1
research_max_level: R1
background_allowed: false
commit_eligible: true
trace_preservation_required: false
```

## O2

Corrected per feedback:

```text
max_depth: 3
max_patch_radius: 3
max_branches: 4
research_default_level: R1/R2
research_max_level: R3 only if correctness depends on an external fact
background_allowed: limited
commit_eligible: true
trace_preservation_required: false
```

Phase 1 does not perform live research, but the contract should be defined for later.

## O3

```text
max_depth: 5
max_patch_radius: 4
max_branches: 6
research_default_level: R2
research_max_level: R4
background_allowed: true
commit_eligible: false unless promoted through gate
trace_preservation_required: true
```

## Og

```text
max_depth: diagnostic-dependent
max_patch_radius: 1
max_branches: 4
research_default_level: R2
research_max_level: R5
background_allowed: true
commit_eligible: usually false
trace_preservation_required: true
```

Phase 1 enforcement:

```text
ModeContract must be checked during BranchIR lowering and before execution.
```

---

# 6. Promotion Candidate Rule

Clarify this early.

```text
promotion_candidate branches do not perform new risky work.
```

A promotion branch may:

```text
read already-produced branch artifacts
read verifier results
read replay records
read contract status
evaluate commit eligibility
produce a promotion recommendation
```

A promotion branch may not:

```text
modify source logic
change metrics
change verifier logic
create a new risky patch
self-approve a failed branch
bypass commit checks
```

Promotion means:

```text
Move already-verified work from quarantine/background status to commit eligibility.
```

It does not mean:

```text
Do more powerful patching.
```

---

# 7. Verifier Self-Validation Rule

Add this invariant from the feedback:

```text
A branch that modifies verifier logic cannot use the modified verifier as sole evidence for its own success.
```

A verifier patch requires at least one of:

```text
previous verifier baseline
golden fixtures
meta-verifier tests
cross-check against unchanged external checks
human approval
```

Phase 1 implementation:

If `branch_type == verifier_patch` or `contract_write_set` includes a `VerifierContract`, then commit requires:

```text
verifier_self_validation_safe = true
```

This flag can be produced by a meta-verifier or manually set in a controlled test fixture for Phase 1.

---

# 8. Branch Invalidation Rules

Phase 1 should include simple invalidation.

Invalidate or quarantine a branch if:

```text
base snapshot changed and branch cannot rebase cleanly
required contract was written by another committed branch
verifier version changed
dataset hash changed
metric definition changed
task objective changed
branch exceeded mode budget
branch exceeded verifier budget
evidence context hash changed
forbidden write was detected
claim evidence became stale
```

Add an `InvalidationReason` enum:

```text
base_snapshot_changed
contract_invalidated
verifier_changed
dataset_changed
metric_definition_changed
task_changed
budget_exceeded
evidence_context_changed
forbidden_write_detected
claim_stale
```

Branch statuses:

```text
created
decoded
lowered
rejected
admitted
executing
executed
verifying
verified
failed
invalidated
quarantined
commit_candidate
committed
commit_rejected
rolled_back
```

---

# 9. Core Components and Responsibilities

## 9.1 SnapshotManager

Responsibilities:

```text
create snapshot
compute snapshot hash
record snapshot metadata
validate current state against snapshot
compute evidence context hash
```

MVP implementation:

```text
Use git hash if inside a git repo.
Otherwise compute recursive file hash.
Exclude .runtime/, .git/, __pycache__, node_modules, venv by default.
```

Primary methods:

```python
create_snapshot(root_path) -> SnapshotRecord
compute_snapshot_hash(root_path) -> str
validate_snapshot(snapshot_id, root_path) -> bool
```

---

## 9.2 WorkspaceManager

Responsibilities:

```text
create isolated branch workspace
copy or checkout snapshot state
prevent writes to main repo
collect diff
store artifacts
clean workspace
```

MVP implementation options:

```text
If git repo: use git worktree or copytree.
If non-git repo: use copytree into .runtime/branches/<id>/workspace.
```

Primary methods:

```python
create_workspace(branch_ir) -> Path
collect_diff(branch_id) -> Path
list_changed_files(branch_id) -> list[str]
```

Important:

```text
All execution commands run with cwd set to branch workspace.
No command runs from main repo root.
```

---

## 9.3 PermissionValidator

Responsibilities:

```text
validate branch type and privilege compatibility
validate mode limits
validate read/write sets
validate forbidden write sets
validate tool/network policy
validate contract read/write declarations
```

Phase 1 should block:

```text
observe_only writing source
research_only patching source
test_generation editing production source
local_patch redefining metrics
metric_patch claiming metric improvement
verifier_patch self-validating
any branch writing forbidden paths
any branch exceeding patch radius
any branch using network if network_policy is disabled
```

---

## 9.4 ContractResourceRegistry

Responsibilities:

```text
load contracts.json
validate branch contract references
detect contract read/write conflicts
apply invalidation rules
```

Primary methods:

```python
load_contracts(path) -> list[ContractResource]
validate_contract_sets(branch_ir) -> ValidationResult
detect_conflicts(branch_ir, committed_records) -> list[Conflict]
```

---

## 9.5 VerifierRunner

Responsibilities:

```text
run allowed verifier commands
capture stdout/stderr
capture exit code
write verifier_result.json
compute verifier version hash
emit verifier events
```

Verifier config example:

```json
{
  "verifiers": [
    {
      "verifier_id": "unit_tests",
      "command": "pytest -q",
      "timeout_seconds": 120,
      "required_for": ["minimal_patch", "config_patch"]
    },
    {
      "verifier_id": "claim_ledger_check",
      "command": "specctl validate-claims",
      "timeout_seconds": 30,
      "required_for": ["all"]
    }
  ]
}
```

Phase 1 can start with shell commands and timeouts.

---

## 9.6 ClaimValidator

Responsibilities:

```text
ensure every claim has evidence IDs
ensure evidence files exist
ensure evidence context hash matches
ensure unsupported claims are not promoted
enforce metric-claim rule
enforce external-source authority rule
```

Phase 1 rules:

```text
No evidence ID → claim is not_checked.
Evidence file missing → claim is unsupported.
Evidence context mismatch → claim is stale.
Metric definition write + metric improvement claim → commit blocked.
```

---

## 9.7 CommitManager

Responsibilities:

```text
validate snapshot unchanged
validate branch status
validate verifier passed
validate claims supported
validate contract conflicts
validate forbidden writes
validate rollback exists
apply patch
write commit result
emit event
write replay
```

Commit gate order:

```text
1. Load BranchIR.
2. Validate base snapshot.
3. Validate branch was executed in isolated workspace.
4. Validate changed files are within write_set.
5. Validate forbidden_write_set untouched.
6. Validate contract conflicts.
7. Validate verifier result.
8. Validate claim ledger.
9. Validate verifier self-validation rule.
10. Create rollback record.
11. Apply patch.
12. Write commit event.
13. Write replay record.
```

Phase 1 can implement patch application by copying changed files from workspace into main repo only after the gate passes.

---

## 9.8 ReplayWriter

Responsibilities:

```text
write replay_record.json
append replay_log.jsonl
include branch outcome, verifier result, claims, conflicts, invalidation reason, commit decision
```

ReplayRecord schema:

```python
class ReplayRecord:
    replay_id: str
    task_id: str
    branch_id: str

    branch_type: str
    branch_family: str
    optimization_mode: str
    privilege_level: str

    hypothesis: str
    outcome: str

    verifier_status: str
    commit_status: str

    claims_summary: dict
    evidence_summary: dict
    contract_conflicts: list[str]
    invalidation_reasons: list[str]

    patch_files_changed: list[str]
    patch_line_count: int

    regret_status: str
    notes: list[str]
```

Phase 1 regret can be simple:

```text
unknown
none_observed
potential
confirmed
```

---

## 9.9 RuntimeEventLog

Responsibilities:

```text
append RuntimeEvent records
ensure every major transition is logged
support event replay/debugging
```

Phase 1 storage:

```text
.runtime/events/runtime_events.jsonl
.runtime/branches/<branch_id>/events.jsonl
```

---

# 10. Basic Branch Passes for Phase 1

Do not overbuild the optimizer. Implement the useful safety/waste passes.

## Pass order

```text
1. PermissionValidationPass
2. ForbiddenWriteSetPass
3. SnapshotBindingPass
4. VerifierRequirementPass
5. EvidenceRequirementPass
6. ContractValidationPass
7. DeadBranchElimination
8. DuplicateBranchMerge
9. BasicConflictAnalysis
10. StrengthReduction
11. AdmissionScoring
```

## DeadBranchElimination

Reject if:

```text
no hypothesis
no verifier targets
no expected evidence
write_set intersects forbidden_write_set
patch_radius exceeds mode contract
branch_type incompatible with privilege
```

## DuplicateBranchMerge

For Phase 1:

```text
If two branches have same hypothesis, read_set, write_set, and verifier_targets,
keep one and mark the other duplicate.
```

## BasicConflictAnalysis

Detect:

```text
file write/write conflicts
file write/read invalidation
contract write/write conflicts
contract write/read invalidation
forbidden write conflicts
```

## StrengthReduction

For Phase 1, this can be simple:

```text
If branch asks for depth > mode max_depth, lower to mode max_depth.
If O3 branch is commit_eligible, mark commit_eligible false unless promotion_candidate.
If broad patch_radius requested, clamp or reject.
```

---

# 11. CLI Design

A simple CLI makes this easy for agents and tests.

Use Typer or argparse.

Recommended commands:

```text
specctl init
specctl create-task --objective "... "
specctl snapshot create
specctl branch create --task <task_id> --ticket ticket.json
specctl branch lower --branch <branch_id>
specctl branch validate --branch <branch_id>
specctl workspace create --branch <branch_id>
specctl branch execute --branch <branch_id> --command "..."
specctl verify --branch <branch_id> --verifier unit_tests
specctl claims validate --branch <branch_id>
specctl commit attempt --branch <branch_id>
specctl replay show --branch <branch_id>
specctl events tail
```

Phase 1 does not need a daemon. A CLI plus JSON files is enough.

---

# 12. Demo Scenario for Phase 1

The first end-to-end demo should prove the kernel.

## Demo setup

Create a tiny repo:

```text
demo_project/
  app.py
  tests/test_app.py
```

`app.py` has a small bug.

## Demo branches

### Branch A: observe-only

```text
branch_type: observe
privilege_level: observe_only
write_set: artifacts only
```

Expected result:

```text
allowed to write diagnostic artifact
not allowed to edit app.py
```

### Branch B: forbidden write

```text
branch_type: observe
privilege_level: observe_only
attempts to edit app.py
```

Expected result:

```text
rejected before commit
event logged
replay written
```

### Branch C: minimal patch

```text
branch_type: minimal_patch
privilege_level: local_patch
write_set: app.py
verifier: pytest
```

Expected result:

```text
runs in workspace
produces patch.diff
pytest passes
claim ledger references evidence
commit manager validates snapshot
patch applied to main repo
replay written
```

### Branch D: metric self-gaming

```text
branch_type: metric_patch
contract_write_set: MetricContract:QPM
claim: QPM improved
```

Expected result:

```text
commit rejected
reason: metric-definition change cannot claim metric improvement in same branch
```

### Branch E: verifier self-validation

```text
branch_type: verifier_patch
contract_write_set: VerifierContract:unit_tests
uses modified verifier as only evidence
```

Expected result:

```text
commit rejected
reason: verifier cannot verify itself
```

This demo proves the safety model.

---

# 13. Required Tests

## Schema tests

```text
TaskPacket rejects missing objective.
BranchTicket rejects unknown branch_type.
BranchIR requires base_snapshot_id.
ModeContract rejects invalid max_depth.
```

## Permission tests

```text
observe_only cannot write source.
test_generation cannot edit production source.
local_patch cannot write metric contracts.
metric_patch cannot claim metric improvement.
verifier_patch cannot self-validate.
```

## Workspace tests

```text
workspace is created outside main repo.
branch command runs inside workspace.
main repo unchanged before commit.
diff collection detects changed files.
```

## Snapshot tests

```text
snapshot hash changes when source changes.
commit rejected when base snapshot changed.
evidence context mismatch triggers quarantine.
```

## Contract tests

```text
contract read/write sets validated.
contract write invalidates dependent reader branch.
MetricContract write blocks same-branch improvement claim.
VerifierContract write triggers self-validation rule.
```

## Commit tests

```text
commit rejected without verifier result.
commit rejected if verifier failed.
commit rejected if changed files outside write_set.
commit rejected if forbidden file changed.
commit accepted when all gates pass.
rollback record created before commit.
```

## Claim tests

```text
claim without evidence marked not_checked.
missing evidence marks claim unsupported.
stale evidence blocks commit.
unsupported claims cannot be durable.
```

## Event log tests

```text
task_created event is written.
branch_lowered event is written.
verifier_finished event is written.
commit_rejected event includes reason.
runtime_events.jsonl is append-only.
```

## Replay tests

```text
replay record written for rejected branch.
replay record written for committed branch.
replay contains branch type, outcome, verifier status, claim status, and commit decision.
```

---

# 14. Acceptance Criteria

Phase 1 is complete when all of the following are true:

```text
1. A TaskPacket can be created and stored.
2. A BranchTicket can be created and validated.
3. A BranchTicket can be lowered into BranchIR.
4. A branch workspace can be created from a snapshot.
5. Branch execution cannot mutate the main repo.
6. Verifier commands run only inside the workspace.
7. Changed files are collected into a patch/diff.
8. Commit is rejected without passing verifier output.
9. Commit is rejected if snapshot changed.
10. Commit is rejected if branch changed forbidden files.
11. Commit is rejected if branch wrote undeclared contracts.
12. Commit is rejected if claim evidence is missing/stale/unsupported.
13. Commit is rejected for metric-definition plus same-branch metric improvement claim.
14. Commit is rejected for verifier self-validation.
15. Valid minimal patch can be committed through the commit manager.
16. Rollback artifact is created before commit.
17. Every major transition is written to event log.
18. Every branch outcome writes a replay record.
19. Unit tests cover the above.
```

---

# 15. Implementation Sequence for an Agent

Give the implementation agent a strict order.

## Step 1 — Create schemas

Implement Pydantic or dataclass schemas:

```text
TaskPacket
BranchTicket
BranchIR
ContractResource
EvidencePacket
ClaimLedger
VerifierResult
ReplayRecord
RuntimeEvent
ModeContract
```

Add schema tests.

---

## Step 2 — Create runtime directory manager

Implement:

```text
.runtime/
.runtime/snapshots/
.runtime/branches/
.runtime/replay/
.runtime/contracts/
.runtime/events/
```

Add `specctl init`.

---

## Step 3 — Implement SnapshotManager

Implement recursive hashing and snapshot records.

Add tests for hash changes.

---

## Step 4 — Implement WorkspaceManager

Implement isolated workspace creation.

Add tests proving main repo does not change before commit.

---

## Step 5 — Implement ModeContract enforcement

Implement `Os/O1/O2/O3/Og` contracts.

Add tests for max depth, patch radius, and research policy validation.

---

## Step 6 — Implement BranchIR lowering

Convert BranchTicket to BranchIR.

Apply initial validation.

Write `branch_ir.json`.

---

## Step 7 — Implement PermissionValidator

Enforce branch type, privilege, file sets, forbidden sets, and mode limits.

Add negative tests.

---

## Step 8 — Implement ContractResourceRegistry

Load `contracts.json`.

Validate contract read/write sets.

Detect basic contract conflicts.

---

## Step 9 — Implement VerifierRunner

Run configured commands in branch workspace.

Capture result into `verifier_result.json`.

Add timeout handling.

---

## Step 10 — Implement ClaimLedger validation

Validate evidence IDs and evidence context.

Implement metric self-gaming rule.

Implement verifier self-validation rule.

---

## Step 11 — Implement CommitManager

Gate order:

```text
snapshot
workspace
write_set
forbidden_write_set
contract conflicts
verifier result
claim ledger
self-validation
rollback creation
apply patch
event
replay
```

---

## Step 12 — Implement ReplayWriter and EventLog

Append JSONL records.

Ensure failed/rejected branches also produce replay.

---

## Step 13 — Implement CLI

Expose end-to-end commands.

---

## Step 14 — Build demo project and tests

Create the demo scenario and pass all tests.

---

# 16. Agent Handoff Prompt

Use this as the implementation prompt.

```text
You are implementing Phase 1 of a microkernel-first speculative process runtime.

Do not build the full mature cognitive runtime.
Do not implement live web research.
Do not implement learned policy.
Do not implement distributed workers.
Do not implement advanced semantic inference.
Do not implement parallel execution.

Build a local file-based runtime that enforces these invariants:

1. No branch can mutate durable state directly.
2. Every branch runs in an isolated workspace.
3. Every branch has a TaskPacket, BranchTicket, and BranchIR.
4. Every branch declares file read/write sets and contract read/write sets.
5. Forbidden write sets are enforced before execution and commit.
6. No branch can commit without verifier output.
7. No claim can become durable knowledge without evidence status.
8. Metric-definition changes cannot claim metric improvement in the same branch.
9. Verifier patches cannot use the modified verifier as sole evidence for their own success.
10. External sources may update evidence, never authority.
11. If snapshot or evidence context changes, verification must rerun or the branch is quarantined.
12. Every major transition must be written to an append-only event log.

Implement these modules:

- schemas: TaskPacket, BranchTicket, BranchIR, ContractResource, EvidencePacket, ClaimLedger, VerifierResult, ReplayRecord, RuntimeEvent, ModeContract
- core: SnapshotManager, WorkspaceManager, BranchIRLowerer, PermissionValidator, ContractResourceRegistry, VerifierRunner, ClaimValidator, CommitManager, ReplayWriter, EventLog
- modes: enforceable Os/O1/O2/O3/Og contracts
- passes: initial safety and waste-reduction passes
- cli: specctl
- tests: full safety invariant test suite

Use JSON and JSONL files under .runtime/.
Do not use a database.
Do not allow any execution command to run from the main repo root.
All branch execution must occur inside .runtime/branches/<branch_id>/workspace.
CommitManager is the only component allowed to apply branch changes back to durable state.

Phase 1 is complete only when tests prove:
- branches are isolated,
- forbidden writes are blocked,
- verifier-gated commits work,
- metric self-gaming is rejected,
- verifier self-validation is rejected,
- contract conflicts invalidate branches,
- snapshot changes block stale commits,
- replay records and runtime events are written for all outcomes.
```

---

# 17. Final Phase 1 Deliverable

The Phase 1 deliverable is not an intelligent agent.

It is a **safe local branch-control kernel**.

When complete, it should be able to say:

```text
A model may propose a patch.
The patch may execute only in isolation.
The patch may commit only through a verifier-gated transaction.
Every claim must point to evidence.
Every decision is replayable.
Unsafe branches fail closed.
```

That is the correct foundation. Once this works, Phase 2 can add stronger compiler passes, Phase 3 can add richer contract resources, Phase 4 can add the Research Gateway, and Phase 5 can add replay-based priors.
