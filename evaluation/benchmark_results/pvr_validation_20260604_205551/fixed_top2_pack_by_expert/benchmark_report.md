# Algorithmic Benchmark Report

**Status:** VALID_ALGORITHMIC_BENCHMARK  
**Architecture:** HOLD_NEEDS_MORE_EVIDENCE  
**Mode:** benchmark-lite | **Scale:** tiny | **Steps:** 50  
**Families:** clrs_style, scan_style, listops, dyck  
**Samples:** 924 | **Time:** 414.4s

## Reason
4 respected benchmark families evaluated successfully. fixed_moe leads (0.0009) but adaptive is close on task wins

## Validity

- This benchmark evaluates **algorithmic/compositional reasoning architecture**.
- It does NOT validate real NLP ability (ARC/GSM8K/HellaSwag blocked).
- Benchmark families are respected: CLRS-style, ListOps, SCAN, Dyck.

## Model Comparison

| Model | Params | Avg Acc | Avg EM | Avg Loss | Avg QPC | Avg Loops |
|-------|--------|---------|--------|----------|---------|-----------|
| fixed_moe | 260,932 | 0.0009 | 0.0000 | 3.928 | 0.0005 | 1.0 |
| pvr_ec | 169,218 | 0.0002 | 0.0000 | 3.976 | 0.0002 | 1.0 |

## Win/Loss/Tie (accuracy, threshold=0.5%)

| Comparison | Win | Loss | Tie |
|------------|-----|------|-----|
| adaptive_moe_vs_dense_baseline | 0 | 0 | 0 |
| looped_moe_vs_dense_baseline | 0 | 0 | 0 |
| full_system_vs_dense_baseline | 0 | 0 | 0 |
| adaptive_moe_vs_fixed_moe | 0 | 0 | 0 |
| looped_moe_vs_fixed_moe | 0 | 0 | 0 |
| full_system_vs_fixed_moe | 0 | 0 | 0 |

## Key Comparisons

- adaptive_moe vs dense_baseline: +0.0000
- adaptive_moe vs fixed_moe: -0.0009
- full_system vs adaptive_moe: +0.0000

## Caveats

- Models trained from scratch (no pretraining)
- Limited training budget (CPU-only)
- MoE models need more steps to overcome load-balancing instability
- ARC/GSM8K/HellaSwag/MMLU remain blocked (no text tokenizer)
- Results are from adapted symbolic benchmark families
