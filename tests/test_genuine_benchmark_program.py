from benchmark.runners.run_genuine_benchmark_program import _stable_learning_gate, _volume_gate, run
from benchmark.scripts.generate_model_size_matrix import generate
from benchmark.common import load_json_or_yaml, write_json


def test_genuine_program_blocks_without_real_data_and_checkpoints(tmp_path):
    generate(tmp_path)
    suite = tmp_path / "benchmark" / "configs" / "generated" / "benchmark_100m_suite.yaml"
    suite_payload = load_json_or_yaml(suite)
    for item in suite_payload["models"]:
        config_path = tmp_path / "benchmark" / "configs" / "generated" / f"{item['model_variant']}.yaml"
        config = load_json_or_yaml(config_path)
        config["checkpoint_path"] = str(tmp_path / "missing_checkpoints" / item["model_variant"] / "checkpoint.pt")
        config["training_data_paths"] = [str(tmp_path / "missing_data" / "broad_nlp_train")]
        config["eval_data_paths"] = [str(tmp_path / "missing_data" / "eval")]
        write_json(config_path, config)
    payload = run(str(suite), str(tmp_path / "program"), size="100m", execute_suite=False)

    assert payload["target_status"] == "PVR_EC_O_100M_GENUINE_BENCHMARK_COMPLETE"
    assert payload["status"] == "NOT_RUN_MISSING_DATA"
    assert payload["completed"] is False
    assert payload["benchmark_evidence"] is False
    assert payload["model_count"] == 8
    assert payload["required_seeds"] == [42, 123, 777]
    assert "model construction is not benchmark evidence" in payload["invalid_claims_blocked"]

    for row in payload["model_audits"]:
        assert row["can_claim_benchmark_evidence"] is False
        assert row["trained_checkpoint"]["exists"] is False
        assert row["training"]["status"] == "NOT_RUN_MISSING_DATA"
        assert row["seeds"]["status"] == "SEED_REDUCTION_RESOURCE_BLOCKED"
        assert row["contamination"]["status"] == "CONTAMINATION_STATUS_UNKNOWN"
        assert row["required_artifacts"]["trained_checkpoint"] is False
        assert row["required_artifacts"]["scorecard"] is False

    pvr_rows = [row for row in payload["model_audits"] if row["model_family"] == "pvr_ec_o"]
    assert pvr_rows
    for row in pvr_rows:
        assert row["routing_diagnostics_required"] is True
        assert row["routing_diagnostics"]["hard_invariants_validated"] is False
        assert row["routing_diagnostics"]["hard_invariants"]["owners_per_token"] == 1.0


def test_one_step_volume_cannot_claim_benchmark_evidence():
    audit = {
        "training": {
            "optimizer_steps": 1,
            "training_tokens_seen": 16,
            "effective_batch_tokens": 16,
        }
    }
    card = {
        "eval_token_count": 2048,
        "heldout_eval_token_count": 512,
    }
    result = _volume_gate(
        audit,
        card,
        {
            "min_optimizer_steps": 20,
            "min_training_tokens": 1024,
            "min_effective_batch_tokens": 32,
            "min_eval_tokens": 1024,
            "min_heldout_eval_tokens": 256,
        },
    )

    assert result["passed"] is False
    assert "optimizer_steps" in result["failures"]
    assert "training_tokens_seen" in result["failures"]
    assert "effective_batch_tokens" in result["failures"]


def test_real_comparison_gate_requires_meaningful_training_tokens_and_windows():
    audit = {
        "training": {
            "optimizer_steps": 1000,
            "training_tokens_seen": 256000,
            "effective_batch_tokens": 256,
            "eval_window_count": 10,
        }
    }
    card = {
        "eval_token_count": 51200,
        "heldout_eval_token_count": 12800,
    }
    result = _volume_gate(
        audit,
        card,
        {
            "min_optimizer_steps": 1000,
            "min_training_tokens": 1_000_000,
            "min_effective_batch_tokens": 32,
            "min_eval_tokens": 50_000,
            "min_heldout_eval_tokens": 10_000,
            "min_eval_windows": 10,
        },
    )

    assert result["passed"] is False
    assert "training_tokens_seen" in result["failures"]
    assert "optimizer_steps" not in result["failures"]
    assert "eval_windows" not in result["failures"]


def test_routing_diagnostics_over_time_required_for_pvr():
    audit = {
        "model_family": "pvr_ec_o",
        "training": {
            "loss_curve": [{"loss": 3.0}, {"loss": 2.0}],
            "eval_curve": [{"eval_loss": 3.5}, {"eval_loss": 2.5}],
            "routing_curve": [{"owners_per_token": 1.0}],
        },
    }
    result = _stable_learning_gate(audit, {"min_eval_windows": 2})

    assert result["passed"] is False
    assert "routing_diagnostics_over_time_present" in result["failures"]
