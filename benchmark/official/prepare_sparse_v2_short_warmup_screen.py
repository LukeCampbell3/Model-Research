"""Generate a matched short-warmup sparse-v2 teacher-free screen."""

from __future__ import annotations

import argparse
import copy
from pathlib import Path

from benchmark.common import load_json_or_yaml, write_json


SETTINGS = [
    (50, 0.001),
    (100, 0.001),
    (200, 0.001),
    (350, 0.001),
    (100, 0.01),
]


def prepare(output="benchmark/configs/generated/sparse_v2_short_warmup_screen"):
    root = Path(output)
    config_root = root / "configs"
    config_root.mkdir(parents=True, exist_ok=True)
    source_path = Path(
        "benchmark/configs/generated/sparse_v2_curriculum_screen/configs/"
        "pvr_sparse_v2_full_from_start_aux001_100m.yaml"
    )
    base = load_json_or_yaml(source_path)
    paths = [source_path.as_posix()]
    for warmup_steps, aux_weight in SETTINGS:
        suffix = str(aux_weight).replace(".", "")
        variant = f"pvr_sparse_v2_shared_warmup{warmup_steps}_aux{suffix}_100m"
        config = copy.deepcopy(base)
        config.update({
            "model_variant": variant,
            "checkpoint_path": f"checkpoints/sparse_v2_short_warmup_screen/{variant}/checkpoint.pt",
            "output_path": f"benchmark/reports/generated/sparse_v2_short_warmup_screen/{variant}",
            "training_curriculum": "shared_then_strict_top1",
            "shared_warmup_steps": warmup_steps,
            "routing_aux_weight": aux_weight,
        })
        path = config_root / f"{variant}.yaml"
        write_json(path, config)
        paths.append(path.as_posix())
    suite = {
        "schema_version": "1.0",
        "experiment": "PVR_SPARSE_V2_SHORT_WARMUP_SCREEN",
        "model_configs": paths,
        "selection_rule": "Lowest non-test Frankenstein heldout LM loss with nonzero router gradients and clean Top1.",
        "official_test_data_used_for_selection": False,
    }
    write_json(root / "sparse_v2_short_warmup_screen_suite.yaml", suite)
    return suite


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="benchmark/configs/generated/sparse_v2_short_warmup_screen")
    args = parser.parse_args()
    print(len(prepare(args.output)["model_configs"]))


if __name__ == "__main__":
    main()
