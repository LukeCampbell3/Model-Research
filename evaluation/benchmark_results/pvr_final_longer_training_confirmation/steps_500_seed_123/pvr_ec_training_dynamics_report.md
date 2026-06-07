# PVR-EC Training Dynamics Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-07T17:52:03.305144",
    "run_id": "algo_20260607_175021_benchmark-lite",
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
      "run_longer_training_confirmation_gate": true
    },
    "diagnostic_sweeps": {
      "train_steps_list": [
        500
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
      "train_steps": 500,
      "train_loss": 0.15063753724098206,
      "eval_loss": 0.21594616118818521,
      "accuracy": 0.49127272727272725
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.15063753724098206,
      "eval_loss": 0.1755795106291771,
      "accuracy": 0.5577925153955471
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.15063753724098206,
      "eval_loss": 0.20173880364745855,
      "accuracy": 0.5481997677119629
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "listops",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.15063753724098206,
      "eval_loss": 1.5207750350236893,
      "accuracy": 0.16809486952675806
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.15063753724098206,
      "eval_loss": 0.1994481198489666,
      "accuracy": 0.08578584846587352
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.15063753724098206,
      "eval_loss": 0.2926559578627348,
      "accuracy": 0.040863981319322826
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.15063753724098206,
      "eval_loss": 0.4141271449625492,
      "accuracy": 0.022579970729667574
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.15063753724098206,
      "eval_loss": 0.2827530813713868,
      "accuracy": 0.058148893360160964
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.2435163501650095,
      "accuracy": 0.43618181818181817
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.21343904361128807,
      "accuracy": 0.4347465656087163
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.23340520728379488,
      "accuracy": 0.4263453348819202
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "listops",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 1.398505061864853,
      "accuracy": 0.24107142857142858
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.1875611413270235,
      "accuracy": 0.1427676894176581
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.27947625145316124,
      "accuracy": 0.0840630472854641
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.3927343413233757,
      "accuracy": 0.03846957976165587
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.26141560822725296,
      "accuracy": 0.06800804828973843
    }
  ],
  "specialization_metrics": {
    "expert_utilization": 0.5,
    "expert_gradient_norm_by_expert": {},
    "expert_output_norm_by_expert": {}
  }
}
```