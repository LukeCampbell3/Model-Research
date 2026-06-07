# PVR-EC Root Cause Loop Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-06T18:57:26.691549",
    "run_id": "algo_20260606_185724_inference-only",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "N/A",
    "cuda_available": false,
    "gpu_name": "",
    "amp_enabled": false,
    "seed": 42,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode inference-only --scale tiny --seed 42 --models fixed_moe_vectorized,pvr_ec_deploy_top1,pvr_ec_ownership_top1_delta_medium,pvr_ec_ownership_top1_full_expert_ffn_control --run-latency-stability-diagnostic --batch-size-list 1,8 --seq-len-list 16,64 --warmup-steps 3 --timed-steps 10 --output-dir evaluation/benchmark_results/docker_pvr_ec_latency_stability_actual",
    "model_variants": [
      "fixed_moe_vectorized",
      "pvr_ec_deploy_top1",
      "pvr_ec_ownership_top1_delta_medium",
      "pvr_ec_ownership_top1_full_expert_ffn_control"
    ],
    "batch_sizes": [
      1,
      8
    ],
    "sequence_lengths": [
      16,
      64
    ],
    "train_steps": 500,
    "sample_limit": null,
    "mode": "inference-only",
    "scale": "tiny",
    "families": [
      "clrs",
      "listops",
      "scan",
      "dyck"
    ],
    "root_cause_flags": {
      "run_root_baseline_matrix": false,
      "run_training_dynamics_diagnostic": false,
      "run_ownership_integration_diagnostic": false,
      "run_shared_sparse_ablation": false,
      "run_loss_calibration_diagnostic": false,
      "run_task_fit_diagnostic": false,
      "run_latency_stability_diagnostic": true
    },
    "diagnostic_sweeps": {
      "train_steps_list": [],
      "seed_list": [
        42
      ],
      "ownership_schedule_sweep": [],
      "loss_schedule_sweep": [],
      "task_loss_schedule_sweep": [],
      "batch_size_list": [
        1,
        8
      ],
      "seq_len_list": [
        16,
        64
      ]
    },
    "source": "inference_only"
  },
  "status": "PVR_EC_ROOT_CAUSE_INCONCLUSIVE",
  "statuses": [
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