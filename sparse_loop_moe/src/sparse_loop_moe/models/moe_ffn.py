"""Phase 2: Mixture-of-Experts Feed-Forward Network.

Implements the MoE FFN block with optional shared expert,
load balancing loss, and expert utilization metrics.
"""

from __future__ import annotations

import torch
import torch.nn as nn
import torch.nn.functional as F

from sparse_loop_moe.core.types import RouterMetrics


class Expert(nn.Module):
    """Single expert: a feed-forward network."""

    def __init__(self, d_model: int, d_ff: int, dropout: float = 0.1):
        super().__init__()
        self.w1 = nn.Linear(d_model, d_ff)
        self.w2 = nn.Linear(d_ff, d_model)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.w2(self.dropout(F.gelu(self.w1(x))))


class MoEFFN(nn.Module):
    """Mixture-of-Experts Feed-Forward Network.

    Supports:
    - Multiple experts with independent parameters
    - Optional shared expert (always active)
    - Top-k routing with load balancing
    - Expert utilization tracking
    """

    def __init__(
        self,
        d_model: int,
        d_ff: int,
        num_experts: int = 8,
        top_k: int = 2,
        use_shared_expert: bool = True,
        dropout: float = 0.1,
        capacity_factor: float = 1.25,
    ):
        super().__init__()
        self.d_model = d_model
        self.num_experts = num_experts
        self.top_k = top_k
        self.use_shared_expert = use_shared_expert
        self.capacity_factor = capacity_factor

        # Expert pool
        self.experts = nn.ModuleList(
            [Expert(d_model, d_ff, dropout) for _ in range(num_experts)]
        )

        # Optional shared expert (always active, provides baseline capacity)
        if use_shared_expert:
            self.shared_expert = Expert(d_model, d_ff, dropout)
            self.shared_gate = nn.Linear(d_model, 1)

        # Router gate
        self.gate = nn.Linear(d_model, num_experts, bias=False)

        # Tracking
        self._expert_counts: torch.Tensor | None = None
        self.expert_execution_mode = "LOOPED"

    def forward(
        self, x: torch.Tensor, fixed_k: int | None = None
    ) -> tuple[torch.Tensor, dict[str, torch.Tensor]]:
        """Forward pass through MoE FFN.

        Args:
            x: Input tensor [batch, seq_len, d_model]
            fixed_k: Override top_k if provided (for adaptive width)

        Returns:
            output: Processed tensor [batch, seq_len, d_model]
            aux: Dictionary with auxiliary losses and metrics
        """
        batch_size, seq_len, d_model = x.shape
        k = fixed_k if fixed_k is not None else self.top_k

        # Flatten for routing
        flat_x = x.view(-1, d_model)  # [batch*seq, d_model]
        num_tokens = flat_x.shape[0]

        # Compute router logits and probabilities
        router_logits = self.gate(flat_x)  # [num_tokens, num_experts]
        router_probs = F.softmax(router_logits, dim=-1)

        # Top-k selection
        top_k_probs, top_k_indices = torch.topk(router_probs, k, dim=-1)

        # Normalize top-k probabilities
        top_k_probs = top_k_probs / (top_k_probs.sum(dim=-1, keepdim=True) + 1e-8)

        # Compute expert outputs
        output = torch.zeros_like(flat_x)
        for i in range(k):
            expert_idx = top_k_indices[:, i]  # [num_tokens]
            expert_weight = top_k_probs[:, i].unsqueeze(-1)  # [num_tokens, 1]

            for e_idx in range(self.num_experts):
                mask = expert_idx == e_idx
                if mask.any():
                    expert_input = flat_x[mask]
                    expert_output = self.experts[e_idx](expert_input)
                    output[mask] += expert_weight[mask] * expert_output

        # Add shared expert contribution
        if self.use_shared_expert:
            shared_weight = torch.sigmoid(self.shared_gate(flat_x))
            shared_output = self.shared_expert(flat_x)
            output = output + shared_weight * shared_output

        output = output.view(batch_size, seq_len, d_model)

        # Compute auxiliary losses and metrics
        aux = self._compute_aux(router_probs, top_k_indices, num_tokens)

        return output, aux

    def _compute_aux(
        self,
        router_probs: torch.Tensor,
        top_k_indices: torch.Tensor,
        num_tokens: int,
    ) -> dict[str, torch.Tensor]:
        """Compute load balance loss and routing metrics."""
        # Load balance loss (Switch Transformer style)
        # f_i = fraction of tokens routed to expert i
        # P_i = mean router probability for expert i
        expert_mask = F.one_hot(top_k_indices, self.num_experts).float()
        expert_mask = expert_mask.sum(dim=1)  # [num_tokens, num_experts]

        tokens_per_expert = expert_mask.sum(dim=0)  # [num_experts]
        f = tokens_per_expert / num_tokens
        P = router_probs.mean(dim=0)  # [num_experts]

        load_balance_loss = self.num_experts * (f * P).sum()

        # Routing entropy
        entropy = -(router_probs * torch.log(router_probs + 1e-8)).sum(dim=-1).mean()

        # Expert utilization
        utilization = (tokens_per_expert > 0).float().mean()
        dead_experts = (tokens_per_expert == 0).sum()

        # Load imbalance (coefficient of variation)
        load_imbalance = tokens_per_expert.std() / (tokens_per_expert.mean() + 1e-8)

        return {
            "load_balance_loss": load_balance_loss,
            "routing_entropy": entropy,
            "expert_utilization": utilization,
            "dead_expert_count": dead_experts,
            "load_imbalance": load_imbalance,
            "tokens_per_expert": tokens_per_expert,
        }

    def get_router_metrics(self, x: torch.Tensor) -> RouterMetrics:
        """Get detailed router metrics for a given input."""
        flat_x = x.view(-1, self.d_model)
        router_logits = self.gate(flat_x)
        router_probs = F.softmax(router_logits, dim=-1)

        entropy = -(router_probs * torch.log(router_probs + 1e-8)).sum(dim=-1).mean()
        top_k_probs, top_k_indices = torch.topk(router_probs, self.top_k, dim=-1)

        expert_mask = F.one_hot(top_k_indices, self.num_experts).float().sum(dim=1)
        tokens_per_expert = expert_mask.sum(dim=0)
        utilization = (tokens_per_expert / tokens_per_expert.sum()).tolist()

        return RouterMetrics(
            routing_entropy=entropy.item(),
            expert_utilization=utilization,
            dead_expert_count=int((tokens_per_expert == 0).sum().item()),
            load_imbalance=(tokens_per_expert.std() / (tokens_per_expert.mean() + 1e-8)).item(),
            selected_k=self.top_k,
        )


class VectorizedMoEFFN(MoEFFN):
    """MoE FFN with vectorized top-k expert execution.

    This preserves the looped MoEFFN parameter layout and routing math while
    replacing per-expert Python dispatch with batched weight gathers.
    """

    def __init__(
        self,
        d_model: int,
        d_ff: int,
        num_experts: int = 8,
        top_k: int = 2,
        use_shared_expert: bool = True,
        dropout: float = 0.1,
        capacity_factor: float = 1.25,
    ):
        super().__init__(
            d_model=d_model,
            d_ff=d_ff,
            num_experts=num_experts,
            top_k=top_k,
            use_shared_expert=use_shared_expert,
            dropout=dropout,
            capacity_factor=capacity_factor,
        )
        self.expert_execution_mode = "FULLY_VECTORIZED"

    def forward(
        self, x: torch.Tensor, fixed_k: int | None = None
    ) -> tuple[torch.Tensor, dict[str, torch.Tensor]]:
        batch_size, seq_len, d_model = x.shape
        k = fixed_k if fixed_k is not None else self.top_k
        k = min(k, self.num_experts)

        flat_x = x.reshape(-1, d_model)
        num_tokens = flat_x.shape[0]

        router_logits = self.gate(flat_x)
        router_probs = F.softmax(router_logits, dim=-1)
        top_k_probs, top_k_indices = torch.topk(router_probs, k, dim=-1)
        top_k_probs = top_k_probs / (top_k_probs.sum(dim=-1, keepdim=True) + 1e-8)

        w1 = torch.stack([expert.w1.weight.transpose(0, 1) for expert in self.experts], dim=0)
        b1 = torch.stack([expert.w1.bias for expert in self.experts], dim=0)
        w2 = torch.stack([expert.w2.weight.transpose(0, 1) for expert in self.experts], dim=0)
        b2 = torch.stack([expert.w2.bias for expert in self.experts], dim=0)

        selected_w1 = w1[top_k_indices]
        selected_b1 = b1[top_k_indices]
        selected_w2 = w2[top_k_indices]
        selected_b2 = b2[top_k_indices]

        hidden = torch.einsum("nd,nkdf->nkf", flat_x, selected_w1) + selected_b1
        hidden = F.gelu(hidden)
        hidden = F.dropout(hidden, p=self.experts[0].dropout.p, training=self.training)
        expert_output = torch.einsum("nkf,nkfd->nkd", hidden, selected_w2) + selected_b2
        output = (top_k_probs.unsqueeze(-1) * expert_output).sum(dim=1)

        if self.use_shared_expert:
            shared_weight = torch.sigmoid(self.shared_gate(flat_x))
            shared_output = self.shared_expert(flat_x)
            output = output + shared_weight * shared_output

        aux = self._compute_aux(router_probs, top_k_indices, num_tokens)
        return output.reshape(batch_size, seq_len, d_model), aux
