# Phase 1: Integration Foundation — PVR-EC-O × Cognitive Microkernel Bridge

## Status: PLANNED
## Timeline: Post-Release Hardening
## Prerequisite: PVR_EC_RELEASE_READY_FOR_CANARY

---

## 1. Objective

Connect the validated PVR-EC-O deployment candidate (`pvr_ec_descriptor_curriculum_final_candidate_v1_1`) to the cognitive microkernel runtime as a first-class expert backend.

The cognitive microkernel defines experts as interchangeable. PVR-EC-O is the first expert that:
- Uses descriptor-conditioned routing (Top1, single-owner)
- Has validated task-family transfer via descriptor curriculum
- Has release-hardened artifacts with drift monitoring

Phase 1 does not change PVR-EC-O's architecture or the microkernel's process lifecycle. It builds the bridge: expert interface, evidence translation, claim extraction, and trace replay compatibility.

---

## 2. Deliverables

### 2.1 Expert Interface Adapter

```
cognitive_microkernel/src/cognitive_microkernel/experts/pvr_ec_expert.py
```

Implements the `Expert` interface from the microkernel with:
- `execute(ExpertInput) -> ExpertOutput` using PVR-EC-O forward pass
- Descriptor selection from `ExpertInput.task_state_slice`
- Claim extraction from model logits + confidence
- Evidence record generation from routing diagnostics
- Support tag derivation from descriptor-control margin

**Key constraint:** The expert adapter must NOT:
- Execute Top2/Top4 at runtime
- Mutate production maps
- Write files during forward
- Introduce CPU/GPU synchronization in the hot path

### 2.2 Evidence Translation Layer

```
cognitive_microkernel/src/cognitive_microkernel/evidence/pvr_ec_evidence.py
```

Translates PVR-EC-O diagnostics into microkernel evidence records:

| PVR-EC-O Diagnostic | Microkernel Evidence |
|---------------------|---------------------|
| `descriptor_control_margin` | Confidence evidence for claim support |
| `owner_entropy` | Routing stability evidence |
| `membership_entropy` | Prototype geometry evidence |
| `high_confidence_failure_rate` | Calibration reliability evidence |
| `unknown_failure_count` | Observatory gap evidence |

### 2.3 Descriptor-to-Process Mapping

Map microkernel process types to PVR-EC-O descriptor tokens:

| Process Type | Descriptor Token |
|-------------|-----------------|
| `observe_and_plan` | `<task:compositional_grammar>` |
| `verify_commit` | `<task:agreement_dependency>` |
| `resolve_contradiction` | `<task:negation_polarity>` |
| `disambiguate` | `<task:ambiguous_word_sense>` |
| `resolve_reference` | `<task:coreference_memory>` |
| `execute_instruction` | `<task:instruction_micro>` |
| `retrieve_structured` | `<task:multisentence_delimiter>` |
| `compare_equivalence` | `<task:paraphrase_invariance>` |

### 2.4 Trace Replay Compatibility

PVR-EC-O forward passes must be replayable from stored artifacts:
- Input tokens stored as artifact (content-addressed)
- Descriptor token stored in process metadata
- Output logits stored as artifact
- Routing decisions stored as evidence
- No model call needed for replay (artifact-based reconstruction)

### 2.5 Forward Purity Enforcement

The bridge must enforce forward purity at the interface level:

```python
class PVRECExpertPurityGuard:
    """Enforces deployment invariants at the expert interface boundary."""
    
    def pre_execute_check(self, expert_input: ExpertInput) -> bool:
        # No Top2/Top4 request
        # No production map access
        # No file I/O
        # No CPU/GPU sync
        pass
    
    def post_execute_check(self, expert_output: ExpertOutput) -> bool:
        # owners/token == 1.0
        # Top2 executions == 0
        # Top4 executions == 0
        # No map mutation
        pass
```

---

## 3. Architecture

```
┌──────────────────────────────────────────┐
│         Cognitive Microkernel            │
│                                          │
│  ProcessDescriptor → ExpertRouter        │
│       │                                  │
│       ▼                                  │
│  ┌─────────────────────────────────┐     │
│  │     PVR-EC Expert Adapter       │     │
│  │                                 │     │
│  │  1. Map process → descriptor    │     │
│  │  2. Tokenize input             │     │
│  │  3. Forward (Top1 only)        │     │
│  │  4. Extract claims from logits  │     │
│  │  5. Generate evidence records   │     │
│  │  6. Return ExpertOutput         │     │
│  └─────────────────────────────────┘     │
│       │                                  │
│       ▼                                  │
│  EvidenceLedger ← ClaimRegistry          │
│       │                                  │
│       ▼                                  │
│  Transaction → Commit/Rollback           │
└──────────────────────────────────────────┘
```

---

## 4. Validation Criteria

Phase 1 passes if:

- [ ] PVR-EC expert adapter implements full Expert interface
- [ ] Descriptor selection works for all 8 process types
- [ ] Evidence translation produces valid EvidenceRecord objects
- [ ] Claims extracted from logits have correct support status
- [ ] Forward purity guard catches all invariant violations
- [ ] Trace replay works without model calls (artifact-only)
- [ ] No regression in cognitive microkernel test suite
- [ ] No regression in PVR-EC deployment gate tests
- [ ] Integration test: full observe→branch→expert→claim→evidence→verify→commit loop

---

## 5. Non-Goals

Phase 1 does NOT:
- Activate learned policies (still shadow-only)
- Enable memory promotion
- Enable autonomous research
- Train new experts
- Change PVR-EC-O architecture
- Add runtime Top2/Top4
- Change microkernel process lifecycle

---

## 6. Risk Mitigations

| Risk | Mitigation |
|------|-----------|
| Forward purity violation at boundary | PurityGuard with pre/post checks |
| Descriptor mismatch for new process types | Explicit mapping table, fallback to `observe_and_plan` |
| Evidence flood from verbose diagnostics | Sampling + relevance filtering |
| Replay incompatibility | Content-addressed input/output storage |
| Latency from tokenization overhead | Pre-computed descriptor token cache |

---

## 7. Files to Create

```
cognitive_microkernel/src/cognitive_microkernel/experts/
├── __init__.py
├── pvr_ec_expert.py          # Expert adapter
├── pvr_ec_evidence.py        # Evidence translation
├── pvr_ec_purity_guard.py    # Forward purity enforcement
└── pvr_ec_descriptor_map.py  # Process-to-descriptor mapping

tests/
├── test_pvr_ec_expert_adapter.py
├── test_pvr_ec_evidence_translation.py
├── test_pvr_ec_integration_loop.py
└── test_pvr_ec_purity_guard.py
```

---

## 8. Dependencies

- Cognitive microkernel v1 (complete)
- PVR-EC-O release candidate `v1_1` (confirmed)
- Release artifacts package (hardened)
- Drift monitoring baselines (created)
