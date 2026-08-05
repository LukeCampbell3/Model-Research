from pathlib import Path

from benchmark.common import ARCHITECTURE_STATUSES, INFRASTRUCTURE_STATUSES


VALID_PHRASES = [
    "PVR-EC-O does not yet beat generalized baselines.",
    "PVR-EC-O beats generalized baselines but lags internal strong-router control.",
    "PVR-EC-O matches internal strong-router control.",
    "PVR-EC-O beats internal strong-router control.",
]


def test_report_templates_use_valid_language():
    text = "\n".join(path.read_text(encoding="utf-8") for path in Path("benchmark/reports").glob("*_template.md"))
    assert "PVR-EC-O failed because fixed_moe won" not in text
    for phrase in VALID_PHRASES:
        assert phrase in text
    assert "BENCH_INFRASTRUCTURE_READY" in text
    assert "PVR_EC_O_BROAD_NLP_COMPETITIVE" in ARCHITECTURE_STATUSES
    assert "NOT_RUN_MISSING_CHECKPOINT" in INFRASTRUCTURE_STATUSES

