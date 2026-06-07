# PVR-EC Latency Stability Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-07T20:08:01.397829",
    "run_id": "algo_20260607_200559_benchmark-lite",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 42,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode benchmark-lite --scale small --sample-limit 1000 --train-steps 500 --seed-list 42,123,777,2026,9001 --device cuda --amp --models fixed_moe_vectorized,pvr_ec_deploy_top1,pvr_ec_ownership_top1_final_candidate_v1_1 --enable-ownership-map --ownership-map-mode frozen --run-final-candidate-revalidation --output-dir evaluation/benchmark_results/pvr_final_candidate_v1_1_revalidation",
    "model_variants": [
      "fixed_moe_vectorized",
      "pvr_ec_deploy_top1",
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
        42
      ],
      "batch_size_list": [
        1,
        32
      ],
      "seq_len_list": [
        64
      ],
      "max_train_seconds": null,
      "repeatability_repair_variants": [],
      "calibration_repair_variants": []
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
      "avg_loss": 0.3886076922838887,
      "avg_accuracy": 0.25857819999606313,
      "avg_train_loss": 0.13683609664440155,
      "latency_p50_ms": 827.7164399623871,
      "latency_p95_ms": 827.7164399623871,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_deploy_top1": {
      "count": 8,
      "avg_loss": 0.45097945421002805,
      "avg_accuracy": 0.0771500010285979,
      "avg_train_loss": 0.17677822709083557,
      "latency_p50_ms": 579.0242552757263,
      "latency_p95_ms": 579.0242552757263,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1_1": {
      "count": 8,
      "avg_loss": 0.41567398770712316,
      "avg_accuracy": 0.24662427509545803,
      "avg_train_loss": 0.1481063961982727,
      "latency_p50_ms": 490.47744274139404,
      "latency_p95_ms": 490.47744274139404,
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
      "latency_p50_ms": 977.7674674987793,
      "latency_p95_ms": 977.7674674987793,
      "latency_p99_ms": 977.7674674987793,
      "latency_max_ms": 977.7674674987793,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 897.4781036376953,
      "latency_p95_ms": 897.4781036376953,
      "latency_p99_ms": 897.4781036376953,
      "latency_max_ms": 897.4781036376953,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 905.7197570800781,
      "latency_p95_ms": 905.7197570800781,
      "latency_p99_ms": 905.7197570800781,
      "latency_max_ms": 905.7197570800781,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 904.5009613037109,
      "latency_p95_ms": 904.5009613037109,
      "latency_p99_ms": 904.5009613037109,
      "latency_max_ms": 904.5009613037109,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 903.6381244659424,
      "latency_p95_ms": 903.6381244659424,
      "latency_p99_ms": 903.6381244659424,
      "latency_max_ms": 903.6381244659424,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 453.1245231628418,
      "latency_p95_ms": 453.1245231628418,
      "latency_p99_ms": 453.1245231628418,
      "latency_max_ms": 453.1245231628418,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 901.3166427612305,
      "latency_p95_ms": 901.3166427612305,
      "latency_p99_ms": 901.3166427612305,
      "latency_max_ms": 901.3166427612305,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 678.1859397888184,
      "latency_p95_ms": 678.1859397888184,
      "latency_p99_ms": 678.1859397888184,
      "latency_max_ms": 678.1859397888184,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 633.9921951293945,
      "latency_p95_ms": 633.9921951293945,
      "latency_p99_ms": 633.9921951293945,
      "latency_max_ms": 633.9921951293945,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 638.5917663574219,
      "latency_p95_ms": 638.5917663574219,
      "latency_p99_ms": 638.5917663574219,
      "latency_max_ms": 638.5917663574219,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 649.038553237915,
      "latency_p95_ms": 649.038553237915,
      "latency_p99_ms": 649.038553237915,
      "latency_max_ms": 649.038553237915,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 664.3290519714355,
      "latency_p95_ms": 664.3290519714355,
      "latency_p99_ms": 664.3290519714355,
      "latency_max_ms": 664.3290519714355,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 630.3811073303223,
      "latency_p95_ms": 630.3811073303223,
      "latency_p99_ms": 630.3811073303223,
      "latency_max_ms": 630.3811073303223,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 316.2119388580322,
      "latency_p95_ms": 316.2119388580322,
      "latency_p99_ms": 316.2119388580322,
      "latency_max_ms": 316.2119388580322,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 625.3931522369385,
      "latency_p95_ms": 625.3931522369385,
      "latency_p99_ms": 625.3931522369385,
      "latency_max_ms": 625.3931522369385,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 474.2562770843506,
      "latency_p95_ms": 474.2562770843506,
      "latency_p99_ms": 474.2562770843506,
      "latency_max_ms": 474.2562770843506,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1_1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 542.1316623687744,
      "latency_p95_ms": 542.1316623687744,
      "latency_p99_ms": 542.1316623687744,
      "latency_max_ms": 542.1316623687744,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1_1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 556.6871166229248,
      "latency_p95_ms": 556.6871166229248,
      "latency_p99_ms": 556.6871166229248,
      "latency_max_ms": 556.6871166229248,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1_1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 542.3798561096191,
      "latency_p95_ms": 542.3798561096191,
      "latency_p99_ms": 542.3798561096191,
      "latency_max_ms": 542.3798561096191,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1_1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 558.9931011199951,
      "latency_p95_ms": 558.9931011199951,
      "latency_p99_ms": 558.9931011199951,
      "latency_max_ms": 558.9931011199951,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1_1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 529.7949314117432,
      "latency_p95_ms": 529.7949314117432,
      "latency_p99_ms": 529.7949314117432,
      "latency_max_ms": 529.7949314117432,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1_1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 266.3261890411377,
      "latency_p95_ms": 266.3261890411377,
      "latency_p99_ms": 266.3261890411377,
      "latency_max_ms": 266.3261890411377,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1_1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 529.2301177978516,
      "latency_p95_ms": 529.2301177978516,
      "latency_p99_ms": 529.2301177978516,
      "latency_max_ms": 529.2301177978516,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1_1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 398.27656745910645,
      "latency_p95_ms": 398.27656745910645,
      "latency_p99_ms": 398.27656745910645,
      "latency_max_ms": 398.27656745910645,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    }
  ]
}
```