# PVR-EC Training Dynamics Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-07T18:36:16.468381",
    "run_id": "algo_20260607_183400_benchmark-lite",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 42,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode benchmark-lite --scale small --sample-limit 1000 --train-steps 500 --device cuda --amp --models fixed_moe_vectorized,pvr_ec_deploy_top1,pvr_ec_ownership_top1_final_candidate_v1 --enable-ownership-map --ownership-map-mode frozen --run-family-regression-gate --output-dir evaluation/benchmark_results/pvr_final_family_regression_gate",
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
      "run_family_regression_gate": true,
      "run_quality_per_ms_memory_gate": false,
      "run_reliability_proxy_gate": false
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
      "curriculum_variants": [],
      "sparse_aux_loss_variants": [],
      "sparse_aux_scopes": [],
      "final_calibration_variants": [],
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
  "loss_curve": [
    {
      "model": "fixed_moe_vectorized",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.13683611154556274,
      "eval_loss": 0.21254643611609936,
      "accuracy": 0.49845454545454543
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.13683611154556274,
      "eval_loss": 0.19413983169943094,
      "accuracy": 0.524896510940272
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.13683611154556274,
      "eval_loss": 0.1954027395695448,
      "accuracy": 0.54045683313976
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "listops",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.13683611154556274,
      "eval_loss": 1.3568206988275051,
      "accuracy": 0.22077739706790991
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.13683611154556274,
      "eval_loss": 0.19047189503908157,
      "accuracy": 0.1043172898161537
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.13683611154556274,
      "eval_loss": 0.27171851694583893,
      "accuracy": 0.07577118897873615
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.13683611154556274,
      "eval_loss": 0.41219974867999554,
      "accuracy": 0.02989242863053372
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.13683611154556274,
      "eval_loss": 0.27556165183583897,
      "accuracy": 0.07405940594059406
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.17677822709083557,
      "eval_loss": 0.27750235982239246,
      "accuracy": 0.1831818181818182
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.17677822709083557,
      "eval_loss": 0.2479988867416978,
      "accuracy": 0.19101123595505617
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.17677822709083557,
      "eval_loss": 0.2770938128232956,
      "accuracy": 0.13985675571041425
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "listops",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.17677822709083557,
      "eval_loss": 1.589727409183979,
      "accuracy": 0.08681121159355165
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.17677822709083557,
      "eval_loss": 0.2083501284942031,
      "accuracy": 0.01094815120842801
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.17677822709083557,
      "eval_loss": 0.2918624170124531,
      "accuracy": 0.005390835579514825
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.17677822709083557,
      "eval_loss": 0.42143215239048004,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.17677822709083557,
      "eval_loss": 0.2938684672117233,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063961982727,
      "eval_loss": 0.24142212327569723,
      "accuracy": 0.49918181818181817
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063961982727,
      "eval_loss": 0.20873637683689594,
      "accuracy": 0.5117681845062093
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063961982727,
      "eval_loss": 0.23053767159581184,
      "accuracy": 0.49661246612466126
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "listops",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063961982727,
      "eval_loss": 1.3296168148517609,
      "accuracy": 0.22673144975565915
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063961982727,
      "eval_loss": 0.19809814915060997,
      "accuracy": 0.08572608965089858
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063961982727,
      "eval_loss": 0.2804417908191681,
      "accuracy": 0.055705300988319856
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063961982727,
      "eval_loss": 0.4041307009756565,
      "accuracy": 0.03568473314025652
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063961982727,
      "eval_loss": 0.27329832191268605,
      "accuracy": 0.06158415841584158
    }
  ],
  "specialization_metrics": {
    "expert_utilization": 0.6666666666666666,
    "expert_gradient_norm_by_expert": {},
    "expert_output_norm_by_expert": {}
  }
}
```