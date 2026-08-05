# PVR-EC-O Model Comparison Report

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
  "comparison_type": "architecture_materialization_and_parameter_accounting",
  "comparisons_by_size": {
    "100m": [
      {
        "active_params_per_token_actual": 77203188,
        "active_params_vs_dense_ratio": 1.0,
        "benchmark_evidence": false,
        "comparison_group": "primary_generalized_baseline",
        "model_family": "dense_transformer",
        "model_variant": "dense_transformer_100m",
        "total_params_actual": 77203188
      },
      {
        "active_params_per_token_actual": 71974248,
        "active_params_vs_dense_ratio": 0.932270413496396,
        "benchmark_evidence": false,
        "comparison_group": "primary_generalized_reference_moe",
        "model_family": "vanilla_switch_top1_reference",
        "model_variant": "vanilla_switch_top1_reference_100m",
        "total_params_actual": 78106836
      },
      {
        "active_params_per_token_actual": 79946472,
        "active_params_vs_dense_ratio": 1.035533299479809,
        "benchmark_evidence": false,
        "comparison_group": "pvr_ec_o_primary",
        "model_family": "pvr_ec_o",
        "model_variant": "pvr_ec_o_full_100m",
        "total_params_actual": 85433520
      },
      {
        "active_params_per_token_actual": 72850332,
        "active_params_vs_dense_ratio": 0.9436181832283921,
        "benchmark_evidence": false,
        "comparison_group": "primary_generalized_reference_moe",
        "model_family": "generic_top2_moe_reference",
        "model_variant": "generic_top2_moe_reference_100m",
        "total_params_actual": 78106836
      },
      {
        "active_params_per_token_actual": 79651560,
        "active_params_vs_dense_ratio": 1.0317133535988177,
        "benchmark_evidence": false,
        "comparison_group": "pvr_ec_o_ablation",
        "model_family": "pvr_ec_o",
        "model_variant": "pvr_ec_o_no_prototypes_100m",
        "total_params_actual": 85138608
      },
      {
        "active_params_per_token_actual": 79946472,
        "active_params_vs_dense_ratio": 1.035533299479809,
        "benchmark_evidence": false,
        "comparison_group": "pvr_ec_o_ablation",
        "model_family": "pvr_ec_o",
        "model_variant": "pvr_ec_o_no_contrastive_geometry_100m",
        "total_params_actual": 85433520
      },
      {
        "active_params_per_token_actual": 72868584,
        "active_params_vs_dense_ratio": 0.9438545983360169,
        "benchmark_evidence": false,
        "comparison_group": "pvr_ec_o_ablation",
        "model_family": "pvr_ec_o",
        "model_variant": "pvr_ec_o_no_descriptor_operator_100m",
        "total_params_actual": 78355632
      },
      {
        "active_params_per_token_actual": 42228540,
        "active_params_vs_dense_ratio": 0.5469792257801582,
        "benchmark_evidence": false,
        "comparison_group": "pvr_ec_o_ablation",
        "model_family": "pvr_ec_o",
        "model_variant": "pvr_ec_o_shared_only_100m",
        "total_params_actual": 91741416
      }
    ]
  },
  "model_count": 8,
  "schema_version": "1.0",
  "status": "BENCH_INFRASTRUCTURE_READY",
  "valid_claim": "Models were created and compared for architecture accounting only. Capability comparison remains blocked until real training/eval data and checkpoints exist."
}
```