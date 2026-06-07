# PVR-EC Sparse Direction Repair Selection Report

**Status:** PVR_EC_SPARSE_AUXILIARY_LOSS_HELPFUL

**Statuses:** PVR_EC_DO_NOT_PROMOTE, PVR_EC_SPARSE_AUXILIARY_LOSS_HELPFUL, PVR_EC_SPARSE_AUXILIARY_LOSS_IMPLEMENTED

```json
{
  "metadata": {
    "timestamp": "2026-06-07T03:18:03.818607",
    "run_id": "algo_20260607_031408_benchmark-lite",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 42,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode benchmark-lite --scale small --sample-limit 1000 --train-steps 500 --device cuda --amp --models pvr_ec_ownership_top1_scale_schedule_1_to_8 --enable-ownership-map --ownership-map-mode frozen --run-sparse-auxiliary-loss-sweep --sparse-aux-loss-variants baseline_main_loss,sparse_ce_0_03,sparse_ce_0_05,margin_align_0_03_m0_5,margin_align_0_05_m0_5,wrong_suppress_0_03_t0_25,sparse_ce_0_03_plus_margin_0_03,margin_0_03_plus_wrong_suppress_0_03,sparse_ce_0_03_plus_harm_0_03 --output-dir evaluation/benchmark_results/pvr_sparse_auxiliary_loss_sweep",
    "model_variants": [
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
  "status": "PVR_EC_SPARSE_AUXILIARY_LOSS_HELPFUL",
  "statuses": [
    "PVR_EC_DO_NOT_PROMOTE",
    "PVR_EC_SPARSE_AUXILIARY_LOSS_HELPFUL",
    "PVR_EC_SPARSE_AUXILIARY_LOSS_IMPLEMENTED"
  ],
  "promotion_ready": false,
  "selected_repair": "sparse_ce_0_05",
  "best_auxiliary_loss": "sparse_ce_0_05",
  "selection_reason": "selected lowest-loss auxiliary variant without accuracy regression",
  "complexity_penalty_applied": true
}
```