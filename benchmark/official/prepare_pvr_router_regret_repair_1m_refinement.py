"""Prepare a narrow 1M-token refinement sweep for PVR router-regret repair."""

from __future__ import annotations

import argparse
import copy
from pathlib import Path

from benchmark.common import load_json_or_yaml, write_json


SOURCE_CONFIG = "benchmark/configs/generated/pvr_router_regret_repair_screen/configs/pvr_router_regret_repair_regret0p005_300m.yaml"

VARIANTS = [
    {
        "suffix": "regret0p0025",
        "router_regret_aux_weight": 0.0025,
        "router_oracle_kl_weight": 0.0,
        "notes": "Lower expected-regret weight after regret0p01 reduced regret but missed 1M eval.",
    },
    {
        "suffix": "regret0p005",
        "router_regret_aux_weight": 0.005,
        "router_oracle_kl_weight": 0.0,
        "notes": "Best final-block regret tradeoff from the 500K screen, retested at 1M.",
    },
    {
        "suffix": "regret0p0075",
        "router_regret_aux_weight": 0.0075,
        "router_oracle_kl_weight": 0.0,
        "notes": "Intermediate expected-regret weight between 0.005 and the failed 0.01 confirmation.",
    },
]


def prepare(output: str = "benchmark/configs/generated/pvr_router_regret_repair_1m_refinement") -> dict:
    root = Path(output)
    config_root = root / "configs"
    config_root.mkdir(parents=True, exist_ok=True)
    base = load_json_or_yaml(SOURCE_CONFIG)
    paths = []
    for item in VARIANTS:
        config = copy.deepcopy(base)
        variant = f"pvr_router_regret_repair_{item['suffix']}_300m_1m_refine"
        config.update(
            {
                "model_variant": variant,
                "checkpoint_path": f"checkpoints/pvr_router_regret_repair_1m_refinement/{variant}/checkpoint.pt",
                "output_path": f"benchmark/reports/generated/pvr_router_regret_repair_1m_refinement_run/{variant}",
                "official_like_development_eval": True,
                "official_final_files_used_for_training": False,
                "official_final_files_used_for_selection": False,
                "router_regret_repair_1m_refinement": True,
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
        "experiment": "PVR_ROUTER_REGRET_REPAIR_1M_REFINEMENT",
        "model_configs": paths,
        "official_test_data_used_for_selection": False,
        "training_data": "data/broad_nlp_train",
        "eval_data": "data/eval/official_like_dev",
        "target_training_tokens": 1_000_448,
        "rung_tokens": [249_856, 499_712, 749_568, 999_424],
        "baseline_reference_report": "benchmark/reports/generated/pvr_router_regret_repair_1m_confirmation/pvr_router_repair_screen.json",
        "selection_rule": "Compare lower regret weights against the completed 1M no-regret baseline. Final official bounded files remain untouched.",
        "variant_definitions": VARIANTS,
    }
    write_json(root / "pvr_router_regret_repair_1m_refinement_suite.yaml", suite)
    return suite


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="benchmark/configs/generated/pvr_router_regret_repair_1m_refinement")
    args = parser.parse_args()
    print(len(prepare(args.output)["model_configs"]))


if __name__ == "__main__":
    main()
