"""Full Sparse Loop-MoE Model.

Assembles the complete architecture: embedding, multiple Sparse Loop-MoE blocks,
output head, and optional verifier.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field

import torch
import torch.nn as nn
import torch.nn.functional as F

from sparse_loop_moe.core.cognitive_state import CognitiveState
from sparse_loop_moe.core.cognitive_kernel import CognitiveKernel, KernelConstraints
from sparse_loop_moe.core.types import LoopStats
from sparse_loop_moe.models.sparse_loop_moe_block import SparseLoopMoEBlock


@dataclass
class SparseLoopMoEConfig:
    """Configuration for the full Sparse Loop-MoE model."""

    # Embedding
    vocab_size: int = 512
    d_model: int = 256
    max_seq_len: int = 256

    # Architecture
    n_layers: int = 4
    n_heads: int = 4
    d_ff: int = 512
    num_experts: int = 8
    max_k: int = 4
    max_loops: int = 8

    # Features (for ablation control)
    use_adaptive_router: bool = True
    use_probes: bool = True
    use_reflection: bool = True
    use_shared_expert: bool = True
    use_loops: bool = True
    vectorized_moe: bool = False

    # Thresholds
    delta_threshold: float = 0.01
    utility_threshold: float = 0.005

    # Regularization
    dropout: float = 0.1
    tie_weights: bool = True

    # Kernel constraints
    kernel_constraints: KernelConstraints = field(default_factory=KernelConstraints)


class SparseLoopMoEModel(nn.Module):
    """Full Sparse Loop-MoE model.

    Supports multiple configurations for ablation studies:
    - Dense baseline (no MoE, no loops)
    - Fixed MoE (fixed top-k, no loops)
    - Adaptive MoE (adaptive width, no loops)
    - Looped MoE (fixed width, with loops)
    - Full Sparse Loop-MoE (adaptive width, loops, probes, reflection)
    """

    def __init__(self, config: SparseLoopMoEConfig | None = None):
        super().__init__()
        self.config = config or SparseLoopMoEConfig()
        c = self.config

        # Cognitive kernel (immutable)
        self.kernel = CognitiveKernel(c.kernel_constraints)

        # Embeddings
        self.token_emb = nn.Embedding(c.vocab_size, c.d_model)
        self.pos_emb = nn.Embedding(c.max_seq_len, c.d_model)
        self.dropout = nn.Dropout(c.dropout)

        # Sparse Loop-MoE blocks
        self.blocks = nn.ModuleList(
            [
                SparseLoopMoEBlock(
                    d_model=c.d_model,
                    d_ff=c.d_ff,
                    n_heads=c.n_heads,
                    num_experts=c.num_experts,
                    max_k=c.max_k,
                    max_loops=c.max_loops if c.use_loops else 1,
                    delta_threshold=c.delta_threshold,
                    utility_threshold=c.utility_threshold,
                    use_adaptive_router=c.use_adaptive_router,
                    use_probes=c.use_probes,
                    use_reflection=c.use_reflection,
                    use_shared_expert=c.use_shared_expert,
                    vectorized_moe=c.vectorized_moe,
                    dropout=c.dropout,
                )
                for _ in range(c.n_layers)
            ]
        )

        # Output
        self.ln_f = nn.LayerNorm(c.d_model)
        self.head = nn.Linear(c.d_model, c.vocab_size, bias=False)

        if c.tie_weights:
            self.head.weight = self.token_emb.weight

        self._init_weights()

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
        targets: torch.Tensor | None = None,
        cognitive_state: CognitiveState | None = None,
    ) -> dict[str, torch.Tensor | list[LoopStats] | CognitiveState]:
        """Forward pass through the full model.

        Args:
            input_ids: Token IDs [batch, seq_len]
            targets: Target token IDs [batch, seq_len] (for loss)
            cognitive_state: Optional initial cognitive state

        Returns:
            Dictionary with:
            - logits: Output logits [batch, seq_len, vocab_size]
            - loss: Task loss (if targets provided)
            - hidden_states: Final hidden states
            - loop_stats: List of LoopStats per block
            - cognitive_state: Final cognitive state
            - aux_losses: Aggregated auxiliary losses
        """
        batch_size, seq_len = input_ids.shape
        device = input_ids.device

        if cognitive_state is None:
            cognitive_state = CognitiveState(max_loops=self.config.max_loops)

        # Embeddings
        positions = torch.arange(seq_len, device=device).unsqueeze(0)
        x = self.dropout(self.token_emb(input_ids) + self.pos_emb(positions))

        # Process through Sparse Loop-MoE blocks
        all_loop_stats: list[LoopStats] = []
        all_aux_losses: dict[str, list[torch.Tensor]] = {}

        for block in self.blocks:
            x, cognitive_state, loop_stats, aux = block(
                x, cognitive_state=cognitive_state, kernel=self.kernel
            )
            all_loop_stats.append(loop_stats)

            for key, val in aux.items():
                if key not in all_aux_losses:
                    all_aux_losses[key] = []
                all_aux_losses[key].append(val)

        # Output
        x = self.ln_f(x)
        logits = self.head(x)

        result: dict = {
            "logits": logits,
            "hidden_states": x,
            "loop_stats": all_loop_stats,
            "cognitive_state": cognitive_state,
        }

        # Aggregate aux losses
        aggregated_aux = {}
        for key, vals in all_aux_losses.items():
            if key == "probe_outputs":
                continue  # Don't average probe outputs
            aggregated_aux[key] = torch.stack(vals).mean()
        result["aux_losses"] = aggregated_aux

        # Task loss
        if targets is not None:
            loss = F.cross_entropy(
                logits.view(-1, self.config.vocab_size), targets.view(-1)
            )
            result["loss"] = loss

        return result

    def count_parameters(self) -> int:
        return sum(p.numel() for p in self.parameters() if p.requires_grad)

    def count_active_parameters(self, loop_stats: list[LoopStats]) -> int:
        """Estimate active parameters based on actual routing decisions."""
        # Base parameters (embeddings, layernorms, output head)
        base_params = (
            self.token_emb.weight.numel()
            + self.pos_emb.weight.numel()
            + self.ln_f.weight.numel()
            + self.ln_f.bias.numel()
            + self.head.weight.numel()
        )

        # Per-block active params depend on experts used
        expert_params = self.config.d_model * self.config.d_ff * 2  # w1 + w2
        active_expert_params = 0
        for stats in loop_stats:
            for k in stats.experts_used_per_loop:
                active_expert_params += k * expert_params * stats.loops_used

        return base_params + active_expert_params

    def get_compute_summary(
        self, loop_stats: list[LoopStats]
    ) -> dict[str, float]:
        """Get a summary of compute usage."""
        total_loops = sum(s.loops_used for s in loop_stats)
        avg_loops = total_loops / max(len(loop_stats), 1)
        avg_experts = (
            sum(sum(s.experts_used_per_loop) for s in loop_stats)
            / max(total_loops, 1)
        )
        halt_rate = sum(1 for s in loop_stats if s.halted_early) / max(len(loop_stats), 1)
        rollback_rate = sum(s.rollback_count for s in loop_stats) / max(total_loops, 1)
        oscillation_rate = sum(1 for s in loop_stats if s.oscillation_detected) / max(
            len(loop_stats), 1
        )

        return {
            "total_loops": total_loops,
            "avg_loops_per_block": avg_loops,
            "avg_experts_per_step": avg_experts,
            "halt_rate": halt_rate,
            "rollback_rate": rollback_rate,
            "oscillation_rate": oscillation_rate,
        }
