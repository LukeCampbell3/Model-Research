"""Instantiate benchmark model architectures and verify accounting metadata."""

from __future__ import annotations

import argparse
from pathlib import Path

import torch

from benchmark.common import load_json_or_yaml, write_json, write_markdown_report
from benchmark.model_factory import build_model


def _iter_suite_configs(suite_or_config: str) -> list[dict]:
    payload = load_json_or_yaml(suite_or_config)
    if "models" not in payload:
        return [payload]
    return [load_json_or_yaml(item["config_path"]) for item in payload["models"]]


def _forward_probe(materialized, config: dict, device: str, batch_size: int, seq_len: int) -> dict:
    if device == "meta":
        return {"executed_forward": False, "reason": "meta_device_parameter_accounting_only"}
    model = materialized.model
    model.eval()
    vocab = int(config.get("vocab_size", 50_257))
    seq = min(seq_len, int(config["context_length"]))
    with torch.no_grad():
        x = torch.randint(0, vocab, (batch_size, seq), device=device)
        logits = model(x)
    return {
        "executed_forward": True,
        "input_shape": [batch_size, seq],
        "output_shape": list(logits.shape),
        "finite_output": bool(torch.isfinite(logits).all().item()),
    }


def run(
    suite_or_config: str,
    output: str,
    device: str = "meta",
    limit: int | None = None,
    forward_check: bool = False,
    batch_size: int = 1,
    seq_len: int = 8,
) -> dict:
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    configs = _iter_suite_configs(suite_or_config)
    rows = []
    for config in configs[: limit or len(configs)]:
        materialized = build_model(config, device=device)
        total_target = int(config["total_params"])
        active_target = int(config["active_params_per_token"])
        total_actual = int(materialized.total_params_actual)
        active_actual = int(materialized.active_params_per_token_actual)
        total_ratio = total_actual / max(total_target, 1)
        active_ratio = active_actual / max(active_target, 1)
        probe = _forward_probe(materialized, config, device, batch_size, seq_len) if forward_check else {
            "executed_forward": False,
            "reason": "forward_check_not_requested",
        }
        rows.append({
            "model_variant": config["model_variant"],
            "model_family": config["model_family"],
            "model_size_label": config["model_size_label"],
            "comparison_group": config["comparison_group"],
            "device": device,
            "created": True,
            "benchmark_evidence": False,
            "total_params_target": total_target,
            "total_params_actual": total_actual,
            "total_param_ratio_actual_to_target": total_ratio,
            "active_params_per_token_target": active_target,
            "active_params_per_token_actual": active_actual,
            "active_param_ratio_actual_to_target": active_ratio,
            "experts_active_per_token": config.get("experts_active_per_token"),
            "top1_runtime_ownership_expected": config["model_family"] == "pvr_ec_o",
            "owners_per_token_expected": 1.0 if config["model_family"] == "pvr_ec_o" else None,
            "top2_execution_count_expected": 0 if config["model_family"] == "pvr_ec_o" else None,
            "top4_execution_count_expected": 0 if config["model_family"] == "pvr_ec_o" else None,
            "notes": "Architecture materialized for parameter accounting only; this is not a trained checkpoint or capability result.",
            "forward_probe": probe,
        })
        del materialized
        if device == "cuda" and torch.cuda.is_available():
            torch.cuda.empty_cache()
    payload = {
        "schema_version": "1.0",
        "status": "BENCH_INFRASTRUCTURE_READY",
        "created_model_count": len(rows),
        "benchmark_evidence": False,
        "device": device,
        "forward_check": forward_check,
        "rows": rows,
    }
    write_json(out / "model_creation_report.json", payload)
    write_markdown_report(out / "model_creation_report.md", "PVR-EC-O Model Creation Report", payload)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description="Create benchmark model architectures")
    parser.add_argument("--suite", default=None)
    parser.add_argument("--config", default=None)
    parser.add_argument("--output", required=True)
    parser.add_argument("--device", default="meta")
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--forward-check", action="store_true")
    parser.add_argument("--batch-size", type=int, default=1)
    parser.add_argument("--seq-len", type=int, default=8)
    args = parser.parse_args()
    target = args.suite or args.config
    if not target:
        raise SystemExit("--suite or --config is required")
    payload = run(target, args.output, args.device, args.limit, args.forward_check, args.batch_size, args.seq_len)
    print(payload["status"])


if __name__ == "__main__":
    main()
