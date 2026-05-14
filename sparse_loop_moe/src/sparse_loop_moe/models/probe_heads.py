"""Phase 5: Latent Probe Heads.

Lightweight probes that do not decode full answers. They feed the
controller and influence loop depth, expert width, branching,
validation, and halting decisions.
"""

from __future__ import annotations

import torch
import torch.nn as nn
import torch.nn.functional as F

from sparse_loop_moe.core.types import ProbeSignals


class ProbeHeads(nn.Module):
    """Latent probe heads for internal state evaluation.

    These probes predict:
    - failure_risk: probability of task failure
    - missing_context: probability that critical context is missing
    - coverage_gap: probability that expert coverage is insufficient
    - validation_fail_probability: probability that output would fail validation
    - route_confidence: confidence in current expert routing
    - hidden_constraint_probability: probability of undiscovered constraints
    - false_commitment_risk: risk of premature commitment to wrong path
    - representation_drift: how much the representation has drifted from stable
    - novelty_score: how novel/unfamiliar the current input is
    - memory_relevance: relevance of stored memory to current task
    """

    NUM_PROBES = 10

    def __init__(self, d_model: int, d_probe: int = 64):
        super().__init__()
        self.d_model = d_model

        # Shared feature extractor
        self.shared_encoder = nn.Sequential(
            nn.Linear(d_model, d_probe * 2),
            nn.GELU(),
            nn.Linear(d_probe * 2, d_probe),
            nn.GELU(),
        )

        # Individual probe heads (each outputs a scalar probability)
        self.failure_risk_head = nn.Linear(d_probe, 1)
        self.missing_context_head = nn.Linear(d_probe, 1)
        self.coverage_gap_head = nn.Linear(d_probe, 1)
        self.validation_fail_head = nn.Linear(d_probe, 1)
        self.route_confidence_head = nn.Linear(d_probe, 1)
        self.hidden_constraint_head = nn.Linear(d_probe, 1)
        self.false_commitment_head = nn.Linear(d_probe, 1)
        self.representation_drift_head = nn.Linear(d_probe, 1)
        self.novelty_head = nn.Linear(d_probe, 1)
        self.memory_relevance_head = nn.Linear(d_probe, 1)

    def forward(self, hidden_state: torch.Tensor) -> tuple[ProbeSignals, torch.Tensor]:
        """Compute probe signals from hidden state.

        Args:
            hidden_state: [batch, seq_len, d_model] or [batch, d_model]

        Returns:
            signals: ProbeSignals dataclass
            raw_tensor: Raw probe outputs as tensor [10]
        """
        # Pool if sequence dimension present
        if hidden_state.dim() == 3:
            pooled = hidden_state.mean(dim=1)  # [batch, d_model]
        else:
            pooled = hidden_state

        # Average over batch for aggregate signals
        if pooled.dim() == 2:
            pooled = pooled.mean(dim=0)  # [d_model]

        features = self.shared_encoder(pooled)  # [d_probe]

        # Compute each probe
        raw_outputs = torch.cat(
            [
                torch.sigmoid(self.failure_risk_head(features)),
                torch.sigmoid(self.missing_context_head(features)),
                torch.sigmoid(self.coverage_gap_head(features)),
                torch.sigmoid(self.validation_fail_head(features)),
                torch.sigmoid(self.route_confidence_head(features)),
                torch.sigmoid(self.hidden_constraint_head(features)),
                torch.sigmoid(self.false_commitment_head(features)),
                torch.sigmoid(self.representation_drift_head(features)),
                torch.sigmoid(self.novelty_head(features)),
                torch.sigmoid(self.memory_relevance_head(features)),
            ],
            dim=-1,
        )  # [10]

        signals = ProbeSignals.from_tensor(raw_outputs)
        return signals, raw_outputs

    def compute_probe_loss(
        self,
        predicted: torch.Tensor,
        targets: torch.Tensor,
    ) -> torch.Tensor:
        """Compute probe training loss (binary cross-entropy per probe).

        Args:
            predicted: [10] predicted probe values
            targets: [10] ground truth probe values (from task labels)
        """
        return F.binary_cross_entropy(predicted, targets)
