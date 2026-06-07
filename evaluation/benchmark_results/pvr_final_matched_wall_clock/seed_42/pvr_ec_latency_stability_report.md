# PVR-EC Latency Stability Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-07T18:25:52.779118",
    "run_id": "algo_20260607_182334_benchmark-lite",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 42,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode benchmark-lite --scale small --sample-limit 1000 --max-train-seconds 120 --seed-list 42,123,777 --device cuda --amp --models fixed_moe_vectorized,pvr_ec_deploy_top1,pvr_ec_ownership_top1_final_candidate_v1 --enable-ownership-map --ownership-map-mode frozen --run-matched-wall-clock-gate --output-dir evaluation/benchmark_results/pvr_final_matched_wall_clock",
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
      "run_matched_wall_clock_gate": true
    },
    "diagnostic_sweeps": {
      "train_steps_list": [
        500
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
      "max_train_seconds": 120.0
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
      "avg_loss": 0.38860771482965595,
      "avg_accuracy": 0.2585774652971577,
      "avg_train_loss": 0.13683576881885529,
      "latency_p50_ms": 957.6640129089355,
      "latency_p95_ms": 957.6640129089355,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_deploy_top1": {
      "count": 8,
      "avg_loss": 0.45097945421002805,
      "avg_accuracy": 0.0771500010285979,
      "avg_train_loss": 0.17677822709083557,
      "latency_p50_ms": 649.6281921863556,
      "latency_p95_ms": 649.6281921863556,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1": {
      "count": 8,
      "avg_loss": 0.39578524367728585,
      "avg_accuracy": 0.24662427509545803,
      "avg_train_loss": 0.1481063961982727,
      "latency_p50_ms": 581.1775922775269,
      "latency_p95_ms": 581.1775922775269,
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
      "latency_p50_ms": 1120.1388835906982,
      "latency_p95_ms": 1120.1388835906982,
      "latency_p99_ms": 1120.1388835906982,
      "latency_max_ms": 1120.1388835906982,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1039.2448902130127,
      "latency_p95_ms": 1039.2448902130127,
      "latency_p99_ms": 1039.2448902130127,
      "latency_max_ms": 1039.2448902130127,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1042.2964096069336,
      "latency_p95_ms": 1042.2964096069336,
      "latency_p99_ms": 1042.2964096069336,
      "latency_max_ms": 1042.2964096069336,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1052.2215366363525,
      "latency_p95_ms": 1052.2215366363525,
      "latency_p99_ms": 1052.2215366363525,
      "latency_max_ms": 1052.2215366363525,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1051.6927242279053,
      "latency_p95_ms": 1051.6927242279053,
      "latency_p99_ms": 1051.6927242279053,
      "latency_max_ms": 1051.6927242279053,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 523.92578125,
      "latency_p95_ms": 523.92578125,
      "latency_p99_ms": 523.92578125,
      "latency_max_ms": 523.92578125,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1044.8765754699707,
      "latency_p95_ms": 1044.8765754699707,
      "latency_p99_ms": 1044.8765754699707,
      "latency_max_ms": 1044.8765754699707,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 786.9153022766113,
      "latency_p95_ms": 786.9153022766113,
      "latency_p99_ms": 786.9153022766113,
      "latency_max_ms": 786.9153022766113,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 720.9062576293945,
      "latency_p95_ms": 720.9062576293945,
      "latency_p99_ms": 720.9062576293945,
      "latency_max_ms": 720.9062576293945,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 718.1699275970459,
      "latency_p95_ms": 718.1699275970459,
      "latency_p99_ms": 718.1699275970459,
      "latency_max_ms": 718.1699275970459,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 741.9366836547852,
      "latency_p95_ms": 741.9366836547852,
      "latency_p99_ms": 741.9366836547852,
      "latency_max_ms": 741.9366836547852,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 746.7892169952393,
      "latency_p95_ms": 746.7892169952393,
      "latency_p99_ms": 746.7892169952393,
      "latency_max_ms": 746.7892169952393,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 704.1115760803223,
      "latency_p95_ms": 704.1115760803223,
      "latency_p99_ms": 704.1115760803223,
      "latency_max_ms": 704.1115760803223,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 353.8942337036133,
      "latency_p95_ms": 353.8942337036133,
      "latency_p99_ms": 353.8942337036133,
      "latency_max_ms": 353.8942337036133,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 692.5480365753174,
      "latency_p95_ms": 692.5480365753174,
      "latency_p99_ms": 692.5480365753174,
      "latency_max_ms": 692.5480365753174,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 518.669605255127,
      "latency_p95_ms": 518.669605255127,
      "latency_p99_ms": 518.669605255127,
      "latency_max_ms": 518.669605255127,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 647.5872993469238,
      "latency_p95_ms": 647.5872993469238,
      "latency_p99_ms": 647.5872993469238,
      "latency_max_ms": 647.5872993469238,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 638.9927864074707,
      "latency_p95_ms": 638.9927864074707,
      "latency_p99_ms": 638.9927864074707,
      "latency_max_ms": 638.9927864074707,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 641.7160034179688,
      "latency_p95_ms": 641.7160034179688,
      "latency_p99_ms": 641.7160034179688,
      "latency_max_ms": 641.7160034179688,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 668.3261394500732,
      "latency_p95_ms": 668.3261394500732,
      "latency_p99_ms": 668.3261394500732,
      "latency_max_ms": 668.3261394500732,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 630.0351619720459,
      "latency_p95_ms": 630.0351619720459,
      "latency_p99_ms": 630.0351619720459,
      "latency_max_ms": 630.0351619720459,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 321.7029571533203,
      "latency_p95_ms": 321.7029571533203,
      "latency_p99_ms": 321.7029571533203,
      "latency_max_ms": 321.7029571533203,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 625.9016990661621,
      "latency_p95_ms": 625.9016990661621,
      "latency_p99_ms": 625.9016990661621,
      "latency_max_ms": 625.9016990661621,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 475.15869140625,
      "latency_p95_ms": 475.15869140625,
      "latency_p99_ms": 475.15869140625,
      "latency_max_ms": 475.15869140625,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    }
  ]
}
```