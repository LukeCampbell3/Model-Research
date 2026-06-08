# PVR-EC Latency Stability Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-07T23:44:16.858525",
    "run_id": "algo_20260607_234206_benchmark-lite",
    "git_commit": "51e443da02bdc0a13c33b86368b863343ae036a2",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 777,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode benchmark-lite --scale small --sample-limit 1000 --train-steps 500 --seed-list 123,777 --families clrs_style,listops --device cuda --amp --models fixed_moe_vectorized,pvr_ec_deploy_top1,pvr_ec_ownership_top1_final_candidate_v1,pvr_ec_ownership_top1_final_candidate_v1_1 --enable-ownership-map --ownership-map-mode frozen --run-collapse-case-replay --output-dir evaluation/benchmark_results/pvr_minimax_collapse_case_replay",
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
      "latency_p50_ms": 880.5426955223083,
      "latency_p95_ms": 880.5426955223083,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_deploy_top1": {
      "count": 4,
      "avg_loss": 0.5899287902284414,
      "avg_accuracy": 0.16611370851563104,
      "avg_train_loss": 0.18943354487419128,
      "latency_p50_ms": 352.79935598373413,
      "latency_p95_ms": 352.79935598373413,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1": {
      "count": 4,
      "avg_loss": 0.5544045781716704,
      "avg_accuracy": 0.41903433213089625,
      "avg_train_loss": 0.16685862839221954,
      "latency_p50_ms": 305.3699731826782,
      "latency_p95_ms": 305.3699731826782,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1_1": {
      "count": 4,
      "avg_loss": 0.5711596482433379,
      "avg_accuracy": 0.41903433213089625,
      "avg_train_loss": 0.16685862839221954,
      "latency_p50_ms": 300.2287745475769,
      "latency_p95_ms": 300.2287745475769,
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
      "latency_p50_ms": 881.7410469055176,
      "latency_p95_ms": 881.7410469055176,
      "latency_p99_ms": 881.7410469055176,
      "latency_max_ms": 881.7410469055176,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 865.1633262634277,
      "latency_p95_ms": 865.1633262634277,
      "latency_p99_ms": 865.1633262634277,
      "latency_max_ms": 865.1633262634277,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 881.0782432556152,
      "latency_p95_ms": 881.0782432556152,
      "latency_p99_ms": 881.0782432556152,
      "latency_max_ms": 881.0782432556152,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 894.1881656646729,
      "latency_p95_ms": 894.1881656646729,
      "latency_p99_ms": 894.1881656646729,
      "latency_max_ms": 894.1881656646729,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 347.6855754852295,
      "latency_p95_ms": 347.6855754852295,
      "latency_p99_ms": 347.6855754852295,
      "latency_max_ms": 347.6855754852295,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 339.31875228881836,
      "latency_p95_ms": 339.31875228881836,
      "latency_p99_ms": 339.31875228881836,
      "latency_max_ms": 339.31875228881836,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 354.5677661895752,
      "latency_p95_ms": 354.5677661895752,
      "latency_p99_ms": 354.5677661895752,
      "latency_max_ms": 354.5677661895752,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 369.6253299713135,
      "latency_p95_ms": 369.6253299713135,
      "latency_p99_ms": 369.6253299713135,
      "latency_max_ms": 369.6253299713135,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 299.82924461364746,
      "latency_p95_ms": 299.82924461364746,
      "latency_p99_ms": 299.82924461364746,
      "latency_max_ms": 299.82924461364746,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 306.6399097442627,
      "latency_p95_ms": 306.6399097442627,
      "latency_p99_ms": 306.6399097442627,
      "latency_max_ms": 306.6399097442627,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 305.217981338501,
      "latency_p95_ms": 305.217981338501,
      "latency_p99_ms": 305.217981338501,
      "latency_max_ms": 305.217981338501,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 309.79275703430176,
      "latency_p95_ms": 309.79275703430176,
      "latency_p99_ms": 309.79275703430176,
      "latency_max_ms": 309.79275703430176,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1_1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 291.1665439605713,
      "latency_p95_ms": 291.1665439605713,
      "latency_p99_ms": 291.1665439605713,
      "latency_max_ms": 291.1665439605713,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1_1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 300.9157180786133,
      "latency_p95_ms": 300.9157180786133,
      "latency_p99_ms": 300.9157180786133,
      "latency_max_ms": 300.9157180786133,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1_1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 304.2318820953369,
      "latency_p95_ms": 304.2318820953369,
      "latency_p99_ms": 304.2318820953369,
      "latency_max_ms": 304.2318820953369,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1_1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 304.60095405578613,
      "latency_p95_ms": 304.60095405578613,
      "latency_p99_ms": 304.60095405578613,
      "latency_max_ms": 304.60095405578613,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    }
  ]
}
```