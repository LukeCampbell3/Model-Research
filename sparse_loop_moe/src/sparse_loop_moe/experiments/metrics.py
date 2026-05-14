"""Metrics tracking and logging for experiments.

Tracks:
- Task metrics: accuracy, exact match, pass@1, validation pass rate
- Compute metrics: FLOPs/sample, active experts/token, loops/sample, quality-per-compute
- Routing metrics: entropy, utilization, dead experts, load imbalance, route regret
- Loop metrics: avg loops, halt accuracy, spinlock rate, oscillation rate
- Reflection metrics: trigger accuracy, revision success, bad revision rate

Core metric:
    risk_adjusted_quality_per_compute = validated_success * risk_reduction / active_compute

Also tracks:
    reflection_value = (performance_after - performance_before) / extra_compute_used
"""

from __future__ import annotations

import json
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import torch

from sparse_loop_moe.core.types import LoopStats, RouterMetrics


@dataclass
class ExperimentMetrics:
    """Aggregated metrics for an experiment run."""

    # Task metrics
    accuracy: float = 0.0
    exact_match: float = 0.0
    pass_at_1: float = 0.0
    validation_pass_rate: float = 0.0
    constraint_satisfaction_rate: float = 0.0

    # Compute metrics
    flops_per_sample: float = 0.0
    active_experts_per_token: float = 0.0
    loops_per_sample: float = 0.0
    latency_ms: float = 0.0
    tokens_per_sec: float = 0.0
    quality_per_compute: float = 0.0

    # Routing metrics
    routing_entropy: float = 0.0
    expert_utilization: float = 0.0
    dead_expert_count: float = 0.0
    load_imbalance: float = 0.0
    expert_overlap: float = 0.0
    route_regret: float = 0.0

    # Loop metrics
    avg_loops_used: float = 0.0
    halt_accuracy: float = 0.0
    unnecessary_loop_rate: float = 0.0
    spinlock_rate: float = 0.0
    oscillation_rate: float = 0.0
    progress_per_loop: float = 0.0
    rollback_success_rate: float = 0.0

    # Reflection metrics
    reflection_trigger_accuracy: float = 0.0
    revision_success_rate: float = 0.0
    bad_revision_rate: float = 0.0
    early_wrong_commitment_reduction: float = 0.0
    hidden_constraint_discovery_rate: float = 0.0
    validation_before_commit_rate: float = 0.0

    # Core composite metrics
    risk_adjusted_quality_per_compute: float = 0.0
    reflection_value: float = 0.0

    def to_dict(self) -> dict[str, float]:
        """Convert to dictionary."""
        return {
            k: v for k, v in self.__dict__.items() if isinstance(v, (int, float))
        }


class MetricsLogger:
    """Logs and aggregates metrics across training and evaluation.

    Supports:
    - Per-step metric recording
    - Windowed averages
    - Experiment comparison
    - JSON export
    """

    def __init__(self, experiment_name: str, output_dir: str = "results"):
        self.experiment_name = experiment_name
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.step_metrics: list[dict[str, float]] = []
        self.eval_metrics: list[dict[str, float]] = []
        self.loop_stats_history: list[list[LoopStats]] = []
        self.start_time = time.time()

    def log_step(self, metrics: dict[str, float]) -> None:
        """Log metrics for a single training step."""
        metrics["timestamp"] = time.time() - self.start_time
        self.step_metrics.append(metrics)

    def log_eval(self, metrics: dict[str, float]) -> None:
        """Log evaluation metrics."""
        metrics["timestamp"] = time.time() - self.start_time
        self.eval_metrics.append(metrics)

    def log_loop_stats(self, stats: list[LoopStats]) -> None:
        """Log loop statistics from a forward pass."""
        self.loop_stats_history.append(stats)

    def compute_aggregate_metrics(
        self, window: int = 100
    ) -> ExperimentMetrics:
        """Compute aggregate metrics over recent history."""
        metrics = ExperimentMetrics()

        if not self.step_metrics:
            return metrics

        recent = self.step_metrics[-window:]

        # Task metrics from eval
        if self.eval_metrics:
            last_eval = self.eval_metrics[-1]
            metrics.accuracy = last_eval.get("eval/accuracy", 0.0)

        # Compute metrics from step history
        if recent:
            metrics.quality_per_compute = self._compute_quality_per_compute(recent)

        # Loop metrics from stats history
        if self.loop_stats_history:
            recent_stats = self.loop_stats_history[-window:]
            metrics.avg_loops_used = self._avg_loops(recent_stats)
            metrics.spinlock_rate = self._spinlock_rate(recent_stats)
            metrics.oscillation_rate = self._oscillation_rate(recent_stats)
            metrics.rollback_success_rate = self._rollback_rate(recent_stats)

        # Core metric
        metrics.risk_adjusted_quality_per_compute = (
            metrics.accuracy * (1.0 - metrics.spinlock_rate)
            / max(metrics.avg_loops_used * metrics.active_experts_per_token, 0.1)
        )

        return metrics

    def _compute_quality_per_compute(
        self, recent: list[dict[str, float]]
    ) -> float:
        """Compute quality-per-compute ratio."""
        avg_loss = sum(m.get("task_loss", 1.0) for m in recent) / len(recent)
        avg_compute = sum(m.get("loops/total", 1.0) for m in recent) / len(recent)
        # Quality = 1 - normalized_loss, compute = loops used
        quality = max(1.0 - avg_loss, 0.0)
        return quality / max(avg_compute, 0.1)

    def _avg_loops(self, stats_history: list[list[LoopStats]]) -> float:
        """Average loops used across all blocks and samples."""
        total = 0
        count = 0
        for stats_list in stats_history:
            for s in stats_list:
                total += s.loops_used
                count += 1
        return total / max(count, 1)

    def _spinlock_rate(self, stats_history: list[list[LoopStats]]) -> float:
        """Rate of spinlock detection (oscillation without progress)."""
        spinlocks = 0
        total = 0
        for stats_list in stats_history:
            for s in stats_list:
                total += 1
                if s.oscillation_detected:
                    spinlocks += 1
        return spinlocks / max(total, 1)

    def _oscillation_rate(self, stats_history: list[list[LoopStats]]) -> float:
        """Rate of oscillation detection."""
        return self._spinlock_rate(stats_history)  # Same metric currently

    def _rollback_rate(self, stats_history: list[list[LoopStats]]) -> float:
        """Rate of rollbacks."""
        rollbacks = 0
        total_loops = 0
        for stats_list in stats_history:
            for s in stats_list:
                rollbacks += s.rollback_count
                total_loops += s.loops_used
        return rollbacks / max(total_loops, 1)

    def save(self) -> None:
        """Save all metrics to disk."""
        output = {
            "experiment_name": self.experiment_name,
            "total_steps": len(self.step_metrics),
            "total_time_seconds": time.time() - self.start_time,
            "final_metrics": self.compute_aggregate_metrics().to_dict(),
            "step_metrics": self.step_metrics[-100:],  # Last 100 steps
            "eval_metrics": self.eval_metrics,
        }

        output_path = self.output_dir / f"{self.experiment_name}.json"
        with open(output_path, "w") as f:
            json.dump(output, f, indent=2, default=str)

    def compare_with(
        self, other: "MetricsLogger"
    ) -> dict[str, dict[str, float]]:
        """Compare metrics with another experiment."""
        self_metrics = self.compute_aggregate_metrics()
        other_metrics = other.compute_aggregate_metrics()

        comparison = {}
        self_dict = self_metrics.to_dict()
        other_dict = other_metrics.to_dict()

        for key in self_dict:
            if key in other_dict:
                diff = self_dict[key] - other_dict[key]
                pct = diff / max(abs(other_dict[key]), 1e-8) * 100
                comparison[key] = {
                    "self": self_dict[key],
                    "other": other_dict[key],
                    "diff": diff,
                    "pct_change": pct,
                }

        return comparison
