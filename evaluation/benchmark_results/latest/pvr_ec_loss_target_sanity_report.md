# PVR-EC Loss Target Sanity Report

**Status:** PVR_EC_LOSS_TARGET_SANITY_PASSED

**Statuses:** PVR_EC_DO_NOT_PROMOTE, PVR_EC_LOSS_TARGET_SANITY_PASSED, PVR_EC_OVERFIT_SANITY_FAILED, PVR_EC_OVERFIT_SANITY_READY, PVR_EC_ROUTED_EXPERT_GRADIENTS_PRESENT, PVR_EC_ROUTED_EXPERT_OUTPUT_PRESENT

```json
{
  "metadata": {
    "timestamp": "2026-06-10T12:06:15.343576",
    "run_id": "algo_20260610_120614_pvr-overfit-sanity",
    "git_commit": "40abf0eeee8adcd8bbeaf41be833cfb6fd251c98",
    "docker_image": "N/A",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": false,
    "seed": 42,
    "benchmark_command": "/opt/conda/lib/python3.10/site-packages/pytest/__main__.py sparse_loop_moe/tests/test_pvr_ec.py sparse_loop_moe/tests/test_pvr_ec_ownership.py sparse_loop_moe/tests/test_pvr_ec_family_preservation.py sparse_loop_moe/tests/test_pvr_ec_final_deployment_gate.py sparse_loop_moe/tests/test_pvr_ec_descriptor_semantic_identity_repair.py sparse_loop_moe/tests/test_pvr_ec_same_input_wrong_descriptor.py -q --tb=line",
    "model_variants": [
      "pvr_full"
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
    "mode": "pvr-overfit-sanity",
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
    "pvr_overfit_steps": 1,
    "pvr_overfit_batch_size": 2,
    "pvr_overfit_single_batch": true,
    "failures": []
  },
  "statuses": [
    "PVR_EC_DO_NOT_PROMOTE",
    "PVR_EC_LOSS_TARGET_SANITY_PASSED",
    "PVR_EC_OVERFIT_SANITY_FAILED",
    "PVR_EC_OVERFIT_SANITY_READY",
    "PVR_EC_ROUTED_EXPERT_GRADIENTS_PRESENT",
    "PVR_EC_ROUTED_EXPERT_OUTPUT_PRESENT"
  ],
  "promotion_ready": false,
  "rows": [
    {
      "model": "pvr_full",
      "task": "toy_identity",
      "initial_train_loss": 5.014286041259766,
      "final_train_loss": 5.071128845214844,
      "loss_reduction_pct": -0.01133617098971825,
      "steps_to_90pct_loss_reduction": null,
      "final_train_accuracy": 0.5,
      "overfit_success": false,
      "train_loss_curve": [
        5.071128845214844
      ],
      "train_accuracy_curve": [
        0.5
      ],
      "expert_delta_scale_curve": [
        1.0
      ],
      "schedule_step_metrics": [
        {
          "step": 0,
          "expert_delta_scale_t": 1.0,
          "train_loss": 5.071128845214844,
          "eval_loss": 5.071128845214844,
          "accuracy": 0.5,
          "shared_output_norm": 0.15537328273057938,
          "sparse_output_norm": 3.867004871368408,
          "expert_delta_contribution_pct": 0.9613727807833664,
          "expert_grad_norm": 0.04300216730189277,
          "shared_grad_norm": 0.04241122439270839,
          "expert_grad_to_shared_grad_ratio": 1.0139336441625104,
          "logit_norm": 2.5639214515686035,
          "prediction_entropy": 5.532199859619141,
          "confidence_when_correct": 0.007168280892074108,
          "confidence_when_wrong": 0.006065475754439831,
          "ece": 0.49944859743118286,
          "calibration_proxy": 0.49944859743118286,
          "loss_accuracy_disagreement": 2.535564422607422,
          "latency_ms": 4.1904449462890625
        }
      ],
      "gradient_metrics": {
        "shared_gradient_norm": 0.04241122439270839,
        "expert_gradient_norm_mean": 0.04300216730189277,
        "expert_gradient_norm_max": 0.07200656994245946,
        "expert_gradient_norm_min": 0.023816932400222868,
        "expert_gradient_norm_by_expert": {
          "0": 0.0417815365944989,
          "1": 0.07200656994245946,
          "2": 0.03440363027038984,
          "3": 0.023816932400222868
        },
        "router_gradient_norm": 0.0025225801412792257,
        "prototype_gradient_norm": 0.0,
        "ownership_bias_gradient_norm_if_trainable": 0.0,
        "expert_grad_to_shared_grad_ratio": 1.0139336441625104,
        "dead_gradient_expert_count": 0,
        "zero_gradient_expert_count": 0,
        "expert_gradient_cv": 0.41676337452818474,
        "expert_gradient_cosine_similarity": 0.10166250169277191
      },
      "optimizer_metrics": {
        "parameter_requires_grad_by_group": {
          "other": 20,
          "shared": 12,
          "expert": 32,
          "router": 8
        },
        "parameter_in_optimizer_group": {
          "other": 20,
          "shared": 12,
          "expert": 32,
          "router": 8
        },
        "parameter_update_norm_by_group": {
          "other": 0.09421256855130196,
          "shared": 0.10014940906936924,
          "expert": 0.10780884564155713,
          "router": 0.06333986215759069
        },
        "expert_parameter_update_norm": 0.10780884564155713,
        "shared_parameter_update_norm": 0.10014940906936924,
        "router_parameter_update_norm": 0.06333986215759069,
        "prototype_parameter_update_norm": 0.0,
        "ownership_parameter_update_norm": 0.0
      },
      "contribution_metrics": {
        "shared_output_norm": 0.15537328273057938,
        "sparse_output_norm": 3.867004871368408,
        "expert_delta_output_norm_mean": 3.867004871368408,
        "expert_delta_output_norm_by_expert": {},
        "combined_output_norm": null,
        "shared_sparse_ratio": 0.040275173261761665,
        "expert_delta_contribution_pct": 0.9613727807833664,
        "expert_delta_to_shared_ratio": 24.888480203342798,
        "expert_output_diversity": null,
        "expert_output_correlation": null
      },
      "loss_target_sanity": {
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
          2,
          241
        ],
        "class_distribution": {
          "2": 2,
          "26": 1,
          "32": 1,
          "34": 1,
          "45": 1,
          "47": 1,
          "50": 1,
          "56": 1,
          "77": 1,
          "81": 1,
          "90": 1,
          "104": 1,
          "112": 1,
          "114": 1,
          "130": 2,
          "134": 1,
          "135": 1,
          "146": 1,
          "154": 1,
          "157": 1,
          "158": 1,
          "165": 1,
          "169": 1,
          "183": 1,
          "186": 1,
          "189": 1,
          "203": 1,
          "236": 1,
          "239": 1,
          "241": 1
        },
        "baseline_random_loss": 5.014286041259766,
        "expected_random_loss": 5.545177444479562,
        "accuracy_definition": "mean argmax token accuracy over all positions"
      },
      "debug_owner_mode": "",
      "debug_force_expert_id": null,
      "pvr_shared_scale": 1.0,
      "pvr_expert_delta_scale": 1.0,
      "pvr_expert_delta_scale_schedule": "constant",
      "pvr_expert_delta_scale_start": 1.0,
      "pvr_expert_delta_scale_end": 1.0,
      "pvr_expert_delta_scale_decay": null,
      "scale_schedule_name": "constant"
    }
  ],
  "model_summary": {
    "pvr_full": {
      "avg_final_train_loss": 5.071128845214844,
      "avg_final_train_accuracy": 0.5,
      "avg_loss_reduction_pct": -0.01133617098971825,
      "overfit_success_rate": 0.0
    }
  },
  "status": "PVR_EC_LOSS_TARGET_SANITY_PASSED",
  "loss_target_rows": [
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
        2,
        241
      ],
      "class_distribution": {
        "2": 2,
        "26": 1,
        "32": 1,
        "34": 1,
        "45": 1,
        "47": 1,
        "50": 1,
        "56": 1,
        "77": 1,
        "81": 1,
        "90": 1,
        "104": 1,
        "112": 1,
        "114": 1,
        "130": 2,
        "134": 1,
        "135": 1,
        "146": 1,
        "154": 1,
        "157": 1,
        "158": 1,
        "165": 1,
        "169": 1,
        "183": 1,
        "186": 1,
        "189": 1,
        "203": 1,
        "236": 1,
        "239": 1,
        "241": 1
      },
      "baseline_random_loss": 5.014286041259766,
      "expected_random_loss": 5.545177444479562,
      "accuracy_definition": "mean argmax token accuracy over all positions"
    }
  ]
}
```