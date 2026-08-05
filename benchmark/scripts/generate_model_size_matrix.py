"""Generate the PVR-EC-O multi-size benchmark matrix and manifests."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from benchmark.common import REQUIRED_MODEL_CONFIG_FIELDS, manifest_payload, utc_now, write_json


SIZE_SPECS: dict[str, dict[str, int]] = {
    "100m": {"total_params": 100_000_000, "layers": 12, "hidden": 768, "heads": 12, "training_tokens": 20_000_000_000},
    "300m": {"total_params": 300_000_000, "layers": 24, "hidden": 1024, "heads": 16, "training_tokens": 60_000_000_000},
    "700m": {"total_params": 700_000_000, "layers": 32, "hidden": 1536, "heads": 24, "training_tokens": 140_000_000_000},
    "1_3b": {"total_params": 1_300_000_000, "layers": 40, "hidden": 2048, "heads": 32, "training_tokens": 260_000_000_000},
}

EVAL_SUITE = [
    "lm_c4_heldout",
    "lm_wikitext_103",
    "lm_pg19",
    "mmlu_pro",
    "gpqa",
    "bbh",
    "musr",
    "math_lvl_5",
    "ifeval",
    "arc_challenge",
    "hellaswag",
    "truthfulqa",
    "winogrande",
    "boolq",
    "gsm8k",
    "routing_sensitive_nlp_probes",
    "humaneval_plus",
    "mbpp_plus",
    "bigcodebench_complete",
    "bigcodebench_instruct",
    "livecodebench",
    "repobench",
]


def _active_params(total: int, family: str, experts_active: int) -> int:
    if family == "dense_transformer":
        return total
    if family in {"vanilla_switch_top1_reference", "pvr_ec_o"}:
        return int(total * 0.35)
    if family == "generic_top2_moe_reference":
        return int(total * 0.50)
    return total


def _config(
    *,
    family: str,
    variant: str,
    size: str,
    comparison_group: str,
    is_primary_baseline: bool,
    is_internal_strong_router_control: bool = False,
    ablation: str | None = None,
) -> dict[str, Any]:
    spec = SIZE_SPECS[size]
    experts = 0 if family == "dense_transformer" else 8
    active_experts = 0 if family == "dense_transformer" else (2 if family == "generic_top2_moe_reference" else 1)
    active_params = _active_params(spec["total_params"], family, active_experts)
    cfg = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "model_family": family,
        "model_variant": variant,
        "model_size_label": size,
        "total_params": spec["total_params"],
        "active_params_per_token": active_params,
        "active_flops_estimate": int(active_params * 6),
        "num_layers": spec["layers"],
        "hidden_size": spec["hidden"],
        "num_heads": spec["heads"],
        "num_experts_if_applicable": experts,
        "experts_active_per_token": active_experts,
        "context_length": 4096,
        "training_tokens": spec["training_tokens"],
        "batch_tokens": 1_048_576,
        "optimizer": "adamw",
        "scheduler": "cosine_with_warmup",
        "eval_suite": EVAL_SUITE,
        "output_path": f"benchmark/reports/generated/{variant}",
        "comparison_group": comparison_group,
        "is_primary_baseline": is_primary_baseline,
        "is_internal_strong_router_control": is_internal_strong_router_control,
        "tokenizer": "tiktoken_compatible_bpe",
        "precision": "bf16",
        "checkpoint_path": f"checkpoints/benchmark_{size}/{variant}/checkpoint.pt",
        "training_data_paths": ["data/broad_nlp_train"],
        "eval_data_paths": ["data/eval/broad_nlp", "data/eval/coding", "data/eval/routing_probes"],
        "contamination_scan_required": True,
        "fairness_views": [
            "parameter_matched",
            "active_parameter_matched",
            "training_token_matched",
            "wall_clock_matched",
            "inference_budget_matched",
        ],
        "public_positioning_only": False,
        "ablation": ablation,
    }
    missing = [field for field in REQUIRED_MODEL_CONFIG_FIELDS if field not in cfg]
    if missing:
        raise AssertionError(f"Generated config missing fields: {missing}")
    return cfg


def _public_config(variant: str, size_band: str, model_family: str) -> dict[str, Any]:
    size = "300m" if size_band == "small" else "700m"
    cfg = _config(
        family=model_family,
        variant=variant,
        size=size,
        comparison_group="external_positioning_only",
        is_primary_baseline=False,
    )
    cfg.update({
        "public_positioning_only": True,
        "not_controlled_architecture_evidence": True,
        "requires_external_checkpoint": True,
        "checkpoint_path": f"external_checkpoints/{variant}",
        "training_data_paths": [],
        "eval_data_paths": ["data/eval/broad_nlp", "data/eval/coding"],
        "notes": "Public model positioning only; not controlled architecture evidence unless tokenizer, data, training budget, contamination exposure, and inference setup are controlled.",
    })
    return cfg


def model_configs() -> list[dict[str, Any]]:
    configs: list[dict[str, Any]] = []
    for size in ["100m", "300m", "700m", "1_3b"]:
        configs.append(_config(
            family="dense_transformer",
            variant=f"dense_transformer_{size}",
            size=size,
            comparison_group="primary_generalized_baseline",
            is_primary_baseline=True,
        ))
        configs.append(_config(
            family="vanilla_switch_top1_reference",
            variant=f"vanilla_switch_top1_reference_{size}",
            size=size,
            comparison_group="primary_generalized_reference_moe",
            is_primary_baseline=True,
        ))
        configs.append(_config(
            family="pvr_ec_o",
            variant=f"pvr_ec_o_full_{size}",
            size=size,
            comparison_group="pvr_ec_o_primary",
            is_primary_baseline=False,
        ))
    for size in ["100m", "300m", "700m"]:
        configs.append(_config(
            family="generic_top2_moe_reference",
            variant=f"generic_top2_moe_reference_{size}",
            size=size,
            comparison_group="primary_generalized_reference_moe",
            is_primary_baseline=True,
        ))
        for ablation in ["no_prototypes", "no_contrastive_geometry", "no_descriptor_operator", "shared_only"]:
            configs.append(_config(
                family="pvr_ec_o",
                variant=f"pvr_ec_o_{ablation}_{size}",
                size=size,
                comparison_group="pvr_ec_o_ablation",
                is_primary_baseline=False,
                ablation=ablation,
            ))
    configs.append(_config(
        family="custom_fixed_moe_strong_router",
        variant="custom_fixed_moe_strong_router_700m",
        size="700m",
        comparison_group="internal_strong_router_control",
        is_primary_baseline=False,
        is_internal_strong_router_control=True,
    ))
    for variant, size_band, family in [
        ("public_dense_small", "small", "public_dense"),
        ("public_dense_mid", "mid", "public_dense"),
        ("public_instruction_small", "small", "public_instruction"),
        ("public_instruction_mid", "mid", "public_instruction"),
        ("public_code_small", "small", "public_code"),
        ("public_code_mid", "mid", "public_code"),
        ("public_moe_if_available", "mid", "public_moe"),
    ]:
        configs.append(_public_config(variant, size_band, family))
    return configs


def _write_yaml_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def _suite_payload(configs: list[dict[str, Any]], size: str) -> dict[str, Any]:
    primary = [
        cfg for cfg in configs
        if cfg["model_size_label"] == size
        and cfg["comparison_group"] in {"primary_generalized_baseline", "primary_generalized_reference_moe", "pvr_ec_o_primary", "pvr_ec_o_ablation"}
    ]
    return {
        "schema_version": "1.0",
        "suite_name": f"pvr_ec_o_{size}_genuine_architecture_benchmark",
        "stage": f"genuine_{size}_architecture_benchmark",
        "subset_label": "genuine_reduced_eval",
        "models": [
            {
                "model_variant": cfg["model_variant"],
                "config_path": f"benchmark/configs/generated/{cfg['model_variant']}.yaml",
                "comparison_group": cfg["comparison_group"],
            }
            for cfg in primary
        ],
        "required_artifacts": [
            "scorecards",
            "manifests",
            "routing_diagnostics",
            "contamination_scan",
            "benchmark_report",
        ],
        "evidence_rule": "Only runs with real checkpoint, real data, routing diagnostics, contamination scan, and scorecards count as benchmark evidence.",
    }


def generate(root: str | Path = ".") -> dict[str, Any]:
    base = Path(root)
    config_dir = base / "benchmark" / "configs" / "generated"
    manifest_dir = base / "benchmark" / "manifests"
    configs = model_configs()
    for cfg in configs:
        _write_yaml_json(config_dir / f"{cfg['model_variant']}.yaml", cfg)
    for size in ["100m", "300m", "700m", "1_3b"]:
        _write_yaml_json(config_dir / f"benchmark_{size}_suite.yaml", _suite_payload(configs, size))

    primary_models = [
        cfg["model_variant"] for cfg in configs
        if cfg["comparison_group"] in {"primary_generalized_baseline", "primary_generalized_reference_moe", "pvr_ec_o_primary", "pvr_ec_o_ablation"}
    ]
    matrix = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "required_fields": REQUIRED_MODEL_CONFIG_FIELDS,
        "size_ladder": ["100m", "300m", "700m", "1_3b", "3b_if_budget_allows"],
        "architecture_evidence_requires": ["100m", "300m", "700m"],
        "models": configs,
        "primary_generalized_baseline_suite": primary_models,
        "internal_strong_router_control_suite": [
            cfg["model_variant"] for cfg in configs if cfg["is_internal_strong_router_control"]
        ],
        "public_external_positioning_suite": [
            cfg["model_variant"] for cfg in configs if cfg.get("public_positioning_only")
        ],
        "rules": {
            "custom_fixed_moe_strong_router_not_primary_baseline": "custom_fixed_moe_strong_router_700m" not in primary_models,
            "external_public_models_positioning_only": True,
            "first_genuine_benchmark_command": "python -m benchmark.runners.run_genuine_benchmark_program --suite benchmark/configs/generated/benchmark_100m_suite.yaml --size 100m --output benchmark/reports/generated/genuine_program_100m/",
            "scaling_report_command": "python -m benchmark.runners.run_scaling_report --results benchmark/reports/generated/ --matrix benchmark/manifests/model_size_matrix_manifest.json --output benchmark/reports/generated/scaling_report/",
        },
    }
    write_json(manifest_dir / "model_size_matrix_manifest.json", matrix)

    manifest_specs = {
        "training_data_manifest.json": (["data/broad_nlp_train", "data/code_train"], "Training data paths are declared; absence blocks benchmark evidence."),
        "eval_manifest.json": (["data/eval/broad_nlp", "data/eval/coding"], "Evaluation data paths are declared; absence blocks benchmark evidence."),
        "contamination_scan_manifest.json": (["benchmark/runners/run_contamination_scan.py"], "Contamination scan tooling exists. Unknown contamination is not clean."),
        "hardware_manifest.json": ([], "Hardware is recorded by each runner at execution time."),
        "reproducibility_manifest.json": (["benchmark"], "Benchmark harness reproducibility manifest."),
        "model_registry_manifest.json": ([str(config_dir)], "Generated model registry for broad-NLP and coding benchmark regime."),
    }
    for name, (paths, notes) in manifest_specs.items():
        write_json(manifest_dir / name, manifest_payload(paths, notes))
    return matrix


def main() -> None:
    matrix = generate(".")
    print(f"Generated {len(matrix['models'])} model configs")
    print("Wrote benchmark/manifests/model_size_matrix_manifest.json")


if __name__ == "__main__":
    main()
