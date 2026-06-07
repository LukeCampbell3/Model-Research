# PVR-EC Latency Stability Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-06T18:57:26.691549",
    "run_id": "algo_20260606_185724_inference-only",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "N/A",
    "cuda_available": false,
    "gpu_name": "",
    "amp_enabled": false,
    "seed": 42,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode inference-only --scale tiny --seed 42 --models fixed_moe_vectorized,pvr_ec_deploy_top1,pvr_ec_ownership_top1_delta_medium,pvr_ec_ownership_top1_full_expert_ffn_control --run-latency-stability-diagnostic --batch-size-list 1,8 --seq-len-list 16,64 --warmup-steps 3 --timed-steps 10 --output-dir evaluation/benchmark_results/docker_pvr_ec_latency_stability_actual",
    "model_variants": [
      "fixed_moe_vectorized",
      "pvr_ec_deploy_top1",
      "pvr_ec_ownership_top1_delta_medium",
      "pvr_ec_ownership_top1_full_expert_ffn_control"
    ],
    "batch_sizes": [
      1,
      8
    ],
    "sequence_lengths": [
      16,
      64
    ],
    "train_steps": 500,
    "sample_limit": null,
    "mode": "inference-only",
    "scale": "tiny",
    "families": [
      "clrs",
      "listops",
      "scan",
      "dyck"
    ],
    "root_cause_flags": {
      "run_root_baseline_matrix": false,
      "run_training_dynamics_diagnostic": false,
      "run_ownership_integration_diagnostic": false,
      "run_shared_sparse_ablation": false,
      "run_loss_calibration_diagnostic": false,
      "run_task_fit_diagnostic": false,
      "run_latency_stability_diagnostic": true
    },
    "diagnostic_sweeps": {
      "train_steps_list": [],
      "seed_list": [
        42
      ],
      "ownership_schedule_sweep": [],
      "loss_schedule_sweep": [],
      "task_loss_schedule_sweep": [],
      "batch_size_list": [
        1,
        8
      ],
      "seq_len_list": [
        16,
        64
      ]
    },
    "source": "inference_only"
  },
  "status": "PVR_EC_ROOT_CAUSE_INCONCLUSIVE",
  "statuses": [
    "PVR_EC_DO_NOT_PROMOTE",
    "PVR_EC_ROOT_CAUSE_INCONCLUSIVE"
  ],
  "by_model": {
    "fixed_moe_vectorized": {
      "count": 4,
      "avg_loss": 5.55166482925415,
      "avg_accuracy": 0.0,
      "avg_train_loss": null,
      "latency_p50_ms": 24.70420575002663,
      "latency_p95_ms": 27.21417094986691,
      "latency_p95_p50_ratio": 1.1524277005490606,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_deploy_top1": {
      "count": 4,
      "avg_loss": 5.533101320266724,
      "avg_accuracy": 0.001953125,
      "avg_train_loss": null,
      "latency_p50_ms": 5.141379874885388,
      "latency_p95_ms": 8.585600887715822,
      "latency_p95_p50_ratio": 1.5606888001301227,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_delta_medium": {
      "count": 4,
      "avg_loss": 5.559172987937927,
      "avg_accuracy": 0.001953125,
      "avg_train_loss": null,
      "latency_p50_ms": 4.471528875114927,
      "latency_p95_ms": 5.7241903125827776,
      "latency_p95_p50_ratio": 1.3210381910424436,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_full_expert_ffn_control": {
      "count": 4,
      "avg_loss": 5.528628468513489,
      "avg_accuracy": 0.0009765625,
      "avg_train_loss": null,
      "latency_p50_ms": 9.644951499808485,
      "latency_p95_ms": 11.288897162535248,
      "latency_p95_p50_ratio": 1.227399610050683,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    }
  },
  "latency_p95_p50_ratio_reported": true,
  "max_latency_p95_p50_ratio": 2.5907657961099293,
  "rows": [
    {
      "model": "fixed_moe_vectorized",
      "batch_size": 1,
      "sequence_length": 16,
      "latency_p50_ms": 4.649661999792443,
      "latency_p95_ms": 5.635870749847527,
      "latency_p99_ms": 5.635870749847527,
      "latency_max_ms": 5.635870749847527,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.2121033206497822
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": 1,
      "sequence_length": 64,
      "latency_p50_ms": 12.887811500149837,
      "latency_p95_ms": 14.431751299844109,
      "latency_p99_ms": 14.431751299844109,
      "latency_max_ms": 14.431751299844109,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.119798446747636
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": 8,
      "sequence_length": 16,
      "latency_p50_ms": 20.832054000038625,
      "latency_p95_ms": 25.713657099549888,
      "latency_p99_ms": 25.713657099549888,
      "latency_max_ms": 25.713657099549888,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.2343313385949466
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": 8,
      "sequence_length": 64,
      "latency_p50_ms": 60.44729550012562,
      "latency_p95_ms": 63.07540465022612,
      "latency_p99_ms": 63.07540465022612,
      "latency_max_ms": 63.07540465022612,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0434776962038779
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": 1,
      "sequence_length": 16,
      "latency_p50_ms": 2.7667629997267795,
      "latency_p95_ms": 3.6978469001041954,
      "latency_p99_ms": 3.6978469001041954,
      "latency_max_ms": 3.6978469001041954,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.3365246320228228
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": 1,
      "sequence_length": 64,
      "latency_p50_ms": 3.8689009998051915,
      "latency_p95_ms": 4.752223600235083,
      "latency_p99_ms": 4.752223600235083,
      "latency_max_ms": 4.752223600235083,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.2283135703070118
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": 8,
      "sequence_length": 16,
      "latency_p50_ms": 6.781432000025234,
      "latency_p95_ms": 7.372441950656139,
      "latency_p99_ms": 7.372441950656139,
      "latency_max_ms": 7.372441950656139,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0871512020807266
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": 8,
      "sequence_length": 64,
      "latency_p50_ms": 7.148423499984347,
      "latency_p95_ms": 18.519891099867873,
      "latency_p99_ms": 18.519891099867873,
      "latency_max_ms": 18.519891099867873,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 2.5907657961099293
    },
    {
      "model": "pvr_ec_ownership_top1_delta_medium",
      "batch_size": 1,
      "sequence_length": 16,
      "latency_p50_ms": 2.6505055002417066,
      "latency_p95_ms": 3.7127578999388784,
      "latency_p99_ms": 3.7127578999388784,
      "latency_max_ms": 3.7127578999388784,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.4007735126753376
    },
    {
      "model": "pvr_ec_ownership_top1_delta_medium",
      "batch_size": 1,
      "sequence_length": 64,
      "latency_p50_ms": 3.652122499715915,
      "latency_p95_ms": 4.676622449915158,
      "latency_p99_ms": 4.676622449915158,
      "latency_max_ms": 4.676622449915158,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.280521792540895
    },
    {
      "model": "pvr_ec_ownership_top1_delta_medium",
      "batch_size": 8,
      "sequence_length": 16,
      "latency_p50_ms": 3.556326500074647,
      "latency_p95_ms": 5.079884600263539,
      "latency_p99_ms": 5.079884600263539,
      "latency_max_ms": 5.079884600263539,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.4284078248037442
    },
    {
      "model": "pvr_ec_ownership_top1_delta_medium",
      "batch_size": 8,
      "sequence_length": 64,
      "latency_p50_ms": 8.02716100042744,
      "latency_p95_ms": 9.427496300213534,
      "latency_p99_ms": 9.427496300213534,
      "latency_max_ms": 9.427496300213534,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.1744496341497979
    },
    {
      "model": "pvr_ec_ownership_top1_full_expert_ffn_control",
      "batch_size": 1,
      "sequence_length": 16,
      "latency_p50_ms": 3.718726499755576,
      "latency_p95_ms": 4.6128810502978,
      "latency_p99_ms": 4.6128810502978,
      "latency_max_ms": 4.6128810502978,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.2404464406298756
    },
    {
      "model": "pvr_ec_ownership_top1_full_expert_ffn_control",
      "batch_size": 1,
      "sequence_length": 64,
      "latency_p50_ms": 4.186779999599821,
      "latency_p95_ms": 5.645164599900453,
      "latency_p99_ms": 5.645164599900453,
      "latency_max_ms": 5.645164599900453,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.3483308414676736
    },
    {
      "model": "pvr_ec_ownership_top1_full_expert_ffn_control",
      "batch_size": 8,
      "sequence_length": 16,
      "latency_p50_ms": 5.372948000058386,
      "latency_p95_ms": 6.422809999958189,
      "latency_p99_ms": 6.422809999958189,
      "latency_max_ms": 6.422809999958189,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.1953977592726366
    },
    {
      "model": "pvr_ec_ownership_top1_full_expert_ffn_control",
      "batch_size": 8,
      "sequence_length": 64,
      "latency_p50_ms": 25.301351499820157,
      "latency_p95_ms": 28.47473299998455,
      "latency_p99_ms": 28.47473299998455,
      "latency_max_ms": 28.47473299998455,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.1254233988325466
    }
  ]
}
```