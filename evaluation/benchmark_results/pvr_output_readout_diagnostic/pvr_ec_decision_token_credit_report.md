# PVR-EC Decision Token Credit Report

**Status:** PVR_EC_TASK_LEVEL_TRANSFER_BLOCKER

**Statuses:** PVR_EC_BENCHMARK_CAPABILITY_NOT_IMPROVED, PVR_EC_BENCHMARK_TRANSFER_BLOCKER, PVR_EC_DO_NOT_PROMOTE, PVR_EC_DYCK_FINAL_STATE_BLOCKER, PVR_EC_EXPERT_RESIDUAL_ALIGNMENT_BLOCKER, PVR_EC_LISTOPS_TRANSFER_BLOCKER, PVR_EC_RESIDUAL_ALIGNED_TO_BENCHMARK, PVR_EC_SCAN_TRANSFER_BLOCKER, PVR_EC_TASK_LEVEL_TRANSFER_BLOCKER

```json
{
  "metadata": {
    "timestamp": "2026-06-07T02:34:22.355073",
    "run_id": "algo_20260607_023350_benchmark-lite",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 42,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode benchmark-lite --scale small --sample-limit 1000 --train-steps 500 --device cuda --amp --models pvr_ec_ownership_top1_scale_schedule_1_to_8 --enable-ownership-map --ownership-map-mode frozen --run-output-readout-diagnostic --readout-variants baseline_output_head,shared_only_output_head,sparse_only_output_head,combined_output_head,concat_shared_sparse_readout,gated_shared_sparse_readout,final_state_readout,mean_pool_readout,attention_pool_readout_diagnostic --output-dir evaluation/benchmark_results/pvr_output_readout_diagnostic",
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
  "status": "PVR_EC_TASK_LEVEL_TRANSFER_BLOCKER",
  "statuses": [
    "PVR_EC_BENCHMARK_CAPABILITY_NOT_IMPROVED",
    "PVR_EC_BENCHMARK_TRANSFER_BLOCKER",
    "PVR_EC_DO_NOT_PROMOTE",
    "PVR_EC_DYCK_FINAL_STATE_BLOCKER",
    "PVR_EC_EXPERT_RESIDUAL_ALIGNMENT_BLOCKER",
    "PVR_EC_LISTOPS_TRANSFER_BLOCKER",
    "PVR_EC_RESIDUAL_ALIGNED_TO_BENCHMARK",
    "PVR_EC_SCAN_TRANSFER_BLOCKER",
    "PVR_EC_TASK_LEVEL_TRANSFER_BLOCKER"
  ],
  "promotion_ready": false,
  "loss_delta_by_position": {
    "final": -0.6754102862905711,
    "decision": -0.6754102862905711,
    "nondecision": -0.6723187046591192
  },
  "accuracy_delta_by_position": {
    "decision": 0.04910628016902289
  },
  "residual_help_rate_by_position": {
    "decision": 0.6470743940056611,
    "all": 0.6453027786531795
  },
  "residual_harm_rate_by_position": {
    "decision": 0.352685123992463,
    "all": 0.3544546033566197
  },
  "expert_contribution_by_position": {
    "decision": 0.922526032812233,
    "all": 0.922526032812233
  },
  "final_token_loss_delta": -0.6754102862905711,
  "final_state_loss_delta": -0.6754102862905711,
  "decision_position_loss_delta": -0.6754102862905711,
  "nondecision_position_loss_delta": -0.6723187046591192,
  "decision_token_help_rate": 0.6470743940056611,
  "decision_token_harm_rate": 0.352685123992463,
  "decision_token_expert_contribution_pct": 0.922526032812233,
  "by_family": {
    "clrs_style": {
      "decision_token_help_rate": 0.8264945422609647,
      "decision_position_loss_delta": -0.931000754237175
    },
    "dyck": {
      "decision_token_help_rate": 0.617033274223407,
      "decision_position_loss_delta": -0.5247642192989588
    },
    "listops": {
      "decision_token_help_rate": 0.5959620401263237,
      "decision_position_loss_delta": -0.428361302241683
    },
    "scan_style": {
      "decision_token_help_rate": 0.4335414683446288,
      "decision_position_loss_delta": -0.5661951433867216
    }
  }
}
```