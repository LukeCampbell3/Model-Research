# PVR-EC Parity Loss Target Sanity Report

**Status:** PVR_EC_LOSS_TARGET_SANITY_PASSED

**Statuses:** PVR_EC_DO_NOT_PROMOTE, PVR_EC_EXPERT_SCALE_UNDERPOWERED, PVR_EC_FIXED_OWNER_PARITY_PASSED, PVR_EC_NONLINEAR_OVERFIT_PASSED, PVR_EC_NONLINEAR_OVERFIT_READY, PVR_EC_PARITY_OVERFIT_PASSED, PVR_EC_ROUND_ROBIN_PARITY_PASSED

```json
{
  "metadata": {
    "timestamp": "2026-06-09T01:53:06.310242",
    "run_id": "algo_20260609_014426_pvr-overfit-sanity",
    "git_commit": "aff470f9ed548af833e78f9fb075ed1fa78a9af1",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 42,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode pvr-overfit-sanity --scale small --device cuda --amp --pvr-overfit-tasks toy_identity,toy_copy,toy_xor_or_parity,toy_xor_or_parity_balanced,toy_nonlinear_lookup,toy_composition_2step,single_batch_memorization --pvr-overfit-steps 500 --pvr-overfit-batch-size 32 --models dense_baseline,fixed_moe_vectorized,pvr_shared_only,pvr_sparse_only,pvr_full,pvr_full_fixed_owner_e0,pvr_full_fixed_owner_round_robin,pvr_full_uniform_owner,pvr_full_expert_delta_scale_1,pvr_full_expert_delta_scale_2,pvr_full_expert_delta_scale_4,pvr_full_expert_delta_scale_8,pvr_full_delta_rank_16,pvr_full_delta_rank_128,pvr_full_micro_ffn_0_5x --run-nonlinear-overfit-diagnostic --run-gradient-flow-diagnostic --run-expert-contribution-diagnostic --run-loss-target-sanity --output-dir evaluation/benchmark_results/pvr_nonlinear_overfit_500",
    "model_variants": [
      "dense_baseline",
      "fixed_moe_vectorized",
      "pvr_shared_only",
      "pvr_sparse_only",
      "pvr_full",
      "pvr_full_fixed_owner_e0",
      "pvr_full_fixed_owner_round_robin",
      "pvr_full_uniform_owner",
      "pvr_full_expert_delta_scale_1",
      "pvr_full_expert_delta_scale_2",
      "pvr_full_expert_delta_scale_4",
      "pvr_full_expert_delta_scale_8",
      "pvr_full_delta_rank_16",
      "pvr_full_delta_rank_128",
      "pvr_full_micro_ffn_0_5x"
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
    "pvr_overfit_tasks": [
      "toy_identity",
      "toy_copy",
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
    "PVR_EC_FIXED_OWNER_PARITY_PASSED",
    "PVR_EC_NONLINEAR_OVERFIT_PASSED",
    "PVR_EC_NONLINEAR_OVERFIT_READY",
    "PVR_EC_PARITY_OVERFIT_PASSED",
    "PVR_EC_ROUND_ROBIN_PARITY_PASSED"
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
      "PVR_EC_ROUND_ROBIN_PARITY_PASSED"
    ],
    "controls_pass": true,
    "fixed_owner_parity": true,
    "round_robin_parity": true,
    "uniform_owner_parity": true,
    "learned_owner_parity": true,
    "sparse_only_parity": true,
    "shared_only_parity": true,
    "dense_parity": true,
    "fixed_moe_parity": true,
    "micro_ffn_parity": true,
    "best_expert_delta_scale": 8.0,
    "best_expert_delta_scale_accuracy": 0.87890625,
    "dominant_failure_mode": "expert_scale_underpowered",
    "recommended_repair": "expert_delta_scale_schedule_target_8.0",
    "parity_results_by_model": {
      "dense_baseline": {
        "toy_xor_or_parity": {
          "accuracy": 0.796875,
          "loss": 0.41053926944732666,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.826171875,
          "loss": 0.3420129716396332,
          "passed": true
        }
      },
      "fixed_moe_vectorized": {
        "toy_xor_or_parity": {
          "accuracy": 0.509765625,
          "loss": 0.6927924156188965,
          "passed": false
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.845703125,
          "loss": 0.362593412399292,
          "passed": true
        }
      },
      "pvr_shared_only": {
        "toy_xor_or_parity": {
          "accuracy": 0.82421875,
          "loss": 0.3410707414150238,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.818359375,
          "loss": 0.3635461628437042,
          "passed": true
        }
      },
      "pvr_sparse_only": {
        "toy_xor_or_parity": {
          "accuracy": 0.84765625,
          "loss": 0.3523159623146057,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.861328125,
          "loss": 0.3188694715499878,
          "passed": true
        }
      },
      "pvr_full": {
        "toy_xor_or_parity": {
          "accuracy": 0.84375,
          "loss": 0.35769525170326233,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.82421875,
          "loss": 0.35173657536506653,
          "passed": true
        }
      },
      "pvr_full_fixed_owner_e0": {
        "toy_xor_or_parity": {
          "accuracy": 0.857421875,
          "loss": 0.3290098011493683,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.853515625,
          "loss": 0.33194106817245483,
          "passed": true
        }
      },
      "pvr_full_fixed_owner_round_robin": {
        "toy_xor_or_parity": {
          "accuracy": 0.904296875,
          "loss": 0.23576894402503967,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.78125,
          "loss": 0.4545818865299225,
          "passed": true
        }
      },
      "pvr_full_uniform_owner": {
        "toy_xor_or_parity": {
          "accuracy": 0.904296875,
          "loss": 0.23576894402503967,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.78125,
          "loss": 0.4545818865299225,
          "passed": true
        }
      },
      "pvr_full_expert_delta_scale_1": {
        "toy_xor_or_parity": {
          "accuracy": 0.84375,
          "loss": 0.35769525170326233,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.82421875,
          "loss": 0.35173657536506653,
          "passed": true
        }
      },
      "pvr_full_expert_delta_scale_2": {
        "toy_xor_or_parity": {
          "accuracy": 0.861328125,
          "loss": 0.3195511996746063,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.841796875,
          "loss": 0.3535851240158081,
          "passed": true
        }
      },
      "pvr_full_expert_delta_scale_4": {
        "toy_xor_or_parity": {
          "accuracy": 0.83984375,
          "loss": 0.363572359085083,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.82421875,
          "loss": 0.3535269796848297,
          "passed": true
        }
      },
      "pvr_full_expert_delta_scale_8": {
        "toy_xor_or_parity": {
          "accuracy": 0.87890625,
          "loss": 0.2637801468372345,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.80078125,
          "loss": 0.4102482199668884,
          "passed": true
        }
      },
      "pvr_full_delta_rank_16": {
        "toy_xor_or_parity": {
          "accuracy": 0.837890625,
          "loss": 0.38578876852989197,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.849609375,
          "loss": 0.32867398858070374,
          "passed": true
        }
      },
      "pvr_full_delta_rank_128": {
        "toy_xor_or_parity": {
          "accuracy": 0.8046875,
          "loss": 0.42358240485191345,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.802734375,
          "loss": 0.4144759774208069,
          "passed": true
        }
      },
      "pvr_full_micro_ffn_0_5x": {
        "toy_xor_or_parity": {
          "accuracy": 0.8046875,
          "loss": 0.42358240485191345,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.802734375,
          "loss": 0.4144759774208069,
          "passed": true
        }
      }
    },
    "nonlinear_results_by_model": {
      "dense_baseline": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.0006300712120719254,
          "passed": true
        },
        "toy_composition_2step": {
          "accuracy": 1.0,
          "loss": 0.0007317297859117389,
          "passed": true
        }
      },
      "fixed_moe_vectorized": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.0005578104173764586,
          "passed": true
        },
        "toy_composition_2step": {
          "accuracy": 1.0,
          "loss": 0.0018665791722014546,
          "passed": true
        }
      },
      "pvr_shared_only": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.0016847208607941866,
          "passed": true
        },
        "toy_composition_2step": {
          "accuracy": 1.0,
          "loss": 0.001044837525114417,
          "passed": true
        }
      },
      "pvr_sparse_only": {
        "toy_nonlinear_lookup": {
          "accuracy": 0.998046875,
          "loss": 0.007777318824082613,
          "passed": true
        },
        "toy_composition_2step": {
          "accuracy": 0.99609375,
          "loss": 0.013921980746090412,
          "passed": true
        }
      },
      "pvr_full": {
        "toy_nonlinear_lookup": {
          "accuracy": 0.998046875,
          "loss": 0.007906927727162838,
          "passed": true
        },
        "toy_composition_2step": {
          "accuracy": 1.0,
          "loss": 0.0010678712278604507,
          "passed": true
        }
      },
      "pvr_full_fixed_owner_e0": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.000528734119143337,
          "passed": true
        },
        "toy_composition_2step": {
          "accuracy": 0.998046875,
          "loss": 0.0056428443640470505,
          "passed": true
        }
      },
      "pvr_full_fixed_owner_round_robin": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.0015886081382632256,
          "passed": true
        },
        "toy_composition_2step": {
          "accuracy": 1.0,
          "loss": 0.0018943854374811053,
          "passed": true
        }
      },
      "pvr_full_uniform_owner": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.0015886081382632256,
          "passed": true
        },
        "toy_composition_2step": {
          "accuracy": 1.0,
          "loss": 0.0018943854374811053,
          "passed": true
        }
      },
      "pvr_full_expert_delta_scale_1": {
        "toy_nonlinear_lookup": {
          "accuracy": 0.998046875,
          "loss": 0.007906927727162838,
          "passed": true
        },
        "toy_composition_2step": {
          "accuracy": 1.0,
          "loss": 0.0010678712278604507,
          "passed": true
        }
      },
      "pvr_full_expert_delta_scale_2": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.002740811323747039,
          "passed": true
        },
        "toy_composition_2step": {
          "accuracy": 1.0,
          "loss": 0.0023305502254515886,
          "passed": true
        }
      },
      "pvr_full_expert_delta_scale_4": {
        "toy_nonlinear_lookup": {
          "accuracy": 0.998046875,
          "loss": 0.004821423441171646,
          "passed": true
        },
        "toy_composition_2step": {
          "accuracy": 1.0,
          "loss": 0.0024692928418517113,
          "passed": true
        }
      },
      "pvr_full_expert_delta_scale_8": {
        "toy_nonlinear_lookup": {
          "accuracy": 0.998046875,
          "loss": 0.0103463688865304,
          "passed": true
        },
        "toy_composition_2step": {
          "accuracy": 0.99609375,
          "loss": 0.005721672438085079,
          "passed": true
        }
      },
      "pvr_full_delta_rank_16": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.0007089923019520938,
          "passed": true
        },
        "toy_composition_2step": {
          "accuracy": 0.998046875,
          "loss": 0.005053055007010698,
          "passed": true
        }
      },
      "pvr_full_delta_rank_128": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.0007157090585678816,
          "passed": true
        },
        "toy_composition_2step": {
          "accuracy": 1.0,
          "loss": 0.005009970627725124,
          "passed": true
        }
      },
      "pvr_full_micro_ffn_0_5x": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.0007157090585678816,
          "passed": true
        },
        "toy_composition_2step": {
          "accuracy": 1.0,
          "loss": 0.005009970627725124,
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
        "0": 0.50390625,
        "1": 0.49609375
      },
      "max_class_ratio": 0.50390625
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.46875,
        "1": 0.53125
      },
      "max_class_ratio": 0.53125
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.50390625,
        "1": 0.49609375
      },
      "max_class_ratio": 0.50390625
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.46875,
        "1": 0.53125
      },
      "max_class_ratio": 0.53125
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.50390625,
        "1": 0.49609375
      },
      "max_class_ratio": 0.50390625
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.46875,
        "1": 0.53125
      },
      "max_class_ratio": 0.53125
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.50390625,
        "1": 0.49609375
      },
      "max_class_ratio": 0.50390625
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.46875,
        "1": 0.53125
      },
      "max_class_ratio": 0.53125
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.50390625,
        "1": 0.49609375
      },
      "max_class_ratio": 0.50390625
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.46875,
        "1": 0.53125
      },
      "max_class_ratio": 0.53125
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.50390625,
        "1": 0.49609375
      },
      "max_class_ratio": 0.50390625
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.46875,
        "1": 0.53125
      },
      "max_class_ratio": 0.53125
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.50390625,
        "1": 0.49609375
      },
      "max_class_ratio": 0.50390625
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.46875,
        "1": 0.53125
      },
      "max_class_ratio": 0.53125
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.50390625,
        "1": 0.49609375
      },
      "max_class_ratio": 0.50390625
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.46875,
        "1": 0.53125
      },
      "max_class_ratio": 0.53125
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.50390625,
        "1": 0.49609375
      },
      "max_class_ratio": 0.50390625
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.46875,
        "1": 0.53125
      },
      "max_class_ratio": 0.53125
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.50390625,
        "1": 0.49609375
      },
      "max_class_ratio": 0.50390625
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.46875,
        "1": 0.53125
      },
      "max_class_ratio": 0.53125
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.50390625,
        "1": 0.49609375
      },
      "max_class_ratio": 0.50390625
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.46875,
        "1": 0.53125
      },
      "max_class_ratio": 0.53125
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.50390625,
        "1": 0.49609375
      },
      "max_class_ratio": 0.50390625
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.46875,
        "1": 0.53125
      },
      "max_class_ratio": 0.53125
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.50390625,
        "1": 0.49609375
      },
      "max_class_ratio": 0.50390625
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.46875,
        "1": 0.53125
      },
      "max_class_ratio": 0.53125
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.50390625,
        "1": 0.49609375
      },
      "max_class_ratio": 0.50390625
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.46875,
        "1": 0.53125
      },
      "max_class_ratio": 0.53125
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.50390625,
        "1": 0.49609375
      },
      "max_class_ratio": 0.50390625
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.46875,
        "1": 0.53125
      },
      "max_class_ratio": 0.53125
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
        "1": 2,
        "2": 1,
        "3": 1,
        "4": 3,
        "5": 2,
        "6": 2,
        "8": 2,
        "9": 1,
        "10": 1,
        "12": 1,
        "13": 3,
        "14": 3,
        "16": 2,
        "17": 1,
        "18": 1,
        "19": 1,
        "20": 2,
        "21": 2,
        "22": 2,
        "23": 3,
        "24": 3,
        "25": 3,
        "26": 4,
        "28": 3,
        "29": 3,
        "30": 3,
        "31": 1,
        "33": 2,
        "34": 2,
        "35": 1,
        "36": 2,
        "37": 1
      },
      "baseline_random_loss": 4.9041900634765625,
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
        "1": 1,
        "2": 3,
        "3": 1,
        "4": 2,
        "5": 2,
        "6": 2,
        "7": 1,
        "8": 1,
        "9": 3,
        "11": 4,
        "12": 1,
        "13": 4,
        "16": 2,
        "18": 2,
        "19": 2,
        "20": 1,
        "21": 2,
        "22": 4,
        "23": 2,
        "24": 4,
        "25": 4,
        "27": 2,
        "28": 2,
        "29": 2,
        "30": 2,
        "31": 2,
        "33": 4,
        "34": 4,
        "38": 3,
        "39": 3,
        "40": 3,
        "41": 4
      },
      "baseline_random_loss": 5.550412654876709,
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
        "0": 258,
        "1": 254
      },
      "baseline_random_loss": 5.216707706451416,
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
        "0": 240,
        "1": 272
      },
      "baseline_random_loss": 5.212786674499512,
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
        "0": 32,
        "1": 28,
        "2": 34,
        "3": 37,
        "4": 29,
        "5": 38,
        "6": 34,
        "7": 29,
        "8": 29,
        "9": 40,
        "10": 28,
        "11": 28,
        "12": 28,
        "13": 21,
        "14": 35,
        "15": 42
      },
      "baseline_random_loss": 5.559519290924072,
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
        "0": 36,
        "1": 26,
        "2": 31,
        "3": 27,
        "4": 31,
        "5": 45,
        "6": 26,
        "7": 34,
        "8": 27,
        "9": 34,
        "10": 31,
        "11": 26,
        "12": 27,
        "13": 41,
        "14": 32,
        "15": 38
      },
      "baseline_random_loss": 5.613066673278809,
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
        "0": 1,
        "1": 2,
        "3": 2,
        "4": 3,
        "5": 3,
        "6": 7,
        "7": 2,
        "8": 3,
        "9": 1,
        "10": 2,
        "11": 3,
        "12": 1,
        "13": 1,
        "14": 6,
        "15": 2,
        "16": 1,
        "17": 2,
        "18": 3,
        "21": 2,
        "22": 2,
        "24": 3,
        "25": 4,
        "26": 1,
        "27": 2,
        "28": 1,
        "29": 3,
        "30": 2,
        "31": 3,
        "32": 1,
        "33": 1,
        "35": 3,
        "36": 4
      },
      "baseline_random_loss": 5.571826934814453,
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
        "1": 2,
        "2": 1,
        "3": 1,
        "4": 3,
        "5": 2,
        "6": 2,
        "8": 2,
        "9": 1,
        "10": 1,
        "12": 1,
        "13": 3,
        "14": 3,
        "16": 2,
        "17": 1,
        "18": 1,
        "19": 1,
        "20": 2,
        "21": 2,
        "22": 2,
        "23": 3,
        "24": 3,
        "25": 3,
        "26": 4,
        "28": 3,
        "29": 3,
        "30": 3,
        "31": 1,
        "33": 2,
        "34": 2,
        "35": 1,
        "36": 2,
        "37": 1
      },
      "baseline_random_loss": 4.808420658111572,
      "expected_random_loss": 5.545177444479562,
      "accuracy_definition": "mean argmax token accuracy over all positions"
    }
  ]
}
```