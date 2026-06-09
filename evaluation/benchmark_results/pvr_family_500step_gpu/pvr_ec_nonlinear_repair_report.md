# PVR-EC Nonlinear Repair Report

**Status:** PVR_EC_NONLINEAR_REPAIR_APPLIED

**Statuses:** PVR_EC_DO_NOT_PROMOTE, PVR_EC_EXPERT_SCALE_UNDERPOWERED, PVR_EC_FIXED_OWNER_PARITY_FAILED, PVR_EC_NONLINEAR_OVERFIT_PASSED, PVR_EC_NONLINEAR_OVERFIT_READY, PVR_EC_PARITY_OVERFIT_PASSED, PVR_EC_ROUND_ROBIN_PARITY_PASSED

```json
{
  "metadata": {
    "timestamp": "2026-06-09T01:18:35.140547",
    "run_id": "algo_20260609_011533_pvr-overfit-sanity",
    "git_commit": "aff470f9ed548af833e78f9fb075ed1fa78a9af1",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 42,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode pvr-overfit-sanity --scale tiny --device cuda --amp --pvr-overfit-tasks toy_identity,toy_xor_or_parity,toy_xor_or_parity_balanced,toy_nonlinear_lookup,single_batch_memorization --pvr-overfit-steps 500 --pvr-overfit-batch-size 32 --models dense_baseline,fixed_moe_vectorized,pvr_full,pvr_full_fixed_owner_e0,pvr_full_fixed_owner_round_robin,pvr_full_expert_delta_scale_4,pvr_full_expert_delta_scale_8,pvr_full_micro_ffn_0_5x --run-nonlinear-overfit-diagnostic --run-gradient-flow-diagnostic --run-expert-contribution-diagnostic --run-loss-target-sanity --output-dir evaluation/benchmark_results/pvr_family_500step_gpu",
    "model_variants": [
      "dense_baseline",
      "fixed_moe_vectorized",
      "pvr_full",
      "pvr_full_fixed_owner_e0",
      "pvr_full_fixed_owner_round_robin",
      "pvr_full_expert_delta_scale_4",
      "pvr_full_expert_delta_scale_8",
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
      "toy_xor_or_parity_balanced",
      "toy_nonlinear_lookup",
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
    "PVR_EC_ROUND_ROBIN_PARITY_PASSED"
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
      "PVR_EC_ROUND_ROBIN_PARITY_PASSED"
    ],
    "controls_pass": true,
    "fixed_owner_parity": false,
    "round_robin_parity": true,
    "uniform_owner_parity": false,
    "learned_owner_parity": true,
    "sparse_only_parity": false,
    "shared_only_parity": false,
    "dense_parity": true,
    "fixed_moe_parity": false,
    "micro_ffn_parity": true,
    "best_expert_delta_scale": 8.0,
    "best_expert_delta_scale_accuracy": 0.8046875,
    "dominant_failure_mode": "expert_scale_underpowered",
    "recommended_repair": "expert_delta_scale_schedule_target_8.0",
    "parity_results_by_model": {
      "dense_baseline": {
        "toy_xor_or_parity": {
          "accuracy": 0.767578125,
          "loss": 0.4201437830924988,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.75390625,
          "loss": 0.44394946098327637,
          "passed": true
        }
      },
      "fixed_moe_vectorized": {
        "toy_xor_or_parity": {
          "accuracy": 0.62109375,
          "loss": 0.6504129767417908,
          "passed": false
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.654296875,
          "loss": 0.6322320699691772,
          "passed": false
        }
      },
      "pvr_full": {
        "toy_xor_or_parity": {
          "accuracy": 0.73046875,
          "loss": 0.5112131237983704,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.833984375,
          "loss": 0.36243146657943726,
          "passed": true
        }
      },
      "pvr_full_fixed_owner_e0": {
        "toy_xor_or_parity": {
          "accuracy": 0.62890625,
          "loss": 0.6600556969642639,
          "passed": false
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.5234375,
          "loss": 0.691436231136322,
          "passed": false
        }
      },
      "pvr_full_fixed_owner_round_robin": {
        "toy_xor_or_parity": {
          "accuracy": 0.67578125,
          "loss": 0.5897818803787231,
          "passed": false
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.76171875,
          "loss": 0.45360827445983887,
          "passed": true
        }
      },
      "pvr_full_expert_delta_scale_4": {
        "toy_xor_or_parity": {
          "accuracy": 0.751953125,
          "loss": 0.4450244605541229,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.77734375,
          "loss": 0.44185444712638855,
          "passed": true
        }
      },
      "pvr_full_expert_delta_scale_8": {
        "toy_xor_or_parity": {
          "accuracy": 0.68359375,
          "loss": 0.5452841520309448,
          "passed": false
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.8046875,
          "loss": 0.38640928268432617,
          "passed": true
        }
      },
      "pvr_full_micro_ffn_0_5x": {
        "toy_xor_or_parity": {
          "accuracy": 0.73046875,
          "loss": 0.5112131237983704,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.833984375,
          "loss": 0.36243146657943726,
          "passed": true
        }
      }
    },
    "nonlinear_results_by_model": {
      "dense_baseline": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.0011454967316240072,
          "passed": true
        }
      },
      "fixed_moe_vectorized": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.0010864429641515017,
          "passed": true
        }
      },
      "pvr_full": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.0009301644167862833,
          "passed": true
        }
      },
      "pvr_full_fixed_owner_e0": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.0010312689701095223,
          "passed": true
        }
      },
      "pvr_full_fixed_owner_round_robin": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.0010269364574924111,
          "passed": true
        }
      },
      "pvr_full_expert_delta_scale_4": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.000982863362878561,
          "passed": true
        }
      },
      "pvr_full_expert_delta_scale_8": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.0009598180768080056,
          "passed": true
        }
      },
      "pvr_full_micro_ffn_0_5x": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.0009301644167862833,
          "passed": true
        }
      }
    }
  },
  "status": "PVR_EC_NONLINEAR_REPAIR_APPLIED",
  "dominant_failure_mode": "expert_scale_underpowered",
  "recommended_repair": "expert_delta_scale_schedule_target_8.0",
  "repair_applied": false,
  "note": "Repair must be applied and confirmed in a follow-up run"
}
```