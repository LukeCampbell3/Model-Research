"""Full-network official-like alignment audit for router-regret repair checkpoints."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import torch
import torch.nn.functional as F

from benchmark.common import git_commit, load_json_or_yaml, utc_now, write_json
from benchmark.model_factory import build_model


DEFAULT_CONFIGS = {
    "baseline": "benchmark/configs/generated/pvr_router_regret_repair_1m_confirmation/configs/pvr_router_regret_repair_baseline_no_regret_300m_1m_confirm.yaml",
    "regret0p01": "benchmark/configs/generated/pvr_router_regret_repair_1m_confirmation/configs/pvr_router_regret_repair_regret0p01_300m_1m_confirm.yaml",
}


def _load_model(config_path: str, device: str):
    config = load_json_or_yaml(config_path)
    materialized = build_model(config, device=device)
    checkpoint = torch.load(config["checkpoint_path"], map_location=device, weights_only=False)
    materialized.model.load_state_dict(checkpoint.get("model_state_dict", checkpoint), strict=False)
    materialized.model.eval()
    return config, materialized.model


def _read_eval_bytes(path: Path, jsonl_text_field: str | None) -> bytes:
    if not jsonl_text_field:
        return path.read_bytes()
    chunks = []
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            continue
        value = row.get(jsonl_text_field)
        if isinstance(value, str):
            chunks.append(value)
    return "\n".join(chunks).encode("utf-8", errors="replace")


def _loss_on_blocks(
    model,
    path: Path,
    *,
    seq_len: int,
    max_blocks: int,
    device: str,
    jsonl_text_field: str | None,
) -> dict[str, Any]:
    tokens = torch.tensor(list(_read_eval_bytes(path, jsonl_text_field)), dtype=torch.long)
    parts = []
    token_count = 0
    with torch.no_grad():
        for block_idx in range(max_blocks):
            offset = block_idx * seq_len
            if offset + seq_len + 1 > len(tokens):
                break
            block = tokens[offset : offset + seq_len + 1].unsqueeze(0).to(device)
            logits = model(block[:, :-1])
            loss_sum = F.cross_entropy(
                logits.reshape(-1, logits.shape[-1]),
                block[:, 1:].reshape(-1),
                reduction="sum",
            )
            value = float(loss_sum.detach().cpu())
            parts.append({"block_idx": block_idx, "loss_sum": value, "tokens": seq_len, "loss": value / seq_len})
            token_count += seq_len
    loss_sum = sum(part["loss_sum"] for part in parts)
    return {
        "file": path.name,
        "tokens": token_count,
        "loss_sum": loss_sum,
        "loss": loss_sum / token_count if token_count else None,
        "blocks": parts,
    }


def run(
    *,
    official_like_root: str = "data/eval/official_like_dev",
    seq_len: int = 64,
    max_blocks_per_file: int = 1,
    jsonl_text_field: str | None = None,
    output: str = "benchmark/reports/generated/pvr_router_regret_full_network_alignment_audit",
    device: str | None = None,
) -> dict[str, Any]:
    device = device or ("cuda" if torch.cuda.is_available() else "cpu")
    files = sorted(Path(official_like_root).glob("*.jsonl"))
    models = {name: _load_model(path, device) for name, path in DEFAULT_CONFIGS.items()}
    rows = []
    for file_path in files:
        row: dict[str, Any] = {"file": file_path.name}
        for name, (_config, model) in models.items():
            result = _loss_on_blocks(
                model,
                file_path,
                seq_len=seq_len,
                max_blocks=max_blocks_per_file,
                device=device,
                jsonl_text_field=jsonl_text_field,
            )
            row[f"{name}_loss"] = result["loss"]
            row[f"{name}_loss_sum"] = result["loss_sum"]
            row[f"{name}_tokens"] = result["tokens"]
            row[f"{name}_blocks"] = result["blocks"]
        if isinstance(row.get("regret0p01_loss"), (int, float)) and isinstance(row.get("baseline_loss"), (int, float)):
            row["regret0p01_minus_baseline"] = row["regret0p01_loss"] - row["baseline_loss"]
        rows.append(row)

    def micro(name: str) -> float | None:
        tokens = sum(row.get(f"{name}_tokens") or 0 for row in rows)
        if not tokens:
            return None
        return sum(row.get(f"{name}_loss_sum") or 0.0 for row in rows) / tokens

    def macro(name: str) -> float | None:
        values = [row.get(f"{name}_loss") for row in rows if isinstance(row.get(f"{name}_loss"), (int, float))]
        return sum(values) / len(values) if values else None

    baseline_micro = micro("baseline")
    repair_micro = micro("regret0p01")
    baseline_macro = macro("baseline")
    repair_macro = macro("regret0p01")
    micro_delta = repair_micro - baseline_micro if baseline_micro is not None and repair_micro is not None else None
    macro_delta = repair_macro - baseline_macro if baseline_macro is not None and repair_macro is not None else None
    file_wins = sum(1 for row in rows if isinstance(row.get("regret0p01_minus_baseline"), (int, float)) and row["regret0p01_minus_baseline"] < 0)
    decision = (
        "PVR_ROUTER_REGRET_REPAIR_FULL_NETWORK_ALIGNMENT_SUPPORTED"
        if isinstance(micro_delta, (int, float)) and micro_delta < 0.0 and file_wins >= max(1, len(rows) // 2 + 1)
        else "PVR_ROUTER_REGRET_REPAIR_FULL_NETWORK_ALIGNMENT_NOT_SUPPORTED"
    )
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "git_commit": git_commit(),
        "experiment": "PVR_ROUTER_REGRET_REPAIR_FULL_NETWORK_ALIGNMENT_AUDIT",
        "status": "PVR_ROUTER_REGRET_REPAIR_FULL_NETWORK_ALIGNMENT_AUDIT_COMPLETE",
        "decision": decision,
        "device": device,
        "seq_len": seq_len,
        "max_blocks_per_file": max_blocks_per_file,
        "jsonl_text_field": jsonl_text_field,
        "official_like_root": official_like_root,
        "rows": rows,
        "micro_loss": {"baseline": baseline_micro, "regret0p01": repair_micro},
        "macro_loss": {"baseline": baseline_macro, "regret0p01": repair_macro},
        "micro_delta_regret0p01_minus_baseline": micro_delta,
        "macro_delta_regret0p01_minus_baseline": macro_delta,
        "file_wins_regret0p01": file_wins,
        "file_count": len(rows),
        "scope": "Full-network LM loss on official-like development files only. Uses bounded file coverage to align with the oracle/regret audit without touching final official bounded files.",
    }
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    write_json(out / "pvr_router_regret_full_network_alignment_audit.json", payload)
    lines = [
        "# PVR Router Regret Full-Network Alignment Audit",
        "",
        f"Status: `{payload['status']}`",
        f"Decision: `{payload['decision']}`",
        f"Git commit: `{payload['git_commit']}`",
        "",
        payload["scope"],
        f"JSONL text field: `{jsonl_text_field}`",
        "",
        "## Aggregate",
        "",
        f"Baseline micro loss: `{baseline_micro}`",
        f"Regret0p01 micro loss: `{repair_micro}`",
        f"Micro delta: `{micro_delta}`",
        f"Macro delta: `{macro_delta}`",
        f"File wins: `{file_wins}/{len(rows)}`",
        "",
        "## Per File",
        "",
        "| file | tokens | baseline | regret0p01 | delta |",
        "|---|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row['file']} | {row.get('baseline_tokens')} | {row.get('baseline_loss')} | "
            f"{row.get('regret0p01_loss')} | {row.get('regret0p01_minus_baseline')} |"
        )
    (out / "pvr_router_regret_full_network_alignment_audit.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--official-like-root", default="data/eval/official_like_dev")
    parser.add_argument("--seq-len", type=int, default=64)
    parser.add_argument("--max-blocks-per-file", type=int, default=1)
    parser.add_argument("--jsonl-text-field", default=None)
    parser.add_argument("--output", default="benchmark/reports/generated/pvr_router_regret_full_network_alignment_audit")
    parser.add_argument("--device", default=None)
    args = parser.parse_args()
    payload = run(**vars(args))
    print(json.dumps({"status": payload["status"], "decision": payload["decision"], "micro_delta": payload["micro_delta_regret0p01_minus_baseline"], "file_wins": payload["file_wins_regret0p01"]}, indent=2))


if __name__ == "__main__":
    main()
