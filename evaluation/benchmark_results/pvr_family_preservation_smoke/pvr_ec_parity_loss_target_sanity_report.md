# PVR-EC Parity Loss Target Sanity Report

**Status:** PVR_EC_LOSS_SCHEDULE_BLOCKER

**Statuses:** PVR_EC_DO_NOT_PROMOTE, PVR_EC_FIXED_OWNER_PARITY_FAILED, PVR_EC_LEARNED_OWNER_PARITY_FAILED, PVR_EC_LOSS_SCHEDULE_BLOCKER, PVR_EC_NONLINEAR_OVERFIT_FAILED, PVR_EC_NONLINEAR_OVERFIT_READY, PVR_EC_PARITY_OVERFIT_FAILED, PVR_EC_ROUND_ROBIN_PARITY_FAILED

```json
{
  "metadata": {
    "timestamp": "2026-06-09T01:14:59.087652",
    "run_id": "algo_20260609_011444_pvr-overfit-sanity",
    "git_commit": "aff470f9ed548af833e78f9fb075ed1fa78a9af1",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 42,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode pvr-overfit-sanity --scale tiny --device cuda --amp --pvr-overfit-tasks toy_identity,toy_xor_or_parity,single_batch_memorization --pvr-overfit-steps 100 --pvr-overfit-batch-size 32 --models dense_baseline,fixed_moe_vectorized,pvr_full,pvr_full_fixed_owner_e0,pvr_full_fixed_owner_round_robin --run-nonlinear-overfit-diagnostic --run-gradient-flow-diagnostic --run-expert-contribution-diagnostic --output-dir evaluation/benchmark_results/pvr_family_preservation_smoke",
    "model_variants": [
      "dense_baseline",
      "fixed_moe_vectorized",
      "pvr_full",
      "pvr_full_fixed_owner_e0",
      "pvr_full_fixed_owner_round_robin"
    ],
    "batch_sizes": [
      1,
      32
    ],
    "sequence_lengths": [
      64
    ],
    "train_steps": 500,
    "sample_limit": null,
    "mode": "pvr-nonlinear-overfit",
    "scale": "tiny",
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
    "pvr_overfit_tasks": [
      "toy_identity",
      "toy_xor_or_parity",
      "single_batch_memorization"
    ],
    "pvr_overfit_steps": 100,
    "pvr_overfit_batch_size": 32,
    "failures": []
  },
  "statuses": [
    "PVR_EC_DO_NOT_PROMOTE",
    "PVR_EC_FIXED_OWNER_PARITY_FAILED",
    "PVR_EC_LEARNED_OWNER_PARITY_FAILED",
    "PVR_EC_LOSS_SCHEDULE_BLOCKER",
    "PVR_EC_NONLINEAR_OVERFIT_FAILED",
    "PVR_EC_NONLINEAR_OVERFIT_READY",
    "PVR_EC_PARITY_OVERFIT_FAILED",
    "PVR_EC_ROUND_ROBIN_PARITY_FAILED"
  ],
  "promotion_ready": false,
  "analysis": {
    "overall_status": "PVR_EC_NONLINEAR_OVERFIT_FAILED",
    "statuses": [
      "PVR_EC_DO_NOT_PROMOTE",
      "PVR_EC_FIXED_OWNER_PARITY_FAILED",
      "PVR_EC_LEARNED_OWNER_PARITY_FAILED",
      "PVR_EC_LOSS_SCHEDULE_BLOCKER",
      "PVR_EC_NONLINEAR_OVERFIT_FAILED",
      "PVR_EC_NONLINEAR_OVERFIT_READY",
      "PVR_EC_PARITY_OVERFIT_FAILED",
      "PVR_EC_ROUND_ROBIN_PARITY_FAILED"
    ],
    "controls_pass": true,
    "fixed_owner_parity": false,
    "round_robin_parity": false,
    "uniform_owner_parity": false,
    "learned_owner_parity": false,
    "sparse_only_parity": false,
    "shared_only_parity": false,
    "dense_parity": false,
    "fixed_moe_parity": false,
    "micro_ffn_parity": false,
    "best_expert_delta_scale": null,
    "best_expert_delta_scale_accuracy": 0.0,
    "dominant_failure_mode": "loss_schedule_or_target_blocker",
    "recommended_repair": "verify_parity_target_and_loss_construction",
    "parity_results_by_model": {
      "dense_baseline": {
        "toy_xor_or_parity": {
          "accuracy": 0.650390625,
          "loss": 0.6089653968811035,
          "passed": false
        }
      },
      "fixed_moe_vectorized": {
        "toy_xor_or_parity": {
          "accuracy": 0.49609375,
          "loss": 0.6946998238563538,
          "passed": false
        }
      },
      "pvr_full": {
        "toy_xor_or_parity": {
          "accuracy": 0.49609375,
          "loss": 0.6946975588798523,
          "passed": false
        }
      },
      "pvr_full_fixed_owner_e0": {
        "toy_xor_or_parity": {
          "accuracy": 0.47265625,
          "loss": 0.6949355006217957,
          "passed": false
        }
      },
      "pvr_full_fixed_owner_round_robin": {
        "toy_xor_or_parity": {
          "accuracy": 0.5234375,
          "loss": 0.6919474005699158,
          "passed": false
        }
      }
    },
    "nonlinear_results_by_model": {
      "dense_baseline": {},
      "fixed_moe_vectorized": {},
      "pvr_full": {},
      "pvr_full_fixed_owner_e0": {},
      "pvr_full_fixed_owner_round_robin": {}
    }
  },
  "status": "PVR_EC_LOSS_SCHEDULE_BLOCKER",
  "parity_class_balance": [
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.49609375,
        "1": 0.50390625
      },
      "max_class_ratio": 0.50390625
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.49609375,
        "1": 0.50390625
      },
      "max_class_ratio": 0.50390625
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.49609375,
        "1": 0.50390625
      },
      "max_class_ratio": 0.50390625
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.49609375,
        "1": 0.50390625
      },
      "max_class_ratio": 0.50390625
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.49609375,
        "1": 0.50390625
      },
      "max_class_ratio": 0.50390625
    }
  ],
  "loss_target_sanity": [
    {
      "target_shape": [
        32,
        16
      ],
      "logit_shape": [
        32,
        16,
        256
      ],
      "loss_function": "cross_entropy",
      "ignore_index": null,
      "num_classes": 256,
      "target_value_range": [
        1,
        255
      ],
      "class_distribution": {
        "1": 4,
        "3": 1,
        "4": 1,
        "5": 5,
        "6": 1,
        "7": 3,
        "8": 1,
        "9": 2,
        "10": 1,
        "11": 2,
        "12": 2,
        "13": 1,
        "14": 2,
        "15": 1,
        "17": 3,
        "19": 1,
        "20": 1,
        "21": 1,
        "22": 3,
        "23": 1,
        "24": 1,
        "25": 1,
        "26": 2,
        "27": 3,
        "28": 2,
        "29": 2,
        "30": 1,
        "31": 1,
        "32": 4,
        "33": 2,
        "34": 2,
        "35": 4
      },
      "baseline_random_loss": 5.004273414611816,
      "expected_random_loss": 5.545177444479562,
      "accuracy_definition": "mean argmax token accuracy over all positions"
    },
    {
      "target_shape": [
        32,
        16
      ],
      "logit_shape": [
        32,
        16,
        256
      ],
      "loss_function": "cross_entropy",
      "ignore_index": null,
      "num_classes": 256,
      "target_value_range": [
        0,
        1
      ],
      "class_distribution": {
        "0": 254,
        "1": 258
      },
      "baseline_random_loss": 5.312471866607666,
      "expected_random_loss": 5.545177444479562,
      "accuracy_definition": "mean argmax token accuracy over all positions"
    },
    {
      "target_shape": [
        32,
        16
      ],
      "logit_shape": [
        32,
        16,
        256
      ],
      "loss_function": "cross_entropy",
      "ignore_index": null,
      "num_classes": 256,
      "target_value_range": [
        0,
        253
      ],
      "class_distribution": {
        "0": 1,
        "1": 3,
        "2": 1,
        "4": 3,
        "5": 3,
        "6": 3,
        "7": 2,
        "8": 5,
        "9": 4,
        "10": 6,
        "11": 4,
        "12": 2,
        "13": 3,
        "14": 2,
        "15": 4,
        "16": 2,
        "18": 4,
        "19": 3,
        "20": 2,
        "21": 1,
        "22": 3,
        "23": 2,
        "24": 3,
        "25": 2,
        "26": 1,
        "27": 1,
        "28": 1,
        "30": 3,
        "31": 2,
        "32": 1,
        "33": 3,
        "35": 3
      },
      "baseline_random_loss": 5.553832530975342,
      "expected_random_loss": 5.545177444479562,
      "accuracy_definition": "mean argmax token accuracy over all positions"
    },
    {
      "target_shape": [
        32,
        16
      ],
      "logit_shape": [
        32,
        16,
        256
      ],
      "loss_function": "cross_entropy",
      "ignore_index": null,
      "num_classes": 256,
      "target_value_range": [
        1,
        255
      ],
      "class_distribution": {
        "1": 4,
        "3": 1,
        "4": 1,
        "5": 5,
        "6": 1,
        "7": 3,
        "8": 1,
        "9": 2,
        "10": 1,
        "11": 2,
        "12": 2,
        "13": 1,
        "14": 2,
        "15": 1,
        "17": 3,
        "19": 1,
        "20": 1,
        "21": 1,
        "22": 3,
        "23": 1,
        "24": 1,
        "25": 1,
        "26": 2,
        "27": 3,
        "28": 2,
        "29": 2,
        "30": 1,
        "31": 1,
        "32": 4,
        "33": 2,
        "34": 2,
        "35": 4
      },
      "baseline_random_loss": 5.066739082336426,
      "expected_random_loss": 5.545177444479562,
      "accuracy_definition": "mean argmax token accuracy over all positions"
    },
    {
      "target_shape": [
        32,
        16
      ],
      "logit_shape": [
        32,
        16,
        256
      ],
      "loss_function": "cross_entropy",
      "ignore_index": null,
      "num_classes": 256,
      "target_value_range": [
        0,
        1
      ],
      "class_distribution": {
        "0": 254,
        "1": 258
      },
      "baseline_random_loss": 5.348642349243164,
      "expected_random_loss": 5.545177444479562,
      "accuracy_definition": "mean argmax token accuracy over all positions"
    },
    {
      "target_shape": [
        32,
        16
      ],
      "logit_shape": [
        32,
        16,
        256
      ],
      "loss_function": "cross_entropy",
      "ignore_index": null,
      "num_classes": 256,
      "target_value_range": [
        0,
        253
      ],
      "class_distribution": {
        "0": 1,
        "1": 3,
        "2": 1,
        "4": 3,
        "5": 3,
        "6": 3,
        "7": 2,
        "8": 5,
        "9": 4,
        "10": 6,
        "11": 4,
        "12": 2,
        "13": 3,
        "14": 2,
        "15": 4,
        "16": 2,
        "18": 4,
        "19": 3,
        "20": 2,
        "21": 1,
        "22": 3,
        "23": 2,
        "24": 3,
        "25": 2,
        "26": 1,
        "27": 1,
        "28": 1,
        "30": 3,
        "31": 2,
        "32": 1,
        "33": 3,
        "35": 3
      },
      "baseline_random_loss": 5.5468430519104,
      "expected_random_loss": 5.545177444479562,
      "accuracy_definition": "mean argmax token accuracy over all positions"
    },
    {
      "target_shape": [
        32,
        16
      ],
      "logit_shape": [
        32,
        16,
        256
      ],
      "loss_function": "cross_entropy",
      "ignore_index": null,
      "num_classes": 256,
      "target_value_range": [
        1,
        255
      ],
      "class_distribution": {
        "1": 4,
        "3": 1,
        "4": 1,
        "5": 5,
        "6": 1,
        "7": 3,
        "8": 1,
        "9": 2,
        "10": 1,
        "11": 2,
        "12": 2,
        "13": 1,
        "14": 2,
        "15": 1,
        "17": 3,
        "19": 1,
        "20": 1,
        "21": 1,
        "22": 3,
        "23": 1,
        "24": 1,
        "25": 1,
        "26": 2,
        "27": 3,
        "28": 2,
        "29": 2,
        "30": 1,
        "31": 1,
        "32": 4,
        "33": 2,
        "34": 2,
        "35": 4
      },
      "baseline_random_loss": 5.032907009124756,
      "expected_random_loss": 5.545177444479562,
      "accuracy_definition": "mean argmax token accuracy over all positions"
    },
    {
      "target_shape": [
        32,
        16
      ],
      "logit_shape": [
        32,
        16,
        256
      ],
      "loss_function": "cross_entropy",
      "ignore_index": null,
      "num_classes": 256,
      "target_value_range": [
        0,
        1
      ],
      "class_distribution": {
        "0": 254,
        "1": 258
      },
      "baseline_random_loss": 5.400063514709473,
      "expected_random_loss": 5.545177444479562,
      "accuracy_definition": "mean argmax token accuracy over all positions"
    }
  ]
}
```