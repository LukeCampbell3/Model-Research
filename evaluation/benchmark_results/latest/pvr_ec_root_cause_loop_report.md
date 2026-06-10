# PVR-EC Root Cause Loop Report

**Status:** PVR_EC_ROUTED_EXPERT_UNDERCONTRIBUTION_BLOCKER

**Statuses:** PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_LATENCY_VARIANCE_BLOCKER, PVR_EC_LEARNING_SEPARATION_DIAGNOSTIC_READY, PVR_EC_ROOT_CAUSE_INCONCLUSIVE, PVR_EC_ROUTED_EXPERT_UNDERCONTRIBUTION_BLOCKER

```json
{
  "metadata": {
    "timestamp": "2026-06-10T20:14:37.226565",
    "run_id": "algo_20260610_201437_smoke",
    "git_commit": "48f9fbfd8e16a3775c479d71d0994955f572a033",
    "docker_image": "N/A",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": false,
    "seed": 42,
    "benchmark_command": "/opt/conda/lib/python3.10/site-packages/pytest/__main__.py sparse_loop_moe/tests/test_pvr_ec_release_freeze.py sparse_loop_moe/tests/test_pvr_ec_release_package.py sparse_loop_moe/tests/test_pvr_ec_manifest_lock.py sparse_loop_moe/tests/test_pvr_ec_production_shape_profile.py sparse_loop_moe/tests/test_pvr_ec_canary_rollout.py sparse_loop_moe/tests/test_pvr_ec_drift_monitoring.py sparse_loop_moe/tests/test_pvr_ec_release_readiness.py sparse_loop_moe/tests/test_pvr_ec.py -q --tb=line",
    "model_variants": [
      "dense_baseline",
      "fixed_moe",
      "fixed_moe_looped_reference",
      "fixed_moe_vectorized",
      "adaptive_moe",
      "looped_moe",
      "full_system",
      "pvr_ec",
      "pvr_ec_matched",
      "pvr_ec_fixed_top2",
      "pvr_ec_no_prototypes",
      "pvr_ec_no_load_bias",
      "pvr_ec_no_extra_experts",
      "pvr_ec_deploy_top1",
      "pvr_ec_deploy_top2",
      "pvr_ec_deploy_bucketed",
      "pvr_ec_deploy_dense_masked_control",
      "pvr_ec_ownership_top1_frozen_candidate",
      "pvr_ec_ownership_top1_delta_small",
      "pvr_ec_ownership_top1_delta_medium",
      "pvr_ec_ownership_top1_delta_large",
      "pvr_ec_ownership_top1_full_expert_ffn_control",
      "pvr_ec_ownership_top1_rank_8",
      "pvr_ec_ownership_top1_rank_16",
      "pvr_ec_ownership_top1_rank_32",
      "pvr_ec_ownership_top1_rank_64",
      "pvr_ec_ownership_top1_rank_128",
      "pvr_ec_ownership_top1_micro_ffn_0_25x",
      "pvr_ec_ownership_top1_micro_ffn_0_5x",
      "pvr_ec_ownership_top1_micro_ffn_1_0x",
      "pvr_ec_ownership_top1_delta_rank_8",
      "pvr_ec_ownership_top1_delta_rank_16",
      "pvr_ec_ownership_top1_delta_rank_32",
      "pvr_ec_ownership_top1_delta_rank_64",
      "pvr_ec_ownership_top1_delta_rank_128",
      "pvr_ec_learning_full",
      "pvr_ec_learning_shared_only",
      "pvr_ec_learning_sparse_only",
      "pvr_ec_learning_shared_scale_0_5",
      "pvr_ec_learning_expert_delta_scale_2_0",
      "pvr_ec_ownership_top1_delayed_candidate",
      "pvr_shared_only",
      "pvr_sparse_only",
      "pvr_full",
      "pvr_full_shared_scale_1_0",
      "pvr_full_shared_scale_0_5",
      "pvr_full_shared_scale_0_25",
      "pvr_full_shared_scale_0_0",
      "pvr_full_expert_delta_scale_0_5",
      "pvr_full_expert_delta_scale_1_0",
      "pvr_full_expert_delta_scale_2_0",
      "pvr_full_expert_delta_scale_4_0",
      "pvr_full_fixed_owner_e0",
      "pvr_full_fixed_owner_round_robin",
      "pvr_full_uniform_owner",
      "pvr_full_expert_delta_scale_1",
      "pvr_full_expert_delta_scale_2",
      "pvr_full_expert_delta_scale_4",
      "pvr_full_expert_delta_scale_8",
      "pvr_full_delta_rank_16",
      "pvr_full_delta_rank_64",
      "pvr_full_delta_rank_128",
      "pvr_full_micro_ffn_0_5x",
      "pvr_ec_ownership_top1_constant_1",
      "pvr_ec_ownership_top1_constant_2",
      "pvr_ec_ownership_top1_constant_4",
      "pvr_ec_ownership_top1_constant_8",
      "pvr_full_scale_schedule_1_to_4",
      "pvr_full_scale_schedule_1_to_8",
      "pvr_full_scale_schedule_1_to_8_to_4",
      "pvr_ec_ownership_top1_scale_schedule_1_to_4",
      "pvr_ec_ownership_top1_scale_schedule_1_to_8",
      "pvr_ec_ownership_top1_scale_schedule_1_to_8_to_4",
      "pvr_ec_ownership_top1_scale_schedule_1_to_8_to_2",
      "pvr_ec_ownership_top1_scale_schedule_1_to_4_to_2",
      "pvr_ec_ownership_top1_best_scale_repair",
      "pvr_ec_ownership_top1_best_transfer_repair",
      "pvr_ec_ownership_top1_best_sparse_logit_repair",
      "pvr_ec_ownership_top1_final_candidate_v1",
      "pvr_ec_ownership_top1_final_candidate_v1_1",
      "pvr_ec_ownership_top1_final_candidate_v1_2"
    ],
    "batch_sizes": [
      1,
      32
    ],
    "sequence_lengths": [
      64
    ],
    "train_steps": 30,
    "sample_limit": null,
    "mode": "smoke",
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
      "run_root_baseline_matrix": true,
      "run_training_dynamics_diagnostic": true,
      "run_ownership_integration_diagnostic": true,
      "run_shared_sparse_ablation": true,
      "run_loss_calibration_diagnostic": true,
      "run_task_fit_diagnostic": true,
      "run_latency_stability_diagnostic": true
    },
    "diagnostic_sweeps": {
      "loss_schedule_sweep": [
        "ce_only",
        "aux_delta"
      ],
      "task_loss_schedule_sweep": [
        "uniform",
        "family_balanced"
      ]
    },
    "source": "trained_benchmark"
  },
  "status": "PVR_EC_ROUTED_EXPERT_UNDERCONTRIBUTION_BLOCKER",
  "statuses": [
    "PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY",
    "PVR_EC_DO_NOT_PROMOTE",
    "PVR_EC_LATENCY_VARIANCE_BLOCKER",
    "PVR_EC_LEARNING_SEPARATION_DIAGNOSTIC_READY",
    "PVR_EC_ROOT_CAUSE_INCONCLUSIVE",
    "PVR_EC_ROUTED_EXPERT_UNDERCONTRIBUTION_BLOCKER"
  ],
  "promotion_ready": false,
  "diagnostic_loop": [
    {
      "name": "pvr_ec_root_baseline_matrix",
      "json": "pvr_ec_root_baseline_matrix.json",
      "md": "pvr_ec_root_baseline_matrix.md"
    },
    {
      "name": "pvr_ec_training_dynamics_report",
      "json": "pvr_ec_training_dynamics_report.json",
      "md": "pvr_ec_training_dynamics_report.md"
    },
    {
      "name": "pvr_ec_ownership_integration_report",
      "json": "pvr_ec_ownership_integration_report.json",
      "md": "pvr_ec_ownership_integration_report.md"
    },
    {
      "name": "pvr_ec_shared_sparse_ablation_report",
      "json": "pvr_ec_shared_sparse_ablation_report.json",
      "md": "pvr_ec_shared_sparse_ablation_report.md"
    },
    {
      "name": "pvr_ec_learning_separation_report",
      "json": "pvr_ec_learning_separation_report.json",
      "md": "pvr_ec_learning_separation_report.md"
    },
    {
      "name": "pvr_ec_loss_calibration_report",
      "json": "pvr_ec_loss_calibration_report.json",
      "md": "pvr_ec_loss_calibration_report.md"
    },
    {
      "name": "pvr_ec_task_fit_report",
      "json": "pvr_ec_task_fit_report.json",
      "md": "pvr_ec_task_fit_report.md"
    },
    {
      "name": "pvr_ec_latency_stability_report",
      "json": "pvr_ec_latency_stability_report.json",
      "md": "pvr_ec_latency_stability_report.md"
    }
  ],
  "evidence": [
    {
      "label": "latency_p95_p50_ratio",
      "value": 4.0
    },
    {
      "label": "full_model_score_minus_shared_only_score",
      "value": -0.15000000000000002
    }
  ]
}
```