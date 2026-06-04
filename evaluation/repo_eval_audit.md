# Repository Evaluation Audit

## Discovery Summary

**Repository:** `brain` (C:\Users\jcthi\Code\brain)  
**Date:** 2026-06-02  
**Auditor:** Automated ML Evaluation Engineer

---

## System Classification

| Component | Type | Can Run Inference | Can Benchmark Against Standard NLP |
|-----------|------|-------------------|------------------------------------|
| sparse_loop_moe | Research transformer (tiny, synthetic-only) | YES | **NO** |
| cognitive_microkernel | Rule-based process runtime | YES (non-neural) | **NO** |

## Discovered Model/System Entry Points

### sparse_loop_moe
- `SparseLoopMoEModel.forward()` — main neural forward pass (input_ids → logits)
- `DenseTransformer.forward()` — dense baseline forward pass
- `ExperimentRunner.run_single()` — full train+eval pipeline
- `scripts/quick_test.py` — validation harness
- `scripts/run_from_config.py` — config-driven experiments

### cognitive_microkernel
- `Runtime.execute_minimal_loop(observation: str)` — orchestration pipeline
- Mock experts (PlannerExpert, VerifierExpert, ClaimExtractorExpert) — stub implementations

## Supported Task Types

### sparse_loop_moe (synthetic algorithmic)
- Addition (with/without distractors) — arithmetic reasoning
- Sorting — sequence ordering
- Parentheses matching — structural validation
- Multi-hop lookup — chain reasoning
- Hidden constraint discovery — rule induction

### cognitive_microkernel (non-neural)
- Branch generation
- Claim/evidence management
- Transaction commit/rollback
- Process replay

## Available Configs

- `sparse_loop_moe/configs/quick_test.yaml` — tiny model (64-dim, 4 experts, 100 steps)
- `sparse_loop_moe/configs/full_experiment.yaml` — research scale (256-dim, 8 experts, 10K steps)

## Existing Metrics

- accuracy, exact_match, pass_at_1, validation_pass_rate
- quality_per_compute, routing_entropy, expert_utilization
- avg_loops_used, halt_accuracy, spinlock_rate, oscillation_rate
- reflection_trigger_accuracy, revision_success_rate, risk_adjusted_quality_per_compute

## Existing Tests

- `sparse_loop_moe/scripts/quick_test.py` — 10 component tests (all pass)
- `cognitive_microkernel/tests/test_core.py` — 49 tests (all pass)
- `cognitive_microkernel/demo/run_demos.py` — 4 integration demos (all pass)

## Evaluation Gaps

### CRITICAL: Cannot benchmark against standard NLP datasets

| Reason | Detail |
|--------|--------|
| Vocabulary too small | 128-512 custom tokens vs 32K+ needed for language |
| No real tokenizer | Custom digit/operator encoding, not BPE/SentencePiece |
| No language modeling | Trained on synthetic algorithmic patterns only |
| Tiny model size | ~350K params (full) / ~77K params (dense baseline) |
| No pretrained weights | Trains from scratch each run |
| No text generation | No autoregressive decode loop for free-form text |

### What CAN be evaluated

The system's **architectural innovations** can be evaluated by:
1. Training all 9 model variants on identical synthetic tasks
2. Comparing accuracy, loss, and quality-per-compute across variants
3. Running the full ablation matrix
4. Running the critical comparison (adaptive vs random loop depth)
5. Measuring whether adaptive compute allocation actually improves outcomes

## Assumptions Made

1. The research value is in comparing **architecture variants** on synthetic tasks, not NLP capability
2. The correct benchmark is the internal experiment matrix (9 configs + 7 ablations + critical comparison)
3. Standard NLP benchmarks are inappropriate and would produce meaningless results (random performance)
4. The evaluation should focus on: Does adaptive sparse compute beat fixed compute? Does reflection beat no reflection? Do probes help?

## Recommendation

**CANNOT evaluate against standard NLP benchmarks.** The system was designed as a research testbed for architectural innovations, not as a language model.

**CAN evaluate:** The full experiment matrix comparing architectural variants, which is what the system was designed to answer. This is scientifically valid because:
- All variants use the same synthetic data (controlled variable)
- Tasks have automatic ground truth labels
- Tasks are parameterized by difficulty, uncertainty, ambiguity
- Metrics include both accuracy AND compute efficiency

**Appropriate benchmark approach:**
1. Run the full 9-variant experiment matrix with sufficient training steps
2. Run all 7 ablation studies
3. Run the critical adaptive-vs-random comparison
4. Report per-task-family results (easy/medium/hard, by task type)
5. Compare quality-per-compute ratios
6. Report statistical confidence via multiple seeds
