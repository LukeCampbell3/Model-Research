"""Generate expert-card interpretability artifacts from an expert probe report."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from benchmark.common import git_commit, utc_now, write_json


STATUS_COMPLETE = "PVR_EXPERT_CARD_REPORT_GENERATION_COMPLETE"
STATUS_INPUT_NOT_SUPPORTED = "PVR_EXPERT_CARD_REPORT_INPUT_NOT_SUPPORTED"


def _load_json(path: str | Path) -> dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _top_items(mapping: dict[str, float], *, reverse: bool, limit: int) -> list[dict[str, Any]]:
    return [
        {"token_class": key, "benefit": value}
        for key, value in sorted(mapping.items(), key=lambda item: item[1], reverse=reverse)[:limit]
    ]


def _dist(values: list[float]) -> dict[str, Any]:
    if not values:
        return {"count": 0, "mean": None, "min": None, "max": None}
    ordered = sorted(values)
    return {
        "count": len(values),
        "mean": sum(values) / len(values),
        "min": ordered[0],
        "p50": ordered[len(ordered) // 2],
        "p95": ordered[min(len(ordered) - 1, int(0.95 * (len(ordered) - 1)))],
        "max": ordered[-1],
    }


def _example_distributions(card: dict[str, Any]) -> dict[str, Any]:
    examples = list(card.get("top_positive_examples") or []) + list(card.get("top_negative_examples") or [])
    return {
        "route_margin_examples": _dist([
            float(item["route_margin"])
            for item in examples
            if isinstance(item.get("route_margin"), (int, float))
        ]),
        "delta_norm_examples": _dist([
            float(item["delta_norm"])
            for item in examples
            if isinstance(item.get("delta_norm"), (int, float))
        ]),
    }


def _expert_card(expert_id: str, card: dict[str, Any], *, class_limit: int, example_limit: int) -> dict[str, Any]:
    token_benefit = {
        key: float(value)
        for key, value in (card.get("token_class_benefit") or {}).items()
        if isinstance(value, (int, float))
    }
    top_benefit = _top_items(token_benefit, reverse=True, limit=class_limit)
    top_harm = _top_items(token_benefit, reverse=False, limit=class_limit)
    return {
        "expert_id": expert_id,
        "activation_count": card.get("activation_count"),
        "total_assigned_benefit": card.get("total_assigned_benefit"),
        "mean_assigned_benefit": card.get("mean_assigned_benefit"),
        "positive_benefit_rate": card.get("positive_benefit_rate"),
        "mean_positive_benefit": card.get("mean_positive_benefit"),
        "mean_harm": card.get("mean_harm"),
        "structured_benefit": card.get("structured_benefit"),
        "prose_benefit": card.get("prose_benefit"),
        "structured_prose_benefit_ratio": card.get("structured_prose_benefit_ratio"),
        "mean_route_margin": card.get("mean_route_margin"),
        "mean_delta_norm": card.get("mean_delta_norm"),
        "top_benefit_token_classes": top_benefit,
        "top_harm_token_classes": top_harm,
        "top_positive_examples": list(card.get("top_positive_examples") or [])[:example_limit],
        "top_negative_examples": list(card.get("top_negative_examples") or [])[:example_limit],
        "example_distributions": _example_distributions(card),
        "interpretation": _interpret_card(top_benefit, top_harm, card),
    }


def _interpret_card(top_benefit: list[dict[str, Any]], top_harm: list[dict[str, Any]], card: dict[str, Any]) -> str:
    benefit_classes = [item["token_class"] for item in top_benefit[:4]]
    harm_classes = [item["token_class"] for item in top_harm[:3] if item["benefit"] < 0]
    ratio = card.get("structured_prose_benefit_ratio")
    role = "structured/syntax residual" if isinstance(ratio, (int, float)) and ratio >= 2.0 else "mixed residual"
    harm = f"; harm concentrated in {', '.join(harm_classes)}" if harm_classes else ""
    return f"{role}; strongest benefit on {', '.join(benefit_classes)}{harm}."


def _rankings(cards: list[dict[str, Any]]) -> dict[str, Any]:
    def numeric(card: dict[str, Any], key: str) -> float:
        value = card.get(key)
        return float(value) if isinstance(value, (int, float)) else float("-inf")

    return {
        "total_assigned_benefit_desc": [
            {"expert_id": card["expert_id"], "total_assigned_benefit": card["total_assigned_benefit"]}
            for card in sorted(cards, key=lambda item: numeric(item, "total_assigned_benefit"), reverse=True)
        ],
        "structured_prose_ratio_desc": [
            {"expert_id": card["expert_id"], "structured_prose_benefit_ratio": card["structured_prose_benefit_ratio"]}
            for card in sorted(cards, key=lambda item: numeric(item, "structured_prose_benefit_ratio"), reverse=True)
        ],
        "activation_count_desc": [
            {"expert_id": card["expert_id"], "activation_count": card["activation_count"]}
            for card in sorted(cards, key=lambda item: numeric(item, "activation_count"), reverse=True)
        ],
    }


def run(
    *,
    input_report: str = "benchmark/reports/generated/expert_function_probe_audit/expert_function_probe_audit_report.json",
    output: str = "benchmark/reports/generated/expert_cards",
    class_limit: int = 6,
    example_limit: int = 5,
) -> dict[str, Any]:
    source = _load_json(input_report)
    supported = source.get("status") == "PVR_EXPERT_FUNCTION_PROBE_SUPPORTED"
    cards = [
        _expert_card(expert_id, card, class_limit=class_limit, example_limit=example_limit)
        for expert_id, card in sorted((source.get("metrics", {}).get("global_expert_cards") or {}).items())
    ]
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "git_commit": git_commit(),
        "status": STATUS_COMPLETE if supported else STATUS_INPUT_NOT_SUPPORTED,
        "experiment": "PVR_EXPERT_CARD_REPORT_GENERATION",
        "source_report": input_report,
        "source_status": source.get("status"),
        "candidate_config": source.get("candidate_config"),
        "overall": source.get("metrics", {}).get("overall"),
        "expert_cards": cards,
        "rankings": _rankings(cards),
        "interpretability_scope": (
            "Post-hoc functional expert cards are supported by the probe report. "
            "They do not prove route-margin interpretability, semantic owner geometry, or expert-delta causality."
        ),
    }
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    write_json(out / "expert_card_report.json", payload)
    _write_markdown(out / "expert_card_report.md", payload)
    return payload


def _write_markdown(path: Path, payload: dict[str, Any]) -> None:
    lines = [
        "# PVR Expert Card Report",
        "",
        f"Status: `{payload['status']}`",
        "",
        payload["interpretability_scope"],
        "",
        "| expert | activations | total benefit | mean benefit | structured/prose | top benefit classes | top harm classes |",
        "|---|---:|---:|---:|---:|---|---|",
    ]
    for card in payload["expert_cards"]:
        benefit = ", ".join(item["token_class"] for item in card["top_benefit_token_classes"][:4])
        harm = ", ".join(item["token_class"] for item in card["top_harm_token_classes"][:4])
        lines.append(
            f"| {card['expert_id']} | {card['activation_count']} | {card['total_assigned_benefit']} | "
            f"{card['mean_assigned_benefit']} | {card['structured_prose_benefit_ratio']} | {benefit} | {harm} |"
        )
    lines.extend(["", "## Cards", ""])
    for card in payload["expert_cards"]:
        lines.extend([
            f"### Expert {card['expert_id']}",
            "",
            card["interpretation"],
            "",
            f"- Activations: `{card['activation_count']}`",
            f"- Total assigned benefit: `{card['total_assigned_benefit']}`",
            f"- Positive assignment rate: `{card['positive_benefit_rate']}`",
            f"- Mean route margin: `{card['mean_route_margin']}`",
            f"- Mean delta norm: `{card['mean_delta_norm']}`",
            "",
        ])
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-report", default="benchmark/reports/generated/expert_function_probe_audit/expert_function_probe_audit_report.json")
    parser.add_argument("--output", default="benchmark/reports/generated/expert_cards")
    parser.add_argument("--class-limit", type=int, default=6)
    parser.add_argument("--example-limit", type=int, default=5)
    args = parser.parse_args()
    payload = run(
        input_report=args.input_report,
        output=args.output,
        class_limit=args.class_limit,
        example_limit=args.example_limit,
    )
    print(payload["status"])


if __name__ == "__main__":
    main()
