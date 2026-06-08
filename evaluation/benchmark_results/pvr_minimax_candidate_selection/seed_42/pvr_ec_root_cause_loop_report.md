# PVR-EC Root Cause Loop Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-07T23:49:17.579238",
    "run_id": "algo_20260607_234431_benchmark-lite",
    "git_commit": "51e443da02bdc0a13c33b86368b863343ae036a2",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 42,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode benchmark-lite --scale small --sample-limit 1000 --train-steps 500 --seed-list 42,123,777,2026,9001 --device cuda --amp --models fixed_moe_vectorized,pvr_ec_deploy_top1,pvr_ec_ownership_top1_final_candidate_v1 --enable-ownership-map --ownership-map-mode frozen --run-minimax-candidate-selection --minimax-variants v1,v1_1_logit_norm_medium,sparse_ce_0_03_plus_logit_norm_light,sparse_ce_0_05_plus_logit_norm_light,sparse_ce_0_05_plus_logit_norm_medium,sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light,sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light,sparse_ce_0_03_plus_temperature_T_1_2,sparse_ce_0_05_plus_temperature_T_1_2 --output-dir evaluation/benchmark_results/pvr_minimax_candidate_selection",
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
      "dyck",
      "listops",
      "scan"
    ],
    "pvr_expert_delta_scale": null,
    "pvr_expert_delta_scale_schedule": "constant",
    "pvr_expert_delta_scale_start": null,
    "pvr_expert_delta_scale_end": null,
    "pvr_expert_delta_scale_warmup_steps": null,
    "pvr_expert_delta_scale_hold_steps": null,
    "pvr_expert_delta_scale_decay": null,
    "root_cause_flags": {
      "run_minimax_candidate_selection": true
    },
    "diagnostic_sweeps": {
      "train_steps_list": [
        500
      ],
      "seed_list": [
        42
      ],
      "batch_size_list": [
        1,
        32
      ],
      "seq_len_list": [
        64
      ],
      "shape_pairs": [],
      "max_train_seconds": null,
      "repeatability_repair_variants": [],
      "calibration_repair_variants": [],
      "minimax_variants": [
        "v1",
        "v1_1_logit_norm_medium",
        "sparse_ce_0_03_plus_logit_norm_light",
        "sparse_ce_0_05_plus_logit_norm_light",
        "sparse_ce_0_05_plus_logit_norm_medium",
        "sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
        "sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
        "sparse_ce_0_03_plus_temperature_T_1_2",
        "sparse_ce_0_05_plus_temperature_T_1_2"
      ],
      "stability_repair_variants": []
    },
    "source": "trained_benchmark"
  },
  "status": "PVR_EC_ROOT_CAUSE_INCONCLUSIVE",
  "statuses": [
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
      "label": "root_cause",
      "value": "insufficient clean evidence"
    }
  ]
}
```