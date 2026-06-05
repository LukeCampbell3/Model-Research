# PVR-EC Sparse Dispatch Ablation Report

**Status:** PARTIAL_PVR_EC_DIAGNOSTIC_IMPLEMENTATION
**Statuses:** PVR_EC_SOFT_SPECULATION_ONLY, PVR_EC_BRANCH_TICKETS_SHADOW_ONLY, PVR_EC_RUNTIME_BRANCHING_DISABLED, PVR_EC_FORMULAIC_MERGEABILITY_ENABLED, PVR_EC_MERGEABILITY_FORMULA_SHADOW_MODE, PVR_EC_SPARSE_DISPATCH_BOTTLENECK, PVR_EC_SPARSE_TRANSITION_NOT_SOLVED

Hard runtime branching is disabled. Branch tickets are shadow-only.

## Mode Summary

{
  "fixed_top2_all_experts_masked": {
    "record_count": 2,
    "avg_accuracy": 0.0,
    "avg_loss": 4.602883577346802,
    "avg_qpc": 0.0,
    "quality_per_ms": 0.0,
    "fixed_moe_quality_per_ms": 0.0,
    "quality_per_ms_ratio_vs_fixed_moe": 0.0,
    "avg_training_time_s": 0.9378445148468018,
    "avg_inference_time_s": 0.08591508865356445,
    "dispatch_overhead_ratio": 0.8668945890255283,
    "compute_to_dispatch_ratio": 24744274.93289113,
    "actual_avg_k": 2.0,
    "assignment_budget_drift": 0.0
  }
}