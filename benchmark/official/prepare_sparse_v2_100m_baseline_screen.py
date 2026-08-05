"""Generate corrected 100M dense/MoE controls for sparse-v2 screening."""

from __future__ import annotations

import argparse
import copy
from pathlib import Path

from benchmark.common import load_json_or_yaml, write_json


SPECS = [
    ("dense_transformer_100m", "dense_v2_100m_matched", 4864, False),
    ("vanilla_switch_top1_reference_100m", "switch_top1_sparse_v2_100m_matched", 608, True),
    ("generic_top2_moe_reference_100m", "generic_top2_sparse_v2_100m_matched", 608, True),
]


def prepare(output="benchmark/configs/generated/sparse_v2_100m_baseline_screen"):
    root = Path(output)
    config_root = root / "configs"
    config_root.mkdir(parents=True, exist_ok=True)
    paths = []
    for source_name, variant, ffn_size, attention_only in SPECS:
        config = copy.deepcopy(load_json_or_yaml(f"benchmark/configs/generated/{source_name}.yaml"))
        config.update({
            "model_variant": variant,
            "checkpoint_path": f"checkpoints/sparse_v2_100m_baseline_screen/{variant}/checkpoint.pt",
            "output_path": f"benchmark/reports/generated/sparse_v2_100m_baseline_screen/{variant}",
            "materialization_ffn_size": ffn_size,
            "attention_only_trunk": attention_only,
            "training_curriculum": "full_training",
            "teacher_checkpoint_loaded": False,
            "selection_data_excludes_official_test": True,
        })
        path = config_root / f"{variant}.yaml"
        write_json(path, config)
        paths.append(path.as_posix())
    candidate = Path(
        "benchmark/configs/generated/sparse_v2_curriculum_screen/configs/"
        "pvr_sparse_v2_full_from_start_aux001_100m.yaml"
    )
    paths.append(candidate.as_posix())
    suite = {
        "schema_version": "1.0",
        "experiment": "PVR_SPARSE_V2_100M_BASELINE_SCREEN",
        "model_configs": paths,
        "official_test_data_used_for_selection": False,
        "training_tokens_per_model": 486_400,
    }
    write_json(root / "sparse_v2_100m_baseline_screen_suite.yaml", suite)
    return suite


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="benchmark/configs/generated/sparse_v2_100m_baseline_screen")
    args = parser.parse_args()
    print(len(prepare(args.output)["model_configs"]))


if __name__ == "__main__":
    main()
