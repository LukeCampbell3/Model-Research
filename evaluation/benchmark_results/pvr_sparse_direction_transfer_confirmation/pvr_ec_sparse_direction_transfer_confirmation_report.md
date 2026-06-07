# PVR-EC Sparse Direction Transfer Confirmation Report

**Status:** PVR_EC_BENCHMARK_TRANSFER_REPAIRED

**Statuses:** PVR_EC_BENCHMARK_TRANSFER_REPAIRED, PVR_EC_CALIBRATION_REGRESSION, PVR_EC_DO_NOT_PROMOTE, PVR_EC_SPARSE_LOGIT_DIRECTION_DIAGNOSTIC_READY, PVR_EC_SPARSE_LOGIT_DIRECTION_MISALIGNED

```json
{
  "metadata": {
    "timestamp": "2026-06-07T03:30:49.443760",
    "run_id": "algo_20260607_032819_benchmark-lite",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 42,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode benchmark-lite --scale small --sample-limit 1000 --train-steps 500 --device cuda --amp --models fixed_moe_vectorized,pvr_ec_deploy_top1,pvr_ec_ownership_top1_scale_schedule_1_to_8,pvr_ec_ownership_top1_best_sparse_logit_repair --enable-ownership-map --ownership-map-mode frozen --run-sparse-direction-transfer-confirmation --output-dir evaluation/benchmark_results/pvr_sparse_direction_transfer_confirmation",
    "model_variants": [
      "fixed_moe_vectorized",
      "pvr_ec_deploy_top1",
      "pvr_ec_ownership_top1_scale_schedule_1_to_8",
      "pvr_ec_ownership_top1_best_sparse_logit_repair"
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
  "status": "PVR_EC_BENCHMARK_TRANSFER_REPAIRED",
  "statuses": [
    "PVR_EC_BENCHMARK_TRANSFER_REPAIRED",
    "PVR_EC_CALIBRATION_REGRESSION",
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
    "avg_loss": 0.45097945421002805,
    "avg_qpc": 0.0771500010285979,
    "avg_loops": 1.0
  },
  "pvr_ec_ownership_top1_scale_schedule_1_to_8": {
    "params": 482690,
    "avg_accuracy": 0.06054665483850138,
    "avg_exact_match": 0.0,
    "avg_loss": 0.46348366168482846,
    "avg_qpc": 0.06054665483850138,
    "avg_loops": 1.0
  },
  "pvr_ec_ownership_top1_best_sparse_logit_repair": {
    "params": 482690,
    "avg_accuracy": 0.24243722927027295,
    "avg_exact_match": 0.0,
    "avg_loss": 0.4004437902864689,
    "avg_qpc": 0.24243722927027295,
    "avg_loops": 1.0
  },
  "loss_gate_vs_deploy_top1": true,
  "accuracy_gate_vs_deploy_top1": true,
  "owner_count_per_token": 1.0,
  "Top2_executions": 0.0,
  "Top4_executions": 0.0,
  "calibration_proxy": 0.129966046250579,
  "deploy_top1_calibration_proxy": 0.09132675538426735,
  "calibration_regression": true,
  "latency_p50": 0.5439489781856537,
  "latency_p95": 0.5439489781856537,
  "loss_by_family": {
    "clrs_style": 0.23170064017176628,
    "listops": 1.3692205734550953,
    "scan_style": 0.2792850360274315,
    "dyck": 0.2721846265097459
  },
  "accuracy_by_family": {
    "clrs_style": 0.44870305845915603,
    "listops": 0.20945907993034882,
    "scan_style": 0.06708595387840671,
    "dyck": 0.0897029702970297
  },
  "correct_class_logit_delta": 4.7784558494264875,
  "incorrect_class_logit_delta_max": 5.837446682155132,
  "delta_correct_minus_top_wrong": -1.058990823570639,
  "residual_help_rate": 0.9835581281222403,
  "residual_harm_rate": 0.016441862707324617,
  "token_to_sequence_transfer_ratio": 0.05323877146522142
}
```