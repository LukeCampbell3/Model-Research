"""Generate active-budget-constrained sparse-v2 capacity reallocations."""

from __future__ import annotations

import argparse
import copy
from pathlib import Path

from benchmark.common import load_json_or_yaml, write_json


SETTINGS = [
    (16, 640, 256),
    (16, 768, 256),
    (20, 384, 224),
    (24, 512, 176),
]


def prepare(output="benchmark/configs/generated/sparse_v2_capacity_screen"):
    root = Path(output)
    config_root = root / "configs"
    config_root.mkdir(parents=True, exist_ok=True)
    source = Path(
        "benchmark/configs/generated/sparse_v2_curriculum_screen/configs/"
        "pvr_sparse_v2_full_from_start_aux001_100m.yaml"
    )
    base = load_json_or_yaml(source)
    paths = [source.as_posix()]
    for experts, shared_ffn, expert_ffn in SETTINGS:
        variant = f"pvr_sparse_v2_e{experts}_shared{shared_ffn}_expert{expert_ffn}_100m"
        config = copy.deepcopy(base)
        config.update({
            "model_variant": variant,
            "checkpoint_path": f"checkpoints/sparse_v2_capacity_screen/{variant}/checkpoint.pt",
            "output_path": f"benchmark/reports/generated/sparse_v2_capacity_screen/{variant}",
            "num_experts_if_applicable": experts,
            "shared_materialization_ffn_size": shared_ffn,
            "materialization_ffn_size": expert_ffn,
            "capacity_screen": True,
            "active_budget_ceiling": 92_649_984,
        })
        path = config_root / f"{variant}.yaml"
        write_json(path, config)
        paths.append(path.as_posix())
    suite = {
        "schema_version": "1.0",
        "experiment": "PVR_SPARSE_V2_CAPACITY_REALLOCATION_SCREEN",
        "model_configs": paths,
        "official_test_data_used_for_selection": False,
        "active_budget_ceiling": 92_649_984,
        "selection_rule": "Lowest non-test LM loss among strict Top1 variants below generic Top2 active parameters.",
    }
    write_json(root / "sparse_v2_capacity_screen_suite.yaml", suite)
    return suite


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="benchmark/configs/generated/sparse_v2_capacity_screen")
    args = parser.parse_args()
    print(len(prepare(args.output)["model_configs"]))


if __name__ == "__main__":
    main()
