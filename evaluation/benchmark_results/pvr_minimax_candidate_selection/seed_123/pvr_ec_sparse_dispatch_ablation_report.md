# PVR-EC Sparse Dispatch Ablation Report

**Status:** PARTIAL_PVR_EC_DIAGNOSTIC_IMPLEMENTATION
**Statuses:** PVR_EC_SOFT_SPECULATION_ONLY, PVR_EC_BRANCH_TICKETS_SHADOW_ONLY, PVR_EC_RUNTIME_BRANCHING_DISABLED, PVR_EC_FORMULAIC_MERGEABILITY_ENABLED, PVR_EC_MERGEABILITY_FORMULA_SHADOW_MODE, PVR_EC_SPARSE_DISPATCH_PREMATURE, PVR_EC_SPARSE_TRANSITION_NOT_SOLVED

Hard runtime branching is disabled. Branch tickets are shadow-only.

## Mode Summary

{
  "pvr_ec_deploy_top1": {
    "record_count": 80,
    "avg_accuracy": 0.2005307098664959,
    "avg_loss": 0.41218280038253086,
    "avg_qpc": 0.2005307098664959,
    "quality_per_ms": 0.0006958564208625163,
    "fixed_moe_quality_per_ms": 0.0,
    "quality_per_ms_ratio_vs_fixed_moe": 69585.64208625162,
    "avg_training_time_s": 20.942034459114076,
    "avg_inference_time_s": 0.2816945403814316,
    "dispatch_overhead_ratio": 0.0,
    "compute_to_dispatch_ratio": 0.0,
    "actual_avg_k": 1.0,
    "assignment_budget_drift": 0.0
  }
}