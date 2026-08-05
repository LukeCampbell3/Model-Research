from benchmark.analysis.summarize_shared_trunk_init_300m_repeat import (
    STATUS_SCORECARD_SUPPORTED_EVAL_MIXED,
    run,
)
from benchmark.common import write_json


def test_repeat_summary_marks_scorecard_supported_eval_curve_mixed(tmp_path):
    seed_report = tmp_path / "seed_report.json"
    baseline_scorecard = tmp_path / "baseline_scorecard.json"
    init_scorecard = tmp_path / "init_scorecard.json"
    dense_report = tmp_path / "dense_report.json"
    write_json(seed_report, {
        "seed": 42,
        "status": "PVR_SHARED_TRUNK_INIT_300M_NOT_SUPPORTED",
        "summary": {
            "rows": {
                "baseline": {
                    "mean_eval_loss": 4.8,
                    "final_train_loss": 2.8,
                },
                "shared_trunk_init_from_dense": {
                    "mean_eval_loss": 4.9,
                    "final_train_loss": 2.6,
                    "loss_supported": False,
                    "route_stable": True,
                    "top1_invariants_clean": True,
                    "deltas": {
                        "mean_eval_loss_delta_vs_baseline": 0.1,
                        "final_train_loss_delta_vs_baseline": -0.2,
                        "mean_route_margin_delta_vs_baseline": 0.01,
                        "mean_owner_entropy_delta_vs_baseline": 0.02,
                        "mean_prototype_monopoly_rate_delta_vs_baseline": -0.03,
                    },
                },
            }
        },
    })
    write_json(baseline_scorecard, {"scorecard": {"lm_loss": 3.4}})
    write_json(init_scorecard, {"scorecard": {"lm_loss": 3.0}})
    write_json(dense_report, {"rows": [{"model": "dense_transformer_300m", "lm_loss": 3.3}]})
    payload = run(
        seed_report=str(seed_report),
        baseline_scorecard=str(baseline_scorecard),
        init_scorecard=str(init_scorecard),
        dense_reference_report=str(dense_report),
        output=str(tmp_path / "out"),
    )
    assert payload["status"] == STATUS_SCORECARD_SUPPORTED_EVAL_MIXED
    assert payload["reduced_lm_scorecard_decision"]["scorecard_dense_gap_closed"] is True
