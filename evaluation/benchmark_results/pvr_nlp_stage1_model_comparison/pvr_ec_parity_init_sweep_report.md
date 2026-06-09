# PVR-EC Parity Init Sweep Report

**Status:** PVR_EC_NONLINEAR_OVERFIT_READY

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
  "status": "PVR_EC_NONLINEAR_OVERFIT_READY",
  "note": "Init sweep included via delta_rank and micro_ffn variants"
}
```