from benchmark.scripts.generate_model_size_matrix import generate


def test_public_models_are_external_positioning_only(tmp_path):
    matrix = generate(tmp_path)
    primary = set(matrix["primary_generalized_baseline_suite"])
    public = set(matrix["public_external_positioning_suite"])
    expected = {
        "public_dense_small",
        "public_dense_mid",
        "public_instruction_small",
        "public_instruction_mid",
        "public_code_small",
        "public_code_mid",
        "public_moe_if_available",
    }
    assert expected <= public
    assert not (public & primary)
    for model in matrix["models"]:
        if model["model_variant"] in expected:
            assert model["comparison_group"] == "external_positioning_only"
            assert model["public_positioning_only"] is True
            assert model["not_controlled_architecture_evidence"] is True
            assert model["is_primary_baseline"] is False
