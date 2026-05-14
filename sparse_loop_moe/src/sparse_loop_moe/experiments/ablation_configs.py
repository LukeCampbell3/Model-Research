"""Ablation study configurations.

Required ablations:
- remove adaptive expert width
- remove loops
- remove probes
- remove reflection
- remove halting head
- remove anti-spinlock guards
- remove utility threshold
- remove ambiguity signal
- remove risk signal
- remove memory consolidation
- replace learned loop depth with random loop depth
- replace reflection controller with answer-only critic

Most important comparison:
    Sparse Loop-MoE with random loop depth
    vs
    Sparse Loop-MoE with uncertainty/risk/reflection-based loop depth
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from sparse_loop_moe.models.full_model import SparseLoopMoEConfig
from sparse_loop_moe.models.dense_transformer import DenseTransformerConfig
from sparse_loop_moe.core.cognitive_kernel import KernelConstraints


@dataclass
class AblationConfig:
    """Configuration for a single ablation experiment."""

    name: str
    description: str
    model_config: SparseLoopMoEConfig | DenseTransformerConfig
    is_baseline: bool = False
    ablation_type: str = ""  # What was removed/changed


def get_experiment_matrix() -> list[AblationConfig]:
    """Get the full experiment matrix (Phase 9).

    Returns configurations for all model variants to compare:
    1. Dense transformer baseline
    2. Fixed MoE (top-2)
    3. Fixed MoE + shared expert
    4. Adaptive MoE (no loops)
    5. Looped transformer (no MoE)
    6. Sparse Loop-MoE (no probes)
    7. Sparse Loop-MoE + probes
    8. Sparse Loop-MoE + probes + reflection
    9. Full system (probes + reflection + guards + memory)
    """
    configs = []

    # 1. Dense baseline
    configs.append(
        AblationConfig(
            name="dense_baseline",
            description="Dense decoder-only transformer (no MoE, no loops)",
            model_config=DenseTransformerConfig(
                vocab_size=512, d_model=256, n_heads=4, n_layers=4, d_ff=512
            ),
            is_baseline=True,
        )
    )

    # 2. Fixed MoE (top-2, no shared expert)
    configs.append(
        AblationConfig(
            name="fixed_moe_top2",
            description="Fixed top-2 MoE, no shared expert, no loops",
            model_config=SparseLoopMoEConfig(
                use_adaptive_router=False,
                use_probes=False,
                use_reflection=False,
                use_shared_expert=False,
                use_loops=False,
                num_experts=8,
                max_k=2,
            ),
        )
    )

    # 3. Fixed MoE + shared expert
    configs.append(
        AblationConfig(
            name="fixed_moe_shared",
            description="Fixed top-2 MoE with shared expert, no loops",
            model_config=SparseLoopMoEConfig(
                use_adaptive_router=False,
                use_probes=False,
                use_reflection=False,
                use_shared_expert=True,
                use_loops=False,
                num_experts=8,
                max_k=2,
            ),
        )
    )

    # 4. Adaptive MoE (no loops)
    configs.append(
        AblationConfig(
            name="adaptive_moe_no_loops",
            description="Adaptive width MoE, no loops",
            model_config=SparseLoopMoEConfig(
                use_adaptive_router=True,
                use_probes=False,
                use_reflection=False,
                use_shared_expert=True,
                use_loops=False,
                num_experts=8,
                max_k=4,
            ),
            ablation_type="no_loops",
        )
    )

    # 5. Looped transformer (fixed width, with loops)
    configs.append(
        AblationConfig(
            name="looped_fixed_moe",
            description="Fixed top-2 MoE with bounded loops, no probes/reflection",
            model_config=SparseLoopMoEConfig(
                use_adaptive_router=False,
                use_probes=False,
                use_reflection=False,
                use_shared_expert=True,
                use_loops=True,
                num_experts=8,
                max_k=2,
                max_loops=8,
            ),
            ablation_type="fixed_width_loops",
        )
    )

    # 6. Sparse Loop-MoE without probes
    configs.append(
        AblationConfig(
            name="sparse_loop_moe_no_probes",
            description="Adaptive MoE + loops, no probe heads",
            model_config=SparseLoopMoEConfig(
                use_adaptive_router=True,
                use_probes=False,
                use_reflection=False,
                use_shared_expert=True,
                use_loops=True,
                num_experts=8,
                max_k=4,
                max_loops=8,
            ),
            ablation_type="no_probes",
        )
    )

    # 7. Sparse Loop-MoE with probes
    configs.append(
        AblationConfig(
            name="sparse_loop_moe_probes",
            description="Adaptive MoE + loops + probe heads, no reflection",
            model_config=SparseLoopMoEConfig(
                use_adaptive_router=True,
                use_probes=True,
                use_reflection=False,
                use_shared_expert=True,
                use_loops=True,
                num_experts=8,
                max_k=4,
                max_loops=8,
            ),
            ablation_type="no_reflection",
        )
    )

    # 8. Sparse Loop-MoE + probes + reflection
    configs.append(
        AblationConfig(
            name="sparse_loop_moe_reflection",
            description="Adaptive MoE + loops + probes + reflection controller",
            model_config=SparseLoopMoEConfig(
                use_adaptive_router=True,
                use_probes=True,
                use_reflection=True,
                use_shared_expert=True,
                use_loops=True,
                num_experts=8,
                max_k=4,
                max_loops=8,
            ),
        )
    )

    # 9. Full system
    configs.append(
        AblationConfig(
            name="full_sparse_loop_moe",
            description="Full system: adaptive MoE + loops + probes + reflection + guards + memory",
            model_config=SparseLoopMoEConfig(
                use_adaptive_router=True,
                use_probes=True,
                use_reflection=True,
                use_shared_expert=True,
                use_loops=True,
                num_experts=8,
                max_k=4,
                max_loops=8,
                kernel_constraints=KernelConstraints(
                    max_loop_depth=16,
                    oscillation_window=3,
                    oscillation_threshold=0.02,
                    max_consecutive_rollbacks=3,
                ),
            ),
        )
    )

    return configs


def get_ablation_configs() -> list[AblationConfig]:
    """Get specific ablation study configurations.

    These isolate individual components to measure their contribution.
    """
    base = SparseLoopMoEConfig(
        use_adaptive_router=True,
        use_probes=True,
        use_reflection=True,
        use_shared_expert=True,
        use_loops=True,
        num_experts=8,
        max_k=4,
        max_loops=8,
    )

    ablations = []

    # Remove adaptive width (use fixed top-2)
    cfg = SparseLoopMoEConfig(**{**base.__dict__, "use_adaptive_router": False})
    ablations.append(
        AblationConfig(
            name="ablation_no_adaptive_width",
            description="Remove adaptive expert width, use fixed top-2",
            model_config=cfg,
            ablation_type="no_adaptive_width",
        )
    )

    # Remove loops
    cfg = SparseLoopMoEConfig(**{**base.__dict__, "use_loops": False})
    ablations.append(
        AblationConfig(
            name="ablation_no_loops",
            description="Remove bounded loops (single pass)",
            model_config=cfg,
            ablation_type="no_loops",
        )
    )

    # Remove probes
    cfg = SparseLoopMoEConfig(**{**base.__dict__, "use_probes": False})
    ablations.append(
        AblationConfig(
            name="ablation_no_probes",
            description="Remove latent probe heads",
            model_config=cfg,
            ablation_type="no_probes",
        )
    )

    # Remove reflection
    cfg = SparseLoopMoEConfig(**{**base.__dict__, "use_reflection": False})
    ablations.append(
        AblationConfig(
            name="ablation_no_reflection",
            description="Remove self-reflection controller",
            model_config=cfg,
            ablation_type="no_reflection",
        )
    )

    # Remove shared expert
    cfg = SparseLoopMoEConfig(**{**base.__dict__, "use_shared_expert": False})
    ablations.append(
        AblationConfig(
            name="ablation_no_shared_expert",
            description="Remove shared expert",
            model_config=cfg,
            ablation_type="no_shared_expert",
        )
    )

    # Disable anti-spinlock (very high thresholds)
    cfg = SparseLoopMoEConfig(
        **{
            **base.__dict__,
            "kernel_constraints": KernelConstraints(
                oscillation_threshold=999.0,
                max_consecutive_rollbacks=999,
            ),
        }
    )
    ablations.append(
        AblationConfig(
            name="ablation_no_antispinlock",
            description="Disable anti-spinlock guards",
            model_config=cfg,
            ablation_type="no_antispinlock",
        )
    )

    # Remove utility threshold
    cfg = SparseLoopMoEConfig(**{**base.__dict__, "utility_threshold": 0.0})
    ablations.append(
        AblationConfig(
            name="ablation_no_utility_threshold",
            description="Remove utility improvement threshold",
            model_config=cfg,
            ablation_type="no_utility_threshold",
        )
    )

    return ablations


def get_critical_comparison() -> tuple[AblationConfig, AblationConfig]:
    """Get the most important comparison:

    Sparse Loop-MoE with random loop depth
    vs
    Sparse Loop-MoE with uncertainty/risk/reflection-based loop depth

    If adaptive looping does not beat random looping, the controller
    is not learning useful compute allocation.
    """
    # Adaptive (full system)
    adaptive = AblationConfig(
        name="critical_adaptive_loops",
        description="Full Sparse Loop-MoE with learned adaptive loop depth",
        model_config=SparseLoopMoEConfig(
            use_adaptive_router=True,
            use_probes=True,
            use_reflection=True,
            use_shared_expert=True,
            use_loops=True,
            max_loops=8,
        ),
    )

    # Random loop depth (same architecture but random halting)
    random_loops = AblationConfig(
        name="critical_random_loops",
        description="Sparse Loop-MoE with RANDOM loop depth (control)",
        model_config=SparseLoopMoEConfig(
            use_adaptive_router=True,
            use_probes=True,
            use_reflection=False,  # No reflection = no learned halting
            use_shared_expert=True,
            use_loops=True,
            max_loops=8,
            # Will need custom training that randomizes loop count
        ),
        ablation_type="random_loop_depth",
    )

    return adaptive, random_loops
