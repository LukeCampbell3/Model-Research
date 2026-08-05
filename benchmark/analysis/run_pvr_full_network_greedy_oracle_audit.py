"""Greedy full-network PVR oracle audit.

At each PVR block, this evaluates every expert from the same block input through
the remaining network suffix, chooses the per-token lowest-loss expert, then
continues to the next block. This is a full-network greedy oracle diagnostic,
not an exhaustive combinatorial oracle over all block/expert assignments.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import torch
import torch.nn.functional as F

from benchmark.common import load_json_or_yaml, utc_now, write_json
from benchmark.model_factory import build_model
from benchmark.analysis.run_pvr_final_block_expert_sweep_audit import _blocks, _gather_expert_outputs


def _load(config_path: str, device: str):
    config = load_json_or_yaml(config_path)
    materialized = build_model(config, device=device)
    checkpoint = torch.load(config["checkpoint_path"], map_location=device)
    materialized.model.load_state_dict(checkpoint.get("model_state_dict", checkpoint), strict=False)
    materialized.model.eval()
    return config, materialized.model


def _loss(model, x: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
    logits = model.head(model.ln_f(x))
    return F.cross_entropy(logits.reshape(-1, logits.shape[-1]), targets.reshape(-1), reduction="none").reshape(targets.shape)


def _suffix_selected(model, x: torch.Tensor, start_block: int, mask: torch.Tensor) -> torch.Tensor:
    for idx in range(start_block, len(model.blocks)):
        x = model.attn[idx](x, src_mask=mask)
        x = model.blocks[idx](x)
    return x


def _normal_selected_loss(model, input_ids: torch.Tensor, targets: torch.Tensor, mask: torch.Tensor) -> torch.Tensor:
    x = model.token_emb(input_ids) + model.pos_emb(torch.arange(input_ids.shape[1], device=input_ids.device).unsqueeze(0))
    x = _suffix_selected(model, x, 0, mask)
    return _loss(model, x, targets)


def _batch_greedy_oracle(model, batch: torch.Tensor, *, device: str) -> dict[str, Any]:
    input_ids = batch[:, :-1].to(device)
    targets = batch[:, 1:].to(device)
    seq_len = input_ids.shape[1]
    mask = torch.triu(torch.ones(seq_len, seq_len, device=device), diagonal=1).bool()
    positions = torch.arange(seq_len, device=device).unsqueeze(0)
    selected = _normal_selected_loss(model, input_ids, targets, mask)
    x = model.token_emb(input_ids) + model.pos_emb(positions)
    regret_values: list[float] = []
    selected_is_oracle = 0
    selected_is_top2 = 0
    decision_count = 0

    for block_idx, block in enumerate(model.blocks):
        x = model.attn[block_idx](x, src_mask=mask)
        h = block.ln(x)
        if block.descriptor_operator is not None:
            h = h + block.descriptor_operator(h)
        shared = block.shared(h)
        scores = block.routing_scores(h) if hasattr(block, "routing_scores") else block.router(h)
        selected_owner = torch.argmax(scores, dim=-1)
        expert_outputs = torch.stack([expert(h) for expert in block.experts], dim=0)
        candidate_losses = []
        for expert_id in range(expert_outputs.shape[0]):
            candidate_x = x + shared + expert_outputs[expert_id]
            candidate_final = _suffix_selected(model, candidate_x, block_idx + 1, mask)
            candidate_losses.append(_loss(model, candidate_final, targets))
        losses_by_expert = torch.stack(candidate_losses, dim=0)
        sorted_losses, sorted_indices = torch.sort(losses_by_expert, dim=0)
        selected_loss = losses_by_expert.gather(0, selected_owner.unsqueeze(0)).squeeze(0)
        regret = selected_loss - sorted_losses[0]
        regret_values.extend(float(item) for item in regret.detach().cpu().reshape(-1))
        selected_rank = (losses_by_expert < selected_loss.unsqueeze(0)).sum(dim=0) + 1
        selected_is_oracle += int((selected_rank == 1).sum().detach().cpu())
        selected_is_top2 += int((selected_rank <= 2).sum().detach().cpu())
        decision_count += int(selected_rank.numel())
        greedy_owner = sorted_indices[0]
        greedy_residual = _gather_expert_outputs(expert_outputs, greedy_owner)
        x = x + shared + greedy_residual

    greedy_loss = _loss(model, x, targets)
    regrets_sorted = sorted(regret_values)
    return {
        "token_count": int(targets.numel()),
        "decision_count": decision_count,
        "selected_loss_sum": float(selected.sum().detach().cpu()),
        "greedy_oracle_loss_sum": float(greedy_loss.sum().detach().cpu()),
        "mean_router_regret_sum": float(sum(regret_values)),
        "regret_count": len(regret_values),
        "p95_router_regret": regrets_sorted[min(len(regrets_sorted) - 1, int(0.95 * len(regrets_sorted)))] if regrets_sorted else None,
        "selected_is_oracle": selected_is_oracle,
        "selected_is_top2": selected_is_top2,
    }


def _summarize(parts: list[dict[str, Any]]) -> dict[str, Any]:
    token_count = sum(row["token_count"] for row in parts)
    regret_count = sum(row["regret_count"] for row in parts)
    p95_values = [row["p95_router_regret"] for row in parts if row.get("p95_router_regret") is not None]
    decision_count = sum(row["decision_count"] for row in parts)
    return {
        "token_count": token_count,
        "decision_count": decision_count,
        "selected_loss": sum(row["selected_loss_sum"] for row in parts) / token_count,
        "greedy_full_network_oracle_loss": sum(row["greedy_oracle_loss_sum"] for row in parts) / token_count,
        "greedy_oracle_improvement_over_selected": (
            sum(row["greedy_oracle_loss_sum"] for row in parts) - sum(row["selected_loss_sum"] for row in parts)
        ) / token_count,
        "mean_router_regret_across_block_decisions": sum(row["mean_router_regret_sum"] for row in parts) / max(1, regret_count),
        "p95_router_regret_block_decision_median_of_batches": sorted(p95_values)[len(p95_values) // 2] if p95_values else None,
        "selected_is_oracle_rate_across_block_decisions": sum(row["selected_is_oracle"] for row in parts) / max(1, decision_count),
        "selected_is_top2_rate_across_block_decisions": sum(row["selected_is_top2"] for row in parts) / max(1, decision_count),
    }


def run(
    *,
    config: str,
    official_like_root: str = "data/eval/official_like_dev",
    output: str = "benchmark/reports/generated/pvr_full_network_greedy_oracle_audit",
    device: str = "cuda",
    seq_len: int = 64,
    max_blocks_per_file: int = 1,
    batch_size: int = 1,
) -> dict[str, Any]:
    cfg, model = _load(config, device)
    rows = []
    all_parts = []
    with torch.no_grad():
        for path in sorted(Path(official_like_root).glob("*.jsonl")):
            parts = [
                _batch_greedy_oracle(model, batch, device=device)
                for batch in _blocks(path, seq_len=seq_len, max_blocks=max_blocks_per_file, batch_size=batch_size)
            ]
            if not parts:
                continue
            summary = _summarize(parts)
            rows.append({"file": path.name, **summary})
            all_parts.extend(parts)
    overall = _summarize(all_parts)
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "experiment": "PVR_FULL_NETWORK_GREEDY_ORACLE_EXPERT_SELECTION",
        "status": "PVR_FULL_NETWORK_GREEDY_ORACLE_EXPERT_SELECTION_COMPLETE",
        "scope": "Official-like development set only. Greedy blockwise full-network oracle; not exhaustive combinatorial oracle.",
        "model_variant": cfg["model_variant"],
        "overall": overall,
        "rows": rows,
        "claim_gates": {
            "greedy_oracle_beats_selected": overall["greedy_full_network_oracle_loss"] < overall["selected_loss"],
            "router_regret_present": overall["mean_router_regret_across_block_decisions"] > 0.0,
            "official_final_files_used": False,
        },
    }
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    write_json(out / "pvr_full_network_greedy_oracle_audit.json", payload)
    lines = [
        "# PVR Full-Network Greedy Oracle Audit",
        "",
        f"Status: `{payload['status']}`",
        "",
        payload["scope"],
        "",
        "## Overall",
        "",
        f"Selected loss: `{overall['selected_loss']}`",
        f"Greedy full-network oracle loss: `{overall['greedy_full_network_oracle_loss']}`",
        f"Greedy oracle improvement over selected: `{overall['greedy_oracle_improvement_over_selected']}`",
        f"Mean router regret across block decisions: `{overall['mean_router_regret_across_block_decisions']}`",
        f"Selected-is-oracle rate across block decisions: `{overall['selected_is_oracle_rate_across_block_decisions']}`",
        f"Selected-is-top2 rate across block decisions: `{overall['selected_is_top2_rate_across_block_decisions']}`",
        "",
        "## Per File",
        "",
        "| file | selected | greedy oracle | delta | oracle rate | top2 rate |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row['file']} | {row['selected_loss']} | {row['greedy_full_network_oracle_loss']} | "
            f"{row['greedy_oracle_improvement_over_selected']} | {row['selected_is_oracle_rate_across_block_decisions']} | "
            f"{row['selected_is_top2_rate_across_block_decisions']} |"
        )
    (out / "pvr_full_network_greedy_oracle_audit.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", required=True)
    parser.add_argument("--official-like-root", default="data/eval/official_like_dev")
    parser.add_argument("--output", default="benchmark/reports/generated/pvr_full_network_greedy_oracle_audit")
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--seq-len", type=int, default=64)
    parser.add_argument("--max-blocks-per-file", type=int, default=1)
    parser.add_argument("--batch-size", type=int, default=1)
    args = parser.parse_args()
    payload = run(**vars(args))
    print(json.dumps({"status": payload["status"], "overall": payload["overall"], "claim_gates": payload["claim_gates"]}, indent=2))


if __name__ == "__main__":
    main()
