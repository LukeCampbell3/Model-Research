"""Inspect bad training-window spans for the EAN init candidate."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

import torch
import torch.nn.functional as F

from benchmark.common import git_commit, load_json_or_yaml, utc_now, write_json
from benchmark.model_factory import build_model
from benchmark.runners.run_training import _batch, _files


STATUS_COMPLETE = "PVR_EAN_BAD_TOKEN_SPAN_INSPECTION_COMPLETE"

MODEL_CONFIGS = {
    "dense_300m": "benchmark/configs/generated/dense_transformer_300m.yaml",
    "pvr_baseline_seed42": "benchmark/reports/generated/shared_trunk_init_300m_repeat_seed_42/pvr_ec_o_full_300m_baseline_seed_42/run_config.yaml",
    "full_copy_seed42": "benchmark/reports/generated/shared_trunk_init_300m_repeat_seed_42/pvr_ec_o_full_300m_shared_trunk_init_from_dense_seed_42/run_config.yaml",
    "ean_seed42": "benchmark/reports/generated/ean_init_300m_repeat_seed_42/pvr_ec_o_full_300m_shared_trunk_init_v1_scope_embeddings_attention_norms_seed_42/run_config.yaml",
}


def _load_json(path: str | Path) -> dict[str, Any]:
    return json.loads(Path(str(path).replace("\\", "/")).read_text(encoding="utf-8"))


def _load_eval_bytes_with_sources(paths: list[str]) -> tuple[torch.Tensor, list[dict[str, Any]]]:
    chunks = bytearray()
    sources = []
    for path in _files(paths):
        start = len(chunks)
        data = path.read_bytes()
        chunks.extend(data)
        end = len(chunks)
        sources.append({"path": str(path), "start": start, "end": end})
        chunks.append(10)
    return torch.tensor(list(chunks), dtype=torch.long), sources


def _source_for_offset(sources: list[dict[str, Any]], offset: int) -> dict[str, Any]:
    for source in sources:
        if int(source["start"]) <= offset < int(source["end"]):
            return {
                "path": source["path"],
                "offset_in_source": offset - int(source["start"]),
            }
    return {"path": None, "offset_in_source": None}


def _load_model(config: dict[str, Any], device: str):
    materialized = build_model(config, device=device)
    checkpoint = torch.load(config["checkpoint_path"], map_location=device)
    state = checkpoint.get("model_state_dict", checkpoint)
    materialized.model.load_state_dict(state, strict=False)
    materialized.model.eval()
    return materialized.model


def _per_token_losses(model, x: torch.Tensor, y: torch.Tensor) -> tuple[float, list[float], list[int]]:
    with torch.no_grad():
        logits = model(x)
        losses = F.cross_entropy(logits.reshape(-1, logits.shape[-1]), y.reshape(-1), reduction="none").view_as(y)
        pred = torch.argmax(logits, dim=-1)
    return (
        float(losses.mean().detach().cpu().item()),
        [float(item) for item in losses.detach().cpu().reshape(-1)],
        [int(item) for item in pred.detach().cpu().reshape(-1)],
    )


def _route_trace(model, config: dict[str, Any], x: torch.Tensor) -> dict[str, Any] | None:
    if config.get("model_family") != "pvr_ec_o" or not hasattr(model, "blocks"):
        return None
    traces: list[dict[str, Any]] = []

    def hook(module, inputs, _output):
        with torch.no_grad():
            h = module.ln(inputs[0])
            if module.descriptor_operator is not None:
                h = h + module.descriptor_operator(h)
            scores = module.router(h)
            top = torch.topk(scores, k=min(2, scores.shape[-1]), dim=-1)
            owners = top.indices[..., 0].detach().cpu().reshape(-1).tolist()
            margins = (
                (top.values[..., 0] - top.values[..., 1]).detach().cpu().reshape(-1).tolist()
                if top.values.shape[-1] > 1
                else []
            )
            traces.append({"owners": [int(item) for item in owners], "margins": [float(item) for item in margins]})

    handles = [block.register_forward_hook(hook) for block in model.blocks]
    try:
        with torch.no_grad():
            model(x)
    finally:
        for handle in handles:
            handle.remove()
    if not traces:
        return None
    token_count = len(traces[0]["owners"])
    owner_ids = []
    route_margins = []
    for idx in range(token_count):
        owners = [layer["owners"][idx] for layer in traces if idx < len(layer["owners"])]
        margins = [layer["margins"][idx] for layer in traces if idx < len(layer["margins"])]
        owner_ids.append(owners)
        route_margins.append(sum(margins) / len(margins) if margins else None)
    flat_owners = [owner for token in owner_ids for owner in token]
    counts = {str(owner): flat_owners.count(owner) for owner in sorted(set(flat_owners))}
    return {
        "owner_ids_by_token": owner_ids,
        "mean_route_margin_by_token": route_margins,
        "owner_histogram": counts,
        "mean_route_margin": sum(m for m in route_margins if m is not None) / max(1, sum(m is not None for m in route_margins)),
    }


def _span_stats(tokens: list[int], text: str) -> dict[str, Any]:
    printable = sum(32 <= token <= 126 for token in tokens)
    controls = sum(token < 32 or token == 127 for token in tokens)
    unknown = sum(token > 127 for token in tokens)
    repeated = sum(1 for a, b in zip(tokens, tokens[1:]) if a == b)
    lowered = text.lower()
    return {
        "sequence_length": len(tokens),
        "special_token_density": controls / max(1, len(tokens)),
        "unknown_or_non_ascii_density": unknown / max(1, len(tokens)),
        "printable_ascii_density": printable / max(1, len(tokens)),
        "repeated_token_rate": repeated / max(1, len(tokens) - 1),
        "code_marker_count": sum(lowered.count(item) for item in ["def ", "class ", "import ", "{", "}", "return", "lambda"]),
        "math_marker_count": sum(lowered.count(item) for item in ["=", "+", "-", "*", "/", "prime", "number"]),
        "schema_marker_count": sum(lowered.count(item) for item in ["json", "schema", "type", "properties", "required"]),
    }


def _high_conf_high_loss_tokens(
    *,
    token_ids: list[int],
    target_ids: list[int],
    text: str,
    ean_losses: list[float],
    baseline_losses: list[float],
    route_trace: dict[str, Any] | None,
    top_k: int = 16,
) -> list[dict[str, Any]]:
    margins = route_trace.get("mean_route_margin_by_token", []) if route_trace else []
    owners = route_trace.get("owner_ids_by_token", []) if route_trace else []
    rows = []
    for idx, loss in enumerate(ean_losses):
        margin = margins[idx] if idx < len(margins) else None
        rows.append({
            "position": idx,
            "input_token_id": token_ids[idx] if idx < len(token_ids) else None,
            "target_token_id": target_ids[idx] if idx < len(target_ids) else None,
            "target_char": chr(target_ids[idx]) if idx < len(target_ids) and 32 <= target_ids[idx] <= 126 else repr(bytes([target_ids[idx]])) if idx < len(target_ids) else None,
            "ean_loss": loss,
            "baseline_loss": baseline_losses[idx] if idx < len(baseline_losses) else None,
            "ean_minus_baseline_loss": loss - baseline_losses[idx] if idx < len(baseline_losses) else None,
            "route_margin": margin,
            "owner_ids": owners[idx] if idx < len(owners) else None,
            "context_excerpt": text[max(0, idx - 24): idx + 24],
        })
    rows.sort(key=lambda item: ((item["route_margin"] or 0.0), item["ean_loss"]), reverse=True)
    return rows[:top_k]


def _robust_delta_stats(values: list[float]) -> dict[str, Any]:
    if not values:
        return {}
    ordered = sorted(values)
    trim = max(0, int(len(ordered) * 0.1))
    trimmed = ordered[trim: len(ordered) - trim] if len(ordered) - trim > trim else ordered
    return {
        "mean_delta": sum(values) / len(values),
        "median_delta": ordered[len(ordered) // 2],
        "trimmed_mean_delta": sum(trimmed) / len(trimmed),
        "wins": sum(value < 0 for value in values),
        "total": len(values),
        "worst_window_delta": max(values),
        "best_window_delta": min(values),
        "outlier_count_gt_1_loss": sum(value > 1.0 for value in values),
        "outlier_contribution_to_mean": sum(value for value in values if value > 1.0) / len(values),
    }


def _bad_windows_from_alignment(path: str, limit: int) -> list[dict[str, Any]]:
    report = _load_json(path)
    windows = report["rows"]["ean_seed42"]["per_window_deltas_vs_pvr_baseline"]["training_window_style_final_checkpoint"]
    ordered = sorted(
        [window for window in windows if isinstance(window.get("delta_vs_baseline"), (int, float))],
        key=lambda item: float(item["delta_vs_baseline"]),
        reverse=True,
    )
    return ordered[:limit]


def run(
    *,
    output: str = "benchmark/reports/generated/ean_bad_token_span_inspection",
    alignment_report: str = "benchmark/reports/generated/ean_scorecard_eval_curve_alignment_audit/alignment_audit_report.json",
    limit: int = 4,
    device: str = "cuda",
    seq_len: int = 128,
) -> dict[str, Any]:
    if device == "cuda" and not torch.cuda.is_available():
        device = "cpu"
    configs = {name: load_json_or_yaml(path) for name, path in MODEL_CONFIGS.items()}
    eval_tokens, sources = _load_eval_bytes_with_sources(list(configs["ean_seed42"].get("eval_data_paths") or []))
    models = {name: _load_model(config, device) for name, config in configs.items()}
    bad_windows = _bad_windows_from_alignment(alignment_report, limit)
    inspected = []
    for window in bad_windows:
        step = int(window["step"])
        step_idx = max(0, step - 1)
        x, y = _batch(eval_tokens, step_idx, 1, seq_len, device)
        span = x.detach().cpu().reshape(-1).tolist()
        targets = y.detach().cpu().reshape(-1).tolist()
        start = ((step_idx * 1) * (seq_len + 1)) % max(1, len(eval_tokens) - (seq_len + 1))
        text = bytes(span).decode("utf-8", errors="replace")
        target_text = bytes(targets).decode("utf-8", errors="replace")
        model_losses: dict[str, Any] = {}
        route_traces: dict[str, Any] = {}
        for name, model in models.items():
            mean_loss, per_token, pred = _per_token_losses(model, x, y)
            model_losses[name] = {
                "mean_loss": mean_loss,
                "per_token_loss": per_token,
                "predicted_token_ids": pred,
            }
            trace = _route_trace(model, configs[name], x)
            if trace is not None:
                route_traces[name] = trace
        ean_losses = model_losses["ean_seed42"]["per_token_loss"]
        baseline_losses = model_losses["pvr_baseline_seed42"]["per_token_loss"]
        per_token_rows = []
        for idx, loss in enumerate(ean_losses):
            per_token_rows.append({
                "position": idx,
                "input_token_id": span[idx],
                "target_token_id": targets[idx],
                "target_char": chr(targets[idx]) if 32 <= targets[idx] <= 126 else repr(bytes([targets[idx]])),
                "dense_loss": model_losses["dense_300m"]["per_token_loss"][idx],
                "baseline_pvr_loss": baseline_losses[idx],
                "full_copy_loss": model_losses["full_copy_seed42"]["per_token_loss"][idx],
                "ean_loss": loss,
                "ean_minus_baseline_loss": loss - baseline_losses[idx],
                "ean_route_margin": (
                    route_traces.get("ean_seed42", {}).get("mean_route_margin_by_token", [None] * len(ean_losses))[idx]
                ),
                "ean_owner_ids": (
                    route_traces.get("ean_seed42", {}).get("owner_ids_by_token", [None] * len(ean_losses))[idx]
                ),
            })
        per_token_rows_sorted = sorted(per_token_rows, key=lambda item: item["ean_minus_baseline_loss"], reverse=True)
        inspected.append({
            "window_id": f"step_{step}",
            "step": step,
            "start_offset_in_concatenated_eval_bytes": start,
            "source": _source_for_offset(sources, start),
            "raw_decoded_text": text,
            "target_decoded_text": target_text,
            "token_ids": span,
            "target_token_ids": targets,
            "span_stats": _span_stats(span, text),
            "alignment_delta_vs_baseline": window.get("delta_vs_baseline"),
            "model_mean_losses": {name: info["mean_loss"] for name, info in model_losses.items()},
            "model_loss_deltas_vs_baseline": {
                name: info["mean_loss"] - model_losses["pvr_baseline_seed42"]["mean_loss"]
                for name, info in model_losses.items()
            },
            "route_summaries": {
                name: {
                    "owner_histogram": trace["owner_histogram"],
                    "mean_route_margin": trace["mean_route_margin"],
                }
                for name, trace in route_traces.items()
            },
            "worst_ean_minus_baseline_tokens": per_token_rows_sorted[:24],
            "high_confidence_high_loss_tokens": _high_conf_high_loss_tokens(
                token_ids=span,
                target_ids=targets,
                text=text,
                ean_losses=ean_losses,
                baseline_losses=baseline_losses,
                route_trace=route_traces.get("ean_seed42"),
            ),
        })
    deltas = [float(item["alignment_delta_vs_baseline"]) for item in inspected if isinstance(item.get("alignment_delta_vs_baseline"), (int, float))]
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "git_commit": git_commit(),
        "status": STATUS_COMPLETE,
        "experiment": "PVR_EAN_BAD_TOKEN_SPAN_INSPECTION",
        "alignment_report": alignment_report,
        "device": device,
        "seq_len": seq_len,
        "inspected_window_count": len(inspected),
        "robust_bad_window_delta_stats": _robust_delta_stats(deltas),
        "windows": inspected,
        "interpretation": "Inspect whether high-loss training eval windows are real weaknesses or eval artifacts before changing model design.",
    }
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    write_json(out / "bad_token_span_inspection_report.json", payload)
    _write_markdown(out / "bad_token_span_inspection_report.md", payload)
    return payload


def _write_markdown(path: Path, payload: dict[str, Any]) -> None:
    lines = [
        "# EAN Bad Token Span Inspection",
        "",
        f"Status: `{payload['status']}`",
        "",
        "| window | source | delta | EAN loss | baseline loss | controls | code markers | schema markers |",
        "|---|---|---:|---:|---:|---:|---:|---:|",
    ]
    for window in payload["windows"]:
        stats = window["span_stats"]
        losses = window["model_mean_losses"]
        lines.append(
            f"| {window['window_id']} | {window['source']['path']} | {window['alignment_delta_vs_baseline']} | "
            f"{losses['ean_seed42']} | {losses['pvr_baseline_seed42']} | "
            f"{stats['special_token_density']} | {stats['code_marker_count']} | {stats['schema_marker_count']} |"
        )
    lines.extend(["", "```json", json.dumps(payload, indent=2, sort_keys=True, default=str), "```", ""])
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="benchmark/reports/generated/ean_bad_token_span_inspection")
    parser.add_argument("--alignment-report", default="benchmark/reports/generated/ean_scorecard_eval_curve_alignment_audit/alignment_audit_report.json")
    parser.add_argument("--limit", type=int, default=4)
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--seq-len", type=int, default=128)
    args = parser.parse_args()
    payload = run(output=args.output, alignment_report=args.alignment_report, limit=args.limit, device=args.device, seq_len=args.seq_len)
    print(payload["status"])


if __name__ == "__main__":
    main()
