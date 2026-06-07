"""PVR-EC Full Model: integrates with existing experiment/benchmark infrastructure.

This is a decoder-only transformer that uses PVR-EC MoE blocks instead of
the standard MoE FFN. It implements the same interface as SparseLoopMoEModel
and DenseTransformer so it can be used in the benchmark runner.
"""

from __future__ import annotations

from dataclasses import dataclass
import math

import torch
import torch.nn as nn
import torch.nn.functional as F

from sparse_loop_moe.models.pvr_ec.pvr_ec_moe import PVRECMoEFFN


@dataclass
class PVRECModelConfig:
    """Configuration for PVR-EC model variant."""
    vocab_size: int = 256
    d_model: int = 128
    max_seq_len: int = 256
    n_layers: int = 2
    n_heads: int = 4
    d_ff: int = 256
    num_experts: int = 4
    num_prototypes: int = 16
    max_k: int = 4
    d_expert: int = 128  # Expert delta hidden dim (smaller than d_ff)
    dropout: float = 0.1
    tie_weights: bool = True
    load_bias_cap: float = 0.20
    pvr_execution_mode: str = "variable_k_pack_by_expert"
    pvr_expert_type: str = "delta_rank_medium"
    pvr_training_dispatch_mode: str | None = None
    pvr_inference_dispatch_mode: str | None = None
    target_avg_k: float = 2.0
    expert_capacity: int | None = None
    branch_ticket_shadow_mode: bool = True
    emit_branch_tickets_during_training: bool = False
    max_shadow_branch_tickets: int = 64
    pvr_deploy_mode: str = "off"
    pvr_aux_alpha: float = 0.5
    pvr_shared_scale: float = 1.0
    pvr_expert_delta_scale: float = 1.0
    pvr_expert_delta_scale_schedule: str = "constant"
    pvr_expert_delta_scale_start: float | None = None
    pvr_expert_delta_scale_end: float | None = None
    pvr_expert_delta_scale_warmup_steps: int = 0
    pvr_expert_delta_scale_hold_steps: int = 0
    pvr_expert_delta_scale_decay: float | None = None
    pvr_debug_force_expert_id: int | None = None
    pvr_debug_owner_mode: str = ""
    pvr_sparse_aux_loss_variant: str = "baseline_main_loss"
    pvr_sparse_aux_scope: str = "aux_all_tokens"
    pvr_sparse_aux_schedule_total_steps: int = 500
    pvr_output_temperature: float = 1.0
    profile: bool = False
    collect_debug: bool = False
    emit_branch_tickets: bool = False
    mergeability_mode: str = "disabled"
    runtime_branching: bool = False


class PVRECBlock(nn.Module):
    """Single PVR-EC transformer block: attention + PVR-EC MoE."""

    def __init__(self, config: PVRECModelConfig):
        super().__init__()
        self.attn_ln = nn.LayerNorm(config.d_model)
        self.attn = nn.MultiheadAttention(
            config.d_model, config.n_heads, dropout=config.dropout, batch_first=True
        )
        self.attn_dropout = nn.Dropout(config.dropout)

        self.moe_ln = nn.LayerNorm(config.d_model)
        self.moe = PVRECMoEFFN(
            d_model=config.d_model,
            d_ff=config.d_ff,
            num_experts=config.num_experts,
            d_expert=config.d_expert,
            num_prototypes=config.num_prototypes,
            max_k=config.max_k,
            dropout=config.dropout,
            load_bias_cap=config.load_bias_cap,
            execution_mode=config.pvr_execution_mode,
            expert_type=config.pvr_expert_type,
            pvr_training_dispatch_mode=config.pvr_training_dispatch_mode,
            pvr_inference_dispatch_mode=config.pvr_inference_dispatch_mode,
            target_avg_k=config.target_avg_k,
            expert_capacity=config.expert_capacity,
            branch_ticket_shadow_mode=config.branch_ticket_shadow_mode,
            emit_branch_tickets_during_training=config.emit_branch_tickets_during_training,
            max_shadow_branch_tickets=config.max_shadow_branch_tickets,
            pvr_deploy_mode=config.pvr_deploy_mode,
            pvr_aux_alpha=config.pvr_aux_alpha,
            pvr_shared_scale=config.pvr_shared_scale,
            pvr_expert_delta_scale=config.pvr_expert_delta_scale,
            pvr_expert_delta_scale_schedule=config.pvr_expert_delta_scale_schedule,
            pvr_expert_delta_scale_start=config.pvr_expert_delta_scale_start,
            pvr_expert_delta_scale_end=config.pvr_expert_delta_scale_end,
            pvr_expert_delta_scale_warmup_steps=config.pvr_expert_delta_scale_warmup_steps,
            pvr_expert_delta_scale_hold_steps=config.pvr_expert_delta_scale_hold_steps,
            pvr_expert_delta_scale_decay=config.pvr_expert_delta_scale_decay,
            pvr_debug_force_expert_id=config.pvr_debug_force_expert_id,
            pvr_debug_owner_mode=config.pvr_debug_owner_mode,
            profile=config.profile,
            collect_debug=config.collect_debug,
            emit_branch_tickets=config.emit_branch_tickets,
            mergeability_mode=config.mergeability_mode,
            runtime_branching=config.runtime_branching,
        )

    def forward(self, x: torch.Tensor) -> tuple[torch.Tensor, dict]:
        # Self-attention
        attn_in = self.attn_ln(x)
        attn_out, _ = self.attn(attn_in, attn_in, attn_in, need_weights=False)
        x = x + self.attn_dropout(attn_out)

        # PVR-EC MoE FFN
        moe_in = self.moe_ln(x)
        moe_out, aux = self.moe(moe_in)
        x = x + moe_out

        return x, aux


class PVRECModel(nn.Module):
    """Full PVR-EC model for benchmarking.

    Same interface as DenseTransformer and SparseLoopMoEModel:
    forward(input_ids, targets) -> {"logits", "loss", "hidden_states", ...}
    """

    def __init__(self, config: PVRECModelConfig):
        super().__init__()
        self.config = config

        # Embeddings
        self.token_emb = nn.Embedding(config.vocab_size, config.d_model)
        self.pos_emb = nn.Embedding(config.max_seq_len, config.d_model)
        self.dropout = nn.Dropout(config.dropout)

        # PVR-EC blocks
        self.blocks = nn.ModuleList([
            PVRECBlock(config) for _ in range(config.n_layers)
        ])

        # Output
        self.ln_f = nn.LayerNorm(config.d_model)
        self.head = nn.Linear(config.d_model, config.vocab_size, bias=False)

        if config.tie_weights:
            self.head.weight = self.token_emb.weight

        self._init_weights()
        self._training_step = 0

    def set_training_step(self, step: int) -> float:
        """Propagate a training step to all PVR-EC MoE blocks."""

        self._training_step = int(step)
        values = []
        for block in self.blocks:
            values.append(float(block.moe.set_training_step(step)))
        return sum(values) / max(len(values), 1)

    def get_expert_delta_scale(self) -> float:
        values = [float(block.moe.get_expert_delta_scale()) for block in self.blocks]
        return sum(values) / max(len(values), 1)

    def _init_weights(self):
        for module in self.modules():
            if isinstance(module, nn.Linear):
                nn.init.normal_(module.weight, mean=0.0, std=0.02)
                if module.bias is not None:
                    nn.init.zeros_(module.bias)
            elif isinstance(module, nn.Embedding):
                nn.init.normal_(module.weight, mean=0.0, std=0.02)

    def forward(
        self,
        input_ids: torch.Tensor,
        targets: torch.Tensor = None,
    ) -> dict:
        """Forward pass compatible with benchmark infrastructure.

        Args:
            input_ids: [batch, seq_len]
            targets: [batch, seq_len] optional

        Returns:
            dict with logits, loss, hidden_states, loop_stats, aux_losses
        """
        batch_size, seq_len = input_ids.shape
        device = input_ids.device

        positions = torch.arange(seq_len, device=device).unsqueeze(0)
        x = self.dropout(self.token_emb(input_ids) + self.pos_emb(positions))

        all_aux = []
        for block in self.blocks:
            x, aux = block(x)
            all_aux.append(aux)

        x = self.ln_f(x)
        logits = self.head(x)
        temperature = float(self.config.pvr_output_temperature or 1.0)
        if not self.training and abs(temperature - 1.0) > 1e-6:
            logits = logits / max(temperature, 1e-6)
        needs_sparse_aux = (
            self.training
            and targets is not None
            and str(self.config.pvr_sparse_aux_loss_variant or "baseline_main_loss")
            not in {"", "baseline", "baseline_main_loss", "none"}
        )
        logit_decomposition = self._build_sparse_logit_decomposition(all_aux) if self.training else {}

        result = {
            "logits": logits,
            "hidden_states": x,
            "loop_stats": [],  # No loops in PVR-EC base (compatible interface)
            "aux_losses": {},
        }
        if logit_decomposition:
            result["pvr_logit_decomposition"] = logit_decomposition

        # Aggregate aux losses
        if all_aux:
            lb_losses = [a["load_balance_loss"] for a in all_aux if "load_balance_loss" in a]
            if lb_losses:
                result["aux_losses"]["load_balance_loss"] = torch.stack(lb_losses).mean()
            result["pvr_diagnostics"] = self._aggregate_pvr_diagnostics(all_aux)

        # Task loss
        if targets is not None:
            loss = F.cross_entropy(
                logits.view(-1, self.config.vocab_size), targets.view(-1)
            )
            result["loss"] = loss
            if needs_sparse_aux:
                aux_loss, aux_metrics = self._sparse_direction_auxiliary_loss(
                    result=result,
                    targets=targets,
                )
                if aux_loss is not None:
                    result["aux_losses"]["sparse_auxiliary_loss"] = aux_loss
                if aux_metrics:
                    result["pvr_sparse_auxiliary"] = aux_metrics

        return result

    def _build_sparse_logit_decomposition(self, all_aux: list[dict]) -> dict[str, torch.Tensor]:
        if not all_aux:
            return {}
        last_aux = all_aux[-1]
        required = ("shared_hidden", "sparse_delta", "combined_hidden")
        if not all(key in last_aux for key in required):
            return {}
        shared_hidden = last_aux["shared_hidden"]
        sparse_delta = last_aux["sparse_delta"]
        combined_hidden = shared_hidden + sparse_delta
        return {
            "shared_hidden": shared_hidden,
            "sparse_delta": sparse_delta,
            "combined_hidden": combined_hidden,
            "shared_logits": self.head(shared_hidden),
            "sparse_delta_logits": self.head(sparse_delta),
            "combined_logits_from_parts": self.head(combined_hidden),
        }

    def _sparse_direction_auxiliary_loss(
        self,
        result: dict,
        targets: torch.Tensor,
    ) -> tuple[torch.Tensor | None, dict[str, float]]:
        variant = str(self.config.pvr_sparse_aux_loss_variant or "baseline_main_loss")
        if variant in {"", "baseline", "baseline_main_loss", "none"}:
            return None, {
                "sparse_aux_loss_variant": variant,
                "sparse_aux_scope": self.config.pvr_sparse_aux_scope,
                "sparse_auxiliary_loss": 0.0,
            }
        decomposition = result.get("pvr_logit_decomposition") or {}
        sparse_logits = decomposition.get("sparse_delta_logits")
        shared_logits = decomposition.get("shared_logits")
        combined_logits = result.get("logits")
        if sparse_logits is None or shared_logits is None or combined_logits is None:
            return None, {}

        mask = self._sparse_auxiliary_mask(targets)
        if not mask.any():
            mask = targets != 0
        if not mask.any():
            mask = torch.ones_like(targets, dtype=torch.bool)

        sparse_flat = sparse_logits[mask]
        shared_flat = shared_logits[mask]
        combined_flat = combined_logits[mask]
        target_flat = targets[mask]
        one_hot = F.one_hot(target_flat, num_classes=sparse_flat.shape[-1]).bool()
        wrong_sparse = sparse_flat.masked_fill(one_hot, -1e9)
        delta_correct = sparse_flat.gather(-1, target_flat.unsqueeze(-1)).squeeze(-1)
        delta_wrong_max = wrong_sparse.max(dim=-1).values

        weighted_losses: list[torch.Tensor] = []
        metrics: dict[str, float] = {
            "sparse_aux_loss_variant": variant,
            "sparse_aux_scope": self.config.pvr_sparse_aux_scope,
        }

        def add_sparse_ce(weight: float) -> None:
            loss = F.cross_entropy(sparse_flat, target_flat)
            weighted_losses.append(float(weight) * loss)
            metrics["sparse_ce_loss"] = float(loss.detach().item())

        def add_margin(weight: float, margin_target: float) -> None:
            loss = F.relu(float(margin_target) - (delta_correct - delta_wrong_max)).mean()
            weighted_losses.append(float(weight) * loss)
            metrics["margin_alignment_loss"] = float(loss.detach().item())

        def add_wrong_suppress(weight: float, threshold: float) -> None:
            wrong_values = sparse_flat.masked_select(~one_hot)
            loss = F.relu(wrong_values - float(threshold)).mean()
            weighted_losses.append(float(weight) * loss)
            metrics["wrong_suppression_loss"] = float(loss.detach().item())

        def add_logit_norm(weight: float) -> None:
            loss = sparse_flat.float().pow(2).mean()
            weighted_losses.append(float(weight) * loss)
            metrics["logit_norm_penalty_loss"] = float(loss.detach().item())

        def add_temperature_regularization(weight: float, min_entropy_ratio: float = 0.55) -> None:
            probs = F.softmax(sparse_flat.float(), dim=-1)
            entropy = -(probs * probs.clamp_min(1e-12).log()).sum(dim=-1)
            target_entropy = math.log(max(sparse_flat.shape[-1], 2)) * float(min_entropy_ratio)
            loss = F.relu(float(target_entropy) - entropy).mean()
            weighted_losses.append(float(weight) * loss)
            metrics["temperature_regularization_loss"] = float(loss.detach().item())

        def add_harm(weight: float, tolerance: float) -> None:
            combined_loss = F.cross_entropy(combined_flat, target_flat, reduction="none")
            shared_loss = F.cross_entropy(shared_flat, target_flat, reduction="none").detach()
            loss = F.relu(combined_loss - shared_loss + float(tolerance)).mean()
            weighted_losses.append(float(weight) * loss)
            metrics["residual_harm_loss"] = float(loss.detach().item())

        if variant == "sparse_ce_0_03":
            add_sparse_ce(0.03)
        elif variant == "sparse_ce_0_05":
            add_sparse_ce(0.05)
        elif variant == "sparse_ce_0_10":
            add_sparse_ce(0.10)
        elif variant in {"sparse_ce_warmup_then_decay", "sparse_ce_warmup_decay"}:
            add_sparse_ce(self._sparse_ce_warmup_decay_weight())
        elif variant == "margin_align_0_03_m0_5":
            add_margin(0.03, 0.5)
        elif variant == "margin_align_0_05_m0_5":
            add_margin(0.05, 0.5)
        elif variant == "wrong_suppress_0_03_t0_25":
            add_wrong_suppress(0.03, 0.25)
        elif variant == "sparse_ce_0_03_plus_margin_0_03":
            add_sparse_ce(0.03)
            add_margin(0.03, 0.5)
        elif variant == "sparse_ce_0_03_plus_wrong_suppress_0_03":
            add_sparse_ce(0.03)
            add_wrong_suppress(0.03, 0.25)
        elif variant == "sparse_ce_0_05_plus_wrong_suppress_0_01":
            add_sparse_ce(0.05)
            add_wrong_suppress(0.01, 0.25)
        elif variant in {"sparse_ce_0_03_plus_logit_norm_penalty_light", "sparse_ce_0_03_plus_logit_norm_light"}:
            add_sparse_ce(0.03)
            add_logit_norm(0.0005)
        elif variant == "sparse_ce_0_05_plus_logit_norm_penalty_light":
            add_sparse_ce(0.05)
            add_logit_norm(0.0005)
        elif variant == "sparse_ce_0_07_plus_logit_norm_penalty_light":
            add_sparse_ce(0.07)
            add_logit_norm(0.0005)
        elif variant == "sparse_ce_0_05_plus_logit_norm_penalty_medium":
            add_sparse_ce(0.05)
            add_logit_norm(0.0015)
        elif variant == "sparse_ce_0_05_plus_temperature_regularization":
            add_sparse_ce(0.05)
            add_temperature_regularization(0.01)
        elif variant in {"sparse_ce_0_05_plus_posthoc_temperature_calibration", "posthoc_temperature_T_1_2"}:
            add_sparse_ce(0.05)
            add_temperature_regularization(0.005)
        elif variant == "sparse_ce_0_03_plus_posthoc_temperature_calibration":
            add_sparse_ce(0.03)
            add_temperature_regularization(0.005)
        elif variant in {
            "sparse_ce_0_05_plus_logit_norm_light_plus_wrong_suppress_0_01",
            "sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
            "wrong_suppress_0_01_plus_logit_norm_light",
        }:
            add_sparse_ce(0.05)
            add_logit_norm(0.0005)
            add_wrong_suppress(0.01, 0.25)
        elif variant == "sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light":
            add_sparse_ce(0.03)
            add_logit_norm(0.0005)
            add_wrong_suppress(0.01, 0.25)
        elif variant == "logit_norm_penalty_medium":
            add_sparse_ce(0.05)
            add_logit_norm(0.0015)
        elif variant == "margin_0_03_plus_wrong_suppress_0_03":
            add_margin(0.03, 0.5)
            add_wrong_suppress(0.03, 0.25)
        elif variant == "sparse_ce_0_03_plus_harm_0_03":
            add_sparse_ce(0.03)
            add_harm(0.03, 0.0)
        else:
            return None, metrics

        total = torch.stack(weighted_losses).sum() if weighted_losses else None
        if total is not None:
            metrics["sparse_auxiliary_loss"] = float(total.detach().item())
            metrics["delta_correct_minus_top_wrong"] = float((delta_correct - delta_wrong_max).detach().mean().item())
        return total, metrics

    def _sparse_ce_warmup_decay_weight(self) -> float:
        total = max(1, int(self.config.pvr_sparse_aux_schedule_total_steps or 500))
        progress = max(0.0, min(1.0, float(self._training_step) / float(total)))
        if progress < 0.30:
            return 0.05
        if progress < 0.80:
            return 0.03
        return 0.01

    def _sparse_auxiliary_mask(self, targets: torch.Tensor) -> torch.Tensor:
        scope = str(self.config.pvr_sparse_aux_scope or "aux_all_tokens")
        mask = targets != 0
        if scope in {"aux_decision_tokens_only", "aux_final_tokens_only", "aux_dyck_final_state_only"}:
            final_mask = torch.zeros_like(mask)
            final_mask[:, -1] = True
            return final_mask & mask
        return mask

    def count_parameters(self) -> int:
        return sum(p.numel() for p in self.parameters() if p.requires_grad)

    @staticmethod
    def _mean_dict_values(items: list[dict], key: str) -> float:
        values = []
        for item in items:
            value = item.get(key)
            if isinstance(value, torch.Tensor):
                value = value.detach().float().mean().item()
            if isinstance(value, (int, float)):
                values.append(float(value))
        return sum(values) / max(len(values), 1)

    def _aggregate_pvr_diagnostics(self, all_aux: list[dict]) -> dict:
        """Aggregate per-block PVR diagnostics into benchmark-friendly scalars."""

        timings = [a.get("timing", {}) for a in all_aux]
        routing = [a.get("routing_metrics", {}) for a in all_aux]
        contribution = [a.get("contribution_metrics", {}) for a in all_aux]
        mergeability = [a.get("mergeability", {}) for a in all_aux]
        branch_tickets = sum(len(a.get("branch_tickets", [])) for a in all_aux)
        first_aux = all_aux[0] if all_aux else {}
        first_routing = routing[0] if routing else {}

        return {
            "pvr_execution_mode": first_aux.get("pvr_execution_mode", self.config.pvr_execution_mode),
            "pvr_expert_type": first_aux.get("pvr_expert_type", self.config.pvr_expert_type),
            "expert_architecture_id": first_aux.get("expert_architecture_id", ""),
            "expert_inner_dim": self._mean_dict_values(all_aux, "expert_inner_dim"),
            "total_step_time_ms": self._mean_dict_values(timings, "total_step_time_ms"),
            "router_score_time_ms": self._mean_dict_values(timings, "router_score_time_ms"),
            "prototype_shortlist_time_ms": self._mean_dict_values(timings, "prototype_shortlist_time_ms"),
            "bitset_mask_time_ms": self._mean_dict_values(timings, "bitset_mask_time_ms"),
            "assignment_build_time_ms": self._mean_dict_values(timings, "assignment_build_time_ms"),
            "pack_time_ms": self._mean_dict_values(timings, "pack_time_ms"),
            "expert_compute_time_ms": self._mean_dict_values(timings, "expert_compute_time_ms"),
            "small_expert_execution_time_ms": self._mean_dict_values(
                timings, "small_expert_execution_time_ms"
            ),
            "scatter_time_ms": self._mean_dict_values(timings, "scatter_time_ms"),
            "tokens_per_second": self._mean_dict_values(timings, "tokens_per_second"),
            "dispatch_overhead_ratio": self._mean_dict_values(timings, "dispatch_overhead_ratio"),
            "compute_to_dispatch_ratio": self._mean_dict_values(timings, "compute_to_dispatch_ratio"),
            "forward_dispatch_overhead_ratio": self._mean_dict_values(
                timings, "forward_dispatch_overhead_ratio"
            ),
            "backward_dispatch_overhead_ratio": self._mean_dict_values(
                timings, "backward_dispatch_overhead_ratio"
            ),
            "training_compute_to_dispatch_ratio": self._mean_dict_values(
                timings, "training_compute_to_dispatch_ratio"
            ),
            "avg_tokens_per_active_expert": self._mean_dict_values(
                timings, "avg_tokens_per_active_expert"
            ),
            "small_expert_batch_rate": self._mean_dict_values(timings, "small_expert_batch_rate"),
            "avg_k": self._mean_dict_values(routing, "actual_avg_k"),
            "actual_avg_k": self._mean_dict_values(routing, "actual_avg_k"),
            "target_avg_K": self._mean_dict_values(routing, "target_avg_K"),
            "assignment_budget_drift": self._mean_dict_values(routing, "assignment_budget_drift"),
            "fallback_top1_count": self._mean_dict_values(routing, "fallback_top1_count"),
            "overflow_count": self._mean_dict_values(routing, "overflow_count"),
            "expert_utilization": self._mean_dict_values(routing, "expert_utilization"),
            "expert_load_cv": self._mean_dict_values(routing, "load_imbalance"),
            "route_entropy": self._mean_dict_values(routing, "routing_entropy"),
            "num_k1_tokens": self._mean_dict_values(routing, "num_k1_tokens"),
            "num_k2_tokens": self._mean_dict_values(routing, "num_k2_tokens"),
            "num_k4_tokens": self._mean_dict_values(routing, "num_k4_tokens"),
            "assignment_budget_status": first_routing.get("assignment_budget_status", "unknown"),
            "mergeability_score_mean": self._mean_dict_values(
                mergeability, "mergeability_score_mean"
            ),
            "mergeability_score_std": self._mean_dict_values(
                mergeability, "mergeability_score_std"
            ),
            "expert_disagreement_mean": self._mean_dict_values(
                mergeability, "expert_disagreement_mean"
            ),
            "shared_output_norm": self._mean_dict_values(contribution, "shared_output_norm"),
            "sparse_output_norm": self._mean_dict_values(contribution, "sparse_output_norm"),
            "shared_sparse_ratio": self._mean_dict_values(contribution, "shared_sparse_ratio"),
            "pvr_shared_scale": self._mean_dict_values(contribution, "pvr_shared_scale"),
            "pvr_expert_delta_scale": self._mean_dict_values(contribution, "pvr_expert_delta_scale"),
            "pvr_expert_delta_scale_t": self._mean_dict_values(contribution, "pvr_expert_delta_scale_t"),
            "pvr_expert_delta_scale_schedule": first_aux.get("contribution_metrics", {}).get(
                "pvr_expert_delta_scale_schedule",
                self.config.pvr_expert_delta_scale_schedule,
            ),
            "branch_ticket_count": branch_tickets,
            "runtime_branching_enabled": False,
            "branch_tickets_shadow_only": True,
            "actual_owner_count_per_token": self._mean_dict_values(
                routing, "actual_owner_count_per_token"
            ),
            "actual_experts_executed": self._mean_dict_values(routing, "actual_experts_executed"),
            "actual_expert_slots_per_token": self._mean_dict_values(
                routing, "actual_expert_slots_per_token"
            ),
            "dense_all_experts_executed": any(
                bool(item.get("dense_all_experts_executed", False)) for item in routing
            ),
            "oracle_owner_used": any(bool(item.get("oracle_owner_used", False)) for item in routing),
            "forced_action_path_used": any(
                bool(item.get("forced_action_path_used", False)) for item in routing
            ),
            "replay_probe_labels_used": any(
                bool(item.get("replay_probe_labels_used", False)) for item in routing
            ),
        }
