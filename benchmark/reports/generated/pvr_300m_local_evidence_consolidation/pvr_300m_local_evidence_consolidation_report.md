# PVR-EC-O 300M Local Evidence Consolidation

Status: `PVR_EC_O_300M_LOCAL_EVIDENCE_CONSOLIDATION_REPORT_COMPLETE`
Candidate: `pvr_ec_o_ean_retention_gated_delta_replay_v1`

At 300M local reduced-file scale, pvr_ec_o_ean_retention_gated_delta_replay_v1 achieves repeat-supported active-compute Pareto advantage under strict Top1 execution. Its selected expert path is inference-causally useful across two available replay-seed artifacts, with strongest effects on structured/syntax-heavy token classes.

## Supported

### PVR_ACTIVE_COMPUTE_PARETO_ADVANTAGE_REPEAT_SUPPORTED

Status: `SUPPORTED`

Evidence:
- Seed 42 and seed 123 candidate artifacts both pass active-compute Pareto gates.
- Candidate remains at 105M active params/token and 630M active FLOPs/token.

Caveat: Seed 777 is NOT_RUN_MISSING_ARTIFACT; local reduced-file audit only.

### PVR_STRICT_TOP1_ACTIVE_COMPUTE_SUFFICIENCY_SUPPORTED

Status: `SUPPORTED`

Evidence:
- Strict Top1 beats dense, Switch Top1, and generic Top2 on local broad LM.
- Runtime Top2/Top4 PVR escalation worsens loss and quality/FLOP.

Caveat: Runtime Top2/Top4 are eval-only controls, not trained candidates.

### PVR_EXPERT_BENEFIT_LOCALIZATION_SUPPORTED

Status: `SUPPORTED`

Evidence:
- Expert benefit is positive overall and concentrated in structured/syntax-heavy classes.
- Structured benefit share exceeds structured token fraction.

Caveat: Byte-level heuristic token classes; local reduced files.

### PVR_EXPERT_FUNCTION_PROBE_SUPPORTED

Status: `SUPPORTED`

Evidence:
- All global experts are active and positive in post-hoc assigned benefit.
- Expert cards expose top benefit/harm classes and examples.

Caveat: Post-hoc attribution, not causal proof by itself.

### PVR_EXPERT_DELTA_CAUSALITY_REPEAT_SUPPORTED

Status: `SUPPORTED`

Evidence:
- Full model beats shared-only on both available replay seeds.
- Wrong-expert intervention harms loss on both available replay seeds.
- Structured classes show strongest repeated harm.

Caveat: Inference-time causal support over seeds 42 and 123; seed 777 missing; not training-causal proof.

## Partially Supported

### PVR_ROUTE_GEOMETRY_PARTIAL_SIGNAL

Status: `PARTIAL`

Evidence:
- Owner/token-class and owner/syntax NMI show lift over shuffled controls.
- Signal is below strict semantic-geometry thresholds.

Caveat: Do not claim semantic owner geometry specialization.

## Blocked

### PVR_ROUTE_MARGIN_PREDICTS_EXPERT_BENEFIT_SUPPORTED

Status: `BLOCKED`

Evidence:
- Margin/benefit correlation is negative near zero.
- High-margin tokens do not beat low-margin tokens.
- Margin quartiles are not monotonic.

Caveat: Route margin should not be described as calibrated confidence.

### PVR_ROUTE_GEOMETRY_SPECIALIZATION_SUPPORTED

Status: `BLOCKED`

Evidence:
- Family-level geometry audit fails.
- Fine-grained route geometry audit fails strict gate.
- Semantic owner geometry proof misses strict NMI/loss-bucket thresholds.

Caveat: Owner IDs are not yet strongly human-interpretable.

### PVR_REPLAY_ARCHITECTURE_SPECIFIC_ADVANTAGE_SUPPORTED

Status: `BLOCKED`

Evidence:
- Cross-architecture replay control does not show PVR-specific replay advantage.

Caveat: Replay appears broadly useful, not uniquely PVR-specific under this control.

### PVR_BENEFIT_WEIGHTED_ROUTE_GEOMETRY_INDUCTION_SUPPORTED

Status: `BLOCKED`

Evidence:
- Benefit-weighted route induction worsens intended NMI/consistency metrics.

Caveat: Do not push this route-forcing repair path as supported.

### PVR_EXPERT_DELTA_TRAINING_CAUSALITY_SUPPORTED

Status: `BLOCKED`

Evidence:
- No training-causal intervention has been run.

Caveat: Current causality support is inference-time only.

## Not Tested

### PVR_OFFICIAL_BROAD_NLP_SUPPORTED

Status: `NOT_TESTED`

Evidence:
- Official broad NLP adapters remain NOT_RUN_NOT_IMPLEMENTED.

Caveat: Local reduced-file evidence only.

### PVR_OFFICIAL_CODE_BENCH_SUPPORTED

Status: `NOT_TESTED`

Evidence:
- Official code benchmark adapters remain NOT_RUN_NOT_IMPLEMENTED.

Caveat: Local reduced-file evidence only.

### PVR_FROM_SCRATCH_DENSE_GAP_CLOSED

Status: `NOT_TESTED`

Evidence:
- Current best candidate uses EAN teacher-initialized scaffold.

Caveat: Do not claim from-scratch dense dominance.

### PVR_TEACHER_INDEPENDENCE_SUPPORTED

Status: `NOT_TESTED`

Evidence:
- Current best candidate depends on dense-compatible EAN initialization.

Caveat: Teacher independence remains an open research target.

## Source Statuses

```json
{
  "active_compute_frontier": "PVR_ACTIVE_COMPUTE_PARETO_ADVANTAGE_SUPPORTED",
  "active_compute_frontier_repeat": "PVR_ACTIVE_COMPUTE_PARETO_ADVANTAGE_REPEAT_SUPPORTED",
  "benefit_weighted_route_induction": "PVR_BENEFIT_WEIGHTED_ROUTE_GEOMETRY_INDUCTION_NOT_SUPPORTED",
  "causal_ablation": "PVR_EAN_RETENTION_REPLAY_CAUSAL_ABLATION_NOT_SUPPORTED",
  "claim_proof_battery": "PVR_CLAIM_PROOF_BATTERY_PARTIAL_SUPPORTED",
  "expert_benefit_localization": "PVR_EXPERT_BENEFIT_LOCALIZATION_SUPPORTED",
  "expert_cards": "PVR_EXPERT_CARD_REPORT_GENERATION_COMPLETE",
  "expert_delta_causality_repeat": "PVR_EXPERT_DELTA_CAUSALITY_REPEAT_SUPPORTED",
  "expert_function_probe": "PVR_EXPERT_FUNCTION_PROBE_SUPPORTED",
  "replay_cross_architecture": "PVR_REPLAY_ARCHITECTURE_SPECIFIC_ADVANTAGE_NOT_SUPPORTED",
  "route_geometry_finegrain": "PVR_ROUTE_GEOMETRY_FINEGRAIN_NOT_SUPPORTED",
  "route_geometry_specialization": "PVR_ROUTE_GEOMETRY_SPECIALIZATION_NOT_SUPPORTED",
  "strict_top1_vs_top2": "PVR_STRICT_TOP1_ACTIVE_COMPUTE_SUFFICIENCY_SUPPORTED"
}
```
