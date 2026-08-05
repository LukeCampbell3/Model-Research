import json

from benchmark.analysis.dense_approximation import (
    DENSE_STATUS_GAP_IDENTIFIED,
    ROUTE_WIN_STATUS,
    run,
    write_deprecation_report,
)


def test_dense_approximation_report_writes_outputs(tmp_path):
    payload = run(size="300m", output=tmp_path)
    assert payload["status"] in {DENSE_STATUS_GAP_IDENTIFIED, ROUTE_WIN_STATUS}
    assert (tmp_path / "dense_approximation_report.json").exists()
    assert (tmp_path / "route_conditional_loss_windows.json").exists()
    saved = json.loads((tmp_path / "dense_approximation_report.json").read_text())
    assert "pvr_minus_dense_lm_loss" in saved
    assert saved["forbidden_repair"]["route_confidence_regularization_0_01"] == "DO_NOT_USE_AGAIN"


def test_rba_update_deprecation_report_advises_against_reuse(tmp_path):
    payload = write_deprecation_report(tmp_path / "deprecated.json")
    assert payload["status"] == "RBA_ROUTE_CONFIDENCE_UPDATE_DEPRECATED"
    assert "route_confidence_regularization_0_01" in payload["do_not_use_again"]
    assert (tmp_path / "deprecated.md").exists()

