# PVR-EC Training Dynamics Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-08T03:29:20.212121",
    "run_id": "algo_20260608_032649_benchmark-lite",
    "git_commit": "c214633e8dfb56a3ba797333eee2da2c985b17cd",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 123,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode benchmark-lite --scale small --sample-limit 1000 --train-steps 500 --seed-list 123,777 --families clrs_style,listops --device cuda --amp --models fixed_moe_vectorized,pvr_ec_deploy_top1,pvr_ec_ownership_top1_final_candidate_v1,pvr_ec_ownership_top1_final_candidate_v1_1 --enable-ownership-map --ownership-map-mode frozen --run-failure-case-replay --run-failure-attribution --output-dir evaluation/benchmark_results/pvr_failure_observatory_known_replay",
    "model_variants": [
      "fixed_moe_vectorized",
      "pvr_ec_deploy_top1",
      "pvr_ec_ownership_top1_final_candidate_v1",
      "pvr_ec_ownership_top1_final_candidate_v1_1"
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
      "listops"
    ],
    "pvr_expert_delta_scale": null,
    "pvr_expert_delta_scale_schedule": "constant",
    "pvr_expert_delta_scale_start": null,
    "pvr_expert_delta_scale_end": null,
    "pvr_expert_delta_scale_warmup_steps": null,
    "pvr_expert_delta_scale_hold_steps": null,
    "pvr_expert_delta_scale_decay": null,
    "root_cause_flags": {
      "run_collapse_case_replay": true
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
      "shape_pairs": [],
      "max_train_seconds": null,
      "repeatability_repair_variants": [],
      "calibration_repair_variants": [],
      "minimax_variants": [],
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
      "model": "pvr_ec_deploy_top1",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.2083549052476883,
      "eval_loss": 0.2900001537054777,
      "accuracy": 0.14772727272727273
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.2083549052476883,
      "eval_loss": 0.2672149548307061,
      "accuracy": 0.09438654666035054
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.2083549052476883,
      "eval_loss": 0.3000552002340555,
      "accuracy": 0.0886566008517228
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "listops",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.2083549052476883,
      "eval_loss": 1.6239676922559738,
      "accuracy": 0.07245134896063689
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
      "model": "pvr_ec_ownership_top1_final_candidate_v1_1",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.26725670229643583,
      "accuracy": 0.43618181818181817
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1_1",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.23323369026184082,
      "accuracy": 0.4347465656087163
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1_1",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.25374074652791023,
      "accuracy": 0.4263453348819202
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1_1",
      "family": "listops",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 1.3914664909243584,
      "accuracy": 0.24107142857142858
    }
  ],
  "specialization_metrics": {
    "expert_utilization": 0.75,
    "expert_gradient_norm_by_expert": {},
    "expert_output_norm_by_expert": {}
  }
}
```