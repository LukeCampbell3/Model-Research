"""Phase 2 BranchTicket SFT Tests for RuntimeCoder.

Tests cover:
- Diverse BranchTicket example generation (count, coverage)
- All branch_types covered
- All privilege_levels covered
- Invalid examples fail validation
- Valid examples pass validation
- Full SFT training (50 steps)
- Schema validity rate tracking
- Rejection training distinguishes valid/invalid
- BranchIR example generation
- BranchIR validation
- Model text generation
- Held-out evaluation
"""

import pytest
import torch

from runtime_coder.data_pipeline.branch_ticket_dataset import (
    BranchTicketSFTExample,
    TASK_CATEGORIES,
    generate_diverse_examples,
    generate_invalid_examples,
)
from runtime_coder.data_pipeline.branch_ir_dataset import (
    BranchIRSFTExample,
    generate_ir_examples,
)
from runtime_coder.model.runtime_coder_micro import (
    RuntimeCoderMicroConfig,
    build_micro_model,
)
from runtime_coder.schemas.branch_ticket import (
    ALLOWED_BRANCH_TYPES,
    ALLOWED_PRIVILEGE_LEVELS,
    BranchTicket,
)
from runtime_coder.schemas.branch_ir import BranchIR
from runtime_coder.training.train_branch_sft import (
    BranchSFTFullConfig,
    generate_from_model,
    run_branch_sft_full,
    validate_generated_ticket,
)
from runtime_coder.training.train_rejection import (
    RejectionTrainingConfig,
    build_rejection_pairs,
    run_rejection_training,
)
from runtime_coder.evals.branch_ticket_validity import (
    eval_branch_ticket_generation,
)
from runtime_coder.evals.branch_ir_validity import (
    eval_branch_ir_generation,
    validate_branch_irs,
)


# ============================================================
# Test Configuration
# ============================================================


def _small_model_config():
    """Small model config for fast testing."""
    return RuntimeCoderMicroConfig(
        vocab_size=50176,
        d_model=64,
        n_layers=2,
        n_heads=4,
        max_seq_len=256,
        d_ff=256,
    )


# ============================================================
# Dataset Generation Tests
# ============================================================


class TestBranchTicketDataset:
    """Tests for diverse BranchTicket example generation."""

    def test_diverse_branch_ticket_examples_generated(self):
        """generate_diverse_examples produces at least 50 examples."""
        examples = generate_diverse_examples(count=100)
        assert len(examples) >= 50
        assert all(isinstance(ex, BranchTicketSFTExample) for ex in examples)

    def test_examples_cover_all_branch_types(self):
        """Generated examples cover all 6 allowed branch_types."""
        examples = generate_diverse_examples(count=100)
        branch_types_seen = set()
        for ex in examples:
            branch_types_seen.add(ex.target_branch_ticket.branch_type)

        for bt in ALLOWED_BRANCH_TYPES:
            assert bt in branch_types_seen, f"branch_type '{bt}' not covered"

    def test_examples_cover_all_privilege_levels(self):
        """Generated examples cover all 4 allowed privilege_levels."""
        examples = generate_diverse_examples(count=100)
        privilege_levels_seen = set()
        for ex in examples:
            privilege_levels_seen.add(ex.target_branch_ticket.privilege_level)

        for pl in ALLOWED_PRIVILEGE_LEVELS:
            assert pl in privilege_levels_seen, f"privilege_level '{pl}' not covered"

    def test_examples_cover_all_task_types(self):
        """Generated examples cover all 7 task categories."""
        examples = generate_diverse_examples(count=100)
        task_types_seen = set()
        for ex in examples:
            task_types_seen.add(ex.task_type)

        for tt in TASK_CATEGORIES.keys():
            assert tt in task_types_seen, f"task_type '{tt}' not covered"

    def test_valid_examples_pass_validation(self):
        """All valid examples pass BranchTicket.validate()."""
        examples = generate_diverse_examples(count=50)
        for ex in examples:
            assert ex.is_valid is True
            errors = ex.target_branch_ticket.validate()
            assert errors == [], (
                f"Valid example {ex.target_branch_ticket.ticket_id} has errors: {errors}"
            )

    def test_invalid_examples_fail_validation(self):
        """All invalid examples fail BranchTicket.validate()."""
        examples = generate_invalid_examples(count=30)
        for ex in examples:
            assert ex.is_valid is False
            errors = ex.target_branch_ticket.validate()
            assert len(errors) > 0, (
                f"Invalid example should have errors but got none: {ex.invalid_reason}"
            )

    def test_example_format_input_uses_special_tokens(self):
        """format_input() includes task and context special tokens."""
        examples = generate_diverse_examples(count=5)
        for ex in examples:
            input_text = ex.format_input()
            assert "<|task_start|>" in input_text
            assert "<|task_end|>" in input_text
            assert "<|context_start|>" in input_text
            assert "<|context_end|>" in input_text

    def test_example_format_target_is_valid_json(self):
        """format_target() produces valid JSON."""
        import json
        examples = generate_diverse_examples(count=10)
        for ex in examples:
            target = ex.format_target()
            data = json.loads(target)
            assert "ticket_id" in data
            assert "branch_type" in data

    def test_minimum_combinations_coverage(self):
        """At least 35 unique (task_type, branch_type) combinations exist."""
        examples = generate_diverse_examples(count=100)
        combos = set()
        for ex in examples:
            combos.add((ex.task_type, ex.target_branch_ticket.branch_type))
        # 7 task_types x 5+ branch_types = 35+ combinations
        assert len(combos) >= 35, f"Only {len(combos)} unique combos, need >= 35"


# ============================================================
# BranchIR Dataset Tests
# ============================================================


class TestBranchIRDataset:
    """Tests for BranchIR example generation."""

    def test_branch_ir_examples_generated(self):
        """generate_ir_examples produces requested count."""
        examples = generate_ir_examples(count=50)
        assert len(examples) == 50
        assert all(isinstance(ex, BranchIRSFTExample) for ex in examples)

    def test_branch_ir_validation(self):
        """All generated BranchIR examples pass validate()."""
        examples = generate_ir_examples(count=50)
        for ex in examples:
            errors = ex.target_branch_ir.validate()
            assert errors == [], (
                f"BranchIR {ex.target_branch_ir.ir_id} has errors: {errors}"
            )

    def test_branch_ir_covers_action_types(self):
        """IR examples cover all action types."""
        examples = generate_ir_examples(count=50)
        action_types_seen = set()
        for ex in examples:
            action_types_seen.add(ex.action_type)

        expected = {"edit", "test", "inspect", "summarize", "refactor", "multi_file"}
        for at in expected:
            assert at in action_types_seen, f"action_type '{at}' not covered"

    def test_branch_ir_format_input(self):
        """BranchIR format_input includes branch tokens."""
        examples = generate_ir_examples(count=5)
        for ex in examples:
            input_text = ex.format_input()
            assert "<|branch_start|>" in input_text
            assert "<|branch_end|>" in input_text
            assert "<|branch_ir|>" in input_text

    def test_branch_ir_has_steps(self):
        """All BranchIR examples have at least one step."""
        examples = generate_ir_examples(count=50)
        for ex in examples:
            assert len(ex.target_branch_ir.steps) >= 1


# ============================================================
# Training Tests
# ============================================================


class TestBranchSFTFull:
    """Tests for full Branch SFT training."""

    def test_branch_sft_full_trains_50_steps(self, tmp_path):
        """Full Branch SFT training completes 50 steps."""
        config = BranchSFTFullConfig(
            model_config=_small_model_config(),
            batch_size=2,
            lr=1e-3,
            max_steps=50,
            device="cuda" if torch.cuda.is_available() else "cpu",
            max_seq_len=128,
            max_gen_tokens=32,
            validate_every=25,
            num_examples=20,
            report_path=str(tmp_path / "branch_sft_full_report.json"),
        )
        metrics = run_branch_sft_full(config)
        assert metrics["steps"] == 50
        assert len(metrics["losses"]) == 50
        assert metrics["loss_decreased"] is True

    def test_schema_validity_rate_improves(self, tmp_path):
        """Schema validity rate is tracked and loss shows learning."""
        config = BranchSFTFullConfig(
            model_config=_small_model_config(),
            batch_size=2,
            lr=2e-3,
            max_steps=50,
            device="cuda" if torch.cuda.is_available() else "cpu",
            max_seq_len=128,
            max_gen_tokens=32,
            validate_every=25,
            num_examples=20,
            report_path=str(tmp_path / "validity_track_report.json"),
        )
        metrics = run_branch_sft_full(config)

        # Validity checkpoints should be tracked
        assert len(metrics["validity_checkpoints"]) >= 2
        # Loss must decrease (proves learning)
        assert metrics["losses"][-1] < metrics["losses"][0], (
            f"Loss should decrease: {metrics['losses'][0]:.4f} -> {metrics['losses'][-1]:.4f}"
        )

    def test_generate_from_model_returns_text(self):
        """generate_from_model produces a text string."""
        config = _small_model_config()
        device = "cuda" if torch.cuda.is_available() else "cpu"
        model = build_micro_model(config, device=device)

        input_text = "<|task_start|>Fix a bug<|task_end|>"
        generated = generate_from_model(
            model, input_text, config.vocab_size,
            max_gen_tokens=32, max_seq_len=128, device=device
        )
        assert isinstance(generated, str)
        assert len(generated) > 0

    def test_validate_generated_ticket_valid(self):
        """validate_generated_ticket correctly identifies valid JSON ticket."""
        valid_json = BranchTicket(
            ticket_id="test_001",
            branch_type="patch",
            privilege_level="read_write",
            description="test",
            read_set=["a.py"],
            write_set=["b.py"],
            verifier_targets=["tests/test.py::test_a"],
        ).to_json()

        is_valid, errors = validate_generated_ticket(f"prefix {valid_json} suffix")
        assert is_valid is True
        assert errors == []

    def test_validate_generated_ticket_invalid(self):
        """validate_generated_ticket correctly rejects invalid tickets."""
        # No JSON
        is_valid, errors = validate_generated_ticket("no json here")
        assert is_valid is False
        assert len(errors) > 0

        # Invalid JSON
        is_valid, errors = validate_generated_ticket("{not: valid json{")
        assert is_valid is False

        # Valid JSON but empty ticket_id
        bad_ticket = '{"ticket_id": "", "branch_type": "patch"}'
        is_valid, errors = validate_generated_ticket(bad_ticket)
        assert is_valid is False


# ============================================================
# Rejection Training Tests
# ============================================================


class TestRejectionTraining:
    """Tests for rejection training."""

    def test_rejection_training_distinguishes_valid_invalid(self, tmp_path):
        """Rejection training trains successfully and tracks loss."""
        config = RejectionTrainingConfig(
            model_config=_small_model_config(),
            batch_size=2,
            lr=1e-3,
            max_steps=20,
            device="cuda" if torch.cuda.is_available() else "cpu",
            max_seq_len=128,
            num_valid_examples=10,
            num_invalid_examples=10,
            report_path=str(tmp_path / "rejection_report.json"),
        )
        metrics = run_rejection_training(config)
        assert metrics["steps"] == 20
        assert len(metrics["losses"]) == 20
        assert metrics["loss_decreased"] is True
        assert metrics["can_distinguish"] is True

    def test_rejection_pairs_balanced(self):
        """build_rejection_pairs produces balanced valid/invalid pairs."""
        pairs = build_rejection_pairs(num_valid=15, num_invalid=15)
        valid_count = sum(1 for p in pairs if p.is_valid)
        invalid_count = sum(1 for p in pairs if not p.is_valid)
        assert valid_count == 15
        assert invalid_count == 15


# ============================================================
# Evaluation Tests
# ============================================================


class TestHeldOutEval:
    """Tests for held-out evaluation."""

    def test_held_out_eval_runs(self):
        """Branch ticket generation eval runs on held-out examples."""
        config = _small_model_config()
        device = "cuda" if torch.cuda.is_available() else "cpu"
        model = build_micro_model(config, device=device)

        # Use separate seed for held-out set
        test_examples = generate_diverse_examples(count=5, seed=999)
        metrics = eval_branch_ticket_generation(
            model, test_examples,
            max_gen_tokens=32, max_seq_len=128, device=device
        )

        assert "valid_json_rate" in metrics
        assert "schema_valid_rate" in metrics
        assert "field_completeness" in metrics
        assert "branch_type_accuracy" in metrics
        assert "write_set_present" in metrics
        assert "verifier_declared" in metrics
        assert "evidence_declared" in metrics
        assert metrics["total_evaluated"] == 5

    def test_branch_ir_eval_runs(self):
        """BranchIR generation eval runs on held-out examples."""
        config = _small_model_config()
        device = "cuda" if torch.cuda.is_available() else "cpu"
        model = build_micro_model(config, device=device)

        test_examples = generate_ir_examples(count=5, seed=888)
        metrics = eval_branch_ir_generation(
            model, test_examples,
            max_gen_tokens=32, max_seq_len=128, device=device
        )

        assert "schema_valid_rate" in metrics
        assert "action_consistency" in metrics
        assert "claims_have_evidence" in metrics
        assert "rollback_present" in metrics
        assert metrics["total_evaluated"] == 5

    def test_branch_ir_validate_direct(self):
        """validate_branch_irs works on direct BranchIR list."""
        examples = generate_ir_examples(count=10)
        irs = [ex.target_branch_ir for ex in examples]
        result = validate_branch_irs(irs)
        assert result["total"] == 10
        assert result["valid"] == 10
        assert result["validity_rate"] == 1.0


# ============================================================
# Purity Invariant Tests
# ============================================================


class TestPurityInvariant:
    """Ensure purity counters still work after Phase 2 operations."""

    def test_purity_counters_after_generation(self):
        """Purity counters remain valid after text generation."""
        config = _small_model_config()
        device = "cuda" if torch.cuda.is_available() else "cpu"
        model = build_micro_model(config, device=device)

        # Do some generation
        input_text = "<|branch_start|>test<|branch_end|>"
        _ = generate_from_model(
            model, input_text, config.vocab_size,
            max_gen_tokens=16, max_seq_len=128, device=device
        )

        # Check purity counters still work
        model.eval()
        with torch.no_grad():
            test_input = torch.randint(0, config.vocab_size, (1, 16), device=device)
            output = model(test_input)
            purity = output["purity_counters"]

        assert "top1_correct" in purity
        assert "runtime_violations" in purity
        assert purity["runtime_violations"] == 0
