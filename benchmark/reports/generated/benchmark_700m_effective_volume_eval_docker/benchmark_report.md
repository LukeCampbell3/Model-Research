# PVR-EC-O Genuine Benchmark Suite Report

Status: `NOT_RUN_MISSING_CHECKPOINT`

This report distinguishes primary generalized baselines, public external positioning, and internal strong-router controls.
Do not infer an architecture win from missing checkpoints, missing data, infrastructure execution, or internal control comparisons.

Allowed comparison language:
- PVR-EC-O does not yet beat generalized baselines.
- PVR-EC-O beats generalized baselines but lags internal strong-router control.
- PVR-EC-O matches internal strong-router control.
- PVR-EC-O beats internal strong-router control.

```json
{
  "benchmark_evidence_count": 4,
  "copied_manifests": [
    "benchmark/reports/generated/benchmark_700m_effective_volume_eval_docker/manifests/contamination_scan_manifest.json",
    "benchmark/reports/generated/benchmark_700m_effective_volume_eval_docker/manifests/eval_manifest.json",
    "benchmark/reports/generated/benchmark_700m_effective_volume_eval_docker/manifests/hardware_manifest.json",
    "benchmark/reports/generated/benchmark_700m_effective_volume_eval_docker/manifests/model_registry_manifest.json",
    "benchmark/reports/generated/benchmark_700m_effective_volume_eval_docker/manifests/model_size_matrix_manifest.json",
    "benchmark/reports/generated/benchmark_700m_effective_volume_eval_docker/manifests/reproducibility_manifest.json",
    "benchmark/reports/generated/benchmark_700m_effective_volume_eval_docker/manifests/training_data_manifest.json"
  ],
  "invalid_claims_blocked": [
    "script execution is not benchmark evidence",
    "missing checkpoints are not model results",
    "custom_fixed_moe_strong_router is not a generic MoE baseline"
  ],
  "limit": 196,
  "model_results": [
    {
      "artifacts": {
        "coding_scorecard": "benchmark/reports/generated/benchmark_700m_effective_volume_eval_docker/scorecards/dense_transformer_700m/coding_scorecard.json",
        "contamination_scan": "benchmark/reports/generated/benchmark_700m_effective_volume_eval_docker/contamination/dense_transformer_700m.json",
        "merged_scorecard": "benchmark/reports/generated/benchmark_700m_effective_volume_eval_docker/scorecards/dense_transformer_700m/merged_scorecard.json",
        "nlp_scorecard": "benchmark/reports/generated/benchmark_700m_effective_volume_eval_docker/scorecards/dense_transformer_700m/nlp_scorecard.json",
        "routing_diagnostics": "benchmark/reports/generated/benchmark_700m_effective_volume_eval_docker/routing_diagnostics/dense_transformer_700m.json"
      },
      "benchmark_evidence": true,
      "comparison_group": "primary_generalized_baseline",
      "model_variant": "dense_transformer_700m",
      "status": "GENUINE_REDUCED_EVAL"
    },
    {
      "artifacts": {
        "coding_scorecard": "benchmark/reports/generated/benchmark_700m_effective_volume_eval_docker/scorecards/vanilla_switch_top1_reference_700m/coding_scorecard.json",
        "contamination_scan": "benchmark/reports/generated/benchmark_700m_effective_volume_eval_docker/contamination/vanilla_switch_top1_reference_700m.json",
        "merged_scorecard": "benchmark/reports/generated/benchmark_700m_effective_volume_eval_docker/scorecards/vanilla_switch_top1_reference_700m/merged_scorecard.json",
        "nlp_scorecard": "benchmark/reports/generated/benchmark_700m_effective_volume_eval_docker/scorecards/vanilla_switch_top1_reference_700m/nlp_scorecard.json",
        "routing_diagnostics": "benchmark/reports/generated/benchmark_700m_effective_volume_eval_docker/routing_diagnostics/vanilla_switch_top1_reference_700m.json"
      },
      "benchmark_evidence": true,
      "comparison_group": "primary_generalized_reference_moe",
      "model_variant": "vanilla_switch_top1_reference_700m",
      "status": "GENUINE_REDUCED_EVAL"
    },
    {
      "artifacts": {
        "coding_scorecard": "benchmark/reports/generated/benchmark_700m_effective_volume_eval_docker/scorecards/pvr_ec_o_full_700m/coding_scorecard.json",
        "contamination_scan": "benchmark/reports/generated/benchmark_700m_effective_volume_eval_docker/contamination/pvr_ec_o_full_700m.json",
        "merged_scorecard": "benchmark/reports/generated/benchmark_700m_effective_volume_eval_docker/scorecards/pvr_ec_o_full_700m/merged_scorecard.json",
        "nlp_scorecard": "benchmark/reports/generated/benchmark_700m_effective_volume_eval_docker/scorecards/pvr_ec_o_full_700m/nlp_scorecard.json",
        "routing_diagnostics": "benchmark/reports/generated/benchmark_700m_effective_volume_eval_docker/routing_diagnostics/pvr_ec_o_full_700m.json"
      },
      "benchmark_evidence": true,
      "comparison_group": "pvr_ec_o_primary",
      "model_variant": "pvr_ec_o_full_700m",
      "status": "GENUINE_REDUCED_EVAL"
    },
    {
      "artifacts": {
        "coding_scorecard": "benchmark/reports/generated/benchmark_700m_effective_volume_eval_docker/scorecards/generic_top2_moe_reference_700m/coding_scorecard.json",
        "contamination_scan": "benchmark/reports/generated/benchmark_700m_effective_volume_eval_docker/contamination/generic_top2_moe_reference_700m.json",
        "merged_scorecard": "benchmark/reports/generated/benchmark_700m_effective_volume_eval_docker/scorecards/generic_top2_moe_reference_700m/merged_scorecard.json",
        "nlp_scorecard": "benchmark/reports/generated/benchmark_700m_effective_volume_eval_docker/scorecards/generic_top2_moe_reference_700m/nlp_scorecard.json",
        "routing_diagnostics": "benchmark/reports/generated/benchmark_700m_effective_volume_eval_docker/routing_diagnostics/generic_top2_moe_reference_700m.json"
      },
      "benchmark_evidence": true,
      "comparison_group": "primary_generalized_reference_moe",
      "model_variant": "generic_top2_moe_reference_700m",
      "status": "GENUINE_REDUCED_EVAL"
    },
    {
      "artifacts": {
        "coding_scorecard": "benchmark/reports/generated/benchmark_700m_effective_volume_eval_docker/scorecards/pvr_ec_o_no_prototypes_700m/coding_scorecard.json",
        "contamination_scan": "benchmark/reports/generated/benchmark_700m_effective_volume_eval_docker/contamination/pvr_ec_o_no_prototypes_700m.json",
        "merged_scorecard": "benchmark/reports/generated/benchmark_700m_effective_volume_eval_docker/scorecards/pvr_ec_o_no_prototypes_700m/merged_scorecard.json",
        "nlp_scorecard": "benchmark/reports/generated/benchmark_700m_effective_volume_eval_docker/scorecards/pvr_ec_o_no_prototypes_700m/nlp_scorecard.json",
        "routing_diagnostics": "benchmark/reports/generated/benchmark_700m_effective_volume_eval_docker/routing_diagnostics/pvr_ec_o_no_prototypes_700m.json"
      },
      "benchmark_evidence": false,
      "comparison_group": "pvr_ec_o_ablation",
      "model_variant": "pvr_ec_o_no_prototypes_700m",
      "status": "NOT_RUN_MISSING_CHECKPOINT"
    },
    {
      "artifacts": {
        "coding_scorecard": "benchmark/reports/generated/benchmark_700m_effective_volume_eval_docker/scorecards/pvr_ec_o_no_contrastive_geometry_700m/coding_scorecard.json",
        "contamination_scan": "benchmark/reports/generated/benchmark_700m_effective_volume_eval_docker/contamination/pvr_ec_o_no_contrastive_geometry_700m.json",
        "merged_scorecard": "benchmark/reports/generated/benchmark_700m_effective_volume_eval_docker/scorecards/pvr_ec_o_no_contrastive_geometry_700m/merged_scorecard.json",
        "nlp_scorecard": "benchmark/reports/generated/benchmark_700m_effective_volume_eval_docker/scorecards/pvr_ec_o_no_contrastive_geometry_700m/nlp_scorecard.json",
        "routing_diagnostics": "benchmark/reports/generated/benchmark_700m_effective_volume_eval_docker/routing_diagnostics/pvr_ec_o_no_contrastive_geometry_700m.json"
      },
      "benchmark_evidence": false,
      "comparison_group": "pvr_ec_o_ablation",
      "model_variant": "pvr_ec_o_no_contrastive_geometry_700m",
      "status": "NOT_RUN_MISSING_CHECKPOINT"
    },
    {
      "artifacts": {
        "coding_scorecard": "benchmark/reports/generated/benchmark_700m_effective_volume_eval_docker/scorecards/pvr_ec_o_no_descriptor_operator_700m/coding_scorecard.json",
        "contamination_scan": "benchmark/reports/generated/benchmark_700m_effective_volume_eval_docker/contamination/pvr_ec_o_no_descriptor_operator_700m.json",
        "merged_scorecard": "benchmark/reports/generated/benchmark_700m_effective_volume_eval_docker/scorecards/pvr_ec_o_no_descriptor_operator_700m/merged_scorecard.json",
        "nlp_scorecard": "benchmark/reports/generated/benchmark_700m_effective_volume_eval_docker/scorecards/pvr_ec_o_no_descriptor_operator_700m/nlp_scorecard.json",
        "routing_diagnostics": "benchmark/reports/generated/benchmark_700m_effective_volume_eval_docker/routing_diagnostics/pvr_ec_o_no_descriptor_operator_700m.json"
      },
      "benchmark_evidence": false,
      "comparison_group": "pvr_ec_o_ablation",
      "model_variant": "pvr_ec_o_no_descriptor_operator_700m",
      "status": "NOT_RUN_MISSING_CHECKPOINT"
    },
    {
      "artifacts": {
        "coding_scorecard": "benchmark/reports/generated/benchmark_700m_effective_volume_eval_docker/scorecards/pvr_ec_o_shared_only_700m/coding_scorecard.json",
        "contamination_scan": "benchmark/reports/generated/benchmark_700m_effective_volume_eval_docker/contamination/pvr_ec_o_shared_only_700m.json",
        "merged_scorecard": "benchmark/reports/generated/benchmark_700m_effective_volume_eval_docker/scorecards/pvr_ec_o_shared_only_700m/merged_scorecard.json",
        "nlp_scorecard": "benchmark/reports/generated/benchmark_700m_effective_volume_eval_docker/scorecards/pvr_ec_o_shared_only_700m/nlp_scorecard.json",
        "routing_diagnostics": "benchmark/reports/generated/benchmark_700m_effective_volume_eval_docker/routing_diagnostics/pvr_ec_o_shared_only_700m.json"
      },
      "benchmark_evidence": false,
      "comparison_group": "pvr_ec_o_ablation",
      "model_variant": "pvr_ec_o_shared_only_700m",
      "status": "NOT_RUN_MISSING_CHECKPOINT"
    }
  ],
  "required_artifacts_generated": {
    "benchmark_report": true,
    "contamination_scan": true,
    "manifests": true,
    "routing_diagnostics": true,
    "scorecards": true
  },
  "schema_version": "1.0",
  "status": "NOT_RUN_MISSING_CHECKPOINT",
  "suite": {
    "evidence_rule": "Only runs with real checkpoint, real data, routing diagnostics, contamination scan, and scorecards count as benchmark evidence.",
    "models": [
      {
        "comparison_group": "primary_generalized_baseline",
        "config_path": "benchmark/configs/generated/dense_transformer_700m.yaml",
        "model_variant": "dense_transformer_700m"
      },
      {
        "comparison_group": "primary_generalized_reference_moe",
        "config_path": "benchmark/configs/generated/vanilla_switch_top1_reference_700m.yaml",
        "model_variant": "vanilla_switch_top1_reference_700m"
      },
      {
        "comparison_group": "pvr_ec_o_primary",
        "config_path": "benchmark/configs/generated/pvr_ec_o_full_700m.yaml",
        "model_variant": "pvr_ec_o_full_700m"
      },
      {
        "comparison_group": "primary_generalized_reference_moe",
        "config_path": "benchmark/configs/generated/generic_top2_moe_reference_700m.yaml",
        "model_variant": "generic_top2_moe_reference_700m"
      },
      {
        "comparison_group": "pvr_ec_o_ablation",
        "config_path": "benchmark/configs/generated/pvr_ec_o_no_prototypes_700m.yaml",
        "model_variant": "pvr_ec_o_no_prototypes_700m"
      },
      {
        "comparison_group": "pvr_ec_o_ablation",
        "config_path": "benchmark/configs/generated/pvr_ec_o_no_contrastive_geometry_700m.yaml",
        "model_variant": "pvr_ec_o_no_contrastive_geometry_700m"
      },
      {
        "comparison_group": "pvr_ec_o_ablation",
        "config_path": "benchmark/configs/generated/pvr_ec_o_no_descriptor_operator_700m.yaml",
        "model_variant": "pvr_ec_o_no_descriptor_operator_700m"
      },
      {
        "comparison_group": "pvr_ec_o_ablation",
        "config_path": "benchmark/configs/generated/pvr_ec_o_shared_only_700m.yaml",
        "model_variant": "pvr_ec_o_shared_only_700m"
      }
    ],
    "required_artifacts": [
      "scorecards",
      "manifests",
      "routing_diagnostics",
      "contamination_scan",
      "benchmark_report"
    ],
    "schema_version": "1.0",
    "stage": "genuine_700m_architecture_benchmark",
    "subset_label": "genuine_reduced_eval",
    "suite_name": "pvr_ec_o_700m_genuine_architecture_benchmark"
  },
  "valid_claim": "Genuine benchmark evidence produced for models with real checkpoints and data."
}
```