# Algorithmic Benchmark Report

**Status:** VALID_ALGORITHMIC_BENCHMARK  
**Architecture:** DENSE_BASELINE_CURRENT_BEST  
**Mode:** benchmark-lite | **Scale:** small | **Steps:** 500  
**Families:** clrs_style, dyck, listops, scan_style  
**Samples:** 32,625 | **Time:** 223.9s

## Reason
4 respected benchmark families evaluated successfully. dense (0.0000) >= all MoE variants — MoE overhead not justified

## Validity

- This benchmark evaluates **algorithmic/compositional reasoning architecture**.
- It does NOT validate real NLP ability (ARC/GSM8K/HellaSwag blocked).
- Benchmark families are respected: CLRS-style, ListOps, SCAN, Dyck.

## Model Comparison

| Model | Params | Avg Acc | Avg EM | Avg Loss | Avg QPC | Avg Loops |
|-------|--------|---------|--------|----------|---------|-----------|
| pvr_ec_ownership_top1_constant_1 | 482,690 | 0.0510 | 0.0000 | 0.472 | 0.0510 | 1.0 |
| pvr_ec_ownership_top1_constant_2 | 482,690 | 0.0524 | 0.0000 | 0.470 | 0.0524 | 1.0 |
| pvr_ec_ownership_top1_constant_4 | 482,690 | 0.0502 | 0.0000 | 0.478 | 0.0502 | 1.0 |
| pvr_ec_ownership_top1_constant_8 | 482,690 | 0.0391 | 0.0000 | 0.476 | 0.0391 | 1.0 |
| pvr_ec_ownership_top1_scale_schedule_1_to_4 | 482,690 | 0.0425 | 0.0000 | 0.471 | 0.0425 | 1.0 |
| pvr_ec_ownership_top1_scale_schedule_1_to_8 | 482,690 | 0.0605 | 0.0000 | 0.463 | 0.0605 | 1.0 |
| pvr_ec_ownership_top1_scale_schedule_1_to_8_to_4 | 482,690 | 0.0611 | 0.0000 | 0.467 | 0.0611 | 1.0 |
| pvr_ec_ownership_top1_scale_schedule_1_to_8_to_2 | 482,690 | 0.0543 | 0.0000 | 0.472 | 0.0543 | 1.0 |
| pvr_ec_ownership_top1_scale_schedule_1_to_4_to_2 | 482,690 | 0.0428 | 0.0000 | 0.475 | 0.0428 | 1.0 |

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
