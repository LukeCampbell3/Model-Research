"""Materialize benchmark model families for architecture checks.

These models are for construction, parameter accounting, and runner plumbing.
They are not trained checkpoints and must not be reported as benchmark
capability evidence.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import torch
import torch.nn as nn
import torch.nn.functional as F


class DenseCausalLM(nn.Module):
    def __init__(self, *, vocab_size: int, hidden_size: int, num_layers: int, num_heads: int, context_length: int, ffn_size: int):
        super().__init__()
        self.token_emb = nn.Embedding(vocab_size, hidden_size)
        self.pos_emb = nn.Embedding(context_length, hidden_size)
        layer = nn.TransformerEncoderLayer(
            d_model=hidden_size,
            nhead=num_heads,
            dim_feedforward=ffn_size,
            dropout=0.0,
            activation="gelu",
            batch_first=True,
            norm_first=True,
        )
        self.layers = nn.TransformerEncoder(layer, num_layers=num_layers)
        self.ln_f = nn.LayerNorm(hidden_size)
        self.head = nn.Linear(hidden_size, vocab_size, bias=False)
        self.head.weight = self.token_emb.weight

    def forward(self, input_ids: torch.Tensor) -> torch.Tensor:
        seq_len = input_ids.shape[1]
        positions = torch.arange(seq_len, device=input_ids.device).unsqueeze(0)
        x = self.token_emb(input_ids) + self.pos_emb(positions)
        mask = torch.triu(torch.ones(seq_len, seq_len, device=input_ids.device), diagonal=1).bool()
        x = self.layers(x, mask=mask)
        return self.head(self.ln_f(x))


class ExpertMLP(nn.Module):
    def __init__(self, hidden_size: int, ffn_size: int):
        super().__init__()
        self.w1 = nn.Linear(hidden_size, ffn_size)
        self.w2 = nn.Linear(ffn_size, hidden_size)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.w2(F.gelu(self.w1(x)))


class AttentionOnlyBlock(nn.Module):
    """Transformer attention block without the dense FFN sublayer."""

    def __init__(self, *, hidden_size: int, num_heads: int):
        super().__init__()
        self.norm1 = nn.LayerNorm(hidden_size)
        self.self_attn = nn.MultiheadAttention(hidden_size, num_heads, dropout=0.0, batch_first=True)
        self.norm2 = nn.LayerNorm(hidden_size)

    def forward(self, src: torch.Tensor, src_mask: torch.Tensor | None = None) -> torch.Tensor:
        h = self.norm1(src)
        attn, _ = self.self_attn(h, h, h, attn_mask=src_mask, need_weights=False)
        return self.norm2(src + attn)


class IdentityTrunkBlock(nn.Module):
    """No shared contextual trunk beyond token and position embeddings."""

    def forward(self, src: torch.Tensor, src_mask: torch.Tensor | None = None) -> torch.Tensor:
        del src_mask
        return src


class AttentionNoNormBlock(nn.Module):
    """Self-attention substrate without LayerNorm geometry support."""

    def __init__(self, *, hidden_size: int, num_heads: int):
        super().__init__()
        self.self_attn = nn.MultiheadAttention(hidden_size, num_heads, dropout=0.0, batch_first=True)

    def forward(self, src: torch.Tensor, src_mask: torch.Tensor | None = None) -> torch.Tensor:
        attn, _ = self.self_attn(src, src, src, attn_mask=src_mask, need_weights=False)
        return src + attn


class NormOnlyBlock(nn.Module):
    """LayerNorm substrate without contextual attention."""

    def __init__(self, *, hidden_size: int):
        super().__init__()
        self.norm = nn.LayerNorm(hidden_size)

    def forward(self, src: torch.Tensor, src_mask: torch.Tensor | None = None) -> torch.Tensor:
        del src_mask
        return self.norm(src)


def _substrate_block(*, substrate_mode: str, hidden_size: int, num_heads: int, ffn_size: int) -> nn.Module:
    if substrate_mode == "embeddings_only":
        return IdentityTrunkBlock()
    if substrate_mode == "embeddings_attention":
        return AttentionNoNormBlock(hidden_size=hidden_size, num_heads=num_heads)
    if substrate_mode == "embeddings_norms":
        return NormOnlyBlock(hidden_size=hidden_size)
    if substrate_mode == "attention_norms":
        return AttentionOnlyBlock(hidden_size=hidden_size, num_heads=num_heads)
    if substrate_mode == "full_transformer_random_ean":
        return nn.TransformerEncoderLayer(
            d_model=hidden_size,
            nhead=num_heads,
            dim_feedforward=ffn_size,
            dropout=0.0,
            activation="gelu",
            batch_first=True,
            norm_first=True,
        )
    raise ValueError(f"Unsupported substrate_mode: {substrate_mode}")


class ReferenceMoEBlock(nn.Module):
    def __init__(self, *, hidden_size: int, num_experts: int, experts_active: int, ffn_size: int):
        super().__init__()
        self.ln = nn.LayerNorm(hidden_size)
        self.router = nn.Linear(hidden_size, num_experts, bias=False)
        self.experts = nn.ModuleList([ExpertMLP(hidden_size, ffn_size) for _ in range(num_experts)])
        self.experts_active = experts_active

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        h = self.ln(x)
        scores = self.router(h)
        topk = torch.topk(scores, k=self.experts_active, dim=-1).indices
        # This construction path is not the benchmark hot path. It is a small
        # correctness fallback for tiny local checks.
        out = torch.zeros_like(x)
        for expert_id, expert in enumerate(self.experts):
            mask = (topk == expert_id).any(dim=-1)
            if mask.any():
                out[mask] += expert(h[mask]) / float(self.experts_active)
        return x + out


class ReferenceMoELM(nn.Module):
    def __init__(
        self,
        *,
        vocab_size: int,
        hidden_size: int,
        num_layers: int,
        num_heads: int,
        context_length: int,
        num_experts: int,
        experts_active: int,
        ffn_size: int,
        attention_only_trunk: bool = False,
        substrate_mode: str | None = None,
    ):
        super().__init__()
        substrate_mode = substrate_mode or ("attention_norms" if attention_only_trunk else "full_transformer_random_ean")
        self.token_emb = nn.Embedding(vocab_size, hidden_size)
        self.pos_emb = nn.Embedding(context_length, hidden_size)
        self.attn = nn.ModuleList([
            _substrate_block(substrate_mode=substrate_mode, hidden_size=hidden_size, num_heads=num_heads, ffn_size=ffn_size)
            for _ in range(num_layers)
        ])
        self.moe = nn.ModuleList([
            ReferenceMoEBlock(hidden_size=hidden_size, num_experts=num_experts, experts_active=experts_active, ffn_size=ffn_size)
            for _ in range(num_layers)
        ])
        self.ln_f = nn.LayerNorm(hidden_size)
        self.head = nn.Linear(hidden_size, vocab_size, bias=False)
        self.head.weight = self.token_emb.weight

    def forward(self, input_ids: torch.Tensor) -> torch.Tensor:
        seq_len = input_ids.shape[1]
        positions = torch.arange(seq_len, device=input_ids.device).unsqueeze(0)
        x = self.token_emb(input_ids) + self.pos_emb(positions)
        mask = torch.triu(torch.ones(seq_len, seq_len, device=input_ids.device), diagonal=1).bool()
        for attn, moe in zip(self.attn, self.moe):
            x = attn(x, src_mask=mask)
            x = moe(x)
        return self.head(self.ln_f(x))


class PVRECOBlock(nn.Module):
    def __init__(
        self,
        *,
        hidden_size: int,
        num_experts: int,
        experts_active: int,
        expert_ffn_size: int,
        shared_ffn_size: int,
        use_prototypes: bool,
        use_descriptor_operator: bool,
        shared_only: bool,
        straight_through_router: bool = False,
        prototype_routing: bool = False,
    ):
        super().__init__()
        self.ln = nn.LayerNorm(hidden_size)
        self.shared = ExpertMLP(hidden_size, shared_ffn_size)
        self.router = nn.Linear(hidden_size, num_experts, bias=False)
        self.experts = nn.ModuleList([] if shared_only else [ExpertMLP(hidden_size, expert_ffn_size) for _ in range(num_experts)])
        self.prototypes = nn.Parameter(torch.empty(num_experts * 4, hidden_size)) if use_prototypes else None
        self.descriptor_operator = nn.Linear(hidden_size, hidden_size, bias=False) if use_descriptor_operator else None
        self.experts_active = experts_active
        self.shared_only = shared_only
        self.straight_through_router = straight_through_router
        self.prototype_routing = prototype_routing
        self.last_owner_count = 0
        if self.prototypes is not None:
            nn.init.normal_(self.prototypes, mean=0.0, std=0.02)

    def routing_scores(self, h: torch.Tensor) -> torch.Tensor:
        scores = self.router(h)
        if self.prototype_routing and self.prototypes is not None:
            expert_prototypes = self.prototypes.reshape(self.router.out_features, -1, h.shape[-1]).mean(dim=1)
            proto_scores = h @ expert_prototypes.to(dtype=h.dtype).T
            scores = scores + proto_scores / max(1.0, h.shape[-1] ** 0.5)
        return scores

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        h = self.ln(x)
        if self.descriptor_operator is not None:
            h = h + self.descriptor_operator(h)
        out = self.shared(h)
        if not self.shared_only:
            scores = self.routing_scores(h)
            owner = torch.argmax(scores, dim=-1)
            self.last_owner_count = 1
            sparse = torch.zeros_like(x)
            for expert_id, expert in enumerate(self.experts):
                mask = owner == expert_id
                if mask.any():
                    sparse[mask] = expert(h[mask])
            if self.straight_through_router:
                probs = F.softmax(scores, dim=-1)
                dense_sparse = torch.zeros_like(x)
                for expert_id, expert in enumerate(self.experts):
                    dense_sparse = dense_sparse + probs[..., expert_id : expert_id + 1] * expert(h)
                sparse = sparse + dense_sparse - dense_sparse.detach()
            out = out + sparse
        return x + out


class PVRECOLM(nn.Module):
    def __init__(
        self,
        *,
        vocab_size: int,
        hidden_size: int,
        num_layers: int,
        num_heads: int,
        context_length: int,
        num_experts: int,
        ffn_size: int,
        ablation: str | None,
        shared_ffn_size: int | None = None,
        attention_only_trunk: bool = False,
        straight_through_router: bool = False,
        prototype_routing: bool = False,
        substrate_mode: str | None = None,
    ):
        super().__init__()
        shared_ffn_size = shared_ffn_size or ffn_size
        substrate_mode = substrate_mode or ("attention_norms" if attention_only_trunk else "full_transformer_random_ean")
        self.token_emb = nn.Embedding(vocab_size, hidden_size)
        self.pos_emb = nn.Embedding(context_length, hidden_size)
        self.attn = nn.ModuleList([
            _substrate_block(substrate_mode=substrate_mode, hidden_size=hidden_size, num_heads=num_heads, ffn_size=ffn_size)
            for _ in range(num_layers)
        ])
        self.blocks = nn.ModuleList([
            PVRECOBlock(
                hidden_size=hidden_size,
                num_experts=num_experts,
                experts_active=1,
                expert_ffn_size=ffn_size,
                shared_ffn_size=shared_ffn_size,
                use_prototypes=ablation != "no_prototypes",
                use_descriptor_operator=ablation != "no_descriptor_operator",
                shared_only=ablation == "shared_only",
                straight_through_router=straight_through_router,
                prototype_routing=prototype_routing,
            )
            for _ in range(num_layers)
        ])
        self.ln_f = nn.LayerNorm(hidden_size)
        self.head = nn.Linear(hidden_size, vocab_size, bias=False)
        self.head.weight = self.token_emb.weight

    def forward(self, input_ids: torch.Tensor) -> torch.Tensor:
        seq_len = input_ids.shape[1]
        positions = torch.arange(seq_len, device=input_ids.device).unsqueeze(0)
        x = self.token_emb(input_ids) + self.pos_emb(positions)
        mask = torch.triu(torch.ones(seq_len, seq_len, device=input_ids.device), diagonal=1).bool()
        for attn, block in zip(self.attn, self.blocks):
            x = attn(x, src_mask=mask)
            x = block(x)
        return self.head(self.ln_f(x))

    def routing_aux_loss(self) -> torch.Tensor:
        losses = []
        for block in self.blocks:
            if block.prototypes is not None:
                proto = F.normalize(block.prototypes.float(), dim=-1)
                gram = proto @ proto.T
                eye = torch.eye(gram.shape[0], device=gram.device)
                losses.append(((gram - eye) ** 2).mean())
        if not losses:
            return torch.zeros((), device=self.token_emb.weight.device)
        return torch.stack(losses).mean()


@dataclass
class ModelMaterialization:
    model: nn.Module
    total_params_actual: int
    active_params_per_token_actual: int
    family: str
    variant: str


def count_parameters(model: nn.Module) -> int:
    return sum(p.numel() for p in model.parameters())


def _active_params_estimate(config: dict[str, Any], total_actual: int) -> int:
    family = str(config.get("model_family"))
    if family == "dense_transformer":
        return total_actual
    hidden = int(config["hidden_size"])
    layers = int(config["num_layers"])
    active_experts = int(config.get("experts_active_per_token") or 1)
    ffn_size = int(config.get("materialization_ffn_size") or _infer_ffn_size(config))
    shared_ffn_size = int(config.get("shared_materialization_ffn_size") or ffn_size)
    expert_params = hidden * ffn_size * 2 + ffn_size + hidden
    shared_params = hidden * shared_ffn_size * 2 + shared_ffn_size + hidden
    base = max(0, total_actual - int(config.get("num_experts_if_applicable") or 0) * layers * expert_params)
    if family == "pvr_ec_o":
        base = max(0, total_actual - layers * shared_params - int(config.get("num_experts_if_applicable") or 0) * layers * expert_params)
        return base + layers * shared_params + active_experts * layers * expert_params
    return base + active_experts * layers * expert_params


def _infer_ffn_size(config: dict[str, Any]) -> int:
    family = str(config.get("model_family"))
    target = int(config.get("total_params") or 100_000_000)
    vocab = int(config.get("vocab_size", 50_257))
    hidden = int(config["hidden_size"])
    layers = int(config["num_layers"])
    experts = max(1, int(config.get("num_experts_if_applicable") or 1))
    embeddings = vocab * hidden + int(config["context_length"]) * hidden + vocab * hidden
    attn_per_layer = 4 * hidden * hidden + 8 * hidden
    norms_per_layer = 8 * hidden
    available = max(target - embeddings - layers * (attn_per_layer + norms_per_layer), layers * hidden * hidden)
    if family == "dense_transformer":
        denom = max(1, layers * (2 * hidden + 1))
    elif family in {"vanilla_switch_top1_reference", "generic_top2_moe_reference", "custom_fixed_moe_strong_router"}:
        denom = max(1, layers * experts * (2 * hidden + 1))
    elif family == "pvr_ec_o":
        ablation = config.get("ablation")
        expert_count = 0 if ablation == "shared_only" else experts
        denom = max(1, layers * (expert_count + 1) * (2 * hidden + 1))
    else:
        denom = max(1, layers * (2 * hidden + 1))
    return max(16, min(hidden * 4, int(available / denom)))


def build_model(config: dict[str, Any], *, device: str = "meta") -> ModelMaterialization:
    family = str(config["model_family"])
    kwargs = {
        "vocab_size": int(config.get("vocab_size", 50_257)),
        "hidden_size": int(config["hidden_size"]),
        "num_layers": int(config["num_layers"]),
        "num_heads": int(config["num_heads"]),
        "context_length": int(config["context_length"]),
        "ffn_size": int(config.get("materialization_ffn_size") or _infer_ffn_size(config)),
    }
    with torch.device(device):
        if family == "dense_transformer":
            model = DenseCausalLM(**kwargs)
        elif family == "vanilla_switch_top1_reference":
            model = ReferenceMoELM(
                **kwargs,
                num_experts=int(config.get("num_experts_if_applicable") or 8),
                experts_active=1,
                attention_only_trunk=bool(config.get("attention_only_trunk", False)),
                substrate_mode=config.get("substrate_mode"),
            )
        elif family == "generic_top2_moe_reference":
            model = ReferenceMoELM(
                **kwargs,
                num_experts=int(config.get("num_experts_if_applicable") or 8),
                experts_active=2,
                attention_only_trunk=bool(config.get("attention_only_trunk", False)),
                substrate_mode=config.get("substrate_mode"),
            )
        elif family == "pvr_ec_o":
            model = PVRECOLM(
                **kwargs,
                num_experts=int(config.get("num_experts_if_applicable") or 8),
                ablation=config.get("ablation"),
                shared_ffn_size=int(config["shared_materialization_ffn_size"]) if config.get("shared_materialization_ffn_size") else None,
                attention_only_trunk=bool(config.get("attention_only_trunk", False)),
                straight_through_router=bool(config.get("straight_through_router", False)),
                prototype_routing=bool(config.get("prototype_routing", False)),
                substrate_mode=config.get("substrate_mode"),
            )
        elif family == "custom_fixed_moe_strong_router":
            model = ReferenceMoELM(
                **kwargs,
                num_experts=int(config.get("num_experts_if_applicable") or 8),
                experts_active=2,
            )
        else:
            raise ValueError(f"Unsupported model family: {family}")
    total_actual = count_parameters(model)
    return ModelMaterialization(
        model=model,
        total_params_actual=total_actual,
        active_params_per_token_actual=_active_params_estimate(config, total_actual),
        family=family,
        variant=str(config["model_variant"]),
    )
