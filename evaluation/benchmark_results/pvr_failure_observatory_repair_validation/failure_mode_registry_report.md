# PVR-EC Failure Mode Registry Report

**Status:** PVR_EC_FAILURE_OBSERVATORY_READY

```json
{
  "status": "PVR_EC_FAILURE_OBSERVATORY_READY",
  "mode_count": 18,
  "required_fields": [
    "id",
    "name",
    "description",
    "trigger_conditions",
    "required_evidence",
    "severity",
    "repeatability_requirement",
    "primary_metrics",
    "secondary_metrics",
    "allowed_repairs",
    "disallowed_repairs",
    "promotion_impact",
    "research_impact"
  ],
  "modes": {
    "PVR_EC_FAILURE_OWNER_PROTOTYPE_COLLAPSE": {
      "id": "PVR_EC_FAILURE_OWNER_PROTOTYPE_COLLAPSE",
      "name": "Owner Prototype Collapse",
      "description": "PVR-EC-O failure mode: Owner Prototype Collapse.",
      "trigger_conditions": [
        "owner_entropy",
        "prototype_entropy",
        "dead_expert_count",
        "expert_monopoly_rate",
        "prototype_local_monopoly_rate"
      ],
      "required_evidence": [
        "owner_entropy",
        "prototype_entropy",
        "dead_expert_count",
        "expert_monopoly_rate",
        "prototype_local_monopoly_rate"
      ],
      "severity": "high",
      "repeatability_requirement": "replay known seed/family/shape before promotion or research expansion",
      "primary_metrics": [
        "owner_entropy",
        "prototype_entropy",
        "dead_expert_count"
      ],
      "secondary_metrics": [
        "expert_monopoly_rate",
        "prototype_local_monopoly_rate"
      ],
      "allowed_repairs": [
        "family_balanced_sampling",
        "family_balanced_loss_light",
        "ownership_bias_clip_adjustment",
        "prototype_entropy_regularization_light",
        "owner_entropy_floor_diagnostic_only"
      ],
      "disallowed_repairs": [
        "Top2/Top4 execution",
        "new router architecture",
        "larger experts",
        "distillation"
      ],
      "promotion_impact": "blocks deployment until repaired or explicitly waived by deployment gate",
      "research_impact": "blocks research only if unknown, unreplayable, or forward purity is violated"
    },
    "PVR_EC_FAILURE_SPARSE_RESIDUAL_UNHELPFUL": {
      "id": "PVR_EC_FAILURE_SPARSE_RESIDUAL_UNHELPFUL",
      "name": "Sparse Residual Unhelpful",
      "description": "PVR-EC-O failure mode: Sparse Residual Unhelpful.",
      "trigger_conditions": [
        "residual_help_rate",
        "residual_harm_rate",
        "expert_delta_contribution_pct",
        "expert_grad_norm",
        "shared_sparse_ratio"
      ],
      "required_evidence": [
        "residual_help_rate",
        "residual_harm_rate",
        "expert_delta_contribution_pct",
        "expert_grad_norm",
        "shared_sparse_ratio"
      ],
      "severity": "high",
      "repeatability_requirement": "replay known seed/family/shape before promotion or research expansion",
      "primary_metrics": [
        "residual_help_rate",
        "residual_harm_rate",
        "expert_delta_contribution_pct"
      ],
      "secondary_metrics": [
        "expert_grad_norm",
        "shared_sparse_ratio"
      ],
      "allowed_repairs": [
        "expert_delta_scale_schedule adjustment",
        "sparse_ce_weight adjustment",
        "decision-token sparse CE",
        "gradient clipping",
        "shared/sparse scale balancing"
      ],
      "disallowed_repairs": [
        "ownership map changes",
        "Top2/Top4",
        "larger experts unless capacity has been proven blocker"
      ],
      "promotion_impact": "blocks deployment until repaired or explicitly waived by deployment gate",
      "research_impact": "blocks research only if unknown, unreplayable, or forward purity is violated"
    },
    "PVR_EC_FAILURE_SPARSE_LOGIT_MISDIRECTION": {
      "id": "PVR_EC_FAILURE_SPARSE_LOGIT_MISDIRECTION",
      "name": "Sparse Logit Misdirection",
      "description": "PVR-EC-O failure mode: Sparse Logit Misdirection.",
      "trigger_conditions": [
        "correct_class_logit_delta",
        "incorrect_class_logit_delta_max",
        "delta_correct_minus_top_wrong",
        "incorrect_overamp_rate",
        "logit_norm"
      ],
      "required_evidence": [
        "correct_class_logit_delta",
        "incorrect_class_logit_delta_max",
        "delta_correct_minus_top_wrong",
        "incorrect_overamp_rate",
        "logit_norm"
      ],
      "severity": "high",
      "repeatability_requirement": "replay known seed/family/shape before promotion or research expansion",
      "primary_metrics": [
        "correct_class_logit_delta",
        "incorrect_class_logit_delta_max",
        "delta_correct_minus_top_wrong"
      ],
      "secondary_metrics": [
        "incorrect_overamp_rate",
        "logit_norm"
      ],
      "allowed_repairs": [
        "sparse_ce",
        "margin alignment",
        "wrong suppress",
        "logit norm penalty",
        "sparse_ce decay",
        "temperature calibration"
      ],
      "disallowed_repairs": [
        "routing changes",
        "expert capacity changes",
        "Top2/Top4 execution"
      ],
      "promotion_impact": "blocks deployment until repaired or explicitly waived by deployment gate",
      "research_impact": "blocks research only if unknown, unreplayable, or forward purity is violated"
    },
    "PVR_EC_FAILURE_INCORRECT_LOGIT_OVERAMP": {
      "id": "PVR_EC_FAILURE_INCORRECT_LOGIT_OVERAMP",
      "name": "Incorrect Logit Overamp",
      "description": "PVR-EC-O failure mode: Incorrect Logit Overamp.",
      "trigger_conditions": [
        "correct_class_logit_delta",
        "incorrect_class_logit_delta_max",
        "delta_correct_minus_top_wrong",
        "incorrect_overamp_rate",
        "logit_norm"
      ],
      "required_evidence": [
        "correct_class_logit_delta",
        "incorrect_class_logit_delta_max",
        "delta_correct_minus_top_wrong",
        "incorrect_overamp_rate",
        "logit_norm"
      ],
      "severity": "high",
      "repeatability_requirement": "replay known seed/family/shape before promotion or research expansion",
      "primary_metrics": [
        "correct_class_logit_delta",
        "incorrect_class_logit_delta_max",
        "delta_correct_minus_top_wrong"
      ],
      "secondary_metrics": [
        "incorrect_overamp_rate",
        "logit_norm"
      ],
      "allowed_repairs": [
        "sparse_ce",
        "margin alignment",
        "wrong suppress",
        "logit norm penalty",
        "sparse_ce decay",
        "temperature calibration"
      ],
      "disallowed_repairs": [
        "routing changes",
        "expert capacity changes",
        "Top2/Top4 execution"
      ],
      "promotion_impact": "blocks deployment until repaired or explicitly waived by deployment gate",
      "research_impact": "blocks research only if unknown, unreplayable, or forward purity is violated"
    },
    "PVR_EC_FAILURE_CALIBRATION_COLLAPSE": {
      "id": "PVR_EC_FAILURE_CALIBRATION_COLLAPSE",
      "name": "Calibration Collapse",
      "description": "PVR-EC-O failure mode: Calibration Collapse.",
      "trigger_conditions": [
        "ECE_proxy",
        "calibration_proxy",
        "confidence_when_correct",
        "confidence_when_wrong",
        "high_confidence_failure_rate"
      ],
      "required_evidence": [
        "ECE_proxy",
        "calibration_proxy",
        "confidence_when_correct",
        "confidence_when_wrong",
        "high_confidence_failure_rate"
      ],
      "severity": "high",
      "repeatability_requirement": "replay known seed/family/shape before promotion or research expansion",
      "primary_metrics": [
        "ECE_proxy",
        "calibration_proxy",
        "confidence_when_correct"
      ],
      "secondary_metrics": [
        "confidence_when_wrong",
        "high_confidence_failure_rate"
      ],
      "allowed_repairs": [
        "posthoc temperature scaling",
        "logit norm medium",
        "sparse_ce decay",
        "entropy-based temperature diagnostic",
        "wrong suppress light"
      ],
      "disallowed_repairs": [
        "capacity increase",
        "routing changes",
        "deployment promotion"
      ],
      "promotion_impact": "blocks deployment until repaired or explicitly waived by deployment gate",
      "research_impact": "blocks research only if unknown, unreplayable, or forward purity is violated"
    },
    "PVR_EC_FAILURE_LOCAL_TO_GLOBAL_TRANSFER": {
      "id": "PVR_EC_FAILURE_LOCAL_TO_GLOBAL_TRANSFER",
      "name": "Local To Global Transfer",
      "description": "PVR-EC-O failure mode: Local To Global Transfer.",
      "trigger_conditions": [
        "token_accuracy",
        "sequence_accuracy",
        "exact_match",
        "decision_token_help_rate",
        "final_token_loss_delta",
        "token_to_sequence_transfer_ratio"
      ],
      "required_evidence": [
        "token_accuracy",
        "sequence_accuracy",
        "exact_match",
        "decision_token_help_rate",
        "final_token_loss_delta",
        "token_to_sequence_transfer_ratio"
      ],
      "severity": "high",
      "repeatability_requirement": "replay known seed/family/shape before promotion or research expansion",
      "primary_metrics": [
        "token_accuracy",
        "sequence_accuracy",
        "exact_match"
      ],
      "secondary_metrics": [
        "decision_token_help_rate",
        "final_token_loss_delta",
        "token_to_sequence_transfer_ratio"
      ],
      "allowed_repairs": [
        "decision-token weighting",
        "final-token weighting",
        "sequence-level diagnostic loss",
        "readout diagnostic only"
      ],
      "disallowed_repairs": [
        "assuming residual is useless",
        "adding Top2/Top4",
        "changing ownership map first"
      ],
      "promotion_impact": "blocks deployment until repaired or explicitly waived by deployment gate",
      "research_impact": "blocks research only if unknown, unreplayable, or forward purity is violated"
    },
    "PVR_EC_FAILURE_SEQUENCE_LENGTH_GENERALIZATION": {
      "id": "PVR_EC_FAILURE_SEQUENCE_LENGTH_GENERALIZATION",
      "name": "Sequence Length Generalization",
      "description": "PVR-EC-O failure mode: Sequence Length Generalization.",
      "trigger_conditions": [
        "loss_gap_vs_fixed",
        "accuracy_gap_vs_fixed",
        "calibration_gap",
        "runtime_purity_passed"
      ],
      "required_evidence": [
        "loss_gap_vs_fixed",
        "accuracy_gap_vs_fixed",
        "calibration_gap",
        "runtime_purity_passed"
      ],
      "severity": "high",
      "repeatability_requirement": "replay known seed/family/shape before promotion or research expansion",
      "primary_metrics": [
        "loss_gap_vs_fixed",
        "accuracy_gap_vs_fixed",
        "calibration_gap"
      ],
      "secondary_metrics": [
        "runtime_purity_passed"
      ],
      "allowed_repairs": [
        "bounded diagnostic-only repair",
        "repeatability replay",
        "slice-specific validation"
      ],
      "disallowed_repairs": [
        "Top2/Top4 execution",
        "new routing architecture",
        "distillation",
        "quantization",
        "model size increase"
      ],
      "promotion_impact": "blocks deployment until repaired or explicitly waived by deployment gate",
      "research_impact": "blocks research only if unknown, unreplayable, or forward purity is violated"
    },
    "PVR_EC_FAILURE_DATA_SPLIT_DIFFICULTY": {
      "id": "PVR_EC_FAILURE_DATA_SPLIT_DIFFICULTY",
      "name": "Data Split Difficulty",
      "description": "PVR-EC-O failure mode: Data Split Difficulty.",
      "trigger_conditions": [
        "loss_gap_vs_fixed",
        "accuracy_gap_vs_fixed",
        "calibration_gap",
        "runtime_purity_passed"
      ],
      "required_evidence": [
        "loss_gap_vs_fixed",
        "accuracy_gap_vs_fixed",
        "calibration_gap",
        "runtime_purity_passed"
      ],
      "severity": "high",
      "repeatability_requirement": "replay known seed/family/shape before promotion or research expansion",
      "primary_metrics": [
        "loss_gap_vs_fixed",
        "accuracy_gap_vs_fixed",
        "calibration_gap"
      ],
      "secondary_metrics": [
        "runtime_purity_passed"
      ],
      "allowed_repairs": [
        "bounded diagnostic-only repair",
        "repeatability replay",
        "slice-specific validation"
      ],
      "disallowed_repairs": [
        "Top2/Top4 execution",
        "new routing architecture",
        "distillation",
        "quantization",
        "model size increase"
      ],
      "promotion_impact": "blocks deployment until repaired or explicitly waived by deployment gate",
      "research_impact": "blocks research only if unknown, unreplayable, or forward purity is violated"
    },
    "PVR_EC_FAILURE_QPM_SHAPE_REGRESSION": {
      "id": "PVR_EC_FAILURE_QPM_SHAPE_REGRESSION",
      "name": "Qpm Shape Regression",
      "description": "PVR-EC-O failure mode: Qpm Shape Regression.",
      "trigger_conditions": [
        "latency_p50",
        "latency_p95",
        "p95_p50_ratio",
        "memory_peak",
        "diagnostic_tensor_retention",
        "cuda_sync_count",
        "cpu_transfer_count",
        "temporary_tensor_alloc_estimate"
      ],
      "required_evidence": [
        "latency_p50",
        "latency_p95",
        "p95_p50_ratio",
        "memory_peak",
        "diagnostic_tensor_retention",
        "cuda_sync_count",
        "cpu_transfer_count",
        "temporary_tensor_alloc_estimate"
      ],
      "severity": "high",
      "repeatability_requirement": "replay known seed/family/shape before promotion or research expansion",
      "primary_metrics": [
        "latency_p50",
        "latency_p95",
        "p95_p50_ratio"
      ],
      "secondary_metrics": [
        "memory_peak",
        "diagnostic_tensor_retention",
        "cuda_sync_count",
        "cpu_transfer_count",
        "temporary_tensor_alloc_estimate"
      ],
      "allowed_repairs": [
        "separate diagnostic and inference paths",
        "disable sparse logit decomposition in inference timing",
        "preallocate tensors",
        "cache masks and ownership bias",
        "remove Python objects from measured forward",
        "CUDA events instead of global sync",
        "warmup per shape"
      ],
      "disallowed_repairs": [
        "changing model math",
        "removing required expert execution",
        "changing output",
        "Top2/Top4"
      ],
      "promotion_impact": "blocks deployment until repaired or explicitly waived by deployment gate",
      "research_impact": "blocks research only if unknown, unreplayable, or forward purity is violated"
    },
    "PVR_EC_FAILURE_RUNTIME_PATH_POLLUTION": {
      "id": "PVR_EC_FAILURE_RUNTIME_PATH_POLLUTION",
      "name": "Runtime Path Pollution",
      "description": "PVR-EC-O failure mode: Runtime Path Pollution.",
      "trigger_conditions": [
        "loss_gap_vs_fixed",
        "accuracy_gap_vs_fixed",
        "calibration_gap",
        "runtime_purity_passed"
      ],
      "required_evidence": [
        "loss_gap_vs_fixed",
        "accuracy_gap_vs_fixed",
        "calibration_gap",
        "runtime_purity_passed"
      ],
      "severity": "high",
      "repeatability_requirement": "replay known seed/family/shape before promotion or research expansion",
      "primary_metrics": [
        "loss_gap_vs_fixed",
        "accuracy_gap_vs_fixed",
        "calibration_gap"
      ],
      "secondary_metrics": [
        "runtime_purity_passed"
      ],
      "allowed_repairs": [
        "bounded diagnostic-only repair",
        "repeatability replay",
        "slice-specific validation"
      ],
      "disallowed_repairs": [
        "Top2/Top4 execution",
        "new routing architecture",
        "distillation",
        "quantization",
        "model size increase"
      ],
      "promotion_impact": "blocks deployment until repaired or explicitly waived by deployment gate",
      "research_impact": "blocks research only if unknown, unreplayable, or forward purity is violated"
    },
    "PVR_EC_FAILURE_SHARED_SPARSE_IMBALANCE": {
      "id": "PVR_EC_FAILURE_SHARED_SPARSE_IMBALANCE",
      "name": "Shared Sparse Imbalance",
      "description": "PVR-EC-O failure mode: Shared Sparse Imbalance.",
      "trigger_conditions": [
        "loss_gap_vs_fixed",
        "accuracy_gap_vs_fixed",
        "calibration_gap",
        "runtime_purity_passed"
      ],
      "required_evidence": [
        "loss_gap_vs_fixed",
        "accuracy_gap_vs_fixed",
        "calibration_gap",
        "runtime_purity_passed"
      ],
      "severity": "high",
      "repeatability_requirement": "replay known seed/family/shape before promotion or research expansion",
      "primary_metrics": [
        "loss_gap_vs_fixed",
        "accuracy_gap_vs_fixed",
        "calibration_gap"
      ],
      "secondary_metrics": [
        "runtime_purity_passed"
      ],
      "allowed_repairs": [
        "bounded diagnostic-only repair",
        "repeatability replay",
        "slice-specific validation"
      ],
      "disallowed_repairs": [
        "Top2/Top4 execution",
        "new routing architecture",
        "distillation",
        "quantization",
        "model size increase"
      ],
      "promotion_impact": "blocks deployment until repaired or explicitly waived by deployment gate",
      "research_impact": "blocks research only if unknown, unreplayable, or forward purity is violated"
    },
    "PVR_EC_FAILURE_EXPERT_DEAD_OR_MONOPOLIZED": {
      "id": "PVR_EC_FAILURE_EXPERT_DEAD_OR_MONOPOLIZED",
      "name": "Expert Dead Or Monopolized",
      "description": "PVR-EC-O failure mode: Expert Dead Or Monopolized.",
      "trigger_conditions": [
        "loss_gap_vs_fixed",
        "accuracy_gap_vs_fixed",
        "calibration_gap",
        "runtime_purity_passed"
      ],
      "required_evidence": [
        "loss_gap_vs_fixed",
        "accuracy_gap_vs_fixed",
        "calibration_gap",
        "runtime_purity_passed"
      ],
      "severity": "high",
      "repeatability_requirement": "replay known seed/family/shape before promotion or research expansion",
      "primary_metrics": [
        "loss_gap_vs_fixed",
        "accuracy_gap_vs_fixed",
        "calibration_gap"
      ],
      "secondary_metrics": [
        "runtime_purity_passed"
      ],
      "allowed_repairs": [
        "bounded diagnostic-only repair",
        "repeatability replay",
        "slice-specific validation"
      ],
      "disallowed_repairs": [
        "Top2/Top4 execution",
        "new routing architecture",
        "distillation",
        "quantization",
        "model size increase"
      ],
      "promotion_impact": "blocks deployment until repaired or explicitly waived by deployment gate",
      "research_impact": "blocks research only if unknown, unreplayable, or forward purity is violated"
    },
    "PVR_EC_FAILURE_HIGH_CONFIDENCE_WRONG": {
      "id": "PVR_EC_FAILURE_HIGH_CONFIDENCE_WRONG",
      "name": "High Confidence Wrong",
      "description": "PVR-EC-O failure mode: High Confidence Wrong.",
      "trigger_conditions": [
        "loss_gap_vs_fixed",
        "accuracy_gap_vs_fixed",
        "calibration_gap",
        "runtime_purity_passed"
      ],
      "required_evidence": [
        "loss_gap_vs_fixed",
        "accuracy_gap_vs_fixed",
        "calibration_gap",
        "runtime_purity_passed"
      ],
      "severity": "high",
      "repeatability_requirement": "replay known seed/family/shape before promotion or research expansion",
      "primary_metrics": [
        "loss_gap_vs_fixed",
        "accuracy_gap_vs_fixed",
        "calibration_gap"
      ],
      "secondary_metrics": [
        "runtime_purity_passed"
      ],
      "allowed_repairs": [
        "bounded diagnostic-only repair",
        "repeatability replay",
        "slice-specific validation"
      ],
      "disallowed_repairs": [
        "Top2/Top4 execution",
        "new routing architecture",
        "distillation",
        "quantization",
        "model size increase"
      ],
      "promotion_impact": "blocks deployment until repaired or explicitly waived by deployment gate",
      "research_impact": "blocks research only if unknown, unreplayable, or forward purity is violated"
    },
    "PVR_EC_FAILURE_BENCHMARK_FAMILY_SPECIFIC": {
      "id": "PVR_EC_FAILURE_BENCHMARK_FAMILY_SPECIFIC",
      "name": "Benchmark Family Specific",
      "description": "PVR-EC-O failure mode: Benchmark Family Specific.",
      "trigger_conditions": [
        "loss_gap_vs_fixed",
        "accuracy_gap_vs_fixed",
        "calibration_gap",
        "runtime_purity_passed"
      ],
      "required_evidence": [
        "loss_gap_vs_fixed",
        "accuracy_gap_vs_fixed",
        "calibration_gap",
        "runtime_purity_passed"
      ],
      "severity": "high",
      "repeatability_requirement": "replay known seed/family/shape before promotion or research expansion",
      "primary_metrics": [
        "loss_gap_vs_fixed",
        "accuracy_gap_vs_fixed",
        "calibration_gap"
      ],
      "secondary_metrics": [
        "runtime_purity_passed"
      ],
      "allowed_repairs": [
        "bounded diagnostic-only repair",
        "repeatability replay",
        "slice-specific validation"
      ],
      "disallowed_repairs": [
        "Top2/Top4 execution",
        "new routing architecture",
        "distillation",
        "quantization",
        "model size increase"
      ],
      "promotion_impact": "blocks deployment until repaired or explicitly waived by deployment gate",
      "research_impact": "blocks research only if unknown, unreplayable, or forward purity is violated"
    },
    "PVR_EC_FAILURE_OWNERSHIP_MAP_STALENESS": {
      "id": "PVR_EC_FAILURE_OWNERSHIP_MAP_STALENESS",
      "name": "Ownership Map Staleness",
      "description": "PVR-EC-O failure mode: Ownership Map Staleness.",
      "trigger_conditions": [
        "loss_gap_vs_fixed",
        "accuracy_gap_vs_fixed",
        "calibration_gap",
        "runtime_purity_passed"
      ],
      "required_evidence": [
        "loss_gap_vs_fixed",
        "accuracy_gap_vs_fixed",
        "calibration_gap",
        "runtime_purity_passed"
      ],
      "severity": "high",
      "repeatability_requirement": "replay known seed/family/shape before promotion or research expansion",
      "primary_metrics": [
        "loss_gap_vs_fixed",
        "accuracy_gap_vs_fixed",
        "calibration_gap"
      ],
      "secondary_metrics": [
        "runtime_purity_passed"
      ],
      "allowed_repairs": [
        "bounded diagnostic-only repair",
        "repeatability replay",
        "slice-specific validation"
      ],
      "disallowed_repairs": [
        "Top2/Top4 execution",
        "new routing architecture",
        "distillation",
        "quantization",
        "model size increase"
      ],
      "promotion_impact": "blocks deployment until repaired or explicitly waived by deployment gate",
      "research_impact": "blocks research only if unknown, unreplayable, or forward purity is violated"
    },
    "PVR_EC_FAILURE_PROTOTYPE_DRIFT": {
      "id": "PVR_EC_FAILURE_PROTOTYPE_DRIFT",
      "name": "Prototype Drift",
      "description": "PVR-EC-O failure mode: Prototype Drift.",
      "trigger_conditions": [
        "loss_gap_vs_fixed",
        "accuracy_gap_vs_fixed",
        "calibration_gap",
        "runtime_purity_passed"
      ],
      "required_evidence": [
        "loss_gap_vs_fixed",
        "accuracy_gap_vs_fixed",
        "calibration_gap",
        "runtime_purity_passed"
      ],
      "severity": "high",
      "repeatability_requirement": "replay known seed/family/shape before promotion or research expansion",
      "primary_metrics": [
        "loss_gap_vs_fixed",
        "accuracy_gap_vs_fixed",
        "calibration_gap"
      ],
      "secondary_metrics": [
        "runtime_purity_passed"
      ],
      "allowed_repairs": [
        "bounded diagnostic-only repair",
        "repeatability replay",
        "slice-specific validation"
      ],
      "disallowed_repairs": [
        "Top2/Top4 execution",
        "new routing architecture",
        "distillation",
        "quantization",
        "model size increase"
      ],
      "promotion_impact": "blocks deployment until repaired or explicitly waived by deployment gate",
      "research_impact": "blocks research only if unknown, unreplayable, or forward purity is violated"
    },
    "PVR_EC_FAILURE_REPAIR_OVERFITS_COLLAPSE_CASE": {
      "id": "PVR_EC_FAILURE_REPAIR_OVERFITS_COLLAPSE_CASE",
      "name": "Repair Overfits Collapse Case",
      "description": "PVR-EC-O failure mode: Repair Overfits Collapse Case.",
      "trigger_conditions": [
        "loss_gap_vs_fixed",
        "accuracy_gap_vs_fixed",
        "calibration_gap",
        "runtime_purity_passed"
      ],
      "required_evidence": [
        "loss_gap_vs_fixed",
        "accuracy_gap_vs_fixed",
        "calibration_gap",
        "runtime_purity_passed"
      ],
      "severity": "high",
      "repeatability_requirement": "replay known seed/family/shape before promotion or research expansion",
      "primary_metrics": [
        "loss_gap_vs_fixed",
        "accuracy_gap_vs_fixed",
        "calibration_gap"
      ],
      "secondary_metrics": [
        "runtime_purity_passed"
      ],
      "allowed_repairs": [
        "bounded diagnostic-only repair",
        "repeatability replay",
        "slice-specific validation"
      ],
      "disallowed_repairs": [
        "Top2/Top4 execution",
        "new routing architecture",
        "distillation",
        "quantization",
        "model size increase"
      ],
      "promotion_impact": "blocks deployment until repaired or explicitly waived by deployment gate",
      "research_impact": "blocks research only if unknown, unreplayable, or forward purity is violated"
    },
    "PVR_EC_FAILURE_UNKNOWN": {
      "id": "PVR_EC_FAILURE_UNKNOWN",
      "name": "Unknown",
      "description": "PVR-EC-O failure mode: Unknown.",
      "trigger_conditions": [
        "loss_gap_vs_fixed",
        "accuracy_gap_vs_fixed",
        "calibration_gap",
        "runtime_purity_passed"
      ],
      "required_evidence": [
        "loss_gap_vs_fixed",
        "accuracy_gap_vs_fixed",
        "calibration_gap",
        "runtime_purity_passed"
      ],
      "severity": "blocking",
      "repeatability_requirement": "replay known seed/family/shape before promotion or research expansion",
      "primary_metrics": [
        "loss_gap_vs_fixed",
        "accuracy_gap_vs_fixed",
        "calibration_gap"
      ],
      "secondary_metrics": [
        "runtime_purity_passed"
      ],
      "allowed_repairs": [
        "bounded diagnostic-only repair",
        "repeatability replay",
        "slice-specific validation"
      ],
      "disallowed_repairs": [
        "Top2/Top4 execution",
        "new routing architecture",
        "distillation",
        "quantization",
        "model size increase"
      ],
      "promotion_impact": "blocks deployment until repaired or explicitly waived by deployment gate",
      "research_impact": "blocks research only if unknown, unreplayable, or forward purity is violated"
    }
  }
}
```