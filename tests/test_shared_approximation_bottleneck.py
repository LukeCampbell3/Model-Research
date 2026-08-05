import torch

from benchmark.common import load_json_or_yaml
from benchmark.model_factory import build_model
from benchmark.runners.run_shared_approximation_bottleneck import (
    _gated_teacher_loss,
    _variant_config,
    copy_compatible_dense_weights_to_pvr,
    dense_gap_window_classification,
    summarize_matrix,
)


def test_shared_capacity_plus_uses_explicit_shared_ffn_size(tmp_path):
    cfg = load_json_or_yaml("benchmark/configs/generated/pvr_ec_o_full_100m.yaml")
    variant = _variant_config(
        cfg,
        "pvr_test_shared_capacity",
        str(tmp_path / "ckpt"),
        str(tmp_path / "out"),
        shared_capacity_multiplier=4.0,
    )
    assert variant["shared_materialization_ffn_size"] > variant["materialization_ffn_size"]
    model = build_model(variant, device="cpu").model
    assert model.blocks[0].shared.w1.out_features == variant["shared_materialization_ffn_size"]
    assert model.blocks[0].experts[0].w1.out_features == variant["materialization_ffn_size"]


def test_copy_compatible_dense_weights_to_pvr_copies_embeddings():
    dense_cfg = {
        "model_family": "dense_transformer",
        "model_variant": "dense_tiny",
        "hidden_size": 16,
        "num_layers": 1,
        "num_heads": 4,
        "context_length": 16,
        "vocab_size": 64,
        "total_params": 1000,
        "materialization_ffn_size": 32,
    }
    pvr_cfg = {
        **dense_cfg,
        "model_family": "pvr_ec_o",
        "model_variant": "pvr_tiny",
        "num_experts_if_applicable": 4,
        "experts_active_per_token": 1,
        "ablation": None,
    }
    dense = build_model(dense_cfg, device="cpu").model
    pvr = build_model(pvr_cfg, device="cpu").model
    with torch.no_grad():
        dense.token_emb.weight.fill_(0.123)
    report = copy_compatible_dense_weights_to_pvr(dense, pvr)
    assert report["copied_count"] > 0
    assert torch.allclose(pvr.token_emb.weight, dense.token_emb.weight)


def test_copy_compatible_dense_weights_to_pvr_supports_embeddings_only_scope():
    dense_cfg = {
        "model_family": "dense_transformer",
        "model_variant": "dense_tiny",
        "hidden_size": 16,
        "num_layers": 1,
        "num_heads": 4,
        "context_length": 16,
        "vocab_size": 64,
        "total_params": 1000,
        "materialization_ffn_size": 32,
    }
    pvr_cfg = {
        **dense_cfg,
        "model_family": "pvr_ec_o",
        "model_variant": "pvr_tiny",
        "num_experts_if_applicable": 4,
        "experts_active_per_token": 1,
        "ablation": None,
    }
    dense = build_model(dense_cfg, device="cpu").model
    pvr = build_model(pvr_cfg, device="cpu").model
    original_attn = pvr.attn[0].self_attn.in_proj_weight.detach().clone()
    with torch.no_grad():
        dense.token_emb.weight.fill_(0.456)
        dense.layers.layers[0].self_attn.in_proj_weight.fill_(0.789)
    report = copy_compatible_dense_weights_to_pvr(dense, pvr, copy_scope="embeddings_only")
    assert report["copy_scope"] == "embeddings_only"
    assert "token_emb.weight" in report["copied"]
    assert torch.allclose(pvr.token_emb.weight, dense.token_emb.weight)
    assert torch.allclose(pvr.attn[0].self_attn.in_proj_weight, original_attn)


def test_copy_compatible_dense_weights_to_pvr_rejects_unknown_scope():
    dense_cfg = {
        "model_family": "dense_transformer",
        "model_variant": "dense_tiny",
        "hidden_size": 16,
        "num_layers": 1,
        "num_heads": 4,
        "context_length": 16,
        "vocab_size": 64,
        "total_params": 1000,
        "materialization_ffn_size": 32,
    }
    pvr_cfg = {
        **dense_cfg,
        "model_family": "pvr_ec_o",
        "model_variant": "pvr_tiny",
        "num_experts_if_applicable": 4,
        "experts_active_per_token": 1,
        "ablation": None,
    }
    dense = build_model(dense_cfg, device="cpu").model
    pvr = build_model(pvr_cfg, device="cpu").model
    try:
        copy_compatible_dense_weights_to_pvr(dense, pvr, copy_scope="copy_everything")
    except ValueError as exc:
        assert "Unsupported copy_scope" in str(exc)
    else:
        raise AssertionError("unknown copy_scope should raise ValueError")


def test_gated_teacher_loss_masks_high_loss_or_low_margin_tokens():
    student_logits = torch.randn(2, 4, 8)
    teacher_logits = torch.randn(2, 4, 8)
    token_losses = torch.tensor([[1.0, 2.0, 3.0, 4.0], [4.0, 3.0, 2.0, 1.0]])
    route_margins = torch.tensor([[0.9, 0.1, 0.8, 0.2], [0.7, 0.3, 0.6, 0.4]])
    loss, metrics = _gated_teacher_loss(
        student_logits=student_logits,
        teacher_logits=teacher_logits,
        token_losses=token_losses,
        route_margins=route_margins,
        temperature=2.0,
    )
    assert loss.item() > 0
    assert 0.0 < metrics["gated_teacher_mask_rate"] <= 1.0
    assert metrics["gated_teacher_high_loss_rate"] == 0.5
    assert metrics["gated_teacher_low_margin_rate"] == 0.5


def test_summarize_matrix_reports_supported_variant(tmp_path):
    baseline = tmp_path / "baseline"
    repair = tmp_path / "repair"
    baseline.mkdir()
    repair.mkdir()
    clean_route = {
        "owners_per_token": 1.0,
        "top2_execution_count": 0,
        "top4_execution_count": 0,
        "runtime_dynamic_k_count": 0,
        "runtime_expert_choice_count": 0,
        "production_map_mutated": False,
        "prototype_margin": 0.5,
        "owner_entropy": 1.0,
        "prototype_monopoly_rate": 0.2,
    }
    for path, train_loss, eval_loss in [(baseline, 3.0, 4.0), (repair, 2.5, 3.9)]:
        (path / "training_curve.json").write_text(f'{{"loss_curve":[{{"loss":{train_loss}}}]}}')
        (path / "eval_curve.json").write_text(f'{{"eval_curve":[{{"eval_loss":{eval_loss}}}]}}')
        (path / "routing_curve.json").write_text(
            '{"routing_curve":['
            + ",".join([str(clean_route).replace("'", '"').replace("False", "false").replace("True", "true")])
            + "]}"
        )
    payload = summarize_matrix(tmp_path, {
        "baseline": "baseline",
        "shared_trunk_init_from_dense": "repair",
    })
    assert payload["status"] == "PVR_SHARED_TRUNK_INIT_SUPPORTED"


def test_dense_gap_window_classification_buckets_dense_and_pvr_wins(tmp_path):
    dense_path = tmp_path / "dense_eval.json"
    dense_path.write_text('{"eval_curve":[{"step":1,"eval_loss":2.0},{"step":2,"eval_loss":5.0}]}')
    model_dir = tmp_path / "repair"
    model_dir.mkdir()
    (model_dir / "eval_curve.json").write_text('{"eval_curve":[{"step":1,"eval_loss":3.0},{"step":2,"eval_loss":4.0}]}')
    (model_dir / "routing_curve.json").write_text('{"routing_curve":[{"step":1,"prototype_margin":0.9},{"step":2,"prototype_margin":0.1}]}')
    payload = dense_gap_window_classification(
        output_root=tmp_path,
        variants={"shared_trunk_init_from_dense": "repair"},
        dense_eval_curve_path=dense_path,
    )
    counts = payload["variants"]["shared_trunk_init_from_dense"]["bucket_counts"]
    assert counts["dense_better_route_high_confidence"] == 1
    assert counts["pvr_better_route_low_confidence"] == 1
