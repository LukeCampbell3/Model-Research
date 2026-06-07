# PVR-EC Training Dynamics Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-07T19:09:27.298036",
    "run_id": "algo_20260607_190742_benchmark-lite",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 2026,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode benchmark-lite --scale small --sample-limit 1000 --train-steps 500 --seed-list 42,123,777,2026,9001 --device cuda --amp --models fixed_moe_vectorized,pvr_ec_ownership_top1_final_candidate_v1 --enable-ownership-map --ownership-map-mode frozen --run-repeatability-collapse-isolation --output-dir evaluation/benchmark_results/pvr_blocker_repeatability_isolation",
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
      "run_repeatability_collapse_isolation": true
    },
    "diagnostic_sweeps": {
      "train_steps_list": [
        500
      ],
      "seed_list": [
        2026
      ],
      "batch_size_list": [
        1,
        32
      ],
      "seq_len_list": [
        64
      ],
      "max_train_seconds": null,
      "repeatability_repair_variants": [],
      "calibration_repair_variants": []
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
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.17279662191867828,
      "eval_loss": 0.2217050138860941,
      "accuracy": 0.4459090909090909
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.17279662191867828,
      "eval_loss": 0.19360523577779531,
      "accuracy": 0.5109610143381917
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.17279662191867828,
      "eval_loss": 0.21613057143986225,
      "accuracy": 0.5083236546651181
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "listops",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.17279662191867828,
      "eval_loss": 1.4341276176273823,
      "accuracy": 0.11868028923563337
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "scan_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.17279662191867828,
      "eval_loss": 0.19747881777584553,
      "accuracy": 0.08431771894093687
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "scan_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.17279662191867828,
      "eval_loss": 0.3002091757953167,
      "accuracy": 0.03771491957848031
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "dyck",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.17279662191867828,
      "eval_loss": 0.4059776086360216,
      "accuracy": 0.0037359900373599006
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "dyck",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.17279662191867828,
      "eval_loss": 0.2726379583279292,
      "accuracy": 0.03446238676644348
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15224745869636536,
      "eval_loss": 0.18395077250897884,
      "accuracy": 0.693
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15224745869636536,
      "eval_loss": 0.17868976388126612,
      "accuracy": 0.5263656831378125
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15224745869636536,
      "eval_loss": 0.1796662723645568,
      "accuracy": 0.6953155245838173
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "listops",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15224745869636536,
      "eval_loss": 1.286568507552147,
      "accuracy": 0.2292221669252613
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "scan_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15224745869636536,
      "eval_loss": 0.19539925176650286,
      "accuracy": 0.1154786150712831
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "scan_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15224745869636536,
      "eval_loss": 0.29588529095053673,
      "accuracy": 0.08347199112590127
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "dyck",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15224745869636536,
      "eval_loss": 0.40159808844327927,
      "accuracy": 0.05904939809049398
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "dyck",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15224745869636536,
      "eval_loss": 0.2721534085770448,
      "accuracy": 0.10456872784560851
    }
  ],
  "specialization_metrics": {
    "expert_utilization": 0.5,
    "expert_gradient_norm_by_expert": {},
    "expert_output_norm_by_expert": {}
  }
}
```