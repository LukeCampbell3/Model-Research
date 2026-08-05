"""Generate multi-size scaling report from benchmark scorecards."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from benchmark.common import load_json_or_yaml, write_json, write_markdown_report


SCALING_AXES = [
    "capability_by_size",
    "efficiency_by_size",
    "routing_specialization_by_size",
    "coding_capability_by_size",
    "quality_per_active_param_by_size",
    "quality_per_gpu_hour_by_size",
    "code_score_per_active_flop_by_size",
]


def _load_scorecards(results: Path) -> list[dict[str, Any]]:
    cards = []
    for path in sorted(results.rglob("merged_scorecard.json")):
        cards.append(json.loads(path.read_text(encoding="utf-8")))
    return cards


def _matrix_models(matrix: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {item["model_variant"]: item for item in matrix.get("models", [])}


def generate(results: str, matrix_path: str, output: str, limit: int | None = None) -> dict[str, Any]:
    matrix = load_json_or_yaml(matrix_path)
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    cards = _load_scorecards(Path(results))
    model_lookup = _matrix_models(matrix)
    by_axis = {axis: [] for axis in SCALING_AXES}
    for card in cards:
        model = card.get("model")
        cfg = model_lookup.get(model, {})
        row = {
            "model": model,
            "model_family": cfg.get("model_family"),
            "model_size_label": cfg.get("model_size_label"),
            "comparison_group": cfg.get("comparison_group"),
            "status": card.get("status"),
            "benchmark_evidence": card.get("benchmark_evidence", False),
            "active_params_per_token": cfg.get("active_params_per_token"),
            "active_flops_estimate": cfg.get("active_flops_estimate"),
            "gpu_hours": None,
            "quality": None,
            "coding_score": None,
            "routing_specialization_score": None,
        }
        by_axis["capability_by_size"].append(row)
        by_axis["efficiency_by_size"].append(row)
        by_axis["routing_specialization_by_size"].append(row)
        by_axis["coding_capability_by_size"].append(row)
        by_axis["quality_per_active_param_by_size"].append(row)
        by_axis["quality_per_gpu_hour_by_size"].append(row)
        by_axis["code_score_per_active_flop_by_size"].append(row)
    required_sizes = {"100m", "300m", "700m"}
    observed_sizes = {str(model_lookup.get(card.get("model"), {}).get("model_size_label")) for card in cards}
    evidence_ready = required_sizes <= observed_sizes and all(card.get("benchmark_evidence") for card in cards)
    payload = {
        "schema_version": "1.0",
        "status": "PVR_EC_O_BROAD_NLP_SCALE_POSITIONED" if evidence_ready else "NOT_RUN_RESOURCE_BLOCKED",
        "limit": limit,
        "result_count": len(cards),
        "required_sizes": sorted(required_sizes),
        "observed_sizes": sorted(s for s in observed_sizes if s and s != "None"),
        "benchmark_evidence": evidence_ready,
        "scaling_axes": by_axis,
        "decision_language": [
            "PVR-EC-O does not yet beat generalized baselines.",
            "PVR-EC-O beats generalized baselines but lags internal strong-router control.",
            "PVR-EC-O matches internal strong-router control.",
            "PVR-EC-O beats internal strong-router control.",
        ],
    }
    write_json(out / "scaling_report.json", payload)
    write_markdown_report(out / "scaling_report.md", "PVR-EC-O Multi-Size Scaling Report", payload)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate PVR-EC-O scaling report")
    parser.add_argument("--config", default=None)
    parser.add_argument("--results", required=True)
    parser.add_argument("--matrix", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--limit", type=int, default=None)
    args = parser.parse_args()
    payload = generate(args.results, args.matrix, args.output, args.limit)
    print(payload["status"])


if __name__ == "__main__":
    main()
