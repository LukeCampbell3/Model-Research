# Phase 3: Multi-Expert Orchestration — Durable Memory, Research Processes, and Expert Ecosystem

## Status: PLANNED
## Timeline: Post-Phase 2 Policy Activation
## Prerequisite: Phase 2 policies active and stable for 30+ days

---

## 1. Objective

Evolve the cognitive microkernel from a single-expert system (PVR-EC-O only) to a multi-expert orchestration platform with durable memory, controlled research processes, and an expert ecosystem that can grow without architectural overhaul.

Phase 1 connected PVR-EC-O as the first expert. Phase 2 activated learned policies for routing and branch selection. Phase 3 unlocks the full cognitive architecture: multiple specialized experts, durable memory promotion, and controlled autonomous research — all gated by evidence quality and reversibility guarantees.

---

## 2. Scope

### What Unlocks in Phase 3

| Feature | V1 Status | Phase 2 Status | Phase 3 Status |
|---------|-----------|----------------|----------------|
| Expert Router | Shadow | Active | **Multi-Expert Active** |
| Branch Value Model | Shadow | Active | Active + Expert-Aware |
| Context Selector | Shadow | Shadow + Eval | **Conditionally Active** |
| Depth Policy | Shadow | Active | Active + Memory-Aware |
| Research Trigger | Shadow | Shadow + Eval | **Gated Active** |
| Memory Promotion | Blocked | Blocked | **Evidence-Gated Active** |
| Expert Adapters | Blocked | Blocked | **Offline Training Active** |
| Multi-Expert Execution | N/A | N/A | **Orchestrated** |
| Autonomous Research | Blocked | Blocked | **Bounded Active** |

### What Remains Blocked

| Feature | Reason |
|---------|--------|
| Irreversible actions without approval | Core safety doctrine |
| Unbounded compute allocation | Budget enforcement required |
| Direct production state mutation | Transactional-only |
| Expert self-modification during forward | Forward purity doctrine |

---

## 3. Multi-Expert Architecture

### 3.1 Expert Types

| Expert | Role | Status |
|--------|------|--------|
| PVR-EC-O (v1_1) | Primary task execution | **Deployed** |
| Retrieval Expert | Context retrieval from artifact store | Phase 3 |
| Verification Expert | Claim verification and evidence checking | Phase 3 |
| Planning Expert | Branch generation and strategy | Phase 3 |
| Research Expert | Bounded autonomous research | Phase 3 (gated) |

### 3.2 Expert Routing Matrix

The learned expert router (Phase 2) expands to multi-expert selection:

```
Process Type          → Primary Expert    → Fallback Expert
─────────────────────────────────────────────────────────────
observe_and_plan      → Planning Expert   → PVR-EC-O
verify_commit         → Verification Expert → PVR-EC-O
resolve_contradiction → PVR-EC-O          → Verification Expert
disambiguate          → PVR-EC-O          → Retrieval Expert
resolve_reference     → Retrieval Expert  → PVR-EC-O
execute_instruction   → PVR-EC-O          → Planning Expert
retrieve_structured   → Retrieval Expert  → PVR-EC-O
compare_equivalence   → PVR-EC-O          → Verification Expert
research_topic        → Research Expert   → PVR-EC-O (bounded)
```

### 3.3 Expert Composition Rules

- **Single-expert execution per token** (preserves Top1 doctrine per expert)
- **Sequential expert composition** allowed (expert A output → expert B input)
- **Parallel expert execution** allowed for independent branches
- **Expert disagreement** generates evidence, does not block commits
- **Expert cascade** limited to depth 3 (prevent infinite loops)

---

## 4. Durable Memory Promotion

### 4.1 What Memory Promotion Means

Items can be promoted from temporary evidence/speculation to durable memory:
- Frequently-accessed evidence records → Durable knowledge entries
- Validated claims with strong evidence → Durable facts
- Successful branch strategies → Durable heuristics
- Expert performance patterns → Durable routing preferences

### 4.2 Promotion Gate (Evidence-Based)

```python
class DurableMemoryPromotionGate:
    # All must be satisfied for promotion
    min_access_count: int = 10           # Accessed 10+ times
    min_evidence_support: float = 0.9    # 90% evidence supports
    min_replay_success: float = 0.95     # 95% replay succeeds
    max_contradiction_rate: float = 0.05 # <5% contradictions
    min_age_hours: int = 24              # At least 24h old
    requires_human_approval_first_10: bool = True  # First 10 need approval
    max_memory_size_mb: int = 100        # Total durable memory cap
```

### 4.3 Memory Lifecycle

```
Evidence Record
     │
     ▼ (access_count > 10, support > 90%)
Promotion Candidate
     │
     ▼ (gate passes)
Durable Memory Entry
     │
     ├── Active (used in context selection)
     ├── Archived (moved to cold storage after 90 days inactive)
     └── Revoked (contradicted by new evidence)
```

### 4.4 Memory Safety

- **Immutability:** Promoted memories are versioned, never mutated in place
- **Revocation:** New contradicting evidence can revoke (not delete) memories
- **Capacity:** Hard cap on total durable memory (100MB default)
- **Audit:** Every promotion logged with full evidence chain
- **Rollback:** Memory state can be rolled back to any prior version

---

## 5. Controlled Autonomous Research

### 5.1 What Research Means

The Research Expert can:
- Formulate hypotheses from evidence gaps
- Design experiments (branch sequences) to test hypotheses
- Execute bounded research processes with explicit budgets
- Report findings as evidence records

### 5.2 Research Constraints

```python
class ResearchBounds:
    max_budget_per_research: float = 10.0      # Max token budget per research
    max_concurrent_research: int = 2            # Max parallel research processes
    max_research_depth: int = 5                 # Max branch depth in research
    max_research_duration_hours: float = 1.0    # Max wall-clock time
    requires_justification: bool = True         # Must cite evidence gap
    requires_budget_approval: bool = True       # Budget must be pre-approved
    auto_terminate_on_loop: bool = True         # Detect and kill loops
    max_daily_research_count: int = 10          # Daily cap
```

### 5.3 Research Safety

- **Bounded:** Every research process has explicit budget and time limits
- **Justified:** Must cite an evidence gap or unsupported claim
- **Observable:** All research branches visible in ProcessDAG
- **Terminable:** Can be killed at any point without state corruption
- **Non-destructive:** Research cannot modify canonical state (speculative only)
- **Replayable:** Research traces stored for audit and replay

---

## 6. Expert Adapter Training (Offline)

### 6.1 Training Pipeline

```
Production Traces
     │
     ▼ (filter: successful commits only)
Training Data
     │
     ▼ (offline, separate from production)
Expert Adapter Candidates
     │
     ▼ (validation: held-out traces)
Candidate Evaluation
     │
     ▼ (deployment gate: same as PVR-EC-O gates)
New Expert Version
     │
     ▼ (canary → rollout)
Production Expert
```

### 6.2 Training Constraints

- **Offline only:** No training during production serving
- **Validation required:** Must pass deployment gates before promotion
- **Canary required:** Must pass canary before full rollout
- **Rollback ready:** Previous version always available
- **Evidence-linked:** Training data traced to evidence records

---

## 7. Deliverables

### 7.1 Multi-Expert System

```
cognitive_microkernel/src/cognitive_microkernel/experts/
├── __init__.py
├── expert_registry.py          # Expert lifecycle management
├── expert_composer.py          # Sequential/parallel composition
├── pvr_ec_expert.py           # (Phase 1) PVR-EC-O adapter
├── retrieval_expert.py        # Context retrieval from artifacts
├── verification_expert.py     # Claim verification
├── planning_expert.py         # Branch strategy generation
├── research_expert.py         # Bounded autonomous research
└── expert_cascade_guard.py    # Depth limit enforcement
```

### 7.2 Durable Memory

```
cognitive_microkernel/src/cognitive_microkernel/memory/
├── __init__.py
├── durable_store.py           # Versioned durable memory
├── promotion_gate.py          # Evidence-gated promotion
├── memory_lifecycle.py        # Active/archived/revoked states
├── memory_indexer.py          # Retrieval indexing
├── memory_capacity_guard.py   # Size cap enforcement
└── memory_audit_log.py        # Full promotion audit trail
```

### 7.3 Research Processes

```
cognitive_microkernel/src/cognitive_microkernel/research/
├── __init__.py
├── research_manager.py        # Research process lifecycle
├── hypothesis_generator.py    # Evidence gap → hypothesis
├── experiment_designer.py     # Hypothesis → branch sequence
├── research_bounds.py         # Budget/time/depth enforcement
├── research_terminator.py     # Loop detection and kill
└── research_reporter.py       # Findings → evidence records
```

### 7.4 Expert Training Pipeline

```
cognitive_microkernel/src/cognitive_microkernel/training/
├── __init__.py
├── trace_filter.py            # Filter production traces for training
├── training_data_builder.py   # Convert traces to training examples
├── adapter_trainer.py         # Train expert adapters offline
├── candidate_evaluator.py     # Validate against held-out traces
├── deployment_gate.py         # Same gates as PVR-EC-O
└── canary_controller.py       # Canary rollout for new experts
```

---

## 8. Validation Criteria

Phase 3 passes if:

- [ ] Multi-expert routing works (Planning + PVR-EC-O + Retrieval + Verification)
- [ ] Expert composition produces valid evidence chains
- [ ] Expert cascade depth limit enforced (tested via deliberate loop)
- [ ] Durable memory promotion gate correctly accepts/rejects candidates
- [ ] Promoted memories are versioned and immutable
- [ ] Memory revocation works (contradicting evidence revokes)
- [ ] Memory capacity cap enforced
- [ ] Research processes are bounded (budget, time, depth)
- [ ] Research auto-terminates on detected loops
- [ ] Research findings appear as evidence records
- [ ] Expert adapter training produces valid candidates offline
- [ ] New expert versions pass deployment gate before activation
- [ ] Canary rollout works for new expert versions
- [ ] Rollback works for each subsystem independently
- [ ] No forward purity violation in any expert
- [ ] All prior test suites pass (microkernel, PVR-EC-O, Phase 1, Phase 2)

---

## 9. Safety Architecture

### 9.1 Layered Safety

```
Layer 1: Forward Purity (per-expert)
  → No file writes, no CPU/GPU syncs, no map mutation

Layer 2: Execution Bounds (per-process)
  → Budget limits, depth limits, time limits

Layer 3: Evidence Gates (per-state-change)
  → Claims need evidence, commits need verification

Layer 4: Promotion Gates (per-capability-upgrade)
  → Memory promotion, policy activation, expert deployment

Layer 5: Research Bounds (per-research-process)
  → Justified, bounded, terminable, non-destructive

Layer 6: System Caps (global)
  → Memory cap, daily research cap, concurrent process cap
```

### 9.2 Invariants That Never Change

These are permanent architectural constraints:

1. **Canonical state is immutable** — only new states via transaction
2. **Claims require evidence** — unsupported claims cannot commit
3. **Experts are interchangeable** — no expert is irreplaceable
4. **Everything is replayable** — full audit trail always available
5. **Rollback is always possible** — no irreversible state change without approval
6. **Forward passes are pure** — no side effects in computation path

---

## 10. Success Metrics

| Metric | Target |
|--------|--------|
| Multi-expert task completion rate | >80% |
| Memory promotion precision | >95% (promoted items remain valid) |
| Research hypothesis validation rate | >30% (expected to fail often) |
| Expert composition overhead | <2x single-expert latency |
| System uptime with active policies | >99.5% |
| Rollback success rate | 100% |
| Evidence quality (support ratio) | >85% |
| Unknown failure rate | <1% |

---

## 11. Timeline and Milestones

```
Phase 3A (Weeks 1-4): Multi-Expert Framework
  → Expert registry, composition, cascade guard
  → Retrieval and Verification experts implemented
  → Integration tests with PVR-EC-O

Phase 3B (Weeks 5-8): Durable Memory
  → Promotion gate, versioned store, lifecycle management
  → Capacity guard, audit logging
  → Integration tests with evidence ledger

Phase 3C (Weeks 9-12): Research Processes
  → Research manager, bounds enforcement, terminator
  → Hypothesis generator, experiment designer
  → Integration tests with branch system

Phase 3D (Weeks 13-16): Expert Training Pipeline
  → Trace filtering, adapter training, candidate evaluation
  → Deployment gate integration, canary controller
  → End-to-end validation

Phase 3E (Weeks 17-20): System Integration
  → All subsystems active simultaneously
  → Load testing, failure injection, rollback verification
  → Final validation against all criteria
```

---

## 12. Dependencies

- Phase 1 integration stable in production
- Phase 2 policies active for 30+ days without rollback
- PVR-EC-O canary stable with no drift alerts
- Evidence ledger has 1000+ validated traces
- Shadow policy data sufficient for multi-expert routing
- Drift monitoring infrastructure operational
- Rollback mechanisms validated in production
