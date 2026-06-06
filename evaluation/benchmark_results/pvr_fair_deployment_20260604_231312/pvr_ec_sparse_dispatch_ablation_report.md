# PVR-EC Sparse Dispatch Ablation Report

**Status:** PARTIAL_PVR_EC_DIAGNOSTIC_IMPLEMENTATION
**Statuses:** PVR_EC_SOFT_SPECULATION_ONLY, PVR_EC_BRANCH_TICKETS_SHADOW_ONLY, PVR_EC_RUNTIME_BRANCHING_DISABLED, PVR_EC_FORMULAIC_MERGEABILITY_ENABLED, PVR_EC_MERGEABILITY_FORMULA_SHADOW_MODE, PVR_EC_SPARSE_DISPATCH_PREMATURE, PVR_EC_SPARSE_TRANSITION_NOT_SOLVED

Hard runtime branching is disabled. Branch tickets are shadow-only.

## Mode Summary

{
  "pvr_ec_deploy_top1": {
    "record_count": 8,
    "avg_accuracy": 0.0791813094787608,
    "avg_loss": 0.4484410215324412,
    "avg_qpc": 0.0791813094787608,
    "quality_per_ms": 0.0008401014185824504,
    "fixed_moe_quality_per_ms": 0.0,
    "quality_per_ms_ratio_vs_fixed_moe": 84010.14185824504,
    "avg_training_time_s": 9.520155906677246,
    "avg_inference_time_s": 0.09908202290534973,
    "dispatch_overhead_ratio": 0.0,
    "compute_to_dispatch_ratio": 0.0,
    "actual_avg_k": 1.0,
    "assignment_budget_drift": 0.0
  },
  "pvr_ec_deploy_top2": {
    "record_count": 8,
    "avg_accuracy": 0.07186246571581625,
    "avg_loss": 0.4491594148178895,
    "avg_qpc": 0.07186246571581625,
    "quality_per_ms": 0.0005002739002595026,
    "fixed_moe_quality_per_ms": 0.0,
    "quality_per_ms_ratio_vs_fixed_moe": 50027.390025950255,
    "avg_training_time_s": 12.436001300811768,
    "avg_inference_time_s": 0.15101882815361023,
    "dispatch_overhead_ratio": 0.0,
    "compute_to_dispatch_ratio": 0.0,
    "actual_avg_k": 2.0,
    "assignment_budget_drift": 0.0
  },
  "pvr_ec_deploy_bucketed": {
    "record_count": 8,
    "avg_accuracy": 0.07889782474299675,
    "avg_loss": 0.4455392089827607,
    "avg_qpc": 0.07889782474299675,
    "quality_per_ms": 0.0003651888056732388,
    "fixed_moe_quality_per_ms": 0.0,
    "quality_per_ms_ratio_vs_fixed_moe": 36518.88056732388,
    "avg_training_time_s": 16.919455766677856,
    "avg_inference_time_s": 0.2261243462562561,
    "dispatch_overhead_ratio": 0.0,
    "compute_to_dispatch_ratio": 0.0,
    "actual_avg_k": 3.09580930074056,
    "assignment_budget_drift": 0.0
  }
}