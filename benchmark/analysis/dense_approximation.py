"""Dense-approximation and route-conditional loss diagnostics.

This analysis is intentionally diagnostic-only. It does not add routing
complexity, does not change Top1 execution, and does not treat confidence
regularization as a repair path. Its purpose is to answer whether PVR-EC-O is
close enough to dense behavior before specialization is trusted.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from statistics import median
from typing import Any

from benchmark.common import git_commit, utc_now, write_json


DENSE_STATUS_GAP_IDENTIFIED = "PVR_DENSE_APPROXIMATION_GAP_IDENTIFIED"
ROUTE_WIN_STATUS = "PVR_ROUTE_CONDITIONAL_LOSS_WIN_SUPPORTED"
INCONCLUSIVE_STATUS = "PVR_DENSE_APPROXIMATION_DIAGNOSTIC_INCONCLUSIVE"


def _read_json(path: str | Path) -> dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _maybe_json(path: str | Path) -> dict[str, Any]:
    p = Path(path)
    return _read_json(p) if p.exists() else {}


def _mean(values: list[float | int | None]) -> float | None:
    xs = [float(value) for value in values if isinstance(value, (int, float))]
    return sum(xs) / len(xs) if xs else None


def _comparison_path(size: str) -> Path:
    preferred = Path(f"benchmark/reports/generated/comparison_{size}_real_4k/benchmark_comparison_report.json")
    if preferred.exists():
        return preferred
    return Path(f"benchmark/reports/generated/comparison_{size}_real/benchmark_comparison_report.json")


def _training_dir(size: str, model: str) -> Path:
    return Path(f"benchmark/reports/generated/training_{size}_real_4k") / model


def _row_by_model(comparison: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {str(row.get("model")): row for row in comparison.get("rows", [])}


def _curve(path: Path, key: str) -> list[dict[str, Any]]:
    return _maybe_json(path).get(key, [])


def _paired_eval_windows(size: str, pvr_model: str, dense_model: str) -> list[dict[str, Any]]:
    pvr_eval = _curve(_training_dir(size, pvr_model) / "eval_curve.json", "eval_curve")
    dense_eval = _curve(_training_dir(size, dense_model) / "eval_curve.json", "eval_curve")
    pvr_routing = _curve(_training_dir(size, pvr_model) / "routing_curve.json", "routing_curve")
    dense_by_step = {row.get("step"): row for row in dense_eval}
    routing_by_step = {row.get("step"): row for row in pvr_routing}
    margins = [
        float(row.get("prototype_margin"))
        for row in pvr_routing
        if isinstance(row.get("prototype_margin"), (int, float))
    ]
    margin_median = median(margins) if margins else None
    rows = []
    for pvr_row in pvr_eval:
        step = pvr_row.get("step")
        dense_row = dense_by_step.get(step)
        routing_row = routing_by_step.get(step, {})
        pvr_loss = pvr_row.get("eval_loss")
        dense_loss = dense_row.get("eval_loss") if dense_row else None
        margin = routing_row.get("prototype_margin")
        if not isinstance(pvr_loss, (int, float)) or not isinstance(dense_loss, (int, float)):
            continue
        high_margin = bool(isinstance(margin, (int, float)) and margin_median is not None and margin >= margin_median)
        rows.append({
            "step": step,
            "pvr_eval_loss": float(pvr_loss),
            "dense_eval_loss": float(dense_loss),
            "pvr_minus_dense_eval_loss": float(pvr_loss) - float(dense_loss),
            "prototype_margin": float(margin) if isinstance(margin, (int, float)) else None,
            "high_margin_routed_window": high_margin,
        })
    return rows


def analyze_size(size: str) -> dict[str, Any]:
    comparison_path = _comparison_path(size)
    comparison = _maybe_json(comparison_path)
    rows = _row_by_model(comparison)
    dense_model = f"dense_transformer_{size}"
    pvr_model = f"pvr_ec_o_full_{size}"
    shared_model = f"pvr_ec_o_shared_only_{size}"
    no_proto_model = f"pvr_ec_o_no_prototypes_{size}"
    generic_top2_model = f"generic_top2_moe_reference_{size}"
    dense = rows.get(dense_model, {})
    pvr = rows.get(pvr_model, {})
    shared = rows.get(shared_model, {})
    no_proto = rows.get(no_proto_model, {})
    generic_top2 = rows.get(generic_top2_model, {})
    paired = _paired_eval_windows(size, pvr_model, dense_model)
    high_margin_rows = [row for row in paired if row["high_margin_routed_window"]]
    low_margin_rows = [row for row in paired if not row["high_margin_routed_window"]]
    high_margin_gap = _mean([row["pvr_minus_dense_eval_loss"] for row in high_margin_rows])
    low_margin_gap = _mean([row["pvr_minus_dense_eval_loss"] for row in low_margin_rows])
    pvr_lm_loss = pvr.get("lm_loss")
    dense_lm_loss = dense.get("lm_loss")
    dense_gap = pvr_lm_loss - dense_lm_loss if isinstance(pvr_lm_loss, (int, float)) and isinstance(dense_lm_loss, (int, float)) else None
    shared_delta = pvr_lm_loss - shared.get("lm_loss") if isinstance(pvr_lm_loss, (int, float)) and isinstance(shared.get("lm_loss"), (int, float)) else None
    no_proto_delta = pvr_lm_loss - no_proto.get("lm_loss") if isinstance(pvr_lm_loss, (int, float)) and isinstance(no_proto.get("lm_loss"), (int, float)) else None
    top2_delta = pvr_lm_loss - generic_top2.get("lm_loss") if isinstance(pvr_lm_loss, (int, float)) and isinstance(generic_top2.get("lm_loss"), (int, float)) else None
    high_margin_dense_match = high_margin_gap is not None and high_margin_gap < 0
    route_conditional_win = (
        high_margin_dense_match
        and low_margin_gap is not None
        and high_margin_gap < low_margin_gap
    )
    dense_gap_closed = dense_gap is not None and dense_gap <= 0
    if route_conditional_win:
        status = ROUTE_WIN_STATUS
    elif dense_gap is not None:
        status = DENSE_STATUS_GAP_IDENTIFIED
    else:
        status = INCONCLUSIVE_STATUS
    return {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "git_commit": git_commit(),
        "status": status,
        "size": size,
        "comparison_path": str(comparison_path),
        "dense_model": dense_model,
        "pvr_model": pvr_model,
        "dense_lm_loss": dense_lm_loss,
        "pvr_lm_loss": pvr_lm_loss,
        "pvr_minus_dense_lm_loss": dense_gap,
        "pvr_minus_shared_only_lm_loss": shared_delta,
        "pvr_minus_no_prototypes_lm_loss": no_proto_delta,
        "pvr_minus_generic_top2_lm_loss": top2_delta,
        "dense_gap_closed": dense_gap_closed,
        "high_margin_dense_match_supported": high_margin_dense_match,
        "route_conditional_loss_win_supported": route_conditional_win,
        "paired_eval_window_count": len(paired),
        "high_margin_window_count": len(high_margin_rows),
        "low_margin_window_count": len(low_margin_rows),
        "high_margin_mean_pvr_minus_dense_eval_loss": high_margin_gap,
        "low_margin_mean_pvr_minus_dense_eval_loss": low_margin_gap,
        "paired_eval_windows": paired,
        "interpretation": _interpret(
            dense_gap=dense_gap,
            shared_delta=shared_delta,
            no_proto_delta=no_proto_delta,
            top2_delta=top2_delta,
            high_margin_gap=high_margin_gap,
            low_margin_gap=low_margin_gap,
        ),
        "forbidden_repair": {
            "route_confidence_regularization_0_01": "DO_NOT_USE_AGAIN",
            "reason": "Matched diagnostic ablation worsened train/eval loss and reduced route margin.",
        },
        "recommended_next_experiment": {
            "name": "dense_mimic_then_specialize",
            "objective": "Close the dense approximation gap before relying on expert specialization.",
            "phases": [
                "shared-heavy dense imitation",
                "strict Top1 diagnostics while keeping shared path strong",
                "expert specialization after dense gap narrows",
                "route-family loss evaluation",
            ],
        },
    }


def _interpret(
    *,
    dense_gap: float | None,
    shared_delta: float | None,
    no_proto_delta: float | None,
    top2_delta: float | None,
    high_margin_gap: float | None,
    low_margin_gap: float | None,
) -> dict[str, Any]:
    findings = []
    if dense_gap is None:
        findings.append("Dense/PVR comparison is missing.")
    elif dense_gap > 0:
        findings.append("PVR full still trails dense on global LM loss.")
    else:
        findings.append("PVR full closes or beats dense on global LM loss.")
    if shared_delta is not None and shared_delta < 0:
        findings.append("PVR full beats shared-only, so routed residuals help relative to shared-only.")
    elif shared_delta is not None:
        findings.append("PVR full does not beat shared-only; routed residuals are not buying loss.")
    if no_proto_delta is not None and no_proto_delta > 0:
        findings.append("No-prototypes beats full, so prototype structure is not helping loss yet.")
    if top2_delta is not None and top2_delta > 0:
        findings.append("Generic Top2 reference beats PVR full on LM loss.")
    if high_margin_gap is not None and high_margin_gap >= 0:
        findings.append("High-margin routed windows do not beat dense; route-conditional loss win is not supported.")
    elif high_margin_gap is not None and low_margin_gap is not None and high_margin_gap < low_margin_gap:
        findings.append("High-margin routed windows beat dense and outperform low-margin windows; route-conditional loss win is supported.")
    elif high_margin_gap is not None:
        findings.append("High-margin routed windows beat dense, but not better than low-margin windows; dense match is present but route-confidence usefulness is not supported.")
    if high_margin_gap is not None and low_margin_gap is not None:
        findings.append("High-vs-low margin gap delta is {:.6f}.".format(high_margin_gap - low_margin_gap))
    return {
        "findings": findings,
        "bottom_line": "Dense approximation gap must be closed before adding more routing/confidence machinery.",
    }


def write_deprecation_report(output: str | Path = "benchmark/reports/generated/rba_update_deprecation_report.json") -> dict[str, Any]:
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "status": "RBA_ROUTE_CONFIDENCE_UPDATE_DEPRECATED",
        "do_not_use_again": [
            "in_bounds_probability_head_as_currently_implemented",
            "route_confidence_regularization_0_01",
            "margin_proxy_confidence_as_capability_claim",
        ],
        "evidence": "Matched 100M diagnostic ablation worsened train/eval loss and reduced route margin.",
        "replacement_direction": "dense approximation first, routing specialization second, efficiency compression third",
    }
    write_json(output, payload)
    md = [
        "# RBA Update Deprecation Report",
        "",
        "Status: `RBA_ROUTE_CONFIDENCE_UPDATE_DEPRECATED`",
        "",
        "Do not use the previous in-bounds head plus route-confidence regularization update again as a repair path.",
        "It changed confidence metadata but worsened matched diagnostic loss and reduced route margin.",
        "",
        "Recommended replacement: dense approximation first, routing specialization second, efficiency compression third.",
    ]
    Path(str(output).replace(".json", ".md")).write_text("\n".join(md), encoding="utf-8")
    return payload


def run(size: str = "300m", output: str | Path | None = None) -> dict[str, Any]:
    payload = analyze_size(size)
    out = Path(output or f"benchmark/reports/generated/dense_approximation_{size}")
    out.mkdir(parents=True, exist_ok=True)
    write_json(out / "dense_approximation_report.json", payload)
    write_json(out / "route_conditional_loss_windows.json", {
        "schema_version": "1.0",
        "status": payload["status"],
        "size": size,
        "paired_eval_windows": payload["paired_eval_windows"],
    })
    md = [
        "# Dense Approximation Diagnostic",
        "",
        f"Status: `{payload['status']}`",
        "",
        f"PVR minus dense LM loss: `{payload['pvr_minus_dense_lm_loss']}`",
        f"High-margin PVR minus dense eval loss: `{payload['high_margin_mean_pvr_minus_dense_eval_loss']}`",
        f"Low-margin PVR minus dense eval loss: `{payload['low_margin_mean_pvr_minus_dense_eval_loss']}`",
        "",
        "Conclusion: " + payload["interpretation"]["bottom_line"],
    ]
    (out / "dense_approximation_report.md").write_text("\n".join(md), encoding="utf-8")
    write_deprecation_report()
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description="Run dense-approximation diagnostics")
    parser.add_argument("--size", default="300m")
    parser.add_argument("--output", default=None)
    args = parser.parse_args()
    payload = run(size=args.size, output=args.output)
    print(payload["status"])


if __name__ == "__main__":
    main()
