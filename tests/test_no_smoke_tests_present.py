from pathlib import Path


def test_no_smoke_benchmark_artifacts_or_flags():
    assert not Path("benchmark/smoke").exists()
    assert not Path("smoke_config.yaml").exists()
    for path in Path("benchmark").rglob("*"):
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8", errors="ignore").lower()
        assert "--smoke" not in text
        if path.suffix in {".md", ".json", ".py"}:
            assert "smoke-test evidence" not in text

