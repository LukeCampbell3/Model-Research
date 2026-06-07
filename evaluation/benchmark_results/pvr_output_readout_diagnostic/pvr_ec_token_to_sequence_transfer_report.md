# PVR-EC Token To Sequence Transfer Report

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
  "token_loss_improvement": 0.6723309271037579,
  "sequence_loss_improvement": 0.6754102862905711,
  "sequence_accuracy_improvement": 0.04910628016902289,
  "token_to_sequence_transfer_ratio": 0.06254858933453986,
  "by_task_family": {
    "clrs_style": {
      "token_loss_improvement": 0.931000754237175,
      "sequence_accuracy_improvement": 0.11241238643560791,
      "token_to_sequence_transfer_ratio": 0.12071818088970905
    },
    "dyck": {
      "token_loss_improvement": 0.5247642192989588,
      "sequence_accuracy_improvement": -0.0007348532538647607,
      "token_to_sequence_transfer_ratio": -0.002984253947253528
    },
    "listops": {
      "token_loss_improvement": 0.4037264287471771,
      "sequence_accuracy_improvement": 0.06020080257439986,
      "token_to_sequence_transfer_ratio": 0.15138016782056835
    },
    "scan_style": {
      "token_loss_improvement": 0.5661951433867216,
      "sequence_accuracy_improvement": -0.0015590070106554776,
      "token_to_sequence_transfer_ratio": -0.0035887439594348034
    }
  },
  "by_sequence_length_bucket": {
    "mixed": 0.06254858933453986
  },
  "by_difficulty_bucket": {
    "mixed": 0.06254858933453986
  },
  "by_prototype_id": {
    "diagnostic_all": 0.06254858933453986
  },
  "by_owner_expert": {
    "diagnostic_all": 0.06254858933453986
  },
  "by_decision_position_type": {
    "final": 0.06254858933453986
  }
}
```