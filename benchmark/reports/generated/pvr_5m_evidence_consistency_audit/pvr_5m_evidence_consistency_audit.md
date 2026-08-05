# PVR 5M Evidence Consistency Audit

Status: `PVR_5M_EVIDENCE_CONSISTENCY_AUDIT_COMPLETE`
Decision: `PVR_5M_AUTHORITATIVE_VALUES_SET_A_STALE_SET_B_NOT_PRESENT_WEIGHT_ONLY_FINAL_CHECKPOINT`
Git commit: `bce74c6d7a7bd91cbe8b197f6bc5d37b6b22c457`

Audits current raw 5M artifacts and report lineage only; no model training or final official-file selection.

## Authoritative PVR 5M Result

Variant: `pvr_teacher_independent_sparse_v2_300m_long_curve`
Mean eval loss: `11.337301993370057`
Final eval loss: `10.112784385681152`
Final train loss: `1.962173342704773`
Optimizer steps: `4883`
Training tokens seen: `5000192`
Eval windows: `10`
Checkpoint path: `checkpoints\sparse_v2_300m_long_curve_validation\pvr_teacher_independent_sparse_v2_300m_long_curve\checkpoint.pt`
Checkpoint hash: `b45c4e0ac10002c6e94821348ccc1f6b05d6ed1ca039f0a0d185b29883fd7c50`

## Assertions

- report_row_present: `True`
- displayed_mean_eval_matches_raw: `True`
- displayed_final_eval_matches_raw: `True`
- displayed_final_train_matches_raw: `True`
- displayed_steps_match_raw: `True`
- displayed_tokens_match_raw: `True`
- displayed_checkpoint_hash_matches_manifest: `True`
- manifest_checkpoint_hash_matches_file: `True`
- set_a_matches_raw: `True`
- set_b_matches_raw: `False`
- checkpoint_contains_exact_resume_state: `False`

## Set Reconciliation

Set A matches current raw artifacts: `True`
Set B matches current raw artifacts: `False`

Set B is treated as stale/not authoritative unless another raw artifact is provided that contains those values.

## Checkpoint Resume Caveat

The final checkpoint is loadable and its hash matches the manifest, but it does not contain optimizer and RNG state. It is therefore a weight-only final checkpoint, not evidence that interrupted training could be resumed exactly.

## Evaluation Windows

| step | tokens seen | eval tokens | eval loss |
|---:|---:|---:|---:|
| 488 | 499712 | 64 | 21.773025512695312 |
| 976 | 999424 | 64 | 14.527545928955078 |
| 1464 | 1499136 | 64 | 9.39953899383545 |
| 1952 | 1998848 | 64 | 10.125415802001953 |
| 2440 | 2498560 | 64 | 10.773747444152832 |
| 2928 | 2998272 | 64 | 18.317325592041016 |
| 3416 | 3497984 | 64 | 3.302612066268921 |
| 3904 | 3997696 | 64 | 5.520256996154785 |
| 4392 | 4497408 | 64 | 9.520767211914062 |
| 4880 | 4997120 | 64 | 10.112784385681152 |
