# PVR-EC Conditional Scale Oracle Report

**Status:** PVR_EC_BENCHMARK_TRANSFER_BLOCKER

**Statuses:** PVR_EC_BENCHMARK_CAPABILITY_NOT_IMPROVED, PVR_EC_BENCHMARK_TRANSFER_BLOCKER, PVR_EC_DO_NOT_PROMOTE, PVR_EC_EXPERT_RESIDUAL_ALIGNMENT_BLOCKER, PVR_EC_RESIDUAL_ALIGNED_TO_BENCHMARK

```json
{
  "metadata": {
    "timestamp": "2026-06-07T02:35:48.876480",
    "run_id": "algo_20260607_023517_benchmark-lite",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 42,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode benchmark-lite --scale small --sample-limit 1000 --train-steps 500 --device cuda --amp --models pvr_ec_ownership_top1_scale_schedule_1_to_8 --enable-ownership-map --ownership-map-mode frozen --run-segment-residual-diagnostic --output-dir evaluation/benchmark_results/pvr_segment_residual_diagnostic",
    "model_variants": [
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
  "status": "PVR_EC_BENCHMARK_TRANSFER_BLOCKER",
  "statuses": [
    "PVR_EC_BENCHMARK_CAPABILITY_NOT_IMPROVED",
    "PVR_EC_BENCHMARK_TRANSFER_BLOCKER",
    "PVR_EC_DO_NOT_PROMOTE",
    "PVR_EC_EXPERT_RESIDUAL_ALIGNMENT_BLOCKER",
    "PVR_EC_RESIDUAL_ALIGNED_TO_BENCHMARK"
  ],
  "promotion_ready": false,
  "diagnostic_only": true,
  "conditional_scale_modes": [],
  "best_scale_by_family": {
    "clrs_style": {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8",
      "scale": "warmup_hold_1_to_8",
      "loss": 0.29691687040030956,
      "accuracy": 0.11316433984218958,
      "quality_per_ms": 0.11316433984218958,
      "residual_help_rate": 0.8264945422609647,
      "residual_harm_rate": 0.17344332796831927,
      "expert_delta_contribution_pct": 0.9216746845863724,
      "shared_sparse_ratio": 0.11632073135115206,
      "logit_norm": 32.577272733052574,
      "prediction_entropy": 3.0151160856088004,
      "ECE_proxy": 0.07585504488642315,
      "owner_stability": 1.0,
      "prototype_owner_entropy": 0.0
    },
    "dyck": {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8",
      "scale": "warmup_hold_1_to_8",
      "loss": 0.3498579583441218,
      "accuracy": 0.007735737371833997,
      "quality_per_ms": 0.007735737371833997,
      "residual_help_rate": 0.617033274223407,
      "residual_harm_rate": 0.3824177350228032,
      "expert_delta_contribution_pct": 0.9213599923884825,
      "shared_sparse_ratio": 0.11626427316029245,
      "logit_norm": 17.14210353295008,
      "prediction_entropy": 5.08198327322801,
      "ECE_proxy": 0.10213167781636057,
      "owner_stability": 1.0,
      "prototype_owner_entropy": 0.0
    },
    "listops": {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8",
      "scale": "warmup_hold_1_to_8",
      "loss": 1.625009048730135,
      "accuracy": 0.09487165084536314,
      "quality_per_ms": 0.09487165084536314,
      "residual_help_rate": 0.5817891173064709,
      "residual_harm_rate": 0.4180718418210745,
      "expert_delta_contribution_pct": 0.9305554046500178,
      "shared_sparse_ratio": 0.09421674243640155,
      "logit_norm": 26.041479349136353,
      "prediction_entropy": 4.570935130119324,
      "ECE_proxy": 0.04694782571866794,
      "owner_stability": 1.0,
      "prototype_owner_entropy": 0.0
    },
    "scan_style": {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8",
      "scale": "warmup_hold_1_to_8",
      "loss": 0.24619680177420378,
      "accuracy": 0.01726854679620559,
      "quality_per_ms": 0.01726854679620559,
      "residual_help_rate": 0.4335414683446288,
      "residual_harm_rate": 0.5661997655406594,
      "expert_delta_contribution_pct": 0.9209543448405708,
      "shared_sparse_ratio": 0.1170818458776921,
      "logit_norm": 17.200516521930695,
      "prediction_entropy": 5.044208839535713,
      "ECE_proxy": 0.09508743158507935,
      "owner_stability": 1.0,
      "prototype_owner_entropy": 0.0
    }
  },
  "best_scale_by_prototype": {
    "diagnostic_bucket_all": {
      "clrs_style": {
        "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8",
        "scale": "warmup_hold_1_to_8",
        "loss": 0.29691687040030956,
        "accuracy": 0.11316433984218958,
        "quality_per_ms": 0.11316433984218958,
        "residual_help_rate": 0.8264945422609647,
        "residual_harm_rate": 0.17344332796831927,
        "expert_delta_contribution_pct": 0.9216746845863724,
        "shared_sparse_ratio": 0.11632073135115206,
        "logit_norm": 32.577272733052574,
        "prediction_entropy": 3.0151160856088004,
        "ECE_proxy": 0.07585504488642315,
        "owner_stability": 1.0,
        "prototype_owner_entropy": 0.0
      },
      "dyck": {
        "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8",
        "scale": "warmup_hold_1_to_8",
        "loss": 0.3498579583441218,
        "accuracy": 0.007735737371833997,
        "quality_per_ms": 0.007735737371833997,
        "residual_help_rate": 0.617033274223407,
        "residual_harm_rate": 0.3824177350228032,
        "expert_delta_contribution_pct": 0.9213599923884825,
        "shared_sparse_ratio": 0.11626427316029245,
        "logit_norm": 17.14210353295008,
        "prediction_entropy": 5.08198327322801,
        "ECE_proxy": 0.10213167781636057,
        "owner_stability": 1.0,
        "prototype_owner_entropy": 0.0
      },
      "listops": {
        "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8",
        "scale": "warmup_hold_1_to_8",
        "loss": 1.625009048730135,
        "accuracy": 0.09487165084536314,
        "quality_per_ms": 0.09487165084536314,
        "residual_help_rate": 0.5817891173064709,
        "residual_harm_rate": 0.4180718418210745,
        "expert_delta_contribution_pct": 0.9305554046500178,
        "shared_sparse_ratio": 0.09421674243640155,
        "logit_norm": 26.041479349136353,
        "prediction_entropy": 4.570935130119324,
        "ECE_proxy": 0.04694782571866794,
        "owner_stability": 1.0,
        "prototype_owner_entropy": 0.0
      },
      "scan_style": {
        "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8",
        "scale": "warmup_hold_1_to_8",
        "loss": 0.24619680177420378,
        "accuracy": 0.01726854679620559,
        "quality_per_ms": 0.01726854679620559,
        "residual_help_rate": 0.4335414683446288,
        "residual_harm_rate": 0.5661997655406594,
        "expert_delta_contribution_pct": 0.9209543448405708,
        "shared_sparse_ratio": 0.1170818458776921,
        "logit_norm": 17.200516521930695,
        "prediction_entropy": 5.044208839535713,
        "ECE_proxy": 0.09508743158507935,
        "owner_stability": 1.0,
        "prototype_owner_entropy": 0.0
      }
    }
  },
  "best_scale_by_owner": {
    "diagnostic_owner_all": {
      "clrs_style": {
        "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8",
        "scale": "warmup_hold_1_to_8",
        "loss": 0.29691687040030956,
        "accuracy": 0.11316433984218958,
        "quality_per_ms": 0.11316433984218958,
        "residual_help_rate": 0.8264945422609647,
        "residual_harm_rate": 0.17344332796831927,
        "expert_delta_contribution_pct": 0.9216746845863724,
        "shared_sparse_ratio": 0.11632073135115206,
        "logit_norm": 32.577272733052574,
        "prediction_entropy": 3.0151160856088004,
        "ECE_proxy": 0.07585504488642315,
        "owner_stability": 1.0,
        "prototype_owner_entropy": 0.0
      },
      "dyck": {
        "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8",
        "scale": "warmup_hold_1_to_8",
        "loss": 0.3498579583441218,
        "accuracy": 0.007735737371833997,
        "quality_per_ms": 0.007735737371833997,
        "residual_help_rate": 0.617033274223407,
        "residual_harm_rate": 0.3824177350228032,
        "expert_delta_contribution_pct": 0.9213599923884825,
        "shared_sparse_ratio": 0.11626427316029245,
        "logit_norm": 17.14210353295008,
        "prediction_entropy": 5.08198327322801,
        "ECE_proxy": 0.10213167781636057,
        "owner_stability": 1.0,
        "prototype_owner_entropy": 0.0
      },
      "listops": {
        "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8",
        "scale": "warmup_hold_1_to_8",
        "loss": 1.625009048730135,
        "accuracy": 0.09487165084536314,
        "quality_per_ms": 0.09487165084536314,
        "residual_help_rate": 0.5817891173064709,
        "residual_harm_rate": 0.4180718418210745,
        "expert_delta_contribution_pct": 0.9305554046500178,
        "shared_sparse_ratio": 0.09421674243640155,
        "logit_norm": 26.041479349136353,
        "prediction_entropy": 4.570935130119324,
        "ECE_proxy": 0.04694782571866794,
        "owner_stability": 1.0,
        "prototype_owner_entropy": 0.0
      },
      "scan_style": {
        "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8",
        "scale": "warmup_hold_1_to_8",
        "loss": 0.24619680177420378,
        "accuracy": 0.01726854679620559,
        "quality_per_ms": 0.01726854679620559,
        "residual_help_rate": 0.4335414683446288,
        "residual_harm_rate": 0.5661997655406594,
        "expert_delta_contribution_pct": 0.9209543448405708,
        "shared_sparse_ratio": 0.1170818458776921,
        "logit_norm": 17.200516521930695,
        "prediction_entropy": 5.044208839535713,
        "ECE_proxy": 0.09508743158507935,
        "owner_stability": 1.0,
        "prototype_owner_entropy": 0.0
      }
    }
  },
  "conditional_scale_gain_over_global": -0.16601152229122818,
  "conditional_scale_overfit_risk": "high: oracle selected from validation rows; diagnostic only",
  "global_best_loss": 0.4634836475209644
}
```