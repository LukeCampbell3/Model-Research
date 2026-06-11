"""Tests for new CLI commands (Phase 3)."""

import pytest
import sys
from unittest.mock import patch
from io import StringIO

from runtime_coder.cli import main


class TestPythonCLI:
    """Tests for Phase 3 CLI commands."""

    def test_validate_runtime_tokenizer_command(self):
        """validate-runtime-tokenizer command runs without crash."""
        with patch("sys.argv", ["runtime_coder", "validate-runtime-tokenizer"]):
            ret = main()
        assert ret == 0

    def test_build_python_curriculum_command(self):
        """build-python-curriculum command runs without crash."""
        with patch("sys.argv", ["runtime_coder", "build-python-curriculum", "--stage", "A", "--size", "5"]):
            ret = main()
        assert ret == 0

    def test_build_python_curriculum_all_stages(self):
        """build-python-curriculum works for all stages."""
        for stage in ["A", "B", "C"]:
            with patch("sys.argv", ["runtime_coder", "build-python-curriculum", "--stage", stage, "--size", "3"]):
                ret = main()
            assert ret == 0, f"Stage {stage} failed"

    def test_train_python_command_help(self):
        """train-python-branch-ticket --help doesn't crash."""
        with patch("sys.argv", ["runtime_coder", "train-python-branch-ticket", "--help"]):
            with pytest.raises(SystemExit) as exc_info:
                main()
            # argparse calls sys.exit(0) on --help
            assert exc_info.value.code == 0

    def test_no_command_shows_help(self):
        """No command shows help and returns 1."""
        with patch("sys.argv", ["runtime_coder"]):
            ret = main()
        assert ret == 1
