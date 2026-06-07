# PVR-EC Latency Stability Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-07T18:16:56.836609",
    "run_id": "algo_20260607_181030_benchmark-lite",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 123,
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
    "train_steps": 2000,
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
        2000
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
      "avg_loss": 0.2735070433603444,
      "avg_accuracy": 0.5057861131607642,
      "avg_train_loss": 0.020037148147821426,
      "latency_p50_ms": 973.1265902519226,
      "latency_p95_ms": 973.1265902519226,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1": {
      "count": 8,
      "avg_loss": 0.24154047189707245,
      "avg_accuracy": 0.8151431904364748,
      "avg_train_loss": 0.012056197039783001,
      "latency_p50_ms": 646.1461186408997,
      "latency_p95_ms": 646.1461186408997,
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
      "latency_p50_ms": 1039.0617847442627,
      "latency_p95_ms": 1039.0617847442627,
      "latency_p99_ms": 1039.0617847442627,
      "latency_max_ms": 1039.0617847442627,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1039.1204357147217,
      "latency_p95_ms": 1039.1204357147217,
      "latency_p99_ms": 1039.1204357147217,
      "latency_max_ms": 1039.1204357147217,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1037.0595455169678,
      "latency_p95_ms": 1037.0595455169678,
      "latency_p99_ms": 1037.0595455169678,
      "latency_max_ms": 1037.0595455169678,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1102.1971702575684,
      "latency_p95_ms": 1102.1971702575684,
      "latency_p99_ms": 1102.1971702575684,
      "latency_max_ms": 1102.1971702575684,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1094.5239067077637,
      "latency_p95_ms": 1094.5239067077637,
      "latency_p99_ms": 1094.5239067077637,
      "latency_max_ms": 1094.5239067077637,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 549.8776435852051,
      "latency_p95_ms": 549.8776435852051,
      "latency_p99_ms": 549.8776435852051,
      "latency_max_ms": 549.8776435852051,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1103.6906242370605,
      "latency_p95_ms": 1103.6906242370605,
      "latency_p99_ms": 1103.6906242370605,
      "latency_max_ms": 1103.6906242370605,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 819.481611251831,
      "latency_p95_ms": 819.481611251831,
      "latency_p99_ms": 819.481611251831,
      "latency_max_ms": 819.481611251831,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 694.1494941711426,
      "latency_p95_ms": 694.1494941711426,
      "latency_p99_ms": 694.1494941711426,
      "latency_max_ms": 694.1494941711426,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 690.5369758605957,
      "latency_p95_ms": 690.5369758605957,
      "latency_p99_ms": 690.5369758605957,
      "latency_max_ms": 690.5369758605957,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 691.7924880981445,
      "latency_p95_ms": 691.7924880981445,
      "latency_p99_ms": 691.7924880981445,
      "latency_max_ms": 691.7924880981445,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 751.4777183532715,
      "latency_p95_ms": 751.4777183532715,
      "latency_p99_ms": 751.4777183532715,
      "latency_max_ms": 751.4777183532715,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 727.2229194641113,
      "latency_p95_ms": 727.2229194641113,
      "latency_p99_ms": 727.2229194641113,
      "latency_max_ms": 727.2229194641113,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 359.6014976501465,
      "latency_p95_ms": 359.6014976501465,
      "latency_p99_ms": 359.6014976501465,
      "latency_max_ms": 359.6014976501465,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 719.4788455963135,
      "latency_p95_ms": 719.4788455963135,
      "latency_p99_ms": 719.4788455963135,
      "latency_max_ms": 719.4788455963135,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 534.9090099334717,
      "latency_p95_ms": 534.9090099334717,
      "latency_p99_ms": 534.9090099334717,
      "latency_max_ms": 534.9090099334717,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    }
  ]
}
```