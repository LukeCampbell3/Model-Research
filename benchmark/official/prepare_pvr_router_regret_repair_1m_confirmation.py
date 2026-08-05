"""Prepare 1M-token confirmation for the supported router-regret repair."""

from __future__ import annotations

import argparse
import copy
from pathlib import Path

from benchmark.common import load_json_or_yaml, write_json


SOURCE_CONFIGS = [
    "benchmark/configs/generated/pvr_router_regret_repair_screen/configs/pvr_router_regret_repair_baseline_no_regret_300m.yaml",
    "benchmark/configs/generated/pvr_router_regret_repair_screen/configs/pvr_router_regret_repair_regret0p01_300m.yaml",
]


def prepare(output: str = "benchmark/configs/generated/pvr_router_regret_repair_1m_confirmation") -> dict:
    root = Path(output)
    config_root = root / "configs"
    config_root.mkdir(parents=True, exist_ok=True)
    paths = []
    for source in SOURCE_CONFIGS:
        base = load_json_or_yaml(source)
        variant = f"{base['model_variant']}_1m_confirm"
        config = copy.deepcopy(base)
        config.update(
            {
                "model_variant": variant,
                "checkpoint_path": f"checkpoints/pvr_router_regret_repair_1m_confirmation/{variant}/checkpoint.pt",
                "output_path": f"benchmark/reports/generated/pvr_router_regret_repair_1m_confirmation_run/{variant}",
                "router_regret_repair_1m_confirmation": True,
                "official_final_files_used_for_training": False,
                "official_final_files_used_for_selection": False,
            }
        )
        path = config_root / f"{variant}.yaml"
        write_json(path, config)
        paths.append(path.as_posix())
    suite = {
        "schema_version": "1.0",
        "experiment": "PVR_ROUTER_REGRET_REPAIR_1M_CONFIRMATION",
        "model_configs": paths,
        "official_test_data_used_for_selection": False,
        "training_data": "data/broad_nlp_train",
        "eval_data": "data/eval/official_like_dev",
        "target_training_tokens": 1_000_448,
        "rung_tokens": [249_856, 499_712, 749_568, 999_424],
        "selection_rule": "Confirm supported regret0p01 repair against no-repair baseline on official_like_dev. Final official bounded files remain untouched.",
    }
    write_json(root / "pvr_router_regret_repair_1m_confirmation_suite.yaml", suite)
    return suite


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="benchmark/configs/generated/pvr_router_regret_repair_1m_confirmation")
    args = parser.parse_args()
    print(len(prepare(args.output)["model_configs"]))


if __name__ == "__main__":
    main()
