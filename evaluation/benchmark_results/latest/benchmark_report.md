# Algorithmic Benchmark Report

**Status:** VALID_ALGORITHMIC_BENCHMARK  
**Architecture:** HOLD_NEEDS_MORE_EVIDENCE  
**Mode:** benchmark-lite | **Scale:** small | **Steps:** 300  
**Families:** dyck, listops, scan_style, clrs_style  
**Samples:** 5,433 | **Time:** 748.6s

## Reason
4 respected benchmark families evaluated successfully. fixed_moe leads (0.0704) but adaptive is close on task wins

## Validity

- This benchmark evaluates **algorithmic/compositional reasoning architecture**.
- It does NOT validate real NLP ability (ARC/GSM8K/HellaSwag blocked).
- Benchmark families are respected: CLRS-style, ListOps, SCAN, Dyck.

## Model Comparison

| Model | Params | Avg Acc | Avg EM | Avg Loss | Avg QPC | Avg Loops |
|-------|--------|---------|--------|----------|---------|-----------|
| fixed_moe | 1,001,092 | 0.0704 | 0.0000 | 0.439 | 0.0352 | 1.0 |
| pvr_ec | 614,274 | 0.0356 | 0.0000 | 0.457 | 0.0356 | 1.0 |
| pvr_ec_matched | 879,618 | 0.0589 | 0.0000 | 0.449 | 0.0589 | 1.0 |

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
- adaptive_moe vs fixed_moe: -0.0704
- full_system vs adaptive_moe: +0.0000

## Caveats

- Models trained from scratch (no pretraining)
- Limited training budget (CPU-only)
- MoE models need more steps to overcome load-balancing instability
- ARC/GSM8K/HellaSwag/MMLU remain blocked (no text tokenizer)
- Results are from adapted symbolic benchmark families
