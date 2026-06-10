# Phase 2: Learned Policy Activation — Shadow-to-Active Promotion Pipeline

## Status: PLANNED
## Timeline: Post-Phase 1 Integration
## Prerequisite: Phase 1 validation complete, canary rollout stable

---

## 1. Objective

Activate the cognitive microkernel's learned policy pipeline from shadow-only to conditionally-active, using PVR-EC-O's validated routing diagnostics as the training signal.

Phase 1 proved that PVR-EC-O can serve as a reliable expert backend. Phase 2 uses the accumulated evidence from production traces to train policies that improve the microkernel's branch selection, context paging, and expert routing — without changing PVR-EC-O's forward path.

The key insight: PVR-EC-O's descriptor-control margin, routing entropy, and prototype geometry provide ground-truth signals about task difficulty and expert suitability. These signals can train the microkernel's branch value model and depth policy without requiring the expert itself to be retrained.

---

## 2. Scope

### What Activates

| Policy | V1 Status | Phase 2 Status |
|--------|-----------|---------------|
| Expert Router | Shadow-only | **Conditionally Active** |
| Branch Value Model | Shadow-only | **Conditionally Active** |
| Context Selector | Shadow-only | Shadow + Evaluation |
| Depth Policy | Shadow-only | **Conditionally Active** |
| Research Trigger | Shadow-only | Shadow + Evaluation |

### What Remains Blocked

| Feature | Status | Reason |
|---------|--------|--------|
| Memory Promotion | Blocked | Requires Phase 3 validation |
| Autonomous Research | Blocked | Requires safety review |
| Expert Adapter Updates | Blocked | Requires offline retraining pipeline |
| Irreversible Actions | Blocked | Requires explicit approval gate |

---

## 3. Training Signal Architecture

### 3.1 From PVR-EC-O Traces → Policy Training Data

Every PVR-EC-O expert execution produces:

```
routing_diagnostics:
  descriptor_control_margin: float  → task_confidence signal
  owner_entropy: float              → routing_certainty signal
  membership_entropy: float         → state_novelty signal
  membership_margin: float          → assignment_clarity signal
  high_confidence_failure_rate: float → calibration_quality signal
```

These map to policy training targets:

| PVR-EC-O Signal | Policy Target |
|-----------------|---------------|
| High descriptor margin → high branch value | Branch Value Model |
| Low owner entropy → prefer same expert | Expert Router |
| High membership entropy → allocate more depth | Depth Policy |
| Low membership margin → expand branch width | Branch Value Model |
| High failure rate → flag for review | Research Trigger |

### 3.2 Evidence-Backed Policy Updates

Policy updates are gated by evidence quality:

```python
class PolicyUpdateGate:
    min_traces: int = 100          # Minimum validated traces
    min_evidence_quality: float = 0.8  # Evidence support ratio
    max_hallucination_rate: float = 0.02  # Max unsupported claims
    requires_replay_verification: bool = True
    requires_shadow_agreement: float = 0.7  # Shadow must agree 70%
```

No policy activates until its shadow predictions agree with production heuristics on 70%+ of decisions AND the evidence ledger has 100+ validated traces.

### 3.3 Promotion Pipeline

```
┌─────────────────────────────────────────────────────┐
│  Phase 2 Promotion Pipeline                         │
│                                                     │
│  1. Accumulate PVR-EC-O traces (Phase 1 canary)    │
│  2. Shadow policies log predictions                 │
│  3. Compare shadow vs heuristic outcomes            │
│  4. Train policy on validated traces                │
│  5. Evaluate on held-out traces                     │
│  6. Gate: evidence quality + agreement threshold    │
│  7. Activate with rollback trigger                  │
│  8. Monitor for drift                              │
│                                                     │
│  Rollback: If activated policy regresses quality    │
│  by > 5%, auto-revert to heuristic                 │
└─────────────────────────────────────────────────────┘
```

---

## 4. Deliverables

### 4.1 Policy Training Infrastructure

```
cognitive_microkernel/src/cognitive_microkernel/policy_training/
├── __init__.py
├── trace_collector.py        # Collect validated traces from evidence ledger
├── feature_extractor.py      # Extract policy features from PVR-EC-O diagnostics
├── policy_trainer.py         # Train policies on collected traces
├── shadow_evaluator.py       # Evaluate shadow predictions vs outcomes
├── promotion_gate.py         # Evidence-gated promotion decisions
└── rollback_controller.py    # Auto-rollback on regression
```

### 4.2 Activated Policies

#### Expert Router Policy
- **Input:** Process type, state complexity (from membership entropy), budget remaining
- **Output:** Recommended expert (currently only PVR-EC-O, future: multiple experts)
- **Training signal:** Which descriptor produced lowest loss for each process type
- **Activation gate:** 100 traces, 70% shadow agreement, evidence quality > 0.8

#### Branch Value Policy
- **Input:** Branch hypothesis text features, parent state hash, evidence count
- **Output:** Predicted value (0-1), uncertainty estimate
- **Training signal:** Branches that led to successful commits vs rollbacks
- **Activation gate:** 200 traces, 65% shadow agreement, no catastrophic mispredictions

#### Depth Policy
- **Input:** Task difficulty (from membership entropy + margin), budget remaining
- **Output:** Recommended depth (1-5), recommended branch width (1-3)
- **Training signal:** PVR-EC-O's routing confidence inversely correlates with needed depth
- **Activation gate:** 100 traces, 70% shadow agreement

### 4.3 Monitoring Extensions

Extend drift monitoring from Phase 1:

| Monitor | Source | Threshold |
|---------|--------|-----------|
| Policy activation rate | Promotion gate | Warning if >3 activations/day |
| Policy agreement drift | Shadow vs active | Rollback if <60% agreement |
| Branch value calibration | Predicted vs actual | Warning if Brier >0.3 |
| Depth allocation efficiency | Budget usage | Warning if >80% wasted |
| Expert routing stability | Owner churn | Rollback if churn >20% |

---

## 5. Safety Constraints

### 5.1 Activation is Reversible
Every activated policy has a kill switch:
- Auto-rollback if quality regresses >5%
- Manual rollback via monitoring dashboard
- Shadow mode can be re-entered at any time

### 5.2 Evidence Requirements
No policy activates without evidence:
- Minimum trace count enforced
- Evidence quality threshold enforced
- Replay verification required
- Human approval required for first activation (relaxed after 3 successful promotions)

### 5.3 Scope Limits
Activated policies control:
- Which expert to route to (from available pool)
- How much depth/width to allocate
- Which branch seeds to prioritize

Activated policies do NOT control:
- Whether to commit or rollback (still evidence-gated)
- Whether to promote memory (still blocked)
- Whether to initiate research (still blocked)
- Expert internal behavior (PVR-EC-O is frozen)

---

## 6. Validation Criteria

Phase 2 passes if:

- [ ] At least one policy promotes from shadow to active
- [ ] Promoted policy improves branch selection efficiency (measured by commit rate)
- [ ] No quality regression in PVR-EC-O expert performance
- [ ] No forward purity violation
- [ ] Rollback mechanism works (tested via deliberate regression injection)
- [ ] Evidence quality gate correctly blocks premature promotion
- [ ] Shadow logging captures all decision points
- [ ] Drift monitoring detects policy agreement degradation
- [ ] 100+ validated traces collected from Phase 1 canary
- [ ] All cognitive microkernel tests pass
- [ ] All PVR-EC-O deployment gate tests pass

---

## 7. Architecture Evolution

```
Phase 1:                          Phase 2:
┌───────────────────┐            ┌───────────────────┐
│ Microkernel       │            │ Microkernel       │
│   Heuristic-only  │            │   Heuristic +     │
│   Shadow logging  │            │   Active Policies │
│   PVR-EC expert   │     →      │   Policy Training │
│   Evidence ledger │            │   Promotion Gates │
│   Trace replay    │            │   Rollback Ctrl   │
└───────────────────┘            │   PVR-EC expert   │
                                 │   Evidence ledger │
                                 │   Trace replay    │
                                 └───────────────────┘
```

---

## 8. Files to Create

```
cognitive_microkernel/src/cognitive_microkernel/policy_training/
├── __init__.py
├── trace_collector.py
├── feature_extractor.py
├── policy_trainer.py
├── shadow_evaluator.py
├── promotion_gate.py
└── rollback_controller.py

cognitive_microkernel/src/cognitive_microkernel/policies/
├── __init__.py
├── expert_router_policy.py
├── branch_value_policy.py
├── depth_policy.py
└── policy_registry.py

tests/
├── test_policy_training_pipeline.py
├── test_promotion_gate.py
├── test_policy_rollback.py
├── test_shadow_to_active_transition.py
└── test_policy_drift_monitoring.py
```

---

## 9. Dependencies

- Phase 1 integration complete
- PVR-EC-O canary stable (no rollback triggered)
- Minimum 100 validated traces in evidence ledger
- Drift monitoring baselines active
- Shadow policy runner collecting predictions
