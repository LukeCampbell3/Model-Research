# PVR-EC Sparse Direction Transfer Confirmation Report

**Status:** PVR_EC_BENCHMARK_CAPABILITY_NOT_IMPROVED

**Statuses:** PVR_EC_BENCHMARK_CAPABILITY_NOT_IMPROVED, PVR_EC_DO_NOT_PROMOTE, PVR_EC_SPARSE_LOGIT_DIRECTION_DIAGNOSTIC_READY, PVR_EC_SPARSE_LOGIT_DIRECTION_MISALIGNED

```json
{
  "metadata": {
    "timestamp": "2026-06-07T03:13:54.653030",
    "run_id": "algo_20260607_031113_benchmark-lite",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 42,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode benchmark-lite --scale small --sample-limit 1000 --train-steps 500 --device cuda --amp --models fixed_moe_vectorized,pvr_ec_deploy_top1,pvr_ec_ownership_top1_scale_schedule_1_to_8 --enable-ownership-map --ownership-map-mode frozen --run-sparse-logit-direction-diagnostic --output-dir evaluation/benchmark_results/pvr_sparse_logit_direction",
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
  "status": "PVR_EC_BENCHMARK_CAPABILITY_NOT_IMPROVED",
  "statuses": [
    "PVR_EC_BENCHMARK_CAPABILITY_NOT_IMPROVED",
    "PVR_EC_DO_NOT_PROMOTE",
    "PVR_EC_SPARSE_LOGIT_DIRECTION_DIAGNOSTIC_READY",
    "PVR_EC_SPARSE_LOGIT_DIRECTION_MISALIGNED"
  ],
  "promotion_ready": false,
  "fixed_moe_vectorized": {
    "params": 1001092,
    "avg_accuracy": 0.25857819999606313,
    "avg_exact_match": 0.00925,
    "avg_loss": 0.3886076922838887,
    "avg_qpc": 0.12928909999803156,
    "avg_loops": 1.0
  },
  "pvr_ec_deploy_top1": {
    "params": 614274,
    "avg_accuracy": 0.0771500010285979,
    "avg_exact_match": 0.0,
    "avg_loss": 0.4509794550249353,
    "avg_qpc": 0.0771500010285979,
    "avg_loops": 1.0
  },
  "pvr_ec_ownership_top1_scale_schedule_1_to_8": {
    "params": 482690,
    "avg_accuracy": 0.06054665483850138,
    "avg_exact_match": 0.0,
    "avg_loss": 0.4634839184194183,
    "avg_qpc": 0.06054665483850138,
    "avg_loops": 1.0
  },
  "pvr_ec_ownership_top1_best_sparse_logit_repair": {},
  "loss_gate_vs_deploy_top1": false,
  "accuracy_gate_vs_deploy_top1": false,
  "owner_count_per_token": null,
  "Top2_executions": 0.0,
  "Top4_executions": 0.0,
  "calibration_proxy": null,
  "latency_p50": null,
  "latency_p95": null,
  "loss_by_family": {},
  "accuracy_by_family": {},
  "correct_class_logit_delta": null,
  "incorrect_class_logit_delta_max": null,
  "delta_correct_minus_top_wrong": null,
  "residual_help_rate": null,
  "residual_harm_rate": null,
  "token_to_sequence_transfer_ratio": null
}
```