# Shared-Trunk Init 300M Repeat Decision

Status: `PVR_SHARED_TRUNK_INIT_300M_REPEAT_SCORECARD_SUPPORTED_EVAL_CURVE_MIXED`

```json
{
  "created_at": "2026-06-16T23:16:41.039296+00:00",
  "git_commit": "243422e88483ef7ff3ae133eb8cbd77a7b2f2fce",
  "interpretation": "Repeat seed supports the reduced LM scorecard dense-gap claim, but does not support the training eval-curve gate because mean eval loss regressed while final train loss and reduced LM loss improved.",
  "reduced_lm_scorecard_decision": {
    "baseline_pvr_lm_loss": 3.422222343683243,
    "dense_reference_lm_loss": 3.305846790075302,
    "init_minus_baseline_lm_loss": -0.40945056557655324,
    "init_minus_dense_lm_loss": -0.2930750119686123,
    "paths": {
      "baseline": "benchmark/reports/generated/shared_trunk_init_300m_repeat_seed_42/lm_eval/pvr_ec_o_full_300m_baseline_seed_42_nlp_scorecard.json",
      "shared_trunk_init": "benchmark/reports/generated/shared_trunk_init_300m_repeat_seed_42/lm_eval/pvr_ec_o_full_300m_shared_trunk_init_from_dense_seed_42_nlp_scorecard.json"
    },
    "scorecard_dense_gap_closed": true,
    "shared_trunk_init_pvr_lm_loss": 3.0127717781066896
  },
  "route_stability": {
    "mean_owner_entropy_delta_vs_baseline": 0.025607521279422674,
    "mean_prototype_monopoly_rate_delta_vs_baseline": -0.022330729166666674,
    "mean_route_margin_delta_vs_baseline": 0.03602253538059208,
    "route_stable": true,
    "top1_invariants_clean": true
  },
  "schema_version": "1.0",
  "seed": 42,
  "source_seed_report": "benchmark/reports/generated/shared_trunk_init_300m_repeat_seed_42/shared_trunk_init_seed_report.json",
  "status": "PVR_SHARED_TRUNK_INIT_300M_REPEAT_SCORECARD_SUPPORTED_EVAL_CURVE_MIXED",
  "training_eval_curve_decision": {
    "baseline_pvr_final_train_loss": 2.8410847187042236,
    "baseline_pvr_mean_eval_loss": 4.856676840782166,
    "init_minus_baseline_final_train_loss": -0.24588608741760254,
    "init_minus_baseline_mean_eval_loss": 0.13120231628417933,
    "shared_trunk_init_final_train_loss": 2.595198631286621,
    "shared_trunk_init_mean_eval_loss": 4.987879157066345,
    "status": "PVR_SHARED_TRUNK_INIT_300M_NOT_SUPPORTED"
  }
}
```
