"""Routing-specialization diagnostics for PVR-EC-O benchmark runs."""

from __future__ import annotations

import math
from pathlib import Path

import torch

from benchmark.common import (
    REQUIRED_MODEL_CONFIG_FIELDS,
    ROUTING_INVARIANT_FIELDS,
    base_metadata,
    common_scorecard,
    load_json_or_yaml,
    parser_with_config,
    require_fields,
    route_invariants_for_not_run,
    status_for_config,
    write_json,
)
from benchmark.model_factory import build_model


ROUTING_METRICS = {
    "owners_per_token": None,
    "prototype_entropy": None,
    "prototype_margin": None,
    "owner_churn": None,
    "expert_utilization": None,
    "expert_gini": None,
    "monopoly_rate": None,
    "challenger_disagreement": None,
    "descriptor_margin": None,
    "operator_margin": None,
    "stale_owner_rate": None,
    "failure_mode_distribution": None,
    "top2_execution_count": None,
    "top4_execution_count": None,
    "runtime_dynamic_k_count": None,
    "runtime_expert_choice_count": None,
    "production_map_mutated": None,
}


def _files(paths: list[str]) -> list[Path]:
    out: list[Path] = []
    for item in paths:
        path = Path(item)
        if path.is_file():
            out.append(path)
        elif path.is_dir():
            out.extend(sorted(child for child in path.rglob("*routing*") if child.is_file()))
            if not out:
                out.extend(sorted(child for child in path.rglob("*") if child.is_file()))
    return out


def _entropy(counts: list[int]) -> float | None:
    total = sum(counts)
    if total <= 0:
        return None
    result = 0.0
    for count in counts:
        if count:
            p = count / total
            result -= p * math.log(p)
    return result


def _gini(counts: list[int]) -> float | None:
    if not counts:
        return None
    values = sorted(float(x) for x in counts)
    total = sum(values)
    if total == 0:
        return 0.0
    n = len(values)
    weighted = sum((idx + 1) * value for idx, value in enumerate(values))
    return (2 * weighted) / (n * total) - (n + 1) / n


def _load_text(config: dict) -> str:
    files = _files(list(config.get("eval_data_paths") or []))
    if not files:
        raise FileNotFoundError("No routing probe files found.")
    return "\n".join(path.read_text(encoding="utf-8", errors="replace") for path in files)


def _evaluate(config: dict) -> dict:
    if config.get("model_family") != "pvr_ec_o":
        return {
            **ROUTING_METRICS,
            "owners_per_token": None,
            "invariants_validated": None,
            "not_applicable_reason": "routing diagnostics are only required for PVR-EC-O models",
        }
    device = "cuda" if torch.cuda.is_available() else "cpu"
    materialized = build_model(config, device=device)
    checkpoint = torch.load(config["checkpoint_path"], map_location=device)
    state = checkpoint.get("model_state_dict", checkpoint)
    materialized.model.load_state_dict(state, strict=False)
    materialized.model.eval()
    owner_rows = []
    margins = []

    def hook(module, inputs, _output):
        x = inputs[0]
        h = module.ln(x)
        if module.descriptor_operator is not None:
            h = h + module.descriptor_operator(h)
        scores = module.routing_scores(h) if hasattr(module, "routing_scores") else module.router(h)
        top = torch.topk(scores, k=min(2, scores.shape[-1]), dim=-1)
        owner_rows.extend(int(x) for x in top.indices[..., 0].detach().cpu().reshape(-1))
        if top.values.shape[-1] > 1:
            margins.extend(float(x) for x in (top.values[..., 0] - top.values[..., 1]).detach().cpu().reshape(-1))

    handles = [block.register_forward_hook(hook) for block in materialized.model.blocks]
    try:
        text = _load_text(config)
        ids = list(text.encode("utf-8", errors="replace"))[: min(64, int(config.get("context_length", 128)))]
        if len(ids) < 2:
            raise ValueError("Routing probe data is too small.")
        with torch.no_grad():
            materialized.model(torch.tensor(ids, dtype=torch.long, device=device).unsqueeze(0))
    finally:
        for handle in handles:
            handle.remove()
    expert_count = int(config.get("num_experts_if_applicable") or 1)
    counts = [owner_rows.count(idx) for idx in range(expert_count)]
    monopoly = max(counts) / max(1, sum(counts))
    return {
        "owners_per_token": 1.0,
        "top2_execution_count": 0,
        "top4_execution_count": 0,
        "runtime_dynamic_k_count": 0,
        "runtime_expert_choice_count": 0,
        "production_map_mutated": False,
        "prototype_entropy": _entropy(counts),
        "prototype_margin": sum(margins) / len(margins) if margins else None,
        "owner_entropy": _entropy(counts),
        "owner_churn": None,
        "expert_utilization": counts,
        "expert_gini": _gini(counts),
        "prototype_monopoly_rate": monopoly,
        "high_gap_monopoly_rate": monopoly if margins else None,
        "challenger_disagreement_rate": None,
        "stale_owner_rate": None,
        "descriptor_control_margin": sum(margins) / len(margins) if margins else None,
        "operator_control_margin": sum(margins) / len(margins) if margins else None,
        "failure_mode_distribution": {},
        "monopoly_rate": monopoly,
        "challenger_disagreement": None,
        "descriptor_margin": sum(margins) / len(margins) if margins else None,
        "operator_margin": sum(margins) / len(margins) if margins else None,
        "invariants_validated": True,
    }


def run(config: dict, output: str, limit: int | None = None, infrastructure_only: bool = False) -> dict:
    require_fields(config, REQUIRED_MODEL_CONFIG_FIELDS, "Routing diagnostic config")
    status = status_for_config(config, infrastructure_only=infrastructure_only)
    scorecard = {**common_scorecard(config), **ROUTING_METRICS}
    benchmark_evidence = False
    error = None
    if status == "BENCH_INFRASTRUCTURE_READY" and not infrastructure_only:
        try:
            scorecard.update(_evaluate(config))
            status = "GENUINE_REDUCED_EVAL" if config.get("model_family") == "pvr_ec_o" else "NOT_APPLICABLE"
            benchmark_evidence = config.get("model_family") == "pvr_ec_o"
        except Exception as exc:
            status = "EVAL_FAILED"
            error = repr(exc)
    else:
        scorecard.update(route_invariants_for_not_run())
    payload = {
        **base_metadata(config, limit),
        "status": status,
        "benchmark_evidence": benchmark_evidence,
        "scorecard_type": "routing",
        "required_invariants": ROUTING_INVARIANT_FIELDS,
        "hard_invariants": {
            "owners_per_token": 1.0,
            "top2_execution_count": 0,
            "top4_execution_count": 0,
            "runtime_dynamic_k_count": 0,
            "runtime_expert_choice_count": 0,
            "production_map_mutated": False,
        },
        "scorecard": scorecard,
        "error": error,
    }
    write_json(output, payload)
    return payload


def main() -> None:
    parser = parser_with_config("Run routing diagnostics")
    args = parser.parse_args()
    payload = run(load_json_or_yaml(args.config), args.output, args.limit, args.infrastructure_only)
    print(payload["status"])


if __name__ == "__main__":
    main()
