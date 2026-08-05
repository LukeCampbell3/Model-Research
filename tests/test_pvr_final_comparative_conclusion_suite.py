import json
from pathlib import Path

import pytest

from benchmark.analysis.pvr_final_comparative_conclusion import (
    ALWAYS_BLOCKED_CLAIMS,
    build_report,
    evaluate_300m_scaffold,
    is_probe_only,
)


@pytest.fixture(scope="session")
def generated_final_report(tmp_path_factory):
    out = tmp_path_factory.mktemp("pvr_final_suite")
    return build_report(out, seeds=["42", "123"], use_existing=True, allow_partial=True)


def _row(loss, *, teacher_loaded=False, top1=True, steps=1100):
    return {
        "lm_loss": loss,
        "eval_token_count": 50176,
        "heldout_eval_token_count": 12544,
        "teacher_checkpoint_loaded": teacher_loaded,
        "optimizer_steps": steps,
        "owners_per_token": 1.0 if top1 else 2.0,
        "top2_execution_count": 0 if top1 else 1,
        "top4_execution_count": 0,
        "runtime_dynamic_k_count": 0,
        "runtime_expert_choice_count": 0,
        "production_map_mutated": False,
    }


def _manifest(tokens=1126400, steps=1100):
    return {
        "optimizer_steps": steps,
        "target_steps": steps,
        "training_tokens_seen": tokens,
        "tokens_seen": tokens,
        "target_training_tokens": tokens,
        "effective_batch_tokens": 1024,
        "eval_window_count": 11,
    }


def _base_300m_report(tmp_path, *, candidate_loss=4.6, no_head_loss=4.8, teacher_loaded=True, top1=True, tokens=1126400, steps=1100):
    checkpoint = tmp_path / "teacher.pt"
    checkpoint.write_bytes(b"teacher")
    rows = {
        "pvr_full_scratch_300m_matched": _row(5.0, steps=steps),
        "pvr_shared_warmup_no_geometry_head_300m_matched": _row(no_head_loss, steps=steps),
        "pvr_self_instilled_uniformity_geometry_head_v1_300m_matched": _row(candidate_loss, teacher_loaded=False, top1=top1, steps=steps),
        "pvr_descriptor_curriculum_head_300m_matched": _row(4.7, teacher_loaded=False, steps=steps),
        "pvr_descriptor_plus_uniformity_head_300m_matched": _row(4.65, teacher_loaded=False, steps=steps),
        "pvr_teacher_ean_300m_matched": {**_row(4.0, teacher_loaded=True, steps=steps), "checkpoint_path": str(checkpoint)},
    }
    return {
        "rows": rows,
        "training_manifests": {key: _manifest(tokens=tokens, steps=steps) for key in rows},
        "routing_health": {"all_routing_health_gates_pass": True},
        "geometry_health": {"all_health_gates_pass": True},
        "init_report": {
            "teacher_checkpoint_loaded": teacher_loaded,
            "copy_scope": "embeddings_attention_norms",
            "copied_count": 3,
            "skipped_count": 2,
            "copied": ["token_emb.weight", "attn.0.self_attn.in_proj_weight", "attn.0.norm1.weight"],
        },
    }


def _claim(branch, name):
    return next(row for row in branch["claims"] if row["claim"] == name)


def test_report_json_schema_contains_required_sections(generated_final_report):
    path = Path(generated_final_report["json_report_path"])
    data = json.loads(path.read_text(encoding="utf-8"))
    for key in ["claim_ledger", "experiments", "figures", "tables", "final_conclusion"]:
        assert key in data


def test_refuses_narrows_ean_gap_if_teacher_checkpoint_did_not_load(tmp_path):
    report = _base_300m_report(tmp_path, teacher_loaded=False, candidate_loss=4.2)
    branch = evaluate_300m_scaffold(report, root=tmp_path, source_path="synthetic.json")
    claim = _claim(branch, "PVR_SELF_INSTILLED_EAN_GEOMETRY_HEAD_NARROWS_TEACHER_GAP")
    assert claim["status"] == "blocked"
    assert claim["status_detail"] == "blocked_invalid_teacher_reference"
    assert "PVR_SELF_INSTILLED_EAN_GEOMETRY_HEAD_NARROWS_TEACHER_GAP" not in branch["supported_labels"]


def test_refuses_support_labels_when_token_budgets_do_not_match(tmp_path):
    report = _base_300m_report(tmp_path, candidate_loss=4.6)
    report["training_manifests"]["pvr_descriptor_plus_uniformity_head_300m_matched"] = _manifest(tokens=1000)
    branch = evaluate_300m_scaffold(report, root=tmp_path, source_path="synthetic.json")
    assert branch["token_budget_validation"]["complete"] is False
    assert "PVR_SELF_INSTILLED_EAN_GEOMETRY_HEAD_SUPPORTED" not in branch["supported_labels"]


def test_marks_100_step_probes_probe_only_and_never_capability_supported(tmp_path):
    report = _base_300m_report(tmp_path, candidate_loss=4.6, steps=100)
    branch = evaluate_300m_scaffold(report, root=tmp_path, source_path="synthetic_probe.json")
    candidate = next(row for row in branch["variants"] if row["variant"] == "pvr_self_instilled_uniformity_geometry_head_v1_300m_matched")
    assert is_probe_only(report["rows"]["pvr_self_instilled_uniformity_geometry_head_v1_300m_matched"], "synthetic_probe.json")
    assert candidate["probe_only"] is True
    assert candidate["capability_evidence"] is False
    assert "PVR_SELF_INSTILLED_EAN_GEOMETRY_HEAD_SUPPORTED" not in branch["supported_labels"]


def test_requires_geometry_candidate_to_beat_no_head_warmup_before_support(tmp_path):
    report = _base_300m_report(tmp_path, candidate_loss=4.9, no_head_loss=4.8)
    branch = evaluate_300m_scaffold(report, root=tmp_path, source_path="synthetic.json")
    assert branch["support_conditions"]["beats_no_head_warmup"] is False
    assert _claim(branch, "PVR_SELF_INSTILLED_EAN_GEOMETRY_HEAD_SUPPORTED")["status"] == "blocked"


def test_preserves_branch_separation(generated_final_report):
    experiments = generated_final_report["experiments"]
    assert set(experiments) >= {"descriptor_deployment", "scaffold_300m", "frontier_700m", "official_benchmark"}
    descriptor = experiments["descriptor_deployment"]
    assert descriptor["deployment_supported"] is True
    assert experiments["official_benchmark"]["status"] == "blocked"
    assert generated_final_report["final_conclusion"]["claim_outcomes"]["PVR_TEACHER_INDEPENDENCE_SUPPORTED"].startswith("blocked")


def test_figure_files_exist_and_are_non_empty(generated_final_report):
    for figure in generated_final_report["figures"]:
        assert Path(figure["png"]).stat().st_size > 0
        assert Path(figure["pdf"]).stat().st_size > 0


def test_figure_csv_data_files_exist_and_are_non_empty(generated_final_report):
    for figure in generated_final_report["figures"]:
        assert Path(figure["csv"]).stat().st_size > 0


def test_top1_invariant_violations_force_support_labels_blocked(tmp_path):
    report = _base_300m_report(tmp_path, candidate_loss=4.6, top1=False)
    branch = evaluate_300m_scaffold(report, root=tmp_path, source_path="synthetic.json")
    assert branch["support_conditions"]["top1_clean"] is False
    assert "PVR_SELF_INSTILLED_EAN_GEOMETRY_HEAD_SUPPORTED" not in branch["supported_labels"]


def test_blocked_claims_remain_blocked_without_explicit_evidence(generated_final_report):
    outcomes = generated_final_report["final_conclusion"]["claim_outcomes"]
    for claim in ALWAYS_BLOCKED_CLAIMS:
        assert outcomes[claim].startswith("blocked")

