"""PVR-EC: Prototype Variable-k Router with Expert-Choice Expansion.

A collapse-resistant sparse routing system that:
- Routes through semantic prototype neighborhoods
- Guarantees every token a top1 expert owner
- Uses bucketed variable-k (EASY/NORMAL/HARD)
- Expands uncertain tokens through fixed-capacity expert-choice slots
- Applies load-pressure bias without overpowering semantic fit
- Uses bitsets for binary routing structure
- Packs routed tokens by expert id for batched execution
"""

from sparse_loop_moe.models.pvr_ec.pvr_ec_router import PVRECRouter
from sparse_loop_moe.models.pvr_ec.pvr_ec_moe import PVRECMoEFFN
from sparse_loop_moe.models.pvr_ec.diagnostics import (
    EXECUTION_MODES,
    EXPERT_TYPES,
    PVR_EC_STATUSES,
    write_diagnostic_reports,
)

__all__ = [
    "PVRECRouter",
    "PVRECMoEFFN",
    "EXECUTION_MODES",
    "EXPERT_TYPES",
    "PVR_EC_STATUSES",
    "write_diagnostic_reports",
]
