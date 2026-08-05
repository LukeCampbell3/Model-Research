# Sparse-v2 300M 5M Long-Curve Validation

Status: `PVR_300M_5M_LONG_CURVE_VALIDATION_COMPLETE_WITH_AUX_FAILURE`
Decision: `PVR_TEACHER_INDEPENDENT_300M_5M_OFFICIAL_LIKE_ADVANTAGE_NOT_SUPPORTED`

5,000,192 training tokens/model for completed rows; train on broad_nlp_train, eval on official_like_dev. Final official bounded files not used.

## Completed Rows

| rank | variant | mean eval | final eval | final train | steps | tokens |
|---:|---|---:|---:|---:|---:|---:|
| 1 | generic_top2_sparse_v2_300m_matched_long_curve | 10.32124400138855 | 11.496098518371582 | 2.2771010398864746 | 4883 | 5000192 |
| 2 | switch_top1_sparse_v2_300m_matched_long_curve | 10.355957651138306 | 11.131117820739746 | 2.249508857727051 | 4883 | 5000192 |
| 3 | dense_sparse_v2_300m_matched_long_curve | 10.597127103805542 | 9.947757720947266 | 1.933674931526184 | 4883 | 5000192 |
| 4 | pvr_teacher_independent_sparse_v2_300m_long_curve | 11.337301993370057 | 10.112784385681152 | 1.962173342704773 | 4883 | 5000192 |

## Failed/Invalid Rows

| variant | status | steps | tokens | eval windows | reason |
|---|---|---:|---:|---:|---|
| pvr_teacher_independent_sparse_v2_300m_aux0005_long_curve | TRAINING_FAILED | 414 | 423936 | 0 | invalid/no eval windows |

## Interpretation

Current teacher-independent PVR reaches dense-like train loss but has worse official-like dev mean eval than dense, Switch, and generic Top2 at the 5M-token rung.
