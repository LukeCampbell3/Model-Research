"""Phase 4: Sparse Loop-MoE Block.

The core computational unit: combines adaptive expert routing with
bounded latent looping, probe heads, and reflection-based halting.

Forward pass:
1. Receive hidden state and cognitive state
2. Compute router logits
3. Compute uncertainty, ambiguity, risk, route regret
4. Select adaptive expert width
5. Route through experts and shared expert
6. Update hidden state
7. Run probe heads
8. Run reflection controller
9. Decide: halt / continue / add expert / switch / branch / validate / rollback
10. Return best hidden state, updated cognitive state, and loop stats
"""

from __future__ import annotations

import torch
import torch.nn as nn
import torch.nn.functional as F

from sparse_loop_moe.core.cognitive_state import CognitiveState
from sparse_loop_moe.core.cognitive_kernel import CognitiveKernel
from sparse_loop_moe.core.types import LoopStats, ProbeSignals, ReflectionAction
from sparse_loop_moe.models.moe_ffn import MoEFFN, Expert
from sparse_loop_moe.models.routers import AdaptiveWidthRouter, FixedTopKRouter
from sparse_loop_moe.models.probe_heads import ProbeHeads
from sparse_loop_moe.models.reflection_controller import ReflectionController


class SparseLoopMoEBlock(nn.Module):
    """Sparse Loop-MoE Block with bounded latent looping.

    Each block refines hidden state for a limited number of iterations.
    The loop:
    - updates hidden state
    - recomputes router signals
    - evaluates uncertainty/risk/probe signals
    - decides whether to continue, halt, branch, or rollback

    Never allows unbounded recursion. Uses:
    - max_loop_count
    - delta threshold
    - oscillation detector
    - compute budget
    - utility improvement threshold
    - best-state rollback
    """

    def __init__(
        self,
        d_model: int,
        d_ff: int,
        n_heads: int = 4,
        num_experts: int = 8,
        max_k: int = 4,
        max_loops: int = 8,
        delta_threshold: float = 0.01,
        utility_threshold: float = 0.005,
        use_adaptive_router: bool = True,
        use_probes: bool = True,
        use_reflection: bool = True,
        use_shared_expert: bool = True,
        dropout: float = 0.1,
    ):
        super().__init__()
        self.d_model = d_model
        self.max_loops = max_loops
        self.delta_threshold = delta_threshold
        self.utility_threshold = utility_threshold
        self.use_adaptive_router = use_adaptive_router
        self.use_probes = use_probes
        self.use_reflection = use_reflection

        # Self-attention for loop refinement
        self.attn_ln = nn.LayerNorm(d_model)
        self.self_attn = nn.MultiheadAttention(
            d_model, n_heads, dropout=dropout, batch_first=True
        )
        self.attn_dropout = nn.Dropout(dropout)

        # MoE FFN
        self.moe_ln = nn.LayerNorm(d_model)
        self.moe_ffn = MoEFFN(
            d_model=d_model,
            d_ff=d_ff,
            num_experts=num_experts,
            top_k=2,  # default, overridden by router
            use_shared_expert=use_shared_expert,
            dropout=dropout,
        )

        # Router
        if use_adaptive_router:
            self.router = AdaptiveWidthRouter(
                d_model=d_model, num_experts=num_experts, max_k=max_k
            )
        else:
            self.router = FixedTopKRouter(
                d_model=d_model, num_experts=num_experts, top_k=2
            )

        # Loop state projection (for iterative refinement)
        self.loop_proj = nn.Sequential(
            nn.Linear(d_model, d_model),
            nn.GELU(),
            nn.Linear(d_model, d_model),
        )
        self.loop_ln = nn.LayerNorm(d_model)
        self.loop_gate = nn.Sequential(
            nn.Linear(d_model * 2, d_model),
            nn.Sigmoid(),
        )

        # Probe heads
        if use_probes:
            self.probe_heads = ProbeHeads(d_model)

        # Reflection controller
        if use_reflection:
            self.reflection_controller = ReflectionController(d_model)

        # Halting head (learned halting probability)
        self.halt_head = nn.Sequential(
            nn.Linear(d_model, d_model // 4),
            nn.GELU(),
            nn.Linear(d_model // 4, 1),
            nn.Sigmoid(),
        )

    def forward(
        self,
        x: torch.Tensor,
        cognitive_state: CognitiveState | None = None,
        kernel: CognitiveKernel | None = None,
        causal_mask: torch.Tensor | None = None,
    ) -> tuple[torch.Tensor, CognitiveState, LoopStats, dict[str, torch.Tensor]]:
        """Forward pass with bounded latent looping.

        Args:
            x: Input hidden state [batch, seq_len, d_model]
            cognitive_state: Current cognitive state (created if None)
            kernel: Cognitive kernel for safety constraints
            causal_mask: Optional attention mask

        Returns:
            output: Refined hidden state [batch, seq_len, d_model]
            cognitive_state: Updated cognitive state
            loop_stats: Statistics about the loop execution
            aux_losses: Dictionary of auxiliary losses
        """
        if cognitive_state is None:
            cognitive_state = CognitiveState(max_loops=self.max_loops)
        if kernel is None:
            kernel = CognitiveKernel()

        batch_size, seq_len, d_model = x.shape
        device = x.device

        # Initialize loop tracking
        stats = LoopStats()
        aux_losses: dict[str, torch.Tensor] = {}
        all_balance_losses = []
        all_probe_outputs = []

        best_state = x.clone()
        best_score = float("-inf")
        prev_state = x.clone()
        deltas: list[float] = []

        for loop_idx in range(self.max_loops):
            stats.loops_used = loop_idx + 1
            cognitive_state.loop_count = loop_idx

            # --- Step 1: Self-attention refinement ---
            attn_input = self.attn_ln(x)
            attn_out, _ = self.self_attn(
                attn_input, attn_input, attn_input,
                attn_mask=causal_mask,
                need_weights=False,
            )
            x = x + self.attn_dropout(attn_out)

            # --- Step 2: Compute adaptive expert width ---
            flat_x = x.view(-1, d_model)
            if self.use_adaptive_router:
                top_k_probs, top_k_indices, k = self.router(
                    flat_x, cognitive_state=cognitive_state
                )
            else:
                top_k_probs, top_k_indices, k = self.router(flat_x)

            stats.experts_used_per_loop.append(k)

            # --- Step 3: MoE FFN with selected width ---
            moe_input = self.moe_ln(x)
            moe_out, moe_aux = self.moe_ffn(moe_input, fixed_k=k)
            x = x + moe_out
            all_balance_losses.append(moe_aux["load_balance_loss"])

            # --- Step 4: Loop refinement gate ---
            loop_refined = self.loop_proj(x)
            gate = self.loop_gate(torch.cat([x, loop_refined], dim=-1))
            x = self.loop_ln(gate * loop_refined + (1 - gate) * x)

            # --- Step 5: Compute delta (improvement) ---
            delta = (x - prev_state).norm().item() / (prev_state.norm().item() + 1e-8)
            deltas.append(delta)
            stats.delta_per_loop.append(delta)

            # --- Step 6: Run probe heads ---
            probe_signals = ProbeSignals()
            if self.use_probes:
                probe_signals, probe_raw = self.probe_heads(x)
                stats.probe_signals_per_loop.append(probe_signals)
                all_probe_outputs.append(probe_raw)

                # Update cognitive state from probes
                cognitive_state.uncertainty = probe_signals.failure_risk
                cognitive_state.missing_context_score = probe_signals.missing_context
                cognitive_state.route_regret = 1.0 - probe_signals.route_confidence

            # --- Step 7: Compute state score ---
            # Score = route_confidence - failure_risk - false_commitment_risk
            state_score = (
                probe_signals.route_confidence
                - probe_signals.failure_risk
                - probe_signals.false_commitment_risk
            )
            stats.utility_per_loop.append(state_score)

            if state_score > best_score:
                best_score = state_score
                best_state = x.clone()
                stats.best_state_loop = loop_idx

            # --- Step 8: Halting decision ---
            halt_prob = self.halt_head(x.mean(dim=(0, 1))).item()

            # --- Step 9: Reflection controller ---
            action = ReflectionAction.CONTINUE
            utility = 1.0

            if self.use_reflection:
                action, halt_prob_refl, utility, reflection_scores = (
                    self.reflection_controller(
                        hidden_state=x,
                        probe_signals=probe_signals,
                        cognitive_state=cognitive_state,
                        loop_count=loop_idx,
                        max_loops=self.max_loops,
                        recent_deltas=deltas,
                    )
                )
                stats.actions_taken.append(action)

            # --- Step 10: Anti-spinlock checks ---
            # Check oscillation
            if kernel.check_oscillation(deltas):
                stats.oscillation_detected = True
                stats.halted_early = True
                stats.halt_reason = "oscillation_detected"
                x = best_state
                break

            # Check delta threshold
            if delta < self.delta_threshold and loop_idx > 0:
                stats.halted_early = True
                stats.halt_reason = "delta_below_threshold"
                break

            # Check utility threshold
            if utility < self.utility_threshold and loop_idx > 0:
                stats.halted_early = True
                stats.halt_reason = "utility_below_threshold"
                break

            # Check kernel loop limit
            if not kernel.validate_loop_count(loop_idx + 1):
                stats.halted_early = True
                stats.halt_reason = "kernel_loop_limit"
                stats.compute_budget_exhausted = True
                break

            # Process reflection action
            if action == ReflectionAction.HALT:
                stats.halted_early = True
                stats.halt_reason = "reflection_halt"
                break
            elif action == ReflectionAction.ROLLBACK:
                x = best_state.clone()
                stats.rollback_count += 1
                if stats.rollback_count >= kernel.constraints.max_consecutive_rollbacks:
                    stats.halted_early = True
                    stats.halt_reason = "max_rollbacks"
                    break

            prev_state = x.clone()

        # Aggregate auxiliary losses
        if all_balance_losses:
            aux_losses["load_balance_loss"] = torch.stack(all_balance_losses).mean()
        if all_probe_outputs:
            aux_losses["probe_outputs"] = torch.stack(all_probe_outputs)

        # Use best state if current is worse
        final_score = (
            probe_signals.route_confidence
            - probe_signals.failure_risk
            - probe_signals.false_commitment_risk
        )
        if final_score < best_score:
            x = best_state

        return x, cognitive_state, stats, aux_losses
