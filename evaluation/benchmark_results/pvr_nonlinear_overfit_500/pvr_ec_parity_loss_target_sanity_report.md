# PVR-EC Parity Loss Target Sanity Report

**Status:** PVR_EC_LOSS_TARGET_SANITY_PASSED

**Statuses:** PVR_EC_DO_NOT_PROMOTE, PVR_EC_EXPERT_SCALE_UNDERPOWERED, PVR_EC_FIXED_OWNER_PARITY_PASSED, PVR_EC_NONLINEAR_OVERFIT_PASSED, PVR_EC_NONLINEAR_OVERFIT_READY, PVR_EC_PARITY_OVERFIT_PASSED, PVR_EC_ROUND_ROBIN_PARITY_PASSED

```json
{
  "metadata": {
    "timestamp": "2026-06-07T00:12:06.267046",
    "run_id": "algo_20260606_235335_pvr-overfit-sanity",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 42,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode pvr-overfit-sanity --scale tiny --device cuda --amp --pvr-overfit-tasks toy_xor_or_parity,toy_xor_or_parity_balanced,toy_xor_or_parity_longer_context,toy_nonlinear_lookup,toy_composition_2step,single_batch_memorization,toy_identity,toy_copy --pvr-overfit-steps 500 --pvr-overfit-batch-size 32 --models dense_baseline,fixed_moe_vectorized,pvr_shared_only,pvr_sparse_only,pvr_full,pvr_full_fixed_owner_e0,pvr_full_fixed_owner_round_robin,pvr_full_uniform_owner,pvr_full_shared_scale_0_5,pvr_full_shared_scale_0_25,pvr_full_shared_scale_0_0,pvr_full_expert_delta_scale_1,pvr_full_expert_delta_scale_2,pvr_full_expert_delta_scale_4,pvr_full_expert_delta_scale_8,pvr_full_delta_rank_16,pvr_full_delta_rank_64,pvr_full_delta_rank_128,pvr_full_micro_ffn_0_5x --run-nonlinear-overfit-diagnostic --run-gradient-flow-diagnostic --run-expert-contribution-diagnostic --run-loss-target-sanity --output-dir evaluation/benchmark_results/pvr_nonlinear_overfit_500",
    "model_variants": [
      "dense_baseline",
      "fixed_moe_vectorized",
      "pvr_shared_only",
      "pvr_sparse_only",
      "pvr_full",
      "pvr_full_fixed_owner_e0",
      "pvr_full_fixed_owner_round_robin",
      "pvr_full_uniform_owner",
      "pvr_full_shared_scale_0_5",
      "pvr_full_shared_scale_0_25",
      "pvr_full_shared_scale_0_0",
      "pvr_full_expert_delta_scale_1",
      "pvr_full_expert_delta_scale_2",
      "pvr_full_expert_delta_scale_4",
      "pvr_full_expert_delta_scale_8",
      "pvr_full_delta_rank_16",
      "pvr_full_delta_rank_64",
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
    "scale": "tiny",
    "families": [
      "clrs",
      "listops",
      "scan",
      "dyck"
    ],
    "pvr_overfit_tasks": [
      "toy_xor_or_parity",
      "toy_xor_or_parity_balanced",
      "toy_xor_or_parity_longer_context",
      "toy_nonlinear_lookup",
      "toy_composition_2step",
      "single_batch_memorization",
      "toy_identity",
      "toy_copy"
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
    "fixed_moe_parity": false,
    "micro_ffn_parity": true,
    "best_expert_delta_scale": 8.0,
    "best_expert_delta_scale_accuracy": 0.853515625,
    "dominant_failure_mode": "expert_scale_underpowered",
    "recommended_repair": "expert_delta_scale_schedule_target_8.0",
    "parity_results_by_model": {
      "dense_baseline": {
        "toy_xor_or_parity": {
          "accuracy": 0.76171875,
          "loss": 0.47207963466644287,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.80078125,
          "loss": 0.40709388256073,
          "passed": true
        }
      },
      "fixed_moe_vectorized": {
        "toy_xor_or_parity": {
          "accuracy": 0.7109375,
          "loss": 0.551121175289154,
          "passed": false
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.615234375,
          "loss": 0.6467021703720093,
          "passed": false
        }
      },
      "pvr_shared_only": {
        "toy_xor_or_parity": {
          "accuracy": 0.720703125,
          "loss": 0.4968399405479431,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.53515625,
          "loss": 0.6910150647163391,
          "passed": false
        }
      },
      "pvr_sparse_only": {
        "toy_xor_or_parity": {
          "accuracy": 0.77734375,
          "loss": 0.4247889518737793,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.80078125,
          "loss": 0.3846411108970642,
          "passed": true
        }
      },
      "pvr_full": {
        "toy_xor_or_parity": {
          "accuracy": 0.8046875,
          "loss": 0.3971809446811676,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.796875,
          "loss": 0.42494431138038635,
          "passed": true
        }
      },
      "pvr_full_shared_scale_0_5": {
        "toy_xor_or_parity": {
          "accuracy": 0.771484375,
          "loss": 0.4656349718570709,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.75,
          "loss": 0.4686985909938812,
          "passed": true
        }
      },
      "pvr_full_shared_scale_0_25": {
        "toy_xor_or_parity": {
          "accuracy": 0.81640625,
          "loss": 0.38131117820739746,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.724609375,
          "loss": 0.5357493162155151,
          "passed": true
        }
      },
      "pvr_full_shared_scale_0_0": {
        "toy_xor_or_parity": {
          "accuracy": 0.77734375,
          "loss": 0.4247889518737793,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.80078125,
          "loss": 0.3846411108970642,
          "passed": true
        }
      },
      "pvr_full_fixed_owner_e0": {
        "toy_xor_or_parity": {
          "accuracy": 0.740234375,
          "loss": 0.5044806003570557,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.623046875,
          "loss": 0.6422012448310852,
          "passed": false
        }
      },
      "pvr_full_fixed_owner_round_robin": {
        "toy_xor_or_parity": {
          "accuracy": 0.673828125,
          "loss": 0.5772316455841064,
          "passed": false
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.771484375,
          "loss": 0.43294835090637207,
          "passed": true
        }
      },
      "pvr_full_uniform_owner": {
        "toy_xor_or_parity": {
          "accuracy": 0.673828125,
          "loss": 0.5772316455841064,
          "passed": false
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.771484375,
          "loss": 0.43294835090637207,
          "passed": true
        }
      },
      "pvr_full_expert_delta_scale_1": {
        "toy_xor_or_parity": {
          "accuracy": 0.8046875,
          "loss": 0.3971809446811676,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.796875,
          "loss": 0.42494431138038635,
          "passed": true
        }
      },
      "pvr_full_expert_delta_scale_2": {
        "toy_xor_or_parity": {
          "accuracy": 0.755859375,
          "loss": 0.46945804357528687,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.794921875,
          "loss": 0.41787275671958923,
          "passed": true
        }
      },
      "pvr_full_expert_delta_scale_4": {
        "toy_xor_or_parity": {
          "accuracy": 0.794921875,
          "loss": 0.4144524037837982,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.71875,
          "loss": 0.5258010029792786,
          "passed": true
        }
      },
      "pvr_full_expert_delta_scale_8": {
        "toy_xor_or_parity": {
          "accuracy": 0.779296875,
          "loss": 0.45803773403167725,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.853515625,
          "loss": 0.3090191185474396,
          "passed": true
        }
      },
      "pvr_full_delta_rank_16": {
        "toy_xor_or_parity": {
          "accuracy": 0.802734375,
          "loss": 0.3905750811100006,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.794921875,
          "loss": 0.3956773281097412,
          "passed": true
        }
      },
      "pvr_full_delta_rank_64": {
        "toy_xor_or_parity": {
          "accuracy": 0.8046875,
          "loss": 0.3971809446811676,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.796875,
          "loss": 0.42494431138038635,
          "passed": true
        }
      },
      "pvr_full_delta_rank_128": {
        "toy_xor_or_parity": {
          "accuracy": 0.625,
          "loss": 0.626086950302124,
          "passed": false
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.794921875,
          "loss": 0.4034782648086548,
          "passed": true
        }
      },
      "pvr_full_micro_ffn_0_5x": {
        "toy_xor_or_parity": {
          "accuracy": 0.8046875,
          "loss": 0.3971809446811676,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.796875,
          "loss": 0.42494431138038635,
          "passed": true
        }
      }
    },
    "nonlinear_results_by_model": {
      "dense_baseline": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.0012303892290219665,
          "passed": true
        },
        "toy_composition_2step": {
          "accuracy": 1.0,
          "loss": 0.001221793470904231,
          "passed": true
        }
      },
      "fixed_moe_vectorized": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.001068345969542861,
          "passed": true
        },
        "toy_composition_2step": {
          "accuracy": 1.0,
          "loss": 0.0011327901156619191,
          "passed": true
        }
      },
      "pvr_shared_only": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.00107915501575917,
          "passed": true
        },
        "toy_composition_2step": {
          "accuracy": 1.0,
          "loss": 0.0013454275904223323,
          "passed": true
        }
      },
      "pvr_sparse_only": {
        "toy_nonlinear_lookup": {
          "accuracy": 0.99609375,
          "loss": 0.018191849812865257,
          "passed": true
        },
        "toy_composition_2step": {
          "accuracy": 1.0,
          "loss": 0.0009404309093952179,
          "passed": true
        }
      },
      "pvr_full": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.0009064886253327131,
          "passed": true
        },
        "toy_composition_2step": {
          "accuracy": 1.0,
          "loss": 0.0009820028208196163,
          "passed": true
        }
      },
      "pvr_full_shared_scale_0_5": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.000965653860475868,
          "passed": true
        },
        "toy_composition_2step": {
          "accuracy": 1.0,
          "loss": 0.0009901876328513026,
          "passed": true
        }
      },
      "pvr_full_shared_scale_0_25": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.002358114579692483,
          "passed": true
        },
        "toy_composition_2step": {
          "accuracy": 1.0,
          "loss": 0.001000001560896635,
          "passed": true
        }
      },
      "pvr_full_shared_scale_0_0": {
        "toy_nonlinear_lookup": {
          "accuracy": 0.99609375,
          "loss": 0.018191849812865257,
          "passed": true
        },
        "toy_composition_2step": {
          "accuracy": 1.0,
          "loss": 0.0009404309093952179,
          "passed": true
        }
      },
      "pvr_full_fixed_owner_e0": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.0010915970196947455,
          "passed": true
        },
        "toy_composition_2step": {
          "accuracy": 1.0,
          "loss": 0.001021679723635316,
          "passed": true
        }
      },
      "pvr_full_fixed_owner_round_robin": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.0011035837233066559,
          "passed": true
        },
        "toy_composition_2step": {
          "accuracy": 1.0,
          "loss": 0.0010299419518560171,
          "passed": true
        }
      },
      "pvr_full_uniform_owner": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.0011035837233066559,
          "passed": true
        },
        "toy_composition_2step": {
          "accuracy": 1.0,
          "loss": 0.0010299419518560171,
          "passed": true
        }
      },
      "pvr_full_expert_delta_scale_1": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.0009064886253327131,
          "passed": true
        },
        "toy_composition_2step": {
          "accuracy": 1.0,
          "loss": 0.0009820028208196163,
          "passed": true
        }
      },
      "pvr_full_expert_delta_scale_2": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.0014260424068197608,
          "passed": true
        },
        "toy_composition_2step": {
          "accuracy": 1.0,
          "loss": 0.0012056099949404597,
          "passed": true
        }
      },
      "pvr_full_expert_delta_scale_4": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.003146643517538905,
          "passed": true
        },
        "toy_composition_2step": {
          "accuracy": 1.0,
          "loss": 0.0010255401721224189,
          "passed": true
        }
      },
      "pvr_full_expert_delta_scale_8": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.001524430001154542,
          "passed": true
        },
        "toy_composition_2step": {
          "accuracy": 1.0,
          "loss": 0.001019660267047584,
          "passed": true
        }
      },
      "pvr_full_delta_rank_16": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.0010937904007732868,
          "passed": true
        },
        "toy_composition_2step": {
          "accuracy": 1.0,
          "loss": 0.0011708762031048536,
          "passed": true
        }
      },
      "pvr_full_delta_rank_64": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.0009064886253327131,
          "passed": true
        },
        "toy_composition_2step": {
          "accuracy": 1.0,
          "loss": 0.0009820028208196163,
          "passed": true
        }
      },
      "pvr_full_delta_rank_128": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.0010717957047745585,
          "passed": true
        },
        "toy_composition_2step": {
          "accuracy": 0.998046875,
          "loss": 0.011942648328840733,
          "passed": true
        }
      },
      "pvr_full_micro_ffn_0_5x": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.0009064886253327131,
          "passed": true
        },
        "toy_composition_2step": {
          "accuracy": 1.0,
          "loss": 0.0009820028208196163,
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
        "0": 0.509765625,
        "1": 0.490234375
      },
      "max_class_ratio": 0.509765625
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.525390625,
        "1": 0.474609375
      },
      "max_class_ratio": 0.525390625
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.4609375,
        "1": 0.5390625
      },
      "max_class_ratio": 0.5390625
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
        "0": 0.525390625,
        "1": 0.474609375
      },
      "max_class_ratio": 0.525390625
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.4609375,
        "1": 0.5390625
      },
      "max_class_ratio": 0.5390625
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
        "0": 0.525390625,
        "1": 0.474609375
      },
      "max_class_ratio": 0.525390625
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.4609375,
        "1": 0.5390625
      },
      "max_class_ratio": 0.5390625
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
        "0": 0.525390625,
        "1": 0.474609375
      },
      "max_class_ratio": 0.525390625
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.4609375,
        "1": 0.5390625
      },
      "max_class_ratio": 0.5390625
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
        "0": 0.525390625,
        "1": 0.474609375
      },
      "max_class_ratio": 0.525390625
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.4609375,
        "1": 0.5390625
      },
      "max_class_ratio": 0.5390625
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
        "0": 0.525390625,
        "1": 0.474609375
      },
      "max_class_ratio": 0.525390625
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.4609375,
        "1": 0.5390625
      },
      "max_class_ratio": 0.5390625
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
        "0": 0.525390625,
        "1": 0.474609375
      },
      "max_class_ratio": 0.525390625
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.4609375,
        "1": 0.5390625
      },
      "max_class_ratio": 0.5390625
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
        "0": 0.525390625,
        "1": 0.474609375
      },
      "max_class_ratio": 0.525390625
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.4609375,
        "1": 0.5390625
      },
      "max_class_ratio": 0.5390625
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
        "0": 0.525390625,
        "1": 0.474609375
      },
      "max_class_ratio": 0.525390625
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.4609375,
        "1": 0.5390625
      },
      "max_class_ratio": 0.5390625
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
        "0": 0.525390625,
        "1": 0.474609375
      },
      "max_class_ratio": 0.525390625
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.4609375,
        "1": 0.5390625
      },
      "max_class_ratio": 0.5390625
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
        "0": 0.525390625,
        "1": 0.474609375
      },
      "max_class_ratio": 0.525390625
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.4609375,
        "1": 0.5390625
      },
      "max_class_ratio": 0.5390625
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
        "0": 0.525390625,
        "1": 0.474609375
      },
      "max_class_ratio": 0.525390625
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.4609375,
        "1": 0.5390625
      },
      "max_class_ratio": 0.5390625
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
        "0": 0.525390625,
        "1": 0.474609375
      },
      "max_class_ratio": 0.525390625
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.4609375,
        "1": 0.5390625
      },
      "max_class_ratio": 0.5390625
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
        "0": 0.525390625,
        "1": 0.474609375
      },
      "max_class_ratio": 0.525390625
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.4609375,
        "1": 0.5390625
      },
      "max_class_ratio": 0.5390625
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
        "0": 0.525390625,
        "1": 0.474609375
      },
      "max_class_ratio": 0.525390625
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.4609375,
        "1": 0.5390625
      },
      "max_class_ratio": 0.5390625
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
        "0": 0.525390625,
        "1": 0.474609375
      },
      "max_class_ratio": 0.525390625
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.4609375,
        "1": 0.5390625
      },
      "max_class_ratio": 0.5390625
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
        "0": 0.525390625,
        "1": 0.474609375
      },
      "max_class_ratio": 0.525390625
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.4609375,
        "1": 0.5390625
      },
      "max_class_ratio": 0.5390625
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
        "0": 0.525390625,
        "1": 0.474609375
      },
      "max_class_ratio": 0.525390625
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.4609375,
        "1": 0.5390625
      },
      "max_class_ratio": 0.5390625
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
        "0": 0.525390625,
        "1": 0.474609375
      },
      "max_class_ratio": 0.525390625
    },
    {
      "balanced": true,
      "class_ratios": {
        "0": 0.4609375,
        "1": 0.5390625
      },
      "max_class_ratio": 0.5390625
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
        "0": 261,
        "1": 251
      },
      "baseline_random_loss": 5.305920600891113,
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
        "0": 269,
        "1": 243
      },
      "baseline_random_loss": 5.291004180908203,
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
        "0": 236,
        "1": 276
      },
      "baseline_random_loss": 5.331918716430664,
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
        "0": 30,
        "1": 23,
        "2": 39,
        "3": 33,
        "4": 24,
        "5": 39,
        "6": 29,
        "7": 36,
        "8": 39,
        "9": 30,
        "10": 37,
        "11": 24,
        "12": 40,
        "13": 26,
        "14": 31,
        "15": 32
      },
      "baseline_random_loss": 5.529552459716797,
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
        "0": 37,
        "1": 31,
        "2": 25,
        "3": 25,
        "4": 37,
        "5": 25,
        "6": 35,
        "7": 46,
        "8": 25,
        "9": 30,
        "10": 40,
        "11": 28,
        "12": 35,
        "13": 32,
        "14": 32,
        "15": 29
      },
      "baseline_random_loss": 5.576483726501465,
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
        "0": 2,
        "1": 3,
        "2": 1,
        "4": 2,
        "5": 2,
        "6": 2,
        "8": 1,
        "9": 2,
        "10": 3,
        "11": 2,
        "13": 2,
        "14": 3,
        "15": 3,
        "16": 1,
        "17": 1,
        "18": 2,
        "19": 2,
        "21": 1,
        "22": 2,
        "23": 3,
        "24": 2,
        "25": 4,
        "26": 2,
        "27": 1,
        "28": 3,
        "30": 1,
        "32": 1,
        "33": 1,
        "34": 2,
        "35": 1,
        "36": 1,
        "37": 2
      },
      "baseline_random_loss": 5.551106929779053,
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
        "1": 3,
        "2": 1,
        "4": 3,
        "5": 2,
        "6": 3,
        "7": 3,
        "9": 2,
        "10": 1,
        "11": 4,
        "13": 3,
        "15": 2,
        "16": 1,
        "18": 3,
        "20": 3,
        "21": 2,
        "23": 6,
        "26": 2,
        "27": 4,
        "28": 2,
        "30": 3,
        "31": 2,
        "32": 4,
        "35": 1,
        "37": 1,
        "38": 1,
        "39": 3,
        "40": 1,
        "41": 1,
        "42": 2,
        "43": 2,
        "44": 1,
        "45": 2
      },
      "baseline_random_loss": 5.002363204956055,
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
        "1": 5,
        "2": 2,
        "3": 1,
        "4": 2,
        "5": 2,
        "6": 2,
        "9": 5,
        "10": 1,
        "11": 2,
        "12": 6,
        "13": 1,
        "15": 4,
        "16": 3,
        "17": 2,
        "18": 2,
        "20": 3,
        "21": 2,
        "22": 5,
        "23": 1,
        "24": 4,
        "26": 3,
        "27": 2,
        "28": 1,
        "29": 1,
        "30": 1,
        "31": 1,
        "32": 2,
        "33": 2,
        "34": 2,
        "35": 2,
        "36": 4,
        "37": 1
      },
      "baseline_random_loss": 5.52034854888916,
      "expected_random_loss": 5.545177444479562,
      "accuracy_definition": "mean argmax token accuracy over all positions"
    }
  ]
}
```