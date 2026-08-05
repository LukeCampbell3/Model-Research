from benchmark.common import write_json
from benchmark.runners.run_shared_trunk_copy_scope_ablation import (
    _baseline_from_seed_report,
    _row_from_artifacts,
)


def test_baseline_from_seed_report_loads_matched_lm_scorecard(tmp_path):
    scorecard = tmp_path / "baseline_scorecard.json"
    write_json(scorecard, {"scorecard": {"lm_loss": 3.5}})
    seed_report = tmp_path / "seed_report.json"
    write_json(seed_report, {
        "lm_eval_confirmation": {"paths": {"baseline": str(scorecard)}},
        "rows": [
            {
                "variant_name": "baseline",
                "model_variant": "pvr_baseline",
                "checkpoint_path": "checkpoint.pt",
                "final_loss": 2.9,
            }
        ],
        "summary": {
            "rows": {
                "baseline": {
                    "final_train_loss": 2.8,
                    "mean_eval_loss": 5.5,
                    "mean_route_margin": 0.4,
                    "mean_owner_entropy": 2.0,
                    "mean_prototype_monopoly_rate": 0.2,
                    "top1_invariants_clean": True,
                }
            }
        },
    })
    baseline = _baseline_from_seed_report(str(seed_report))
    assert baseline["model"] == "pvr_baseline"
    assert baseline["lm_loss"] == 3.5
    assert baseline["mean_eval_loss"] == 5.5


def test_copy_scope_row_requires_loss_improvement_and_route_stability(tmp_path):
    train = tmp_path / "training_curve.json"
    eval_curve = tmp_path / "eval_curve.json"
    routing = tmp_path / "routing_curve.json"
    write_json(train, {"loss_curve": [{"loss": 2.4}]})
    write_json(eval_curve, {"eval_curve": [{"eval_loss": 4.9}, {"eval_loss": 5.0}]})
    clean_route = {
        "owners_per_token": 1.0,
        "top2_execution_count": 0,
        "top4_execution_count": 0,
        "runtime_dynamic_k_count": 0,
        "runtime_expert_choice_count": 0,
        "production_map_mutated": False,
        "prototype_margin": 0.42,
        "owner_entropy": 2.1,
        "prototype_monopoly_rate": 0.18,
    }
    write_json(routing, {"routing_curve": [clean_route, clean_route]})
    baseline = {
        "final_train_loss": 2.8,
        "mean_eval_loss": 5.5,
        "lm_loss": 3.5,
        "mean_route_margin": 0.4,
        "mean_owner_entropy": 2.0,
        "mean_prototype_monopoly_rate": 0.2,
    }
    row = _row_from_artifacts(
        "embeddings_attention_norms",
        {
            "model_variant": "scope_model",
            "training_curve": str(train),
            "eval_curve": str(eval_curve),
            "routing_curve": str(routing),
            "optimizer_steps": 4000,
            "training_tokens_seen": 1024000,
            "effective_batch_tokens": 256,
            "status": "GENUINE_REDUCED_TRAINING_COMPLETE",
        },
        baseline,
        {"scorecard": {"lm_loss": 3.1, "perplexity": 22.0}},
    )
    assert row["top1_invariants_clean"] is True
    assert row["route_stable"] is True
    assert row["loss_supported"] is True
    assert row["deltas"]["lm_loss_delta_vs_baseline"] == -0.3999999999999999
