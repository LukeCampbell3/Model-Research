# Phase 2 Branch Compiler Baseline — FROZEN

**Frozen:** 2026-06-10
**Status:** VALIDATED
**Tests:** 144/144 pass
**Phase 1 Baseline:** PRESERVED (112/112)
**Phase 2 Tests Added:** 32

---

## Test Summary

| Suite | Tests | Status |
|-------|-------|--------|
| Core (test_core.py) | 49 | PASS |
| Hallucination + Efficiency (test_hallucination_efficiency.py) | 30 | PASS |
| Stress (test_stress.py) | 33 | PASS |
| **Compiler (test_compiler.py)** | **32** | **PASS** |

---

## Compiler Passes

| Pass | Purpose | Behavior |
|------|---------|----------|
| DeadBranchElimination | Remove provably dead branches | Kills: zero upside, stale parent, cancelled/failed, budget-exceeds-value |
| DuplicateBranchMerge | Merge semantically identical branches | Merges: keyword overlap ≥80%, same parent. Survivor inherits best attrs |
| BasicConflictAnalysis | Detect inter-branch conflicts | **Annotates only** — does not eliminate. Penalizes via downstream scoring |
| StrengthReduction | Simplify over-specified branches | Dedup evidence, clamp upside, reduce trivial costs, downgrade invalid commit candidates |
| AdmissionScoring | Score and filter for workspace admission | Composite score: upside, priority, efficiency, conflict penalty, evidence readiness |

---

## Workspace Gate Behavior

- `BranchPlan.can_create_workspace` returns `True` only if at least one branch passes admission
- `BranchPlan.admitted` is the only set that receives workspace allocation
- Rejected branches are archived with explicit rejection reasons
- The workspace gate is an **execution admission** gate, NOT a commit authority

---

## Phase 2 Invariants (FROZEN)

These invariants must hold for all compiler passes, present and future:

### 1. No compiler pass may increase privilege.
A branch entering the compiler with read-only scope cannot exit with write scope.
The compiler transforms branch metadata — it does not grant capabilities.

### 2. No compiler pass may expand write scope.
If a branch's `side_effect_policy` is `READ_ONLY`, no pass may change it to
`TRANSACTIONAL_WRITE` or `EXTERNAL_REVERSIBLE_ACTION`.

### 3. No compiler pass may remove verifier requirements.
If a branch requires verification (`validation_required=True`), no pass may
set it to `False`. StrengthReduction may downgrade types but cannot remove
the verification obligation.

### 4. No compiler pass may remove evidence obligations.
If a branch has `evidence_needed`, passes may deduplicate or cap the list,
but may not empty it entirely when the branch depends on that evidence for
commit eligibility.

### 5. No compiler pass may make Level 0 branches commit-eligible directly.
A `BRANCH_SEED` (expansion_level=0) cannot be promoted to `COMMIT_CANDIDATE`
by any compiler pass. Promotion requires evidence collection and verification
through the full runtime lifecycle.

### 6. Conflict analysis may annotate, penalize, order, or quarantine, but must not silently erase useful diagnostic branches.
`BasicConflictAnalysis` produces annotations and conflict records. It does NOT
reduce the branch set. Conflicting branches remain in the pipeline for downstream
scoring — they receive penalties, not deletion.

### 7. BranchPlan remains advisory for execution, not authority for commit.
The BranchPlan controls which branches are admitted to workspace creation.
It does NOT control whether a branch's output can be committed to canonical state.
Commit authority belongs exclusively to the CommitManager + verification gate.

### 8. CommitManager remains the only component that mutates durable state.
No compiler pass, admission scorer, branch plan, or workspace controller may
write to the CanonicalState, EvidenceLedger, or ClaimRegistry as a side effect
of compilation. Only the `CanonicalStateCommitter` (via verified transaction)
may advance canonical state.

---

## Authority Separation (Critical Doctrine)

```
┌─────────────────────────────────────────────────────────────────┐
│  BranchPlan                    │  CommitManager                  │
│  ─────────                     │  ─────────────                  │
│  Controls: execution admission │  Controls: durable state        │
│  Scope: which branches get     │  Scope: which outputs become    │
│         workspaces             │         canonical state          │
│  Authority: advisory           │  Authority: authoritative        │
│  Can reject: yes               │  Can reject: yes                │
│  Can commit: NO                │  Can commit: YES (with evidence)│
│  Mutates state: NO             │  Mutates state: YES             │
└─────────────────────────────────────────────────────────────────┘

These MUST NOT collapse into the same authority.
```

---

## Known Limitations

- Conflict analysis uses keyword heuristics, not semantic understanding
- Admission scoring novelty bonus is placeholder (not yet similarity-based)
- DuplicateBranchMerge is O(n²) within each parent-hash group
- No inter-pass optimization (passes don't share intermediate representations)
- BranchPlan doesn't yet enforce budget limits across the admitted set

---

## System Summary at Freeze

```
v0.2 Runtime Architecture:

1. Model proposes branches
2. Runtime stores typed speculative state
3. Compiler filters, merges, annotates, simplifies, and scores branches
4. Only admitted branches may create workspaces
5. Branches execute under the Phase 1 microkernel
6. Verifier and commit gates remain authoritative
7. Replay tracks outcomes

Safety: Claims require evidence. Commits require verification.
Efficiency: Dead branches eliminated. Duplicates merged. Admission gated.
Separation: Execution admission ≠ commit authority.
```

---

## Next Phase Boundary

**Phase 3 should add:**

| Component | Purpose |
|-----------|---------|
| ResearchGateway | Bounded autonomous research initiation |
| PromptInjectionBoundary | Input sanitization at expert boundary |
| EvidencePacket v2 | Structured evidence with provenance chains |
| ReplayPatternMemory | Learn from replay traces |
| PolicyMemory with decay | Time-decayed learned heuristics |
| ContextCompiler | Compile context pages for expert inputs |
| Adjudicator | Resolve conflicts between branch outcomes |
| PromotionGate | Evidence-gated capability upgrades |
| RuntimeAuditReporter | Structured audit trail generation |

**Phase 3 must not violate Phase 2 invariants.**
The compiler's authority boundary is frozen.
