# PVR-EC Training Dynamics Report

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
  "loss_curve": [
    {
      "model": "fixed_moe_vectorized",
      "family": "unknown",
      "seed": 42,
      "train_steps": 500,
      "train_loss": null,
      "eval_loss": 5.507466793060303,
      "accuracy": 0.0
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "unknown",
      "seed": 42,
      "train_steps": 500,
      "train_loss": null,
      "eval_loss": 5.577270030975342,
      "accuracy": 0.0
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "unknown",
      "seed": 42,
      "train_steps": 500,
      "train_loss": null,
      "eval_loss": 5.5558061599731445,
      "accuracy": 0.0
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "unknown",
      "seed": 42,
      "train_steps": 500,
      "train_loss": null,
      "eval_loss": 5.5661163330078125,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "unknown",
      "seed": 42,
      "train_steps": 500,
      "train_loss": null,
      "eval_loss": 5.487056732177734,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "unknown",
      "seed": 42,
      "train_steps": 500,
      "train_loss": null,
      "eval_loss": 5.539806842803955,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "unknown",
      "seed": 42,
      "train_steps": 500,
      "train_loss": null,
      "eval_loss": 5.547452449798584,
      "accuracy": 0.0078125
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "unknown",
      "seed": 42,
      "train_steps": 500,
      "train_loss": null,
      "eval_loss": 5.558089256286621,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_medium",
      "family": "unknown",
      "seed": 42,
      "train_steps": 500,
      "train_loss": null,
      "eval_loss": 5.572970390319824,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_medium",
      "family": "unknown",
      "seed": 42,
      "train_steps": 500,
      "train_loss": null,
      "eval_loss": 5.539572238922119,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_medium",
      "family": "unknown",
      "seed": 42,
      "train_steps": 500,
      "train_loss": null,
      "eval_loss": 5.564937114715576,
      "accuracy": 0.0078125
    },
    {
      "model": "pvr_ec_ownership_top1_delta_medium",
      "family": "unknown",
      "seed": 42,
      "train_steps": 500,
      "train_loss": null,
      "eval_loss": 5.5592122077941895,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_full_expert_ffn_control",
      "family": "unknown",
      "seed": 42,
      "train_steps": 500,
      "train_loss": null,
      "eval_loss": 5.428894519805908,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_full_expert_ffn_control",
      "family": "unknown",
      "seed": 42,
      "train_steps": 500,
      "train_loss": null,
      "eval_loss": 5.545907020568848,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_full_expert_ffn_control",
      "family": "unknown",
      "seed": 42,
      "train_steps": 500,
      "train_loss": null,
      "eval_loss": 5.5828046798706055,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_full_expert_ffn_control",
      "family": "unknown",
      "seed": 42,
      "train_steps": 500,
      "train_loss": null,
      "eval_loss": 5.556907653808594,
      "accuracy": 0.00390625
    }
  ],
  "specialization_metrics": {
    "expert_utilization": null,
    "expert_gradient_norm_by_expert": {},
    "expert_output_norm_by_expert": {}
  }
}
```