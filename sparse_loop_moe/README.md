# Sparse Loop-MoE Research Testbed

## Core Research Question

Can a small model improve quality-per-compute on ambiguous, long-horizon, or underdefined tasks
by dynamically allocating expert width, loop depth, latent probes, self-reflection, and validation
instead of using fixed one-pass inference?

## Architecture

The system treats the model as a **cognitive runtime** that constructs, refines, evaluates, and
commits internal state — not a static input-output function.

### Layers

1. **Cognitive Kernel** — Immutable invariants, safety rules, reasoning constraints
2. **Representation State Layer** — Structured internal state per task
3. **Sparse Loop-MoE Runtime** — Adaptive expert width + bounded loop depth
4. **Self-Reflection Layer** — Metacognitive controller with probe heads
5. **Sandboxed Modification Layer** — Propose → sandbox → evaluate → commit
6. **Memory Architecture** — Fast / Episodic / Semantic / Adapter / Sparse slots

### Implementation Phases

- Phase 1: Dense Transformer Baseline
- Phase 2: Fixed Sparse MoE Baseline
- Phase 3: Adaptive Expert Width
- Phase 4: Bounded Loop Depth
- Phase 5: Latent Probe Heads
- Phase 6: Self-Reflection Controller
- Phase 7: Anti-Spinlock Controls
- Phase 8: Memory and Consolidation
- Phase 9: Full Experiment Matrix

## Running

```bash
pip install -e .
python -m sparse_loop_moe.experiments.run_experiment --config configs/full_experiment.yaml
```

## Scientific Framing

This scaled proxy tests whether adaptive sparse compute, bounded latent recurrence,
self-reflection, and memory isolation improve risk-adjusted quality-per-compute on
ambiguous, underdefined, and long-horizon tasks.
