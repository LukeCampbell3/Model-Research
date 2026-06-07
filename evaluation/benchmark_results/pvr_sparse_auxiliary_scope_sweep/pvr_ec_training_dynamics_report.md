# PVR-EC Training Dynamics Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-07T03:24:43.647776",
    "run_id": "algo_20260607_032151_benchmark-lite",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 42,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode benchmark-lite --scale small --sample-limit 1000 --train-steps 500 --device cuda --amp --models pvr_ec_ownership_top1_scale_schedule_1_to_8 --enable-ownership-map --ownership-map-mode frozen --run-sparse-auxiliary-scope-sweep --sparse-aux-scopes aux_all_tokens,aux_decision_tokens_only,aux_final_tokens_only,aux_listops_scan_only,aux_scan_only,aux_listops_only,aux_dyck_final_state_only --output-dir evaluation/benchmark_results/pvr_sparse_auxiliary_scope_sweep",
    "model_variants": [
      "pvr_ec_ownership_top1_scale_schedule_1_to_8"
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
      "run_sparse_auxiliary_scope_sweep": true,
      "run_sparse_direction_transfer_confirmation": false
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
      "sparse_aux_scopes": [
        "aux_all_tokens",
        "aux_decision_tokens_only",
        "aux_final_tokens_only",
        "aux_listops_scan_only",
        "aux_scan_only",
        "aux_listops_only",
        "aux_dyck_final_state_only"
      ]
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
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_all_tokens",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.2409456493332982,
      "accuracy": 0.46863636363636363
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_all_tokens",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.21231256052851677,
      "accuracy": 0.4853932584269663
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_all_tokens",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.23170064017176628,
      "accuracy": 0.44870305845915603
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_all_tokens",
      "family": "listops",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 1.3692205734550953,
      "accuracy": 0.20945907993034882
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_all_tokens",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.19689467176795006,
      "accuracy": 0.10287130758107829
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_all_tokens",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.2792850360274315,
      "accuracy": 0.06708595387840671
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_all_tokens",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.4010065644979477,
      "accuracy": 0.06764584195283409
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_all_tokens",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.2721846265097459,
      "accuracy": 0.0897029702970297
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_decision_tokens_only",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.2409456493332982,
      "accuracy": 0.46863636363636363
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_decision_tokens_only",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.21231256052851677,
      "accuracy": 0.4853932584269663
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_decision_tokens_only",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.23170064017176628,
      "accuracy": 0.44870305845915603
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_decision_tokens_only",
      "family": "listops",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 1.3692205734550953,
      "accuracy": 0.20945907993034882
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_decision_tokens_only",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.19689467176795006,
      "accuracy": 0.10287130758107829
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_decision_tokens_only",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.2792850360274315,
      "accuracy": 0.06708595387840671
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_decision_tokens_only",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.4010065644979477,
      "accuracy": 0.06764584195283409
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_decision_tokens_only",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.2721846265097459,
      "accuracy": 0.0897029702970297
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_final_tokens_only",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.2409456493332982,
      "accuracy": 0.46863636363636363
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_final_tokens_only",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.21231256052851677,
      "accuracy": 0.4853932584269663
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_final_tokens_only",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.23170064017176628,
      "accuracy": 0.44870305845915603
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_final_tokens_only",
      "family": "listops",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 1.3692205734550953,
      "accuracy": 0.20945907993034882
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_final_tokens_only",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.19689467176795006,
      "accuracy": 0.10287130758107829
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_final_tokens_only",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.2792850360274315,
      "accuracy": 0.06708595387840671
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_final_tokens_only",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.4010065644979477,
      "accuracy": 0.06764584195283409
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_final_tokens_only",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.2721846265097459,
      "accuracy": 0.0897029702970297
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_listops_scan_only",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.2409456493332982,
      "accuracy": 0.46863636363636363
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_listops_scan_only",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.21231256052851677,
      "accuracy": 0.4853932584269663
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_listops_scan_only",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.23170064017176628,
      "accuracy": 0.44870305845915603
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_listops_scan_only",
      "family": "listops",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 1.3692205734550953,
      "accuracy": 0.20945907993034882
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_listops_scan_only",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.19689467176795006,
      "accuracy": 0.10287130758107829
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_listops_scan_only",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.2792850360274315,
      "accuracy": 0.06708595387840671
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_listops_scan_only",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.4010065644979477,
      "accuracy": 0.06764584195283409
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_listops_scan_only",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.2721846265097459,
      "accuracy": 0.0897029702970297
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_scan_only",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.2409456493332982,
      "accuracy": 0.46863636363636363
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_scan_only",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.21231256052851677,
      "accuracy": 0.4853932584269663
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_scan_only",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.23170064017176628,
      "accuracy": 0.44870305845915603
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_scan_only",
      "family": "listops",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 1.3692205734550953,
      "accuracy": 0.20945907993034882
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_scan_only",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.19689467176795006,
      "accuracy": 0.10287130758107829
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_scan_only",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.2792850360274315,
      "accuracy": 0.06708595387840671
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_scan_only",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.4010065644979477,
      "accuracy": 0.06764584195283409
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_scan_only",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.2721846265097459,
      "accuracy": 0.0897029702970297
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_listops_only",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.2409456493332982,
      "accuracy": 0.46863636363636363
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_listops_only",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.21231256052851677,
      "accuracy": 0.4853932584269663
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_listops_only",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.23170064017176628,
      "accuracy": 0.44870305845915603
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_listops_only",
      "family": "listops",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 1.3692205734550953,
      "accuracy": 0.20945907993034882
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_listops_only",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.19689467176795006,
      "accuracy": 0.10287130758107829
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_listops_only",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.2792850360274315,
      "accuracy": 0.06708595387840671
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_listops_only",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.4010065644979477,
      "accuracy": 0.06764584195283409
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_listops_only",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.2721846265097459,
      "accuracy": 0.0897029702970297
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_dyck_final_state_only",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.2409456493332982,
      "accuracy": 0.46863636363636363
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_dyck_final_state_only",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.21231256052851677,
      "accuracy": 0.4853932584269663
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_dyck_final_state_only",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.23170064017176628,
      "accuracy": 0.44870305845915603
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_dyck_final_state_only",
      "family": "listops",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 1.3692205734550953,
      "accuracy": 0.20945907993034882
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_dyck_final_state_only",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.19689467176795006,
      "accuracy": 0.10287130758107829
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_dyck_final_state_only",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.2792850360274315,
      "accuracy": 0.06708595387840671
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_dyck_final_state_only",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.4010065644979477,
      "accuracy": 0.06764584195283409
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8__scope__aux_dyck_final_state_only",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.2721846265097459,
      "accuracy": 0.0897029702970297
    }
  ],
  "specialization_metrics": {
    "expert_utilization": 1.0,
    "expert_gradient_norm_by_expert": {},
    "expert_output_norm_by_expert": {}
  }
}
```