# PVR-EC Latency Stability Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-07T17:38:44.362454",
    "run_id": "algo_20260607_173440_benchmark-lite",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 42,
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
      "avg_loss": 0.38858587376307696,
      "avg_accuracy": 0.25867859962716827,
      "avg_train_loss": 0.13682051002979279,
      "latency_p50_ms": 984.0191900730133,
      "latency_p95_ms": 984.0191900730133,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_deploy_top1": {
      "count": 8,
      "avg_loss": 0.45097945421002805,
      "avg_accuracy": 0.0771500010285979,
      "avg_train_loss": 0.17677822709083557,
      "latency_p50_ms": 699.1321444511414,
      "latency_p95_ms": 699.1321444511414,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1": {
      "count": 8,
      "avg_loss": 0.39578524367728585,
      "avg_accuracy": 0.24662427509545803,
      "avg_train_loss": 0.1481063961982727,
      "latency_p50_ms": 634.6276104450226,
      "latency_p95_ms": 634.6276104450226,
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
      "latency_p50_ms": 1169.2571640014648,
      "latency_p95_ms": 1169.2571640014648,
      "latency_p99_ms": 1169.2571640014648,
      "latency_max_ms": 1169.2571640014648,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1071.3706016540527,
      "latency_p95_ms": 1071.3706016540527,
      "latency_p99_ms": 1071.3706016540527,
      "latency_max_ms": 1071.3706016540527,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1079.63228225708,
      "latency_p95_ms": 1079.63228225708,
      "latency_p99_ms": 1079.63228225708,
      "latency_max_ms": 1079.63228225708,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1072.6521015167236,
      "latency_p95_ms": 1072.6521015167236,
      "latency_p99_ms": 1072.6521015167236,
      "latency_max_ms": 1072.6521015167236,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1068.772792816162,
      "latency_p95_ms": 1068.772792816162,
      "latency_p99_ms": 1068.772792816162,
      "latency_max_ms": 1068.772792816162,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 536.2176895141602,
      "latency_p95_ms": 536.2176895141602,
      "latency_p99_ms": 536.2176895141602,
      "latency_max_ms": 536.2176895141602,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1069.1006183624268,
      "latency_p95_ms": 1069.1006183624268,
      "latency_p99_ms": 1069.1006183624268,
      "latency_max_ms": 1069.1006183624268,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 805.1502704620361,
      "latency_p95_ms": 805.1502704620361,
      "latency_p99_ms": 805.1502704620361,
      "latency_max_ms": 805.1502704620361,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 769.0856456756592,
      "latency_p95_ms": 769.0856456756592,
      "latency_p99_ms": 769.0856456756592,
      "latency_max_ms": 769.0856456756592,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 770.7130908966064,
      "latency_p95_ms": 770.7130908966064,
      "latency_p99_ms": 770.7130908966064,
      "latency_max_ms": 770.7130908966064,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 782.1660041809082,
      "latency_p95_ms": 782.1660041809082,
      "latency_p99_ms": 782.1660041809082,
      "latency_max_ms": 782.1660041809082,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 805.8280944824219,
      "latency_p95_ms": 805.8280944824219,
      "latency_p99_ms": 805.8280944824219,
      "latency_max_ms": 805.8280944824219,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 770.6625461578369,
      "latency_p95_ms": 770.6625461578369,
      "latency_p99_ms": 770.6625461578369,
      "latency_max_ms": 770.6625461578369,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 379.6708583831787,
      "latency_p95_ms": 379.6708583831787,
      "latency_p99_ms": 379.6708583831787,
      "latency_max_ms": 379.6708583831787,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 744.4045543670654,
      "latency_p95_ms": 744.4045543670654,
      "latency_p99_ms": 744.4045543670654,
      "latency_max_ms": 744.4045543670654,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 570.5263614654541,
      "latency_p95_ms": 570.5263614654541,
      "latency_p99_ms": 570.5263614654541,
      "latency_max_ms": 570.5263614654541,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 704.683780670166,
      "latency_p95_ms": 704.683780670166,
      "latency_p99_ms": 704.683780670166,
      "latency_max_ms": 704.683780670166,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 692.6512718200684,
      "latency_p95_ms": 692.6512718200684,
      "latency_p99_ms": 692.6512718200684,
      "latency_max_ms": 692.6512718200684,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 705.6570053100586,
      "latency_p95_ms": 705.6570053100586,
      "latency_p99_ms": 705.6570053100586,
      "latency_max_ms": 705.6570053100586,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 725.0690460205078,
      "latency_p95_ms": 725.0690460205078,
      "latency_p99_ms": 725.0690460205078,
      "latency_max_ms": 725.0690460205078,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 696.3956356048584,
      "latency_p95_ms": 696.3956356048584,
      "latency_p99_ms": 696.3956356048584,
      "latency_max_ms": 696.3956356048584,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 345.3359603881836,
      "latency_p95_ms": 345.3359603881836,
      "latency_p99_ms": 345.3359603881836,
      "latency_max_ms": 345.3359603881836,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 685.9712600708008,
      "latency_p95_ms": 685.9712600708008,
      "latency_p99_ms": 685.9712600708008,
      "latency_max_ms": 685.9712600708008,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 521.2569236755371,
      "latency_p95_ms": 521.2569236755371,
      "latency_p99_ms": 521.2569236755371,
      "latency_max_ms": 521.2569236755371,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    }
  ]
}
```