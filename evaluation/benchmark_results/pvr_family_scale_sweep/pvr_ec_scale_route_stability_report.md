# PVR-EC Scale Route Stability Report

**Status:** PVR_EC_BENCHMARK_TRANSFER_BLOCKER

**Statuses:** PVR_EC_BENCHMARK_CAPABILITY_NOT_IMPROVED, PVR_EC_BENCHMARK_TRANSFER_BLOCKER, PVR_EC_DO_NOT_PROMOTE, PVR_EC_EXPERT_RESIDUAL_ALIGNMENT_BLOCKER, PVR_EC_RESIDUAL_ALIGNED_TO_BENCHMARK

```json
{
  "metadata": {
    "timestamp": "2026-06-07T02:08:45.615666",
    "run_id": "algo_20260607_020501_benchmark-lite",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 42,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode benchmark-lite --scale small --sample-limit 1000 --train-steps 500 --device cuda --amp --models pvr_ec_ownership_top1_constant_1,pvr_ec_ownership_top1_constant_2,pvr_ec_ownership_top1_constant_4,pvr_ec_ownership_top1_constant_8,pvr_ec_ownership_top1_scale_schedule_1_to_4,pvr_ec_ownership_top1_scale_schedule_1_to_8,pvr_ec_ownership_top1_scale_schedule_1_to_8_to_4,pvr_ec_ownership_top1_scale_schedule_1_to_8_to_2,pvr_ec_ownership_top1_scale_schedule_1_to_4_to_2 --enable-ownership-map --ownership-map-mode frozen --run-family-scale-sweep --output-dir evaluation/benchmark_results/pvr_family_scale_sweep",
    "model_variants": [
      "pvr_ec_ownership_top1_constant_1",
      "pvr_ec_ownership_top1_constant_2",
      "pvr_ec_ownership_top1_constant_4",
      "pvr_ec_ownership_top1_constant_8",
      "pvr_ec_ownership_top1_scale_schedule_1_to_4",
      "pvr_ec_ownership_top1_scale_schedule_1_to_8",
      "pvr_ec_ownership_top1_scale_schedule_1_to_8_to_4",
      "pvr_ec_ownership_top1_scale_schedule_1_to_8_to_2",
      "pvr_ec_ownership_top1_scale_schedule_1_to_4_to_2"
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
  "owner_id_match_rate_vs_scale_1": 1.0,
  "owner_change_rate_by_scale": {
    "constant_1": 0.0,
    "constant_2": 0.0,
    "constant_4": 0.0,
    "constant_8": 0.0,
    "warmup_hold_1_to_4": 0.0,
    "warmup_hold_1_to_8": 0.0,
    "warmup_hold_decay_1_to_8_to_4": 0.0,
    "warmup_hold_decay_1_to_8_to_2": 0.0,
    "warmup_hold_decay_1_to_4_to_2": 0.0
  },
  "owner_entropy_by_scale": {
    "constant_1": 0.0,
    "constant_2": 0.0,
    "constant_4": 0.0,
    "constant_8": 0.0,
    "warmup_hold_1_to_4": 0.0,
    "warmup_hold_1_to_8": 0.0,
    "warmup_hold_decay_1_to_8_to_4": 0.0,
    "warmup_hold_decay_1_to_8_to_2": 0.0,
    "warmup_hold_decay_1_to_4_to_2": 0.0
  },
  "prototype_owner_entropy_by_scale": {
    "constant_1": 0.0,
    "constant_2": 0.0,
    "constant_4": 0.0,
    "constant_8": 0.0,
    "warmup_hold_1_to_4": 0.0,
    "warmup_hold_1_to_8": 0.0,
    "warmup_hold_decay_1_to_8_to_4": 0.0,
    "warmup_hold_decay_1_to_8_to_2": 0.0,
    "warmup_hold_decay_1_to_4_to_2": 0.0
  },
  "prototype_local_monopoly_rate": 0.0,
  "top1_oracle_gap_by_scale": {
    "constant_1": 0.0,
    "constant_2": 0.0,
    "constant_4": 0.0,
    "constant_8": 0.0,
    "warmup_hold_1_to_4": 0.0,
    "warmup_hold_1_to_8": 0.0,
    "warmup_hold_decay_1_to_8_to_4": 0.0,
    "warmup_hold_decay_1_to_8_to_2": 0.0,
    "warmup_hold_decay_1_to_4_to_2": 0.0
  },
  "owner_confidence_by_scale": {
    "constant_1": 0.0,
    "constant_2": 0.0,
    "constant_4": 0.0,
    "constant_8": 0.0,
    "warmup_hold_1_to_4": 0.0,
    "warmup_hold_1_to_8": 0.0,
    "warmup_hold_decay_1_to_8_to_4": 0.0,
    "warmup_hold_decay_1_to_8_to_2": 0.0,
    "warmup_hold_decay_1_to_4_to_2": 0.0
  },
  "high_confidence_failure_rate_by_scale": {
    "constant_1": 0.0,
    "constant_2": 0.0,
    "constant_4": 0.0,
    "constant_8": 0.0,
    "warmup_hold_1_to_4": 0.0,
    "warmup_hold_1_to_8": 0.0,
    "warmup_hold_decay_1_to_8_to_4": 0.0,
    "warmup_hold_decay_1_to_8_to_2": 0.0,
    "warmup_hold_decay_1_to_4_to_2": 0.0
  },
  "route_stability_result": "scale_applied_after_routing; owner ids expected stable under scale-only changes"
}
```