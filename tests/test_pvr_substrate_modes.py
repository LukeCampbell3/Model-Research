import torch

from benchmark.model_factory import (
    AttentionNoNormBlock,
    AttentionOnlyBlock,
    IdentityTrunkBlock,
    NormOnlyBlock,
    build_model,
)


def _base_config(substrate_mode: str):
    return {
        "model_variant": f"substrate_{substrate_mode}",
        "model_family": "pvr_ec_o",
        "vocab_size": 256,
        "hidden_size": 16,
        "num_layers": 2,
        "num_heads": 2,
        "context_length": 32,
        "materialization_ffn_size": 24,
        "shared_materialization_ffn_size": 24,
        "num_experts_if_applicable": 4,
        "experts_active_per_token": 1,
        "ablation": "no_descriptor_operator",
        "attention_only_trunk": substrate_mode != "full_transformer_random_ean",
        "substrate_mode": substrate_mode,
        "straight_through_router": True,
        "prototype_routing": True,
    }


def test_pvr_substrate_modes_materialize_distinct_trunk_blocks():
    expected = {
        "embeddings_only": IdentityTrunkBlock,
        "embeddings_attention": AttentionNoNormBlock,
        "embeddings_norms": NormOnlyBlock,
        "attention_norms": AttentionOnlyBlock,
        "full_transformer_random_ean": torch.nn.TransformerEncoderLayer,
    }
    for mode, cls in expected.items():
        materialized = build_model(_base_config(mode), device="cpu")
        assert isinstance(materialized.model.attn[0], cls)
        logits = materialized.model(torch.randint(0, 255, (1, 8)))
        assert logits.shape == (1, 8, 256)
