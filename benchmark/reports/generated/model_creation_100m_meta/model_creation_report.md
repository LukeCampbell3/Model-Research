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
  "device": "meta",
  "forward_check": false,
  "rows": [
    {
      "active_param_ratio_actual_to_target": 0.77203188,
      "active_params_per_token_actual": 77203188,
      "active_params_per_token_target": 100000000,
      "benchmark_evidence": false,
      "comparison_group": "primary_generalized_baseline",
      "created": true,
      "device": "meta",
      "experts_active_per_token": 0,
      "forward_probe": {
        "executed_forward": false,
        "reason": "forward_check_not_requested"
      },
      "model_family": "dense_transformer",
      "model_size_label": "100m",
      "model_variant": "dense_transformer_100m",
      "notes": "Architecture materialized for parameter accounting only; this is not a trained checkpoint or capability result.",
      "owners_per_token_expected": null,
      "top1_runtime_ownership_expected": false,
      "top2_execution_count_expected": null,
      "top4_execution_count_expected": null,
      "total_param_ratio_actual_to_target": 0.77203188,
      "total_params_actual": 77203188,
      "total_params_target": 100000000
    },
    {
      "active_param_ratio_actual_to_target": 2.0564070857142855,
      "active_params_per_token_actual": 71974248,
      "active_params_per_token_target": 35000000,
      "benchmark_evidence": false,
      "comparison_group": "primary_generalized_reference_moe",
      "created": true,
      "device": "meta",
      "experts_active_per_token": 1,
      "forward_probe": {
        "executed_forward": false,
        "reason": "forward_check_not_requested"
      },
      "model_family": "vanilla_switch_top1_reference",
      "model_size_label": "100m",
      "model_variant": "vanilla_switch_top1_reference_100m",
      "notes": "Architecture materialized for parameter accounting only; this is not a trained checkpoint or capability result.",
      "owners_per_token_expected": null,
      "top1_runtime_ownership_expected": false,
      "top2_execution_count_expected": null,
      "top4_execution_count_expected": null,
      "total_param_ratio_actual_to_target": 0.78106836,
      "total_params_actual": 78106836,
      "total_params_target": 100000000
    },
    {
      "active_param_ratio_actual_to_target": 2.2841849142857145,
      "active_params_per_token_actual": 79946472,
      "active_params_per_token_target": 35000000,
      "benchmark_evidence": false,
      "comparison_group": "pvr_ec_o_primary",
      "created": true,
      "device": "meta",
      "experts_active_per_token": 1,
      "forward_probe": {
        "executed_forward": false,
        "reason": "forward_check_not_requested"
      },
      "model_family": "pvr_ec_o",
      "model_size_label": "100m",
      "model_variant": "pvr_ec_o_full_100m",
      "notes": "Architecture materialized for parameter accounting only; this is not a trained checkpoint or capability result.",
      "owners_per_token_expected": 1.0,
      "top1_runtime_ownership_expected": true,
      "top2_execution_count_expected": 0,
      "top4_execution_count_expected": 0,
      "total_param_ratio_actual_to_target": 0.8543352,
      "total_params_actual": 85433520,
      "total_params_target": 100000000
    },
    {
      "active_param_ratio_actual_to_target": 1.45700664,
      "active_params_per_token_actual": 72850332,
      "active_params_per_token_target": 50000000,
      "benchmark_evidence": false,
      "comparison_group": "primary_generalized_reference_moe",
      "created": true,
      "device": "meta",
      "experts_active_per_token": 2,
      "forward_probe": {
        "executed_forward": false,
        "reason": "forward_check_not_requested"
      },
      "model_family": "generic_top2_moe_reference",
      "model_size_label": "100m",
      "model_variant": "generic_top2_moe_reference_100m",
      "notes": "Architecture materialized for parameter accounting only; this is not a trained checkpoint or capability result.",
      "owners_per_token_expected": null,
      "top1_runtime_ownership_expected": false,
      "top2_execution_count_expected": null,
      "top4_execution_count_expected": null,
      "total_param_ratio_actual_to_target": 0.78106836,
      "total_params_actual": 78106836,
      "total_params_target": 100000000
    },
    {
      "active_param_ratio_actual_to_target": 2.2757588571428573,
      "active_params_per_token_actual": 79651560,
      "active_params_per_token_target": 35000000,
      "benchmark_evidence": false,
      "comparison_group": "pvr_ec_o_ablation",
      "created": true,
      "device": "meta",
      "experts_active_per_token": 1,
      "forward_probe": {
        "executed_forward": false,
        "reason": "forward_check_not_requested"
      },
      "model_family": "pvr_ec_o",
      "model_size_label": "100m",
      "model_variant": "pvr_ec_o_no_prototypes_100m",
      "notes": "Architecture materialized for parameter accounting only; this is not a trained checkpoint or capability result.",
      "owners_per_token_expected": 1.0,
      "top1_runtime_ownership_expected": true,
      "top2_execution_count_expected": 0,
      "top4_execution_count_expected": 0,
      "total_param_ratio_actual_to_target": 0.85138608,
      "total_params_actual": 85138608,
      "total_params_target": 100000000
    },
    {
      "active_param_ratio_actual_to_target": 2.2841849142857145,
      "active_params_per_token_actual": 79946472,
      "active_params_per_token_target": 35000000,
      "benchmark_evidence": false,
      "comparison_group": "pvr_ec_o_ablation",
      "created": true,
      "device": "meta",
      "experts_active_per_token": 1,
      "forward_probe": {
        "executed_forward": false,
        "reason": "forward_check_not_requested"
      },
      "model_family": "pvr_ec_o",
      "model_size_label": "100m",
      "model_variant": "pvr_ec_o_no_contrastive_geometry_100m",
      "notes": "Architecture materialized for parameter accounting only; this is not a trained checkpoint or capability result.",
      "owners_per_token_expected": 1.0,
      "top1_runtime_ownership_expected": true,
      "top2_execution_count_expected": 0,
      "top4_execution_count_expected": 0,
      "total_param_ratio_actual_to_target": 0.8543352,
      "total_params_actual": 85433520,
      "total_params_target": 100000000
    },
    {
      "active_param_ratio_actual_to_target": 2.0819595428571427,
      "active_params_per_token_actual": 72868584,
      "active_params_per_token_target": 35000000,
      "benchmark_evidence": false,
      "comparison_group": "pvr_ec_o_ablation",
      "created": true,
      "device": "meta",
      "experts_active_per_token": 1,
      "forward_probe": {
        "executed_forward": false,
        "reason": "forward_check_not_requested"
      },
      "model_family": "pvr_ec_o",
      "model_size_label": "100m",
      "model_variant": "pvr_ec_o_no_descriptor_operator_100m",
      "notes": "Architecture materialized for parameter accounting only; this is not a trained checkpoint or capability result.",
      "owners_per_token_expected": 1.0,
      "top1_runtime_ownership_expected": true,
      "top2_execution_count_expected": 0,
      "top4_execution_count_expected": 0,
      "total_param_ratio_actual_to_target": 0.78355632,
      "total_params_actual": 78355632,
      "total_params_target": 100000000
    },
    {
      "active_param_ratio_actual_to_target": 1.2065297142857143,
      "active_params_per_token_actual": 42228540,
      "active_params_per_token_target": 35000000,
      "benchmark_evidence": false,
      "comparison_group": "pvr_ec_o_ablation",
      "created": true,
      "device": "meta",
      "experts_active_per_token": 1,
      "forward_probe": {
        "executed_forward": false,
        "reason": "forward_check_not_requested"
      },
      "model_family": "pvr_ec_o",
      "model_size_label": "100m",
      "model_variant": "pvr_ec_o_shared_only_100m",
      "notes": "Architecture materialized for parameter accounting only; this is not a trained checkpoint or capability result.",
      "owners_per_token_expected": 1.0,
      "top1_runtime_ownership_expected": true,
      "top2_execution_count_expected": 0,
      "top4_execution_count_expected": 0,
      "total_param_ratio_actual_to_target": 0.91741416,
      "total_params_actual": 91741416,
      "total_params_target": 100000000
    }
  ],
  "schema_version": "1.0",
  "status": "BENCH_INFRASTRUCTURE_READY"
}
```