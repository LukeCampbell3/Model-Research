# PVR-EC Output Readout Report

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
  "diagnostic_only": true,
  "variants": [],
  "best_readout_variant": "baseline_output_head",
  "variant_metrics": {
    "baseline_output_head": {
      "loss": 0.45723156147869304,
      "accuracy": 0.06884832793354963,
      "readout_weight_norm_shared": 7.801002486919364,
      "readout_weight_norm_sparse": 76.53605296959479,
      "sparse_feature_utilization": 0.8922798125039807,
      "shared_feature_utilization": 0.15506214188644662,
      "logit_delta_from_sparse": 23.26655235451957,
      "correct_class_logit_delta": 0.12402329276740909,
      "incorrect_class_logit_delta": 2.3707534082544344,
      "final_state_feature_utilization": 0.8922798125039807
    }
  }
}
```