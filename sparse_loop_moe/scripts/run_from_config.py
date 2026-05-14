"""Run an experiment from a YAML configuration file.

Usage:
    python scripts/run_from_config.py --config configs/quick_test.yaml
    python scripts/run_from_config.py --config configs/full_experiment.yaml
"""

import argparse
import sys

sys.path.insert(0, "src")

import torch

from sparse_loop_moe.models.full_model import SparseLoopMoEModel
from sparse_loop_moe.training.trainer import Trainer
from sparse_loop_moe.training.data_generation import SyntheticTaskGenerator
from sparse_loop_moe.experiments.config_loader import (
    load_config,
    build_model_config,
    build_trainer_config,
)
from sparse_loop_moe.experiments.metrics import MetricsLogger


def main():
    parser = argparse.ArgumentParser(description="Run Sparse Loop-MoE from config")
    parser.add_argument("--config", type=str, required=True, help="Path to YAML config")
    args = parser.parse_args()

    # Load config
    cfg = load_config(args.config)
    experiment_name = cfg.get("experiment", {}).get("name", "unnamed")
    seed = cfg.get("experiment", {}).get("seed", 42)
    output_dir = cfg.get("experiment", {}).get("output_dir", "results")

    print(f"Experiment: {experiment_name}")
    print(f"Seed: {seed}")
    torch.manual_seed(seed)

    # Build model
    model_config = build_model_config(cfg)
    model = SparseLoopMoEModel(model_config)
    total_params = model.count_parameters()
    print(f"Model parameters: {total_params:,}")

    # Build trainer
    trainer_config = build_trainer_config(cfg)
    data_cfg = cfg.get("data", {})
    task_gen = SyntheticTaskGenerator(
        vocab_size=model_config.vocab_size,
        max_seq_len=model_config.max_seq_len,
        seed=seed,
    )

    trainer = Trainer(model=model, config=trainer_config, task_generator=task_gen)

    # Generate eval samples
    eval_size = data_cfg.get("eval_size", 128)
    eval_samples = task_gen.generate_batch(batch_size=eval_size)

    # Create metrics logger
    logger = MetricsLogger(experiment_name=experiment_name, output_dir=output_dir)

    # Train
    print(f"\nStarting training for {trainer_config.max_steps} steps...")
    print(f"Device: {trainer_config.device}")
    print()

    all_metrics = trainer.train(
        num_steps=trainer_config.max_steps,
        eval_samples=eval_samples,
    )

    # Final evaluation
    final_eval = trainer.evaluate(eval_samples)
    print(f"\nFinal evaluation: {final_eval}")

    # Save metrics
    for m in all_metrics:
        logger.log_step(m)
    logger.log_eval(final_eval)
    logger.save()

    # Print summary
    aggregate = logger.compute_aggregate_metrics()
    print(f"\nAggregate metrics:")
    for key, val in aggregate.to_dict().items():
        if val != 0.0:
            print(f"  {key}: {val:.4f}")


if __name__ == "__main__":
    main()
