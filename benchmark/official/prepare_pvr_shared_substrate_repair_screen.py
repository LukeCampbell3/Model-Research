"""Prepare teacher-independent PVR shared-substrate repair screen configs."""

from __future__ import annotations

import argparse
import copy
from pathlib import Path

from benchmark.common import load_json_or_yaml, write_json


SOURCE_CONFIG = "benchmark/configs/generated/sparse_v2_300m_confirmation/configs/pvr_teacher_independent_sparse_v2_300m.yaml"


VARIANTS = [
    {
        "suffix": "attention_norms_current",
        "substrate_mode": "attention_norms",
        "attention_only_trunk": True,
        "notes": "Current attention-only trunk with LayerNorm; authoritative sparse-v2 substrate baseline.",
    },
    {
        "suffix": "embeddings_only",
        "substrate_mode": "embeddings_only",
        "attention_only_trunk": True,
        "notes": "Token/position embedding coordinate system only; no contextual shared trunk.",
    },
    {
        "suffix": "embeddings_attention",
        "substrate_mode": "embeddings_attention",
        "attention_only_trunk": True,
        "notes": "Embeddings plus attention without trunk LayerNorm.",
    },
    {
        "suffix": "embeddings_norms",
        "substrate_mode": "embeddings_norms",
        "attention_only_trunk": True,
        "notes": "Embeddings plus normalization without contextual attention.",
    },
    {
        "suffix": "full_transformer_random_ean",
        "substrate_mode": "full_transformer_random_ean",
        "attention_only_trunk": False,
        "notes": "Randomly initialized dense-style attention+norm+FFN trunk; no teacher transfer.",
    },
    {
        "suffix": "wider_attention_norms",
        "substrate_mode": "attention_norms",
        "attention_only_trunk": True,
        "shared_materialization_ffn_size": 768,
        "notes": "Attention+norms trunk with wider shared residual path; active compute recorded explicitly.",
    },
    {
        "suffix": "deeper_attention_norms",
        "substrate_mode": "attention_norms",
        "attention_only_trunk": True,
        "num_layers": 28,
        "notes": "Deeper attention+norms trunk; active compute recorded explicitly.",
    },
    {
        "suffix": "staged_warmup_attention_norms",
        "substrate_mode": "attention_norms",
        "attention_only_trunk": True,
        "training_curriculum": "shared_warmup_then_top1",
        "shared_warmup_steps": 244,
        "notes": "Current substrate with residual experts disabled for the first ~250K tokens.",
    },
]


def prepare(output: str = "benchmark/configs/generated/pvr_shared_substrate_repair_screen") -> dict:
    root = Path(output)
    config_root = root / "configs"
    config_root.mkdir(parents=True, exist_ok=True)
    base = load_json_or_yaml(SOURCE_CONFIG)
    paths = []
    for item in VARIANTS:
        config = copy.deepcopy(base)
        variant = f"pvr_shared_substrate_{item['suffix']}_300m"
        config.update(
            {
                "model_variant": variant,
                "checkpoint_path": f"checkpoints/pvr_shared_substrate_repair_screen/{variant}/checkpoint.pt",
                "output_path": f"benchmark/reports/generated/pvr_shared_substrate_repair_screen/{variant}",
                "training_data_paths": ["data/broad_nlp_train"],
                "eval_data_paths": ["data/eval/official_like_dev"],
                "official_like_development_eval": True,
                "official_final_files_used_for_training": False,
                "official_final_files_used_for_selection": False,
                "substrate_repair_screen": True,
                "substrate_mode": item["substrate_mode"],
                "attention_only_trunk": item["attention_only_trunk"],
                "screen_notes": item["notes"],
            }
        )
        for key in ["shared_materialization_ffn_size", "num_layers", "training_curriculum", "shared_warmup_steps"]:
            if key in item:
                config[key] = item[key]
        path = config_root / f"{variant}.yaml"
        write_json(path, config)
        paths.append(path.as_posix())
    suite = {
        "schema_version": "1.0",
        "experiment": "PVR_SHARED_SUBSTRATE_REPAIR_SCREEN",
        "model_configs": paths,
        "official_test_data_used_for_selection": False,
        "training_data": "data/broad_nlp_train",
        "eval_data": "data/eval/official_like_dev",
        "target_training_tokens": 1_000_448,
        "rung_tokens": [249_856, 499_712, 749_568, 999_424],
        "selection_rule": "Official-like development loss plus routing health; final official bounded files remain untouched.",
        "variant_definitions": VARIANTS,
    }
    write_json(root / "pvr_shared_substrate_repair_screen_suite.yaml", suite)
    return suite


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="benchmark/configs/generated/pvr_shared_substrate_repair_screen")
    args = parser.parse_args()
    print(len(prepare(args.output)["model_configs"]))


if __name__ == "__main__":
    main()
