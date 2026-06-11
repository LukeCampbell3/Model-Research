"""RuntimeCoder CLI - command-line interface for Phase 0 and Phase 1 operations."""

import argparse
import json
import os
import sys


def cmd_validate_schemas(args):
    """Validate all schema fixtures."""
    from runtime_coder.data_pipeline.fixtures import generate_all_fixtures

    print("=" * 60)
    print("RuntimeCoder Phase 0 - Schema Validation")
    print("=" * 60)

    fixtures = generate_all_fixtures()
    all_valid = True

    for name, fixture in fixtures.items():
        errors = fixture.validate()
        status = "PASS" if not errors else "FAIL"
        if errors:
            all_valid = False
        print(f"  [{status}] {name}: {len(errors)} errors")
        for err in errors:
            print(f"        -> {err}")

    print("-" * 60)
    if all_valid:
        print("Result: ALL SCHEMAS VALID")
    else:
        print("Result: SOME SCHEMAS INVALID")
        return 1

    # Also test round-trip
    print("\nRound-trip serialization test:")
    for name, fixture in fixtures.items():
        json_str = fixture.to_json()
        restored = type(fixture).from_json(json_str)
        match = fixture.to_dict() == restored.to_dict()
        status = "PASS" if match else "FAIL"
        print(f"  [{status}] {name} round-trip")

    print("\nDone.")
    return 0


def cmd_list_special_tokens(args):
    """List all special tokens."""
    from runtime_coder.tokenizer.runtime_special_tokens import (
        SPECIAL_TOKEN_CATEGORIES,
        SPECIAL_TOKENS,
        SPECIAL_TOKEN_ID_OFFSET,
    )

    print("=" * 60)
    print("RuntimeCoder Phase 0 - Special Tokens Registry")
    print("=" * 60)

    total = 0
    for category, tokens in SPECIAL_TOKEN_CATEGORIES.items():
        print(f"\n  [{category.upper()}] ({len(tokens)} tokens)")
        for i, token in enumerate(tokens):
            tid = SPECIAL_TOKEN_ID_OFFSET + total + i
            print(f"    {tid}: {token}")
        total += len(tokens)

    print(f"\n{'=' * 60}")
    print(f"Total special tokens: {len(SPECIAL_TOKENS)}")

    # Uniqueness check
    unique = len(set(SPECIAL_TOKENS))
    if unique == len(SPECIAL_TOKENS):
        print(f"Uniqueness: ALL UNIQUE ({unique}/{len(SPECIAL_TOKENS)})")
    else:
        print(f"WARNING: DUPLICATES FOUND ({unique}/{len(SPECIAL_TOKENS)})")
        return 1

    return 0


def cmd_model_forward_smoke(args):
    """Run model forward pass smoke test."""
    import torch
    from runtime_coder.model.config import TinyRuntimeCoderConfig
    from runtime_coder.model.tiny_runtime_coder import TinyRuntimeCoder

    print("=" * 60)
    print("RuntimeCoder Phase 0 - Model Forward Smoke Test")
    print("=" * 60)

    config = TinyRuntimeCoderConfig()
    model = TinyRuntimeCoder(config)
    model.eval()

    print(f"\n  Config:")
    print(f"    vocab_size: {config.vocab_size}")
    print(f"    hidden_dim: {config.hidden_dim}")
    print(f"    num_heads: {config.num_heads}")
    print(f"    num_layers: {config.num_layers}")
    print(f"    max_seq_len: {config.max_seq_len}")
    print(f"    parameters: {model.num_parameters():,}")

    # Forward pass
    input_ids = torch.randint(0, config.vocab_size, (1, 32))
    with torch.no_grad():
        output = model(input_ids)

    logits = output["logits"]
    purity = output["purity_counters"]

    print(f"\n  Forward pass:")
    print(f"    input shape: {tuple(input_ids.shape)}")
    print(f"    logits shape: {tuple(logits.shape)}")
    print(f"    logits dtype: {logits.dtype}")

    print(f"\n  Purity counters:")
    for k, v in purity.items():
        print(f"    {k}: {v}")

    # Forward with labels (loss computation)
    labels = torch.randint(0, config.vocab_size, (1, 32))
    with torch.no_grad():
        output_with_loss = model(input_ids, labels=labels)

    loss = output_with_loss["loss"]
    print(f"\n  Loss computation:")
    print(f"    loss: {loss.item():.4f}")

    # Save results if output_dir specified
    output_dir = args.output_dir
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
        results = {
            "config": {
                "vocab_size": config.vocab_size,
                "hidden_dim": config.hidden_dim,
                "num_heads": config.num_heads,
                "num_layers": config.num_layers,
                "max_seq_len": config.max_seq_len,
            },
            "num_parameters": model.num_parameters(),
            "logits_shape": list(logits.shape),
            "loss": loss.item(),
            "purity_counters": purity,
        }
        report_path = os.path.join(output_dir, "model_forward_smoke.json")
        with open(report_path, "w") as f:
            json.dump(results, f, indent=2)
        print(f"\n  Report saved: {report_path}")

    print(f"\n{'=' * 60}")
    print("Result: FORWARD PASS OK")
    return 0


def cmd_generate_fixtures(args):
    """Generate and display all fixtures."""
    from runtime_coder.data_pipeline.fixtures import generate_all_fixtures

    print("=" * 60)
    print("RuntimeCoder Phase 0 - Fixture Generation")
    print("=" * 60)

    fixtures = generate_all_fixtures()
    for name, fixture in fixtures.items():
        print(f"\n  [{name}]")
        d = fixture.to_dict()
        for k, v in d.items():
            print(f"    {k}: {repr(v)[:80]}")

    print(f"\n{'=' * 60}")
    print(f"Generated {len(fixtures)} fixtures")
    return 0


def cmd_build_sft(args):
    """Build SFT examples from fixtures."""
    from runtime_coder.data_pipeline.sft_example_builder import build_sft_examples

    print("=" * 60)
    print("RuntimeCoder Phase 0 - SFT Example Builder")
    print("=" * 60)

    examples = build_sft_examples()
    for ex in examples:
        print(f"\n  [{ex['fixture_name']}]")
        print(f"    prompt: {ex['prompt'][:100]}...")
        print(f"    completion: {ex['completion'][:100]}")

    print(f"\n{'=' * 60}")
    print(f"Built {len(examples)} SFT examples")
    return 0


def cmd_eval_compliance(args):
    """Run runtime compliance evaluation."""
    from runtime_coder.data_pipeline.fixtures import generate_all_fixtures
    from runtime_coder.evals.runtime_compliance import compute_runtime_compliance

    print("=" * 60)
    print("RuntimeCoder Phase 0 - Runtime Compliance Eval")
    print("=" * 60)

    fixtures = generate_all_fixtures()
    tickets = [fixtures["branch_ticket"]]
    results = [fixtures["verifier_result"]]

    metrics = compute_runtime_compliance(tickets, results)
    for k, v in metrics.items():
        print(f"  {k}: {v:.4f}")

    print(f"\n{'=' * 60}")
    print("Result: COMPLIANCE EVAL COMPLETE")
    return 0


def cmd_tokenizer_smoke(args):
    """Run tokenizer smoke test."""
    from runtime_coder.tokenizer.tokenizer_smoke import RuntimeTokenizer

    print("=" * 60)
    print("RuntimeCoder Phase 0 - Tokenizer Smoke Test")
    print("=" * 60)

    tok = RuntimeTokenizer()
    print(f"  Vocab size: {tok.vocab_size}")
    print(f"  Special token count: {len(tok.special_token_ids())}")

    # Test encode/decode
    test_text = "<|task_start|>Hello world<|task_end|>"
    ids = tok.encode(test_text)
    decoded = tok.decode(ids)
    print(f"\n  Encode test:")
    print(f"    input:   {test_text}")
    print(f"    ids:     {ids[:10]}... ({len(ids)} total)")
    print(f"    decoded: {decoded}")
    print(f"    match:   {decoded == test_text}")

    print(f"\n{'=' * 60}")
    print("Result: TOKENIZER SMOKE OK")
    return 0


def cmd_train_pretrain_smoke(args):
    """Run pretraining smoke test (5 steps on synthetic data)."""
    from runtime_coder.training.train_pretrain import PretrainConfig, run_pretrain_smoke

    print("=" * 60)
    print("RuntimeCoder Phase 1 - Pretrain Smoke Test")
    print("=" * 60)

    config = PretrainConfig()
    if args.output_dir:
        config.report_path = os.path.join(args.output_dir, "pretrain_smoke_report.json")

    metrics = run_pretrain_smoke(config)

    print(f"\n{'=' * 60}")
    print(f"Result: {'LOSS DECREASED' if metrics.get('loss_decreased') else 'LOSS DID NOT DECREASE'}")
    print(f"  Final loss: {metrics['losses'][-1]:.4f}")
    print(f"  Avg tok/s: {metrics['avg_tokens_per_sec']:.0f}")
    return 0 if metrics.get("loss_decreased") else 1


def cmd_train_branch_sft_smoke(args):
    """Run branch SFT smoke test (3 steps on fixture data)."""
    from runtime_coder.training.train_branch_sft import BranchSFTConfig, run_branch_sft_smoke

    print("=" * 60)
    print("RuntimeCoder Phase 1 - Branch SFT Smoke Test")
    print("=" * 60)

    config = BranchSFTConfig()
    if args.output_dir:
        config.report_path = os.path.join(args.output_dir, "branch_sft_smoke_report.json")

    metrics = run_branch_sft_smoke(config)

    print(f"\n{'=' * 60}")
    print(f"Result: BRANCH SFT SMOKE COMPLETE")
    print(f"  Final loss: {metrics['losses'][-1]:.4f}")
    print(f"  Branch tokens present: {metrics['special_token_validation']['branch_tokens_present']}")
    return 0


def cmd_train_branch_sft_full(args):
    """Run full Branch SFT training (Phase 2)."""
    from runtime_coder.training.train_branch_sft import BranchSFTFullConfig, run_branch_sft_full

    print("=" * 60)
    print("RuntimeCoder Phase 2 - Full Branch SFT Training")
    print("=" * 60)

    config = BranchSFTFullConfig()
    if args.output_dir:
        config.report_path = os.path.join(args.output_dir, "branch_sft_full_report.json")

    metrics = run_branch_sft_full(config)

    print(f"\n{'=' * 60}")
    print(f"Result: BRANCH SFT FULL COMPLETE")
    print(f"  Steps: {metrics['steps']}")
    print(f"  Final loss: {metrics['losses'][-1]:.4f}")
    print(f"  Loss decreased: {metrics['loss_decreased']}")
    print(f"  Final schema validity rate: {metrics['final_schema_validity_rate']:.3f}")
    print(f"  Final field completeness: {metrics['final_field_completeness_rate']:.3f}")
    return 0


def cmd_eval_branch_validity(args):
    """Evaluate BranchTicket generation quality."""
    from runtime_coder.data_pipeline.branch_ticket_dataset import generate_diverse_examples
    from runtime_coder.evals.branch_ticket_validity import eval_branch_ticket_generation
    from runtime_coder.model.runtime_coder_micro import RuntimeCoderMicroConfig, build_micro_model

    print("=" * 60)
    print("RuntimeCoder Phase 2 - Branch Ticket Validity Eval")
    print("=" * 60)

    device = "cuda" if __import__("torch").cuda.is_available() else "cpu"
    config = RuntimeCoderMicroConfig()
    model = build_micro_model(config, device=device)

    # Held-out examples (different seed)
    test_examples = generate_diverse_examples(count=20, seed=777)
    metrics = eval_branch_ticket_generation(
        model, test_examples, device=device
    )

    for k, v in metrics.items():
        if isinstance(v, float):
            print(f"  {k}: {v:.4f}")
        else:
            print(f"  {k}: {v}")

    # Save report
    output_dir = args.output_dir or "evaluation/runtime_coder_phase2"
    os.makedirs(output_dir, exist_ok=True)
    report_path = os.path.join(output_dir, "branch_validity_eval_report.json")
    with open(report_path, "w") as f:
        json.dump(metrics, f, indent=2, default=str)
    print(f"\n  Report saved: {report_path}")

    print(f"\n{'=' * 60}")
    print("Result: BRANCH VALIDITY EVAL COMPLETE")
    return 0


def cmd_build_branch_dataset(args):
    """Build the diverse BranchTicket dataset."""
    from runtime_coder.data_pipeline.branch_ticket_dataset import (
        generate_diverse_examples,
        generate_invalid_examples,
    )
    from runtime_coder.data_pipeline.branch_ir_dataset import generate_ir_examples

    print("=" * 60)
    print("RuntimeCoder Phase 2 - Build Branch Dataset")
    print("=" * 60)

    # Generate main dataset
    valid_examples = generate_diverse_examples(count=100)
    invalid_examples = generate_invalid_examples(count=30)
    ir_examples = generate_ir_examples(count=50)

    print(f"  Valid BranchTicket examples: {len(valid_examples)}")
    print(f"  Invalid BranchTicket examples: {len(invalid_examples)}")
    print(f"  BranchIR examples: {len(ir_examples)}")

    # Task type distribution
    from collections import Counter
    type_dist = Counter(ex.task_type for ex in valid_examples)
    print(f"\n  Task type distribution:")
    for tt, count in sorted(type_dist.items()):
        print(f"    {tt}: {count}")

    # Branch type distribution
    bt_dist = Counter(ex.target_branch_ticket.branch_type for ex in valid_examples)
    print(f"\n  Branch type distribution:")
    for bt, count in sorted(bt_dist.items()):
        print(f"    {bt}: {count}")

    # Save dataset summary
    output_dir = args.output_dir or "evaluation/runtime_coder_phase2"
    os.makedirs(output_dir, exist_ok=True)
    summary = {
        "valid_examples": len(valid_examples),
        "invalid_examples": len(invalid_examples),
        "ir_examples": len(ir_examples),
        "task_type_distribution": dict(type_dist),
        "branch_type_distribution": dict(bt_dist),
    }
    report_path = os.path.join(output_dir, "dataset_summary.json")
    with open(report_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\n  Summary saved: {report_path}")

    print(f"\n{'=' * 60}")
    print("Result: DATASET BUILT")
    return 0


def cmd_eval_pretrain(args):
    """Run pretraining evaluation metrics."""
    from runtime_coder.data_pipeline.fim_dataset import build_fim_dataset
    from runtime_coder.evals.pretraining_eval import (
        eval_fim_completion,
        eval_perplexity,
        eval_special_token_retention,
    )
    from runtime_coder.model.runtime_coder_micro import (
        RuntimeCoderMicroConfig,
        build_micro_model,
    )

    print("=" * 60)
    print("RuntimeCoder Phase 1 - Pretraining Evaluation")
    print("=" * 60)

    device = "cuda" if __import__("torch").cuda.is_available() else "cpu"
    config = RuntimeCoderMicroConfig()
    model = build_micro_model(config, device=device)

    # Perplexity
    dataset = [
        "def binary_search(arr, target):\n    left, right = 0, len(arr) - 1\n    return -1\n",
        "class DataProcessor:\n    def __init__(self):\n        self.data = []\n",
        "import torch\nimport torch.nn as nn\n",
    ]
    ppl = eval_perplexity(model, dataset, device=device)
    print(f"\n  Perplexity: {ppl:.2f}")

    # FIM evaluation
    fim_examples = build_fim_dataset(dataset, count=5, fim_rate=1.0, seed=42)
    fim_metrics = eval_fim_completion(model, fim_examples, device=device)
    print(f"  FIM loss: {fim_metrics['fim_loss']:.4f}")
    print(f"  FIM perplexity: {fim_metrics['fim_perplexity']:.2f}")

    # Special token retention
    retention = eval_special_token_retention(model, device=device)
    print(f"  Special tokens in vocab: {retention['special_tokens_in_vocab']}")
    print(f"  All logits finite: {retention['all_logits_finite']}")
    print(f"  No garbage logits: {retention['no_garbage_logits']}")

    # Save report
    report = {
        "perplexity": ppl,
        "fim_metrics": fim_metrics,
        "special_token_retention": retention,
    }
    output_dir = args.output_dir or "evaluation/runtime_coder_phase1"
    os.makedirs(output_dir, exist_ok=True)
    report_path = os.path.join(output_dir, "pretrain_eval_report.json")
    # Convert non-serializable values
    for k, v in report.get("special_token_retention", {}).items():
        if isinstance(v, bool):
            report["special_token_retention"][k] = v
    with open(report_path, "w") as f:
        json.dump(report, f, indent=2, default=str)
    print(f"\n  Report saved: {report_path}")

    print(f"\n{'=' * 60}")
    print("Result: PRETRAIN EVAL COMPLETE")
    return 0


def main():
    parser = argparse.ArgumentParser(
        prog="runtime_coder",
        description="RuntimeCoder-v1 Phase 0+1+2 CLI",
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # validate-schemas
    sub = subparsers.add_parser("validate-schemas", help="Validate all schema fixtures")
    sub.set_defaults(func=cmd_validate_schemas)

    # list-special-tokens
    sub = subparsers.add_parser("list-special-tokens", help="List all special tokens")
    sub.set_defaults(func=cmd_list_special_tokens)

    # model-forward-smoke
    sub = subparsers.add_parser("model-forward-smoke", help="Run model forward smoke test")
    sub.add_argument("--output-dir", default="", help="Directory to save results")
    sub.set_defaults(func=cmd_model_forward_smoke)

    # generate-fixtures
    sub = subparsers.add_parser("generate-fixtures", help="Generate all fixtures")
    sub.set_defaults(func=cmd_generate_fixtures)

    # build-sft
    sub = subparsers.add_parser("build-sft", help="Build SFT examples")
    sub.set_defaults(func=cmd_build_sft)

    # eval-compliance
    sub = subparsers.add_parser("eval-compliance", help="Run compliance evaluation")
    sub.set_defaults(func=cmd_eval_compliance)

    # tokenizer-smoke
    sub = subparsers.add_parser("tokenizer-smoke", help="Run tokenizer smoke test")
    sub.set_defaults(func=cmd_tokenizer_smoke)

    # Phase 1 commands

    # train-pretrain-smoke
    sub = subparsers.add_parser("train-pretrain-smoke", help="Run pretrain smoke test (5 steps)")
    sub.add_argument("--output-dir", default="", help="Directory to save results")
    sub.set_defaults(func=cmd_train_pretrain_smoke)

    # train-branch-sft-smoke
    sub = subparsers.add_parser("train-branch-sft-smoke", help="Run branch SFT smoke test (3 steps)")
    sub.add_argument("--output-dir", default="", help="Directory to save results")
    sub.set_defaults(func=cmd_train_branch_sft_smoke)

    # eval-pretrain
    sub = subparsers.add_parser("eval-pretrain", help="Run pretraining evaluation")
    sub.add_argument("--output-dir", default="", help="Directory to save results")
    sub.set_defaults(func=cmd_eval_pretrain)

    # Phase 2 commands

    # train-branch-sft-full
    sub = subparsers.add_parser("train-branch-sft-full", help="Run full Branch SFT training (50+ steps)")
    sub.add_argument("--output-dir", default="", help="Directory to save results")
    sub.set_defaults(func=cmd_train_branch_sft_full)

    # eval-branch-validity
    sub = subparsers.add_parser("eval-branch-validity", help="Evaluate BranchTicket generation quality")
    sub.add_argument("--output-dir", default="", help="Directory to save results")
    sub.set_defaults(func=cmd_eval_branch_validity)

    # build-branch-dataset
    sub = subparsers.add_parser("build-branch-dataset", help="Build the diverse BranchTicket dataset")
    sub.add_argument("--output-dir", default="", help="Directory to save results")
    sub.set_defaults(func=cmd_build_branch_dataset)

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return 1

    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())


# Support python -m runtime_coder.cli
