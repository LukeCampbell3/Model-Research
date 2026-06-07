# PVR-EC Latency Stability Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-07T02:12:35.190129",
    "run_id": "algo_20260607_021013_benchmark-lite",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 42,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode benchmark-lite --scale small --sample-limit 1000 --train-steps 500 --device cuda --amp --models fixed_moe_vectorized,pvr_ec_deploy_top1,pvr_ec_ownership_top1_best_scale_repair --enable-ownership-map --ownership-map-mode frozen --run-benchmark-transfer-confirmation --output-dir evaluation/benchmark_results/pvr_benchmark_transfer_repair",
    "model_variants": [
      "fixed_moe_vectorized",
      "pvr_ec_deploy_top1",
      "pvr_ec_ownership_top1_best_scale_repair"
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
      "run_root_baseline_matrix": false,
      "run_training_dynamics_diagnostic": false,
      "run_ownership_integration_diagnostic": false,
      "run_shared_sparse_ablation": false,
      "run_learning_separation_diagnostic": false,
      "run_loss_calibration_diagnostic": false,
      "run_task_fit_diagnostic": false,
      "run_latency_stability_diagnostic": false,
      "run_gradient_flow_diagnostic": false,
      "run_optimizer_update_diagnostic": false,
      "run_expert_contribution_diagnostic": false,
      "run_loss_target_sanity": false,
      "run_shared_absorption_diagnostic": false,
      "run_expert_initialization_diagnostic": false,
      "run_after_repair_confirmation": false,
      "run_nonlinear_overfit_diagnostic": false,
      "run_fixed_owner_parity_diagnostic": false,
      "run_parity_scale_sweep": false,
      "run_nonlinear_overfit_confirmation": false,
      "run_after_nonlinear_repair_confirmation": false,
      "run_expert_delta_scale_schedule_diagnostic": false,
      "run_expert_delta_scale_schedule_confirmation": false,
      "run_residual_alignment_diagnostic": false,
      "run_family_scale_sweep": false,
      "run_conditional_scale_oracle": false,
      "run_benchmark_transfer_confirmation": true
    },
    "diagnostic_sweeps": {
      "train_steps_list": [
        500
      ],
      "seed_list": [
        42
      ],
      "ownership_schedule_sweep": [],
      "shared_scale_sweep": [],
      "expert_delta_scale_sweep": [],
      "loss_schedule_sweep": [],
      "task_loss_schedule_sweep": [],
      "batch_size_list": [
        1,
        32
      ],
      "seq_len_list": [
        64
      ],
      "pvr_overfit_tasks": [
        "toy_identity"
      ],
      "pvr_overfit_steps": 100,
      "pvr_overfit_batch_size": 16,
      "pvr_overfit_single_batch": false,
      "pvr_shared_scale_sweep": [],
      "pvr_expert_delta_scale_sweep": [],
      "pvr_expert_init_sweep": [],
      "pvr_expert_delta_scale_schedule": "constant",
      "pvr_expert_delta_scale_start": null,
      "pvr_expert_delta_scale_end": null,
      "pvr_expert_delta_scale_warmup_steps": null,
      "pvr_expert_delta_scale_hold_steps": null,
      "pvr_expert_delta_scale_decay": null,
      "conditional_scale_modes": []
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
      "latency_p50_ms": 1023.766815662384,
      "latency_p95_ms": 1023.766815662384,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_deploy_top1": {
      "count": 8,
      "avg_loss": 0.45097945421002805,
      "avg_accuracy": 0.0771500010285979,
      "avg_train_loss": 0.17677822709083557,
      "latency_p50_ms": 606.8336367607117,
      "latency_p95_ms": 606.8336367607117,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_best_scale_repair": {
      "count": 8,
      "avg_loss": 0.46348366168482846,
      "avg_accuracy": 0.06054665483850138,
      "avg_train_loss": 0.18761539459228516,
      "latency_p50_ms": 493.425577878952,
      "latency_p95_ms": 493.425577878952,
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
      "latency_p50_ms": 1158.8621139526367,
      "latency_p95_ms": 1158.8621139526367,
      "latency_p99_ms": 1158.8621139526367,
      "latency_max_ms": 1158.8621139526367,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1134.4952583312988,
      "latency_p95_ms": 1134.4952583312988,
      "latency_p99_ms": 1134.4952583312988,
      "latency_max_ms": 1134.4952583312988,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1116.6741847991943,
      "latency_p95_ms": 1116.6741847991943,
      "latency_p99_ms": 1116.6741847991943,
      "latency_max_ms": 1116.6741847991943,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1133.7628364562988,
      "latency_p95_ms": 1133.7628364562988,
      "latency_p99_ms": 1133.7628364562988,
      "latency_max_ms": 1133.7628364562988,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1121.3958263397217,
      "latency_p95_ms": 1121.3958263397217,
      "latency_p99_ms": 1121.3958263397217,
      "latency_max_ms": 1121.3958263397217,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 553.9720058441162,
      "latency_p95_ms": 553.9720058441162,
      "latency_p99_ms": 553.9720058441162,
      "latency_max_ms": 553.9720058441162,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1119.9991703033447,
      "latency_p95_ms": 1119.9991703033447,
      "latency_p99_ms": 1119.9991703033447,
      "latency_max_ms": 1119.9991703033447,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 850.9731292724609,
      "latency_p95_ms": 850.9731292724609,
      "latency_p99_ms": 850.9731292724609,
      "latency_max_ms": 850.9731292724609,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 661.0407829284668,
      "latency_p95_ms": 661.0407829284668,
      "latency_p99_ms": 661.0407829284668,
      "latency_max_ms": 661.0407829284668,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 668.1568622589111,
      "latency_p95_ms": 668.1568622589111,
      "latency_p99_ms": 668.1568622589111,
      "latency_max_ms": 668.1568622589111,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 683.9079856872559,
      "latency_p95_ms": 683.9079856872559,
      "latency_p99_ms": 683.9079856872559,
      "latency_max_ms": 683.9079856872559,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 703.3534049987793,
      "latency_p95_ms": 703.3534049987793,
      "latency_p99_ms": 703.3534049987793,
      "latency_max_ms": 703.3534049987793,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 662.7118587493896,
      "latency_p95_ms": 662.7118587493896,
      "latency_p99_ms": 662.7118587493896,
      "latency_max_ms": 662.7118587493896,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 331.2265872955322,
      "latency_p95_ms": 331.2265872955322,
      "latency_p99_ms": 331.2265872955322,
      "latency_max_ms": 331.2265872955322,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 653.03635597229,
      "latency_p95_ms": 653.03635597229,
      "latency_p99_ms": 653.03635597229,
      "latency_max_ms": 653.03635597229,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 491.23525619506836,
      "latency_p95_ms": 491.23525619506836,
      "latency_p99_ms": 491.23525619506836,
      "latency_max_ms": 491.23525619506836,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_best_scale_repair",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 550.9510040283203,
      "latency_p95_ms": 550.9510040283203,
      "latency_p99_ms": 550.9510040283203,
      "latency_max_ms": 550.9510040283203,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_best_scale_repair",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 535.1102352142334,
      "latency_p95_ms": 535.1102352142334,
      "latency_p99_ms": 535.1102352142334,
      "latency_max_ms": 535.1102352142334,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_best_scale_repair",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 577.5599479675293,
      "latency_p95_ms": 577.5599479675293,
      "latency_p99_ms": 577.5599479675293,
      "latency_max_ms": 577.5599479675293,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_best_scale_repair",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 563.532829284668,
      "latency_p95_ms": 563.532829284668,
      "latency_p99_ms": 563.532829284668,
      "latency_max_ms": 563.532829284668,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_best_scale_repair",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 536.264181137085,
      "latency_p95_ms": 536.264181137085,
      "latency_p99_ms": 536.264181137085,
      "latency_max_ms": 536.264181137085,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_best_scale_repair",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 268.12076568603516,
      "latency_p95_ms": 268.12076568603516,
      "latency_p99_ms": 268.12076568603516,
      "latency_max_ms": 268.12076568603516,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_best_scale_repair",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 524.8253345489502,
      "latency_p95_ms": 524.8253345489502,
      "latency_p99_ms": 524.8253345489502,
      "latency_max_ms": 524.8253345489502,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_best_scale_repair",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 391.0403251647949,
      "latency_p95_ms": 391.0403251647949,
      "latency_p99_ms": 391.0403251647949,
      "latency_max_ms": 391.0403251647949,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    }
  ]
}
```