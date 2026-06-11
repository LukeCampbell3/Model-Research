"""PromptInjectionBoundary: sanitize inputs at the expert interface.

Detects and neutralizes prompt injection attempts before they reach experts.
This is a defense layer — it does not guarantee complete safety but raises
the cost of adversarial inputs.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any
import re


@dataclass
class SanitizationResult:
    """Result of input sanitization."""
    original_length: int
    sanitized_length: int
    injection_detected: bool
    injection_types: list[str] = field(default_factory=list)
    sanitized_text: str = ""
    risk_score: float = 0.0  # 0=safe, 1=highly suspicious


# Patterns that suggest prompt injection
_INJECTION_PATTERNS = [
    (r"ignore\s+.{0,30}(instructions?|rules?|context)", "instruction_override"),
    (r"you\s+are\s+now\s+a?\s*", "role_hijack"),
    (r"system\s*:\s*", "system_prompt_injection"),
    (r"<\|?(system|im_start|endoftext)\|?>", "control_token_injection"),
    (r"forget\s+(everything|all|what)", "memory_wipe"),
    (r"do\s+not\s+follow\s+(any|the|your)", "constraint_bypass"),
    (r"pretend\s+(you|that|to)\s+(are|be|have)", "persona_injection"),
    (r"\]\]>\s*<", "xml_escape_injection"),
]


class PromptInjectionBoundary:
    """Sanitize and score inputs before they reach expert execution.

    This boundary sits between the process descriptor and the expert.
    It does NOT modify canonical state — it only filters the expert's input.
    """

    def __init__(self, max_input_length: int = 50000, risk_threshold: float = 0.5):
        self._max_length = max_input_length
        self._risk_threshold = risk_threshold
        self._patterns = [(re.compile(p, re.IGNORECASE), name) for p, name in _INJECTION_PATTERNS]

    def sanitize(self, text: str) -> SanitizationResult:
        """Sanitize input text and return result with risk assessment."""
        original_length = len(text)
        injection_types: list[str] = []
        risk_score = 0.0

        # Length check
        if len(text) > self._max_length:
            text = text[:self._max_length]
            risk_score += 0.1

        # Pattern matching
        for pattern, injection_type in self._patterns:
            if pattern.search(text):
                injection_types.append(injection_type)
                risk_score += 0.2

        # Excessive special characters
        special_ratio = sum(1 for c in text if not c.isalnum() and not c.isspace()) / max(len(text), 1)
        if special_ratio > 0.3:
            risk_score += 0.15
            injection_types.append("excessive_special_chars")

        # Control characters
        control_chars = sum(1 for c in text if ord(c) < 32 and c not in '\n\r\t')
        if control_chars > 0:
            risk_score += 0.1 * min(control_chars, 5)
            injection_types.append("control_characters")

        # Clamp risk
        risk_score = min(risk_score, 1.0)
        injection_detected = risk_score >= self._risk_threshold

        # Sanitize: strip control chars, truncate
        sanitized = ''.join(c for c in text if ord(c) >= 32 or c in '\n\r\t')

        return SanitizationResult(
            original_length=original_length,
            sanitized_length=len(sanitized),
            injection_detected=injection_detected,
            injection_types=injection_types,
            sanitized_text=sanitized,
            risk_score=risk_score,
        )

    def is_safe(self, text: str) -> bool:
        """Quick check: is this input safe to pass to an expert?"""
        result = self.sanitize(text)
        return not result.injection_detected
