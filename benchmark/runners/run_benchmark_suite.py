"""Run the first executable genuine benchmark layer.

This runner never fabricates benchmark evidence. If checkpoints or data are
missing, it writes NOT_RUN artifacts and a benchmark report explaining the
resource block.
"""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

from benchmark.common import load_json_or_yaml, manifest_payload, write_json, write_markdown_report
from benchmark.runners import run_code_eval, run_contamination_scan, run_lm_eval, run_routing_diagnostics, run_scorecard_merge


def _copy_manifests(out: Path) -> list[str]:
    manifest_dir = Path("benchmark/manifests")
    copied = []
    if not manifest_dir.exists():
        return copied
    target = out / "manifests"
    target.mkdir(parents=True, exist_ok=True)
    for path in sorted(manifest_dir.glob("*.json")):
        shutil.copy2(path, target / path.name)
        copied.append(str(target / path.name))
    return copied


def run_suite(suite_path: str, output: str, limit: int | None = None, infrastructure_only: bool = False) -> dict:
    suite = load_json_or_yaml(suite_path)
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    copied_manifests = _copy_manifests(out)
    write_json(out / "manifests" / "run_reproducibility_manifest.json", manifest_payload([suite_path], "Suite execution reproducibility manifest."))

    model_results = []
    for item in suite.get("models", []):
        config_path = item["config_path"]
        config = load_json_or_yaml(config_path)
        model_out = out / "scorecards" / config["model_variant"]
        nlp = run_lm_eval.run(config, str(model_out / "nlp_scorecard.json"), limit, infrastructure_only)
        code = run_code_eval.run(config, str(model_out / "coding_scorecard.json"), limit, infrastructure_only)
        routing = run_routing_diagnostics.run(config, str(out / "routing_diagnostics" / f"{config['model_variant']}.json"), limit, infrastructure_only)
        contamination = run_contamination_scan.run(config, str(out / "contamination" / f"{config['model_variant']}.json"), limit, infrastructure_only)
        merged = run_scorecard_merge.run(
            config,
            str(model_out / "merged_scorecard.json"),
            limit,
            [
                str(model_out / "nlp_scorecard.json"),
                str(model_out / "coding_scorecard.json"),
                str(out / "routing_diagnostics" / f"{config['model_variant']}.json"),
                str(out / "contamination" / f"{config['model_variant']}.json"),
            ],
        )
        model_results.append({
            "model_variant": config["model_variant"],
            "comparison_group": config["comparison_group"],
            "status": merged["status"],
            "benchmark_evidence": bool(merged.get("benchmark_evidence")),
            "artifacts": {
                "nlp_scorecard": str(model_out / "nlp_scorecard.json"),
                "coding_scorecard": str(model_out / "coding_scorecard.json"),
                "routing_diagnostics": str(out / "routing_diagnostics" / f"{config['model_variant']}.json"),
                "contamination_scan": str(out / "contamination" / f"{config['model_variant']}.json"),
                "merged_scorecard": str(model_out / "merged_scorecard.json"),
            },
        })

    status = "BENCH_INFRASTRUCTURE_READY"
    if model_results and all(r["benchmark_evidence"] for r in model_results):
        status = "GENUINE_REDUCED_EVAL"
    elif any(r["status"] == "EVAL_FAILED" for r in model_results):
        status = "EVAL_FAILED"
    elif any(r["status"] == "NOT_RUN_MISSING_DATA" for r in model_results):
        status = "NOT_RUN_MISSING_DATA"
    elif any(r["status"] == "NOT_RUN_MISSING_CHECKPOINT" for r in model_results):
        status = "NOT_RUN_MISSING_CHECKPOINT"
    evidence_count = sum(1 for r in model_results if r["benchmark_evidence"])
    payload = {
        "schema_version": "1.0",
        "status": status,
        "suite": suite,
        "limit": limit,
        "model_results": model_results,
        "benchmark_evidence_count": evidence_count,
        "copied_manifests": copied_manifests,
        "required_artifacts_generated": {
            "scorecards": True,
            "manifests": bool(copied_manifests),
            "routing_diagnostics": True,
            "contamination_scan": True,
            "benchmark_report": True,
        },
        "valid_claim": "Benchmark infrastructure is ready to run genuine comparisons." if evidence_count == 0 else "Genuine benchmark evidence produced for models with real checkpoints and data.",
        "invalid_claims_blocked": [
            "script execution is not benchmark evidence",
            "missing checkpoints are not model results",
            "custom_fixed_moe_strong_router is not a generic MoE baseline",
        ],
    }
    write_json(out / "benchmark_suite_result.json", payload)
    write_markdown_report(out / "benchmark_report.md", "PVR-EC-O Genuine Benchmark Suite Report", payload)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description="Run PVR-EC-O benchmark suite")
    parser.add_argument("--suite", default=None)
    parser.add_argument("--config", default=None)
    parser.add_argument("--output", required=True)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--infrastructure-only", action="store_true")
    args = parser.parse_args()
    suite = args.suite or args.config
    if not suite:
        raise SystemExit("--suite or --config is required")
    payload = run_suite(suite, args.output, args.limit, args.infrastructure_only)
    print(payload["status"])


if __name__ == "__main__":
    main()
