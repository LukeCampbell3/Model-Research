# PVR-EC Parity Init Sweep Report

**Status:** PVR_EC_NONLINEAR_OVERFIT_READY

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
  "status": "PVR_EC_NONLINEAR_OVERFIT_READY",
  "note": "Init sweep included via delta_rank and micro_ffn variants"
}
```