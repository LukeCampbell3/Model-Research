"""Audit alignment between reduced scorecard eval and training eval windows."""

from __future__ import annotations

import argparse
import json
import math
import statistics
from pathlib import Path
from typing import Any

import torch
import torch.nn.functional as F

from benchmark.common import git_commit, load_json_or_yaml, utc_now, write_json
from benchmark.model_factory import build_model
from benchmark.runners.run_lm_eval import _files, _text_for
from benchmark.runners.run_training import _batch, _load_bytes


STATUS_COMPLETE = "PVR_EAN_SCORECARD_EVAL_CURVE_ALIGNMENT_AUDIT_COMPLETE"


DEFAULT_MODELS = {
    "dense_300m": {
        "label": "dense_300m",
        "config": "benchmark/configs/generated/dense_transformer_300m.yaml",
        "recorded_eval_curve": "benchmark/reports/generated/training_300m_real_4k/dense_transformer_300m/eval_curve.json",
        "scorecard": "benchmark/reports/generated/genuine_program_300m_real_4k/scorecard_artifacts/nlp/dense_transformer_300m.json",
    },
    "pvr_baseline_seed42": {
        "label": "pvr_baseline_seed42",
        "config": "benchmark/reports/generated/shared_trunk_init_300m_repeat_seed_42/pvr_ec_o_full_300m_baseline_seed_42/run_config.yaml",
        "recorded_eval_curve": "benchmark/reports/generated/shared_trunk_init_300m_repeat_seed_42/pvr_ec_o_full_300m_baseline_seed_42/eval_curve.json",
        "scorecard": "benchmark/reports/generated/shared_trunk_init_300m_repeat_seed_42/lm_eval/pvr_ec_o_full_300m_baseline_seed_42_nlp_scorecard.json",
    },
    "full_copy_seed42": {
        "label": "full_copy_seed42",
        "config": "benchmark/reports/generated/shared_trunk_init_300m_repeat_seed_42/pvr_ec_o_full_300m_shared_trunk_init_from_dense_seed_42/run_config.yaml",
        "recorded_eval_curve": "benchmark/reports/generated/shared_trunk_init_300m_repeat_seed_42/pvr_ec_o_full_300m_shared_trunk_init_from_dense_seed_42/eval_curve.json",
        "scorecard": "benchmark/reports/generated/shared_trunk_init_300m_repeat_seed_42/lm_eval/pvr_ec_o_full_300m_shared_trunk_init_from_dense_seed_42_nlp_scorecard.json",
    },
    "ean_seed42": {
        "label": "ean_seed42",
        "config": "benchmark/reports/generated/ean_init_300m_repeat_seed_42/pvr_ec_o_full_300m_shared_trunk_init_v1_scope_embeddings_attention_norms_seed_42/run_config.yaml",
        "recorded_eval_curve": "benchmark/reports/generated/ean_init_300m_repeat_seed_42/pvr_ec_o_full_300m_shared_trunk_init_v1_scope_embeddings_attention_norms_seed_42/eval_curve.json",
        "scorecard": "benchmark/reports/generated/ean_init_300m_repeat_seed_42/lm_eval/pvr_ec_o_full_300m_shared_trunk_init_v1_scope_embeddings_attention_norms_seed_42_nlp_scorecard.json",
    },
}


def _load_json(path: str | Path) -> dict[str, Any]:
    return json.loads(Path(str(path).replace("\\", "/")).read_text(encoding="utf-8"))


def _safe_mean(values: list[Any]) -> float | None:
    xs = [float(value) for value in values if isinstance(value, (int, float))]
    return sum(xs) / len(xs) if xs else None


def _variance(values: list[Any]) -> float | None:
    xs = [float(value) for value in values if isinstance(value, (int, float))]
    return statistics.pvariance(xs) if len(xs) >= 2 else None


def _corr(xs: list[Any], ys: list[Any]) -> float | None:
    pairs = [(float(x), float(y)) for x, y in zip(xs, ys) if isinstance(x, (int, float)) and isinstance(y, (int, float))]
    if len(pairs) < 2:
        return None
    x_vals, y_vals = zip(*pairs)
    mean_x = sum(x_vals) / len(x_vals)
    mean_y = sum(y_vals) / len(y_vals)
    num = sum((x - mean_x) * (y - mean_y) for x, y in pairs)
    den_x = math.sqrt(sum((x - mean_x) ** 2 for x in x_vals))
    den_y = math.sqrt(sum((y - mean_y) ** 2 for y in y_vals))
    if den_x == 0 or den_y == 0:
        return None
    return num / (den_x * den_y)


def _load_model(config: dict[str, Any], device: str):
    materialized = build_model(config, device=device)
    checkpoint = torch.load(config["checkpoint_path"], map_location=device)
    state = checkpoint.get("model_state_dict", checkpoint)
    materialized.model.load_state_dict(state, strict=False)
    materialized.model.eval()
    return materialized.model


def _loss_windows_contiguous(model, tokens: torch.Tensor, *, seq_len: int, max_windows: int, device: str) -> list[dict[str, Any]]:
    if len(tokens) < seq_len + 1:
        return []
    rows = []
    with torch.no_grad():
        for idx in range(max_windows):
            offset = idx * seq_len
            if offset + seq_len + 1 > len(tokens):
                break
            block = tokens[offset : offset + seq_len + 1].unsqueeze(0).to(device)
            logits = model(block[:, :-1])
            loss = F.cross_entropy(logits.reshape(-1, logits.shape[-1]), block[:, 1:].reshape(-1))
            rows.append({
                "window_index": idx,
                "offset": offset,
                "tokens": seq_len,
                "loss": float(loss.detach().cpu().item()),
            })
    return rows


def _loss_training_offsets(
    model,
    tokens: torch.Tensor,
    *,
    eval_steps: list[int],
    seq_len: int,
    device: str,
) -> list[dict[str, Any]]:
    if len(tokens) < seq_len + 1:
        return []
    rows = []
    with torch.no_grad():
        for step in eval_steps:
            step_idx = max(0, int(step) - 1)
            x, y = _batch(tokens, step_idx, 1, seq_len, device)
            logits = model(x)
            loss = F.cross_entropy(logits.reshape(-1, logits.shape[-1]), y.reshape(-1))
            rows.append({
                "step": int(step),
                "step_index": step_idx,
                "tokens": int(x.numel()),
                "loss": float(loss.detach().cpu().item()),
            })
    return rows


def _curve(path: str | Path) -> list[dict[str, Any]]:
    p = Path(str(path).replace("\\", "/"))
    if not p.exists():
        return []
    return _load_json(p).get("eval_curve", [])


def _scorecard_lm_loss(path: str | Path) -> float | None:
    p = Path(str(path).replace("\\", "/"))
    if not p.exists():
        return None
    payload = _load_json(p)
    if "scorecard" in payload:
        return payload["scorecard"].get("lm_loss")
    return payload.get("scorecards", {}).get("nlp_scorecard", {}).get("scorecard", {}).get("lm_loss")


def _summarize_windows(rows: list[dict[str, Any]]) -> dict[str, Any]:
    losses = [row.get("loss") for row in rows]
    return {
        "window_count": len(rows),
        "mean_loss": _safe_mean(losses),
        "loss_variance": _variance(losses),
        "min_loss": min([float(x) for x in losses if isinstance(x, (int, float))], default=None),
        "max_loss": max([float(x) for x in losses if isinstance(x, (int, float))], default=None),
    }


def _delta_windows(rows: list[dict[str, Any]], baseline_rows: list[dict[str, Any]], key: str) -> list[dict[str, Any]]:
    out = []
    for row, baseline in zip(rows, baseline_rows):
        loss = row.get("loss")
        base_loss = baseline.get("loss")
        out.append({
            key: row.get(key),
            "loss": loss,
            "baseline_loss": base_loss,
            "delta_vs_baseline": float(loss) - float(base_loss)
            if isinstance(loss, (int, float)) and isinstance(base_loss, (int, float))
            else None,
        })
    return out


def run(
    *,
    output: str = "benchmark/reports/generated/ean_scorecard_eval_curve_alignment_audit",
    models: dict[str, dict[str, str]] | None = None,
    device: str = "cuda",
    scorecard_windows: int = 200,
    scorecard_seq_len: int = 64,
    training_seq_len: int = 128,
    eval_interval: int = 400,
    max_steps: int = 4000,
) -> dict[str, Any]:
    if device == "cuda" and not torch.cuda.is_available():
        device = "cpu"
    specs = models or DEFAULT_MODELS
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    eval_steps = list(range(eval_interval, max_steps + 1, eval_interval))
    rows: dict[str, Any] = {}
    scorecard_general_windows: dict[str, list[dict[str, Any]]] = {}
    final_training_windows: dict[str, list[dict[str, Any]]] = {}
    for name, spec in specs.items():
        cfg = load_json_or_yaml(spec["config"])
        model = _load_model(cfg, device)
        eval_files = _files(list(cfg.get("eval_data_paths") or []))
        general_tokens = torch.tensor(
            list(_text_for(eval_files, ["heldout", "gutenberg", "frankenstein"]).encode("utf-8", errors="replace")),
            dtype=torch.long,
        )
        eval_tokens = _load_bytes(list(cfg.get("eval_data_paths") or []), require=False)
        scorecard_general = _loss_windows_contiguous(
            model,
            general_tokens,
            seq_len=min(scorecard_seq_len, int(cfg.get("context_length", scorecard_seq_len + 1)) - 1),
            max_windows=scorecard_windows,
            device=device,
        )
        training_style = _loss_training_offsets(
            model,
            eval_tokens,
            eval_steps=eval_steps,
            seq_len=min(training_seq_len, int(cfg.get("context_length", training_seq_len + 1)) - 1),
            device=device,
        )
        recorded_curve = _curve(spec["recorded_eval_curve"])
        recorded_losses = [row.get("eval_loss") for row in recorded_curve]
        scorecard_general_windows[name] = scorecard_general
        final_training_windows[name] = training_style
        rows[name] = {
            "label": spec["label"],
            "model_variant": cfg.get("model_variant"),
            "checkpoint_path": cfg.get("checkpoint_path"),
            "scorecard_lm_loss_recorded": _scorecard_lm_loss(spec["scorecard"]),
            "scorecard_style_final_checkpoint": _summarize_windows(scorecard_general),
            "training_window_style_final_checkpoint": _summarize_windows(training_style),
            "recorded_during_training_eval_curve": {
                "path": spec["recorded_eval_curve"],
                "window_count": len(recorded_curve),
                "mean_loss": _safe_mean(recorded_losses),
                "loss_variance": _variance(recorded_losses),
                "windows": recorded_curve,
            },
            "same_heldout_tokens": {
                "scorecard_seq_len": scorecard_seq_len,
                "window_count": len(scorecard_general),
                "mean_loss": _safe_mean([row.get("loss") for row in scorecard_general]),
                "loss_variance": _variance([row.get("loss") for row in scorecard_general]),
            },
        }
        if device == "cuda":
            torch.cuda.empty_cache()
    baseline_key = "pvr_baseline_seed42"
    baseline_scorecard = rows[baseline_key]["scorecard_style_final_checkpoint"]["mean_loss"]
    baseline_training_final = rows[baseline_key]["training_window_style_final_checkpoint"]["mean_loss"]
    baseline_recorded = rows[baseline_key]["recorded_during_training_eval_curve"]["mean_loss"]
    for name, row in rows.items():
        row["deltas_vs_pvr_baseline"] = {
            "scorecard_style_final_checkpoint_mean": (
                row["scorecard_style_final_checkpoint"]["mean_loss"] - baseline_scorecard
                if isinstance(row["scorecard_style_final_checkpoint"]["mean_loss"], (int, float))
                and isinstance(baseline_scorecard, (int, float))
                else None
            ),
            "training_window_style_final_checkpoint_mean": (
                row["training_window_style_final_checkpoint"]["mean_loss"] - baseline_training_final
                if isinstance(row["training_window_style_final_checkpoint"]["mean_loss"], (int, float))
                and isinstance(baseline_training_final, (int, float))
                else None
            ),
            "recorded_during_training_eval_curve_mean": (
                row["recorded_during_training_eval_curve"]["mean_loss"] - baseline_recorded
                if isinstance(row["recorded_during_training_eval_curve"]["mean_loss"], (int, float))
                and isinstance(baseline_recorded, (int, float))
                else None
            ),
        }
        row["per_window_deltas_vs_pvr_baseline"] = {
            "scorecard_style_general": _delta_windows(
                scorecard_general_windows[name],
                scorecard_general_windows[baseline_key],
                "window_index",
            ),
            "training_window_style_final_checkpoint": _delta_windows(
                final_training_windows[name],
                final_training_windows[baseline_key],
                "step",
            ),
        }
    scorecard_means = [rows[name]["scorecard_style_final_checkpoint"]["mean_loss"] for name in specs]
    training_means = [rows[name]["training_window_style_final_checkpoint"]["mean_loss"] for name in specs]
    recorded_means = [rows[name]["recorded_during_training_eval_curve"]["mean_loss"] for name in specs]
    scorecard_deltas = [rows[name]["deltas_vs_pvr_baseline"]["scorecard_style_final_checkpoint_mean"] for name in specs if name != baseline_key]
    final_training_deltas = [rows[name]["deltas_vs_pvr_baseline"]["training_window_style_final_checkpoint_mean"] for name in specs if name != baseline_key]
    recorded_deltas = [rows[name]["deltas_vs_pvr_baseline"]["recorded_during_training_eval_curve_mean"] for name in specs if name != baseline_key]
    ean = rows["ean_seed42"]
    status_detail = (
        "SCORECARD_AND_FINAL_TRAINING_WINDOWS_AGREE_EAN_POSITIVE"
        if (ean["deltas_vs_pvr_baseline"]["scorecard_style_final_checkpoint_mean"] or 0) < 0
        and (ean["deltas_vs_pvr_baseline"]["training_window_style_final_checkpoint_mean"] or 0) < 0
        else "EVAL_PATH_MISMATCH_OR_NOISE_REMAINS"
    )
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "git_commit": git_commit(),
        "status": STATUS_COMPLETE,
        "status_detail": status_detail,
        "experiment": "PVR_EAN_SCORECARD_EVAL_CURVE_ALIGNMENT_AUDIT",
        "device": device,
        "scorecard_windows": scorecard_windows,
        "scorecard_seq_len": scorecard_seq_len,
        "training_seq_len": training_seq_len,
        "eval_steps": eval_steps,
        "rows": rows,
        "correlations": {
            "scorecard_style_vs_final_training_window_mean_across_models": _corr(scorecard_means, training_means),
            "scorecard_style_vs_recorded_training_curve_mean_across_models": _corr(scorecard_means, recorded_means),
            "scorecard_delta_vs_final_training_window_delta_vs_baseline": _corr(scorecard_deltas, final_training_deltas),
            "scorecard_delta_vs_recorded_training_curve_delta_vs_baseline": _corr(scorecard_deltas, recorded_deltas),
        },
        "interpretation": (
            "This audit distinguishes final-checkpoint evaluation path mismatch from genuine during-training eval-curve "
            "instability by evaluating the same checkpoints on both scorecard-style heldout windows and training-style eval offsets."
        ),
    }
    write_json(out / "alignment_audit_report.json", payload)
    _write_markdown(out / "alignment_audit_report.md", payload)
    return payload


def _write_markdown(path: Path, payload: dict[str, Any]) -> None:
    lines = [
        "# EAN Scorecard/Eval-Curve Alignment Audit",
        "",
        f"Status: `{payload['status']}`",
        f"Detail: `{payload['status_detail']}`",
        "",
        "| model | scorecard-style mean | final training-window mean | recorded eval mean | scorecard delta | final-window delta | recorded delta |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for name, row in payload["rows"].items():
        deltas = row["deltas_vs_pvr_baseline"]
        lines.append(
            f"| {name} | {row['scorecard_style_final_checkpoint']['mean_loss']} | "
            f"{row['training_window_style_final_checkpoint']['mean_loss']} | "
            f"{row['recorded_during_training_eval_curve']['mean_loss']} | "
            f"{deltas['scorecard_style_final_checkpoint_mean']} | "
            f"{deltas['training_window_style_final_checkpoint_mean']} | "
            f"{deltas['recorded_during_training_eval_curve_mean']} |"
        )
    lines.extend(["", "```json", json.dumps(payload, indent=2, sort_keys=True, default=str), "```", ""])
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="benchmark/reports/generated/ean_scorecard_eval_curve_alignment_audit")
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--scorecard-windows", type=int, default=200)
    parser.add_argument("--scorecard-seq-len", type=int, default=64)
    parser.add_argument("--training-seq-len", type=int, default=128)
    parser.add_argument("--eval-interval", type=int, default=400)
    parser.add_argument("--max-steps", type=int, default=4000)
    args = parser.parse_args()
    payload = run(
        output=args.output,
        device=args.device,
        scorecard_windows=args.scorecard_windows,
        scorecard_seq_len=args.scorecard_seq_len,
        training_seq_len=args.training_seq_len,
        eval_interval=args.eval_interval,
        max_steps=args.max_steps,
    )
    print(payload["status"])


if __name__ == "__main__":
    main()
