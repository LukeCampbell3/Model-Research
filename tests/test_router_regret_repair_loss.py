import torch

from benchmark.model_factory import build_model
from benchmark.runners.run_training import _pvr_final_block_router_repair_loss


def test_final_block_router_regret_loss_has_router_gradient():
    config = {
        "model_variant": "router_regret_smoke",
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
        "attention_only_trunk": True,
        "substrate_mode": "attention_norms",
        "straight_through_router": True,
        "prototype_routing": True,
        "router_regret_aux_weight": 0.01,
        "router_oracle_kl_weight": 0.01,
        "router_regret_temperature": 1.0,
    }
    model = build_model(config, device="cpu").model
    input_ids = torch.randint(0, 255, (2, 8))
    targets = torch.randint(0, 255, (2, 8))
    loss, metrics = _pvr_final_block_router_repair_loss(model, input_ids, targets, config, device="cpu")
    assert torch.isfinite(loss)
    assert metrics["router_expected_regret_loss"] >= 0.0
    loss.backward()
    grad = model.blocks[-1].router.weight.grad
    assert grad is not None
    assert float(grad.abs().sum()) > 0.0
