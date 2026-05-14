"""Verifier: validates outputs before commitment.

The verifier checks whether model outputs satisfy task constraints,
pass consistency checks, and meet quality thresholds before
allowing them to be committed as final answers.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable

import torch
import torch.nn as nn


@dataclass
class VerificationResult:
    """Result of a verification check."""

    passed: bool
    confidence: float
    failure_reasons: list[str]
    suggestions: list[str]


class Verifier(nn.Module):
    """Output verifier for the Sparse Loop-MoE system.

    Checks:
    - Constraint satisfaction
    - Internal consistency
    - Confidence thresholds
    - Format validity
    - Regression against known-good outputs
    """

    def __init__(self, d_model: int = 256, num_constraints: int = 8):
        super().__init__()
        self.d_model = d_model

        # Learned constraint checker
        self.constraint_head = nn.Sequential(
            nn.Linear(d_model, d_model // 2),
            nn.GELU(),
            nn.Linear(d_model // 2, num_constraints),
            nn.Sigmoid(),
        )

        # Consistency checker (compares input representation with output)
        self.consistency_head = nn.Sequential(
            nn.Linear(d_model * 2, d_model),
            nn.GELU(),
            nn.Linear(d_model, 1),
            nn.Sigmoid(),
        )

        # Confidence estimator
        self.confidence_head = nn.Sequential(
            nn.Linear(d_model, d_model // 4),
            nn.GELU(),
            nn.Linear(d_model // 4, 1),
            nn.Sigmoid(),
        )

        # Rule-based validators
        self._rule_validators: list[Callable] = []

    def forward(
        self,
        output_hidden: torch.Tensor,
        input_hidden: torch.Tensor | None = None,
        min_confidence: float = 0.5,
    ) -> VerificationResult:
        """Verify an output.

        Args:
            output_hidden: Hidden state of the output [d_model]
            input_hidden: Hidden state of the input [d_model] (for consistency)
            min_confidence: Minimum confidence threshold

        Returns:
            VerificationResult
        """
        if output_hidden.dim() > 1:
            output_hidden = output_hidden.mean(dim=0)
            if output_hidden.dim() > 1:
                output_hidden = output_hidden.mean(dim=0)

        failure_reasons = []
        suggestions = []

        # Check constraints
        constraint_scores = self.constraint_head(output_hidden)
        failed_constraints = (constraint_scores < 0.5).sum().item()
        if failed_constraints > 0:
            failure_reasons.append(
                f"{int(failed_constraints)} constraints not satisfied"
            )
            suggestions.append("Re-evaluate with additional expert coverage")

        # Check consistency
        consistency_score = 1.0
        if input_hidden is not None:
            if input_hidden.dim() > 1:
                input_hidden = input_hidden.mean(dim=0)
                if input_hidden.dim() > 1:
                    input_hidden = input_hidden.mean(dim=0)
            combined = torch.cat([input_hidden, output_hidden], dim=-1)
            consistency_score = self.consistency_head(combined).item()
            if consistency_score < 0.5:
                failure_reasons.append("Output inconsistent with input representation")
                suggestions.append("Run additional loop iterations")

        # Check confidence
        confidence = self.confidence_head(output_hidden).item()
        if confidence < min_confidence:
            failure_reasons.append(
                f"Confidence {confidence:.3f} below threshold {min_confidence}"
            )
            suggestions.append("Increase expert width or loop depth")

        # Run rule-based validators
        for validator in self._rule_validators:
            result = validator(output_hidden)
            if not result.get("passed", True):
                failure_reasons.append(result.get("reason", "Rule check failed"))
                if "suggestion" in result:
                    suggestions.append(result["suggestion"])

        passed = len(failure_reasons) == 0

        return VerificationResult(
            passed=passed,
            confidence=confidence,
            failure_reasons=failure_reasons,
            suggestions=suggestions,
        )

    def add_rule_validator(self, validator: Callable) -> None:
        """Add a rule-based validator function.

        Validator should accept a tensor and return a dict with:
        - passed: bool
        - reason: str (if failed)
        - suggestion: str (optional)
        """
        self._rule_validators.append(validator)

    def compute_verification_loss(
        self,
        predicted_pass: torch.Tensor,
        actual_pass: torch.Tensor,
    ) -> torch.Tensor:
        """Compute verification training loss."""
        return nn.functional.binary_cross_entropy(predicted_pass, actual_pass)
