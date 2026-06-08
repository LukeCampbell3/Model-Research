# PVR-EC Sparse Dispatch Ablation Report

**Status:** PARTIAL_PVR_EC_DIAGNOSTIC_IMPLEMENTATION
**Statuses:** PVR_EC_SOFT_SPECULATION_ONLY, PVR_EC_BRANCH_TICKETS_SHADOW_ONLY, PVR_EC_RUNTIME_BRANCHING_DISABLED, PVR_EC_FORMULAIC_MERGEABILITY_ENABLED, PVR_EC_MERGEABILITY_FORMULA_SHADOW_MODE, PVR_EC_SPARSE_DISPATCH_PREMATURE, PVR_EC_SPARSE_TRANSITION_NOT_SOLVED

Hard runtime branching is disabled. Branch tickets are shadow-only.

## Mode Summary

{
  "pvr_ec_deploy_top1": {
    "record_count": 12,
    "avg_accuracy": 0.2899926719739791,
    "avg_loss": 0.559650107830142,
    "avg_qpc": 0.2899926719739791,
    "quality_per_ms": 0.0009557548612454687,
    "fixed_moe_quality_per_ms": 0.0,
    "quality_per_ms_ratio_vs_fixed_moe": 95575.48612454686,
    "avg_training_time_s": 21.96028717358907,
    "avg_inference_time_s": 0.320076326529185,
    "dispatch_overhead_ratio": 0.0,
    "compute_to_dispatch_ratio": 0.0,
    "actual_avg_k": 1.0,
    "assignment_budget_drift": 0.0
  }
}