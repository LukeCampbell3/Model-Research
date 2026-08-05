"""Run paired block-bootstrap LM significance on a non-test heldout corpus."""

from __future__ import annotations

import argparse
import gc
import json
import random
from pathlib import Path

import torch
import torch.nn.functional as F

from benchmark.common import load_json_or_yaml, utc_now, write_json
from benchmark.model_factory import build_model


def _load(config, device):
    materialized = build_model(config, device=device)
    checkpoint = torch.load(config["checkpoint_path"], map_location=device)
    materialized.model.load_state_dict(checkpoint.get("model_state_dict", checkpoint), strict=True)
    materialized.model.eval()
    return materialized


def _block_losses(config, corpus: bytes, *, device: str, seq_len: int, max_blocks: int, batch_size: int):
    materialized = _load(config, device)
    tokens = torch.tensor(list(corpus), dtype=torch.long)
    count = min(max_blocks, max(0, (len(tokens) - 1) // seq_len))
    losses = []
    with torch.no_grad():
        for start_block in range(0, count, batch_size):
            rows = []
            for block_index in range(start_block, min(count, start_block + batch_size)):
                offset = block_index * seq_len
                rows.append(tokens[offset : offset + seq_len + 1])
            batch = torch.stack(rows).to(device)
            logits = materialized.model(batch[:, :-1])
            token_losses = F.cross_entropy(
                logits.reshape(-1, logits.shape[-1]),
                batch[:, 1:].reshape(-1),
                reduction="none",
            ).reshape(batch.shape[0], seq_len)
            losses.extend(float(value) for value in token_losses.mean(dim=1).detach().cpu())
    row = {
        "model_variant": config["model_variant"],
        "block_losses": losses,
        "mean_loss": sum(losses) / len(losses),
        "total_params_actual": materialized.total_params_actual,
        "active_params_per_token_actual": materialized.active_params_per_token_actual,
    }
    del materialized
    gc.collect()
    if device == "cuda":
        torch.cuda.empty_cache()
    return row


def _paired(candidate, baseline, *, samples: int, seed: int):
    differences = [a - b for a, b in zip(candidate["block_losses"], baseline["block_losses"])]
    rng = random.Random(f"{seed}:{candidate['model_variant']}:{baseline['model_variant']}")
    bootstrap = []
    for _ in range(samples):
        bootstrap.append(sum(differences[rng.randrange(len(differences))] for _ in differences) / len(differences))
    bootstrap.sort()
    return {
        "baseline": baseline["model_variant"],
        "candidate_minus_baseline_mean_loss": sum(differences) / len(differences),
        "paired_block_count": len(differences),
        "ci95": [bootstrap[int(0.025 * samples)], bootstrap[min(samples - 1, int(0.975 * samples))]],
        "probability_candidate_better": sum(value < 0 for value in bootstrap) / samples,
        "significant_candidate_win": bootstrap[min(samples - 1, int(0.975 * samples))] < 0,
        "candidate_active_params_delta": candidate["active_params_per_token_actual"] - baseline["active_params_per_token_actual"],
    }


def run(
    *,
    candidate_config: str,
    baseline_configs: list[str],
    output: str,
    corpus_path="data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
    device="cuda",
    seq_len=64,
    max_blocks=512,
    batch_size=16,
    bootstrap_samples=10000,
    seed=20260621,
):
    corpus = Path(corpus_path).read_bytes()
    candidate = _block_losses(load_json_or_yaml(candidate_config), corpus, device=device, seq_len=seq_len, max_blocks=max_blocks, batch_size=batch_size)
    baselines = [
        _block_losses(load_json_or_yaml(path), corpus, device=device, seq_len=seq_len, max_blocks=max_blocks, batch_size=batch_size)
        for path in baseline_configs
    ]
    comparisons = [_paired(candidate, baseline, samples=bootstrap_samples, seed=seed) for baseline in baselines]
    sparse = [row for row in comparisons if "dense" not in row["baseline"]]
    significant_sparse_wins = bool(sparse) and all(row["significant_candidate_win"] for row in sparse)
    status = "PVR_SPARSE_V2_LOCAL_SIGNIFICANCE_SUPPORTED" if significant_sparse_wins else "PVR_SPARSE_V2_LOCAL_SIGNIFICANCE_NOT_SUPPORTED"
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "status": status,
        "official_test_data_used": False,
        "corpus_path": corpus_path,
        "seq_len": seq_len,
        "paired_block_count": len(candidate["block_losses"]),
        "candidate": {key: value for key, value in candidate.items() if key != "block_losses"},
        "baselines": [{key: value for key, value in row.items() if key != "block_losses"} for row in baselines],
        "comparisons": comparisons,
        "decision_rule": "Support requires paired block-bootstrap upper CI < 0 against both Switch Top1 and generic Top2.",
    }
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    write_json(out / "paired_lm_significance_report.json", payload)
    lines = ["# Paired LM Significance", "", f"Status: `{status}`", "", "| baseline | loss delta | 95% CI | active delta | significant |", "|---|---:|---:|---:|---|"]
    for row in comparisons:
        lines.append(f"| {row['baseline']} | {row['candidate_minus_baseline_mean_loss']} | {row['ci95']} | {row['candidate_active_params_delta']} | {row['significant_candidate_win']} |")
    (out / "paired_lm_significance_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return payload


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidate-config", required=True)
    parser.add_argument("--baseline-configs", nargs="+", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--corpus-path", default="data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt")
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--seq-len", type=int, default=64)
    parser.add_argument("--max-blocks", type=int, default=512)
    parser.add_argument("--batch-size", type=int, default=16)
    parser.add_argument("--bootstrap-samples", type=int, default=10000)
    parser.add_argument("--seed", type=int, default=20260621)
    args = parser.parse_args()
    payload = run(**vars(args))
    print(json.dumps({"status": payload["status"], "comparisons": payload["comparisons"]}, indent=2))


if __name__ == "__main__":
    main()
