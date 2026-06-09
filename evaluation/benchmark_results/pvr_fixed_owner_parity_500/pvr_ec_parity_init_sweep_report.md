# PVR-EC Parity Init Sweep Report

**Status:** PVR_EC_NONLINEAR_OVERFIT_READY

**Statuses:** PVR_EC_DO_NOT_PROMOTE, PVR_EC_FIXED_OWNER_PARITY_PASSED, PVR_EC_NONLINEAR_OVERFIT_PASSED, PVR_EC_NONLINEAR_OVERFIT_READY, PVR_EC_PARITY_OVERFIT_PASSED, PVR_EC_ROUND_ROBIN_PARITY_PASSED

```json
{
  "metadata": {
    "timestamp": "2026-06-09T01:56:23.960785",
    "run_id": "algo_20260609_015459_pvr-overfit-sanity",
    "git_commit": "aff470f9ed548af833e78f9fb075ed1fa78a9af1",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 42,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode pvr-overfit-sanity --scale small --device cuda --amp --pvr-overfit-tasks toy_xor_or_parity,toy_xor_or_parity_balanced,toy_nonlinear_lookup --pvr-overfit-steps 500 --pvr-overfit-batch-size 32 --models pvr_full,pvr_full_fixed_owner_e0,pvr_full_fixed_owner_round_robin,pvr_full_uniform_owner,pvr_sparse_only,pvr_shared_only --run-nonlinear-overfit-diagnostic --output-dir evaluation/benchmark_results/pvr_fixed_owner_parity_500",
    "model_variants": [
      "pvr_full",
      "pvr_full_fixed_owner_e0",
      "pvr_full_fixed_owner_round_robin",
      "pvr_full_uniform_owner",
      "pvr_sparse_only",
      "pvr_shared_only"
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
      "toy_xor_or_parity",
      "toy_xor_or_parity_balanced",
      "toy_nonlinear_lookup"
    ],
    "pvr_overfit_steps": 500,
    "pvr_overfit_batch_size": 32,
    "failures": []
  },
  "statuses": [
    "PVR_EC_DO_NOT_PROMOTE",
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
    "dense_parity": false,
    "fixed_moe_parity": false,
    "micro_ffn_parity": false,
    "best_expert_delta_scale": null,
    "best_expert_delta_scale_accuracy": 0.0,
    "dominant_failure_mode": "unknown",
    "recommended_repair": "none",
    "parity_results_by_model": {
      "pvr_shared_only": {
        "toy_xor_or_parity": {
          "accuracy": 0.833984375,
          "loss": 0.33894726634025574,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.80859375,
          "loss": 0.36571696400642395,
          "passed": true
        }
      },
      "pvr_sparse_only": {
        "toy_xor_or_parity": {
          "accuracy": 0.802734375,
          "loss": 0.41138383746147156,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.802734375,
          "loss": 0.4059789180755615,
          "passed": true
        }
      },
      "pvr_full": {
        "toy_xor_or_parity": {
          "accuracy": 0.830078125,
          "loss": 0.3407552242279053,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.84375,
          "loss": 0.34503689408302307,
          "passed": true
        }
      },
      "pvr_full_fixed_owner_e0": {
        "toy_xor_or_parity": {
          "accuracy": 0.859375,
          "loss": 0.3024533987045288,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.8515625,
          "loss": 0.33646851778030396,
          "passed": true
        }
      },
      "pvr_full_fixed_owner_round_robin": {
        "toy_xor_or_parity": {
          "accuracy": 0.859375,
          "loss": 0.28743794560432434,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.90234375,
          "loss": 0.25693443417549133,
          "passed": true
        }
      },
      "pvr_full_uniform_owner": {
        "toy_xor_or_parity": {
          "accuracy": 0.859375,
          "loss": 0.28743794560432434,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.90234375,
          "loss": 0.25693443417549133,
          "passed": true
        }
      }
    },
    "nonlinear_results_by_model": {
      "pvr_shared_only": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.0013917478499934077,
          "passed": true
        }
      },
      "pvr_sparse_only": {
        "toy_nonlinear_lookup": {
          "accuracy": 0.998046875,
          "loss": 0.006234675645828247,
          "passed": true
        }
      },
      "pvr_full": {
        "toy_nonlinear_lookup": {
          "accuracy": 0.998046875,
          "loss": 0.014162704348564148,
          "passed": true
        }
      },
      "pvr_full_fixed_owner_e0": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.002840080764144659,
          "passed": true
        }
      },
      "pvr_full_fixed_owner_round_robin": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.000980533310212195,
          "passed": true
        }
      },
      "pvr_full_uniform_owner": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.000980533310212195,
          "passed": true
        }
      }
    }
  },
  "status": "PVR_EC_NONLINEAR_OVERFIT_READY",
  "note": "Init sweep included via delta_rank and micro_ffn variants"
}
```