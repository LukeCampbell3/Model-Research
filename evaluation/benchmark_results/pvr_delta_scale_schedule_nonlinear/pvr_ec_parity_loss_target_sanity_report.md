# PVR-EC Parity Loss Target Sanity Report

**Status:** PVR_EC_LOSS_TARGET_SANITY_PASSED

**Statuses:** PVR_EC_DO_NOT_PROMOTE, PVR_EC_EXPERT_SCALE_UNDERPOWERED, PVR_EC_FIXED_OWNER_PARITY_FAILED, PVR_EC_NONLINEAR_OVERFIT_PASSED, PVR_EC_NONLINEAR_OVERFIT_READY, PVR_EC_PARITY_OVERFIT_PASSED, PVR_EC_ROUND_ROBIN_PARITY_FAILED

```json
{
  "metadata": {
    "timestamp": "2026-06-07T01:40:36.464413",
    "run_id": "algo_20260607_005309_pvr-overfit-sanity",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 42,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode pvr-overfit-sanity --scale tiny --device cuda --amp --pvr-overfit-tasks toy_xor_or_parity,toy_xor_or_parity_balanced,toy_nonlinear_lookup,toy_composition_2step,single_batch_memorization --pvr-overfit-steps 500 --pvr-overfit-batch-size 32 --models pvr_full,pvr_full_expert_delta_scale_4,pvr_full_expert_delta_scale_8,pvr_full_scale_schedule_1_to_4,pvr_full_scale_schedule_1_to_8,pvr_full_scale_schedule_1_to_8_to_4 --run-expert-delta-scale-schedule-diagnostic --run-gradient-flow-diagnostic --run-expert-contribution-diagnostic --output-dir evaluation/benchmark_results/pvr_delta_scale_schedule_nonlinear",
    "model_variants": [
      "pvr_full",
      "pvr_full_expert_delta_scale_4",
      "pvr_full_expert_delta_scale_8",
      "pvr_full_scale_schedule_1_to_4",
      "pvr_full_scale_schedule_1_to_8",
      "pvr_full_scale_schedule_1_to_8_to_4"
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
      "toy_xor_or_parity",
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
    "PVR_EC_FIXED_OWNER_PARITY_FAILED",
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
      "PVR_EC_FIXED_OWNER_PARITY_FAILED",
      "PVR_EC_NONLINEAR_OVERFIT_PASSED",
      "PVR_EC_NONLINEAR_OVERFIT_READY",
      "PVR_EC_PARITY_OVERFIT_PASSED",
      "PVR_EC_ROUND_ROBIN_PARITY_FAILED"
    ],
    "controls_pass": true,
    "fixed_owner_parity": false,
    "round_robin_parity": false,
    "uniform_owner_parity": false,
    "learned_owner_parity": true,
    "sparse_only_parity": false,
    "shared_only_parity": false,
    "dense_parity": false,
    "fixed_moe_parity": false,
    "micro_ffn_parity": false,
    "best_expert_delta_scale": 4.0,
    "best_expert_delta_scale_accuracy": 0.78515625,
    "dominant_failure_mode": "expert_scale_underpowered",
    "recommended_repair": "expert_delta_scale_schedule_target_4.0",
    "parity_results_by_model": {
      "pvr_full": {
        "toy_xor_or_parity": {
          "accuracy": 0.708984375,
          "loss": 0.5254838466644287,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.77734375,
          "loss": 0.4219593107700348,
          "passed": true
        }
      },
      "pvr_full_expert_delta_scale_4": {
        "toy_xor_or_parity": {
          "accuracy": 0.751953125,
          "loss": 0.46617746353149414,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.78515625,
          "loss": 0.4229607582092285,
          "passed": true
        }
      },
      "pvr_full_expert_delta_scale_8": {
        "toy_xor_or_parity": {
          "accuracy": 0.751953125,
          "loss": 0.4536593556404114,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.779296875,
          "loss": 0.42691612243652344,
          "passed": true
        }
      },
      "pvr_full_scale_schedule_1_to_4": {
        "toy_xor_or_parity": {
          "accuracy": 0.744140625,
          "loss": 0.4740981161594391,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.8125,
          "loss": 0.3831399977207184,
          "passed": true
        }
      },
      "pvr_full_scale_schedule_1_to_8": {
        "toy_xor_or_parity": {
          "accuracy": 0.875,
          "loss": 0.2841958999633789,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.802734375,
          "loss": 0.40833303332328796,
          "passed": true
        }
      },
      "pvr_full_scale_schedule_1_to_8_to_4": {
        "toy_xor_or_parity": {
          "accuracy": 0.861328125,
          "loss": 0.30808866024017334,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.78515625,
          "loss": 0.43290501832962036,
          "passed": true
        }
      }
    },
    "nonlinear_results_by_model": {
      "pvr_full": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.0013114844914525747,
          "passed": true
        },
        "toy_composition_2step": {
          "accuracy": 1.0,
          "loss": 0.0009944270132109523,
          "passed": true
        }
      },
      "pvr_full_expert_delta_scale_4": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.0011855174088850617,
          "passed": true
        },
        "toy_composition_2step": {
          "accuracy": 1.0,
          "loss": 0.0009868592023849487,
          "passed": true
        }
      },
      "pvr_full_expert_delta_scale_8": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.0016073697479441762,
          "passed": true
        },
        "toy_composition_2step": {
          "accuracy": 1.0,
          "loss": 0.0013343584723770618,
          "passed": true
        }
      },
      "pvr_full_scale_schedule_1_to_4": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.0011473287595435977,
          "passed": true
        },
        "toy_composition_2step": {
          "accuracy": 1.0,
          "loss": 0.0009775159414857626,
          "passed": true
        }
      },
      "pvr_full_scale_schedule_1_to_8": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.0010865906951949,
          "passed": true
        },
        "toy_composition_2step": {
          "accuracy": 1.0,
          "loss": 0.0017387374537065625,
          "passed": true
        }
      },
      "pvr_full_scale_schedule_1_to_8_to_4": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.001107592019252479,
          "passed": true
        },
        "toy_composition_2step": {
          "accuracy": 1.0,
          "loss": 0.0010289824567735195,
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
        "0": 0.48046875,
        "1": 0.51953125
      },
      "max_class_ratio": 0.51953125
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.509765625,
        "1": 0.490234375
      },
      "max_class_ratio": 0.509765625
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.48046875,
        "1": 0.51953125
      },
      "max_class_ratio": 0.51953125
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.509765625,
        "1": 0.490234375
      },
      "max_class_ratio": 0.509765625
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.48046875,
        "1": 0.51953125
      },
      "max_class_ratio": 0.51953125
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.509765625,
        "1": 0.490234375
      },
      "max_class_ratio": 0.509765625
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.48046875,
        "1": 0.51953125
      },
      "max_class_ratio": 0.51953125
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.509765625,
        "1": 0.490234375
      },
      "max_class_ratio": 0.509765625
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.48046875,
        "1": 0.51953125
      },
      "max_class_ratio": 0.51953125
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.509765625,
        "1": 0.490234375
      },
      "max_class_ratio": 0.509765625
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.48046875,
        "1": 0.51953125
      },
      "max_class_ratio": 0.51953125
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.509765625,
        "1": 0.490234375
      },
      "max_class_ratio": 0.509765625
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
        0,
        1
      ],
      "class_distribution": {
        "0": 246,
        "1": 266
      },
      "baseline_random_loss": 5.400834083557129,
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
        "0": 261,
        "1": 251
      },
      "baseline_random_loss": 5.401081085205078,
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
        "0": 27,
        "1": 31,
        "2": 40,
        "3": 29,
        "4": 33,
        "5": 32,
        "6": 26,
        "7": 24,
        "8": 38,
        "9": 31,
        "10": 41,
        "11": 26,
        "12": 27,
        "13": 31,
        "14": 39,
        "15": 37
      },
      "baseline_random_loss": 5.615107536315918,
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
        "0": 26,
        "1": 36,
        "2": 27,
        "3": 37,
        "4": 23,
        "5": 31,
        "6": 36,
        "7": 28,
        "8": 37,
        "9": 30,
        "10": 41,
        "11": 30,
        "12": 40,
        "13": 32,
        "14": 30,
        "15": 28
      },
      "baseline_random_loss": 5.578101634979248,
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
        254
      ],
      "class_distribution": {
        "0": 3,
        "1": 5,
        "2": 3,
        "4": 1,
        "5": 2,
        "6": 3,
        "7": 1,
        "9": 1,
        "10": 1,
        "11": 2,
        "12": 1,
        "13": 3,
        "14": 2,
        "15": 1,
        "16": 2,
        "17": 3,
        "18": 1,
        "19": 2,
        "20": 3,
        "21": 4,
        "22": 4,
        "23": 3,
        "24": 2,
        "25": 3,
        "26": 1,
        "27": 1,
        "28": 4,
        "29": 1,
        "30": 3,
        "31": 3,
        "32": 2,
        "33": 1
      },
      "baseline_random_loss": 5.551196098327637,
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
        "0": 246,
        "1": 266
      },
      "baseline_random_loss": 5.393401145935059,
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
        "0": 261,
        "1": 251
      },
      "baseline_random_loss": 5.395267963409424,
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
        "0": 27,
        "1": 31,
        "2": 40,
        "3": 29,
        "4": 33,
        "5": 32,
        "6": 26,
        "7": 24,
        "8": 38,
        "9": 31,
        "10": 41,
        "11": 26,
        "12": 27,
        "13": 31,
        "14": 39,
        "15": 37
      },
      "baseline_random_loss": 5.617520809173584,
      "expected_random_loss": 5.545177444479562,
      "accuracy_definition": "mean argmax token accuracy over all positions"
    }
  ]
}
```