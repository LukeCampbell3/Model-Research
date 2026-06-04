"""Benchmark evaluation pipeline for the Sparse Loop-MoE research testbed.

This system uses tiny models (128-256 dim, 256-512 vocab) with custom token
encoding for synthetic algorithmic tasks. It CANNOT process natural language.

The benchmark evaluates architectural innovations by comparing model variants
on controlled synthetic tasks with automatic ground truth.

For real NLP benchmarks (ARC, GSM8K, HellaSwag), the model interface would need:
- A real tokenizer (BPE/SentencePiece, 32K+ vocab)
- Scaled model (10M+ params)
- Text generation / multiple-choice scoring
- Input formatting for each benchmark

Usage:
    python evaluation/run_benchmarks.py --mode smoke
    python evaluation/run_benchmarks.py --mode benchmark-lite
    python evaluation/run_benchmarks.py --mode benchmark-lite --attempt-real-datasets
"""

import argparse
import csv
import hashlib
import json
import platform
import sys
import time
import traceback
from datetime import datetime
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import Optional

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "sparse_loop_moe" / "src"))

import torch
import numpy as np
import yaml

from sparse_loop_moe.models.dense_transformer import DenseTransformer, DenseTransformerConfig
from sparse_loop_moe.models.full_model import SparseLoopMoEModel, SparseLoopMoEConfig
from sparse_loop_moe.training.trainer import Trainer, TrainerConfig
from sparse_loop_moe.training.data_generation import SyntheticTaskGenerator, TaskSample
from sparse_loop_moe.core.types import LoopStats


# =============================================================================
# Result Schemas
# =============================================================================

@dataclass
class ModelResult:
    run_id: str
    model_name: str
    dataset: str
    dataset_type: str  # "synthetic" or "real"
    difficulty: str
    split: str = "eval"
    sample_count: int = 0
    accuracy: float = 0.0
    loss: float = 0.0
    avg_loops: float = 1.0
    avg_experts: float = 1.0
    halt_rate: float = 0.0
    oscillation_rate: float = 0.0
    quality_per_compute: float = 0.0
    training_time_seconds: float = 0.0
    inference_time_seconds: float = 0.0
    total_parameters: int = 0
    error: str = ""
    seed: int = 42


@dataclass
class ComparisonResult:
    model_a: str
    model_b: str
    dataset: str
    metric: str
    value_a: float
    value_b: float
    absolute_delta: float
    relative_delta_pct: float
    a_wins: bool


# =============================================================================
# Real Dataset Interface Check
# =============================================================================

class RealDatasetChecker:
    """Check whether the model can interface with real NLP benchmarks."""

    REQUIRED_REAL_DATASETS = ["arc_challenge", "gsm8k", "hellaswag"]

    @staticmethod
    def check_model_interface_compatibility() -> dict:
        """Check if current model architecture can consume real NLP datasets.

        Returns a compatibility report.
        """
        issues = []

        # Check 1: Vocabulary
        # The model uses vocab_size=256-512 with custom digit/operator tokens.
        # Real datasets need 32K+ vocab with BPE tokenization.
        issues.append(
            "VOCAB_TOO_SMALL: Model uses vocab_size=256-512 (custom digit/operator encoding). "
            "Real NLP benchmarks require 32K+ vocabulary with BPE/SentencePiece tokenizer."
        )

        # Check 2: Tokenizer
        # No real tokenizer exists. Input is encoded as digit tokens + operator tokens.
        issues.append(
            "NO_TEXT_TOKENIZER: Model has no text tokenizer. Input is encoded as "
            "custom integer sequences (digits=4-13, operators=14+). Cannot encode English text."
        )

        # Check 3: Task format
        # Model is trained on next-token prediction of synthetic sequences.
        # It cannot do multiple-choice scoring or free-form text generation.
        issues.append(
            "INCOMPATIBLE_TASK_FORMAT: Model is trained for next-token prediction on synthetic "
            "algorithmic sequences. Cannot perform multiple-choice scoring (ARC, HellaSwag) "
            "or free-form math answer generation (GSM8K)."
        )

        # Check 4: Model scale
        # 128-256 dim, 2-4 layers. Far too small for language understanding.
        issues.append(
            "MODEL_TOO_SMALL: 128-256 hidden dim, 2-4 layers, 300K-1.1M params. "
            "Minimum for language tasks is ~10M params with real pretraining."
        )

        return {
            "compatible": False,
            "issues": issues,
            "required_for_real_benchmarks": [
                "Add BPE/SentencePiece tokenizer with 32K+ vocab",
                "Scale model to at least 10M parameters",
                "Add multiple-choice scoring head for ARC/HellaSwag",
                "Add chain-of-thought + answer extraction for GSM8K",
                "Pretrain on natural language corpus",
                "Add text generation (autoregressive decoding) loop",
            ],
            "what_can_be_evaluated": [
                "Architecture comparison on synthetic algorithmic tasks",
                "Adaptive routing vs fixed routing (same synthetic data)",
                "Looping vs single-pass (same synthetic data)",
                "Probe/reflection benefit (same synthetic data)",
                "Quality-per-compute ratio across variants",
            ],
        }

    @staticmethod
    def attempt_real_dataset_load(dataset_name: str) -> dict:
        """Attempt to load a real dataset and report what happens."""
        result = {
            "dataset": dataset_name,
            "loaded": False,
            "error": "",
            "reason": "",
        }

        try:
            # Try importing datasets library
            import datasets as hf_datasets
            # Attempt download
            if dataset_name == "arc_challenge":
                ds = hf_datasets.load_dataset("allenai/ai2_arc", "ARC-Challenge", split="test", streaming=True)
                sample = next(iter(ds))
                result["loaded"] = True
                result["sample_keys"] = list(sample.keys())
                result["reason"] = "Dataset accessible but model cannot process text input"
            elif dataset_name == "gsm8k":
                ds = hf_datasets.load_dataset("openai/gsm8k", "main", split="test", streaming=True)
                sample = next(iter(ds))
                result["loaded"] = True
                result["sample_keys"] = list(sample.keys())
                result["reason"] = "Dataset accessible but model cannot process text input"
            elif dataset_name == "hellaswag":
                ds = hf_datasets.load_dataset("Rowan/hellaswag", split="validation", streaming=True)
                sample = next(iter(ds))
                result["loaded"] = True
                result["sample_keys"] = list(sample.keys())
                result["reason"] = "Dataset accessible but model cannot process text input"
        except ImportError:
            result["error"] = "DATASET_LIBRARY_NOT_INSTALLED"
            result["reason"] = "pip install datasets required"
        except Exception as e:
            result["error"] = f"DATASET_DOWNLOAD_FAILED: {type(e).__name__}: {str(e)[:200]}"
            result["reason"] = str(e)[:200]

        return result


# =============================================================================
# Core Benchmark Runner
# =============================================================================

class BenchmarkRunner:
    """Runs architecture comparison benchmark on synthetic tasks."""

    def __init__(self, config_path: str, mode: str = "smoke", attempt_real: bool = False):
        with open(config_path, "r") as f:
            self.config = yaml.safe_load(f)

        self.mode = mode
        self.attempt_real = attempt_real
        self.seed = self.config["benchmark"]["seed"]
        self.device = self.config["benchmark"].get("device", "cpu")
        if self.device == "auto":
            self.device = "cuda" if torch.cuda.is_available() else "cpu"

        self.output_dir = Path(self.config["benchmark"]["output_dir"])
        self.output_dir.mkdir(parents=True, exist_ok=True)

        training_cfg = self.config["training"]
        if mode == "smoke":
            self.num_steps = training_cfg["steps_smoke"]
        elif mode == "benchmark-lite":
            self.num_steps = training_cfg["steps_lite"]
        else:
            self.num_steps = training_cfg["steps_full"]

        self.batch_size = training_cfg["batch_size"]
        self.results: list[ModelResult] = []
        self.failures: list[dict] = []
        self.run_id = f"run_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}_{mode}"

    def run(self) -> dict:
        """Execute the full benchmark."""
        print(f"{'='*70}")
        print(f"  SPARSE LOOP-MOE ARCHITECTURE BENCHMARK")
        print(f"  Mode: {self.mode} | Steps: {self.num_steps} | Device: {self.device}")
        print(f"  Run ID: {self.run_id}")
        print(f"  CUDA: {torch.cuda.is_available()} | Torch: {torch.__version__}")
        print(f"{'='*70}\n")

        start_time = time.time()

        # Step 1: Check real dataset compatibility
        interface_check = RealDatasetChecker.check_model_interface_compatibility()
        real_dataset_results = []
        if self.attempt_real:
            print("  Attempting real dataset access...")
            for ds_name in RealDatasetChecker.REQUIRED_REAL_DATASETS:
                result = RealDatasetChecker.attempt_real_dataset_load(ds_name)
                real_dataset_results.append(result)
                status = "OK (accessible)" if result["loaded"] else f"FAILED: {result['error']}"
                print(f"    {ds_name}: {status}")
            print()

        # Step 2: Train and evaluate model variants on synthetic tasks
        model_configs = self.config["models"]
        for model_name, model_cfg in model_configs.items():
            print(f"\n{'-'*70}")
            print(f"  Model: {model_name} | {model_cfg['description']}")
            print(f"{'-'*70}")

            try:
                model_results = self._train_and_evaluate(model_name, model_cfg)
                self.results.extend(model_results)
            except Exception as e:
                error_msg = f"{type(e).__name__}: {str(e)}"
                print(f"  FAILED: {error_msg}")
                self.failures.append({
                    "model": model_name,
                    "error": error_msg,
                    "traceback": traceback.format_exc(),
                })
                self.results.append(ModelResult(
                    run_id=self.run_id,
                    model_name=model_name,
                    dataset="ALL_FAILED",
                    dataset_type="synthetic",
                    difficulty="unknown",
                    error=error_msg,
                ))

        total_time = time.time() - start_time

        # Step 3: Validate results
        valid_results = [r for r in self.results if not r.error and r.sample_count > 0]

        # Step 4: Generate outputs
        self._save_raw_results()
        comparisons = self._compute_comparisons(valid_results)
        self._save_comparisons(comparisons)
        summary = self._generate_summary(valid_results, comparisons, total_time, interface_check, real_dataset_results)
        self._save_summary(summary)
        self._save_failure_analysis(interface_check, real_dataset_results)
        self._save_reproducibility_manifest(total_time)
        self._generate_report(summary, comparisons, interface_check)

        print(f"\n{'='*70}")
        print(f"  BENCHMARK COMPLETE | {total_time:.1f}s | {len(valid_results)} valid results")
        print(f"  Output: {self.output_dir}")
        print(f"{'='*70}\n")

        return summary

    def _train_and_evaluate(self, model_name: str, model_cfg: dict) -> list[ModelResult]:
        """Train one model variant and evaluate on all synthetic datasets."""
        results = []
        torch.manual_seed(self.seed)
        np.random.seed(self.seed)

        # Build model
        model_base = self.config["model_base"]
        if model_cfg["type"] == "dense":
            model = DenseTransformer(DenseTransformerConfig(
                vocab_size=model_base["vocab_size"],
                d_model=model_base["d_model"],
                n_heads=model_base["n_heads"],
                n_layers=model_base["n_layers"],
                d_ff=model_base["d_ff"],
                max_seq_len=model_base["max_seq_len"],
                dropout=model_base["dropout"],
            ))
        else:
            overrides = model_cfg.get("config_overrides", {})
            model = SparseLoopMoEModel(SparseLoopMoEConfig(
                vocab_size=model_base["vocab_size"],
                d_model=model_base["d_model"],
                n_heads=model_base["n_heads"],
                n_layers=model_base["n_layers"],
                d_ff=model_base["d_ff"],
                max_seq_len=model_base["max_seq_len"],
                num_experts=model_base["num_experts"],
                dropout=model_base["dropout"],
                **overrides,
            ))

        total_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
        assert total_params > 0, f"Model {model_name} has 0 parameters"
        print(f"  Params: {total_params:,}")

        # Train
        task_gen = SyntheticTaskGenerator(
            vocab_size=model_base["vocab_size"],
            max_seq_len=model_base["max_seq_len"],
            seed=self.seed,
        )
        warmup = max(1, min(self.config["training"]["warmup_steps"], self.num_steps // 5))
        trainer_config = TrainerConfig(
            learning_rate=self.config["training"]["learning_rate"],
            weight_decay=self.config["training"]["weight_decay"],
            warmup_steps=warmup,
            max_steps=self.num_steps,
            batch_size=self.batch_size,
            eval_interval=self.num_steps + 1,  # No mid-train eval
            log_interval=max(self.num_steps // 3, 1),
            device=self.device,
        )
        trainer = Trainer(model=model, config=trainer_config, task_generator=task_gen)

        t0 = time.time()
        trainer.train(num_steps=self.num_steps)
        train_time = time.time() - t0
        print(f"  Trained: {train_time:.1f}s")

        # Evaluate per-dataset
        datasets = self.config["datasets"]
        for ds_name, ds_cfg in datasets.items():
            if ds_name == "mixed_training":
                continue
            samples = self._generate_eval_samples(ds_cfg)
            assert len(samples) > 0, f"Dataset {ds_name} generated 0 samples"

            t1 = time.time()
            result = self._evaluate(model, samples, model_name, ds_name, ds_cfg)
            result.training_time_seconds = train_time
            result.inference_time_seconds = time.time() - t1
            result.total_parameters = total_params
            result.seed = self.seed
            results.append(result)

            print(f"    {ds_name:20s} | n={result.sample_count:3d} | acc={result.accuracy:.4f} | "
                  f"loss={result.loss:.3f} | loops={result.avg_loops:.1f} | qpc={result.quality_per_compute:.4f}")

        return results

    def _generate_eval_samples(self, ds_cfg: dict) -> list[TaskSample]:
        """Generate deterministic eval samples for a dataset config."""
        eval_gen = SyntheticTaskGenerator(
            vocab_size=self.config["model_base"]["vocab_size"],
            max_seq_len=self.config["model_base"]["max_seq_len"],
            seed=self.seed + 9999,
        )
        count = ds_cfg["sample_count"]
        if self.mode == "smoke":
            count = min(count, 32)
        elif self.mode == "benchmark-lite":
            count = min(count, 256)

        task_type = ds_cfg["task_type"]
        params = ds_cfg.get("params", {})
        samples = []
        for _ in range(count):
            if task_type == "addition":
                samples.append(eval_gen.generate_addition_task(**params))
            elif task_type == "sorting":
                samples.append(eval_gen.generate_sorting_task(**params))
            elif task_type == "parentheses":
                samples.append(eval_gen.generate_parentheses_task(**params))
            elif task_type == "multi_hop":
                samples.append(eval_gen.generate_multi_hop_lookup(**params))
            elif task_type == "hidden_constraint":
                samples.append(eval_gen.generate_hidden_constraint_task())
            else:
                samples.append(eval_gen.generate_addition_task())
        return samples

    def _evaluate(self, model, samples: list[TaskSample], model_name: str, ds_name: str, ds_cfg: dict) -> ModelResult:
        """Evaluate trained model on samples."""
        model.eval()
        device = torch.device(self.device)

        total_correct = 0
        total_tokens = 0
        total_loss = 0.0
        total_loops = 0
        total_experts = 0
        loop_count = 0
        halt_count = 0
        osc_count = 0
        num_batches = 0

        with torch.no_grad():
            for i in range(0, len(samples), self.batch_size):
                batch = samples[i:i + self.batch_size]
                input_ids = torch.stack([s.input_ids for s in batch]).to(device)
                target_ids = torch.stack([s.target_ids for s in batch]).to(device)

                output = model(input_ids=input_ids, targets=target_ids)
                total_loss += output["loss"].item()

                preds = output["logits"].argmax(dim=-1)
                mask = target_ids != 0
                total_correct += ((preds == target_ids) & mask).sum().item()
                total_tokens += mask.sum().item()

                loop_stats = output.get("loop_stats", [])
                if loop_stats and isinstance(loop_stats[0], LoopStats):
                    for s in loop_stats:
                        total_loops += s.loops_used
                        total_experts += sum(s.experts_used_per_loop) if s.experts_used_per_loop else 1
                        loop_count += 1
                        if s.halted_early:
                            halt_count += 1
                        if s.oscillation_detected:
                            osc_count += 1
                num_batches += 1

        accuracy = total_correct / max(total_tokens, 1)
        avg_loss = total_loss / max(num_batches, 1)
        avg_loops = total_loops / max(loop_count, 1) if loop_count > 0 else 1.0
        avg_experts = total_experts / max(total_loops, 1) if total_loops > 0 else 1.0
        halt_rate = halt_count / max(loop_count, 1) if loop_count > 0 else 0.0
        osc_rate = osc_count / max(loop_count, 1) if loop_count > 0 else 0.0
        compute = max(avg_loops * avg_experts, 0.01)
        qpc = accuracy / compute

        return ModelResult(
            run_id=self.run_id, model_name=model_name, dataset=ds_name,
            dataset_type="synthetic", difficulty=ds_cfg.get("expected_difficulty", "unknown"),
            sample_count=len(samples), accuracy=accuracy, loss=avg_loss,
            avg_loops=avg_loops, avg_experts=avg_experts, halt_rate=halt_rate,
            oscillation_rate=osc_rate, quality_per_compute=qpc,
        )

    # =========================================================================
    # Output
    # =========================================================================

    def _save_raw_results(self):
        rows = [asdict(r) for r in self.results]
        with open(self.output_dir / "per_dataset_metrics.csv", "w", newline="") as f:
            if rows:
                w = csv.DictWriter(f, fieldnames=rows[0].keys())
                w.writeheader()
                w.writerows(rows)
        with open(self.output_dir / "per_dataset_metrics.json", "w") as f:
            json.dump(rows, f, indent=2, default=str)

    def _compute_comparisons(self, valid_results: list[ModelResult]) -> list[ComparisonResult]:
        comparisons = []
        baselines = ["dense_baseline", "fixed_moe"]
        candidates = ["adaptive_moe", "looped_moe", "full_system"]

        for baseline in baselines:
            for candidate in candidates:
                for ds_cfg_name in self.config["datasets"]:
                    if ds_cfg_name == "mixed_training":
                        continue
                    r_base = next((r for r in valid_results if r.model_name == baseline and r.dataset == ds_cfg_name), None)
                    r_cand = next((r for r in valid_results if r.model_name == candidate and r.dataset == ds_cfg_name), None)
                    if not r_base or not r_cand:
                        continue

                    for metric in ["accuracy", "loss", "quality_per_compute"]:
                        va = getattr(r_cand, metric)
                        vb = getattr(r_base, metric)
                        delta = va - vb
                        rel = (delta / max(abs(vb), 1e-8)) * 100
                        wins = (va < vb) if metric == "loss" else (va > vb)
                        comparisons.append(ComparisonResult(
                            model_a=candidate, model_b=baseline, dataset=ds_cfg_name,
                            metric=metric, value_a=va, value_b=vb,
                            absolute_delta=delta, relative_delta_pct=rel, a_wins=wins,
                        ))
        return comparisons

    def _save_comparisons(self, comparisons: list[ComparisonResult]):
        rows = [asdict(c) for c in comparisons]
        with open(self.output_dir / "baseline_comparison.csv", "w", newline="") as f:
            if rows:
                w = csv.DictWriter(f, fieldnames=rows[0].keys())
                w.writeheader()
                w.writerows(rows)
        with open(self.output_dir / "baseline_comparison.json", "w") as f:
            json.dump(rows, f, indent=2)

    def _generate_summary(self, valid_results, comparisons, total_time, interface_check, real_ds_results) -> dict:
        model_summaries = {}
        for r in valid_results:
            if r.model_name not in model_summaries:
                model_summaries[r.model_name] = {"acc": [], "loss": [], "qpc": [], "easy": [], "hard": [], "params": r.total_parameters}
            model_summaries[r.model_name]["acc"].append(r.accuracy)
            model_summaries[r.model_name]["loss"].append(r.loss)
            model_summaries[r.model_name]["qpc"].append(r.quality_per_compute)
            if r.difficulty == "easy":
                model_summaries[r.model_name]["easy"].append(r.accuracy)
            elif r.difficulty == "hard":
                model_summaries[r.model_name]["hard"].append(r.accuracy)

        table = {}
        for m, d in model_summaries.items():
            table[m] = {
                "avg_accuracy": float(np.mean(d["acc"])) if d["acc"] else 0,
                "avg_loss": float(np.mean(d["loss"])) if d["loss"] else 0,
                "avg_qpc": float(np.mean(d["qpc"])) if d["qpc"] else 0,
                "avg_easy_accuracy": float(np.mean(d["easy"])) if d["easy"] else 0,
                "avg_hard_accuracy": float(np.mean(d["hard"])) if d["hard"] else 0,
                "parameters": d["params"],
            }

        wlt = {}
        for c in comparisons:
            key = f"{c.model_a}_vs_{c.model_b}"
            if key not in wlt:
                wlt[key] = {"win": 0, "loss": 0, "tie": 0}
            if abs(c.absolute_delta) < 0.001:
                wlt[key]["tie"] += 1
            elif c.a_wins:
                wlt[key]["win"] += 1
            else:
                wlt[key]["loss"] += 1

        recommendation = self._compute_recommendation(table, comparisons, valid_results, interface_check)

        return {
            "run_id": self.run_id,
            "mode": self.mode,
            "total_time_seconds": total_time,
            "num_models_evaluated": len(model_summaries),
            "num_models_failed": len(self.failures),
            "num_datasets": len(self.config["datasets"]) - 1,
            "total_valid_results": len(valid_results),
            "total_samples_evaluated": sum(r.sample_count for r in valid_results),
            "training_steps": self.num_steps,
            "model_summaries": table,
            "win_loss_tie": wlt,
            "real_dataset_compatibility": interface_check,
            "recommendation": recommendation,
        }

    def _compute_recommendation(self, table, comparisons, valid_results, interface_check):
        # Hard gates
        if not valid_results:
            return {"status": "INVALID_EVAL_PIPELINE", "reason": "Zero valid results. All models failed."}
        if sum(r.sample_count for r in valid_results) == 0:
            return {"status": "INVALID_EVAL_PIPELINE", "reason": "Zero samples evaluated."}
        if self.mode == "smoke":
            return {"status": "INVALID_EVAL_PIPELINE", "reason": "Smoke mode: pipeline verification only, not evidence."}
        if not interface_check.get("compatible", False):
            return {
                "status": "INVALID_MODEL_INTERFACE_FOR_REAL_BENCHMARKS",
                "reason": "Model cannot consume real NLP datasets (custom 256-512 token vocab, no text tokenizer). "
                          "Results are from synthetic algorithmic tasks ONLY. "
                          "This does NOT validate the architecture on real-world reasoning benchmarks.",
                "what_works": "Architecture variant comparison on synthetic tasks with automatic ground truth.",
                "what_is_missing": interface_check.get("required_for_real_benchmarks", []),
            }

        # If somehow we get here with real data support:
        return {"status": "HOLD_NEEDS_MORE_EVIDENCE", "reason": "Unexpected state."}

    def _save_summary(self, summary):
        with open(self.output_dir / "aggregate_summary.json", "w") as f:
            json.dump(summary, f, indent=2, default=str)

    def _save_failure_analysis(self, interface_check, real_ds_results):
        lines = ["# Failure Analysis\n"]
        lines.append(f"**Run ID:** {self.run_id}  ")
        lines.append(f"**Mode:** {self.mode}\n")

        # Model interface check
        lines.append("## Model Interface Compatibility with Real NLP Benchmarks\n")
        lines.append(f"**Compatible:** {interface_check['compatible']}\n")
        lines.append("### Issues:\n")
        for issue in interface_check.get("issues", []):
            lines.append(f"- {issue}")
        lines.append("\n### Required for Real Benchmarks:\n")
        for req in interface_check.get("required_for_real_benchmarks", []):
            lines.append(f"- {req}")

        # Real dataset attempts
        if real_ds_results:
            lines.append("\n## Real Dataset Access Attempts\n")
            for r in real_ds_results:
                status = "ACCESSIBLE" if r.get("loaded") else "FAILED"
                lines.append(f"- **{r['dataset']}**: {status} | {r.get('error', r.get('reason', ''))}")

        # Model failures
        if self.failures:
            lines.append("\n## Model Training/Evaluation Failures\n")
            for f in self.failures:
                lines.append(f"- **{f['model']}**: {f['error']}")

        # What CAN be evaluated
        lines.append("\n## What This Benchmark Actually Evaluates\n")
        lines.append("This benchmark compares architecture variants on **synthetic algorithmic tasks**:\n")
        for item in interface_check.get("what_can_be_evaluated", []):
            lines.append(f"- {item}")
        lines.append("\n## What This Benchmark CANNOT Evaluate\n")
        lines.append("- Performance on natural language reasoning (ARC, HellaSwag)")
        lines.append("- Performance on math word problems (GSM8K)")
        lines.append("- Performance on any text-based benchmark")
        lines.append("- Generalization to real-world tasks")

        with open(self.output_dir / "failure_analysis.md", "w") as f:
            f.write("\n".join(lines))

    def _save_reproducibility_manifest(self, total_time):
        manifest = {
            "run_id": self.run_id,
            "timestamp": datetime.utcnow().isoformat(),
            "hardware": {
                "os": platform.system(),
                "os_version": platform.version(),
                "machine": platform.machine(),
                "processor": platform.processor(),
                "python_version": platform.python_version(),
                "torch_version": torch.__version__,
                "cuda_available": torch.cuda.is_available(),
                "device_used": self.device,
            },
            "config": {
                "mode": self.mode,
                "training_steps": self.num_steps,
                "batch_size": self.batch_size,
                "seed": self.seed,
                "num_models": len(self.config["models"]),
                "num_datasets": len(self.config["datasets"]),
                "model_dim": self.config["model_base"]["d_model"],
                "vocab_size": self.config["model_base"]["vocab_size"],
            },
            "total_time_seconds": total_time,
        }
        with open(self.output_dir / "reproducibility_manifest.json", "w") as f:
            json.dump(manifest, f, indent=2)

    def _generate_report(self, summary, comparisons, interface_check):
        lines = ["# Sparse Loop-MoE Architecture Benchmark Report\n"]
        lines.append(f"**Run ID:** {self.run_id}  ")
        lines.append(f"**Mode:** {self.mode}  ")
        lines.append(f"**Steps:** {self.num_steps} | **Device:** {self.device} | **Time:** {summary['total_time_seconds']:.1f}s\n")

        # Recommendation
        rec = summary["recommendation"]
        lines.append(f"## Status: {rec['status']}\n")
        lines.append(f"{rec['reason']}\n")

        # Validity
        lines.append("## Evaluation Validity\n")
        lines.append(f"- Models evaluated: {summary['num_models_evaluated']}")
        lines.append(f"- Models failed: {summary['num_models_failed']}")
        lines.append(f"- Datasets: {summary['num_datasets']} (synthetic algorithmic)")
        lines.append(f"- Total samples: {summary['total_samples_evaluated']}")
        lines.append(f"- Real NLP compatible: **NO** (see failure_analysis.md)\n")

        # Model table
        if summary["model_summaries"]:
            lines.append("## Model Comparison (Synthetic Tasks)\n")
            lines.append("| Model | Params | Avg Acc | Avg Loss | Easy Acc | Hard Acc | QPC |")
            lines.append("|-------|--------|---------|----------|----------|----------|-----|")
            for m, d in summary["model_summaries"].items():
                lines.append(f"| {m} | {d['parameters']:,} | {d['avg_accuracy']:.4f} | "
                             f"{d['avg_loss']:.3f} | {d['avg_easy_accuracy']:.4f} | "
                             f"{d['avg_hard_accuracy']:.4f} | {d['avg_qpc']:.4f} |")

        # Win/loss/tie
        if summary["win_loss_tie"]:
            lines.append("\n## Win/Loss/Tie\n")
            lines.append("| Comparison | Win | Loss | Tie |")
            lines.append("|------------|-----|------|-----|")
            for k, v in summary["win_loss_tie"].items():
                lines.append(f"| {k} | {v['win']} | {v['loss']} | {v['tie']} |")

        # Caveats
        lines.append("\n## Critical Caveats\n")
        lines.append("1. **NO real NLP benchmarks evaluated.** Model cannot process natural language.")
        lines.append("2. Results are from synthetic algorithmic tasks with custom encoding.")
        lines.append("3. This evaluates architecture design choices, NOT language capability.")
        lines.append(f"4. Model vocab: {self.config['model_base']['vocab_size']} tokens (custom).")
        lines.append(f"5. Model dim: {self.config['model_base']['d_model']} (research scale).\n")

        with open(self.output_dir / "benchmark_report.md", "w") as f:
            f.write("\n".join(lines))


# =============================================================================
# CLI
# =============================================================================

def main():
    parser = argparse.ArgumentParser(description="Sparse Loop-MoE Benchmark")
    parser.add_argument("--mode", choices=["smoke", "benchmark-lite", "benchmark-full"], default="smoke")
    parser.add_argument("--config", default="evaluation/benchmark_config.yaml")
    parser.add_argument("--attempt-real-datasets", action="store_true",
                        help="Try to load real NLP datasets to demonstrate interface incompatibility")
    args = parser.parse_args()

    runner = BenchmarkRunner(config_path=args.config, mode=args.mode, attempt_real=args.attempt_real_datasets)
    summary = runner.run()

    rec = summary["recommendation"]
    print(f"\n  STATUS: {rec['status']}")
    print(f"  {rec['reason']}")


if __name__ == "__main__":
    main()
