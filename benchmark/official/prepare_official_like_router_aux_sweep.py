"""Prepare a bounded official-like router auxiliary-weight sweep."""

from __future__ import annotations

import argparse
import copy
from pathlib import Path

from benchmark.common import load_json_or_yaml, write_json


WEIGHTS = [0.0, 0.0001, 0.00025, 0.0005, 0.001, 0.002]


def prepare(output: str = "benchmark/configs/generated/official_like_router_aux_sweep") -> dict:
    root = Path(output)
    config_root = root / "configs"
    config_root.mkdir(parents=True, exist_ok=True)
    source = Path("benchmark/configs/generated/sparse_v2_curriculum_screen/configs/pvr_sparse_v2_full_from_start_aux001_100m.yaml")
    base = load_json_or_yaml(source)
    paths = []
    for weight in WEIGHTS:
        suffix = str(weight).replace(".", "p")
        variant = f"pvr_sparse_v2_official_like_aux{suffix}_100m"
        config = copy.deepcopy(base)
        config.update(
            {
                "model_variant": variant,
                "checkpoint_path": f"checkpoints/official_like_router_aux_sweep/{variant}/checkpoint.pt",
                "output_path": f"benchmark/reports/generated/official_like_router_aux_sweep/{variant}",
                "training_data_paths": ["data/eval/official_like_dev"],
                "eval_data_paths": ["data/eval/official_like_dev"],
                "routing_aux_weight": weight,
                "official_like_development_training": True,
                "official_final_files_used_for_training": False,
                "selection_rule": "Best Pareto point on official-like development LM loss, router health, and strict Top1.",
            }
        )
        path = config_root / f"{variant}.yaml"
        write_json(path, config)
        paths.append(path.as_posix())
    suite = {
        "schema_version": "1.0",
        "experiment": "PVR_OFFICIAL_LIKE_ROUTER_AUX_WEIGHT_SWEEP",
        "model_configs": paths,
        "official_test_data_used_for_selection": False,
        "official_like_development_data_used": True,
        "weights": WEIGHTS,
    }
    write_json(root / "official_like_router_aux_sweep_suite.yaml", suite)
    return suite


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="benchmark/configs/generated/official_like_router_aux_sweep")
    args = parser.parse_args()
    print(len(prepare(args.output)["model_configs"]))


if __name__ == "__main__":
    main()
