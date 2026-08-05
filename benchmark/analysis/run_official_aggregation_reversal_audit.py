"""Audit micro/macro aggregation reversals on bounded official LM files."""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path
from typing import Any

import torch
import torch.nn.functional as F

from benchmark.common import load_json_or_yaml, utc_now, write_json
from benchmark.model_factory import build_model


CANDIDATE = "pvr_teacher_independent_sparse_v2_300m"


def _load_model(config_path: str, device: str):
    config = load_json_or_yaml(config_path)
    materialized = build_model(config, device=device)
    checkpoint = torch.load(config["checkpoint_path"], map_location=device)
    materialized.model.load_state_dict(checkpoint.get("model_state_dict", checkpoint), strict=False)
    materialized.model.eval()
    return config, materialized


def _file_loss(model, path: Path, *, device: str, seq_len: int, max_blocks: int, batch_size: int) -> dict[str, Any]:
    tokens = torch.tensor(list(path.read_bytes()), dtype=torch.long)
    available = max(0, (len(tokens) - 1) // seq_len)
    block_count = min(max_blocks, available)
    losses: list[float] = []
    if block_count:
        with torch.no_grad():
            for start in range(0, block_count, batch_size):
                rows = []
                for block_index in range(start, min(block_count, start + batch_size)):
                    offset = block_index * seq_len
                    rows.append(tokens[offset : offset + seq_len + 1])
                batch = torch.stack(rows).to(device)
                logits = model(batch[:, :-1])
                token_losses = F.cross_entropy(
                    logits.reshape(-1, logits.shape[-1]),
                    batch[:, 1:].reshape(-1),
                    reduction="none",
                ).reshape(batch.shape[0], seq_len)
                losses.extend(float(value) for value in token_losses.mean(dim=1).detach().cpu())
    return {
        "file": path.name,
        "raw_bytes": int(len(tokens)),
        "available_blocks": int(available),
        "evaluated_blocks": int(block_count),
        "evaluated_tokens": int(block_count * seq_len),
        "loss": sum(losses) / len(losses) if losses else None,
        "block_losses": losses,
    }


def _evaluate_model(config_path: str, files: list[Path], *, device: str, seq_len: int, max_blocks_per_file: int, batch_size: int) -> dict[str, Any]:
    config, materialized = _load_model(config_path, device)
    per_file = {
        path.name: _file_loss(materialized.model, path, device=device, seq_len=seq_len, max_blocks=max_blocks_per_file, batch_size=batch_size)
        for path in files
    }
    total_tokens = sum(row["evaluated_tokens"] for row in per_file.values())
    micro_loss = sum((row["loss"] or 0.0) * row["evaluated_tokens"] for row in per_file.values()) / total_tokens
    valid_losses = [row["loss"] for row in per_file.values() if row["loss"] is not None]
    return {
        "model_variant": config["model_variant"],
        "config_path": config_path,
        "total_params_actual": materialized.total_params_actual,
        "active_params_per_token_actual": materialized.active_params_per_token_actual,
        "micro_loss": micro_loss,
        "macro_file_loss": sum(valid_losses) / len(valid_losses),
        "evaluated_tokens": total_tokens,
        "per_file": per_file,
    }


def _exact_sign_test(wins: int, n: int) -> float:
    if n <= 0:
        return 1.0
    extreme = min(wins, n - wins)
    prob = sum(math_comb(n, k) for k in range(0, extreme + 1)) / (2**n)
    return min(1.0, 2.0 * prob)


def math_comb(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    value = 1
    for i in range(1, k + 1):
        value = value * (n - i + 1) // i
    return value


def _sign_flip_pvalue(diffs: list[float]) -> float:
    observed = abs(sum(diffs) / len(diffs))
    count = 0
    total = 0
    for signs in itertools.product((-1.0, 1.0), repeat=len(diffs)):
        total += 1
        value = abs(sum(sign * diff for sign, diff in zip(signs, diffs)) / len(diffs))
        if value >= observed - 1e-12:
            count += 1
    return count / total


def _compare(candidate: dict[str, Any], baseline: dict[str, Any]) -> dict[str, Any]:
    file_rows = []
    for file_name, c_row in candidate["per_file"].items():
        b_row = baseline["per_file"][file_name]
        delta = c_row["loss"] - b_row["loss"]
        file_rows.append({
            "file": file_name,
            "evaluated_tokens": c_row["evaluated_tokens"],
            "candidate_loss": c_row["loss"],
            "baseline_loss": b_row["loss"],
            "candidate_minus_baseline": delta,
            "candidate_win": delta < 0.0,
        })
    total_tokens = sum(row["evaluated_tokens"] for row in file_rows)
    micro_delta = sum(row["candidate_minus_baseline"] * row["evaluated_tokens"] for row in file_rows) / total_tokens
    macro_delta = sum(row["candidate_minus_baseline"] for row in file_rows) / len(file_rows)
    leave_one_out = []
    for leave in file_rows:
        kept = [row for row in file_rows if row["file"] != leave["file"]]
        kept_tokens = sum(row["evaluated_tokens"] for row in kept)
        leave_one_out.append({
            "left_out": leave["file"],
            "micro_delta": sum(row["candidate_minus_baseline"] * row["evaluated_tokens"] for row in kept) / kept_tokens,
            "macro_delta": sum(row["candidate_minus_baseline"] for row in kept) / len(kept),
        })
    contributions = []
    denom = micro_delta * total_tokens
    for row in file_rows:
        contribution = row["candidate_minus_baseline"] * row["evaluated_tokens"]
        contributions.append({
            "file": row["file"],
            "delta_token_sum": contribution,
            "share_of_micro_delta_sum": contribution / denom if abs(denom) > 1e-12 else None,
        })
    wins = sum(1 for row in file_rows if row["candidate_win"])
    return {
        "baseline": baseline["model_variant"],
        "candidate_minus_baseline_micro": micro_delta,
        "candidate_minus_baseline_macro_file": macro_delta,
        "candidate_file_wins": wins,
        "file_count": len(file_rows),
        "exact_sign_test_p": _exact_sign_test(wins, len(file_rows)),
        "exact_sign_flip_p": _sign_flip_pvalue([row["candidate_minus_baseline"] for row in file_rows]),
        "per_file": file_rows,
        "leave_one_file_out": leave_one_out,
        "largest_abs_contributors": sorted(contributions, key=lambda row: abs(row["delta_token_sum"]), reverse=True),
    }


def run(
    *,
    candidate_config: str,
    baseline_configs: list[str],
    official_root: str = "data/eval/official_300m_bounded",
    scorecard_root: str = "benchmark/reports/generated/sparse_v2_300m_official_bounded_benchmark",
    output: str,
    device: str = "cuda",
    seq_len: int = 64,
    max_blocks_per_file: int = 32,
    batch_size: int = 8,
) -> dict[str, Any]:
    files = sorted(Path(official_root).glob("*.jsonl"))
    if not files:
        raise FileNotFoundError(f"No official bounded files found in {official_root}")
    candidate = _evaluate_model(candidate_config, files, device=device, seq_len=seq_len, max_blocks_per_file=max_blocks_per_file, batch_size=batch_size)
    baselines = [_evaluate_model(path, files, device=device, seq_len=seq_len, max_blocks_per_file=max_blocks_per_file, batch_size=batch_size) for path in baseline_configs]
    comparisons = [_compare(candidate, baseline) for baseline in baselines]
    combined_file_table = []
    for path in files:
        row = {
            "file": path.name,
            "evaluated_tokens": candidate["per_file"][path.name]["evaluated_tokens"],
            "pvr_loss": candidate["per_file"][path.name]["loss"],
        }
        for baseline in baselines:
            row[f"{baseline['model_variant']}_loss"] = baseline["per_file"][path.name]["loss"]
            row[f"pvr_minus_{baseline['model_variant']}"] = (
                candidate["per_file"][path.name]["loss"] - baseline["per_file"][path.name]["loss"]
            )
        combined_file_table.append(row)
    scorecard_rows = {}
    for row in [candidate, *baselines]:
        path = Path(scorecard_root) / "scorecards" / row["model_variant"] / "nlp_scorecard.json"
        if path.exists():
            scorecard_rows[row["model_variant"]] = json.loads(path.read_text(encoding="utf-8")).get("scorecard", {})
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "status": "PVR_OFFICIAL_BOUNDED_AGGREGATION_REVERSAL_AUDIT_COMPLETE",
        "official_full_benchmark": False,
        "candidate": {key: value for key, value in candidate.items() if key != "per_file"},
        "baselines": [{key: value for key, value in row.items() if key != "per_file"} for row in baselines],
        "files": [str(path) for path in files],
        "scorecard_rows": scorecard_rows,
        "combined_file_table": combined_file_table,
        "comparisons": comparisons,
        "aggregation_definitions": {
            "paired_micro": "All evaluated blocks across all official JSONL files, weighted by evaluated token count.",
            "paired_macro_file": "Mean of per-file candidate-minus-baseline differences, each official JSONL file weighted equally.",
            "domain_weighted": "Equivalent to paired_macro_file in this bounded suite because each top-level official JSONL file is treated as one domain.",
            "scorecard_lm_loss": "Existing run_lm_eval scorecard lm_loss; with the current runner and --limit it evaluates the first limited windows of selected concatenated text, so it is not identical to this all-file paired audit.",
        },
    }
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    write_json(out / "official_aggregation_reversal_audit.json", payload)
    lines = [
        "# Official Aggregation Reversal Audit",
        "",
        f"Status: `{payload['status']}`",
        "",
        "The existing scorecard `lm_loss` and this paired all-file audit use different aggregation definitions. Treat reversals as evaluator-alignment findings, not model-proof by themselves.",
        "",
        "## Combined Per-File Table",
        "",
        "| file | tokens | PVR loss | dense loss | PVR-dense | Switch loss | PVR-Switch | Top2 loss | PVR-Top2 |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    dense_key = "dense_sparse_v2_300m_matched"
    switch_key = "switch_top1_sparse_v2_300m_matched"
    top2_key = "generic_top2_sparse_v2_300m_matched"
    for row in combined_file_table:
        lines.append(
            f"| {row['file']} | {row['evaluated_tokens']} | {row['pvr_loss']} | "
            f"{row.get(dense_key + '_loss')} | {row.get('pvr_minus_' + dense_key)} | "
            f"{row.get(switch_key + '_loss')} | {row.get('pvr_minus_' + switch_key)} | "
            f"{row.get(top2_key + '_loss')} | {row.get('pvr_minus_' + top2_key)} |"
        )
    lines.extend([
        "",
    ])
    for comparison in comparisons:
        lines.extend([
            f"## PVR vs {comparison['baseline']}",
            "",
            f"Micro delta: `{comparison['candidate_minus_baseline_micro']}`",
            f"Macro file delta: `{comparison['candidate_minus_baseline_macro_file']}`",
            f"File wins: `{comparison['candidate_file_wins']}/{comparison['file_count']}`",
            f"Exact sign-test p: `{comparison['exact_sign_test_p']}`",
            f"Exact sign-flip p: `{comparison['exact_sign_flip_p']}`",
            "",
            "| file | tokens | PVR loss | baseline loss | PVR-baseline | PVR win |",
            "|---|---:|---:|---:|---:|---|",
        ])
        for row in comparison["per_file"]:
            lines.append(
                f"| {row['file']} | {row['evaluated_tokens']} | {row['candidate_loss']} | "
                f"{row['baseline_loss']} | {row['candidate_minus_baseline']} | {row['candidate_win']} |"
            )
        lines.append("")
    (out / "official_aggregation_reversal_audit.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidate-config", required=True)
    parser.add_argument("--baseline-configs", nargs="+", required=True)
    parser.add_argument("--official-root", default="data/eval/official_300m_bounded")
    parser.add_argument("--scorecard-root", default="benchmark/reports/generated/sparse_v2_300m_official_bounded_benchmark")
    parser.add_argument("--output", required=True)
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--seq-len", type=int, default=64)
    parser.add_argument("--max-blocks-per-file", type=int, default=32)
    parser.add_argument("--batch-size", type=int, default=8)
    args = parser.parse_args()
    payload = run(**vars(args))
    print(json.dumps({"status": payload["status"]}, indent=2))


if __name__ == "__main__":
    main()
