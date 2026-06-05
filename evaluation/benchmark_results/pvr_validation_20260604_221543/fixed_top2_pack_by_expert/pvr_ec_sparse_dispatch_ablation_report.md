# PVR-EC Sparse Dispatch Ablation Report

**Status:** PARTIAL_PVR_EC_DIAGNOSTIC_IMPLEMENTATION
**Statuses:** PVR_EC_SOFT_SPECULATION_ONLY, PVR_EC_BRANCH_TICKETS_SHADOW_ONLY, PVR_EC_RUNTIME_BRANCHING_DISABLED, PVR_EC_FORMULAIC_MERGEABILITY_ENABLED, PVR_EC_MERGEABILITY_FORMULA_SHADOW_MODE, PVR_EC_SPARSE_DISPATCH_BOTTLENECK, PVR_EC_SPARSE_DISPATCH_PREMATURE, PVR_EC_SPARSE_TRANSITION_NOT_SOLVED

Hard runtime branching is disabled. Branch tickets are shadow-only.

## Mode Summary

{
  "fixed_top2_pack_by_expert": {
    "record_count": 2,
    "avg_accuracy": 0.0,
    "avg_loss": 4.605987548828125,
    "avg_qpc": 0.0,
    "quality_per_ms": 0.0,
    "fixed_moe_quality_per_ms": 0.0,
    "quality_per_ms_ratio_vs_fixed_moe": 0.0,
    "avg_training_time_s": 0.9428141117095947,
    "avg_inference_time_s": 0.08882224559783936,
    "dispatch_overhead_ratio": 0.8251033354966979,
    "compute_to_dispatch_ratio": 0.3275342191958087,
    "actual_avg_k": 2.0,
    "assignment_budget_drift": 0.0
  }
}