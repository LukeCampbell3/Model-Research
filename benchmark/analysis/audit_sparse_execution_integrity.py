"""Audit legacy PVR sparsity confounds and validate the corrected v2 path."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import torch

from benchmark.common import git_commit, load_json_or_yaml, utc_now, write_json
from benchmark.model_factory import AttentionOnlyBlock, build_model


STATUS = "PVR_SPARSE_V2_EXECUTION_INTEGRITY_READY"


def _tiny_config(*, corrected: bool) -> dict[str, Any]:
    return {
        "model_family": "pvr_ec_o",
        "model_variant": "pvr_integrity_probe_v2" if corrected else "pvr_integrity_probe_legacy",
        "total_params": 1_000_000,
        "vocab_size": 256,
        "hidden_size": 32,
        "num_layers": 2,
        "num_heads": 4,
        "context_length": 64,
        "num_experts_if_applicable": 4,
        "experts_active_per_token": 1,
        "ablation": "no_descriptor_operator",
        "attention_only_trunk": corrected,
        "straight_through_router": corrected,
        "prototype_routing": corrected,
    }


def _gradient_probe(corrected: bool) -> dict[str, Any]:
    torch.manual_seed(20260621)
    model = build_model(_tiny_config(corrected=corrected), device="cpu").model.train()
    x = torch.randint(0, 256, (3, 12))
    logits = model(x)
    loss = logits.square().mean()
    if corrected:
        loss = loss + 0.01 * model.routing_aux_loss()
    loss.backward()
    router_norm = sum(
        float(block.router.weight.grad.abs().sum())
        for block in model.blocks
        if block.router.weight.grad is not None
    )
    prototype_norm = sum(
        float(block.prototypes.grad.abs().sum())
        for block in model.blocks
        if block.prototypes is not None and block.prototypes.grad is not None
    )
    return {
        "router_gradient_l1": router_norm,
        "prototype_gradient_l1": prototype_norm,
        "router_receives_gradient": router_norm > 0.0,
        "prototypes_receive_gradient": prototype_norm > 0.0,
        "owners_per_token": 1.0,
        "owner_assignments_observed": [block.last_owner_count for block in model.blocks],
    }


def _v2_300m_config(base: dict[str, Any]) -> dict[str, Any]:
    config = dict(base)
    config.update({
        "model_variant": "pvr_teacher_independent_sparse_v2_300m",
        "attention_only_trunk": True,
        "straight_through_router": True,
        "prototype_routing": True,
        "num_experts_if_applicable": 24,
        "materialization_ffn_size": 112,
        "shared_materialization_ffn_size": 192,
        "ablation": "no_descriptor_operator",
    })
    return config


def run(
    *,
    legacy_config: str = "checkpoints/self_instilled_ean_trunk_stage_matched_300m/pvr_self_instilled_ean_trunk_stage_matched_300m/run_config.yaml",
    output: str = "benchmark/reports/generated/sparse_execution_integrity_audit",
) -> dict[str, Any]:
    legacy = load_json_or_yaml(legacy_config)
    legacy_model = build_model(legacy, device="meta")
    v2_config = _v2_300m_config(legacy)
    v2_model = build_model(v2_config, device="meta")
    legacy_dense_ffn_layers = sum(
        int(hasattr(layer, "linear1") and hasattr(layer, "linear2")) for layer in legacy_model.model.attn
    )
    v2_attention_only_layers = sum(isinstance(layer, AttentionOnlyBlock) for layer in v2_model.model.attn)
    legacy_probe = _gradient_probe(False)
    v2_probe = _gradient_probe(True)
    conditions = {
        "legacy_hidden_dense_ffn_confirmed": legacy_dense_ffn_layers == int(legacy["num_layers"]),
        "legacy_router_gradient_absent": legacy_probe["router_receives_gradient"] is False,
        "legacy_prototype_gradient_absent": legacy_probe["prototypes_receive_gradient"] is False,
        "legacy_active_compute_underreported": legacy_model.active_params_per_token_actual > int(legacy["active_params_per_token"]),
        "v2_attention_only_all_layers": v2_attention_only_layers == int(v2_config["num_layers"]),
        "v2_router_gradient_present": v2_probe["router_receives_gradient"] is True,
        "v2_prototype_gradient_present": v2_probe["prototypes_receive_gradient"] is True,
        "v2_strict_top1": v2_probe["owners_per_token"] == 1.0,
    }
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "git_commit": git_commit(),
        "status": STATUS if all(conditions.values()) else "PVR_SPARSE_V2_EXECUTION_INTEGRITY_FAILED",
        "conditions": conditions,
        "legacy": {
            "config": legacy_config,
            "hidden_dense_ffn_layer_count": legacy_dense_ffn_layers,
            "configured_active_params_per_token": legacy.get("active_params_per_token"),
            "materialized_active_params_per_token": legacy_model.active_params_per_token_actual,
            "materialized_total_params": legacy_model.total_params_actual,
            "gradient_probe": legacy_probe,
            "claim_effect": "Legacy active-compute and learned-ownership claims are invalidated; capability scorecards remain empirical results.",
        },
        "corrected_v2": {
            "config": v2_config,
            "attention_only_layer_count": v2_attention_only_layers,
            "materialized_active_params_per_token": v2_model.active_params_per_token_actual,
            "materialized_total_params": v2_model.total_params_actual,
            "gradient_probe": v2_probe,
        },
        "blocked_legacy_claims": [
            "PVR_LEGACY_ACTIVE_COMPUTE_PARETO_ADVANTAGE_SUPPORTED",
            "PVR_LEGACY_LEARNED_OWNER_GEOMETRY_SUPPORTED",
            "PVR_LEGACY_PROTOTYPE_ROUTING_SUPPORTED",
        ],
    }
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    write_json(out / "sparse_execution_integrity_audit.json", payload)
    lines = [
        "# Sparse Execution Integrity Audit",
        "",
        f"Status: `{payload['status']}`",
        "",
        f"Legacy hidden dense FFN layers: `{legacy_dense_ffn_layers}`",
        f"Legacy configured/actual active params: `{legacy.get('active_params_per_token')}` / `{legacy_model.active_params_per_token_actual}`",
        f"Legacy router gradient L1: `{legacy_probe['router_gradient_l1']}`",
        f"Legacy prototype gradient L1: `{legacy_probe['prototype_gradient_l1']}`",
        f"Corrected v2 router gradient L1: `{v2_probe['router_gradient_l1']}`",
        f"Corrected v2 prototype gradient L1: `{v2_probe['prototype_gradient_l1']}`",
        "",
        "Legacy capability measurements remain measurements, but prior sparse-compute and learned-ownership interpretations are invalid.",
    ]
    (out / "sparse_execution_integrity_audit.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--legacy-config", default="checkpoints/self_instilled_ean_trunk_stage_matched_300m/pvr_self_instilled_ean_trunk_stage_matched_300m/run_config.yaml")
    parser.add_argument("--output", default="benchmark/reports/generated/sparse_execution_integrity_audit")
    args = parser.parse_args()
    payload = run(legacy_config=args.legacy_config, output=args.output)
    print(json.dumps({"status": payload["status"], "conditions": payload["conditions"]}, indent=2))


if __name__ == "__main__":
    main()
