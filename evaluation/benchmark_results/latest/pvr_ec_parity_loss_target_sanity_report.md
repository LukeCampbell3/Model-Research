# PVR-EC Parity Loss Target Sanity Report

**Status:** PVR_EC_LOSS_SCHEDULE_BLOCKER

**Statuses:** PVR_EC_DO_NOT_PROMOTE, PVR_EC_FIXED_OWNER_PARITY_FAILED, PVR_EC_LEARNED_OWNER_PARITY_FAILED, PVR_EC_LOSS_SCHEDULE_BLOCKER, PVR_EC_NONLINEAR_OVERFIT_FAILED, PVR_EC_NONLINEAR_OVERFIT_READY, PVR_EC_PARITY_OVERFIT_FAILED, PVR_EC_ROUND_ROBIN_PARITY_FAILED

```json
{
  "metadata": {
    "timestamp": "2026-06-10T00:39:23.556648",
    "run_id": "algo_20260610_003923_pvr-overfit-sanity",
    "git_commit": "928992ecf24f649e7449de43e61a75deed225384",
    "docker_image": "N/A",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": false,
    "seed": 42,
    "benchmark_command": "/opt/conda/lib/python3.10/site-packages/pytest/__main__.py sparse_loop_moe/tests/test_pvr_ec_stage3f_descriptor_confirmation.py sparse_loop_moe/tests/test_pvr_ec_stage4_small_nlp_bridge.py sparse_loop_moe/tests/test_pvr_ec_stage5_research_nlp.py sparse_loop_moe/tests/test_pvr_ec_final_research_gate.py sparse_loop_moe/tests/test_pvr_ec_stage3e_gate.py sparse_loop_moe/tests/test_pvr_ec.py -q --tb=line",
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
        8,
        244
      ],
      "class_distribution": {
        "8": 1,
        "18": 1,
        "20": 1,
        "37": 1,
        "40": 1,
        "44": 1,
        "45": 2,
        "49": 1,
        "55": 1,
        "62": 1,
        "63": 1,
        "64": 1,
        "77": 1,
        "78": 1,
        "95": 1,
        "96": 1,
        "126": 1,
        "136": 1,
        "145": 1,
        "174": 1,
        "175": 1,
        "182": 1,
        "200": 1,
        "202": 1,
        "203": 1,
        "220": 1,
        "226": 1,
        "228": 1,
        "229": 1,
        "243": 1,
        "244": 1
      },
      "baseline_random_loss": 5.040003776550293,
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
        8,
        244
      ],
      "class_distribution": {
        "8": 1,
        "18": 1,
        "20": 1,
        "37": 1,
        "40": 1,
        "44": 1,
        "45": 2,
        "49": 1,
        "55": 1,
        "62": 1,
        "63": 1,
        "64": 1,
        "77": 1,
        "78": 1,
        "95": 1,
        "96": 1,
        "126": 1,
        "136": 1,
        "145": 1,
        "174": 1,
        "175": 1,
        "182": 1,
        "200": 1,
        "202": 1,
        "203": 1,
        "220": 1,
        "226": 1,
        "228": 1,
        "229": 1,
        "243": 1,
        "244": 1
      },
      "baseline_random_loss": 5.040339469909668,
      "expected_random_loss": 5.545177444479562,
      "accuracy_definition": "mean argmax token accuracy over all positions"
    }
  ]
}
```