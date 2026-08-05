"""Paired/file-bootstrap LM significance on bounded official-data slices."""

from __future__ import annotations

import argparse
import gc
import json
import random
from pathlib import Path
from typing import Any

import torch
import torch.nn.functional as F

from benchmark.common import load_json_or_yaml, utc_now, write_json
from benchmark.model_factory import build_model


def _official_files(root: str) -> list[Path]:
    files = sorted(Path(root).glob("*.jsonl"))
    if not files:
        raise FileNotFoundError(f"No official bounded JSONL files found in {root}")
    return files


def _load(config: dict[str, Any], device: str):
    materialized = build_model(config, device=device)
    checkpoint = torch.load(config["checkpoint_path"], map_location=device)
    materialized.model.load_state_dict(checkpoint.get("model_state_dict", checkpoint), strict=False)
    materialized.model.eval()
    return materialized


def _losses_for_file(model, path: Path, *, device: str, seq_len: int, max_blocks: int, batch_size: int) -> list[float]:
    tokens = torch.tensor(list(path.read_bytes()), dtype=torch.long)
    block_count = min(max_blocks, max(0, (len(tokens) - 1) // seq_len))
    losses: list[float] = []
    if block_count <= 0:
        return losses
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
    return losses


def _model_losses(config_path: str, files: list[Path], *, device: str, seq_len: int, max_blocks_per_file: int, batch_size: int) -> dict[str, Any]:
    config = load_json_or_yaml(config_path)
    materialized = _load(config, device)
    file_losses = {}
    all_losses: list[float] = []
    for path in files:
        losses = _losses_for_file(materialized.model, path, device=device, seq_len=seq_len, max_blocks=max_blocks_per_file, batch_size=batch_size)
        file_losses[path.name] = losses
        all_losses.extend(losses)
    row = {
        "model_variant": config["model_variant"],
        "config_path": config_path,
        "mean_loss": sum(all_losses) / len(all_losses),
        "block_count": len(all_losses),
        "file_count": len([losses for losses in file_losses.values() if losses]),
        "file_losses": file_losses,
        "total_params_actual": materialized.total_params_actual,
        "active_params_per_token_actual": materialized.active_params_per_token_actual,
    }
    del materialized
    gc.collect()
    if device == "cuda":
        torch.cuda.empty_cache()
    return row


def _bootstrap(values: list[float], *, samples: int, rng: random.Random) -> list[float]:
    out = []
    for _ in range(samples):
        out.append(sum(values[rng.randrange(len(values))] for _ in values) / len(values))
    out.sort()
    return out


def _paired(candidate: dict[str, Any], baseline: dict[str, Any], *, samples: int, seed: int) -> dict[str, Any]:
    block_diffs: list[float] = []
    file_diffs: list[float] = []
    per_file = {}
    for file_name, candidate_losses in candidate["file_losses"].items():
        baseline_losses = baseline["file_losses"].get(file_name, [])
        count = min(len(candidate_losses), len(baseline_losses))
        if count <= 0:
            continue
        diffs = [candidate_losses[idx] - baseline_losses[idx] for idx in range(count)]
        block_diffs.extend(diffs)
        file_mean = sum(diffs) / len(diffs)
        file_diffs.append(file_mean)
        per_file[file_name] = {
            "paired_block_count": count,
            "candidate_minus_baseline_mean_loss": file_mean,
            "candidate_win": file_mean < 0.0,
        }
    rng = random.Random(f"{seed}:{candidate['model_variant']}:{baseline['model_variant']}")
    block_boot = _bootstrap(block_diffs, samples=samples, rng=rng)
    file_boot = _bootstrap(file_diffs, samples=samples, rng=rng) if file_diffs else []
    return {
        "baseline": baseline["model_variant"],
        "candidate_minus_baseline_mean_loss": sum(block_diffs) / len(block_diffs),
        "candidate_minus_baseline_file_mean_loss": sum(file_diffs) / len(file_diffs),
        "paired_block_count": len(block_diffs),
        "paired_file_count": len(file_diffs),
        "block_bootstrap_ci95": [block_boot[int(0.025 * samples)], block_boot[min(samples - 1, int(0.975 * samples))]],
        "file_bootstrap_ci95": [file_boot[int(0.025 * samples)], file_boot[min(samples - 1, int(0.975 * samples))]] if file_boot else None,
        "probability_candidate_better_block_bootstrap": sum(value < 0 for value in block_boot) / samples,
        "probability_candidate_better_file_bootstrap": sum(value < 0 for value in file_boot) / samples if file_boot else None,
        "significant_candidate_win_block_bootstrap": block_boot[min(samples - 1, int(0.975 * samples))] < 0,
        "significant_candidate_win_file_bootstrap": bool(file_boot and file_boot[min(samples - 1, int(0.975 * samples))] < 0),
        "file_win_count": sum(1 for value in per_file.values() if value["candidate_win"]),
        "per_file": per_file,
        "candidate_active_params_delta": candidate["active_params_per_token_actual"] - baseline["active_params_per_token_actual"],
    }


def run(
    *,
    candidate_config: str,
    baseline_configs: list[str],
    official_root: str = "data/eval/official_300m_bounded",
    output: str,
    device: str = "cuda",
    seq_len: int = 64,
    max_blocks_per_file: int = 32,
    batch_size: int = 8,
    bootstrap_samples: int = 5000,
    seed: int = 20260715,
) -> dict[str, Any]:
    files = _official_files(official_root)
    candidate = _model_losses(candidate_config, files, device=device, seq_len=seq_len, max_blocks_per_file=max_blocks_per_file, batch_size=batch_size)
    baselines = [
        _model_losses(path, files, device=device, seq_len=seq_len, max_blocks_per_file=max_blocks_per_file, batch_size=batch_size)
        for path in baseline_configs
    ]
    comparisons = [_paired(candidate, baseline, samples=bootstrap_samples, seed=seed) for baseline in baselines]
    significant_official_wins = comparisons and all(row["significant_candidate_win_file_bootstrap"] for row in comparisons)
    status = (
        "PVR_SPARSE_V2_300M_OFFICIAL_BOUNDED_PAIRED_ADVANTAGE_SUPPORTED"
        if significant_official_wins
        else "PVR_SPARSE_V2_300M_OFFICIAL_BOUNDED_PAIRED_ADVANTAGE_NOT_SUPPORTED"
    )
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "status": status,
        "official_full_benchmark": False,
        "official_root": official_root,
        "files": [str(path) for path in files],
        "seq_len": seq_len,
        "max_blocks_per_file": max_blocks_per_file,
        "candidate": {key: value for key, value in candidate.items() if key != "file_losses"},
        "baselines": [{key: value for key, value in row.items() if key != "file_losses"} for row in baselines],
        "comparisons": comparisons,
        "decision_rule": "Support requires file-bootstrap upper CI < 0 against every listed baseline.",
    }
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    write_json(out / "official_bounded_paired_lm_significance_report.json", payload)
    lines = [
        "# Official Bounded Paired LM Significance",
        "",
        f"Status: `{status}`",
        "",
        "| baseline | block delta | block 95% CI | file delta | file 95% CI | file wins | significant file win |",
        "|---|---:|---|---:|---|---:|---|",
    ]
    for row in comparisons:
        lines.append(
            f"| {row['baseline']} | {row['candidate_minus_baseline_mean_loss']} | {row['block_bootstrap_ci95']} | "
            f"{row['candidate_minus_baseline_file_mean_loss']} | {row['file_bootstrap_ci95']} | "
            f"{row['file_win_count']}/{row['paired_file_count']} | {row['significant_candidate_win_file_bootstrap']} |"
        )
    (out / "official_bounded_paired_lm_significance_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidate-config", required=True)
    parser.add_argument("--baseline-configs", nargs="+", required=True)
    parser.add_argument("--official-root", default="data/eval/official_300m_bounded")
    parser.add_argument("--output", required=True)
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--seq-len", type=int, default=64)
    parser.add_argument("--max-blocks-per-file", type=int, default=32)
    parser.add_argument("--batch-size", type=int, default=8)
    parser.add_argument("--bootstrap-samples", type=int, default=5000)
    parser.add_argument("--seed", type=int, default=20260715)
    args = parser.parse_args()
    payload = run(**vars(args))
    print(json.dumps({"status": payload["status"], "comparisons": payload["comparisons"]}, indent=2))


if __name__ == "__main__":
    main()
