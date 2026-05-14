"""Experiment runner: orchestrates training, evaluation, and comparison.

Supports running the full experiment matrix (Phase 9) with:
- Multiple model configurations
- Ablation studies
- Metric comparison
- Result aggregation
"""

from __future__ import annotations

import argparse
import json
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import torch

from sparse_loop_moe.models.dense_transformer import DenseTransformer, DenseTransformerConfig
from sparse_loop_moe.models.full_model import SparseLoopMoEModel, SparseLoopMoEConfig
from sparse_loop_moe.training.trainer import Trainer, TrainerConfig
from sparse_loop_moe.training.data_generation import SyntheticTaskGenerator
from sparse_loop_moe.experiments.metrics import MetricsLogger, ExperimentMetrics
from sparse_loop_moe.experiments.ablation_configs import (
    AblationConfig,
    get_experiment_matrix,
    get_ablation_configs,
    get_critical_comparison,
)


@dataclass
class ExperimentResult:
    """Result from a single experiment run."""

    config_name: str
    metrics: ExperimentMetrics
    training_time_seconds: float
    total_parameters: int
    final_loss: float


class ExperimentRunner:
    """Orchestrates the full experiment matrix.

    Runs all model configurations, collects metrics, and produces
    comparison reports.
    """

    def __init__(
        self,
        output_dir: str = "results",
        device: str | None = None,
        seed: int = 42,
    ):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.seed = seed
        self.results: list[ExperimentResult] = []

    def run_single(
        self,
        config: AblationConfig,
        num_steps: int = 2000,
        batch_size: int = 32,
        eval_every: int = 500,
    ) -> ExperimentResult:
        """Run a single experiment configuration.

        Args:
            config: Ablation/experiment configuration
            num_steps: Training steps
            batch_size: Batch size
            eval_every: Evaluation frequency

        Returns:
            ExperimentResult with final metrics
        """
        print(f"\n{'='*60}")
        print(f"Running: {config.name}")
        print(f"Description: {config.description}")
        print(f"{'='*60}\n")

        # Set seed for reproducibility
        torch.manual_seed(self.seed)

        # Create model
        if isinstance(config.model_config, DenseTransformerConfig):
            model = DenseTransformer(config.model_config)
        else:
            model = SparseLoopMoEModel(config.model_config)

        total_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
        print(f"Total parameters: {total_params:,}")

        # Create data generator
        task_gen = SyntheticTaskGenerator(
            vocab_size=config.model_config.vocab_size
            if hasattr(config.model_config, "vocab_size")
            else 512,
            seed=self.seed,
        )

        # Create trainer
        trainer_config = TrainerConfig(
            learning_rate=3e-4,
            max_steps=num_steps,
            batch_size=batch_size,
            eval_interval=eval_every,
            log_interval=100,
            device=self.device,
        )
        trainer = Trainer(model=model, config=trainer_config, task_generator=task_gen)

        # Create eval samples
        eval_samples = task_gen.generate_batch(batch_size=128)

        # Create metrics logger
        logger = MetricsLogger(
            experiment_name=config.name,
            output_dir=str(self.output_dir),
        )

        # Train
        start_time = time.time()
        all_metrics = trainer.train(num_steps=num_steps, eval_samples=eval_samples)
        training_time = time.time() - start_time

        # Final evaluation
        final_eval = trainer.evaluate(eval_samples)
        print(f"\nFinal eval: {final_eval}")

        # Log metrics
        for m in all_metrics:
            logger.log_step(m)
        logger.log_eval(final_eval)
        logger.save()

        # Build result
        aggregate = logger.compute_aggregate_metrics()
        result = ExperimentResult(
            config_name=config.name,
            metrics=aggregate,
            training_time_seconds=training_time,
            total_parameters=total_params,
            final_loss=final_eval.get("eval/loss", float("inf")),
        )

        self.results.append(result)
        return result

    def run_experiment_matrix(
        self, num_steps: int = 2000, batch_size: int = 32
    ) -> list[ExperimentResult]:
        """Run the full experiment matrix (Phase 9)."""
        configs = get_experiment_matrix()
        results = []

        for config in configs:
            result = self.run_single(config, num_steps=num_steps, batch_size=batch_size)
            results.append(result)

        self._save_comparison(results, "experiment_matrix")
        return results

    def run_ablation_study(
        self, num_steps: int = 2000, batch_size: int = 32
    ) -> list[ExperimentResult]:
        """Run all ablation studies."""
        configs = get_ablation_configs()
        results = []

        for config in configs:
            result = self.run_single(config, num_steps=num_steps, batch_size=batch_size)
            results.append(result)

        self._save_comparison(results, "ablation_study")
        return results

    def run_critical_comparison(
        self, num_steps: int = 3000, batch_size: int = 32
    ) -> tuple[ExperimentResult, ExperimentResult]:
        """Run the most important comparison:
        Adaptive loop depth vs Random loop depth.

        If adaptive doesn't beat random, the controller isn't learning.
        """
        adaptive_config, random_config = get_critical_comparison()

        adaptive_result = self.run_single(
            adaptive_config, num_steps=num_steps, batch_size=batch_size
        )
        random_result = self.run_single(
            random_config, num_steps=num_steps, batch_size=batch_size
        )

        # Compare
        comparison = {
            "adaptive": adaptive_result.metrics.to_dict(),
            "random": random_result.metrics.to_dict(),
            "adaptive_wins": {},
        }

        adaptive_dict = adaptive_result.metrics.to_dict()
        random_dict = random_result.metrics.to_dict()

        for key in adaptive_dict:
            if key in random_dict:
                diff = adaptive_dict[key] - random_dict[key]
                comparison["adaptive_wins"][key] = diff > 0

        output_path = self.output_dir / "critical_comparison.json"
        with open(output_path, "w") as f:
            json.dump(comparison, f, indent=2)

        print(f"\n{'='*60}")
        print("CRITICAL COMPARISON: Adaptive vs Random Loop Depth")
        print(f"{'='*60}")
        print(f"Adaptive accuracy: {adaptive_result.metrics.accuracy:.4f}")
        print(f"Random accuracy:   {random_result.metrics.accuracy:.4f}")
        print(f"Adaptive QPC:      {adaptive_result.metrics.quality_per_compute:.4f}")
        print(f"Random QPC:        {random_result.metrics.quality_per_compute:.4f}")
        print(f"{'='*60}\n")

        return adaptive_result, random_result

    def _save_comparison(
        self, results: list[ExperimentResult], name: str
    ) -> None:
        """Save comparison report."""
        report = {
            "name": name,
            "num_experiments": len(results),
            "results": [],
        }

        for r in results:
            report["results"].append(
                {
                    "config_name": r.config_name,
                    "total_parameters": r.total_parameters,
                    "training_time_seconds": r.training_time_seconds,
                    "final_loss": r.final_loss,
                    "metrics": r.metrics.to_dict(),
                }
            )

        output_path = self.output_dir / f"{name}_report.json"
        with open(output_path, "w") as f:
            json.dump(report, f, indent=2)

        print(f"\nComparison report saved to: {output_path}")

    def print_summary(self) -> None:
        """Print a summary table of all results."""
        if not self.results:
            print("No results to summarize.")
            return

        print(f"\n{'='*80}")
        print(f"{'EXPERIMENT SUMMARY':^80}")
        print(f"{'='*80}")
        print(
            f"{'Config':<35} {'Params':>10} {'Loss':>8} "
            f"{'Acc':>8} {'QPC':>8} {'Loops':>6}"
        )
        print("-" * 80)

        for r in self.results:
            print(
                f"{r.config_name:<35} {r.total_parameters:>10,} "
                f"{r.final_loss:>8.4f} {r.metrics.accuracy:>8.4f} "
                f"{r.metrics.quality_per_compute:>8.4f} "
                f"{r.metrics.avg_loops_used:>6.1f}"
            )

        print(f"{'='*80}\n")


def main():
    """Main entry point for running experiments."""
    parser = argparse.ArgumentParser(description="Sparse Loop-MoE Experiment Runner")
    parser.add_argument(
        "--mode",
        choices=["matrix", "ablation", "critical", "quick"],
        default="quick",
        help="Experiment mode",
    )
    parser.add_argument("--steps", type=int, default=2000, help="Training steps")
    parser.add_argument("--batch-size", type=int, default=32, help="Batch size")
    parser.add_argument("--output-dir", type=str, default="results", help="Output directory")
    parser.add_argument("--device", type=str, default=None, help="Device (cuda/cpu)")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")

    args = parser.parse_args()

    runner = ExperimentRunner(
        output_dir=args.output_dir,
        device=args.device,
        seed=args.seed,
    )

    if args.mode == "quick":
        # Quick test: just run dense baseline and full model
        configs = get_experiment_matrix()
        # Run first (dense) and last (full)
        runner.run_single(configs[0], num_steps=min(args.steps, 500), batch_size=args.batch_size)
        runner.run_single(configs[-1], num_steps=min(args.steps, 500), batch_size=args.batch_size)
    elif args.mode == "matrix":
        runner.run_experiment_matrix(num_steps=args.steps, batch_size=args.batch_size)
    elif args.mode == "ablation":
        runner.run_ablation_study(num_steps=args.steps, batch_size=args.batch_size)
    elif args.mode == "critical":
        runner.run_critical_comparison(num_steps=args.steps, batch_size=args.batch_size)

    runner.print_summary()


if __name__ == "__main__":
    main()
