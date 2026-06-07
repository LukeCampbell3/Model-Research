# PVR-EC Family Failure Decomposition Report

**Status:** PVR_EC_TASK_LEVEL_TRANSFER_BLOCKER

**Statuses:** PVR_EC_BENCHMARK_CAPABILITY_NOT_IMPROVED, PVR_EC_BENCHMARK_TRANSFER_BLOCKER, PVR_EC_DO_NOT_PROMOTE, PVR_EC_DYCK_FINAL_STATE_BLOCKER, PVR_EC_EXPERT_RESIDUAL_ALIGNMENT_BLOCKER, PVR_EC_LISTOPS_TRANSFER_BLOCKER, PVR_EC_RESIDUAL_ALIGNED_TO_BENCHMARK, PVR_EC_SCALE_HELPFUL_BY_FAMILY, PVR_EC_SCAN_TRANSFER_BLOCKER, PVR_EC_TASK_LEVEL_TRANSFER_BLOCKER

```json
{
  "metadata": {
    "timestamp": "2026-06-07T02:38:37.744118",
    "run_id": "algo_20260607_023602_benchmark-lite",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 42,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode benchmark-lite --scale small --sample-limit 1000 --train-steps 500 --device cuda --amp --models fixed_moe_vectorized,pvr_ec_deploy_top1,pvr_ec_ownership_top1_best_transfer_repair --enable-ownership-map --ownership-map-mode frozen --run-benchmark-transfer-confirmation --output-dir evaluation/benchmark_results/pvr_task_transfer_repair_confirmation",
    "model_variants": [
      "fixed_moe_vectorized",
      "pvr_ec_deploy_top1",
      "pvr_ec_ownership_top1_best_transfer_repair"
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
    "PVR_EC_SCAN_TRANSFER_BLOCKER",
    "PVR_EC_TASK_LEVEL_TRANSFER_BLOCKER"
  ],
  "promotion_ready": false,
  "by_family": {
    "clrs_style": {
      "baseline_loss": null,
      "pvr_loss": 0.26753168646246195,
      "scaled_pvr_loss": 0.26753168646246195,
      "baseline_accuracy": null,
      "pvr_accuracy": 0.1713499366157629,
      "scaled_pvr_accuracy": 0.1713499366157629,
      "residual_help_rate": 0.7543035758038362,
      "residual_harm_rate": 0.24549427178377906,
      "decision_token_help_rate": 0.7543035758038362,
      "final_state_help_rate": 0.7543035758038362,
      "owner_entropy": 0.0,
      "prototype_entropy": 0.0,
      "expert_contribution_pct": 0.8927741461681865,
      "calibration_proxy": 0.07047602426504876,
      "top_error_modes": [
        "low_sequence_accuracy",
        "decision_credit_or_aggregation"
      ]
    },
    "dyck": {
      "baseline_loss": null,
      "pvr_loss": 0.3576503098011017,
      "scaled_pvr_loss": 0.3498579617589712,
      "baseline_accuracy": null,
      "pvr_accuracy": 0.0,
      "scaled_pvr_accuracy": 0.007735737371833997,
      "residual_help_rate": 0.5272507594587902,
      "residual_harm_rate": 0.4721299461089075,
      "decision_token_help_rate": 0.5272507594587902,
      "final_state_help_rate": 0.5272507594587902,
      "owner_entropy": 0.0,
      "prototype_entropy": 0.0,
      "expert_contribution_pct": 0.8918826884475157,
      "calibration_proxy": 0.11153604823230753,
      "top_error_modes": [
        "low_sequence_accuracy",
        "decision_credit_or_aggregation"
      ]
    },
    "listops": {
      "baseline_loss": null,
      "pvr_loss": 1.589727409183979,
      "scaled_pvr_loss": 1.589727409183979,
      "baseline_accuracy": null,
      "pvr_accuracy": 0.08681121159355165,
      "scaled_pvr_accuracy": 0.08681121159355165,
      "residual_help_rate": 0.6583926975727081,
      "residual_harm_rate": 0.3413939536549151,
      "decision_token_help_rate": 0.7151608914136887,
      "final_state_help_rate": 0.7151608914136887,
      "owner_entropy": 0.0,
      "prototype_entropy": 0.0,
      "expert_contribution_pct": 0.8960048874281952,
      "calibration_proxy": 0.04745421975906301,
      "top_error_modes": [
        "low_sequence_accuracy",
        "decision_credit_or_aggregation"
      ]
    },
    "scan_style": {
      "baseline_loss": null,
      "pvr_loss": 0.2501062727533281,
      "scaled_pvr_loss": 0.2461968050338328,
      "baseline_accuracy": null,
      "pvr_accuracy": 0.008169493393971418,
      "scaled_pvr_accuracy": 0.01726854679620559,
      "residual_help_rate": 0.4542821808718145,
      "residual_harm_rate": 0.5453439801931381,
      "decision_token_help_rate": 0.4542821808718145,
      "final_state_help_rate": 0.4542821808718145,
      "owner_entropy": 0.0,
      "prototype_entropy": 0.0,
      "expert_contribution_pct": 0.8900728986020299,
      "calibration_proxy": 0.10891413230394979,
      "top_error_modes": [
        "low_sequence_accuracy",
        "decision_credit_or_aggregation"
      ]
    }
  },
  "listops_decomposition": {
    "nesting_depth_bucket": "mixed",
    "operator_type": "mixed",
    "sequence_length_bucket": "mixed",
    "final_answer_position": "final",
    "operator_close_position": "diagnostic",
    "depth_generalization_error": "not_isolated",
    "final_answer_error": "low_accuracy"
  },
  "scan_decomposition": {
    "command_length_bucket": "mixed",
    "action_length_bucket": "mixed",
    "composition_type": "mixed",
    "primitive_mapping_error": "not_isolated",
    "length_generalization_error": "low_accuracy",
    "repetition_error": "not_isolated",
    "composition_boundary_error": "not_isolated"
  },
  "dyck_decomposition": {
    "stack_depth_bucket": "mixed",
    "closing_token_error": "low_accuracy",
    "completion_position_error": "low_accuracy",
    "validity_error": "not_isolated",
    "final_state_error": "low_accuracy"
  }
}
```