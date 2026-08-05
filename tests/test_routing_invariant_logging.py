import json

from benchmark.common import ROUTING_INVARIANT_FIELDS
from benchmark.runners.run_routing_diagnostics import run as run_routing
from benchmark.scripts.generate_model_size_matrix import generate


def test_routing_invariants_are_logged(tmp_path):
    generate(tmp_path)
    config = json.loads((tmp_path / "benchmark" / "configs" / "generated" / "pvr_ec_o_full_100m.yaml").read_text())
    config["checkpoint_path"] = str(tmp_path / "missing" / "checkpoint.pt")
    config["eval_data_paths"] = [str(tmp_path / "missing_eval")]
    payload = run_routing(config, str(tmp_path / "routing.json"))
    assert payload["required_invariants"] == ROUTING_INVARIANT_FIELDS
    for field in ROUTING_INVARIANT_FIELDS:
        assert field in payload["scorecard"]
    assert payload["scorecard"]["invariants_validated"] is False
