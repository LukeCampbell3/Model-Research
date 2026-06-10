# PVR-EC Parity Loss Target Sanity Report

**Status:** PVR_EC_LOSS_SCHEDULE_BLOCKER

**Statuses:** PVR_EC_DO_NOT_PROMOTE, PVR_EC_FIXED_OWNER_PARITY_FAILED, PVR_EC_LEARNED_OWNER_PARITY_FAILED, PVR_EC_LOSS_SCHEDULE_BLOCKER, PVR_EC_NONLINEAR_OVERFIT_FAILED, PVR_EC_NONLINEAR_OVERFIT_READY, PVR_EC_PARITY_OVERFIT_FAILED, PVR_EC_ROUND_ROBIN_PARITY_FAILED

```json
{
  "metadata": {
    "timestamp": "2026-06-10T20:14:14.023035",
    "run_id": "algo_20260610_201413_pvr-overfit-sanity",
    "git_commit": "48f9fbfd8e16a3775c479d71d0994955f572a033",
    "docker_image": "N/A",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": false,
    "seed": 42,
    "benchmark_command": "/opt/conda/lib/python3.10/site-packages/pytest/__main__.py sparse_loop_moe/tests/test_pvr_ec_release_freeze.py sparse_loop_moe/tests/test_pvr_ec_release_package.py sparse_loop_moe/tests/test_pvr_ec_manifest_lock.py sparse_loop_moe/tests/test_pvr_ec_production_shape_profile.py sparse_loop_moe/tests/test_pvr_ec_canary_rollout.py sparse_loop_moe/tests/test_pvr_ec_drift_monitoring.py sparse_loop_moe/tests/test_pvr_ec_release_readiness.py sparse_loop_moe/tests/test_pvr_ec.py -q --tb=line",
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
    "controls_pass": false,
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
        11,
        237
      ],
      "class_distribution": {
        "11": 1,
        "46": 1,
        "47": 1,
        "53": 1,
        "62": 1,
        "63": 1,
        "69": 1,
        "80": 1,
        "88": 1,
        "89": 1,
        "96": 1,
        "108": 1,
        "114": 1,
        "115": 1,
        "119": 2,
        "136": 1,
        "142": 1,
        "143": 1,
        "145": 1,
        "151": 1,
        "152": 2,
        "154": 1,
        "163": 1,
        "170": 1,
        "195": 1,
        "214": 1,
        "219": 1,
        "220": 1,
        "221": 1,
        "237": 1
      },
      "baseline_random_loss": 4.972649574279785,
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
        11,
        237
      ],
      "class_distribution": {
        "11": 1,
        "46": 1,
        "47": 1,
        "53": 1,
        "62": 1,
        "63": 1,
        "69": 1,
        "80": 1,
        "88": 1,
        "89": 1,
        "96": 1,
        "108": 1,
        "114": 1,
        "115": 1,
        "119": 2,
        "136": 1,
        "142": 1,
        "143": 1,
        "145": 1,
        "151": 1,
        "152": 2,
        "154": 1,
        "163": 1,
        "170": 1,
        "195": 1,
        "214": 1,
        "219": 1,
        "220": 1,
        "221": 1,
        "237": 1
      },
      "baseline_random_loss": 4.971438884735107,
      "expected_random_loss": 5.545177444479562,
      "accuracy_definition": "mean argmax token accuracy over all positions"
    }
  ]
}
```