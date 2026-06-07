# PVR-EC Training Dynamics Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-07T03:30:48.781904",
    "run_id": "algo_20260607_032819_benchmark-lite",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 42,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode benchmark-lite --scale small --sample-limit 1000 --train-steps 500 --device cuda --amp --models fixed_moe_vectorized,pvr_ec_deploy_top1,pvr_ec_ownership_top1_scale_schedule_1_to_8,pvr_ec_ownership_top1_best_sparse_logit_repair --enable-ownership-map --ownership-map-mode frozen --run-sparse-direction-transfer-confirmation --output-dir evaluation/benchmark_results/pvr_sparse_direction_transfer_confirmation",
    "model_variants": [
      "fixed_moe_vectorized",
      "pvr_ec_deploy_top1",
      "pvr_ec_ownership_top1_scale_schedule_1_to_8",
      "pvr_ec_ownership_top1_best_sparse_logit_repair"
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
      "run_sparse_auxiliary_scope_sweep": false,
      "run_sparse_direction_transfer_confirmation": true
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
      "sparse_aux_scopes": []
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
      "train_loss": 0.13683609664440155,
      "eval_loss": 0.21254643518477678,
      "accuracy": 0.49845454545454543
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.13683609664440155,
      "eval_loss": 0.19413983263075352,
      "accuracy": 0.524896510940272
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.13683609664440155,
      "eval_loss": 0.19540273770689964,
      "accuracy": 0.54045683313976
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "listops",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.13683609664440155,
      "eval_loss": 1.3568207398056984,
      "accuracy": 0.22077739706790991
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.13683609664440155,
      "eval_loss": 0.19047189597040415,
      "accuracy": 0.1043172898161537
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.13683609664440155,
      "eval_loss": 0.27171850576996803,
      "accuracy": 0.07577118897873615
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.13683609664440155,
      "eval_loss": 0.4121997430920601,
      "accuracy": 0.02989242863053372
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.13683609664440155,
      "eval_loss": 0.2755616481105487,
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
    },
    {
      "model": "pvr_ec_ownership_top1_best_sparse_logit_repair",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.2409456493332982,
      "accuracy": 0.46863636363636363
    },
    {
      "model": "pvr_ec_ownership_top1_best_sparse_logit_repair",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.21231256052851677,
      "accuracy": 0.4853932584269663
    },
    {
      "model": "pvr_ec_ownership_top1_best_sparse_logit_repair",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.23170064017176628,
      "accuracy": 0.44870305845915603
    },
    {
      "model": "pvr_ec_ownership_top1_best_sparse_logit_repair",
      "family": "listops",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 1.3692205734550953,
      "accuracy": 0.20945907993034882
    },
    {
      "model": "pvr_ec_ownership_top1_best_sparse_logit_repair",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.19689467176795006,
      "accuracy": 0.10287130758107829
    },
    {
      "model": "pvr_ec_ownership_top1_best_sparse_logit_repair",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.2792850360274315,
      "accuracy": 0.06708595387840671
    },
    {
      "model": "pvr_ec_ownership_top1_best_sparse_logit_repair",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.4010065644979477,
      "accuracy": 0.06764584195283409
    },
    {
      "model": "pvr_ec_ownership_top1_best_sparse_logit_repair",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.151417076587677,
      "eval_loss": 0.2721846265097459,
      "accuracy": 0.0897029702970297
    }
  ],
  "specialization_metrics": {
    "expert_utilization": 0.75,
    "expert_gradient_norm_by_expert": {},
    "expert_output_norm_by_expert": {}
  }
}
```