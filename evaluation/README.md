# Evaluation — Sparse Loop-MoE Architecture Benchmark

## What This Evaluates

This is **NOT** a standard NLP benchmark. This repository contains a research testbed
with tiny models (128-dim to 256-dim, 512-token vocab) that solve synthetic algorithmic tasks.

The benchmark evaluates the **architectural innovations** (adaptive routing, bounded looping,
probe heads, self-reflection) by comparing 5 model variants on 9 controlled synthetic datasets.

## Why Not Standard NLP Benchmarks?

| Limitation | Detail |
|------------|--------|
| Vocab too small | 256-512 custom tokens (not a real tokenizer) |
| No language modeling | Trained on synthetic arithmetic/sorting/logic only |
| Tiny models | 314K-1.1M params (research scale, not language capable) |
| No pretrained weights | Trains from scratch each run |
| Custom encoding | Digits/operators as special tokens, not text |

Standard benchmarks (MMLU, ARC, GSM8K, HumanEval) would produce **random performance**
because these models cannot process natural language.

## What IS Evaluated

### Models (5 variants, same data, same hyperparameters)

1. **Dense baseline** — Standard transformer, no MoE, no loops (314K params)
2. **Fixed MoE** — Top-2 MoE with shared expert, no loops (985K params)
3. **Adaptive MoE** — Adaptive width routing, no loops (1M params)
4. **Looped MoE** — Fixed routing + 8 bounded loops (985K params)
5. **Full system** — Adaptive + loops + probes + reflection (1.1M params)

### Datasets (9 synthetic, auto-labeled)

- Addition (easy/hard) — arithmetic with/without distractors
- Sorting (easy/hard) — list ordering by size
- Parentheses (easy/hard) — bracket matching with/without noise
- Multi-hop lookup (easy/hard) — chain reasoning through tables
- Hidden constraint — rule induction from examples

### Metrics

- **accuracy** — Token-level prediction correctness (non-padding)
- **loss** — Cross-entropy training loss
- **quality_per_compute** — accuracy / (avg_loops * avg_experts)
- **avg_loops** — Mean loop iterations per block
- **halt_rate** — Early stopping frequency
- **oscillation_rate** — Spinlock detection rate

## Running

```bash
# Verify pipeline (20 steps, ~2 min)
python -X utf8 evaluation/run_benchmarks.py --mode smoke

# Partial evidence (500 steps, ~2.5 hours on CPU)
python -X utf8 evaluation/run_benchmarks.py --mode benchmark-lite

# Full evidence (2000 steps, ~10 hours on CPU or ~1 hour on GPU)
python -X utf8 evaluation/run_benchmarks.py --mode benchmark-full
```

## Output Artifacts

```
evaluation/benchmark_results/latest/
  per_dataset_metrics.csv          # Raw metrics per model per dataset
  per_dataset_metrics.json
  baseline_comparison.csv          # Pairwise comparisons
  baseline_comparison.json
  aggregate_summary.json           # Summary with recommendation
  benchmark_report.md              # Human-readable report
  reproducibility_manifest.json    # Hardware, versions, config
```

## Current Status

- **Pipeline: VERIFIED** (smoke mode passes, all 5 models train and evaluate)
- **Evidence: INSUFFICIENT** (only smoke mode run due to CPU time constraints)
- **Recommendation: HOLD_NEEDS_MORE_EVIDENCE**

To produce valid evidence, run benchmark-lite or benchmark-full on a machine with GPU.
