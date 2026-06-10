# PVR-EC Nonlinear Overfit Report

**Status:** PVR_EC_NONLINEAR_OVERFIT_FAILED

**Statuses:** PVR_EC_DO_NOT_PROMOTE, PVR_EC_FIXED_OWNER_PARITY_FAILED, PVR_EC_LEARNED_OWNER_PARITY_FAILED, PVR_EC_LOSS_SCHEDULE_BLOCKER, PVR_EC_NONLINEAR_OVERFIT_FAILED, PVR_EC_NONLINEAR_OVERFIT_READY, PVR_EC_PARITY_OVERFIT_FAILED, PVR_EC_ROUND_ROBIN_PARITY_FAILED

```json
{
  "metadata": {
    "timestamp": "2026-06-10T12:06:16.155070",
    "run_id": "algo_20260610_120616_pvr-overfit-sanity",
    "git_commit": "40abf0eeee8adcd8bbeaf41be833cfb6fd251c98",
    "docker_image": "N/A",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": false,
    "seed": 42,
    "benchmark_command": "/opt/conda/lib/python3.10/site-packages/pytest/__main__.py sparse_loop_moe/tests/test_pvr_ec.py sparse_loop_moe/tests/test_pvr_ec_ownership.py sparse_loop_moe/tests/test_pvr_ec_family_preservation.py sparse_loop_moe/tests/test_pvr_ec_final_deployment_gate.py sparse_loop_moe/tests/test_pvr_ec_descriptor_semantic_identity_repair.py sparse_loop_moe/tests/test_pvr_ec_same_input_wrong_descriptor.py -q --tb=line",
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
  "status": "PVR_EC_NONLINEAR_OVERFIT_FAILED",
  "best_model_by_parity_loss": "none",
  "best_model_by_parity_accuracy": "none",
  "whether_fixed_owner_passed": false,
  "whether_round_robin_passed": false,
  "whether_learned_owner_passed": false,
  "whether_sparse_only_passed": false,
  "whether_shared_only_passed": false,
  "dominant_failure_mode": "loss_schedule_or_target_blocker",
  "recommended_repair": "verify_parity_target_and_loss_construction",
  "rows": [
    {
      "model": "pvr_full",
      "task": "toy_identity",
      "initial_train_loss": 5.014286041259766,
      "final_train_loss": 4.848557949066162,
      "loss_reduction_pct": 0.03305118432213867,
      "steps_to_90pct_loss_reduction": null,
      "final_train_accuracy": 0.9375,
      "overfit_success": false,
      "train_loss_curve": [
        5.071128845214844,
        4.848557949066162
      ],
      "train_accuracy_curve": [
        0.5,
        0.9375
      ],
      "expert_delta_scale_curve": [
        1.0,
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
          "expert_grad_norm": 0.04300216683623148,
          "shared_grad_norm": 0.04241122439270839,
          "expert_grad_to_shared_grad_ratio": 1.0139336331828395,
          "logit_norm": 2.5639214515686035,
          "prediction_entropy": 5.532199859619141,
          "confidence_when_correct": 0.007168280892074108,
          "confidence_when_wrong": 0.006065475754439831,
          "ece": 0.49944859743118286,
          "calibration_proxy": 0.49944859743118286,
          "loss_accuracy_disagreement": 2.535564422607422,
          "latency_ms": 2.6993751525878906
        },
        {
          "step": 1,
          "expert_delta_scale_t": 1.0,
          "train_loss": 4.848557949066162,
          "eval_loss": 4.848557949066162,
          "accuracy": 0.9375,
          "shared_output_norm": 0.17419583350419998,
          "sparse_output_norm": 3.3223572969436646,
          "expert_delta_contribution_pct": 0.9501806988181278,
          "expert_grad_norm": 0.047991201892727986,
          "shared_grad_norm": 0.05453693092567846,
          "expert_grad_to_shared_grad_ratio": 0.8799762120484772,
          "logit_norm": 2.677553653717041,
          "prediction_entropy": 5.530823707580566,
          "confidence_when_correct": 0.00814538449048996,
          "confidence_when_wrong": 0.006158899981528521,
          "ece": 0.9302487373352051,
          "calibration_proxy": 0.9302487373352051,
          "loss_accuracy_disagreement": 0.30303487181663513,
          "latency_ms": 2.299785614013672
        }
      ],
      "gradient_metrics": {
        "shared_gradient_norm": 0.05453693092567846,
        "expert_gradient_norm_mean": 0.047991201892727986,
        "expert_gradient_norm_max": 0.06640843395143747,
        "expert_gradient_norm_min": 0.04037152271484956,
        "expert_gradient_norm_by_expert": {
          "0": 0.04176711433683522,
          "1": 0.04037152271484956,
          "2": 0.04341773656778969,
          "3": 0.06640843395143747
        },
        "router_gradient_norm": 0.002210024462935204,
        "prototype_gradient_norm": 0.0,
        "ownership_bias_gradient_norm_if_trainable": 0.0,
        "expert_grad_to_shared_grad_ratio": 0.8799762120484772,
        "dead_gradient_expert_count": 0,
        "zero_gradient_expert_count": 0,
        "expert_gradient_cv": 0.22270174171780455,
        "expert_gradient_cosine_similarity": -0.03699968755245209
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
          "expert": 0.10780884517589584,
          "router": 0.06333986215759069
        },
        "expert_parameter_update_norm": 0.10780884517589584,
        "shared_parameter_update_norm": 0.10014940906936924,
        "router_parameter_update_norm": 0.06333986215759069,
        "prototype_parameter_update_norm": 0.0,
        "ownership_parameter_update_norm": 0.0
      },
      "contribution_metrics": {
        "shared_output_norm": 0.17419583350419998,
        "sparse_output_norm": 3.3223572969436646,
        "expert_delta_output_norm_mean": 3.3223572969436646,
        "expert_delta_output_norm_by_expert": {},
        "combined_output_norm": null,
        "shared_sparse_ratio": 0.052436480298638344,
        "expert_delta_contribution_pct": 0.9501806988181278,
        "expert_delta_to_shared_ratio": 19.072541691208478,
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
      "scale_schedule_name": "constant",
      "parity_class_balance": {
        "balanced": true,
        "note": "non-parity task"
      }
    },
    {
      "model": "pvr_full_scale_schedule_1_to_4",
      "task": "toy_identity",
      "initial_train_loss": 5.005834579467773,
      "final_train_loss": 4.8420867919921875,
      "loss_reduction_pct": 0.03271138605882494,
      "steps_to_90pct_loss_reduction": null,
      "final_train_accuracy": 0.9375,
      "overfit_success": false,
      "train_loss_curve": [
        5.064294815063477,
        4.8420867919921875
      ],
      "train_accuracy_curve": [
        0.5625,
        0.9375
      ],
      "expert_delta_scale_curve": [
        4.0,
        4.0
      ],
      "schedule_step_metrics": [
        {
          "step": 0,
          "expert_delta_scale_t": 4.0,
          "train_loss": 5.064294815063477,
          "eval_loss": 5.064294815063477,
          "accuracy": 0.5625,
          "shared_output_norm": 0.15522047132253647,
          "sparse_output_norm": 15.4665846824646,
          "expert_delta_contribution_pct": 0.9900638581908758,
          "expert_grad_norm": 0.045589837223815266,
          "shared_grad_norm": 0.011276538440142758,
          "expert_grad_to_shared_grad_ratio": 4.042892902446233,
          "logit_norm": 2.5725598335266113,
          "prediction_entropy": 5.532104969024658,
          "confidence_when_correct": 0.007076374255120754,
          "confidence_when_wrong": 0.006086212582886219,
          "ece": 0.5611822605133057,
          "calibration_proxy": 0.5611822605133057,
          "loss_accuracy_disagreement": 2.215628981590271,
          "latency_ms": 2.554655075073242
        },
        {
          "step": 1,
          "expert_delta_scale_t": 4.0,
          "train_loss": 4.8420867919921875,
          "eval_loss": 4.8420867919921875,
          "accuracy": 0.9375,
          "shared_output_norm": 0.17503218352794647,
          "sparse_output_norm": 13.568902969360352,
          "expert_delta_contribution_pct": 0.9872647693996749,
          "expert_grad_norm": 0.05148250803904375,
          "shared_grad_norm": 0.014279137511039153,
          "expert_grad_to_shared_grad_ratio": 3.605435412274922,
          "logit_norm": 2.6699137687683105,
          "prediction_entropy": 5.530808448791504,
          "confidence_when_correct": 0.008166192099452019,
          "confidence_when_wrong": 0.00637679360806942,
          "ece": 0.9302427768707275,
          "calibration_proxy": 0.9302427768707275,
          "loss_accuracy_disagreement": 0.3026304244995117,
          "latency_ms": 3.593921661376953
        }
      ],
      "gradient_metrics": {
        "shared_gradient_norm": 0.014279137511039153,
        "expert_gradient_norm_mean": 0.05148250803904375,
        "expert_gradient_norm_max": 0.06146860879380256,
        "expert_gradient_norm_min": 0.04393825103761628,
        "expert_gradient_norm_by_expert": {
          "0": 0.04576146538602188,
          "1": 0.04393825103761628,
          "2": 0.05476170693873428,
          "3": 0.06146860879380256
        },
        "router_gradient_norm": 0.0005849653049760187,
        "prototype_gradient_norm": 0.0,
        "ownership_bias_gradient_norm_if_trainable": 0.0,
        "expert_grad_to_shared_grad_ratio": 3.605435412274922,
        "dead_gradient_expert_count": 0,
        "zero_gradient_expert_count": 0,
        "expert_gradient_cv": 0.13739065032524742,
        "expert_gradient_cosine_similarity": -0.12906047701835632
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
          "other": 0.0941965258680284,
          "shared": 0.10010205504174034,
          "expert": 0.10782985732657835,
          "router": 0.06287171470467001
        },
        "expert_parameter_update_norm": 0.10782985732657835,
        "shared_parameter_update_norm": 0.10010205504174034,
        "router_parameter_update_norm": 0.06287171470467001,
        "prototype_parameter_update_norm": 0.0,
        "ownership_parameter_update_norm": 0.0
      },
      "contribution_metrics": {
        "shared_output_norm": 0.17503218352794647,
        "sparse_output_norm": 13.568902969360352,
        "expert_delta_output_norm_mean": 13.568902969360352,
        "expert_delta_output_norm_by_expert": {},
        "combined_output_norm": null,
        "shared_sparse_ratio": 0.012918607331812382,
        "expert_delta_contribution_pct": 0.9872647693996749,
        "expert_delta_to_shared_ratio": 77.52233158420192,
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
        "baseline_random_loss": 5.005834579467773,
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
  ],
  "failures": []
}
```