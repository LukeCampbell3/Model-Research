# PVR-EC Latency Stability Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-09T01:21:58.712838",
    "run_id": "algo_20260609_012119_benchmark-lite",
    "git_commit": "aff470f9ed548af833e78f9fb075ed1fa78a9af1",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 42,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode benchmark-lite --scale small --sample-limit 512 --train-steps 200 --seed 42 --families clrs,listops,scan,dyck --device cuda --amp --models dense_baseline,fixed_moe_vectorized,pvr_full --output-dir evaluation/benchmark_results/pvr_family_benchmark_lite",
    "model_variants": [
      "dense_baseline",
      "fixed_moe_vectorized",
      "pvr_full"
    ],
    "batch_sizes": [
      1,
      32
    ],
    "sequence_lengths": [
      64
    ],
    "train_steps": 200,
    "sample_limit": 512,
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
      "run_qpm_failing_shape_replay": false,
      "run_qpm_formula_audit": false,
      "run_shape_qpm_runtime_repair": false,
      "run_failure_case_replay": false,
      "run_failure_attribution": false,
      "run_failure_repair_candidates": false,
      "run_failure_repair_validation": false
    },
    "diagnostic_sweeps": {
      "train_steps_list": [
        200
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
      "shape_pairs": [],
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
    "source": "trained_benchmark"
  },
  "status": "PVR_EC_ROOT_CAUSE_INCONCLUSIVE",
  "statuses": [
    "PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY",
    "PVR_EC_DO_NOT_PROMOTE",
    "PVR_EC_ROOT_CAUSE_INCONCLUSIVE"
  ],
  "by_model": {
    "dense_baseline": {
      "count": 8,
      "avg_loss": 0.44256602305298054,
      "avg_accuracy": 0.06708629865773938,
      "avg_train_loss": 0.29558122158050537,
      "latency_p50_ms": 110.64940690994263,
      "latency_p95_ms": 110.64940690994263,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "fixed_moe_vectorized": {
      "count": 8,
      "avg_loss": 0.4403862536419183,
      "avg_accuracy": 0.0405815215621312,
      "avg_train_loss": 0.31766414642333984,
      "latency_p50_ms": 396.76883816719055,
      "latency_p95_ms": 396.76883816719055,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_full": {
      "count": 8,
      "avg_loss": 0.45161311755267286,
      "avg_accuracy": 0.07171890165302205,
      "avg_train_loss": 0.33932358026504517,
      "latency_p50_ms": 127.45031714439392,
      "latency_p95_ms": 127.45031714439392,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    }
  },
  "latency_p95_p50_ratio_reported": true,
  "max_latency_p95_p50_ratio": 1.0,
  "rows": [
    {
      "model": "dense_baseline",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 266.69907569885254,
      "latency_p95_ms": 266.69907569885254,
      "latency_p99_ms": 266.69907569885254,
      "latency_max_ms": 266.69907569885254,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "dense_baseline",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 111.21392250061035,
      "latency_p95_ms": 111.21392250061035,
      "latency_p99_ms": 111.21392250061035,
      "latency_max_ms": 111.21392250061035,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "dense_baseline",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 108.62994194030762,
      "latency_p95_ms": 108.62994194030762,
      "latency_p99_ms": 108.62994194030762,
      "latency_max_ms": 108.62994194030762,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "dense_baseline",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 97.69177436828613,
      "latency_p95_ms": 97.69177436828613,
      "latency_p99_ms": 97.69177436828613,
      "latency_max_ms": 97.69177436828613,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "dense_baseline",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 93.94168853759766,
      "latency_p95_ms": 93.94168853759766,
      "latency_p99_ms": 93.94168853759766,
      "latency_max_ms": 93.94168853759766,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "dense_baseline",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 45.81427574157715,
      "latency_p95_ms": 45.81427574157715,
      "latency_p99_ms": 45.81427574157715,
      "latency_max_ms": 45.81427574157715,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "dense_baseline",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 91.98713302612305,
      "latency_p95_ms": 91.98713302612305,
      "latency_p99_ms": 91.98713302612305,
      "latency_max_ms": 91.98713302612305,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "dense_baseline",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 69.21744346618652,
      "latency_p95_ms": 69.21744346618652,
      "latency_p99_ms": 69.21744346618652,
      "latency_max_ms": 69.21744346618652,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 437.2291564941406,
      "latency_p95_ms": 437.2291564941406,
      "latency_p99_ms": 437.2291564941406,
      "latency_max_ms": 437.2291564941406,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 443.3331489562988,
      "latency_p95_ms": 443.3331489562988,
      "latency_p99_ms": 443.3331489562988,
      "latency_max_ms": 443.3331489562988,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 436.3110065460205,
      "latency_p95_ms": 436.3110065460205,
      "latency_p99_ms": 436.3110065460205,
      "latency_max_ms": 436.3110065460205,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 440.4714107513428,
      "latency_p95_ms": 440.4714107513428,
      "latency_p99_ms": 440.4714107513428,
      "latency_max_ms": 440.4714107513428,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 436.21206283569336,
      "latency_p95_ms": 436.21206283569336,
      "latency_p99_ms": 436.21206283569336,
      "latency_max_ms": 436.21206283569336,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 217.94462203979492,
      "latency_p95_ms": 217.94462203979492,
      "latency_p99_ms": 217.94462203979492,
      "latency_max_ms": 217.94462203979492,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 435.81175804138184,
      "latency_p95_ms": 435.81175804138184,
      "latency_p99_ms": 435.81175804138184,
      "latency_max_ms": 435.81175804138184,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 326.83753967285156,
      "latency_p95_ms": 326.83753967285156,
      "latency_p99_ms": 326.83753967285156,
      "latency_max_ms": 326.83753967285156,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_full",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 137.50076293945312,
      "latency_p95_ms": 137.50076293945312,
      "latency_p99_ms": 137.50076293945312,
      "latency_max_ms": 137.50076293945312,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_full",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 152.1151065826416,
      "latency_p95_ms": 152.1151065826416,
      "latency_p99_ms": 152.1151065826416,
      "latency_max_ms": 152.1151065826416,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_full",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 135.79034805297852,
      "latency_p95_ms": 135.79034805297852,
      "latency_p99_ms": 135.79034805297852,
      "latency_max_ms": 135.79034805297852,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_full",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 143.85247230529785,
      "latency_p95_ms": 143.85247230529785,
      "latency_p99_ms": 143.85247230529785,
      "latency_max_ms": 143.85247230529785,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_full",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 139.81366157531738,
      "latency_p95_ms": 139.81366157531738,
      "latency_p99_ms": 139.81366157531738,
      "latency_max_ms": 139.81366157531738,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_full",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 68.55988502502441,
      "latency_p95_ms": 68.55988502502441,
      "latency_p99_ms": 68.55988502502441,
      "latency_max_ms": 68.55988502502441,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_full",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 137.85505294799805,
      "latency_p95_ms": 137.85505294799805,
      "latency_p99_ms": 137.85505294799805,
      "latency_max_ms": 137.85505294799805,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_full",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 104.11524772644043,
      "latency_p95_ms": 104.11524772644043,
      "latency_p99_ms": 104.11524772644043,
      "latency_max_ms": 104.11524772644043,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    }
  ]
}
```