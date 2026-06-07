# PVR-EC Token To Sequence Transfer Report

**Status:** PVR_EC_TASK_LEVEL_TRANSFER_BLOCKER

**Statuses:** PVR_EC_BENCHMARK_CAPABILITY_NOT_IMPROVED, PVR_EC_BENCHMARK_TRANSFER_BLOCKER, PVR_EC_DO_NOT_PROMOTE, PVR_EC_DYCK_FINAL_STATE_BLOCKER, PVR_EC_EXPERT_RESIDUAL_ALIGNMENT_BLOCKER, PVR_EC_LISTOPS_TRANSFER_BLOCKER, PVR_EC_RESIDUAL_ALIGNED_TO_BENCHMARK, PVR_EC_SCALE_HELPFUL_BY_FAMILY, PVR_EC_SCALE_OVERAMPLIFIES_BENCHMARK_NOISE, PVR_EC_SCAN_TRANSFER_BLOCKER, PVR_EC_TASK_LEVEL_TRANSFER_BLOCKER

```json
{
  "metadata": {
    "timestamp": "2026-06-07T02:33:38.757263",
    "run_id": "algo_20260607_023103_benchmark-lite",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 42,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode benchmark-lite --scale small --sample-limit 1000 --train-steps 500 --device cuda --amp --models fixed_moe_vectorized,pvr_ec_deploy_top1,pvr_ec_ownership_top1_scale_schedule_1_to_8 --enable-ownership-map --ownership-map-mode frozen --run-task-level-transfer-diagnostic --run-decision-token-credit-diagnostic --run-token-to-sequence-transfer-diagnostic --run-family-failure-decomposition --output-dir evaluation/benchmark_results/pvr_task_level_transfer",
    "model_variants": [
      "fixed_moe_vectorized",
      "pvr_ec_deploy_top1",
      "pvr_ec_ownership_top1_scale_schedule_1_to_8"
    ],
    "batch_sizes": [
      1,
      32
    ],
    "sequence_lengths": [
      64
    ],
    "train_steps": 500,
    "sample_limit": 1000,
    "mode": "benchmark-lite",
    "scale": "small",
    "families": [
      "clrs",
      "listops",
      "scan",
      "dyck"
    ],
    "pvr_expert_delta_scale": null,
    "pvr_expert_delta_scale_schedule": "constant",
    "pvr_expert_delta_scale_start": null,
    "pvr_expert_delta_scale_end": null,
    "pvr_expert_delta_scale_warmup_steps": null,
    "pvr_expert_delta_scale_hold_steps": null,
    "pvr_expert_delta_scale_decay": null
  },
  "status": "PVR_EC_TASK_LEVEL_TRANSFER_BLOCKER",
  "statuses": [
    "PVR_EC_BENCHMARK_CAPABILITY_NOT_IMPROVED",
    "PVR_EC_BENCHMARK_TRANSFER_BLOCKER",
    "PVR_EC_DO_NOT_PROMOTE",
    "PVR_EC_DYCK_FINAL_STATE_BLOCKER",
    "PVR_EC_EXPERT_RESIDUAL_ALIGNMENT_BLOCKER",
    "PVR_EC_LISTOPS_TRANSFER_BLOCKER",
    "PVR_EC_RESIDUAL_ALIGNED_TO_BENCHMARK",
    "PVR_EC_SCALE_HELPFUL_BY_FAMILY",
    "PVR_EC_SCALE_OVERAMPLIFIES_BENCHMARK_NOISE",
    "PVR_EC_SCAN_TRANSFER_BLOCKER",
    "PVR_EC_TASK_LEVEL_TRANSFER_BLOCKER"
  ],
  "promotion_ready": false,
  "token_loss_improvement": 0.38572552934670057,
  "sequence_loss_improvement": 0.39924823243086394,
  "sequence_accuracy_improvement": 0.022701894626910264,
  "token_to_sequence_transfer_ratio": -1.471803878530161,
  "by_task_family": {
    "clrs_style": {
      "token_loss_improvement": 0.49298800195538206,
      "sequence_accuracy_improvement": 0.08035180757360649,
      "token_to_sequence_transfer_ratio": 0.7070233901532123
    },
    "dyck": {
      "token_loss_improvement": 0.27694554842310026,
      "sequence_accuracy_improvement": -0.010955798191086311,
      "token_to_sequence_transfer_ratio": -0.37144736817193397
    },
    "listops": {
      "token_loss_improvement": 0.48559148982167244,
      "sequence_accuracy_improvement": 0.026904232014203444,
      "token_to_sequence_transfer_ratio": 0.06940707152427893
    },
    "scan_style": {
      "token_loss_improvement": 0.2836788211197927,
      "sequence_accuracy_improvement": -0.03221645066878409,
      "token_to_sequence_transfer_ratio": -6.611006766940668
    }
  },
  "by_sequence_length_bucket": {
    "mixed": -1.471803878530161
  },
  "by_difficulty_bucket": {
    "mixed": -1.471803878530161
  },
  "by_prototype_id": {
    "diagnostic_all": -1.471803878530161
  },
  "by_owner_expert": {
    "diagnostic_all": -1.471803878530161
  },
  "by_decision_position_type": {
    "final": -1.471803878530161
  }
}
```