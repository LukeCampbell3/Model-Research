# PVR-EC Latency Stability Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-07T17:43:21.166647",
    "run_id": "algo_20260607_174103_benchmark-lite",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 777,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode benchmark-lite --scale small --sample-limit 1000 --train-steps 500 --seed-list 42,123,777,2026,9001 --device cuda --amp --models fixed_moe_vectorized,pvr_ec_deploy_top1,pvr_ec_ownership_top1_final_candidate_v1 --enable-ownership-map --ownership-map-mode frozen --run-multiseed-confirmation-gate --output-dir evaluation/benchmark_results/pvr_final_multiseed_confirmation",
    "model_variants": [
      "fixed_moe_vectorized",
      "pvr_ec_deploy_top1",
      "pvr_ec_ownership_top1_final_candidate_v1"
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
    "pvr_expert_delta_scale_decay": null,
    "root_cause_flags": {
      "run_multiseed_confirmation_gate": true
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
      "max_train_seconds": null
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
      "count": 8,
      "avg_loss": 0.41424106022653484,
      "avg_accuracy": 0.15306213128950222,
      "avg_train_loss": 0.16213898360729218,
      "latency_p50_ms": 1051.8064200878143,
      "latency_p95_ms": 1051.8064200878143,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_deploy_top1": {
      "count": 8,
      "avg_loss": 0.4450599988146374,
      "avg_accuracy": 0.09719952415064355,
      "avg_train_loss": 0.18943354487419128,
      "latency_p50_ms": 718.6373472213745,
      "latency_p95_ms": 718.6373472213745,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1": {
      "count": 8,
      "avg_loss": 0.41956419885779417,
      "avg_accuracy": 0.2635769454047967,
      "avg_train_loss": 0.16685864329338074,
      "latency_p50_ms": 670.5679893493652,
      "latency_p95_ms": 670.5679893493652,
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
      "latency_p50_ms": 1118.8571453094482,
      "latency_p95_ms": 1118.8571453094482,
      "latency_p99_ms": 1118.8571453094482,
      "latency_max_ms": 1118.8571453094482,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1233.680009841919,
      "latency_p95_ms": 1233.680009841919,
      "latency_p99_ms": 1233.680009841919,
      "latency_max_ms": 1233.680009841919,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1239.3054962158203,
      "latency_p95_ms": 1239.3054962158203,
      "latency_p99_ms": 1239.3054962158203,
      "latency_max_ms": 1239.3054962158203,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1216.8715000152588,
      "latency_p95_ms": 1216.8715000152588,
      "latency_p99_ms": 1216.8715000152588,
      "latency_max_ms": 1216.8715000152588,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1080.4424285888672,
      "latency_p95_ms": 1080.4424285888672,
      "latency_p99_ms": 1080.4424285888672,
      "latency_max_ms": 1080.4424285888672,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 581.2623500823975,
      "latency_p95_ms": 581.2623500823975,
      "latency_p99_ms": 581.2623500823975,
      "latency_max_ms": 581.2623500823975,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1131.4072608947754,
      "latency_p95_ms": 1131.4072608947754,
      "latency_p99_ms": 1131.4072608947754,
      "latency_max_ms": 1131.4072608947754,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 812.6251697540283,
      "latency_p95_ms": 812.6251697540283,
      "latency_p99_ms": 812.6251697540283,
      "latency_max_ms": 812.6251697540283,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 790.3625965118408,
      "latency_p95_ms": 790.3625965118408,
      "latency_p99_ms": 790.3625965118408,
      "latency_max_ms": 790.3625965118408,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 780.3595066070557,
      "latency_p95_ms": 780.3595066070557,
      "latency_p99_ms": 780.3595066070557,
      "latency_max_ms": 780.3595066070557,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 799.1416454315186,
      "latency_p95_ms": 799.1416454315186,
      "latency_p99_ms": 799.1416454315186,
      "latency_max_ms": 799.1416454315186,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 814.8925304412842,
      "latency_p95_ms": 814.8925304412842,
      "latency_p99_ms": 814.8925304412842,
      "latency_max_ms": 814.8925304412842,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 794.6410179138184,
      "latency_p95_ms": 794.6410179138184,
      "latency_p99_ms": 794.6410179138184,
      "latency_max_ms": 794.6410179138184,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 396.4974880218506,
      "latency_p95_ms": 396.4974880218506,
      "latency_p99_ms": 396.4974880218506,
      "latency_max_ms": 396.4974880218506,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 779.059648513794,
      "latency_p95_ms": 779.059648513794,
      "latency_p99_ms": 779.059648513794,
      "latency_max_ms": 779.059648513794,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 594.144344329834,
      "latency_p95_ms": 594.144344329834,
      "latency_p99_ms": 594.144344329834,
      "latency_max_ms": 594.144344329834,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 697.2510814666748,
      "latency_p95_ms": 697.2510814666748,
      "latency_p99_ms": 697.2510814666748,
      "latency_max_ms": 697.2510814666748,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 711.4996910095215,
      "latency_p95_ms": 711.4996910095215,
      "latency_p99_ms": 711.4996910095215,
      "latency_max_ms": 711.4996910095215,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 802.9277324676514,
      "latency_p95_ms": 802.9277324676514,
      "latency_p99_ms": 802.9277324676514,
      "latency_max_ms": 802.9277324676514,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 810.2798461914062,
      "latency_p95_ms": 810.2798461914062,
      "latency_p99_ms": 810.2798461914062,
      "latency_max_ms": 810.2798461914062,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 748.011589050293,
      "latency_p95_ms": 748.011589050293,
      "latency_p99_ms": 748.011589050293,
      "latency_max_ms": 748.011589050293,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 389.2333507537842,
      "latency_p95_ms": 389.2333507537842,
      "latency_p99_ms": 389.2333507537842,
      "latency_max_ms": 389.2333507537842,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 678.0362129211426,
      "latency_p95_ms": 678.0362129211426,
      "latency_p99_ms": 678.0362129211426,
      "latency_max_ms": 678.0362129211426,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 527.3044109344482,
      "latency_p95_ms": 527.3044109344482,
      "latency_p99_ms": 527.3044109344482,
      "latency_max_ms": 527.3044109344482,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    }
  ]
}
```