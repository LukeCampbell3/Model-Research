import json
from pathlib import Path

from benchmark.runners.run_lm_eval import run as run_lm
from benchmark.scripts.generate_model_size_matrix import generate


def test_scorecard_contains_schema_required_fields(tmp_path):
    generate(tmp_path)
    config = json.loads((tmp_path / "benchmark" / "configs" / "generated" / "dense_transformer_100m.yaml").read_text())
    config["checkpoint_path"] = str(tmp_path / "missing" / "checkpoint.pt")
    config["eval_data_paths"] = [str(tmp_path / "missing_eval")]
    out = tmp_path / "scorecard.json"
    payload = run_lm(config, str(out))
    schema = json.loads(Path("benchmark/schemas/scorecard_schema.json").read_text())
    assert set(schema["required"]) <= set(payload)
    assert set(schema["properties"]["scorecard"]["required"]) <= set(payload["scorecard"])
    assert payload["status"] == "NOT_RUN_MISSING_CHECKPOINT"
    assert payload["benchmark_evidence"] is False
