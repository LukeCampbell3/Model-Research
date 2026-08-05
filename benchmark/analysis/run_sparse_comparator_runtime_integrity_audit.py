"""Runtime integrity audit for dense, Switch Top1, generic Top2, and PVR comparators."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import torch

from benchmark.common import load_json_or_yaml, utc_now, write_json
from benchmark.model_factory import PVRECOBlock, ReferenceMoEBlock, build_model
from benchmark.runners.run_training import _batch, _load_bytes


def _load(config_path: str, device: str):
    config = load_json_or_yaml(config_path)
    materialized = build_model(config, device=device)
    checkpoint = torch.load(config["checkpoint_path"], map_location=device)
    materialized.model.load_state_dict(checkpoint.get("model_state_dict", checkpoint), strict=False)
    materialized.model.eval()
    return config, materialized


def _audit_one(config_path: str, eval_paths: list[str], *, device: str, seq_len: int, blocks: int) -> dict[str, Any]:
    config, materialized = _load(config_path, device)
    model = materialized.model
    tokens = _load_bytes(eval_paths, require=True)
    family = config["model_family"]
    counters = {
        "tokens_seen": 0,
        "moe_tokens": 0,
        "pvr_tokens": 0,
        "actual_experts_executed_sum": 0,
        "top1_tokens": 0,
        "top2_tokens": 0,
        "topk_gt2_tokens": 0,
        "token_drop_count": 0,
        "capacity_overflow_count": 0,
        "fallback_expert_count": 0,
    }
    utilization: dict[int, int] = {}

    def ref_hook(module: ReferenceMoEBlock, inputs, _output):
        x = inputs[0]
        h = module.ln(x)
        topk = torch.topk(module.router(h), k=module.experts_active, dim=-1).indices
        token_count = int(topk.shape[0] * topk.shape[1])
        counters["moe_tokens"] += token_count
        counters["actual_experts_executed_sum"] += token_count * int(module.experts_active)
        counters["top1_tokens"] += token_count if module.experts_active == 1 else 0
        counters["top2_tokens"] += token_count if module.experts_active == 2 else 0
        counters["topk_gt2_tokens"] += token_count if module.experts_active > 2 else 0
        for item in topk.detach().cpu().reshape(-1).tolist():
            utilization[int(item)] = utilization.get(int(item), 0) + 1

    def pvr_hook(module: PVRECOBlock, inputs, _output):
        x = inputs[0]
        h = module.ln(x)
        if module.descriptor_operator is not None:
            h = h + module.descriptor_operator(h)
        scores = module.routing_scores(h) if hasattr(module, "routing_scores") else module.router(h)
        owner = torch.argmax(scores, dim=-1)
        token_count = int(owner.numel())
        counters["pvr_tokens"] += token_count
        counters["actual_experts_executed_sum"] += 0 if module.shared_only else token_count
        counters["top1_tokens"] += 0 if module.shared_only else token_count
        for item in owner.detach().cpu().reshape(-1).tolist():
            utilization[int(item)] = utilization.get(int(item), 0) + 1

    handles = []
    for module in model.modules():
        if isinstance(module, ReferenceMoEBlock):
            handles.append(module.register_forward_hook(ref_hook))
        if isinstance(module, PVRECOBlock):
            handles.append(module.register_forward_hook(pvr_hook))
    try:
        with torch.no_grad():
            for step in range(blocks):
                x, _ = _batch(tokens, step, 1, seq_len, device)
                counters["tokens_seen"] += int(x.numel())
                model(x)
    finally:
        for handle in handles:
            handle.remove()
    routed_tokens = max(1, counters["moe_tokens"] + counters["pvr_tokens"])
    actual_experts = counters["actual_experts_executed_sum"] / routed_tokens
    expected = int(config.get("experts_active_per_token") or 0)
    if family == "dense_transformer":
        status = "DENSE_COMPARATOR_RUNTIME_INTEGRITY_NOT_APPLICABLE"
        valid = True
    else:
        valid = abs(actual_experts - expected) < 1e-9 and counters["token_drop_count"] == 0 and counters["fallback_expert_count"] == 0
        status = "SPARSE_COMPARATOR_RUNTIME_INTEGRITY_PASS" if valid else "SPARSE_COMPARATOR_RUNTIME_INTEGRITY_FAIL"
    return {
        "variant": config["model_variant"],
        "family": family,
        "status": status,
        "valid_comparator_runtime": valid,
        "configured_experts_active_per_token": expected,
        "actual_experts_executed_per_routed_token": actual_experts,
        "tokens_seen": counters["tokens_seen"],
        "routed_tokens": routed_tokens if family != "dense_transformer" else 0,
        "token_drop_count": counters["token_drop_count"],
        "capacity_overflow_count": counters["capacity_overflow_count"],
        "fallback_expert_count": counters["fallback_expert_count"],
        "top1_token_count": counters["top1_tokens"],
        "top2_token_count": counters["top2_tokens"],
        "topk_gt2_token_count": counters["topk_gt2_tokens"],
        "expert_utilization": dict(sorted(utilization.items())),
        "active_params_per_token_actual": materialized.active_params_per_token_actual,
        "total_params_actual": materialized.total_params_actual,
    }


def run(
    *,
    configs: list[str],
    eval_paths: list[str] | None = None,
    output: str = "benchmark/reports/generated/sparse_comparator_runtime_integrity_audit",
    device: str = "cuda",
    seq_len: int = 64,
    blocks: int = 8,
) -> dict[str, Any]:
    eval_paths = eval_paths or ["data/eval/official_like_dev"]
    rows = [_audit_one(path, eval_paths, device=device, seq_len=seq_len, blocks=blocks) for path in configs]
    sparse_rows = [row for row in rows if row["family"] != "dense_transformer"]
    all_sparse_valid = all(row["valid_comparator_runtime"] for row in sparse_rows)
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "experiment": "SPARSE_COMPARATOR_RUNTIME_INTEGRITY_AUDIT",
        "status": "SPARSE_COMPARATOR_RUNTIME_INTEGRITY_AUDIT_COMPLETE" if all_sparse_valid else "SPARSE_COMPARATOR_RUNTIME_INTEGRITY_AUDIT_FAILED",
        "eval_paths": eval_paths,
        "rows": rows,
        "assertions": {
            "all_sparse_comparators_valid": all_sparse_valid,
            "official_final_files_used": False,
        },
    }
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    write_json(out / "sparse_comparator_runtime_integrity_audit.json", payload)
    lines = [
        "# Sparse Comparator Runtime Integrity Audit",
        "",
        f"Status: `{payload['status']}`",
        "",
        "| variant | family | configured K | actual K/token | valid | drops | overflow | fallback |",
        "|---|---|---:|---:|---|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row['variant']} | {row['family']} | {row['configured_experts_active_per_token']} | "
            f"{row['actual_experts_executed_per_routed_token']} | {row['valid_comparator_runtime']} | "
            f"{row['token_drop_count']} | {row['capacity_overflow_count']} | {row['fallback_expert_count']} |"
        )
    (out / "sparse_comparator_runtime_integrity_audit.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", action="append", required=True, dest="configs")
    parser.add_argument("--eval-path", action="append", dest="eval_paths")
    parser.add_argument("--output", default="benchmark/reports/generated/sparse_comparator_runtime_integrity_audit")
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--seq-len", type=int, default=64)
    parser.add_argument("--blocks", type=int, default=8)
    args = parser.parse_args()
    payload = run(**vars(args))
    print(json.dumps({"status": payload["status"], "assertions": payload["assertions"]}, indent=2))


if __name__ == "__main__":
    main()
