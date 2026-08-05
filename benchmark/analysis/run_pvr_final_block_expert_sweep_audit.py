"""Final-block all-expert sweep and router-regret audit for PVR checkpoints.

This audit evaluates every final-block expert from the same hidden state. It is
therefore a clean same-representation expert identity test, but it is not a
full-network oracle over all PVR blocks.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import json
import random
from pathlib import Path
from typing import Any

import torch
import torch.nn.functional as F

from benchmark.common import load_json_or_yaml, utc_now, write_json
from benchmark.model_factory import build_model


@dataclass
class ExpertSweepResult:
    """All-expert final-block sweep result for one batch."""

    token_count: int
    selected_loss_sum: float
    shared_loss_sum: float
    oracle_loss_sum: float
    second_best_loss_sum: float
    mean_wrong_loss_sum: float
    shifted_wrong_loss_sum: float
    random_wrong_loss_sum: float
    worst_loss_sum: float
    shuffled_residual_loss_sum: float
    random_residual_loss_sum: float
    regrets: list[float]
    selected_is_oracle: int
    selected_is_top2: int
    oracle_gap_to_second_best_sum: float

    def as_dict(self) -> dict[str, Any]:
        return {
            "token_count": self.token_count,
            "selected_loss_sum": self.selected_loss_sum,
            "shared_loss_sum": self.shared_loss_sum,
            "oracle_loss_sum": self.oracle_loss_sum,
            "second_best_loss_sum": self.second_best_loss_sum,
            "mean_wrong_loss_sum": self.mean_wrong_loss_sum,
            "shifted_wrong_loss_sum": self.shifted_wrong_loss_sum,
            "random_wrong_loss_sum": self.random_wrong_loss_sum,
            "worst_loss_sum": self.worst_loss_sum,
            "shuffled_residual_loss_sum": self.shuffled_residual_loss_sum,
            "random_residual_loss_sum": self.random_residual_loss_sum,
            "regrets": self.regrets,
            "selected_is_oracle": self.selected_is_oracle,
            "selected_is_top2": self.selected_is_top2,
            "oracle_gap_to_second_best_sum": self.oracle_gap_to_second_best_sum,
        }


def _load(config_path: str, device: str):
    config = load_json_or_yaml(config_path)
    materialized = build_model(config, device=device)
    checkpoint = torch.load(config["checkpoint_path"], map_location=device, weights_only=False)
    materialized.model.load_state_dict(checkpoint.get("model_state_dict", checkpoint), strict=False)
    materialized.model.eval()
    return config, materialized


def _blocks(path: Path, *, seq_len: int, max_blocks: int, batch_size: int):
    tokens = torch.tensor(list(path.read_bytes()), dtype=torch.long)
    block_count = min(max_blocks, max(0, (len(tokens) - 1) // seq_len))
    for start in range(0, block_count, batch_size):
        rows = []
        for block_index in range(start, min(block_count, start + batch_size)):
            offset = block_index * seq_len
            rows.append(tokens[offset : offset + seq_len + 1])
        if rows:
            yield torch.stack(rows)


def _token_losses(model, x_after_block: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
    logits = model.head(model.ln_f(x_after_block))
    return F.cross_entropy(
        logits.reshape(-1, logits.shape[-1]),
        targets.reshape(-1),
        reduction="none",
    ).reshape(targets.shape)


def _prefix_to_final_block(model, input_ids: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
    seq_len = input_ids.shape[1]
    positions = torch.arange(seq_len, device=input_ids.device).unsqueeze(0)
    x = model.token_emb(input_ids) + model.pos_emb(positions)
    mask = torch.triu(torch.ones(seq_len, seq_len, device=input_ids.device), diagonal=1).bool()
    for attn, block in zip(model.attn[:-1], model.blocks[:-1]):
        x = attn(x, src_mask=mask)
        x = block(x)
    x = model.attn[-1](x, src_mask=mask)
    block = model.blocks[-1]
    h = block.ln(x)
    if block.descriptor_operator is not None:
        h = h + block.descriptor_operator(h)
    shared = block.shared(h)
    scores = block.routing_scores(h) if hasattr(block, "routing_scores") else block.router(h)
    owner = torch.argmax(scores, dim=-1)
    return x, h, shared, owner


def _random_wrong(owner: torch.Tensor, expert_count: int, rng: random.Random, device: str) -> torch.Tensor:
    values = []
    for item in owner.detach().cpu().reshape(-1).tolist():
        choices = [idx for idx in range(expert_count) if idx != int(item)]
        values.append(rng.choice(choices))
    return torch.tensor(values, dtype=torch.long, device=device).reshape(owner.shape)


def _gather(losses_by_expert: torch.Tensor, indices: torch.Tensor) -> torch.Tensor:
    return losses_by_expert.gather(0, indices.unsqueeze(0)).squeeze(0)


def _gather_expert_outputs(expert_outputs: torch.Tensor, indices: torch.Tensor) -> torch.Tensor:
    gather_index = indices.unsqueeze(0).unsqueeze(-1).expand(1, *indices.shape, expert_outputs.shape[-1])
    return expert_outputs.gather(0, gather_index).squeeze(0)


def evaluate_all_experts(
    model,
    input_ids: torch.Tensor,
    attention_mask: torch.Tensor | None = None,
    *,
    rng: random.Random | None = None,
    device: str = "cuda",
) -> ExpertSweepResult:
    """Return shared-only, selected, every-expert, random, shifted, and oracle losses.

    All final-block expert comparisons use the same prefix/shared hidden state.
    `input_ids` must include one extra target position; losses are computed on
    next-token targets from `input_ids[:, 1:]`.
    """
    del attention_mask
    rng = rng or random.Random(0)
    input_ids = input_ids.to(device)
    targets = input_ids[:, 1:]
    input_ids = input_ids[:, :-1]
    base_x, h, shared, owner = _prefix_to_final_block(model, input_ids)
    block = model.blocks[-1]
    expert_outputs = torch.stack([expert(h) for expert in block.experts], dim=0)
    expert_count = expert_outputs.shape[0]

    losses_by_expert = []
    for expert_id in range(expert_count):
        losses_by_expert.append(_token_losses(model, base_x + shared + expert_outputs[expert_id], targets))
    losses_by_expert_tensor = torch.stack(losses_by_expert, dim=0)
    sorted_losses, sorted_indices = torch.sort(losses_by_expert_tensor, dim=0)

    selected = _gather(losses_by_expert_tensor, owner)
    oracle = sorted_losses[0]
    oracle_idx = sorted_indices[0]
    second_best = sorted_losses[1] if expert_count > 1 else sorted_losses[0]
    worst = sorted_losses[-1]
    shifted_idx = (owner + 1) % expert_count
    random_idx = _random_wrong(owner, expert_count, rng, device)
    shifted = _gather(losses_by_expert_tensor, shifted_idx)
    random_wrong = _gather(losses_by_expert_tensor, random_idx)
    wrong_mask = torch.ones_like(losses_by_expert_tensor, dtype=torch.bool)
    wrong_mask.scatter_(0, owner.unsqueeze(0), False)
    mean_wrong = losses_by_expert_tensor.masked_fill(~wrong_mask, 0.0).sum(dim=0) / max(1, expert_count - 1)
    shared_only = _token_losses(model, base_x + shared, targets)

    selected_residual = _gather_expert_outputs(expert_outputs, owner)
    flat_residual = selected_residual.reshape(-1, selected_residual.shape[-1])
    permutation = torch.randperm(flat_residual.shape[0], device=device)
    shuffled_residual = flat_residual[permutation].reshape_as(selected_residual)
    shuffled = _token_losses(model, base_x + shared + shuffled_residual, targets)
    random_residual = torch.randn_like(selected_residual)
    random_residual = F.normalize(random_residual, dim=-1) * selected_residual.norm(dim=-1, keepdim=True)
    random_residual_loss = _token_losses(model, base_x + shared + random_residual, targets)

    selected_rank = (losses_by_expert_tensor < selected.unsqueeze(0)).sum(dim=0) + 1
    regret = selected - oracle
    return ExpertSweepResult(
        token_count=int(targets.numel()),
        selected_loss_sum=float(selected.sum().detach().cpu()),
        shared_loss_sum=float(shared_only.sum().detach().cpu()),
        oracle_loss_sum=float(oracle.sum().detach().cpu()),
        second_best_loss_sum=float(second_best.sum().detach().cpu()),
        mean_wrong_loss_sum=float(mean_wrong.sum().detach().cpu()),
        shifted_wrong_loss_sum=float(shifted.sum().detach().cpu()),
        random_wrong_loss_sum=float(random_wrong.sum().detach().cpu()),
        worst_loss_sum=float(worst.sum().detach().cpu()),
        shuffled_residual_loss_sum=float(shuffled.sum().detach().cpu()),
        random_residual_loss_sum=float(random_residual_loss.sum().detach().cpu()),
        regrets=[float(value) for value in regret.detach().cpu().reshape(-1)],
        selected_is_oracle=int((selected_rank == 1).sum().detach().cpu()),
        selected_is_top2=int((selected_rank <= 2).sum().detach().cpu()),
        oracle_gap_to_second_best_sum=float((second_best - oracle).sum().detach().cpu()),
    )


def _batch_sweep(model, batch: torch.Tensor, *, rng: random.Random, device: str) -> dict[str, Any]:
    return evaluate_all_experts(model, batch, rng=rng, device=device).as_dict()


def _summarize(parts: list[dict[str, Any]]) -> dict[str, Any]:
    token_count = sum(part["token_count"] for part in parts)
    regrets = [value for part in parts for value in part["regrets"]]
    regrets_sorted = sorted(regrets)

    def mean(key: str) -> float:
        return sum(part[key] for part in parts) / token_count

    return {
        "token_count": token_count,
        "selected_loss": mean("selected_loss_sum"),
        "shared_only_loss": mean("shared_loss_sum"),
        "oracle_loss": mean("oracle_loss_sum"),
        "second_best_loss": mean("second_best_loss_sum"),
        "mean_wrong_loss": mean("mean_wrong_loss_sum"),
        "shifted_wrong_loss": mean("shifted_wrong_loss_sum"),
        "random_wrong_loss": mean("random_wrong_loss_sum"),
        "worst_loss": mean("worst_loss_sum"),
        "shuffled_residual_loss": mean("shuffled_residual_loss_sum"),
        "random_residual_loss": mean("random_residual_loss_sum"),
        "mean_router_regret": sum(regrets) / max(1, len(regrets)),
        "p95_router_regret": regrets_sorted[min(len(regrets_sorted) - 1, int(0.95 * len(regrets_sorted)))] if regrets_sorted else None,
        "selected_is_oracle_rate": sum(part["selected_is_oracle"] for part in parts) / token_count,
        "selected_is_top2_rate": sum(part["selected_is_top2"] for part in parts) / token_count,
        "mean_oracle_gap_to_second_best": mean("oracle_gap_to_second_best_sum"),
    }


def _load_comparator_losses(path: str | None) -> dict[str, float]:
    if not path:
        return {}
    report_path = Path(path)
    if not report_path.exists():
        return {}
    report = json.loads(report_path.read_text(encoding="utf-8"))
    losses = {}
    candidate = report.get("candidate") or {}
    if candidate.get("model_variant") and isinstance(candidate.get("micro_loss"), (int, float)):
        losses[candidate["model_variant"]] = float(candidate["micro_loss"])
    for row in report.get("baselines", []):
        if row.get("model_variant") and isinstance(row.get("micro_loss"), (int, float)):
            losses[row["model_variant"]] = float(row["micro_loss"])
    return losses


def run(
    *,
    config: str,
    official_root: str = "data/eval/official_300m_bounded",
    output: str,
    device: str = "cuda",
    seq_len: int = 64,
    max_blocks_per_file: int = 32,
    batch_size: int = 8,
    seed: int = 20260715,
    comparator_aggregation_report: str | None = "benchmark/reports/generated/sparse_v2_300m_official_aggregation_reversal_audit/official_aggregation_reversal_audit.json",
) -> dict[str, Any]:
    cfg, materialized = _load(config, device)
    files = sorted(Path(official_root).glob("*.jsonl"))
    rng = random.Random(seed)
    rows = []
    all_parts = []
    with torch.no_grad():
        for path in files:
            parts = [
                _batch_sweep(materialized.model, batch, rng=rng, device=device)
                for batch in _blocks(path, seq_len=seq_len, max_blocks=max_blocks_per_file, batch_size=batch_size)
            ]
            summary = _summarize(parts)
            rows.append({"file": path.name, **summary})
            all_parts.extend(parts)
    overall = _summarize(all_parts)
    selected_gate = (
        overall["selected_loss"] < overall["shared_only_loss"]
        and overall["selected_loss"] < overall["mean_wrong_loss"]
        and overall["selected_loss"] < overall["shuffled_residual_loss"]
        and overall["selected_loss"] < overall["random_residual_loss"]
    )
    comparator_losses = _load_comparator_losses(comparator_aggregation_report)
    oracle_comparator_deltas = {
        variant: overall["oracle_loss"] - loss
        for variant, loss in comparator_losses.items()
        if variant != cfg["model_variant"]
    }
    status = "PVR_OFFICIAL_ORACLE_EXPERT_REGRET_AUDIT_COMPLETE"
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "experiment": "PVR_OFFICIAL_FINAL_BLOCK_ORACLE_EXPERT_REGRET_AUDIT",
        "status": status,
        "scope_label": "PVR_OFFICIAL_FINAL_BLOCK_ORACLE_EXPERT_REGRET_AUDIT_COMPLETE",
        "scope": "Final PVR block only; every expert is evaluated from identical final-block hidden states. Full-network oracle routing remains NOT_RUN_NOT_IMPLEMENTED.",
        "config": config,
        "model_variant": cfg["model_variant"],
        "rows": rows,
        "overall": overall,
        "claim_gates": {
            "selected_beats_shared_only": overall["selected_loss"] < overall["shared_only_loss"],
            "selected_beats_mean_wrong": overall["selected_loss"] < overall["mean_wrong_loss"],
            "selected_beats_shuffled_residual": overall["selected_loss"] < overall["shuffled_residual_loss"],
            "selected_beats_random_residual": overall["selected_loss"] < overall["random_residual_loss"],
            "selected_intervention_gate_pass": selected_gate,
            "final_block_oracle_beats_switch_top1": oracle_comparator_deltas.get("switch_top1_sparse_v2_300m_matched", 0.0) < 0.0,
            "final_block_oracle_beats_generic_top2": oracle_comparator_deltas.get("generic_top2_sparse_v2_300m_matched", 0.0) < 0.0,
        },
        "final_block_oracle_vs_comparators": {
            "source": comparator_aggregation_report,
            "comparator_micro_losses": comparator_losses,
            "oracle_minus_comparator_micro_loss": oracle_comparator_deltas,
            "scope_caveat": "Compares final-block oracle intervention loss to independently evaluated comparator micro losses on the same official file/block budget. This is diagnostic capacity evidence, not a deployable full-network oracle model.",
        },
        "not_run": {
            "full_network_oracle_expert_selection": "NOT_RUN_NOT_IMPLEMENTED",
            "full_network_oracle_improvement_over_switch": "NOT_RUN_NOT_IMPLEMENTED",
            "full_network_oracle_improvement_over_top2": "NOT_RUN_NOT_IMPLEMENTED",
        },
    }
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    write_json(out / "pvr_final_block_expert_sweep_audit.json", payload)
    lines = [
        "# PVR Final-Block Expert Sweep and Router-Regret Audit",
        "",
        f"Status: `{status}`",
        "",
        payload["scope"],
        "",
        "## Overall",
        "",
        f"Selected loss: `{overall['selected_loss']}`",
        f"Shared-only loss: `{overall['shared_only_loss']}`",
        f"Oracle loss: `{overall['oracle_loss']}`",
        f"Mean wrong loss: `{overall['mean_wrong_loss']}`",
        f"Shifted wrong loss: `{overall['shifted_wrong_loss']}`",
        f"Random wrong loss: `{overall['random_wrong_loss']}`",
        f"Shuffled residual loss: `{overall['shuffled_residual_loss']}`",
        f"Random residual loss: `{overall['random_residual_loss']}`",
        f"Mean router regret: `{overall['mean_router_regret']}`",
        f"95th-percentile router regret: `{overall['p95_router_regret']}`",
        f"Selected-is-oracle rate: `{overall['selected_is_oracle_rate']}`",
        f"Selected-is-top2 rate: `{overall['selected_is_top2_rate']}`",
        "",
        "## Claim Gates",
        "",
        *[f"- {key}: `{value}`" for key, value in payload["claim_gates"].items()],
        "",
        "## Final-Block Oracle vs Comparators",
        "",
        payload["final_block_oracle_vs_comparators"]["scope_caveat"],
        "",
        "| comparator | comparator micro loss | oracle - comparator |",
        "|---|---:|---:|",
        *[
            f"| {variant} | {comparator_losses[variant]} | {delta} |"
            for variant, delta in oracle_comparator_deltas.items()
        ],
        "",
        "## Per File",
        "",
        "| file | selected | shared | oracle | mean wrong | shifted wrong | random wrong | regret | oracle rate | top2 rate |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row['file']} | {row['selected_loss']} | {row['shared_only_loss']} | {row['oracle_loss']} | "
            f"{row['mean_wrong_loss']} | {row['shifted_wrong_loss']} | {row['random_wrong_loss']} | "
            f"{row['mean_router_regret']} | {row['selected_is_oracle_rate']} | {row['selected_is_top2_rate']} |"
        )
    lines.extend([
        "",
        "Full-network oracle expert selection: `NOT_RUN_NOT_IMPLEMENTED`",
        "Full-network oracle improvement over Switch/Top2: `NOT_RUN_NOT_IMPLEMENTED`",
    ])
    (out / "pvr_final_block_expert_sweep_audit.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", required=True)
    parser.add_argument("--official-root", default="data/eval/official_300m_bounded")
    parser.add_argument("--output", required=True)
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--seq-len", type=int, default=64)
    parser.add_argument("--max-blocks-per-file", type=int, default=32)
    parser.add_argument("--batch-size", type=int, default=8)
    parser.add_argument("--seed", type=int, default=20260715)
    parser.add_argument(
        "--comparator-aggregation-report",
        default="benchmark/reports/generated/sparse_v2_300m_official_aggregation_reversal_audit/official_aggregation_reversal_audit.json",
    )
    args = parser.parse_args()
    payload = run(**vars(args))
    print(json.dumps({"status": payload["status"], "overall": payload["overall"], "claim_gates": payload["claim_gates"]}, indent=2))


if __name__ == "__main__":
    main()
