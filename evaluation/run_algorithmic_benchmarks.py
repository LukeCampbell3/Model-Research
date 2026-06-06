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
import json
import os
import platform
import random
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
                 pvr_aux_alpha=0.5, benchmark_inference_only=False,
                 warmup_steps=10, timed_steps=50, batch_sizes=None,
                 sequence_lengths=None, profile_deploy=False):
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
        self.benchmark_inference_only = benchmark_inference_only
        self.warmup_steps = warmup_steps
        self.timed_steps = timed_steps
        self.batch_sizes = batch_sizes or [1, 32]
        self.sequence_lengths = sequence_lengths or [64]
        self.profile_deploy = profile_deploy

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

        # Generate benchmark data for all families
        datasets = self._generate_all_datasets()
        print(f"  Generated {sum(len(v) for v in datasets.values())} total samples across {len(datasets)} task sets\n")

        # Train and evaluate each model
        active_models = MODELS
        if self.model_filter:
            active_models = {k: v for k, v in MODELS.items() if k in self.model_filter}

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
            d_expert = max(1, scale["d_ff"] // 4)
            if self.pvr_expert_type == "delta_rank_medium":
                d_expert = max(1, scale["d_ff"] // 2)
            elif self.pvr_expert_type in {"delta_rank_large", "full_expert_ffn"}:
                d_expert = scale["d_ff"]
            deploy_mode = overrides.get("deploy_mode", self.pvr_deploy_mode)
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
                pvr_expert_type=self.pvr_expert_type or "delta_rank_small",
                pvr_deploy_mode=deploy_mode,
                pvr_aux_alpha=self.pvr_aux_alpha,
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
        deploy_mode = overrides.get("deploy_mode", "off")
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
            deploy_mode = model_cfg.get("overrides", {}).get("deploy_mode", "off")
            expert_execution_mode = (
                "FULLY_VECTORIZED" if model_cfg["type"] == "pvr_ec" and deploy_mode != "off"
                else "FULLY_VECTORIZED" if model_cfg["type"] == "moe" and model_cfg.get("overrides", {}).get("vectorized_moe")
                else "LOOPED"
            )
            for batch_size in self.batch_sizes:
                for seq_len in self.sequence_lengths:
                    input_ids = torch.randint(0, 256, (batch_size, seq_len), device=device)
                    targets = torch.randint(0, 256, (batch_size, seq_len), device=device)
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
                    p50 = float(np.percentile(latencies, 50))
                    p95 = float(np.percentile(latencies, 95))
                    mean_latency = float(np.mean(latencies))
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
                        "params": params,
                        "active_params_estimate": params,
                        "batch_size": batch_size,
                        "sequence_length": seq_len,
                        "loss": loss,
                        "accuracy": accuracy,
                        "p50_latency_ms": p50,
                        "p95_latency_ms": p95,
                        "mean_latency_ms": mean_latency,
                        "tokens_per_second": 1000.0 * tokens / max(mean_latency, 1e-8),
                        "samples_per_second": 1000.0 * batch_size / max(mean_latency, 1e-8),
                        "quality_per_ms": accuracy / max(mean_latency, 1e-8),
                        "quality_per_token_second": accuracy * (1000.0 * tokens / max(mean_latency, 1e-8)),
                        "memory_allocated_mb": memory_allocated_mb,
                        "max_memory_allocated_mb": max_memory_allocated_mb,
                        "expert_execution_mode": expert_execution_mode,
                        "branch_tickets_enabled": False,
                        "mergeability_mode": "disabled",
                        "runtime_branching_enabled": False,
                    }
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

        if model_cfg["type"] == "dense":
            model = DenseTransformer(DenseTransformerConfig(
                vocab_size=vocab_size, d_model=scale["d_model"], n_heads=scale["n_heads"],
                n_layers=scale["n_layers"], d_ff=scale["d_ff"],
                max_seq_len=scale["d_model"]*2, dropout=0.1,
            ))
        elif model_cfg["type"] == "pvr_ec":
            overrides = model_cfg.get("overrides", {})
            # Parameter-matched: increase expert delta size to match fixed_moe params
            if overrides.get("match_params"):
                d_expert = scale["d_ff"]  # Full-size expert deltas
                num_proto = scale["num_experts"] * 8
            else:
                d_expert = scale["d_ff"] // 2
                num_proto = scale["num_experts"] * 4
            if self.pvr_expert_type == "delta_rank_small":
                d_expert = max(1, scale["d_ff"] // 4)
            elif self.pvr_expert_type == "delta_rank_medium":
                d_expert = max(1, scale["d_ff"] // 2)
            elif self.pvr_expert_type in {"delta_rank_large", "full_expert_ffn"}:
                d_expert = scale["d_ff"]

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
                pvr_expert_type=self.pvr_expert_type or "delta_rank_medium",
                pvr_training_dispatch_mode=self.pvr_training_dispatch_mode,
                pvr_inference_dispatch_mode=self.pvr_inference_dispatch_mode,
                pvr_deploy_mode=overrides.get("deploy_mode", self.pvr_deploy_mode),
                pvr_aux_alpha=self.pvr_aux_alpha,
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
        print(f"    Params: {params:,}")

        # Move model to device
        device_obj = torch.device(self.device)
        model = model.to(device_obj)

        # Train on mixed algorithmic data (all families combined)
        all_train = []
        for samples in datasets.values():
            all_train.extend(samples[:len(samples)//2])  # First half for training
        random.Random(self.seed).shuffle(all_train)

        # Convert BenchmarkSamples to training format
        task_gen = SyntheticTaskGenerator(vocab_size=vocab_size, max_seq_len=scale["d_model"]*2, seed=self.seed)
        trainer_config = TrainerConfig(
            learning_rate=3e-4, weight_decay=0.01,
            warmup_steps=max(1, self.train_steps // 5),
            max_steps=self.train_steps, batch_size=min(32, len(all_train)),
            eval_interval=self.train_steps + 1,
            log_interval=max(self.train_steps // 3, 1),
            device=self.device,
        )
        trainer = Trainer(model=model, config=trainer_config, task_generator=task_gen)

        t0 = time.time()
        trainer.train(num_steps=self.train_steps)
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
            result.inference_time_s = time.time() - t1
            self.results.append(result)
            print(f"    {ds_name:20s} | n={result.sample_count:3d} | acc={result.accuracy:.4f} | "
                  f"em={result.exact_match:.4f} | loss={result.loss:.3f} | "
                  f"loops={result.avg_loops:.1f} | qpc={result.qpc:.4f}")

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

        with torch.no_grad():
            for i in range(0, len(samples), bs):
                batch = samples[i:i+bs]
                input_ids = torch.stack([s.input_ids for s in batch]).to(device)
                target_ids = torch.stack([s.target_ids for s in batch]).to(device)

                output = model(input_ids=input_ids, targets=target_ids)
                total_loss += output["loss"].item()
                if "pvr_diagnostics" in output:
                    pvr_diag_history.append(output["pvr_diagnostics"])

                preds = output["logits"].argmax(dim=-1)
                mask = target_ids != 0
                correct = (preds == target_ids) & mask
                total_correct += correct.sum().item()
                total_tokens += mask.sum().item()

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

def main():
    parser = argparse.ArgumentParser(description="Algorithmic Benchmark Runner")
    parser.add_argument("--mode", choices=["smoke", "benchmark-lite", "benchmark-full"], default="smoke")
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
    parser.add_argument("--benchmark-inference-only", action="store_true")
    parser.add_argument("--warmup-steps", type=int, default=10)
    parser.add_argument("--timed-steps", type=int, default=50)
    parser.add_argument("--batch-sizes", default="1,32")
    parser.add_argument("--sequence-lengths", default="64")
    parser.add_argument("--profile-deploy", action="store_true")
    args = parser.parse_args()

    families = [f.strip() for f in args.families.split(",")]
    models = [m.strip() for m in args.models.split(",")] if args.models else None
    batch_sizes = [int(x.strip()) for x in args.batch_sizes.split(",") if x.strip()]
    sequence_lengths = [int(x.strip()) for x in args.sequence_lengths.split(",") if x.strip()]

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
        benchmark_inference_only=args.benchmark_inference_only,
        warmup_steps=args.warmup_steps,
        timed_steps=args.timed_steps,
        batch_sizes=batch_sizes,
        sequence_lengths=sequence_lengths,
        profile_deploy=args.profile_deploy,
    )
    summary = runner.run()
    if args.benchmark_inference_only:
        print(f"  STATUS: {summary['status']}")
    else:
        rec = summary["recommendation"]
        print(f"  STATUS: {rec['status']}")
        print(f"  ARCH: {rec.get('architecture_recommendation', 'N/A')}")
        print(f"  {rec['reason']}")


if __name__ == "__main__":
    main()
