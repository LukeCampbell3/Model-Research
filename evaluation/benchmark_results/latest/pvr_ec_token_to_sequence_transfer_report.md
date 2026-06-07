# PVR-EC Token To Sequence Transfer Report

**Status:** PVR_EC_LOCAL_RESIDUAL_GLOBAL_TRANSFER_FAILURE

**Statuses:** PVR_EC_BENCHMARK_CAPABILITY_NOT_IMPROVED, PVR_EC_BENCHMARK_TRANSFER_BLOCKER, PVR_EC_DECISION_TOKEN_CREDIT_FAILURE, PVR_EC_DO_NOT_PROMOTE, PVR_EC_EXPERT_RESIDUAL_ALIGNMENT_BLOCKER, PVR_EC_LOCAL_RESIDUAL_GLOBAL_TRANSFER_FAILURE, PVR_EC_RESIDUAL_MISALIGNED_TO_BENCHMARK, PVR_EC_SCALE_HELPFUL_BY_FAMILY, PVR_EC_TASK_FAMILY_CONDITIONED_SCALE_NEEDED, PVR_EC_TASK_LEVEL_TRANSFER_BLOCKER

```json
{
  "metadata": {
    "timestamp": "2026-06-07T20:17:49.770749",
    "run_id": "algo_20260607_201749_benchmark-lite",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "N/A",
    "cuda_available": false,
    "gpu_name": "",
    "amp_enabled": false,
    "seed": 42,
    "benchmark_command": "C:\\Users\\jcthi\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python311\\Scripts\\pytest sparse_loop_moe/tests/test_pvr_ec.py -q",
    "model_variants": [
      "dense_baseline",
      "fixed_moe",
      "fixed_moe_looped_reference",
      "fixed_moe_vectorized",
      "adaptive_moe",
      "looped_moe",
      "full_system",
      "pvr_ec",
      "pvr_ec_matched",
      "pvr_ec_fixed_top2",
      "pvr_ec_no_prototypes",
      "pvr_ec_no_load_bias",
      "pvr_ec_no_extra_experts",
      "pvr_ec_deploy_top1",
      "pvr_ec_deploy_top2",
      "pvr_ec_deploy_bucketed",
      "pvr_ec_deploy_dense_masked_control",
      "pvr_ec_ownership_top1_frozen_candidate",
      "pvr_ec_ownership_top1_delta_small",
      "pvr_ec_ownership_top1_delta_medium",
      "pvr_ec_ownership_top1_delta_large",
      "pvr_ec_ownership_top1_full_expert_ffn_control",
      "pvr_ec_ownership_top1_rank_8",
      "pvr_ec_ownership_top1_rank_16",
      "pvr_ec_ownership_top1_rank_32",
      "pvr_ec_ownership_top1_rank_64",
      "pvr_ec_ownership_top1_rank_128",
      "pvr_ec_ownership_top1_micro_ffn_0_25x",
      "pvr_ec_ownership_top1_micro_ffn_0_5x",
      "pvr_ec_ownership_top1_micro_ffn_1_0x",
      "pvr_ec_ownership_top1_delta_rank_8",
      "pvr_ec_ownership_top1_delta_rank_16",
      "pvr_ec_ownership_top1_delta_rank_32",
      "pvr_ec_ownership_top1_delta_rank_64",
      "pvr_ec_ownership_top1_delta_rank_128",
      "pvr_ec_learning_full",
      "pvr_ec_learning_shared_only",
      "pvr_ec_learning_sparse_only",
      "pvr_ec_learning_shared_scale_0_5",
      "pvr_ec_learning_expert_delta_scale_2_0",
      "pvr_ec_ownership_top1_delayed_candidate",
      "pvr_shared_only",
      "pvr_sparse_only",
      "pvr_full",
      "pvr_full_shared_scale_1_0",
      "pvr_full_shared_scale_0_5",
      "pvr_full_shared_scale_0_25",
      "pvr_full_shared_scale_0_0",
      "pvr_full_expert_delta_scale_0_5",
      "pvr_full_expert_delta_scale_1_0",
      "pvr_full_expert_delta_scale_2_0",
      "pvr_full_expert_delta_scale_4_0",
      "pvr_full_fixed_owner_e0",
      "pvr_full_fixed_owner_round_robin",
      "pvr_full_uniform_owner",
      "pvr_full_expert_delta_scale_1",
      "pvr_full_expert_delta_scale_2",
      "pvr_full_expert_delta_scale_4",
      "pvr_full_expert_delta_scale_8",
      "pvr_full_delta_rank_16",
      "pvr_full_delta_rank_64",
      "pvr_full_delta_rank_128",
      "pvr_full_micro_ffn_0_5x",
      "pvr_ec_ownership_top1_constant_1",
      "pvr_ec_ownership_top1_constant_2",
      "pvr_ec_ownership_top1_constant_4",
      "pvr_ec_ownership_top1_constant_8",
      "pvr_full_scale_schedule_1_to_4",
      "pvr_full_scale_schedule_1_to_8",
      "pvr_full_scale_schedule_1_to_8_to_4",
      "pvr_ec_ownership_top1_scale_schedule_1_to_4",
      "pvr_ec_ownership_top1_scale_schedule_1_to_8",
      "pvr_ec_ownership_top1_scale_schedule_1_to_8_to_4",
      "pvr_ec_ownership_top1_scale_schedule_1_to_8_to_2",
      "pvr_ec_ownership_top1_scale_schedule_1_to_4_to_2",
      "pvr_ec_ownership_top1_best_scale_repair",
      "pvr_ec_ownership_top1_best_transfer_repair",
      "pvr_ec_ownership_top1_best_sparse_logit_repair",
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
    "train_steps": 200,
    "sample_limit": null,
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
  "status": "PVR_EC_LOCAL_RESIDUAL_GLOBAL_TRANSFER_FAILURE",
  "statuses": [
    "PVR_EC_BENCHMARK_CAPABILITY_NOT_IMPROVED",
    "PVR_EC_BENCHMARK_TRANSFER_BLOCKER",
    "PVR_EC_DECISION_TOKEN_CREDIT_FAILURE",
    "PVR_EC_DO_NOT_PROMOTE",
    "PVR_EC_EXPERT_RESIDUAL_ALIGNMENT_BLOCKER",
    "PVR_EC_LOCAL_RESIDUAL_GLOBAL_TRANSFER_FAILURE",
    "PVR_EC_RESIDUAL_MISALIGNED_TO_BENCHMARK",
    "PVR_EC_SCALE_HELPFUL_BY_FAMILY",
    "PVR_EC_TASK_FAMILY_CONDITIONED_SCALE_NEEDED",
    "PVR_EC_TASK_LEVEL_TRANSFER_BLOCKER"
  ],
  "promotion_ready": false,
  "token_loss_improvement": 0.025,
  "sequence_loss_improvement": null,
  "sequence_accuracy_improvement": 0.0,
  "token_to_sequence_transfer_ratio": 0.0,
  "by_task_family": {
    "clrs_style": {
      "token_loss_improvement": 0.025,
      "sequence_accuracy_improvement": 0.0,
      "token_to_sequence_transfer_ratio": 0.0
    },
    "dyck": {
      "token_loss_improvement": 0.025,
      "sequence_accuracy_improvement": 0.0,
      "token_to_sequence_transfer_ratio": 0.0
    },
    "listops": {
      "token_loss_improvement": 0.025,
      "sequence_accuracy_improvement": 0.0,
      "token_to_sequence_transfer_ratio": 0.0
    },
    "scan_style": {
      "token_loss_improvement": 0.025,
      "sequence_accuracy_improvement": 0.0,
      "token_to_sequence_transfer_ratio": 0.0
    }
  },
  "by_sequence_length_bucket": {
    "mixed": 0.0
  },
  "by_difficulty_bucket": {
    "mixed": 0.0
  },
  "by_prototype_id": {
    "diagnostic_all": 0.0
  },
  "by_owner_expert": {
    "diagnostic_all": 0.0
  },
  "by_decision_position_type": {
    "final": 0.0
  }
}
```