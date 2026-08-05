"""Generate a teacher-free 100M sparse-v2 curriculum screen."""

from __future__ import annotations

import argparse
import copy
from pathlib import Path

from benchmark.common import load_json_or_yaml, write_json


VARIANTS = [
    ("pvr_sparse_v2_full_from_start_aux001_100m", "full_training", 0.001, True),
    ("pvr_sparse_v2_shared_then_top1_aux0_100m", "shared_then_strict_top1", 0.0, True),
    ("pvr_sparse_v2_shared_then_top1_aux0001_100m", "shared_then_strict_top1", 0.001, True),
    ("pvr_sparse_v2_shared_then_top1_aux001_100m", "shared_then_strict_top1", 0.01, True),
    ("pvr_sparse_v2_shared_then_top1_no_prototypes_100m", "shared_then_strict_top1", 0.001, False),
]


def prepare(output: str = "benchmark/configs/generated/sparse_v2_curriculum_screen"):
    root = Path(output)
    config_root = root / "configs"
    config_root.mkdir(parents=True, exist_ok=True)
    base = load_json_or_yaml("benchmark/configs/generated/pvr_ec_o_full_100m.yaml")
    paths = []
    for variant, curriculum, aux_weight, prototypes in VARIANTS:
        config = copy.deepcopy(base)
        config.update({
            "model_variant": variant,
            "checkpoint_path": f"checkpoints/sparse_v2_curriculum_screen/{variant}/checkpoint.pt",
            "output_path": f"benchmark/reports/generated/sparse_v2_curriculum_screen/{variant}",
            "attention_only_trunk": True,
            "straight_through_router": True,
            "prototype_routing": prototypes,
            "num_experts_if_applicable": 24,
            "materialization_ffn_size": 192,
            "shared_materialization_ffn_size": 192,
            "ablation": "no_descriptor_operator",
            "training_curriculum": curriculum,
            "routing_aux_weight": aux_weight,
            "teacher_checkpoint_loaded": False,
            "selection_data_excludes_official_test": True,
        })
        path = config_root / f"{variant}.yaml"
        write_json(path, config)
        paths.append(path.as_posix())
    suite = {
        "schema_version": "1.0",
        "experiment": "PVR_SPARSE_V2_TEACHER_FREE_CURRICULUM_SCREEN",
        "model_configs": paths,
        "selection_rule": "Lowest Frankenstein heldout LM loss with nonzero router gradients and clean strict Top1.",
        "official_test_data_used_for_selection": False,
    }
    write_json(root / "sparse_v2_curriculum_screen_suite.yaml", suite)
    return suite


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="benchmark/configs/generated/sparse_v2_curriculum_screen")
    args = parser.parse_args()
    payload = prepare(args.output)
    print(len(payload["model_configs"]))


if __name__ == "__main__":
    main()
