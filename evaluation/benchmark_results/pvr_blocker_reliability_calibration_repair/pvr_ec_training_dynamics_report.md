# PVR-EC Training Dynamics Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-07T19:47:02.580018",
    "run_id": "algo_20260607_194114_benchmark-lite",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 42,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode benchmark-lite --scale small --sample-limit 1000 --train-steps 500 --device cuda --amp --models fixed_moe_vectorized,pvr_ec_deploy_top1,pvr_ec_ownership_top1_final_candidate_v1 --enable-ownership-map --ownership-map-mode frozen --run-reliability-calibration-repair --calibration-repair-variants final_candidate_v1,posthoc_temperature_T_1_1,posthoc_temperature_T_1_2,posthoc_temperature_T_1_3,posthoc_temperature_T_1_5,logit_norm_penalty_medium,wrong_suppress_0_01_plus_logit_norm_light,sparse_ce_0_03_plus_logit_norm_light,sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light --output-dir evaluation/benchmark_results/pvr_blocker_reliability_calibration_repair",
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
      "run_family_regression_gate": false,
      "run_quality_per_ms_memory_gate": false,
      "run_reliability_proxy_gate": false,
      "run_repeatability_collapse_isolation": false,
      "run_repeatability_repair_sweep": false,
      "run_qpm_shape_regression_analysis": false,
      "run_qpm_memory_repair": false,
      "run_reliability_calibration_repair": true,
      "run_final_candidate_revalidation": false
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
      "repeatability_repair_variants": [],
      "calibration_repair_variants": [
        "final_candidate_v1",
        "posthoc_temperature_T_1_1",
        "posthoc_temperature_T_1_2",
        "posthoc_temperature_T_1_3",
        "posthoc_temperature_T_1_5",
        "logit_norm_penalty_medium",
        "wrong_suppress_0_01_plus_logit_norm_light",
        "sparse_ce_0_03_plus_logit_norm_light",
        "sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light"
      ],
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
      "train_loss": 0.13691090047359467,
      "eval_loss": 0.21306014526635408,
      "accuracy": 0.4970909090909091
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.13691090047359467,
      "eval_loss": 0.1945193037390709,
      "accuracy": 0.524896510940272
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.13691090047359467,
      "eval_loss": 0.195757276378572,
      "accuracy": 0.5387146728610144
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "listops",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.13691090047359467,
      "eval_loss": 1.357865795493126,
      "accuracy": 0.22010335336741
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.13691090047359467,
      "eval_loss": 0.1904891598969698,
      "accuracy": 0.1043172898161537
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.13691090047359467,
      "eval_loss": 0.2717258520424366,
      "accuracy": 0.07577118897873615
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.13691090047359467,
      "eval_loss": 0.41223434545099735,
      "accuracy": 0.029271824575920563
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.13691090047359467,
      "eval_loss": 0.2756502317885558,
      "accuracy": 0.07366336633663366
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
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__final_candidate_v1",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063812971115,
      "eval_loss": 0.24142222199589014,
      "accuracy": 0.49918181818181817
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__final_candidate_v1",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063812971115,
      "eval_loss": 0.20873628836125135,
      "accuracy": 0.5117681845062093
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__final_candidate_v1",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063812971115,
      "eval_loss": 0.2305377433076501,
      "accuracy": 0.49661246612466126
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__final_candidate_v1",
      "family": "listops",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063812971115,
      "eval_loss": 1.329617828130722,
      "accuracy": 0.22673144975565915
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__final_candidate_v1",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063812971115,
      "eval_loss": 0.1980981295928359,
      "accuracy": 0.08572608965089858
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__final_candidate_v1",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063812971115,
      "eval_loss": 0.2804417796432972,
      "accuracy": 0.055705300988319856
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__final_candidate_v1",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063812971115,
      "eval_loss": 0.40413068048655987,
      "accuracy": 0.03568473314025652
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__final_candidate_v1",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063812971115,
      "eval_loss": 0.2732982970774174,
      "accuracy": 0.06158415841584158
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__posthoc_temperature_T_1_1",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.14816072583198547,
      "eval_loss": 0.2511328896507621,
      "accuracy": 0.49927272727272726
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__posthoc_temperature_T_1_1",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.14816072583198547,
      "eval_loss": 0.21745024621486664,
      "accuracy": 0.51224127735068
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__posthoc_temperature_T_1_1",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.14816072583198547,
      "eval_loss": 0.23843637853860855,
      "accuracy": 0.4980642663569493
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__posthoc_temperature_T_1_1",
      "family": "listops",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.14816072583198547,
      "eval_loss": 1.3249500095844269,
      "accuracy": 0.2263944279054092
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__posthoc_temperature_T_1_1",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.14816072583198547,
      "eval_loss": 0.20524254348129034,
      "accuracy": 0.08572608965089858
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__posthoc_temperature_T_1_1",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.14816072583198547,
      "eval_loss": 0.28729262575507164,
      "accuracy": 0.056004791853848455
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__posthoc_temperature_T_1_1",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.14816072583198547,
      "eval_loss": 0.4109709057956934,
      "accuracy": 0.0358916011584609
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__posthoc_temperature_T_1_1",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.14816072583198547,
      "eval_loss": 0.2806572603682677,
      "accuracy": 0.05900990099009901
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__posthoc_temperature_T_1_2",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063961982727,
      "eval_loss": 0.2684176620095968,
      "accuracy": 0.49918181818181817
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__posthoc_temperature_T_1_2",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063961982727,
      "eval_loss": 0.23377175815403461,
      "accuracy": 0.5117681845062093
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__posthoc_temperature_T_1_2",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063961982727,
      "eval_loss": 0.2541435621678829,
      "accuracy": 0.49661246612466126
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__posthoc_temperature_T_1_2",
      "family": "listops",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063961982727,
      "eval_loss": 1.3323042653501034,
      "accuracy": 0.22673144975565915
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__posthoc_temperature_T_1_2",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063961982727,
      "eval_loss": 0.21845487412065268,
      "accuracy": 0.08572608965089858
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__posthoc_temperature_T_1_2",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063961982727,
      "eval_loss": 0.30021874606609344,
      "accuracy": 0.055705300988319856
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__posthoc_temperature_T_1_2",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063961982727,
      "eval_loss": 0.42397673800587654,
      "accuracy": 0.03568473314025652
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__posthoc_temperature_T_1_2",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063961982727,
      "eval_loss": 0.29410430540641147,
      "accuracy": 0.06158415841584158
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__posthoc_temperature_T_1_3",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.14810779690742493,
      "eval_loss": 0.29532528296113014,
      "accuracy": 0.499
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__posthoc_temperature_T_1_3",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.14810779690742493,
      "eval_loss": 0.259494099766016,
      "accuracy": 0.5116499112950916
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__posthoc_temperature_T_1_3",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.14810779690742493,
      "eval_loss": 0.27973660454154015,
      "accuracy": 0.49680603948896634
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__posthoc_temperature_T_1_3",
      "family": "listops",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.14810779690742493,
      "eval_loss": 1.3514391109347343,
      "accuracy": 0.22678762006403416
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__posthoc_temperature_T_1_3",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.14810779690742493,
      "eval_loss": 0.24103962816298008,
      "accuracy": 0.08572608965089858
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__posthoc_temperature_T_1_3",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.14810779690742493,
      "eval_loss": 0.32243437692523,
      "accuracy": 0.055705300988319856
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__posthoc_temperature_T_1_3",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.14810779690742493,
      "eval_loss": 0.4461641777306795,
      "accuracy": 0.03568473314025652
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__posthoc_temperature_T_1_3",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.14810779690742493,
      "eval_loss": 0.3169243261218071,
      "accuracy": 0.06158415841584158
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__posthoc_temperature_T_1_5",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.14800703525543213,
      "eval_loss": 0.3889148999005556,
      "accuracy": 0.49963636363636366
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__posthoc_temperature_T_1_5",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.14800703525543213,
      "eval_loss": 0.3510359786450863,
      "accuracy": 0.516380839739799
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__posthoc_temperature_T_1_5",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.14800703525543213,
      "eval_loss": 0.37136652134358883,
      "accuracy": 0.49796747967479676
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__posthoc_temperature_T_1_5",
      "family": "listops",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.14800703525543213,
      "eval_loss": 1.4286720231175423,
      "accuracy": 0.22664719429309668
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__posthoc_temperature_T_1_5",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.14800703525543213,
      "eval_loss": 0.3265695199370384,
      "accuracy": 0.0865523652137988
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__posthoc_temperature_T_1_5",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.14800703525543213,
      "eval_loss": 0.40689612925052643,
      "accuracy": 0.055405810122791256
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__posthoc_temperature_T_1_5",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.14800703525543213,
      "eval_loss": 0.530048904940486,
      "accuracy": 0.03609846917666529
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__posthoc_temperature_T_1_5",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.14800703525543213,
      "eval_loss": 0.4026319334904353,
      "accuracy": 0.059207920792079205
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_penalty_medium",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1511673480272293,
      "eval_loss": 0.2415832867845893,
      "accuracy": 0.4769090909090909
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_penalty_medium",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1511673480272293,
      "eval_loss": 0.20936034806072712,
      "accuracy": 0.4998225901833235
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_penalty_medium",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1511673480272293,
      "eval_loss": 0.23035485576838255,
      "accuracy": 0.4626403406891212
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_penalty_medium",
      "family": "listops",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1511673480272293,
      "eval_loss": 1.3107546158134937,
      "accuracy": 0.22451272257484695
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_penalty_medium",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1511673480272293,
      "eval_loss": 0.19833189714699984,
      "accuracy": 0.08221441850857261
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_penalty_medium",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1511673480272293,
      "eval_loss": 0.28078920766711235,
      "accuracy": 0.05390835579514825
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_penalty_medium",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1511673480272293,
      "eval_loss": 0.40399773977696896,
      "accuracy": 0.03103020273065784
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_penalty_medium",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1511673480272293,
      "eval_loss": 0.2743444914619128,
      "accuracy": 0.053465346534653464
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_01_plus_logit_norm_light",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.14932295680046082,
      "eval_loss": 0.2441703863441944,
      "accuracy": 0.4812727272727273
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_01_plus_logit_norm_light",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.14932295680046082,
      "eval_loss": 0.21370423957705498,
      "accuracy": 0.5049083382613838
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_01_plus_logit_norm_light",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.14932295680046082,
      "eval_loss": 0.2341784816235304,
      "accuracy": 0.4699961285327139
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_01_plus_logit_norm_light",
      "family": "listops",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.14932295680046082,
      "eval_loss": 1.3174872882664204,
      "accuracy": 0.21662079424816041
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_01_plus_logit_norm_light",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.14932295680046082,
      "eval_loss": 0.1997331902384758,
      "accuracy": 0.07539764511464574
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_01_plus_logit_norm_light",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.14932295680046082,
      "eval_loss": 0.28254682943224907,
      "accuracy": 0.04791853848457622
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_01_plus_logit_norm_light",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.14932295680046082,
      "eval_loss": 0.40497460402548313,
      "accuracy": 0.027099710384774513
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_01_plus_logit_norm_light",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.14932295680046082,
      "eval_loss": 0.2754017983873685,
      "accuracy": 0.048712871287128715
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.16285622119903564,
      "eval_loss": 0.26534003019332886,
      "accuracy": 0.36563636363636365
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.16285622119903564,
      "eval_loss": 0.22786620538681746,
      "accuracy": 0.3348314606741573
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.16285622119903564,
      "eval_loss": 0.26019474398344755,
      "accuracy": 0.3147502903600465
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "family": "listops",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.16285622119903564,
      "eval_loss": 1.3443554043769836,
      "accuracy": 0.22358591248665954
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.16285622119903564,
      "eval_loss": 0.2005924517288804,
      "accuracy": 0.09440198306135096
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.16285622119903564,
      "eval_loss": 0.28284819796681404,
      "accuracy": 0.06229410002994909
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.16285622119903564,
      "eval_loss": 0.404697110876441,
      "accuracy": 0.046235002068680184
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.16285622119903564,
      "eval_loss": 0.27479483808080357,
      "accuracy": 0.07247524752475247
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.16354820132255554,
      "eval_loss": 0.2672253930941224,
      "accuracy": 0.3473636363636364
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.16354820132255554,
      "eval_loss": 0.229547418653965,
      "accuracy": 0.3217031342400946
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.16354820132255554,
      "eval_loss": 0.2613238897174597,
      "accuracy": 0.30226480836236935
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "listops",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.16354820132255554,
      "eval_loss": 1.3362408615648746,
      "accuracy": 0.22176037746447227
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.16354820132255554,
      "eval_loss": 0.20329942367970943,
      "accuracy": 0.09151001859120017
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.16354820132255554,
      "eval_loss": 0.2857021242380142,
      "accuracy": 0.0631925726265349
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.16354820132255554,
      "eval_loss": 0.40837262012064457,
      "accuracy": 0.04468349193214729
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.16354820132255554,
      "eval_loss": 0.2789803519845009,
      "accuracy": 0.06574257425742575
    }
  ],
  "specialization_metrics": {
    "expert_utilization": 0.9090909090909091,
    "expert_gradient_norm_by_expert": {},
    "expert_output_norm_by_expert": {}
  }
}
```