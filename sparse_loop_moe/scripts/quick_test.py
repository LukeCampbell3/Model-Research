"""Quick test script to verify the full system works end-to-end.

Runs a minimal training loop with the full Sparse Loop-MoE architecture
to confirm all components integrate correctly.
"""

import sys
import torch

sys.path.insert(0, "src")

from sparse_loop_moe.core.cognitive_state import CognitiveState
from sparse_loop_moe.core.cognitive_kernel import CognitiveKernel, KernelConstraints
from sparse_loop_moe.core.types import LoopStats, ProbeSignals, ReflectionAction
from sparse_loop_moe.models.dense_transformer import DenseTransformer, DenseTransformerConfig
from sparse_loop_moe.models.full_model import SparseLoopMoEModel, SparseLoopMoEConfig
from sparse_loop_moe.training.data_generation import SyntheticTaskGenerator
from sparse_loop_moe.training.losses import CombinedLoss
from sparse_loop_moe.memory.memory_store import MemoryStore
from sparse_loop_moe.verification.verifier import Verifier
from sparse_loop_moe.verification.sandbox import SandboxedModification, ModificationProposal


def test_cognitive_state():
    """Test cognitive state creation and manipulation."""
    print("Testing CognitiveState...")
    state = CognitiveState(
        task_goal="test",
        uncertainty=0.7,
        ambiguity=0.5,
        expected_risk=0.3,
    )
    compute_need = state.compute_need()
    assert 0 < compute_need < 1, f"Unexpected compute_need: {compute_need}"
    tensor = state.to_tensor()
    assert tensor.shape == (10,), f"Unexpected shape: {tensor.shape}"
    print(f"  compute_need={compute_need:.4f}, tensor_shape={tensor.shape} ✓")


def test_cognitive_kernel():
    """Test kernel immutability and validation."""
    print("Testing CognitiveKernel...")
    kernel = CognitiveKernel()
    assert kernel.validate_loop_count(5)
    assert not kernel.validate_loop_count(100)
    assert kernel.validate_expert_count(4)
    assert not kernel.validate_expert_count(10)
    assert kernel.validate_modification("fast_memory")
    assert not kernel.validate_modification("cognitive_kernel")

    # Test immutability
    try:
        kernel._constraints = None
        assert False, "Should have raised AttributeError"
    except AttributeError:
        pass

    print("  All kernel validations passed ✓")


def test_dense_baseline():
    """Test dense transformer baseline."""
    print("Testing DenseTransformer...")
    config = DenseTransformerConfig(
        vocab_size=128, d_model=64, n_heads=2, n_layers=2, d_ff=128, max_seq_len=32
    )
    model = DenseTransformer(config)
    params = model.count_parameters()

    input_ids = torch.randint(0, 128, (2, 16))
    targets = torch.randint(0, 128, (2, 16))
    output = model(input_ids, targets)

    assert "logits" in output
    assert "loss" in output
    assert output["logits"].shape == (2, 16, 128)
    print(f"  params={params:,}, loss={output['loss'].item():.4f} ✓")


def test_sparse_loop_moe():
    """Test full Sparse Loop-MoE model."""
    print("Testing SparseLoopMoEModel...")
    config = SparseLoopMoEConfig(
        vocab_size=128,
        d_model=64,
        n_heads=2,
        n_layers=2,
        d_ff=128,
        num_experts=4,
        max_k=2,
        max_loops=4,
        max_seq_len=32,
        use_adaptive_router=True,
        use_probes=True,
        use_reflection=True,
        use_shared_expert=True,
        use_loops=True,
    )
    model = SparseLoopMoEModel(config)
    params = model.count_parameters()

    input_ids = torch.randint(0, 128, (2, 16))
    targets = torch.randint(0, 128, (2, 16))
    output = model(input_ids, targets)

    assert "logits" in output
    assert "loss" in output
    assert "loop_stats" in output
    assert "cognitive_state" in output
    assert output["logits"].shape == (2, 16, 128)

    loop_stats = output["loop_stats"]
    assert len(loop_stats) == 2  # n_layers
    for stats in loop_stats:
        assert isinstance(stats, LoopStats)
        assert stats.loops_used >= 1

    compute_summary = model.get_compute_summary(loop_stats)
    print(f"  params={params:,}, loss={output['loss'].item():.4f}")
    print(f"  loops={compute_summary['total_loops']}, "
          f"avg_experts={compute_summary['avg_experts_per_step']:.1f}, "
          f"halt_rate={compute_summary['halt_rate']:.2f} ✓")


def test_data_generation():
    """Test synthetic data generation."""
    print("Testing SyntheticTaskGenerator...")
    gen = SyntheticTaskGenerator(vocab_size=128, max_seq_len=64)

    # Test individual task types
    sample = gen.generate_addition_task(num_digits=2)
    assert sample.input_ids.shape == (64,)
    assert sample.metadata["task_type"] == "addition"

    sample = gen.generate_sorting_task(list_length=4)
    assert sample.metadata["task_type"] == "sorting"

    sample = gen.generate_hidden_constraint_task()
    assert sample.metadata["has_hidden_constraints"]

    # Test batch generation
    batch = gen.generate_batch(batch_size=16)
    assert len(batch) == 16
    print(f"  Generated 16 mixed samples, types: "
          f"{set(s.metadata['task_type'] for s in batch)} ✓")


def test_memory_store():
    """Test memory architecture."""
    print("Testing MemoryStore...")
    store = MemoryStore(d_model=64)

    # Fast memory
    store.fast.write("key1", "value1")
    assert store.fast.read("key1") == "value1"

    # Episodic memory
    key = torch.randn(64)
    store.episodic.store(key, {"task": "test", "result": "success"})
    results = store.episodic.retrieve(key, top_k=1)
    assert len(results) == 1

    # Task lifecycle
    store.task_start()
    assert len(store.fast) == 0  # Cleared

    store.task_end(
        task_embedding=torch.randn(64),
        outcome={"success": True, "pattern_key": "test_pattern"},
    )
    assert len(store.episodic) == 2  # Original + new

    print("  All memory operations passed ✓")


def test_verifier():
    """Test verification layer."""
    print("Testing Verifier...")
    verifier = Verifier(d_model=64, num_constraints=4)

    output_hidden = torch.randn(64)
    input_hidden = torch.randn(64)

    result = verifier(output_hidden, input_hidden, min_confidence=0.3)
    assert hasattr(result, "passed")
    assert hasattr(result, "confidence")
    assert 0 <= result.confidence <= 1
    print(f"  passed={result.passed}, confidence={result.confidence:.4f} ✓")


def test_sandbox():
    """Test sandboxed modification layer."""
    print("Testing SandboxedModification...")
    kernel = CognitiveKernel()
    sandbox = SandboxedModification(kernel)
    state = CognitiveState(uncertainty=0.5)

    # Valid proposal
    proposal = ModificationProposal(
        target="active_assumptions",
        description="Add assumption about input format",
        new_value=["input is numeric"],
        confidence=0.8,
    )
    assert sandbox.propose(proposal)

    # Invalid proposal (kernel modification)
    bad_proposal = ModificationProposal(
        target="cognitive_kernel",
        description="Try to modify kernel",
        new_value="hacked",
    )
    assert not sandbox.propose(bad_proposal)

    # Evaluate in sandbox
    result = sandbox.evaluate_in_sandbox(
        proposal, state, score_fn=lambda s: 1.0 - s.uncertainty
    )
    print(f"  proposal_approved={result.approved}, "
          f"improvement={result.improvement:.4f} ✓")


def test_training_step():
    """Test a single training step end-to-end."""
    print("Testing training step...")
    config = SparseLoopMoEConfig(
        vocab_size=128, d_model=64, n_heads=2, n_layers=2,
        d_ff=128, num_experts=4, max_k=2, max_loops=3, max_seq_len=32,
        use_adaptive_router=True, use_probes=True, use_reflection=True,
        use_shared_expert=True, use_loops=True,
    )
    model = SparseLoopMoEModel(config)
    optimizer = torch.optim.AdamW(model.parameters(), lr=1e-3)
    loss_fn = CombinedLoss()

    # Generate data
    gen = SyntheticTaskGenerator(vocab_size=128, max_seq_len=32)
    batch = gen.generate_batch(batch_size=4)
    input_ids = torch.stack([s.input_ids for s in batch])
    target_ids = torch.stack([s.target_ids for s in batch])

    # Forward
    model.train()
    output = model(input_ids, target_ids)

    # Loss
    total_loss, components = loss_fn(
        task_loss=output["loss"],
        aux_losses=output.get("aux_losses", {}),
        loop_stats=output.get("loop_stats", []),
    )

    # Backward
    optimizer.zero_grad()
    total_loss.backward()
    grad_norm = torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
    optimizer.step()

    print(f"  total_loss={total_loss.item():.4f}, "
          f"grad_norm={grad_norm:.4f}, "
          f"components={list(components.keys())} ✓")


def test_ablation_configs():
    """Test that all ablation configs are valid."""
    print("Testing ablation configurations...")
    from sparse_loop_moe.experiments.ablation_configs import (
        get_experiment_matrix,
        get_ablation_configs,
        get_critical_comparison,
    )

    matrix = get_experiment_matrix()
    assert len(matrix) == 9, f"Expected 9 configs, got {len(matrix)}"

    ablations = get_ablation_configs()
    assert len(ablations) >= 7, f"Expected ≥7 ablations, got {len(ablations)}"

    adaptive, random = get_critical_comparison()
    assert adaptive.name != random.name

    print(f"  matrix={len(matrix)} configs, "
          f"ablations={len(ablations)} configs, "
          f"critical_pair=({adaptive.name}, {random.name}) ✓")


def main():
    print("=" * 60)
    print("Sparse Loop-MoE Research Testbed — Quick Validation")
    print("=" * 60)
    print()

    tests = [
        test_cognitive_state,
        test_cognitive_kernel,
        test_dense_baseline,
        test_sparse_loop_moe,
        test_data_generation,
        test_memory_store,
        test_verifier,
        test_sandbox,
        test_training_step,
        test_ablation_configs,
    ]

    passed = 0
    failed = 0

    for test in tests:
        try:
            test()
            passed += 1
        except Exception as e:
            print(f"  FAILED: {e}")
            failed += 1
        print()

    print("=" * 60)
    print(f"Results: {passed} passed, {failed} failed, {len(tests)} total")
    print("=" * 60)

    if failed > 0:
        sys.exit(1)
    else:
        print("\n✓ All systems operational. Ready for experiments.")


if __name__ == "__main__":
    main()
