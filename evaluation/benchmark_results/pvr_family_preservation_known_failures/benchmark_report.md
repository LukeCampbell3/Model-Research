# Algorithmic Benchmark Report

**Status:** VALID_ALGORITHMIC_BENCHMARK  
**Architecture:** DENSE_BASELINE_CURRENT_BEST  
**Mode:** benchmark-lite | **Scale:** small | **Steps:** 500  
**Families:** dyck, listops, scan_style, clrs_style  
**Samples:** 18,125 | **Time:** 139.9s

## Reason
4 respected benchmark families evaluated successfully. dense (0.0511) >= all MoE variants — MoE overhead not justified

## Validity

- This benchmark evaluates **algorithmic/compositional reasoning architecture**.
- It does NOT validate real NLP ability (ARC/GSM8K/HellaSwag blocked).
- Benchmark families are respected: CLRS-style, ListOps, SCAN, Dyck.

## Model Comparison

| Model | Params | Avg Acc | Avg EM | Avg Loss | Avg QPC | Avg Loops |
|-------|--------|---------|--------|----------|---------|-----------|
| dense_baseline | 330,752 | 0.0511 | 0.0000 | 0.510 | 0.0511 | 1.0 |
| fixed_moe_vectorized | 1,001,092 | 0.2586 | 0.0092 | 0.389 | 0.1293 | 1.0 |
| pvr_full | 482,690 | 0.0510 | 0.0000 | 0.472 | 0.0510 | 1.0 |
| pvr_full_fixed_owner_e0 | 482,690 | 0.0462 | 0.0000 | 0.483 | 0.0462 | 1.0 |
| pvr_full_expert_delta_scale_4 | 482,690 | 0.0502 | 0.0000 | 0.478 | 0.0502 | 1.0 |

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

- adaptive_moe vs dense_baseline: -0.0511
- adaptive_moe vs fixed_moe: +0.0000
- full_system vs adaptive_moe: +0.0000

## Caveats

- Models trained from scratch (no pretraining)
- Limited training budget (CPU-only)
- MoE models need more steps to overcome load-balancing instability
- ARC/GSM8K/HellaSwag/MMLU remain blocked (no text tokenizer)
- Results are from adapted symbolic benchmark families
