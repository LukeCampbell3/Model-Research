"""Repair playbooks and validation rules for PVR-EC-O failure observatory."""

from __future__ import annotations

from typing import Any

from .failure_registry import repair_playbooks


REPAIR_RESULT_LABELS = (
    "REPAIR_SOLVED",
    "REPAIR_PARTIAL",
    "REPAIR_HARMFUL",
    "REPAIR_OVERFIT_COLLAPSE_CASE",
    "REPAIR_NO_EFFECT",
    "REPAIR_REQUIRES_MORE_EVIDENCE",
)


def repair_candidates_for_modes(modes: list[str]) -> dict[str, dict[str, list[str]]]:
    playbooks = repair_playbooks()
    return {mode: playbooks.get(mode, playbooks["PVR_EC_FAILURE_UNKNOWN"]) for mode in sorted(set(modes))}


def validate_repair_result(result: dict[str, Any]) -> str:
    if result.get("forward_purity_regression") or result.get("Top2_executions", 0) or result.get("Top4_executions", 0):
        return "REPAIR_HARMFUL"
    if result.get("calibration_regression"):
        return "REPAIR_HARMFUL"
    if result.get("fixed_only_original_case") and result.get("new_collapse_created"):
        return "REPAIR_OVERFIT_COLLAPSE_CASE"
    if result.get("collapse_count_after", 1) == 0 and result.get("qpm_failed_after", 0) <= result.get("qpm_failed_before", 0):
        return "REPAIR_SOLVED"
    if result.get("collapse_count_after", 999) < result.get("collapse_count_before", 999):
        return "REPAIR_PARTIAL"
    if result.get("needs_more_evidence"):
        return "REPAIR_REQUIRES_MORE_EVIDENCE"
    return "REPAIR_NO_EFFECT"
