# PVR-EC Latency Stability Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-07T18:04:30.101763",
    "run_id": "algo_20260607_180124_benchmark-lite",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 777,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode benchmark-lite --scale small --sample-limit 1000 --train-steps-list 500,1000,2000 --seed-list 42,123,777 --device cuda --amp --models fixed_moe_vectorized,pvr_ec_ownership_top1_final_candidate_v1 --enable-ownership-map --ownership-map-mode frozen --run-longer-training-confirmation-gate --output-dir evaluation/benchmark_results/pvr_final_longer_training_confirmation",
    "model_variants": [
      "fixed_moe_vectorized",
      "pvr_ec_ownership_top1_final_candidate_v1"
    ],
    "batch_sizes": [
      1,
      32
    ],
    "sequence_lengths": [
      64
    ],
    "train_steps": 1000,
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
      "run_longer_training_confirmation_gate": true
    },
    "diagnostic_sweeps": {
      "train_steps_list": [
        1000
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
      "avg_loss": 0.32257950779361033,
      "avg_accuracy": 0.4160115638386701,
      "avg_train_loss": 0.04234958812594414,
      "latency_p50_ms": 913.2477939128876,
      "latency_p95_ms": 913.2477939128876,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1": {
      "count": 8,
      "avg_loss": 0.31974026510336745,
      "avg_accuracy": 0.5304247336716077,
      "avg_train_loss": 0.039028894156217575,
      "latency_p50_ms": 601.3778746128082,
      "latency_p95_ms": 601.3778746128082,
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
      "latency_p50_ms": 1012.1364593505859,
      "latency_p95_ms": 1012.1364593505859,
      "latency_p99_ms": 1012.1364593505859,
      "latency_max_ms": 1012.1364593505859,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 995.5844879150391,
      "latency_p95_ms": 995.5844879150391,
      "latency_p99_ms": 995.5844879150391,
      "latency_max_ms": 995.5844879150391,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1006.1678886413574,
      "latency_p95_ms": 1006.1678886413574,
      "latency_p99_ms": 1006.1678886413574,
      "latency_max_ms": 1006.1678886413574,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1011.744499206543,
      "latency_p95_ms": 1011.744499206543,
      "latency_p99_ms": 1011.744499206543,
      "latency_max_ms": 1011.744499206543,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1009.7665786743164,
      "latency_p95_ms": 1009.7665786743164,
      "latency_p99_ms": 1009.7665786743164,
      "latency_max_ms": 1009.7665786743164,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 500.66637992858887,
      "latency_p95_ms": 500.66637992858887,
      "latency_p99_ms": 500.66637992858887,
      "latency_max_ms": 500.66637992858887,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1009.2337131500244,
      "latency_p95_ms": 1009.2337131500244,
      "latency_p99_ms": 1009.2337131500244,
      "latency_max_ms": 1009.2337131500244,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 760.6823444366455,
      "latency_p95_ms": 760.6823444366455,
      "latency_p99_ms": 760.6823444366455,
      "latency_max_ms": 760.6823444366455,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 650.1412391662598,
      "latency_p95_ms": 650.1412391662598,
      "latency_p99_ms": 650.1412391662598,
      "latency_max_ms": 650.1412391662598,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 638.904333114624,
      "latency_p95_ms": 638.904333114624,
      "latency_p99_ms": 638.904333114624,
      "latency_max_ms": 638.904333114624,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 671.2205410003662,
      "latency_p95_ms": 671.2205410003662,
      "latency_p99_ms": 671.2205410003662,
      "latency_max_ms": 671.2205410003662,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 698.5163688659668,
      "latency_p95_ms": 698.5163688659668,
      "latency_p99_ms": 698.5163688659668,
      "latency_max_ms": 698.5163688659668,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 664.9665832519531,
      "latency_p95_ms": 664.9665832519531,
      "latency_p99_ms": 664.9665832519531,
      "latency_max_ms": 664.9665832519531,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 335.58130264282227,
      "latency_p95_ms": 335.58130264282227,
      "latency_p99_ms": 335.58130264282227,
      "latency_max_ms": 335.58130264282227,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 668.1263446807861,
      "latency_p95_ms": 668.1263446807861,
      "latency_p99_ms": 668.1263446807861,
      "latency_max_ms": 668.1263446807861,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 483.5662841796875,
      "latency_p95_ms": 483.5662841796875,
      "latency_p99_ms": 483.5662841796875,
      "latency_max_ms": 483.5662841796875,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    }
  ]
}
```