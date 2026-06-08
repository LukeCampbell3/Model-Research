import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "sparse_loop_moe" / "src"))
sys.path.insert(0, str(ROOT))

from sparse_loop_moe.models.pvr_ec.failure_attribution import attribution_for_event
from sparse_loop_moe.models.pvr_ec.failure_observatory import (
    FAILURE_EVENT_SCHEMA,
    blank_failure_event,
    events_from_rows,
    finalize_event,
    observatory_gate_payload,
)
from sparse_loop_moe.models.pvr_ec.failure_registry import (
    FAILURE_MODE_IDS,
    REQUIRED_FAILURE_MODE_FIELDS,
    failure_mode_registry,
)
from sparse_loop_moe.models.pvr_ec.failure_replay import failure_case_payload
from sparse_loop_moe.models.pvr_ec.failure_repairs import validate_repair_result
from evaluation.run_algorithmic_benchmarks import write_failure_observatory_reports


def test_failure_registry_has_required_modes_and_fields():
    registry = failure_mode_registry()
    assert set(FAILURE_MODE_IDS) <= set(registry)
    for mode in FAILURE_MODE_IDS:
        assert set(REQUIRED_FAILURE_MODE_FIELDS) <= set(registry[mode])
        assert registry[mode]["promotion_impact"]
        assert registry[mode]["research_impact"]


def test_failure_event_schema_contains_required_observability_fields():
    required = {
        "loss_gap_vs_fixed",
        "candidate_calibration",
        "delta_correct_minus_top_wrong",
        "owners_per_token",
        "Top2_executions",
        "runtime_purity_passed",
        "tokenization_type",
        "owner_entropy_by_length",
        "failure_mode_by_length",
    }
    assert required <= set(FAILURE_EVENT_SCHEMA)


def test_known_collapse_classification_prefers_owner_prototype_collapse():
    event = finalize_event(blank_failure_event(
        seed=123,
        family="clrs_style",
        model="pvr_ec_ownership_top1_final_candidate_v1",
        candidate_config="final_candidate_v1",
        fixed_loss=0.4,
        candidate_loss=0.7,
        loss_gap_vs_fixed=0.3,
        fixed_accuracy=0.3,
        candidate_accuracy=0.15,
        accuracy_gap_vs_fixed=-0.15,
        candidate_calibration=0.14,
        calibration_gap=0.04,
        owner_entropy=0.0,
        prototype_entropy=0.0,
        residual_help_rate=0.01,
        expert_delta_contribution_pct=0.0,
    ))
    assert event["failure_mode_primary"] == "PVR_EC_FAILURE_OWNER_PROTOTYPE_COLLAPSE"
    assert event["collapse_detected"] is True
    assert event["failure_is_explained"] is True


def test_qpm_runtime_rows_create_shape_regression_without_top2():
    rows = [
        {
            "model": "fixed_moe_vectorized",
            "batch_size": 16,
            "seq_len": 64,
            "quality_per_ms": 0.20,
            "latency_p50": 10.0,
            "latency_p95": 11.0,
            "loss": 0.5,
            "accuracy": 0.2,
        },
        {
            "model": "pvr_ec_ownership_top1_final_candidate_v1",
            "batch_size": 16,
            "seq_len": 64,
            "quality_per_ms": 0.10,
            "latency_p50": 10.0,
            "latency_p95": 25.0,
            "owner_count_per_token": 1.0,
            "Top2_executions": 0.0,
            "Top4_executions": 0.0,
            "loss": 0.6,
            "accuracy": 0.2,
        },
    ]
    event = events_from_rows(rows, run_id="qpm")[0]
    assert event["shape"] == "b16-s64"
    assert event["failure_mode_primary"] == "PVR_EC_FAILURE_QPM_SHAPE_REGRESSION"
    assert event["owners_per_token"] == 1.0
    assert event["Top2_executions"] == 0.0


def test_replay_payload_scores_known_failure_repeatability():
    event = finalize_event(blank_failure_event(
        seed=123,
        family="clrs_style",
        model="pvr_ec_ownership_top1_final_candidate_v1",
        candidate_config="final_candidate_v1",
        owner_entropy=0.0,
        prototype_entropy=0.0,
        loss_gap_vs_fixed=0.2,
    ))
    payload = failure_case_payload([event], "seed123_clrs_style_final_candidate_v1")
    assert payload["repeatability_rate"] == 1.0
    assert payload["same_primary_mode_rate"] == 1.0
    assert "PVR_EC_FAILURE_OWNER_PROTOTYPE_COLLAPSE" in payload["repair_candidate_recommendation"]


def test_repair_validation_blocks_harmful_or_overfit_repairs():
    assert validate_repair_result({"Top2_executions": 1}) == "REPAIR_HARMFUL"
    assert validate_repair_result({"calibration_regression": True}) == "REPAIR_HARMFUL"
    assert validate_repair_result({"fixed_only_original_case": True, "new_collapse_created": True}) == "REPAIR_OVERFIT_COLLAPSE_CASE"
    assert validate_repair_result({"collapse_count_after": 0, "qpm_failed_before": 1, "qpm_failed_after": 0}) == "REPAIR_SOLVED"


def test_observatory_reports_and_nlp_bridge_plan(tmp_path):
    event = finalize_event(blank_failure_event(
        model="pvr_ec_ownership_top1_final_candidate_v1",
        loss_gap_vs_fixed=0.2,
        owner_entropy=0.0,
        prototype_entropy=0.0,
    ))
    summary = write_failure_observatory_reports(tmp_path, [event])
    assert summary["gate"]["deployment_verdict"] == "PVR_EC_DEPLOYMENT_STILL_BLOCKED"
    assert (tmp_path / "failure_observatory_events.csv").exists()
    assert (tmp_path / "failure_mode_registry_report.json").exists()
    bridge = json.loads((tmp_path / "pvr_ec_nlp_observatory_bridge_plan.json").read_text())
    assert "token_accuracy" in bridge["required_nlp_observatory_fields"]
    assert observatory_gate_payload([event])["all_failures_classified"] is True


def test_runtime_purity_attribution_blocks_research():
    attribution = attribution_for_event(blank_failure_event(
        owners_per_token=2.0,
        Top2_executions=1.0,
    ))
    assert attribution["primary_failure_mode"] == "PVR_EC_FAILURE_RUNTIME_PATH_POLLUTION"
    assert attribution["research_expansion_allowed"] is False
