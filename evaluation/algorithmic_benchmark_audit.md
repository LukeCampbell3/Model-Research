# Algorithmic Benchmark Audit

## Discovery Summary

**Date:** 2026-06-03
**System:** Sparse Loop-MoE Research Testbed

## Model Interface

| Property | Value |
|----------|-------|
| Input format | Integer token sequences (torch.Tensor) |
| Output format | Next-token logits over vocab |
| Vocab size | 256-512 (configurable) |
| Special tokens | PAD=0, BOS=1, EOS=2, SEP=3 |
| Digit tokens | 4-13 (digits 0-9) |
| Operator tokens | 14+ (PLUS=14, EQUALS=15, ARROW=16, etc.) |
| Max seq len | 128-256 (configurable) |
| Task format | Sequence-to-sequence via next-token prediction |
| Loss | Cross-entropy on target tokens |
| Evaluation | Token accuracy on non-padding positions |

## Compatible Benchmark Families

### 1. CLRS-Style Algorithmic Reasoning (ADAPTED)
- **Status:** IMPLEMENTABLE as sequence-encoded tasks
- **Fidelity:** Faithful task structure, sequence encoding instead of graph tensors
- **Tasks:** Sorting, searching, string matching, DP subsequences
- **Label:** CLRS_STYLE_SEQUENCE_ADAPTER (not official CLRS)
- **Why adapted:** Official CLRS uses structured graph/pointer inputs incompatible with flat token sequences

### 2. ListOps-Style Long-Range Compositional Reasoning
- **Status:** DIRECTLY IMPLEMENTABLE
- **Fidelity:** Faithful — ListOps is natively a token-sequence task
- **Tasks:** Nested list operations with variable depth/length
- **Label:** LISTOPS_FAITHFUL_IMPLEMENTATION
- **Note:** ListOps was designed for exactly this kind of evaluation

### 3. SCAN-Style Compositional Generalization
- **Status:** IMPLEMENTABLE with symbolic command vocabulary
- **Fidelity:** Faithful structure, commands encoded as symbolic tokens (not English text)
- **Tasks:** Command-to-action mapping with systematic splits
- **Label:** SCAN_STYLE_SYMBOLIC_ADAPTER
- **Splits:** Random, length, primitive (jump)

### 4. Dyck Language Bracket Reasoning
- **Status:** DIRECTLY IMPLEMENTABLE
- **Fidelity:** Perfect — Dyck languages are natively token sequences
- **Tasks:** Multi-type bracket validation, next-token prediction, depth generalization
- **Label:** DYCK_FAITHFUL_IMPLEMENTATION

## Model Variants Available

| Variant | Adaptive Router | Probes | Reflection | Loops | Shared Expert |
|---------|----------------|--------|------------|-------|---------------|
| dense_baseline | No | No | No | No | No |
| fixed_moe | No (top-2) | No | No | No | Yes |
| adaptive_moe | Yes | No | No | No | Yes |
| looped_moe | No (top-2) | No | No | Yes (4) | Yes |
| full_system | Yes | Yes | Yes | Yes (4) | Yes |

## Current Blockers

- **NLP benchmarks:** Blocked (no text tokenizer, vocab too small)
- **Official CLRS:** Requires graph/tensor inputs (adapted version needed)
- **GPU:** Not available (CPU only, limits training steps)

## Assumptions

1. ListOps and Dyck are directly compatible — no adapter needed beyond token encoding
2. CLRS tasks are adapted to flat sequences — clearly labeled as adapted
3. SCAN commands use symbolic tokens instead of English words — documented
4. All benchmark families use the same model interface (input_ids → logits)
5. Training budget limited by CPU — 50-100 steps for lite, 200+ for full
