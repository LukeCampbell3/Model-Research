import json

from benchmark.runners.run_dense_mimic_experiment import (
    LOSS_ONLY_WEAK_STATUS,
    NOT_SUPPORTED_STATUS,
    SUPPORTED_STATUS,
    distill_weight_for_step,
    summarize_effectiveness,
)


def test_distill_weight_schedule_imitation_then_specialization():
    assert distill_weight_for_step(1, warmup_steps=10, distill_weight=0.5, decay_steps=10) == 0.5
    assert distill_weight_for_step(10, warmup_steps=10, distill_weight=0.5, decay_steps=10) == 0.5
    assert distill_weight_for_step(15, warmup_steps=10, distill_weight=0.5, decay_steps=10) == 0.25
    assert distill_weight_for_step(20, warmup_steps=10, distill_weight=0.5, decay_steps=10) == 0.0


def test_summarize_effectiveness_uses_loss_decision_rule(tmp_path):
    baseline = tmp_path / "baseline"
    mimic = tmp_path / "mimic"
    baseline.mkdir()
    mimic.mkdir()
    (baseline / "training_curve.json").write_text(json.dumps({"loss_curve": [{"loss": 5.0}, {"loss": 4.0}]}))
    (mimic / "training_curve.json").write_text(json.dumps({"loss_curve": [{"loss": 5.0}, {"loss": 3.5}]}))
    (baseline / "eval_curve.json").write_text(json.dumps({"eval_curve": [{"eval_loss": 4.0}]}))
    (mimic / "eval_curve.json").write_text(json.dumps({"eval_curve": [{"eval_loss": 4.1}]}))
    clean_route = {
        "owners_per_token": 1.0,
        "top2_execution_count": 0,
        "top4_execution_count": 0,
        "runtime_dynamic_k_count": 0,
        "runtime_expert_choice_count": 0,
        "production_map_mutated": False,
        "prototype_margin": 0.2,
        "owner_entropy": 1.0,
        "prototype_monopoly_rate": 0.2,
        "step": 1,
    }
    (baseline / "routing_curve.json").write_text(json.dumps({"routing_curve": [clean_route]}))
    mimic_route = {**clean_route, "prototype_margin": 0.3, "prototype_monopoly_rate": 0.2}
    (mimic / "routing_curve.json").write_text(json.dumps({"routing_curve": [mimic_route]}))
    payload = summarize_effectiveness(tmp_path, "baseline", "mimic")
    assert payload["status"] == NOT_SUPPORTED_STATUS
    (mimic / "eval_curve.json").write_text(json.dumps({"eval_curve": [{"eval_loss": 3.9}]}))
    payload = summarize_effectiveness(tmp_path, "baseline", "mimic")
    assert payload["status"] == SUPPORTED_STATUS
    collapsed_route = {**clean_route, "prototype_margin": 0.01, "prototype_monopoly_rate": 0.5}
    (mimic / "routing_curve.json").write_text(json.dumps({"routing_curve": [collapsed_route]}))
    payload = summarize_effectiveness(tmp_path, "baseline", "mimic")
    assert payload["status"] == LOSS_ONLY_WEAK_STATUS
