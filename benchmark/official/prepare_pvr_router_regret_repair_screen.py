"""Prepare bounded PVR router-regret repair screen configs."""

from __future__ import annotations

import argparse
import copy
from pathlib import Path

from benchmark.common import load_json_or_yaml, write_json


SOURCE_CONFIG = "benchmark/configs/generated/pvr_shared_substrate_repair_screen/configs/pvr_shared_substrate_full_transformer_random_ean_300m.yaml"


VARIANTS = [
    {
        "suffix": "baseline_no_regret",
        "router_regret_aux_weight": 0.0,
        "router_oracle_kl_weight": 0.0,
        "notes": "Full random Transformer substrate winner with no regret-weighted router repair.",
    },
    {
        "suffix": "regret0p001",
        "router_regret_aux_weight": 0.001,
        "router_oracle_kl_weight": 0.0,
        "notes": "Light expected-regret router objective.",
    },
    {
        "suffix": "regret0p005",
        "router_regret_aux_weight": 0.005,
        "router_oracle_kl_weight": 0.0,
        "notes": "Medium expected-regret router objective.",
    },
    {
        "suffix": "regret0p01",
        "router_regret_aux_weight": 0.01,
        "router_oracle_kl_weight": 0.0,
        "notes": "Strong expected-regret router objective.",
    },
    {
        "suffix": "kl0p005",
        "router_regret_aux_weight": 0.0,
        "router_oracle_kl_weight": 0.005,
        "notes": "Soft oracle KL target without expected-regret term.",
    },
    {
        "suffix": "regret0p005_kl0p001",
        "router_regret_aux_weight": 0.005,
        "router_oracle_kl_weight": 0.001,
        "notes": "Medium expected-regret plus light soft-oracle KL.",
    },
]


def prepare(output: str = "benchmark/configs/generated/pvr_router_regret_repair_screen") -> dict:
    root = Path(output)
    config_root = root / "configs"
    config_root.mkdir(parents=True, exist_ok=True)
    base = load_json_or_yaml(SOURCE_CONFIG)
    paths = []
    for item in VARIANTS:
        config = copy.deepcopy(base)
        variant = f"pvr_router_regret_repair_{item['suffix']}_300m"
        config.update(
            {
                "model_variant": variant,
                "checkpoint_path": f"checkpoints/pvr_router_regret_repair_screen/{variant}/checkpoint.pt",
                "output_path": f"benchmark/reports/generated/pvr_router_regret_repair_screen_run/{variant}",
                "training_data_paths": ["data/broad_nlp_train"],
                "eval_data_paths": ["data/eval/official_like_dev"],
                "official_like_development_eval": True,
                "official_final_files_used_for_training": False,
                "official_final_files_used_for_selection": False,
                "router_regret_repair_screen": True,
                "router_regret_aux_weight": item["router_regret_aux_weight"],
                "router_oracle_kl_weight": item["router_oracle_kl_weight"],
                "router_regret_temperature": 1.0,
                "screen_notes": item["notes"],
            }
        )
        path = config_root / f"{variant}.yaml"
        write_json(path, config)
        paths.append(path.as_posix())
    suite = {
        "schema_version": "1.0",
        "experiment": "PVR_ROUTER_REGRET_REPAIR_SCREEN",
        "model_configs": paths,
        "official_test_data_used_for_selection": False,
        "training_data": "data/broad_nlp_train",
        "eval_data": "data/eval/official_like_dev",
        "target_training_tokens": 500_736,
        "rung_tokens": [249_856, 499_712],
        "selection_rule": "Official-like development loss plus final-block router regret and strict Top1. Final official bounded files remain untouched.",
        "variant_definitions": VARIANTS,
    }
    write_json(root / "pvr_router_regret_repair_screen_suite.yaml", suite)
    return suite


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="benchmark/configs/generated/pvr_router_regret_repair_screen")
    args = parser.parse_args()
    print(len(prepare(args.output)["model_configs"]))


if __name__ == "__main__":
    main()
