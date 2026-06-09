# PVR-EC Optimizer Update Report

**Status:** PVR_EC_OPTIMIZER_GROUP_REPAIRED

**Statuses:** PVR_EC_DO_NOT_PROMOTE, PVR_EC_LOSS_TARGET_SANITY_PASSED, PVR_EC_OVERFIT_SANITY_FAILED, PVR_EC_OVERFIT_SANITY_READY, PVR_EC_ROUTED_EXPERT_GRADIENTS_PRESENT, PVR_EC_ROUTED_EXPERT_OUTPUT_PRESENT

```json
{
  "metadata": {
    "timestamp": "2026-06-09T00:46:49.386540",
    "run_id": "algo_20260609_004648_pvr-overfit-sanity",
    "git_commit": "aff470f9ed548af833e78f9fb075ed1fa78a9af1",
    "docker_image": "N/A",
    "cuda_available": false,
    "gpu_name": "",
    "amp_enabled": false,
    "seed": 42,
    "benchmark_command": "C:\\Users\\jcthi\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python311\\site-packages\\pytest\\__main__.py sparse_loop_moe/tests/test_pvr_ec.py sparse_loop_moe/tests/test_pvr_ec_ownership.py sparse_loop_moe/tests/test_pvr_ec_failure_observatory.py sparse_loop_moe/tests/test_pvr_ec_family_preservation.py sparse_loop_moe/tests/test_pvr_ec_nlp_stage1.py sparse_loop_moe/tests/test_pvr_ec_family_preserving_router.py sparse_loop_moe/tests/test_pvr_ec_nonlinear_overfit.py -q",
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
      "initial_train_loss": 4.985724449157715,
      "final_train_loss": 4.9954447746276855,
      "loss_reduction_pct": -0.0019496315067337605,
      "steps_to_90pct_loss_reduction": null,
      "final_train_accuracy": 0.78125,
      "overfit_success": false,
      "train_loss_curve": [
        4.9954447746276855
      ],
      "train_accuracy_curve": [
        0.78125
      ],
      "expert_delta_scale_curve": [
        1.0
      ],
      "schedule_step_metrics": [
        {
          "step": 0,
          "expert_delta_scale_t": 1.0,
          "train_loss": 4.9954447746276855,
          "eval_loss": 4.9954447746276855,
          "accuracy": 0.78125,
          "shared_output_norm": 0.1655062735080719,
          "sparse_output_norm": 4.299094200134277,
          "expert_delta_contribution_pct": 0.9629292084509754,
          "expert_grad_norm": 0.04613378545764135,
          "shared_grad_norm": 0.04438722680788487,
          "expert_grad_to_shared_grad_ratio": 1.0393482264011642,
          "logit_norm": 2.6371123790740967,
          "prediction_entropy": 5.531332969665527,
          "confidence_when_correct": 0.007202188950031996,
          "confidence_when_wrong": 0.006241656374186277,
          "ece": 0.7769886255264282,
          "calibration_proxy": 0.7769886255264282,
          "loss_accuracy_disagreement": 1.0927535444498062,
          "latency_ms": 0.0
        }
      ],
      "gradient_metrics": {
        "shared_gradient_norm": 0.04438722680788487,
        "expert_gradient_norm_mean": 0.04613378545764135,
        "expert_gradient_norm_max": 0.06330140188219957,
        "expert_gradient_norm_min": 0.02483337582089007,
        "expert_gradient_norm_by_expert": {
          "0": 0.048486965184565634,
          "1": 0.06330140188219957,
          "2": 0.047913398942910135,
          "3": 0.02483337582089007
        },
        "router_gradient_norm": 0.003438567883373859,
        "prototype_gradient_norm": 0.0,
        "ownership_bias_gradient_norm_if_trainable": 0.0,
        "expert_grad_to_shared_grad_ratio": 1.0393482264011642,
        "dead_gradient_expert_count": 0,
        "zero_gradient_expert_count": 0,
        "expert_gradient_cv": 0.2982213394578734,
        "expert_gradient_cosine_similarity": -0.13027441501617432
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
          "other": 0.0942157014273107,
          "shared": 0.10014779912307858,
          "expert": 0.10784096730640158,
          "router": 0.0629480762872845
        },
        "expert_parameter_update_norm": 0.10784096730640158,
        "shared_parameter_update_norm": 0.10014779912307858,
        "router_parameter_update_norm": 0.0629480762872845,
        "prototype_parameter_update_norm": 0.0,
        "ownership_parameter_update_norm": 0.0
      },
      "contribution_metrics": {
        "shared_output_norm": 0.1655062735080719,
        "sparse_output_norm": 4.299094200134277,
        "expert_delta_output_norm_mean": 4.299094200134277,
        "expert_delta_output_norm_by_expert": {},
        "combined_output_norm": null,
        "shared_sparse_ratio": 0.03856103494763374,
        "expert_delta_contribution_pct": 0.9629292084509754,
        "expert_delta_to_shared_ratio": 25.975415366503352,
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
          21,
          242
        ],
        "class_distribution": {
          "21": 1,
          "42": 1,
          "48": 1,
          "69": 1,
          "85": 1,
          "93": 1,
          "97": 1,
          "99": 1,
          "105": 1,
          "106": 1,
          "108": 1,
          "110": 1,
          "115": 1,
          "121": 1,
          "128": 1,
          "137": 1,
          "143": 1,
          "152": 1,
          "153": 1,
          "177": 1,
          "179": 1,
          "192": 1,
          "197": 1,
          "198": 1,
          "200": 1,
          "202": 1,
          "208": 1,
          "213": 1,
          "234": 1,
          "236": 1,
          "241": 1,
          "242": 1
        },
        "baseline_random_loss": 4.985724449157715,
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
      "avg_final_train_loss": 4.9954447746276855,
      "avg_final_train_accuracy": 0.78125,
      "avg_loss_reduction_pct": -0.0019496315067337605,
      "overfit_success_rate": 0.0
    }
  },
  "status": "PVR_EC_OPTIMIZER_GROUP_REPAIRED",
  "optimizer_update_rows": [
    {
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
        "other": 0.0942157014273107,
        "shared": 0.10014779912307858,
        "expert": 0.10784096730640158,
        "router": 0.0629480762872845
      },
      "expert_parameter_update_norm": 0.10784096730640158,
      "shared_parameter_update_norm": 0.10014779912307858,
      "router_parameter_update_norm": 0.0629480762872845,
      "prototype_parameter_update_norm": 0.0,
      "ownership_parameter_update_norm": 0.0
    }
  ]
}
```