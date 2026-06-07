# PVR-EC Latency Stability Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-07T18:01:24.148585",
    "run_id": "algo_20260607_175654_benchmark-lite",
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
      "avg_loss": 0.33208357432158664,
      "avg_accuracy": 0.3969976342147131,
      "avg_train_loss": 0.03698534891009331,
      "latency_p50_ms": 911.1579358577728,
      "latency_p95_ms": 911.1579358577728,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1": {
      "count": 8,
      "avg_loss": 0.3172225089510903,
      "avg_accuracy": 0.4869787673654481,
      "avg_train_loss": 0.04325160011649132,
      "latency_p50_ms": 635.3747248649597,
      "latency_p95_ms": 635.3747248649597,
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
      "latency_p50_ms": 980.785608291626,
      "latency_p95_ms": 980.785608291626,
      "latency_p99_ms": 980.785608291626,
      "latency_max_ms": 980.785608291626,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1005.3708553314209,
      "latency_p95_ms": 1005.3708553314209,
      "latency_p99_ms": 1005.3708553314209,
      "latency_max_ms": 1005.3708553314209,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 995.2311515808105,
      "latency_p95_ms": 995.2311515808105,
      "latency_p99_ms": 995.2311515808105,
      "latency_max_ms": 995.2311515808105,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1016.0081386566162,
      "latency_p95_ms": 1016.0081386566162,
      "latency_p99_ms": 1016.0081386566162,
      "latency_max_ms": 1016.0081386566162,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1019.6759700775146,
      "latency_p95_ms": 1019.6759700775146,
      "latency_p99_ms": 1019.6759700775146,
      "latency_max_ms": 1019.6759700775146,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 509.60326194763184,
      "latency_p95_ms": 509.60326194763184,
      "latency_p99_ms": 509.60326194763184,
      "latency_max_ms": 509.60326194763184,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1011.0635757446289,
      "latency_p95_ms": 1011.0635757446289,
      "latency_p99_ms": 1011.0635757446289,
      "latency_max_ms": 1011.0635757446289,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 751.5249252319336,
      "latency_p95_ms": 751.5249252319336,
      "latency_p99_ms": 751.5249252319336,
      "latency_max_ms": 751.5249252319336,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 690.6907558441162,
      "latency_p95_ms": 690.6907558441162,
      "latency_p99_ms": 690.6907558441162,
      "latency_max_ms": 690.6907558441162,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 693.709135055542,
      "latency_p95_ms": 693.709135055542,
      "latency_p99_ms": 693.709135055542,
      "latency_max_ms": 693.709135055542,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 709.1360092163086,
      "latency_p95_ms": 709.1360092163086,
      "latency_p99_ms": 709.1360092163086,
      "latency_max_ms": 709.1360092163086,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 760.3967189788818,
      "latency_p95_ms": 760.3967189788818,
      "latency_p99_ms": 760.3967189788818,
      "latency_max_ms": 760.3967189788818,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 686.9597434997559,
      "latency_p95_ms": 686.9597434997559,
      "latency_p99_ms": 686.9597434997559,
      "latency_max_ms": 686.9597434997559,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 342.51976013183594,
      "latency_p95_ms": 342.51976013183594,
      "latency_p99_ms": 342.51976013183594,
      "latency_max_ms": 342.51976013183594,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 678.9400577545166,
      "latency_p95_ms": 678.9400577545166,
      "latency_p99_ms": 678.9400577545166,
      "latency_max_ms": 678.9400577545166,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 520.6456184387207,
      "latency_p95_ms": 520.6456184387207,
      "latency_p99_ms": 520.6456184387207,
      "latency_max_ms": 520.6456184387207,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    }
  ]
}
```