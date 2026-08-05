# PVR Resume Validity Audit

Status: `PVR_WEIGHT_ONLY_RESUME_NON_EQUIVALENT_CONFIRMED`
Comparison status: `PVR_5M_COMPARISON_HAS_WEIGHT_ONLY_CHECKPOINT_CAVEAT`
Git commit: `bce74c6d7a7bd91cbe8b197f6bc5d37b6b22c457`

Legacy final checkpoints are loadable for evaluation but do not contain enough optimizer/RNG state to prove exact interrupted continuation.

| variant | run status | steps | tokens | resume validity | checkpoint kind | has optimizer | has RNG |
|---|---|---:|---:|---|---|---|---|
| generic_top2_sparse_v2_300m_matched_long_curve | GENUINE_REDUCED_TRAINING_COMPLETE | 4883 | 5000192 | RESUME_STATE_UNKNOWN_OR_MISSING | None | None | False |
| switch_top1_sparse_v2_300m_matched_long_curve | GENUINE_REDUCED_TRAINING_COMPLETE | 4883 | 5000192 | RESUME_STATE_UNKNOWN_OR_MISSING | None | None | False |
| dense_sparse_v2_300m_matched_long_curve | GENUINE_REDUCED_TRAINING_COMPLETE | 4883 | 5000192 | RESUME_STATE_UNKNOWN_OR_MISSING | None | None | False |
| pvr_teacher_independent_sparse_v2_300m_long_curve | GENUINE_REDUCED_TRAINING_COMPLETE | 4883 | 5000192 | WEIGHT_ONLY_CHECKPOINT_NON_EQUIVALENT_FOR_EXACT_RESUME | WEIGHT_ONLY_LEGACY | False | False |
| pvr_teacher_independent_sparse_v2_300m_aux0005_long_curve | TRAINING_FAILED | 414 | 423936 | TRAINING_FAILED_NON_COMPARABLE | None | None | False |

## Required Interpretation

- Weight-only checkpoints may be evaluated as final weights.
- Weight-only checkpoints must not be reported as exact Adam-style continuation evidence.
- Any future interrupted run must restore optimizer, scheduler/scaler where applicable, RNG state, step, tokens, config hash, and source commit.
