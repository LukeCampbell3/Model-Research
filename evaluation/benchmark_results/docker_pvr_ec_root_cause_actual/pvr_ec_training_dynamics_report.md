# PVR-EC Training Dynamics Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DO_NOT_PROMOTE, PVR_EC_EXPERT_CAPACITY_NOT_PRIMARY_BLOCKER, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-06T18:57:09.527724",
    "run_id": "algo_20260606_185440_benchmark-lite",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "N/A",
    "cuda_available": false,
    "gpu_name": "",
    "amp_enabled": false,
    "seed": 42,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode benchmark-lite --scale tiny --families clrs,listops,scan,dyck --sample-limit 128 --train-steps 50 --seed 42 --models fixed_moe_vectorized,pvr_ec_deploy_top1,pvr_ec_ownership_top1_delta_medium,pvr_ec_ownership_top1_delta_large,pvr_ec_ownership_top1_full_expert_ffn_control --enable-ownership-map --ownership-map-mode frozen_candidate --run-root-baseline-matrix --run-training-dynamics-diagnostic --run-ownership-integration-diagnostic --run-shared-sparse-ablation --run-loss-calibration-diagnostic --run-task-fit-diagnostic --output-dir evaluation/benchmark_results/docker_pvr_ec_root_cause_actual",
    "model_variants": [
      "fixed_moe_vectorized",
      "pvr_ec_deploy_top1",
      "pvr_ec_ownership_top1_delta_medium",
      "pvr_ec_ownership_top1_delta_large",
      "pvr_ec_ownership_top1_full_expert_ffn_control"
    ],
    "batch_sizes": [
      1,
      32
    ],
    "sequence_lengths": [
      64
    ],
    "train_steps": 50,
    "sample_limit": 128,
    "mode": "benchmark-lite",
    "scale": "tiny",
    "families": [
      "clrs",
      "listops",
      "scan",
      "dyck"
    ],
    "root_cause_flags": {
      "run_root_baseline_matrix": true,
      "run_training_dynamics_diagnostic": true,
      "run_ownership_integration_diagnostic": true,
      "run_shared_sparse_ablation": true,
      "run_loss_calibration_diagnostic": true,
      "run_task_fit_diagnostic": true,
      "run_latency_stability_diagnostic": false
    },
    "diagnostic_sweeps": {
      "train_steps_list": [
        50
      ],
      "seed_list": [
        42
      ],
      "ownership_schedule_sweep": [],
      "loss_schedule_sweep": [],
      "task_loss_schedule_sweep": [],
      "batch_size_list": [
        1,
        32
      ],
      "seq_len_list": [
        64
      ]
    },
    "source": "trained_benchmark"
  },
  "status": "PVR_EC_ROOT_CAUSE_INCONCLUSIVE",
  "statuses": [
    "PVR_EC_DO_NOT_PROMOTE",
    "PVR_EC_EXPERT_CAPACITY_NOT_PRIMARY_BLOCKER",
    "PVR_EC_ROOT_CAUSE_INCONCLUSIVE"
  ],
  "loss_curve": [
    {
      "model": "fixed_moe_vectorized",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 50,
      "train_loss": 3.9719300270080566,
      "eval_loss": 3.8843966722488403,
      "accuracy": 0.0
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 50,
      "train_loss": 3.9719300270080566,
      "eval_loss": 3.842640519142151,
      "accuracy": 0.0
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 50,
      "train_loss": 3.9719300270080566,
      "eval_loss": 3.865084409713745,
      "accuracy": 0.0
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "listops",
      "seed": 42,
      "train_steps": 50,
      "train_loss": 3.9719300270080566,
      "eval_loss": 4.398575782775879,
      "accuracy": 0.007493540051679587
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 50,
      "train_loss": 3.9719300270080566,
      "eval_loss": 3.7875505685806274,
      "accuracy": 0.0
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 50,
      "train_loss": 3.9719300270080566,
      "eval_loss": 3.850219964981079,
      "accuracy": 0.0
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "dyck",
      "seed": 42,
      "train_steps": 50,
      "train_loss": 3.9719300270080566,
      "eval_loss": 3.9346662759780884,
      "accuracy": 0.0
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "dyck",
      "seed": 42,
      "train_steps": 50,
      "train_loss": 3.9719300270080566,
      "eval_loss": 3.858448028564453,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 50,
      "train_loss": 4.054466724395752,
      "eval_loss": 3.9561479091644287,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 50,
      "train_loss": 4.054466724395752,
      "eval_loss": 3.9152584075927734,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 50,
      "train_loss": 4.054466724395752,
      "eval_loss": 3.9402164220809937,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "listops",
      "seed": 42,
      "train_steps": 50,
      "train_loss": 4.054466724395752,
      "eval_loss": 4.435037612915039,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 50,
      "train_loss": 4.054466724395752,
      "eval_loss": 3.865699529647827,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 50,
      "train_loss": 4.054466724395752,
      "eval_loss": 3.927276372909546,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "dyck",
      "seed": 42,
      "train_steps": 50,
      "train_loss": 4.054466724395752,
      "eval_loss": 3.9968419075012207,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "dyck",
      "seed": 42,
      "train_steps": 50,
      "train_loss": 4.054466724395752,
      "eval_loss": 3.9264070987701416,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_medium",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 50,
      "train_loss": 4.076566219329834,
      "eval_loss": 3.952233076095581,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_medium",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 50,
      "train_loss": 4.076566219329834,
      "eval_loss": 3.9130570888519287,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_medium",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 50,
      "train_loss": 4.076566219329834,
      "eval_loss": 3.9457054138183594,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_medium",
      "family": "listops",
      "seed": 42,
      "train_steps": 50,
      "train_loss": 4.076566219329834,
      "eval_loss": 4.493920803070068,
      "accuracy": 0.00516795865633075
    },
    {
      "model": "pvr_ec_ownership_top1_delta_medium",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 50,
      "train_loss": 4.076566219329834,
      "eval_loss": 3.8574278354644775,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_medium",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 50,
      "train_loss": 4.076566219329834,
      "eval_loss": 3.91726016998291,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_medium",
      "family": "dyck",
      "seed": 42,
      "train_steps": 50,
      "train_loss": 4.076566219329834,
      "eval_loss": 4.000998497009277,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_medium",
      "family": "dyck",
      "seed": 42,
      "train_steps": 50,
      "train_loss": 4.076566219329834,
      "eval_loss": 3.92809796333313,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_large",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 50,
      "train_loss": 4.054471492767334,
      "eval_loss": 3.95614755153656,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_large",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 50,
      "train_loss": 4.054471492767334,
      "eval_loss": 3.915259003639221,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_large",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 50,
      "train_loss": 4.054471492767334,
      "eval_loss": 3.940216898918152,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_large",
      "family": "listops",
      "seed": 42,
      "train_steps": 50,
      "train_loss": 4.054471492767334,
      "eval_loss": 4.435037136077881,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_large",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 50,
      "train_loss": 4.054471492767334,
      "eval_loss": 3.8657000064849854,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_large",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 50,
      "train_loss": 4.054471492767334,
      "eval_loss": 3.927276611328125,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_large",
      "family": "dyck",
      "seed": 42,
      "train_steps": 50,
      "train_loss": 4.054471492767334,
      "eval_loss": 3.996843099594116,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_large",
      "family": "dyck",
      "seed": 42,
      "train_steps": 50,
      "train_loss": 4.054471492767334,
      "eval_loss": 3.9264076948165894,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_full_expert_ffn_control",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 50,
      "train_loss": 4.066606521606445,
      "eval_loss": 3.991487741470337,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_full_expert_ffn_control",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 50,
      "train_loss": 4.066606521606445,
      "eval_loss": 3.948591947555542,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_full_expert_ffn_control",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 50,
      "train_loss": 4.066606521606445,
      "eval_loss": 3.9699047803878784,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_full_expert_ffn_control",
      "family": "listops",
      "seed": 42,
      "train_steps": 50,
      "train_loss": 4.066606521606445,
      "eval_loss": 4.465749979019165,
      "accuracy": 0.03643410852713178
    },
    {
      "model": "pvr_ec_ownership_top1_full_expert_ffn_control",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 50,
      "train_loss": 4.066606521606445,
      "eval_loss": 3.894876480102539,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_full_expert_ffn_control",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 50,
      "train_loss": 4.066606521606445,
      "eval_loss": 3.955662727355957,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_full_expert_ffn_control",
      "family": "dyck",
      "seed": 42,
      "train_steps": 50,
      "train_loss": 4.066606521606445,
      "eval_loss": 4.005615711212158,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_full_expert_ffn_control",
      "family": "dyck",
      "seed": 42,
      "train_steps": 50,
      "train_loss": 4.066606521606445,
      "eval_loss": 3.9410061836242676,
      "accuracy": 0.0
    }
  ],
  "specialization_metrics": {
    "expert_utilization": 0.8,
    "expert_gradient_norm_by_expert": {},
    "expert_output_norm_by_expert": {}
  }
}
```