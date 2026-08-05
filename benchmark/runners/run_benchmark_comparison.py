"""Compare genuine benchmark scorecards for one completed tier."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from benchmark.common import utc_now, write_json, write_markdown_report


def _load_merged_scorecards(root: Path) -> list[dict[str, Any]]:
    cards = []
    for path in sorted(root.rglob("merged_scorecard.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        payload["_path"] = str(path)
        cards.append(payload)
    return cards


def _metric(card: dict[str, Any], source: str, key: str) -> Any:
    return card.get("scorecards", {}).get(source, {}).get("scorecard", {}).get(key)


def _load_checkpoint_sidecars(card: dict[str, Any]) -> dict[str, Any]:
    checkpoint = card.get("config", {}).get("checkpoint_path")
    if not checkpoint:
        return {}
    root = Path(checkpoint).parent
    sidecars = {}
    for name in ["checkpoint_manifest", "hardware_manifest", "training_curve", "eval_curve", "routing_curve"]:
        path = root / f"{name}.json"
        if path.exists():
            sidecars[name] = json.loads(path.read_text(encoding="utf-8"))
    return sidecars


def run(results: str, output: str, program_report: str | None = None) -> dict[str, Any]:
    root = Path(results)
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    cards = _load_merged_scorecards(root)
    rows = []
    for card in cards:
        lm_loss = _metric(card, "nlp_scorecard", "lm_loss")
        compile_rate = _metric(card, "coding_scorecard", "compile_rate")
        sidecars = _load_checkpoint_sidecars(card)
        checkpoint_manifest = sidecars.get("checkpoint_manifest", {})
        hardware_manifest = sidecars.get("hardware_manifest", {})
        gpu_hours = hardware_manifest.get("gpu_hours", _metric(card, "nlp_scorecard", "gpu_hours"))
        active_params = _metric(card, "nlp_scorecard", "active_params_per_token")
        routing = card.get("scorecards", {}).get("routing_diagnostics", {}).get("scorecard", {})
        training_curve = sidecars.get("training_curve", {}).get("loss_curve", [])
        eval_curve = sidecars.get("eval_curve", {}).get("eval_curve", [])
        routing_curve = sidecars.get("routing_curve", {}).get("routing_curve", [])
        train_losses = [item.get("loss") for item in training_curve if isinstance(item.get("loss"), (int, float))]
        eval_losses = [item.get("eval_loss") for item in eval_curve if isinstance(item.get("eval_loss"), (int, float))]
        train_slope = ((train_losses[-1] - train_losses[0]) / max(1, len(train_losses) - 1)) if len(train_losses) >= 2 else None
        eval_slope = ((eval_losses[-1] - eval_losses[0]) / max(1, len(eval_losses) - 1)) if len(eval_losses) >= 2 else None
        train_eval_gap = (eval_losses[-1] - train_losses[-1]) if train_losses and eval_losses else None
        active_flops = card.get("config", {}).get("active_flops_estimate")
        rows.append({
            "model": card.get("model"),
            "status": card.get("status"),
            "benchmark_evidence": bool(card.get("benchmark_evidence")),
            "comparison_group": card.get("config", {}).get("comparison_group"),
            "lm_loss": lm_loss,
            "perplexity": _metric(card, "nlp_scorecard", "perplexity"),
            "code_heavy_loss": _metric(card, "nlp_scorecard", "code_token_loss"),
            "math_heavy_loss": _metric(card, "nlp_scorecard", "math_token_loss"),
            "json_schema_loss": _metric(card, "nlp_scorecard", "json_token_loss"),
            "compile_rate": compile_rate,
            "tokens_per_second": _metric(card, "nlp_scorecard", "throughput"),
            "training_tokens_per_second": hardware_manifest.get("tokens_per_second"),
            "eval_latency_ms_per_token": _metric(card, "nlp_scorecard", "eval_latency_ms_per_token"),
            "vram_peak": _metric(card, "nlp_scorecard", "vram_peak") or hardware_manifest.get("vram_peak"),
            "gpu_hours": gpu_hours,
            "training_tokens_seen": checkpoint_manifest.get("training_tokens_seen", checkpoint_manifest.get("tokens_seen")),
            "optimizer_steps": checkpoint_manifest.get("optimizer_steps"),
            "effective_batch_tokens": checkpoint_manifest.get("effective_batch_tokens"),
            "eval_window_count": len(eval_curve),
            "routing_window_count": len(routing_curve),
            "train_loss_slope": train_slope,
            "eval_loss_slope": eval_slope,
            "train_eval_gap": train_eval_gap,
            "eval_token_count": _metric(card, "nlp_scorecard", "eval_token_count"),
            "heldout_eval_token_count": _metric(card, "nlp_scorecard", "heldout_eval_token_count"),
            "active_params_per_token": active_params,
            "active_flops_per_token": active_flops,
            "routing_diagnostics": {
                "owners_per_token": routing.get("owners_per_token"),
                "top2_execution_count": routing.get("top2_execution_count"),
                "top4_execution_count": routing.get("top4_execution_count"),
                "runtime_dynamic_k_count": routing.get("runtime_dynamic_k_count"),
                "runtime_expert_choice_count": routing.get("runtime_expert_choice_count"),
                "owner_entropy": routing.get("owner_entropy"),
                "expert_gini": routing.get("expert_gini"),
                "prototype_margin": routing.get("prototype_margin"),
                "prototype_monopoly_rate": routing.get("prototype_monopoly_rate"),
                "hard_invariants_validated": routing.get("invariants_validated"),
            },
            "quality_per_active_param": (1.0 / lm_loss / active_params) if isinstance(lm_loss, (int, float)) and lm_loss > 0 and active_params else None,
            "quality_per_active_flop": (1.0 / lm_loss / active_flops) if isinstance(lm_loss, (int, float)) and lm_loss > 0 and active_flops else None,
            "quality_per_gpu_hour": (1.0 / lm_loss / gpu_hours) if isinstance(lm_loss, (int, float)) and lm_loss > 0 and gpu_hours else None,
            "scorecard_path": card.get("_path"),
        })
    evidence_ready = bool(rows) and all(row["benchmark_evidence"] for row in rows)
    program = json.loads(Path(program_report).read_text(encoding="utf-8")) if program_report and Path(program_report).exists() else None
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "status": "GENUINE_BENCHMARK_COMPARISON_COMPLETE" if evidence_ready else "NOT_RUN_RESOURCE_BLOCKED",
        "benchmark_evidence": evidence_ready,
        "program_status": program.get("status") if program else None,
        "model_count": len(rows),
        "completed_model_count": sum(1 for row in rows if row["benchmark_evidence"]),
        "rows": rows,
        "rankings": {
            "lm_loss_ascending": sorted(
                [{"model": row["model"], "lm_loss": row["lm_loss"]} for row in rows if isinstance(row["lm_loss"], (int, float))],
                key=lambda item: item["lm_loss"],
            ),
            "compile_rate_descending": sorted(
                [{"model": row["model"], "compile_rate": row["compile_rate"]} for row in rows if isinstance(row["compile_rate"], (int, float))],
                key=lambda item: item["compile_rate"],
                reverse=True,
            ),
        },
        "notes": "Reduced genuine benchmark comparison. Official broad NLP and coding benchmark adapters may still report NOT_RUN_NOT_IMPLEMENTED inside scorecards.",
    }
    write_json(out / "benchmark_comparison_report.json", payload)
    write_markdown_report(out / "benchmark_comparison_report.md", "PVR-EC-O 100M Genuine Benchmark Comparison", payload)
    print(payload["status"])
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description="Compare genuine benchmark scorecards")
    parser.add_argument("--results", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--program-report", default=None)
    args = parser.parse_args()
    run(args.results, args.output, args.program_report)


if __name__ == "__main__":
    main()
