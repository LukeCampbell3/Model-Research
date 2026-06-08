# PVR-EC Root Cause Loop Report

**Status:** PVR_EC_CAPABILITY_SIGNAL_TOO_WEAK_FOR_FINAL_ROOT_CAUSE

**Statuses:** PVR_EC_CAPABILITY_SIGNAL_TOO_WEAK_FOR_FINAL_ROOT_CAUSE, PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-08T00:40:08.727770",
    "run_id": "algo_20260608_003949_inference-only",
    "git_commit": "51e443da02bdc0a13c33b86368b863343ae036a2",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 42,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode inference-only --scale small --device cuda --amp --models fixed_moe_vectorized,pvr_ec_deploy_top1,pvr_ec_ownership_top1_final_candidate_v1 --enable-ownership-map --ownership-map-mode frozen --shape-list b8-s64,b16-s64,b16-s128,b32-s64,b32-s128,b64-s16,b64-s64,b64-s128,b1-s16,b1-s64,b8-s16,b32-s16 --run-qpm-failing-shape-replay --output-dir evaluation/benchmark_results/pvr_minimax_qpm_failing_shape_replay",
    "model_variants": [
      "fixed_moe_vectorized",
      "pvr_ec_deploy_top1",
      "pvr_ec_ownership_top1_final_candidate_v1"
    ],
    "batch_sizes": [
      1,
      8,
      16,
      32,
      64
    ],
    "sequence_lengths": [
      16,
      64,
      128
    ],
    "train_steps": 500,
    "sample_limit": null,
    "mode": "inference-only",
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
      "run_benchmark_transfer_confirmation": false,
      "run_task_level_transfer_diagnostic": false,
      "run_decision_token_credit_diagnostic": false,
      "run_token_to_sequence_transfer_diagnostic": false,
      "run_family_failure_decomposition": false,
      "run_output_readout_diagnostic": false,
      "run_loss_credit_repair_sweep": false,
      "run_curriculum_repair_sweep": false,
      "run_segment_residual_diagnostic": false,
      "run_sparse_logit_direction_diagnostic": false,
      "run_sparse_auxiliary_loss_sweep": false,
      "run_calibration_constrained_sparse_aux_sweep": false,
      "run_sparse_auxiliary_scope_sweep": false,
      "run_sparse_direction_transfer_confirmation": false,
      "run_final_config_manifest": false,
      "run_forward_purity_gate": false,
      "run_multiseed_confirmation_gate": false,
      "run_longer_training_confirmation_gate": false,
      "run_matched_wall_clock_gate": false,
      "run_final_calibration_sweep": false,
      "run_family_regression_gate": false,
      "run_quality_per_ms_memory_gate": false,
      "run_reliability_proxy_gate": false,
      "run_repeatability_collapse_isolation": false,
      "run_repeatability_repair_sweep": false,
      "run_qpm_shape_regression_analysis": false,
      "run_qpm_memory_repair": false,
      "run_reliability_calibration_repair": false,
      "run_final_candidate_revalidation": false,
      "run_collapse_case_replay": false,
      "run_minimax_candidate_selection": false,
      "run_stability_repair_sweep": false,
      "run_qpm_failing_shape_replay": true,
      "run_qpm_formula_audit": false,
      "run_shape_qpm_runtime_repair": false
    },
    "diagnostic_sweeps": {
      "train_steps_list": [],
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
        8,
        16,
        32,
        64
      ],
      "seq_len_list": [
        16,
        64,
        128
      ],
      "shape_pairs": [
        [
          8,
          64
        ],
        [
          16,
          64
        ],
        [
          16,
          128
        ],
        [
          32,
          64
        ],
        [
          32,
          128
        ],
        [
          64,
          16
        ],
        [
          64,
          64
        ],
        [
          64,
          128
        ],
        [
          1,
          16
        ],
        [
          1,
          64
        ],
        [
          8,
          16
        ],
        [
          32,
          16
        ]
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
      "curriculum_variants": [],
      "sparse_aux_loss_variants": [],
      "sparse_aux_scopes": [],
      "final_calibration_variants": [],
      "repeatability_repair_variants": [],
      "calibration_repair_variants": [],
      "minimax_variants": [],
      "stability_repair_variants": [],
      "max_train_seconds": null
    },
    "source": "inference_only"
  },
  "status": "PVR_EC_CAPABILITY_SIGNAL_TOO_WEAK_FOR_FINAL_ROOT_CAUSE",
  "statuses": [
    "PVR_EC_CAPABILITY_SIGNAL_TOO_WEAK_FOR_FINAL_ROOT_CAUSE",
    "PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY",
    "PVR_EC_DO_NOT_PROMOTE",
    "PVR_EC_ROOT_CAUSE_INCONCLUSIVE"
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
      "label": "max_accuracy_too_low_for_decisive_root_cause",
      "value": 0.0087890625
    }
  ]
}
```