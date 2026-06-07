# PVR-EC Transfer Profile Report

**Status:** PVR_EC_TASK_LEVEL_TRANSFER_BLOCKER

**Statuses:** PVR_EC_BENCHMARK_CAPABILITY_NOT_IMPROVED, PVR_EC_BENCHMARK_TRANSFER_BLOCKER, PVR_EC_DO_NOT_PROMOTE, PVR_EC_DYCK_FINAL_STATE_BLOCKER, PVR_EC_EXPERT_RESIDUAL_ALIGNMENT_BLOCKER, PVR_EC_LISTOPS_TRANSFER_BLOCKER, PVR_EC_RESIDUAL_ALIGNED_TO_BENCHMARK, PVR_EC_SCAN_TRANSFER_BLOCKER, PVR_EC_TASK_LEVEL_TRANSFER_BLOCKER

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
  "status": "PVR_EC_TASK_LEVEL_TRANSFER_BLOCKER",
  "statuses": [
    "PVR_EC_BENCHMARK_CAPABILITY_NOT_IMPROVED",
    "PVR_EC_BENCHMARK_TRANSFER_BLOCKER",
    "PVR_EC_DO_NOT_PROMOTE",
    "PVR_EC_DYCK_FINAL_STATE_BLOCKER",
    "PVR_EC_EXPERT_RESIDUAL_ALIGNMENT_BLOCKER",
    "PVR_EC_LISTOPS_TRANSFER_BLOCKER",
    "PVR_EC_RESIDUAL_ALIGNED_TO_BENCHMARK",
    "PVR_EC_SCAN_TRANSFER_BLOCKER",
    "PVR_EC_TASK_LEVEL_TRANSFER_BLOCKER"
  ],
  "promotion_ready": false,
  "model_table": {
    "pvr_ec_ownership_top1_scale_schedule_1_to_8": {
      "params": 482690,
      "avg_accuracy": 0.06054665483850138,
      "avg_exact_match": 0.0,
      "avg_loss": 0.4634836475209644,
      "avg_qpc": 0.06054665483850138,
      "avg_loops": 1.0
    }
  },
  "loss_by_family": {
    "pvr_ec_ownership_top1_scale_schedule_1_to_8": {
      "clrs_style": 0.29691687040030956,
      "listops": 1.625009048730135,
      "scan_style": 0.24619680177420378,
      "dyck": 0.3498579583441218
    }
  },
  "accuracy_by_family": {
    "pvr_ec_ownership_top1_scale_schedule_1_to_8": {
      "clrs_style": 0.11316433984218958,
      "listops": 0.09487165084536314,
      "scan_style": 0.01726854679620559,
      "dyck": 0.007735737371833997
    }
  },
  "residual_help_rate_by_family": {
    "clrs_style": 0.8264945422609647,
    "dyck": 0.617033274223407,
    "listops": 0.5817891173064709,
    "scan_style": 0.4335414683446288
  },
  "residual_harm_rate_by_family": {
    "clrs_style": 0.17344332796831927,
    "dyck": 0.3824177350228032,
    "listops": 0.4180718418210745,
    "scan_style": 0.5661997655406594
  },
  "expert_delta_contribution_pct_by_family": {
    "clrs_style": 0.9216746845863724,
    "dyck": 0.9213599923884825,
    "listops": 0.9305554046500178,
    "scan_style": 0.9209543448405708
  },
  "shared_sparse_ratio_by_family": {
    "clrs_style": 0.11632073135115206,
    "dyck": 0.11626427316029245,
    "listops": 0.09421674243640155,
    "scan_style": 0.1170818458776921
  },
  "calibration_proxy_by_family": {
    "clrs_style": 0.07585504488642315,
    "dyck": 0.10213167781636057,
    "listops": 0.04694782571866794,
    "scan_style": 0.09508743158507935
  },
  "latency_p50": 0.6111965477466583,
  "latency_p95": 0.6111965477466583,
  "owner_count_per_token": 1.0,
  "Top2_executions": 0.0,
  "Top4_executions": 0.0
}
```