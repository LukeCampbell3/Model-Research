"""PVR full/shared/wrong-expert decomposition on bounded official files."""

from __future__ import annotations

import argparse
import contextlib
import json
import types
from pathlib import Path
from typing import Any

import torch
import torch.nn.functional as F

from benchmark.common import load_json_or_yaml, utc_now, write_json
from benchmark.model_factory import build_model


def _patch_pvr_blocks(model, mode: str):
    originals = []
    for block in model.blocks:
        originals.append((block, block.forward))

        def patched(self, x, *, _mode=mode):
            h = self.ln(x)
            if self.descriptor_operator is not None:
                h = h + self.descriptor_operator(h)
            out = self.shared(h)
            if not self.shared_only and _mode != "shared_only":
                scores = self.routing_scores(h) if hasattr(self, "routing_scores") else self.router(h)
                owner = torch.argmax(scores, dim=-1)
                if _mode == "wrong_shift":
                    owner = (owner + 1) % len(self.experts)
                sparse = torch.zeros_like(x)
                for expert_id, expert in enumerate(self.experts):
                    mask = owner == expert_id
                    if mask.any():
                        sparse[mask] = expert(h[mask])
                out = out + sparse
            return x + out

        block.forward = types.MethodType(patched, block)
    return originals


@contextlib.contextmanager
def _intervention(model, mode: str):
    if mode == "full":
        yield
        return
    originals = _patch_pvr_blocks(model, mode)
    try:
        yield
    finally:
        for block, forward in originals:
            block.forward = forward


def _load(config_path: str, device: str):
    config = load_json_or_yaml(config_path)
    materialized = build_model(config, device=device)
    checkpoint = torch.load(config["checkpoint_path"], map_location=device)
    materialized.model.load_state_dict(checkpoint.get("model_state_dict", checkpoint), strict=False)
    materialized.model.eval()
    return config, materialized


def _loss(model, path: Path, *, mode: str, device: str, seq_len: int, max_blocks: int, batch_size: int) -> dict[str, Any]:
    tokens = torch.tensor(list(path.read_bytes()), dtype=torch.long)
    block_count = min(max_blocks, max(0, (len(tokens) - 1) // seq_len))
    losses = []
    with _intervention(model, mode), torch.no_grad():
        for start in range(0, block_count, batch_size):
            rows = []
            for block_index in range(start, min(block_count, start + batch_size)):
                offset = block_index * seq_len
                rows.append(tokens[offset : offset + seq_len + 1])
            if not rows:
                continue
            batch = torch.stack(rows).to(device)
            logits = model(batch[:, :-1])
            loss = F.cross_entropy(
                logits.reshape(-1, logits.shape[-1]),
                batch[:, 1:].reshape(-1),
                reduction="none",
            ).reshape(batch.shape[0], seq_len)
            losses.extend(float(value) for value in loss.mean(dim=1).detach().cpu())
    return {
        "mode": mode,
        "evaluated_blocks": block_count,
        "evaluated_tokens": block_count * seq_len,
        "loss": sum(losses) / len(losses) if losses else None,
    }


def _routing_snapshot(model, path: Path, *, device: str, seq_len: int) -> dict[str, Any]:
    owner_rows = []
    margins = []

    def hook(module, inputs, _output):
        x = inputs[0]
        h = module.ln(x)
        if module.descriptor_operator is not None:
            h = h + module.descriptor_operator(h)
        scores = module.routing_scores(h) if hasattr(module, "routing_scores") else module.router(h)
        top = torch.topk(scores, k=min(2, scores.shape[-1]), dim=-1)
        owner_rows.extend(int(value) for value in top.indices[..., 0].detach().cpu().reshape(-1))
        if top.values.shape[-1] > 1:
            margins.extend(float(value) for value in (top.values[..., 0] - top.values[..., 1]).detach().cpu().reshape(-1))

    handles = [block.register_forward_hook(hook) for block in model.blocks]
    try:
        ids = list(path.read_bytes())[: seq_len + 1]
        if len(ids) < seq_len + 1:
            ids = (ids + [10] * (seq_len + 1))[: seq_len + 1]
        with torch.no_grad():
            model(torch.tensor(ids[:-1], dtype=torch.long, device=device).unsqueeze(0))
    finally:
        for handle in handles:
            handle.remove()
    expert_count = len(model.blocks[0].experts)
    counts = [owner_rows.count(idx) for idx in range(expert_count)]
    total = max(1, sum(counts))
    entropy = 0.0
    for count in counts:
        if count:
            p = count / total
            entropy -= p * torch.log(torch.tensor(p)).item()
    return {
        "owners_per_token": 1.0,
        "top2_execution_count": 0,
        "top4_execution_count": 0,
        "owner_entropy": entropy,
        "prototype_margin": sum(margins) / len(margins) if margins else None,
        "expert_utilization": counts,
        "prototype_monopoly_rate": max(counts) / total if counts else None,
    }


def run(
    *,
    config: str,
    official_root: str = "data/eval/official_300m_bounded",
    output: str,
    device: str = "cuda",
    seq_len: int = 64,
    max_blocks_per_file: int = 32,
    batch_size: int = 8,
) -> dict[str, Any]:
    cfg, materialized = _load(config, device)
    files = sorted(Path(official_root).glob("*.jsonl"))
    rows = []
    for path in files:
        losses = {
            mode: _loss(materialized.model, path, mode=mode, device=device, seq_len=seq_len, max_blocks=max_blocks_per_file, batch_size=batch_size)
            for mode in ("full", "shared_only", "wrong_shift")
        }
        full = losses["full"]["loss"]
        shared = losses["shared_only"]["loss"]
        wrong = losses["wrong_shift"]["loss"]
        rows.append({
            "file": path.name,
            "evaluated_tokens": losses["full"]["evaluated_tokens"],
            "full_loss": full,
            "shared_only_loss": shared,
            "wrong_shift_loss": wrong,
            "full_minus_shared": full - shared,
            "wrong_shift_minus_full": wrong - full,
            "selected_expert_helpful_vs_shared": full < shared,
            "wrong_shift_harms_vs_full": wrong > full,
            "routing": _routing_snapshot(materialized.model, path, device=device, seq_len=seq_len),
        })
    mean_full_minus_shared = sum(row["full_minus_shared"] for row in rows) / len(rows)
    mean_wrong_minus_full = sum(row["wrong_shift_minus_full"] for row in rows) / len(rows)
    status = (
        "PVR_OFFICIAL_DECOMPOSITION_SELECTED_EXPERT_HELP_SUPPORTED"
        if mean_full_minus_shared < 0.0 and mean_wrong_minus_full > 0.0
        else "PVR_OFFICIAL_DECOMPOSITION_SELECTED_EXPERT_HELP_NOT_SUPPORTED"
    )
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "experiment": "PVR_OFFICIAL_SHARED_EXPERT_DECOMPOSITION_AUDIT",
        "status": status,
        "config": config,
        "model_variant": cfg["model_variant"],
        "oracle_expert_selection": "NOT_RUN_NOT_IMPLEMENTED",
        "rows": rows,
        "summary": {
            "mean_full_minus_shared": mean_full_minus_shared,
            "mean_wrong_shift_minus_full": mean_wrong_minus_full,
            "full_beats_shared_files": sum(1 for row in rows if row["selected_expert_helpful_vs_shared"]),
            "wrong_shift_harms_files": sum(1 for row in rows if row["wrong_shift_harms_vs_full"]),
            "file_count": len(rows),
        },
        "interpretation_rule": (
            "If full beats shared and wrong-shift harms, selected experts help. If full fails to beat shared, "
            "the current setup has weak or harmful expert residuals on these files. Oracle routing remains a future audit."
        ),
    }
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    write_json(out / "pvr_official_decomposition_audit.json", payload)
    lines = [
        "# PVR Official Shared/Expert Decomposition Audit",
        "",
        f"Status: `{status}`",
        "",
        f"Mean full-minus-shared: `{mean_full_minus_shared}`",
        f"Mean wrong-shift-minus-full: `{mean_wrong_minus_full}`",
        f"Full beats shared files: `{payload['summary']['full_beats_shared_files']}/{len(rows)}`",
        f"Wrong-shift harms files: `{payload['summary']['wrong_shift_harms_files']}/{len(rows)}`",
        "",
        "| file | full | shared-only | full-shared | wrong-shift | wrong-full | owner entropy | margin |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row['file']} | {row['full_loss']} | {row['shared_only_loss']} | {row['full_minus_shared']} | "
            f"{row['wrong_shift_loss']} | {row['wrong_shift_minus_full']} | {row['routing']['owner_entropy']} | {row['routing']['prototype_margin']} |"
        )
    lines.extend(["", "Oracle expert selection: `NOT_RUN_NOT_IMPLEMENTED`"])
    (out / "pvr_official_decomposition_audit.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
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
    args = parser.parse_args()
    payload = run(**vars(args))
    print(json.dumps({"status": payload["status"], "summary": payload["summary"]}, indent=2))


if __name__ == "__main__":
    main()
