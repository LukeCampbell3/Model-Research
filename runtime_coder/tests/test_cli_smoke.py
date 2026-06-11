"""CLI smoke tests - verify all CLI commands run without error."""

import subprocess
import sys
import pytest


def run_cli(*args):
    """Run the CLI as a subprocess and return the result."""
    cmd = [sys.executable, "-m", "runtime_coder.cli"] + list(args)
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    return result


class TestCLISmoke:
    """Smoke tests verifying CLI commands execute successfully."""

    def test_validate_schemas(self):
        result = run_cli("validate-schemas")
        assert result.returncode == 0, f"stderr: {result.stderr}"
        assert "ALL SCHEMAS VALID" in result.stdout

    def test_list_special_tokens(self):
        result = run_cli("list-special-tokens")
        assert result.returncode == 0, f"stderr: {result.stderr}"
        assert "ALL UNIQUE" in result.stdout

    def test_generate_fixtures(self):
        result = run_cli("generate-fixtures")
        assert result.returncode == 0, f"stderr: {result.stderr}"
        assert "Generated" in result.stdout

    def test_build_sft(self):
        result = run_cli("build-sft")
        assert result.returncode == 0, f"stderr: {result.stderr}"
        assert "Built" in result.stdout

    def test_eval_compliance(self):
        result = run_cli("eval-compliance")
        assert result.returncode == 0, f"stderr: {result.stderr}"
        assert "COMPLIANCE EVAL COMPLETE" in result.stdout

    def test_tokenizer_smoke(self):
        result = run_cli("tokenizer-smoke")
        assert result.returncode == 0, f"stderr: {result.stderr}"
        assert "TOKENIZER SMOKE OK" in result.stdout

    def test_no_command_returns_error(self):
        result = run_cli()
        assert result.returncode == 1

    def test_model_forward_smoke(self):
        result = run_cli("model-forward-smoke")
        assert result.returncode == 0, f"stderr: {result.stderr}"
        assert "FORWARD PASS OK" in result.stdout
