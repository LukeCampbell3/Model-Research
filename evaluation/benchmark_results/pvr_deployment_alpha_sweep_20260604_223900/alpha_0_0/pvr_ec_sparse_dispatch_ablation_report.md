# PVR-EC Sparse Dispatch Ablation Report

**Status:** PARTIAL_PVR_EC_DIAGNOSTIC_IMPLEMENTATION
**Statuses:** PVR_EC_SOFT_SPECULATION_ONLY, PVR_EC_BRANCH_TICKETS_SHADOW_ONLY, PVR_EC_RUNTIME_BRANCHING_DISABLED, PVR_EC_FORMULAIC_MERGEABILITY_ENABLED, PVR_EC_MERGEABILITY_FORMULA_SHADOW_MODE, PVR_EC_SPARSE_DISPATCH_PREMATURE, PVR_EC_SPARSE_TRANSITION_NOT_SOLVED

Hard runtime branching is disabled. Branch tickets are shadow-only.

## Mode Summary

{
  "pvr_ec_deploy_top2": {
    "record_count": 8,
    "avg_accuracy": 0.0008720930232558139,
    "avg_loss": 3.9870482981204987,
    "avg_qpc": 0.0008720930232558139,
    "quality_per_ms": 3.954147034585814e-05,
    "fixed_moe_quality_per_ms": 2.51312807945691e-05,
    "quality_per_ms_ratio_vs_fixed_moe": 1.5733965438961273,
    "avg_training_time_s": 1.2076594829559326,
    "avg_inference_time_s": 0.019990652799606323,
    "dispatch_overhead_ratio": 0.0,
    "compute_to_dispatch_ratio": 0.0,
    "actual_avg_k": 2.0,
    "assignment_budget_drift": 0.0
  }
}