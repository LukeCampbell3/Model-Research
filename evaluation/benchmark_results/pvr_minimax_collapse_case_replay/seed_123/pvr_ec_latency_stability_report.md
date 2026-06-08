# PVR-EC Latency Stability Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-07T23:42:05.698447",
    "run_id": "algo_20260607_233951_benchmark-lite",
    "git_commit": "51e443da02bdc0a13c33b86368b863343ae036a2",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 123,
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
      "latency_p50_ms": 907.1608185768127,
      "latency_p95_ms": 907.1608185768127,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_deploy_top1": {
      "count": 4,
      "avg_loss": 0.6203095002565533,
      "avg_accuracy": 0.10080544229999575,
      "avg_train_loss": 0.2083549052476883,
      "latency_p50_ms": 361.2043261528015,
      "latency_p95_ms": 361.2043261528015,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1": {
      "count": 4,
      "avg_loss": 0.5222164157312363,
      "avg_accuracy": 0.3845862868109708,
      "avg_train_loss": 0.1834246814250946,
      "latency_p50_ms": 303.6370873451233,
      "latency_p95_ms": 303.6370873451233,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1_1": {
      "count": 4,
      "avg_loss": 0.5364244075026363,
      "avg_accuracy": 0.3845862868109708,
      "avg_train_loss": 0.1834246814250946,
      "latency_p50_ms": 295.3875660896301,
      "latency_p95_ms": 295.3875660896301,
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
      "latency_p50_ms": 976.2020111083984,
      "latency_p95_ms": 976.2020111083984,
      "latency_p99_ms": 976.2020111083984,
      "latency_max_ms": 976.2020111083984,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 880.713701248169,
      "latency_p95_ms": 880.713701248169,
      "latency_p99_ms": 880.713701248169,
      "latency_max_ms": 880.713701248169,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 881.1056613922119,
      "latency_p95_ms": 881.1056613922119,
      "latency_p99_ms": 881.1056613922119,
      "latency_max_ms": 881.1056613922119,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 890.6219005584717,
      "latency_p95_ms": 890.6219005584717,
      "latency_p99_ms": 890.6219005584717,
      "latency_max_ms": 890.6219005584717,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 352.99158096313477,
      "latency_p95_ms": 352.99158096313477,
      "latency_p99_ms": 352.99158096313477,
      "latency_max_ms": 352.99158096313477,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 358.5638999938965,
      "latency_p95_ms": 358.5638999938965,
      "latency_p99_ms": 358.5638999938965,
      "latency_max_ms": 358.5638999938965,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 366.44554138183594,
      "latency_p95_ms": 366.44554138183594,
      "latency_p99_ms": 366.44554138183594,
      "latency_max_ms": 366.44554138183594,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 366.81628227233887,
      "latency_p95_ms": 366.81628227233887,
      "latency_p99_ms": 366.81628227233887,
      "latency_max_ms": 366.81628227233887,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 295.8700656890869,
      "latency_p95_ms": 295.8700656890869,
      "latency_p99_ms": 295.8700656890869,
      "latency_max_ms": 295.8700656890869,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 302.49905586242676,
      "latency_p95_ms": 302.49905586242676,
      "latency_p99_ms": 302.49905586242676,
      "latency_max_ms": 302.49905586242676,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 296.459436416626,
      "latency_p95_ms": 296.459436416626,
      "latency_p99_ms": 296.459436416626,
      "latency_max_ms": 296.459436416626,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 319.7197914123535,
      "latency_p95_ms": 319.7197914123535,
      "latency_p99_ms": 319.7197914123535,
      "latency_max_ms": 319.7197914123535,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1_1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 285.311222076416,
      "latency_p95_ms": 285.311222076416,
      "latency_p99_ms": 285.311222076416,
      "latency_max_ms": 285.311222076416,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1_1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 296.13304138183594,
      "latency_p95_ms": 296.13304138183594,
      "latency_p99_ms": 296.13304138183594,
      "latency_max_ms": 296.13304138183594,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1_1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 290.0350093841553,
      "latency_p95_ms": 290.0350093841553,
      "latency_p99_ms": 290.0350093841553,
      "latency_max_ms": 290.0350093841553,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1_1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 310.0709915161133,
      "latency_p95_ms": 310.0709915161133,
      "latency_p99_ms": 310.0709915161133,
      "latency_max_ms": 310.0709915161133,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    }
  ]
}
```