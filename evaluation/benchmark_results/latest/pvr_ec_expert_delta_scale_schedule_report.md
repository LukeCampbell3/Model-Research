# PVR-EC Expert Delta Scale Schedule Report

**Status:** PVR_EC_EXPERT_DELTA_SCALE_SCHEDULE_HELPFUL

**Statuses:** PVR_EC_DO_NOT_PROMOTE, PVR_EC_EXPERT_DELTA_SCALE_SCHEDULE_HELPFUL, PVR_EC_EXPERT_DELTA_SCALE_SCHEDULE_IMPLEMENTED, PVR_EC_NONLINEAR_REPAIR_CONFIRMED

```json
{
  "metadata": {
    "timestamp": "2026-06-07T23:38:11.403645",
    "run_id": "algo_20260607_233811_pvr-overfit-sanity",
    "git_commit": "51e443da02bdc0a13c33b86368b863343ae036a2",
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
  "source": "nonlinear_overfit",
  "status": "PVR_EC_EXPERT_DELTA_SCALE_SCHEDULE_HELPFUL",
  "statuses": [
    "PVR_EC_DO_NOT_PROMOTE",
    "PVR_EC_EXPERT_DELTA_SCALE_SCHEDULE_HELPFUL",
    "PVR_EC_EXPERT_DELTA_SCALE_SCHEDULE_IMPLEMENTED",
    "PVR_EC_NONLINEAR_REPAIR_CONFIRMED"
  ],
  "promotion_ready": false,
  "schedule_name": "warmup_hold_1_to_4",
  "scale_start": 1.0,
  "scale_end": 4.0,
  "warmup_steps": null,
  "hold_steps": null,
  "decay_enabled": false,
  "best_model": "pvr_full_scale_schedule_1_to_4",
  "best_constant_model": null,
  "best_step": 1,
  "best_loss": 4.778498649597168,
  "best_accuracy": 1.0,
  "best_expert_delta_contribution_pct": 0.9885431236997967,
  "calibration_regression": false,
  "latency_regression": false,
  "benchmark_capability_improved": false,
  "recommendation": "keep warmup_hold_1_to_4 as the next single repair candidate",
  "model_summary": {
    "pvr_full": {
      "schedule_name": "constant_1",
      "scale_start": 1.0,
      "scale_end": 1.0,
      "warmup_steps": null,
      "hold_steps": null,
      "decay_enabled": false,
      "avg_loss": 4.793283462524414,
      "avg_accuracy": 1.0,
      "expert_delta_contribution_pct": 0.9558441627707778,
      "shared_sparse_ratio": 0.046223703771829605,
      "calibration_proxy": 0.8844137489795685,
      "prediction_entropy": 5.5311055183410645,
      "logit_norm": 2.648272752761841,
      "latency_ms": 1.0013580322265625,
      "final_expert_delta_scale_t": 1.0
    },
    "pvr_full_scale_schedule_1_to_4": {
      "schedule_name": "warmup_hold_1_to_4",
      "scale_start": 1.0,
      "scale_end": 4.0,
      "warmup_steps": null,
      "hold_steps": null,
      "decay_enabled": false,
      "avg_loss": 4.778498649597168,
      "avg_accuracy": 1.0,
      "expert_delta_contribution_pct": 0.9885431236997967,
      "shared_sparse_ratio": 0.011593705043196678,
      "calibration_proxy": 0.884345144033432,
      "prediction_entropy": 5.531071662902832,
      "logit_norm": 2.645519256591797,
      "latency_ms": 8.205056190490723,
      "final_expert_delta_scale_t": 2.5
    }
  },
  "source_summary": {},
  "rows": [
    {
      "model": "pvr_full_scale_schedule_1_to_4",
      "task": "toy_identity",
      "initial_train_loss": 5.00361967086792,
      "final_train_loss": 4.778498649597168,
      "loss_reduction_pct": 0.04499163327329849,
      "steps_to_90pct_loss_reduction": null,
      "final_train_accuracy": 1.0,
      "overfit_success": true,
      "train_loss_curve": [
        5.011830806732178,
        4.778498649597168
      ],
      "train_accuracy_curve": [
        0.78125,
        1.0
      ],
      "expert_delta_scale_curve": [
        4.0,
        4.0
      ],
      "schedule_step_metrics": [
        {
          "step": 0,
          "expert_delta_scale_t": 4.0,
          "train_loss": 5.011830806732178,
          "eval_loss": 5.011830806732178,
          "accuracy": 0.78125,
          "shared_output_norm": 0.16169939190149307,
          "sparse_output_norm": 15.028989315032959,
          "expert_delta_contribution_pct": 0.9893553613650394,
          "expert_grad_norm": 0.04556677773507545,
          "shared_grad_norm": 0.010979646656778641,
          "expert_grad_to_shared_grad_ratio": 4.150113310517449,
          "logit_norm": 2.600454568862915,
          "prediction_entropy": 5.531764984130859,
          "confidence_when_correct": 0.007012442220002413,
          "confidence_when_wrong": 0.00638520997017622,
          "ece": 0.777168333530426,
          "calibration_proxy": 0.777168333530426,
          "loss_accuracy_disagreement": 1.0963379889726639,
          "latency_ms": 0.0
        },
        {
          "step": 1,
          "expert_delta_scale_t": 4.0,
          "train_loss": 4.778498649597168,
          "eval_loss": 4.778498649597168,
          "accuracy": 1.0,
          "shared_output_norm": 0.16873255372047424,
          "sparse_output_norm": 14.558890342712402,
          "expert_delta_contribution_pct": 0.9885431236997967,
          "expert_grad_norm": 0.05037601638287015,
          "shared_grad_norm": 0.013602364953840151,
          "expert_grad_to_shared_grad_ratio": 3.7034748408693625,
          "logit_norm": 2.6905839443206787,
          "prediction_entropy": 5.530378341674805,
          "confidence_when_correct": 0.008478052914142609,
          "confidence_when_wrong": 0.0,
          "ece": 0.991521954536438,
          "calibration_proxy": 0.991521954536438,
          "loss_accuracy_disagreement": 0.0,
          "latency_ms": 16.410112380981445
        }
      ],
      "gradient_metrics": {
        "shared_gradient_norm": 0.013602364953840151,
        "expert_gradient_norm_mean": 0.05037601638287015,
        "expert_gradient_norm_max": 0.0687331625376828,
        "expert_gradient_norm_min": 0.017529232361994218,
        "expert_gradient_norm_by_expert": {
          "0": 0.0687331625376828,
          "1": 0.017529232361994218,
          "2": 0.06229419313604012,
          "3": 0.05294747749576345
        },
        "router_gradient_norm": 0.000523388977550591,
        "prototype_gradient_norm": 0.0,
        "ownership_bias_gradient_norm_if_trainable": 0.0,
        "expert_grad_to_shared_grad_ratio": 3.7034748408693625,
        "dead_gradient_expert_count": 0,
        "zero_gradient_expert_count": 0,
        "expert_gradient_cv": 0.3925916862311518,
        "expert_gradient_cosine_similarity": 0.11847400665283203
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
          "other": 0.0942002278752625,
          "shared": 0.10010333778336644,
          "expert": 0.10775858029955998,
          "router": 0.062270040274597704
        },
        "expert_parameter_update_norm": 0.10775858029955998,
        "shared_parameter_update_norm": 0.10010333778336644,
        "router_parameter_update_norm": 0.062270040274597704,
        "prototype_parameter_update_norm": 0.0,
        "ownership_parameter_update_norm": 0.0
      },
      "contribution_metrics": {
        "shared_output_norm": 0.16873255372047424,
        "sparse_output_norm": 14.558890342712402,
        "expert_delta_output_norm_mean": 14.558890342712402,
        "expert_delta_output_norm_by_expert": {},
        "combined_output_norm": null,
        "shared_sparse_ratio": 0.011593705043196678,
        "expert_delta_contribution_pct": 0.9885431236997967,
        "expert_delta_to_shared_ratio": 86.28382621904102,
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
          248
        ],
        "class_distribution": {
          "2": 1,
          "3": 1,
          "13": 1,
          "17": 1,
          "18": 1,
          "27": 1,
          "35": 1,
          "83": 1,
          "94": 1,
          "102": 1,
          "111": 1,
          "115": 1,
          "121": 1,
          "125": 1,
          "126": 1,
          "132": 1,
          "150": 1,
          "157": 1,
          "170": 1,
          "171": 1,
          "172": 1,
          "183": 1,
          "191": 1,
          "197": 2,
          "219": 2,
          "228": 1,
          "231": 2,
          "232": 1,
          "248": 1
        },
        "baseline_random_loss": 5.00361967086792,
        "expected_random_loss": 5.545177444479562,
        "accuracy_definition": "mean argmax token accuracy over all positions"
      },
      "debug_owner_mode": "",
      "debug_force_expert_id": null,
      "pvr_shared_scale": 1.0,
      "pvr_expert_delta_scale": 1.0,
      "pvr_expert_delta_scale_schedule": "warmup_hold",
      "pvr_expert_delta_scale_start": 1.0,
      "pvr_expert_delta_scale_end": 4.0,
      "pvr_expert_delta_scale_decay": null,
      "scale_schedule_name": "warmup_hold_1_to_4",
      "parity_class_balance": {
        "balanced": true,
        "note": "non-parity task"
      }
    }
  ]
}
```