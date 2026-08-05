# PVR-EC-O Model Creation Report

Status: `BENCH_INFRASTRUCTURE_READY`

This report distinguishes primary generalized baselines, public external positioning, and internal strong-router controls.
Do not infer an architecture win from missing checkpoints, missing data, infrastructure execution, or internal control comparisons.

Allowed comparison language:
- PVR-EC-O does not yet beat generalized baselines.
- PVR-EC-O beats generalized baselines but lags internal strong-router control.
- PVR-EC-O matches internal strong-router control.
- PVR-EC-O beats internal strong-router control.

```json
{
  "benchmark_evidence": false,
  "created_model_count": 8,
  "device": "cuda",
  "forward_check": true,
  "rows": [
    {
      "active_param_ratio_actual_to_target": 0.8278519733333334,
      "active_params_per_token_actual": 248355592,
      "active_params_per_token_target": 300000000,
      "benchmark_evidence": false,
      "comparison_group": "primary_generalized_baseline",
      "created": true,
      "device": "cuda",
      "experts_active_per_token": 0,
      "forward_probe": {
        "executed_forward": true,
        "finite_output": true,
        "input_shape": [
          1,
          8
        ],
        "output_shape": [
          1,
          8,
          50257
        ]
      },
      "model_family": "dense_transformer",
      "model_size_label": "300m",
      "model_variant": "dense_transformer_300m",
      "notes": "Architecture materialized for parameter accounting only; this is not a trained checkpoint or capability result.",
      "owners_per_token_expected": null,
      "top1_runtime_ownership_expected": false,
      "top2_execution_count_expected": null,
      "top4_execution_count_expected": null,
      "total_param_ratio_actual_to_target": 0.8278519733333334,
      "total_params_actual": 248355592,
      "total_params_target": 300000000
    },
    {
      "active_param_ratio_actual_to_target": 1.7117176380952381,
      "active_params_per_token_actual": 179730352,
      "active_params_per_token_target": 105000000,
      "benchmark_evidence": false,
      "comparison_group": "primary_generalized_reference_moe",
      "created": true,
      "device": "cuda",
      "experts_active_per_token": 1,
      "forward_probe": {
        "executed_forward": true,
        "finite_output": true,
        "input_shape": [
          1,
          8
        ],
        "output_shape": [
          1,
          8,
          50257
        ]
      },
      "model_family": "vanilla_switch_top1_reference",
      "model_size_label": "300m",
      "model_variant": "vanilla_switch_top1_reference_300m",
      "notes": "Architecture materialized for parameter accounting only; this is not a trained checkpoint or capability result.",
      "owners_per_token_expected": null,
      "top1_runtime_ownership_expected": false,
      "top2_execution_count_expected": null,
      "top4_execution_count_expected": null,
      "total_param_ratio_actual_to_target": 0.8670281333333333,
      "total_params_actual": 260108440,
      "total_params_target": 300000000
    },
    {
      "active_param_ratio_actual_to_target": 2.031709180952381,
      "active_params_per_token_actual": 213329464,
      "active_params_per_token_target": 105000000,
      "benchmark_evidence": false,
      "comparison_group": "pvr_ec_o_primary",
      "created": true,
      "device": "cuda",
      "experts_active_per_token": 1,
      "forward_probe": {
        "executed_forward": true,
        "finite_output": true,
        "input_shape": [
          1,
          8
        ],
        "output_shape": [
          1,
          8,
          50257
        ]
      },
      "model_family": "pvr_ec_o",
      "model_size_label": "300m",
      "model_variant": "pvr_ec_o_full_300m",
      "notes": "Architecture materialized for parameter accounting only; this is not a trained checkpoint or capability result.",
      "owners_per_token_expected": 1.0,
      "top1_runtime_ownership_expected": true,
      "top2_execution_count_expected": 0,
      "top4_execution_count_expected": 0,
      "total_param_ratio_actual_to_target": 0.9491917333333333,
      "total_params_actual": 284757520,
      "total_params_target": 300000000
    },
    {
      "active_param_ratio_actual_to_target": 1.2747529066666667,
      "active_params_per_token_actual": 191212936,
      "active_params_per_token_target": 150000000,
      "benchmark_evidence": false,
      "comparison_group": "primary_generalized_reference_moe",
      "created": true,
      "device": "cuda",
      "experts_active_per_token": 2,
      "forward_probe": {
        "executed_forward": true,
        "finite_output": true,
        "input_shape": [
          1,
          8
        ],
        "output_shape": [
          1,
          8,
          50257
        ]
      },
      "model_family": "generic_top2_moe_reference",
      "model_size_label": "300m",
      "model_variant": "generic_top2_moe_reference_300m",
      "notes": "Architecture materialized for parameter accounting only; this is not a trained checkpoint or capability result.",
      "owners_per_token_expected": null,
      "top1_runtime_ownership_expected": false,
      "top2_execution_count_expected": null,
      "top4_execution_count_expected": null,
      "total_param_ratio_actual_to_target": 0.8670281333333333,
      "total_params_actual": 260108440,
      "total_params_target": 300000000
    },
    {
      "active_param_ratio_actual_to_target": 2.0242193523809524,
      "active_params_per_token_actual": 212543032,
      "active_params_per_token_target": 105000000,
      "benchmark_evidence": false,
      "comparison_group": "pvr_ec_o_ablation",
      "created": true,
      "device": "cuda",
      "experts_active_per_token": 1,
      "forward_probe": {
        "executed_forward": true,
        "finite_output": true,
        "input_shape": [
          1,
          8
        ],
        "output_shape": [
          1,
          8,
          50257
        ]
      },
      "model_family": "pvr_ec_o",
      "model_size_label": "300m",
      "model_variant": "pvr_ec_o_no_prototypes_300m",
      "notes": "Architecture materialized for parameter accounting only; this is not a trained checkpoint or capability result.",
      "owners_per_token_expected": 1.0,
      "top1_runtime_ownership_expected": true,
      "top2_execution_count_expected": 0,
      "top4_execution_count_expected": 0,
      "total_param_ratio_actual_to_target": 0.9465702933333333,
      "total_params_actual": 283971088,
      "total_params_target": 300000000
    },
    {
      "active_param_ratio_actual_to_target": 2.031709180952381,
      "active_params_per_token_actual": 213329464,
      "active_params_per_token_target": 105000000,
      "benchmark_evidence": false,
      "comparison_group": "pvr_ec_o_ablation",
      "created": true,
      "device": "cuda",
      "experts_active_per_token": 1,
      "forward_probe": {
        "executed_forward": true,
        "finite_output": true,
        "input_shape": [
          1,
          8
        ],
        "output_shape": [
          1,
          8,
          50257
        ]
      },
      "model_family": "pvr_ec_o",
      "model_size_label": "300m",
      "model_variant": "pvr_ec_o_no_contrastive_geometry_300m",
      "notes": "Architecture materialized for parameter accounting only; this is not a trained checkpoint or capability result.",
      "owners_per_token_expected": 1.0,
      "top1_runtime_ownership_expected": true,
      "top2_execution_count_expected": 0,
      "top4_execution_count_expected": 0,
      "total_param_ratio_actual_to_target": 0.9491917333333333,
      "total_params_actual": 284757520,
      "total_params_target": 300000000
    },
    {
      "active_param_ratio_actual_to_target": 1.7920346666666667,
      "active_params_per_token_actual": 188163640,
      "active_params_per_token_target": 105000000,
      "benchmark_evidence": false,
      "comparison_group": "pvr_ec_o_ablation",
      "created": true,
      "device": "cuda",
      "experts_active_per_token": 1,
      "forward_probe": {
        "executed_forward": true,
        "finite_output": true,
        "input_shape": [
          1,
          8
        ],
        "output_shape": [
          1,
          8,
          50257
        ]
      },
      "model_family": "pvr_ec_o",
      "model_size_label": "300m",
      "model_variant": "pvr_ec_o_no_descriptor_operator_300m",
      "notes": "Architecture materialized for parameter accounting only; this is not a trained checkpoint or capability result.",
      "owners_per_token_expected": 1.0,
      "top1_runtime_ownership_expected": true,
      "top2_execution_count_expected": 0,
      "top4_execution_count_expected": 0,
      "total_param_ratio_actual_to_target": 0.8653056533333333,
      "total_params_actual": 259591696,
      "total_params_target": 300000000
    },
    {
      "active_param_ratio_actual_to_target": 0.8746301714285715,
      "active_params_per_token_actual": 91836168,
      "active_params_per_token_target": 105000000,
      "benchmark_evidence": false,
      "comparison_group": "pvr_ec_o_ablation",
      "created": true,
      "device": "cuda",
      "experts_active_per_token": 1,
      "forward_probe": {
        "executed_forward": true,
        "finite_output": true,
        "input_shape": [
          1,
          8
        ],
        "output_shape": [
          1,
          8,
          50257
        ]
      },
      "model_family": "pvr_ec_o",
      "model_size_label": "300m",
      "model_variant": "pvr_ec_o_shared_only_300m",
      "notes": "Architecture materialized for parameter accounting only; this is not a trained checkpoint or capability result.",
      "owners_per_token_expected": 1.0,
      "top1_runtime_ownership_expected": true,
      "top2_execution_count_expected": 0,
      "top4_execution_count_expected": 0,
      "total_param_ratio_actual_to_target": 1.2212992533333333,
      "total_params_actual": 366389776,
      "total_params_target": 300000000
    }
  ],
  "schema_version": "1.0",
  "status": "BENCH_INFRASTRUCTURE_READY"
}
```