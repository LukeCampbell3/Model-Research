# PVR-EC Decision Token Credit Report

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
  "loss_delta_by_position": {
    "final": -0.39924823243086394,
    "decision": -0.39924823243086394,
    "nondecision": -0.38570646272887643
  },
  "accuracy_delta_by_position": {
    "decision": 0.022701894626910264
  },
  "residual_help_rate_by_position": {
    "decision": 0.6176421874358008,
    "all": 0.6105461632056782
  },
  "residual_harm_rate_by_position": {
    "decision": 0.38201467058388516,
    "all": 0.38910307770129293
  },
  "expert_contribution_by_position": {
    "decision": 0.8922798124707707,
    "all": 0.8922798124707707
  },
  "final_token_loss_delta": -0.39924823243086394,
  "final_state_loss_delta": -0.39924823243086394,
  "decision_position_loss_delta": -0.39924823243086394,
  "nondecision_position_loss_delta": -0.38570646272887643,
  "decision_token_help_rate": 0.6176421874358008,
  "decision_token_harm_rate": 0.38201467058388516,
  "decision_token_expert_contribution_pct": 0.8922798124707707,
  "by_family": {
    "clrs_style": {
      "decision_token_help_rate": 0.7543035758038362,
      "decision_position_loss_delta": -0.49298800195538206
    },
    "dyck": {
      "decision_token_help_rate": 0.5272507594587902,
      "decision_position_loss_delta": -0.27694554842310026
    },
    "listops": {
      "decision_token_help_rate": 0.7151608914136887,
      "decision_position_loss_delta": -0.5937731144949794
    },
    "scan_style": {
      "decision_token_help_rate": 0.4542821808718145,
      "decision_position_loss_delta": -0.2836788211197927
    }
  }
}
```