# PVR Teacher-Independent Repair Attribution Report

Status: `PVR_TEACHER_INDEPENDENT_REPAIR_ATTRIBUTION_REPORT_COMPLETE`
Decision: `COMBINED_ROUTER_AND_SUBSTRATE_LIMITATION_DIAGNOSTIC_SUPPORTED`
Git commit: `bce74c6d7a7bd91cbe8b197f6bc5d37b6b22c457`

## Authoritative 5M Evidence

Evidence audit status: `PVR_5M_EVIDENCE_CONSISTENCY_AUDIT_COMPLETE`
Evidence decision: `PVR_5M_AUTHORITATIVE_VALUES_SET_A_STALE_SET_B_NOT_PRESENT_WEIGHT_ONLY_FINAL_CHECKPOINT`
PVR mean eval loss: `11.337301993370057`
PVR final eval loss: `10.112784385681152`
PVR final train loss: `1.962173342704773`
Optimizer steps: `4883`
Training tokens seen: `5000192`

Set A is authoritative in current artifacts. Set B is not present in the current filesystem artifacts.

## Resume Validity

Resume audit status: `PVR_WEIGHT_ONLY_RESUME_NON_EQUIVALENT_CONFIRMED`
Comparison status: `PVR_5M_COMPARISON_HAS_WEIGHT_ONLY_CHECKPOINT_CAVEAT`

Legacy 5M checkpoints are loadable for evaluation but do not prove exact optimizer/RNG continuation.

## Router Regret

Router audit status: `PVR_ROUTER_REGRET_BOTTLENECK_DIAGNOSTIC_SUPPORTED`
Final-block mean regret: `1.469227062610173`
Final-block selected-is-oracle rate: `0.17779541015625`
Official-like greedy oracle improvement: `-4.248973710196359`

Router regret is material in diagnostics. This supports router repair before scale, not architecture promotion.

## Comparator Integrity

Comparator audit status: `SPARSE_COMPARATOR_RUNTIME_INTEGRITY_AUDIT_COMPLETE`
All sparse comparators valid: `True`

## Repair Screens

Shared substrate screen: `PVR_SHARED_SUBSTRATE_REPAIR_SCREEN_COMPLETE`
Router repair screen: `PVR_ROUTER_REGRET_REPAIR_SCREEN_COMPLETE`
Router repair 1M confirmation: `PVR_ROUTER_REGRET_REPAIR_SCREEN_COMPLETE`
Router repair 1M confirmation decision: `PVR_ROUTER_REGRET_REPAIR_NOT_SUPPORTED`
Router repair 1M refinement: `PVR_ROUTER_REGRET_REPAIR_1M_REFINEMENT_INCOMPLETE_OR_INVALID`
Router regret / LM mismatch analysis: `PVR_ROUTER_REGRET_LM_MISMATCH_ANALYSIS_COMPLETE`
Router testing gap resolution: `PVR_ROUTER_REGRET_TESTING_GAP_RESOLUTION_COMPLETE`
Curriculum attribution: `PVR_TRAINING_CURRICULUM_ATTRIBUTION_COMPLETE_NOT_SUPPORTED`

Substrate decision: `PVR_SHARED_SUBSTRATE_REPAIR_CANDIDATE_IDENTIFIED`
Substrate winner: `pvr_shared_substrate_full_transformer_random_ean_300m`
Substrate winner delta vs current: `-0.7552423477172852`

The substrate matrix and bounded regret-weighted router repair screen are complete. The aux=0.0005 5M run remains invalid because it failed before producing eval windows.

Regret0p01 improved final-block router metrics but failed the 1M LM eval gate. Final eval delta was `0.04692554473876953`, while oracle selected-loss delta was `-0.971287727355957` and router-regret delta was `-0.20840166567670942`.

Follow-up alignment audits resolved the gap: raw JSON first-block evaluation was metadata-prefix biased, raw JSON two-block evaluation failed, text-only evaluation was mixed, and full-network greedy oracle comparison did not show full-network regret reduction versus baseline.

## Supported Claims

- `OFFICIAL_EVALUATION_BOUNDARY_FROZEN`
- `PVR_5M_EVIDENCE_CONSISTENCY_AUDIT_COMPLETE`
- `PVR_WEIGHT_ONLY_RESUME_NON_EQUIVALENT_CONFIRMED`
- `PVR_ROUTER_REGRET_BOTTLENECK_DIAGNOSTIC_SUPPORTED`
- `SPARSE_COMPARATOR_RUNTIME_INTEGRITY_AUDIT_COMPLETE`
- `PVR_OFFICIAL_DECOMPOSITION_SELECTED_EXPERT_HELP_SUPPORTED`
- `PVR_SHARED_SUBSTRATE_REPAIR_SCREEN_COMPLETE`
- `PVR_SHARED_SUBSTRATE_REPAIR_CANDIDATE_IDENTIFIED`
- `PVR_ROUTER_REGRET_REPAIR_SCREEN_COMPLETE`
- `PVR_ROUTER_REGRET_REPAIR_SUPPORTED`
- `PVR_ROUTER_REGRET_REPAIR_1M_CONFIRMATION_COMPLETE`
- `PVR_ROUTER_REGRET_LM_MISMATCH_ANALYSIS_COMPLETE`
- `PVR_ROUTER_REGRET_METRIC_IMPROVEMENT_SUPPORTED`
- `PVR_ROUTER_REGRET_REPAIR_1M_LM_GATE_NOT_SUPPORTED`
- `PVR_ROUTER_REPAIR_EVAL_ORACLE_ALIGNMENT_MISMATCH_CONFIRMED`
- `PVR_ROUTER_REGRET_OBJECTIVE_OVER_CONCENTRATION_RISK_SUPPORTED`
- `PVR_ROUTER_REGRET_TESTING_GAPS_RESOLVED`
- `PVR_ROUTER_REGRET_REPAIR_FINAL_BLOCK_METRIC_IMPROVEMENT_SUPPORTED`
- `PVR_ROUTER_REGRET_REPAIR_RAW_JSON_PREFIX_SUPPORTED_ONLY`
- `PVR_ROUTER_REGRET_REPAIR_RAW_JSON_TWO_BLOCK_NOT_SUPPORTED`
- `PVR_ROUTER_REGRET_REPAIR_TEXT_CONTENT_BROAD_SUPPORT_NOT_ESTABLISHED`
- `PVR_ROUTER_REGRET_REPAIR_FULL_NETWORK_REGRET_REDUCTION_NOT_SUPPORTED`
- `PVR_ROUTER_REGRET_REPAIR_REGRET0P01_DO_NOT_PROMOTE`

## Rejected / Not Supported

- `PVR_TEACHER_INDEPENDENT_300M_5M_OFFICIAL_LIKE_ADVANTAGE_NOT_SUPPORTED`
- `PVR_SPARSE_V2_CURRICULUM_SCREEN_NOT_SUPPORTED`
- `PVR_5M_AUX0005_SCIENTIFIC_FAILURE_NOT_SUPPORTED_BECAUSE_RUN_FAILED`
- `PVR_ROUTER_REGRET_REPAIR_1M_CONFIRMATION_NOT_SUPPORTED`
- `PVR_ROUTER_REGRET_REPAIR_REGRET0P01_NOT_SUPPORTED_FOR_PROMOTION`

## Blocked / Unresolved

- `PVR_ROUTER_REGRET_REPAIR_1M_REFINEMENT_INCOMPLETE_OR_INVALID`
- `PVR_FULL_NETWORK_ORACLE_ON_FINAL_OFFICIAL_NOT_RUN`
- `PVR_MATCHED_INFORMATION_ROUTING_ATTRIBUTION_MATRIX_NOT_RUN`
- `PVR_TEACHER_INDEPENDENCE_SUPPORTED_BLOCKED`
- `PVR_ARCHITECTURE_SUPERIORITY_SUPPORTED_BLOCKED`

## Recommendation

Do not promote regret0p01. It reduced final-block router regret at 1M, but did not improve official-like LM eval. Lower-weight refinement remains incomplete because the Docker run timed out after an earlier disk-full failure; rerun only after disk/runtime headroom is available.
