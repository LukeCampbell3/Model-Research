"""Generate the pre-registered teacher-free sparse-v2 300M confirmation suite."""

from __future__ import annotations

import argparse
import copy
from pathlib import Path

from benchmark.common import load_json_or_yaml, write_json


SPECS = [
    {
        "source": "dense_transformer_300m",
        "variant": "dense_sparse_v2_300m_matched",
        "materialization_ffn_size": 2944,
        "attention_only_trunk": False,
    },
    {
        "source": "vanilla_switch_top1_reference_300m",
        "variant": "switch_top1_sparse_v2_300m_matched",
        "materialization_ffn_size": 364,
        "attention_only_trunk": True,
    },
    {
        "source": "generic_top2_moe_reference_300m",
        "variant": "generic_top2_sparse_v2_300m_matched",
        "materialization_ffn_size": 364,
        "attention_only_trunk": True,
    },
]

CANDIDATE = "pvr_teacher_independent_sparse_v2_300m"


def prepare(output="benchmark/configs/generated/sparse_v2_300m_confirmation"):
    root = Path(output)
    config_root = root / "configs"
    config_root.mkdir(parents=True, exist_ok=True)
    paths = []
    for spec in SPECS:
        config = copy.deepcopy(load_json_or_yaml(f"benchmark/configs/generated/{spec['source']}.yaml"))
        config.update({
            "model_variant": spec["variant"],
            "checkpoint_path": f"checkpoints/sparse_v2_300m_confirmation/{spec['variant']}/checkpoint.pt",
            "output_path": f"benchmark/reports/generated/sparse_v2_300m_confirmation/{spec['variant']}",
            "materialization_ffn_size": spec["materialization_ffn_size"],
            "attention_only_trunk": spec["attention_only_trunk"],
            "training_curriculum": "full_training",
            "teacher_checkpoint_loaded": False,
            "benchmark_training_tokens_accounted": 2_150_400,
            "pre_registered_300m_confirmation": True,
        })
        path = config_root / f"{spec['variant']}.yaml"
        write_json(path, config)
        paths.append(path.as_posix())
    candidate = copy.deepcopy(load_json_or_yaml("benchmark/configs/generated/pvr_ec_o_full_300m.yaml"))
    candidate.update({
        "model_variant": CANDIDATE,
        "checkpoint_path": f"checkpoints/sparse_v2_300m_confirmation/{CANDIDATE}/checkpoint.pt",
        "output_path": f"benchmark/reports/generated/sparse_v2_300m_confirmation/{CANDIDATE}",
        "attention_only_trunk": True,
        "straight_through_router": True,
        "prototype_routing": True,
        "num_experts_if_applicable": 16,
        "shared_materialization_ffn_size": 512,
        "materialization_ffn_size": 148,
        "ablation": "no_descriptor_operator",
        "training_curriculum": "full_training",
        "routing_aux_weight": 0.001,
        "teacher_checkpoint_loaded": False,
        "benchmark_training_tokens_accounted": 2_150_400,
        "pre_registered_300m_confirmation": True,
        "selection_provenance": "Scaled from non-test sparse-v2 160M capacity winner under Top2 active budget.",
    })
    candidate_path = config_root / f"{CANDIDATE}.yaml"
    write_json(candidate_path, candidate)
    paths.append(candidate_path.as_posix())
    suite = {
        "schema_version": "1.0",
        "experiment": "PVR_TEACHER_INDEPENDENT_SPARSE_V2_300M_CONFIRMATION",
        "model_configs": paths,
        "candidate_model_variant": CANDIDATE,
        "training_tokens_per_model": 2_150_400,
        "official_test_data_used_for_selection": False,
        "promotion_rule": (
            "Candidate must significantly beat Switch and Top2 on paired heldout loss, remain below Top2 active params, "
            "keep strict Top1 clean, and show no teacher checkpoint load."
        ),
    }
    write_json(root / "sparse_v2_300m_confirmation_suite.yaml", suite)
    return suite


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="benchmark/configs/generated/sparse_v2_300m_confirmation")
    args = parser.parse_args()
    print(len(prepare(args.output)["model_configs"]))


if __name__ == "__main__":
    main()
