# PVR-EC Sparse Dispatch Ablation Report

**Status:** PARTIAL_PVR_EC_DIAGNOSTIC_IMPLEMENTATION
**Statuses:** PVR_EC_SOFT_SPECULATION_ONLY, PVR_EC_BRANCH_TICKETS_SHADOW_ONLY, PVR_EC_RUNTIME_BRANCHING_DISABLED, PVR_EC_FORMULAIC_MERGEABILITY_ENABLED, PVR_EC_MERGEABILITY_FORMULA_SHADOW_MODE, PVR_EC_SPARSE_DISPATCH_BOTTLENECK, PVR_EC_SPARSE_DISPATCH_PREMATURE, PVR_EC_ASSIGNMENT_BUDGET_DRIFT, PVR_EC_SPECULATIVE_ROUTER_ENABLED, PVR_EC_SPARSE_TRANSITION_NOT_SOLVED

Hard runtime branching is disabled. Branch tickets are shadow-only.

## Mode Summary

{
  "hybrid_expert_choice_bucketed": {
    "record_count": 2,
    "avg_accuracy": 0.0,
    "avg_loss": 4.607866287231445,
    "avg_qpc": 0.0,
    "quality_per_ms": 0.0,
    "fixed_moe_quality_per_ms": 0.0,
    "quality_per_ms_ratio_vs_fixed_moe": 0.0,
    "avg_training_time_s": 1.0236051082611084,
    "avg_inference_time_s": 0.10060393810272217,
    "dispatch_overhead_ratio": 0.867059207356967,
    "compute_to_dispatch_ratio": 0.24911878131741522,
    "actual_avg_k": 3.5134074091911316,
    "assignment_budget_drift": 0.7567036946614584
  }
}