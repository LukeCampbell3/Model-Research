"""Audit routing and expert-delta behavior on EAN structured-span outliers."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any

import torch
import torch.nn.functional as F

from benchmark.common import git_commit, load_json_or_yaml, utc_now, write_json
from benchmark.model_factory import build_model
from benchmark.runners.run_training import _batch
from benchmark.analysis.run_ean_bad_token_span_inspection import (
    MODEL_CONFIGS,
    _load_eval_bytes_with_sources,
    _source_for_offset,
)


STATUS_COMPLETE = "PVR_EAN_STRUCTURED_SPAN_ROUTE_AUDIT_COMPLETE"
STATUS_ROUTE_SHIFT_DELTA_HARM = "PVR_EAN_STRUCTURED_SPAN_ROUTE_SHIFT_AND_DELTA_HARM_OBSERVED"


def _load_json(path: str | Path) -> dict[str, Any]:
    return json.loads(Path(str(path).replace("\\", "/")).read_text(encoding="utf-8"))


def _load_model(config: dict[str, Any], device: str):
    materialized = build_model(config, device=device)
    checkpoint = torch.load(config["checkpoint_path"], map_location=device)
    state = checkpoint.get("model_state_dict", checkpoint)
    materialized.model.load_state_dict(state, strict=False)
    materialized.model.eval()
    return materialized.model


def _losses_from_logits(logits: torch.Tensor, y: torch.Tensor) -> list[float]:
    losses = F.cross_entropy(logits.reshape(-1, logits.shape[-1]), y.reshape(-1), reduction="none").view_as(y)
    return [float(item) for item in losses.detach().cpu().reshape(-1)]


def _forward_logits(model, x: torch.Tensor) -> torch.Tensor:
    with torch.no_grad():
        return model(x)


def _forward_shared_only_logits(model, config: dict[str, Any], x: torch.Tensor) -> torch.Tensor | None:
    if config.get("model_family") != "pvr_ec_o" or not hasattr(model, "blocks"):
        return None
    handles = []

    def hook(module, inputs, _output):
        with torch.no_grad():
            incoming = inputs[0]
            h = module.ln(incoming)
            if module.descriptor_operator is not None:
                h = h + module.descriptor_operator(h)
            return incoming + module.shared(h)

    try:
        handles = [block.register_forward_hook(hook) for block in model.blocks]
        with torch.no_grad():
            return model(x)
    finally:
        for handle in handles:
            handle.remove()


def _route_and_delta_trace(model, config: dict[str, Any], x: torch.Tensor) -> dict[str, Any] | None:
    if config.get("model_family") != "pvr_ec_o" or not hasattr(model, "blocks"):
        return None
    traces = []

    def hook(module, inputs, _output):
        with torch.no_grad():
            incoming = inputs[0]
            h = module.ln(incoming)
            if module.descriptor_operator is not None:
                h = h + module.descriptor_operator(h)
            scores = module.router(h)
            top = torch.topk(scores, k=min(2, scores.shape[-1]), dim=-1)
            owners = top.indices[..., 0]
            margins = top.values[..., 0] - top.values[..., 1] if top.values.shape[-1] > 1 else torch.zeros_like(owners, dtype=h.dtype)
            sparse = torch.zeros_like(incoming)
            delta_norm = torch.zeros_like(owners, dtype=h.dtype)
            for expert_id, expert in enumerate(module.experts):
                mask = owners == expert_id
                if mask.any():
                    expert_out = expert(h[mask])
                    sparse[mask] = expert_out
                    delta_norm[mask] = torch.linalg.vector_norm(expert_out, dim=-1)
            proto_ids = None
            proto_margins = None
            if module.prototypes is not None:
                proto_scores = torch.matmul(F.normalize(h, dim=-1), F.normalize(module.prototypes, dim=-1).T)
                proto_top = torch.topk(proto_scores, k=min(2, proto_scores.shape[-1]), dim=-1)
                proto_ids = proto_top.indices[..., 0]
                proto_margins = proto_top.values[..., 0] - proto_top.values[..., 1] if proto_top.values.shape[-1] > 1 else torch.zeros_like(owners, dtype=h.dtype)
            traces.append({
                "owners": owners.detach().cpu().reshape(-1).tolist(),
                "margins": margins.detach().cpu().reshape(-1).tolist(),
                "expert_delta_norm": delta_norm.detach().cpu().reshape(-1).tolist(),
                "prototype_ids": proto_ids.detach().cpu().reshape(-1).tolist() if proto_ids is not None else None,
                "prototype_margins": proto_margins.detach().cpu().reshape(-1).tolist() if proto_margins is not None else None,
            })

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
    by_token = []
    flat_owners = []
    for idx in range(token_count):
        owners = [int(layer["owners"][idx]) for layer in traces if idx < len(layer["owners"])]
        margins = [float(layer["margins"][idx]) for layer in traces if idx < len(layer["margins"])]
        norms = [float(layer["expert_delta_norm"][idx]) for layer in traces if idx < len(layer["expert_delta_norm"])]
        protos = [
            int(layer["prototype_ids"][idx])
            for layer in traces
            if layer.get("prototype_ids") is not None and idx < len(layer["prototype_ids"])
        ]
        proto_margins = [
            float(layer["prototype_margins"][idx])
            for layer in traces
            if layer.get("prototype_margins") is not None and idx < len(layer["prototype_margins"])
        ]
        flat_owners.extend(owners)
        by_token.append({
            "owner_ids": owners,
            "mean_owner_id": sum(owners) / max(1, len(owners)),
            "mean_route_margin": sum(margins) / max(1, len(margins)),
            "mean_expert_delta_norm": sum(norms) / max(1, len(norms)),
            "prototype_ids": protos,
            "mean_prototype_margin": sum(proto_margins) / max(1, len(proto_margins)) if proto_margins else None,
            "owner_churn": sum(a != b for a, b in zip(owners, owners[1:])) / max(1, len(owners) - 1),
        })
    return {
        "by_token": by_token,
        "owner_histogram": dict(Counter(str(owner) for owner in flat_owners)),
        "mean_route_margin": sum(item["mean_route_margin"] for item in by_token) / max(1, len(by_token)),
        "mean_expert_delta_norm": sum(item["mean_expert_delta_norm"] for item in by_token) / max(1, len(by_token)),
        "mean_owner_churn": sum(item["owner_churn"] for item in by_token) / max(1, len(by_token)),
    }


def _token_type(token: int, text: str, pos: int, source_path: str) -> str:
    ch = chr(token) if 0 <= token <= 255 else ""
    if ch in "{}[]()":
        return "brace_bracket_paren"
    if ch in "\"'":
        return "quote"
    if ch in ",:;":
        return "comma_colon_semicolon"
    if ch in "\r\n":
        return "newline"
    if ch in " \t":
        return "indent_or_space"
    if ch.isdigit():
        return "digit"
    if ch == "_":
        return "identifier"
    if ch.isalpha():
        line_start = text.rfind("\n", 0, pos) + 1
        line_end = text.find("\n", pos)
        if line_end < 0:
            line_end = len(text)
        line = text[line_start:line_end]
        if "def " in line[: max(0, pos - line_start) + 8]:
            return "function_signature"
        if "json" in source_path.lower() and '"' in line and ":" in line:
            return "schema_key_or_value"
        return "identifier"
    return "other"


def _group_stats(rows: list[dict[str, Any]], key: str) -> dict[str, Any]:
    grouped: dict[str, list[dict[str, Any]]] = {}
    for row in rows:
        grouped.setdefault(str(row.get(key)), []).append(row)
    out = {}
    for group, items in grouped.items():
        ean_minus_base = [float(item["ean_minus_baseline_loss"]) for item in items]
        expert_help = [float(item["ean_expert_help_delta"]) for item in items if item.get("ean_expert_help_delta") is not None]
        route_disagree = [float(item["ean_baseline_owner_disagreement_rate"]) for item in items if item.get("ean_baseline_owner_disagreement_rate") is not None]
        out[group] = {
            "count": len(items),
            "mean_ean_minus_baseline_loss": sum(ean_minus_base) / len(ean_minus_base),
            "mean_ean_expert_help_delta": sum(expert_help) / len(expert_help) if expert_help else None,
            "mean_owner_disagreement_rate": sum(route_disagree) / len(route_disagree) if route_disagree else None,
            "mean_ean_route_margin": sum(float(item["ean_route_margin"]) for item in items) / len(items),
            "mean_ean_expert_delta_norm": sum(float(item["ean_expert_delta_norm"]) for item in items) / len(items),
        }
    return out


def _positive_structured_windows(report_path: str) -> list[dict[str, Any]]:
    report = _load_json(report_path)
    return [
        item for item in report.get("windows", [])
        if isinstance(item.get("alignment_delta_vs_baseline"), (int, float)) and item["alignment_delta_vs_baseline"] > 1.0
    ]


def run(
    *,
    output: str = "benchmark/reports/generated/ean_structured_span_route_audit",
    bad_span_report: str = "benchmark/reports/generated/ean_bad_token_span_inspection/bad_token_span_inspection_report.json",
    device: str = "cuda",
    seq_len: int = 128,
) -> dict[str, Any]:
    if device == "cuda" and not torch.cuda.is_available():
        device = "cpu"
    configs = {name: load_json_or_yaml(path) for name, path in MODEL_CONFIGS.items()}
    eval_tokens, sources = _load_eval_bytes_with_sources(list(configs["ean_seed42"].get("eval_data_paths") or []))
    models = {name: _load_model(config, device) for name, config in configs.items()}
    windows = []
    for source_window in _positive_structured_windows(bad_span_report):
        step = int(source_window["step"])
        step_idx = max(0, step - 1)
        x, y = _batch(eval_tokens, step_idx, 1, seq_len, device)
        token_ids = x.detach().cpu().reshape(-1).tolist()
        target_ids = y.detach().cpu().reshape(-1).tolist()
        start = ((step_idx * 1) * (seq_len + 1)) % max(1, len(eval_tokens) - (seq_len + 1))
        text = bytes(token_ids).decode("utf-8", errors="replace")
        source = _source_for_offset(sources, start)
        full_losses = {}
        shared_losses = {}
        traces = {}
        for name, model in models.items():
            full_losses[name] = _losses_from_logits(_forward_logits(model, x), y)
            shared_logits = _forward_shared_only_logits(model, configs[name], x)
            if shared_logits is not None:
                shared_losses[name] = _losses_from_logits(shared_logits, y)
            trace = _route_and_delta_trace(model, configs[name], x)
            if trace is not None:
                traces[name] = trace
        token_rows = []
        for pos, token in enumerate(token_ids):
            ean_trace = traces["ean_seed42"]["by_token"][pos]
            base_trace = traces["pvr_baseline_seed42"]["by_token"][pos]
            full_trace = traces["full_copy_seed42"]["by_token"][pos]
            owner_disagreement = sum(a != b for a, b in zip(ean_trace["owner_ids"], base_trace["owner_ids"])) / max(1, len(ean_trace["owner_ids"]))
            token_type = _token_type(target_ids[pos], text, pos, str(source.get("path") or ""))
            ean_expert_help = (
                full_losses["ean_seed42"][pos] - shared_losses["ean_seed42"][pos]
                if "ean_seed42" in shared_losses
                else None
            )
            base_expert_help = (
                full_losses["pvr_baseline_seed42"][pos] - shared_losses["pvr_baseline_seed42"][pos]
                if "pvr_baseline_seed42" in shared_losses
                else None
            )
            token_rows.append({
                "position": pos,
                "input_token_id": token,
                "target_token_id": target_ids[pos],
                "target_char": chr(target_ids[pos]) if 32 <= target_ids[pos] <= 126 else repr(bytes([target_ids[pos]])),
                "token_type": token_type,
                "syntax_region": token_type,
                "dense_loss": full_losses["dense_300m"][pos],
                "baseline_pvr_loss": full_losses["pvr_baseline_seed42"][pos],
                "full_copy_loss": full_losses["full_copy_seed42"][pos],
                "ean_loss": full_losses["ean_seed42"][pos],
                "ean_minus_baseline_loss": full_losses["ean_seed42"][pos] - full_losses["pvr_baseline_seed42"][pos],
                "ean_expert_help_delta": ean_expert_help,
                "baseline_expert_help_delta": base_expert_help,
                "ean_minus_baseline_expert_help_delta": (
                    ean_expert_help - base_expert_help
                    if ean_expert_help is not None and base_expert_help is not None
                    else None
                ),
                "ean_owner_ids": ean_trace["owner_ids"],
                "baseline_owner_ids": base_trace["owner_ids"],
                "full_copy_owner_ids": full_trace["owner_ids"],
                "ean_baseline_owner_disagreement_rate": owner_disagreement,
                "ean_route_margin": ean_trace["mean_route_margin"],
                "baseline_route_margin": base_trace["mean_route_margin"],
                "ean_prototype_ids": ean_trace["prototype_ids"],
                "baseline_prototype_ids": base_trace["prototype_ids"],
                "ean_prototype_margin": ean_trace["mean_prototype_margin"],
                "ean_expert_delta_norm": ean_trace["mean_expert_delta_norm"],
                "baseline_expert_delta_norm": base_trace["mean_expert_delta_norm"],
                "ean_owner_churn": ean_trace["owner_churn"],
                "baseline_owner_churn": base_trace["owner_churn"],
                "context_excerpt": text[max(0, pos - 32): pos + 32],
            })
        worst = sorted(token_rows, key=lambda item: item["ean_minus_baseline_loss"], reverse=True)[:32]
        expert_harm = [row for row in token_rows if row.get("ean_expert_help_delta") is not None and row["ean_expert_help_delta"] > 0]
        route_shift_high_loss = [
            row for row in token_rows
            if row["ean_baseline_owner_disagreement_rate"] >= 0.5 and row["ean_minus_baseline_loss"] > 1.0
        ]
        windows.append({
            "window_id": source_window["window_id"],
            "step": step,
            "source": source,
            "alignment_delta_vs_baseline": source_window["alignment_delta_vs_baseline"],
            "raw_decoded_text": text,
            "route_summaries": {
                name: {
                    "owner_histogram": trace["owner_histogram"],
                    "mean_route_margin": trace["mean_route_margin"],
                    "mean_expert_delta_norm": trace["mean_expert_delta_norm"],
                    "mean_owner_churn": trace["mean_owner_churn"],
                }
                for name, trace in traces.items()
            },
            "token_type_loss_summary": _group_stats(token_rows, "token_type"),
            "syntax_region_loss_summary": _group_stats(token_rows, "syntax_region"),
            "worst_ean_minus_baseline_tokens": worst,
            "high_loss_route_shift_tokens": route_shift_high_loss[:32],
            "expert_harm_token_count": len(expert_harm),
            "route_shift_high_loss_token_count": len(route_shift_high_loss),
            "mean_ean_baseline_owner_disagreement_rate": sum(row["ean_baseline_owner_disagreement_rate"] for row in token_rows) / len(token_rows),
            "mean_ean_expert_help_delta": sum(row["ean_expert_help_delta"] for row in token_rows if row["ean_expert_help_delta"] is not None) / max(1, sum(row["ean_expert_help_delta"] is not None for row in token_rows)),
            "mean_baseline_expert_help_delta": sum(row["baseline_expert_help_delta"] for row in token_rows if row["baseline_expert_help_delta"] is not None) / max(1, sum(row["baseline_expert_help_delta"] is not None for row in token_rows)),
        })
        if device == "cuda":
            torch.cuda.empty_cache()
    route_shift = any(window["route_shift_high_loss_token_count"] > 0 for window in windows)
    delta_harm = any(window["expert_harm_token_count"] > 0 and window["mean_ean_expert_help_delta"] > 0 for window in windows)
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "git_commit": git_commit(),
        "status": STATUS_COMPLETE,
        "secondary_status": STATUS_ROUTE_SHIFT_DELTA_HARM if route_shift or delta_harm else None,
        "experiment": "PVR_EAN_STRUCTURED_SPAN_ROUTE_AUDIT",
        "candidate": "pvr_ec_o_embeddings_attention_norms_init_v1",
        "device": device,
        "seq_len": seq_len,
        "inspected_window_count": len(windows),
        "windows": windows,
        "decision": {
            "route_shift_observed_on_high_loss_tokens": route_shift,
            "ean_expert_delta_harm_observed": delta_harm,
            "architecture_change_recommended": False,
            "next_recommended_step": "structured-span curriculum or robust eval stratification, not broad routing redesign",
        },
    }
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    write_json(out / "structured_span_route_audit_report.json", payload)
    _write_markdown(out / "structured_span_route_audit_report.md", payload)
    return payload


def _write_markdown(path: Path, payload: dict[str, Any]) -> None:
    lines = [
        "# EAN Structured Span Route Audit",
        "",
        f"Status: `{payload['status']}`",
        f"Secondary: `{payload.get('secondary_status')}`",
        "",
        "| window | source | delta | owner disagreement | EAN expert help | baseline expert help | route-shift high-loss tokens |",
        "|---|---|---:|---:|---:|---:|---:|",
    ]
    for window in payload["windows"]:
        lines.append(
            f"| {window['window_id']} | {window['source']['path']} | {window['alignment_delta_vs_baseline']} | "
            f"{window['mean_ean_baseline_owner_disagreement_rate']} | {window['mean_ean_expert_help_delta']} | "
            f"{window['mean_baseline_expert_help_delta']} | {window['route_shift_high_loss_token_count']} |"
        )
    lines.extend(["", "```json", json.dumps(payload, indent=2, sort_keys=True, default=str), "```", ""])
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="benchmark/reports/generated/ean_structured_span_route_audit")
    parser.add_argument("--bad-span-report", default="benchmark/reports/generated/ean_bad_token_span_inspection/bad_token_span_inspection_report.json")
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--seq-len", type=int, default=128)
    args = parser.parse_args()
    payload = run(output=args.output, bad_span_report=args.bad_span_report, device=args.device, seq_len=args.seq_len)
    print(payload["status"])


if __name__ == "__main__":
    main()
