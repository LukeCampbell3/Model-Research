# PVR-EC Training Dynamics Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-09T01:58:56.339003",
    "run_id": "algo_20260609_015636_benchmark-lite",
    "git_commit": "aff470f9ed548af833e78f9fb075ed1fa78a9af1",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 42,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode benchmark-lite --scale small --sample-limit 1000 --train-steps 500 --seed 42 --families clrs,listops,scan,dyck --device cuda --amp --models dense_baseline,fixed_moe_vectorized,pvr_full,pvr_full_fixed_owner_e0,pvr_full_expert_delta_scale_4 --output-dir evaluation/benchmark_results/pvr_family_preservation_known_failures",
    "model_variants": [
      "dense_baseline",
      "fixed_moe_vectorized",
      "pvr_full",
      "pvr_full_fixed_owner_e0",
      "pvr_full_expert_delta_scale_4"
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
  "loss_curve": [
    {
      "model": "dense_baseline",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1864786148071289,
      "eval_loss": 0.30445483326911926,
      "accuracy": 0.06636363636363636
    },
    {
      "model": "dense_baseline",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1864786148071289,
      "eval_loss": 0.2642211178317666,
      "accuracy": 0.09036073329390892
    },
    {
      "model": "dense_baseline",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1864786148071289,
      "eval_loss": 0.3168967980891466,
      "accuracy": 0.062137049941927994
    },
    {
      "model": "dense_baseline",
      "family": "listops",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1864786148071289,
      "eval_loss": 1.5325019508600235,
      "accuracy": 0.06462393978542942
    },
    {
      "model": "dense_baseline",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1864786148071289,
      "eval_loss": 0.28982960246503353,
      "accuracy": 0.030778764718033463
    },
    {
      "model": "dense_baseline",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1864786148071289,
      "eval_loss": 0.4012259393930435,
      "accuracy": 0.03504043126684636
    },
    {
      "model": "dense_baseline",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1864786148071289,
      "eval_loss": 0.5708926282823086,
      "accuracy": 0.01737691352916839
    },
    {
      "model": "dense_baseline",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1864786148071289,
      "eval_loss": 0.39861596127351123,
      "accuracy": 0.041782178217821785
    },
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
      "model": "pvr_full",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18775048851966858,
      "eval_loss": 0.3074029963463545,
      "accuracy": 0.1378181818181818
    },
    {
      "model": "pvr_full",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18775048851966858,
      "eval_loss": 0.28325783275067806,
      "accuracy": 0.07344766410408042
    },
    {
      "model": "pvr_full",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18775048851966858,
      "eval_loss": 0.3238312490284443,
      "accuracy": 0.08091366627951994
    },
    {
      "model": "pvr_full",
      "family": "listops",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18775048851966858,
      "eval_loss": 1.6209645047783852,
      "accuracy": 0.11464359939336068
    },
    {
      "model": "pvr_full",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18775048851966858,
      "eval_loss": 0.21884552482515574,
      "accuracy": 0.0
    },
    {
      "model": "pvr_full",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18775048851966858,
      "eval_loss": 0.3002347759902477,
      "accuracy": 0.0
    },
    {
      "model": "pvr_full",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18775048851966858,
      "eval_loss": 0.4245618898421526,
      "accuracy": 0.0
    },
    {
      "model": "pvr_full",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18775048851966858,
      "eval_loss": 0.29722652584314346,
      "accuracy": 0.0007920792079207921
    },
    {
      "model": "pvr_full_fixed_owner_e0",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1881854236125946,
      "eval_loss": 0.31244483031332493,
      "accuracy": 0.11427272727272728
    },
    {
      "model": "pvr_full_fixed_owner_e0",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1881854236125946,
      "eval_loss": 0.2841526158154011,
      "accuracy": 0.10147841513897102
    },
    {
      "model": "pvr_full_fixed_owner_e0",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1881854236125946,
      "eval_loss": 0.3302482310682535,
      "accuracy": 0.08236546651180797
    },
    {
      "model": "pvr_full_fixed_owner_e0",
      "family": "listops",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1881854236125946,
      "eval_loss": 1.7004116885364056,
      "accuracy": 0.07057799247317868
    },
    {
      "model": "pvr_full_fixed_owner_e0",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1881854236125946,
      "eval_loss": 0.21699993591755629,
      "accuracy": 0.0
    },
    {
      "model": "pvr_full_fixed_owner_e0",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1881854236125946,
      "eval_loss": 0.2974763661623001,
      "accuracy": 0.0
    },
    {
      "model": "pvr_full_fixed_owner_e0",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1881854236125946,
      "eval_loss": 0.42559670843183994,
      "accuracy": 0.0
    },
    {
      "model": "pvr_full_fixed_owner_e0",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1881854236125946,
      "eval_loss": 0.2957934613029162,
      "accuracy": 0.0007920792079207921
    },
    {
      "model": "pvr_full_expert_delta_scale_4",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.19066591560840607,
      "eval_loss": 0.30516638047993183,
      "accuracy": 0.14481818181818182
    },
    {
      "model": "pvr_full_expert_delta_scale_4",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.19066591560840607,
      "eval_loss": 0.28202829137444496,
      "accuracy": 0.10065050266114725
    },
    {
      "model": "pvr_full_expert_delta_scale_4",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.19066591560840607,
      "eval_loss": 0.3265083581209183,
      "accuracy": 0.07994579945799458
    },
    {
      "model": "pvr_full_expert_delta_scale_4",
      "family": "listops",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.19066591560840607,
      "eval_loss": 1.6789878457784653,
      "accuracy": 0.07479076560130316
    },
    {
      "model": "pvr_full_expert_delta_scale_4",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.19066591560840607,
      "eval_loss": 0.21670475415885448,
      "accuracy": 0.0
    },
    {
      "model": "pvr_full_expert_delta_scale_4",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.19066591560840607,
      "eval_loss": 0.2968834191560745,
      "accuracy": 0.0
    },
    {
      "model": "pvr_full_expert_delta_scale_4",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.19066591560840607,
      "eval_loss": 0.4244465231895447,
      "accuracy": 0.0
    },
    {
      "model": "pvr_full_expert_delta_scale_4",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.19066591560840607,
      "eval_loss": 0.2950296724836032,
      "accuracy": 0.0015841584158415843
    }
  ],
  "specialization_metrics": {
    "expert_utilization": 0.6,
    "expert_gradient_norm_by_expert": {},
    "expert_output_norm_by_expert": {}
  }
}
```