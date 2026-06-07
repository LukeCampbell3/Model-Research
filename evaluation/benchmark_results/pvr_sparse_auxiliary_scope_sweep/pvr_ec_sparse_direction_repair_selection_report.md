# PVR-EC Sparse Direction Repair Selection Report

**Status:** PVR_EC_BENCHMARK_CAPABILITY_NOT_IMPROVED

**Statuses:** PVR_EC_BENCHMARK_CAPABILITY_NOT_IMPROVED, PVR_EC_DO_NOT_PROMOTE, PVR_EC_SPARSE_AUXILIARY_LOSS_IMPLEMENTED

```json
{
  "metadata": {
    "timestamp": "2026-06-07T03:24:44.342132",
    "run_id": "algo_20260607_032151_benchmark-lite",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 42,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode benchmark-lite --scale small --sample-limit 1000 --train-steps 500 --device cuda --amp --models pvr_ec_ownership_top1_scale_schedule_1_to_8 --enable-ownership-map --ownership-map-mode frozen --run-sparse-auxiliary-scope-sweep --sparse-aux-scopes aux_all_tokens,aux_decision_tokens_only,aux_final_tokens_only,aux_listops_scan_only,aux_scan_only,aux_listops_only,aux_dyck_final_state_only --output-dir evaluation/benchmark_results/pvr_sparse_auxiliary_scope_sweep",
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
  "status": "PVR_EC_BENCHMARK_CAPABILITY_NOT_IMPROVED",
  "statuses": [
    "PVR_EC_BENCHMARK_CAPABILITY_NOT_IMPROVED",
    "PVR_EC_DO_NOT_PROMOTE",
    "PVR_EC_SPARSE_AUXILIARY_LOSS_IMPLEMENTED"
  ],
  "promotion_ready": false,
  "selected_repair": "reject_sparse_logit_auxiliary_loss",
  "best_auxiliary_loss": "sparse_ce_0_05",
  "selection_reason": "no sparse auxiliary variant beat baseline cleanly",
  "complexity_penalty_applied": true
}
```