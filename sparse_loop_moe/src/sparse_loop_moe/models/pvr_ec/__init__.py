"""PVR-EC: Prototype Variable-k Router with Expert-Choice Expansion.

A collapse-resistant sparse routing system that:
- Routes through semantic prototype neighborhoods
- Guarantees every token a top1 expert owner
- Uses bucketed variable-k (EASY/NORMAL/HARD)
- Expands uncertain tokens through fixed-capacity expert-choice slots
- Applies load-pressure bias without overpowering semantic fit
- Uses bitsets for binary routing structure
- Packs routed tokens by expert id for batched execution
- Ownership map recall expansion + calibration (offline candidate refresh)
"""

from sparse_loop_moe.models.pvr_ec.pvr_ec_router import PVRECRouter
from sparse_loop_moe.models.pvr_ec.pvr_ec_moe import PVRECMoEFFN
from sparse_loop_moe.models.pvr_ec.diagnostics import (
    EXECUTION_MODES,
    EXPERT_TYPES,
    PVR_EC_STATUSES,
    write_diagnostic_reports,
)
from sparse_loop_moe.models.pvr_ec.ownership_map import (
    OwnershipMapConfig,
    OwnershipMapState,
    PVR_EC_OWNERSHIP_STATUSES,
    PROMOTION_REASON_CODES,
    CANDIDATE_SOURCES,
    generate_candidates,
    compute_semantic_margin,
    ownership_bias_allowed,
    apply_ownership_bias,
    refresh_ownership_map,
    compute_candidate_owner_recall,
    compute_owner_change_metrics,
    compute_failure_decomposition,
    evaluate_promotion_gate,
    select_best_safe_config,
    aggregate_multiseed_results,
    write_ownership_reports,
    build_ownership_map_tensor,
    export_frozen_candidate_map,
    load_frozen_candidate_map,
)

__all__ = [
    "PVRECRouter",
    "PVRECMoEFFN",
    "EXECUTION_MODES",
    "EXPERT_TYPES",
    "PVR_EC_STATUSES",
    "PVR_EC_OWNERSHIP_STATUSES",
    "PROMOTION_REASON_CODES",
    "CANDIDATE_SOURCES",
    "write_diagnostic_reports",
    "OwnershipMapConfig",
    "OwnershipMapState",
    "generate_candidates",
    "compute_semantic_margin",
    "ownership_bias_allowed",
    "apply_ownership_bias",
    "refresh_ownership_map",
    "compute_candidate_owner_recall",
    "compute_owner_change_metrics",
    "compute_failure_decomposition",
    "evaluate_promotion_gate",
    "select_best_safe_config",
    "aggregate_multiseed_results",
    "write_ownership_reports",
    "build_ownership_map_tensor",
    "export_frozen_candidate_map",
    "load_frozen_candidate_map",
]
