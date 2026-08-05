"""Merge NLP, coding, routing, and contamination artifacts into one scorecard."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from benchmark.common import base_metadata, load_json_or_yaml, require_fields, write_json


def run(config: dict, output: str, limit: int | None = None, inputs: list[str] | None = None) -> dict:
    require_fields(config, ["model_variant", "model_family"], "Scorecard merge config")
    loaded = {}
    for item in inputs or []:
        path = Path(item)
        if path.exists():
            if path.parent.name == "routing_diagnostics":
                key = "routing_diagnostics"
            elif path.parent.name == "contamination":
                key = "contamination_scan"
            else:
                key = path.stem
            loaded[key] = json.loads(path.read_text(encoding="utf-8"))
    statuses = sorted({str(data.get("status")) for data in loaded.values() if isinstance(data, dict)})
    nlp_ready = bool(loaded.get("nlp_scorecard", {}).get("benchmark_evidence"))
    coding_ready = bool(loaded.get("coding_scorecard", {}).get("benchmark_evidence"))
    contamination_ready = bool(loaded.get("contamination_scan", {}).get("benchmark_evidence"))
    if config.get("model_family") == "pvr_ec_o":
        routing_ready = bool(loaded.get("routing_diagnostics", {}).get("benchmark_evidence"))
    else:
        routing_ready = True
    benchmark_evidence = nlp_ready and coding_ready and contamination_ready and routing_ready
    if any(status in {"EVAL_FAILED", "TRAINING_FAILED"} for status in statuses):
        status = "EVAL_FAILED"
    elif any(status in {"NOT_RUN_MISSING_DATA", "NOT_RUN_MISSING_CHECKPOINT"} for status in statuses):
        status = "NOT_RUN_MISSING_DATA" if "NOT_RUN_MISSING_DATA" in statuses else "NOT_RUN_MISSING_CHECKPOINT"
    elif benchmark_evidence:
        status = "GENUINE_REDUCED_EVAL"
    else:
        status = "NOT_RUN_NOT_IMPLEMENTED" if "NOT_RUN_NOT_IMPLEMENTED" in statuses else "BENCH_INFRASTRUCTURE_READY"
    payload = {
        **base_metadata(config, limit),
        "status": status if loaded else "BENCH_INFRASTRUCTURE_INCOMPLETE",
        "model": config.get("model_variant"),
        "scorecards": loaded,
        "source_statuses": statuses,
        "benchmark_evidence": benchmark_evidence if loaded else False,
        "evidence_requirements": {
            "nlp_ready": nlp_ready,
            "coding_ready": coding_ready,
            "contamination_ready": contamination_ready,
            "routing_ready": routing_ready,
        },
    }
    write_json(output, payload)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description="Merge scorecards")
    parser.add_argument("--config", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--inputs", default="")
    args = parser.parse_args()
    payload = run(
        load_json_or_yaml(args.config),
        args.output,
        args.limit,
        [x.strip() for x in args.inputs.split(",") if x.strip()],
    )
    print(payload["status"])


if __name__ == "__main__":
    main()
