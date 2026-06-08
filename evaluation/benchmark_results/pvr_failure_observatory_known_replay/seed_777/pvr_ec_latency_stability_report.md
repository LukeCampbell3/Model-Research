# PVR-EC Latency Stability Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-08T03:31:47.886691",
    "run_id": "algo_20260608_032921_benchmark-lite",
    "git_commit": "c214633e8dfb56a3ba797333eee2da2c985b17cd",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 777,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode benchmark-lite --scale small --sample-limit 1000 --train-steps 500 --seed-list 123,777 --families clrs_style,listops --device cuda --amp --models fixed_moe_vectorized,pvr_ec_deploy_top1,pvr_ec_ownership_top1_final_candidate_v1,pvr_ec_ownership_top1_final_candidate_v1_1 --enable-ownership-map --ownership-map-mode frozen --run-failure-case-replay --run-failure-attribution --output-dir evaluation/benchmark_results/pvr_failure_observatory_known_replay",
    "model_variants": [
      "fixed_moe_vectorized",
      "pvr_ec_deploy_top1",
      "pvr_ec_ownership_top1_final_candidate_v1",
      "pvr_ec_ownership_top1_final_candidate_v1_1"
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
      "listops"
    ],
    "pvr_expert_delta_scale": null,
    "pvr_expert_delta_scale_schedule": "constant",
    "pvr_expert_delta_scale_start": null,
    "pvr_expert_delta_scale_end": null,
    "pvr_expert_delta_scale_warmup_steps": null,
    "pvr_expert_delta_scale_hold_steps": null,
    "pvr_expert_delta_scale_decay": null,
    "root_cause_flags": {
      "run_collapse_case_replay": true
    },
    "diagnostic_sweeps": {
      "train_steps_list": [
        500
      ],
      "seed_list": [
        777
      ],
      "batch_size_list": [
        1,
        32
      ],
      "seq_len_list": [
        64
      ],
      "shape_pairs": [],
      "max_train_seconds": null,
      "repeatability_repair_variants": [],
      "calibration_repair_variants": [],
      "minimax_variants": [],
      "stability_repair_variants": []
    },
    "source": "trained_benchmark"
  },
  "status": "PVR_EC_ROOT_CAUSE_INCONCLUSIVE",
  "statuses": [
    "PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY",
    "PVR_EC_DO_NOT_PROMOTE",
    "PVR_EC_ROOT_CAUSE_INCONCLUSIVE"
  ],
  "by_model": {
    "fixed_moe_vectorized": {
      "count": 4,
      "avg_loss": 0.5409156021196395,
      "avg_accuracy": 0.2438579845435691,
      "avg_train_loss": 0.16213898360729218,
      "latency_p50_ms": 1007.3688626289368,
      "latency_p95_ms": 1007.3688626289368,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_deploy_top1": {
      "count": 4,
      "avg_loss": 0.5899287902284414,
      "avg_accuracy": 0.16611370851563104,
      "avg_train_loss": 0.18943354487419128,
      "latency_p50_ms": 403.39720249176025,
      "latency_p95_ms": 403.39720249176025,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1": {
      "count": 4,
      "avg_loss": 0.5544045781716704,
      "avg_accuracy": 0.41903433213089625,
      "avg_train_loss": 0.16685862839221954,
      "latency_p50_ms": 349.4915962219238,
      "latency_p95_ms": 349.4915962219238,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1_1": {
      "count": 4,
      "avg_loss": 0.5711596482433379,
      "avg_accuracy": 0.41903433213089625,
      "avg_train_loss": 0.16685862839221954,
      "latency_p50_ms": 337.84669637680054,
      "latency_p95_ms": 337.84669637680054,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    }
  },
  "latency_p95_p50_ratio_reported": true,
  "max_latency_p95_p50_ratio": 1.0,
  "rows": [
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1007.4408054351807,
      "latency_p95_ms": 1007.4408054351807,
      "latency_p99_ms": 1007.4408054351807,
      "latency_max_ms": 1007.4408054351807,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 996.35910987854,
      "latency_p95_ms": 996.35910987854,
      "latency_p99_ms": 996.35910987854,
      "latency_max_ms": 996.35910987854,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1006.2658786773682,
      "latency_p95_ms": 1006.2658786773682,
      "latency_p99_ms": 1006.2658786773682,
      "latency_max_ms": 1006.2658786773682,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1019.4096565246582,
      "latency_p95_ms": 1019.4096565246582,
      "latency_p99_ms": 1019.4096565246582,
      "latency_max_ms": 1019.4096565246582,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 398.23198318481445,
      "latency_p95_ms": 398.23198318481445,
      "latency_p99_ms": 398.23198318481445,
      "latency_max_ms": 398.23198318481445,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 392.2145366668701,
      "latency_p95_ms": 392.2145366668701,
      "latency_p99_ms": 392.2145366668701,
      "latency_max_ms": 392.2145366668701,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 402.06027030944824,
      "latency_p95_ms": 402.06027030944824,
      "latency_p99_ms": 402.06027030944824,
      "latency_max_ms": 402.06027030944824,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 421.0820198059082,
      "latency_p95_ms": 421.0820198059082,
      "latency_p99_ms": 421.0820198059082,
      "latency_max_ms": 421.0820198059082,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 340.99340438842773,
      "latency_p95_ms": 340.99340438842773,
      "latency_p99_ms": 340.99340438842773,
      "latency_max_ms": 340.99340438842773,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 349.1802215576172,
      "latency_p95_ms": 349.1802215576172,
      "latency_p99_ms": 349.1802215576172,
      "latency_max_ms": 349.1802215576172,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 350.724458694458,
      "latency_p95_ms": 350.724458694458,
      "latency_p99_ms": 350.724458694458,
      "latency_max_ms": 350.724458694458,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 357.0683002471924,
      "latency_p95_ms": 357.0683002471924,
      "latency_p99_ms": 357.0683002471924,
      "latency_max_ms": 357.0683002471924,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1_1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 326.76124572753906,
      "latency_p95_ms": 326.76124572753906,
      "latency_p99_ms": 326.76124572753906,
      "latency_max_ms": 326.76124572753906,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1_1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 347.4395275115967,
      "latency_p95_ms": 347.4395275115967,
      "latency_p99_ms": 347.4395275115967,
      "latency_max_ms": 347.4395275115967,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1_1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 338.73939514160156,
      "latency_p95_ms": 338.73939514160156,
      "latency_p99_ms": 338.73939514160156,
      "latency_max_ms": 338.73939514160156,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1_1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 338.44661712646484,
      "latency_p95_ms": 338.44661712646484,
      "latency_p99_ms": 338.44661712646484,
      "latency_max_ms": 338.44661712646484,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    }
  ]
}
```