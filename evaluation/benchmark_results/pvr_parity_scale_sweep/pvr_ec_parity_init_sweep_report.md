# PVR-EC Parity Init Sweep Report

**Status:** PVR_EC_NONLINEAR_OVERFIT_READY

**Statuses:** PVR_EC_DO_NOT_PROMOTE, PVR_EC_EXPERT_SCALE_UNDERPOWERED, PVR_EC_FIXED_OWNER_PARITY_FAILED, PVR_EC_NONLINEAR_OVERFIT_FAILED, PVR_EC_NONLINEAR_OVERFIT_READY, PVR_EC_PARITY_OVERFIT_PASSED, PVR_EC_ROUND_ROBIN_PARITY_FAILED

```json
{
  "metadata": {
    "timestamp": "2026-06-09T01:54:48.039474",
    "run_id": "algo_20260609_015325_pvr-overfit-sanity",
    "git_commit": "aff470f9ed548af833e78f9fb075ed1fa78a9af1",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 42,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode pvr-overfit-sanity --scale small --device cuda --amp --pvr-overfit-tasks toy_xor_or_parity,toy_xor_or_parity_balanced --pvr-overfit-steps 500 --pvr-overfit-batch-size 32 --models pvr_full,pvr_full_shared_scale_0_5,pvr_full_shared_scale_0_25,pvr_full_shared_scale_0_0,pvr_full_expert_delta_scale_1,pvr_full_expert_delta_scale_2,pvr_full_expert_delta_scale_4,pvr_full_expert_delta_scale_8 --run-nonlinear-overfit-diagnostic --output-dir evaluation/benchmark_results/pvr_parity_scale_sweep",
    "model_variants": [
      "pvr_full",
      "pvr_full_shared_scale_0_5",
      "pvr_full_shared_scale_0_25",
      "pvr_full_shared_scale_0_0",
      "pvr_full_expert_delta_scale_1",
      "pvr_full_expert_delta_scale_2",
      "pvr_full_expert_delta_scale_4",
      "pvr_full_expert_delta_scale_8"
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
      "toy_xor_or_parity_balanced"
    ],
    "pvr_overfit_steps": 500,
    "pvr_overfit_batch_size": 32,
    "failures": []
  },
  "statuses": [
    "PVR_EC_DO_NOT_PROMOTE",
    "PVR_EC_EXPERT_SCALE_UNDERPOWERED",
    "PVR_EC_FIXED_OWNER_PARITY_FAILED",
    "PVR_EC_NONLINEAR_OVERFIT_FAILED",
    "PVR_EC_NONLINEAR_OVERFIT_READY",
    "PVR_EC_PARITY_OVERFIT_PASSED",
    "PVR_EC_ROUND_ROBIN_PARITY_FAILED"
  ],
  "promotion_ready": false,
  "analysis": {
    "overall_status": "PVR_EC_NONLINEAR_OVERFIT_FAILED",
    "statuses": [
      "PVR_EC_DO_NOT_PROMOTE",
      "PVR_EC_EXPERT_SCALE_UNDERPOWERED",
      "PVR_EC_FIXED_OWNER_PARITY_FAILED",
      "PVR_EC_NONLINEAR_OVERFIT_FAILED",
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
    "best_expert_delta_scale": 2.0,
    "best_expert_delta_scale_accuracy": 0.8671875,
    "dominant_failure_mode": "expert_scale_underpowered",
    "recommended_repair": "expert_delta_scale_schedule_target_2.0",
    "parity_results_by_model": {
      "pvr_full": {
        "toy_xor_or_parity": {
          "accuracy": 0.84765625,
          "loss": 0.35332849621772766,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.77734375,
          "loss": 0.4032782018184662,
          "passed": true
        }
      },
      "pvr_full_shared_scale_0_5": {
        "toy_xor_or_parity": {
          "accuracy": 0.82421875,
          "loss": 0.3624371886253357,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.80859375,
          "loss": 0.3753509521484375,
          "passed": true
        }
      },
      "pvr_full_shared_scale_0_25": {
        "toy_xor_or_parity": {
          "accuracy": 0.787109375,
          "loss": 0.4257141947746277,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.787109375,
          "loss": 0.4234113097190857,
          "passed": true
        }
      },
      "pvr_full_shared_scale_0_0": {
        "toy_xor_or_parity": {
          "accuracy": 0.7890625,
          "loss": 0.41980597376823425,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.810546875,
          "loss": 0.39652928709983826,
          "passed": true
        }
      },
      "pvr_full_expert_delta_scale_1": {
        "toy_xor_or_parity": {
          "accuracy": 0.84765625,
          "loss": 0.35332849621772766,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.77734375,
          "loss": 0.4032782018184662,
          "passed": true
        }
      },
      "pvr_full_expert_delta_scale_2": {
        "toy_xor_or_parity": {
          "accuracy": 0.8671875,
          "loss": 0.3185996413230896,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.818359375,
          "loss": 0.41827279329299927,
          "passed": true
        }
      },
      "pvr_full_expert_delta_scale_4": {
        "toy_xor_or_parity": {
          "accuracy": 0.861328125,
          "loss": 0.31747058033943176,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.84375,
          "loss": 0.3162716031074524,
          "passed": true
        }
      },
      "pvr_full_expert_delta_scale_8": {
        "toy_xor_or_parity": {
          "accuracy": 0.841796875,
          "loss": 0.36368608474731445,
          "passed": true
        },
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.83203125,
          "loss": 0.3323166072368622,
          "passed": true
        }
      }
    },
    "nonlinear_results_by_model": {
      "pvr_full": {},
      "pvr_full_shared_scale_0_5": {},
      "pvr_full_shared_scale_0_25": {},
      "pvr_full_shared_scale_0_0": {},
      "pvr_full_expert_delta_scale_1": {},
      "pvr_full_expert_delta_scale_2": {},
      "pvr_full_expert_delta_scale_4": {},
      "pvr_full_expert_delta_scale_8": {}
    }
  },
  "status": "PVR_EC_NONLINEAR_OVERFIT_READY",
  "note": "Init sweep included via delta_rank and micro_ffn variants"
}
```