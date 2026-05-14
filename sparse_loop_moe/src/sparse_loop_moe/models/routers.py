"""Phase 2-3: Router implementations.

- FixedTopKRouter: Standard fixed top-k expert selection
- AdaptiveWidthRouter: Dynamic expert width based on compute need
"""

from __future__ import annotations

import torch
import torch.nn as nn
import torch.nn.functional as F

from sparse_loop_moe.core.cognitive_state import CognitiveState


class FixedTopKRouter(nn.Module):
    """Fixed top-k router: always selects the same number of experts.

    Phase 2 baseline router.
    """

    def __init__(self, d_model: int, num_experts: int, top_k: int = 2):
        super().__init__()
        self.d_model = d_model
        self.num_experts = num_experts
        self.top_k = top_k
        self.gate = nn.Linear(d_model, num_experts, bias=False)

    def forward(
        self, x: torch.Tensor
    ) -> tuple[torch.Tensor, torch.Tensor, int]:
        """Route tokens to experts.

        Args:
            x: Input tensor [batch*seq, d_model]

        Returns:
            top_k_probs: Routing weights [num_tokens, k]
            top_k_indices: Expert indices [num_tokens, k]
            k: Number of experts selected
        """
        router_logits = self.gate(x)
        router_probs = F.softmax(router_logits, dim=-1)
        top_k_probs, top_k_indices = torch.topk(router_probs, self.top_k, dim=-1)
        top_k_probs = top_k_probs / (top_k_probs.sum(dim=-1, keepdim=True) + 1e-8)
        return top_k_probs, top_k_indices, self.top_k

    def get_entropy(self, x: torch.Tensor) -> torch.Tensor:
        """Compute routing entropy for the input."""
        router_logits = self.gate(x)
        router_probs = F.softmax(router_logits, dim=-1)
        return -(router_probs * torch.log(router_probs + 1e-8)).sum(dim=-1)


class AdaptiveWidthRouter(nn.Module):
    """Adaptive width router: dynamically selects expert count based on compute need.

    Phase 3 implementation. Computes:
        compute_need = alpha * uncertainty + beta * ambiguity + gamma * risk
                     + delta * missing_context + epsilon * abstraction_gap

    Then selects k based on thresholds:
        k=1 if compute_need < low_threshold
        k=2 if compute_need < medium_threshold
        k=4 otherwise (up to max_k=6 for larger experiments)
    """

    def __init__(
        self,
        d_model: int,
        num_experts: int,
        max_k: int = 4,
        low_threshold: float = 0.3,
        medium_threshold: float = 0.6,
        # Compute need weights
        alpha: float = 0.3,
        beta: float = 0.25,
        gamma: float = 0.2,
        delta: float = 0.15,
        epsilon: float = 0.1,
    ):
        super().__init__()
        self.d_model = d_model
        self.num_experts = num_experts
        self.max_k = max_k
        self.low_threshold = low_threshold
        self.medium_threshold = medium_threshold

        # Compute need weights
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.delta = delta
        self.epsilon = epsilon

        # Router gate
        self.gate = nn.Linear(d_model, num_experts, bias=False)

        # Learned compute need estimator (from hidden state)
        # Predicts: [uncertainty, ambiguity, risk, missing_context, abstraction_gap]
        self.compute_need_head = nn.Sequential(
            nn.Linear(d_model, d_model // 2),
            nn.GELU(),
            nn.Linear(d_model // 2, 5),
            nn.Sigmoid(),
        )

    def compute_adaptive_k(
        self,
        x: torch.Tensor,
        cognitive_state: CognitiveState | None = None,
    ) -> int:
        """Compute adaptive expert width.

        Uses either the cognitive state (if available) or the learned
        compute need estimator.
        """
        if cognitive_state is not None:
            compute_need = cognitive_state.compute_need(
                self.alpha, self.beta, self.gamma, self.delta, self.epsilon
            )
        else:
            # Use learned estimator from pooled hidden state
            pooled = x.mean(dim=0)  # [d_model]
            signals = self.compute_need_head(pooled)  # [5]
            compute_need = (
                self.alpha * signals[0]
                + self.beta * signals[1]
                + self.gamma * signals[2]
                + self.delta * signals[3]
                + self.epsilon * signals[4]
            ).item()

        # Threshold-based k selection
        if compute_need < self.low_threshold:
            k = 1
        elif compute_need < self.medium_threshold:
            k = 2
        else:
            k = self.max_k

        return min(k, self.num_experts)

    def forward(
        self,
        x: torch.Tensor,
        cognitive_state: CognitiveState | None = None,
        force_k: int | None = None,
    ) -> tuple[torch.Tensor, torch.Tensor, int]:
        """Route tokens to experts with adaptive width.

        Args:
            x: Input tensor [num_tokens, d_model]
            cognitive_state: Optional cognitive state for compute need
            force_k: Override adaptive k (for ablation)

        Returns:
            top_k_probs: Routing weights [num_tokens, k]
            top_k_indices: Expert indices [num_tokens, k]
            k: Number of experts selected
        """
        k = force_k if force_k is not None else self.compute_adaptive_k(x, cognitive_state)

        router_logits = self.gate(x)
        router_probs = F.softmax(router_logits, dim=-1)
        top_k_probs, top_k_indices = torch.topk(router_probs, k, dim=-1)
        top_k_probs = top_k_probs / (top_k_probs.sum(dim=-1, keepdim=True) + 1e-8)

        return top_k_probs, top_k_indices, k

    def get_entropy(self, x: torch.Tensor) -> torch.Tensor:
        """Compute routing entropy."""
        router_logits = self.gate(x)
        router_probs = F.softmax(router_logits, dim=-1)
        return -(router_probs * torch.log(router_probs + 1e-8)).sum(dim=-1)

    def get_compute_need_signals(self, x: torch.Tensor) -> dict[str, float]:
        """Get the individual compute need signals."""
        pooled = x.mean(dim=0)
        signals = self.compute_need_head(pooled).detach().cpu().tolist()
        return {
            "uncertainty": signals[0],
            "ambiguity": signals[1],
            "expected_risk": signals[2],
            "missing_context": signals[3],
            "abstraction_gap": signals[4],
        }
