# PVR-EC Failure Case Replay Report

**Status:** PVR_EC_FAILURE_CASES_REPLAYED

```json
{
  "status": "PVR_EC_FAILURE_CASES_REPLAYED",
  "case_count": 5,
  "matched_case_count": 2,
  "repeatability_rate": 0.4,
  "same_failure_mode_rate": 0.3,
  "same_primary_mode_rate": 0.4,
  "same_secondary_mode_rate": 0.2,
  "metric_delta_vs_original": [
    {
      "case_id": "seed123_clrs_style_final_candidate_v1",
      "loss_gap_vs_fixed": 0.16,
      "accuracy_gap_vs_fixed": -0.08,
      "qpm_gap": "",
      "calibration_gap": 0.04
    },
    {
      "case_id": "shape_b16_s64_qpm",
      "loss_gap_vs_fixed": "",
      "accuracy_gap_vs_fixed": "",
      "qpm_gap": -0.04,
      "calibration_gap": ""
    }
  ],
  "repair_candidate_recommendation": {
    "PVR_EC_FAILURE_OWNER_PROTOTYPE_COLLAPSE": {
      "inspect": [
        "owner_entropy",
        "prototype_entropy",
        "dead_expert_count",
        "expert_monopoly_rate",
        "prototype_local_monopoly_rate"
      ],
      "allowed_repairs": [
        "family_balanced_sampling",
        "family_balanced_loss_light",
        "ownership_bias_clip_adjustment",
        "prototype_entropy_regularization_light",
        "owner_entropy_floor_diagnostic_only"
      ],
      "disallowed_repairs": [
        "Top2/Top4 execution",
        "new router architecture",
        "larger experts",
        "distillation"
      ]
    },
    "PVR_EC_FAILURE_QPM_SHAPE_REGRESSION": {
      "inspect": [
        "latency_p50",
        "latency_p95",
        "p95_p50_ratio",
        "memory_peak",
        "diagnostic_tensor_retention",
        "cuda_sync_count",
        "cpu_transfer_count",
        "temporary_tensor_alloc_estimate"
      ],
      "allowed_repairs": [
        "separate diagnostic and inference paths",
        "disable sparse logit decomposition in inference timing",
        "preallocate tensors",
        "cache masks and ownership bias",
        "remove Python objects from measured forward",
        "CUDA events instead of global sync",
        "warmup per shape"
      ],
      "disallowed_repairs": [
        "changing model math",
        "removing required expert execution",
        "changing output",
        "Top2/Top4"
      ]
    }
  },
  "cases": [
    {
      "case_id": "seed123_clrs_style_final_candidate_v1",
      "case": {
        "seed": 123,
        "family": "clrs_style",
        "candidate_config": "final_candidate_v1",
        "expected_primary_modes": [
          "PVR_EC_FAILURE_OWNER_PROTOTYPE_COLLAPSE",
          "PVR_EC_FAILURE_CALIBRATION_COLLAPSE",
          "PVR_EC_FAILURE_SPARSE_RESIDUAL_UNHELPFUL"
        ]
      },
      "repeatable": true,
      "matched_event_count": 1,
      "expected_failure_modes": [
        "PVR_EC_FAILURE_CALIBRATION_COLLAPSE",
        "PVR_EC_FAILURE_OWNER_PROTOTYPE_COLLAPSE",
        "PVR_EC_FAILURE_SPARSE_RESIDUAL_UNHELPFUL"
      ],
      "observed_primary_modes": [
        "PVR_EC_FAILURE_OWNER_PROTOTYPE_COLLAPSE"
      ],
      "observed_secondary_modes": [
        "PVR_EC_FAILURE_BENCHMARK_FAMILY_SPECIFIC",
        "PVR_EC_FAILURE_CALIBRATION_COLLAPSE",
        "PVR_EC_FAILURE_SPARSE_RESIDUAL_UNHELPFUL"
      ],
      "same_primary_mode": true,
      "same_secondary_mode": true
    },
    {
      "case_id": "seed123_clrs_style_final_candidate_v1_1",
      "case": {
        "seed": 123,
        "family": "clrs_style",
        "candidate_config": "final_candidate_v1_1",
        "expected_primary_modes": [
          "PVR_EC_FAILURE_OWNER_PROTOTYPE_COLLAPSE",
          "PVR_EC_FAILURE_CALIBRATION_COLLAPSE",
          "PVR_EC_FAILURE_SPARSE_RESIDUAL_UNHELPFUL"
        ]
      },
      "repeatable": false,
      "matched_event_count": 0,
      "expected_failure_modes": [
        "PVR_EC_FAILURE_CALIBRATION_COLLAPSE",
        "PVR_EC_FAILURE_OWNER_PROTOTYPE_COLLAPSE",
        "PVR_EC_FAILURE_SPARSE_RESIDUAL_UNHELPFUL"
      ],
      "observed_primary_modes": [],
      "observed_secondary_modes": [],
      "same_primary_mode": false,
      "same_secondary_mode": false
    },
    {
      "case_id": "seed777_listops_final_candidate_v1",
      "case": {
        "seed": 777,
        "family": "listops",
        "candidate_config": "final_candidate_v1",
        "expected_primary_modes": [
          "PVR_EC_FAILURE_DATA_SPLIT_DIFFICULTY",
          "PVR_EC_FAILURE_OWNER_PROTOTYPE_COLLAPSE",
          "PVR_EC_FAILURE_SPARSE_RESIDUAL_UNHELPFUL"
        ]
      },
      "repeatable": false,
      "matched_event_count": 0,
      "expected_failure_modes": [
        "PVR_EC_FAILURE_DATA_SPLIT_DIFFICULTY",
        "PVR_EC_FAILURE_OWNER_PROTOTYPE_COLLAPSE",
        "PVR_EC_FAILURE_SPARSE_RESIDUAL_UNHELPFUL"
      ],
      "observed_primary_modes": [],
      "observed_secondary_modes": [],
      "same_primary_mode": false,
      "same_secondary_mode": false
    },
    {
      "case_id": "seed777_listops_final_candidate_v1_1",
      "case": {
        "seed": 777,
        "family": "listops",
        "candidate_config": "final_candidate_v1_1",
        "expected_primary_modes": [
          "PVR_EC_FAILURE_DATA_SPLIT_DIFFICULTY",
          "PVR_EC_FAILURE_OWNER_PROTOTYPE_COLLAPSE",
          "PVR_EC_FAILURE_SPARSE_RESIDUAL_UNHELPFUL"
        ]
      },
      "repeatable": false,
      "matched_event_count": 0,
      "expected_failure_modes": [
        "PVR_EC_FAILURE_DATA_SPLIT_DIFFICULTY",
        "PVR_EC_FAILURE_OWNER_PROTOTYPE_COLLAPSE",
        "PVR_EC_FAILURE_SPARSE_RESIDUAL_UNHELPFUL"
      ],
      "observed_primary_modes": [],
      "observed_secondary_modes": [],
      "same_primary_mode": false,
      "same_secondary_mode": false
    },
    {
      "case_id": "shape_b16_s64_qpm",
      "case": {
        "shape": "b16-s64",
        "candidate_config": "final_candidate_v1",
        "expected_primary_modes": [
          "PVR_EC_FAILURE_QPM_SHAPE_REGRESSION"
        ]
      },
      "repeatable": true,
      "matched_event_count": 1,
      "expected_failure_modes": [
        "PVR_EC_FAILURE_QPM_SHAPE_REGRESSION"
      ],
      "observed_primary_modes": [
        "PVR_EC_FAILURE_QPM_SHAPE_REGRESSION"
      ],
      "observed_secondary_modes": [],
      "same_primary_mode": true,
      "same_secondary_mode": false
    }
  ]
}
```