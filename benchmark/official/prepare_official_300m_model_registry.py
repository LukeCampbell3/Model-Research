"""Generate compute-matched control configs and the official 300M registry."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from benchmark.common import load_json_or_yaml, write_json


TOKENS = 2_150_400
BASELINES = (
    "dense_transformer_300m",
    "vanilla_switch_top1_reference_300m",
    "generic_top2_moe_reference_300m",
)


def _portable(value: str | Path) -> str:
    return str(value).replace("\\", "/")


def _portable_config(config: dict[str, Any]) -> dict[str, Any]:
    for key in ("checkpoint_path", "output_path"):
        if key in config:
            config[key] = _portable(config[key])
    for key in ("training_data_paths", "eval_data_paths"):
        if key in config:
            config[key] = [_portable(value) for value in config[key]]
    return config


def _control_config(name: str, config_root: Path, checkpoint_root: Path, report_root: Path) -> dict[str, Any]:
    source = load_json_or_yaml(Path("benchmark/configs/generated") / f"{name}.yaml")
    variant = f"{name}_official_compute_matched"
    source.update({
        "model_variant": variant,
        "checkpoint_path": _portable(checkpoint_root / variant / "checkpoint.pt"),
        "output_path": _portable(report_root / variant),
        "benchmark_training_tokens_accounted": TOKENS,
        "training_recipe": "4000x256 tokens, optimizer reset, 1100x1024 tokens",
        "official_300m_control": True,
    })
    source = _portable_config(source)
    path = config_root / f"{variant}.yaml"
    write_json(path, source)
    return {"path": _portable(path), "variant": variant}


def _existing_config(source_path: str, config_root: Path, *, tokens: int = TOKENS) -> dict[str, Any]:
    source = load_json_or_yaml(source_path)
    source["benchmark_training_tokens_accounted"] = tokens
    source["official_300m_evaluation"] = True
    source = _portable_config(source)
    path = config_root / f"{source['model_variant']}.yaml"
    write_json(path, source)
    return {"path": _portable(path), "variant": source["model_variant"]}


def prepare(output: str) -> dict[str, Any]:
    root = Path(output)
    config_root = root / "configs"
    checkpoint_root = Path("checkpoints/official_300m_compute_matched")
    training_report_root = Path("benchmark/reports/generated/official_300m_compute_matched_training")
    config_root.mkdir(parents=True, exist_ok=True)
    controls = [_control_config(name, config_root, checkpoint_root, training_report_root) for name in BASELINES]
    candidate = _existing_config(
        "checkpoints/self_instilled_ean_trunk_stage_matched_300m/pvr_self_instilled_ean_trunk_stage_matched_300m/run_config.yaml",
        config_root,
    )
    teacher = _existing_config(
        "checkpoints/self_instilled_ean_geometry_head_300m_matched_volume_screen/pvr_teacher_ean_300m_matched/run_config.yaml",
        config_root,
    )
    scratch = _existing_config(
        "checkpoints/self_instilled_trunk_total_compute_matched_300m/pvr_full_scratch_300m_total_compute_matched/run_config.yaml",
        config_root,
    )
    training_suite = {"schema_version": "1.0", "model_configs": [row["path"] for row in controls]}
    benchmark_registry = {
        "schema_version": "1.0",
        "candidate_model_variant": candidate["variant"],
        "promotion_baselines": [row["variant"] for row in controls],
        "model_configs": [row["path"] for row in controls] + [scratch["path"], teacher["path"], candidate["path"]],
        "training_tokens_per_model": TOKENS,
        "fairness_note": "All models account for 2,150,400 recipe-total tokens. Generalized controls match both update phases and optimizer reset.",
    }
    write_json(root / "official_300m_control_training_suite.yaml", training_suite)
    write_json(root / "official_300m_benchmark_registry.yaml", benchmark_registry)
    return benchmark_registry


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="benchmark/configs/generated/official_300m_bounded")
    args = parser.parse_args()
    payload = prepare(args.output)
    print(payload["candidate_model_variant"])


if __name__ == "__main__":
    main()
