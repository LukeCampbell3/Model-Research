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
  "created_model_count": 1,
  "device": "cuda",
  "forward_check": true,
  "rows": [
    {
      "active_param_ratio_actual_to_target": 0.77203188,
      "active_params_per_token_actual": 77203188,
      "active_params_per_token_target": 100000000,
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
    }
  ],
  "schema_version": "1.0",
  "status": "BENCH_INFRASTRUCTURE_READY"
}
```