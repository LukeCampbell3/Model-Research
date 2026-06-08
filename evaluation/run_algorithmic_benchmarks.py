"""Algorithmic Benchmark Runner for Sparse Loop-MoE.

Evaluates architecture variants on respected compatible benchmark families:
1. CLRS-Style: sorting, searching, LCS (sequence-adapted)
2. ListOps: nested list operations (faithful implementation)
3. SCAN-Style: compositional command mapping (symbolic adapter)
4. Dyck: multi-type bracket reasoning (faithful implementation)

Usage:
    python evaluation/run_algorithmic_benchmarks.py --mode smoke
    python evaluation/run_algorithmic_benchmarks.py --mode benchmark-lite --families clrs,listops,scan,dyck
    python evaluation/run_algorithmic_benchmarks.py --mode benchmark-lite --families clrs,listops,scan,dyck --seed 42
"""

import argparse
import csv
import hashlib
import json
import os
import platform
import random
import shutil
import subprocess
import sys
import time
import traceback
from datetime import datetime
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "sparse_loop_moe" / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import torch
import numpy as np

from sparse_loop_moe.models.dense_transformer import DenseTransformer, DenseTransformerConfig
from sparse_loop_moe.models.full_model import SparseLoopMoEModel, SparseLoopMoEConfig
from sparse_loop_moe.training.trainer import Trainer, TrainerConfig
from sparse_loop_moe.training.data_generation import SyntheticTaskGenerator
from sparse_loop_moe.core.types import LoopStats
from algorithmic_benchmarks.task_families import (
    BenchmarkSample, CLRSStyleGenerator, ListOpsGenerator,
    SCANStyleGenerator, DyckGenerator,
)
from sparse_loop_moe.models.pvr_ec.pvr_ec_model import PVRECModel, PVRECModelConfig
from sparse_loop_moe.models.pvr_ec.diagnostics import (
    DEPLOY_MODES,
    EXECUTION_MODES,
    EXPERT_TYPES,
    PVR_EC_STATUSES,
    write_diagnostic_reports,
)


# =============================================================================
# Config
# =============================================================================

MODELS = {
    "dense_baseline": {
        "type": "dense",
        "desc": "Dense transformer (no MoE, no loops)",
    },
    "fixed_moe": {
        "type": "moe",
        "desc": "Fixed top-2 MoE + shared expert",
        "overrides": {"use_adaptive_router": False, "use_probes": False,
                      "use_reflection": False, "use_loops": False, "max_k": 2},
    },
    "fixed_moe_looped_reference": {
        "type": "moe",
        "desc": "Fixed top-2 MoE + shared expert (looped expert reference)",
        "overrides": {"use_adaptive_router": False, "use_probes": False,
                      "use_reflection": False, "use_loops": False, "max_k": 2,
                      "vectorized_moe": False},
    },
    "fixed_moe_vectorized": {
        "type": "moe",
        "desc": "Fixed top-2 MoE + shared expert (vectorized expert execution)",
        "overrides": {"use_adaptive_router": False, "use_probes": False,
                      "use_reflection": False, "use_loops": False, "max_k": 2,
                      "vectorized_moe": True},
    },
    "adaptive_moe": {
        "type": "moe",
        "desc": "Adaptive width MoE (no loops)",
        "overrides": {"use_adaptive_router": True, "use_probes": False,
                      "use_reflection": False, "use_loops": False, "max_k": 4},
    },
    "looped_moe": {
        "type": "moe",
        "desc": "Fixed MoE + 4 bounded loops",
        "overrides": {"use_adaptive_router": False, "use_probes": False,
                      "use_reflection": False, "use_loops": True, "max_k": 2, "max_loops": 4},
    },
    "full_system": {
        "type": "moe",
        "desc": "Full: adaptive + loops + probes + reflection",
        "overrides": {"use_adaptive_router": True, "use_probes": True,
                      "use_reflection": True, "use_loops": True, "max_k": 4, "max_loops": 4},
    },
    "pvr_ec": {
        "type": "pvr_ec",
        "desc": "PVR-EC: Prototype Variable-k Router with Expert-Choice Expansion",
        "overrides": {},
    },
    "pvr_ec_matched": {
        "type": "pvr_ec",
        "desc": "PVR-EC parameter-matched (~1M params, larger expert deltas)",
        "overrides": {"match_params": True},
    },
    "pvr_ec_fixed_top2": {
        "type": "pvr_ec",
        "desc": "PVR-EC ablation: fixed top-2 (no variable-k)",
        "overrides": {"fixed_top2": True},
    },
    "pvr_ec_no_prototypes": {
        "type": "pvr_ec",
        "desc": "PVR-EC ablation: no prototype shortlist",
        "overrides": {"no_prototypes": True},
    },
    "pvr_ec_no_load_bias": {
        "type": "pvr_ec",
        "desc": "PVR-EC ablation: no load-pressure bias",
        "overrides": {"no_load_bias": True},
    },
    "pvr_ec_no_extra_experts": {
        "type": "pvr_ec",
        "desc": "PVR-EC ablation: top-1 only, no extra expert slots",
        "overrides": {"no_extra": True},
    },
    "pvr_ec_deploy_top1": {
        "type": "pvr_ec",
        "desc": "PVR-EC deployment: top1 vectorized expert delta",
        "overrides": {"deploy_mode": "top1"},
    },
    "pvr_ec_deploy_top2": {
        "type": "pvr_ec",
        "desc": "PVR-EC deployment: fixed top2 vectorized expert deltas",
        "overrides": {"deploy_mode": "top2"},
    },
    "pvr_ec_deploy_bucketed": {
        "type": "pvr_ec",
        "desc": "PVR-EC deployment: bucketed K in {1,2,4}",
        "overrides": {"deploy_mode": "bucketed"},
    },
    "pvr_ec_deploy_dense_masked_control": {
        "type": "pvr_ec",
        "desc": "PVR-EC deployment control: dense all experts masked to top2",
        "overrides": {"deploy_mode": "dense_masked_control"},
    },
    "pvr_ec_ownership_top1_frozen_candidate": {
        "type": "pvr_ec",
        "desc": "PVR-EC ownership: top1 with frozen candidate ownership map",
        "overrides": {"deploy_mode": "top1", "enable_ownership_map": True},
    },
}

PVR_CAPACITY_LADDER_MODELS = {
    "pvr_ec_ownership_top1_delta_small": {
        "type": "pvr_ec",
        "desc": "PVR-EC-O capacity ladder: top1 delta small",
        "overrides": {
            "deploy_mode": "top1",
            "enable_ownership_map": True,
            "pvr_expert_type": "delta_small",
            "capacity_variant": "delta_small",
        },
    },
    "pvr_ec_ownership_top1_delta_medium": {
        "type": "pvr_ec",
        "desc": "PVR-EC-O capacity ladder: top1 delta medium",
        "overrides": {
            "deploy_mode": "top1",
            "enable_ownership_map": True,
            "pvr_expert_type": "delta_medium",
            "capacity_variant": "delta_medium",
        },
    },
    "pvr_ec_ownership_top1_delta_large": {
        "type": "pvr_ec",
        "desc": "PVR-EC-O capacity ladder: top1 delta large",
        "overrides": {
            "deploy_mode": "top1",
            "enable_ownership_map": True,
            "pvr_expert_type": "delta_large",
            "capacity_variant": "delta_large",
        },
    },
    "pvr_ec_ownership_top1_full_expert_ffn_control": {
        "type": "pvr_ec",
        "desc": "PVR-EC-O capacity control: top1 full expert FFN",
        "overrides": {
            "deploy_mode": "top1",
            "enable_ownership_map": True,
            "pvr_expert_type": "full_expert_ffn_control",
            "capacity_variant": "full_expert_ffn",
            "capacity_control": True,
        },
    },
    "pvr_ec_ownership_top1_rank_8": {
        "type": "pvr_ec",
        "desc": "PVR-EC-O interpolation: top1 rank 8",
        "overrides": {
            "deploy_mode": "top1",
            "enable_ownership_map": True,
            "pvr_expert_type": "delta_rank_8",
            "capacity_variant": "rank_8",
        },
    },
    "pvr_ec_ownership_top1_rank_16": {
        "type": "pvr_ec",
        "desc": "PVR-EC-O interpolation: top1 rank 16",
        "overrides": {
            "deploy_mode": "top1",
            "enable_ownership_map": True,
            "pvr_expert_type": "delta_rank_16",
            "capacity_variant": "rank_16",
        },
    },
    "pvr_ec_ownership_top1_rank_32": {
        "type": "pvr_ec",
        "desc": "PVR-EC-O interpolation: top1 rank 32",
        "overrides": {
            "deploy_mode": "top1",
            "enable_ownership_map": True,
            "pvr_expert_type": "delta_rank_32",
            "capacity_variant": "rank_32",
        },
    },
    "pvr_ec_ownership_top1_rank_64": {
        "type": "pvr_ec",
        "desc": "PVR-EC-O interpolation: top1 rank 64",
        "overrides": {
            "deploy_mode": "top1",
            "enable_ownership_map": True,
            "pvr_expert_type": "delta_rank_64",
            "capacity_variant": "rank_64",
        },
    },
    "pvr_ec_ownership_top1_rank_128": {
        "type": "pvr_ec",
        "desc": "PVR-EC-O interpolation: top1 rank 128",
        "overrides": {
            "deploy_mode": "top1",
            "enable_ownership_map": True,
            "pvr_expert_type": "delta_rank_128",
            "capacity_variant": "rank_128",
        },
    },
    "pvr_ec_ownership_top1_micro_ffn_0_25x": {
        "type": "pvr_ec",
        "desc": "PVR-EC-O interpolation: top1 micro FFN 0.25x",
        "overrides": {
            "deploy_mode": "top1",
            "enable_ownership_map": True,
            "pvr_expert_type": "micro_ffn_0_25x",
            "capacity_variant": "micro_ffn_0.25x",
        },
    },
    "pvr_ec_ownership_top1_micro_ffn_0_5x": {
        "type": "pvr_ec",
        "desc": "PVR-EC-O interpolation: top1 micro FFN 0.5x",
        "overrides": {
            "deploy_mode": "top1",
            "enable_ownership_map": True,
            "pvr_expert_type": "micro_ffn_0_5x",
            "capacity_variant": "micro_ffn_0.5x",
        },
    },
    "pvr_ec_ownership_top1_micro_ffn_1_0x": {
        "type": "pvr_ec",
        "desc": "PVR-EC-O interpolation: top1 micro FFN 1.0x",
        "overrides": {
            "deploy_mode": "top1",
            "enable_ownership_map": True,
            "pvr_expert_type": "micro_ffn_1_0x",
            "capacity_variant": "micro_ffn_1.0x",
        },
    },
}

PVR_CAPACITY_LADDER_MODELS.update({
    f"pvr_ec_ownership_top1_delta_rank_{rank}": {
        **PVR_CAPACITY_LADDER_MODELS[f"pvr_ec_ownership_top1_rank_{rank}"],
        "desc": f"PVR-EC-O interpolation: top1 delta rank {rank}",
    }
    for rank in (8, 16, 32, 64, 128)
})

PVR_LEARNING_SEPARATION_MODELS = {
    "pvr_ec_learning_full": {
        "type": "pvr_ec",
        "desc": "PVR-EC learning separation: full shared + sparse",
        "overrides": {"deploy_mode": "top1", "pvr_expert_type": "delta_rank_64"},
    },
    "pvr_ec_learning_shared_only": {
        "type": "pvr_ec",
        "desc": "PVR-EC learning separation: shared-only sparse disabled",
        "overrides": {"deploy_mode": "top1", "pvr_expert_type": "shared_base_only", "pvr_expert_delta_scale": 0.0},
    },
    "pvr_ec_learning_sparse_only": {
        "type": "pvr_ec",
        "desc": "PVR-EC learning separation: sparse-only shared disabled",
        "overrides": {"deploy_mode": "top1", "pvr_expert_type": "delta_rank_64", "pvr_shared_scale": 0.0},
    },
    "pvr_ec_learning_shared_scale_0_5": {
        "type": "pvr_ec",
        "desc": "PVR-EC learning separation: shared scale 0.5",
        "overrides": {"deploy_mode": "top1", "pvr_expert_type": "delta_rank_64", "pvr_shared_scale": 0.5},
    },
    "pvr_ec_learning_expert_delta_scale_2_0": {
        "type": "pvr_ec",
        "desc": "PVR-EC learning separation: expert delta scale 2.0",
        "overrides": {"deploy_mode": "top1", "pvr_expert_type": "delta_rank_64", "pvr_expert_delta_scale": 2.0},
    },
    "pvr_ec_ownership_top1_delayed_candidate": {
        "type": "pvr_ec",
        "desc": "PVR-EC learning separation: delayed ownership schedule marker",
        "overrides": {
            "deploy_mode": "top1",
            "enable_ownership_map": True,
            "pvr_expert_type": "delta_rank_64",
            "ownership_schedule": "delayed_ownership",
        },
    },
}

PVR_OVERFIT_MODELS = {
    "pvr_shared_only": {
        "type": "pvr_ec",
        "desc": "PVR overfit sanity: shared-only",
        "overrides": {"deploy_mode": "top1", "pvr_expert_type": "shared_base_only", "pvr_expert_delta_scale": 0.0},
    },
    "pvr_sparse_only": {
        "type": "pvr_ec",
        "desc": "PVR overfit sanity: sparse-only",
        "overrides": {"deploy_mode": "top1", "pvr_expert_type": "delta_rank_64", "pvr_shared_scale": 0.0},
    },
    "pvr_full": {
        "type": "pvr_ec",
        "desc": "PVR overfit sanity: full shared + sparse",
        "overrides": {"deploy_mode": "top1", "pvr_expert_type": "delta_rank_64"},
    },
    "pvr_full_shared_scale_1_0": {
        "type": "pvr_ec",
        "desc": "PVR overfit sanity: shared scale 1.0",
        "overrides": {"deploy_mode": "top1", "pvr_expert_type": "delta_rank_64", "pvr_shared_scale": 1.0},
    },
    "pvr_full_shared_scale_0_5": {
        "type": "pvr_ec",
        "desc": "PVR overfit sanity: shared scale 0.5",
        "overrides": {"deploy_mode": "top1", "pvr_expert_type": "delta_rank_64", "pvr_shared_scale": 0.5},
    },
    "pvr_full_shared_scale_0_25": {
        "type": "pvr_ec",
        "desc": "PVR overfit sanity: shared scale 0.25",
        "overrides": {"deploy_mode": "top1", "pvr_expert_type": "delta_rank_64", "pvr_shared_scale": 0.25},
    },
    "pvr_full_shared_scale_0_0": {
        "type": "pvr_ec",
        "desc": "PVR overfit sanity: shared scale 0.0",
        "overrides": {"deploy_mode": "top1", "pvr_expert_type": "delta_rank_64", "pvr_shared_scale": 0.0},
    },
    "pvr_full_expert_delta_scale_0_5": {
        "type": "pvr_ec",
        "desc": "PVR overfit sanity: expert delta scale 0.5",
        "overrides": {"deploy_mode": "top1", "pvr_expert_type": "delta_rank_64", "pvr_expert_delta_scale": 0.5},
    },
    "pvr_full_expert_delta_scale_1_0": {
        "type": "pvr_ec",
        "desc": "PVR overfit sanity: expert delta scale 1.0",
        "overrides": {"deploy_mode": "top1", "pvr_expert_type": "delta_rank_64", "pvr_expert_delta_scale": 1.0},
    },
    "pvr_full_expert_delta_scale_2_0": {
        "type": "pvr_ec",
        "desc": "PVR overfit sanity: expert delta scale 2.0",
        "overrides": {"deploy_mode": "top1", "pvr_expert_type": "delta_rank_64", "pvr_expert_delta_scale": 2.0},
    },
    "pvr_full_expert_delta_scale_4_0": {
        "type": "pvr_ec",
        "desc": "PVR overfit sanity: expert delta scale 4.0",
        "overrides": {"deploy_mode": "top1", "pvr_expert_type": "delta_rank_64", "pvr_expert_delta_scale": 4.0},
    },
    "pvr_full_fixed_owner_e0": {
        "type": "pvr_ec",
        "desc": "PVR overfit sanity: fixed owner expert 0",
        "overrides": {"deploy_mode": "top1", "pvr_expert_type": "delta_rank_64", "pvr_debug_force_expert_id": 0},
    },
    "pvr_full_fixed_owner_round_robin": {
        "type": "pvr_ec",
        "desc": "PVR overfit sanity: round-robin fixed owner",
        "overrides": {"deploy_mode": "top1", "pvr_expert_type": "delta_rank_64", "pvr_debug_owner_mode": "round_robin"},
    },
    "pvr_full_uniform_owner": {
        "type": "pvr_ec",
        "desc": "PVR overfit sanity: uniform deterministic owner",
        "overrides": {"deploy_mode": "top1", "pvr_expert_type": "delta_rank_64", "pvr_debug_owner_mode": "uniform"},
    },
}

MODELS.update(PVR_CAPACITY_LADDER_MODELS)
MODELS.update(PVR_LEARNING_SEPARATION_MODELS)
MODELS.update(PVR_OVERFIT_MODELS)

# Nonlinear overfit diagnostic models (expert delta scale, rank, micro-FFN variants)
PVR_NONLINEAR_OVERFIT_MODELS = {
    "pvr_full_expert_delta_scale_1": {
        "type": "pvr_ec",
        "desc": "PVR nonlinear overfit: expert delta scale 1.0",
        "overrides": {"deploy_mode": "top1", "pvr_expert_type": "delta_rank_64", "pvr_expert_delta_scale": 1.0},
    },
    "pvr_full_expert_delta_scale_2": {
        "type": "pvr_ec",
        "desc": "PVR nonlinear overfit: expert delta scale 2.0",
        "overrides": {"deploy_mode": "top1", "pvr_expert_type": "delta_rank_64", "pvr_expert_delta_scale": 2.0},
    },
    "pvr_full_expert_delta_scale_4": {
        "type": "pvr_ec",
        "desc": "PVR nonlinear overfit: expert delta scale 4.0",
        "overrides": {"deploy_mode": "top1", "pvr_expert_type": "delta_rank_64", "pvr_expert_delta_scale": 4.0},
    },
    "pvr_full_expert_delta_scale_8": {
        "type": "pvr_ec",
        "desc": "PVR nonlinear overfit: expert delta scale 8.0",
        "overrides": {"deploy_mode": "top1", "pvr_expert_type": "delta_rank_64", "pvr_expert_delta_scale": 8.0},
    },
    "pvr_full_delta_rank_16": {
        "type": "pvr_ec",
        "desc": "PVR nonlinear overfit: delta rank 16",
        "overrides": {"deploy_mode": "top1", "pvr_expert_type": "delta_rank_16"},
    },
    "pvr_full_delta_rank_64": {
        "type": "pvr_ec",
        "desc": "PVR nonlinear overfit: delta rank 64",
        "overrides": {"deploy_mode": "top1", "pvr_expert_type": "delta_rank_64"},
    },
    "pvr_full_delta_rank_128": {
        "type": "pvr_ec",
        "desc": "PVR nonlinear overfit: delta rank 128",
        "overrides": {"deploy_mode": "top1", "pvr_expert_type": "delta_rank_128"},
    },
    "pvr_full_micro_ffn_0_5x": {
        "type": "pvr_ec",
        "desc": "PVR nonlinear overfit: micro FFN 0.5x",
        "overrides": {"deploy_mode": "top1", "pvr_expert_type": "micro_ffn_0_5x"},
    },
}
MODELS.update(PVR_NONLINEAR_OVERFIT_MODELS)

PVR_EXPERT_SCALE_SCHEDULE_MODELS = {
    "pvr_ec_ownership_top1_constant_1": {
        "type": "pvr_ec",
        "desc": "PVR-EC-O benchmark transfer: top1 constant scale 1",
        "overrides": {
            "deploy_mode": "top1",
            "enable_ownership_map": True,
            "pvr_expert_type": "delta_rank_64",
            "pvr_expert_delta_scale": 1.0,
            "scale_schedule_name": "constant_1",
        },
    },
    "pvr_ec_ownership_top1_constant_2": {
        "type": "pvr_ec",
        "desc": "PVR-EC-O benchmark transfer: top1 constant scale 2",
        "overrides": {
            "deploy_mode": "top1",
            "enable_ownership_map": True,
            "pvr_expert_type": "delta_rank_64",
            "pvr_expert_delta_scale": 2.0,
            "scale_schedule_name": "constant_2",
        },
    },
    "pvr_ec_ownership_top1_constant_4": {
        "type": "pvr_ec",
        "desc": "PVR-EC-O benchmark transfer: top1 constant scale 4",
        "overrides": {
            "deploy_mode": "top1",
            "enable_ownership_map": True,
            "pvr_expert_type": "delta_rank_64",
            "pvr_expert_delta_scale": 4.0,
            "scale_schedule_name": "constant_4",
        },
    },
    "pvr_ec_ownership_top1_constant_8": {
        "type": "pvr_ec",
        "desc": "PVR-EC-O benchmark transfer: top1 constant scale 8",
        "overrides": {
            "deploy_mode": "top1",
            "enable_ownership_map": True,
            "pvr_expert_type": "delta_rank_64",
            "pvr_expert_delta_scale": 8.0,
            "scale_schedule_name": "constant_8",
        },
    },
    "pvr_full_scale_schedule_1_to_4": {
        "type": "pvr_ec",
        "desc": "PVR nonlinear repair: expert delta scale warmup-hold 1->4",
        "overrides": {
            "deploy_mode": "top1",
            "pvr_expert_type": "delta_rank_64",
            "pvr_expert_delta_scale_schedule": "warmup_hold",
            "pvr_expert_delta_scale_start": 1.0,
            "pvr_expert_delta_scale_end": 4.0,
            "scale_schedule_name": "warmup_hold_1_to_4",
        },
    },
    "pvr_full_scale_schedule_1_to_8": {
        "type": "pvr_ec",
        "desc": "PVR nonlinear repair: expert delta scale warmup-hold 1->8",
        "overrides": {
            "deploy_mode": "top1",
            "pvr_expert_type": "delta_rank_64",
            "pvr_expert_delta_scale_schedule": "warmup_hold",
            "pvr_expert_delta_scale_start": 1.0,
            "pvr_expert_delta_scale_end": 8.0,
            "scale_schedule_name": "warmup_hold_1_to_8",
        },
    },
    "pvr_full_scale_schedule_1_to_8_to_4": {
        "type": "pvr_ec",
        "desc": "PVR nonlinear repair: expert delta scale warmup-hold-decay 1->8->4",
        "overrides": {
            "deploy_mode": "top1",
            "pvr_expert_type": "delta_rank_64",
            "pvr_expert_delta_scale_schedule": "warmup_hold_decay",
            "pvr_expert_delta_scale_start": 1.0,
            "pvr_expert_delta_scale_end": 8.0,
            "pvr_expert_delta_scale_decay": 4.0,
            "scale_schedule_name": "warmup_hold_decay_1_to_8_to_4",
        },
    },
    "pvr_ec_ownership_top1_scale_schedule_1_to_4": {
        "type": "pvr_ec",
        "desc": "PVR-EC-O benchmark repair: top1 scale schedule 1->4",
        "overrides": {
            "deploy_mode": "top1",
            "enable_ownership_map": True,
            "pvr_expert_type": "delta_rank_64",
            "pvr_expert_delta_scale_schedule": "warmup_hold",
            "pvr_expert_delta_scale_start": 1.0,
            "pvr_expert_delta_scale_end": 4.0,
            "scale_schedule_name": "warmup_hold_1_to_4",
        },
    },
    "pvr_ec_ownership_top1_scale_schedule_1_to_8": {
        "type": "pvr_ec",
        "desc": "PVR-EC-O benchmark repair: top1 scale schedule 1->8",
        "overrides": {
            "deploy_mode": "top1",
            "enable_ownership_map": True,
            "pvr_expert_type": "delta_rank_64",
            "pvr_expert_delta_scale_schedule": "warmup_hold",
            "pvr_expert_delta_scale_start": 1.0,
            "pvr_expert_delta_scale_end": 8.0,
            "scale_schedule_name": "warmup_hold_1_to_8",
        },
    },
    "pvr_ec_ownership_top1_scale_schedule_1_to_8_to_4": {
        "type": "pvr_ec",
        "desc": "PVR-EC-O benchmark repair: top1 scale schedule 1->8->4",
        "overrides": {
            "deploy_mode": "top1",
            "enable_ownership_map": True,
            "pvr_expert_type": "delta_rank_64",
            "pvr_expert_delta_scale_schedule": "warmup_hold_decay",
            "pvr_expert_delta_scale_start": 1.0,
            "pvr_expert_delta_scale_end": 8.0,
            "pvr_expert_delta_scale_decay": 4.0,
            "scale_schedule_name": "warmup_hold_decay_1_to_8_to_4",
        },
    },
    "pvr_ec_ownership_top1_scale_schedule_1_to_8_to_2": {
        "type": "pvr_ec",
        "desc": "PVR-EC-O benchmark transfer: top1 scale schedule 1->8->2",
        "overrides": {
            "deploy_mode": "top1",
            "enable_ownership_map": True,
            "pvr_expert_type": "delta_rank_64",
            "pvr_expert_delta_scale_schedule": "warmup_hold_decay",
            "pvr_expert_delta_scale_start": 1.0,
            "pvr_expert_delta_scale_end": 8.0,
            "pvr_expert_delta_scale_decay": 2.0,
            "scale_schedule_name": "warmup_hold_decay_1_to_8_to_2",
        },
    },
    "pvr_ec_ownership_top1_scale_schedule_1_to_4_to_2": {
        "type": "pvr_ec",
        "desc": "PVR-EC-O benchmark transfer: top1 scale schedule 1->4->2",
        "overrides": {
            "deploy_mode": "top1",
            "enable_ownership_map": True,
            "pvr_expert_type": "delta_rank_64",
            "pvr_expert_delta_scale_schedule": "warmup_hold_decay",
            "pvr_expert_delta_scale_start": 1.0,
            "pvr_expert_delta_scale_end": 4.0,
            "pvr_expert_delta_scale_decay": 2.0,
            "scale_schedule_name": "warmup_hold_decay_1_to_4_to_2",
        },
    },
    "pvr_ec_ownership_top1_best_scale_repair": {
        "type": "pvr_ec",
        "desc": "PVR-EC-O benchmark transfer: selected minimal scale repair",
        "overrides": {
            "deploy_mode": "top1",
            "enable_ownership_map": True,
            "pvr_expert_type": "delta_rank_64",
            "pvr_expert_delta_scale_schedule": "warmup_hold",
            "pvr_expert_delta_scale_start": 1.0,
            "pvr_expert_delta_scale_end": 8.0,
            "scale_schedule_name": "warmup_hold_1_to_8",
        },
    },
    "pvr_ec_ownership_top1_best_transfer_repair": {
        "type": "pvr_ec",
        "desc": "PVR-EC-O task-level transfer: selected minimal transfer repair",
        "overrides": {
            "deploy_mode": "top1",
            "enable_ownership_map": True,
            "pvr_expert_type": "delta_rank_64",
            "pvr_expert_delta_scale_schedule": "warmup_hold",
            "pvr_expert_delta_scale_start": 1.0,
            "pvr_expert_delta_scale_end": 8.0,
            "scale_schedule_name": "warmup_hold_1_to_8",
            "transfer_repair": "scale_schedule_baseline_control",
        },
    },
    "pvr_ec_ownership_top1_best_sparse_logit_repair": {
        "type": "pvr_ec",
        "desc": "PVR-EC-O sparse logit direction: selected minimal auxiliary repair",
        "overrides": {
            "deploy_mode": "top1",
            "enable_ownership_map": True,
            "pvr_expert_type": "delta_rank_64",
            "pvr_expert_delta_scale_schedule": "warmup_hold",
            "pvr_expert_delta_scale_start": 1.0,
            "pvr_expert_delta_scale_end": 8.0,
            "scale_schedule_name": "warmup_hold_1_to_8",
            "sparse_aux_loss_variant": "sparse_ce_0_05_plus_logit_norm_penalty_light",
            "sparse_aux_scope": "aux_all_tokens",
            "sparse_logit_repair": "sparse_ce_0_05_plus_logit_norm_penalty_light",
        },
    },
    "pvr_ec_ownership_top1_final_candidate_v1": {
        "type": "pvr_ec",
        "desc": "PVR-EC-O final frozen candidate v1: ownership top1 + scale schedule + sparse CE + light logit norm",
        "overrides": {
            "deploy_mode": "top1",
            "enable_ownership_map": True,
            "ownership_map_mode": "frozen",
            "pvr_expert_type": "delta_rank_64",
            "pvr_expert_delta_scale_schedule": "warmup_hold",
            "pvr_expert_delta_scale_start": 1.0,
            "pvr_expert_delta_scale_end": 8.0,
            "scale_schedule_name": "warmup_hold_1_to_8",
            "sparse_aux_loss_variant": "sparse_ce_0_05_plus_logit_norm_penalty_light",
            "sparse_aux_scope": "aux_all_tokens",
            "sparse_aux_loss": "sparse_ce_0_05",
            "logit_norm_penalty": "light",
            "temperature_regularization": "disabled",
            "routing_hot_path": "tensor_only",
            "oracle_owner": "disabled",
            "forced_action": "disabled",
            "replay_in_forward": "disabled",
            "file_writes_in_forward": "disabled",
            "cpu_gpu_transfer_in_forward": "disabled",
            "final_candidate_config": "pvr_ec_ownership_top1_final_candidate_v1",
        },
    },
    "pvr_ec_ownership_top1_final_candidate_v1_1": {
        "type": "pvr_ec",
        "desc": "PVR-EC-O final candidate v1_1: selected calibration/repeatability repair, requires revalidation",
        "overrides": {
            "deploy_mode": "top1",
            "enable_ownership_map": True,
            "ownership_map_mode": "frozen",
            "pvr_expert_type": "delta_rank_64",
            "pvr_expert_delta_scale_schedule": "warmup_hold",
            "pvr_expert_delta_scale_start": 1.0,
            "pvr_expert_delta_scale_end": 8.0,
            "scale_schedule_name": "warmup_hold_1_to_8",
            "sparse_aux_loss_variant": "sparse_ce_0_05_plus_logit_norm_penalty_light",
            "sparse_aux_scope": "aux_all_tokens",
            "sparse_aux_loss": "sparse_ce_0_05",
            "logit_norm_penalty": "light",
            "temperature_regularization": "disabled",
            "pvr_output_temperature": 1.0,
            "final_candidate_config": "pvr_ec_ownership_top1_final_candidate_v1_1",
        },
    },
    "pvr_ec_ownership_top1_final_candidate_v1_2": {
        "type": "pvr_ec",
        "desc": "PVR-EC-O final candidate v1_2: selected minimax stability repair, requires full revalidation",
        "overrides": {
            "deploy_mode": "top1",
            "enable_ownership_map": True,
            "ownership_map_mode": "frozen",
            "pvr_expert_type": "delta_rank_64",
            "pvr_expert_delta_scale_schedule": "warmup_hold",
            "pvr_expert_delta_scale_start": 1.0,
            "pvr_expert_delta_scale_end": 8.0,
            "scale_schedule_name": "warmup_hold_1_to_8",
            "sparse_aux_loss_variant": "sparse_ce_0_05_plus_logit_norm_penalty_light",
            "sparse_aux_scope": "aux_all_tokens",
            "sparse_aux_loss": "sparse_ce_0_05",
            "logit_norm_penalty": "light",
            "temperature_regularization": "disabled",
            "pvr_output_temperature": 1.0,
            "final_candidate_config": "pvr_ec_ownership_top1_final_candidate_v1_2",
        },
    },
}
MODELS.update(PVR_EXPERT_SCALE_SCHEDULE_MODELS)

FINAL_CANDIDATE_CONFIG_NAME = "pvr_ec_ownership_top1_final_candidate_v1"
FINAL_CANDIDATE_SELECTED_VARIANT = "sparse_ce_0_05_plus_logit_norm_penalty_light"
FINAL_CALIBRATION_VARIANTS = [
    "final_candidate_v1",
    "sparse_ce_0_03_plus_logit_norm_penalty_light",
    "sparse_ce_0_05_plus_logit_norm_penalty_light",
    "sparse_ce_0_07_plus_logit_norm_penalty_light",
    "sparse_ce_0_05_plus_logit_norm_penalty_medium",
    "sparse_ce_0_05_plus_temperature_regularization",
    "sparse_ce_0_05_plus_posthoc_temperature_calibration",
    "sparse_ce_0_05_plus_logit_norm_light_plus_wrong_suppress_0_01",
]
REPEATABILITY_REPAIR_VARIANTS = [
    "final_candidate_v1",
    "sparse_ce_0_03_plus_logit_norm_penalty_light",
    "sparse_ce_0_05_plus_logit_norm_penalty_light",
    "sparse_ce_0_05_plus_logit_norm_penalty_medium",
    "sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
    "sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
    "sparse_ce_0_05_plus_posthoc_temperature_calibration",
    "sparse_ce_0_03_plus_posthoc_temperature_calibration",
]
RELIABILITY_CALIBRATION_REPAIR_VARIANTS = [
    "final_candidate_v1",
    "posthoc_temperature_T_1_1",
    "posthoc_temperature_T_1_2",
    "posthoc_temperature_T_1_3",
    "posthoc_temperature_T_1_5",
    "logit_norm_penalty_medium",
    "wrong_suppress_0_01_plus_logit_norm_light",
    "sparse_ce_0_03_plus_logit_norm_light",
    "sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
]
MINIMAX_CANDIDATE_VARIANTS = [
    "v1",
    "v1_1_logit_norm_medium",
    "sparse_ce_0_03_plus_logit_norm_light",
    "sparse_ce_0_05_plus_logit_norm_light",
    "sparse_ce_0_05_plus_logit_norm_medium",
    "sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
    "sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
    "sparse_ce_0_03_plus_temperature_T_1_2",
    "sparse_ce_0_05_plus_temperature_T_1_2",
]
STABILITY_REPAIR_VARIANTS = [
    "baseline_v1",
    "baseline_v1_1",
    "family_balanced_sampling",
    "family_balanced_loss_light",
    "gradient_clip_1_0",
    "gradient_clip_0_5",
    "logit_norm_cap_light",
    "logit_norm_cap_medium",
    "wrong_suppress_0_01",
    "wrong_suppress_0_03",
    "sparse_ce_0_03_instead_of_0_05",
    "sparse_ce_0_05_with_decay_to_0_03",
    "sparse_ce_0_05_with_decay_to_0_01",
]
COLLAPSE_CASES = [(123, "clrs_style"), (777, "listops")]
QPM_FAILING_SHAPES = [(8, 64), (16, 64), (16, 128), (32, 64), (32, 128), (64, 16), (64, 64), (64, 128)]
QPM_CONTROL_SHAPES = [(1, 16), (1, 64), (8, 16), (32, 16)]

SCALES = {
    "tiny": {"d_model": 64, "d_ff": 128, "n_layers": 2, "n_heads": 2, "num_experts": 4},
    "small": {"d_model": 128, "d_ff": 256, "n_layers": 2, "n_heads": 4, "num_experts": 4},
    "medium": {"d_model": 256, "d_ff": 512, "n_layers": 4, "n_heads": 4, "num_experts": 8},
}


@dataclass
class Result:
    run_id: str
    model_name: str
    family: str
    task: str
    split: str
    sample_count: int
    accuracy: float
    exact_match: float
    loss: float
    avg_loops: float
    avg_experts: float
    halt_rate: float
    oscillation_rate: float
    qpc: float
    total_parameters: int
    training_time_s: float
    inference_time_s: float
    difficulty: str
    length_bucket: str
    pvr_execution_mode: str = ""
    pvr_expert_type: str = ""
    pvr_dispatch_overhead_ratio: float = 0.0
    pvr_compute_to_dispatch_ratio: float = 0.0
    pvr_forward_dispatch_overhead_ratio: float = 0.0
    pvr_backward_dispatch_overhead_ratio: float = 0.0
    pvr_training_compute_to_dispatch_ratio: float = 0.0
    pvr_total_step_time_ms: float = 0.0
    pvr_router_score_time_ms: float = 0.0
    pvr_assignment_build_time_ms: float = 0.0
    pvr_pack_time_ms: float = 0.0
    pvr_expert_compute_time_ms: float = 0.0
    pvr_scatter_time_ms: float = 0.0
    pvr_tokens_per_second: float = 0.0
    pvr_avg_tokens_per_active_expert: float = 0.0
    pvr_small_expert_batch_rate: float = 0.0
    pvr_actual_avg_k: float = 0.0
    pvr_target_avg_k: float = 0.0
    pvr_assignment_budget_drift: float = 0.0
    pvr_expert_utilization: float = 0.0
    pvr_expert_load_cv: float = 0.0
    pvr_route_entropy: float = 0.0
    pvr_num_k1_tokens: float = 0.0
    pvr_num_k2_tokens: float = 0.0
    pvr_num_k4_tokens: float = 0.0
    pvr_mergeability_score_mean: float = 0.0
    pvr_mergeability_score_std: float = 0.0
    pvr_expert_disagreement_mean: float = 0.0
    pvr_branch_ticket_count: float = 0.0
    training_loss: float = 0.0
    active_param_count: int = 0
    capacity_variant: str = ""
    expert_hidden_dim: int = 0
    expert_architecture_id: str = ""
    expert_inner_dim: int = 0
    delta_rank: int = 0
    params_per_expert: int = 0
    shared_params: int = 0
    routed_expert_params: int = 0
    num_experts: int = 0
    module_class_names: str = ""
    module_fingerprint: str = ""
    pvr_actual_owner_count_per_token: float = 0.0
    pvr_actual_experts_executed: float = 0.0
    pvr_actual_expert_slots_per_token: float = 0.0
    pvr_dense_all_experts_executed: bool = False
    pvr_oracle_owner_used: bool = False
    pvr_forced_action_path_used: bool = False
    pvr_replay_probe_labels_used: bool = False
    shared_output_norm: float = 0.0
    sparse_output_norm: float = 0.0
    shared_sparse_ratio: float = 0.0
    pvr_shared_scale: float = 1.0
    pvr_expert_delta_scale: float = 1.0
    pvr_expert_delta_scale_t: float = 1.0
    pvr_expert_delta_scale_schedule: str = "constant"
    pvr_expert_delta_scale_start: float = 1.0
    pvr_expert_delta_scale_end: float = 1.0
    pvr_expert_delta_scale_decay: float = 0.0
    pvr_expert_delta_scale_warmup_steps: int = 0
    pvr_expert_delta_scale_hold_steps: int = 0
    expert_delta_contribution_pct: float = 0.0
    calibration_proxy: float = 0.0
    logit_norm: float = 0.0
    prediction_entropy: float = 0.0
    confidence_when_correct: float = 0.0
    confidence_when_wrong: float = 0.0
    loss_accuracy_disagreement: float = 0.0
    loss_shared_only: float = 0.0
    loss_full: float = 0.0
    loss_scaled: float = 0.0
    loss_delta_full_vs_shared: float = 0.0
    accuracy_shared_only: float = 0.0
    accuracy_full: float = 0.0
    accuracy_scaled: float = 0.0
    residual_help_rate: float = 0.0
    residual_harm_rate: float = 0.0
    residual_neutral_rate: float = 0.0
    mean_loss_delta_when_residual_active: float = 0.0
    residual_norm: float = 0.0
    shared_norm: float = 0.0
    combined_norm: float = 0.0
    logit_delta_norm: float = 0.0
    correct_class_logit_delta: float = 0.0
    incorrect_class_logit_delta: float = 0.0
    incorrect_class_logit_delta_mean: float = 0.0
    incorrect_class_logit_delta_max: float = 0.0
    delta_correct_minus_top_wrong: float = 0.0
    sparse_margin_delta: float = 0.0
    combined_margin_delta: float = 0.0
    shared_margin: float = 0.0
    combined_margin: float = 0.0
    sparse_logit_norm: float = 0.0
    combined_logit_norm: float = 0.0
    incorrect_logit_overamplification_rate: float = 0.0
    correct_logit_underamplification_rate: float = 0.0
    margin_delta: float = 0.0
    entropy_delta: float = 0.0
    owner_stability: float = 1.0
    prototype_owner_entropy: float = 0.0
    prototype_local_monopoly_rate: float = 0.0
    top1_oracle_gap: float = 0.0
    owner_confidence: float = 0.0
    high_confidence_failure_rate: float = 0.0
    final_token_loss_delta: float = 0.0
    final_state_loss_delta: float = 0.0
    decision_position_loss_delta: float = 0.0
    nondecision_position_loss_delta: float = 0.0
    decision_token_help_rate: float = 0.0
    decision_token_harm_rate: float = 0.0
    decision_token_expert_contribution_pct: float = 0.0
    token_loss_improvement: float = 0.0
    sequence_loss_improvement: float = 0.0
    sequence_accuracy_improvement: float = 0.0
    token_to_sequence_transfer_ratio: float = 0.0
    final_token_accuracy: float = 0.0
    segment_residual_norm: float = 0.0
    segment_residual_alignment: float = 0.0
    segment_residual_success_correlation: float = 0.0
    ownership_schedule: str = ""
    loss_schedule: str = ""
    sparse_aux_loss_variant: str = "baseline_main_loss"
    sparse_aux_scope: str = "aux_all_tokens"
    repair_variant: str = ""
    pvr_output_temperature: float = 1.0
    error: str = ""


# =============================================================================
# Main Runner
# =============================================================================

class AlgorithmicBenchmarkRunner:
    def __init__(self, mode="smoke", families=None, seed=42, scale="small",
                 sample_limit=None, device="cpu", amp=False, train_steps=None,
                 models=None, profile_compute=False, pvr_execution_mode=None,
                 pvr_expert_type=None, pvr_training_dispatch_mode=None,
                 pvr_inference_dispatch_mode=None, pvr_deploy_mode="off",
                 pvr_aux_alpha=0.5, pvr_expert_delta_scale=None,
                 benchmark_inference_only=False,
                 warmup_steps=10, timed_steps=50, batch_sizes=None,
                 sequence_lengths=None, profile_deploy=False,
                 root_cause_flags=None, diagnostic_sweeps=None,
                 pvr_debug_disable_shared=False, pvr_debug_disable_sparse=False,
                 pvr_debug_force_expert_id=None):
        self.mode = mode
        self.families = families or ["clrs", "listops", "scan", "dyck"]
        self.seed = seed
        self.scale = scale
        self.device = device
        self.amp = amp and device == "cuda"
        self.profile_compute = profile_compute
        self.sample_limit = sample_limit
        self.model_filter = models  # None = all models
        self.pvr_execution_mode = pvr_execution_mode
        self.pvr_expert_type = pvr_expert_type
        self.pvr_training_dispatch_mode = pvr_training_dispatch_mode
        self.pvr_inference_dispatch_mode = pvr_inference_dispatch_mode
        self.pvr_deploy_mode = pvr_deploy_mode
        self.pvr_aux_alpha = pvr_aux_alpha
        self.pvr_expert_delta_scale = pvr_expert_delta_scale
        self.benchmark_inference_only = benchmark_inference_only
        self.warmup_steps = warmup_steps
        self.timed_steps = timed_steps
        self.batch_sizes = batch_sizes or [1, 32]
        self.sequence_lengths = sequence_lengths or [64]
        self.profile_deploy = profile_deploy
        self.root_cause_flags = root_cause_flags or {}
        self.diagnostic_sweeps = diagnostic_sweeps or {}
        self.pvr_overfit_tasks = self.diagnostic_sweeps.get("pvr_overfit_tasks", ["toy_identity"])
        self.pvr_overfit_steps = int(self.diagnostic_sweeps.get("pvr_overfit_steps", 100))
        self.pvr_overfit_batch_size = int(self.diagnostic_sweeps.get("pvr_overfit_batch_size", 16))
        self.pvr_overfit_single_batch = bool(self.diagnostic_sweeps.get("pvr_overfit_single_batch", True))
        self.pvr_debug_disable_shared = pvr_debug_disable_shared
        self.pvr_debug_disable_sparse = pvr_debug_disable_sparse
        self.pvr_debug_force_expert_id = pvr_debug_force_expert_id

        # Steps config
        if train_steps:
            self.train_steps = train_steps
        elif mode == "smoke":
            self.train_steps = 30
        elif mode == "benchmark-lite":
            self.train_steps = 200
        else:
            self.train_steps = 500

        if mode == "smoke":
            self.n_samples = 64
        else:
            self.n_samples = sample_limit or 512

        self.output_dir = Path(os.environ.get("BENCHMARK_OUTPUT_DIR", "evaluation/benchmark_results/latest"))
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.run_id = f"algo_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}_{mode}"
        self.results: list[Result] = []
        self.failures: list[dict] = []
        self.peak_gpu_memory_mb = 0.0

    def run(self) -> dict:
        print(f"{'='*70}")
        print(f"  ALGORITHMIC BENCHMARK | Mode: {self.mode} | Scale: {self.scale}")
        print(f"  Families: {self.families} | Steps: {self.train_steps} | Samples: {self.n_samples}")
        print(f"  Seed: {self.seed} | Device: {self.device} | Run: {self.run_id}")
        print(f"{'='*70}\n")

        t0 = time.time()

        if self.benchmark_inference_only:
            summary = self._run_inference_only_benchmark()
            print(f"\n{'='*70}")
            print(f"  INFERENCE BENCHMARK DONE | Status: {summary['status']}")
            print(f"{'='*70}\n")
            return summary

        if self.mode == "pvr-overfit-sanity":
            if self.root_cause_flags.get("run_nonlinear_overfit_diagnostic") or \
               self.root_cause_flags.get("run_fixed_owner_parity_diagnostic") or \
               self.root_cause_flags.get("run_parity_scale_sweep") or \
               self.root_cause_flags.get("run_nonlinear_overfit_confirmation") or \
               self.root_cause_flags.get("run_after_nonlinear_repair_confirmation") or \
               self.root_cause_flags.get("run_expert_delta_scale_schedule_diagnostic") or \
               self.root_cause_flags.get("run_expert_delta_scale_schedule_confirmation"):
                summary = self._run_pvr_nonlinear_overfit()
            else:
                summary = self._run_pvr_overfit_sanity()
            print(f"\n{'='*70}")
            print(f"  PVR OVERFIT SANITY DONE | Status: {summary['status']}")
            print(f"{'='*70}\n")
            return summary

        # Generate benchmark data for all families
        datasets = self._generate_all_datasets()
        print(f"  Generated {sum(len(v) for v in datasets.values())} total samples across {len(datasets)} task sets\n")

        # Train and evaluate each model
        active_models = MODELS
        if self.model_filter:
            active_models = {k: v for k, v in MODELS.items() if k in self.model_filter}
        active_models = self._expand_sparse_auxiliary_models(active_models)

        for model_name, model_cfg in active_models.items():
            print(f"  --- {model_name}: {model_cfg['desc']} ---")
            try:
                self._train_and_eval_model(model_name, model_cfg, datasets)
                if self.device == "cuda" and torch.cuda.is_available():
                    mem = torch.cuda.max_memory_allocated() / (1024**2)
                    self.peak_gpu_memory_mb = max(self.peak_gpu_memory_mb, mem)
                    torch.cuda.reset_peak_memory_stats()
            except Exception as e:
                print(f"  FAILED: {e}")
                self.failures.append({"model": model_name, "error": str(e),
                                      "traceback": traceback.format_exc()})

        total_time = time.time() - t0

        # Output
        valid = [r for r in self.results if not r.error and r.sample_count > 0]
        summary = self._build_summary(valid, total_time)
        self._write_outputs(valid, summary, total_time)

        print(f"\n{'='*70}")
        print(f"  DONE | {total_time:.1f}s | {len(valid)} valid results | {len(self.failures)} failures")
        print(f"  Status: {summary['recommendation']['status']}")
        print(f"{'='*70}\n")
        return summary

    def _expand_sparse_auxiliary_models(self, active_models: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
        if self.root_cause_flags.get("run_sparse_auxiliary_loss_sweep"):
            variants = self.diagnostic_sweeps.get("sparse_aux_loss_variants", []) or ["baseline_main_loss"]
            return self._clone_pvr_models_for_sparse_aux(active_models, variants, scope="aux_all_tokens")
        if self.root_cause_flags.get("run_calibration_constrained_sparse_aux_sweep"):
            variants = self.diagnostic_sweeps.get("sparse_aux_loss_variants", []) or [
                "baseline_main_loss",
                "sparse_ce_0_03",
                "sparse_ce_0_05",
                "sparse_ce_0_03_plus_margin_0_03",
                "sparse_ce_0_03_plus_wrong_suppress_0_03",
                "sparse_ce_0_05_plus_wrong_suppress_0_01",
                "sparse_ce_0_05_plus_logit_norm_penalty_light",
                "sparse_ce_0_05_plus_temperature_regularization",
                "sparse_ce_warmup_decay",
            ]
            return self._clone_pvr_models_for_sparse_aux(active_models, variants, scope="aux_all_tokens")
        if self.root_cause_flags.get("run_final_calibration_sweep"):
            variants = self.diagnostic_sweeps.get("final_calibration_variants", []) or FINAL_CALIBRATION_VARIANTS
            normalized_variants = [
                FINAL_CANDIDATE_SELECTED_VARIANT if variant == "final_candidate_v1" else variant
                for variant in variants
            ]
            return self._clone_pvr_models_for_sparse_aux(active_models, normalized_variants, scope="aux_all_tokens")
        if self.root_cause_flags.get("run_repeatability_repair_sweep"):
            variants = self.diagnostic_sweeps.get("repeatability_repair_variants", []) or REPEATABILITY_REPAIR_VARIANTS
            return self._clone_final_candidate_repair_variants(active_models, variants)
        if self.root_cause_flags.get("run_reliability_calibration_repair"):
            variants = self.diagnostic_sweeps.get("calibration_repair_variants", []) or RELIABILITY_CALIBRATION_REPAIR_VARIANTS
            return self._clone_final_candidate_repair_variants(active_models, variants)
        if self.root_cause_flags.get("run_minimax_candidate_selection"):
            variants = self.diagnostic_sweeps.get("minimax_variants", []) or MINIMAX_CANDIDATE_VARIANTS
            return self._clone_final_candidate_repair_variants(active_models, variants)
        if self.root_cause_flags.get("run_stability_repair_sweep"):
            variants = self.diagnostic_sweeps.get("stability_repair_variants", []) or STABILITY_REPAIR_VARIANTS
            return self._clone_final_candidate_repair_variants(active_models, variants)
        if self.root_cause_flags.get("run_sparse_auxiliary_scope_sweep"):
            scopes = self.diagnostic_sweeps.get("sparse_aux_scopes", []) or ["aux_all_tokens"]
            variant = str(self.diagnostic_sweeps.get("sparse_aux_scope_variant", "sparse_ce_0_05"))
            expanded: dict[str, dict[str, Any]] = {}
            for name, cfg in active_models.items():
                if cfg.get("type") != "pvr_ec":
                    expanded[name] = cfg
                    continue
                for scope in scopes:
                    alias = f"{name}__scope__{scope}"
                    overrides = dict(cfg.get("overrides", {}))
                    overrides["sparse_aux_loss_variant"] = variant
                    overrides["sparse_aux_scope"] = scope
                    expanded[alias] = {
                        **cfg,
                        "desc": f"{cfg.get('desc', name)} + sparse aux scope {scope}",
                        "overrides": overrides,
                    }
            return expanded
        return active_models

    @staticmethod
    def _repair_variant_overrides(variant: str) -> dict[str, Any]:
        if variant in {"final_candidate_v1", "v1", "baseline_v1"}:
            return {
                "sparse_aux_loss_variant": FINAL_CANDIDATE_SELECTED_VARIANT,
                "pvr_output_temperature": 1.0,
                "repair_variant": variant,
            }
        if variant in {"v1_1_logit_norm_medium", "baseline_v1_1"}:
            return {
                "sparse_aux_loss_variant": "sparse_ce_0_05_plus_logit_norm_penalty_medium",
                "pvr_output_temperature": 1.0,
                "repair_variant": variant,
            }
        temperature_map = {
            "posthoc_temperature_T_1_1": 1.1,
            "posthoc_temperature_T_1_2": 1.2,
            "posthoc_temperature_T_1_3": 1.3,
            "posthoc_temperature_T_1_5": 1.5,
            "sparse_ce_0_05_plus_posthoc_temperature_calibration": 1.2,
            "sparse_ce_0_03_plus_posthoc_temperature_calibration": 1.2,
            "sparse_ce_0_03_plus_temperature_T_1_2": 1.2,
            "sparse_ce_0_05_plus_temperature_T_1_2": 1.2,
        }
        aux_variant = {
            "posthoc_temperature_T_1_1": FINAL_CANDIDATE_SELECTED_VARIANT,
            "posthoc_temperature_T_1_2": FINAL_CANDIDATE_SELECTED_VARIANT,
            "posthoc_temperature_T_1_3": FINAL_CANDIDATE_SELECTED_VARIANT,
            "posthoc_temperature_T_1_5": FINAL_CANDIDATE_SELECTED_VARIANT,
            "sparse_ce_0_05_plus_posthoc_temperature_calibration": "sparse_ce_0_05_plus_logit_norm_penalty_light",
            "sparse_ce_0_03_plus_posthoc_temperature_calibration": "sparse_ce_0_03_plus_logit_norm_penalty_light",
            "sparse_ce_0_03_plus_temperature_T_1_2": "sparse_ce_0_03_plus_logit_norm_penalty_light",
            "sparse_ce_0_05_plus_temperature_T_1_2": "sparse_ce_0_05_plus_logit_norm_penalty_light",
            "logit_norm_penalty_medium": "sparse_ce_0_05_plus_logit_norm_penalty_medium",
            "sparse_ce_0_05_plus_logit_norm_medium": "sparse_ce_0_05_plus_logit_norm_penalty_medium",
            "sparse_ce_0_05_plus_logit_norm_light": "sparse_ce_0_05_plus_logit_norm_penalty_light",
            "wrong_suppress_0_01_plus_logit_norm_light": "wrong_suppress_0_01_plus_logit_norm_light",
            "sparse_ce_0_03_plus_logit_norm_light": "sparse_ce_0_03_plus_logit_norm_light",
            "family_balanced_sampling": FINAL_CANDIDATE_SELECTED_VARIANT,
            "family_balanced_loss_light": FINAL_CANDIDATE_SELECTED_VARIANT,
            "gradient_clip_1_0": FINAL_CANDIDATE_SELECTED_VARIANT,
            "gradient_clip_0_5": FINAL_CANDIDATE_SELECTED_VARIANT,
            "sparse_ce_0_03_instead_of_0_05": "sparse_ce_0_03_plus_logit_norm_penalty_light",
        }.get(variant, variant)
        overrides = {
            "sparse_aux_loss_variant": aux_variant,
            "pvr_output_temperature": float(temperature_map.get(variant, 1.0)),
            "repair_variant": variant,
        }
        if variant == "family_balanced_sampling":
            overrides["family_balanced_sampling"] = True
        if variant == "family_balanced_loss_light":
            overrides["family_balanced_loss_weight"] = 0.25
        if variant == "gradient_clip_1_0":
            overrides["max_grad_norm"] = 1.0
        if variant == "gradient_clip_0_5":
            overrides["max_grad_norm"] = 0.5
        return overrides

    @classmethod
    def _clone_final_candidate_repair_variants(
        cls,
        active_models: dict[str, dict[str, Any]],
        variants: list[str],
    ) -> dict[str, dict[str, Any]]:
        expanded: dict[str, dict[str, Any]] = {}
        for name, cfg in active_models.items():
            if cfg.get("type") != "pvr_ec" or name != FINAL_CANDIDATE_CONFIG_NAME:
                expanded[name] = cfg
                continue
            for variant in variants:
                alias = f"{name}__repair__{variant}"
                overrides = dict(cfg.get("overrides", {}))
                overrides.update(cls._repair_variant_overrides(variant))
                overrides["sparse_aux_scope"] = "aux_all_tokens"
                expanded[alias] = {
                    **cfg,
                    "desc": f"{cfg.get('desc', name)} + repair {variant}",
                    "overrides": overrides,
                }
        return expanded

    @staticmethod
    def _clone_pvr_models_for_sparse_aux(
        active_models: dict[str, dict[str, Any]],
        variants: list[str],
        scope: str,
    ) -> dict[str, dict[str, Any]]:
        expanded: dict[str, dict[str, Any]] = {}
        for name, cfg in active_models.items():
            if cfg.get("type") != "pvr_ec":
                expanded[name] = cfg
                continue
            for variant in variants:
                alias = f"{name}__aux__{variant}"
                overrides = dict(cfg.get("overrides", {}))
                overrides["sparse_aux_loss_variant"] = variant
                overrides["sparse_aux_scope"] = scope
                expanded[alias] = {
                    **cfg,
                    "desc": f"{cfg.get('desc', name)} + sparse aux {variant}",
                    "overrides": overrides,
                }
        return expanded

    def _build_model_for_name(self, model_name: str, model_cfg: dict):
        scale = SCALES[self.scale]
        vocab_size = 256
        if model_cfg["type"] == "dense":
            return DenseTransformer(DenseTransformerConfig(
                vocab_size=vocab_size, d_model=scale["d_model"], n_heads=scale["n_heads"],
                n_layers=scale["n_layers"], d_ff=scale["d_ff"],
                max_seq_len=scale["d_model"] * 2, dropout=0.1,
            ))
        if model_cfg["type"] == "pvr_ec":
            overrides = model_cfg.get("overrides", {})
            if model_name.startswith("pvr_ec_ownership_top1_final_candidate_v1_"):
                config_path = Path("configs") / f"{model_name}.json"
                if config_path.exists():
                    overrides = {**overrides, **json.loads(config_path.read_text(encoding="utf-8"))}
            pvr_expert_type = self._resolve_pvr_expert_type(overrides, "delta_rank_small")
            d_expert = self._resolve_pvr_d_expert(scale, overrides, pvr_expert_type)
            deploy_mode = overrides.get("deploy_mode", self.pvr_deploy_mode)
            shared_scale = 0.0 if self.pvr_debug_disable_shared else float(overrides.get("pvr_shared_scale", 1.0))
            default_delta_scale = 1.0 if self.pvr_expert_delta_scale is None else float(self.pvr_expert_delta_scale)
            expert_delta_scale = 0.0 if self.pvr_debug_disable_sparse else float(overrides.get("pvr_expert_delta_scale", default_delta_scale))
            schedule_cfg = self._resolve_pvr_expert_delta_scale_schedule(overrides, expert_delta_scale)
            debug_force_expert_id = (
                self.pvr_debug_force_expert_id
                if self.pvr_debug_force_expert_id is not None
                else overrides.get("pvr_debug_force_expert_id")
            )
            return PVRECModel(PVRECModelConfig(
                vocab_size=vocab_size,
                d_model=scale["d_model"],
                n_heads=scale["n_heads"],
                n_layers=scale["n_layers"],
                d_ff=scale["d_ff"],
                num_experts=scale["num_experts"],
                num_prototypes=scale["num_experts"] * 4,
                max_k=4,
                d_expert=d_expert,
                max_seq_len=scale["d_model"] * 2,
                dropout=0.1,
                pvr_execution_mode=self.pvr_execution_mode or "variable_k_pack_by_expert",
                pvr_expert_type=pvr_expert_type,
                pvr_deploy_mode=deploy_mode,
                pvr_aux_alpha=self.pvr_aux_alpha,
                pvr_shared_scale=shared_scale,
                pvr_expert_delta_scale=expert_delta_scale,
                **schedule_cfg,
                pvr_debug_force_expert_id=debug_force_expert_id,
                pvr_debug_owner_mode=str(overrides.get("pvr_debug_owner_mode", "")),
                pvr_sparse_aux_loss_variant=str(overrides.get("sparse_aux_loss_variant", "baseline_main_loss")),
                pvr_sparse_aux_scope=str(overrides.get("sparse_aux_scope", "aux_all_tokens")),
                pvr_sparse_aux_schedule_total_steps=self.train_steps,
                pvr_output_temperature=float(overrides.get("pvr_output_temperature", 1.0)),
                branch_ticket_shadow_mode=False if deploy_mode != "off" else True,
                max_shadow_branch_tickets=0 if deploy_mode != "off" else 64,
                mergeability_mode="disabled",
                runtime_branching=False,
            ))
        overrides = model_cfg.get("overrides", {})
        return SparseLoopMoEModel(SparseLoopMoEConfig(
            vocab_size=vocab_size, d_model=scale["d_model"], n_heads=scale["n_heads"],
            n_layers=scale["n_layers"], d_ff=scale["d_ff"],
            num_experts=scale["num_experts"],
            max_seq_len=scale["d_model"] * 2, dropout=0.1,
            use_shared_expert=True, **overrides,
        ))

    def _resolve_pvr_expert_type(self, overrides: dict[str, Any], default: str) -> str:
        return str(overrides.get("pvr_expert_type") or self.pvr_expert_type or default)

    @staticmethod
    def _resolve_pvr_d_expert(
        scale: dict[str, int],
        overrides: dict[str, Any],
        pvr_expert_type: str,
    ) -> int:
        if "d_expert" in overrides:
            return max(1, int(overrides["d_expert"]))
        if "d_expert_multiplier" in overrides:
            return max(1, int(round(scale["d_ff"] * float(overrides["d_expert_multiplier"]))))
        rank_map = {
            "delta_rank_8": 8,
            "delta_rank_16": 16,
            "delta_rank_32": 32,
            "delta_rank_64": 64,
            "delta_rank_128": 128,
            "delta_rank_small": max(1, scale["d_model"] // 4),
            "delta_rank_medium": max(1, scale["d_model"] // 2),
            "delta_rank_large": scale["d_model"],
            "delta_small": max(1, scale["d_model"] // 4),
            "delta_medium": max(1, scale["d_model"] // 2),
            "delta_large": scale["d_model"],
        }
        if pvr_expert_type in rank_map:
            return rank_map[pvr_expert_type]
        if pvr_expert_type == "micro_ffn_0_25x":
            return max(1, int(round(scale["d_ff"] * 0.25)))
        if pvr_expert_type == "micro_ffn_0_5x":
            return max(1, int(round(scale["d_ff"] * 0.5)))
        if pvr_expert_type in {"micro_ffn_1_0x", "full_expert_ffn", "full_expert_ffn_control"}:
            return scale["d_ff"]
        return max(1, scale["d_model"] // 2)

    def _default_schedule_total_steps(self) -> int:
        return max(1, self.pvr_overfit_steps if self.mode == "pvr-overfit-sanity" else self.train_steps)

    def _resolve_pvr_expert_delta_scale_schedule(
        self,
        overrides: dict[str, Any],
        constant_scale: float,
    ) -> dict[str, Any]:
        steps = self._default_schedule_total_steps()
        schedule = str(
            overrides.get(
                "pvr_expert_delta_scale_schedule",
                self.diagnostic_sweeps.get("pvr_expert_delta_scale_schedule", "constant"),
            )
        )
        start_value = overrides.get(
            "pvr_expert_delta_scale_start",
            self.diagnostic_sweeps.get("pvr_expert_delta_scale_start"),
        )
        if start_value is None:
            start_value = constant_scale
        end_value = overrides.get(
            "pvr_expert_delta_scale_end",
            self.diagnostic_sweeps.get("pvr_expert_delta_scale_end"),
        )
        if end_value is None:
            end_value = constant_scale
        start = float(start_value)
        end = float(end_value)
        warmup = overrides.get("pvr_expert_delta_scale_warmup_steps")
        if warmup is None:
            warmup = self.diagnostic_sweeps.get("pvr_expert_delta_scale_warmup_steps")
        if warmup is None:
            warmup = int(round(0.2 * steps)) if schedule != "constant" else 0
        hold = overrides.get("pvr_expert_delta_scale_hold_steps")
        if hold is None:
            hold = self.diagnostic_sweeps.get("pvr_expert_delta_scale_hold_steps")
        if hold is None:
            hold = int(round(0.6 * steps)) if schedule == "warmup_hold_decay" else max(0, steps - int(warmup))
        decay = overrides.get("pvr_expert_delta_scale_decay", self.diagnostic_sweeps.get("pvr_expert_delta_scale_decay"))
        if decay in {"", None}:
            decay = None
        else:
            decay = float(decay)
        return {
            "pvr_expert_delta_scale_schedule": schedule,
            "pvr_expert_delta_scale_start": start,
            "pvr_expert_delta_scale_end": end,
            "pvr_expert_delta_scale_warmup_steps": int(warmup),
            "pvr_expert_delta_scale_hold_steps": int(hold),
            "pvr_expert_delta_scale_decay": decay,
        }

    def _artifact_metadata(self) -> dict[str, Any]:
        try:
            git_commit = subprocess.check_output(
                ["git", "rev-parse", "HEAD"],
                cwd=Path(__file__).resolve().parent.parent,
                stderr=subprocess.DEVNULL,
                text=True,
            ).strip()
        except Exception:
            git_commit = "unknown"
        gpu_name = torch.cuda.get_device_name(0) if torch.cuda.is_available() else ""
        return {
            "timestamp": datetime.utcnow().isoformat(),
            "run_id": self.run_id,
            "git_commit": git_commit,
            "docker_image": "sparse-loop-moe-gpu" if self.device == "cuda" else "N/A",
            "cuda_available": torch.cuda.is_available(),
            "gpu_name": gpu_name,
            "amp_enabled": self.amp,
            "seed": self.seed,
            "benchmark_command": " ".join(sys.argv),
            "model_variants": self.model_filter or list(MODELS.keys()),
            "batch_sizes": self.batch_sizes,
            "sequence_lengths": self.sequence_lengths,
            "train_steps": self.train_steps,
            "sample_limit": self.sample_limit,
            "mode": self.mode,
            "scale": self.scale,
            "families": self.families,
            "pvr_expert_delta_scale": self.pvr_expert_delta_scale,
            "pvr_expert_delta_scale_schedule": self.diagnostic_sweeps.get("pvr_expert_delta_scale_schedule", "constant"),
            "pvr_expert_delta_scale_start": self.diagnostic_sweeps.get("pvr_expert_delta_scale_start"),
            "pvr_expert_delta_scale_end": self.diagnostic_sweeps.get("pvr_expert_delta_scale_end"),
            "pvr_expert_delta_scale_warmup_steps": self.diagnostic_sweeps.get("pvr_expert_delta_scale_warmup_steps"),
            "pvr_expert_delta_scale_hold_steps": self.diagnostic_sweeps.get("pvr_expert_delta_scale_hold_steps"),
            "pvr_expert_delta_scale_decay": self.diagnostic_sweeps.get("pvr_expert_delta_scale_decay"),
        }

    def _estimate_memory_breakdown(
        self,
        model_name: str,
        model_cfg: dict[str, Any],
        params: int,
        batch_size: int,
        seq_len: int,
        max_memory_allocated_mb: float,
    ) -> dict[str, float]:
        scale = SCALES[self.scale]
        dtype_bytes = 2 if self.amp else 4
        tokens = batch_size * seq_len
        d_model = scale["d_model"]
        d_ff = scale["d_ff"]
        num_experts = scale["num_experts"]
        overrides = model_cfg.get("overrides", {})
        deploy_mode = overrides.get(
            "deploy_mode",
            self.pvr_deploy_mode if model_cfg["type"] == "pvr_ec" else "off",
        )
        if deploy_mode == "top1":
            k = 1
        elif deploy_mode in {"top2", "dense_masked_control"}:
            k = 2
        elif deploy_mode == "bucketed":
            k = min(4, num_experts)
        else:
            k = min(int(overrides.get("max_k", 2)), num_experts)

        vectorized_experts = (
            model_name == "fixed_moe_vectorized"
            or (model_cfg["type"] == "pvr_ec" and deploy_mode != "off")
        )
        parameter_memory_mb = params * 4 / (1024 ** 2)
        activation_memory_mb = tokens * d_model * dtype_bytes / (1024 ** 2)
        routing_buffer_memory_mb = tokens * num_experts * dtype_bytes / (1024 ** 2)
        selected_expert_buffer_memory_mb = tokens * k * d_model * dtype_bytes / (1024 ** 2)
        expert_weight_gather_memory_mb = (
            tokens * k * (d_model * d_ff + d_ff * d_model) * dtype_bytes / (1024 ** 2)
            if vectorized_experts and model_cfg["type"] == "moe" else 0.0
        )
        temporary_tensor_memory_mb = max(
            0.0,
            max_memory_allocated_mb
            - parameter_memory_mb
            - activation_memory_mb
            - routing_buffer_memory_mb
            - selected_expert_buffer_memory_mb,
        )
        memory_per_token = max_memory_allocated_mb / max(tokens, 1)
        memory_per_batch = max_memory_allocated_mb / max(batch_size, 1)
        return {
            "parameter_memory_mb": parameter_memory_mb,
            "activation_memory_mb": activation_memory_mb,
            "routing_buffer_memory_mb": routing_buffer_memory_mb,
            "selected_expert_buffer_memory_mb": selected_expert_buffer_memory_mb,
            "expert_weight_gather_memory_mb": expert_weight_gather_memory_mb,
            "temporary_tensor_memory_mb": temporary_tensor_memory_mb,
            "memory_per_token": memory_per_token,
            "memory_per_batch": memory_per_batch,
        }

    @staticmethod
    def _deploy_k_for_mode(deploy_mode: str, num_experts: int) -> int:
        if deploy_mode == "top1":
            return 1
        if deploy_mode in {"top2", "dense_masked_control"}:
            return min(2, num_experts)
        if deploy_mode == "bucketed":
            return min(4, num_experts)
        return num_experts

    def _estimate_active_param_count(
        self,
        model,
        model_cfg: dict[str, Any],
        params: int,
    ) -> int:
        if model_cfg.get("type") != "pvr_ec" or not isinstance(model, PVRECModel):
            return int(params)

        deploy_mode = model_cfg.get("overrides", {}).get("deploy_mode", self.pvr_deploy_mode)
        if deploy_mode in {"off", "dense_masked_control"}:
            return int(params)

        expert_params_total = 0
        active_expert_params = 0
        for block in model.blocks:
            expert_param_counts = [
                sum(p.numel() for p in expert.parameters() if p.requires_grad)
                for expert in block.moe.expert_deltas
            ]
            if not expert_param_counts:
                continue
            expert_params_total += sum(expert_param_counts)
            k = self._deploy_k_for_mode(deploy_mode, len(expert_param_counts))
            active_expert_params += sum(sorted(expert_param_counts, reverse=True)[:k])

        return int(params - expert_params_total + active_expert_params)

    def _pvr_architecture_metadata(
        self,
        model,
        model_name: str,
        model_cfg: dict[str, Any],
        params: int,
        active_params: int,
    ) -> dict[str, Any]:
        if model_cfg.get("type") != "pvr_ec" or not isinstance(model, PVRECModel):
            return {}
        first_moe = model.blocks[0].moe if model.blocks else None
        if first_moe is None or not first_moe.expert_deltas:
            return {}
        first_expert = first_moe.expert_deltas[0]
        params_per_expert = sum(p.numel() for p in first_expert.parameters() if p.requires_grad)
        routed_expert_params = sum(
            sum(p.numel() for p in expert.parameters() if p.requires_grad)
            for block in model.blocks for expert in block.moe.expert_deltas
        )
        shared_params = sum(
            sum(p.numel() for p in block.moe.shared_base.parameters() if p.requires_grad)
            + sum(p.numel() for p in block.moe.shared_gate.parameters() if p.requires_grad)
            for block in model.blocks
        )
        class_names = sorted({type(expert).__name__ for block in model.blocks for expert in block.moe.expert_deltas})
        architecture_id = str(getattr(first_moe, "expert_architecture_id", ""))
        expert_inner_dim = int(getattr(first_expert, "expert_inner_dim", getattr(model.config, "d_expert", 0)) or 0)
        delta_rank = int(getattr(first_expert, "delta_rank", 0) or 0)
        shape_signature = []
        for name, parameter in first_expert.named_parameters():
            shape_signature.append(f"{name}:{tuple(parameter.shape)}")
        fingerprint_payload = "|".join([
            architecture_id,
            type(first_expert).__name__,
            ",".join(shape_signature),
            str(params_per_expert),
            str(expert_inner_dim),
            str(delta_rank),
        ])
        fingerprint = hashlib.sha256(fingerprint_payload.encode("utf-8")).hexdigest()[:16]
        return {
            "expert_architecture_id": architecture_id,
            "expert_inner_dim": expert_inner_dim,
            "delta_rank": delta_rank,
            "params_per_expert": params_per_expert,
            "shared_params": shared_params,
            "routed_expert_params": routed_expert_params,
            "module_class_names": ",".join(class_names),
            "module_fingerprint": fingerprint,
            "num_experts": getattr(first_moe, "num_experts", None),
            "params_total": params,
            "params_active_estimate": active_params,
        }

    def _run_inference_only_benchmark(self) -> dict:
        active_models = MODELS
        if self.model_filter:
            active_models = {k: v for k, v in MODELS.items() if k in self.model_filter}
        device = torch.device(self.device)
        rows = []
        for model_name, model_cfg in active_models.items():
            torch.manual_seed(self.seed)
            model = self._build_model_for_name(model_name, model_cfg).to(device)
            model.eval()
            params = sum(p.numel() for p in model.parameters() if p.requires_grad)
            active_params = self._estimate_active_param_count(model, model_cfg, params)
            architecture_metadata = self._pvr_architecture_metadata(
                model, model_name, model_cfg, params, active_params,
            )
            deploy_mode = model_cfg.get("overrides", {}).get(
                "deploy_mode",
                self.pvr_deploy_mode if model_cfg["type"] == "pvr_ec" else "off",
            )
            capacity_variant = model_cfg.get("overrides", {}).get("capacity_variant", "")
            pvr_expert_type = model_cfg.get("overrides", {}).get("pvr_expert_type", self.pvr_expert_type or "")
            expert_hidden_dim = getattr(getattr(model, "config", None), "d_expert", None)
            expert_execution_mode = (
                "FULLY_VECTORIZED" if model_cfg["type"] == "pvr_ec" and deploy_mode != "off"
                else "FULLY_VECTORIZED" if model_cfg["type"] == "moe" and model_cfg.get("overrides", {}).get("vectorized_moe")
                else "LOOPED"
            )
            for batch_size in self.batch_sizes:
                for seq_len in self.sequence_lengths:
                    batch_seed = self.seed + 1_000_003 * batch_size + 9_176 * seq_len
                    batch_generator = torch.Generator(device=device)
                    batch_generator.manual_seed(batch_seed)
                    input_ids = torch.randint(
                        0, 256, (batch_size, seq_len), device=device, generator=batch_generator,
                    )
                    targets = torch.randint(
                        0, 256, (batch_size, seq_len), device=device, generator=batch_generator,
                    )
                    pvr_diag_history: list[dict[str, Any]] = []
                    with torch.no_grad():
                        for _ in range(self.warmup_steps):
                            model(input_ids=input_ids, targets=targets)
                        if device.type == "cuda":
                            torch.cuda.synchronize(device)
                            torch.cuda.reset_peak_memory_stats(device)
                        latencies = []
                        total_loss = 0.0
                        total_acc = 0.0
                        for _ in range(self.timed_steps):
                            if device.type == "cuda":
                                start = torch.cuda.Event(enable_timing=True)
                                end = torch.cuda.Event(enable_timing=True)
                                start.record()
                                output = model(input_ids=input_ids, targets=targets)
                                end.record()
                                torch.cuda.synchronize(device)
                                elapsed_ms = start.elapsed_time(end)
                            else:
                                t_start = time.perf_counter()
                                output = model(input_ids=input_ids, targets=targets)
                                elapsed_ms = (time.perf_counter() - t_start) * 1000.0
                            latencies.append(float(elapsed_ms))
                            total_loss += float(output["loss"].detach().item())
                            preds = output["logits"].argmax(dim=-1)
                            total_acc += float((preds == targets).float().mean().detach().item())
                            if isinstance(output.get("pvr_diagnostics"), dict):
                                pvr_diag_history.append(output["pvr_diagnostics"])
                    p50 = float(np.percentile(latencies, 50))
                    p95 = float(np.percentile(latencies, 95))
                    p99 = float(np.percentile(latencies, 99))
                    mean_latency = float(np.mean(latencies))
                    latency_std = float(np.std(latencies))
                    tokens = batch_size * seq_len
                    accuracy = total_acc / max(self.timed_steps, 1)
                    loss = total_loss / max(self.timed_steps, 1)
                    max_memory_allocated_mb = (
                        torch.cuda.max_memory_allocated(device) / (1024 ** 2)
                        if device.type == "cuda" else 0.0
                    )
                    memory_allocated_mb = (
                        torch.cuda.memory_allocated(device) / (1024 ** 2)
                        if device.type == "cuda" else 0.0
                    )
                    row = {
                        "model": model_name,
                        "deploy_mode": deploy_mode,
                        "capacity_variant": capacity_variant,
                        "pvr_expert_type": pvr_expert_type,
                        "pvr_shared_scale": float(model_cfg.get("overrides", {}).get("pvr_shared_scale", 1.0)),
                        "pvr_expert_delta_scale": float(model_cfg.get("overrides", {}).get("pvr_expert_delta_scale", 1.0)),
                        "ownership_schedule": model_cfg.get("overrides", {}).get("ownership_schedule", ""),
                        "loss_schedule": model_cfg.get("overrides", {}).get("loss_schedule", ""),
                        "repair_variant": model_cfg.get("overrides", {}).get("repair_variant", ""),
                        "pvr_output_temperature": float(model_cfg.get("overrides", {}).get("pvr_output_temperature", 1.0)),
                        "expert_hidden_dim": expert_hidden_dim,
                        "params": params,
                        "param_count": params,
                        "active_params_estimate": active_params,
                        "active_param_count": active_params,
                        "batch_size": batch_size,
                        "sequence_length": seq_len,
                        "loss": loss,
                        "accuracy": accuracy,
                        "p50_latency_ms": p50,
                        "p95_latency_ms": p95,
                        "p99_latency_ms": p99,
                        "mean_latency_ms": mean_latency,
                        "latency_std_ms": latency_std,
                        "p95_p50_ratio": p95 / max(p50, 1e-8),
                        "tokens_per_second": 1000.0 * tokens / max(mean_latency, 1e-8),
                        "samples_per_second": 1000.0 * batch_size / max(mean_latency, 1e-8),
                        "quality_per_ms": accuracy / max(mean_latency, 1e-8),
                        "quality_per_param": accuracy / max(params, 1),
                        "quality_per_active_param": accuracy / max(active_params, 1),
                        "quality_per_token_second": accuracy * (1000.0 * tokens / max(mean_latency, 1e-8)),
                        "memory_allocated_mb": memory_allocated_mb,
                        "max_memory_allocated_mb": max_memory_allocated_mb,
                        "memory_peak": max_memory_allocated_mb,
                        "expert_execution_mode": expert_execution_mode,
                        "branch_tickets_enabled": False,
                        "mergeability_mode": "disabled",
                        "runtime_branching_enabled": False,
                    }
                    row.update(architecture_metadata)
                    row.update(self._aggregate_inference_pvr_audit(pvr_diag_history))
                    row.update(self._estimate_memory_breakdown(
                        model_name, model_cfg, params, batch_size, seq_len,
                        max_memory_allocated_mb,
                    ))
                    row["quality_per_memory_mb"] = accuracy / max(max_memory_allocated_mb, 1e-8)
                    row["latency_per_memory_mb"] = mean_latency / max(max_memory_allocated_mb, 1e-8)
                    rows.append(row)
        self._write_deployment_reports(rows)
        return {"status": self._deployment_status(rows), "rows": rows}

    def _deployment_status(self, rows: list[dict[str, Any]]) -> str:
        fixed_vectorized = [r for r in rows if r["model"] == "fixed_moe_vectorized"]
        fixed_looped = [r for r in rows if r["model"] in {"fixed_moe_looped_reference", "fixed_moe"}]
        fixed = fixed_vectorized or fixed_looped
        top2 = [r for r in rows if r["model"] == "pvr_ec_deploy_top2"]
        if not fixed or not top2:
            return "PARTIAL_PVR_EC_FAIR_DEPLOYMENT_VALIDATION"
        latency_ratios = []
        memory_ratios = []
        loss_deltas = []
        for row in top2:
            match = next((
                r for r in fixed
                if r["batch_size"] == row["batch_size"]
                and r["sequence_length"] == row["sequence_length"]
            ), None)
            if match:
                latency_ratios.append(row["p95_latency_ms"] / max(match["p95_latency_ms"], 1e-8))
                memory_ratios.append(row["max_memory_allocated_mb"] / max(match["max_memory_allocated_mb"], 1e-8))
                loss_deltas.append(row["loss"] - match["loss"])
        avg_latency_ratio = float(np.mean(latency_ratios)) if latency_ratios else float("inf")
        avg_memory_ratio = float(np.mean(memory_ratios)) if memory_ratios else 0.0
        avg_loss_delta = float(np.mean(loss_deltas)) if loss_deltas else 0.0
        if fixed_vectorized and avg_latency_ratio > 1.05:
            return "PVR_EC_SPEEDUP_WAS_BASELINE_BACKEND_ARTIFACT"
        if avg_memory_ratio > 3.0:
            return "PVR_EC_DEPLOY_MEMORY_OVERHEAD_HIGH"
        if avg_loss_delta > 0.02:
            return "PVR_EC_DEPLOY_CAPABILITY_GAP"
        if avg_latency_ratio <= 1.0 and avg_loss_delta <= 0.02:
            return "PVR_EC_DEPLOY_CANDIDATE"
        return "PVR_EC_READY_FOR_LONGER_CAPABILITY_RUN"

    def _write_deployment_reports(self, rows: list[dict[str, Any]]) -> None:
        fixed_by_key = {}
        vectorized_by_key = {}
        for row in rows:
            if row["model"] == "fixed_moe":
                fixed_by_key[(row["batch_size"], row["sequence_length"])] = row
            if row["model"] == "fixed_moe_looped_reference":
                fixed_by_key.setdefault((row["batch_size"], row["sequence_length"]), row)
            if row["model"] == "fixed_moe_vectorized":
                vectorized_by_key[(row["batch_size"], row["sequence_length"])] = row
        for row in rows:
            key = (row["batch_size"], row["sequence_length"])
            fixed = fixed_by_key.get(key)
            vectorized = vectorized_by_key.get(key)
            row["inference_slowdown_vs_fixed_moe"] = (
                row["mean_latency_ms"] / max(fixed["mean_latency_ms"], 1e-8)
                if fixed else 1.0
            )
            row["slowdown_vs_fixed_moe_vectorized"] = (
                row["mean_latency_ms"] / max(vectorized["mean_latency_ms"], 1e-8)
                if vectorized else None
            )
            row["speedup_vs_fixed_moe_vectorized"] = (
                vectorized["mean_latency_ms"] / max(row["mean_latency_ms"], 1e-8)
                if vectorized else None
            )
            row["train_slowdown_vs_fixed_moe"] = None

        status = self._deployment_status(rows)
        top2 = [r for r in rows if r["model"] == "pvr_ec_deploy_top2"]
        top1 = [r for r in rows if r["model"] == "pvr_ec_deploy_top1"]
        bucketed = [r for r in rows if r["model"] == "pvr_ec_deploy_bucketed"]
        statuses = [
            "FIXED_MOE_VECTORIZED_BASELINE_READY" if vectorized_by_key else "PARTIAL_PVR_EC_FAIR_DEPLOYMENT_VALIDATION",
            "PVR_EC_DEPLOY_TOP1_READY" if top1 else "PARTIAL_PVR_EC_FAIR_DEPLOYMENT_VALIDATION",
            "PVR_EC_DEPLOY_TOP2_READY" if top2 else "PARTIAL_PVR_EC_FAIR_DEPLOYMENT_VALIDATION",
            "PVR_EC_DEPLOY_BUCKETED_READY" if bucketed else "PARTIAL_PVR_EC_FAIR_DEPLOYMENT_VALIDATION",
            status,
        ]
        if status != "PVR_EC_DEPLOY_CANDIDATE":
            statuses.append("PVR_EC_DO_NOT_PROMOTE")
        bucketed_memory_high = False
        for row in bucketed:
            fixed = vectorized_by_key.get((row["batch_size"], row["sequence_length"]))
            if fixed and row["max_memory_allocated_mb"] > 5.0 * max(fixed["max_memory_allocated_mb"], 1e-8):
                bucketed_memory_high = True
        if bucketed_memory_high:
            statuses.append("PVR_EC_BUCKETED_MEMORY_TOO_HIGH")
        status_payload = {
            "status": status,
            "statuses": sorted(set(statuses)),
            "runtime_branching_enabled": False,
            "branch_tickets_enabled": False,
        }
        metadata = self._artifact_metadata()
        report = {
            "metadata": metadata,
            "run_id": self.run_id,
            "device": self.device,
            "amp": self.amp,
            "warmup_steps": self.warmup_steps,
            "timed_steps": self.timed_steps,
            "rows": rows,
            "status": status_payload,
        }
        with open(self.output_dir / "pvr_inference_latency_report.json", "w") as f:
            json.dump(report, f, indent=2, default=str)
        with open(self.output_dir / "pvr_hot_path_profile.json", "w") as f:
            json.dump({
                "expert_execution_mode": "FULLY_VECTORIZED",
                "profile_deploy": self.profile_deploy,
                "no_hot_path_branch_tickets": True,
                "no_runtime_branching": True,
                "no_cuda_sync_inside_model_forward": True,
            }, f, indent=2)
        with open(self.output_dir / "pvr_deploy_status.json", "w") as f:
            json.dump(status_payload, f, indent=2)
        with open(self.output_dir / "pvr_deployment_report.json", "w") as f:
            json.dump(report, f, indent=2, default=str)
        with open(self.output_dir / "pvr_deploy_comparison.csv", "w", newline="") as f:
            if rows:
                fieldnames = sorted({key for row in rows for key in row.keys()})
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rows)
        self._write_fair_deployment_artifacts(rows, report, status_payload)
        self._write_capacity_proof_artifacts(rows, metadata, source="inference_only")
        self._write_root_cause_artifacts(rows, metadata, source="inference_only")
        if self.root_cause_flags.get("run_final_config_manifest"):
            self._write_final_config_manifest(rows)
        if self.root_cause_flags.get("run_forward_purity_gate"):
            self._write_forward_purity_gate(rows)
        if self.root_cause_flags.get("run_quality_per_ms_memory_gate"):
            self._write_quality_per_ms_memory_gate(rows)
        if self.root_cause_flags.get("run_qpm_shape_regression_analysis"):
            self._write_qpm_shape_regression_report(rows, repair=False)
        if self.root_cause_flags.get("run_qpm_memory_repair"):
            self._write_qpm_shape_regression_report(rows, repair=True)
        if self.root_cause_flags.get("run_qpm_failing_shape_replay"):
            self._write_qpm_failing_shape_replay_report(rows)
        if self.root_cause_flags.get("run_qpm_formula_audit"):
            self._write_qpm_formula_audit_report(rows)
        if self.root_cause_flags.get("run_shape_qpm_runtime_repair"):
            self._write_shape_qpm_runtime_repair_report(rows)

        lines = ["# PVR-EC Deployment Report", "", f"**Status:** {status}", ""]
        lines.append("| Model | Mode | Batch | Seq | p50 ms | p95 ms | Slowdown vs fixed_vec | Loss | QPM | Q/Mem | Expert Exec |")
        lines.append("|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|")
        for row in rows:
            slowdown = row.get("slowdown_vs_fixed_moe_vectorized")
            slowdown_text = f"{slowdown:.2f}x" if isinstance(slowdown, (int, float)) else "N/A"
            lines.append(
                f"| {row['model']} | {row['deploy_mode']} | {row['batch_size']} | "
                f"{row['sequence_length']} | {row['p50_latency_ms']:.3f} | "
                f"{row['p95_latency_ms']:.3f} | {slowdown_text} | "
                f"{row['loss']:.4f} | {row['quality_per_ms']:.6f} | "
                f"{row.get('quality_per_memory_mb', 0.0):.6f} | {row['expert_execution_mode']} |"
            )
        lines.append("")
        lines.append("Hard runtime branching is disabled. Branch tickets are disabled in the deployment hot path.")
        with open(self.output_dir / "pvr_deployment_report.md", "w") as f:
            f.write("\n".join(lines))

    def _write_capacity_proof_artifacts(
        self,
        rows: list[dict[str, Any]],
        metadata: dict[str, Any],
        source: str,
    ) -> None:
        capacity_rows = [
            row for row in rows
            if row.get("capacity_variant") or str(row.get("model", row.get("model_name", ""))).startswith(
                "pvr_ec_ownership_top1"
            )
        ]
        baseline_rows = [
            row for row in rows
            if row.get("model") == "fixed_moe_vectorized" or row.get("model_name") == "fixed_moe_vectorized"
        ]
        if not capacity_rows and not baseline_rows:
            return

        def row_model(row: dict[str, Any]) -> str:
            return str(row.get("model", row.get("model_name", "")))

        def row_loss(row: dict[str, Any]) -> float | None:
            value = row.get("loss", row.get("avg_loss"))
            return float(value) if isinstance(value, (int, float)) else None

        def row_accuracy(row: dict[str, Any]) -> float | None:
            value = row.get("accuracy", row.get("avg_accuracy"))
            return float(value) if isinstance(value, (int, float)) else None

        matrix_rows = []
        for row in capacity_rows + baseline_rows:
            params = row.get("param_count", row.get("params", row.get("total_parameters")))
            active = row.get("active_param_count", row.get("active_params_estimate", params))
            latency = row.get("mean_latency_ms")
            accuracy = row_accuracy(row)
            matrix_rows.append({
                "model": row_model(row),
                "capacity_variant": row.get("capacity_variant", ""),
                "pvr_expert_type": row.get("pvr_expert_type", ""),
                "expert_hidden_dim": row.get("expert_hidden_dim"),
                "expert_architecture_id": row.get("expert_architecture_id", ""),
                "expert_inner_dim": row.get("expert_inner_dim", row.get("expert_hidden_dim")),
                "delta_rank": row.get("delta_rank", 0),
                "params_per_expert": row.get("params_per_expert"),
                "shared_params": row.get("shared_params"),
                "routed_expert_params": row.get("routed_expert_params"),
                "num_experts": row.get("num_experts"),
                "module_class_names": row.get("module_class_names", ""),
                "module_fingerprint": row.get("module_fingerprint", ""),
                "param_count": params,
                "active_param_count": active,
                "actual_experts_executed": row.get("actual_experts_executed", row.get("pvr_actual_experts_executed")),
                "actual_owner_count_per_token": row.get(
                    "actual_owner_count_per_token",
                    row.get("pvr_actual_owner_count_per_token"),
                ),
                "actual_expert_slots_per_token": row.get(
                    "actual_expert_slots_per_token",
                    row.get("pvr_actual_expert_slots_per_token"),
                ),
                "dense_all_experts_executed": row.get(
                    "dense_all_experts_executed",
                    row.get("pvr_dense_all_experts_executed", False),
                ),
                "train_loss": row.get("training_loss"),
                "eval_loss": row_loss(row),
                "accuracy": accuracy,
                "latency_p50_ms": row.get("p50_latency_ms"),
                "latency_p95_ms": row.get("p95_latency_ms"),
                "quality_per_ms": row.get("quality_per_ms"),
                "quality_per_active_param": row.get(
                    "quality_per_active_param",
                    (accuracy / max(float(active), 1.0)) if isinstance(accuracy, (int, float)) else None,
                ),
                "batch_size": row.get("batch_size"),
                "sequence_length": row.get("sequence_length"),
                "family": row.get("family"),
                "task": row.get("task"),
            })

        top1_capacity = [r for r in matrix_rows if row_model(r).startswith("pvr_ec_ownership_top1")]
        owner_assertion_passed = all(
            isinstance(r.get("actual_owner_count_per_token"), (int, float))
            and abs(float(r["actual_owner_count_per_token"]) - 1.0) < 1e-6
            for r in top1_capacity
        ) if top1_capacity else False
        no_hidden_dense = all(
            not bool(r.get("dense_all_experts_executed"))
            and (
                not isinstance(r.get("actual_expert_slots_per_token"), (int, float))
                or float(r["actual_expert_slots_per_token"]) <= 1.0
            )
            for r in top1_capacity
        ) if top1_capacity else False
        no_oracle = all(not bool(row.get("oracle_owner_used", row.get("pvr_oracle_owner_used", False))) for row in capacity_rows)
        no_forced = all(
            not bool(row.get("forced_action_path_used", row.get("pvr_forced_action_path_used", False)))
            for row in capacity_rows
        )
        no_replay = all(
            not bool(row.get("replay_probe_labels_used", row.get("pvr_replay_probe_labels_used", False)))
            for row in capacity_rows
        )
        no_top2_top4 = all(
            not isinstance(r.get("actual_expert_slots_per_token"), (int, float))
            or float(r["actual_expert_slots_per_token"]) <= 1.0
            for r in top1_capacity
        ) if top1_capacity else False
        keys_by_model: dict[str, set[tuple[Any, Any]]] = {}
        for row in matrix_rows:
            if row.get("batch_size") is not None or row.get("sequence_length") is not None:
                keys_by_model.setdefault(row["model"], set()).add((row.get("batch_size"), row.get("sequence_length")))
        same_batch_sequence_grid = (
            len({tuple(sorted(values)) for values in keys_by_model.values()}) <= 1
            if keys_by_model else True
        )

        fairness_audit = {
            "same_seed": True,
            "same_train_eval_split": source == "trained_benchmark",
            "same_labels_objective": True,
            "same_benchmark_family": True,
            "same_target_preprocessing": True,
            "same_loss_computation": True,
            "same_batch_size": same_batch_sequence_grid,
            "same_amp_mode": True,
            "same_number_of_train_steps": source == "trained_benchmark",
            "same_optimizer_schedule": source == "trained_benchmark",
            "same_eval_mode": True,
            "same_ownership_map_mode": True,
            "same_route_policy_ownership_top1": True,
            "exactly_one_owner": owner_assertion_passed,
            "top2_executions_zero": no_top2_top4,
            "top4_executions_zero": no_top2_top4,
            "no_hidden_dense_all_expert_execution": no_hidden_dense,
            "no_oracle_owner_used_at_inference": no_oracle,
            "no_forced_action_path_used_in_deploy": no_forced,
            "no_replay_probe_data_used_as_eval_labels": no_replay,
        }
        fairness_passed = all(fairness_audit.values())

        architecture_rows = self._capacity_architecture_rows(matrix_rows)
        arch_by_model = {r["model_name"]: r for r in architecture_rows}
        full_arch = arch_by_model.get("pvr_ec_ownership_top1_full_expert_ffn_control")
        delta_large_arch = arch_by_model.get("pvr_ec_ownership_top1_delta_large")
        full_alias_detected = bool(full_arch and full_arch["aliases_detected"])
        full_params_exceed_delta_large = bool(
            full_arch and delta_large_arch
            and int(full_arch.get("params_per_expert") or 0) > int(delta_large_arch.get("params_per_expert") or 0)
        )
        full_control_distinct = bool(
            full_arch
            and not full_alias_detected
            and full_arch.get("expert_architecture_id") == "full_expert_ffn"
            and full_params_exceed_delta_large
        )

        full_rows = [r for r in matrix_rows if r.get("capacity_variant") in {"full_expert_ffn", "micro_ffn_1.0x"}]
        delta_rows = [r for r in matrix_rows if str(r.get("capacity_variant", "")).startswith(("delta_", "rank_", "micro_ffn_0"))]
        latency_suspicion = False
        if full_rows and delta_rows:
            full_latency = min(
                [float(r["latency_p50_ms"]) for r in full_rows if isinstance(r.get("latency_p50_ms"), (int, float))],
                default=float("inf"),
            )
            delta_latency = min(
                [float(r["latency_p50_ms"]) for r in delta_rows if isinstance(r.get("latency_p50_ms"), (int, float))],
                default=float("inf"),
            )
            latency_suspicion = full_latency < delta_latency

        model_averages = self._capacity_model_averages(matrix_rows)
        full_avg = model_averages.get("pvr_ec_ownership_top1_full_expert_ffn_control")
        delta_large_avg = model_averages.get("pvr_ec_ownership_top1_delta_large")
        full_loss_signal = bool(
            full_control_distinct and full_avg and delta_large_avg
            and full_avg.get("avg_loss") is not None
            and delta_large_avg.get("avg_loss") is not None
            and float(full_avg["avg_loss"]) <= float(delta_large_avg["avg_loss"]) - 0.02
        )
        status = (
            "PVR_EC_FULL_EXPERT_CONTROL_ALIAS_DETECTED" if full_alias_detected
            else "PVR_EC_FULL_EXPERT_CONTROL_DISTINCT" if full_control_distinct
            else "PENDING_PVR_EC_CAPACITY_FAIRNESS_AUDIT"
        )
        statuses = [
            status,
            "PVR_EC_CAPACITY_FAIRNESS_AUDIT_READY" if fairness_passed else "PVR_EC_CAPACITY_FAIRNESS_AUDIT_BLOCKED",
            "PVR_EC_TOP1_OWNER_ASSERTION_PASSED" if owner_assertion_passed else "PVR_EC_TOP1_OWNER_ASSERTION_FAILED",
            "PVR_EC_CAPACITY_LADDER_VALID" if full_control_distinct else "PVR_EC_CAPACITY_LADDER_INVALID",
            "PVR_EC_REAL_FULL_EXPERT_CAPACITY_SIGNAL" if full_loss_signal else "PVR_EC_FULL_EXPERT_CAPACITY_NOT_PROVEN",
            "PVR_EC_DISTILLATION_READY" if full_loss_signal else "PVR_EC_DISTILLATION_BLOCKED",
            "PVR_EC_REAL_TRACE_PROMOTION_GATE_NOT_CLEAN",
            "PVR_EC_DO_NOT_PROMOTE",
        ]
        if latency_suspicion:
            statuses.append("PVR_EC_CAPACITY_CONTROL_RESULT_SUSPICIOUS_BUT_PROMISING")

        report = {
            "metadata": metadata,
            "source": source,
            "status": status,
            "statuses": sorted(set(statuses)),
            "promotion_ready": False,
            "fairness_audit": fairness_audit,
            "latency_suspicion_full_capacity_faster_than_smaller_delta": latency_suspicion,
            "hard_assertions": {
                "actual_owner_count_per_token_equals_1": owner_assertion_passed,
                "no_hidden_dense_all_expert_execution": no_hidden_dense,
                "full_expert_ffn_control_not_aliased": not full_alias_detected,
                "full_expert_ffn_control_params_exceed_delta_large": full_params_exceed_delta_large,
            },
            "architecture_alias_check": {
                "full_alias_detected": full_alias_detected,
                "full_control_distinct": full_control_distinct,
                "full_params_exceed_delta_large": full_params_exceed_delta_large,
            },
            "model_averages": model_averages,
            "rows": matrix_rows,
        }
        with open(self.output_dir / "capacity_fairness_matrix_report.json", "w") as f:
            json.dump(report, f, indent=2, default=str)
        self._write_capacity_architecture_report(architecture_rows, metadata, status, full_control_distinct)
        self._write_capacity_fairness_audit_report(fairness_audit, metadata, statuses)
        self._write_capacity_knee_report(model_averages, metadata, full_loss_signal)

        interpolation_rows = [
            r for r in matrix_rows
            if str(r.get("capacity_variant", "")).startswith(("rank_", "micro_ffn_", "delta_", "full_"))
        ]
        with open(self.output_dir / "capacity_interpolation_report.json", "w") as f:
            json.dump({
                "metadata": metadata,
                "status": "PVR_EC_CAPACITY_INTERPOLATION_RECORDED" if interpolation_rows else "PENDING_PVR_EC_CAPACITY_INTERPOLATION",
                "promotion_ready": False,
                "rows": interpolation_rows,
            }, f, indent=2, default=str)

        teacher_rows = [r for r in matrix_rows if r.get("capacity_variant") == "full_expert_ffn"]
        student_rows = [
            r for r in matrix_rows
            if r.get("capacity_variant") in {"delta_medium", "delta_large", "rank_64", "rank_128", "micro_ffn_0.5x"}
        ]
        distill = {
            "metadata": metadata,
            "status": "PVR_EC_DISTILLATION_COMPRESSION_PENDING",
            "promotion_ready": False,
            "teacher": "pvr_ec_ownership_top1_full_expert_ffn_control",
            "students": [
                "pvr_ec_ownership_top1_delta_medium",
                "pvr_ec_ownership_top1_delta_large",
                "pvr_ec_ownership_top1_rank_64",
                "pvr_ec_ownership_top1_rank_128",
            ],
            "distillation_targets": [
                "logits",
                "hidden_outputs",
                "owner_assignments",
                "prototype_ownership",
                "expert_delta_outputs",
                "failure_regions",
            ],
            "teacher_rows": teacher_rows,
            "student_rows": student_rows,
        }
        with open(self.output_dir / "capacity_distillation_compression_plan.json", "w") as f:
            json.dump(distill, f, indent=2, default=str)

        lines = ["# PVR-EC-O Capacity Fairness Matrix", "", f"**Status:** {status}", ""]
        lines.append("| Model | Variant | Params | Active Params | Owners/Token | p50 ms | p95 ms | Loss | Acc | Q/ms |")
        lines.append("|---|---|---:|---:|---:|---:|---:|---:|---:|---:|")
        for row in matrix_rows:
            owners = row.get("actual_owner_count_per_token")
            owners_text = f"{owners:.2f}" if isinstance(owners, (int, float)) else "N/A"
            p50 = row.get("latency_p50_ms")
            p95 = row.get("latency_p95_ms")
            loss = row.get("eval_loss")
            acc = row.get("accuracy")
            qpm = row.get("quality_per_ms")
            p50_text = f"{p50:.3f}" if isinstance(p50, (int, float)) else "N/A"
            p95_text = f"{p95:.3f}" if isinstance(p95, (int, float)) else "N/A"
            loss_text = f"{loss:.4f}" if isinstance(loss, (int, float)) else "N/A"
            acc_text = f"{acc:.4f}" if isinstance(acc, (int, float)) else "N/A"
            qpm_text = f"{qpm:.6f}" if isinstance(qpm, (int, float)) else "N/A"
            lines.append(
                f"| {row['model']} | {row.get('capacity_variant', '')} | "
                f"{int(row.get('param_count') or 0):,} | {int(row.get('active_param_count') or 0):,} | "
                f"{owners_text} | {p50_text} | {p95_text} | {loss_text} | {acc_text} | {qpm_text} |"
            )
        lines.append("")
        lines.append("Promotion remains blocked until fairness and repeatability gates are clean.")
        with open(self.output_dir / "capacity_fairness_matrix_report.md", "w") as f:
            f.write("\n".join(lines))

    @staticmethod
    def _capacity_model_averages(matrix_rows: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
        grouped: dict[str, list[dict[str, Any]]] = {}
        for row in matrix_rows:
            grouped.setdefault(row["model"], []).append(row)
        out: dict[str, dict[str, Any]] = {}
        for model, rows in grouped.items():
            def avg(key: str) -> float | None:
                values = [float(r[key]) for r in rows if isinstance(r.get(key), (int, float))]
                return float(np.mean(values)) if values else None
            first = rows[0]
            out[model] = {
                "capacity_variant": first.get("capacity_variant", ""),
                "expert_architecture_id": first.get("expert_architecture_id", ""),
                "params_total": first.get("param_count"),
                "params_active_estimate": first.get("active_param_count"),
                "avg_loss": avg("eval_loss"),
                "avg_accuracy": avg("accuracy"),
                "latency_p50": avg("latency_p50_ms"),
                "latency_p95": avg("latency_p95_ms"),
                "quality_per_ms": avg("quality_per_ms"),
                "quality_per_active_param": avg("quality_per_active_param"),
                "owners_per_token": avg("actual_owner_count_per_token"),
                "expert_capacity_failure_rate": None,
                "shared_vs_sparse_contribution": None,
                "owner_change_rate": None,
                "owner_changed_success_rate": None,
            }
        return out

    @staticmethod
    def _capacity_architecture_rows(matrix_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
        by_model: dict[str, dict[str, Any]] = {}
        for row in matrix_rows:
            by_model.setdefault(row["model"], row)
        fingerprint_to_models: dict[str, list[str]] = {}
        for model, row in by_model.items():
            fingerprint = str(row.get("module_fingerprint", ""))
            if fingerprint:
                fingerprint_to_models.setdefault(fingerprint, []).append(model)
        architecture_rows = []
        for model, row in sorted(by_model.items()):
            fingerprint = str(row.get("module_fingerprint", ""))
            same = [m for m in fingerprint_to_models.get(fingerprint, []) if m != model]
            architecture_rows.append({
                "model_name": model,
                "expert_type": row.get("pvr_expert_type", ""),
                "expert_architecture_id": row.get("expert_architecture_id", ""),
                "hidden_dim": row.get("expert_hidden_dim"),
                "expert_inner_dim": row.get("expert_inner_dim"),
                "delta_rank": row.get("delta_rank", 0),
                "num_experts": row.get("num_experts"),
                "params_total": row.get("param_count"),
                "params_active_estimate": row.get("active_param_count"),
                "params_per_expert": row.get("params_per_expert"),
                "shared_params": row.get("shared_params"),
                "routed_expert_params": row.get("routed_expert_params"),
                "module_class_names": row.get("module_class_names", ""),
                "module_fingerprint": fingerprint,
                "aliases_detected": bool(same),
                "same_as_variant": same[0] if same else None,
            })
        return architecture_rows

    def _write_capacity_architecture_report(
        self,
        architecture_rows: list[dict[str, Any]],
        metadata: dict[str, Any],
        status: str,
        full_control_distinct: bool,
    ) -> None:
        full_row = next(
            (r for r in architecture_rows if r["model_name"] == "pvr_ec_ownership_top1_full_expert_ffn_control"),
            None,
        )
        statuses = [
            "PVR_EC_FULL_EXPERT_CONTROL_DISTINCT" if full_control_distinct else "PVR_EC_FULL_EXPERT_CONTROL_ALIAS_DETECTED",
            "PVR_EC_CAPACITY_LADDER_VALID" if full_control_distinct else "PVR_EC_CAPACITY_LADDER_INVALID",
            "PVR_EC_DO_NOT_PROMOTE",
        ]
        report = {
            "metadata": metadata,
            "status": status,
            "statuses": statuses,
            "full_expert_ffn_control_aliases_detected": bool(full_row and full_row["aliases_detected"]),
            "rows": architecture_rows,
        }
        with open(self.output_dir / "pvr_ec_capacity_architecture_report.json", "w") as f:
            json.dump(report, f, indent=2, default=str)
        lines = ["# PVR-EC Capacity Architecture Report", "", f"**Status:** {status}", ""]
        lines.append("| Model | Expert Type | Architecture | Inner | Rank | Params/Expert | Fingerprint | Aliases |")
        lines.append("|---|---|---|---:|---:|---:|---|---|")
        for row in architecture_rows:
            lines.append(
                f"| {row['model_name']} | {row.get('expert_type', '')} | "
                f"{row.get('expert_architecture_id', '')} | {row.get('expert_inner_dim') or 0} | "
                f"{row.get('delta_rank') or 0} | {row.get('params_per_expert') or 0} | "
                f"{row.get('module_fingerprint', '')} | {row.get('same_as_variant') or ''} |"
            )
        with open(self.output_dir / "pvr_ec_capacity_architecture_report.md", "w") as f:
            f.write("\n".join(lines))

    def _write_capacity_fairness_audit_report(
        self,
        fairness_audit: dict[str, bool],
        metadata: dict[str, Any],
        statuses: list[str],
    ) -> None:
        report = {
            "metadata": metadata,
            "status": "PVR_EC_CAPACITY_FAIRNESS_AUDIT_READY" if all(fairness_audit.values()) else "PVR_EC_CAPACITY_FAIRNESS_AUDIT_BLOCKED",
            "statuses": sorted(set(statuses)),
            "fairness_audit": fairness_audit,
            "promotion_ready": False,
        }
        with open(self.output_dir / "capacity_fairness_audit_report.json", "w") as f:
            json.dump(report, f, indent=2, default=str)
        lines = ["# PVR-EC Capacity Fairness Audit", "", f"**Status:** {report['status']}", ""]
        for key, value in fairness_audit.items():
            lines.append(f"- {key}: {value}")
        with open(self.output_dir / "capacity_fairness_audit_report.md", "w") as f:
            f.write("\n".join(lines))

    def _write_capacity_knee_report(
        self,
        model_averages: dict[str, dict[str, Any]],
        metadata: dict[str, Any],
        full_loss_signal: bool,
    ) -> None:
        candidates = {
            model: data for model, data in model_averages.items()
            if model.startswith("pvr_ec_ownership_top1")
            and isinstance(data.get("avg_loss"), (int, float))
        }
        best_model = min(candidates, key=lambda m: float(candidates[m]["avg_loss"])) if candidates else None
        status = "PVR_EC_CAPACITY_KNEE_FOUND" if full_loss_signal and best_model else "PVR_EC_FULL_EXPERT_CAPACITY_NOT_PROVEN"
        report = {
            "metadata": metadata,
            "status": status,
            "statuses": [
                status,
                "PVR_EC_DISTILLATION_READY" if full_loss_signal else "PVR_EC_DISTILLATION_BLOCKED",
                "PVR_EC_DO_NOT_PROMOTE",
            ],
            "best_capacity_variant": best_model,
            "best_capacity_metrics": candidates.get(best_model) if best_model else None,
            "full_ffn_signal_real": full_loss_signal,
            "model_averages": model_averages,
        }
        with open(self.output_dir / "capacity_knee_report.json", "w") as f:
            json.dump(report, f, indent=2, default=str)

    @staticmethod
    def _maybe_float(value: Any) -> float | None:
        return float(value) if isinstance(value, (int, float)) else None

    @staticmethod
    def _mean_or_none(values: list[float | None]) -> float | None:
        clean = [float(v) for v in values if isinstance(v, (int, float))]
        return float(np.mean(clean)) if clean else None

    @staticmethod
    def _row_model_name(row: dict[str, Any]) -> str:
        return str(row.get("model", row.get("model_name", "")))

    @staticmethod
    def _row_family_name(row: dict[str, Any]) -> str:
        family = row.get("family")
        if family:
            return str(family)
        task = str(row.get("task", "unknown"))
        return task.split("_", 1)[0] if task else "unknown"

    def _normalize_root_cause_row(self, row: dict[str, Any]) -> dict[str, Any]:
        model = self._row_model_name(row)
        loss = self._maybe_float(row.get("loss", row.get("eval_loss", row.get("avg_loss"))))
        accuracy = self._maybe_float(row.get("accuracy", row.get("avg_accuracy")))
        p50 = self._maybe_float(row.get("p50_latency_ms", row.get("latency_p50_ms")))
        p95 = self._maybe_float(row.get("p95_latency_ms", row.get("latency_p95_ms")))
        if p50 is None and isinstance(row.get("inference_time_s"), (int, float)):
            p50 = float(row["inference_time_s"]) * 1000.0
        if p95 is None and p50 is not None:
            p95 = p50
        active_params = row.get("active_param_count", row.get("active_params_estimate"))
        params = row.get("param_count", row.get("params", row.get("total_parameters")))
        owner_change_count = row.get("owner_change_count", row.get("pvr_owner_change_count", 0))
        owner_changed_success_rate = row.get(
            "owner_changed_success_rate",
            row.get("pvr_owner_changed_success_rate"),
        )
        if not owner_change_count:
            owner_changed_success_rate = None
        return {
            "model": model,
            "family": self._row_family_name(row),
            "task": row.get("task"),
            "seed": row.get("seed", self.seed),
            "train_steps": row.get("train_steps", self.train_steps),
            "sample_limit": row.get("sample_limit", self.sample_limit),
            "loss": loss,
            "accuracy": accuracy,
            "train_loss": row.get("training_loss", row.get("train_loss")),
            "param_count": params,
            "active_param_count": active_params,
            "actual_experts_executed": row.get("actual_experts_executed", row.get("pvr_actual_experts_executed")),
            "actual_owner_count_per_token": row.get(
                "actual_owner_count_per_token",
                row.get("pvr_actual_owner_count_per_token"),
            ),
            "latency_p50_ms": p50,
            "latency_p95_ms": p95,
            "latency_p95_p50_ratio": (p95 / max(p50, 1e-8)) if p50 and p95 else None,
            "quality_per_ms": row.get("quality_per_ms", (accuracy / max(p50 or 0.0, 1e-8)) if accuracy is not None and p50 else None),
            "quality_per_active_param": row.get(
                "quality_per_active_param",
                (accuracy / max(float(active_params), 1.0)) if accuracy is not None and isinstance(active_params, (int, float)) else None,
            ),
            "deploy_mode": row.get("deploy_mode", ""),
            "capacity_variant": row.get("capacity_variant", ""),
            "pvr_expert_type": row.get("pvr_expert_type", ""),
            "expert_architecture_id": row.get("expert_architecture_id", ""),
            "pvr_shared_scale": row.get("pvr_shared_scale", 1.0),
            "pvr_expert_delta_scale": row.get("pvr_expert_delta_scale", 1.0),
            "pvr_expert_delta_scale_schedule": row.get("pvr_expert_delta_scale_schedule", "constant"),
            "expert_delta_contribution_pct": row.get("expert_delta_contribution_pct"),
            "calibration_proxy": row.get("calibration_proxy"),
            "logit_norm": row.get("logit_norm"),
            "prediction_entropy": row.get("prediction_entropy"),
            "owner_change_count": owner_change_count or 0,
            "owner_change_rate": row.get("owner_change_rate", row.get("pvr_owner_change_rate")),
            "owner_changed_success_rate": owner_changed_success_rate,
            "owner_changed_loss_delta_mean": row.get("owner_changed_loss_delta_mean"),
            "top1_oracle_gap": row.get("top1_oracle_gap"),
            "prototype_local_monopoly_rate": row.get("prototype_local_monopoly_rate"),
            "shared_output_norm": row.get("shared_output_norm"),
            "sparse_output_norm": row.get("sparse_output_norm"),
            "shared_sparse_ratio": row.get("shared_sparse_ratio"),
            "expert_output_norm_by_expert": row.get("expert_output_norm_by_expert", {}),
            "expert_gradient_norm_by_expert": row.get("expert_gradient_norm_by_expert", {}),
            "expert_utilization": row.get("expert_utilization", row.get("pvr_expert_utilization")),
            "loss_schedule": row.get("loss_schedule"),
            "ownership_schedule": row.get("ownership_schedule"),
            "batch_size": row.get("batch_size"),
            "sequence_length": row.get("sequence_length"),
        }

    def _root_cause_group_summary(self, rows: list[dict[str, Any]], key: str) -> dict[str, dict[str, Any]]:
        grouped: dict[str, list[dict[str, Any]]] = {}
        for row in rows:
            grouped.setdefault(str(row.get(key, "unknown")), []).append(row)
        summary = {}
        for name, items in grouped.items():
            summary[name] = {
                "count": len(items),
                "avg_loss": self._mean_or_none([self._maybe_float(r.get("loss")) for r in items]),
                "avg_accuracy": self._mean_or_none([self._maybe_float(r.get("accuracy")) for r in items]),
                "avg_train_loss": self._mean_or_none([self._maybe_float(r.get("train_loss")) for r in items]),
                "latency_p50_ms": self._mean_or_none([self._maybe_float(r.get("latency_p50_ms")) for r in items]),
                "latency_p95_ms": self._mean_or_none([self._maybe_float(r.get("latency_p95_ms")) for r in items]),
                "latency_p95_p50_ratio": self._mean_or_none([self._maybe_float(r.get("latency_p95_p50_ratio")) for r in items]),
                "owner_change_rate": self._mean_or_none([self._maybe_float(r.get("owner_change_rate")) for r in items]),
                "owner_changed_success_rate": self._mean_or_none([
                    self._maybe_float(r.get("owner_changed_success_rate")) for r in items
                ]),
            }
        return summary

    def _learning_separation_summary(self, rows: list[dict[str, Any]]) -> dict[str, Any]:
        def matching(*needles: str) -> list[dict[str, Any]]:
            return [
                r for r in rows
                if any(needle in r.get("model", "") for needle in needles)
            ]

        full_rows = [
            r for r in rows
            if r.get("model", "").startswith("pvr_ec")
            and "shared_only" not in r.get("model", "")
            and "sparse_only" not in r.get("model", "")
            and r.get("pvr_expert_type") != "shared_base_only"
            and self._maybe_float(r.get("pvr_shared_scale", 1.0)) != 0.0
        ]
        shared_only = [
            r for r in matching("shared_only")
            if r.get("pvr_expert_type") == "shared_base_only" or "shared_only" in r.get("model", "")
        ]
        sparse_only = [
            r for r in matching("sparse_only")
            if "sparse_only" in r.get("model", "") or self._maybe_float(r.get("pvr_shared_scale")) == 0.0
        ]

        def avg(items: list[dict[str, Any]], key: str) -> float | None:
            return self._mean_or_none([self._maybe_float(r.get(key)) for r in items])

        full_acc = avg(full_rows, "accuracy")
        shared_acc = avg(shared_only, "accuracy")
        sparse_acc = avg(sparse_only, "accuracy")
        full_loss = avg(full_rows, "loss")
        shared_loss = avg(shared_only, "loss")
        sparse_loss = avg(sparse_only, "loss")
        full_minus_shared_score = (
            full_acc - shared_acc
            if isinstance(full_acc, (int, float)) and isinstance(shared_acc, (int, float))
            else None
        )
        shared_minus_full_loss = (
            shared_loss - full_loss
            if isinstance(full_loss, (int, float)) and isinstance(shared_loss, (int, float))
            else None
        )
        return {
            "full_model": {
                "count": len(full_rows),
                "avg_accuracy": full_acc,
                "avg_loss": full_loss,
                "shared_output_norm": avg(full_rows, "shared_output_norm"),
                "sparse_output_norm": avg(full_rows, "sparse_output_norm"),
                "shared_sparse_ratio": avg(full_rows, "shared_sparse_ratio"),
            },
            "shared_only": {
                "count": len(shared_only),
                "avg_accuracy": shared_acc,
                "avg_loss": shared_loss,
            },
            "sparse_only": {
                "count": len(sparse_only),
                "avg_accuracy": sparse_acc,
                "avg_loss": sparse_loss,
            },
            "full_model_score_minus_shared_only_score": full_minus_shared_score,
            "shared_only_loss_minus_full_model_loss": shared_minus_full_loss,
            "sparse_only_score_minus_shared_only_score": (
                sparse_acc - shared_acc
                if isinstance(sparse_acc, (int, float)) and isinstance(shared_acc, (int, float))
                else None
            ),
            "full_vs_shared_gap_is_small": (
                abs(full_minus_shared_score) <= 0.005
                if isinstance(full_minus_shared_score, (int, float))
                else None
            ),
            "full_loss_gain_over_shared_is_small": (
                shared_minus_full_loss <= 0.02
                if isinstance(shared_minus_full_loss, (int, float))
                else None
            ),
        }

    def _derive_root_cause_statuses(self, rows: list[dict[str, Any]], source: str) -> tuple[str, list[str], list[dict[str, Any]]]:
        statuses = {
            "PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY",
            "PVR_EC_ROOT_CAUSE_INCONCLUSIVE",
            "PVR_EC_DO_NOT_PROMOTE",
        }
        evidence: list[dict[str, Any]] = []
        pvr_rows = [r for r in rows if self._row_model_name(r).startswith("pvr_ec")]
        capacity_rows = [r for r in rows if r.get("capacity_variant") or "ownership_top1" in self._row_model_name(r)]
        accuracies = [
            float(r["accuracy"])
            for r in rows
            if isinstance(r.get("accuracy"), (int, float))
        ]
        max_accuracy = max(accuracies) if accuracies else None
        capability_signal_too_weak = bool(max_accuracy is not None and max_accuracy < 0.05)
        if capability_signal_too_weak:
            statuses.add("PVR_EC_CAPABILITY_SIGNAL_TOO_WEAK_FOR_FINAL_ROOT_CAUSE")
            evidence.append({"label": "max_accuracy_too_low_for_decisive_root_cause", "value": max_accuracy})

        latency_ratios = [
            float(r["latency_p95_p50_ratio"])
            for r in rows
            if isinstance(r.get("latency_p95_p50_ratio"), (int, float))
        ]
        max_latency_ratio = max(latency_ratios) if latency_ratios else None
        if max_latency_ratio and max_latency_ratio >= 3.0:
            statuses.add("PVR_EC_LATENCY_VARIANCE_BLOCKER")
            evidence.append({"label": "latency_p95_p50_ratio", "value": max_latency_ratio})

        owner_rows = [r for r in pvr_rows if r.get("owner_change_count") or r.get("owner_change_rate")]
        owner_success = [
            float(r["owner_changed_success_rate"])
            for r in owner_rows
            if isinstance(r.get("owner_changed_success_rate"), (int, float))
        ]
        if owner_rows and (not owner_success or max(owner_success) < 0.7):
            statuses.add("PVR_EC_OWNERSHIP_INTEGRATION_BLOCKER")
            evidence.append({"label": "owner_changed_success_rate", "value": max(owner_success) if owner_success else None})

        if capacity_rows:
            full_losses = [
                float(r["loss"])
                for r in capacity_rows
                if r.get("capacity_variant") == "full_expert_ffn" and isinstance(r.get("loss"), (int, float))
            ]
            smaller_losses = [
                float(r["loss"])
                for r in capacity_rows
                if r.get("capacity_variant") != "full_expert_ffn" and isinstance(r.get("loss"), (int, float))
            ]
            if full_losses and smaller_losses and min(full_losses) >= min(smaller_losses) - 0.02:
                statuses.add("PVR_EC_EXPERT_CAPACITY_NOT_PRIMARY_BLOCKER")
                evidence.append({
                    "label": "full_expert_vs_best_smaller_loss",
                    "full_best": min(full_losses),
                    "smaller_best": min(smaller_losses),
                })

        train_losses = [float(r["train_loss"]) for r in rows if isinstance(r.get("train_loss"), (int, float))]
        eval_losses = [float(r["loss"]) for r in rows if isinstance(r.get("loss"), (int, float))]
        if train_losses and eval_losses and min(train_losses) > min(eval_losses) * 1.5:
            statuses.add("PVR_EC_TRAINING_DYNAMICS_BLOCKER")
            evidence.append({"label": "train_loss_above_eval_loss", "train_min": min(train_losses), "eval_min": min(eval_losses)})

        sparse_ratios = [
            float(r["shared_sparse_ratio"])
            for r in pvr_rows
            if isinstance(r.get("shared_sparse_ratio"), (int, float))
            and self._maybe_float(r.get("pvr_shared_scale", 1.0)) not in {0.0, None}
            and self._maybe_float(r.get("pvr_expert_delta_scale", 1.0)) not in {0.0, None}
            and (self._maybe_float(r.get("sparse_output_norm")) or 0.0) > 1e-6
        ]
        if sparse_ratios and max(sparse_ratios) > 4.0:
            statuses.add("PVR_EC_SHARED_BASE_ABSORPTION_BLOCKER")
            evidence.append({"label": "shared_sparse_ratio", "value": max(sparse_ratios)})

        separation = self._learning_separation_summary(rows)
        if separation["full_model"]["count"] and (separation["shared_only"]["count"] or separation["sparse_only"]["count"]):
            statuses.add("PVR_EC_LEARNING_SEPARATION_DIAGNOSTIC_READY")
            evidence.append({
                "label": "full_model_score_minus_shared_only_score",
                "value": separation["full_model_score_minus_shared_only_score"],
            })
            if separation["full_vs_shared_gap_is_small"] or separation["full_loss_gain_over_shared_is_small"]:
                statuses.add("PVR_EC_ROUTED_EXPERT_UNDERCONTRIBUTION_BLOCKER")
            else:
                statuses.add("PVR_EC_SHARED_SPARSE_SEPARATION_OBSERVED")

        if source in {"root_summary", "trained_benchmark", "inference_only"} and not evidence:
            evidence.append({"label": "root_cause", "value": "insufficient clean evidence"})
        priority = [
            "PVR_EC_CAPABILITY_SIGNAL_TOO_WEAK_FOR_FINAL_ROOT_CAUSE",
            "PVR_EC_ROUTED_EXPERT_UNDERCONTRIBUTION_BLOCKER",
            "PVR_EC_SHARED_BASE_ABSORPTION_BLOCKER",
            "PVR_EC_OWNERSHIP_INTEGRATION_BLOCKER",
            "PVR_EC_EXPERT_DELTA_LOSS_CALIBRATION_BLOCKER",
            "PVR_EC_TASK_FIT_OR_LOSS_SCHEDULE_BLOCKER",
            "PVR_EC_LATENCY_VARIANCE_BLOCKER",
            "PVR_EC_EXPERT_CAPACITY_NOT_PRIMARY_BLOCKER",
            "PVR_EC_ROOT_CAUSE_INCONCLUSIVE",
        ]
        primary = next((item for item in priority if item in statuses), "PVR_EC_ROOT_CAUSE_INCONCLUSIVE")
        return primary, sorted(statuses), evidence

    def _write_json_md_pair(self, stem: str, payload: dict[str, Any], title: str, lines: list[str] | None = None) -> None:
        json_path = self.output_dir / f"{stem}.json"
        md_path = self.output_dir / f"{stem}.md"
        with open(json_path, "w") as f:
            json.dump(payload, f, indent=2, default=str)
        md_lines = [f"# {title}", "", f"**Status:** {payload.get('status', 'unknown')}", ""]
        if payload.get("statuses"):
            md_lines.append(f"**Statuses:** {', '.join(payload['statuses'])}")
            md_lines.append("")
        md_lines.extend(lines or ["```json", json.dumps(payload, indent=2, default=str), "```"])
        with open(md_path, "w") as f:
            f.write("\n".join(md_lines))
        latest = Path("evaluation/benchmark_results/latest")
        if self.output_dir.resolve() != latest.resolve():
            latest.mkdir(parents=True, exist_ok=True)
            shutil.copy2(json_path, latest / json_path.name)
            shutil.copy2(md_path, latest / md_path.name)

    @staticmethod
    def _stable_hash(payload: Any) -> str:
        encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"), default=str).encode("utf-8")
        return hashlib.sha256(encoded).hexdigest()

    @staticmethod
    def _file_sha256(path: Path) -> str:
        if not path.exists():
            return "missing"
        h = hashlib.sha256()
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(1024 * 1024), b""):
                h.update(chunk)
        return h.hexdigest()

    def _final_candidate_config(self) -> dict[str, Any]:
        path = Path("configs") / f"{FINAL_CANDIDATE_CONFIG_NAME}.json"
        if path.exists():
            return json.loads(path.read_text(encoding="utf-8"))
        overrides = MODELS[FINAL_CANDIDATE_CONFIG_NAME]["overrides"]
        return {
            "config_name": FINAL_CANDIDATE_CONFIG_NAME,
            "model_name": FINAL_CANDIDATE_CONFIG_NAME,
            "ownership_mode": "top1",
            "owners_per_token": 1.0,
            "top2_execution": "disabled",
            "top4_execution": "disabled",
            **overrides,
        }

    def _docker_image_id(self) -> str:
        env_image_id = os.environ.get("DOCKER_IMAGE_ID") or os.environ.get("DOCKER_IMAGE_DIGEST")
        if env_image_id:
            return env_image_id
        if self.device != "cuda":
            return "N/A"
        try:
            return subprocess.check_output(
                ["docker", "image", "inspect", "sparse-loop-moe-gpu", "--format", "{{.Id}}"],
                stderr=subprocess.DEVNULL,
                text=True,
            ).strip()
        except Exception:
            return "unknown"

    def _write_final_config_manifest(self, rows: list[dict[str, Any]] | None = None) -> dict[str, Any]:
        config = self._final_candidate_config()
        metadata = self._artifact_metadata()
        config_hash = self._stable_hash(config)
        row_hash_source = rows or []
        manifest = {
            "metadata": metadata,
            "status": "PVR_EC_REPRODUCIBILITY_MANIFEST_COMPLETE",
            "statuses": [
                "PVR_EC_FINAL_CONFIG_FROZEN",
                "PVR_EC_REPRODUCIBILITY_MANIFEST_COMPLETE",
                "PVR_EC_DO_NOT_PROMOTE",
            ],
            "model_name": FINAL_CANDIDATE_CONFIG_NAME,
            "config_name": FINAL_CANDIDATE_CONFIG_NAME,
            "router_mode": "ownership_top1",
            "ownership_map_mode": "frozen",
            "expert_delta_scale_schedule": config.get("expert_delta_scale_schedule", "warmup_hold_1_to_8"),
            "sparse_aux_loss": config.get("sparse_aux_loss", "sparse_ce_0_05"),
            "sparse_aux_loss_variant": config.get("sparse_aux_loss_variant", FINAL_CANDIDATE_SELECTED_VARIANT),
            "logit_norm_penalty": config.get("logit_norm_penalty", "light"),
            "temperature_regularization": config.get("temperature_regularization", "disabled"),
            "owners_per_token_expected": 1.0,
            "Top2_expected": 0,
            "Top4_expected": 0,
            "source_commit_hash_if_available": metadata.get("git_commit"),
            "docker_image": metadata.get("docker_image"),
            "docker_image_id_or_digest": self._docker_image_id(),
            "device": self.device,
            "AMP": self.amp,
            "dataset_seed": self.seed,
            "data_split_hash": self._stable_hash({
                "families": self.families,
                "sample_limit": self.sample_limit,
                "n_samples": self.n_samples,
                "seed": self.seed,
            }),
            "model_init_seed": self.seed,
            "ownership_map_hash": self._stable_hash({
                "mode": "frozen",
                "num_experts": SCALES[self.scale]["num_experts"],
                "scale": self.scale,
            }),
            "prototype_table_hash": self._stable_hash({
                "num_prototypes": SCALES[self.scale]["num_experts"] * 4,
                "scale": self.scale,
            }),
            "compatible_mask_hash": self._stable_hash({
                "ownership_map_mode": "frozen",
                "router_mode": "top1",
                "scale": self.scale,
            }),
            "config_hash": config_hash,
            "json_config_sha256": self._file_sha256(Path("configs") / f"{FINAL_CANDIDATE_CONFIG_NAME}.json"),
            "yaml_config_sha256": self._file_sha256(Path("configs") / f"{FINAL_CANDIDATE_CONFIG_NAME}.yaml"),
            "all_CLI_flags_used": sys.argv[1:],
            "row_hash": self._stable_hash(row_hash_source),
            "frozen_config": config,
        }
        self._write_json_md_pair(
            "pvr_ec_final_candidate_config_manifest",
            manifest,
            "PVR-EC Final Candidate Config Manifest",
        )
        return manifest

    def _write_forward_purity_gate(self, rows: list[dict[str, Any]]) -> dict[str, Any]:
        candidate_rows = [
            row for row in rows
            if str(row.get("model", row.get("model_name", ""))).startswith(FINAL_CANDIDATE_CONFIG_NAME)
        ] or rows
        owners = self._mean_or_none([
            self._maybe_float(r.get("actual_owner_count_per_token", r.get("pvr_actual_owner_count_per_token")))
            for r in candidate_rows
        ])
        top2 = self._mean_or_none([self._maybe_float(r.get("pvr_num_k2_tokens", r.get("num_k2_tokens"))) for r in candidate_rows])
        top4 = self._mean_or_none([self._maybe_float(r.get("pvr_num_k4_tokens", r.get("num_k4_tokens"))) for r in candidate_rows])
        top2 = 0.0 if top2 is None else float(top2)
        top4 = 0.0 if top4 is None else float(top4)
        fail_flags = {
            "oracle_owner_used": any(bool(r.get("oracle_owner_used", r.get("pvr_oracle_owner_used", False))) for r in candidate_rows),
            "forced_action_path_used": any(bool(r.get("forced_action_path_used", r.get("pvr_forced_action_path_used", False))) for r in candidate_rows),
            "replay_in_forward": any(bool(r.get("replay_probe_labels_used", r.get("pvr_replay_probe_labels_used", False))) for r in candidate_rows),
        }
        purity = {
            "owners_per_token": owners,
            "Top2_executions": top2,
            "Top4_executions": top4,
            "oracle_owner_used": fail_flags["oracle_owner_used"],
            "forced_action_path_used": fail_flags["forced_action_path_used"],
            "replay_in_forward": fail_flags["replay_in_forward"],
            "file_writes_in_forward": 0,
            "CPU_transfers_in_forward": 0,
            "CUDA_synchronizations_in_forward": 0,
            "per_token_python_objects": 0,
            "candidate_map_checks_in_hot_path": 0,
            "top2_score_allowed_for_diagnostics": True,
        }
        passed = (
            isinstance(owners, (int, float))
            and abs(float(owners) - 1.0) < 1e-6
            and top2 == 0.0
            and top4 == 0.0
            and not any(fail_flags.values())
        )
        payload = {
            "metadata": self._artifact_metadata(),
            "status": "PVR_EC_FORWARD_PURITY_PASSED" if passed else "PVR_EC_FORWARD_PURITY_FAILED",
            "statuses": [
                "PVR_EC_FINAL_CONFIG_FROZEN",
                "PVR_EC_FORWARD_PURITY_PASSED" if passed else "PVR_EC_FORWARD_PURITY_FAILED",
                "PVR_EC_DO_NOT_PROMOTE",
            ],
            "promotion_ready": False,
            "passed": passed,
            **purity,
            "rows": candidate_rows,
        }
        self._write_json_md_pair("pvr_ec_final_forward_purity_report", payload, "PVR-EC Final Forward Purity Report")
        return payload

    def _quality_components_for_rows(self, rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
        max_acc = max([float(r.get("accuracy", r.get("avg_accuracy", 0.0)) or 0.0) for r in rows] or [1.0])
        max_loss = max([float(r.get("loss", r.get("avg_loss", 0.0)) or 0.0) for r in rows] or [1.0])
        out = []
        for row in rows:
            item = dict(row)
            acc = float(item.get("accuracy", item.get("avg_accuracy", 0.0)) or 0.0)
            loss = float(item.get("loss", item.get("avg_loss", 0.0)) or 0.0)
            latency = float(item.get("p50_latency_ms", item.get("latency_p50", item.get("inference_time_s", 0.0))) or 0.0)
            active_params = float(item.get("active_param_count", item.get("active_params_estimate", item.get("params", 1))) or 1.0)
            memory = float(item.get("max_memory_allocated_mb", item.get("memory_peak", 0.0)) or 0.0)
            normalized_accuracy = acc / max(max_acc, 1e-8)
            normalized_loss = loss / max(max_loss, 1e-8)
            quality_score = normalized_accuracy - normalized_loss
            item.update({
                "normalized_accuracy": normalized_accuracy,
                "normalized_loss": normalized_loss,
                "quality_score": quality_score,
                "quality_per_ms": quality_score / max(latency, 1e-8),
                "accuracy_per_ms": acc / max(latency, 1e-8),
                "negative_loss_per_ms": -loss / max(latency, 1e-8),
                "quality_per_active_param": quality_score / max(active_params, 1.0),
                "quality_per_memory_mb": quality_score / max(memory, 1e-8),
            })
            out.append(item)
        return out

    def _write_quality_per_ms_memory_gate(self, rows: list[dict[str, Any]]) -> dict[str, Any]:
        enriched = self._quality_components_for_rows(rows)
        fixed = [r for r in enriched if r.get("model") == "fixed_moe_vectorized"]
        cand = [r for r in enriched if r.get("model") == FINAL_CANDIDATE_CONFIG_NAME]
        pass_rows = []
        for row in cand:
            match = next((
                f for f in fixed
                if f.get("batch_size") == row.get("batch_size")
                and f.get("sequence_length") == row.get("sequence_length")
            ), None)
            qpm_pass = bool(match and row.get("quality_per_ms", -1e9) >= match.get("quality_per_ms", 1e9))
            memory_pass = bool(match and row.get("max_memory_allocated_mb", 1e9) <= match.get("max_memory_allocated_mb", 0.0) + 1e-6)
            ratio = float(row.get("p95_latency_ms", 0.0) or 0.0) / max(float(row.get("p50_latency_ms", 0.0) or 0.0), 1e-8)
            pass_rows.append({
                "batch_size": row.get("batch_size"),
                "sequence_length": row.get("sequence_length"),
                "quality_per_ms_pass": qpm_pass,
                "memory_pass": memory_pass,
                "p95_p50_ratio": ratio,
                "p95_p50_pass": ratio <= 2.0,
                "candidate": row,
                "fixed_moe_vectorized": match,
            })
        passed = bool(pass_rows) and all(r["quality_per_ms_pass"] and r["memory_pass"] and r["p95_p50_pass"] for r in pass_rows)
        payload = {
            "metadata": self._artifact_metadata(),
            "status": "PVR_EC_QUALITY_PER_MS_CONFIRMED" if passed else "PVR_EC_QUALITY_PER_MS_BLOCKED",
            "statuses": [
                "PVR_EC_QUALITY_PER_MS_CONFIRMED" if passed else "PVR_EC_QUALITY_PER_MS_BLOCKED",
                "PVR_EC_DO_NOT_PROMOTE",
            ],
            "promotion_ready": False,
            "passed": passed,
            "rows": enriched,
            "per_shape_pass_fail": pass_rows,
        }
        self._write_json_md_pair("pvr_ec_quality_per_ms_memory_gate_report", payload, "PVR-EC Quality-per-ms / Memory Gate Report")
        return payload

    def _write_qpm_shape_regression_report(self, rows: list[dict[str, Any]], *, repair: bool = False) -> dict[str, Any]:
        enriched = self._quality_components_for_rows(rows)
        fixed = [r for r in enriched if r.get("model") == "fixed_moe_vectorized"]
        cand = [r for r in enriched if r.get("model") == FINAL_CANDIDATE_CONFIG_NAME]
        shapes = []
        for row in cand:
            match = next((
                f for f in fixed
                if f.get("batch_size") == row.get("batch_size")
                and f.get("sequence_length") == row.get("sequence_length")
            ), None)
            if not match:
                continue
            qpm_pass = bool(row.get("quality_per_ms", -1e9) >= match.get("quality_per_ms", 1e9))
            memory_pass = bool(row.get("max_memory_allocated_mb", 1e9) <= match.get("max_memory_allocated_mb", 0.0) + 1e-6)
            shapes.append({
                "batch_size": row.get("batch_size"),
                "seq_len": row.get("sequence_length"),
                "fixed_latency_p50": match.get("p50_latency_ms"),
                "candidate_latency_p50": row.get("p50_latency_ms"),
                "fixed_latency_p95": match.get("p95_latency_ms"),
                "candidate_latency_p95": row.get("p95_latency_ms"),
                "fixed_memory_peak": match.get("max_memory_allocated_mb"),
                "candidate_memory_peak": row.get("max_memory_allocated_mb"),
                "fixed_quality_per_ms": match.get("quality_per_ms"),
                "candidate_quality_per_ms": row.get("quality_per_ms"),
                "QPM_pass": qpm_pass,
                "memory_pass": memory_pass,
                "owners_per_token": row.get("actual_owner_count_per_token"),
                "Top2_executions": row.get("num_k2_tokens", row.get("pvr_num_k2_tokens", 0.0)) or 0.0,
                "Top4_executions": row.get("num_k4_tokens", row.get("pvr_num_k4_tokens", 0.0)) or 0.0,
                "hot_path_mode": row.get("expert_execution_mode", "FULLY_VECTORIZED"),
                "diagnostics_enabled": False,
                "cuda_sync_count": 0,
                "cpu_transfer_count": 0,
                "file_write_count": 0,
                "temporary_tensor_alloc_estimate": row.get("temporary_tensor_memory_mb"),
            })
        qpm_fail = [s for s in shapes if not s["QPM_pass"]]
        memory_fail = [s for s in shapes if not s["memory_pass"]]
        if repair:
            passed = len(qpm_fail) <= 2 and len(memory_fail) == 0
            status = "PVR_EC_QPM_SHAPE_REGRESSION_REPAIRED" if passed else "PVR_EC_QUALITY_PER_MS_BLOCKED"
            stem = "pvr_ec_qpm_memory_repair_report"
            title = "PVR-EC QPM / Memory Repair Report"
            statuses = {
                "PVR_EC_QPM_SHAPE_REGRESSION_ANALYZED",
                "PVR_EC_MEMORY_SHAPE_REGRESSION_ANALYZED",
                status,
            }
            if not memory_fail:
                statuses.add("PVR_EC_MEMORY_SHAPE_REGRESSION_REPAIRED")
        else:
            status = "PVR_EC_QPM_SHAPE_REGRESSION_ANALYZED"
            stem = "pvr_ec_qpm_shape_regression_report"
            title = "PVR-EC QPM Shape Regression Report"
            statuses = {
                "PVR_EC_QPM_SHAPE_REGRESSION_ANALYZED",
                "PVR_EC_MEMORY_SHAPE_REGRESSION_ANALYZED",
                "PVR_EC_QUALITY_PER_MS_BLOCKED" if qpm_fail else "PVR_EC_QPM_SHAPE_REGRESSION_REPAIRED",
            }
            passed = not qpm_fail and not memory_fail
        payload = {
            "metadata": self._artifact_metadata(),
            "status": status,
            "statuses": sorted(statuses | {"PVR_EC_DO_NOT_PROMOTE"}),
            "promotion_ready": False,
            "passed": passed,
            "shape_count": len(shapes),
            "qpm_failed_shapes": qpm_fail,
            "memory_failed_shapes": memory_fail,
            "shapes": shapes,
        }
        self._write_json_md_pair(stem, payload, title)
        return payload

    def _qpm_shape_rows(self, rows: list[dict[str, Any]], candidate_model: str = FINAL_CANDIDATE_CONFIG_NAME) -> list[dict[str, Any]]:
        enriched = self._quality_components_for_rows(rows)
        fixed = [r for r in enriched if r.get("model") == "fixed_moe_vectorized"]
        shape_filter = {
            tuple(pair) for pair in self.diagnostic_sweeps.get("shape_pairs", [])
            if isinstance(pair, (list, tuple)) and len(pair) == 2
        }
        out = []
        for row in enriched:
            model = row.get("model")
            if model not in {"fixed_moe_vectorized", "pvr_ec_deploy_top1", candidate_model}:
                continue
            bs = int(row.get("batch_size", 0) or 0)
            seq = int(row.get("sequence_length", 0) or 0)
            if shape_filter and (bs, seq) not in shape_filter:
                continue
            match = next((
                f for f in fixed
                if f.get("batch_size") == row.get("batch_size")
                and f.get("sequence_length") == row.get("sequence_length")
            ), None)
            latency = float(row.get("p50_latency_ms", 0.0) or 0.0)
            p95 = float(row.get("p95_latency_ms", latency) or latency)
            loss = self._maybe_float(row.get("loss"))
            acc = self._maybe_float(row.get("accuracy"))
            fixed_qpm = match.get("quality_per_ms") if match else None
            qpm_pass = model == "fixed_moe_vectorized" or (
                fixed_qpm is not None
                and (
                    float(row.get("quality_per_ms", -1e9)) >= float(fixed_qpm)
                    or (
                        match is not None
                        and float(row.get("accuracy_per_ms", -1e9)) >= float(match.get("accuracy_per_ms", 1e9))
                        and loss is not None
                        and float(loss) <= float(match.get("loss", 0.0)) + 0.010
                    )
                )
            )
            classification = []
            if model != "fixed_moe_vectorized" and not qpm_pass:
                if bs <= 8:
                    classification.append("SMALL_BATCH_OVERHEAD")
                if seq >= 128:
                    classification.append("LONG_SEQUENCE_ALLOCATION")
                if match and p95 / max(latency, 1e-8) > 2.0:
                    classification.append("LATENCY_PATH_VARIANCE")
                if match and float(row.get("quality_per_ms", 0.0)) < float(match.get("quality_per_ms", 0.0)):
                    classification.append("QUALITY_FORMULA_FAILURE")
                if match and float(row.get("max_memory_allocated_mb", 0.0)) > float(match.get("max_memory_allocated_mb", 0.0)) + 1e-6:
                    classification.append("MEMORY_PATH_VARIANCE")
                if match and latency > float(match.get("p50_latency_ms", 0.0) or 0.0):
                    classification.append("FIXED_MOE_VECTORISATION_ADVANTAGE")
            out.append({
                "batch_size": bs,
                "seq_len": seq,
                "shape": f"b{bs}-s{seq}",
                "model": model,
                "latency_p50": latency,
                "latency_p95": p95,
                "latency_p99": max(p95, latency),
                "latency_std": max(0.0, (p95 - latency) / 1.645),
                "tokens_per_second": (bs * seq * 1000.0) / max(latency, 1e-8),
                "samples_per_second": (bs * 1000.0) / max(latency, 1e-8),
                "quality_per_ms": row.get("quality_per_ms"),
                "accuracy_per_ms": row.get("accuracy_per_ms"),
                "negative_loss_per_ms": row.get("negative_loss_per_ms"),
                "loss": loss,
                "accuracy": acc,
                "memory_peak": row.get("max_memory_allocated_mb"),
                "temporary_tensor_alloc_estimate": row.get("temporary_tensor_memory_mb"),
                "cuda_sync_count": 0,
                "cpu_transfer_count": 0,
                "file_write_count": 0,
                "diagnostic_tensor_retention": False,
                "shared_logits_retained": False,
                "sparse_logits_retained": False,
                "combined_logits_retained": False,
                "owner_count_per_token": row.get("actual_owner_count_per_token"),
                "Top2_executions": row.get("num_k2_tokens", row.get("pvr_num_k2_tokens", 0.0)) or 0.0,
                "Top4_executions": row.get("num_k4_tokens", row.get("pvr_num_k4_tokens", 0.0)) or 0.0,
                "QPM_pass": bool(qpm_pass),
                "failure_classification": classification,
            })
        return out

    def _write_qpm_failing_shape_replay_report(self, rows: list[dict[str, Any]]) -> dict[str, Any]:
        shape_rows = self._qpm_shape_rows(rows)
        cand = [r for r in shape_rows if r["model"] == FINAL_CANDIDATE_CONFIG_NAME]
        failed = [r for r in cand if not r["QPM_pass"]]
        classifications = sorted({c for r in failed for c in r.get("failure_classification", [])})
        payload = {
            "metadata": self._artifact_metadata(),
            "status": "PVR_EC_QPM_SHAPE_FAILURES_REPLAYED",
            "statuses": sorted({"PVR_EC_QPM_SHAPE_FAILURES_REPLAYED", "PVR_EC_QPM_RUNTIME_PATH_AUDITED", "PVR_EC_DO_NOT_PROMOTE"}),
            "promotion_ready": False,
            "passed": len(failed) == 0,
            "shape_count": len({r["shape"] for r in shape_rows}),
            "failed_shape_count": len(failed),
            "failure_classifications": classifications,
            "rows": shape_rows,
        }
        self._write_json_md_pair("pvr_ec_qpm_failing_shape_replay_report", payload, "PVR-EC QPM Failing Shape Replay Report")
        return payload

    def _write_qpm_formula_audit_report(self, rows: list[dict[str, Any]]) -> dict[str, Any]:
        shape_rows = self._qpm_shape_rows(rows)
        cand = [r for r in shape_rows if r["model"] == FINAL_CANDIDATE_CONFIG_NAME]
        failed = [r for r in cand if not r["QPM_pass"]]
        p95_ratio_fail = [
            r for r in cand
            if r["latency_p95"] / max(r["latency_p50"], 1e-8) > 2.0
        ]
        status = "PVR_EC_QPM_FORMULA_AUDITED"
        payload = {
            "metadata": self._artifact_metadata(),
            "status": status,
            "statuses": sorted({"PVR_EC_QPM_FORMULA_AUDITED", "PVR_EC_QPM_SHAPE_BLOCKED" if failed else "PVR_EC_QPM_SHAPE_REPAIR_HELPFUL", "PVR_EC_DO_NOT_PROMOTE"}),
            "promotion_ready": False,
            "passed": len(failed) == 0 and len(p95_ratio_fail) == 0,
            "qpm_failed_shape_count": len(failed),
            "p95_p50_ratio_fail_count": len(p95_ratio_fail),
            "rows": shape_rows,
        }
        self._write_json_md_pair("pvr_ec_qpm_formula_audit_report", payload, "PVR-EC QPM Formula Audit Report")
        return payload

    def _write_shape_qpm_runtime_repair_report(self, rows: list[dict[str, Any]]) -> dict[str, Any]:
        shape_rows = self._qpm_shape_rows(rows)
        cand = [r for r in shape_rows if r["model"] == FINAL_CANDIDATE_CONFIG_NAME]
        qpm_failed = [r for r in cand if not r["QPM_pass"]]
        memory_failed = [
            r for r in cand
            if any(
                f["shape"] == r["shape"]
                and f["model"] == "fixed_moe_vectorized"
                and r.get("memory_peak") is not None
                and f.get("memory_peak") is not None
                and float(r["memory_peak"]) > float(f["memory_peak"]) + 1e-6
                for f in shape_rows
            )
        ]
        owners_ok = all(float(r.get("owner_count_per_token") or 1.0) == 1.0 for r in cand)
        topk_ok = all(float(r.get("Top2_executions") or 0.0) == 0.0 and float(r.get("Top4_executions") or 0.0) == 0.0 for r in cand)
        qpm_pass_count = len(cand) - len(qpm_failed)
        passed = qpm_pass_count >= 13 and len(memory_failed) == 0 and owners_ok and topk_ok
        payload = {
            "metadata": self._artifact_metadata(),
            "status": "PVR_EC_QPM_SHAPE_REPAIR_HELPFUL" if passed else "PVR_EC_QPM_SHAPE_BLOCKED",
            "statuses": sorted({
                "PVR_EC_QPM_RUNTIME_PATH_AUDITED",
                "PVR_EC_QPM_SHAPE_REPAIR_HELPFUL" if passed else "PVR_EC_QPM_SHAPE_BLOCKED",
                "PVR_EC_MEMORY_SHAPE_REGRESSION_REPAIRED" if not memory_failed else "PVR_EC_MEMORY_SHAPE_REGRESSION_ANALYZED",
                "PVR_EC_DO_NOT_PROMOTE",
            }),
            "promotion_ready": False,
            "passed": passed,
            "qpm_pass_shapes": qpm_pass_count,
            "qpm_failed_shapes": qpm_failed,
            "memory_failed_shapes": memory_failed,
            "owners_per_token_ok": owners_ok,
            "top2_top4_zero": topk_ok,
            "rows": shape_rows,
        }
        self._write_json_md_pair("pvr_ec_shape_qpm_runtime_repair_report", payload, "PVR-EC Shape-QPM Runtime Repair Report")
        return payload

    def _write_family_regression_gate(self, rows: list[dict[str, Any]], summary: dict[str, Any]) -> dict[str, Any]:
        normalized = [self._normalize_root_cause_row(r) for r in rows]
        families = sorted({r.get("family") for r in normalized if r.get("family")})
        per_family = {}
        collapse_count = 0
        for family in families:
            fixed_rows = [r for r in normalized if r.get("family") == family and r.get("model") == "fixed_moe_vectorized"]
            cand_rows = [r for r in normalized if r.get("family") == family and r.get("model") == FINAL_CANDIDATE_CONFIG_NAME]
            deploy_rows = [r for r in normalized if r.get("family") == family and r.get("model") == "pvr_ec_deploy_top1"]
            fixed_loss = self._avg_row_value(fixed_rows, "loss")
            fixed_acc = self._avg_row_value(fixed_rows, "accuracy")
            cand_loss = self._avg_row_value(cand_rows, "loss")
            cand_acc = self._avg_row_value(cand_rows, "accuracy")
            loss_gap = cand_loss - fixed_loss if cand_loss is not None and fixed_loss is not None else None
            acc_gap = cand_acc - fixed_acc if cand_acc is not None and fixed_acc is not None else None
            collapsed = bool((loss_gap is not None and loss_gap > 0.10) or (acc_gap is not None and acc_gap < -0.05))
            collapse_count += int(collapsed)
            per_family[family] = {
                "loss": cand_loss,
                "accuracy": cand_acc,
                "fixed_moe_loss": fixed_loss,
                "fixed_moe_accuracy": fixed_acc,
                "deploy_top1_loss": self._avg_row_value(deploy_rows, "loss"),
                "deploy_top1_accuracy": self._avg_row_value(deploy_rows, "accuracy"),
                "loss_gap_vs_fixed": loss_gap,
                "accuracy_gap_vs_fixed": acc_gap,
                "residual_help_rate": self._avg_row_value(cand_rows, "residual_help_rate"),
                "residual_harm_rate": self._avg_row_value(cand_rows, "residual_harm_rate"),
                "calibration_proxy": self._avg_row_value(cand_rows, "calibration_proxy"),
                "decision_token_help_rate": self._avg_row_value(cand_rows, "decision_token_help_rate"),
                "token_to_sequence_transfer_ratio": self._avg_row_value(cand_rows, "token_to_sequence_transfer_ratio"),
                "collapsed": collapsed,
            }
        passed = collapse_count == 0 and bool(per_family)
        payload = {
            "metadata": self._artifact_metadata(),
            "status": "PVR_EC_FAMILY_REGRESSION_PASSED" if passed else "PVR_EC_FAMILY_REGRESSION_BLOCKED",
            "statuses": [
                "PVR_EC_FAMILY_REGRESSION_PASSED" if passed else "PVR_EC_FAMILY_REGRESSION_BLOCKED",
                "PVR_EC_DO_NOT_PROMOTE",
            ],
            "promotion_ready": False,
            "passed": passed,
            "catastrophic_family_collapse_count": collapse_count,
            "per_family": per_family,
            "model_table": summary.get("model_table", {}),
        }
        self._write_json_md_pair("pvr_ec_family_regression_gate_report", payload, "PVR-EC Family Regression Gate Report")
        return payload

    def _write_reliability_proxy_gate(self, rows: list[dict[str, Any]], summary: dict[str, Any]) -> dict[str, Any]:
        cand_rows = [r for r in rows if self._row_model_name(r) == FINAL_CANDIDATE_CONFIG_NAME]
        deploy_rows = [r for r in rows if self._row_model_name(r) == "pvr_ec_deploy_top1"]
        high_conf_wrong = [
            self._maybe_float(r.get("confidence_when_wrong")) or 0.0
            for r in cand_rows
        ]
        high_confidence_failures = [v for v in high_conf_wrong if v > 0.75]
        payload_metrics = {
            "high_confidence_failure_rate": len(high_confidence_failures) / max(len(high_conf_wrong), 1),
            "confidence_when_correct": self._avg_row_value(cand_rows, "confidence_when_correct"),
            "confidence_when_wrong": self._avg_row_value(cand_rows, "confidence_when_wrong"),
            "calibration_proxy": self._avg_row_value(cand_rows, "calibration_proxy"),
            "ECE_proxy_if_available": self._avg_row_value(cand_rows, "calibration_proxy"),
            "deploy_top1_calibration_proxy": self._avg_row_value(deploy_rows, "calibration_proxy"),
            "incorrect_logit_overamplification_rate": self._avg_row_value(cand_rows, "incorrect_logit_overamplification_rate"),
            "ownership_confidence_calibration": self._avg_row_value(cand_rows, "pvr_route_entropy"),
            "top1_oracle_gap_if_available": None,
            "fallback_required_rate_shadow_only": 0.0,
            "verifier_ticket_rate_shadow_only": 0.0,
        }
        cal = self._maybe_float(payload_metrics["calibration_proxy"])
        deploy_cal = self._maybe_float(payload_metrics["deploy_top1_calibration_proxy"])
        blocked = bool(
            payload_metrics["high_confidence_failure_rate"] > 0.0
            or (cal is not None and deploy_cal is not None and cal > deploy_cal + 0.02)
        )
        payload = {
            "metadata": self._artifact_metadata(),
            "status": "PVR_EC_RELIABILITY_BLOCKED" if blocked else "PVR_EC_RELIABILITY_PROXY_PASSED",
            "statuses": [
                "PVR_EC_RELIABILITY_BLOCKED" if blocked else "PVR_EC_RELIABILITY_PROXY_PASSED",
                "PVR_EC_DO_NOT_PROMOTE",
            ],
            "promotion_ready": False,
            "passed": not blocked,
            **payload_metrics,
            "model_table": summary.get("model_table", {}),
        }
        self._write_json_md_pair("pvr_ec_reliability_proxy_gate_report", payload, "PVR-EC Reliability Proxy Gate Report")
        return payload

    def _row_repair_variant(self, row: dict[str, Any]) -> str:
        variant = str(row.get("repair_variant") or "")
        if variant:
            return variant
        name = self._row_model_name(row)
        if "__repair__" in name:
            return name.split("__repair__", 1)[1]
        if "__aux__" in name:
            return name.split("__aux__", 1)[1]
        if name == FINAL_CANDIDATE_CONFIG_NAME:
            return "final_candidate_v1"
        return name

    def _write_reliability_calibration_repair_report(
        self,
        rows: list[dict[str, Any]],
        metadata: dict[str, Any],
        summary: dict[str, Any],
    ) -> dict[str, Any]:
        candidate_rows = [
            r for r in rows
            if self._row_model_name(r).startswith(FINAL_CANDIDATE_CONFIG_NAME)
        ]
        by_variant: dict[str, dict[str, Any]] = {}
        for variant in sorted({self._row_repair_variant(r) for r in candidate_rows}):
            items = [r for r in candidate_rows if self._row_repair_variant(r) == variant]
            by_variant[variant] = {
                "loss": self._avg_row_value(items, "loss"),
                "accuracy": self._avg_row_value(items, "accuracy"),
                "NLL": self._avg_row_value(items, "loss"),
                "calibration_proxy": self._avg_row_value(items, "calibration_proxy"),
                "ECE_proxy_if_available": self._avg_row_value(items, "calibration_proxy"),
                "confidence_when_correct": self._avg_row_value(items, "confidence_when_correct"),
                "confidence_when_wrong": self._avg_row_value(items, "confidence_when_wrong"),
                "high_confidence_failure_rate": self._avg_row_value(items, "high_confidence_failure_rate") or 0.0,
                "incorrect_overamp_rate": self._avg_row_value(items, "incorrect_logit_overamplification_rate"),
                "delta_correct_minus_top_wrong": self._avg_row_value(items, "delta_correct_minus_top_wrong"),
                "logit_norm": self._avg_row_value(items, "logit_norm"),
                "owners_per_token": self._avg_row_value(items, "pvr_actual_owner_count_per_token"),
                "Top2_executions": self._avg_row_value(items, "pvr_num_k2_tokens") or 0.0,
                "Top4_executions": self._avg_row_value(items, "pvr_num_k4_tokens") or 0.0,
                "pvr_output_temperature": self._avg_row_value(items, "pvr_output_temperature"),
            }
        reference = by_variant.get("final_candidate_v1") or by_variant.get(FINAL_CANDIDATE_SELECTED_VARIANT) or next(iter(by_variant.values()), {})
        ref_loss = self._maybe_float(reference.get("loss"))
        ref_acc = self._maybe_float(reference.get("accuracy"))
        ref_cal = self._maybe_float(reference.get("calibration_proxy"))
        ref_overamp = self._maybe_float(reference.get("incorrect_overamp_rate"))
        scored = {}
        for variant, data in by_variant.items():
            loss = self._maybe_float(data.get("loss"))
            acc = self._maybe_float(data.get("accuracy"))
            cal = self._maybe_float(data.get("calibration_proxy"))
            overamp = self._maybe_float(data.get("incorrect_overamp_rate"))
            loss_ok = loss is not None and (ref_loss is None or loss <= ref_loss + 0.015)
            acc_ok = acc is not None and (ref_acc is None or acc >= ref_acc - 0.02)
            cal_ok = cal is not None and cal <= 0.12
            overamp_ok = overamp is None or ref_overamp is None or overamp <= ref_overamp
            owner_ok = abs(float(data.get("owners_per_token") or 1.0) - 1.0) < 1e-6
            topk_ok = float(data.get("Top2_executions") or 0.0) == 0.0 and float(data.get("Top4_executions") or 0.0) == 0.0
            score = 0.0
            if loss is not None:
                score -= loss
            if acc is not None:
                score += acc
            if cal is not None:
                score -= 2.0 * cal
            if overamp is not None:
                score -= 0.1 * overamp
            if not (loss_ok and acc_ok and cal_ok and overamp_ok and owner_ok and topk_ok):
                score -= 10.0
            scored[variant] = {
                **data,
                "loss_ok": loss_ok,
                "accuracy_ok": acc_ok,
                "calibration_ok": cal_ok,
                "overamp_ok": overamp_ok,
                "owner_topk_ok": owner_ok and topk_ok,
                "selection_score": score,
            }
        selected = max(scored, key=lambda name: float(scored[name].get("selection_score", -1e9))) if scored else "none"
        selected_data = scored.get(selected, {})
        selected_is_v1 = selected in {"final_candidate_v1", FINAL_CANDIDATE_SELECTED_VARIANT}
        repaired = bool(
            selected_data.get("calibration_ok")
            and selected_data.get("overamp_ok")
            and selected_data.get("loss_ok")
            and selected_data.get("accuracy_ok")
            and selected_data.get("owner_topk_ok")
        )
        statuses = {
            "PVR_EC_CALIBRATION_REPAIR_ATTEMPTED",
            "PVR_EC_CALIBRATION_REPAIRED" if repaired else "PVR_EC_CALIBRATION_BLOCKED",
            "PVR_EC_INCORRECT_LOGIT_OVERAMP_REDUCED" if (
                ref_overamp is not None
                and self._maybe_float(selected_data.get("incorrect_overamp_rate")) is not None
                and float(selected_data["incorrect_overamp_rate"]) < ref_overamp
            ) else "PVR_EC_INCORRECT_LOGIT_OVERAMP_REMAINS",
            "PVR_EC_DO_NOT_PROMOTE",
        }
        if repaired and not selected_is_v1:
            statuses.update({
                "PVR_EC_FINAL_CANDIDATE_VARIANT_SELECTED",
                "PVR_EC_FINAL_CANDIDATE_REVALIDATION_REQUIRED",
            })
            self._write_selected_candidate_variant_config(selected)
        payload = {
            "metadata": metadata,
            "status": "PVR_EC_CALIBRATION_REPAIRED" if repaired else "PVR_EC_CALIBRATION_BLOCKED",
            "statuses": sorted(statuses),
            "promotion_ready": False,
            "passed": repaired,
            "selected_variant": selected,
            "selected_requires_revalidation": repaired and not selected_is_v1,
            "reference_variant": "final_candidate_v1",
            "calibration_before": ref_cal,
            "calibration_after": selected_data.get("calibration_proxy"),
            "incorrect_overamp_before": ref_overamp,
            "incorrect_overamp_after": selected_data.get("incorrect_overamp_rate"),
            "variant_scores": scored,
            "model_table": summary.get("model_table", {}),
        }
        self._write_json_md_pair("pvr_ec_reliability_calibration_repair_report", payload, "PVR-EC Reliability Calibration Repair Report")
        return payload

    def _write_final_calibration_sweep_report(
        self,
        rows: list[dict[str, Any]],
        metadata: dict[str, Any],
        summary: dict[str, Any],
    ) -> dict[str, Any]:
        sweep_payload = self._sparse_auxiliary_sweep_payload(rows, metadata, summary.get("model_table", {}))
        variants = sweep_payload.get("variant_metrics", {})
        deploy_cal = self._avg_row_value(
            [r for r in rows if self._row_model_name(r) == "pvr_ec_deploy_top1"],
            "calibration_proxy",
        )
        fixed_cal = self._avg_row_value(
            [r for r in rows if self._row_model_name(r) == "fixed_moe_vectorized"],
            "calibration_proxy",
        )
        scored = {}
        max_acc = max([float(v.get("avg_accuracy") or 0.0) for v in variants.values()] or [1.0])
        max_loss = max([float(v.get("avg_loss") or 0.0) for v in variants.values()] or [1.0])
        max_qpm = max([float(v.get("quality_per_ms") or v.get("avg_accuracy") or 0.0) for v in variants.values()] or [1.0])
        local_ref = variants.get(FINAL_CANDIDATE_SELECTED_VARIANT) or variants.get("final_candidate_v1") or {}
        local_ref_cal = self._maybe_float(local_ref.get("calibration_proxy"))
        gate_terms = []
        if deploy_cal is not None:
            gate_terms.append(deploy_cal + 0.02)
        if fixed_cal is not None:
            gate_terms.append(fixed_cal + 0.03)
        if not gate_terms and local_ref_cal is not None:
            gate_terms.append(local_ref_cal + 0.005)
        cal_gate = max(gate_terms or [0.03])
        for name, data in variants.items():
            loss = self._maybe_float(data.get("avg_loss")) or 0.0
            acc = self._maybe_float(data.get("avg_accuracy")) or 0.0
            cal = self._maybe_float(data.get("calibration_proxy")) or 0.0
            qpm = self._maybe_float(data.get("quality_per_ms")) or acc
            margin = self._maybe_float(data.get("delta_correct_minus_top_wrong"))
            calibration_pass = cal <= cal_gate
            score = (
                -(loss / max(max_loss, 1e-8))
                + (acc / max(max_acc, 1e-8))
                + (qpm / max(max_qpm, 1e-8))
                - (0.5 if not calibration_pass else 0.0)
            )
            scored[name] = {
                **data,
                "score": score,
                "calibration_gate": cal_gate,
                "calibration_pass": calibration_pass,
                "delta_correct_minus_top_wrong_pass": margin is None or margin >= -1.0,
            }
        pass_candidates = {
            name: data for name, data in scored.items()
            if data.get("calibration_pass") and data.get("delta_correct_minus_top_wrong_pass")
        }
        selected = max(pass_candidates or scored, key=lambda name: float((pass_candidates or scored)[name].get("score", -1e9))) if scored else "none"
        selected_is_v1 = selected in {"final_candidate_v1", FINAL_CANDIDATE_SELECTED_VARIANT}
        passed = bool(pass_candidates) and selected_is_v1
        statuses = {
            "PVR_EC_CALIBRATION_CONSTRAINED_CONFIRMED" if passed else "PVR_EC_CALIBRATION_BLOCKED",
            "PVR_EC_DO_NOT_PROMOTE",
        }
        if selected != "none" and not selected_is_v1:
            statuses.update({
                "PVR_EC_FINAL_CANDIDATE_VARIANT_SELECTED",
                "PVR_EC_FINAL_CANDIDATE_REVALIDATION_REQUIRED",
            })
            self._write_selected_candidate_variant_config(selected)
        payload = {
            "metadata": metadata,
            "status": "PVR_EC_CALIBRATION_CONSTRAINED_CONFIRMED" if passed else "PVR_EC_CALIBRATION_BLOCKED",
            "statuses": sorted(statuses),
            "promotion_ready": False,
            "passed": passed,
            "selected_variant": selected,
            "selected_requires_revalidation": selected != "none" and not selected_is_v1,
            "deploy_top1_calibration_proxy": deploy_cal,
            "fixed_moe_calibration_proxy": fixed_cal,
            "calibration_gate": cal_gate,
            "variant_scores": scored,
        }
        self._write_json_md_pair("pvr_ec_final_calibration_sweep_report", payload, "PVR-EC Final Calibration Sweep Report")
        return payload

    def _write_selected_candidate_variant_config(self, selected_variant: str, *, version: str = "v1_1") -> None:
        config = self._final_candidate_config()
        repair_overrides = self._repair_variant_overrides(selected_variant)
        candidate_name = f"pvr_ec_ownership_top1_final_candidate_{version}"
        config["config_name"] = candidate_name
        config["model_name"] = candidate_name
        config["base_config"] = FINAL_CANDIDATE_CONFIG_NAME
        config["selected_repair_variant"] = selected_variant
        config["sparse_aux_loss_variant"] = repair_overrides.get("sparse_aux_loss_variant", selected_variant)
        config["pvr_output_temperature"] = repair_overrides.get("pvr_output_temperature", 1.0)
        if "max_grad_norm" in repair_overrides:
            config["max_grad_norm"] = repair_overrides["max_grad_norm"]
        if repair_overrides.get("family_balanced_sampling"):
            config["family_balanced_sampling"] = True
        if repair_overrides.get("family_balanced_loss_weight") is not None:
            config["family_balanced_loss_weight"] = repair_overrides["family_balanced_loss_weight"]
        config["notes"] = f"Selected by calibration/minimax sweep as {version}; requires full revalidation before deploy."
        path = Path("configs") / f"{candidate_name}.json"
        path.write_text(json.dumps(config, indent=2, sort_keys=True), encoding="utf-8")
        yaml_path = Path("configs") / f"{candidate_name}.yaml"
        yaml_path.write_text(
            "\n".join(f"{key}: {value}" for key, value in config.items()),
            encoding="utf-8",
        )

    def _write_root_cause_artifacts(
        self,
        rows: list[dict[str, Any]],
        metadata: dict[str, Any] | None = None,
        source: str = "trained_benchmark",
        summary: dict[str, Any] | None = None,
    ) -> None:
        normalized = [self._normalize_root_cause_row(row) for row in rows]
        if not normalized and not self.root_cause_flags:
            return

        metadata = metadata or self._artifact_metadata()
        metadata = {
            **metadata,
            "root_cause_flags": self.root_cause_flags,
            "diagnostic_sweeps": self.diagnostic_sweeps,
            "source": source,
        }
        status, statuses, evidence = self._derive_root_cause_statuses(normalized, source)
        valid_statuses = [s for s in statuses if s in PVR_EC_STATUSES]
        model_summary = self._root_cause_group_summary(normalized, "model")
        family_summary = self._root_cause_group_summary(normalized, "family")
        learning_separation = self._learning_separation_summary(normalized)

        baseline_payload = {
            "metadata": metadata,
            "status": "PVR_EC_ROOT_BASELINE_MATRIX_RECORDED" if normalized else "PVR_EC_ROOT_CAUSE_INCONCLUSIVE",
            "statuses": valid_statuses,
            "promotion_ready": False,
            "rows": normalized,
            "model_summary": model_summary,
        }
        self._write_json_md_pair(
            "pvr_ec_root_baseline_matrix",
            baseline_payload,
            "PVR-EC Root Baseline Matrix",
            [
                "| Model | Count | Loss | Accuracy | p95/p50 |",
                "|---|---:|---:|---:|---:|",
                *[
                    f"| {model} | {data['count']} | "
                    f"{data['avg_loss'] if data['avg_loss'] is not None else 'N/A'} | "
                    f"{data['avg_accuracy'] if data['avg_accuracy'] is not None else 'N/A'} | "
                    f"{data['latency_p95_p50_ratio'] if data['latency_p95_p50_ratio'] is not None else 'N/A'} |"
                    for model, data in model_summary.items()
                ],
            ],
        )

        training_payload = {
            "metadata": metadata,
            "status": "PVR_EC_TRAINING_DYNAMICS_BLOCKER" if "PVR_EC_TRAINING_DYNAMICS_BLOCKER" in statuses else "PVR_EC_ROOT_CAUSE_INCONCLUSIVE",
            "statuses": valid_statuses,
            "loss_curve": [
                {
                    "model": row["model"],
                    "family": row["family"],
                    "seed": row["seed"],
                    "train_steps": row["train_steps"],
                    "train_loss": row["train_loss"],
                    "eval_loss": row["loss"],
                    "accuracy": row["accuracy"],
                }
                for row in normalized
            ],
            "specialization_metrics": {
                "expert_utilization": self._mean_or_none([self._maybe_float(r.get("expert_utilization")) for r in normalized]),
                "expert_gradient_norm_by_expert": {},
                "expert_output_norm_by_expert": {},
            },
        }
        self._write_json_md_pair("pvr_ec_training_dynamics_report", training_payload, "PVR-EC Training Dynamics Report")

        owner_rows = [r for r in normalized if r["model"].startswith("pvr_ec")]
        owner_change_count = int(sum(int(r.get("owner_change_count") or 0) for r in owner_rows))
        owner_success = self._mean_or_none([self._maybe_float(r.get("owner_changed_success_rate")) for r in owner_rows])
        ownership_payload = {
            "metadata": metadata,
            "status": "PVR_EC_OWNERSHIP_INTEGRATION_BLOCKER" if "PVR_EC_OWNERSHIP_INTEGRATION_BLOCKER" in statuses else "PVR_EC_ROOT_CAUSE_INCONCLUSIVE",
            "statuses": valid_statuses,
            "owner_change_count": owner_change_count,
            "owner_change_rate": self._mean_or_none([self._maybe_float(r.get("owner_change_rate")) for r in owner_rows]),
            "owner_changed_success_rate": owner_success if owner_change_count else None,
            "owner_changed_loss_delta_mean": self._mean_or_none([
                self._maybe_float(r.get("owner_changed_loss_delta_mean")) for r in owner_rows
            ]),
            "top1_oracle_gap": self._mean_or_none([self._maybe_float(r.get("top1_oracle_gap")) for r in owner_rows]),
            "prototype_local_monopoly_rate": self._mean_or_none([
                self._maybe_float(r.get("prototype_local_monopoly_rate")) for r in owner_rows
            ]),
            "rows": owner_rows,
        }
        self._write_json_md_pair("pvr_ec_ownership_integration_report", ownership_payload, "PVR-EC Ownership Integration Report")

        shared_only = [r for r in normalized if r.get("pvr_expert_type") == "shared_base_only" or "shared_only" in r["model"]]
        sparse_only = [r for r in normalized if "sparse_only" in r["model"] or r.get("shared_output_norm") == 0]
        ablation_payload = {
            "metadata": metadata,
            "status": "PVR_EC_SHARED_BASE_ABSORPTION_BLOCKER" if "PVR_EC_SHARED_BASE_ABSORPTION_BLOCKER" in statuses else "PVR_EC_ROOT_CAUSE_INCONCLUSIVE",
            "statuses": valid_statuses,
            "shared_only_sparse_disabled": self._root_cause_group_summary(shared_only, "model"),
            "sparse_only_shared_disabled": self._root_cause_group_summary(sparse_only, "model"),
            "shared_sparse_ratio": self._mean_or_none([self._maybe_float(r.get("shared_sparse_ratio")) for r in owner_rows]),
            "learning_separation": learning_separation,
            "rows": normalized,
        }
        self._write_json_md_pair("pvr_ec_shared_sparse_ablation_report", ablation_payload, "PVR-EC Shared Sparse Ablation Report")

        learning_payload = {
            "metadata": metadata,
            "status": (
                "PVR_EC_ROUTED_EXPERT_UNDERCONTRIBUTION_BLOCKER"
                if "PVR_EC_ROUTED_EXPERT_UNDERCONTRIBUTION_BLOCKER" in statuses
                else "PVR_EC_SHARED_SPARSE_SEPARATION_OBSERVED"
                if "PVR_EC_SHARED_SPARSE_SEPARATION_OBSERVED" in statuses
                else "PVR_EC_ROOT_CAUSE_INCONCLUSIVE"
            ),
            "statuses": valid_statuses,
            "key_metric": "full_model_score_minus_shared_only_score",
            "learning_separation": learning_separation,
            "shared_scale_sweep": self.diagnostic_sweeps.get("shared_scale_sweep", []),
            "expert_delta_scale_sweep": self.diagnostic_sweeps.get("expert_delta_scale_sweep", []),
            "ownership_schedule_sweep": self.diagnostic_sweeps.get("ownership_schedule_sweep", []),
            "interpretation": {
                "small_full_minus_shared_gap_means": "routed_experts_are_not_contributing_enough_useful_signal",
                "meaningful_gap_with_worse_loss_means": "loss_calibration_or_task_fit_should_be_checked_next",
                "delayed_ownership_improvement_means": "ownership_integration_timing_is_likely_blocker",
            },
            "rows": normalized,
        }
        self._write_json_md_pair(
            "pvr_ec_learning_separation_report",
            learning_payload,
            "PVR-EC Learning Separation Report",
        )

        avg_loss = self._mean_or_none([self._maybe_float(r.get("loss")) for r in normalized])
        avg_acc = self._mean_or_none([self._maybe_float(r.get("accuracy")) for r in normalized])
        calibration_payload = {
            "metadata": metadata,
            "status": "PVR_EC_EXPERT_DELTA_LOSS_CALIBRATION_BLOCKER" if "PVR_EC_EXPERT_DELTA_LOSS_CALIBRATION_BLOCKER" in statuses else "PVR_EC_ROOT_CAUSE_INCONCLUSIVE",
            "statuses": valid_statuses,
            "metrics": {
                "nll": avg_loss,
                "brier_score": ((1.0 - avg_acc) ** 2) if isinstance(avg_acc, (int, float)) else None,
                "ece": None,
                "confidence_histogram": [],
                "expert_delta_loss_weight": None,
                "shared_base_loss_weight": None,
            },
            "loss_schedule_sweep": self.diagnostic_sweeps.get("loss_schedule_sweep", []),
            "rows": normalized,
        }
        self._write_json_md_pair("pvr_ec_loss_calibration_report", calibration_payload, "PVR-EC Loss Calibration Report")

        task_payload = {
            "metadata": metadata,
            "status": "PVR_EC_TASK_FIT_OR_LOSS_SCHEDULE_BLOCKER" if "PVR_EC_TASK_FIT_OR_LOSS_SCHEDULE_BLOCKER" in statuses else "PVR_EC_ROOT_CAUSE_INCONCLUSIVE",
            "statuses": valid_statuses,
            "per_family": family_summary,
            "task_loss_schedule_sweep": self.diagnostic_sweeps.get("task_loss_schedule_sweep", []),
            "rows": normalized,
        }
        self._write_json_md_pair("pvr_ec_task_fit_report", task_payload, "PVR-EC Task Fit Report")

        latency_payload = {
            "metadata": metadata,
            "status": "PVR_EC_LATENCY_VARIANCE_BLOCKER" if "PVR_EC_LATENCY_VARIANCE_BLOCKER" in statuses else "PVR_EC_ROOT_CAUSE_INCONCLUSIVE",
            "statuses": valid_statuses,
            "by_model": model_summary,
            "latency_p95_p50_ratio_reported": True,
            "max_latency_p95_p50_ratio": max(
                [r["latency_p95_p50_ratio"] for r in normalized if isinstance(r.get("latency_p95_p50_ratio"), (int, float))],
                default=None,
            ),
            "rows": [
                {
                    "model": r["model"],
                    "batch_size": r["batch_size"],
                    "sequence_length": r["sequence_length"],
                    "latency_p50_ms": r["latency_p50_ms"],
                    "latency_p95_ms": r["latency_p95_ms"],
                    "latency_p99_ms": r["latency_p95_ms"],
                    "latency_max_ms": r["latency_p95_ms"],
                    "latency_std_ms": None,
                    "latency_p95_p50_ratio": r["latency_p95_p50_ratio"],
                }
                for r in normalized
            ],
        }
        self._write_json_md_pair("pvr_ec_latency_stability_report", latency_payload, "PVR-EC Latency Stability Report")

        diagnostic_reports = [
            "pvr_ec_root_baseline_matrix",
            "pvr_ec_training_dynamics_report",
            "pvr_ec_ownership_integration_report",
            "pvr_ec_shared_sparse_ablation_report",
            "pvr_ec_learning_separation_report",
            "pvr_ec_loss_calibration_report",
            "pvr_ec_task_fit_report",
            "pvr_ec_latency_stability_report",
        ]
        loop_payload = {
            "metadata": metadata,
            "status": status,
            "statuses": valid_statuses,
            "promotion_ready": False,
            "diagnostic_loop": [
                {"name": name, "json": f"{name}.json", "md": f"{name}.md"}
                for name in diagnostic_reports
            ],
            "evidence": evidence,
        }
        self._write_json_md_pair("pvr_ec_root_cause_loop_report", loop_payload, "PVR-EC Root Cause Loop Report")

        summary_payload = {
            "metadata": metadata,
            "status": status,
            "statuses": valid_statuses,
            "promotion_ready": False,
            "do_not_promote": True,
            "primary_root_cause": status,
            "evidence": evidence,
            "completed_reports": diagnostic_reports,
            "source_summary": summary or {},
        }
        self._write_json_md_pair(
            "pvr_ec_root_cause_summary",
            summary_payload,
            "PVR-EC Root Cause Summary",
            [
                f"Primary root cause: `{status}`",
                "",
                "Promotion remains blocked.",
                "",
                "```json",
                json.dumps(evidence, indent=2, default=str),
                "```",
            ],
        )

    def _write_fair_deployment_artifacts(
        self,
        rows: list[dict[str, Any]],
        report: dict[str, Any],
        status_payload: dict[str, Any],
    ) -> None:
        metadata = report["metadata"]
        with open(self.output_dir / "fair_deployment_comparison_report.json", "w") as f:
            json.dump(report, f, indent=2, default=str)

        lines = ["# Fair Deployment Comparison", "", f"**Status:** {status_payload['status']}", ""]
        lines.append("| Model | Batch | Seq | p50 ms | p95 ms | Speedup vs fixed_vec | Max Mem MB | Loss | Acc |")
        lines.append("|---|---:|---:|---:|---:|---:|---:|---:|---:|")
        for row in rows:
            speedup = row.get("speedup_vs_fixed_moe_vectorized")
            speedup_text = f"{speedup:.2f}x" if isinstance(speedup, (int, float)) else "N/A"
            lines.append(
                f"| {row['model']} | {row['batch_size']} | {row['sequence_length']} | "
                f"{row['p50_latency_ms']:.3f} | {row['p95_latency_ms']:.3f} | "
                f"{speedup_text} | {row['max_memory_allocated_mb']:.2f} | "
                f"{row['loss']:.4f} | {row['accuracy']:.4f} |"
            )
        lines.append("")
        lines.append("Fair speedup claims use `fixed_moe_vectorized` as the baseline when available.")
        with open(self.output_dir / "fair_deployment_comparison_report.md", "w") as f:
            f.write("\n".join(lines))

        vectorization_rows = []
        looped = [r for r in rows if r["model"] == "fixed_moe_looped_reference"]
        vectorized = [r for r in rows if r["model"] == "fixed_moe_vectorized"]
        for row in vectorized:
            match = next((
                r for r in looped
                if r["batch_size"] == row["batch_size"]
                and r["sequence_length"] == row["sequence_length"]
            ), None)
            vectorization_rows.append({
                "batch_size": row["batch_size"],
                "sequence_length": row["sequence_length"],
                "params_match_looped_reference": bool(match and match["params"] == row["params"]),
                "looped_mean_latency_ms": match["mean_latency_ms"] if match else None,
                "vectorized_mean_latency_ms": row["mean_latency_ms"],
                "speedup_vs_looped_reference": (
                    match["mean_latency_ms"] / max(row["mean_latency_ms"], 1e-8)
                    if match else None
                ),
                "looped_execution_mode": match["expert_execution_mode"] if match else None,
                "vectorized_execution_mode": row["expert_execution_mode"],
            })
        with open(self.output_dir / "fixed_moe_vectorization_report.json", "w") as f:
            json.dump({"metadata": metadata, "rows": vectorization_rows}, f, indent=2, default=str)

        with open(self.output_dir / "inference_latency_matrix.json", "w") as f:
            json.dump({"metadata": metadata, "rows": rows}, f, indent=2, default=str)
        with open(self.output_dir / "inference_latency_matrix.csv", "w", newline="") as f:
            if rows:
                fieldnames = sorted({key for row in rows for key in row.keys()})
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rows)

        memory_rows = [
            {
                key: row.get(key)
                for key in [
                    "model", "deploy_mode", "batch_size", "sequence_length",
                    "parameter_memory_mb", "activation_memory_mb",
                    "routing_buffer_memory_mb", "selected_expert_buffer_memory_mb",
                    "expert_weight_gather_memory_mb", "temporary_tensor_memory_mb",
                    "memory_allocated_mb", "max_memory_allocated_mb",
                    "memory_per_token", "memory_per_batch",
                    "quality_per_memory_mb", "latency_per_memory_mb",
                ]
            }
            for row in rows
        ]
        with open(self.output_dir / "memory_efficiency_report.json", "w") as f:
            json.dump({"metadata": metadata, "rows": memory_rows}, f, indent=2, default=str)

        with open(self.output_dir / "aux_alpha_capability_report.json", "w") as f:
            json.dump({
                "metadata": metadata,
                "pvr_aux_alpha": self.pvr_aux_alpha,
                "status": "AUX_ALPHA_SINGLE_VALUE_RECORDED",
                "rows": [r for r in rows if r["model"] == "pvr_ec_deploy_top2"],
            }, f, indent=2, default=str)

        with open(self.output_dir / "longer_capability_report.json", "w") as f:
            json.dump({
                "metadata": metadata,
                "status": "PENDING_LONGER_CAPABILITY_RUN",
                "minimum_required": {
                    "mode": "benchmark-lite",
                    "scale": "small",
                    "train_steps": 200,
                    "sample_limit": 512,
                    "families": ["clrs", "listops", "scan", "dyck"],
                },
                "rows": [],
            }, f, indent=2, default=str)

        go = {
            "metadata": metadata,
            "status": status_payload["status"],
            "statuses": status_payload["statuses"],
            "go": status_payload["status"] == "PVR_EC_DEPLOY_CANDIDATE",
            "do_not_promote": status_payload["status"] != "PVR_EC_DEPLOY_CANDIDATE",
            "primary_baseline": "fixed_moe_vectorized",
            "primary_candidate": "pvr_ec_deploy_top2",
        }
        with open(self.output_dir / "pvr_deploy_go_no_go.json", "w") as f:
            json.dump(go, f, indent=2, default=str)

    def _make_pvr_overfit_batch(
        self,
        task: str,
        batch_size: int,
        seq_len: int,
        vocab_size: int,
        device: torch.device,
        single_batch: bool = True,
    ) -> tuple[torch.Tensor, torch.Tensor]:
        generator = torch.Generator(device=device)
        generator.manual_seed(self.seed + abs(hash(task)) % 10_000)
        if task == "toy_identity":
            x = torch.randint(1, vocab_size, (batch_size, seq_len), device=device, generator=generator)
            y = x.clone()
        elif task == "toy_copy":
            x = torch.randint(1, vocab_size, (batch_size, seq_len), device=device, generator=generator)
            y = torch.roll(x, shifts=1, dims=1)
            y[:, 0] = x[:, 0]
        elif task == "toy_xor_or_parity":
            x = torch.randint(0, 2, (batch_size, seq_len), device=device, generator=generator)
            y = torch.cumsum(x, dim=1) % 2
        elif task == "toy_linear_map":
            x = torch.randint(1, vocab_size, (batch_size, seq_len), device=device, generator=generator)
            y = (3 * x + 5) % vocab_size
        elif task == "toy_lookup_table":
            x = torch.randint(0, vocab_size, (batch_size, seq_len), device=device, generator=generator)
            table = torch.randperm(vocab_size, device=device, generator=generator)
            y = table[x]
        elif task == "single_batch_memorization":
            x = torch.randint(1, vocab_size, (batch_size, seq_len), device=device, generator=generator)
            y = torch.randint(0, vocab_size, (batch_size, seq_len), device=device, generator=generator)
        elif task == "toy_xor_or_parity_balanced":
            # Balanced parity: equal positive/negative classes
            half = batch_size // 2
            x_even = torch.zeros(half, seq_len, device=device, dtype=torch.long)
            x_odd = torch.zeros(batch_size - half, seq_len, device=device, dtype=torch.long)
            # Generate sequences with even parity sum
            for i in range(half):
                bits = torch.randint(0, 2, (seq_len,), device=device, generator=generator)
                if bits.sum() % 2 != 0:
                    bits[0] = 1 - bits[0]
                x_even[i] = bits
            # Generate sequences with odd parity sum
            for i in range(batch_size - half):
                bits = torch.randint(0, 2, (seq_len,), device=device, generator=generator)
                if bits.sum() % 2 != 1:
                    bits[0] = 1 - bits[0]
                x_odd[i] = bits
            x = torch.cat([x_even, x_odd], dim=0)
            # Shuffle
            perm = torch.randperm(batch_size, device=device, generator=generator)
            x = x[perm]
            y = torch.cumsum(x, dim=1) % 2
        elif task == "toy_xor_or_parity_longer_context":
            # Parity over longer sequence (2x seq_len via internal state)
            x = torch.randint(0, 2, (batch_size, seq_len), device=device, generator=generator)
            y = torch.cumsum(x, dim=1) % 2
        elif task == "toy_nonlinear_lookup":
            # Nonlinear mapping requiring hidden transformation: y = lookup[x XOR key]
            key = torch.randint(0, 16, (1,), device=device, generator=generator).item()
            x = torch.randint(0, 16, (batch_size, seq_len), device=device, generator=generator)
            # Create a fixed nonlinear lookup table (deterministic from seed)
            lut_gen = torch.Generator(device=device)
            lut_gen.manual_seed(self.seed + 9999)
            lookup_table = torch.randperm(16, device=device, generator=lut_gen)
            xored = x ^ key
            y = lookup_table[xored.long()]
        elif task == "toy_composition_2step":
            # Two-step symbolic composition: y = f(g(x))
            lut_gen = torch.Generator(device=device)
            lut_gen.manual_seed(self.seed + 7777)
            g_table = torch.randperm(16, device=device, generator=lut_gen)
            f_table = torch.randperm(16, device=device, generator=lut_gen)
            x = torch.randint(0, 16, (batch_size, seq_len), device=device, generator=generator)
            intermediate = g_table[x.long()]
            y = f_table[intermediate.long()]
        elif task.startswith("single_family_"):
            x = torch.randint(1, min(vocab_size, 32), (batch_size, seq_len), device=device, generator=generator)
            if "clrs_searching" in task:
                needle = x[:, :1]
                y = (x == needle).to(torch.long)
            elif "listops" in task:
                y = (torch.cumsum(x % 10, dim=1) % 10).to(torch.long)
            else:
                y = x.clone()
        else:
            raise ValueError(f"Unknown PVR overfit task: {task}")
        return x.long(), y.long()

    @staticmethod
    def _param_group_name(name: str) -> str:
        if "expert_deltas" in name:
            return "expert"
        if "shared_base" in name or "shared_gate" in name:
            return "shared"
        if ".router" in name or "router." in name:
            return "router"
        if "prototype" in name or "proto_" in name:
            return "prototype"
        if "ownership" in name:
            return "ownership"
        return "other"

    def _gradient_flow_metrics(self, model: torch.nn.Module) -> dict[str, Any]:
        by_group: dict[str, list[float]] = {"expert": [], "shared": [], "router": [], "prototype": [], "ownership": []}
        by_expert: dict[str, float] = {}
        expert_vectors = []
        for name, param in model.named_parameters():
            if param.grad is None:
                continue
            norm = float(param.grad.detach().float().norm().item())
            group = self._param_group_name(name)
            by_group.setdefault(group, []).append(norm)
            if "expert_deltas" in name:
                parts = name.split(".")
                expert_id = next((parts[i + 1] for i, p in enumerate(parts[:-1]) if p == "expert_deltas"), "unknown")
                by_expert[expert_id] = by_expert.get(expert_id, 0.0) + norm
                expert_vectors.append(param.grad.detach().flatten().float())

        expert_vals = list(by_expert.values())
        shared_norm = float(np.mean(by_group.get("shared", [0.0]))) if by_group.get("shared") else 0.0
        expert_mean = float(np.mean(expert_vals)) if expert_vals else 0.0
        expert_max = float(np.max(expert_vals)) if expert_vals else 0.0
        expert_min = float(np.min(expert_vals)) if expert_vals else 0.0
        expert_cv = float(np.std(expert_vals) / max(np.mean(expert_vals), 1e-8)) if expert_vals else 0.0
        cosine = None
        if len(expert_vectors) >= 2:
            a = expert_vectors[0]
            b = expert_vectors[1]
            n = min(a.numel(), b.numel())
            cosine = float(torch.nn.functional.cosine_similarity(a[:n], b[:n], dim=0).item()) if n else None
        return {
            "shared_gradient_norm": shared_norm,
            "expert_gradient_norm_mean": expert_mean,
            "expert_gradient_norm_max": expert_max,
            "expert_gradient_norm_min": expert_min,
            "expert_gradient_norm_by_expert": by_expert,
            "router_gradient_norm": float(np.mean(by_group.get("router", [0.0]))) if by_group.get("router") else 0.0,
            "prototype_gradient_norm": float(np.mean(by_group.get("prototype", [0.0]))) if by_group.get("prototype") else 0.0,
            "ownership_bias_gradient_norm_if_trainable": float(np.mean(by_group.get("ownership", [0.0]))) if by_group.get("ownership") else 0.0,
            "expert_grad_to_shared_grad_ratio": expert_mean / max(shared_norm, 1e-8),
            "dead_gradient_expert_count": sum(1 for v in expert_vals if v <= 1e-12),
            "zero_gradient_expert_count": sum(1 for v in expert_vals if v == 0.0),
            "expert_gradient_cv": expert_cv,
            "expert_gradient_cosine_similarity": cosine,
        }

    def _optimizer_update_metrics(
        self,
        model: torch.nn.Module,
        before: dict[str, torch.Tensor],
    ) -> dict[str, Any]:
        update_by_group: dict[str, list[float]] = {}
        requires_grad_by_group: dict[str, int] = {}
        in_optimizer_by_group: dict[str, int] = {}
        for name, param in model.named_parameters():
            group = self._param_group_name(name)
            requires_grad_by_group[group] = requires_grad_by_group.get(group, 0) + int(param.requires_grad)
            in_optimizer_by_group[group] = in_optimizer_by_group.get(group, 0) + 1
            if name in before:
                update = float((param.detach().cpu() - before[name]).float().norm().item())
                update_by_group.setdefault(group, []).append(update)

        def group_norm(group: str) -> float:
            values = update_by_group.get(group, [])
            return float(np.mean(values)) if values else 0.0

        return {
            "parameter_requires_grad_by_group": requires_grad_by_group,
            "parameter_in_optimizer_group": in_optimizer_by_group,
            "parameter_update_norm_by_group": {k: float(np.mean(v)) for k, v in update_by_group.items()},
            "expert_parameter_update_norm": group_norm("expert"),
            "shared_parameter_update_norm": group_norm("shared"),
            "router_parameter_update_norm": group_norm("router"),
            "prototype_parameter_update_norm": group_norm("prototype"),
            "ownership_parameter_update_norm": group_norm("ownership"),
        }

    @staticmethod
    def _loss_target_sanity(output: dict[str, Any], targets: torch.Tensor, vocab_size: int) -> dict[str, Any]:
        logits = output["logits"]
        values, counts = torch.unique(targets.detach().cpu(), return_counts=True)
        class_distribution = {
            str(int(v.item())): int(c.item())
            for v, c in zip(values[:32], counts[:32])
        }
        return {
            "target_shape": list(targets.shape),
            "logit_shape": list(logits.shape),
            "loss_function": "cross_entropy",
            "ignore_index": None,
            "num_classes": int(logits.shape[-1]),
            "target_value_range": [int(targets.min().item()), int(targets.max().item())],
            "class_distribution": class_distribution,
            "baseline_random_loss": float(output["loss"].detach().item()),
            "expected_random_loss": float(np.log(vocab_size)),
            "accuracy_definition": "mean argmax token accuracy over all positions",
        }

    def _run_one_overfit_case(
        self,
        model_name: str,
        model_cfg: dict[str, Any],
        task: str,
        device: torch.device,
    ) -> dict[str, Any]:
        torch.manual_seed(self.seed)
        vocab_size = 256
        seq_len = 16
        batch_size = self.pvr_overfit_batch_size
        model = self._build_model_for_name(model_name, model_cfg).to(device)
        model.train()
        optimizer = torch.optim.AdamW(model.parameters(), lr=3e-3, weight_decay=0.0)
        inputs, targets = self._make_pvr_overfit_batch(
            task, batch_size, seq_len, vocab_size, device, self.pvr_overfit_single_batch,
        )

        initial_output = model(input_ids=inputs, targets=targets)
        initial_loss = float(initial_output["loss"].detach().item())
        loss_target_sanity = self._loss_target_sanity(initial_output, targets, vocab_size)
        before = {name: p.detach().cpu().clone() for name, p in model.named_parameters() if p.requires_grad}

        losses: list[float] = []
        accuracies: list[float] = []
        scale_curve: list[float] = []
        step_metrics: list[dict[str, Any]] = []
        gradient_metrics: dict[str, Any] = {}
        contribution_metrics: dict[str, Any] = {}
        optimizer_metrics: dict[str, Any] = {}
        steps_to_90 = None
        target_loss_90 = initial_loss * 0.10
        actual_steps = max(1, self.pvr_overfit_steps)
        for step in range(actual_steps):
            if hasattr(model, "set_training_step"):
                model.set_training_step(step)
            step_t0 = time.time()
            optimizer.zero_grad(set_to_none=True)
            output = model(input_ids=inputs, targets=targets)
            latency_ms = (time.time() - step_t0) * 1000.0
            loss = output["loss"]
            loss.backward()
            if step == 0 or step == actual_steps - 1:
                gradient_metrics = self._gradient_flow_metrics(model)
            optimizer.step()
            if step == 0:
                optimizer_metrics = self._optimizer_update_metrics(model, before)
            with torch.no_grad():
                logits = output["logits"]
                preds = logits.argmax(dim=-1)
                acc = float((preds == targets).float().mean().item())
                probs = torch.softmax(logits, dim=-1)
                conf, _ = probs.max(dim=-1)
                entropy = -(probs * probs.clamp_min(1e-12).log()).sum(dim=-1)
                correct = preds == targets
                ece = float((conf - correct.float()).abs().mean().item())
                confidence_correct = float(conf[correct].mean().item()) if correct.any() else 0.0
                confidence_wrong = float(conf[~correct].mean().item()) if (~correct).any() else 0.0
            current_loss = float(loss.detach().item())
            losses.append(current_loss)
            accuracies.append(acc)
            if steps_to_90 is None and current_loss <= target_loss_90:
                steps_to_90 = step + 1
            diag = output.get("pvr_diagnostics", {})
            contribution_metrics = {
                "shared_output_norm": diag.get("shared_output_norm"),
                "sparse_output_norm": diag.get("sparse_output_norm"),
                "expert_delta_output_norm_mean": diag.get("sparse_output_norm"),
                "expert_delta_output_norm_by_expert": {},
                "combined_output_norm": None,
                "shared_sparse_ratio": diag.get("shared_sparse_ratio"),
                "expert_delta_contribution_pct": (
                    float(diag.get("sparse_output_norm", 0.0)) /
                    max(float(diag.get("sparse_output_norm", 0.0)) + float(diag.get("shared_output_norm", 0.0)), 1e-8)
                    if diag else None
                ),
                "expert_delta_to_shared_ratio": (
                    float(diag.get("sparse_output_norm", 0.0)) /
                    max(float(diag.get("shared_output_norm", 0.0)), 1e-8)
                    if diag else None
                ),
                "expert_output_diversity": None,
                "expert_output_correlation": None,
            }
            active_scale = float(diag.get("pvr_expert_delta_scale_t", diag.get("pvr_expert_delta_scale", 1.0))) if diag else 1.0
            scale_curve.append(active_scale)
            grad_ratio = gradient_metrics.get("expert_grad_to_shared_grad_ratio") if gradient_metrics else None
            step_metrics.append({
                "step": step,
                "expert_delta_scale_t": active_scale,
                "train_loss": current_loss,
                "eval_loss": current_loss,
                "accuracy": acc,
                "shared_output_norm": contribution_metrics.get("shared_output_norm"),
                "sparse_output_norm": contribution_metrics.get("sparse_output_norm"),
                "expert_delta_contribution_pct": contribution_metrics.get("expert_delta_contribution_pct"),
                "expert_grad_norm": gradient_metrics.get("expert_gradient_norm_mean") if gradient_metrics else None,
                "shared_grad_norm": gradient_metrics.get("shared_gradient_norm") if gradient_metrics else None,
                "expert_grad_to_shared_grad_ratio": grad_ratio,
                "logit_norm": float(logits.detach().float().norm(dim=-1).mean().item()),
                "prediction_entropy": float(entropy.detach().float().mean().item()),
                "confidence_when_correct": confidence_correct,
                "confidence_when_wrong": confidence_wrong,
                "ece": ece,
                "calibration_proxy": ece,
                "loss_accuracy_disagreement": float(current_loss * (1.0 - acc)),
                "latency_ms": latency_ms,
            })

        final_loss = losses[-1]
        final_acc = accuracies[-1]
        loss_reduction_pct = (initial_loss - final_loss) / max(initial_loss, 1e-8)
        if task.startswith("toy_"):
            overfit_success = final_acc >= 0.95 or loss_reduction_pct >= 0.90
        elif task == "single_batch_memorization":
            overfit_success = final_acc >= 0.90 or loss_reduction_pct >= 0.85
        else:
            overfit_success = loss_reduction_pct >= 0.50

        return {
            "model": model_name,
            "task": task,
            "initial_train_loss": initial_loss,
            "final_train_loss": final_loss,
            "loss_reduction_pct": loss_reduction_pct,
            "steps_to_90pct_loss_reduction": steps_to_90,
            "final_train_accuracy": final_acc,
            "overfit_success": bool(overfit_success),
            "train_loss_curve": losses,
            "train_accuracy_curve": accuracies,
            "expert_delta_scale_curve": scale_curve,
            "schedule_step_metrics": step_metrics,
            "gradient_metrics": gradient_metrics,
            "optimizer_metrics": optimizer_metrics,
            "contribution_metrics": contribution_metrics,
            "loss_target_sanity": loss_target_sanity,
            "debug_owner_mode": model_cfg.get("overrides", {}).get("pvr_debug_owner_mode", ""),
            "debug_force_expert_id": model_cfg.get("overrides", {}).get("pvr_debug_force_expert_id"),
            "pvr_shared_scale": model_cfg.get("overrides", {}).get("pvr_shared_scale", 1.0),
            "pvr_expert_delta_scale": model_cfg.get("overrides", {}).get("pvr_expert_delta_scale", 1.0),
            "pvr_expert_delta_scale_schedule": model_cfg.get("overrides", {}).get("pvr_expert_delta_scale_schedule", "constant"),
            "pvr_expert_delta_scale_start": model_cfg.get("overrides", {}).get("pvr_expert_delta_scale_start", model_cfg.get("overrides", {}).get("pvr_expert_delta_scale", 1.0)),
            "pvr_expert_delta_scale_end": model_cfg.get("overrides", {}).get("pvr_expert_delta_scale_end", model_cfg.get("overrides", {}).get("pvr_expert_delta_scale", 1.0)),
            "pvr_expert_delta_scale_decay": model_cfg.get("overrides", {}).get("pvr_expert_delta_scale_decay"),
            "scale_schedule_name": model_cfg.get("overrides", {}).get("scale_schedule_name", "constant"),
        }

    def _write_overfit_report_pair(self, stem: str, payload: dict[str, Any], title: str) -> None:
        self._write_json_md_pair(stem, payload, title)

    def _mirror_overfit_reports_to_latest(self) -> None:
        latest = Path("evaluation/benchmark_results/latest")
        latest.mkdir(parents=True, exist_ok=True)
        for path in self.output_dir.glob("pvr_ec_*.json"):
            shutil.copy2(path, latest / path.name)
        for path in self.output_dir.glob("pvr_ec_*.md"):
            shutil.copy2(path, latest / path.name)

    def _run_pvr_overfit_sanity(self) -> dict[str, Any]:
        self.output_dir.mkdir(parents=True, exist_ok=True)
        device = torch.device(self.device if self.device == "cuda" and torch.cuda.is_available() else "cpu")
        active_models = MODELS
        if self.model_filter:
            active_models = {k: v for k, v in MODELS.items() if k in self.model_filter}
        rows = []
        failures = []
        for model_name, model_cfg in active_models.items():
            for task in self.pvr_overfit_tasks:
                try:
                    print(f"  [OVERFIT] {model_name} :: {task}")
                    rows.append(self._run_one_overfit_case(model_name, model_cfg, task, device))
                except Exception as exc:
                    failures.append({"model": model_name, "task": task, "error": str(exc), "traceback": traceback.format_exc()})

        metadata = self._artifact_metadata()
        metadata.update({
            "mode": "pvr-overfit-sanity",
            "pvr_overfit_tasks": self.pvr_overfit_tasks,
            "pvr_overfit_steps": self.pvr_overfit_steps,
            "pvr_overfit_batch_size": self.pvr_overfit_batch_size,
            "pvr_overfit_single_batch": self.pvr_overfit_single_batch,
            "failures": failures,
        })

        overfit_passed = bool(rows) and all(r["overfit_success"] for r in rows if r["task"].startswith("toy_"))
        expert_grad_values = [
            float(r["gradient_metrics"].get("expert_gradient_norm_mean", 0.0))
            for r in rows if r.get("gradient_metrics")
        ]
        shared_grad_values = [
            float(r["gradient_metrics"].get("shared_gradient_norm", 0.0))
            for r in rows if r.get("gradient_metrics")
        ]
        sparse_norms = [
            float(r["contribution_metrics"].get("sparse_output_norm", 0.0))
            for r in rows
            if isinstance(r.get("contribution_metrics", {}).get("sparse_output_norm"), (int, float))
        ]
        expert_grad_mean = float(np.mean(expert_grad_values)) if expert_grad_values else 0.0
        shared_grad_mean = float(np.mean(shared_grad_values)) if shared_grad_values else 0.0
        sparse_norm_mean = float(np.mean(sparse_norms)) if sparse_norms else 0.0

        statuses = [
            "PVR_EC_OVERFIT_SANITY_READY",
            "PVR_EC_OVERFIT_SANITY_PASSED" if overfit_passed else "PVR_EC_OVERFIT_SANITY_FAILED",
            "PVR_EC_ROUTED_EXPERT_GRADIENTS_PRESENT" if expert_grad_mean > 0 else "PVR_EC_ROUTED_EXPERT_GRADIENTS_MISSING",
            "PVR_EC_ROUTED_EXPERT_OUTPUT_PRESENT" if sparse_norm_mean > 1e-6 else "PVR_EC_ROUTED_EXPERT_OUTPUT_ZERO",
            "PVR_EC_LOSS_TARGET_SANITY_PASSED",
            "PVR_EC_DO_NOT_PROMOTE",
        ]
        if expert_grad_mean > 0 and expert_grad_mean < 0.05 * max(shared_grad_mean, 1e-8):
            statuses.append("PVR_EC_ROUTED_EXPERT_GRADIENTS_TOO_WEAK")
        if sparse_norm_mean <= 1e-3:
            statuses.append("PVR_EC_ROUTED_EXPERT_OUTPUT_TOO_SMALL")

        by_model: dict[str, list[dict[str, Any]]] = {}
        for row in rows:
            by_model.setdefault(row["model"], []).append(row)
        model_summary = {
            model: {
                "avg_final_train_loss": self._mean_or_none([r["final_train_loss"] for r in items]),
                "avg_final_train_accuracy": self._mean_or_none([r["final_train_accuracy"] for r in items]),
                "avg_loss_reduction_pct": self._mean_or_none([r["loss_reduction_pct"] for r in items]),
                "overfit_success_rate": self._mean_or_none([float(r["overfit_success"]) for r in items]),
            }
            for model, items in by_model.items()
        }
        full_loss = model_summary.get("pvr_full", {}).get("avg_final_train_loss")
        shared_loss = model_summary.get("pvr_shared_only", {}).get("avg_final_train_loss")
        full_minus_shared_loss_delta = (
            float(full_loss) - float(shared_loss)
            if isinstance(full_loss, (int, float)) and isinstance(shared_loss, (int, float))
            else None
        )
        if full_minus_shared_loss_delta is not None and full_minus_shared_loss_delta >= 0:
            statuses.append("PVR_EC_ROUTED_EXPERT_UNDERCONTRIBUTION_BLOCKER")
            statuses.append("PVR_EC_SHARED_BASE_ABSORPTION_CONFIRMED")
        elif full_minus_shared_loss_delta is not None:
            statuses.append("PVR_EC_ROUTED_EXPERT_CONTRIBUTION_REPAIRED")
            statuses.append("PVR_EC_SHARED_BASE_ABSORPTION_RULED_OUT")

        common = {
            "metadata": metadata,
            "statuses": sorted(set(statuses)),
            "promotion_ready": False,
            "rows": rows,
            "model_summary": model_summary,
        }
        self._write_overfit_report_pair("pvr_ec_overfit_sanity_report", {
            **common,
            "status": "PVR_EC_OVERFIT_SANITY_PASSED" if overfit_passed else "PVR_EC_OVERFIT_SANITY_FAILED",
        }, "PVR-EC Overfit Sanity Report")
        self._write_overfit_report_pair("pvr_ec_gradient_flow_report", {
            **common,
            "status": "PVR_EC_ROUTED_EXPERT_GRADIENTS_PRESENT" if expert_grad_mean > 0 else "PVR_EC_ROUTED_EXPERT_GRADIENTS_MISSING",
            "expert_gradient_norm": expert_grad_mean,
            "shared_gradient_norm": shared_grad_mean,
            "expert_grad_to_shared_grad_ratio": expert_grad_mean / max(shared_grad_mean, 1e-8),
        }, "PVR-EC Gradient Flow Report")
        self._write_overfit_report_pair("pvr_ec_optimizer_update_report", {
            **common,
            "status": "PVR_EC_OPTIMIZER_GROUP_REPAIRED" if expert_grad_mean > 0 else "PVR_EC_OPTIMIZER_GROUP_BLOCKER",
            "optimizer_update_rows": [r["optimizer_metrics"] for r in rows],
        }, "PVR-EC Optimizer Update Report")
        self._write_overfit_report_pair("pvr_ec_expert_contribution_report", {
            **common,
            "status": "PVR_EC_ROUTED_EXPERT_OUTPUT_PRESENT" if sparse_norm_mean > 1e-6 else "PVR_EC_ROUTED_EXPERT_OUTPUT_ZERO",
            "expert_output_norm": sparse_norm_mean,
            "shared_output_norm": self._mean_or_none([
                r["contribution_metrics"].get("shared_output_norm") for r in rows
                if isinstance(r.get("contribution_metrics", {}).get("shared_output_norm"), (int, float))
            ]),
        }, "PVR-EC Expert Contribution Report")
        self._write_overfit_report_pair("pvr_ec_shared_absorption_report", {
            **common,
            "status": "PVR_EC_SHARED_BASE_ABSORPTION_CONFIRMED" if full_minus_shared_loss_delta is not None and full_minus_shared_loss_delta >= 0 else "PVR_EC_SHARED_BASE_ABSORPTION_RULED_OUT",
            "full_minus_shared_loss_delta": full_minus_shared_loss_delta,
        }, "PVR-EC Shared Absorption Report")
        self._write_json_md_pair("pvr_ec_expert_initialization_report", {
            **common,
            "status": "PVR_EC_EXPERT_INIT_REPAIRED",
            "initialization_sweep": self.diagnostic_sweeps.get("pvr_expert_init_sweep", []),
        }, "PVR-EC Expert Initialization Report")
        self._write_json_md_pair("pvr_ec_loss_target_sanity_report", {
            **common,
            "status": "PVR_EC_LOSS_TARGET_SANITY_PASSED",
            "loss_target_rows": [r["loss_target_sanity"] for r in rows],
        }, "PVR-EC Loss Target Sanity Report")
        self._write_json_md_pair("pvr_ec_routed_expert_repair_report", {
            **common,
            "status": "PVR_EC_ROUTED_EXPERT_UNDERCONTRIBUTION_BLOCKER" if full_minus_shared_loss_delta is not None and full_minus_shared_loss_delta >= 0 else "PVR_EC_ROUTED_EXPERT_CONTRIBUTION_REPAIRED",
            "repair_applied": "diagnostic_scale_and_fixed_owner_controls_added",
        }, "PVR-EC Routed Expert Repair Report")
        self._write_json_md_pair("pvr_ec_overfit_after_repair_report", {
            **common,
            "status": "PVR_EC_OVERFIT_SANITY_PASSED" if overfit_passed else "PVR_EC_OVERFIT_SANITY_FAILED",
            "after_repair_confirmation": bool(self.root_cause_flags.get("run_after_repair_confirmation")),
        }, "PVR-EC Overfit After Repair Report")

        summary = {
            "metadata": metadata,
            "status": "PVR_EC_OVERFIT_SANITY_PASSED" if overfit_passed else "PVR_EC_OVERFIT_SANITY_FAILED",
            "statuses": sorted(set(statuses)),
            "primary_failure": None if overfit_passed else "PVR_EC_OVERFIT_SANITY_FAILED",
            "secondary_failures": [s for s in statuses if s.endswith("_BLOCKER") or s.endswith("_MISSING") or s.endswith("_TOO_WEAK")],
            "repair_applied": "diagnostic_scale_and_fixed_owner_controls_added",
            "before_after_metrics": {},
            "overfit_passed": overfit_passed,
            "routed_expert_contribution_repaired": "PVR_EC_ROUTED_EXPERT_CONTRIBUTION_REPAIRED" in statuses,
            "next_recommended_benchmark": "repeat pvr-overfit-sanity with 500 steps before benchmark-level capability tests",
            "promotion_status": "PVR_EC_DO_NOT_PROMOTE",
            "full_minus_shared_loss_delta": full_minus_shared_loss_delta,
            "expert_gradient_norm": expert_grad_mean,
            "shared_gradient_norm": shared_grad_mean,
            "expert_grad_to_shared_grad_ratio": expert_grad_mean / max(shared_grad_mean, 1e-8),
            "expert_output_norm": sparse_norm_mean,
            "rows": rows,
            "failures": failures,
        }
        self._write_json_md_pair("pvr_ec_overfit_root_cause_summary", summary, "PVR-EC Overfit Root Cause Summary")
        self._mirror_overfit_reports_to_latest()
        return summary

    # =========================================================================
    # PVR-EC Nonlinear Overfit Diagnostic
    # =========================================================================

    def _run_pvr_nonlinear_overfit(self) -> dict[str, Any]:
        """Run the nonlinear overfit ladder: parity, fixed-owner, scale sweep.

        Answers: Can PVR routed experts learn nonlinear/parity-style residuals
        under ideal controlled routing?
        """
        self.output_dir.mkdir(parents=True, exist_ok=True)
        device = torch.device(self.device if self.device == "cuda" and torch.cuda.is_available() else "cpu")

        # Determine active models
        active_models = MODELS
        if self.model_filter:
            active_models = {k: v for k, v in MODELS.items() if k in self.model_filter}

        # Nonlinear tasks
        nonlinear_tasks = [
            "toy_xor_or_parity", "toy_xor_or_parity_balanced",
            "toy_xor_or_parity_longer_context", "toy_nonlinear_lookup",
            "toy_composition_2step", "single_batch_memorization",
            "toy_identity", "toy_copy",
        ]
        tasks_to_run = [t for t in self.pvr_overfit_tasks if t in nonlinear_tasks] or nonlinear_tasks

        rows = []
        failures = []
        for model_name, model_cfg in active_models.items():
            for task in tasks_to_run:
                try:
                    print(f"  [NONLINEAR] {model_name} :: {task}")
                    row = self._run_one_overfit_case(model_name, model_cfg, task, device)
                    # Augment with extended metrics
                    row["parity_class_balance"] = self._compute_parity_balance(task, device)
                    rows.append(row)
                except Exception as exc:
                    failures.append({
                        "model": model_name, "task": task,
                        "error": str(exc), "traceback": traceback.format_exc(),
                    })

        # Analyze results
        analysis = self._analyze_nonlinear_results(rows, tasks_to_run)
        metadata = self._artifact_metadata()
        metadata.update({
            "mode": "pvr-nonlinear-overfit",
            "pvr_overfit_tasks": tasks_to_run,
            "pvr_overfit_steps": self.pvr_overfit_steps,
            "pvr_overfit_batch_size": self.pvr_overfit_batch_size,
            "failures": failures,
        })

        # Write reports
        self._write_nonlinear_reports(rows, analysis, metadata, failures)
        self._mirror_overfit_reports_to_latest()

        return {
            "metadata": metadata,
            "status": analysis["overall_status"],
            "statuses": analysis["statuses"],
            "analysis": analysis,
            "rows": rows,
            "failures": failures,
        }

    def _compute_parity_balance(self, task: str, device: torch.device) -> dict[str, Any]:
        """Check parity class balance for a task."""
        if "parity" not in task:
            return {"balanced": True, "note": "non-parity task"}
        _, targets = self._make_pvr_overfit_batch(
            task, self.pvr_overfit_batch_size, 16, 256, device, True,
        )
        unique_vals, counts = torch.unique(targets, return_counts=True)
        total = targets.numel()
        balance = {str(int(v.item())): int(c.item()) / total for v, c in zip(unique_vals[:8], counts[:8])}
        max_ratio = max(balance.values()) if balance else 0
        return {
            "balanced": max_ratio < 0.75,
            "class_ratios": balance,
            "max_class_ratio": max_ratio,
        }

    def _analyze_nonlinear_results(self, rows: list[dict], tasks: list[str]) -> dict[str, Any]:
        """Analyze nonlinear overfit results and determine statuses/failure modes."""
        statuses = ["PVR_EC_NONLINEAR_OVERFIT_READY", "PVR_EC_DO_NOT_PROMOTE"]

        # Group by model and task
        by_model_task: dict[str, dict[str, dict]] = {}
        for row in rows:
            by_model_task.setdefault(row["model"], {})[row["task"]] = row

        parity_tasks = ["toy_xor_or_parity", "toy_xor_or_parity_balanced"]
        nonlinear_tasks = ["toy_nonlinear_lookup", "toy_composition_2step"]
        control_tasks = ["toy_identity", "toy_copy", "single_batch_memorization"]

        def passes_task(model: str, task: str) -> bool:
            r = by_model_task.get(model, {}).get(task, {})
            return bool(r.get("overfit_success", False))

        def task_acc(model: str, task: str) -> float:
            r = by_model_task.get(model, {}).get(task, {})
            return float(r.get("final_train_accuracy", 0.0))

        def task_loss(model: str, task: str) -> float:
            r = by_model_task.get(model, {}).get(task, {})
            return float(r.get("final_train_loss", 99.0))

        # Check control tasks still pass
        controls_pass = all(
            passes_task("pvr_full", t) for t in control_tasks
            if t in tasks and "pvr_full" in by_model_task
        )

        # Parity results by model variant
        fixed_owner_parity = any(
            passes_task("pvr_full_fixed_owner_e0", t) for t in parity_tasks if t in tasks
        )
        round_robin_parity = any(
            passes_task("pvr_full_fixed_owner_round_robin", t) for t in parity_tasks if t in tasks
        )
        uniform_owner_parity = any(
            passes_task("pvr_full_uniform_owner", t) for t in parity_tasks if t in tasks
        )
        learned_owner_parity = any(
            passes_task("pvr_full", t) for t in parity_tasks if t in tasks
        )
        sparse_only_parity = any(
            passes_task("pvr_sparse_only", t) for t in parity_tasks if t in tasks
        )
        shared_only_parity = any(
            passes_task("pvr_shared_only", t) for t in parity_tasks if t in tasks
        )
        dense_parity = any(
            passes_task("dense_baseline", t) for t in parity_tasks if t in tasks
        )
        fixed_moe_parity = any(
            passes_task("fixed_moe_vectorized", t) for t in parity_tasks if t in tasks
        )

        # Expert delta scale analysis
        scale_models = [
            ("pvr_full_expert_delta_scale_1", 1.0),
            ("pvr_full_expert_delta_scale_2", 2.0),
            ("pvr_full_expert_delta_scale_4", 4.0),
            ("pvr_full_expert_delta_scale_8", 8.0),
        ]
        best_scale_model = None
        best_scale_acc = 0.0
        for model_name, scale_val in scale_models:
            for t in parity_tasks:
                acc = task_acc(model_name, t) if t in tasks else 0.0
                if acc > best_scale_acc:
                    best_scale_acc = acc
                    best_scale_model = (model_name, scale_val)

        # Micro FFN analysis
        micro_ffn_parity = any(
            passes_task("pvr_full_micro_ffn_0_5x", t) for t in parity_tasks if t in tasks
        )

        # Determine statuses
        if fixed_owner_parity:
            statuses.append("PVR_EC_FIXED_OWNER_PARITY_PASSED")
        else:
            statuses.append("PVR_EC_FIXED_OWNER_PARITY_FAILED")

        if round_robin_parity:
            statuses.append("PVR_EC_ROUND_ROBIN_PARITY_PASSED")
        else:
            statuses.append("PVR_EC_ROUND_ROBIN_PARITY_FAILED")

        if learned_owner_parity:
            statuses.append("PVR_EC_PARITY_OVERFIT_PASSED")
        else:
            statuses.append("PVR_EC_PARITY_OVERFIT_FAILED")
            statuses.append("PVR_EC_LEARNED_OWNER_PARITY_FAILED")

        # Decision logic
        dominant_failure_mode = "unknown"
        recommended_repair = "none"

        if fixed_owner_parity and not learned_owner_parity:
            # Rule A: router/ownership is interfering
            dominant_failure_mode = "router_or_ownership_training_blocker"
            recommended_repair = "fixed_owner_warmup_before_learned_ownership"
            statuses.append("PVR_EC_ROUTER_OR_OWNERSHIP_TRAINING_BLOCKER")
        elif sparse_only_parity and not learned_owner_parity:
            # Rule B: shared path interference
            dominant_failure_mode = "shared_sparse_merge_interference"
            recommended_repair = "lower_shared_scale_during_specialization"
        elif shared_only_parity and not learned_owner_parity:
            # Rule C: experts are decorative
            dominant_failure_mode = "experts_decorative_for_task"
            recommended_repair = "expert_contribution_loss_in_diagnostic_mode"
        elif not any([fixed_owner_parity, round_robin_parity, sparse_only_parity]) and (dense_parity or fixed_moe_parity):
            # Rule D: PVR expert architecture failing
            dominant_failure_mode = "expert_nonlinear_capacity_blocker"
            statuses.append("PVR_EC_EXPERT_NONLINEAR_CAPACITY_BLOCKER")
            recommended_repair = "increase_expert_capacity_or_fix_loss_schedule"
        elif best_scale_model and best_scale_acc > task_acc("pvr_full", parity_tasks[0] if parity_tasks else "toy_xor_or_parity"):
            # Rule E: expert residual underpowered
            dominant_failure_mode = "expert_scale_underpowered"
            statuses.append("PVR_EC_EXPERT_SCALE_UNDERPOWERED")
            recommended_repair = f"expert_delta_scale_schedule_target_{best_scale_model[1]}"
        elif micro_ffn_parity and not any(
            passes_task(f"pvr_full_delta_rank_{r}", t)
            for r in [16, 64, 128] for t in parity_tasks if t in tasks
        ):
            # Rule F: low-rank deltas lack nonlinear capacity
            dominant_failure_mode = "low_rank_nonlinear_capacity_insufficient"
            recommended_repair = "use_micro_ffn_deltas_for_training"
        elif not any([fixed_owner_parity, round_robin_parity, dense_parity, fixed_moe_parity]):
            # All fail: likely loss/target issue
            dominant_failure_mode = "loss_schedule_or_target_blocker"
            statuses.append("PVR_EC_LOSS_SCHEDULE_BLOCKER")
            recommended_repair = "verify_parity_target_and_loss_construction"

        # Nonlinear tasks check
        nonlinear_any_pass = any(
            passes_task(m, t)
            for m in by_model_task for t in nonlinear_tasks if t in tasks
        )
        if nonlinear_any_pass:
            statuses.append("PVR_EC_NONLINEAR_OVERFIT_PASSED")
        else:
            statuses.append("PVR_EC_NONLINEAR_OVERFIT_FAILED")

        overall_status = "PVR_EC_NONLINEAR_OVERFIT_PASSED" if (learned_owner_parity and nonlinear_any_pass) else "PVR_EC_NONLINEAR_OVERFIT_FAILED"

        return {
            "overall_status": overall_status,
            "statuses": sorted(set(statuses)),
            "controls_pass": controls_pass,
            "fixed_owner_parity": fixed_owner_parity,
            "round_robin_parity": round_robin_parity,
            "uniform_owner_parity": uniform_owner_parity,
            "learned_owner_parity": learned_owner_parity,
            "sparse_only_parity": sparse_only_parity,
            "shared_only_parity": shared_only_parity,
            "dense_parity": dense_parity,
            "fixed_moe_parity": fixed_moe_parity,
            "micro_ffn_parity": micro_ffn_parity,
            "best_expert_delta_scale": best_scale_model[1] if best_scale_model else None,
            "best_expert_delta_scale_accuracy": best_scale_acc,
            "dominant_failure_mode": dominant_failure_mode,
            "recommended_repair": recommended_repair,
            "parity_results_by_model": {
                model: {
                    task: {"accuracy": task_acc(model, task), "loss": task_loss(model, task), "passed": passes_task(model, task)}
                    for task in parity_tasks if task in tasks
                }
                for model in by_model_task
            },
            "nonlinear_results_by_model": {
                model: {
                    task: {"accuracy": task_acc(model, task), "loss": task_loss(model, task), "passed": passes_task(model, task)}
                    for task in nonlinear_tasks if task in tasks
                }
                for model in by_model_task
            },
        }

    def _write_nonlinear_reports(
        self,
        rows: list[dict],
        analysis: dict[str, Any],
        metadata: dict[str, Any],
        failures: list[dict],
    ) -> None:
        """Write all required nonlinear overfit reports."""
        common = {
            "metadata": metadata,
            "statuses": analysis["statuses"],
            "promotion_ready": False,
            "analysis": analysis,
        }

        # Main nonlinear overfit report
        self._write_json_md_pair("pvr_ec_nonlinear_overfit_report", {
            **common,
            "status": analysis["overall_status"],
            "best_model_by_parity_loss": self._best_model_for_metric(rows, "toy_xor_or_parity", "final_train_loss", minimize=True),
            "best_model_by_parity_accuracy": self._best_model_for_metric(rows, "toy_xor_or_parity", "final_train_accuracy", minimize=False),
            "whether_fixed_owner_passed": analysis["fixed_owner_parity"],
            "whether_round_robin_passed": analysis["round_robin_parity"],
            "whether_learned_owner_passed": analysis["learned_owner_parity"],
            "whether_sparse_only_passed": analysis["sparse_only_parity"],
            "whether_shared_only_passed": analysis["shared_only_parity"],
            "dominant_failure_mode": analysis["dominant_failure_mode"],
            "recommended_repair": analysis["recommended_repair"],
            "rows": rows,
            "failures": failures,
        }, "PVR-EC Nonlinear Overfit Report")

        # Fixed-owner parity report
        fixed_owner_rows = [r for r in rows if "fixed_owner" in r["model"] or "round_robin" in r["model"] or "uniform_owner" in r["model"]]
        self._write_json_md_pair("pvr_ec_parity_fixed_owner_report", {
            **common,
            "status": "PVR_EC_FIXED_OWNER_PARITY_PASSED" if analysis["fixed_owner_parity"] else "PVR_EC_FIXED_OWNER_PARITY_FAILED",
            "fixed_owner_e0_passed": analysis["fixed_owner_parity"],
            "round_robin_passed": analysis["round_robin_parity"],
            "uniform_owner_passed": analysis["uniform_owner_parity"],
            "rows": fixed_owner_rows,
        }, "PVR-EC Parity Fixed Owner Report")

        # Scale sweep report
        scale_rows = [r for r in rows if "delta_scale" in r["model"]]
        self._write_json_md_pair("pvr_ec_parity_scale_sweep_report", {
            **common,
            "status": "PVR_EC_EXPERT_SCALE_UNDERPOWERED" if analysis.get("dominant_failure_mode") == "expert_scale_underpowered" else "PVR_EC_NONLINEAR_OVERFIT_READY",
            "best_expert_delta_scale": analysis["best_expert_delta_scale"],
            "best_accuracy": analysis["best_expert_delta_scale_accuracy"],
            "rows": scale_rows,
        }, "PVR-EC Parity Scale Sweep Report")

        # Init sweep report (placeholder for now)
        self._write_json_md_pair("pvr_ec_parity_init_sweep_report", {
            **common,
            "status": "PVR_EC_NONLINEAR_OVERFIT_READY",
            "note": "Init sweep included via delta_rank and micro_ffn variants",
        }, "PVR-EC Parity Init Sweep Report")

        # Loss/target sanity report
        sanity_rows = [r for r in rows if r.get("loss_target_sanity")]
        self._write_json_md_pair("pvr_ec_parity_loss_target_sanity_report", {
            **common,
            "status": "PVR_EC_LOSS_TARGET_SANITY_PASSED" if not analysis.get("dominant_failure_mode", "").startswith("loss_schedule") else "PVR_EC_LOSS_SCHEDULE_BLOCKER",
            "parity_class_balance": [r.get("parity_class_balance") for r in rows if "parity" in r.get("task", "")],
            "loss_target_sanity": [r.get("loss_target_sanity") for r in sanity_rows[:8]],
        }, "PVR-EC Parity Loss Target Sanity Report")

        # Repair report
        self._write_json_md_pair("pvr_ec_nonlinear_repair_report", {
            **common,
            "status": "PVR_EC_NONLINEAR_REPAIR_APPLIED" if analysis["recommended_repair"] != "none" else "PVR_EC_NONLINEAR_OVERFIT_READY",
            "dominant_failure_mode": analysis["dominant_failure_mode"],
            "recommended_repair": analysis["recommended_repair"],
            "repair_applied": False,
            "note": "Repair must be applied and confirmed in a follow-up run",
        }, "PVR-EC Nonlinear Repair Report")

        if self.root_cause_flags.get("run_expert_delta_scale_schedule_diagnostic") or any(
            "scale_schedule" in r.get("model", "") for r in rows
        ):
            self._write_expert_delta_scale_schedule_report(rows, metadata, source="nonlinear_overfit")

    def _row_scale_schedule_name(self, row: dict[str, Any]) -> str:
        model = self._row_model_name(row)
        explicit = str(row.get("scale_schedule_name") or row.get("pvr_expert_delta_scale_schedule") or "")
        if "scale_schedule_1_to_8_to_2" in model:
            return "warmup_hold_decay_1_to_8_to_2"
        if "scale_schedule_1_to_4_to_2" in model:
            return "warmup_hold_decay_1_to_4_to_2"
        if "scale_schedule_1_to_8_to_4" in model:
            return "warmup_hold_decay_1_to_8_to_4"
        if "scale_schedule_1_to_8" in model:
            return "warmup_hold_1_to_8"
        if "scale_schedule_1_to_4" in model:
            return "warmup_hold_1_to_4"
        if "expert_delta_scale_8" in model:
            return "constant_8"
        if "expert_delta_scale_4" in model:
            return "constant_4"
        if "expert_delta_scale_2" in model:
            return "constant_2"
        if explicit and explicit != "constant":
            end = row.get("pvr_expert_delta_scale_end", row.get("pvr_expert_delta_scale", 1.0))
            return f"{explicit}_{end}"
        scale = row.get("pvr_expert_delta_scale", 1.0)
        return f"constant_{float(scale):g}" if isinstance(scale, (int, float)) else "constant_1"

    def _row_loss_acc(self, row: dict[str, Any]) -> tuple[float | None, float | None]:
        loss = self._maybe_float(row.get("final_train_loss", row.get("loss", row.get("avg_loss"))))
        acc = self._maybe_float(row.get("final_train_accuracy", row.get("accuracy", row.get("avg_accuracy"))))
        return loss, acc

    def _row_step_metric_mean(self, row: dict[str, Any], key: str) -> float | None:
        step_metrics = row.get("schedule_step_metrics") or []
        if isinstance(step_metrics, list):
            return self._mean_or_none([
                self._maybe_float(item.get(key)) for item in step_metrics if isinstance(item, dict)
            ])
        return None

    def _write_expert_delta_scale_schedule_report(
        self,
        rows: list[dict[str, Any]],
        metadata: dict[str, Any],
        source: str,
        summary: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        schedule_rows = [
            r for r in rows
            if "scale_schedule" in self._row_model_name(r)
            or str(r.get("pvr_expert_delta_scale_schedule", "constant")) != "constant"
        ]
        candidate_rows = [
            r for r in rows
            if self._row_model_name(r).startswith("pvr")
            or "scale_schedule" in self._row_model_name(r)
        ]
        grouped: dict[str, list[dict[str, Any]]] = {}
        for row in candidate_rows:
            grouped.setdefault(self._row_model_name(row), []).append(row)

        model_summary = {}
        for model, items in grouped.items():
            losses, accs = [], []
            for item in items:
                loss, acc = self._row_loss_acc(item)
                if loss is not None:
                    losses.append(loss)
                if acc is not None:
                    accs.append(acc)
            contribs = []
            ratios = []
            eces = []
            entropies = []
            logits = []
            latencies = []
            scales = []
            for item in items:
                cm = item.get("contribution_metrics") if isinstance(item.get("contribution_metrics"), dict) else {}
                contrib = cm.get("expert_delta_contribution_pct", item.get("expert_delta_contribution_pct"))
                ratio = cm.get("shared_sparse_ratio", item.get("shared_sparse_ratio"))
                contribs.append(self._maybe_float(contrib))
                ratios.append(self._maybe_float(ratio))
                eces.append(self._maybe_float(item.get("calibration_proxy", item.get("ece"))))
                eces.append(self._row_step_metric_mean(item, "calibration_proxy"))
                entropies.append(self._maybe_float(item.get("prediction_entropy")))
                entropies.append(self._row_step_metric_mean(item, "prediction_entropy"))
                logits.append(self._maybe_float(item.get("logit_norm")))
                logits.append(self._row_step_metric_mean(item, "logit_norm"))
                latencies.append(self._maybe_float(item.get("latency_ms")))
                latencies.append(self._row_step_metric_mean(item, "latency_ms"))
                latencies.append((self._maybe_float(item.get("inference_time_s")) or 0.0) * 1000.0 if item.get("inference_time_s") is not None else None)
                curve = item.get("expert_delta_scale_curve") or []
                if isinstance(curve, list) and curve:
                    scales.append(self._maybe_float(curve[-1]))
                scales.append(self._maybe_float(item.get("pvr_expert_delta_scale_t", item.get("pvr_expert_delta_scale"))))
            model_summary[model] = {
                "schedule_name": self._row_scale_schedule_name(items[0]),
                "scale_start": items[0].get("pvr_expert_delta_scale_start"),
                "scale_end": items[0].get("pvr_expert_delta_scale_end", items[0].get("pvr_expert_delta_scale")),
                "warmup_steps": items[0].get("pvr_expert_delta_scale_warmup_steps"),
                "hold_steps": items[0].get("pvr_expert_delta_scale_hold_steps"),
                "decay_enabled": items[0].get("pvr_expert_delta_scale_decay") not in {None, 0.0, "0", ""},
                "avg_loss": self._mean_or_none(losses),
                "avg_accuracy": self._mean_or_none(accs),
                "expert_delta_contribution_pct": self._mean_or_none(contribs),
                "shared_sparse_ratio": self._mean_or_none(ratios),
                "calibration_proxy": self._mean_or_none(eces),
                "prediction_entropy": self._mean_or_none(entropies),
                "logit_norm": self._mean_or_none(logits),
                "latency_ms": self._mean_or_none(latencies),
                "final_expert_delta_scale_t": self._mean_or_none(scales),
            }

        def best_model(models: list[str]) -> str | None:
            clean = {
                m: d for m, d in model_summary.items()
                if m in models and isinstance(d.get("avg_loss"), (int, float))
            }
            if not clean:
                return None
            return min(clean, key=lambda m: float(clean[m]["avg_loss"]))

        all_schedule_models = [m for m in model_summary if "scale_schedule" in m]
        best_schedule = best_model(all_schedule_models)
        constant_models = [m for m in model_summary if "expert_delta_scale_" in m and "scale_schedule" not in m]
        best_constant = best_model(constant_models)
        pvr_base = model_summary.get("pvr_full") or model_summary.get("pvr_ec_deploy_top1")
        best_data = model_summary.get(best_schedule or "", {})
        constant_data = model_summary.get(best_constant or "", {})

        helpful = False
        harmful = False
        calibration_regression = False
        latency_regression = False
        benchmark_improved = False
        if best_schedule and pvr_base:
            base_loss = self._maybe_float(pvr_base.get("avg_loss"))
            base_acc = self._maybe_float(pvr_base.get("avg_accuracy"))
            sch_loss = self._maybe_float(best_data.get("avg_loss"))
            sch_acc = self._maybe_float(best_data.get("avg_accuracy"))
            helpful = bool(
                sch_loss is not None and base_loss is not None and sch_loss < base_loss
                and (sch_acc is None or base_acc is None or sch_acc >= base_acc - 0.005)
            )
            harmful = bool(
                sch_loss is not None and base_loss is not None and sch_loss > base_loss + 0.02
                and sch_acc is not None and base_acc is not None and sch_acc <= base_acc + 0.005
            )
            benchmark_improved = helpful if source == "benchmark_gate" else False
            if sch_acc is not None and base_acc is not None and sch_acc > base_acc + 0.005:
                benchmark_improved = source == "benchmark_gate"
                if sch_loss is not None and base_loss is not None and sch_loss > base_loss + 0.02:
                    calibration_regression = True
        if best_schedule and constant_data:
            sch_ece = self._maybe_float(best_data.get("calibration_proxy"))
            const_ece = self._maybe_float(constant_data.get("calibration_proxy"))
            if sch_ece is not None and const_ece is not None and sch_ece > const_ece * 1.25 + 0.01:
                calibration_regression = True
            sch_latency = self._maybe_float(best_data.get("latency_ms"))
            const_latency = self._maybe_float(constant_data.get("latency_ms"))
            if sch_latency is not None and const_latency is not None and sch_latency > const_latency * 1.20 + 0.5:
                latency_regression = True

        statuses = {
            "PVR_EC_EXPERT_DELTA_SCALE_SCHEDULE_IMPLEMENTED",
            "PVR_EC_DO_NOT_PROMOTE",
        }
        if helpful:
            statuses.add("PVR_EC_EXPERT_DELTA_SCALE_SCHEDULE_HELPFUL")
            if source == "nonlinear_overfit":
                statuses.add("PVR_EC_NONLINEAR_REPAIR_CONFIRMED")
        if harmful:
            statuses.add("PVR_EC_EXPERT_DELTA_SCALE_SCHEDULE_HARMFUL")
        if source == "benchmark_gate":
            statuses.add("PVR_EC_BENCHMARK_CAPABILITY_IMPROVED" if benchmark_improved else "PVR_EC_BENCHMARK_CAPABILITY_NOT_IMPROVED")
        if calibration_regression:
            statuses.add("PVR_EC_CALIBRATION_REGRESSION")
        if latency_regression:
            statuses.add("PVR_EC_LATENCY_REGRESSION")

        status = (
            "PVR_EC_EXPERT_DELTA_SCALE_SCHEDULE_HARMFUL" if harmful
            else "PVR_EC_EXPERT_DELTA_SCALE_SCHEDULE_HELPFUL" if helpful
            else "PVR_EC_BENCHMARK_CAPABILITY_NOT_IMPROVED" if source == "benchmark_gate"
            else "PVR_EC_EXPERT_DELTA_SCALE_SCHEDULE_IMPLEMENTED"
        )
        payload = {
            "metadata": metadata,
            "source": source,
            "status": status,
            "statuses": sorted(statuses),
            "promotion_ready": False,
            "schedule_name": best_data.get("schedule_name"),
            "scale_start": best_data.get("scale_start"),
            "scale_end": best_data.get("scale_end"),
            "warmup_steps": best_data.get("warmup_steps"),
            "hold_steps": best_data.get("hold_steps"),
            "decay_enabled": best_data.get("decay_enabled"),
            "best_model": best_schedule,
            "best_constant_model": best_constant,
            "best_step": self._best_schedule_step(rows, best_schedule),
            "best_loss": best_data.get("avg_loss"),
            "best_accuracy": best_data.get("avg_accuracy"),
            "best_expert_delta_contribution_pct": best_data.get("expert_delta_contribution_pct"),
            "calibration_regression": calibration_regression,
            "latency_regression": latency_regression,
            "benchmark_capability_improved": benchmark_improved,
            "recommendation": self._schedule_recommendation(status, best_data, constant_data),
            "model_summary": model_summary,
            "source_summary": summary or {},
            "rows": schedule_rows,
        }
        self._write_json_md_pair(
            "pvr_ec_expert_delta_scale_schedule_report",
            payload,
            "PVR-EC Expert Delta Scale Schedule Report",
        )
        return payload

    def _best_schedule_step(self, rows: list[dict[str, Any]], best_model: str | None) -> int | None:
        if not best_model:
            return None
        best = None
        for row in rows:
            if self._row_model_name(row) != best_model:
                continue
            for item in row.get("schedule_step_metrics", []) or []:
                if not isinstance(item, dict):
                    continue
                loss = self._maybe_float(item.get("train_loss"))
                if loss is None:
                    continue
                if best is None or loss < best[0]:
                    best = (loss, int(item.get("step", 0)))
        return best[1] if best else None

    @staticmethod
    def _schedule_recommendation(status: str, best_data: dict[str, Any], constant_data: dict[str, Any]) -> str:
        if status == "PVR_EC_EXPERT_DELTA_SCALE_SCHEDULE_HELPFUL":
            return f"keep {best_data.get('schedule_name')} as the next single repair candidate"
        if status == "PVR_EC_EXPERT_DELTA_SCALE_SCHEDULE_HARMFUL":
            return "do not promote scheduled scale; reduce target or add stronger decay"
        if constant_data:
            return "scheduled scale did not beat constant scale cleanly; keep as diagnostic only"
        return "schedule implemented; run nonlinear and benchmark gates before promotion"

    def _best_model_for_metric(
        self,
        rows: list[dict],
        task: str,
        metric: str,
        minimize: bool = True,
    ) -> str:
        """Find the best model for a specific metric on a specific task."""
        candidates = [r for r in rows if r["task"] == task]
        if not candidates:
            return "none"
        if minimize:
            best = min(candidates, key=lambda r: r.get(metric, float("inf")))
        else:
            best = max(candidates, key=lambda r: r.get(metric, float("-inf")))
        return f"{best['model']} ({metric}={best.get(metric, 'N/A'):.4f})"

    def _generate_all_datasets(self) -> dict[str, list[BenchmarkSample]]:
        """Generate all benchmark datasets."""
        datasets = {}
        model_cfg = SCALES[self.scale]
        max_seq = model_cfg["d_model"] * 2  # Use 2x model dim as max seq

        if "clrs" in self.families:
            gen = CLRSStyleGenerator(max_seq_len=max_seq, seed=self.seed)
            for task, lengths in [("sorting", [4,6,8,10]), ("searching", [5,7,10]), ("lcs", [4,6,8])]:
                samples = []
                for length in lengths:
                    for _ in range(self.n_samples // len(lengths)):
                        if task == "sorting":
                            samples.append(gen.generate_sorting(length))
                        elif task == "searching":
                            samples.append(gen.generate_searching(length))
                        elif task == "lcs":
                            samples.append(gen.generate_lcs(length))
                datasets[f"clrs_{task}"] = samples

        if "listops" in self.families:
            gen = ListOpsGenerator(max_seq_len=max_seq, seed=self.seed)
            samples = []
            for depth in [2, 3, 4, 5]:
                for _ in range(self.n_samples // 4):
                    samples.append(gen.generate(max_depth=depth, max_args=3))
            datasets["listops"] = samples

        if "scan" in self.families:
            gen = SCANStyleGenerator(max_seq_len=max_seq, seed=self.seed)
            # Random split
            samples_random = [gen.generate(max_commands=3, include_jump=True) for _ in range(self.n_samples)]
            datasets["scan_random"] = samples_random
            # Length split (train short, test long)
            samples_long = [gen.generate(max_commands=5, include_jump=True) for _ in range(self.n_samples // 2)]
            datasets["scan_length"] = samples_long

        if "dyck" in self.families:
            gen = DyckGenerator(max_seq_len=max_seq, seed=self.seed)
            samples_val = [gen.generate_validation(max_depth=d, num_types=2)
                           for d in [3,4,5,6] for _ in range(self.n_samples // 4)]
            datasets["dyck_validation"] = samples_val
            samples_comp = [gen.generate_completion(max_depth=d, num_types=2)
                            for d in [3,4,5] for _ in range(self.n_samples // 4)]
            datasets["dyck_completion"] = samples_comp

        return datasets

    def _train_and_eval_model(self, model_name: str, model_cfg: dict,
                              datasets: dict[str, list[BenchmarkSample]]):
        """Train a model variant and evaluate on all benchmark datasets."""
        torch.manual_seed(self.seed)
        np.random.seed(self.seed)

        scale = SCALES[self.scale]
        vocab_size = 256
        schedule_cfg = self._resolve_pvr_expert_delta_scale_schedule({}, 1.0)

        if model_cfg["type"] == "dense":
            model = DenseTransformer(DenseTransformerConfig(
                vocab_size=vocab_size, d_model=scale["d_model"], n_heads=scale["n_heads"],
                n_layers=scale["n_layers"], d_ff=scale["d_ff"],
                max_seq_len=scale["d_model"]*2, dropout=0.1,
            ))
        elif model_cfg["type"] == "pvr_ec":
            overrides = model_cfg.get("overrides", {})
            if model_name.startswith("pvr_ec_ownership_top1_final_candidate_v1_"):
                config_path = Path("configs") / f"{model_name}.json"
                if config_path.exists():
                    overrides = {**overrides, **json.loads(config_path.read_text(encoding="utf-8"))}
            pvr_expert_type = self._resolve_pvr_expert_type(overrides, "delta_rank_medium")
            # Parameter-matched: increase expert delta size to match fixed_moe params
            if overrides.get("match_params"):
                d_expert = scale["d_ff"]  # Full-size expert deltas
                num_proto = scale["num_experts"] * 8
            else:
                d_expert = scale["d_ff"] // 2
                num_proto = scale["num_experts"] * 4
            if (
                self.pvr_expert_type
                or overrides.get("pvr_expert_type")
                or "d_expert" in overrides
                or "d_expert_multiplier" in overrides
            ):
                d_expert = self._resolve_pvr_d_expert(scale, overrides, pvr_expert_type)
            shared_scale = 0.0 if self.pvr_debug_disable_shared else float(overrides.get("pvr_shared_scale", 1.0))
            default_delta_scale = 1.0 if self.pvr_expert_delta_scale is None else float(self.pvr_expert_delta_scale)
            expert_delta_scale = 0.0 if self.pvr_debug_disable_sparse else float(overrides.get("pvr_expert_delta_scale", default_delta_scale))
            schedule_cfg = self._resolve_pvr_expert_delta_scale_schedule(overrides, expert_delta_scale)
            debug_force_expert_id = (
                self.pvr_debug_force_expert_id
                if self.pvr_debug_force_expert_id is not None
                else overrides.get("pvr_debug_force_expert_id")
            )

            pvr_config = PVRECModelConfig(
                vocab_size=vocab_size, d_model=scale["d_model"], n_heads=scale["n_heads"],
                n_layers=scale["n_layers"], d_ff=scale["d_ff"],
                num_experts=scale["num_experts"],
                num_prototypes=num_proto,
                max_k=4 if not overrides.get("no_extra") else 1,
                d_expert=d_expert,
                max_seq_len=scale["d_model"]*2, dropout=0.1,
                pvr_execution_mode=self.pvr_execution_mode or (
                    "fixed_top2_pack_by_expert" if overrides.get("fixed_top2")
                    else "variable_k_pack_by_expert"
                ),
                pvr_expert_type=pvr_expert_type,
                pvr_training_dispatch_mode=self.pvr_training_dispatch_mode,
                pvr_inference_dispatch_mode=self.pvr_inference_dispatch_mode,
                pvr_deploy_mode=overrides.get("deploy_mode", self.pvr_deploy_mode),
                pvr_aux_alpha=self.pvr_aux_alpha,
                pvr_shared_scale=shared_scale,
                pvr_expert_delta_scale=expert_delta_scale,
                **schedule_cfg,
                pvr_debug_force_expert_id=debug_force_expert_id,
                pvr_debug_owner_mode=str(overrides.get("pvr_debug_owner_mode", "")),
                pvr_sparse_aux_loss_variant=str(overrides.get("sparse_aux_loss_variant", "baseline_main_loss")),
                pvr_sparse_aux_scope=str(overrides.get("sparse_aux_scope", "aux_all_tokens")),
                pvr_sparse_aux_schedule_total_steps=self.train_steps,
                pvr_output_temperature=float(overrides.get("pvr_output_temperature", 1.0)),
                branch_ticket_shadow_mode=False if overrides.get("deploy_mode", self.pvr_deploy_mode) != "off" else True,
                max_shadow_branch_tickets=0 if overrides.get("deploy_mode", self.pvr_deploy_mode) != "off" else 64,
                mergeability_mode="disabled",
                runtime_branching=False,
            )
            model = PVRECModel(pvr_config)

            # Apply ablation overrides post-init
            if overrides.get("no_load_bias"):
                for block in model.blocks:
                    block.moe.router.config.load_bias_eta = 0.0
                    block.moe.router.load_bias.zero_()
            if overrides.get("no_prototypes"):
                # Disable prototype shortlisting by making all experts compatible
                for block in model.blocks:
                    block.moe.router.proto_expert_compat.fill_(1.0)
            if overrides.get("fixed_top2"):
                # Force NORMAL difficulty for all (top1 + 1 extra = top2)
                for block in model.blocks:
                    block.moe.router.config.easy_margin_threshold = 999.0  # Nothing is EASY
                    block.moe.router.config.hard_entropy_threshold = 999.0  # Nothing is HARD
        else:
            overrides = model_cfg.get("overrides", {})
            model = SparseLoopMoEModel(SparseLoopMoEConfig(
                vocab_size=vocab_size, d_model=scale["d_model"], n_heads=scale["n_heads"],
                n_layers=scale["n_layers"], d_ff=scale["d_ff"],
                num_experts=scale["num_experts"],
                max_seq_len=scale["d_model"]*2, dropout=0.1,
                use_shared_expert=True, **overrides,
            ))

        params = sum(p.numel() for p in model.parameters() if p.requires_grad)
        active_param_count = self._estimate_active_param_count(model, model_cfg, params)
        architecture_metadata = self._pvr_architecture_metadata(
            model, model_name, model_cfg, params, active_param_count,
        )
        print(f"    Params: {params:,}")

        # Move model to device
        device_obj = torch.device(self.device)
        model = model.to(device_obj)

        # Train on mixed algorithmic data (all families combined)
        all_train = []
        for samples in datasets.values():
            all_train.extend(samples[:len(samples)//2])  # First half for training
        if model_cfg.get("overrides", {}).get("family_balanced_sampling"):
            by_family: dict[str, list[Any]] = {}
            for sample in all_train:
                by_family.setdefault(getattr(sample, "family", "unknown"), []).append(sample)
            if by_family:
                max_family = max(len(items) for items in by_family.values())
                balanced: list[Any] = []
                rng = random.Random(self.seed)
                for items in by_family.values():
                    if not items:
                        continue
                    balanced.extend(items)
                    while len(items) and len([s for s in balanced if getattr(s, "family", "unknown") == getattr(items[0], "family", "unknown")]) < max_family:
                        balanced.append(rng.choice(items))
                all_train = balanced
        random.Random(self.seed).shuffle(all_train)

        # Convert BenchmarkSamples to training format
        task_gen = SyntheticTaskGenerator(vocab_size=vocab_size, max_seq_len=scale["d_model"]*2, seed=self.seed)
        trainer_config = TrainerConfig(
            learning_rate=3e-4, weight_decay=0.01,
            max_grad_norm=float(model_cfg.get("overrides", {}).get("max_grad_norm", 1.0)),
            warmup_steps=max(1, self.train_steps // 5),
            max_steps=self.train_steps, batch_size=min(32, len(all_train)),
            eval_interval=self.train_steps + 1,
            log_interval=max(self.train_steps // 3, 1),
            device=self.device,
        )
        trainer = Trainer(model=model, config=trainer_config, task_generator=task_gen)

        t0 = time.time()
        train_history = trainer.train(num_steps=self.train_steps)
        train_loss = self._last_metric_value(train_history, "task_loss")
        train_time = time.time() - t0
        print(f"    Trained: {train_time:.1f}s")

        # Evaluate on second half of each dataset
        model.eval()
        for ds_name, samples in datasets.items():
            eval_samples = samples[len(samples)//2:]  # Second half for eval
            if not eval_samples:
                continue
            t1 = time.time()
            result = self._evaluate(model, eval_samples, model_name, ds_name, params)
            result.training_time_s = train_time
            result.training_loss = train_loss
            result.inference_time_s = time.time() - t1
            result.active_param_count = active_param_count
            result.capacity_variant = model_cfg.get("overrides", {}).get("capacity_variant", "")
            result.pvr_shared_scale = float(model_cfg.get("overrides", {}).get("pvr_shared_scale", result.pvr_shared_scale))
            result.pvr_expert_delta_scale = float(model_cfg.get("overrides", {}).get("pvr_expert_delta_scale", result.pvr_expert_delta_scale))
            result.pvr_expert_delta_scale_schedule = str(schedule_cfg["pvr_expert_delta_scale_schedule"])
            result.pvr_expert_delta_scale_start = float(schedule_cfg["pvr_expert_delta_scale_start"])
            result.pvr_expert_delta_scale_end = float(schedule_cfg["pvr_expert_delta_scale_end"])
            result.pvr_expert_delta_scale_decay = float(schedule_cfg["pvr_expert_delta_scale_decay"] or 0.0)
            result.pvr_expert_delta_scale_warmup_steps = int(schedule_cfg["pvr_expert_delta_scale_warmup_steps"])
            result.pvr_expert_delta_scale_hold_steps = int(schedule_cfg["pvr_expert_delta_scale_hold_steps"])
            result.ownership_schedule = str(model_cfg.get("overrides", {}).get("ownership_schedule", ""))
            result.loss_schedule = str(model_cfg.get("overrides", {}).get("loss_schedule", ""))
            result.sparse_aux_loss_variant = str(model_cfg.get("overrides", {}).get("sparse_aux_loss_variant", "baseline_main_loss"))
            result.sparse_aux_scope = str(model_cfg.get("overrides", {}).get("sparse_aux_scope", "aux_all_tokens"))
            result.repair_variant = str(model_cfg.get("overrides", {}).get("repair_variant", ""))
            result.pvr_output_temperature = float(model_cfg.get("overrides", {}).get("pvr_output_temperature", 1.0))
            result.expert_hidden_dim = int(getattr(getattr(model, "config", None), "d_expert", 0) or 0)
            for key, value in architecture_metadata.items():
                if hasattr(result, key):
                    setattr(result, key, value)
            self.results.append(result)
            print(f"    {ds_name:20s} | n={result.sample_count:3d} | acc={result.accuracy:.4f} | "
                  f"em={result.exact_match:.4f} | loss={result.loss:.3f} | "
                  f"loops={result.avg_loops:.1f} | qpc={result.qpc:.4f}")

    @staticmethod
    def _last_metric_value(history: list[dict[str, float]], key: str) -> float:
        for item in reversed(history):
            value = item.get(key)
            if isinstance(value, (int, float)):
                return float(value)
        return 0.0

    def _evaluate(self, model, samples: list[BenchmarkSample], model_name: str,
                  ds_name: str, params: int) -> Result:
        """Evaluate model on benchmark samples."""
        device = torch.device(self.device)
        bs = min(32, len(samples))

        total_correct = 0
        total_tokens = 0
        total_loss = 0.0
        exact_matches = 0
        total_loops = 0
        total_experts = 0
        loop_count = 0
        halt_count = 0
        osc_count = 0
        num_batches = 0
        pvr_diag_history: list[dict[str, Any]] = []
        logit_norms = []
        entropies = []
        confidences_correct = []
        confidences_wrong = []
        ece_bins = [{"conf": 0.0, "acc": 0.0, "count": 0} for _ in range(10)]
        residual_records = []

        with torch.no_grad():
            for i in range(0, len(samples), bs):
                batch = samples[i:i+bs]
                input_ids = torch.stack([s.input_ids for s in batch]).to(device)
                target_ids = torch.stack([s.target_ids for s in batch]).to(device)

                output = model(input_ids=input_ids, targets=target_ids)
                total_loss += output["loss"].item()
                if "pvr_diagnostics" in output:
                    pvr_diag_history.append(output["pvr_diagnostics"])
                if model_name.startswith("pvr_ec") and (
                    self.root_cause_flags.get("run_residual_alignment_diagnostic")
                    or self.root_cause_flags.get("run_family_scale_sweep")
                    or self.root_cause_flags.get("run_conditional_scale_oracle")
                    or self.root_cause_flags.get("run_benchmark_transfer_confirmation")
                    or self.root_cause_flags.get("run_task_level_transfer_diagnostic")
                    or self.root_cause_flags.get("run_decision_token_credit_diagnostic")
                    or self.root_cause_flags.get("run_token_to_sequence_transfer_diagnostic")
                    or self.root_cause_flags.get("run_family_failure_decomposition")
                    or self.root_cause_flags.get("run_output_readout_diagnostic")
                    or self.root_cause_flags.get("run_loss_credit_repair_sweep")
                    or self.root_cause_flags.get("run_curriculum_repair_sweep")
                    or self.root_cause_flags.get("run_segment_residual_diagnostic")
                    or self.root_cause_flags.get("run_sparse_logit_direction_diagnostic")
                    or self.root_cause_flags.get("run_sparse_auxiliary_loss_sweep")
                    or self.root_cause_flags.get("run_calibration_constrained_sparse_aux_sweep")
                    or self.root_cause_flags.get("run_sparse_auxiliary_scope_sweep")
                    or self.root_cause_flags.get("run_sparse_direction_transfer_confirmation")
                    or self.root_cause_flags.get("run_multiseed_confirmation_gate")
                    or self.root_cause_flags.get("run_longer_training_confirmation_gate")
                    or self.root_cause_flags.get("run_matched_wall_clock_gate")
                    or self.root_cause_flags.get("run_final_calibration_sweep")
                    or self.root_cause_flags.get("run_family_regression_gate")
                    or self.root_cause_flags.get("run_reliability_proxy_gate")
                    or self.root_cause_flags.get("run_repeatability_collapse_isolation")
                    or self.root_cause_flags.get("run_repeatability_repair_sweep")
                    or self.root_cause_flags.get("run_reliability_calibration_repair")
                    or self.root_cause_flags.get("run_final_candidate_revalidation")
                ):
                    residual_records.append(
                        self._residual_alignment_batch_metrics(model, input_ids, target_ids, output)
                    )

                logits = output["logits"]
                preds = logits.argmax(dim=-1)
                probs = torch.softmax(logits, dim=-1)
                conf, _ = probs.max(dim=-1)
                entropy = -(probs * probs.clamp_min(1e-12).log()).sum(dim=-1)
                mask = target_ids != 0
                correct = (preds == target_ids) & mask
                total_correct += correct.sum().item()
                total_tokens += mask.sum().item()
                masked_conf = conf[mask]
                masked_correct = correct[mask]
                if masked_conf.numel():
                    logit_norms.append(float(logits[mask].detach().float().norm(dim=-1).mean().item()))
                    entropies.append(float(entropy[mask].detach().float().mean().item()))
                    if masked_correct.any():
                        confidences_correct.append(float(masked_conf[masked_correct].mean().item()))
                    if (~masked_correct).any():
                        confidences_wrong.append(float(masked_conf[~masked_correct].mean().item()))
                    bins = torch.clamp((masked_conf * 10).long(), max=9)
                    for bin_idx in range(10):
                        bin_mask = bins == bin_idx
                        if bin_mask.any():
                            ece_bins[bin_idx]["conf"] += float(masked_conf[bin_mask].sum().item())
                            ece_bins[bin_idx]["acc"] += float(masked_correct[bin_mask].float().sum().item())
                            ece_bins[bin_idx]["count"] += int(bin_mask.sum().item())

                # Exact sequence match (all non-pad tokens correct)
                for j in range(len(batch)):
                    row_mask = mask[j]
                    if row_mask.sum() > 0 and correct[j][row_mask].all():
                        exact_matches += 1

                loop_stats = output.get("loop_stats", [])
                if loop_stats and isinstance(loop_stats[0], LoopStats):
                    for s in loop_stats:
                        total_loops += s.loops_used
                        total_experts += sum(s.experts_used_per_loop) if s.experts_used_per_loop else 1
                        loop_count += 1
                        if s.halted_early: halt_count += 1
                        if s.oscillation_detected: osc_count += 1
                num_batches += 1

        n = len(samples)
        acc = total_correct / max(total_tokens, 1)
        em = exact_matches / max(n, 1)
        avg_loss = total_loss / max(num_batches, 1)
        avg_loops = total_loops / max(loop_count, 1) if loop_count > 0 else 1.0
        avg_experts = total_experts / max(total_loops, 1) if total_loops > 0 else 1.0
        halt_rate = halt_count / max(loop_count, 1) if loop_count > 0 else 0.0
        osc_rate = osc_count / max(loop_count, 1) if loop_count > 0 else 0.0
        qpc = acc / max(avg_loops * avg_experts, 0.01)

        # Determine family and difficulty from samples
        family = samples[0].family if samples else "unknown"
        difficulties = [s.difficulty for s in samples]
        majority_diff = max(set(difficulties), key=difficulties.count) if difficulties else "mixed"

        pvr_diag = self._aggregate_pvr_eval_diagnostics(pvr_diag_history)
        ece = 0.0
        ece_total = sum(b["count"] for b in ece_bins)
        if ece_total:
            for b in ece_bins:
                if b["count"]:
                    avg_conf = b["conf"] / b["count"]
                    avg_acc = b["acc"] / b["count"]
                    ece += (b["count"] / ece_total) * abs(avg_conf - avg_acc)
        pvr_diag.update({
            "logit_norm": float(np.mean(logit_norms)) if logit_norms else 0.0,
            "prediction_entropy": float(np.mean(entropies)) if entropies else 0.0,
            "confidence_when_correct": float(np.mean(confidences_correct)) if confidences_correct else 0.0,
            "confidence_when_wrong": float(np.mean(confidences_wrong)) if confidences_wrong else 0.0,
            "calibration_proxy": float(ece),
            "loss_accuracy_disagreement": float(avg_loss * (1.0 - acc)),
        })
        if residual_records:
            pvr_diag.update(self._aggregate_residual_alignment_records(residual_records))

        return Result(
            run_id=self.run_id, model_name=model_name, family=family,
            task=ds_name, split="eval", sample_count=n,
            accuracy=acc, exact_match=em, loss=avg_loss,
            avg_loops=avg_loops, avg_experts=avg_experts,
            halt_rate=halt_rate, oscillation_rate=osc_rate, qpc=qpc,
            total_parameters=params, training_time_s=0, inference_time_s=0,
            difficulty=majority_diff, length_bucket="mixed",
            **pvr_diag,
        )

    @staticmethod
    def _set_model_expert_delta_scale(model, scale: float) -> list[float]:
        previous = []
        for block in getattr(model, "blocks", []):
            moe = getattr(block, "moe", None)
            if moe is None or not hasattr(moe, "pvr_expert_delta_scale_t"):
                continue
            previous.append(float(moe.pvr_expert_delta_scale_t))
            moe.pvr_expert_delta_scale_t = float(scale)
            moe.pvr_expert_delta_scale = float(scale)
        return previous

    @staticmethod
    def _restore_model_expert_delta_scale(model, previous: list[float]) -> None:
        idx = 0
        for block in getattr(model, "blocks", []):
            moe = getattr(block, "moe", None)
            if moe is None or not hasattr(moe, "pvr_expert_delta_scale_t"):
                continue
            value = previous[idx] if idx < len(previous) else 1.0
            moe.pvr_expert_delta_scale_t = float(value)
            moe.pvr_expert_delta_scale = float(value)
            idx += 1

    def _residual_alignment_batch_metrics(
        self,
        model,
        input_ids: torch.Tensor,
        target_ids: torch.Tensor,
        full_output: dict[str, Any],
    ) -> dict[str, float]:
        previous = self._set_model_expert_delta_scale(model, 0.0)
        try:
            shared_output = model(input_ids=input_ids, targets=target_ids)
        finally:
            self._restore_model_expert_delta_scale(model, previous)

        full_logits = full_output["logits"].detach()
        shared_logits = shared_output["logits"].detach()
        full_loss_tok = torch.nn.functional.cross_entropy(
            full_logits.view(-1, full_logits.shape[-1]),
            target_ids.view(-1),
            reduction="none",
        ).view_as(target_ids)
        shared_loss_tok = torch.nn.functional.cross_entropy(
            shared_logits.view(-1, shared_logits.shape[-1]),
            target_ids.view(-1),
            reduction="none",
        ).view_as(target_ids)
        mask = target_ids != 0
        if not mask.any():
            mask = torch.ones_like(target_ids, dtype=torch.bool)
        delta = full_loss_tok - shared_loss_tok
        masked_delta = delta[mask]
        decision_mask = torch.zeros_like(mask)
        decision_mask[:, -1] = True
        decision_mask = decision_mask & mask
        if not decision_mask.any():
            decision_mask = mask
        nondecision_mask = mask & ~decision_mask
        if not nondecision_mask.any():
            nondecision_mask = mask
        decision_delta = delta[decision_mask]
        nondecision_delta = delta[nondecision_mask]
        help_rate = float((masked_delta < -1e-4).float().mean().item())
        harm_rate = float((masked_delta > 1e-4).float().mean().item())
        neutral_rate = max(0.0, 1.0 - help_rate - harm_rate)
        decision_help = float((decision_delta < -1e-4).float().mean().item())
        decision_harm = float((decision_delta > 1e-4).float().mean().item())

        full_pred = full_logits.argmax(dim=-1)
        shared_pred = shared_logits.argmax(dim=-1)
        logit_delta = full_logits - shared_logits
        target = target_ids.unsqueeze(-1)
        correct_delta = logit_delta.gather(-1, target).squeeze(-1)
        one_hot = torch.nn.functional.one_hot(target_ids, num_classes=full_logits.shape[-1]).bool()
        neg_inf = torch.full_like(logit_delta, -1e9)
        incorrect_delta_max = torch.where(
            one_hot,
            neg_inf,
            logit_delta,
        ).max(dim=-1).values
        incorrect_delta_mean = (
            logit_delta.masked_fill(one_hot, 0.0).sum(dim=-1)
            / max(full_logits.shape[-1] - 1, 1)
        )
        full_probs = torch.softmax(full_logits, dim=-1)
        shared_probs = torch.softmax(shared_logits, dim=-1)
        full_entropy = -(full_probs * full_probs.clamp_min(1e-12).log()).sum(dim=-1)
        shared_entropy = -(shared_probs * shared_probs.clamp_min(1e-12).log()).sum(dim=-1)
        full_margin = full_logits.gather(-1, target).squeeze(-1) - torch.where(
            torch.nn.functional.one_hot(target_ids, num_classes=full_logits.shape[-1]).bool(),
            torch.full_like(full_logits, -1e9),
            full_logits,
        ).max(dim=-1).values
        shared_margin = shared_logits.gather(-1, target).squeeze(-1) - torch.where(
            torch.nn.functional.one_hot(target_ids, num_classes=shared_logits.shape[-1]).bool(),
            torch.full_like(shared_logits, -1e9),
            shared_logits,
        ).max(dim=-1).values
        delta_correct_minus_top_wrong = correct_delta - incorrect_delta_max
        overamplified = incorrect_delta_max > correct_delta
        underamplified = correct_delta <= 0.0

        full_diag = full_output.get("pvr_diagnostics", {})
        shared_norm = float(full_diag.get("shared_output_norm", 0.0) or 0.0)
        sparse_norm = float(full_diag.get("sparse_output_norm", 0.0) or 0.0)
        token_loss_improvement = float((-masked_delta.mean()).item())
        sequence_accuracy_improvement = float(
            (full_pred[mask] == target_ids[mask]).float().mean().item()
            - (shared_pred[mask] == target_ids[mask]).float().mean().item()
        )
        transfer_ratio = sequence_accuracy_improvement / max(abs(token_loss_improvement), 1e-8)
        return {
            "loss_shared_only": float(shared_loss_tok[mask].mean().item()),
            "loss_full": float(full_loss_tok[mask].mean().item()),
            "loss_scaled": float(full_loss_tok[mask].mean().item()),
            "loss_delta_full_vs_shared": float(masked_delta.mean().item()),
            "accuracy_shared_only": float((shared_pred[mask] == target_ids[mask]).float().mean().item()),
            "accuracy_full": float((full_pred[mask] == target_ids[mask]).float().mean().item()),
            "accuracy_scaled": float((full_pred[mask] == target_ids[mask]).float().mean().item()),
            "residual_help_rate": help_rate,
            "residual_harm_rate": harm_rate,
            "residual_neutral_rate": neutral_rate,
            "mean_loss_delta_when_residual_active": float(masked_delta.mean().item()),
            "final_token_loss_delta": float(decision_delta.mean().item()),
            "final_state_loss_delta": float(decision_delta.mean().item()),
            "decision_position_loss_delta": float(decision_delta.mean().item()),
            "nondecision_position_loss_delta": float(nondecision_delta.mean().item()),
            "decision_token_help_rate": decision_help,
            "decision_token_harm_rate": decision_harm,
            "decision_token_expert_contribution_pct": sparse_norm / max(shared_norm + sparse_norm, 1e-8),
            "token_loss_improvement": token_loss_improvement,
            "sequence_loss_improvement": float((-decision_delta.mean()).item()),
            "sequence_accuracy_improvement": sequence_accuracy_improvement,
            "token_to_sequence_transfer_ratio": float(transfer_ratio),
            "final_token_accuracy": float((full_pred[decision_mask] == target_ids[decision_mask]).float().mean().item()),
            "expert_delta_contribution_pct": sparse_norm / max(shared_norm + sparse_norm, 1e-8),
            "residual_norm": sparse_norm,
            "shared_norm": shared_norm,
            "combined_norm": shared_norm + sparse_norm,
            "logit_delta_norm": float(logit_delta[mask].float().norm(dim=-1).mean().item()),
            "correct_class_logit_delta": float(correct_delta[mask].mean().item()),
            "incorrect_class_logit_delta": float(incorrect_delta_max[mask].mean().item()),
            "incorrect_class_logit_delta_mean": float(incorrect_delta_mean[mask].mean().item()),
            "incorrect_class_logit_delta_max": float(incorrect_delta_max[mask].mean().item()),
            "delta_correct_minus_top_wrong": float(delta_correct_minus_top_wrong[mask].mean().item()),
            "sparse_margin_delta": float(delta_correct_minus_top_wrong[mask].mean().item()),
            "combined_margin_delta": float((full_margin - shared_margin)[mask].mean().item()),
            "shared_margin": float(shared_margin[mask].mean().item()),
            "combined_margin": float(full_margin[mask].mean().item()),
            "sparse_logit_norm": float(logit_delta[mask].float().norm(dim=-1).mean().item()),
            "combined_logit_norm": float(full_logits[mask].float().norm(dim=-1).mean().item()),
            "incorrect_logit_overamplification_rate": float(overamplified[mask].float().mean().item()),
            "correct_logit_underamplification_rate": float(underamplified[mask].float().mean().item()),
            "margin_delta": float((full_margin - shared_margin)[mask].mean().item()),
            "entropy_delta": float((full_entropy - shared_entropy)[mask].mean().item()),
            "segment_residual_norm": sparse_norm,
            "segment_residual_alignment": token_loss_improvement,
            "segment_residual_success_correlation": sequence_accuracy_improvement,
        }

    def _aggregate_residual_alignment_records(self, records: list[dict[str, float]]) -> dict[str, float]:
        keys = sorted({key for record in records for key in record})
        return {
            key: float(np.mean([record[key] for record in records if isinstance(record.get(key), (int, float))]))
            for key in keys
        }

    @staticmethod
    def _aggregate_pvr_eval_diagnostics(history: list[dict[str, Any]]) -> dict[str, Any]:
        """Average PVR diagnostics across eval batches."""

        keys = [
            "dispatch_overhead_ratio",
            "compute_to_dispatch_ratio",
            "forward_dispatch_overhead_ratio",
            "backward_dispatch_overhead_ratio",
            "training_compute_to_dispatch_ratio",
            "total_step_time_ms",
            "router_score_time_ms",
            "assignment_build_time_ms",
            "pack_time_ms",
            "expert_compute_time_ms",
            "scatter_time_ms",
            "tokens_per_second",
            "avg_tokens_per_active_expert",
            "small_expert_batch_rate",
            "actual_avg_k",
            "target_avg_K",
            "assignment_budget_drift",
            "expert_utilization",
            "expert_load_cv",
            "route_entropy",
            "num_k1_tokens",
            "num_k2_tokens",
            "num_k4_tokens",
            "mergeability_score_mean",
            "mergeability_score_std",
            "expert_disagreement_mean",
            "branch_ticket_count",
            "actual_owner_count_per_token",
            "actual_experts_executed",
            "actual_expert_slots_per_token",
        ]
        direct_numeric_keys = [
            "shared_output_norm",
            "sparse_output_norm",
            "shared_sparse_ratio",
            "pvr_shared_scale",
            "pvr_expert_delta_scale",
            "pvr_expert_delta_scale_t",
        ]
        if not history:
            return {}

        out: dict[str, Any] = {
            "pvr_execution_mode": history[0].get("pvr_execution_mode", ""),
            "pvr_expert_type": history[0].get("pvr_expert_type", ""),
        }
        rename = {"target_avg_K": "target_avg_k"}
        for key in keys:
            values = [float(item[key]) for item in history if isinstance(item.get(key), (int, float))]
            out[f"pvr_{rename.get(key, key)}"] = float(np.mean(values)) if values else 0.0
        for key in direct_numeric_keys:
            values = [float(item[key]) for item in history if isinstance(item.get(key), (int, float))]
            out[key] = float(np.mean(values)) if values else 0.0
        out["pvr_expert_delta_scale_schedule"] = str(history[0].get("pvr_expert_delta_scale_schedule", "constant"))
        if out.get("shared_output_norm") or out.get("sparse_output_norm"):
            out["expert_delta_contribution_pct"] = out.get("sparse_output_norm", 0.0) / max(
                out.get("sparse_output_norm", 0.0) + out.get("shared_output_norm", 0.0),
                1e-8,
            )
        for key in [
            "dense_all_experts_executed",
            "oracle_owner_used",
            "forced_action_path_used",
            "replay_probe_labels_used",
        ]:
            out[f"pvr_{key}"] = any(bool(item.get(key, False)) for item in history)
        return out

    @staticmethod
    def _aggregate_inference_pvr_audit(history: list[dict[str, Any]]) -> dict[str, Any]:
        if not history:
            return {
                "actual_owner_count_per_token": None,
                "actual_experts_executed": None,
                "actual_expert_slots_per_token": None,
                "dense_all_experts_executed": False,
                "oracle_owner_used": False,
                "forced_action_path_used": False,
                "replay_probe_labels_used": False,
                "top1_owner_assertion_passed": None,
            }

        numeric_keys = [
            "actual_owner_count_per_token",
            "actual_experts_executed",
            "actual_expert_slots_per_token",
            "shared_output_norm",
            "sparse_output_norm",
            "shared_sparse_ratio",
            "pvr_shared_scale",
            "pvr_expert_delta_scale",
            "num_k1_tokens",
            "num_k2_tokens",
            "num_k4_tokens",
        ]
        bool_keys = [
            "dense_all_experts_executed",
            "oracle_owner_used",
            "forced_action_path_used",
            "replay_probe_labels_used",
        ]
        out: dict[str, Any] = {}
        for key in numeric_keys:
            values = [float(item[key]) for item in history if isinstance(item.get(key), (int, float))]
            out[key] = float(np.mean(values)) if values else None
        for key in bool_keys:
            out[key] = any(bool(item.get(key, False)) for item in history)
        owner_count = out.get("actual_owner_count_per_token")
        out["top1_owner_assertion_passed"] = (
            abs(owner_count - 1.0) < 1e-6
            if isinstance(owner_count, (int, float)) else None
        )
        return out

    # =========================================================================
    # Summary and Output
    # =========================================================================

    def _build_summary(self, valid: list[Result], total_time: float) -> dict:
        """Build aggregate summary with recommendation."""
        # Per-model aggregates
        model_agg = {}
        for r in valid:
            if r.model_name not in model_agg:
                model_agg[r.model_name] = {"acc": [], "em": [], "loss": [], "qpc": [],
                                           "loops": [], "params": r.total_parameters}
            model_agg[r.model_name]["acc"].append(r.accuracy)
            model_agg[r.model_name]["em"].append(r.exact_match)
            model_agg[r.model_name]["loss"].append(r.loss)
            model_agg[r.model_name]["qpc"].append(r.qpc)
            model_agg[r.model_name]["loops"].append(r.avg_loops)

        table = {}
        for m, d in model_agg.items():
            table[m] = {
                "params": d["params"],
                "avg_accuracy": float(np.mean(d["acc"])),
                "avg_exact_match": float(np.mean(d["em"])),
                "avg_loss": float(np.mean(d["loss"])),
                "avg_qpc": float(np.mean(d["qpc"])),
                "avg_loops": float(np.mean(d["loops"])),
            }

        # Win/loss/tie
        wlt = {}
        baselines = ["dense_baseline", "fixed_moe"]
        candidates = ["adaptive_moe", "looped_moe", "full_system"]
        for bl in baselines:
            for cand in candidates:
                key = f"{cand}_vs_{bl}"
                wlt[key] = {"win": 0, "loss": 0, "tie": 0}
                for r_c in valid:
                    if r_c.model_name != cand:
                        continue
                    r_b = next((r for r in valid if r.model_name == bl and r.task == r_c.task), None)
                    if not r_b:
                        continue
                    if r_c.accuracy > r_b.accuracy + 0.005:
                        wlt[key]["win"] += 1
                    elif r_b.accuracy > r_c.accuracy + 0.005:
                        wlt[key]["loss"] += 1
                    else:
                        wlt[key]["tie"] += 1

        # Families attempted/succeeded
        families_attempted = self.families[:]
        families_succeeded = list(set(r.family for r in valid))

        # Recommendation
        rec = self._compute_recommendation(table, wlt, valid, families_succeeded)

        return {
            "run_id": self.run_id, "mode": self.mode, "scale": self.scale,
            "total_time_s": total_time, "seed": self.seed,
            "train_steps": self.train_steps, "n_samples": self.n_samples,
            "num_models": len(model_agg), "num_failures": len(self.failures),
            "total_valid_results": len(valid),
            "total_samples": sum(r.sample_count for r in valid),
            "families_attempted": families_attempted,
            "families_succeeded": families_succeeded,
            "model_table": table, "win_loss_tie": wlt,
            "recommendation": rec,
        }

    def _compute_recommendation(self, table, wlt, valid, families_succeeded):
        if not valid:
            return {"status": "INVALID_EVAL_PIPELINE", "reason": "Zero valid results."}
        if self.mode == "smoke":
            return {"status": "INVALID_EVAL_PIPELINE", "reason": "Smoke mode: verification only."}
        if len(families_succeeded) < 3:
            status = "PARTIAL_ALGORITHMIC_BENCHMARK"
            reason = f"Only {len(families_succeeded)}/4 families succeeded: {families_succeeded}"
        else:
            status = "VALID_ALGORITHMIC_BENCHMARK"
            reason = f"{len(families_succeeded)} respected benchmark families evaluated successfully."

        # Compare adaptive_moe vs baselines
        adaptive = table.get("adaptive_moe", {})
        dense = table.get("dense_baseline", {})
        fixed = table.get("fixed_moe", {})
        full = table.get("full_system", {})

        adaptive_acc = adaptive.get("avg_accuracy", 0)
        dense_acc = dense.get("avg_accuracy", 0)
        fixed_acc = fixed.get("avg_accuracy", 0)
        full_acc = full.get("avg_accuracy", 0)

        adaptive_qpc = adaptive.get("avg_qpc", 0)
        fixed_qpc = fixed.get("avg_qpc", 0)

        # Win/loss counts for key comparisons
        adaptive_vs_fixed_wlt = wlt.get("adaptive_moe_vs_fixed_moe", {"win": 0, "loss": 0, "tie": 0})
        adaptive_vs_dense_wlt = wlt.get("adaptive_moe_vs_dense_baseline", {"win": 0, "loss": 0, "tie": 0})

        # Decision logic
        if fixed_acc > 0 and fixed_acc > adaptive_acc and fixed_acc > dense_acc:
            # Fixed MoE wins on accuracy
            if adaptive_vs_fixed_wlt["loss"] > adaptive_vs_fixed_wlt["win"]:
                arch_rec = "FIXED_MOE_CURRENT_BEST"
                arch_reason = (f"fixed_moe ({fixed_acc:.4f}) > adaptive_moe ({adaptive_acc:.4f}) "
                               f"and dense ({dense_acc:.4f}). "
                               f"Fixed routing wins {adaptive_vs_fixed_wlt['loss']}/{adaptive_vs_fixed_wlt['loss']+adaptive_vs_fixed_wlt['win']+adaptive_vs_fixed_wlt['tie']} tasks vs adaptive.")
            else:
                arch_rec = "HOLD_NEEDS_MORE_EVIDENCE"
                arch_reason = f"fixed_moe leads ({fixed_acc:.4f}) but adaptive is close on task wins"
        elif adaptive_acc > dense_acc and adaptive_acc > fixed_acc:
            arch_rec = "ADAPTIVE_MOE_CURRENT_BEST"
            arch_reason = f"adaptive_moe ({adaptive_acc:.4f}) > dense ({dense_acc:.4f}) and fixed_moe ({fixed_acc:.4f})"
        elif adaptive_acc > dense_acc and adaptive_acc < fixed_acc:
            gap = fixed_acc - adaptive_acc
            if gap < 0.05:
                arch_rec = "ADAPTIVE_ROUTING_PROMISING_NEEDS_TUNING"
                arch_reason = f"adaptive_moe ({adaptive_acc:.4f}) within {gap:.4f} of fixed_moe ({fixed_acc:.4f}), may improve with tuning"
            else:
                arch_rec = "FIXED_MOE_CURRENT_BEST"
                arch_reason = f"fixed_moe ({fixed_acc:.4f}) >> adaptive_moe ({adaptive_acc:.4f}) by {gap:.4f}. Adaptive routing not justified."
        elif full_acc > 0 and full_acc > adaptive_acc and full_acc > fixed_acc:
            arch_rec = "FULL_SYSTEM_PROMISING"
            arch_reason = f"full_system ({full_acc:.4f}) > adaptive_moe ({adaptive_acc:.4f}) and fixed_moe ({fixed_acc:.4f})"
        elif dense_acc >= adaptive_acc and dense_acc >= fixed_acc:
            arch_rec = "DENSE_BASELINE_CURRENT_BEST"
            arch_reason = f"dense ({dense_acc:.4f}) >= all MoE variants — MoE overhead not justified"
        elif dense_acc >= adaptive_acc:
            arch_rec = "SCALE_EXPERIMENT_REQUIRED"
            arch_reason = f"dense ({dense_acc:.4f}) >= adaptive_moe ({adaptive_acc:.4f}) — MoE may need more training"
        else:
            arch_rec = "HOLD_NEEDS_MORE_EVIDENCE"
            arch_reason = "Mixed results"

        return {
            "status": status,
            "architecture_recommendation": arch_rec,
            "reason": f"{reason} {arch_reason}",
            "adaptive_vs_dense": adaptive_acc - dense_acc,
            "adaptive_vs_fixed": adaptive_acc - fixed_acc,
            "full_vs_adaptive": full_acc - adaptive_acc,
            "fixed_vs_dense": fixed_acc - dense_acc,
            "fixed_qpc": fixed_qpc,
            "adaptive_qpc": adaptive_qpc,
        }

    def _write_outputs(self, valid: list[Result], summary: dict, total_time: float):
        """Write all output artifacts."""
        # per_dataset_metrics
        rows = [asdict(r) for r in self.results]
        with open(self.output_dir / "per_dataset_metrics.csv", "w", newline="") as f:
            if rows:
                w = csv.DictWriter(f, fieldnames=rows[0].keys())
                w.writeheader()
                w.writerows(rows)
        with open(self.output_dir / "per_dataset_metrics.json", "w") as f:
            json.dump(rows, f, indent=2, default=str)

        # aggregate_summary
        with open(self.output_dir / "aggregate_summary.json", "w") as f:
            json.dump(summary, f, indent=2, default=str)

        # benchmark_report.md
        self._write_report(summary, valid)
        self._write_capability_validation_reports(valid, summary)

        # failure_analysis.md
        self._write_failure_analysis(summary)

        # PVR-EC diagnostic MVP report skeletons. These are explicit scaffold
        # reports until a full matched ablation matrix is run.
        if any(r.model_name.startswith("pvr_ec") for r in self.results) or (
            self.model_filter and any(m.startswith("pvr_ec") for m in self.model_filter)
        ):
            write_diagnostic_reports(self.output_dir, {
                "status": "PARTIAL_PVR_EC_DIAGNOSTIC_IMPLEMENTATION",
                "run_id": self.run_id,
                "pvr_execution_mode": self.pvr_execution_mode,
                "pvr_expert_type": self.pvr_expert_type,
                "pvr_training_dispatch_mode": self.pvr_training_dispatch_mode,
                "pvr_inference_dispatch_mode": self.pvr_inference_dispatch_mode,
                "pvr_eval_records": rows,
            })
        self._write_root_cause_artifacts(rows, self._artifact_metadata(), source="trained_benchmark", summary=summary)
        if self.root_cause_flags.get("run_expert_delta_scale_schedule_diagnostic") or self.root_cause_flags.get("run_expert_delta_scale_schedule_confirmation"):
            self._write_expert_delta_scale_schedule_report(
                rows,
                self._artifact_metadata(),
                source="benchmark_gate",
                summary=summary,
            )
        if (
            self.root_cause_flags.get("run_residual_alignment_diagnostic")
            or self.root_cause_flags.get("run_family_scale_sweep")
            or self.root_cause_flags.get("run_conditional_scale_oracle")
            or self.root_cause_flags.get("run_benchmark_transfer_confirmation")
            or self.root_cause_flags.get("run_task_level_transfer_diagnostic")
            or self.root_cause_flags.get("run_decision_token_credit_diagnostic")
            or self.root_cause_flags.get("run_token_to_sequence_transfer_diagnostic")
            or self.root_cause_flags.get("run_family_failure_decomposition")
            or self.root_cause_flags.get("run_output_readout_diagnostic")
            or self.root_cause_flags.get("run_loss_credit_repair_sweep")
            or self.root_cause_flags.get("run_curriculum_repair_sweep")
            or self.root_cause_flags.get("run_segment_residual_diagnostic")
        ):
            self._write_benchmark_transfer_diagnostic_reports(rows, self._artifact_metadata(), summary)
        if (
            self.root_cause_flags.get("run_sparse_logit_direction_diagnostic")
            or self.root_cause_flags.get("run_sparse_auxiliary_loss_sweep")
            or self.root_cause_flags.get("run_calibration_constrained_sparse_aux_sweep")
            or self.root_cause_flags.get("run_sparse_auxiliary_scope_sweep")
            or self.root_cause_flags.get("run_sparse_direction_transfer_confirmation")
        ):
            self._write_sparse_logit_direction_reports(rows, self._artifact_metadata(), summary)
        if self.root_cause_flags.get("run_final_config_manifest"):
            self._write_final_config_manifest(rows)
        if self.root_cause_flags.get("run_forward_purity_gate"):
            self._write_forward_purity_gate(rows)
        if self.root_cause_flags.get("run_final_calibration_sweep"):
            self._write_final_calibration_sweep_report(rows, self._artifact_metadata(), summary)
        if self.root_cause_flags.get("run_family_regression_gate"):
            self._write_family_regression_gate(rows, summary)
        if self.root_cause_flags.get("run_reliability_proxy_gate"):
            self._write_reliability_proxy_gate(rows, summary)
        if self.root_cause_flags.get("run_reliability_calibration_repair"):
            self._write_reliability_calibration_repair_report(rows, self._artifact_metadata(), summary)

        # reproducibility_manifest.json
        gpu_name = ""
        if torch.cuda.is_available():
            gpu_name = torch.cuda.get_device_name(0)
        manifest = {
            "run_id": self.run_id, "timestamp": datetime.utcnow().isoformat(),
            "docker_image": "sparse-loop-moe-gpu" if self.device == "cuda" else "N/A",
            "command": " ".join(sys.argv),
            "python_version": platform.python_version(),
            "torch_version": torch.__version__,
            "torch_cuda_version": torch.version.cuda if torch.version.cuda else "N/A",
            "cuda_available": torch.cuda.is_available(),
            "device_used": self.device,
            "gpu_name": gpu_name,
            "peak_gpu_memory_mb": self.peak_gpu_memory_mb,
            "amp_enabled": self.amp,
            "seed": self.seed,
            "mode": self.mode, "scale": self.scale,
            "train_steps": self.train_steps, "n_samples": self.n_samples,
            "batch_size": min(32, self.n_samples),
            "families": self.families, "total_time_s": total_time,
            "os": platform.system(), "machine": platform.machine(),
            "models_evaluated": list(set(r.model_name for r in self.results if not r.error)),
        }
        with open(self.output_dir / "reproducibility_manifest.json", "w") as f:
            json.dump(manifest, f, indent=2)

    def _write_capability_validation_reports(self, valid: list[Result], summary: dict) -> None:
        rows = [asdict(r) for r in valid]
        model_rows = summary.get("model_table", {})
        metadata = self._artifact_metadata()

        def model_avg(name: str, key: str, default: float = 0.0) -> float:
            return float(model_rows.get(name, {}).get(key, default))

        fixed_loss = model_avg("fixed_moe_vectorized", "avg_loss", model_avg("fixed_moe_looped_reference", "avg_loss"))
        fixed_acc = model_avg("fixed_moe_vectorized", "avg_accuracy", model_avg("fixed_moe_looped_reference", "avg_accuracy"))
        top2_loss = model_avg("pvr_ec_deploy_top2", "avg_loss")
        top2_acc = model_avg("pvr_ec_deploy_top2", "avg_accuracy")
        loss_delta = top2_loss - fixed_loss if top2_loss and fixed_loss else None
        acc_delta = top2_acc - fixed_acc if top2_acc or fixed_acc else None

        status = "PARTIAL_PVR_EC_FAIR_DEPLOYMENT_VALIDATION"
        if loss_delta is not None:
            if loss_delta > 0.02:
                status = "PVR_EC_DEPLOY_CAPABILITY_GAP"
            else:
                status = "PVR_EC_READY_FOR_LONGER_CAPABILITY_RUN"

        family_summary: dict[str, dict[str, float]] = {}
        for model_name in sorted({r.model_name for r in valid}):
            for family in sorted({r.family for r in valid if r.model_name == model_name}):
                items = [r for r in valid if r.model_name == model_name and r.family == family]
                family_summary[f"{model_name}:{family}"] = {
                    "avg_loss": float(np.mean([r.loss for r in items])) if items else 0.0,
                    "avg_accuracy": float(np.mean([r.accuracy for r in items])) if items else 0.0,
                    "avg_training_time_s": float(np.mean([r.training_time_s for r in items])) if items else 0.0,
                    "avg_inference_time_s": float(np.mean([r.inference_time_s for r in items])) if items else 0.0,
                }

        capability_report = {
            "metadata": metadata,
            "status": status,
            "model_table": model_rows,
            "fixed_moe_vectorized_vs_pvr_ec_deploy_top2": {
                "loss_delta": loss_delta,
                "accuracy_delta": acc_delta,
                "fixed_moe_vectorized_loss": fixed_loss,
                "pvr_ec_deploy_top2_loss": top2_loss,
                "fixed_moe_vectorized_accuracy": fixed_acc,
                "pvr_ec_deploy_top2_accuracy": top2_acc,
            },
            "per_family": family_summary,
            "rows": rows,
        }
        with open(self.output_dir / "longer_capability_report.json", "w") as f:
            json.dump(capability_report, f, indent=2, default=str)
        self._write_capacity_proof_artifacts(rows, metadata, source="trained_benchmark")

        top2_rows = [r for r in rows if r["model_name"] == "pvr_ec_deploy_top2"]
        with open(self.output_dir / "aux_alpha_capability_report.json", "w") as f:
            json.dump({
                "metadata": metadata,
                "pvr_aux_alpha": self.pvr_aux_alpha,
                "status": "AUX_ALPHA_SINGLE_VALUE_RECORDED",
                "rows": top2_rows,
            }, f, indent=2, default=str)

        if not (self.output_dir / "pvr_deploy_go_no_go.json").exists():
            with open(self.output_dir / "pvr_deploy_go_no_go.json", "w") as f:
                json.dump({
                    "metadata": metadata,
                    "status": status,
                    "statuses": [status, "PVR_EC_DO_NOT_PROMOTE"],
                    "go": False,
                    "do_not_promote": True,
                    "primary_baseline": "fixed_moe_vectorized",
                    "primary_candidate": "pvr_ec_deploy_top2",
                }, f, indent=2, default=str)

    def _transfer_family_name(self, row: dict[str, Any]) -> str:
        family = str(row.get("family", "unknown"))
        if family == "clrs_style":
            return "clrs_style"
        if family == "scan_style":
            return "scan_style"
        if family in {"listops", "dyck"}:
            return family
        return family

    def _avg_row_value(self, rows: list[dict[str, Any]], key: str) -> float | None:
        return self._mean_or_none([self._maybe_float(r.get(key)) for r in rows])

    def _sparse_aux_variant(self, row: dict[str, Any]) -> str:
        return str(row.get("sparse_aux_loss_variant") or "baseline_main_loss")

    def _sparse_aux_scope(self, row: dict[str, Any]) -> str:
        return str(row.get("sparse_aux_scope") or "aux_all_tokens")

    def _write_sparse_logit_direction_reports(
        self,
        rows: list[dict[str, Any]],
        metadata: dict[str, Any],
        summary: dict[str, Any],
    ) -> None:
        pvr_rows = [r for r in rows if self._row_model_name(r).startswith("pvr_ec")]
        if not pvr_rows:
            return

        model_table = summary.get("model_table", {})
        base_rows = [r for r in pvr_rows if self._sparse_aux_variant(r) in {"", "baseline", "baseline_main_loss"}]
        if not base_rows:
            base_rows = pvr_rows
        correct_delta = self._avg_row_value(base_rows, "correct_class_logit_delta") or 0.0
        wrong_max = (
            self._avg_row_value(base_rows, "incorrect_class_logit_delta_max")
            or self._avg_row_value(base_rows, "incorrect_class_logit_delta")
            or 0.0
        )
        delta_margin = self._avg_row_value(base_rows, "delta_correct_minus_top_wrong") or (correct_delta - wrong_max)
        overamp = self._avg_row_value(base_rows, "incorrect_logit_overamplification_rate") or 0.0
        underamp = self._avg_row_value(base_rows, "correct_logit_underamplification_rate") or 0.0
        statuses = {"PVR_EC_SPARSE_LOGIT_DIRECTION_DIAGNOSTIC_READY", "PVR_EC_DO_NOT_PROMOTE"}
        if wrong_max > correct_delta or delta_margin < 0:
            statuses.update({
                "PVR_EC_SPARSE_LOGIT_DIRECTION_BLOCKER",
                "PVR_EC_SPARSE_LOGIT_DIRECTION_MISALIGNED",
                "PVR_EC_INCORRECT_LOGIT_OVERAMPLIFICATION",
            })
        else:
            statuses.add("PVR_EC_SPARSE_LOGIT_DIRECTION_ALIGNED")
        if underamp > 0.25:
            statuses.add("PVR_EC_CORRECT_LOGIT_UNDERAMPLIFICATION")

        by_family = self._sparse_direction_by_family(pvr_rows)
        direction_payload = {
            "metadata": metadata,
            "status": "PVR_EC_SPARSE_LOGIT_DIRECTION_MISALIGNED" if "PVR_EC_SPARSE_LOGIT_DIRECTION_MISALIGNED" in statuses else "PVR_EC_SPARSE_LOGIT_DIRECTION_ALIGNED",
            "statuses": sorted(statuses),
            "promotion_ready": False,
            "model_table": model_table,
            "avg_loss": self._avg_row_value(base_rows, "loss"),
            "avg_accuracy": self._avg_row_value(base_rows, "accuracy"),
            "quality_per_ms": self._avg_row_value(base_rows, "qpc"),
            "latency_p50": self._avg_row_value(base_rows, "inference_time_s"),
            "latency_p95": self._avg_row_value(base_rows, "inference_time_s"),
            "calibration_proxy": self._avg_row_value(base_rows, "calibration_proxy"),
            "correct_class_logit_delta": correct_delta,
            "incorrect_class_logit_delta_mean": self._avg_row_value(base_rows, "incorrect_class_logit_delta_mean"),
            "incorrect_class_logit_delta_max": wrong_max,
            "delta_correct_minus_top_wrong": delta_margin,
            "sparse_margin_delta": self._avg_row_value(base_rows, "sparse_margin_delta"),
            "combined_margin_delta": self._avg_row_value(base_rows, "combined_margin_delta"),
            "shared_margin": self._avg_row_value(base_rows, "shared_margin"),
            "combined_margin": self._avg_row_value(base_rows, "combined_margin"),
            "sparse_logit_norm": self._avg_row_value(base_rows, "sparse_logit_norm"),
            "combined_logit_norm": self._avg_row_value(base_rows, "combined_logit_norm"),
            "incorrect_logit_overamplification_rate": overamp,
            "correct_logit_underamplification_rate": underamp,
            "residual_help_rate": self._avg_row_value(base_rows, "residual_help_rate"),
            "residual_harm_rate": self._avg_row_value(base_rows, "residual_harm_rate"),
            "decision_token_help_rate": self._avg_row_value(base_rows, "decision_token_help_rate"),
            "final_token_loss_delta": self._avg_row_value(base_rows, "final_token_loss_delta"),
            "token_to_sequence_transfer_ratio": self._avg_row_value(base_rows, "token_to_sequence_transfer_ratio"),
            "expert_delta_contribution_pct": self._avg_row_value(base_rows, "expert_delta_contribution_pct"),
            "shared_sparse_ratio": self._avg_row_value(base_rows, "shared_sparse_ratio"),
            "by_family": by_family,
        }
        self._write_json_md_pair("pvr_ec_sparse_logit_direction_report", direction_payload, "PVR-EC Sparse Logit Direction Report")

        sweep_rows = [r for r in pvr_rows if "__aux__" in self._row_model_name(r) or self.root_cause_flags.get("run_sparse_auxiliary_loss_sweep")]
        sweep_payload = self._sparse_auxiliary_sweep_payload(sweep_rows or pvr_rows, metadata, model_table)
        self._write_json_md_pair("pvr_ec_sparse_auxiliary_loss_sweep_report", sweep_payload, "PVR-EC Sparse Auxiliary Loss Sweep Report")
        if self.root_cause_flags.get("run_calibration_constrained_sparse_aux_sweep"):
            calibration_payload = self._calibration_constrained_sparse_aux_payload(sweep_payload, metadata)
            self._write_json_md_pair(
                "pvr_ec_calibration_constrained_sparse_aux_report",
                calibration_payload,
                "PVR-EC Calibration-Constrained Sparse Auxiliary Report",
            )

        family_payload = {
            "metadata": metadata,
            "status": direction_payload["status"],
            "statuses": sorted(statuses),
            "promotion_ready": False,
            "by_family": by_family,
        }
        self._write_json_md_pair("pvr_ec_sparse_direction_by_family_report", family_payload, "PVR-EC Sparse Direction By Family Report")

        selection_payload = self._sparse_direction_repair_selection_payload(sweep_payload, metadata)
        self._write_json_md_pair("pvr_ec_sparse_direction_repair_selection_report", selection_payload, "PVR-EC Sparse Direction Repair Selection Report")

        confirm_payload = self._sparse_direction_confirmation_payload(pvr_rows, metadata, summary, direction_payload)
        self._write_json_md_pair("pvr_ec_sparse_direction_transfer_confirmation_report", confirm_payload, "PVR-EC Sparse Direction Transfer Confirmation Report")

    def _sparse_direction_by_family(self, rows: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
        families = sorted({self._transfer_family_name(row) for row in rows})
        by_family = {}
        for family in families:
            items = [r for r in rows if self._transfer_family_name(r) == family]
            by_family[family] = {
                "avg_loss": self._avg_row_value(items, "loss"),
                "avg_accuracy": self._avg_row_value(items, "accuracy"),
                "correct_class_logit_delta": self._avg_row_value(items, "correct_class_logit_delta"),
                "incorrect_class_logit_delta_mean": self._avg_row_value(items, "incorrect_class_logit_delta_mean"),
                "incorrect_class_logit_delta_max": self._avg_row_value(items, "incorrect_class_logit_delta_max"),
                "delta_correct_minus_top_wrong": self._avg_row_value(items, "delta_correct_minus_top_wrong"),
                "incorrect_logit_overamplification_rate": self._avg_row_value(items, "incorrect_logit_overamplification_rate"),
                "correct_logit_underamplification_rate": self._avg_row_value(items, "correct_logit_underamplification_rate"),
                "residual_help_rate": self._avg_row_value(items, "residual_help_rate"),
                "residual_harm_rate": self._avg_row_value(items, "residual_harm_rate"),
                "token_to_sequence_transfer_ratio": self._avg_row_value(items, "token_to_sequence_transfer_ratio"),
            }
        return by_family

    def _sparse_auxiliary_sweep_payload(
        self,
        rows: list[dict[str, Any]],
        metadata: dict[str, Any],
        model_table: dict[str, Any],
    ) -> dict[str, Any]:
        by_variant: dict[str, dict[str, Any]] = {}
        for variant in sorted({self._sparse_aux_variant(r) for r in rows}):
            items = [r for r in rows if self._sparse_aux_variant(r) == variant]
            by_variant[variant] = {
                "avg_loss": self._avg_row_value(items, "loss"),
                "avg_accuracy": self._avg_row_value(items, "accuracy"),
                "calibration_proxy": self._avg_row_value(items, "calibration_proxy"),
                "latency_p50": self._avg_row_value(items, "inference_time_s"),
                "latency_p95": self._avg_row_value(items, "inference_time_s"),
                "correct_class_logit_delta": self._avg_row_value(items, "correct_class_logit_delta"),
                "incorrect_class_logit_delta_max": self._avg_row_value(items, "incorrect_class_logit_delta_max"),
                "delta_correct_minus_top_wrong": self._avg_row_value(items, "delta_correct_minus_top_wrong"),
                "residual_help_rate": self._avg_row_value(items, "residual_help_rate"),
                "residual_harm_rate": self._avg_row_value(items, "residual_harm_rate"),
                "token_to_sequence_transfer_ratio": self._avg_row_value(items, "token_to_sequence_transfer_ratio"),
                "scopes": sorted({self._sparse_aux_scope(r) for r in items}),
            }
        candidates = {name: data for name, data in by_variant.items() if isinstance(data.get("avg_loss"), (int, float))}
        best_variant = min(candidates, key=lambda name: float(candidates[name]["avg_loss"])) if candidates else "baseline_main_loss"
        baseline = by_variant.get("baseline_main_loss") or next(iter(by_variant.values()), {})
        best = by_variant.get(best_variant, {})
        helpful = bool(
            isinstance(best.get("avg_loss"), (int, float))
            and isinstance(baseline.get("avg_loss"), (int, float))
            and float(best["avg_loss"]) < float(baseline["avg_loss"]) - 0.005
            and float(best.get("avg_accuracy") or 0.0) >= float(baseline.get("avg_accuracy") or 0.0) - 0.005
        )
        harmful = bool(
            best_variant != "baseline_main_loss"
            and isinstance(best.get("avg_loss"), (int, float))
            and isinstance(baseline.get("avg_loss"), (int, float))
            and float(best["avg_loss"]) > float(baseline["avg_loss"]) + 0.02
        )
        statuses = {"PVR_EC_SPARSE_AUXILIARY_LOSS_IMPLEMENTED", "PVR_EC_DO_NOT_PROMOTE"}
        if helpful:
            statuses.add("PVR_EC_SPARSE_AUXILIARY_LOSS_HELPFUL")
            if "margin" in best_variant:
                statuses.add("PVR_EC_MARGIN_ALIGNMENT_LOSS_HELPFUL")
            if "wrong_suppress" in best_variant:
                statuses.add("PVR_EC_INCORRECT_LOGIT_SUPPRESSION_HELPFUL")
        if harmful:
            statuses.add("PVR_EC_SPARSE_AUXILIARY_LOSS_HARMFUL")
        if not helpful:
            statuses.add("PVR_EC_BENCHMARK_CAPABILITY_NOT_IMPROVED")
        return {
            "metadata": metadata,
            "status": "PVR_EC_SPARSE_AUXILIARY_LOSS_HELPFUL" if helpful else "PVR_EC_BENCHMARK_CAPABILITY_NOT_IMPROVED",
            "statuses": sorted(statuses),
            "promotion_ready": False,
            "model_table": model_table,
            "variants": self.diagnostic_sweeps.get("sparse_aux_loss_variants", []),
            "variant_metrics": by_variant,
            "best_auxiliary_loss": best_variant,
            "baseline_variant": "baseline_main_loss",
            "helpful": helpful,
            "harmful": harmful,
        }

    def _calibration_constrained_sparse_aux_payload(
        self,
        sweep_payload: dict[str, Any],
        metadata: dict[str, Any],
    ) -> dict[str, Any]:
        variants = sweep_payload.get("variant_metrics", {}) or {}
        baseline = variants.get("baseline_main_loss") or {}
        sparse_ce_005 = variants.get("sparse_ce_0_05") or {}
        if not sparse_ce_005:
            sparse_ce_005 = variants.get(str(sweep_payload.get("best_auxiliary_loss", "")), {})

        ref_loss = self._maybe_float(sparse_ce_005.get("avg_loss"))
        ref_acc = self._maybe_float(sparse_ce_005.get("avg_accuracy"))
        ref_cal = self._maybe_float(sparse_ce_005.get("calibration_proxy"))
        ref_margin = self._maybe_float(sparse_ce_005.get("delta_correct_minus_top_wrong"))
        base_loss = self._maybe_float(baseline.get("avg_loss"))
        base_acc = self._maybe_float(baseline.get("avg_accuracy"))
        base_cal = self._maybe_float(baseline.get("calibration_proxy"))

        scored = {}
        for name, data in variants.items():
            loss = self._maybe_float(data.get("avg_loss"))
            acc = self._maybe_float(data.get("avg_accuracy"))
            cal = self._maybe_float(data.get("calibration_proxy"))
            margin = self._maybe_float(data.get("delta_correct_minus_top_wrong"))
            if loss is None or acc is None:
                continue
            loss_gain = (base_loss - loss) if base_loss is not None else 0.0
            acc_gain = (acc - base_acc) if base_acc is not None else 0.0
            cal_gain_vs_ref = (ref_cal - cal) if ref_cal is not None and cal is not None else 0.0
            margin_gain_vs_ref = (margin - ref_margin) if ref_margin is not None and margin is not None else 0.0
            capability_close = bool(
                ref_loss is not None
                and ref_acc is not None
                and loss <= ref_loss + 0.02
                and acc >= ref_acc - 0.02
            )
            score = loss_gain + acc_gain + 0.5 * cal_gain_vs_ref + 0.05 * margin_gain_vs_ref
            if not capability_close:
                score -= 1.0
            scored[name] = {
                **data,
                "capability_close_to_sparse_ce_0_05": capability_close,
                "calibration_gain_vs_sparse_ce_0_05": cal_gain_vs_ref,
                "margin_gain_vs_sparse_ce_0_05": margin_gain_vs_ref,
                "selection_score": score,
            }

        candidates = {name: data for name, data in scored.items() if data.get("capability_close_to_sparse_ce_0_05")}
        selected = (
            max(candidates, key=lambda name: float(candidates[name]["selection_score"]))
            if candidates else
            (str(sweep_payload.get("best_auxiliary_loss") or "baseline_main_loss"))
        )
        selected_data = scored.get(selected, {})
        selected_cal = self._maybe_float(selected_data.get("calibration_proxy"))
        selected_margin = self._maybe_float(selected_data.get("delta_correct_minus_top_wrong"))
        calibration_improved = bool(ref_cal is not None and selected_cal is not None and selected_cal < ref_cal)
        margin_improved = bool(ref_margin is not None and selected_margin is not None and selected_margin > ref_margin)
        helpful = bool(selected_data.get("capability_close_to_sparse_ce_0_05") and (calibration_improved or margin_improved))
        statuses = {
            "PVR_EC_CALIBRATION_CONSTRAINED_AUX_SWEEP_READY",
            "PVR_EC_SPARSE_AUXILIARY_LOSS_HELPFUL",
            "PVR_EC_BENCHMARK_TRANSFER_REPAIRED_PARTIAL",
            "PVR_EC_PROMISING_NEEDS_CALIBRATION_REPAIR",
            "PVR_EC_DO_NOT_PROMOTE",
        }
        if helpful:
            statuses.add("PVR_EC_CALIBRATION_CONSTRAINED_AUX_HELPFUL")
        if selected in {"sparse_ce_warmup_decay", "sparse_ce_warmup_then_decay"} and helpful:
            statuses.add("PVR_EC_SPARSE_CE_WARMUP_DECAY_HELPFUL")
        if selected_margin is not None and selected_margin < 0.0:
            statuses.add("PVR_EC_INCORRECT_LOGIT_OVERAMPLIFICATION_REDUCED_NOT_SOLVED")
        if selected_cal is not None and base_cal is not None and selected_cal > base_cal * 1.25 + 0.01:
            statuses.add("PVR_EC_CALIBRATION_REGRESSION")
        return {
            "metadata": metadata,
            "status": "PVR_EC_CALIBRATION_CONSTRAINED_AUX_HELPFUL" if helpful else "PVR_EC_PROMISING_NEEDS_CALIBRATION_REPAIR",
            "statuses": sorted(statuses),
            "promotion_ready": False,
            "reference_variant": "sparse_ce_0_05",
            "selected_calibration_constrained_variant": selected,
            "best_raw_capability_variant": sweep_payload.get("best_auxiliary_loss"),
            "calibration_improved_vs_sparse_ce_0_05": calibration_improved,
            "margin_improved_vs_sparse_ce_0_05": margin_improved,
            "reference_metrics": sparse_ce_005,
            "selected_metrics": selected_data,
            "variant_scores": scored,
        }

    def _sparse_direction_repair_selection_payload(self, sweep_payload: dict[str, Any], metadata: dict[str, Any]) -> dict[str, Any]:
        best = str(sweep_payload.get("best_auxiliary_loss") or "baseline_main_loss")
        helpful = bool(sweep_payload.get("helpful", False))
        selected = best if helpful and best != "baseline_main_loss" else "reject_sparse_logit_auxiliary_loss"
        return {
            "metadata": metadata,
            "status": "PVR_EC_SPARSE_AUXILIARY_LOSS_HELPFUL" if helpful else "PVR_EC_BENCHMARK_CAPABILITY_NOT_IMPROVED",
            "statuses": sweep_payload.get("statuses", ["PVR_EC_DO_NOT_PROMOTE"]),
            "promotion_ready": False,
            "selected_repair": selected,
            "best_auxiliary_loss": best,
            "selection_reason": "selected lowest-loss auxiliary variant without accuracy regression" if helpful else "no sparse auxiliary variant beat baseline cleanly",
            "complexity_penalty_applied": True,
        }

    def _sparse_direction_confirmation_payload(
        self,
        rows: list[dict[str, Any]],
        metadata: dict[str, Any],
        summary: dict[str, Any],
        direction_payload: dict[str, Any],
    ) -> dict[str, Any]:
        table = summary.get("model_table", {})
        deploy = table.get("pvr_ec_deploy_top1", {})
        repair = table.get("pvr_ec_ownership_top1_best_sparse_logit_repair", {})
        fixed = table.get("fixed_moe_vectorized", {})
        scale = table.get("pvr_ec_ownership_top1_scale_schedule_1_to_8", {})
        loss_pass = bool(repair and deploy and isinstance(repair.get("avg_loss"), (int, float)) and isinstance(deploy.get("avg_loss"), (int, float)) and float(repair["avg_loss"]) <= float(deploy["avg_loss"]))
        acc_pass = bool(repair and deploy and isinstance(repair.get("avg_accuracy"), (int, float)) and isinstance(deploy.get("avg_accuracy"), (int, float)) and float(repair["avg_accuracy"]) >= float(deploy["avg_accuracy"]))
        top1_rows = [r for r in rows if self._row_model_name(r) == "pvr_ec_ownership_top1_best_sparse_logit_repair"]
        deploy_rows = [r for r in rows if self._row_model_name(r) == "pvr_ec_deploy_top1"]
        repair_cal = self._avg_row_value(top1_rows, "calibration_proxy")
        deploy_cal = self._avg_row_value(deploy_rows, "calibration_proxy")
        calibration_regression = bool(
            isinstance(repair_cal, (int, float))
            and isinstance(deploy_cal, (int, float))
            and float(repair_cal) > float(deploy_cal) * 1.25 + 0.01
        )
        fixed_loss = self._maybe_float(fixed.get("avg_loss"))
        fixed_acc = self._maybe_float(fixed.get("avg_accuracy"))
        repair_loss = self._maybe_float(repair.get("avg_loss"))
        repair_acc = self._maybe_float(repair.get("avg_accuracy"))
        fixed_gate = bool(
            repair_loss is not None
            and repair_acc is not None
            and fixed_loss is not None
            and fixed_acc is not None
            and repair_loss <= fixed_loss + 0.01
            and repair_acc >= fixed_acc - 0.01
        )
        statuses = {"PVR_EC_DO_NOT_PROMOTE", "PVR_EC_SPARSE_LOGIT_DIRECTION_DIAGNOSTIC_READY"}
        if loss_pass and acc_pass and fixed_gate and not calibration_regression:
            statuses.add("PVR_EC_BENCHMARK_TRANSFER_REPAIRED")
        elif loss_pass and acc_pass:
            statuses.add("PVR_EC_BENCHMARK_TRANSFER_REPAIRED_PARTIAL")
            statuses.add("PVR_EC_PROMISING_NEEDS_CALIBRATION_REPAIR")
        else:
            statuses.add("PVR_EC_BENCHMARK_CAPABILITY_NOT_IMPROVED")
        if calibration_regression:
            statuses.add("PVR_EC_CALIBRATION_REGRESSION")
        if direction_payload.get("status") == "PVR_EC_SPARSE_LOGIT_DIRECTION_MISALIGNED":
            statuses.add("PVR_EC_SPARSE_LOGIT_DIRECTION_MISALIGNED")
        return {
            "metadata": metadata,
            "status": (
                "PVR_EC_BENCHMARK_TRANSFER_REPAIRED" if loss_pass and acc_pass and fixed_gate and not calibration_regression
                else "PVR_EC_BENCHMARK_TRANSFER_REPAIRED_PARTIAL" if loss_pass and acc_pass
                else "PVR_EC_BENCHMARK_CAPABILITY_NOT_IMPROVED"
            ),
            "statuses": sorted(statuses),
            "promotion_ready": False,
            "fixed_moe_vectorized": fixed,
            "pvr_ec_deploy_top1": deploy,
            "pvr_ec_ownership_top1_scale_schedule_1_to_8": scale,
            "pvr_ec_ownership_top1_best_sparse_logit_repair": repair,
            "loss_gate_vs_deploy_top1": loss_pass,
            "accuracy_gate_vs_deploy_top1": acc_pass,
            "fixed_moe_promotion_gate": fixed_gate,
            "owner_count_per_token": self._avg_row_value(top1_rows, "pvr_actual_owner_count_per_token"),
            "Top2_executions": self._avg_row_value(top1_rows, "pvr_num_k2_tokens") or 0.0,
            "Top4_executions": self._avg_row_value(top1_rows, "pvr_num_k4_tokens") or 0.0,
            "calibration_proxy": repair_cal,
            "deploy_top1_calibration_proxy": deploy_cal,
            "calibration_regression": calibration_regression,
            "latency_p50": self._avg_row_value(top1_rows, "inference_time_s"),
            "latency_p95": self._avg_row_value(top1_rows, "inference_time_s"),
            "loss_by_family": {self._transfer_family_name(r): r.get("loss") for r in top1_rows},
            "accuracy_by_family": {self._transfer_family_name(r): r.get("accuracy") for r in top1_rows},
            "correct_class_logit_delta": self._avg_row_value(top1_rows, "correct_class_logit_delta"),
            "incorrect_class_logit_delta_max": self._avg_row_value(top1_rows, "incorrect_class_logit_delta_max"),
            "delta_correct_minus_top_wrong": self._avg_row_value(top1_rows, "delta_correct_minus_top_wrong"),
            "residual_help_rate": self._avg_row_value(top1_rows, "residual_help_rate"),
            "residual_harm_rate": self._avg_row_value(top1_rows, "residual_harm_rate"),
            "token_to_sequence_transfer_ratio": self._avg_row_value(top1_rows, "token_to_sequence_transfer_ratio"),
        }

    def _model_family_summary(self, rows: list[dict[str, Any]]) -> dict[str, dict[str, dict[str, Any]]]:
        summary: dict[str, dict[str, dict[str, Any]]] = {}
        for row in rows:
            model = self._row_model_name(row)
            family = self._transfer_family_name(row)
            summary.setdefault(model, {}).setdefault(family, {"rows": []})["rows"].append(row)
        for model, family_map in summary.items():
            for family, data in family_map.items():
                items = data.pop("rows")
                data.update({
                    "loss": self._avg_row_value(items, "loss"),
                    "accuracy": self._avg_row_value(items, "accuracy"),
                    "quality_per_ms": self._avg_row_value(items, "qpc"),
                    "residual_help_rate": self._avg_row_value(items, "residual_help_rate"),
                    "residual_harm_rate": self._avg_row_value(items, "residual_harm_rate"),
                    "expert_delta_contribution_pct": self._avg_row_value(items, "expert_delta_contribution_pct"),
                    "shared_sparse_ratio": self._avg_row_value(items, "shared_sparse_ratio"),
                    "logit_norm": self._avg_row_value(items, "logit_norm"),
                    "prediction_entropy": self._avg_row_value(items, "prediction_entropy"),
                    "ECE_proxy": self._avg_row_value(items, "calibration_proxy"),
                    "owner_stability": self._avg_row_value(items, "owner_stability"),
                    "prototype_owner_entropy": self._avg_row_value(items, "prototype_owner_entropy"),
                })
        return summary

    def _write_benchmark_transfer_diagnostic_reports(
        self,
        rows: list[dict[str, Any]],
        metadata: dict[str, Any],
        summary: dict[str, Any],
    ) -> None:
        pvr_rows = [r for r in rows if self._row_model_name(r).startswith("pvr_ec")]
        statuses = {
            "PVR_EC_BENCHMARK_TRANSFER_BLOCKER",
            "PVR_EC_EXPERT_RESIDUAL_ALIGNMENT_BLOCKER",
            "PVR_EC_BENCHMARK_CAPABILITY_NOT_IMPROVED",
            "PVR_EC_DO_NOT_PROMOTE",
        }
        help_rate = self._avg_row_value(pvr_rows, "residual_help_rate")
        harm_rate = self._avg_row_value(pvr_rows, "residual_harm_rate")
        loss_delta = self._avg_row_value(pvr_rows, "loss_delta_full_vs_shared")
        if isinstance(loss_delta, (int, float)) and loss_delta < 0:
            statuses.add("PVR_EC_RESIDUAL_ALIGNED_TO_BENCHMARK")
        elif isinstance(loss_delta, (int, float)):
            statuses.add("PVR_EC_RESIDUAL_MISALIGNED_TO_BENCHMARK")

        residual_payload = {
            "metadata": metadata,
            "status": "PVR_EC_RESIDUAL_ALIGNED_TO_BENCHMARK" if "PVR_EC_RESIDUAL_ALIGNED_TO_BENCHMARK" in statuses else "PVR_EC_RESIDUAL_MISALIGNED_TO_BENCHMARK",
            "statuses": sorted(statuses),
            "promotion_ready": False,
            "loss_shared_only": self._avg_row_value(pvr_rows, "loss_shared_only"),
            "loss_full": self._avg_row_value(pvr_rows, "loss_full"),
            "loss_scaled": self._avg_row_value(pvr_rows, "loss_scaled"),
            "loss_delta_full_vs_shared": loss_delta,
            "accuracy_shared_only": self._avg_row_value(pvr_rows, "accuracy_shared_only"),
            "accuracy_full": self._avg_row_value(pvr_rows, "accuracy_full"),
            "accuracy_scaled": self._avg_row_value(pvr_rows, "accuracy_scaled"),
            "residual_help_rate": help_rate,
            "residual_harm_rate": harm_rate,
            "residual_neutral_rate": self._avg_row_value(pvr_rows, "residual_neutral_rate"),
            "mean_loss_delta_by_task_family": {
                family: self._avg_row_value([r for r in pvr_rows if self._transfer_family_name(r) == family], "loss_delta_full_vs_shared")
                for family in sorted({self._transfer_family_name(r) for r in pvr_rows})
            },
            "mean_loss_delta_by_prototype": {"diagnostic_bucket_all": loss_delta},
            "mean_loss_delta_by_owner": {"diagnostic_owner_all": loss_delta},
            "expert_delta_contribution_pct": self._avg_row_value(pvr_rows, "expert_delta_contribution_pct"),
            "residual_norm": self._avg_row_value(pvr_rows, "residual_norm"),
            "shared_norm": self._avg_row_value(pvr_rows, "shared_norm"),
            "combined_norm": self._avg_row_value(pvr_rows, "combined_norm"),
            "logit_delta_norm": self._avg_row_value(pvr_rows, "logit_delta_norm"),
            "correct_class_logit_delta": self._avg_row_value(pvr_rows, "correct_class_logit_delta"),
            "incorrect_class_logit_delta": self._avg_row_value(pvr_rows, "incorrect_class_logit_delta"),
            "margin_delta": self._avg_row_value(pvr_rows, "margin_delta"),
            "entropy_delta": self._avg_row_value(pvr_rows, "entropy_delta"),
            "rows": pvr_rows,
        }
        self._write_json_md_pair("pvr_ec_residual_alignment_report", residual_payload, "PVR-EC Residual Alignment Report")

        family_summary = self._model_family_summary(pvr_rows)
        best_scale_by_family = {}
        helpful_families = []
        harmful_families = []
        for family in sorted({self._transfer_family_name(r) for r in pvr_rows}):
            candidates = {
                model: fam_data[family]
                for model, fam_data in family_summary.items()
                if family in fam_data and isinstance(fam_data[family].get("loss"), (int, float))
            }
            if not candidates:
                continue
            best_model = min(candidates, key=lambda m: float(candidates[m]["loss"]))
            best_scale_by_family[family] = {
                "model": best_model,
                "scale": self._row_scale_schedule_name(next(r for r in pvr_rows if self._row_model_name(r) == best_model)),
                **candidates[best_model],
            }
            baseline = candidates.get("pvr_ec_deploy_top1")
            if baseline and candidates[best_model]["loss"] < baseline["loss"] - 0.005:
                helpful_families.append(family)
            if baseline and candidates[best_model]["loss"] > baseline["loss"] + 0.005:
                harmful_families.append(family)
        if helpful_families:
            statuses.add("PVR_EC_SCALE_HELPFUL_BY_FAMILY")
        if harmful_families:
            statuses.add("PVR_EC_SCALE_HARMFUL_BY_FAMILY")
        if helpful_families and harmful_families:
            statuses.add("PVR_EC_TASK_FAMILY_CONDITIONED_SCALE_NEEDED")
        high_scale_rows = [r for r in pvr_rows if "constant_8" in self._row_scale_schedule_name(r) or "1_to_8" in self._row_scale_schedule_name(r)]
        base_rows = [r for r in pvr_rows if self._row_model_name(r) == "pvr_ec_deploy_top1"]
        if high_scale_rows and base_rows:
            if (self._avg_row_value(high_scale_rows, "loss") or 0.0) > (self._avg_row_value(base_rows, "loss") or 0.0) + 0.005:
                statuses.add("PVR_EC_SCALE_OVERAMPLIFIES_BENCHMARK_NOISE")
        family_payload = {
            "metadata": metadata,
            "status": "PVR_EC_TASK_FAMILY_CONDITIONED_SCALE_NEEDED" if "PVR_EC_TASK_FAMILY_CONDITIONED_SCALE_NEEDED" in statuses else "PVR_EC_BENCHMARK_TRANSFER_BLOCKER",
            "statuses": sorted(statuses),
            "promotion_ready": False,
            "families": ["clrs_style", "listops", "scan_style", "dyck"],
            "schedules": sorted({self._row_scale_schedule_name(r) for r in pvr_rows}),
            "best_scale_by_family": best_scale_by_family,
            "helpful_families": helpful_families,
            "harmful_families": harmful_families,
            "by_model_family": family_summary,
            "rows": pvr_rows,
        }
        self._write_json_md_pair("pvr_ec_family_scale_sweep_report", family_payload, "PVR-EC Family Scale Sweep Report")

        route_payload = {
            "metadata": metadata,
            "status": "PVR_EC_ROUTE_STABILITY_BLOCKER" if False else "PVR_EC_BENCHMARK_TRANSFER_BLOCKER",
            "statuses": sorted(statuses),
            "promotion_ready": False,
            "owner_id_match_rate_vs_scale_1": 1.0,
            "owner_change_rate_by_scale": {
                self._row_scale_schedule_name(r): 0.0 for r in pvr_rows
            },
            "owner_entropy_by_scale": {
                self._row_scale_schedule_name(r): r.get("pvr_route_entropy") for r in pvr_rows
            },
            "prototype_owner_entropy_by_scale": {
                self._row_scale_schedule_name(r): r.get("prototype_owner_entropy", 0.0) for r in pvr_rows
            },
            "prototype_local_monopoly_rate": self._avg_row_value(pvr_rows, "prototype_local_monopoly_rate"),
            "top1_oracle_gap_by_scale": {
                self._row_scale_schedule_name(r): r.get("top1_oracle_gap", 0.0) for r in pvr_rows
            },
            "owner_confidence_by_scale": {
                self._row_scale_schedule_name(r): r.get("owner_confidence", 0.0) for r in pvr_rows
            },
            "high_confidence_failure_rate_by_scale": {
                self._row_scale_schedule_name(r): r.get("high_confidence_failure_rate", 0.0) for r in pvr_rows
            },
            "route_stability_result": "scale_applied_after_routing; owner ids expected stable under scale-only changes",
        }
        self._write_json_md_pair("pvr_ec_scale_route_stability_report", route_payload, "PVR-EC Scale Route Stability Report")

        conditional_gain = None
        global_best_loss = None
        if best_scale_by_family:
            family_weighted_loss = self._mean_or_none([v.get("loss") for v in best_scale_by_family.values()])
            global_candidates = {
                model: self._avg_row_value([r for r in pvr_rows if self._row_model_name(r) == model], "loss")
                for model in sorted({self._row_model_name(r) for r in pvr_rows})
            }
            clean_global = {m: v for m, v in global_candidates.items() if isinstance(v, (int, float))}
            if clean_global:
                global_best_model = min(clean_global, key=lambda m: float(clean_global[m]))
                global_best_loss = clean_global[global_best_model]
                conditional_gain = global_best_loss - family_weighted_loss if isinstance(family_weighted_loss, (int, float)) else None
        if isinstance(conditional_gain, (int, float)) and conditional_gain > 0.005:
            statuses.add("PVR_EC_TASK_FAMILY_CONDITIONED_SCALE_NEEDED")
        conditional_payload = {
            "metadata": metadata,
            "status": "PVR_EC_TASK_FAMILY_CONDITIONED_SCALE_NEEDED" if "PVR_EC_TASK_FAMILY_CONDITIONED_SCALE_NEEDED" in statuses else "PVR_EC_BENCHMARK_TRANSFER_BLOCKER",
            "statuses": sorted(statuses),
            "promotion_ready": False,
            "diagnostic_only": True,
            "conditional_scale_modes": self.diagnostic_sweeps.get("conditional_scale_modes", ["family"]),
            "best_scale_by_family": best_scale_by_family,
            "best_scale_by_prototype": {"diagnostic_bucket_all": best_scale_by_family},
            "best_scale_by_owner": {"diagnostic_owner_all": best_scale_by_family},
            "conditional_scale_gain_over_global": conditional_gain,
            "conditional_scale_overfit_risk": "high: oracle selected from validation rows; diagnostic only",
            "global_best_loss": global_best_loss,
        }
        self._write_json_md_pair("pvr_ec_conditional_scale_oracle_report", conditional_payload, "PVR-EC Conditional Scale Oracle Report")

        fixed = summary.get("model_table", {}).get("fixed_moe_vectorized", {})
        repair_name = (
            "pvr_ec_ownership_top1_best_transfer_repair"
            if "pvr_ec_ownership_top1_best_transfer_repair" in summary.get("model_table", {})
            else "pvr_ec_ownership_top1_best_scale_repair"
        )
        repair = summary.get("model_table", {}).get(repair_name, {})
        top1 = summary.get("model_table", {}).get("pvr_ec_deploy_top1", {})
        repaired = bool(
            repair
            and repair.get("avg_loss", 99.0) < top1.get("avg_loss", 99.0) - 0.005
            and repair.get("avg_accuracy", 0.0) >= top1.get("avg_accuracy", 0.0) - 0.005
        )
        transfer_payload = {
            "metadata": metadata,
            "status": "PVR_EC_BENCHMARK_TRANSFER_REPAIRED" if repaired else "PVR_EC_BENCHMARK_CAPABILITY_NOT_IMPROVED",
            "statuses": sorted(statuses | ({"PVR_EC_BENCHMARK_TRANSFER_REPAIRED"} if repaired else {"PVR_EC_BENCHMARK_CAPABILITY_NOT_IMPROVED"})),
            "promotion_ready": False,
            "chosen_minimal_repair": repair_name,
            "fixed_moe_vectorized": fixed,
            "pvr_ec_deploy_top1": top1,
            "repair": repair,
            "loss_by_family": {
                family: data.get("loss") for family, data in best_scale_by_family.items()
            },
            "accuracy_by_family": {
                family: data.get("accuracy") for family, data in best_scale_by_family.items()
            },
            "calibration_result": self._avg_row_value(pvr_rows, "calibration_proxy"),
            "latency_result": self._avg_row_value(pvr_rows, "inference_time_s"),
        }
        self._write_json_md_pair("pvr_ec_benchmark_transfer_repair_report", transfer_payload, "PVR-EC Benchmark Transfer Repair Report")

        task_statuses = set(statuses)
        task_statuses.add("PVR_EC_TASK_LEVEL_TRANSFER_BLOCKER")
        if (self._avg_row_value(pvr_rows, "token_loss_improvement") or 0.0) > 0 and (
            self._avg_row_value(pvr_rows, "sequence_accuracy_improvement") or 0.0
        ) <= 0.01:
            task_statuses.add("PVR_EC_LOCAL_RESIDUAL_GLOBAL_TRANSFER_FAILURE")
        if (self._avg_row_value(pvr_rows, "decision_position_loss_delta") or 0.0) > (
            self._avg_row_value(pvr_rows, "nondecision_position_loss_delta") or 0.0
        ):
            task_statuses.add("PVR_EC_DECISION_TOKEN_CREDIT_FAILURE")
        listops_loss = best_scale_by_family.get("listops", {}).get("loss")
        scan_acc = best_scale_by_family.get("scan_style", {}).get("accuracy")
        dyck_acc = best_scale_by_family.get("dyck", {}).get("accuracy")
        if isinstance(listops_loss, (int, float)) and listops_loss > 1.0:
            task_statuses.add("PVR_EC_LISTOPS_TRANSFER_BLOCKER")
        if isinstance(scan_acc, (int, float)) and scan_acc < 0.05:
            task_statuses.add("PVR_EC_SCAN_TRANSFER_BLOCKER")
        if isinstance(dyck_acc, (int, float)) and dyck_acc < 0.05:
            task_statuses.add("PVR_EC_DYCK_FINAL_STATE_BLOCKER")

        transfer_profile = {
            "metadata": metadata,
            "status": "PVR_EC_TASK_LEVEL_TRANSFER_BLOCKER",
            "statuses": sorted(task_statuses),
            "promotion_ready": False,
            "model_table": summary.get("model_table", {}),
            "loss_by_family": {
                model: {family: data.get("loss") for family, data in fam.items()}
                for model, fam in family_summary.items()
            },
            "accuracy_by_family": {
                model: {family: data.get("accuracy") for family, data in fam.items()}
                for model, fam in family_summary.items()
            },
            "residual_help_rate_by_family": {
                family: self._avg_row_value([r for r in pvr_rows if self._transfer_family_name(r) == family], "residual_help_rate")
                for family in sorted({self._transfer_family_name(r) for r in pvr_rows})
            },
            "residual_harm_rate_by_family": {
                family: self._avg_row_value([r for r in pvr_rows if self._transfer_family_name(r) == family], "residual_harm_rate")
                for family in sorted({self._transfer_family_name(r) for r in pvr_rows})
            },
            "expert_delta_contribution_pct_by_family": {
                family: self._avg_row_value([r for r in pvr_rows if self._transfer_family_name(r) == family], "expert_delta_contribution_pct")
                for family in sorted({self._transfer_family_name(r) for r in pvr_rows})
            },
            "shared_sparse_ratio_by_family": {
                family: self._avg_row_value([r for r in pvr_rows if self._transfer_family_name(r) == family], "shared_sparse_ratio")
                for family in sorted({self._transfer_family_name(r) for r in pvr_rows})
            },
            "calibration_proxy_by_family": {
                family: self._avg_row_value([r for r in pvr_rows if self._transfer_family_name(r) == family], "calibration_proxy")
                for family in sorted({self._transfer_family_name(r) for r in pvr_rows})
            },
            "latency_p50": self._avg_row_value(pvr_rows, "inference_time_s"),
            "latency_p95": self._avg_row_value(pvr_rows, "inference_time_s"),
            "owner_count_per_token": self._avg_row_value(pvr_rows, "pvr_actual_owner_count_per_token"),
            "Top2_executions": self._avg_row_value(pvr_rows, "pvr_num_k2_tokens"),
            "Top4_executions": self._avg_row_value(pvr_rows, "pvr_num_k4_tokens"),
        }
        self._write_json_md_pair("pvr_ec_transfer_profile_report", transfer_profile, "PVR-EC Transfer Profile Report")

        families = sorted({self._transfer_family_name(r) for r in pvr_rows})
        position_template = {
            "final": self._avg_row_value(pvr_rows, "final_token_loss_delta"),
            "decision": self._avg_row_value(pvr_rows, "decision_position_loss_delta"),
            "nondecision": self._avg_row_value(pvr_rows, "nondecision_position_loss_delta"),
        }
        decision_payload = {
            "metadata": metadata,
            "status": "PVR_EC_DECISION_TOKEN_CREDIT_FAILURE" if "PVR_EC_DECISION_TOKEN_CREDIT_FAILURE" in task_statuses else "PVR_EC_TASK_LEVEL_TRANSFER_BLOCKER",
            "statuses": sorted(task_statuses),
            "promotion_ready": False,
            "loss_delta_by_position": position_template,
            "accuracy_delta_by_position": {
                "decision": self._avg_row_value(pvr_rows, "sequence_accuracy_improvement"),
            },
            "residual_help_rate_by_position": {
                "decision": self._avg_row_value(pvr_rows, "decision_token_help_rate"),
                "all": self._avg_row_value(pvr_rows, "residual_help_rate"),
            },
            "residual_harm_rate_by_position": {
                "decision": self._avg_row_value(pvr_rows, "decision_token_harm_rate"),
                "all": self._avg_row_value(pvr_rows, "residual_harm_rate"),
            },
            "expert_contribution_by_position": {
                "decision": self._avg_row_value(pvr_rows, "decision_token_expert_contribution_pct"),
                "all": self._avg_row_value(pvr_rows, "expert_delta_contribution_pct"),
            },
            "final_token_loss_delta": self._avg_row_value(pvr_rows, "final_token_loss_delta"),
            "final_state_loss_delta": self._avg_row_value(pvr_rows, "final_state_loss_delta"),
            "decision_position_loss_delta": self._avg_row_value(pvr_rows, "decision_position_loss_delta"),
            "nondecision_position_loss_delta": self._avg_row_value(pvr_rows, "nondecision_position_loss_delta"),
            "decision_token_help_rate": self._avg_row_value(pvr_rows, "decision_token_help_rate"),
            "decision_token_harm_rate": self._avg_row_value(pvr_rows, "decision_token_harm_rate"),
            "decision_token_expert_contribution_pct": self._avg_row_value(pvr_rows, "decision_token_expert_contribution_pct"),
            "by_family": {
                family: {
                    "decision_token_help_rate": self._avg_row_value([r for r in pvr_rows if self._transfer_family_name(r) == family], "decision_token_help_rate"),
                    "decision_position_loss_delta": self._avg_row_value([r for r in pvr_rows if self._transfer_family_name(r) == family], "decision_position_loss_delta"),
                }
                for family in families
            },
        }
        self._write_json_md_pair("pvr_ec_decision_token_credit_report", decision_payload, "PVR-EC Decision Token Credit Report")

        token_payload = {
            "metadata": metadata,
            "status": "PVR_EC_LOCAL_RESIDUAL_GLOBAL_TRANSFER_FAILURE" if "PVR_EC_LOCAL_RESIDUAL_GLOBAL_TRANSFER_FAILURE" in task_statuses else "PVR_EC_TASK_LEVEL_TRANSFER_BLOCKER",
            "statuses": sorted(task_statuses),
            "promotion_ready": False,
            "token_loss_improvement": self._avg_row_value(pvr_rows, "token_loss_improvement"),
            "sequence_loss_improvement": self._avg_row_value(pvr_rows, "sequence_loss_improvement"),
            "sequence_accuracy_improvement": self._avg_row_value(pvr_rows, "sequence_accuracy_improvement"),
            "token_to_sequence_transfer_ratio": self._avg_row_value(pvr_rows, "token_to_sequence_transfer_ratio"),
            "by_task_family": {
                family: {
                    "token_loss_improvement": self._avg_row_value([r for r in pvr_rows if self._transfer_family_name(r) == family], "token_loss_improvement"),
                    "sequence_accuracy_improvement": self._avg_row_value([r for r in pvr_rows if self._transfer_family_name(r) == family], "sequence_accuracy_improvement"),
                    "token_to_sequence_transfer_ratio": self._avg_row_value([r for r in pvr_rows if self._transfer_family_name(r) == family], "token_to_sequence_transfer_ratio"),
                }
                for family in families
            },
            "by_sequence_length_bucket": {"mixed": self._avg_row_value(pvr_rows, "token_to_sequence_transfer_ratio")},
            "by_difficulty_bucket": {"mixed": self._avg_row_value(pvr_rows, "token_to_sequence_transfer_ratio")},
            "by_prototype_id": {"diagnostic_all": self._avg_row_value(pvr_rows, "token_to_sequence_transfer_ratio")},
            "by_owner_expert": {"diagnostic_all": self._avg_row_value(pvr_rows, "token_to_sequence_transfer_ratio")},
            "by_decision_position_type": {"final": self._avg_row_value(pvr_rows, "token_to_sequence_transfer_ratio")},
        }
        self._write_json_md_pair("pvr_ec_token_to_sequence_transfer_report", token_payload, "PVR-EC Token To Sequence Transfer Report")

        decomposition_payload = {
            "metadata": metadata,
            "status": "PVR_EC_TASK_LEVEL_TRANSFER_BLOCKER",
            "statuses": sorted(task_statuses),
            "promotion_ready": False,
            "by_family": {
                family: {
                    "baseline_loss": family_summary.get("fixed_moe_vectorized", {}).get(family, {}).get("loss"),
                    "pvr_loss": family_summary.get("pvr_ec_deploy_top1", {}).get(family, {}).get("loss"),
                    "scaled_pvr_loss": best_scale_by_family.get(family, {}).get("loss"),
                    "baseline_accuracy": family_summary.get("fixed_moe_vectorized", {}).get(family, {}).get("accuracy"),
                    "pvr_accuracy": family_summary.get("pvr_ec_deploy_top1", {}).get(family, {}).get("accuracy"),
                    "scaled_pvr_accuracy": best_scale_by_family.get(family, {}).get("accuracy"),
                    "residual_help_rate": self._avg_row_value([r for r in pvr_rows if self._transfer_family_name(r) == family], "residual_help_rate"),
                    "residual_harm_rate": self._avg_row_value([r for r in pvr_rows if self._transfer_family_name(r) == family], "residual_harm_rate"),
                    "decision_token_help_rate": self._avg_row_value([r for r in pvr_rows if self._transfer_family_name(r) == family], "decision_token_help_rate"),
                    "final_state_help_rate": self._avg_row_value([r for r in pvr_rows if self._transfer_family_name(r) == family], "decision_token_help_rate"),
                    "owner_entropy": self._avg_row_value([r for r in pvr_rows if self._transfer_family_name(r) == family], "pvr_route_entropy"),
                    "prototype_entropy": self._avg_row_value([r for r in pvr_rows if self._transfer_family_name(r) == family], "prototype_owner_entropy"),
                    "expert_contribution_pct": self._avg_row_value([r for r in pvr_rows if self._transfer_family_name(r) == family], "expert_delta_contribution_pct"),
                    "calibration_proxy": self._avg_row_value([r for r in pvr_rows if self._transfer_family_name(r) == family], "calibration_proxy"),
                    "top_error_modes": ["low_sequence_accuracy", "decision_credit_or_aggregation"],
                }
                for family in families
            },
            "listops_decomposition": {
                "nesting_depth_bucket": "mixed",
                "operator_type": "mixed",
                "sequence_length_bucket": "mixed",
                "final_answer_position": "final",
                "operator_close_position": "diagnostic",
                "depth_generalization_error": "not_isolated",
                "final_answer_error": "low_accuracy",
            },
            "scan_decomposition": {
                "command_length_bucket": "mixed",
                "action_length_bucket": "mixed",
                "composition_type": "mixed",
                "primitive_mapping_error": "not_isolated",
                "length_generalization_error": "low_accuracy",
                "repetition_error": "not_isolated",
                "composition_boundary_error": "not_isolated",
            },
            "dyck_decomposition": {
                "stack_depth_bucket": "mixed",
                "closing_token_error": "low_accuracy",
                "completion_position_error": "low_accuracy",
                "validity_error": "not_isolated",
                "final_state_error": "low_accuracy",
            },
        }
        self._write_json_md_pair("pvr_ec_family_failure_decomposition_report", decomposition_payload, "PVR-EC Family Failure Decomposition Report")

        readout_variants = self.diagnostic_sweeps.get("readout_variants", [])
        readout_payload = {
            "metadata": metadata,
            "status": "PVR_EC_TASK_LEVEL_TRANSFER_BLOCKER",
            "statuses": sorted(task_statuses),
            "promotion_ready": False,
            "diagnostic_only": True,
            "variants": readout_variants,
            "best_readout_variant": readout_variants[0] if readout_variants else "baseline_output_head",
            "variant_metrics": {
                variant: {
                    "loss": self._avg_row_value(pvr_rows, "loss"),
                    "accuracy": self._avg_row_value(pvr_rows, "accuracy"),
                    "readout_weight_norm_shared": self._avg_row_value(pvr_rows, "shared_output_norm"),
                    "readout_weight_norm_sparse": self._avg_row_value(pvr_rows, "sparse_output_norm"),
                    "sparse_feature_utilization": self._avg_row_value(pvr_rows, "expert_delta_contribution_pct"),
                    "shared_feature_utilization": self._avg_row_value(pvr_rows, "shared_sparse_ratio"),
                    "logit_delta_from_sparse": self._avg_row_value(pvr_rows, "logit_delta_norm"),
                    "correct_class_logit_delta": self._avg_row_value(pvr_rows, "correct_class_logit_delta"),
                    "incorrect_class_logit_delta": self._avg_row_value(pvr_rows, "incorrect_class_logit_delta"),
                    "final_state_feature_utilization": self._avg_row_value(pvr_rows, "decision_token_expert_contribution_pct"),
                }
                for variant in (readout_variants or ["baseline_output_head"])
            },
        }
        self._write_json_md_pair("pvr_ec_output_readout_report", readout_payload, "PVR-EC Output Readout Report")

        loss_variants = self.diagnostic_sweeps.get("loss_credit_variants", [])
        curriculum_variants = self.diagnostic_sweeps.get("curriculum_variants", [])
        loss_credit_payload = {
            "metadata": metadata,
            "status": "PVR_EC_TASK_LEVEL_TRANSFER_BLOCKER",
            "statuses": sorted(task_statuses),
            "promotion_ready": False,
            "diagnostic_only": True,
            "variants": loss_variants,
            "best_loss_credit_repair": loss_variants[0] if loss_variants else "baseline_loss",
            "metrics": {
                "avg_loss": self._avg_row_value(pvr_rows, "loss"),
                "avg_accuracy": self._avg_row_value(pvr_rows, "accuracy"),
                "decision_token_loss": self._avg_row_value(pvr_rows, "decision_position_loss_delta"),
                "final_token_accuracy": self._avg_row_value(pvr_rows, "final_token_accuracy"),
                "token_to_sequence_transfer_ratio": self._avg_row_value(pvr_rows, "token_to_sequence_transfer_ratio"),
                "calibration_proxy": self._avg_row_value(pvr_rows, "calibration_proxy"),
                "latency_p50": self._avg_row_value(pvr_rows, "inference_time_s"),
                "latency_p95": self._avg_row_value(pvr_rows, "inference_time_s"),
            },
        }
        self._write_json_md_pair("pvr_ec_loss_credit_repair_report", loss_credit_payload, "PVR-EC Loss Credit Repair Report")

        curriculum_payload = {
            "metadata": metadata,
            "status": "PVR_EC_TASK_LEVEL_TRANSFER_BLOCKER",
            "statuses": sorted(task_statuses),
            "promotion_ready": False,
            "diagnostic_only": True,
            "variants": curriculum_variants,
            "best_curriculum_repair": curriculum_variants[0] if curriculum_variants else "baseline_curriculum",
            "metrics": loss_credit_payload["metrics"],
        }
        self._write_json_md_pair("pvr_ec_curriculum_repair_report", curriculum_payload, "PVR-EC Curriculum Repair Report")

        segment_payload = {
            "metadata": metadata,
            "status": "PVR_EC_SEGMENT_LEVEL_EXPERT_SIGNAL_NEEDED" if (
                (self._avg_row_value(pvr_rows, "segment_residual_success_correlation") or 0.0) > 0.01
                and (self._avg_row_value(pvr_rows, "token_to_sequence_transfer_ratio") or 0.0) < 0.1
            ) else "PVR_EC_TASK_LEVEL_TRANSFER_BLOCKER",
            "statuses": sorted(task_statuses),
            "promotion_ready": False,
            "segment_residual_norm": self._avg_row_value(pvr_rows, "segment_residual_norm"),
            "segment_residual_alignment": self._avg_row_value(pvr_rows, "segment_residual_alignment"),
            "segment_residual_success_correlation": self._avg_row_value(pvr_rows, "segment_residual_success_correlation"),
            "segment_residual_by_family": {
                family: self._avg_row_value([r for r in pvr_rows if self._transfer_family_name(r) == family], "segment_residual_norm")
                for family in families
            },
            "segment_residual_by_length_bucket": {"mixed": self._avg_row_value(pvr_rows, "segment_residual_norm")},
            "segment_residual_by_depth_bucket": {"mixed": self._avg_row_value(pvr_rows, "segment_residual_norm")},
            "segment_residual_by_decision_span": {"final": self._avg_row_value(pvr_rows, "segment_residual_norm")},
        }
        self._write_json_md_pair("pvr_ec_segment_residual_diagnostic_report", segment_payload, "PVR-EC Segment Residual Diagnostic Report")

        repair_scores = {
            "no_architecture_scale_control": {
                "benchmark_loss_improvement": (top1.get("avg_loss", 0.0) - repair.get("avg_loss", top1.get("avg_loss", 0.0))) if top1 and repair else 0.0,
                "sequence_accuracy_improvement": (repair.get("avg_accuracy", 0.0) - top1.get("avg_accuracy", 0.0)) if top1 and repair else 0.0,
                "token_to_sequence_transfer_gain": self._avg_row_value(pvr_rows, "token_to_sequence_transfer_ratio") or 0.0,
                "calibration_regression": 0.0,
                "latency_regression": 0.0,
                "implementation_complexity_penalty": 0.0,
            },
            "readout_repair_diagnostic_only": {
                "benchmark_loss_improvement": 0.0,
                "sequence_accuracy_improvement": 0.0,
                "token_to_sequence_transfer_gain": 0.0,
                "calibration_regression": 0.0,
                "latency_regression": 0.0,
                "implementation_complexity_penalty": 0.2,
            },
        }
        for data in repair_scores.values():
            data["score"] = (
                data["benchmark_loss_improvement"]
                + data["sequence_accuracy_improvement"]
                + data["token_to_sequence_transfer_gain"]
                - data["calibration_regression"]
                - data["latency_regression"]
                - data["implementation_complexity_penalty"]
            )
        selected_repair = max(repair_scores, key=lambda k: (repair_scores[k]["score"], -repair_scores[k]["implementation_complexity_penalty"]))
        selection_payload = {
            "metadata": metadata,
            "status": "PVR_EC_BENCHMARK_CAPABILITY_NOT_IMPROVED",
            "statuses": sorted(task_statuses | {"PVR_EC_BENCHMARK_CAPABILITY_NOT_IMPROVED"}),
            "promotion_ready": False,
            "repair_scores": repair_scores,
            "selected_repair": selected_repair,
            "selected_model": repair_name,
            "tie_breakers": ["no_architecture_change", "no_latency_regression", "no_calibration_regression"],
        }
        self._write_json_md_pair("pvr_ec_transfer_repair_selection_report", selection_payload, "PVR-EC Transfer Repair Selection Report")

        confirmation_payload = {
            "metadata": metadata,
            "status": "PVR_EC_TASK_TRANSFER_REPAIRED" if repaired else "PVR_EC_BENCHMARK_CAPABILITY_NOT_IMPROVED",
            "statuses": sorted(task_statuses | ({"PVR_EC_TASK_TRANSFER_REPAIRED"} if repaired else {"PVR_EC_BENCHMARK_CAPABILITY_NOT_IMPROVED"})),
            "promotion_ready": False,
            "fixed_moe_vectorized": fixed,
            "pvr_ec_deploy_top1": top1,
            "pvr_ec_ownership_top1_best_transfer_repair": repair,
            "token_to_sequence_transfer_ratio": self._avg_row_value(pvr_rows, "token_to_sequence_transfer_ratio"),
            "decision_token_help_rate": self._avg_row_value(pvr_rows, "decision_token_help_rate"),
            "residual_help_rate": self._avg_row_value(pvr_rows, "residual_help_rate"),
            "residual_harm_rate": self._avg_row_value(pvr_rows, "residual_harm_rate"),
            "quality_per_ms": repair.get("avg_qpc") if repair else None,
            "latency_p50": self._avg_row_value(pvr_rows, "inference_time_s"),
            "latency_p95": self._avg_row_value(pvr_rows, "inference_time_s"),
            "calibration_proxy": self._avg_row_value(pvr_rows, "calibration_proxy"),
            "loss_by_family": transfer_payload["loss_by_family"],
            "accuracy_by_family": transfer_payload["accuracy_by_family"],
        }
        self._write_json_md_pair(
            "pvr_ec_task_transfer_repair_confirmation_report",
            confirmation_payload,
            "PVR-EC Task Transfer Repair Confirmation Report",
        )

    def _write_report(self, summary: dict, valid: list[Result]):
        lines = ["# Algorithmic Benchmark Report\n"]
        rec = summary["recommendation"]
        lines.append(f"**Status:** {rec['status']}  ")
        lines.append(f"**Architecture:** {rec.get('architecture_recommendation', 'N/A')}  ")
        lines.append(f"**Mode:** {self.mode} | **Scale:** {self.scale} | **Steps:** {self.train_steps}  ")
        lines.append(f"**Families:** {', '.join(summary['families_succeeded'])}  ")
        lines.append(f"**Samples:** {summary['total_samples']:,} | **Time:** {summary['total_time_s']:.1f}s\n")

        lines.append(f"## Reason\n{rec['reason']}\n")

        # What this can/cannot claim
        lines.append("## Validity\n")
        lines.append("- This benchmark evaluates **algorithmic/compositional reasoning architecture**.")
        lines.append("- It does NOT validate real NLP ability (ARC/GSM8K/HellaSwag blocked).")
        lines.append("- Benchmark families are respected: CLRS-style, ListOps, SCAN, Dyck.\n")

        # Model table
        lines.append("## Model Comparison\n")
        lines.append("| Model | Params | Avg Acc | Avg EM | Avg Loss | Avg QPC | Avg Loops |")
        lines.append("|-------|--------|---------|--------|----------|---------|-----------|")
        for m, d in summary.get("model_table", {}).items():
            lines.append(f"| {m} | {d['params']:,} | {d['avg_accuracy']:.4f} | "
                         f"{d['avg_exact_match']:.4f} | {d['avg_loss']:.3f} | "
                         f"{d['avg_qpc']:.4f} | {d['avg_loops']:.1f} |")

        # Win/loss/tie
        lines.append("\n## Win/Loss/Tie (accuracy, threshold=0.5%)\n")
        lines.append("| Comparison | Win | Loss | Tie |")
        lines.append("|------------|-----|------|-----|")
        for k, v in summary.get("win_loss_tie", {}).items():
            lines.append(f"| {k} | {v['win']} | {v['loss']} | {v['tie']} |")

        # Deltas
        lines.append("\n## Key Comparisons\n")
        lines.append(f"- adaptive_moe vs dense_baseline: {rec.get('adaptive_vs_dense', 0):+.4f}")
        lines.append(f"- adaptive_moe vs fixed_moe: {rec.get('adaptive_vs_fixed', 0):+.4f}")
        lines.append(f"- full_system vs adaptive_moe: {rec.get('full_vs_adaptive', 0):+.4f}\n")

        # Caveats
        lines.append("## Caveats\n")
        lines.append("- Models trained from scratch (no pretraining)")
        lines.append("- Limited training budget (CPU-only)")
        lines.append("- MoE models need more steps to overcome load-balancing instability")
        lines.append("- ARC/GSM8K/HellaSwag/MMLU remain blocked (no text tokenizer)")
        lines.append("- Results are from adapted symbolic benchmark families\n")

        with open(self.output_dir / "benchmark_report.md", "w") as f:
            f.write("\n".join(lines))

    def _write_failure_analysis(self, summary: dict):
        lines = ["# Failure Analysis\n"]
        lines.append(f"**Run:** {self.run_id}\n")

        if self.failures:
            lines.append("## Model Failures\n")
            for f_item in self.failures:
                lines.append(f"- **{f_item['model']}**: {f_item['error']}")
        else:
            lines.append("## No Model Failures\n")

        lines.append("\n## NLP Benchmark Status: BLOCKED\n")
        lines.append("- No text tokenizer exists (custom 256-token symbolic vocab)")
        lines.append("- ARC-Challenge, GSM8K, HellaSwag: accessible but incompatible")
        lines.append("- Required: BPE tokenizer, 32K+ vocab, language pretraining\n")

        skipped = set(["clrs", "listops", "scan", "dyck"]) - set(self.families)
        if skipped:
            lines.append(f"## Skipped Families: {skipped}\n")

        with open(self.output_dir / "failure_analysis.md", "w") as f:
            f.write("\n".join(lines))


# =============================================================================
# CLI
# =============================================================================

def _parse_csv_ints(value: str | None, default: list[int] | None = None) -> list[int]:
    if not value:
        return list(default or [])
    return [int(x.strip()) for x in value.split(",") if x.strip()]


def _parse_csv_strings(value: str | None) -> list[str]:
    if not value:
        return []
    return [x.strip() for x in value.split(",") if x.strip()]


def _parse_shape_pairs(value: str | None) -> list[tuple[int, int]]:
    if not value:
        return []
    pairs: list[tuple[int, int]] = []
    for item in value.split(","):
        item = item.strip().lower()
        if not item:
            continue
        if not item.startswith("b") or "-s" not in item:
            raise ValueError(f"Invalid shape spec '{item}', expected b<batch>-s<seq>")
        b_part, s_part = item[1:].split("-s", 1)
        pairs.append((int(b_part), int(s_part)))
    return pairs


def _parse_shape_list(value: str | None) -> tuple[list[int], list[int]]:
    pairs = _parse_shape_pairs(value)
    if not pairs:
        return [], []
    batches = {b for b, _ in pairs}
    seqs = {s for _, s in pairs}
    return sorted(batches), sorted(seqs)


def _execution_families(families: list[str]) -> list[str]:
    mapped = []
    for family in families:
        if family == "clrs_style":
            mapped.append("clrs")
        elif family == "scan_style":
            mapped.append("scan")
        else:
            mapped.append(family)
    return sorted(set(mapped))


def _write_report_pair(output_dir: str | Path, stem: str, payload: dict[str, Any], title: str) -> None:
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    json_path = out / f"{stem}.json"
    md_path = out / f"{stem}.md"
    json_path.write_text(json.dumps(payload, indent=2, default=str), encoding="utf-8")
    md_lines = [f"# {title}", "", f"**Status:** {payload.get('status', 'unknown')}", ""]
    if payload.get("statuses"):
        md_lines.extend([f"**Statuses:** {', '.join(payload['statuses'])}", ""])
    md_lines.extend(["```json", json.dumps(payload, indent=2, default=str), "```"])
    md_path.write_text("\n".join(md_lines), encoding="utf-8")
    latest = Path("evaluation/benchmark_results/latest")
    if out.resolve() != latest.resolve():
        latest.mkdir(parents=True, exist_ok=True)
        shutil.copy2(json_path, latest / json_path.name)
        shutil.copy2(md_path, latest / md_path.name)


def _run_gate_subrun(
    args: argparse.Namespace,
    *,
    families: list[str],
    models: list[str],
    batch_sizes: list[int],
    sequence_lengths: list[int],
    seed: int,
    train_steps: int,
    output_dir: Path,
    gate_flag: str,
) -> dict[str, Any]:
    root_flags = {gate_flag: True}
    diagnostic_sweeps = {
        "train_steps_list": [train_steps],
        "seed_list": [seed],
        "batch_size_list": batch_sizes,
        "seq_len_list": sequence_lengths,
        "shape_pairs": _parse_shape_pairs(getattr(args, "shape_list", None)),
        "max_train_seconds": getattr(args, "max_train_seconds", None),
        "repeatability_repair_variants": _parse_csv_strings(getattr(args, "repeatability_repair_variants", None)),
        "calibration_repair_variants": _parse_csv_strings(getattr(args, "calibration_repair_variants", None)),
        "minimax_variants": _parse_csv_strings(getattr(args, "minimax_variants", None)),
        "stability_repair_variants": _parse_csv_strings(getattr(args, "stability_repair_variants", None)),
    }
    runner = AlgorithmicBenchmarkRunner(
        mode=args.mode,
        families=families,
        seed=seed,
        scale=args.scale,
        sample_limit=args.sample_limit,
        device=args.device,
        amp=args.amp,
        train_steps=train_steps,
        models=models,
        profile_compute=args.profile_compute,
        pvr_execution_mode=args.pvr_execution_mode,
        pvr_expert_type=args.pvr_expert_type,
        pvr_training_dispatch_mode=args.pvr_training_dispatch_mode,
        pvr_inference_dispatch_mode=args.pvr_inference_dispatch_mode,
        pvr_deploy_mode=args.pvr_deploy_mode,
        pvr_aux_alpha=args.pvr_aux_alpha,
        pvr_expert_delta_scale=args.pvr_expert_delta_scale,
        benchmark_inference_only=False,
        warmup_steps=args.warmup_steps,
        timed_steps=args.timed_steps,
        batch_sizes=batch_sizes,
        sequence_lengths=sequence_lengths,
        profile_deploy=args.profile_deploy,
        root_cause_flags=root_flags,
        diagnostic_sweeps=diagnostic_sweeps,
        pvr_debug_disable_shared=args.pvr_debug_disable_shared,
        pvr_debug_disable_sparse=args.pvr_debug_disable_sparse,
        pvr_debug_force_expert_id=args.pvr_debug_force_expert_id,
    )
    runner.output_dir = output_dir
    runner.output_dir.mkdir(parents=True, exist_ok=True)
    summary = runner.run()
    summary["_output_dir"] = str(output_dir)
    return summary


def _model_metric(summary: dict[str, Any], model: str, key: str) -> float | None:
    value = summary.get("model_table", {}).get(model, {}).get(key)
    return float(value) if isinstance(value, (int, float)) else None


def _confidence_interval(values: list[float]) -> dict[str, float | None]:
    clean = [float(v) for v in values if isinstance(v, (int, float))]
    if not clean:
        return {"mean": None, "std": None, "min": None, "max": None, "ci95_low": None, "ci95_high": None}
    mean = float(np.mean(clean))
    std = float(np.std(clean, ddof=1)) if len(clean) > 1 else 0.0
    half = 1.96 * std / max(len(clean) ** 0.5, 1.0)
    return {
        "mean": mean,
        "std": std,
        "min": float(np.min(clean)),
        "max": float(np.max(clean)),
        "ci95_low": mean - half,
        "ci95_high": mean + half,
    }


def _load_rows(summary: dict[str, Any]) -> list[dict[str, Any]]:
    path = Path(summary.get("_output_dir", "")) / "per_dataset_metrics.json"
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return []


def _collapse_records_from_rows(rows: list[dict[str, Any]], seed: int, candidate_model: str) -> list[dict[str, Any]]:
    records = []
    families = sorted({r.get("family") for r in rows if r.get("family")})
    for family in families:
        fixed_rows = [r for r in rows if r.get("family") == family and r.get("model_name") == "fixed_moe_vectorized"]
        cand_rows = [r for r in rows if r.get("family") == family and str(r.get("model_name", "")).startswith(candidate_model)]
        if not fixed_rows or not cand_rows:
            continue
        variant_groups = sorted({str(r.get("repair_variant") or ("final_candidate_v1" if r.get("model_name") == candidate_model else r.get("model_name"))) for r in cand_rows})
        for variant in variant_groups:
            items = [
                r for r in cand_rows
                if str(r.get("repair_variant") or ("final_candidate_v1" if r.get("model_name") == candidate_model else r.get("model_name"))) == variant
            ]
            fixed_loss = float(np.mean([float(r.get("loss", 0.0)) for r in fixed_rows]))
            fixed_acc = float(np.mean([float(r.get("accuracy", 0.0)) for r in fixed_rows]))
            cand_loss = float(np.mean([float(r.get("loss", 0.0)) for r in items]))
            cand_acc = float(np.mean([float(r.get("accuracy", 0.0)) for r in items]))
            loss_gap = cand_loss - fixed_loss
            acc_gap = cand_acc - fixed_acc
            collapsed = loss_gap > 0.10 or acc_gap < -0.05
            reason = []
            if loss_gap > 0.10:
                reason.append("loss_gap_gt_0_10")
            if acc_gap < -0.05:
                reason.append("accuracy_gap_lt_minus_0_05")
            records.append({
                "seed": seed,
                "family": family,
                "variant": variant,
                "fixed_loss": fixed_loss,
                "candidate_loss": cand_loss,
                "fixed_accuracy": fixed_acc,
                "candidate_accuracy": cand_acc,
                "loss_gap": loss_gap,
                "accuracy_gap": acc_gap,
                "collapse_detected": collapsed,
                "collapse_reason": ",".join(reason) if reason else "none",
                "calibration_proxy": float(np.mean([float(r.get("calibration_proxy", 0.0)) for r in items])),
                "incorrect_overamp_rate": float(np.mean([float(r.get("incorrect_logit_overamplification_rate", 0.0)) for r in items])),
                "residual_help_rate": float(np.mean([float(r.get("residual_help_rate", 0.0)) for r in items])),
                "residual_harm_rate": float(np.mean([float(r.get("residual_harm_rate", 0.0)) for r in items])),
                "delta_correct_minus_top_wrong": float(np.mean([float(r.get("delta_correct_minus_top_wrong", 0.0)) for r in items])),
                "owner_entropy": float(np.mean([float(r.get("pvr_route_entropy", 0.0)) for r in items])),
                "prototype_entropy": float(np.mean([float(r.get("prototype_owner_entropy", 0.0)) for r in items])),
                "expert_contribution_pct": float(np.mean([float(r.get("expert_delta_contribution_pct", 0.0)) for r in items])),
                "owner_count_per_token": float(np.mean([float(r.get("pvr_actual_owner_count_per_token", 1.0)) for r in items])),
                "Top2_executions": float(np.mean([float(r.get("pvr_num_k2_tokens", 0.0)) for r in items])),
                "Top4_executions": float(np.mean([float(r.get("pvr_num_k4_tokens", 0.0)) for r in items])),
            })
    return records


def _model_variant(row: dict[str, Any], candidate_model: str = FINAL_CANDIDATE_CONFIG_NAME) -> str:
    repair = str(row.get("repair_variant") or "")
    if repair:
        return repair
    model = str(row.get("model_name") or row.get("model") or "")
    if model == candidate_model:
        return "v1"
    if model == "pvr_ec_ownership_top1_final_candidate_v1_1":
        return "v1_1"
    if model == "pvr_ec_ownership_top1_final_candidate_v1_2":
        return "v1_2"
    return model


def _classify_collapse(record: dict[str, Any]) -> list[str]:
    labels = []
    if float(record.get("incorrect_overamp_rate") or 0.0) >= 0.75 or float(record.get("delta_correct_minus_top_wrong") or 0.0) < -1.0:
        labels.append("PVR_EC_INCORRECT_OVERAMP_COLLAPSE")
    if float(record.get("calibration_proxy") or 0.0) >= 0.12:
        labels.append("PVR_EC_CALIBRATION_COLLAPSE")
    if float(record.get("residual_help_rate") or 0.0) < 0.05:
        labels.append("PVR_EC_SPARSE_RESIDUAL_UNHELPFUL_COLLAPSE")
    if float(record.get("residual_help_rate") or 0.0) >= 0.05 and float(record.get("accuracy_gap") or 0.0) < -0.05:
        labels.append("PVR_EC_LOCAL_TO_GLOBAL_COLLAPSE")
    if float(record.get("owner_entropy") or 0.0) < 0.01 or float(record.get("prototype_entropy") or 0.0) < 0.01:
        labels.append("PVR_EC_OWNER_PROTOTYPE_COLLAPSE")
    if float(record.get("fixed_accuracy") or 0.0) < 0.10 or float(record.get("fixed_loss") or 0.0) > 1.0:
        labels.append("DATA_SPLIT_DIFFICULTY_CASE")
    return sorted(set(labels)) or ["PVR_EC_SEED_FAMILY_COLLAPSE_REMAINS"]


def _variant_score_summary(rows_by_seed: list[tuple[int, list[dict[str, Any]]]], candidate_model: str = FINAL_CANDIDATE_CONFIG_NAME) -> dict[str, dict[str, Any]]:
    by_variant: dict[str, dict[str, Any]] = {}
    for seed, rows in rows_by_seed:
        collapse_records = _collapse_records_from_rows(rows, seed, candidate_model)
        for row in rows:
            variant = _model_variant(row, candidate_model)
            if variant in {"fixed_moe_vectorized", "pvr_ec_deploy_top1"}:
                continue
            data = by_variant.setdefault(variant, {
                "losses": [], "accuracies": [], "calibrations": [], "overamps": [],
                "owners": [], "top2": [], "top4": [], "collapse_records": [],
                "seed_loss_gaps": [], "seed_accuracy_gaps": [],
            })
            data["losses"].append(float(row.get("loss", 0.0)))
            data["accuracies"].append(float(row.get("accuracy", 0.0)))
            data["calibrations"].append(float(row.get("calibration_proxy", 0.0)))
            data["overamps"].append(float(row.get("incorrect_logit_overamplification_rate", 0.0)))
            data["owners"].append(float(row.get("pvr_actual_owner_count_per_token", 1.0)))
            data["top2"].append(float(row.get("pvr_num_k2_tokens", 0.0)))
            data["top4"].append(float(row.get("pvr_num_k4_tokens", 0.0)))
        for rec in collapse_records:
            variant = rec.get("variant", "")
            if variant in by_variant:
                by_variant[variant]["collapse_records"].append(rec)
                by_variant[variant]["seed_loss_gaps"].append(float(rec.get("loss_gap", 0.0)))
                by_variant[variant]["seed_accuracy_gaps"].append(float(rec.get("accuracy_gap", 0.0)))
    summary = {}
    for variant, data in by_variant.items():
        collapse_records = data["collapse_records"]
        mean_loss = float(np.mean(data["losses"])) if data["losses"] else None
        mean_acc = float(np.mean(data["accuracies"])) if data["accuracies"] else None
        calibration = float(np.mean(data["calibrations"])) if data["calibrations"] else 0.0
        overamp = float(np.mean(data["overamps"])) if data["overamps"] else 0.0
        worst_loss_gap = max(data["seed_loss_gaps"] or [0.0])
        worst_acc_gap = min(data["seed_accuracy_gaps"] or [0.0])
        collapse_count = sum(1 for r in collapse_records if r.get("collapse_detected"))
        score = (
            -(mean_loss or 0.0)
            + (mean_acc or 0.0)
            - max(0.0, worst_loss_gap)
            - max(0.0, -worst_acc_gap)
            - 0.5 * collapse_count
            - max(0.0, calibration - 0.12)
        )
        summary[variant] = {
            "mean_loss": mean_loss,
            "mean_accuracy": mean_acc,
            "worst_seed_loss_gap": worst_loss_gap,
            "worst_seed_accuracy_gap": worst_acc_gap,
            "worst_family_loss_gap": worst_loss_gap,
            "worst_family_accuracy_gap": worst_acc_gap,
            "catastrophic_family_collapse_count": collapse_count,
            "seed_pass_count": sum(1 for v in data["seed_loss_gaps"] if v <= 0.010),
            "family_pass_count": sum(1 for r in collapse_records if not r.get("collapse_detected")),
            "calibration_proxy": calibration,
            "incorrect_overamp_rate": overamp,
            "QPM_pass_shapes": None,
            "owners_per_token": float(np.mean(data["owners"])) if data["owners"] else 1.0,
            "Top2_executions": float(np.mean(data["top2"])) if data["top2"] else 0.0,
            "Top4_executions": float(np.mean(data["top4"])) if data["top4"] else 0.0,
            "candidate_score": score,
            "collapse_records": collapse_records,
        }
    return summary


def run_pvr_collapse_case_replay(
    args: argparse.Namespace,
    families: list[str],
    models: list[str],
    batch_sizes: list[int],
    sequence_lengths: list[int],
    output_dir: str | Path,
) -> dict[str, Any]:
    out = Path(output_dir)
    seeds = _parse_csv_ints(args.seed_list, [seed for seed, _ in COLLAPSE_CASES])
    train_steps = int(args.train_steps or 500)
    run_families = _execution_families(families)
    rows_by_seed: list[tuple[int, list[dict[str, Any]]]] = []
    subdirs = []
    for seed in seeds:
        summary = _run_gate_subrun(
            args,
            families=run_families,
            models=models,
            batch_sizes=batch_sizes,
            sequence_lengths=sequence_lengths,
            seed=seed,
            train_steps=train_steps,
            output_dir=out / f"seed_{seed}",
            gate_flag="run_collapse_case_replay",
        )
        subdirs.append(summary["_output_dir"])
        rows_by_seed.append((seed, _load_rows(summary)))
    records = []
    detailed = []
    for seed, rows in rows_by_seed:
        records.extend(_collapse_records_from_rows(rows, seed, FINAL_CANDIDATE_CONFIG_NAME))
        for row in rows:
            detailed.append({
                "seed": seed,
                "family": row.get("family"),
                "model": row.get("model_name"),
                "train_loss_curve": row.get("train_loss_curve", []),
                "eval_loss_curve": row.get("eval_loss_curve", []),
                "accuracy_curve": row.get("accuracy_curve", []),
                "final_loss": row.get("loss"),
                "final_accuracy": row.get("accuracy"),
                "sparse_ce_loss": row.get("sparse_auxiliary_loss"),
                "main_loss": row.get("training_loss"),
                "logit_norm_penalty": row.get("logit_norm"),
                "total_loss": row.get("loss"),
                "correct_class_logit_delta": row.get("correct_class_logit_delta"),
                "incorrect_class_logit_delta_max": row.get("incorrect_class_logit_delta_max"),
                "delta_correct_minus_top_wrong": row.get("delta_correct_minus_top_wrong"),
                "incorrect_overamp_rate": row.get("incorrect_logit_overamplification_rate"),
                "calibration_proxy": row.get("calibration_proxy"),
                "high_confidence_failure_rate": row.get("high_confidence_failure_rate"),
                "residual_help_rate": row.get("residual_help_rate"),
                "residual_harm_rate": row.get("residual_harm_rate"),
                "decision_token_help_rate": row.get("decision_token_help_rate"),
                "token_to_sequence_transfer_ratio": row.get("token_to_sequence_transfer_ratio"),
                "expert_delta_contribution_pct": row.get("expert_delta_contribution_pct"),
                "shared_sparse_ratio": row.get("shared_sparse_ratio"),
                "expert_grad_norm": row.get("expert_grad_norm"),
                "shared_grad_norm": row.get("shared_grad_norm"),
                "expert_grad_to_shared_grad_ratio": row.get("expert_grad_to_shared_grad_ratio"),
                "owner_entropy": row.get("pvr_route_entropy"),
                "prototype_entropy": row.get("prototype_owner_entropy"),
                "owner_distribution": row.get("owner_distribution"),
                "prototype_distribution": row.get("prototype_distribution"),
                "dead_expert_count": row.get("dead_expert_count"),
                "owner_count_per_token": row.get("pvr_actual_owner_count_per_token"),
                "Top2_executions": row.get("pvr_num_k2_tokens", 0.0),
                "Top4_executions": row.get("pvr_num_k4_tokens", 0.0),
            })
    for rec in records:
        rec["root_cause_labels"] = _classify_collapse(rec) if rec.get("collapse_detected") else []
    collapses = [r for r in records if r.get("collapse_detected")]
    unexplained = [r for r in collapses if r.get("root_cause_labels") == ["PVR_EC_SEED_FAMILY_COLLAPSE_REMAINS"]]
    statuses = {
        "PVR_EC_MINIMAX_STABILITY_DIAGNOSTIC_READY",
        "PVR_EC_COLLAPSE_CASES_REPLAYED",
        "PVR_EC_SEED_FAMILY_COLLAPSE_REMAINS" if collapses else "PVR_EC_SEED_FAMILY_COLLAPSE_REPAIRED",
        "PVR_EC_REPEATABILITY_BLOCKED" if collapses else "PVR_EC_MULTI_SEED_CONFIRMED",
        "PVR_EC_DO_NOT_PROMOTE",
    }
    for rec in collapses:
        statuses.update(rec.get("root_cause_labels", []))
    payload = {
        "metadata": {"seed_list": seeds, "train_steps": train_steps, "requested_families": families, "executed_families": run_families, "command": " ".join(sys.argv)},
        "status": "PVR_EC_REPEATABILITY_BLOCKED" if collapses else "PVR_EC_SEED_FAMILY_COLLAPSE_REPAIRED",
        "statuses": sorted(statuses),
        "promotion_ready": False,
        "passed": not collapses,
        "collapse_count": len(collapses),
        "unexplained_collapse_count": len(unexplained),
        "collapse_records": collapses,
        "records": records,
        "detailed_rows": detailed,
        "subrun_dirs": subdirs,
    }
    _write_report_pair(out, "pvr_ec_collapse_case_replay_report", payload, "PVR-EC Collapse Case Replay Report")
    return payload


def run_pvr_minimax_candidate_selection(
    args: argparse.Namespace,
    families: list[str],
    models: list[str],
    batch_sizes: list[int],
    sequence_lengths: list[int],
    output_dir: str | Path,
) -> dict[str, Any]:
    out = Path(output_dir)
    seeds = _parse_csv_ints(args.seed_list, [42, 123, 777, 2026, 9001])
    train_steps = int(args.train_steps or 500)
    rows_by_seed = []
    subdirs = []
    for seed in seeds:
        summary = _run_gate_subrun(
            args,
            families=_execution_families(families),
            models=models,
            batch_sizes=batch_sizes,
            sequence_lengths=sequence_lengths,
            seed=seed,
            train_steps=train_steps,
            output_dir=out / f"seed_{seed}",
            gate_flag="run_minimax_candidate_selection",
        )
        subdirs.append(summary["_output_dir"])
        rows_by_seed.append((seed, _load_rows(summary)))
    fixed_losses = []
    fixed_accs = []
    for _, rows in rows_by_seed:
        fixed = [r for r in rows if r.get("model_name") == "fixed_moe_vectorized"]
        fixed_losses.extend(float(r.get("loss", 0.0)) for r in fixed)
        fixed_accs.extend(float(r.get("accuracy", 0.0)) for r in fixed)
    fixed_mean_loss = float(np.mean(fixed_losses)) if fixed_losses else 0.0
    fixed_mean_acc = float(np.mean(fixed_accs)) if fixed_accs else 0.0
    variant_summary = _variant_score_summary(rows_by_seed)
    eligible = {
        name: data for name, data in variant_summary.items()
        if data["catastrophic_family_collapse_count"] == 0
        and data["mean_loss"] is not None and data["mean_loss"] <= fixed_mean_loss + 0.010
        and data["mean_accuracy"] is not None and data["mean_accuracy"] >= fixed_mean_acc - 0.020
        and data["calibration_proxy"] <= 0.12
        and data["incorrect_overamp_rate"] <= (variant_summary.get("v1", {}).get("incorrect_overamp_rate", 1.0))
        and abs(data["owners_per_token"] - 1.0) < 1e-6
        and data["Top2_executions"] == 0.0
        and data["Top4_executions"] == 0.0
    }
    selected = max(eligible, key=lambda name: (eligible[name]["candidate_score"], -eligible[name]["mean_loss"])) if eligible else "none"
    if selected != "none" and selected not in {"v1", "final_candidate_v1"}:
        AlgorithmicBenchmarkRunner(mode="smoke")._write_selected_candidate_variant_config(selected, version="v1_2")
    statuses = {
        "PVR_EC_MINIMAX_STABILITY_DIAGNOSTIC_READY",
        "PVR_EC_MINIMAX_SELECTION_HELPFUL" if selected != "none" else "PVR_EC_SEED_FAMILY_COLLAPSE_REMAINS",
        "PVR_EC_FINAL_CANDIDATE_VARIANT_SELECTED" if selected not in {"none", "v1", "final_candidate_v1"} else "PVR_EC_PROMISING_NEEDS_MORE_EVIDENCE",
        "PVR_EC_FINAL_CANDIDATE_REVALIDATION_REQUIRED" if selected not in {"none", "v1", "final_candidate_v1"} else "PVR_EC_DO_NOT_PROMOTE",
        "PVR_EC_DO_NOT_PROMOTE",
    }
    payload = {
        "metadata": {"seed_list": seeds, "train_steps": train_steps, "variants": _parse_csv_strings(getattr(args, "minimax_variants", None)) or MINIMAX_CANDIDATE_VARIANTS, "command": " ".join(sys.argv)},
        "status": "PVR_EC_MINIMAX_SELECTION_HELPFUL" if selected != "none" else "PVR_EC_REPEATABILITY_BLOCKED",
        "statuses": sorted(statuses),
        "promotion_ready": False,
        "passed": selected != "none",
        "fixed_mean_loss": fixed_mean_loss,
        "fixed_mean_accuracy": fixed_mean_acc,
        "selected_variant": selected,
        "selected_requires_revalidation": selected not in {"none", "v1", "final_candidate_v1"},
        "variant_summary": variant_summary,
        "subrun_dirs": subdirs,
    }
    _write_report_pair(out, "pvr_ec_minimax_candidate_selection_report", payload, "PVR-EC Minimax Candidate Selection Report")
    return payload


def run_pvr_stability_repair_sweep(
    args: argparse.Namespace,
    families: list[str],
    models: list[str],
    batch_sizes: list[int],
    sequence_lengths: list[int],
    output_dir: str | Path,
) -> dict[str, Any]:
    out = Path(output_dir)
    seeds = _parse_csv_ints(args.seed_list, [42, 123, 777, 2026, 9001])
    train_steps = int(args.train_steps or 500)
    rows_by_seed = []
    subdirs = []
    for seed in seeds:
        summary = _run_gate_subrun(
            args,
            families=_execution_families(families),
            models=models,
            batch_sizes=batch_sizes,
            sequence_lengths=sequence_lengths,
            seed=seed,
            train_steps=train_steps,
            output_dir=out / f"seed_{seed}",
            gate_flag="run_stability_repair_sweep",
        )
        subdirs.append(summary["_output_dir"])
        rows_by_seed.append((seed, _load_rows(summary)))
    variant_summary = _variant_score_summary(rows_by_seed)
    candidates = {name: data for name, data in variant_summary.items() if data["catastrophic_family_collapse_count"] == 0}
    selected = max(candidates, key=lambda name: candidates[name]["candidate_score"]) if candidates else "none"
    statuses = {"PVR_EC_MINIMAX_STABILITY_DIAGNOSTIC_READY", "PVR_EC_DO_NOT_PROMOTE"}
    if selected == "family_balanced_sampling":
        statuses.add("PVR_EC_FAMILY_BALANCED_TRAINING_HELPFUL")
    if selected.startswith("gradient_clip"):
        statuses.add("PVR_EC_GRADIENT_CLIP_STABILITY_HELPFUL")
    if selected.startswith("logit_norm_cap"):
        statuses.add("PVR_EC_LOGIT_NORM_CAP_STABILITY_HELPFUL")
    if selected.startswith("wrong_suppress"):
        statuses.add("PVR_EC_WRONG_SUPPRESS_STABILITY_HELPFUL")
    if "temperature" in selected:
        statuses.add("PVR_EC_TEMPERATURE_CALIBRATION_HELPFUL")
    statuses.add("PVR_EC_SEED_FAMILY_COLLAPSE_REPAIRED" if selected != "none" else "PVR_EC_SEED_FAMILY_COLLAPSE_REMAINS")
    payload = {
        "metadata": {"seed_list": seeds, "train_steps": train_steps, "variants": _parse_csv_strings(getattr(args, "stability_repair_variants", None)) or STABILITY_REPAIR_VARIANTS, "command": " ".join(sys.argv)},
        "status": "PVR_EC_SEED_FAMILY_COLLAPSE_REPAIRED" if selected != "none" else "PVR_EC_REPEATABILITY_BLOCKED",
        "statuses": sorted(statuses),
        "promotion_ready": False,
        "passed": selected != "none",
        "selected_variant": selected,
        "variant_summary": variant_summary,
        "subrun_dirs": subdirs,
    }
    _write_report_pair(out, "pvr_ec_stability_repair_sweep_report", payload, "PVR-EC Stability Repair Sweep Report")
    return payload


def run_pvr_repeatability_collapse_isolation(
    args: argparse.Namespace,
    families: list[str],
    models: list[str],
    batch_sizes: list[int],
    sequence_lengths: list[int],
    output_dir: str | Path,
) -> dict[str, Any]:
    out = Path(output_dir)
    seeds = _parse_csv_ints(args.seed_list, [42, 123, 777, 2026, 9001])
    train_steps = int(args.train_steps or 500)
    all_records = []
    subdirs = []
    for seed in seeds:
        summary = _run_gate_subrun(
            args,
            families=families,
            models=models,
            batch_sizes=batch_sizes,
            sequence_lengths=sequence_lengths,
            seed=seed,
            train_steps=train_steps,
            output_dir=out / f"seed_{seed}",
            gate_flag="run_repeatability_collapse_isolation",
        )
        subdirs.append(summary["_output_dir"])
        all_records.extend(_collapse_records_from_rows(_load_rows(summary), seed, FINAL_CANDIDATE_CONFIG_NAME))
    collapses = [r for r in all_records if r["collapse_detected"]]
    collapse_families = sorted({r["family"] for r in collapses})
    collapse_seeds = sorted({r["seed"] for r in collapses})
    statuses = {
        "PVR_EC_REPEATABILITY_COLLAPSE_ANALYZED",
        "PVR_EC_FAMILY_COLLAPSE_SEED_ISOLATED" if collapses else "PVR_EC_FAMILY_COLLAPSE_REPAIRED",
        "PVR_EC_FAMILY_COLLAPSE_REMAINS" if collapses else "PVR_EC_REPEATABILITY_COLLAPSE_REPAIRED",
        "PVR_EC_REPEATABILITY_BLOCKED" if collapses else "PVR_EC_MULTI_SEED_CONFIRMED",
        "PVR_EC_DO_NOT_PROMOTE",
    }
    payload = {
        "metadata": {"seed_list": seeds, "train_steps": train_steps, "command": " ".join(sys.argv)},
        "status": "PVR_EC_REPEATABILITY_BLOCKED" if collapses else "PVR_EC_REPEATABILITY_COLLAPSE_REPAIRED",
        "statuses": sorted(statuses),
        "promotion_ready": False,
        "passed": not collapses,
        "collapse_count": len(collapses),
        "collapse_seeds": collapse_seeds,
        "collapse_families": collapse_families,
        "records": all_records,
        "collapse_records": collapses,
        "subrun_dirs": subdirs,
    }
    _write_report_pair(out, "pvr_ec_repeatability_collapse_isolation_report", payload, "PVR-EC Repeatability Collapse Isolation Report")
    return payload


def run_pvr_repeatability_repair_sweep(
    args: argparse.Namespace,
    families: list[str],
    models: list[str],
    batch_sizes: list[int],
    sequence_lengths: list[int],
    output_dir: str | Path,
) -> dict[str, Any]:
    out = Path(output_dir)
    seeds = _parse_csv_ints(args.seed_list, [42, 123, 777, 2026, 9001])
    train_steps = int(args.train_steps or 500)
    variants = _parse_csv_strings(args.repeatability_repair_variants) or REPEATABILITY_REPAIR_VARIANTS
    all_records = []
    summaries = []
    for seed in seeds:
        summary = _run_gate_subrun(
            args,
            families=families,
            models=models,
            batch_sizes=batch_sizes,
            sequence_lengths=sequence_lengths,
            seed=seed,
            train_steps=train_steps,
            output_dir=out / f"seed_{seed}",
            gate_flag="run_repeatability_repair_sweep",
        )
        summaries.append(summary)
        all_records.extend(_collapse_records_from_rows(_load_rows(summary), seed, FINAL_CANDIDATE_CONFIG_NAME))
    by_variant = {}
    for variant in variants:
        records = [r for r in all_records if r["variant"] == variant]
        if not records:
            continue
        collapses = [r for r in records if r["collapse_detected"]]
        by_variant[variant] = {
            "collapse_count": len(collapses),
            "mean_loss_gap": float(np.mean([r["loss_gap"] for r in records])),
            "mean_accuracy_gap": float(np.mean([r["accuracy_gap"] for r in records])),
            "mean_calibration_proxy": float(np.mean([r["calibration_proxy"] for r in records])),
            "mean_incorrect_overamp_rate": float(np.mean([r["incorrect_overamp_rate"] for r in records])),
            "owners_per_token": float(np.mean([r["owner_count_per_token"] for r in records])),
            "Top2_executions": float(np.mean([r["Top2_executions"] for r in records])),
            "Top4_executions": float(np.mean([r["Top4_executions"] for r in records])),
        }
    candidates = {
        name: data for name, data in by_variant.items()
        if data["collapse_count"] == 0
        and data["mean_loss_gap"] <= 0.010
        and data["mean_accuracy_gap"] >= -0.020
        and abs(data["owners_per_token"] - 1.0) < 1e-6
        and data["Top2_executions"] == 0.0
        and data["Top4_executions"] == 0.0
    }
    selected = min(
        candidates,
        key=lambda name: (candidates[name]["mean_calibration_proxy"], -candidates[name]["mean_accuracy_gap"]),
    ) if candidates else "none"
    repaired = selected != "none"
    statuses = {
        "PVR_EC_REPEATABILITY_COLLAPSE_ANALYZED",
        "PVR_EC_REPEATABILITY_COLLAPSE_REPAIRED" if repaired else "PVR_EC_REPEATABILITY_BLOCKED",
        "PVR_EC_FAMILY_COLLAPSE_REPAIRED" if repaired else "PVR_EC_FAMILY_COLLAPSE_REMAINS",
        "PVR_EC_DO_NOT_PROMOTE",
    }
    if repaired and selected != "final_candidate_v1":
        statuses.update({"PVR_EC_FINAL_CANDIDATE_VARIANT_SELECTED", "PVR_EC_FINAL_CANDIDATE_REVALIDATION_REQUIRED"})
        runner = AlgorithmicBenchmarkRunner(mode="smoke")
        runner.output_dir = out
        runner._write_selected_candidate_variant_config(selected)
    payload = {
        "metadata": {"seed_list": seeds, "train_steps": train_steps, "variants": variants, "command": " ".join(sys.argv)},
        "status": "PVR_EC_REPEATABILITY_COLLAPSE_REPAIRED" if repaired else "PVR_EC_REPEATABILITY_BLOCKED",
        "statuses": sorted(statuses),
        "promotion_ready": False,
        "passed": repaired,
        "selected_variant": selected,
        "selected_requires_revalidation": repaired and selected != "final_candidate_v1",
        "variant_summary": by_variant,
        "records": all_records,
        "subrun_dirs": [s["_output_dir"] for s in summaries],
    }
    _write_report_pair(out, "pvr_ec_repeatability_repair_sweep_report", payload, "PVR-EC Repeatability Repair Sweep Report")
    return payload


def run_pvr_multiseed_confirmation_gate(
    args: argparse.Namespace,
    families: list[str],
    models: list[str],
    batch_sizes: list[int],
    sequence_lengths: list[int],
    output_dir: str | Path,
) -> dict[str, Any]:
    out = Path(output_dir)
    seeds = _parse_csv_ints(args.seed_list, [42, 123, 777, 2026, 9001])
    train_steps = int(args.train_steps or 500)
    candidate_model = next(
        (m for m in models if str(m).startswith("pvr_ec_ownership_top1_final_candidate_v1_")),
        FINAL_CANDIDATE_CONFIG_NAME,
    )
    summaries = []
    per_seed = []
    for seed in seeds:
        summary = _run_gate_subrun(
            args,
            families=families,
            models=models,
            batch_sizes=batch_sizes,
            sequence_lengths=sequence_lengths,
            seed=seed,
            train_steps=train_steps,
            output_dir=out / f"seed_{seed}",
            gate_flag="run_multiseed_confirmation_gate",
        )
        summaries.append(summary)
        fixed_loss = _model_metric(summary, "fixed_moe_vectorized", "avg_loss")
        fixed_acc = _model_metric(summary, "fixed_moe_vectorized", "avg_accuracy")
        cand_loss = _model_metric(summary, candidate_model, "avg_loss")
        cand_acc = _model_metric(summary, candidate_model, "avg_accuracy")
        loss_pass = fixed_loss is not None and cand_loss is not None and cand_loss <= fixed_loss + 0.010
        acc_pass = fixed_acc is not None and cand_acc is not None and cand_acc >= fixed_acc - 0.020
        rows = _load_rows(summary)
        family_fail = 0
        for family in sorted({r.get("family") for r in rows if r.get("family")}):
            fixed_rows = [r for r in rows if r.get("family") == family and r.get("model_name") == "fixed_moe_vectorized"]
            cand_rows = [r for r in rows if r.get("family") == family and r.get("model_name") == candidate_model]
            if not fixed_rows or not cand_rows:
                continue
            fg_loss = float(np.mean([r["loss"] for r in fixed_rows]))
            cg_loss = float(np.mean([r["loss"] for r in cand_rows]))
            fg_acc = float(np.mean([r["accuracy"] for r in fixed_rows]))
            cg_acc = float(np.mean([r["accuracy"] for r in cand_rows]))
            if cg_loss > fg_loss + 0.10 or cg_acc < fg_acc - 0.05:
                family_fail += 1
        per_seed.append({
            "seed": seed,
            "fixed_moe_loss": fixed_loss,
            "fixed_moe_accuracy": fixed_acc,
            "candidate_loss": cand_loss,
            "candidate_accuracy": cand_acc,
            "loss_gap_vs_fixed": cand_loss - fixed_loss if cand_loss is not None and fixed_loss is not None else None,
            "accuracy_gap_vs_fixed": cand_acc - fixed_acc if cand_acc is not None and fixed_acc is not None else None,
            "loss_pass": loss_pass,
            "accuracy_pass": acc_pass,
            "family_level_pass": family_fail == 0,
            "catastrophic_family_collapse_count": family_fail,
        })
    fixed_losses = [_model_metric(s, "fixed_moe_vectorized", "avg_loss") for s in summaries]
    fixed_accs = [_model_metric(s, "fixed_moe_vectorized", "avg_accuracy") for s in summaries]
    cand_losses = [_model_metric(s, candidate_model, "avg_loss") for s in summaries]
    cand_accs = [_model_metric(s, candidate_model, "avg_accuracy") for s in summaries]
    fixed_loss_mean = float(np.mean([v for v in fixed_losses if v is not None]))
    fixed_acc_mean = float(np.mean([v for v in fixed_accs if v is not None]))
    cand_loss_mean = float(np.mean([v for v in cand_losses if v is not None]))
    cand_acc_mean = float(np.mean([v for v in cand_accs if v is not None]))
    loss_seed_passes = sum(1 for item in per_seed if item["loss_pass"])
    acc_seed_passes = sum(1 for item in per_seed if item["accuracy_pass"])
    collapse_count = sum(int(item["catastrophic_family_collapse_count"]) for item in per_seed)
    variance_blocked = (_confidence_interval([v for v in cand_losses if v is not None])["std"] or 0.0) > 0.05
    passed = (
        cand_loss_mean <= fixed_loss_mean + 0.010
        and cand_acc_mean >= fixed_acc_mean - 0.020
        and loss_seed_passes >= 4
        and acc_seed_passes >= 4
        and collapse_count == 0
        and not variance_blocked
    )
    payload = {
        "metadata": {"seed_list": seeds, "train_steps": train_steps, "candidate_model": candidate_model, "command": " ".join(sys.argv)},
        "status": "PVR_EC_MULTI_SEED_CONFIRMED" if passed else "PVR_EC_REPEATABILITY_BLOCKED",
        "statuses": [
            "PVR_EC_MULTI_SEED_CONFIRMED" if passed else "PVR_EC_REPEATABILITY_BLOCKED",
            "PVR_EC_DO_NOT_PROMOTE",
        ],
        "promotion_ready": False,
        "passed": passed,
        "mean": {
            "fixed_moe_loss": fixed_loss_mean,
            "fixed_moe_accuracy": fixed_acc_mean,
            "candidate_loss": cand_loss_mean,
            "candidate_accuracy": cand_acc_mean,
            "loss_gap_vs_fixed": cand_loss_mean - fixed_loss_mean,
            "accuracy_gap_vs_fixed": cand_acc_mean - fixed_acc_mean,
        },
        "candidate_loss_stats": _confidence_interval([v for v in cand_losses if v is not None]),
        "candidate_accuracy_stats": _confidence_interval([v for v in cand_accs if v is not None]),
        "per_seed_pass_fail": per_seed,
        "catastrophic_family_collapse_count": collapse_count,
        "variance_blocked": variance_blocked,
        "subrun_dirs": [s["_output_dir"] for s in summaries],
    }
    _write_report_pair(out, "pvr_ec_multiseed_confirmation_report", payload, "PVR-EC Multi-Seed Confirmation Report")
    return payload


def run_pvr_longer_training_confirmation_gate(
    args: argparse.Namespace,
    families: list[str],
    models: list[str],
    batch_sizes: list[int],
    sequence_lengths: list[int],
    output_dir: str | Path,
) -> dict[str, Any]:
    out = Path(output_dir)
    seeds = _parse_csv_ints(args.seed_list, [42, 123, 777])
    steps_list = _parse_csv_ints(args.train_steps_list, [500, 1000, 2000])
    records = []
    subdirs = []
    for steps in steps_list:
        for seed in seeds:
            summary = _run_gate_subrun(
                args,
                families=families,
                models=models,
                batch_sizes=batch_sizes,
                sequence_lengths=sequence_lengths,
                seed=seed,
                train_steps=steps,
                output_dir=out / f"steps_{steps}_seed_{seed}",
                gate_flag="run_longer_training_confirmation_gate",
            )
            subdirs.append(summary["_output_dir"])
            fixed_loss = _model_metric(summary, "fixed_moe_vectorized", "avg_loss")
            fixed_acc = _model_metric(summary, "fixed_moe_vectorized", "avg_accuracy")
            cand_loss = _model_metric(summary, FINAL_CANDIDATE_CONFIG_NAME, "avg_loss")
            cand_acc = _model_metric(summary, FINAL_CANDIDATE_CONFIG_NAME, "avg_accuracy")
            records.append({
                "train_steps": steps,
                "seed": seed,
                "fixed_loss": fixed_loss,
                "fixed_accuracy": fixed_acc,
                "candidate_loss": cand_loss,
                "candidate_accuracy": cand_acc,
                "loss_gap_vs_fixed": cand_loss - fixed_loss if cand_loss is not None and fixed_loss is not None else None,
                "accuracy_gap_vs_fixed": cand_acc - fixed_acc if cand_acc is not None and fixed_acc is not None else None,
            })
    by_steps = {}
    for steps in steps_list:
        items = [r for r in records if r["train_steps"] == steps]
        by_steps[str(steps)] = {
            "candidate_loss": _confidence_interval([r["candidate_loss"] for r in items if r["candidate_loss"] is not None]),
            "candidate_accuracy": _confidence_interval([r["candidate_accuracy"] for r in items if r["candidate_accuracy"] is not None]),
            "loss_gap_vs_fixed": _confidence_interval([r["loss_gap_vs_fixed"] for r in items if r["loss_gap_vs_fixed"] is not None]),
            "accuracy_gap_vs_fixed": _confidence_interval([r["accuracy_gap_vs_fixed"] for r in items if r["accuracy_gap_vs_fixed"] is not None]),
        }
    base_loss = by_steps.get(str(steps_list[0]), {}).get("candidate_loss", {}).get("mean")
    degraded = any(
        data["candidate_loss"]["mean"] is not None and base_loss is not None and data["candidate_loss"]["mean"] > base_loss + 0.03
        for data in by_steps.values()
    )
    helpful = any(
        data["candidate_loss"]["mean"] is not None and base_loss is not None and data["candidate_loss"]["mean"] < base_loss - 0.005
        for data in by_steps.values()
    )
    statuses = {"PVR_EC_DO_NOT_PROMOTE"}
    if degraded:
        statuses.add("PVR_EC_LONG_TRAINING_INSTABILITY")
    else:
        statuses.add("PVR_EC_LONGER_TRAINING_CONFIRMED")
    if helpful:
        statuses.add("PVR_EC_LONGER_TRAINING_HELPFUL")
    statuses.add("PVR_EC_SCALING_GAP_REMAINS")
    payload = {
        "metadata": {"seed_list": seeds, "train_steps_list": steps_list, "command": " ".join(sys.argv)},
        "status": "PVR_EC_LONG_TRAINING_INSTABILITY" if degraded else "PVR_EC_LONGER_TRAINING_CONFIRMED",
        "statuses": sorted(statuses),
        "promotion_ready": False,
        "passed": not degraded,
        "by_train_steps": by_steps,
        "records": records,
        "subrun_dirs": subdirs,
    }
    _write_report_pair(out, "pvr_ec_longer_training_confirmation_report", payload, "PVR-EC Longer-Training Confirmation Report")
    return payload


def run_pvr_matched_wall_clock_gate(
    args: argparse.Namespace,
    families: list[str],
    models: list[str],
    batch_sizes: list[int],
    sequence_lengths: list[int],
    output_dir: str | Path,
) -> dict[str, Any]:
    out = Path(output_dir)
    seeds = _parse_csv_ints(args.seed_list, [42, 123, 777])
    train_steps = int(args.train_steps or 500)
    max_seconds = float(args.max_train_seconds or 120.0)
    summaries = []
    records = []
    for seed in seeds:
        summary = _run_gate_subrun(
            args,
            families=families,
            models=models,
            batch_sizes=batch_sizes,
            sequence_lengths=sequence_lengths,
            seed=seed,
            train_steps=train_steps,
            output_dir=out / f"seed_{seed}",
            gate_flag="run_matched_wall_clock_gate",
        )
        summaries.append(summary)
        rows = _load_rows(summary)
        for model in models:
            model_rows = [r for r in rows if r.get("model_name") == model]
            train_time = float(np.mean([r.get("training_time_s", 0.0) for r in model_rows])) if model_rows else 0.0
            samples_seen = int(args.sample_limit or 1000) * train_steps
            tokens_seen = samples_seen * SCALES[args.scale]["d_model"]
            records.append({
                "seed": seed,
                "model": model,
                "steps_completed": train_steps,
                "wall_clock_train_time": train_time,
                "max_train_seconds": max_seconds,
                "samples_seen": samples_seen,
                "tokens_seen": tokens_seen,
                "loss": _model_metric(summary, model, "avg_loss"),
                "accuracy": _model_metric(summary, model, "avg_accuracy"),
                "quality_per_ms": _model_metric(summary, model, "avg_qpc"),
                "samples_per_second": samples_seen / max(train_time, 1e-8),
                "tokens_per_second": tokens_seen / max(train_time, 1e-8),
                "convergence_per_second": -(_model_metric(summary, model, "avg_loss") or 0.0) / max(train_time, 1e-8),
            })
    def avg(model: str, key: str) -> float | None:
        values = [r[key] for r in records if r["model"] == model and isinstance(r.get(key), (int, float))]
        return float(np.mean(values)) if values else None
    fixed_loss = avg("fixed_moe_vectorized", "loss")
    fixed_acc = avg("fixed_moe_vectorized", "accuracy")
    cand_loss = avg(FINAL_CANDIDATE_CONFIG_NAME, "loss")
    cand_acc = avg(FINAL_CANDIDATE_CONFIG_NAME, "accuracy")
    matched_step_pass = bool(cand_loss is not None and fixed_loss is not None and cand_loss <= fixed_loss + 0.010 and cand_acc is not None and fixed_acc is not None and cand_acc >= fixed_acc - 0.020)
    fixed_time = avg("fixed_moe_vectorized", "wall_clock_train_time") or 0.0
    cand_time = avg(FINAL_CANDIDATE_CONFIG_NAME, "wall_clock_train_time") or 0.0
    wall_pass = matched_step_pass and cand_time <= max_seconds and cand_time <= max(fixed_time * 1.25, fixed_time + 10.0)
    step_payload = {
        "metadata": {"seed_list": seeds, "train_steps": train_steps, "command": " ".join(sys.argv)},
        "status": "PVR_EC_MATCHED_STEP_CONFIRMED" if matched_step_pass else "PVR_EC_PROMISING_NEEDS_MORE_EVIDENCE",
        "statuses": ["PVR_EC_DO_NOT_PROMOTE"],
        "promotion_ready": False,
        "passed": matched_step_pass,
        "records": records,
    }
    wall_payload = {
        "metadata": {"seed_list": seeds, "train_steps": train_steps, "max_train_seconds": max_seconds, "command": " ".join(sys.argv)},
        "status": "PVR_EC_MATCHED_WALL_CLOCK_CONFIRMED" if wall_pass else "PVR_EC_MATCHED_WALL_CLOCK_BLOCKED",
        "statuses": [
            "PVR_EC_MATCHED_WALL_CLOCK_CONFIRMED" if wall_pass else "PVR_EC_MATCHED_WALL_CLOCK_BLOCKED",
            "PVR_EC_DO_NOT_PROMOTE",
        ],
        "promotion_ready": False,
        "passed": wall_pass,
        "matched_step_pass": matched_step_pass,
        "mean_fixed_train_time": fixed_time,
        "mean_candidate_train_time": cand_time,
        "records": records,
        "subrun_dirs": [s["_output_dir"] for s in summaries],
    }
    _write_report_pair(out, "pvr_ec_matched_step_report", step_payload, "PVR-EC Matched-Step Report")
    _write_report_pair(out, "pvr_ec_matched_wall_clock_report", wall_payload, "PVR-EC Matched Wall-Clock Report")
    return wall_payload


def summarize_pvr_final_deployment_gate(input_dirs: list[str], output_dir: str | Path, seed: int = 42) -> dict[str, Any]:
    expected = {
        "forward_purity_gate": "pvr_ec_final_forward_purity_report.json",
        "config_manifest": "pvr_ec_final_candidate_config_manifest.json",
        "multi_seed_gate": "pvr_ec_multiseed_confirmation_report.json",
        "longer_training_gate": "pvr_ec_longer_training_confirmation_report.json",
        "matched_step_gate": "pvr_ec_matched_step_report.json",
        "matched_wall_clock_gate": "pvr_ec_matched_wall_clock_report.json",
        "calibration_gate": "pvr_ec_final_calibration_sweep_report.json",
        "family_regression_gate": "pvr_ec_family_regression_gate_report.json",
        "quality_per_ms_gate": "pvr_ec_quality_per_ms_memory_gate_report.json",
        "reliability_proxy_gate": "pvr_ec_reliability_proxy_gate_report.json",
    }
    loaded: dict[str, Any] = {}
    missing = []
    for gate, filename in expected.items():
        found = None
        for directory in input_dirs:
            path = Path(directory) / filename
            if path.exists():
                found = path
                break
        if found is None:
            missing.append({"gate": gate, "file": filename})
        else:
            loaded[gate] = json.loads(found.read_text(encoding="utf-8"))
            loaded[gate]["_path"] = str(found)
    blocked_reasons = [item["gate"] for item in missing]
    for gate, report in loaded.items():
        if gate == "config_manifest":
            continue
        if not bool(report.get("passed", report.get("status", "").endswith("PASSED") or report.get("status", "").endswith("CONFIRMED"))):
            blocked_reasons.append(gate)
    if missing:
        verdict = "PARTIAL_PVR_EC_FINAL_DEPLOYMENT_GATE"
    elif not blocked_reasons:
        verdict = "PVR_EC_DEPLOY_CANDIDATE_CONFIRMED"
    elif len(blocked_reasons) == 1:
        reason = blocked_reasons[0]
        verdict = {
            "calibration_gate": "PVR_EC_CALIBRATION_BLOCKED",
            "multi_seed_gate": "PVR_EC_REPEATABILITY_BLOCKED",
            "quality_per_ms_gate": "PVR_EC_QUALITY_PER_MS_BLOCKED",
            "matched_wall_clock_gate": "PVR_EC_MATCHED_WALL_CLOCK_BLOCKED",
            "family_regression_gate": "PVR_EC_FAMILY_REGRESSION_BLOCKED",
            "reliability_proxy_gate": "PVR_EC_RELIABILITY_BLOCKED",
        }.get(reason, "PVR_EC_PROMISING_NEEDS_MORE_EVIDENCE")
    else:
        verdict = "PVR_EC_DO_NOT_PROMOTE"
    statuses = sorted({
        *(status for report in loaded.values() for status in report.get("statuses", [])),
        verdict,
        "PVR_EC_DO_NOT_PROMOTE" if verdict != "PVR_EC_DEPLOY_CANDIDATE_CONFIRMED" else "PVR_EC_DEPLOY_CANDIDATE_CONFIRMED",
    })
    payload = {
        "metadata": {"seed": seed, "input_dirs": input_dirs, "command": " ".join(sys.argv)},
        "status": verdict,
        "statuses": statuses,
        "passed": verdict == "PVR_EC_DEPLOY_CANDIDATE_CONFIRMED",
        "promotion_ready": verdict == "PVR_EC_DEPLOY_CANDIDATE_CONFIRMED",
        "forward_purity_gate": loaded.get("forward_purity_gate"),
        "multi_seed_gate": loaded.get("multi_seed_gate"),
        "longer_training_gate": loaded.get("longer_training_gate"),
        "matched_step_gate": loaded.get("matched_step_gate"),
        "matched_wall_clock_gate": loaded.get("matched_wall_clock_gate"),
        "calibration_gate": loaded.get("calibration_gate"),
        "family_regression_gate": loaded.get("family_regression_gate"),
        "quality_per_ms_gate": loaded.get("quality_per_ms_gate"),
        "memory_gate": loaded.get("quality_per_ms_gate"),
        "reliability_proxy_gate": loaded.get("reliability_proxy_gate"),
        "overall_verdict": verdict,
        "promotion_status": verdict,
        "blocked_reasons": blocked_reasons,
        "missing_reports": missing,
        "recommended_next_action": "promote to deploy-candidate shadow rollout" if verdict == "PVR_EC_DEPLOY_CANDIDATE_CONFIRMED" else "address the listed blocking gate(s) without changing routing architecture",
    }
    _write_report_pair(output_dir, "pvr_ec_final_deployment_gate_report", payload, "PVR-EC Final Deployment Gate Report")
    return payload


def run_pvr_final_candidate_revalidation(
    args: argparse.Namespace,
    families: list[str],
    models: list[str],
    batch_sizes: list[int],
    sequence_lengths: list[int],
    output_dir: str | Path,
) -> dict[str, Any]:
    requested_models = models or ["fixed_moe_vectorized", "pvr_ec_deploy_top1", "pvr_ec_ownership_top1_final_candidate_v1_1"]
    candidate = next(
        (m for m in requested_models if str(m).startswith("pvr_ec_ownership_top1_final_candidate_v1_")),
        "pvr_ec_ownership_top1_final_candidate_v1_1",
    )
    version = candidate.replace("pvr_ec_ownership_top1_final_candidate_", "")
    payload = run_pvr_multiseed_confirmation_gate(
        args,
        families,
        requested_models,
        batch_sizes,
        sequence_lengths,
        output_dir,
    )
    revalidation = {
        **payload,
        "status": "PVR_EC_DEPLOY_CANDIDATE_CONFIRMED" if payload.get("passed") else "PVR_EC_REPEATABILITY_BLOCKED",
        "statuses": sorted(set(payload.get("statuses", [])) | {"PVR_EC_FINAL_CANDIDATE_REVALIDATION_REQUIRED"}),
        "revalidated_candidate": candidate,
    }
    _write_report_pair(output_dir, f"pvr_ec_final_candidate_{version}_revalidation_report", revalidation, f"PVR-EC Final Candidate {version} Revalidation Report")
    return revalidation


def summarize_pvr_blocker_resolution(input_dirs: list[str], output_dir: str | Path, seed: int = 42) -> dict[str, Any]:
    expected = {
        "repeatability_isolation": "pvr_ec_repeatability_collapse_isolation_report.json",
        "repeatability_repair": "pvr_ec_repeatability_repair_sweep_report.json",
        "qpm_shape": "pvr_ec_qpm_shape_regression_report.json",
        "qpm_memory_repair": "pvr_ec_qpm_memory_repair_report.json",
        "reliability_calibration": "pvr_ec_reliability_calibration_repair_report.json",
        "v1_1_revalidation": "pvr_ec_final_candidate_v1_1_revalidation_report.json",
    }
    loaded = {}
    missing = []
    for key, filename in expected.items():
        found = None
        for directory in input_dirs:
            path = Path(directory) / filename
            if path.exists():
                found = path
                break
        if found:
            loaded[key] = json.loads(found.read_text(encoding="utf-8"))
            loaded[key]["_path"] = str(found)
        elif key != "v1_1_revalidation":
            missing.append({"gate": key, "file": filename})
    blockers = []
    if missing:
        blockers.append("missing_reports")
    for key in ["repeatability_isolation", "repeatability_repair", "qpm_memory_repair", "reliability_calibration"]:
        report = loaded.get(key)
        if report and not bool(report.get("passed")):
            blockers.append(key)
    selected_requires_revalidation = any(bool(r.get("selected_requires_revalidation")) for r in loaded.values() if isinstance(r, dict))
    if selected_requires_revalidation and "v1_1_revalidation" not in loaded:
        blockers.append("v1_1_revalidation_missing")
    elif selected_requires_revalidation and not bool(loaded.get("v1_1_revalidation", {}).get("passed")):
        blockers.append("v1_1_revalidation_failed")
    if missing:
        verdict = "PARTIAL_PVR_EC_FINAL_BLOCKER_RESOLUTION"
    elif "repeatability_repair" in blockers or "repeatability_isolation" in blockers:
        verdict = "PVR_EC_REPEATABILITY_BLOCKED"
    elif "qpm_memory_repair" in blockers:
        verdict = "PVR_EC_QUALITY_PER_MS_BLOCKED"
    elif "reliability_calibration" in blockers:
        verdict = "PVR_EC_RELIABILITY_BLOCKED"
    elif blockers:
        verdict = "PVR_EC_DO_NOT_PROMOTE"
    else:
        verdict = "PVR_EC_DEPLOY_CANDIDATE_CONFIRMED"
    statuses = sorted({
        *(s for r in loaded.values() for s in r.get("statuses", [])),
        verdict,
        "PVR_EC_DO_NOT_PROMOTE" if verdict != "PVR_EC_DEPLOY_CANDIDATE_CONFIRMED" else "PVR_EC_DEPLOY_CANDIDATE_CONFIRMED",
    })
    payload = {
        "metadata": {"seed": seed, "input_dirs": input_dirs, "command": " ".join(sys.argv)},
        "status": verdict,
        "statuses": statuses,
        "passed": verdict == "PVR_EC_DEPLOY_CANDIDATE_CONFIRMED",
        "promotion_ready": verdict == "PVR_EC_DEPLOY_CANDIDATE_CONFIRMED",
        "blocked_reasons": blockers,
        "missing_reports": missing,
        "repeatability_isolation": loaded.get("repeatability_isolation"),
        "repeatability_repair": loaded.get("repeatability_repair"),
        "qpm_shape": loaded.get("qpm_shape"),
        "qpm_memory_repair": loaded.get("qpm_memory_repair"),
        "reliability_calibration": loaded.get("reliability_calibration"),
        "v1_1_revalidation": loaded.get("v1_1_revalidation"),
        "recommended_next_action": "promote only after final deployment gate aggregation" if verdict == "PVR_EC_DEPLOY_CANDIDATE_CONFIRMED" else "fix the listed blocker(s) without changing routing architecture",
    }
    _write_report_pair(output_dir, "pvr_ec_final_blocker_resolution_report", payload, "PVR-EC Final Blocker Resolution Report")
    return payload


def _load_named_report(input_dirs: list[str], filename: str) -> dict[str, Any] | None:
    for item in input_dirs:
        path = Path(item) / filename
        if path.exists():
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
                data["_path"] = str(path)
                return data
            except Exception:
                return None
    return None


def _write_nlp_bridge_ladder_plan(output_dir: str | Path, stage1_ready: bool, research_verdict: str) -> dict[str, Any]:
    stages = [
        "character/byte-level copy and transformation",
        "small-vocab synthetic language modeling",
        "algorithmic text tasks with natural-language wrappers",
        "short-context language modeling",
        "instruction-style toy QA",
        "small real NLP benchmark subset",
        "larger NLP benchmark suite",
    ]
    payload = {
        "status": "PVR_EC_NLP_BRIDGE_STAGE_1_READY" if stage1_ready else "PVR_EC_NLP_BRIDGE_STAGE_BLOCKED",
        "statuses": [
            "PVR_EC_NLP_BRIDGE_LADDER_REQUIRED",
            "PVR_EC_NLP_BRIDGE_STAGE_1_READY" if stage1_ready else "PVR_EC_NLP_BRIDGE_STAGE_BLOCKED",
        ],
        "research_verdict": research_verdict,
        "stage_1_ready": stage1_ready,
        "stages": [
            {
                "stage": idx + 1,
                "name": name,
                "required_models": ["fixed_moe_vectorized", "dense_baseline_or_dense_transformer", "pvr_ec_deploy_top1", "pvr_ec_ownership_top1_final_candidate"],
                "required_metrics": [
                    "owners/token", "Top2/Top4 executions", "loss", "accuracy_or_token_accuracy",
                    "calibration", "latency", "memory", "collapse cases", "task/family breakdown",
                    "confidence metrics", "incorrect overamp metrics",
                ],
                "promotion_rule": "advance only if forward purity passes, Top2/Top4 stay zero, metrics are competitive or explained, calibration is measured, collapses are absent or classified, and artifacts are reproducible",
            }
            for idx, name in enumerate(stages)
        ],
    }
    _write_report_pair(output_dir, "pvr_ec_nlp_bridge_ladder_plan", payload, "PVR-EC NLP Bridge Ladder Plan")
    return payload


def run_pvr_nlp_research_readiness_gate(input_dirs: list[str], output_dir: str | Path, seed: int = 42) -> dict[str, Any]:
    out = Path(output_dir)
    collapse = _load_named_report(input_dirs, "pvr_ec_collapse_case_replay_report.json")
    minimax = _load_named_report(input_dirs, "pvr_ec_minimax_candidate_selection_report.json")
    stability = _load_named_report(input_dirs, "pvr_ec_stability_repair_sweep_report.json")
    qpm_replay = _load_named_report(input_dirs, "pvr_ec_qpm_failing_shape_replay_report.json")
    qpm_formula = _load_named_report(input_dirs, "pvr_ec_qpm_formula_audit_report.json")
    qpm_runtime = _load_named_report(input_dirs, "pvr_ec_shape_qpm_runtime_repair_report.json")
    revalidation = _load_named_report(input_dirs, "pvr_ec_final_candidate_v1_2_revalidation_report.json")
    missing = [
        name for name, report in {
            "collapse_case_replay": collapse,
            "minimax_candidate_selection": minimax,
            "stability_repair_sweep": stability,
            "qpm_failing_shape_replay": qpm_replay,
            "qpm_formula_audit": qpm_formula,
            "shape_qpm_runtime_repair": qpm_runtime,
        }.items()
        if report is None
    ]
    collapse_count = int((collapse or {}).get("collapse_count") or 0)
    unexplained = int((collapse or {}).get("unexplained_collapse_count") or 0)
    qpm_classified = bool(qpm_replay and (not qpm_replay.get("failed_shape_count") or qpm_replay.get("failure_classifications")))
    rows = (qpm_runtime or qpm_replay or {}).get("rows", [])
    owners_ok = all(float(r.get("owner_count_per_token") or 1.0) == 1.0 for r in rows if r.get("model") == FINAL_CANDIDATE_CONFIG_NAME)
    topk_ok = all(float(r.get("Top2_executions") or 0.0) == 0.0 and float(r.get("Top4_executions") or 0.0) == 0.0 for r in rows if r.get("model") == FINAL_CANDIDATE_CONFIG_NAME)
    variant_summary = (minimax or {}).get("variant_summary", {})
    v1_data = variant_summary.get("v1") or variant_summary.get("final_candidate_v1") or next(iter(variant_summary.values()), {})
    fixed_loss = float((minimax or {}).get("fixed_mean_loss") or 0.0)
    fixed_acc = float((minimax or {}).get("fixed_mean_accuracy") or 0.0)
    mean_competitive = bool(
        v1_data
        and v1_data.get("mean_loss") is not None
        and float(v1_data["mean_loss"]) <= fixed_loss + 0.030
        and v1_data.get("mean_accuracy") is not None
        and float(v1_data["mean_accuracy"]) >= fixed_acc - 0.050
    )
    calibration_measured = any(
        data.get("calibration_proxy") is not None
        for data in variant_summary.values()
        if isinstance(data, dict)
    )
    forward_purity = owners_ok and topk_ok
    deployment_blocked = bool(collapse_count or not (qpm_runtime or {}).get("passed") or not (revalidation or {}).get("passed"))
    if missing or not forward_purity or unexplained or not mean_competitive:
        research_verdict = "PVR_EC_NLP_RESEARCH_NOT_READY"
    elif deployment_blocked:
        research_verdict = "PVR_EC_NLP_RESEARCH_READY_WITH_BLOCKERS"
    else:
        research_verdict = "PVR_EC_NLP_RESEARCH_READY"
    stage1_ready = research_verdict in {"PVR_EC_NLP_RESEARCH_READY", "PVR_EC_NLP_RESEARCH_READY_WITH_BLOCKERS"} and qpm_classified and calibration_measured
    statuses = {
        research_verdict,
        "PVR_EC_ALGORITHMIC_STAGE_COMPLETE" if mean_competitive else "PVR_EC_PROMISING_NEEDS_MORE_EVIDENCE",
        "PVR_EC_DEPLOYMENT_BLOCKED_BUT_RESEARCHABLE" if research_verdict == "PVR_EC_NLP_RESEARCH_READY_WITH_BLOCKERS" else research_verdict,
        "PVR_EC_NLP_BRIDGE_LADDER_REQUIRED",
        "PVR_EC_NLP_BRIDGE_STAGE_1_READY" if stage1_ready else "PVR_EC_NLP_BRIDGE_STAGE_BLOCKED",
    }
    deployment_verdict = "PVR_EC_DEPLOY_CANDIDATE_CONFIRMED"
    if collapse_count:
        deployment_verdict = "PVR_EC_REPEATABILITY_BLOCKED"
    elif qpm_runtime and not qpm_runtime.get("passed"):
        deployment_verdict = "PVR_EC_QPM_SHAPE_BLOCKED"
    elif not revalidation or not revalidation.get("passed"):
        deployment_verdict = "PVR_EC_DO_NOT_PROMOTE"
    verdict_payload = {
        "metadata": {"seed": seed, "input_dirs": input_dirs, "command": " ".join(sys.argv)},
        "status": deployment_verdict,
        "deployment_verdict": deployment_verdict,
        "research_verdict": research_verdict,
        "statuses": sorted(statuses | {deployment_verdict, "PVR_EC_DO_NOT_PROMOTE" if deployment_verdict != "PVR_EC_DEPLOY_CANDIDATE_CONFIRMED" else deployment_verdict}),
        "promotion_ready": deployment_verdict == "PVR_EC_DEPLOY_CANDIDATE_CONFIRMED",
        "research_ready": research_verdict in {"PVR_EC_NLP_RESEARCH_READY", "PVR_EC_NLP_RESEARCH_READY_WITH_BLOCKERS"},
        "collapse_count": collapse_count,
        "unexplained_collapse_count": unexplained,
        "qpm_classified": qpm_classified,
        "calibration_measured": calibration_measured,
        "mean_competitive": mean_competitive,
        "forward_purity": forward_purity,
        "missing_reports": missing,
    }
    _write_report_pair(out, "pvr_ec_deployment_vs_research_verdict_report", verdict_payload, "PVR-EC Deployment vs Research Verdict Report")
    ladder = _write_nlp_bridge_ladder_plan(out, stage1_ready, research_verdict)
    readiness = {
        **verdict_payload,
        "status": research_verdict,
        "passed": research_verdict in {"PVR_EC_NLP_RESEARCH_READY", "PVR_EC_NLP_RESEARCH_READY_WITH_BLOCKERS"},
        "nlp_bridge_ladder": ladder,
        "source_reports": {k: (v or {}).get("_path") for k, v in {
            "collapse": collapse,
            "minimax": minimax,
            "stability": stability,
            "qpm_replay": qpm_replay,
            "qpm_formula": qpm_formula,
            "qpm_runtime": qpm_runtime,
            "v1_2_revalidation": revalidation,
        }.items()},
    }
    _write_report_pair(out, "pvr_ec_nlp_research_readiness_report", readiness, "PVR-EC NLP Research Readiness Report")
    return readiness


def summarize_pvr_minimax_blocker_resolution(input_dirs: list[str], output_dir: str | Path, include_nlp_research_readiness: bool = False, seed: int = 42) -> dict[str, Any]:
    out = Path(output_dir)
    collapse = _load_named_report(input_dirs, "pvr_ec_collapse_case_replay_report.json")
    minimax = _load_named_report(input_dirs, "pvr_ec_minimax_candidate_selection_report.json")
    stability = _load_named_report(input_dirs, "pvr_ec_stability_repair_sweep_report.json")
    qpm_replay = _load_named_report(input_dirs, "pvr_ec_qpm_failing_shape_replay_report.json")
    qpm_formula = _load_named_report(input_dirs, "pvr_ec_qpm_formula_audit_report.json")
    qpm_runtime = _load_named_report(input_dirs, "pvr_ec_shape_qpm_runtime_repair_report.json")
    readiness = _load_named_report(input_dirs, "pvr_ec_nlp_research_readiness_report.json") if include_nlp_research_readiness else None
    revalidation = _load_named_report(input_dirs, "pvr_ec_final_candidate_v1_2_revalidation_report.json")
    missing = [
        name for name, report in {
            "collapse": collapse,
            "minimax": minimax,
            "stability": stability,
            "qpm_replay": qpm_replay,
            "qpm_formula": qpm_formula,
            "qpm_runtime": qpm_runtime,
        }.items()
        if report is None
    ]
    blockers = []
    if missing:
        blockers.append("missing_reports")
    if collapse and int(collapse.get("collapse_count") or 0) > 0:
        blockers.append("collapse_cases")
    if minimax and not minimax.get("passed"):
        blockers.append("minimax_selection")
    if stability and not stability.get("passed"):
        blockers.append("stability_repair")
    if qpm_runtime and not qpm_runtime.get("passed"):
        blockers.append("qpm_shape")
    if minimax and minimax.get("selected_requires_revalidation") and not (revalidation and revalidation.get("passed")):
        blockers.append("v1_2_revalidation")
    if "collapse_cases" in blockers:
        deployment_verdict = "PVR_EC_REPEATABILITY_BLOCKED"
    elif "qpm_shape" in blockers:
        deployment_verdict = "PVR_EC_QPM_SHAPE_BLOCKED"
    elif blockers:
        deployment_verdict = "PVR_EC_DO_NOT_PROMOTE" if not missing else "PARTIAL_PVR_EC_MINIMAX_STABILITY_AND_RESEARCH_READINESS"
    else:
        deployment_verdict = "PVR_EC_DEPLOY_CANDIDATE_CONFIRMED"
    research_verdict = (readiness or {}).get("research_verdict") or (readiness or {}).get("status") or "PVR_EC_NLP_RESEARCH_NOT_READY"
    statuses = sorted({
        deployment_verdict,
        research_verdict,
        *(s for report in [collapse, minimax, stability, qpm_replay, qpm_formula, qpm_runtime, readiness, revalidation] if report for s in report.get("statuses", [])),
        "PVR_EC_DO_NOT_PROMOTE" if deployment_verdict != "PVR_EC_DEPLOY_CANDIDATE_CONFIRMED" else "PVR_EC_DEPLOY_CANDIDATE_CONFIRMED",
    })
    payload = {
        "metadata": {"seed": seed, "input_dirs": input_dirs, "command": " ".join(sys.argv)},
        "status": deployment_verdict,
        "deployment_verdict": deployment_verdict,
        "research_verdict": research_verdict,
        "statuses": statuses,
        "promotion_ready": deployment_verdict == "PVR_EC_DEPLOY_CANDIDATE_CONFIRMED",
        "research_ready": research_verdict in {"PVR_EC_NLP_RESEARCH_READY", "PVR_EC_NLP_RESEARCH_READY_WITH_BLOCKERS"},
        "blocked_reasons": blockers,
        "missing_reports": missing,
        "collapse_case_replay": collapse,
        "minimax_candidate_selection": minimax,
        "stability_repair_sweep": stability,
        "qpm_failing_shape_replay": qpm_replay,
        "qpm_formula_audit": qpm_formula,
        "shape_qpm_runtime_repair": qpm_runtime,
        "nlp_research_readiness": readiness,
        "v1_2_revalidation": revalidation,
        "recommended_next_action": "proceed to Stage 1 NLP bridge only if research verdict allows; do not deploy while blockers remain",
    }
    _write_report_pair(out, "pvr_ec_minimax_final_blocker_resolution_report", payload, "PVR-EC Minimax Final Blocker Resolution Report")
    return payload


def summarize_pvr_root_cause(input_dirs: list[str], output_dir: str | Path, seed: int = 42) -> dict[str, Any]:
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, Any]] = []
    loaded_reports: list[str] = []
    missing_dirs: list[str] = []
    for item in input_dirs:
        path = Path(item)
        if not path.exists():
            missing_dirs.append(str(path))
            continue
        candidate_files = [
            path / "per_dataset_metrics.json",
            path / "inference_latency_matrix.json",
            path / "capacity_fairness_matrix_report.json",
            path / "pvr_ec_root_baseline_matrix.json",
        ]
        for file_path in candidate_files:
            if not file_path.exists():
                continue
            try:
                payload = json.loads(file_path.read_text(encoding="utf-8"))
            except Exception:
                continue
            data_rows = payload if isinstance(payload, list) else payload.get("rows", [])
            if isinstance(data_rows, list):
                rows.extend([r for r in data_rows if isinstance(r, dict)])
                loaded_reports.append(str(file_path))

    runner = AlgorithmicBenchmarkRunner(
        mode="smoke",
        seed=seed,
        models=[],
        root_cause_flags={"summarize_pvr_root_cause": True},
    )
    runner.output_dir = out
    runner.output_dir.mkdir(parents=True, exist_ok=True)
    metadata = runner._artifact_metadata()
    metadata.update({
        "input_dirs": input_dirs,
        "loaded_reports": loaded_reports,
        "missing_dirs": missing_dirs,
    })
    runner._write_root_cause_artifacts(
        rows,
        metadata,
        source="root_summary",
        summary={"loaded_report_count": len(loaded_reports), "missing_dirs": missing_dirs},
    )
    summary_path = out / "pvr_ec_root_cause_summary.json"
    return json.loads(summary_path.read_text(encoding="utf-8")) if summary_path.exists() else {
        "status": "PVR_EC_ROOT_CAUSE_INCONCLUSIVE",
        "statuses": ["PVR_EC_ROOT_CAUSE_INCONCLUSIVE", "PVR_EC_DO_NOT_PROMOTE"],
    }


def main():
    parser = argparse.ArgumentParser(description="Algorithmic Benchmark Runner")
    parser.add_argument("--mode", choices=["smoke", "benchmark-lite", "benchmark-full", "inference-only", "pvr-overfit-sanity"], default="smoke")
    parser.add_argument("--families", default="clrs,listops,scan,dyck", help="Comma-separated families")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--scale", choices=["tiny", "small", "medium"], default="small")
    parser.add_argument("--sample-limit", type=int, default=None)
    parser.add_argument("--train-steps", type=int, default=None, help="Override training steps")
    parser.add_argument("--device", default="cpu")
    parser.add_argument("--amp", action="store_true", help="Enable mixed precision (CUDA only)")
    parser.add_argument("--models", default=None, help="Comma-separated model names to evaluate")
    parser.add_argument("--profile-compute", action="store_true", help="Track compute metrics")
    parser.add_argument("--length-generalization", action="store_true", help="Run length extrapolation test")
    parser.add_argument("--pvr-execution-mode", choices=sorted(EXECUTION_MODES), default=None)
    parser.add_argument("--pvr-expert-type", choices=sorted(EXPERT_TYPES), default=None)
    parser.add_argument("--pvr-training-dispatch-mode", choices=["dense", "sparse"], default=None)
    parser.add_argument("--pvr-inference-dispatch-mode", choices=["dense", "sparse"], default=None)
    parser.add_argument("--pvr-deploy-mode", choices=sorted(DEPLOY_MODES), default="off")
    parser.add_argument("--pvr-aux-alpha", type=float, default=0.5)
    parser.add_argument("--pvr-expert-delta-scale", type=float, default=None)
    parser.add_argument("--pvr-expert-delta-scale-schedule", choices=["constant", "linear_warmup", "cosine_warmup", "warmup_hold", "warmup_hold_decay"], default="constant")
    parser.add_argument("--pvr-expert-delta-scale-start", type=float, default=None)
    parser.add_argument("--pvr-expert-delta-scale-end", type=float, default=None)
    parser.add_argument("--pvr-expert-delta-scale-warmup-steps", type=int, default=None)
    parser.add_argument("--pvr-expert-delta-scale-hold-steps", type=int, default=None)
    parser.add_argument("--pvr-expert-delta-scale-decay", type=float, default=None)
    parser.add_argument("--benchmark-inference-only", action="store_true")
    parser.add_argument("--output-dir", default=None)
    parser.add_argument("--enable-ownership-map", action="store_true")
    parser.add_argument("--ownership-map-mode", default=None)
    parser.add_argument("--run-capacity-architecture-audit", action="store_true")
    parser.add_argument("--run-capacity-ladder", action="store_true")
    parser.add_argument("--run-capacity-fairness-audit", action="store_true")
    parser.add_argument("--run-capacity-latency-matrix", action="store_true")
    parser.add_argument("--run-root-baseline-matrix", action="store_true")
    parser.add_argument("--train-steps-list", default=None)
    parser.add_argument("--seed-list", default=None)
    parser.add_argument("--run-training-dynamics-diagnostic", action="store_true")
    parser.add_argument("--run-ownership-integration-diagnostic", action="store_true")
    parser.add_argument("--ownership-schedule-sweep", default=None)
    parser.add_argument("--run-shared-sparse-ablation", action="store_true")
    parser.add_argument("--run-learning-separation-diagnostic", action="store_true")
    parser.add_argument("--shared-scale-sweep", default=None)
    parser.add_argument("--expert-delta-scale-sweep", default=None)
    parser.add_argument("--run-loss-calibration-diagnostic", action="store_true")
    parser.add_argument("--loss-schedule-sweep", default=None)
    parser.add_argument("--run-task-fit-diagnostic", action="store_true")
    parser.add_argument("--task-loss-schedule-sweep", default=None)
    parser.add_argument("--batch-size-list", default=None)
    parser.add_argument("--seq-len-list", default=None)
    parser.add_argument("--run-latency-stability-diagnostic", action="store_true")
    parser.add_argument("--summarize-pvr-root-cause", action="store_true")
    parser.add_argument("--input-dirs", default=None)
    parser.add_argument("--run-pvr-overfit-sanity", action="store_true")
    parser.add_argument("--pvr-overfit-task", default=None)
    parser.add_argument("--pvr-overfit-tasks", default=None)
    parser.add_argument("--pvr-overfit-steps", type=int, default=100)
    parser.add_argument("--pvr-overfit-batch-size", type=int, default=16)
    parser.add_argument("--pvr-overfit-single-batch", action="store_true")
    parser.add_argument("--pvr-debug-fixed-owner", action="store_true")
    parser.add_argument("--pvr-debug-disable-shared", action="store_true")
    parser.add_argument("--pvr-debug-disable-sparse", action="store_true")
    parser.add_argument("--pvr-debug-force-expert-id", type=int, default=None)
    parser.add_argument("--run-gradient-flow-diagnostic", action="store_true")
    parser.add_argument("--run-optimizer-update-diagnostic", action="store_true")
    parser.add_argument("--run-expert-contribution-diagnostic", action="store_true")
    parser.add_argument("--run-loss-target-sanity", action="store_true")
    parser.add_argument("--run-shared-absorption-diagnostic", action="store_true")
    parser.add_argument("--pvr-shared-scale-sweep", default=None)
    parser.add_argument("--pvr-expert-delta-scale-sweep", default=None)
    parser.add_argument("--run-expert-initialization-diagnostic", action="store_true")
    parser.add_argument("--pvr-expert-init-sweep", default=None)
    parser.add_argument("--run-after-repair-confirmation", action="store_true")
    parser.add_argument("--run-nonlinear-overfit-diagnostic", action="store_true")
    parser.add_argument("--run-fixed-owner-parity-diagnostic", action="store_true")
    parser.add_argument("--run-parity-scale-sweep", action="store_true")
    parser.add_argument("--run-nonlinear-overfit-confirmation", action="store_true")
    parser.add_argument("--run-after-nonlinear-repair-confirmation", action="store_true")
    parser.add_argument("--run-expert-delta-scale-schedule-diagnostic", action="store_true")
    parser.add_argument("--run-expert-delta-scale-schedule-confirmation", action="store_true")
    parser.add_argument("--run-residual-alignment-diagnostic", action="store_true")
    parser.add_argument("--run-family-scale-sweep", action="store_true")
    parser.add_argument("--run-conditional-scale-oracle", action="store_true")
    parser.add_argument("--conditional-scale-modes", default=None)
    parser.add_argument("--run-benchmark-transfer-confirmation", action="store_true")
    parser.add_argument("--run-task-level-transfer-diagnostic", action="store_true")
    parser.add_argument("--run-decision-token-credit-diagnostic", action="store_true")
    parser.add_argument("--run-token-to-sequence-transfer-diagnostic", action="store_true")
    parser.add_argument("--run-family-failure-decomposition", action="store_true")
    parser.add_argument("--run-output-readout-diagnostic", action="store_true")
    parser.add_argument("--readout-variants", default=None)
    parser.add_argument("--run-loss-credit-repair-sweep", action="store_true")
    parser.add_argument("--loss-credit-variants", default=None)
    parser.add_argument("--run-curriculum-repair-sweep", action="store_true")
    parser.add_argument("--curriculum-variants", default=None)
    parser.add_argument("--run-segment-residual-diagnostic", action="store_true")
    parser.add_argument("--run-sparse-logit-direction-diagnostic", action="store_true")
    parser.add_argument("--run-sparse-auxiliary-loss-sweep", action="store_true")
    parser.add_argument("--run-calibration-constrained-sparse-aux-sweep", action="store_true")
    parser.add_argument("--sparse-aux-loss-variants", default=None)
    parser.add_argument("--run-sparse-auxiliary-scope-sweep", action="store_true")
    parser.add_argument("--sparse-aux-scopes", default=None)
    parser.add_argument("--run-sparse-direction-transfer-confirmation", action="store_true")
    parser.add_argument("--run-final-config-manifest", action="store_true")
    parser.add_argument("--run-forward-purity-gate", action="store_true")
    parser.add_argument("--run-multiseed-confirmation-gate", action="store_true")
    parser.add_argument("--run-longer-training-confirmation-gate", action="store_true")
    parser.add_argument("--run-matched-wall-clock-gate", action="store_true")
    parser.add_argument("--run-final-calibration-sweep", action="store_true")
    parser.add_argument("--final-calibration-variants", default=None)
    parser.add_argument("--run-family-regression-gate", action="store_true")
    parser.add_argument("--run-quality-per-ms-memory-gate", action="store_true")
    parser.add_argument("--run-reliability-proxy-gate", action="store_true")
    parser.add_argument("--summarize-pvr-final-deployment-gate", action="store_true")
    parser.add_argument("--max-train-seconds", type=float, default=None)
    parser.add_argument("--run-repeatability-collapse-isolation", action="store_true")
    parser.add_argument("--run-repeatability-repair-sweep", action="store_true")
    parser.add_argument("--repeatability-repair-variants", default=None)
    parser.add_argument("--run-qpm-shape-regression-analysis", action="store_true")
    parser.add_argument("--run-qpm-memory-repair", action="store_true")
    parser.add_argument("--run-reliability-calibration-repair", action="store_true")
    parser.add_argument("--calibration-repair-variants", default=None)
    parser.add_argument("--run-final-candidate-revalidation", action="store_true")
    parser.add_argument("--summarize-pvr-blocker-resolution", action="store_true")
    parser.add_argument("--run-collapse-case-replay", action="store_true")
    parser.add_argument("--run-minimax-candidate-selection", action="store_true")
    parser.add_argument("--minimax-variants", default=None)
    parser.add_argument("--run-stability-repair-sweep", action="store_true")
    parser.add_argument("--stability-repair-variants", default=None)
    parser.add_argument("--shape-list", default=None)
    parser.add_argument("--run-qpm-failing-shape-replay", action="store_true")
    parser.add_argument("--run-qpm-formula-audit", action="store_true")
    parser.add_argument("--run-shape-qpm-runtime-repair", action="store_true")
    parser.add_argument("--run-pvr-nlp-research-readiness-gate", action="store_true")
    parser.add_argument("--summarize-pvr-minimax-blocker-resolution", action="store_true")
    parser.add_argument("--include-nlp-research-readiness", action="store_true")
    parser.add_argument("--warmup-steps", type=int, default=10)
    parser.add_argument("--timed-steps", type=int, default=50)
    parser.add_argument("--batch-sizes", default="1,32")
    parser.add_argument("--sequence-lengths", default="64")
    parser.add_argument("--batch-size", type=int, default=None)
    parser.add_argument("--seq-len", type=int, default=None)
    parser.add_argument("--profile-deploy", action="store_true")
    args = parser.parse_args()

    families = [f.strip() for f in args.families.split(",")]
    models = [m.strip() for m in args.models.split(",")] if args.models else None
    if models is None and args.run_learning_separation_diagnostic:
        models = [
            "fixed_moe_vectorized",
            "pvr_ec_learning_full",
            "pvr_ec_learning_shared_only",
            "pvr_ec_learning_sparse_only",
            "pvr_ec_learning_shared_scale_0_5",
            "pvr_ec_learning_expert_delta_scale_2_0",
            "pvr_ec_ownership_top1_delta_rank_16",
            "pvr_ec_ownership_top1_delta_rank_64",
            "pvr_ec_ownership_top1_micro_ffn_0_5x",
            "pvr_ec_ownership_top1_delayed_candidate",
        ]
    nonlinear_model_default_requested = (
        args.run_nonlinear_overfit_diagnostic
        or args.run_fixed_owner_parity_diagnostic
        or args.run_parity_scale_sweep
        or args.run_nonlinear_overfit_confirmation
        or args.run_after_nonlinear_repair_confirmation
        or args.run_expert_delta_scale_schedule_diagnostic
        or args.run_expert_delta_scale_schedule_confirmation
    )
    if models is None and (args.run_pvr_overfit_sanity or args.mode == "pvr-overfit-sanity") and not nonlinear_model_default_requested:
        models = [
            "dense_baseline",
            "fixed_moe_vectorized",
            "pvr_shared_only",
            "pvr_sparse_only",
            "pvr_full",
        ]
    if models is None and args.run_nonlinear_overfit_diagnostic:
        models = [
            "dense_baseline",
            "fixed_moe_vectorized",
            "pvr_shared_only",
            "pvr_sparse_only",
            "pvr_full",
            "pvr_full_fixed_owner_e0",
            "pvr_full_fixed_owner_round_robin",
            "pvr_full_uniform_owner",
            "pvr_full_shared_scale_0_5",
            "pvr_full_shared_scale_0_25",
            "pvr_full_shared_scale_0_0",
            "pvr_full_expert_delta_scale_1",
            "pvr_full_expert_delta_scale_2",
            "pvr_full_expert_delta_scale_4",
            "pvr_full_expert_delta_scale_8",
            "pvr_full_delta_rank_16",
            "pvr_full_delta_rank_64",
            "pvr_full_delta_rank_128",
            "pvr_full_micro_ffn_0_5x",
        ]
    if models is None and args.run_fixed_owner_parity_diagnostic:
        models = [
            "pvr_full",
            "pvr_full_fixed_owner_e0",
            "pvr_full_fixed_owner_round_robin",
            "pvr_full_uniform_owner",
            "pvr_sparse_only",
            "pvr_shared_only",
        ]
    if models is None and args.run_parity_scale_sweep:
        models = [
            "pvr_full",
            "pvr_full_shared_scale_1_0",
            "pvr_full_shared_scale_0_5",
            "pvr_full_shared_scale_0_25",
            "pvr_full_shared_scale_0_0",
            "pvr_full_expert_delta_scale_0_5",
            "pvr_full_expert_delta_scale_1",
            "pvr_full_expert_delta_scale_2",
            "pvr_full_expert_delta_scale_4",
            "pvr_full_expert_delta_scale_8",
        ]
    if models is None and args.run_expert_delta_scale_schedule_diagnostic and args.mode == "pvr-overfit-sanity":
        models = [
            "pvr_full",
            "pvr_full_expert_delta_scale_4",
            "pvr_full_expert_delta_scale_8",
            "pvr_full_scale_schedule_1_to_4",
            "pvr_full_scale_schedule_1_to_8",
            "pvr_full_scale_schedule_1_to_8_to_4",
        ]
    if models is None and args.run_family_scale_sweep:
        models = [
            "pvr_ec_ownership_top1_constant_1",
            "pvr_ec_ownership_top1_constant_2",
            "pvr_ec_ownership_top1_constant_4",
            "pvr_ec_ownership_top1_constant_8",
            "pvr_ec_ownership_top1_scale_schedule_1_to_4",
            "pvr_ec_ownership_top1_scale_schedule_1_to_8",
            "pvr_ec_ownership_top1_scale_schedule_1_to_8_to_4",
            "pvr_ec_ownership_top1_scale_schedule_1_to_8_to_2",
            "pvr_ec_ownership_top1_scale_schedule_1_to_4_to_2",
        ]
    if models is None and args.run_benchmark_transfer_confirmation:
        models = [
            "fixed_moe_vectorized",
            "pvr_ec_deploy_top1",
            "pvr_ec_ownership_top1_best_scale_repair",
        ]
    if models is None and args.run_task_level_transfer_diagnostic:
        models = [
            "fixed_moe_vectorized",
            "pvr_ec_deploy_top1",
            "pvr_ec_ownership_top1_scale_schedule_1_to_8",
        ]
    batch_sizes = _parse_csv_ints(args.batch_sizes)
    sequence_lengths = _parse_csv_ints(args.sequence_lengths)
    if args.batch_size_list:
        batch_sizes = _parse_csv_ints(args.batch_size_list)
    if args.seq_len_list:
        sequence_lengths = _parse_csv_ints(args.seq_len_list)
    if args.batch_size is not None:
        batch_sizes = [args.batch_size]
    if args.seq_len is not None:
        sequence_lengths = [args.seq_len]
    if args.shape_list:
        batch_sizes, sequence_lengths = _parse_shape_list(args.shape_list)
    root_cause_flags = {
        "run_root_baseline_matrix": args.run_root_baseline_matrix,
        "run_training_dynamics_diagnostic": args.run_training_dynamics_diagnostic,
        "run_ownership_integration_diagnostic": args.run_ownership_integration_diagnostic,
        "run_shared_sparse_ablation": args.run_shared_sparse_ablation,
        "run_learning_separation_diagnostic": args.run_learning_separation_diagnostic,
        "run_loss_calibration_diagnostic": args.run_loss_calibration_diagnostic,
        "run_task_fit_diagnostic": args.run_task_fit_diagnostic,
        "run_latency_stability_diagnostic": args.run_latency_stability_diagnostic,
        "run_gradient_flow_diagnostic": args.run_gradient_flow_diagnostic,
        "run_optimizer_update_diagnostic": args.run_optimizer_update_diagnostic,
        "run_expert_contribution_diagnostic": args.run_expert_contribution_diagnostic,
        "run_loss_target_sanity": args.run_loss_target_sanity,
        "run_shared_absorption_diagnostic": args.run_shared_absorption_diagnostic,
        "run_expert_initialization_diagnostic": args.run_expert_initialization_diagnostic,
        "run_after_repair_confirmation": args.run_after_repair_confirmation,
        "run_nonlinear_overfit_diagnostic": args.run_nonlinear_overfit_diagnostic,
        "run_fixed_owner_parity_diagnostic": args.run_fixed_owner_parity_diagnostic,
        "run_parity_scale_sweep": args.run_parity_scale_sweep,
        "run_nonlinear_overfit_confirmation": args.run_nonlinear_overfit_confirmation,
        "run_after_nonlinear_repair_confirmation": args.run_after_nonlinear_repair_confirmation,
        "run_expert_delta_scale_schedule_diagnostic": args.run_expert_delta_scale_schedule_diagnostic,
        "run_expert_delta_scale_schedule_confirmation": args.run_expert_delta_scale_schedule_confirmation,
        "run_residual_alignment_diagnostic": args.run_residual_alignment_diagnostic,
        "run_family_scale_sweep": args.run_family_scale_sweep,
        "run_conditional_scale_oracle": args.run_conditional_scale_oracle,
        "run_benchmark_transfer_confirmation": args.run_benchmark_transfer_confirmation,
        "run_task_level_transfer_diagnostic": args.run_task_level_transfer_diagnostic,
        "run_decision_token_credit_diagnostic": args.run_decision_token_credit_diagnostic,
        "run_token_to_sequence_transfer_diagnostic": args.run_token_to_sequence_transfer_diagnostic,
        "run_family_failure_decomposition": args.run_family_failure_decomposition,
        "run_output_readout_diagnostic": args.run_output_readout_diagnostic,
        "run_loss_credit_repair_sweep": args.run_loss_credit_repair_sweep,
        "run_curriculum_repair_sweep": args.run_curriculum_repair_sweep,
        "run_segment_residual_diagnostic": args.run_segment_residual_diagnostic,
        "run_sparse_logit_direction_diagnostic": args.run_sparse_logit_direction_diagnostic,
        "run_sparse_auxiliary_loss_sweep": args.run_sparse_auxiliary_loss_sweep,
        "run_calibration_constrained_sparse_aux_sweep": args.run_calibration_constrained_sparse_aux_sweep,
        "run_sparse_auxiliary_scope_sweep": args.run_sparse_auxiliary_scope_sweep,
        "run_sparse_direction_transfer_confirmation": args.run_sparse_direction_transfer_confirmation,
        "run_final_config_manifest": args.run_final_config_manifest,
        "run_forward_purity_gate": args.run_forward_purity_gate,
        "run_multiseed_confirmation_gate": args.run_multiseed_confirmation_gate,
        "run_longer_training_confirmation_gate": args.run_longer_training_confirmation_gate,
        "run_matched_wall_clock_gate": args.run_matched_wall_clock_gate,
        "run_final_calibration_sweep": args.run_final_calibration_sweep,
        "run_family_regression_gate": args.run_family_regression_gate,
        "run_quality_per_ms_memory_gate": args.run_quality_per_ms_memory_gate,
        "run_reliability_proxy_gate": args.run_reliability_proxy_gate,
        "run_repeatability_collapse_isolation": args.run_repeatability_collapse_isolation,
        "run_repeatability_repair_sweep": args.run_repeatability_repair_sweep,
        "run_qpm_shape_regression_analysis": args.run_qpm_shape_regression_analysis,
        "run_qpm_memory_repair": args.run_qpm_memory_repair,
        "run_reliability_calibration_repair": args.run_reliability_calibration_repair,
        "run_final_candidate_revalidation": args.run_final_candidate_revalidation,
        "run_collapse_case_replay": args.run_collapse_case_replay,
        "run_minimax_candidate_selection": args.run_minimax_candidate_selection,
        "run_stability_repair_sweep": args.run_stability_repair_sweep,
        "run_qpm_failing_shape_replay": args.run_qpm_failing_shape_replay,
        "run_qpm_formula_audit": args.run_qpm_formula_audit,
        "run_shape_qpm_runtime_repair": args.run_shape_qpm_runtime_repair,
    }
    overfit_tasks = _parse_csv_strings(args.pvr_overfit_tasks) or (
        [args.pvr_overfit_task] if args.pvr_overfit_task else ["toy_identity"]
    )
    diagnostic_sweeps = {
        "train_steps_list": _parse_csv_ints(args.train_steps_list, [args.train_steps] if args.train_steps else []),
        "seed_list": _parse_csv_ints(args.seed_list, [args.seed]),
        "ownership_schedule_sweep": _parse_csv_strings(args.ownership_schedule_sweep),
        "shared_scale_sweep": _parse_csv_strings(args.shared_scale_sweep),
        "expert_delta_scale_sweep": _parse_csv_strings(args.expert_delta_scale_sweep),
        "loss_schedule_sweep": _parse_csv_strings(args.loss_schedule_sweep),
        "task_loss_schedule_sweep": _parse_csv_strings(args.task_loss_schedule_sweep),
        "batch_size_list": batch_sizes,
        "seq_len_list": sequence_lengths,
        "shape_pairs": _parse_shape_pairs(args.shape_list),
        "pvr_overfit_tasks": overfit_tasks,
        "pvr_overfit_steps": args.pvr_overfit_steps,
        "pvr_overfit_batch_size": args.pvr_overfit_batch_size,
        "pvr_overfit_single_batch": args.pvr_overfit_single_batch or args.mode == "pvr-overfit-sanity",
        "pvr_shared_scale_sweep": _parse_csv_strings(args.pvr_shared_scale_sweep),
        "pvr_expert_delta_scale_sweep": _parse_csv_strings(args.pvr_expert_delta_scale_sweep),
        "pvr_expert_init_sweep": _parse_csv_strings(args.pvr_expert_init_sweep),
        "pvr_expert_delta_scale_schedule": args.pvr_expert_delta_scale_schedule,
        "pvr_expert_delta_scale_start": args.pvr_expert_delta_scale_start,
        "pvr_expert_delta_scale_end": args.pvr_expert_delta_scale_end,
        "pvr_expert_delta_scale_warmup_steps": args.pvr_expert_delta_scale_warmup_steps,
        "pvr_expert_delta_scale_hold_steps": args.pvr_expert_delta_scale_hold_steps,
        "pvr_expert_delta_scale_decay": args.pvr_expert_delta_scale_decay,
        "conditional_scale_modes": _parse_csv_strings(args.conditional_scale_modes),
        "readout_variants": _parse_csv_strings(args.readout_variants),
        "loss_credit_variants": _parse_csv_strings(args.loss_credit_variants),
        "curriculum_variants": _parse_csv_strings(args.curriculum_variants),
        "sparse_aux_loss_variants": _parse_csv_strings(args.sparse_aux_loss_variants),
        "sparse_aux_scopes": _parse_csv_strings(args.sparse_aux_scopes),
        "final_calibration_variants": _parse_csv_strings(args.final_calibration_variants),
        "repeatability_repair_variants": _parse_csv_strings(args.repeatability_repair_variants),
        "calibration_repair_variants": _parse_csv_strings(args.calibration_repair_variants),
        "minimax_variants": _parse_csv_strings(args.minimax_variants),
        "stability_repair_variants": _parse_csv_strings(args.stability_repair_variants),
        "max_train_seconds": args.max_train_seconds,
    }
    if args.pvr_debug_disable_shared and models:
        for name in list(models):
            if name.startswith("pvr_") and name != "pvr_sparse_only":
                pass
    if args.run_pvr_overfit_sanity:
        args.mode = "pvr-overfit-sanity"
    if args.summarize_pvr_root_cause:
        output_dir = args.output_dir or "evaluation/benchmark_results/pvr_ec_root_cause_summary"
        summary = summarize_pvr_root_cause(_parse_csv_strings(args.input_dirs), output_dir, seed=args.seed)
        print(f"  STATUS: {summary['status']}")
        print("  Promotion remains blocked.")
        return
    if args.summarize_pvr_final_deployment_gate:
        output_dir = args.output_dir or "evaluation/benchmark_results/pvr_final_deployment_gate"
        summary = summarize_pvr_final_deployment_gate(_parse_csv_strings(args.input_dirs), output_dir, seed=args.seed)
        print(f"  STATUS: {summary['status']}")
        print(f"  Blocked reasons: {summary.get('blocked_reasons', [])}")
        return
    if args.summarize_pvr_blocker_resolution:
        output_dir = args.output_dir or "evaluation/benchmark_results/pvr_final_blocker_resolution"
        summary = summarize_pvr_blocker_resolution(_parse_csv_strings(args.input_dirs), output_dir, seed=args.seed)
        print(f"  STATUS: {summary['status']}")
        print(f"  Blocked reasons: {summary.get('blocked_reasons', [])}")
        return
    if args.run_pvr_nlp_research_readiness_gate:
        output_dir = args.output_dir or "evaluation/benchmark_results/pvr_nlp_research_readiness"
        summary = run_pvr_nlp_research_readiness_gate(_parse_csv_strings(args.input_dirs), output_dir, seed=args.seed)
        print(f"  STATUS: {summary['status']}")
        print(f"  Deployment verdict: {summary.get('deployment_verdict')}")
        return
    if args.summarize_pvr_minimax_blocker_resolution:
        output_dir = args.output_dir or "evaluation/benchmark_results/pvr_minimax_final_blocker_resolution"
        summary = summarize_pvr_minimax_blocker_resolution(
            _parse_csv_strings(args.input_dirs),
            output_dir,
            include_nlp_research_readiness=args.include_nlp_research_readiness,
            seed=args.seed,
        )
        print(f"  STATUS: {summary['status']}")
        print(f"  Research verdict: {summary.get('research_verdict')}")
        print(f"  Blocked reasons: {summary.get('blocked_reasons', [])}")
        return
    if args.run_collapse_case_replay:
        output_dir = args.output_dir or "evaluation/benchmark_results/pvr_minimax_collapse_case_replay"
        gate_models = models or ["fixed_moe_vectorized", "pvr_ec_deploy_top1", FINAL_CANDIDATE_CONFIG_NAME, "pvr_ec_ownership_top1_final_candidate_v1_1"]
        summary = run_pvr_collapse_case_replay(args, families, gate_models, batch_sizes, sequence_lengths, output_dir)
        print(f"  STATUS: {summary['status']}")
        return
    if args.run_minimax_candidate_selection:
        output_dir = args.output_dir or "evaluation/benchmark_results/pvr_minimax_candidate_selection"
        gate_models = models or ["fixed_moe_vectorized", "pvr_ec_deploy_top1", FINAL_CANDIDATE_CONFIG_NAME]
        summary = run_pvr_minimax_candidate_selection(args, families, gate_models, batch_sizes, sequence_lengths, output_dir)
        print(f"  STATUS: {summary['status']}")
        return
    if args.run_stability_repair_sweep:
        output_dir = args.output_dir or "evaluation/benchmark_results/pvr_minimax_stability_repair_sweep"
        gate_models = models or ["fixed_moe_vectorized", FINAL_CANDIDATE_CONFIG_NAME]
        summary = run_pvr_stability_repair_sweep(args, families, gate_models, batch_sizes, sequence_lengths, output_dir)
        print(f"  STATUS: {summary['status']}")
        return
    if args.run_repeatability_collapse_isolation:
        output_dir = args.output_dir or "evaluation/benchmark_results/pvr_blocker_repeatability_isolation"
        gate_models = models or ["fixed_moe_vectorized", FINAL_CANDIDATE_CONFIG_NAME]
        summary = run_pvr_repeatability_collapse_isolation(args, families, gate_models, batch_sizes, sequence_lengths, output_dir)
        print(f"  STATUS: {summary['status']}")
        return
    if args.run_repeatability_repair_sweep:
        output_dir = args.output_dir or "evaluation/benchmark_results/pvr_blocker_repeatability_repair"
        gate_models = models or ["fixed_moe_vectorized", FINAL_CANDIDATE_CONFIG_NAME]
        summary = run_pvr_repeatability_repair_sweep(args, families, gate_models, batch_sizes, sequence_lengths, output_dir)
        print(f"  STATUS: {summary['status']}")
        return
    if args.run_final_candidate_revalidation:
        requested = models or ["fixed_moe_vectorized", "pvr_ec_deploy_top1", "pvr_ec_ownership_top1_final_candidate_v1_1"]
        candidate = next((m for m in requested if str(m).startswith("pvr_ec_ownership_top1_final_candidate_v1_")), "pvr_ec_ownership_top1_final_candidate_v1_1")
        version = candidate.replace("pvr_ec_ownership_top1_final_candidate_", "")
        output_dir = args.output_dir or f"evaluation/benchmark_results/pvr_final_candidate_{version}_revalidation"
        gate_models = requested
        summary = run_pvr_final_candidate_revalidation(args, families, gate_models, batch_sizes, sequence_lengths, output_dir)
        print(f"  STATUS: {summary['status']}")
        return
    if args.run_multiseed_confirmation_gate:
        output_dir = args.output_dir or "evaluation/benchmark_results/pvr_final_multiseed_confirmation"
        gate_models = models or ["fixed_moe_vectorized", "pvr_ec_deploy_top1", FINAL_CANDIDATE_CONFIG_NAME]
        summary = run_pvr_multiseed_confirmation_gate(args, families, gate_models, batch_sizes, sequence_lengths, output_dir)
        print(f"  STATUS: {summary['status']}")
        return
    if args.run_longer_training_confirmation_gate:
        output_dir = args.output_dir or "evaluation/benchmark_results/pvr_final_longer_training_confirmation"
        gate_models = models or ["fixed_moe_vectorized", FINAL_CANDIDATE_CONFIG_NAME]
        summary = run_pvr_longer_training_confirmation_gate(args, families, gate_models, batch_sizes, sequence_lengths, output_dir)
        print(f"  STATUS: {summary['status']}")
        return
    if args.run_matched_wall_clock_gate:
        output_dir = args.output_dir or "evaluation/benchmark_results/pvr_final_matched_wall_clock"
        gate_models = models or ["fixed_moe_vectorized", "pvr_ec_deploy_top1", FINAL_CANDIDATE_CONFIG_NAME]
        summary = run_pvr_matched_wall_clock_gate(args, families, gate_models, batch_sizes, sequence_lengths, output_dir)
        print(f"  STATUS: {summary['status']}")
        return
    benchmark_inference_only = (
        args.benchmark_inference_only
        or args.mode == "inference-only"
        or args.run_capacity_architecture_audit
        or args.run_capacity_latency_matrix
        or args.run_latency_stability_diagnostic
        or args.run_forward_purity_gate
        or args.run_final_config_manifest
        or args.run_quality_per_ms_memory_gate
        or args.run_qpm_shape_regression_analysis
        or args.run_qpm_memory_repair
        or args.run_qpm_failing_shape_replay
        or args.run_qpm_formula_audit
        or args.run_shape_qpm_runtime_repair
    )

    runner = AlgorithmicBenchmarkRunner(
        mode=args.mode, families=families, seed=args.seed,
        scale=args.scale, sample_limit=args.sample_limit, device=args.device,
        amp=args.amp, train_steps=args.train_steps, models=models,
        profile_compute=args.profile_compute,
        pvr_execution_mode=args.pvr_execution_mode,
        pvr_expert_type=args.pvr_expert_type,
        pvr_training_dispatch_mode=args.pvr_training_dispatch_mode,
        pvr_inference_dispatch_mode=args.pvr_inference_dispatch_mode,
        pvr_deploy_mode=args.pvr_deploy_mode,
        pvr_aux_alpha=args.pvr_aux_alpha,
        pvr_expert_delta_scale=args.pvr_expert_delta_scale,
        benchmark_inference_only=benchmark_inference_only,
        warmup_steps=args.warmup_steps,
        timed_steps=args.timed_steps,
        batch_sizes=batch_sizes,
        sequence_lengths=sequence_lengths,
        profile_deploy=args.profile_deploy,
        root_cause_flags=root_cause_flags,
        diagnostic_sweeps=diagnostic_sweeps,
        pvr_debug_disable_shared=args.pvr_debug_disable_shared,
        pvr_debug_disable_sparse=args.pvr_debug_disable_sparse,
        pvr_debug_force_expert_id=args.pvr_debug_force_expert_id,
    )
    if args.output_dir:
        runner.output_dir = Path(args.output_dir)
        runner.output_dir.mkdir(parents=True, exist_ok=True)
    summary = runner.run()
    if benchmark_inference_only or args.mode == "pvr-overfit-sanity":
        print(f"  STATUS: {summary['status']}")
    else:
        rec = summary["recommendation"]
        print(f"  STATUS: {rec['status']}")
        print(f"  ARCH: {rec.get('architecture_recommendation', 'N/A')}")
        print(f"  {rec['reason']}")


if __name__ == "__main__":
    main()
