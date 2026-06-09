# PVR-EC Nonlinear Repair Report

**Status:** PVR_EC_NONLINEAR_REPAIR_APPLIED

**Statuses:** PVR_EC_DO_NOT_PROMOTE, PVR_EC_EXPERT_SCALE_UNDERPOWERED, PVR_EC_FIXED_OWNER_PARITY_PASSED, PVR_EC_NONLINEAR_OVERFIT_PASSED, PVR_EC_NONLINEAR_OVERFIT_READY, PVR_EC_PARITY_OVERFIT_PASSED, PVR_EC_ROUND_ROBIN_PARITY_FAILED

```json
{
  "metadata": {
    "timestamp": "2026-06-09T02:36:45.904990",
    "run_id": "algo_20260609_023354_pvr-overfit-sanity",
    "git_commit": "aff470f9ed548af833e78f9fb075ed1fa78a9af1",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 42,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode pvr-overfit-sanity --scale small --device cuda --amp --seed-list 42,123,777 --pvr-overfit-tasks toy_xor_or_parity_balanced,toy_nonlinear_lookup,single_batch_memorization --pvr-overfit-steps 1000 --pvr-overfit-batch-size 32 --models dense_baseline,fixed_moe_vectorized,pvr_full,pvr_full_fixed_owner_e0,pvr_full_expert_delta_scale_4,pvr_full_micro_ffn_0_5x --run-nonlinear-overfit-diagnostic --output-dir evaluation/benchmark_results/pvr_nonlinear_overfit_1000",
    "model_variants": [
      "dense_baseline",
      "fixed_moe_vectorized",
      "pvr_full",
      "pvr_full_fixed_owner_e0",
      "pvr_full_expert_delta_scale_4",
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
      "toy_xor_or_parity_balanced",
      "toy_nonlinear_lookup",
      "single_batch_memorization"
    ],
    "pvr_overfit_steps": 1000,
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
    "micro_ffn_parity": true,
    "best_expert_delta_scale": 4.0,
    "best_expert_delta_scale_accuracy": 0.921875,
    "dominant_failure_mode": "expert_scale_underpowered",
    "recommended_repair": "expert_delta_scale_schedule_target_4.0",
    "parity_results_by_model": {
      "dense_baseline": {
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.78125,
          "loss": 0.42694929242134094,
          "passed": true
        }
      },
      "fixed_moe_vectorized": {
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.509765625,
          "loss": 0.6930435299873352,
          "passed": false
        }
      },
      "pvr_full": {
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.869140625,
          "loss": 0.3039575517177582,
          "passed": true
        }
      },
      "pvr_full_fixed_owner_e0": {
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.89453125,
          "loss": 0.27240124344825745,
          "passed": true
        }
      },
      "pvr_full_expert_delta_scale_4": {
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.921875,
          "loss": 0.2106875777244568,
          "passed": true
        }
      },
      "pvr_full_micro_ffn_0_5x": {
        "toy_xor_or_parity_balanced": {
          "accuracy": 0.775390625,
          "loss": 0.42588067054748535,
          "passed": true
        }
      }
    },
    "nonlinear_results_by_model": {
      "dense_baseline": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.00016483038780279458,
          "passed": true
        }
      },
      "fixed_moe_vectorized": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.00018473439558874816,
          "passed": true
        }
      },
      "pvr_full": {
        "toy_nonlinear_lookup": {
          "accuracy": 0.998046875,
          "loss": 0.005288973450660706,
          "passed": true
        }
      },
      "pvr_full_fixed_owner_e0": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.00048239532043226063,
          "passed": true
        }
      },
      "pvr_full_expert_delta_scale_4": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 0.002530754543840885,
          "passed": true
        }
      },
      "pvr_full_micro_ffn_0_5x": {
        "toy_nonlinear_lookup": {
          "accuracy": 1.0,
          "loss": 5.8679815992945805e-05,
          "passed": true
        }
      }
    }
  },
  "status": "PVR_EC_NONLINEAR_REPAIR_APPLIED",
  "dominant_failure_mode": "expert_scale_underpowered",
  "recommended_repair": "expert_delta_scale_schedule_target_4.0",
  "repair_applied": false,
  "note": "Repair must be applied and confirmed in a follow-up run"
}
```