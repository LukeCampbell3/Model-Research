# PVR-EC Expert Contribution Report

**Status:** PVR_EC_ROUTED_EXPERT_OUTPUT_PRESENT

**Statuses:** PVR_EC_DO_NOT_PROMOTE, PVR_EC_LOSS_TARGET_SANITY_PASSED, PVR_EC_OVERFIT_SANITY_FAILED, PVR_EC_OVERFIT_SANITY_READY, PVR_EC_ROUTED_EXPERT_GRADIENTS_PRESENT, PVR_EC_ROUTED_EXPERT_OUTPUT_PRESENT

```json
{
  "metadata": {
    "timestamp": "2026-06-10T00:39:22.742342",
    "run_id": "algo_20260610_003922_pvr-overfit-sanity",
    "git_commit": "928992ecf24f649e7449de43e61a75deed225384",
    "docker_image": "N/A",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": false,
    "seed": 42,
    "benchmark_command": "/opt/conda/lib/python3.10/site-packages/pytest/__main__.py sparse_loop_moe/tests/test_pvr_ec_stage3f_descriptor_confirmation.py sparse_loop_moe/tests/test_pvr_ec_stage4_small_nlp_bridge.py sparse_loop_moe/tests/test_pvr_ec_stage5_research_nlp.py sparse_loop_moe/tests/test_pvr_ec_final_research_gate.py sparse_loop_moe/tests/test_pvr_ec_stage3e_gate.py sparse_loop_moe/tests/test_pvr_ec.py -q --tb=line",
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
      "initial_train_loss": 5.040003776550293,
      "final_train_loss": 5.082466125488281,
      "loss_reduction_pct": -0.008425062920697309,
      "steps_to_90pct_loss_reduction": null,
      "final_train_accuracy": 0.6875,
      "overfit_success": false,
      "train_loss_curve": [
        5.082466125488281
      ],
      "train_accuracy_curve": [
        0.6875
      ],
      "expert_delta_scale_curve": [
        1.0
      ],
      "schedule_step_metrics": [
        {
          "step": 0,
          "expert_delta_scale_t": 1.0,
          "train_loss": 5.082466125488281,
          "eval_loss": 5.082466125488281,
          "accuracy": 0.6875,
          "shared_output_norm": 0.15376851707696915,
          "sparse_output_norm": 3.648312568664551,
          "expert_delta_contribution_pct": 0.9595567496827913,
          "expert_grad_norm": 0.04324075311888009,
          "shared_grad_norm": 0.04338757914956659,
          "expert_grad_to_shared_grad_ratio": 0.9966159432361885,
          "logit_norm": 2.5374233722686768,
          "prediction_entropy": 5.532535076141357,
          "confidence_when_correct": 0.006697566714137793,
          "confidence_when_wrong": 0.006169899832457304,
          "ece": 0.6848235130310059,
          "calibration_proxy": 0.6848235130310059,
          "loss_accuracy_disagreement": 1.588270664215088,
          "latency_ms": 4.969358444213867
        }
      ],
      "gradient_metrics": {
        "shared_gradient_norm": 0.04338757914956659,
        "expert_gradient_norm_mean": 0.04324075311888009,
        "expert_gradient_norm_max": 0.05824556079460308,
        "expert_gradient_norm_min": 0.031018176523502916,
        "expert_gradient_norm_by_expert": {
          "0": 0.031018176523502916,
          "1": 0.05824556079460308,
          "2": 0.04143712454242632,
          "3": 0.04226215061498806
        },
        "router_gradient_norm": 0.00303076975736379,
        "prototype_gradient_norm": 0.0,
        "ownership_bias_gradient_norm_if_trainable": 0.0,
        "expert_grad_to_shared_grad_ratio": 0.9966159432361885,
        "dead_gradient_expert_count": 0,
        "zero_gradient_expert_count": 0,
        "expert_gradient_cv": 0.22503547943333607,
        "expert_gradient_cosine_similarity": 0.07406193763017654
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
          "other": 0.09421081207692623,
          "shared": 0.10014523395026724,
          "expert": 0.10779374261619523,
          "router": 0.06294769188389182
        },
        "expert_parameter_update_norm": 0.10779374261619523,
        "shared_parameter_update_norm": 0.10014523395026724,
        "router_parameter_update_norm": 0.06294769188389182,
        "prototype_parameter_update_norm": 0.0,
        "ownership_parameter_update_norm": 0.0
      },
      "contribution_metrics": {
        "shared_output_norm": 0.15376851707696915,
        "sparse_output_norm": 3.648312568664551,
        "expert_delta_output_norm_mean": 3.648312568664551,
        "expert_delta_output_norm_by_expert": {},
        "combined_output_norm": null,
        "shared_sparse_ratio": 0.042169077321887016,
        "expert_delta_contribution_pct": 0.9595567496827913,
        "expert_delta_to_shared_ratio": 23.72600476363039,
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
      "avg_final_train_loss": 5.082466125488281,
      "avg_final_train_accuracy": 0.6875,
      "avg_loss_reduction_pct": -0.008425062920697309,
      "overfit_success_rate": 0.0
    }
  },
  "status": "PVR_EC_ROUTED_EXPERT_OUTPUT_PRESENT",
  "expert_output_norm": 3.648312568664551,
  "shared_output_norm": 0.15376851707696915
}
```