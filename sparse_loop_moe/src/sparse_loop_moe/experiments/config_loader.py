"""Configuration loader for YAML experiment configs."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from sparse_loop_moe.models.full_model import SparseLoopMoEConfig
from sparse_loop_moe.models.dense_transformer import DenseTransformerConfig
from sparse_loop_moe.core.cognitive_kernel import KernelConstraints
from sparse_loop_moe.training.trainer import TrainerConfig
from sparse_loop_moe.training.losses import LossWeights


def load_config(config_path: str | Path) -> dict[str, Any]:
    """Load a YAML configuration file."""
    with open(config_path, "r") as f:
        return yaml.safe_load(f)


def build_model_config(cfg: dict[str, Any]) -> SparseLoopMoEConfig:
    """Build a SparseLoopMoEConfig from a config dictionary."""
    model_cfg = cfg.get("model", {})
    kernel_cfg = cfg.get("kernel", {})

    kernel_constraints = KernelConstraints(
        max_loop_depth=kernel_cfg.get("max_loop_depth", 16),
        max_experts_per_token=kernel_cfg.get("max_experts_per_token", 6),
        min_utility_threshold=kernel_cfg.get("min_utility_threshold", 0.01),
        max_compute_budget_multiplier=kernel_cfg.get("max_compute_budget_multiplier", 4.0),
        oscillation_window=kernel_cfg.get("oscillation_window", 3),
        oscillation_threshold=kernel_cfg.get("oscillation_threshold", 0.02),
        max_consecutive_rollbacks=kernel_cfg.get("max_consecutive_rollbacks", 3),
        max_reflection_depth=kernel_cfg.get("max_reflection_depth", 4),
        reflection_must_improve=kernel_cfg.get("reflection_must_improve", True),
        min_reflection_improvement=kernel_cfg.get("min_reflection_improvement", 0.005),
    )

    return SparseLoopMoEConfig(
        vocab_size=model_cfg.get("vocab_size", 512),
        d_model=model_cfg.get("d_model", 256),
        max_seq_len=model_cfg.get("max_seq_len", 256),
        n_layers=model_cfg.get("n_layers", 4),
        n_heads=model_cfg.get("n_heads", 4),
        d_ff=model_cfg.get("d_ff", 512),
        num_experts=model_cfg.get("num_experts", 8),
        max_k=model_cfg.get("max_k", 4),
        max_loops=model_cfg.get("max_loops", 8),
        use_adaptive_router=model_cfg.get("use_adaptive_router", True),
        use_probes=model_cfg.get("use_probes", True),
        use_reflection=model_cfg.get("use_reflection", True),
        use_shared_expert=model_cfg.get("use_shared_expert", True),
        use_loops=model_cfg.get("use_loops", True),
        delta_threshold=model_cfg.get("delta_threshold", 0.01),
        utility_threshold=model_cfg.get("utility_threshold", 0.005),
        dropout=model_cfg.get("dropout", 0.1),
        tie_weights=model_cfg.get("tie_weights", True),
        kernel_constraints=kernel_constraints,
    )


def build_trainer_config(cfg: dict[str, Any]) -> TrainerConfig:
    """Build a TrainerConfig from a config dictionary."""
    train_cfg = cfg.get("training", {})
    loss_cfg = train_cfg.get("loss_weights", {})

    loss_weights = LossWeights(
        lambda_balance=loss_cfg.get("lambda_balance", 0.01),
        lambda_compute=loss_cfg.get("lambda_compute", 0.001),
        lambda_probe=loss_cfg.get("lambda_probe", 0.1),
        lambda_halt=loss_cfg.get("lambda_halt", 0.05),
        lambda_reflection=loss_cfg.get("lambda_reflection", 0.05),
        lambda_consistency=loss_cfg.get("lambda_consistency", 0.01),
        lambda_revision=loss_cfg.get("lambda_revision", 0.05),
    )

    device = cfg.get("experiment", {}).get("device", "auto")
    if device == "auto":
        import torch
        device = "cuda" if torch.cuda.is_available() else "cpu"

    return TrainerConfig(
        learning_rate=train_cfg.get("learning_rate", 3e-4),
        weight_decay=train_cfg.get("weight_decay", 0.01),
        max_grad_norm=train_cfg.get("max_grad_norm", 1.0),
        warmup_steps=train_cfg.get("warmup_steps", 100),
        max_steps=train_cfg.get("max_steps", 10000),
        batch_size=train_cfg.get("batch_size", 32),
        log_interval=train_cfg.get("log_interval", 50),
        eval_interval=train_cfg.get("eval_interval", 500),
        save_interval=train_cfg.get("save_interval", 1000),
        loss_weights=loss_weights,
        device=device,
    )
