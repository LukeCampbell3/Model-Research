# PVR-EC Latency Stability Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-08T03:29:20.212121",
    "run_id": "algo_20260608_032649_benchmark-lite",
    "git_commit": "c214633e8dfb56a3ba797333eee2da2c985b17cd",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 123,
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
        123
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
      "avg_loss": 0.5285098776221275,
      "avg_accuracy": 0.44133996997674885,
      "avg_train_loss": 0.15063753724098206,
      "latency_p50_ms": 1038.2141470909119,
      "latency_p95_ms": 1038.2141470909119,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_deploy_top1": {
      "count": 4,
      "avg_loss": 0.6203095002565533,
      "avg_accuracy": 0.10080544229999575,
      "avg_train_loss": 0.2083549052476883,
      "latency_p50_ms": 408.679723739624,
      "latency_p95_ms": 408.679723739624,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1": {
      "count": 4,
      "avg_loss": 0.5222164157312363,
      "avg_accuracy": 0.3845862868109708,
      "avg_train_loss": 0.1834246814250946,
      "latency_p50_ms": 343.98412704467773,
      "latency_p95_ms": 343.98412704467773,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1_1": {
      "count": 4,
      "avg_loss": 0.5364244075026363,
      "avg_accuracy": 0.3845862868109708,
      "avg_train_loss": 0.1834246814250946,
      "latency_p50_ms": 332.1107029914856,
      "latency_p95_ms": 332.1107029914856,
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
      "latency_p50_ms": 1106.987714767456,
      "latency_p95_ms": 1106.987714767456,
      "latency_p99_ms": 1106.987714767456,
      "latency_max_ms": 1106.987714767456,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1016.4623260498047,
      "latency_p95_ms": 1016.4623260498047,
      "latency_p99_ms": 1016.4623260498047,
      "latency_max_ms": 1016.4623260498047,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1013.7434005737305,
      "latency_p95_ms": 1013.7434005737305,
      "latency_p99_ms": 1013.7434005737305,
      "latency_max_ms": 1013.7434005737305,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1015.6631469726562,
      "latency_p95_ms": 1015.6631469726562,
      "latency_p99_ms": 1015.6631469726562,
      "latency_max_ms": 1015.6631469726562,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 401.644229888916,
      "latency_p95_ms": 401.644229888916,
      "latency_p99_ms": 401.644229888916,
      "latency_max_ms": 401.644229888916,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 399.932861328125,
      "latency_p95_ms": 399.932861328125,
      "latency_p99_ms": 399.932861328125,
      "latency_max_ms": 399.932861328125,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 416.6734218597412,
      "latency_p95_ms": 416.6734218597412,
      "latency_p99_ms": 416.6734218597412,
      "latency_max_ms": 416.6734218597412,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 416.46838188171387,
      "latency_p95_ms": 416.46838188171387,
      "latency_p99_ms": 416.46838188171387,
      "latency_max_ms": 416.46838188171387,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 338.49120140075684,
      "latency_p95_ms": 338.49120140075684,
      "latency_p99_ms": 338.49120140075684,
      "latency_max_ms": 338.49120140075684,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 342.03124046325684,
      "latency_p95_ms": 342.03124046325684,
      "latency_p99_ms": 342.03124046325684,
      "latency_max_ms": 342.03124046325684,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 337.66913414001465,
      "latency_p95_ms": 337.66913414001465,
      "latency_p99_ms": 337.66913414001465,
      "latency_max_ms": 337.66913414001465,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 357.7449321746826,
      "latency_p95_ms": 357.7449321746826,
      "latency_p99_ms": 357.7449321746826,
      "latency_max_ms": 357.7449321746826,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1_1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 325.8192539215088,
      "latency_p95_ms": 325.8192539215088,
      "latency_p99_ms": 325.8192539215088,
      "latency_max_ms": 325.8192539215088,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1_1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 330.2960395812988,
      "latency_p95_ms": 330.2960395812988,
      "latency_p99_ms": 330.2960395812988,
      "latency_max_ms": 330.2960395812988,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1_1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 328.3102512359619,
      "latency_p95_ms": 328.3102512359619,
      "latency_p99_ms": 328.3102512359619,
      "latency_max_ms": 328.3102512359619,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1_1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 344.01726722717285,
      "latency_p95_ms": 344.01726722717285,
      "latency_p99_ms": 344.01726722717285,
      "latency_max_ms": 344.01726722717285,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    }
  ]
}
```