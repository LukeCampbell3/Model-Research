# PVR-EC Root Cause Loop Report

**Status:** PVR_EC_EXPERT_CAPACITY_NOT_PRIMARY_BLOCKER

**Statuses:** PVR_EC_DO_NOT_PROMOTE, PVR_EC_EXPERT_CAPACITY_NOT_PRIMARY_BLOCKER, PVR_EC_LATENCY_VARIANCE_BLOCKER, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-06T18:57:39.609682",
    "run_id": "algo_20260606_185739_smoke",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "N/A",
    "cuda_available": false,
    "gpu_name": "",
    "amp_enabled": false,
    "seed": 42,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --summarize-pvr-root-cause --input-dirs evaluation/benchmark_results/docker_pvr_ec_root_cause_actual,evaluation/benchmark_results/docker_pvr_ec_latency_stability_actual,evaluation/benchmark_results/docker_capacity_ladder_real_full_ffn,evaluation/benchmark_results/docker_capacity_latency_real_full_ffn --output-dir evaluation/benchmark_results/docker_pvr_ec_root_cause_summary_actual",
    "model_variants": [
      "dense_baseline",
      "fixed_moe",
      "fixed_moe_looped_reference",
      "fixed_moe_vectorized",
      "adaptive_moe",
      "looped_moe",
      "full_system",
      "pvr_ec",
      "pvr_ec_matched",
      "pvr_ec_fixed_top2",
      "pvr_ec_no_prototypes",
      "pvr_ec_no_load_bias",
      "pvr_ec_no_extra_experts",
      "pvr_ec_deploy_top1",
      "pvr_ec_deploy_top2",
      "pvr_ec_deploy_bucketed",
      "pvr_ec_deploy_dense_masked_control",
      "pvr_ec_ownership_top1_frozen_candidate",
      "pvr_ec_ownership_top1_delta_small",
      "pvr_ec_ownership_top1_delta_medium",
      "pvr_ec_ownership_top1_delta_large",
      "pvr_ec_ownership_top1_full_expert_ffn_control",
      "pvr_ec_ownership_top1_rank_8",
      "pvr_ec_ownership_top1_rank_16",
      "pvr_ec_ownership_top1_rank_32",
      "pvr_ec_ownership_top1_rank_64",
      "pvr_ec_ownership_top1_rank_128",
      "pvr_ec_ownership_top1_micro_ffn_0_25x",
      "pvr_ec_ownership_top1_micro_ffn_0_5x",
      "pvr_ec_ownership_top1_micro_ffn_1_0x",
      "pvr_ec_ownership_top1_delta_rank_8",
      "pvr_ec_ownership_top1_delta_rank_16",
      "pvr_ec_ownership_top1_delta_rank_32",
      "pvr_ec_ownership_top1_delta_rank_64",
      "pvr_ec_ownership_top1_delta_rank_128"
    ],
    "batch_sizes": [
      1,
      32
    ],
    "sequence_lengths": [
      64
    ],
    "train_steps": 30,
    "sample_limit": null,
    "mode": "smoke",
    "scale": "small",
    "families": [
      "clrs",
      "listops",
      "scan",
      "dyck"
    ],
    "input_dirs": [
      "evaluation/benchmark_results/docker_pvr_ec_root_cause_actual",
      "evaluation/benchmark_results/docker_pvr_ec_latency_stability_actual",
      "evaluation/benchmark_results/docker_capacity_ladder_real_full_ffn",
      "evaluation/benchmark_results/docker_capacity_latency_real_full_ffn"
    ],
    "loaded_reports": [
      "evaluation/benchmark_results/docker_pvr_ec_root_cause_actual/per_dataset_metrics.json",
      "evaluation/benchmark_results/docker_pvr_ec_root_cause_actual/capacity_fairness_matrix_report.json",
      "evaluation/benchmark_results/docker_pvr_ec_root_cause_actual/pvr_ec_root_baseline_matrix.json",
      "evaluation/benchmark_results/docker_pvr_ec_latency_stability_actual/inference_latency_matrix.json",
      "evaluation/benchmark_results/docker_pvr_ec_latency_stability_actual/capacity_fairness_matrix_report.json",
      "evaluation/benchmark_results/docker_pvr_ec_latency_stability_actual/pvr_ec_root_baseline_matrix.json",
      "evaluation/benchmark_results/docker_capacity_ladder_real_full_ffn/per_dataset_metrics.json",
      "evaluation/benchmark_results/docker_capacity_ladder_real_full_ffn/capacity_fairness_matrix_report.json",
      "evaluation/benchmark_results/docker_capacity_latency_real_full_ffn/inference_latency_matrix.json",
      "evaluation/benchmark_results/docker_capacity_latency_real_full_ffn/capacity_fairness_matrix_report.json"
    ],
    "missing_dirs": [],
    "root_cause_flags": {
      "summarize_pvr_root_cause": true
    },
    "diagnostic_sweeps": {},
    "source": "root_summary"
  },
  "status": "PVR_EC_EXPERT_CAPACITY_NOT_PRIMARY_BLOCKER",
  "statuses": [
    "PVR_EC_DO_NOT_PROMOTE",
    "PVR_EC_EXPERT_CAPACITY_NOT_PRIMARY_BLOCKER",
    "PVR_EC_LATENCY_VARIANCE_BLOCKER",
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
      "label": "latency_p95_p50_ratio",
      "value": 6.2619675166427236
    },
    {
      "label": "full_expert_vs_best_smaller_loss",
      "full_best": 0.23134075663983822,
      "smaller_best": 0.2251367885619402
    }
  ]
}
```