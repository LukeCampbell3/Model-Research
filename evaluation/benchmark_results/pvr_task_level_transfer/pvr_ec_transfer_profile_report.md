# PVR-EC Transfer Profile Report

**Status:** PVR_EC_TASK_LEVEL_TRANSFER_BLOCKER

**Statuses:** PVR_EC_BENCHMARK_CAPABILITY_NOT_IMPROVED, PVR_EC_BENCHMARK_TRANSFER_BLOCKER, PVR_EC_DO_NOT_PROMOTE, PVR_EC_DYCK_FINAL_STATE_BLOCKER, PVR_EC_EXPERT_RESIDUAL_ALIGNMENT_BLOCKER, PVR_EC_LISTOPS_TRANSFER_BLOCKER, PVR_EC_RESIDUAL_ALIGNED_TO_BENCHMARK, PVR_EC_SCALE_HELPFUL_BY_FAMILY, PVR_EC_SCALE_OVERAMPLIFIES_BENCHMARK_NOISE, PVR_EC_SCAN_TRANSFER_BLOCKER, PVR_EC_TASK_LEVEL_TRANSFER_BLOCKER

```json
{
  "metadata": {
    "timestamp": "2026-06-07T02:33:38.757263",
    "run_id": "algo_20260607_023103_benchmark-lite",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 42,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode benchmark-lite --scale small --sample-limit 1000 --train-steps 500 --device cuda --amp --models fixed_moe_vectorized,pvr_ec_deploy_top1,pvr_ec_ownership_top1_scale_schedule_1_to_8 --enable-ownership-map --ownership-map-mode frozen --run-task-level-transfer-diagnostic --run-decision-token-credit-diagnostic --run-token-to-sequence-transfer-diagnostic --run-family-failure-decomposition --output-dir evaluation/benchmark_results/pvr_task_level_transfer",
    "model_variants": [
      "fixed_moe_vectorized",
      "pvr_ec_deploy_top1",
      "pvr_ec_ownership_top1_scale_schedule_1_to_8"
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
    "pvr_expert_delta_scale_decay": null
  },
  "status": "PVR_EC_TASK_LEVEL_TRANSFER_BLOCKER",
  "statuses": [
    "PVR_EC_BENCHMARK_CAPABILITY_NOT_IMPROVED",
    "PVR_EC_BENCHMARK_TRANSFER_BLOCKER",
    "PVR_EC_DO_NOT_PROMOTE",
    "PVR_EC_DYCK_FINAL_STATE_BLOCKER",
    "PVR_EC_EXPERT_RESIDUAL_ALIGNMENT_BLOCKER",
    "PVR_EC_LISTOPS_TRANSFER_BLOCKER",
    "PVR_EC_RESIDUAL_ALIGNED_TO_BENCHMARK",
    "PVR_EC_SCALE_HELPFUL_BY_FAMILY",
    "PVR_EC_SCALE_OVERAMPLIFIES_BENCHMARK_NOISE",
    "PVR_EC_SCAN_TRANSFER_BLOCKER",
    "PVR_EC_TASK_LEVEL_TRANSFER_BLOCKER"
  ],
  "promotion_ready": false,
  "model_table": {
    "fixed_moe_vectorized": {
      "params": 1001092,
      "avg_accuracy": 0.25857819999606313,
      "avg_exact_match": 0.00925,
      "avg_loss": 0.3886076922838887,
      "avg_qpc": 0.12928909999803156,
      "avg_loops": 1.0
    },
    "pvr_ec_deploy_top1": {
      "params": 614274,
      "avg_accuracy": 0.0771500010285979,
      "avg_exact_match": 0.0,
      "avg_loss": 0.45097945421002805,
      "avg_qpc": 0.0771500010285979,
      "avg_loops": 1.0
    },
    "pvr_ec_ownership_top1_scale_schedule_1_to_8": {
      "params": 482690,
      "avg_accuracy": 0.06054665483850138,
      "avg_exact_match": 0.0,
      "avg_loss": 0.46348366168482846,
      "avg_qpc": 0.06054665483850138,
      "avg_loops": 1.0
    }
  },
  "loss_by_family": {
    "pvr_ec_deploy_top1": {
      "clrs_style": 0.26753168646246195,
      "listops": 1.589727409183979,
      "scan_style": 0.2501062727533281,
      "dyck": 0.3576503098011017
    },
    "pvr_ec_ownership_top1_scale_schedule_1_to_8": {
      "clrs_style": 0.29691687412559986,
      "listops": 1.6250091530382633,
      "scan_style": 0.24619679944589734,
      "dyck": 0.34985795958588517
    }
  },
  "accuracy_by_family": {
    "pvr_ec_deploy_top1": {
      "clrs_style": 0.1713499366157629,
      "listops": 0.08681121159355165,
      "scan_style": 0.008169493393971418,
      "dyck": 0.0
    },
    "pvr_ec_ownership_top1_scale_schedule_1_to_8": {
      "clrs_style": 0.11316433984218958,
      "listops": 0.09487165084536314,
      "scan_style": 0.01726854679620559,
      "dyck": 0.007735737371833997
    }
  },
  "residual_help_rate_by_family": {
    "clrs_style": 0.7543035758038362,
    "dyck": 0.5272507594587902,
    "listops": 0.6583926975727081,
    "scan_style": 0.4542821808718145
  },
  "residual_harm_rate_by_family": {
    "clrs_style": 0.24549427178377906,
    "dyck": 0.4721299461089075,
    "listops": 0.3413939536549151,
    "scan_style": 0.5453439801931381
  },
  "expert_delta_contribution_pct_by_family": {
    "clrs_style": 0.8927741461439608,
    "dyck": 0.8918826883748258,
    "listops": 0.8960048874557448,
    "scan_style": 0.890072898564443
  },
  "shared_sparse_ratio_by_family": {
    "clrs_style": 0.15461139501227686,
    "dyck": 0.1546149133258344,
    "listops": 0.14412356179673225,
    "scan_style": 0.1616547807061579
  },
  "calibration_proxy_by_family": {
    "clrs_style": 0.07047602660533542,
    "dyck": 0.11153605039247201,
    "listops": 0.04745422033743196,
    "scan_style": 0.10891413425239099
  },
  "latency_p50": 0.6599661856889725,
  "latency_p95": 0.6599661856889725,
  "owner_count_per_token": 1.0,
  "Top2_executions": 0.0,
  "Top4_executions": 0.0
}
```