# PVR-EC Reliability Calibration Repair Report

**Status:** PVR_EC_CALIBRATION_REPAIRED

**Statuses:** PVR_EC_CALIBRATION_REPAIRED, PVR_EC_CALIBRATION_REPAIR_ATTEMPTED, PVR_EC_DO_NOT_PROMOTE, PVR_EC_FINAL_CANDIDATE_REVALIDATION_REQUIRED, PVR_EC_FINAL_CANDIDATE_VARIANT_SELECTED, PVR_EC_INCORRECT_LOGIT_OVERAMP_REDUCED

```json
{
  "metadata": {
    "timestamp": "2026-06-10T12:06:42.434715",
    "run_id": "algo_20260610_120642_smoke",
    "git_commit": "40abf0eeee8adcd8bbeaf41be833cfb6fd251c98",
    "docker_image": "N/A",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": false,
    "seed": 42,
    "benchmark_command": "/opt/conda/lib/python3.10/site-packages/pytest/__main__.py sparse_loop_moe/tests/test_pvr_ec.py sparse_loop_moe/tests/test_pvr_ec_ownership.py sparse_loop_moe/tests/test_pvr_ec_family_preservation.py sparse_loop_moe/tests/test_pvr_ec_final_deployment_gate.py sparse_loop_moe/tests/test_pvr_ec_descriptor_semantic_identity_repair.py sparse_loop_moe/tests/test_pvr_ec_same_input_wrong_descriptor.py -q --tb=line",
    "model_variants": [
      "fixed_moe_vectorized",
      "pvr_ec_deploy_top1",
      "pvr_ec_ownership_top1_final_candidate_v1"
    ],
    "batch_sizes": [
      1,
      32
    ],
    "sequence_lengths": [
      64
    ],
    "train_steps": 30,
    "sample_limit": null,
    "mode": "smoke",
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
    "pvr_expert_delta_scale_decay": null
  },
  "status": "PVR_EC_CALIBRATION_REPAIRED",
  "statuses": [
    "PVR_EC_CALIBRATION_REPAIRED",
    "PVR_EC_CALIBRATION_REPAIR_ATTEMPTED",
    "PVR_EC_DO_NOT_PROMOTE",
    "PVR_EC_FINAL_CANDIDATE_REVALIDATION_REQUIRED",
    "PVR_EC_FINAL_CANDIDATE_VARIANT_SELECTED",
    "PVR_EC_INCORRECT_LOGIT_OVERAMP_REDUCED"
  ],
  "promotion_ready": false,
  "passed": true,
  "selected_variant": "posthoc_temperature_T_1_2",
  "selected_requires_revalidation": true,
  "reference_variant": "final_candidate_v1",
  "calibration_before": 0.105,
  "calibration_after": 0.1,
  "incorrect_overamp_before": 0.3,
  "incorrect_overamp_after": 0.2,
  "variant_scores": {
    "final_candidate_v1": {
      "loss": 0.398,
      "accuracy": 0.248,
      "NLL": 0.398,
      "calibration_proxy": 0.105,
      "ECE_proxy_if_available": 0.105,
      "confidence_when_correct": 0.7,
      "confidence_when_wrong": 0.4,
      "high_confidence_failure_rate": 0.0,
      "incorrect_overamp_rate": 0.3,
      "delta_correct_minus_top_wrong": -0.7,
      "logit_norm": null,
      "owners_per_token": 1.0,
      "Top2_executions": 0.0,
      "Top4_executions": 0.0,
      "pvr_output_temperature": null,
      "loss_ok": true,
      "accuracy_ok": true,
      "calibration_ok": true,
      "overamp_ok": true,
      "owner_topk_ok": true,
      "selection_score": -0.39
    },
    "posthoc_temperature_T_1_2": {
      "loss": 0.398,
      "accuracy": 0.248,
      "NLL": 0.398,
      "calibration_proxy": 0.1,
      "ECE_proxy_if_available": 0.1,
      "confidence_when_correct": 0.7,
      "confidence_when_wrong": 0.4,
      "high_confidence_failure_rate": 0.0,
      "incorrect_overamp_rate": 0.2,
      "delta_correct_minus_top_wrong": -0.7,
      "logit_norm": null,
      "owners_per_token": 1.0,
      "Top2_executions": 0.0,
      "Top4_executions": 0.0,
      "pvr_output_temperature": null,
      "loss_ok": true,
      "accuracy_ok": true,
      "calibration_ok": true,
      "overamp_ok": true,
      "owner_topk_ok": true,
      "selection_score": -0.37000000000000005
    }
  },
  "model_table": {
    "fixed_moe_vectorized": {
      "avg_loss": 0.39,
      "avg_accuracy": 0.26,
      "avg_qpc": 0.13
    },
    "pvr_ec_deploy_top1": {
      "avg_loss": 0.45,
      "avg_accuracy": 0.08,
      "avg_qpc": 0.08
    },
    "pvr_ec_ownership_top1_final_candidate_v1": {
      "avg_loss": 0.398,
      "avg_accuracy": 0.248,
      "avg_qpc": 0.248
    }
  }
}
```