# PVR-EC Sparse Dispatch Ablation Report

**Status:** PARTIAL_PVR_EC_DIAGNOSTIC_IMPLEMENTATION
**Statuses:** PVR_EC_SOFT_SPECULATION_ONLY, PVR_EC_BRANCH_TICKETS_SHADOW_ONLY, PVR_EC_RUNTIME_BRANCHING_DISABLED, PVR_EC_FORMULAIC_MERGEABILITY_ENABLED, PVR_EC_MERGEABILITY_FORMULA_SHADOW_MODE, PVR_EC_SPARSE_DISPATCH_BOTTLENECK, PVR_EC_SPARSE_DISPATCH_PREMATURE, PVR_EC_ASSIGNMENT_BUDGET_DRIFT, PVR_EC_SPARSE_TRANSITION_NOT_SOLVED

Hard runtime branching is disabled. Branch tickets are shadow-only.

## Mode Summary

{
  "variable_k_pack_by_expert": {
    "record_count": 2,
    "avg_accuracy": 0.0,
    "avg_loss": 4.606795787811279,
    "avg_qpc": 0.0,
    "quality_per_ms": 0.0,
    "fixed_moe_quality_per_ms": 0.0,
    "quality_per_ms_ratio_vs_fixed_moe": 0.0,
    "avg_training_time_s": 1.0572476387023926,
    "avg_inference_time_s": 0.09128761291503906,
    "dispatch_overhead_ratio": 0.86143701549047,
    "compute_to_dispatch_ratio": 0.24089514125148534,
    "actual_avg_k": 3.4541422724723816,
    "assignment_budget_drift": 0.7270711263020834
  }
}