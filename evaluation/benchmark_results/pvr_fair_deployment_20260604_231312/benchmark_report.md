# Algorithmic Benchmark Report

**Status:** VALID_ALGORITHMIC_BENCHMARK  
**Architecture:** DENSE_BASELINE_CURRENT_BEST  
**Mode:** benchmark-lite | **Scale:** small | **Steps:** 200  
**Families:** scan_style, dyck, clrs_style, listops  
**Samples:** 9,270 | **Time:** 80.6s

## Reason
4 respected benchmark families evaluated successfully. dense (0.0000) >= all MoE variants — MoE overhead not justified

## Validity

- This benchmark evaluates **algorithmic/compositional reasoning architecture**.
- It does NOT validate real NLP ability (ARC/GSM8K/HellaSwag blocked).
- Benchmark families are respected: CLRS-style, ListOps, SCAN, Dyck.

## Model Comparison

| Model | Params | Avg Acc | Avg EM | Avg Loss | Avg QPC | Avg Loops |
|-------|--------|---------|--------|----------|---------|-----------|
| fixed_moe_looped_reference | 1,001,092 | 0.0420 | 0.0000 | 0.440 | 0.0210 | 1.0 |
| fixed_moe_vectorized | 1,001,092 | 0.0406 | 0.0000 | 0.440 | 0.0203 | 1.0 |
| pvr_ec_deploy_top1 | 482,690 | 0.0792 | 0.0000 | 0.448 | 0.0792 | 1.0 |
| pvr_ec_deploy_top2 | 482,690 | 0.0719 | 0.0000 | 0.449 | 0.0719 | 1.0 |
| pvr_ec_deploy_bucketed | 482,690 | 0.0789 | 0.0000 | 0.446 | 0.0789 | 1.0 |

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
- adaptive_moe vs fixed_moe: +0.0000
- full_system vs adaptive_moe: +0.0000

## Caveats

- Models trained from scratch (no pretraining)
- Limited training budget (CPU-only)
- MoE models need more steps to overcome load-balancing instability
- ARC/GSM8K/HellaSwag/MMLU remain blocked (no text tokenizer)
- Results are from adapted symbolic benchmark families
