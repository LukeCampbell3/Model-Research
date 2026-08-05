# PVR Final Comparative Conclusion Suite

## Executive conclusion

PVR-EC-O has local reduced-file evidence that EAN geometry transfer plus strict Top1 sparse residual execution plus retention-gated delta replay can produce active-compute frontier wins at 700M under matched-token accounting. Expert deltas are inference-causally useful, especially for structured/syntax-heavy tokens.

Teacher independence is not yet proven. Pure uniformity geometry head failed to replace EAN at 300M matched volume. Descriptor-curriculum-as-EAN-scaffold remains unproven until tested against a verified teacher-EAN baseline.

## Claim ledger

| claim | status | status_detail | scope | evidence_found | caveat | source_report_path |
| --- | --- | --- | --- | --- | --- | --- |
| PVR_SELF_INSTILLED_EAN_GEOMETRY_HEAD_SUPPORTED | blocked | blocked_gate_failed | 300M matched-volume scaffold comparison | {"beats_no_head_warmup": false, "beats_plain_scratch": true, "candidate_not_probe_only": true, "geometry_health_pass": true, "routing_health_pass": true, "teacher_checkpoint_not_loaded_into_candidate": false, "token_budgets_matched": false, "top1_clean": true} | Pure support is local only and does not prove teacher independence. | benchmark/reports/generated/self_instilled_ean_geometry_head_300m_matched_volume_screen/self_instilled_ean_geometry_head_matched_volume_screen_report.json |
| PVR_SELF_INSTILLED_EAN_GEOMETRY_HEAD_NARROWS_TEACHER_GAP | blocked | blocked_invalid_teacher_reference | 300M teacher-scaffold comparison | teacher_valid=False; budget_complete=False; gap=None | No teacher-gap claim is emitted without a verified teacher-EAN reference. | benchmark/reports/generated/self_instilled_ean_geometry_head_300m_matched_volume_screen/self_instilled_ean_geometry_head_matched_volume_screen_report.json |
| PVR_SELF_INSTILLED_EAN_GEOMETRY_HEAD_CLOSES_TEACHER_GAP | blocked | blocked_invalid_teacher_reference | 300M teacher-scaffold comparison | teacher_valid=False; budget_complete=False; gap=None | No teacher-gap claim is emitted without a verified teacher-EAN reference. | benchmark/reports/generated/self_instilled_ean_geometry_head_300m_matched_volume_screen/self_instilled_ean_geometry_head_matched_volume_screen_report.json |
| PVR_DESCRIPTOR_CURRICULUM_NARROWS_EAN_GAP | blocked | blocked_invalid_teacher_reference | 300M teacher-scaffold comparison | teacher_valid=False; budget_complete=False; gap=None | No teacher-gap claim is emitted without a verified teacher-EAN reference. | benchmark/reports/generated/descriptor_ean_scaffold_screen/descriptor_ean_scaffold_screen_report.json |
| PVR_DESCRIPTOR_CURRICULUM_REPLACES_EAN_SCAFFOLD | blocked | blocked_invalid_teacher_reference | 300M teacher-scaffold comparison | teacher_valid=False; budget_complete=False; gap=None | No teacher-gap claim is emitted without a verified teacher-EAN reference. | benchmark/reports/generated/descriptor_ean_scaffold_screen/descriptor_ean_scaffold_screen_report.json |
| PVR_TEACHER_EAN_SCAFFOLD_STILL_REQUIRED | blocked | blocked_invalid_teacher_reference | 300M teacher-scaffold comparison | teacher_valid=False; budget_complete=False; narrows=False | Blocked if teacher-EAN reference is invalid, even if local losses suggest EAN is ahead. | benchmark/reports/generated/self_instilled_ean_geometry_head_300m_matched_volume_screen/self_instilled_ean_geometry_head_matched_volume_screen_report.json |
| PVR_700M_EAN_RETENTION_GATED_TOKEN_MATCHED_FRONTIER_SUPPORTED | supported | supported | 700M local reduced-file token-matched active-compute frontier | supported_seeds=['42', '123'] | Local reduced-file evidence only; not official external benchmark support. | benchmark/reports/generated/ean_retention_gated_token_matched_700m/ean_retention_gated_token_matched_700m_report.json |
| PVR_700M_EAN_RETENTION_GATED_TOKEN_MATCHED_FRONTIER_REPEAT_SUPPORTED | supported | supported | 700M local reduced-file token-matched active-compute frontier repeat | supported_seeds=['42', '123'] | Repeat support is still local and reduced-file. | benchmark/reports/generated/ean_retention_gated_token_matched_700m/ean_retention_gated_token_matched_700m_report.json; benchmark/reports/generated/ean_retention_gated_token_matched_700m_seed_123_strict/ean_retention_gated_token_matched_700m_repeat_report.json |
| PVR_700M_FULL_ACTIVE_COMPUTE_FRONTIER_NOT_SUPPORTED | supported | supported | 700M plain PVR active-compute frontier | Plain PVR rows lose in loaded local reports. | This negative claim does not apply to EAN retention-gated delta replay. | benchmark/reports/generated/ean_retention_gated_token_matched_700m/ean_retention_gated_token_matched_700m_report.json; benchmark/reports/generated/ean_retention_gated_token_matched_700m_seed_123_strict/ean_retention_gated_token_matched_700m_repeat_report.json |
| PVR_EXPERT_DELTA_CAUSALITY_SUPPORTED | supported | supported | Inference-time expert intervention audit | supported_seed_count=2 | Inference-time causal support only; not training-causal proof. | benchmark/reports/generated/expert_delta_causality_repeat_classwise_audit/expert_delta_causality_repeat_classwise_audit_report.json |
| PVR_EXPERT_DELTA_CAUSALITY_REPEAT_SUPPORTED | supported | supported | Inference-time expert intervention repeat audit | status=PVR_EXPERT_DELTA_CAUSALITY_REPEAT_SUPPORTED; supported_seed_count=2 | Inference-time causal support only; not training-causal proof. | benchmark/reports/generated/expert_delta_causality_repeat_classwise_audit/expert_delta_causality_repeat_classwise_audit_report.json |
| PVR_EC_DEPLOYMENT_CANDIDATE_CONFIRMED | supported | supported | Small production-shaped descriptor-controlled routing candidate | {"gates": {"calibration_reliability": true, "descriptor_control": true, "failure_observatory": true, "family_task_regression": true, "forward_purity": true, "multiseed_repeatability": true, "qpm_memory": true}, "top1_clean": true} | Does not prove 300M/700M LM frontier performance, teacher independence, or official benchmark support. | evaluation/benchmark_results/pvr_final_repaired_deployment_gate/pvr_ec_final_repaired_deployment_gate_report.json |
| PVR_EC_RELEASE_READY_FOR_CANARY | supported | supported | Small production-shaped descriptor-controlled routing candidate | final_release_verdict=PVR_EC_RELEASE_READY_FOR_CANARY; top1_clean=True | Canary readiness is scoped to the small production-shaped descriptor branch. | evaluation/benchmark_results/pvr_release_hardening/pvr_ec_final_release_readiness_report.json |
| PVR_ROUTE_MARGIN_PREDICTS_EXPERT_BENEFIT_SUPPORTED | blocked | blocked_missing_explicit_evidence | Official, training-causal, teacher-independence, or route-specialization claim | No explicit passing evidence in this final suite. | Blocked by default unless explicit evidence is present. |  |
| PVR_ROUTE_GEOMETRY_SPECIALIZATION_SUPPORTED | blocked | blocked_missing_explicit_evidence | Official, training-causal, teacher-independence, or route-specialization claim | No explicit passing evidence in this final suite. | Blocked by default unless explicit evidence is present. |  |
| PVR_REPLAY_ARCHITECTURE_SPECIFIC_ADVANTAGE_SUPPORTED | blocked | blocked_missing_explicit_evidence | Official, training-causal, teacher-independence, or route-specialization claim | No explicit passing evidence in this final suite. | Blocked by default unless explicit evidence is present. |  |
| PVR_BENEFIT_WEIGHTED_ROUTE_GEOMETRY_INDUCTION_SUPPORTED | blocked | blocked_missing_explicit_evidence | Official, training-causal, teacher-independence, or route-specialization claim | No explicit passing evidence in this final suite. | Blocked by default unless explicit evidence is present. |  |
| PVR_EXPERT_DELTA_TRAINING_CAUSALITY_SUPPORTED | blocked | blocked_missing_explicit_evidence | Official, training-causal, teacher-independence, or route-specialization claim | No explicit passing evidence in this final suite. | Blocked by default unless explicit evidence is present. |  |
| PVR_OFFICIAL_BROAD_NLP_SUPPORTED | blocked | blocked_missing_explicit_evidence | Official, training-causal, teacher-independence, or route-specialization claim | No explicit passing evidence in this final suite. | Blocked by default unless explicit evidence is present. |  |
| PVR_OFFICIAL_CODE_BENCH_SUPPORTED | blocked | blocked_missing_explicit_evidence | Official, training-causal, teacher-independence, or route-specialization claim | No explicit passing evidence in this final suite. | Blocked by default unless explicit evidence is present. |  |
| PVR_FROM_SCRATCH_DENSE_GAP_CLOSED | blocked | blocked_missing_explicit_evidence | Official, training-causal, teacher-independence, or route-specialization claim | No explicit passing evidence in this final suite. | Blocked by default unless explicit evidence is present. |  |
| PVR_TEACHER_INDEPENDENCE_SUPPORTED | blocked | blocked_missing_explicit_evidence | Official, training-causal, teacher-independence, or route-specialization claim | No explicit passing evidence in this final suite. | Blocked by default unless explicit evidence is present. |  |

## 300M scaffold comparison

| variant | lm_loss | training_tokens | eval_tokens | heldout_eval_tokens | top1_clean | probe_only | capability_evidence | source_branch |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pvr_full_scratch_300m_matched | 4.152685380711848 | 1126400 | 50176 | 12544 | True | False | True | 300m_scaffold |
| pvr_shared_warmup_no_geometry_head_300m_matched | 4.145141032277321 | 1126400 | 50176 | 12544 | True | False | True | 300m_scaffold |
| pvr_self_instilled_uniformity_geometry_head_v1_300m_matched | 4.146520776408059 | 1126400 | 50176 | 12544 | True | False | True | 300m_scaffold |
| pvr_descriptor_curriculum_head_300m_matched | 3.200647759437561 | 256000 | None | None | True | True | False | descriptor_curriculum_probe |
| pvr_descriptor_plus_uniformity_head_300m_matched | 3.167480492591858 | 256000 | None | None | True | True | False | descriptor_curriculum_probe |
| pvr_teacher_ean_300m_matched | 3.110029940702477 | 1126400 | 50176 | 12544 | True | False | True | 300m_scaffold |

Token budget validation:

```json
{
  "complete": false,
  "field_matches": {
    "effective_batch_tokens": false,
    "eval_windows": false,
    "heldout_eval_token_count": false,
    "optimizer_steps": false,
    "scorecard_eval_token_count": false,
    "training_tokens": false
  },
  "missing_variants": [],
  "per_variant": {
    "pvr_descriptor_curriculum_head_300m_matched": {
      "effective_batch_tokens": null,
      "eval_windows": null,
      "heldout_eval_token_count": null,
      "optimizer_steps": null,
      "scorecard_eval_token_count": null,
      "training_tokens": null,
      "variant": "pvr_descriptor_curriculum_head_300m_matched"
    },
    "pvr_descriptor_plus_uniformity_head_300m_matched": {
      "effective_batch_tokens": null,
      "eval_windows": null,
      "heldout_eval_token_count": null,
      "optimizer_steps": null,
      "scorecard_eval_token_count": null,
      "training_tokens": null,
      "variant": "pvr_descriptor_plus_uniformity_head_300m_matched"
    },
    "pvr_full_scratch_300m_matched": {
      "effective_batch_tokens": 1024,
      "eval_windows": 11,
      "heldout_eval_token_count": 12544,
      "optimizer_steps": 1100,
      "scorecard_eval_token_count": 50176,
      "training_tokens": 1126400,
      "variant": "pvr_full_scratch_300m_matched"
    },
    "pvr_self_instilled_uniformity_geometry_head_v1_300m_matched": {
      "effective_batch_tokens": 1024,
      "eval_windows": 11,
      "heldout_eval_token_count": 12544,
      "optimizer_steps": 1100,
      "scorecard_eval_token_count": 50176,
      "training_tokens": 1126400,
      "variant": "pvr_self_instilled_uniformity_geometry_head_v1_300m_matched"
    },
    "pvr_shared_warmup_no_geometry_head_300m_matched": {
      "effective_batch_tokens": 1024,
      "eval_windows": 11,
      "heldout_eval_token_count": 12544,
      "optimizer_steps": 1100,
      "scorecard_eval_token_count": 50176,
      "training_tokens": 1126400,
      "variant": "pvr_shared_warmup_no_geometry_head_300m_matched"
    },
    "pvr_teacher_ean_300m_matched": {
      "effective_batch_tokens": 1024,
      "eval_windows": 11,
      "heldout_eval_token_count": 12544,
      "optimizer_steps": 1100,
      "scorecard_eval_token_count": 50176,
      "training_tokens": 1126400,
      "variant": "pvr_teacher_ean_300m_matched"
    }
  },
  "present_variants": [
    "pvr_full_scratch_300m_matched",
    "pvr_shared_warmup_no_geometry_head_300m_matched",
    "pvr_self_instilled_uniformity_geometry_head_v1_300m_matched",
    "pvr_descriptor_curriculum_head_300m_matched",
    "pvr_descriptor_plus_uniformity_head_300m_matched",
    "pvr_teacher_ean_300m_matched"
  ],
  "summary": {
    "effective_batch_tokens": [
      1024
    ],
    "eval_windows": [
      11
    ],
    "heldout_eval_token_count": [
      12544
    ],
    "optimizer_steps": [
      1100
    ],
    "scorecard_eval_token_count": [
      50176
    ],
    "training_tokens": [
      1126400
    ]
  }
}
```

Teacher-EAN validity validation:

```json
{
  "checkpoint_path": "checkpoints\\self_instilled_ean_geometry_head_300m_matched_volume_screen\\pvr_teacher_ean_300m_matched\\checkpoint.pt",
  "conditions": {
    "copied_count_positive": false,
    "copied_keys_cover_embeddings_attention_norms": false,
    "copy_scope_embeddings_attention_norms": false,
    "skipped_count_positive": false,
    "teacher_checkpoint_loaded": false,
    "teacher_checkpoint_path_exists": false,
    "teacher_checkpoint_path_reported": true,
    "teacher_init_report_exists": false
  },
  "init_report": null,
  "source_report_path": "benchmark/reports/generated/self_instilled_ean_geometry_head_300m_matched_volume_screen/self_instilled_ean_geometry_head_matched_volume_screen_report.json",
  "valid": false
}
```

Teacher-EAN reference is invalid under final hard checks; gap and replacement claims are blocked.

## 700M active-compute frontier

### Seed 42

| model | lm_loss | active_params_per_token | active_flops_per_token | quality_per_active_flop | training_tokens | eval_tokens | heldout_eval_tokens | top1_clean |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| dense_700m | 3.982539808263584 | 700000000 | 4200000000 | 5.978477292334946e-11 | 1126400 | 50176 | 12544 | None |
| switch_top1_700m | 4.000389050464241 | 244999999 | 1469999994 | 1.700514882524272e-10 | 1126400 | 50176 | 12544 | None |
| generic_top2_700m | 4.2018086752113035 | 350000000 | 2100000000 | 1.1332988077248167e-10 | 1126400 | 50176 | 12544 | None |
| pvr_full_700m | 4.300505398487558 | 244999999 | 1469999994 | 1.581842245470504e-10 | 1126400 | 50176 | 12544 | True |
| pvr_ec_o_ean_token_matched_700m | 3.413549836801023 | 244999999 | 1469999994 | 1.9928582975008478e-10 | 1126400 | 50176 | 12544 | True |
| pvr_ec_o_ean_retention_gated_delta_replay_700m | 3.3226158959524974 | 244999999 | 1469999994 | 2.047399196665626e-10 | 1126400 | 50176 | 12544 | True |

### Seed 123

| model | lm_loss | active_params_per_token | active_flops_per_token | quality_per_active_flop | training_tokens | eval_tokens | heldout_eval_tokens | top1_clean |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| dense_700m | 3.997995138168335 | 700000000 | 4200000000 | 5.955365873814455e-11 | 1126400 | 50176 | 12544 | None |
| switch_top1_700m | 4.206539876607 | 244999999 | 1469999994 | 1.617177375170556e-10 | 1126400 | 50176 | 12544 | None |
| generic_top2_700m | 4.264239080098211 | 350000000 | 2100000000 | 1.1167067963260376e-10 | 1126400 | 50176 | 12544 | None |
| pvr_full_700m | 4.267386361044281 | 244999999 | 1469999994 | 1.5941188682378585e-10 | 1126400 | 50176 | 12544 | True |
| pvr_ec_o_ean_token_matched_700m | 3.39870955871076 | 244999999 | 1469999994 | 2.0015600034920528e-10 | 1126400 | 50176 | 12544 | True |
| pvr_ec_o_ean_retention_gated_delta_replay_700m | 3.2408152575395546 | 244999999 | 1469999994 | 2.099077107334482e-10 | 1126400 | 50176 | 12544 | True |

Repeat summary:

```json
{
  "123": {
    "pareto_favorable": true,
    "required_present": true,
    "retention_beats_all": true,
    "source_report_path": "benchmark/reports/generated/ean_retention_gated_token_matched_700m_seed_123_strict/ean_retention_gated_token_matched_700m_repeat_report.json",
    "status": "PVR_700M_EAN_RETENTION_GATED_TOKEN_MATCHED_FRONTIER_SUPPORTED",
    "supported": true,
    "token_matched": true,
    "top1_clean": true
  },
  "42": {
    "pareto_favorable": true,
    "required_present": true,
    "retention_beats_all": true,
    "source_report_path": "benchmark/reports/generated/ean_retention_gated_token_matched_700m/ean_retention_gated_token_matched_700m_report.json",
    "status": "PVR_700M_EAN_RETENTION_GATED_TOKEN_MATCHED_FRONTIER_SUPPORTED",
    "supported": true,
    "token_matched": true,
    "top1_clean": true
  }
}
```

## Expert causality

| seed | status | full_vs_shared_benefit | structured_full_vs_shared_benefit | wrong_expert_harm | structured_wrong_expert_harm |
| --- | --- | --- | --- | --- | --- |
| 42 | PVR_EXPERT_DELTA_CAUSALITY_REPEAT_SUPPORTED | 1.289743077333504 | 2.404115576166546 | 1.2417185518132754 | 2.017081891326066 |
| 123 | PVR_EXPERT_DELTA_CAUSALITY_REPEAT_SUPPORTED | 1.463166709370757 | 2.6533614143299236 | 1.3812738008129095 | 2.2558057758002534 |
| 777 | NOT_RUN_MISSING_ARTIFACT | None | None | None | None |

| class | full_vs_shared_benefit | wrong_expert_harm | wrong_expert_worse_than_full_rate | count |
| --- | --- | --- | --- | --- |
| quote | 8.413899992026534 | 7.518776996462952 | 1.0 | 408 |
| brace_bracket_paren | 4.5219207720861565 | 4.10585804295833 | 0.971311475409836 | 244 |
| operator | 4.295484436882866 | 3.490404653549194 | 0.9222222222222223 | 90 |
| json_key | 1.8356979805203628 | 1.454582904341034 | 0.8847926267281105 | 434 |
| newline | 3.9271796287884584 | 2.2953759926620205 | 1.0 | 274 |
| number | 3.6351761247070744 | 3.004364997568265 | 0.9295774647887324 | 142 |
| function_signature | 3.134624701997508 | 2.7203893604485883 | 0.9043478260869565 | 230 |
| identifier | 1.237139624901558 | 1.0885100576652376 | 0.7963470319634703 | 2190 |
| space | -0.5214926578678544 | -0.16763957282066633 | 0.3356681034482759 | 1856 |
| indentation | -0.34895642024103235 | 0.14274396066020098 | 0.693069306930693 | 1818 |

Inference-time causal support only; this is not training-causal proof.

## Descriptor deployment branch

```json
{
  "deployment_gates": {
    "calibration_reliability": true,
    "descriptor_control": true,
    "failure_observatory": true,
    "family_task_regression": true,
    "forward_purity": true,
    "multiseed_repeatability": true,
    "qpm_memory": true
  },
  "descriptor_ablation_drop": 0.6851623361427126,
  "descriptor_accuracy": 0.9509153621107655,
  "descriptor_control_margin": 0.1873809863181042,
  "descriptor_removed_accuracy": 0.26575302596805295,
  "heldout_family_accuracy": null,
  "peak_gpu_memory_mb": 1424.616448,
  "production_shape_pass_rate": 1.0,
  "total_tests_passed": 28
}
```

This branch proves small production-shaped descriptor-controlled routing readiness. It does not prove 300M/700M LM frontier performance, teacher independence, or official benchmark support.

## Blocked claims

| claim | status_detail | caveat | source_report_path |
| --- | --- | --- | --- |
| PVR_SELF_INSTILLED_EAN_GEOMETRY_HEAD_SUPPORTED | blocked_gate_failed | Pure support is local only and does not prove teacher independence. | benchmark/reports/generated/self_instilled_ean_geometry_head_300m_matched_volume_screen/self_instilled_ean_geometry_head_matched_volume_screen_report.json |
| PVR_SELF_INSTILLED_EAN_GEOMETRY_HEAD_NARROWS_TEACHER_GAP | blocked_invalid_teacher_reference | No teacher-gap claim is emitted without a verified teacher-EAN reference. | benchmark/reports/generated/self_instilled_ean_geometry_head_300m_matched_volume_screen/self_instilled_ean_geometry_head_matched_volume_screen_report.json |
| PVR_SELF_INSTILLED_EAN_GEOMETRY_HEAD_CLOSES_TEACHER_GAP | blocked_invalid_teacher_reference | No teacher-gap claim is emitted without a verified teacher-EAN reference. | benchmark/reports/generated/self_instilled_ean_geometry_head_300m_matched_volume_screen/self_instilled_ean_geometry_head_matched_volume_screen_report.json |
| PVR_DESCRIPTOR_CURRICULUM_NARROWS_EAN_GAP | blocked_invalid_teacher_reference | No teacher-gap claim is emitted without a verified teacher-EAN reference. | benchmark/reports/generated/descriptor_ean_scaffold_screen/descriptor_ean_scaffold_screen_report.json |
| PVR_DESCRIPTOR_CURRICULUM_REPLACES_EAN_SCAFFOLD | blocked_invalid_teacher_reference | No teacher-gap claim is emitted without a verified teacher-EAN reference. | benchmark/reports/generated/descriptor_ean_scaffold_screen/descriptor_ean_scaffold_screen_report.json |
| PVR_TEACHER_EAN_SCAFFOLD_STILL_REQUIRED | blocked_invalid_teacher_reference | Blocked if teacher-EAN reference is invalid, even if local losses suggest EAN is ahead. | benchmark/reports/generated/self_instilled_ean_geometry_head_300m_matched_volume_screen/self_instilled_ean_geometry_head_matched_volume_screen_report.json |
| PVR_ROUTE_MARGIN_PREDICTS_EXPERT_BENEFIT_SUPPORTED | blocked_missing_explicit_evidence | Blocked by default unless explicit evidence is present. |  |
| PVR_ROUTE_GEOMETRY_SPECIALIZATION_SUPPORTED | blocked_missing_explicit_evidence | Blocked by default unless explicit evidence is present. |  |
| PVR_REPLAY_ARCHITECTURE_SPECIFIC_ADVANTAGE_SUPPORTED | blocked_missing_explicit_evidence | Blocked by default unless explicit evidence is present. |  |
| PVR_BENEFIT_WEIGHTED_ROUTE_GEOMETRY_INDUCTION_SUPPORTED | blocked_missing_explicit_evidence | Blocked by default unless explicit evidence is present. |  |
| PVR_EXPERT_DELTA_TRAINING_CAUSALITY_SUPPORTED | blocked_missing_explicit_evidence | Blocked by default unless explicit evidence is present. |  |
| PVR_OFFICIAL_BROAD_NLP_SUPPORTED | blocked_missing_explicit_evidence | Blocked by default unless explicit evidence is present. |  |
| PVR_OFFICIAL_CODE_BENCH_SUPPORTED | blocked_missing_explicit_evidence | Blocked by default unless explicit evidence is present. |  |
| PVR_FROM_SCRATCH_DENSE_GAP_CLOSED | blocked_missing_explicit_evidence | Blocked by default unless explicit evidence is present. |  |
| PVR_TEACHER_INDEPENDENCE_SUPPORTED | blocked_missing_explicit_evidence | Blocked by default unless explicit evidence is present. |  |

## Final recommended next actions

- If teacher-EAN remains ahead: run descriptor-conditioned scaffold V2 against a verified teacher-EAN baseline.
- If official benchmarks are missing: perform the official adapter audit before any broad NLP/code claim.
- If 700M local frontier remains supported: freeze the local frontier claim and preserve the external benchmark caveat.