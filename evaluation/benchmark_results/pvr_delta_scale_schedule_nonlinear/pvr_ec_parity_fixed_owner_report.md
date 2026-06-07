# PVR-EC Parity Fixed Owner Report

**Status:** PVR_EC_FIXED_OWNER_PARITY_FAILED

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
  "status": "PVR_EC_FIXED_OWNER_PARITY_FAILED",
  "fixed_owner_e0_passed": false,
  "round_robin_passed": false,
  "uniform_owner_passed": false,
  "rows": []
}
```