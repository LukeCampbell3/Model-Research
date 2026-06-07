# PVR-EC Latency Stability Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-07T17:56:53.391144",
    "run_id": "algo_20260607_175345_benchmark-lite",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 42,
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
        42
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
      "avg_loss": 0.30550391164918744,
      "avg_accuracy": 0.4564627978615968,
      "avg_train_loss": 0.034878071397542953,
      "latency_p50_ms": 925.4638254642487,
      "latency_p95_ms": 925.4638254642487,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1": {
      "count": 8,
      "avg_loss": 0.30325903320529807,
      "avg_accuracy": 0.5188236464649867,
      "avg_train_loss": 0.027974294498562813,
      "latency_p50_ms": 672.7344989776611,
      "latency_p95_ms": 672.7344989776611,
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
      "latency_p50_ms": 1004.5101642608643,
      "latency_p95_ms": 1004.5101642608643,
      "latency_p99_ms": 1004.5101642608643,
      "latency_max_ms": 1004.5101642608643,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 980.9582233428955,
      "latency_p95_ms": 980.9582233428955,
      "latency_p99_ms": 980.9582233428955,
      "latency_max_ms": 980.9582233428955,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1006.9015026092529,
      "latency_p95_ms": 1006.9015026092529,
      "latency_p99_ms": 1006.9015026092529,
      "latency_max_ms": 1006.9015026092529,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1040.0280952453613,
      "latency_p95_ms": 1040.0280952453613,
      "latency_p99_ms": 1040.0280952453613,
      "latency_max_ms": 1040.0280952453613,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1041.1295890808105,
      "latency_p95_ms": 1041.1295890808105,
      "latency_p99_ms": 1041.1295890808105,
      "latency_max_ms": 1041.1295890808105,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 516.0584449768066,
      "latency_p95_ms": 516.0584449768066,
      "latency_p99_ms": 516.0584449768066,
      "latency_max_ms": 516.0584449768066,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1028.3524990081787,
      "latency_p95_ms": 1028.3524990081787,
      "latency_p99_ms": 1028.3524990081787,
      "latency_max_ms": 1028.3524990081787,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 785.7720851898193,
      "latency_p95_ms": 785.7720851898193,
      "latency_p99_ms": 785.7720851898193,
      "latency_max_ms": 785.7720851898193,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 689.3761157989502,
      "latency_p95_ms": 689.3761157989502,
      "latency_p99_ms": 689.3761157989502,
      "latency_max_ms": 689.3761157989502,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 685.4476928710938,
      "latency_p95_ms": 685.4476928710938,
      "latency_p99_ms": 685.4476928710938,
      "latency_max_ms": 685.4476928710938,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 717.1094417572021,
      "latency_p95_ms": 717.1094417572021,
      "latency_p99_ms": 717.1094417572021,
      "latency_max_ms": 717.1094417572021,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 884.5248222351074,
      "latency_p95_ms": 884.5248222351074,
      "latency_p99_ms": 884.5248222351074,
      "latency_max_ms": 884.5248222351074,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 798.954963684082,
      "latency_p95_ms": 798.954963684082,
      "latency_p99_ms": 798.954963684082,
      "latency_max_ms": 798.954963684082,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 354.3581962585449,
      "latency_p95_ms": 354.3581962585449,
      "latency_p99_ms": 354.3581962585449,
      "latency_max_ms": 354.3581962585449,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 703.7441730499268,
      "latency_p95_ms": 703.7441730499268,
      "latency_p99_ms": 703.7441730499268,
      "latency_max_ms": 703.7441730499268,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 548.3605861663818,
      "latency_p95_ms": 548.3605861663818,
      "latency_p99_ms": 548.3605861663818,
      "latency_max_ms": 548.3605861663818,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    }
  ]
}
```