# PVR-EC Latency Stability Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-07T02:38:37.625534",
    "run_id": "algo_20260607_023602_benchmark-lite",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 42,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode benchmark-lite --scale small --sample-limit 1000 --train-steps 500 --device cuda --amp --models fixed_moe_vectorized,pvr_ec_deploy_top1,pvr_ec_ownership_top1_best_transfer_repair --enable-ownership-map --ownership-map-mode frozen --run-benchmark-transfer-confirmation --output-dir evaluation/benchmark_results/pvr_task_transfer_repair_confirmation",
    "model_variants": [
      "fixed_moe_vectorized",
      "pvr_ec_deploy_top1",
      "pvr_ec_ownership_top1_best_transfer_repair"
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
      "run_benchmark_transfer_confirmation": true,
      "run_task_level_transfer_diagnostic": false,
      "run_decision_token_credit_diagnostic": false,
      "run_token_to_sequence_transfer_diagnostic": false,
      "run_family_failure_decomposition": false,
      "run_output_readout_diagnostic": false,
      "run_loss_credit_repair_sweep": false,
      "run_curriculum_repair_sweep": false,
      "run_segment_residual_diagnostic": false
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
      "conditional_scale_modes": [],
      "readout_variants": [],
      "loss_credit_variants": [],
      "curriculum_variants": []
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
      "latency_p50_ms": 1087.4061584472656,
      "latency_p95_ms": 1087.4061584472656,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_deploy_top1": {
      "count": 8,
      "avg_loss": 0.45097945421002805,
      "avg_accuracy": 0.0771500010285979,
      "avg_train_loss": 0.17677822709083557,
      "latency_p50_ms": 729.4546961784363,
      "latency_p95_ms": 729.4546961784363,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_best_transfer_repair": {
      "count": 8,
      "avg_loss": 0.463483668747358,
      "avg_accuracy": 0.06054665483850138,
      "avg_train_loss": 0.18761540949344635,
      "latency_p50_ms": 619.9401319026947,
      "latency_p95_ms": 619.9401319026947,
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
      "latency_p50_ms": 1269.550085067749,
      "latency_p95_ms": 1269.550085067749,
      "latency_p99_ms": 1269.550085067749,
      "latency_max_ms": 1269.550085067749,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1187.5989437103271,
      "latency_p95_ms": 1187.5989437103271,
      "latency_p99_ms": 1187.5989437103271,
      "latency_max_ms": 1187.5989437103271,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1199.556589126587,
      "latency_p95_ms": 1199.556589126587,
      "latency_p99_ms": 1199.556589126587,
      "latency_max_ms": 1199.556589126587,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1206.2084674835205,
      "latency_p95_ms": 1206.2084674835205,
      "latency_p99_ms": 1206.2084674835205,
      "latency_max_ms": 1206.2084674835205,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1198.8954544067383,
      "latency_p95_ms": 1198.8954544067383,
      "latency_p99_ms": 1198.8954544067383,
      "latency_max_ms": 1198.8954544067383,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 588.651180267334,
      "latency_p95_ms": 588.651180267334,
      "latency_p99_ms": 588.651180267334,
      "latency_max_ms": 588.651180267334,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1168.65873336792,
      "latency_p95_ms": 1168.65873336792,
      "latency_p99_ms": 1168.65873336792,
      "latency_max_ms": 1168.65873336792,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 880.1298141479492,
      "latency_p95_ms": 880.1298141479492,
      "latency_p99_ms": 880.1298141479492,
      "latency_max_ms": 880.1298141479492,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 802.5221824645996,
      "latency_p95_ms": 802.5221824645996,
      "latency_p99_ms": 802.5221824645996,
      "latency_max_ms": 802.5221824645996,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 805.1135540008545,
      "latency_p95_ms": 805.1135540008545,
      "latency_p99_ms": 805.1135540008545,
      "latency_max_ms": 805.1135540008545,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 820.4288482666016,
      "latency_p95_ms": 820.4288482666016,
      "latency_p99_ms": 820.4288482666016,
      "latency_max_ms": 820.4288482666016,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 840.6822681427002,
      "latency_p95_ms": 840.6822681427002,
      "latency_p99_ms": 840.6822681427002,
      "latency_max_ms": 840.6822681427002,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 801.5537261962891,
      "latency_p95_ms": 801.5537261962891,
      "latency_p99_ms": 801.5537261962891,
      "latency_max_ms": 801.5537261962891,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 400.87032318115234,
      "latency_p95_ms": 400.87032318115234,
      "latency_p99_ms": 400.87032318115234,
      "latency_max_ms": 400.87032318115234,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 785.1696014404297,
      "latency_p95_ms": 785.1696014404297,
      "latency_p99_ms": 785.1696014404297,
      "latency_max_ms": 785.1696014404297,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 579.2970657348633,
      "latency_p95_ms": 579.2970657348633,
      "latency_p99_ms": 579.2970657348633,
      "latency_max_ms": 579.2970657348633,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_best_transfer_repair",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 671.3833808898926,
      "latency_p95_ms": 671.3833808898926,
      "latency_p99_ms": 671.3833808898926,
      "latency_max_ms": 671.3833808898926,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_best_transfer_repair",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 666.877269744873,
      "latency_p95_ms": 666.877269744873,
      "latency_p99_ms": 666.877269744873,
      "latency_max_ms": 666.877269744873,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_best_transfer_repair",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 692.7826404571533,
      "latency_p95_ms": 692.7826404571533,
      "latency_p99_ms": 692.7826404571533,
      "latency_max_ms": 692.7826404571533,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_best_transfer_repair",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 690.7358169555664,
      "latency_p95_ms": 690.7358169555664,
      "latency_p99_ms": 690.7358169555664,
      "latency_max_ms": 690.7358169555664,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_best_transfer_repair",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 714.2221927642822,
      "latency_p95_ms": 714.2221927642822,
      "latency_p99_ms": 714.2221927642822,
      "latency_max_ms": 714.2221927642822,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_best_transfer_repair",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 350.99172592163086,
      "latency_p95_ms": 350.99172592163086,
      "latency_p99_ms": 350.99172592163086,
      "latency_max_ms": 350.99172592163086,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_best_transfer_repair",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 665.7922267913818,
      "latency_p95_ms": 665.7922267913818,
      "latency_p99_ms": 665.7922267913818,
      "latency_max_ms": 665.7922267913818,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_best_transfer_repair",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 506.73580169677734,
      "latency_p95_ms": 506.73580169677734,
      "latency_p99_ms": 506.73580169677734,
      "latency_max_ms": 506.73580169677734,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    }
  ]
}
```