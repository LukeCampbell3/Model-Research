# Algorithmic Benchmark Report

**Status:** PARTIAL_ALGORITHMIC_BENCHMARK  
**Architecture:** DENSE_BASELINE_CURRENT_BEST  
**Mode:** benchmark-lite | **Scale:** small | **Steps:** 500  
**Families:** clrs_style, listops  
**Samples:** 8,000 | **Time:** 134.4s

## Reason
Only 2/4 families succeeded: ['clrs_style', 'listops'] dense (0.0000) >= all MoE variants — MoE overhead not justified

## Validity

- This benchmark evaluates **algorithmic/compositional reasoning architecture**.
- It does NOT validate real NLP ability (ARC/GSM8K/HellaSwag blocked).
- Benchmark families are respected: CLRS-style, ListOps, SCAN, Dyck.

## Model Comparison

| Model | Params | Avg Acc | Avg EM | Avg Loss | Avg QPC | Avg Loops |
|-------|--------|---------|--------|----------|---------|-----------|
| fixed_moe_vectorized | 1,001,092 | 0.4413 | 0.0000 | 0.529 | 0.2207 | 1.0 |
| pvr_ec_deploy_top1 | 614,274 | 0.1008 | 0.0000 | 0.620 | 0.1008 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1 | 482,690 | 0.3846 | 0.0000 | 0.522 | 0.3846 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1_1 | 482,690 | 0.3846 | 0.0000 | 0.536 | 0.3846 | 1.0 |

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
