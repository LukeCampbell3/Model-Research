# PVR-EC Parity Loss Target Sanity Report

**Status:** PVR_EC_LOSS_SCHEDULE_BLOCKER

**Statuses:** PVR_EC_DO_NOT_PROMOTE, PVR_EC_FIXED_OWNER_PARITY_FAILED, PVR_EC_LEARNED_OWNER_PARITY_FAILED, PVR_EC_LOSS_SCHEDULE_BLOCKER, PVR_EC_NONLINEAR_OVERFIT_FAILED, PVR_EC_NONLINEAR_OVERFIT_READY, PVR_EC_PARITY_OVERFIT_FAILED, PVR_EC_ROUND_ROBIN_PARITY_FAILED

```json
{
  "metadata": {
    "timestamp": "2026-06-07T20:17:42.750300",
    "run_id": "algo_20260607_201742_pvr-overfit-sanity",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "N/A",
    "cuda_available": false,
    "gpu_name": "",
    "amp_enabled": false,
    "seed": 42,
    "benchmark_command": "C:\\Users\\jcthi\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python311\\Scripts\\pytest sparse_loop_moe/tests/test_pvr_ec.py -q",
    "model_variants": [
      "pvr_full",
      "pvr_full_scale_schedule_1_to_4"
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
      "toy_identity"
    ],
    "pvr_overfit_steps": 2,
    "pvr_overfit_batch_size": 2,
    "failures": []
  },
  "statuses": [
    "PVR_EC_DO_NOT_PROMOTE",
    "PVR_EC_FIXED_OWNER_PARITY_FAILED",
    "PVR_EC_LEARNED_OWNER_PARITY_FAILED",
    "PVR_EC_LOSS_SCHEDULE_BLOCKER",
    "PVR_EC_NONLINEAR_OVERFIT_FAILED",
    "PVR_EC_NONLINEAR_OVERFIT_READY",
    "PVR_EC_PARITY_OVERFIT_FAILED",
    "PVR_EC_ROUND_ROBIN_PARITY_FAILED"
  ],
  "promotion_ready": false,
  "analysis": {
    "overall_status": "PVR_EC_NONLINEAR_OVERFIT_FAILED",
    "statuses": [
      "PVR_EC_DO_NOT_PROMOTE",
      "PVR_EC_FIXED_OWNER_PARITY_FAILED",
      "PVR_EC_LEARNED_OWNER_PARITY_FAILED",
      "PVR_EC_LOSS_SCHEDULE_BLOCKER",
      "PVR_EC_NONLINEAR_OVERFIT_FAILED",
      "PVR_EC_NONLINEAR_OVERFIT_READY",
      "PVR_EC_PARITY_OVERFIT_FAILED",
      "PVR_EC_ROUND_ROBIN_PARITY_FAILED"
    ],
    "controls_pass": true,
    "fixed_owner_parity": false,
    "round_robin_parity": false,
    "uniform_owner_parity": false,
    "learned_owner_parity": false,
    "sparse_only_parity": false,
    "shared_only_parity": false,
    "dense_parity": false,
    "fixed_moe_parity": false,
    "micro_ffn_parity": false,
    "best_expert_delta_scale": null,
    "best_expert_delta_scale_accuracy": 0.0,
    "dominant_failure_mode": "loss_schedule_or_target_blocker",
    "recommended_repair": "verify_parity_target_and_loss_construction",
    "parity_results_by_model": {
      "pvr_full": {},
      "pvr_full_scale_schedule_1_to_4": {}
    },
    "nonlinear_results_by_model": {
      "pvr_full": {},
      "pvr_full_scale_schedule_1_to_4": {}
    }
  },
  "status": "PVR_EC_LOSS_SCHEDULE_BLOCKER",
  "parity_class_balance": [],
  "loss_target_sanity": [
    {
      "target_shape": [
        2,
        16
      ],
      "logit_shape": [
        2,
        16,
        256
      ],
      "loss_function": "cross_entropy",
      "ignore_index": null,
      "num_classes": 256,
      "target_value_range": [
        19,
        255
      ],
      "class_distribution": {
        "19": 1,
        "38": 1,
        "41": 2,
        "53": 1,
        "59": 1,
        "60": 1,
        "61": 2,
        "63": 2,
        "84": 1,
        "90": 1,
        "91": 1,
        "97": 1,
        "132": 1,
        "137": 1,
        "156": 1,
        "166": 1,
        "172": 1,
        "184": 1,
        "196": 1,
        "207": 1,
        "211": 1,
        "213": 1,
        "218": 1,
        "228": 1,
        "239": 1,
        "240": 1,
        "247": 1,
        "251": 1,
        "255": 1
      },
      "baseline_random_loss": 4.999621868133545,
      "expected_random_loss": 5.545177444479562,
      "accuracy_definition": "mean argmax token accuracy over all positions"
    },
    {
      "target_shape": [
        2,
        16
      ],
      "logit_shape": [
        2,
        16,
        256
      ],
      "loss_function": "cross_entropy",
      "ignore_index": null,
      "num_classes": 256,
      "target_value_range": [
        19,
        255
      ],
      "class_distribution": {
        "19": 1,
        "38": 1,
        "41": 2,
        "53": 1,
        "59": 1,
        "60": 1,
        "61": 2,
        "63": 2,
        "84": 1,
        "90": 1,
        "91": 1,
        "97": 1,
        "132": 1,
        "137": 1,
        "156": 1,
        "166": 1,
        "172": 1,
        "184": 1,
        "196": 1,
        "207": 1,
        "211": 1,
        "213": 1,
        "218": 1,
        "228": 1,
        "239": 1,
        "240": 1,
        "247": 1,
        "251": 1,
        "255": 1
      },
      "baseline_random_loss": 4.987950325012207,
      "expected_random_loss": 5.545177444479562,
      "accuracy_definition": "mean argmax token accuracy over all positions"
    }
  ]
}
```