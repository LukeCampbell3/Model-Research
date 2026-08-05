import json
from pathlib import Path

from benchmark.common import REQUIRED_MODEL_CONFIG_FIELDS
from benchmark.scripts.generate_model_size_matrix import generate


REQUIRED_FAMILIES = [
    "dense_transformer",
    "vanilla_switch_top1_reference",
    "generic_top2_moe_reference",
    "pvr_ec_o",
]


def test_model_size_matrix_and_required_configs_exist(tmp_path):
    matrix = generate(tmp_path)
    generated = tmp_path / "benchmark" / "configs" / "generated"
    required_100m = [
        "dense_transformer_100m",
        "vanilla_switch_top1_reference_100m",
        "generic_top2_moe_reference_100m",
        "pvr_ec_o_full_100m",
        "pvr_ec_o_no_prototypes_100m",
        "pvr_ec_o_no_contrastive_geometry_100m",
        "pvr_ec_o_no_descriptor_operator_100m",
        "pvr_ec_o_shared_only_100m",
    ]
    for name in required_100m:
        assert (generated / f"{name}.yaml").exists()
    models = matrix["models"]
    for family in REQUIRED_FAMILIES:
        sizes = {m["model_size_label"] for m in models if m["model_family"] == family}
        assert {"100m", "300m", "700m"} <= sizes
    for config_path in generated.glob("*.yaml"):
        if config_path.name.startswith("benchmark_"):
            continue
        cfg = json.loads(config_path.read_text())
        assert set(REQUIRED_MODEL_CONFIG_FIELDS) <= set(cfg)

