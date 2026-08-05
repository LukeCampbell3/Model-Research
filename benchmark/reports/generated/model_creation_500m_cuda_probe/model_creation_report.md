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
      "active_param_ratio_actual_to_target": 0.870785328,
      "active_params_per_token_actual": 435392664,
      "active_params_per_token_target": 500000000,
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
      "model_size_label": "500m",
      "model_variant": "dense_transformer_500m",
      "notes": "Architecture materialized for parameter accounting only; this is not a trained checkpoint or capability result.",
      "owners_per_token_expected": null,
      "top1_runtime_ownership_expected": false,
      "top2_execution_count_expected": null,
      "top4_execution_count_expected": null,
      "total_param_ratio_actual_to_target": 0.870785328,
      "total_params_actual": 435392664,
      "total_params_target": 500000000
    },
    {
      "active_param_ratio_actual_to_target": 1.71002784,
      "active_params_per_token_actual": 299254872,
      "active_params_per_token_target": 175000000,
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
      "model_size_label": "500m",
      "model_variant": "vanilla_switch_top1_reference_500m",
      "notes": "Architecture materialized for parameter accounting only; this is not a trained checkpoint or capability result.",
      "owners_per_token_expected": null,
      "top1_runtime_ownership_expected": false,
      "top2_execution_count_expected": null,
      "top4_execution_count_expected": null,
      "total_param_ratio_actual_to_target": 0.917251608,
      "total_params_actual": 458625804,
      "total_params_target": 500000000
    },
    {
      "active_param_ratio_actual_to_target": 2.06579936,
      "active_params_per_token_actual": 361514888,
      "active_params_per_token_target": 175000000,
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
      "model_size_label": "500m",
      "model_variant": "pvr_ec_o_full_500m",
      "notes": "Architecture materialized for parameter accounting only; this is not a trained checkpoint or capability result.",
      "owners_per_token_expected": 1.0,
      "top1_runtime_ownership_expected": true,
      "top2_execution_count_expected": 0,
      "top4_execution_count_expected": 0,
      "total_param_ratio_actual_to_target": 1.00663472,
      "total_params_actual": 503317360,
      "total_params_target": 500000000
    },
    {
      "active_param_ratio_actual_to_target": 1.288088592,
      "active_params_per_token_actual": 322022148,
      "active_params_per_token_target": 250000000,
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
      "model_size_label": "500m",
      "model_variant": "generic_top2_moe_reference_500m",
      "notes": "Architecture materialized for parameter accounting only; this is not a trained checkpoint or capability result.",
      "owners_per_token_expected": null,
      "top1_runtime_ownership_expected": false,
      "top2_execution_count_expected": null,
      "top4_execution_count_expected": null,
      "total_param_ratio_actual_to_target": 0.917251608,
      "total_params_actual": 458625804,
      "total_params_target": 500000000
    },
    {
      "active_param_ratio_actual_to_target": 2.05924576,
      "active_params_per_token_actual": 360368008,
      "active_params_per_token_target": 175000000,
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
      "model_size_label": "500m",
      "model_variant": "pvr_ec_o_no_prototypes_500m",
      "notes": "Architecture materialized for parameter accounting only; this is not a trained checkpoint or capability result.",
      "owners_per_token_expected": 1.0,
      "top1_runtime_ownership_expected": true,
      "top2_execution_count_expected": 0,
      "top4_execution_count_expected": 0,
      "total_param_ratio_actual_to_target": 1.00434096,
      "total_params_actual": 502170480,
      "total_params_target": 500000000
    },
    {
      "active_param_ratio_actual_to_target": 2.06579936,
      "active_params_per_token_actual": 361514888,
      "active_params_per_token_target": 175000000,
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
      "model_size_label": "500m",
      "model_variant": "pvr_ec_o_no_contrastive_geometry_500m",
      "notes": "Architecture materialized for parameter accounting only; this is not a trained checkpoint or capability result.",
      "owners_per_token_expected": 1.0,
      "top1_runtime_ownership_expected": true,
      "top2_execution_count_expected": 0,
      "top4_execution_count_expected": 0,
      "total_param_ratio_actual_to_target": 1.00663472,
      "total_params_actual": 503317360,
      "total_params_target": 500000000
    },
    {
      "active_param_ratio_actual_to_target": 1.80365536,
      "active_params_per_token_actual": 315639688,
      "active_params_per_token_target": 175000000,
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
      "model_size_label": "500m",
      "model_variant": "pvr_ec_o_no_descriptor_operator_500m",
      "notes": "Architecture materialized for parameter accounting only; this is not a trained checkpoint or capability result.",
      "owners_per_token_expected": 1.0,
      "top1_runtime_ownership_expected": true,
      "top2_execution_count_expected": 0,
      "top4_execution_count_expected": 0,
      "total_param_ratio_actual_to_target": 0.91488432,
      "total_params_actual": 457442160,
      "total_params_target": 500000000
    },
    {
      "active_param_ratio_actual_to_target": 1.04017568,
      "active_params_per_token_actual": 182030744,
      "active_params_per_token_target": 175000000,
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
      "model_size_label": "500m",
      "model_variant": "pvr_ec_o_shared_only_500m",
      "notes": "Architecture materialized for parameter accounting only; this is not a trained checkpoint or capability result.",
      "owners_per_token_expected": 1.0,
      "top1_runtime_ownership_expected": true,
      "top2_execution_count_expected": 0,
      "top4_execution_count_expected": 0,
      "total_param_ratio_actual_to_target": 1.329607776,
      "total_params_actual": 664803888,
      "total_params_target": 500000000
    }
  ],
  "schema_version": "1.0",
  "status": "BENCH_INFRASTRUCTURE_READY"
}
```