# PVR-EC Final Candidate v1_1 Revalidation Report

**Status:** PVR_EC_REPEATABILITY_BLOCKED

**Statuses:** PVR_EC_DO_NOT_PROMOTE, PVR_EC_FINAL_CANDIDATE_REVALIDATION_REQUIRED, PVR_EC_REPEATABILITY_BLOCKED

```json
{
  "metadata": {
    "seed_list": [
      42,
      123,
      777,
      2026,
      9001
    ],
    "train_steps": 500,
    "candidate_model": "pvr_ec_ownership_top1_final_candidate_v1_1",
    "command": "evaluation/run_algorithmic_benchmarks.py --mode benchmark-lite --scale small --sample-limit 1000 --train-steps 500 --seed-list 42,123,777,2026,9001 --device cuda --amp --models fixed_moe_vectorized,pvr_ec_deploy_top1,pvr_ec_ownership_top1_final_candidate_v1_1 --enable-ownership-map --ownership-map-mode frozen --run-final-candidate-revalidation --output-dir evaluation/benchmark_results/pvr_final_candidate_v1_1_revalidation"
  },
  "status": "PVR_EC_REPEATABILITY_BLOCKED",
  "statuses": [
    "PVR_EC_DO_NOT_PROMOTE",
    "PVR_EC_FINAL_CANDIDATE_REVALIDATION_REQUIRED",
    "PVR_EC_REPEATABILITY_BLOCKED"
  ],
  "promotion_ready": false,
  "passed": false,
  "mean": {
    "fixed_moe_loss": 0.4109203183092177,
    "fixed_moe_accuracy": 0.1944056239153609,
    "candidate_loss": 0.41364575192953146,
    "candidate_accuracy": 0.2786876229496643,
    "loss_gap_vs_fixed": 0.002725433620313744,
    "accuracy_gap_vs_fixed": 0.08428199903430342
  },
  "candidate_loss_stats": {
    "mean": 0.41364575192953146,
    "std": 0.016520275456910868,
    "min": 0.396124194880637,
    "max": 0.43784711696207523,
    "ci95_low": 0.3991650920294912,
    "ci95_high": 0.42812641182957173
  },
  "candidate_accuracy_stats": {
    "mean": 0.2786876229496643,
    "std": 0.043980948285496396,
    "min": 0.23395668899979996,
    "max": 0.335971191900745,
    "ci95_low": 0.2401366220378054,
    "ci95_high": 0.31723862386152324
  },
  "per_seed_pass_fail": [
    {
      "seed": 42,
      "fixed_moe_loss": 0.3886076922838887,
      "fixed_moe_accuracy": 0.25857819999606313,
      "candidate_loss": 0.41567398770712316,
      "candidate_accuracy": 0.24662427509545803,
      "loss_gap_vs_fixed": 0.027066295423234465,
      "accuracy_gap_vs_fixed": -0.011953924900605095,
      "loss_pass": false,
      "accuracy_pass": true,
      "family_level_pass": true,
      "catastrophic_family_collapse_count": 0
    },
    {
      "seed": 123,
      "fixed_moe_loss": 0.4128779768167684,
      "fixed_moe_accuracy": 0.2465923217227525,
      "candidate_loss": 0.41815000923816115,
      "candidate_accuracy": 0.23395668899979996,
      "loss_gap_vs_fixed": 0.005272032421392736,
      "accuracy_gap_vs_fixed": -0.012635632722952539,
      "loss_pass": true,
      "accuracy_pass": true,
      "family_level_pass": false,
      "catastrophic_family_collapse_count": 1
    },
    {
      "seed": 777,
      "fixed_moe_loss": 0.41424106022653484,
      "fixed_moe_accuracy": 0.15306213128950222,
      "candidate_loss": 0.43784711696207523,
      "candidate_accuracy": 0.2635769454047967,
      "loss_gap_vs_fixed": 0.023606056735540393,
      "accuracy_gap_vs_fixed": 0.11051481411529449,
      "loss_pass": false,
      "accuracy_pass": true,
      "family_level_pass": false,
      "catastrophic_family_collapse_count": 1
    },
    {
      "seed": 2026,
      "fixed_moe_loss": 0.40513353542579955,
      "fixed_moe_accuracy": 0.2179172791466334,
      "candidate_loss": 0.396124194880637,
      "candidate_accuracy": 0.31330901334752226,
      "loss_gap_vs_fixed": -0.009009340545162559,
      "accuracy_gap_vs_fixed": 0.09539173420088887,
      "loss_pass": true,
      "accuracy_pass": true,
      "family_level_pass": true,
      "catastrophic_family_collapse_count": 0
    },
    {
      "seed": 9001,
      "fixed_moe_loss": 0.43374132679309696,
      "fixed_moe_accuracy": 0.09587818742185332,
      "candidate_loss": 0.40043345085966087,
      "candidate_accuracy": 0.335971191900745,
      "loss_gap_vs_fixed": -0.03330787593343609,
      "accuracy_gap_vs_fixed": 0.24009300447889165,
      "loss_pass": true,
      "accuracy_pass": true,
      "family_level_pass": true,
      "catastrophic_family_collapse_count": 0
    }
  ],
  "catastrophic_family_collapse_count": 2,
  "variance_blocked": false,
  "subrun_dirs": [
    "evaluation/benchmark_results/pvr_final_candidate_v1_1_revalidation/seed_42",
    "evaluation/benchmark_results/pvr_final_candidate_v1_1_revalidation/seed_123",
    "evaluation/benchmark_results/pvr_final_candidate_v1_1_revalidation/seed_777",
    "evaluation/benchmark_results/pvr_final_candidate_v1_1_revalidation/seed_2026",
    "evaluation/benchmark_results/pvr_final_candidate_v1_1_revalidation/seed_9001"
  ],
  "revalidated_candidate": "pvr_ec_ownership_top1_final_candidate_v1_1"
}
```