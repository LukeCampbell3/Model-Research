from benchmark.scripts.generate_model_size_matrix import generate


def test_custom_fixed_moe_is_only_internal_control(tmp_path):
    matrix = generate(tmp_path)
    primary = set(matrix["primary_generalized_baseline_suite"])
    internal = set(matrix["internal_strong_router_control_suite"])
    assert "custom_fixed_moe_strong_router_700m" not in primary
    assert "custom_fixed_moe_strong_router_700m" in internal
    for model in matrix["models"]:
        if model["model_family"] == "custom_fixed_moe_strong_router":
            assert model["comparison_group"] == "internal_strong_router_control"
            assert model["is_internal_strong_router_control"] is True
            assert model["is_primary_baseline"] is False

