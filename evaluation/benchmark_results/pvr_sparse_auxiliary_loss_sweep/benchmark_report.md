# Algorithmic Benchmark Report

**Status:** VALID_ALGORITHMIC_BENCHMARK  
**Architecture:** DENSE_BASELINE_CURRENT_BEST  
**Mode:** benchmark-lite | **Scale:** small | **Steps:** 500  
**Families:** listops, scan_style, clrs_style, dyck  
**Samples:** 32,625 | **Time:** 234.1s

## Reason
4 respected benchmark families evaluated successfully. dense (0.0000) >= all MoE variants — MoE overhead not justified

## Validity

- This benchmark evaluates **algorithmic/compositional reasoning architecture**.
- It does NOT validate real NLP ability (ARC/GSM8K/HellaSwag blocked).
- Benchmark families are respected: CLRS-style, ListOps, SCAN, Dyck.

## Model Comparison

| Model | Params | Avg Acc | Avg EM | Avg Loss | Avg QPC | Avg Loops |
|-------|--------|---------|--------|----------|---------|-----------|
| pvr_ec_ownership_top1_scale_schedule_1_to_8__aux__baseline_main_loss | 482,690 | 0.0605 | 0.0000 | 0.463 | 0.0605 | 1.0 |
| pvr_ec_ownership_top1_scale_schedule_1_to_8__aux__sparse_ce_0_03 | 482,690 | 0.1727 | 0.0000 | 0.413 | 0.1727 | 1.0 |
| pvr_ec_ownership_top1_scale_schedule_1_to_8__aux__sparse_ce_0_05 | 482,690 | 0.2424 | 0.0000 | 0.400 | 0.2424 | 1.0 |
| pvr_ec_ownership_top1_scale_schedule_1_to_8__aux__margin_align_0_03_m0_5 | 482,690 | 0.1012 | 0.0000 | 0.446 | 0.1012 | 1.0 |
| pvr_ec_ownership_top1_scale_schedule_1_to_8__aux__margin_align_0_05_m0_5 | 482,690 | 0.1124 | 0.0000 | 0.441 | 0.1124 | 1.0 |
| pvr_ec_ownership_top1_scale_schedule_1_to_8__aux__wrong_suppress_0_03_t0_25 | 482,690 | 0.0680 | 0.0000 | 0.442 | 0.0680 | 1.0 |
| pvr_ec_ownership_top1_scale_schedule_1_to_8__aux__sparse_ce_0_03_plus_margin_0_03 | 482,690 | 0.2102 | 0.0000 | 0.422 | 0.2102 | 1.0 |
| pvr_ec_ownership_top1_scale_schedule_1_to_8__aux__margin_0_03_plus_wrong_suppress_0_03 | 482,690 | 0.1154 | 0.0000 | 0.423 | 0.1154 | 1.0 |
| pvr_ec_ownership_top1_scale_schedule_1_to_8__aux__sparse_ce_0_03_plus_harm_0_03 | 482,690 | 0.1762 | 0.0000 | 0.416 | 0.1762 | 1.0 |

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
