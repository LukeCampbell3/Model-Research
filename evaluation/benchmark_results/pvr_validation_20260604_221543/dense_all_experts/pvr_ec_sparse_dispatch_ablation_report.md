# PVR-EC Sparse Dispatch Ablation Report

**Status:** PARTIAL_PVR_EC_DIAGNOSTIC_IMPLEMENTATION
**Statuses:** PVR_EC_SOFT_SPECULATION_ONLY, PVR_EC_BRANCH_TICKETS_SHADOW_ONLY, PVR_EC_RUNTIME_BRANCHING_DISABLED, PVR_EC_FORMULAIC_MERGEABILITY_ENABLED, PVR_EC_MERGEABILITY_FORMULA_SHADOW_MODE, PVR_EC_SPARSE_DISPATCH_BOTTLENECK, PVR_EC_ASSIGNMENT_BUDGET_DRIFT, PVR_EC_SPARSE_TRANSITION_NOT_SOLVED

Hard runtime branching is disabled. Branch tickets are shadow-only.

## Mode Summary

{
  "dense_all_experts": {
    "record_count": 2,
    "avg_accuracy": 0.0,
    "avg_loss": 4.60674524307251,
    "avg_qpc": 0.0,
    "quality_per_ms": 0.0,
    "fixed_moe_quality_per_ms": 0.0,
    "quality_per_ms_ratio_vs_fixed_moe": 0.0,
    "avg_training_time_s": 0.9649522304534912,
    "avg_inference_time_s": 0.09000921249389648,
    "dispatch_overhead_ratio": 0.9104289447196185,
    "compute_to_dispatch_ratio": 25877950.014546514,
    "actual_avg_k": 3.4551392197608948,
    "assignment_budget_drift": 0.727569580078125
  }
}