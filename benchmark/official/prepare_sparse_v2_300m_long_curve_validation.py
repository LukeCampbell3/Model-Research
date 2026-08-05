"""Prepare 300M sparse-v2 long-curve validation configs.

Training uses broad_nlp_train. Evaluation uses official_like_dev. Final official
bounded files are not used for training, tuning, or checkpoint selection.
"""

from __future__ import annotations

import argparse
import copy
from pathlib import Path

from benchmark.common import load_json_or_yaml, write_json


SOURCE_CONFIGS = [
    "benchmark/configs/generated/sparse_v2_300m_confirmation/configs/dense_sparse_v2_300m_matched.yaml",
    "benchmark/configs/generated/sparse_v2_300m_confirmation/configs/switch_top1_sparse_v2_300m_matched.yaml",
    "benchmark/configs/generated/sparse_v2_300m_confirmation/configs/generic_top2_sparse_v2_300m_matched.yaml",
    "benchmark/configs/generated/sparse_v2_300m_confirmation/configs/pvr_teacher_independent_sparse_v2_300m.yaml",
]


def prepare(output: str = "benchmark/configs/generated/sparse_v2_300m_long_curve_validation") -> dict:
    root = Path(output)
    config_root = root / "configs"
    config_root.mkdir(parents=True, exist_ok=True)
    paths = []
    for source in SOURCE_CONFIGS:
        base = load_json_or_yaml(source)
        variant = f"{base['model_variant']}_long_curve"
        config = copy.deepcopy(base)
        config.update(
            {
                "model_variant": variant,
                "checkpoint_path": f"checkpoints/sparse_v2_300m_long_curve_validation/{variant}/checkpoint.pt",
                "output_path": f"benchmark/reports/generated/sparse_v2_300m_long_curve_validation/{variant}",
                "training_data_paths": ["data/broad_nlp_train"],
                "eval_data_paths": ["data/eval/official_like_dev"],
                "official_like_development_eval": True,
                "official_final_files_used_for_training": False,
                "official_final_files_used_for_selection": False,
                "long_curve_validation": True,
            }
        )
        path = config_root / f"{variant}.yaml"
        write_json(path, config)
        paths.append(path.as_posix())

    # Include the best reduced aux setting as a candidate repair configuration.
    pvr = load_json_or_yaml(SOURCE_CONFIGS[-1])
    repaired = copy.deepcopy(pvr)
    repaired_variant = "pvr_teacher_independent_sparse_v2_300m_aux0005_long_curve"
    repaired.update(
        {
            "model_variant": repaired_variant,
            "routing_aux_weight": 0.0005,
            "checkpoint_path": f"checkpoints/sparse_v2_300m_long_curve_validation/{repaired_variant}/checkpoint.pt",
            "output_path": f"benchmark/reports/generated/sparse_v2_300m_long_curve_validation/{repaired_variant}",
            "training_data_paths": ["data/broad_nlp_train"],
            "eval_data_paths": ["data/eval/official_like_dev"],
            "official_like_development_eval": True,
            "official_final_files_used_for_training": False,
            "official_final_files_used_for_selection": False,
            "long_curve_validation": True,
            "repair_source": "official_like_router_aux_sweep_winner_0.0005",
        }
    )
    repaired_path = config_root / f"{repaired_variant}.yaml"
    write_json(repaired_path, repaired)
    paths.append(repaired_path.as_posix())

    suite = {
        "schema_version": "1.0",
        "experiment": "PVR_SPARSE_V2_300M_LONG_CURVE_VALIDATION",
        "model_configs": paths,
        "official_test_data_used_for_selection": False,
        "training_data": "data/broad_nlp_train",
        "eval_data": "data/eval/official_like_dev",
        "selection_rule": "Official-like dev learning curves only; final official files remain untouched.",
    }
    write_json(root / "sparse_v2_300m_long_curve_validation_suite.yaml", suite)
    return suite


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="benchmark/configs/generated/sparse_v2_300m_long_curve_validation")
    args = parser.parse_args()
    print(len(prepare(args.output)["model_configs"]))


if __name__ == "__main__":
    main()
