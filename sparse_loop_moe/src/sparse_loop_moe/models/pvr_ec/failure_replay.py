"""Known failure replay helpers for PVR-EC-O observatory artifacts."""

from __future__ import annotations

from collections import Counter
from typing import Any

from .failure_repairs import repair_candidates_for_modes


KNOWN_FAILURE_CASES: dict[str, dict[str, Any]] = {
    "seed123_clrs_style_final_candidate_v1": {
        "seed": 123,
        "family": "clrs_style",
        "candidate_config": "final_candidate_v1",
        "expected_primary_modes": [
            "PVR_EC_FAILURE_OWNER_PROTOTYPE_COLLAPSE",
            "PVR_EC_FAILURE_CALIBRATION_COLLAPSE",
            "PVR_EC_FAILURE_SPARSE_RESIDUAL_UNHELPFUL",
        ],
    },
    "seed123_clrs_style_final_candidate_v1_1": {
        "seed": 123,
        "family": "clrs_style",
        "candidate_config": "final_candidate_v1_1",
        "expected_primary_modes": [
            "PVR_EC_FAILURE_OWNER_PROTOTYPE_COLLAPSE",
            "PVR_EC_FAILURE_CALIBRATION_COLLAPSE",
            "PVR_EC_FAILURE_SPARSE_RESIDUAL_UNHELPFUL",
        ],
    },
    "seed777_listops_final_candidate_v1": {
        "seed": 777,
        "family": "listops",
        "candidate_config": "final_candidate_v1",
        "expected_primary_modes": [
            "PVR_EC_FAILURE_DATA_SPLIT_DIFFICULTY",
            "PVR_EC_FAILURE_OWNER_PROTOTYPE_COLLAPSE",
            "PVR_EC_FAILURE_SPARSE_RESIDUAL_UNHELPFUL",
        ],
    },
    "seed777_listops_final_candidate_v1_1": {
        "seed": 777,
        "family": "listops",
        "candidate_config": "final_candidate_v1_1",
        "expected_primary_modes": [
            "PVR_EC_FAILURE_DATA_SPLIT_DIFFICULTY",
            "PVR_EC_FAILURE_OWNER_PROTOTYPE_COLLAPSE",
            "PVR_EC_FAILURE_SPARSE_RESIDUAL_UNHELPFUL",
        ],
    },
    "shape_b16_s64_qpm": {
        "shape": "b16-s64",
        "candidate_config": "final_candidate_v1",
        "expected_primary_modes": ["PVR_EC_FAILURE_QPM_SHAPE_REGRESSION"],
    },
}


def _csv_list(value: str | None) -> list[str]:
    if not value:
        return []
    return [item.strip() for item in value.split(",") if item.strip()]


def _matches_case(event: dict[str, Any], case: dict[str, Any]) -> bool:
    for field in ["seed", "shape"]:
        if case.get(field) not in {"", None} and str(event.get(field)) != str(case[field]):
            return False
    candidate = case.get("candidate_config")
    if candidate not in {"", None}:
        event_candidate = str(event.get("candidate_config") or "")
        event_model = str(event.get("model") or "")
        if event_candidate != str(candidate) and str(candidate) not in event_model:
            return False
    family = case.get("family")
    if family:
        aliases = {str(family), str(family).replace("_style", "")}
        if str(event.get("family")) not in aliases:
            return False
    return True


def failure_case_payload(events: list[dict[str, Any]], case_list: str | None = None) -> dict[str, Any]:
    requested = _csv_list(case_list) or list(KNOWN_FAILURE_CASES)
    rows = []
    mode_counter: Counter[str] = Counter()
    repeatable = 0
    same_primary = 0
    same_secondary = 0
    metric_deltas = []

    for case_id in requested:
        case = KNOWN_FAILURE_CASES.get(case_id, {"id": case_id})
        matched = [event for event in events if _matches_case(event, case)]
        repeated = bool(matched)
        repeatable += int(repeated)
        expected = set(case.get("expected_primary_modes") or [])
        observed_modes = {
            str(event.get("failure_mode_primary"))
            for event in matched
            if event.get("failure_mode_primary")
        }
        observed_secondaries = {
            str(mode)
            for event in matched
            for mode in (event.get("failure_mode_secondary") or [])
        }
        mode_counter.update(observed_modes)
        primary_match = bool(expected & observed_modes) if expected else repeated
        secondary_match = bool(expected & observed_secondaries) if expected else False
        same_primary += int(primary_match)
        same_secondary += int(secondary_match)
        for event in matched:
            metric_deltas.append({
                "case_id": case_id,
                "loss_gap_vs_fixed": event.get("loss_gap_vs_fixed"),
                "accuracy_gap_vs_fixed": event.get("accuracy_gap_vs_fixed"),
                "qpm_gap": event.get("qpm_gap"),
                "calibration_gap": event.get("calibration_gap"),
            })
        rows.append({
            "case_id": case_id,
            "case": case,
            "repeatable": repeated,
            "matched_event_count": len(matched),
            "expected_failure_modes": sorted(expected),
            "observed_primary_modes": sorted(observed_modes),
            "observed_secondary_modes": sorted(observed_secondaries),
            "same_primary_mode": primary_match,
            "same_secondary_mode": secondary_match,
        })

    modes = sorted(mode_counter) or sorted({str(event.get("failure_mode_primary")) for event in events if event.get("failure_mode_primary")})
    return {
        "status": "PVR_EC_FAILURE_CASES_REPLAYED" if events else "PARTIAL_PVR_EC_FAILURE_OBSERVATORY",
        "case_count": len(requested),
        "matched_case_count": repeatable,
        "repeatability_rate": repeatable / max(len(requested), 1),
        "same_failure_mode_rate": (same_primary + same_secondary) / max(2 * len(requested), 1),
        "same_primary_mode_rate": same_primary / max(len(requested), 1),
        "same_secondary_mode_rate": same_secondary / max(len(requested), 1),
        "metric_delta_vs_original": metric_deltas,
        "repair_candidate_recommendation": repair_candidates_for_modes(modes),
        "cases": rows,
    }
