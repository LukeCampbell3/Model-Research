"""Phase 1 Pretraining Tests for RuntimeCoder.

Tests cover:
- BPE tokenizer encoding/decoding
- FIM dataset construction
- File boundary dataset construction
- Pretraining smoke test (5 steps, loss decreasing)
- Branch SFT smoke test
- RuntimeCoder-Micro model build and forward pass
- Pretraining eval metrics
- Code corpus filter
"""

import os
import tempfile

import pytest
import torch

from runtime_coder.tokenizer.bpe_tokenizer import BPETokenizer
from runtime_coder.tokenizer.runtime_special_tokens import (
    SPECIAL_TOKENS,
    SPECIAL_TOKEN_ID_OFFSET,
)
from runtime_coder.data_pipeline.fim_dataset import (
    FIMExample,
    build_fim_dataset,
    create_fim_example,
)
from runtime_coder.data_pipeline.file_boundary_dataset import (
    FileBoundaryExample,
    build_file_boundary_dataset,
    create_file_boundary_example,
)
from runtime_coder.data_pipeline.code_corpus_filter import (
    deduplicate_by_hash,
    extract_python_files,
    filter_file,
)
from runtime_coder.model.runtime_coder_micro import (
    RuntimeCoderMicroConfig,
    build_micro_model,
    count_parameters,
)
from runtime_coder.training.train_pretrain import PretrainConfig, run_pretrain_smoke
from runtime_coder.training.train_branch_sft import BranchSFTConfig, run_branch_sft_smoke
from runtime_coder.evals.pretraining_eval import (
    eval_fim_completion,
    eval_perplexity,
    eval_special_token_retention,
)


# ============================================================
# BPE Tokenizer Tests
# ============================================================


class TestBPETokenizer:
    """Tests for the BPE tokenizer scaffold."""

    def test_bpe_tokenizer_encodes_python_code(self):
        """BPE tokenizer can encode Python code to token IDs."""
        tok = BPETokenizer()
        code = "def hello():\n    print('world')\n"
        ids = tok.encode(code)

        assert len(ids) > 0
        assert all(isinstance(i, int) for i in ids)
        # All IDs should be valid
        assert all(0 <= i < tok.vocab_size for i in ids)

    def test_bpe_tokenizer_preserves_special_tokens(self):
        """BPE tokenizer correctly encodes and decodes special tokens."""
        tok = BPETokenizer()

        # Test individual special tokens
        for token in ["<|fim_prefix|>", "<|fim_middle|>", "<|fim_suffix|>",
                      "<|branch_start|>", "<|branch_end|>"]:
            ids = tok.encode(token)
            assert len(ids) == 1, f"Special token {token} should encode to single ID"
            assert ids[0] >= SPECIAL_TOKEN_ID_OFFSET, \
                f"Special token {token} ID should be >= {SPECIAL_TOKEN_ID_OFFSET}"

        # Test mixed text with special tokens
        text = "<|fim_prefix|>def foo():<|fim_suffix|>return x<|fim_middle|>"
        ids = tok.encode(text)
        decoded = tok.decode(ids)
        # Special tokens should survive round-trip
        assert "<|fim_prefix|>" in decoded
        assert "<|fim_suffix|>" in decoded
        assert "<|fim_middle|>" in decoded

    def test_bpe_tokenizer_vocab_size(self):
        """BPE tokenizer has expected vocab size."""
        tok = BPETokenizer()
        assert tok.vocab_size >= SPECIAL_TOKEN_ID_OFFSET + len(SPECIAL_TOKENS)
        assert tok.base_vocab_size > 0

    def test_bpe_tokenizer_train_from_texts(self):
        """BPE tokenizer can train merges from texts."""
        tok = BPETokenizer()
        texts = [
            "def hello(): pass",
            "def world(): return 42",
            "class Foo: pass",
        ]
        tok.train_from_texts(texts, vocab_size=32000)
        # Should have learned some merges
        assert len(tok._merges) > 0


# ============================================================
# FIM Dataset Tests
# ============================================================


class TestFIMDataset:
    """Tests for the FIM dataset construction."""

    def test_fim_dataset_uses_fim_tokens(self):
        """FIM examples use the correct special tokens in training format."""
        texts = [
            "def binary_search(arr, target):\n    left, right = 0, len(arr) - 1\n    return -1\n",
            "class Processor:\n    def __init__(self):\n        self.data = []\n",
        ]
        examples = build_fim_dataset(texts, count=5, fim_rate=1.0, seed=42)
        assert len(examples) > 0

        for ex in examples:
            formatted = ex.to_training_format()
            assert "<|fim_prefix|>" in formatted
            assert "<|fim_suffix|>" in formatted
            assert "<|fim_middle|>" in formatted

    def test_fim_example_structure(self):
        """FIM examples have valid prefix/middle/suffix split."""
        text = "def hello():\n    print('world')\n    return True\n"
        example = create_fim_example(text, fim_rate=1.0)
        assert example is not None
        assert len(example.prefix) > 0
        assert len(example.middle) > 0
        assert len(example.suffix) >= 0
        assert example.full_text == text
        # Reconstruction
        assert example.prefix + example.middle + example.suffix == text

    def test_fim_rate_zero_returns_none(self):
        """FIM with rate=0 always returns None."""
        text = "def foo(): return 42\n" * 5
        result = create_fim_example(text, fim_rate=0.0)
        assert result is None


# ============================================================
# File Boundary Dataset Tests
# ============================================================


class TestFileBoundaryDataset:
    """Tests for the file boundary dataset."""

    def test_file_boundary_uses_separator_tokens(self):
        """File boundary examples use <|file_sep|> and <|path|> tokens."""
        files = [
            ("src/main.py", "def main(): pass"),
            ("src/utils.py", "def helper(): pass"),
            ("tests/test_main.py", "def test_main(): assert True"),
        ]
        result = create_file_boundary_example(files)
        assert "<|file_sep|>" in result
        assert "<|path|>" in result
        assert "src/main.py" in result
        assert "src/utils.py" in result
        assert "def main(): pass" in result

    def test_build_file_boundary_dataset(self):
        """Can build multiple file boundary examples."""
        files = [
            (f"file_{i}.py", f"def func_{i}(): return {i}")
            for i in range(15)
        ]
        examples = build_file_boundary_dataset(files, examples_per_window=5, seed=42)
        assert len(examples) > 0
        for ex in examples:
            assert len(ex.files) >= 2


# ============================================================
# Pretrain Smoke Tests
# ============================================================


class TestPretrainSmoke:
    """Tests for the pretraining smoke test."""

    @pytest.fixture
    def smoke_config(self, tmp_path):
        """Create a config for fast smoke testing."""
        return PretrainConfig(
            model_config=RuntimeCoderMicroConfig(
                vocab_size=50176,
                d_model=128,
                n_layers=2,
                n_heads=4,
                max_seq_len=256,
                d_ff=512,
            ),
            batch_size=2,
            lr=1e-3,
            max_steps=5,
            device="cuda" if torch.cuda.is_available() else "cpu",
            max_seq_len=128,
            report_path=str(tmp_path / "pretrain_smoke_report.json"),
        )

    def test_pretrain_smoke_runs_5_steps(self, smoke_config):
        """Pretrain smoke completes 5 gradient steps."""
        metrics = run_pretrain_smoke(smoke_config)
        assert metrics["steps"] == 5
        assert len(metrics["losses"]) == 5
        assert all(isinstance(l, float) for l in metrics["losses"])

    def test_pretrain_smoke_loss_decreases(self, smoke_config):
        """Pretrain smoke shows loss decreasing over 5 steps."""
        # Use higher LR to ensure loss decrease in 5 steps
        smoke_config.lr = 3e-3
        metrics = run_pretrain_smoke(smoke_config)
        # Check that final loss is less than initial loss
        assert metrics["losses"][-1] < metrics["losses"][0], \
            f"Loss should decrease: {metrics['losses'][0]:.4f} -> {metrics['losses'][-1]:.4f}"


# ============================================================
# Branch SFT Smoke Tests
# ============================================================


class TestBranchSFTSmoke:
    """Tests for the branch SFT smoke test."""

    def test_branch_sft_smoke_runs(self, tmp_path):
        """Branch SFT smoke completes 3 gradient steps."""
        config = BranchSFTConfig(
            model_config=RuntimeCoderMicroConfig(
                vocab_size=50176,
                d_model=128,
                n_layers=2,
                n_heads=4,
                max_seq_len=256,
                d_ff=512,
            ),
            batch_size=2,
            lr=1e-3,
            max_steps=3,
            device="cuda" if torch.cuda.is_available() else "cpu",
            max_seq_len=128,
            report_path=str(tmp_path / "branch_sft_smoke_report.json"),
        )
        metrics = run_branch_sft_smoke(config)
        assert metrics["steps"] == 3
        assert len(metrics["losses"]) == 3
        assert metrics["special_token_validation"]["branch_tokens_present"] is True


# ============================================================
# Micro Model Tests
# ============================================================


class TestMicroModel:
    """Tests for the RuntimeCoder-Micro model."""

    def test_micro_model_builds(self):
        """RuntimeCoder-Micro model can be built."""
        config = RuntimeCoderMicroConfig()
        model = build_micro_model(config, device="cpu")
        assert model is not None
        assert isinstance(model, torch.nn.Module)

    def test_micro_model_forward_pass(self):
        """RuntimeCoder-Micro can perform a forward pass."""
        config = RuntimeCoderMicroConfig()
        model = build_micro_model(config, device="cpu")
        model.eval()

        input_ids = torch.randint(0, config.vocab_size, (1, 64))
        with torch.no_grad():
            output = model(input_ids)

        assert "logits" in output
        assert "purity_counters" in output
        assert output["logits"].shape == (1, 64, config.vocab_size)
        # Verify purity counters work on micro model
        assert isinstance(output["purity_counters"], dict)
        assert "top1_correct" in output["purity_counters"]

    def test_micro_model_parameter_count(self):
        """RuntimeCoder-Micro has reasonable parameter count at default config."""
        config = RuntimeCoderMicroConfig()
        model = build_micro_model(config, device="cpu")
        info = count_parameters(model)

        # At d_model=256, n_layers=6, vocab_size=50176:
        # Embedding: 50176 * 256 = 12.8M (weight-tied with lm_head)
        # Pos emb: 2048 * 256 = 0.5M
        # Per layer: QKV(256*768) + out(256*256) + FF(256*1024 + 1024*256) + LN = ~0.8M
        # 6 layers: ~4.8M
        # Total: ~18M (with weight tying)
        total = info["total"]
        assert total > 5_000_000, f"Too few params: {total:,}"
        assert total < 100_000_000, f"Too many params: {total:,}"


# ============================================================
# Pretraining Eval Tests
# ============================================================


class TestPretrainingEval:
    """Tests for pretraining evaluation metrics."""

    def test_pretraining_eval_runs(self):
        """Pretraining eval metrics can be computed."""
        config = RuntimeCoderMicroConfig(
            vocab_size=50176,
            d_model=128,
            n_layers=2,
            n_heads=4,
            max_seq_len=256,
            d_ff=512,
        )
        model = build_micro_model(config, device="cpu")

        # Test perplexity
        dataset = ["def foo(): return 42\n", "class Bar: pass\n"]
        ppl = eval_perplexity(model, dataset, device="cpu", max_len=64)
        assert ppl > 0
        assert ppl < float("inf")

        # Test FIM eval
        texts = ["def hello():\n    print('world')\n    return True\n" * 3]
        fim_examples = build_fim_dataset(texts, count=3, fim_rate=1.0, seed=42)
        fim_metrics = eval_fim_completion(model, fim_examples, device="cpu", max_len=64)
        assert "fim_loss" in fim_metrics
        assert fim_metrics["examples_evaluated"] > 0

        # Test special token retention
        retention = eval_special_token_retention(model, device="cpu")
        assert "special_tokens_in_vocab" in retention
        assert retention["special_tokens_in_vocab"] is True
        assert retention["all_logits_finite"] is True
        assert retention["no_garbage_logits"] is True


# ============================================================
# Code Corpus Filter Tests
# ============================================================


class TestCodeCorpusFilter:
    """Tests for the code corpus filter."""

    def test_code_corpus_filter(self):
        """Code corpus filter accepts valid Python and rejects binary/generated."""
        # Should accept normal Python
        assert filter_file("main.py", "def hello():\n    print('world')\n" * 5) is True

        # Should reject binary extensions
        assert filter_file("image.png", "binary content") is False
        assert filter_file("lib.so", "binary content") is False

        # Should reject files with null bytes
        assert filter_file("data.py", "normal\x00binary") is False

        # Should reject generated files
        assert filter_file("gen.py", "# AUTO-GENERATED\ncode here\n" + "x" * 100) is False

        # Should reject too-short files
        assert filter_file("tiny.py", "x = 1") is False

        # Should reject too-long files
        assert filter_file("huge.py", "x = 1\n" * 50001) is False

    def test_deduplicate_by_hash(self):
        """Deduplication removes files with identical content."""
        files = [
            ("a.py", "def foo(): pass"),
            ("b.py", "def bar(): pass"),
            ("c.py", "def foo(): pass"),  # duplicate of a.py
        ]
        unique = deduplicate_by_hash(files)
        assert len(unique) == 2
        paths = [p for p, _ in unique]
        assert "a.py" in paths
        assert "b.py" in paths

    def test_extract_python_files(self, tmp_path):
        """Can extract Python files from a directory."""
        # Create test files (must be >= MIN_FILE_LENGTH=50 chars)
        (tmp_path / "main.py").write_text(
            "def main():\n    print('hello world')\n    return 0\n\n# entry point\n"
        )
        (tmp_path / "utils.py").write_text(
            "def helper():\n    \"\"\"A helper utility function.\"\"\"\n    return True\n"
        )
        (tmp_path / "data.txt").write_text("not python" * 20)
        sub = tmp_path / "sub"
        sub.mkdir()
        (sub / "module.py").write_text(
            "class MyClass:\n    def method(self):\n        \"\"\"Do something.\"\"\"\n        pass\n"
        )

        files = extract_python_files(str(tmp_path))
        paths = [p for p, _ in files]
        assert any("main.py" in p for p in paths)
        assert any("utils.py" in p for p in paths)
        assert any("module.py" in p for p in paths)
        assert not any("data.txt" in p for p in paths)
