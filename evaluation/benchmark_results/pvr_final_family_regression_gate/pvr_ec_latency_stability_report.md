# PVR-EC Latency Stability Report

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
  "by_model": {
    "fixed_moe_vectorized": {
      "count": 8,
      "avg_loss": 0.38860768983916694,
      "avg_accuracy": 0.25857819999606313,
      "avg_train_loss": 0.13683611154556274,
      "latency_p50_ms": 939.2883777618408,
      "latency_p95_ms": 939.2883777618408,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_deploy_top1": {
      "count": 8,
      "avg_loss": 0.45097945421002805,
      "avg_accuracy": 0.0771500010285979,
      "avg_train_loss": 0.17677822709083557,
      "latency_p50_ms": 650.0885784626007,
      "latency_p95_ms": 650.0885784626007,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1": {
      "count": 8,
      "avg_loss": 0.39578524367728585,
      "avg_accuracy": 0.24662427509545803,
      "avg_train_loss": 0.1481063961982727,
      "latency_p50_ms": 578.8986384868622,
      "latency_p95_ms": 578.8986384868622,
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
      "latency_p50_ms": 1098.1824398040771,
      "latency_p95_ms": 1098.1824398040771,
      "latency_p99_ms": 1098.1824398040771,
      "latency_max_ms": 1098.1824398040771,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1020.3201770782471,
      "latency_p95_ms": 1020.3201770782471,
      "latency_p99_ms": 1020.3201770782471,
      "latency_max_ms": 1020.3201770782471,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1031.6550731658936,
      "latency_p95_ms": 1031.6550731658936,
      "latency_p99_ms": 1031.6550731658936,
      "latency_max_ms": 1031.6550731658936,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1027.371883392334,
      "latency_p95_ms": 1027.371883392334,
      "latency_p99_ms": 1027.371883392334,
      "latency_max_ms": 1027.371883392334,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1030.0703048706055,
      "latency_p95_ms": 1030.0703048706055,
      "latency_p99_ms": 1030.0703048706055,
      "latency_max_ms": 1030.0703048706055,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 513.1337642669678,
      "latency_p95_ms": 513.1337642669678,
      "latency_p99_ms": 513.1337642669678,
      "latency_max_ms": 513.1337642669678,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1023.7915515899658,
      "latency_p95_ms": 1023.7915515899658,
      "latency_p99_ms": 1023.7915515899658,
      "latency_max_ms": 1023.7915515899658,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 769.7818279266357,
      "latency_p95_ms": 769.7818279266357,
      "latency_p99_ms": 769.7818279266357,
      "latency_max_ms": 769.7818279266357,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 714.5943641662598,
      "latency_p95_ms": 714.5943641662598,
      "latency_p99_ms": 714.5943641662598,
      "latency_max_ms": 714.5943641662598,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 718.395471572876,
      "latency_p95_ms": 718.395471572876,
      "latency_p99_ms": 718.395471572876,
      "latency_max_ms": 718.395471572876,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 734.6100807189941,
      "latency_p95_ms": 734.6100807189941,
      "latency_p99_ms": 734.6100807189941,
      "latency_max_ms": 734.6100807189941,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 748.8114833831787,
      "latency_p95_ms": 748.8114833831787,
      "latency_p99_ms": 748.8114833831787,
      "latency_max_ms": 748.8114833831787,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 707.5200080871582,
      "latency_p95_ms": 707.5200080871582,
      "latency_p99_ms": 707.5200080871582,
      "latency_max_ms": 707.5200080871582,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 362.11204528808594,
      "latency_p95_ms": 362.11204528808594,
      "latency_p99_ms": 362.11204528808594,
      "latency_max_ms": 362.11204528808594,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 688.4210109710693,
      "latency_p95_ms": 688.4210109710693,
      "latency_p99_ms": 688.4210109710693,
      "latency_max_ms": 688.4210109710693,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 526.2441635131836,
      "latency_p95_ms": 526.2441635131836,
      "latency_p99_ms": 526.2441635131836,
      "latency_max_ms": 526.2441635131836,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 636.8598937988281,
      "latency_p95_ms": 636.8598937988281,
      "latency_p99_ms": 636.8598937988281,
      "latency_max_ms": 636.8598937988281,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 629.3888092041016,
      "latency_p95_ms": 629.3888092041016,
      "latency_p99_ms": 629.3888092041016,
      "latency_max_ms": 629.3888092041016,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 637.256383895874,
      "latency_p95_ms": 637.256383895874,
      "latency_p99_ms": 637.256383895874,
      "latency_max_ms": 637.256383895874,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 678.6220073699951,
      "latency_p95_ms": 678.6220073699951,
      "latency_p99_ms": 678.6220073699951,
      "latency_max_ms": 678.6220073699951,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 628.2696723937988,
      "latency_p95_ms": 628.2696723937988,
      "latency_p99_ms": 628.2696723937988,
      "latency_max_ms": 628.2696723937988,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 314.24546241760254,
      "latency_p95_ms": 314.24546241760254,
      "latency_p99_ms": 314.24546241760254,
      "latency_max_ms": 314.24546241760254,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 629.5676231384277,
      "latency_p95_ms": 629.5676231384277,
      "latency_p99_ms": 629.5676231384277,
      "latency_max_ms": 629.5676231384277,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 476.97925567626953,
      "latency_p95_ms": 476.97925567626953,
      "latency_p99_ms": 476.97925567626953,
      "latency_max_ms": 476.97925567626953,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    }
  ]
}
```