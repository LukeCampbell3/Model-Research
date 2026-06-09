# PVR-EC Parity Loss Target Sanity Report

**Status:** PVR_EC_LOSS_TARGET_SANITY_PASSED

**Statuses:** PVR_EC_DO_NOT_PROMOTE, PVR_EC_EXPERT_SCALE_UNDERPOWERED, PVR_EC_FIXED_OWNER_PARITY_PASSED, PVR_EC_NONLINEAR_OVERFIT_PASSED, PVR_EC_NONLINEAR_OVERFIT_READY, PVR_EC_PARITY_OVERFIT_PASSED, PVR_EC_ROUND_ROBIN_PARITY_FAILED

```json
{
  "metadata": {
    "timestamp": "2026-06-09T01:20:50.327590",
    "run_id": "algo_20260609_011910_pvr-overfit-sanity",
    "git_commit": "aff470f9ed548af833e78f9fb075ed1fa78a9af1",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 42,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode pvr-overfit-sanity --scale tiny --device cuda --amp --pvr-overfit-tasks toy_identity,toy_copy,toy_xor_or_parity_balanced,toy_nonlinear_lookup,toy_composition_2step,single_batch_memorization --pvr-overfit-steps 500 --pvr-overfit-batch-size 32 --models dense_baseline,pvr_full,pvr_full_fixed_owner_e0,pvr_full_expert_delta_scale_4 --run-nonlinear-overfit-diagnostic --output-dir evaluation/benchmark_results/pvr_nlp_stage1_model_comparison",
    "model_variants": [
      "dense_baseline",
      "pvr_full",
      "pvr_full_fixed_owner_e0",
      "pvr_full_expert_delta_scale_4"
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
      "toy_copy",
      "toy_xor_or_parity_balanced",
      "toy_nonlinear_lookup",
      "toy_composition_2step",
      "single_batch_memorization"
    ],
    "pvr_overfit_steps": 500,
    "pvr_overfit_batch_size": 32,
    "failures": []
  },
  "statuses": [
    "PVR_EC_DO_NOT_PROMOTE",
    "PVR_EC_EXPERT_SCALE_UNDERPOWERED",
    "PVR_EC_FIXED_OWNER_PARITY_PASSED",
    "PVR_EC_NONLINEAR_OVERFIT_PASSED",
    "PVR_EC_NONLINEAR_OVERFIT_READY",
    "PVR_EC_PARITY_OVERFIT_PASSED",
    "PVR_EC_ROUND_ROBIN_PARITY_FAILED"
  ],
  "promotion_ready": false,
  "analysis": {
    "overall_status": "PVR_EC_NONLINEAR_OVERFIT_PASSED",
    "statuses": [
      "PVR_EC_DO_NOT_PROMOTE",
      "PVR_EC_EXPERT_SCALE_UNDERPOWERED",
      "PVR_EC_FIXED_OWNER_PARITY_PASSED",
      "PVR_EC_NONLINEAR_OVERFIT_PASSED",
      "PVR_EC_NONLINEAR_OVERFIT_READY",
      "PVR_EC_PARITY_OVERFIT_PASSED",
      "PVR_EC_ROUND_ROBIN_PARITY_FAILED"
    ],
    "controls_pass": true,
    "fixed_owner_parity": true,
    "round_robin_parity": false,
    "uniform_owner_parity": false,
    "learned_owner_parity": true,
    "sparse_only_parity": false,
    "shared_only_parity": false,
    "dense_parity": true,
    "fixed_moe_parity": false,
    "micro_ffn_parity": false,
    "best_expert_delta_scale": 4.0,
    "best_expert_delta_scale_accuracy": 0.7734375,
    "dominant_failure_mode": "expert_scale_underpowered",
    "recommended_repair": "expert_delta_scale_schedule_target_4.0",
    "parity_results_by_model": {
      "dense_baseline": {
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.7265625,
          "loss": 0.49161359667778015,
          "passed": true
        }
      },
      "pvr_full": {
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.86328125,
          "loss": 0.2952992916107178,
          "passed": true
        }
      },
      "pvr_full_fixed_owner_e0": {
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.708984375,
          "loss": 0.5120936036109924,
          "passed": true
        }
      },
      "pvr_full_expert_delta_scale_4": {
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.7734375,
          "loss": 0.43197086453437805,
          "passed": true
        }
      }
    },
    "nonlinear_results_by_model": {
      "dense_baseline": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.001334306551143527,
          "passed": true
        },
        "toy_composition_2step": {
          "accuracy": 1.0,
          "loss": 0.0011924740392714739,
          "passed": true
        }
      },
      "pvr_full": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.0010335980914533138,
          "passed": true
        },
        "toy_composition_2step": {
          "accuracy": 1.0,
          "loss": 0.0010257737012580037,
          "passed": true
        }
      },
      "pvr_full_fixed_owner_e0": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.0010998486541211605,
          "passed": true
        },
        "toy_composition_2step": {
          "accuracy": 1.0,
          "loss": 0.0010528683196753263,
          "passed": true
        }
      },
      "pvr_full_expert_delta_scale_4": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.0009895407129079103,
          "passed": true
        },
        "toy_composition_2step": {
          "accuracy": 1.0,
          "loss": 0.0010120994411408901,
          "passed": true
        }
      }
    }
  },
  "status": "PVR_EC_LOSS_TARGET_SANITY_PASSED",
  "parity_class_balance": [
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.5,
        "1": 0.5
      },
      "max_class_ratio": 0.5
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.5,
        "1": 0.5
      },
      "max_class_ratio": 0.5
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.5,
        "1": 0.5
      },
      "max_class_ratio": 0.5
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.5,
        "1": 0.5
      },
      "max_class_ratio": 0.5
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
        254
      ],
      "class_distribution": {
        "1": 2,
        "3": 3,
        "4": 5,
        "6": 5,
        "7": 2,
        "8": 6,
        "9": 1,
        "10": 1,
        "11": 3,
        "12": 2,
        "13": 3,
        "14": 2,
        "15": 2,
        "16": 2,
        "17": 4,
        "18": 1,
        "19": 2,
        "22": 2,
        "23": 2,
        "24": 3,
        "25": 1,
        "26": 4,
        "27": 1,
        "28": 2,
        "29": 1,
        "30": 5,
        "31": 2,
        "32": 4,
        "33": 6,
        "34": 1,
        "35": 1,
        "37": 4
      },
      "baseline_random_loss": 5.010565280914307,
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
        2,
        255
      ],
      "class_distribution": {
        "2": 2,
        "3": 3,
        "4": 5,
        "5": 2,
        "6": 1,
        "7": 1,
        "8": 2,
        "9": 3,
        "11": 1,
        "12": 1,
        "13": 2,
        "14": 5,
        "16": 7,
        "17": 2,
        "18": 5,
        "19": 3,
        "20": 2,
        "21": 5,
        "22": 4,
        "23": 2,
        "24": 5,
        "25": 2,
        "26": 1,
        "27": 2,
        "29": 1,
        "30": 4,
        "31": 2,
        "33": 2,
        "34": 4,
        "35": 2,
        "36": 2,
        "37": 1
      },
      "baseline_random_loss": 5.528257369995117,
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
        "0": 256,
        "1": 256
      },
      "baseline_random_loss": 5.310719013214111,
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
        15
      ],
      "class_distribution": {
        "0": 34,
        "1": 31,
        "2": 28,
        "3": 33,
        "4": 43,
        "5": 27,
        "6": 33,
        "7": 31,
        "8": 28,
        "9": 25,
        "10": 28,
        "11": 24,
        "12": 32,
        "13": 35,
        "14": 38,
        "15": 42
      },
      "baseline_random_loss": 5.52324104309082,
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
        15
      ],
      "class_distribution": {
        "0": 35,
        "1": 29,
        "2": 35,
        "3": 30,
        "4": 40,
        "5": 29,
        "6": 27,
        "7": 39,
        "8": 26,
        "9": 33,
        "10": 24,
        "11": 32,
        "12": 32,
        "13": 34,
        "14": 33,
        "15": 34
      },
      "baseline_random_loss": 5.572707653045654,
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
        255
      ],
      "class_distribution": {
        "0": 5,
        "1": 2,
        "2": 4,
        "3": 6,
        "4": 4,
        "5": 5,
        "6": 4,
        "7": 2,
        "9": 2,
        "12": 3,
        "13": 2,
        "14": 2,
        "15": 3,
        "17": 5,
        "18": 1,
        "19": 3,
        "21": 3,
        "22": 5,
        "23": 2,
        "24": 1,
        "25": 1,
        "26": 2,
        "27": 3,
        "29": 3,
        "30": 2,
        "31": 1,
        "32": 2,
        "33": 1,
        "35": 2,
        "36": 2,
        "37": 1,
        "38": 1
      },
      "baseline_random_loss": 5.566431045532227,
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
        254
      ],
      "class_distribution": {
        "1": 2,
        "3": 3,
        "4": 5,
        "6": 5,
        "7": 2,
        "8": 6,
        "9": 1,
        "10": 1,
        "11": 3,
        "12": 2,
        "13": 3,
        "14": 2,
        "15": 2,
        "16": 2,
        "17": 4,
        "18": 1,
        "19": 2,
        "22": 2,
        "23": 2,
        "24": 3,
        "25": 1,
        "26": 4,
        "27": 1,
        "28": 2,
        "29": 1,
        "30": 5,
        "31": 2,
        "32": 4,
        "33": 6,
        "34": 1,
        "35": 1,
        "37": 4
      },
      "baseline_random_loss": 5.011815547943115,
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
        2,
        255
      ],
      "class_distribution": {
        "2": 2,
        "3": 3,
        "4": 5,
        "5": 2,
        "6": 1,
        "7": 1,
        "8": 2,
        "9": 3,
        "11": 1,
        "12": 1,
        "13": 2,
        "14": 5,
        "16": 7,
        "17": 2,
        "18": 5,
        "19": 3,
        "20": 2,
        "21": 5,
        "22": 4,
        "23": 2,
        "24": 5,
        "25": 2,
        "26": 1,
        "27": 2,
        "29": 1,
        "30": 4,
        "31": 2,
        "33": 2,
        "34": 4,
        "35": 2,
        "36": 2,
        "37": 1
      },
      "baseline_random_loss": 5.517326831817627,
      "expected_random_loss": 5.545177444479562,
      "accuracy_definition": "mean argmax token accuracy over all positions"
    }
  ]
}
```