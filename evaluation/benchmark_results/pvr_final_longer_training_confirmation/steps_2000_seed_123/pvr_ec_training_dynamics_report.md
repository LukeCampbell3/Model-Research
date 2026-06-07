# PVR-EC Training Dynamics Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-07T18:16:56.836609",
    "run_id": "algo_20260607_181030_benchmark-lite",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 123,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode benchmark-lite --scale small --sample-limit 1000 --train-steps-list 500,1000,2000 --seed-list 42,123,777 --device cuda --amp --models fixed_moe_vectorized,pvr_ec_ownership_top1_final_candidate_v1 --enable-ownership-map --ownership-map-mode frozen --run-longer-training-confirmation-gate --output-dir evaluation/benchmark_results/pvr_final_longer_training_confirmation",
    "model_variants": [
      "fixed_moe_vectorized",
      "pvr_ec_ownership_top1_final_candidate_v1"
    ],
    "batch_sizes": [
      1,
      32
    ],
    "sequence_lengths": [
      64
    ],
    "train_steps": 2000,
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
      "run_longer_training_confirmation_gate": true
    },
    "diagnostic_sweeps": {
      "train_steps_list": [
        2000
      ],
      "seed_list": [
        123
      ],
      "batch_size_list": [
        1,
        32
      ],
      "seq_len_list": [
        64
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
      "seed": 123,
      "train_steps": 2000,
      "train_loss": 0.020037148147821426,
      "eval_loss": 0.0522368005476892,
      "accuracy": 0.888090909090909
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 2000,
      "train_loss": 0.020037148147821426,
      "eval_loss": 0.07086695684120059,
      "accuracy": 0.7901468498342018
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 2000,
      "train_loss": 0.020037148147821426,
      "eval_loss": 0.05300899990834296,
      "accuracy": 0.8548199767711963
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "listops",
      "seed": 123,
      "train_steps": 2000,
      "train_loss": 0.020037148147821426,
      "eval_loss": 1.1463853474706411,
      "accuracy": 0.3621185316231756
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 2000,
      "train_loss": 0.020037148147821426,
      "eval_loss": 0.14634281489998102,
      "accuracy": 0.23606762680025048
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 2000,
      "train_loss": 0.020037148147821426,
      "eval_loss": 0.21720465272665024,
      "accuracy": 0.2422650321074139
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "dyck",
      "seed": 123,
      "train_steps": 2000,
      "train_loss": 0.020037148147821426,
      "eval_loss": 0.29892671294510365,
      "accuracy": 0.34340372151369436
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "dyck",
      "seed": 123,
      "train_steps": 2000,
      "train_loss": 0.020037148147821426,
      "eval_loss": 0.20308406154314676,
      "accuracy": 0.3293762575452716
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 2000,
      "train_loss": 0.012056197039783001,
      "eval_loss": 0.04649752750992775,
      "accuracy": 0.9427272727272727
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 2000,
      "train_loss": 0.012056197039783001,
      "eval_loss": 0.06257503991946578,
      "accuracy": 0.8743486499289437
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 2000,
      "train_loss": 0.012056197039783001,
      "eval_loss": 0.0464034762699157,
      "accuracy": 0.9335075493612079
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "listops",
      "seed": 123,
      "train_steps": 2000,
      "train_loss": 0.012056197039783001,
      "eval_loss": 1.0474950801581144,
      "accuracy": 0.4570433436532508
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 2000,
      "train_loss": 0.012056197039783001,
      "eval_loss": 0.1176408133469522,
      "accuracy": 0.8273846796075975
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 2000,
      "train_loss": 0.012056197039783001,
      "eval_loss": 0.17940103635191917,
      "accuracy": 0.8584354932866316
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "dyck",
      "seed": 123,
      "train_steps": 2000,
      "train_loss": 0.012056197039783001,
      "eval_loss": 0.2633036207407713,
      "accuracy": 0.8190466234580807
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "dyck",
      "seed": 123,
      "train_steps": 2000,
      "train_loss": 0.012056197039783001,
      "eval_loss": 0.1690071808795134,
      "accuracy": 0.8086519114688129
    }
  ],
  "specialization_metrics": {
    "expert_utilization": 0.5,
    "expert_gradient_norm_by_expert": {},
    "expert_output_norm_by_expert": {}
  }
}
```