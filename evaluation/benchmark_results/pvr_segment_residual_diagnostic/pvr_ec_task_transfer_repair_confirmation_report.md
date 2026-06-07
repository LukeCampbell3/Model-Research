# PVR-EC Task Transfer Repair Confirmation Report

**Status:** PVR_EC_BENCHMARK_CAPABILITY_NOT_IMPROVED

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
  "status": "PVR_EC_BENCHMARK_CAPABILITY_NOT_IMPROVED",
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
  "fixed_moe_vectorized": {},
  "pvr_ec_deploy_top1": {},
  "pvr_ec_ownership_top1_best_transfer_repair": {},
  "token_to_sequence_transfer_ratio": 0.06254859396826354,
  "decision_token_help_rate": 0.6470743940056611,
  "residual_help_rate": 0.6453027786531795,
  "residual_harm_rate": 0.3544546033566197,
  "quality_per_ms": null,
  "latency_p50": 0.6111965477466583,
  "latency_p95": 0.6111965477466583,
  "calibration_proxy": 0.08361889739760216,
  "loss_by_family": {
    "clrs_style": 0.29691687040030956,
    "dyck": 0.3498579583441218,
    "listops": 1.625009048730135,
    "scan_style": 0.24619680177420378
  },
  "accuracy_by_family": {
    "clrs_style": 0.11316433984218958,
    "dyck": 0.007735737371833997,
    "listops": 0.09487165084536314,
    "scan_style": 0.01726854679620559
  }
}
```