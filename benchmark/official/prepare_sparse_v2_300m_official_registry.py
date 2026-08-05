"""Generate an official-data bounded registry for sparse-v2 300M confirmation."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from benchmark.common import load_json_or_yaml, write_json


CONFIGS = [
    "dense_sparse_v2_300m_matched",
    "switch_top1_sparse_v2_300m_matched",
    "generic_top2_sparse_v2_300m_matched",
    "pvr_teacher_independent_sparse_v2_300m",
]


def _portable(path: str | Path) -> str:
    return str(path).replace("\\", "/")


def prepare(
    *,
    source_root: str = "benchmark/configs/generated/sparse_v2_300m_confirmation/configs",
    output: str = "benchmark/configs/generated/sparse_v2_300m_official_bounded",
    eval_root: str = "data/eval/official_300m_bounded",
) -> dict[str, Any]:
    root = Path(output)
    config_root = root / "configs"
    config_root.mkdir(parents=True, exist_ok=True)

    models: list[dict[str, str]] = []
    config_paths: list[str] = []
    for variant in CONFIGS:
        config = load_json_or_yaml(Path(source_root) / f"{variant}.yaml")
        config["eval_data_paths"] = [_portable(eval_root)]
        config["official_300m_bounded_eval"] = True
        config["official_full_benchmark"] = False
        config["official_bounded_data_manifest"] = _portable(Path(eval_root) / "official_300m_data_manifest.json")
        config["output_path"] = _portable(Path("benchmark/reports/generated/sparse_v2_300m_official_bounded_benchmark/scorecards") / variant)
        path = config_root / f"{variant}.yaml"
        write_json(path, config)
        path_text = _portable(path)
        config_paths.append(path_text)
        models.append({"config_path": path_text, "variant": variant})

    suite = {
        "schema_version": "1.0",
        "experiment": "PVR_SPARSE_V2_300M_OFFICIAL_BOUNDED_BENCHMARK",
        "scope": "Bounded deterministic official-data slices; not full official leaderboard evidence.",
        "candidate_model_variant": "pvr_teacher_independent_sparse_v2_300m",
        "promotion_baselines": [
            "dense_sparse_v2_300m_matched",
            "switch_top1_sparse_v2_300m_matched",
            "generic_top2_sparse_v2_300m_matched",
        ],
        "training_tokens_per_model": 2_150_400,
        "models": models,
        "model_configs": config_paths,
        "decision_rule": (
            "Candidate support requires benchmark evidence, clean Top1 routing, and paired/significant "
            "advantage against sparse baselines. This bounded suite cannot unlock full official claims."
        ),
    }
    write_json(root / "sparse_v2_300m_official_bounded_suite.yaml", suite)
    return suite


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", default="benchmark/configs/generated/sparse_v2_300m_confirmation/configs")
    parser.add_argument("--output", default="benchmark/configs/generated/sparse_v2_300m_official_bounded")
    parser.add_argument("--eval-root", default="data/eval/official_300m_bounded")
    args = parser.parse_args()
    payload = prepare(source_root=args.source_root, output=args.output, eval_root=args.eval_root)
    print(payload["candidate_model_variant"])


if __name__ == "__main__":
    main()
