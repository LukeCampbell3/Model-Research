# PVR-EC Training Dynamics Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-07T02:34:22.246212",
    "run_id": "algo_20260607_023350_benchmark-lite",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 42,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode benchmark-lite --scale small --sample-limit 1000 --train-steps 500 --device cuda --amp --models pvr_ec_ownership_top1_scale_schedule_1_to_8 --enable-ownership-map --ownership-map-mode frozen --run-output-readout-diagnostic --readout-variants baseline_output_head,shared_only_output_head,sparse_only_output_head,combined_output_head,concat_shared_sparse_readout,gated_shared_sparse_readout,final_state_readout,mean_pool_readout,attention_pool_readout_diagnostic --output-dir evaluation/benchmark_results/pvr_output_readout_diagnostic",
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
      "run_output_readout_diagnostic": true,
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
      "readout_variants": [
        "baseline_output_head",
        "shared_only_output_head",
        "sparse_only_output_head",
        "combined_output_head",
        "concat_shared_sparse_readout",
        "gated_shared_sparse_readout",
        "final_state_readout",
        "mean_pool_readout",
        "attention_pool_readout_diagnostic"
      ],
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
  "loss_curve": [
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18761539459228516,
      "eval_loss": 0.30222402699291706,
      "accuracy": 0.13763636363636364
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18761539459228516,
      "eval_loss": 0.27271723560988903,
      "accuracy": 0.10313424009461857
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18761539459228516,
      "eval_loss": 0.3158093597739935,
      "accuracy": 0.09872241579558652
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8",
      "family": "listops",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18761539459228516,
      "eval_loss": 1.6250091530382633,
      "accuracy": 0.09487165084536314
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18761539459228516,
      "eval_loss": 0.20576439518481493,
      "accuracy": 0.023755422433381534
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18761539459228516,
      "eval_loss": 0.28662920370697975,
      "accuracy": 0.01078167115902965
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18761539459228516,
      "eval_loss": 0.41453822143375874,
      "accuracy": 0.007550682664460074
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18761539459228516,
      "eval_loss": 0.28517769773801166,
      "accuracy": 0.007920792079207921
    }
  ],
  "specialization_metrics": {
    "expert_utilization": 1.0,
    "expert_gradient_norm_by_expert": {},
    "expert_output_norm_by_expert": {}
  }
}
```