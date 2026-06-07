# Algorithmic Benchmark Report

**Status:** VALID_ALGORITHMIC_BENCHMARK  
**Architecture:** DENSE_BASELINE_CURRENT_BEST  
**Mode:** benchmark-lite | **Scale:** small | **Steps:** 500  
**Families:** listops, dyck, clrs_style, scan_style  
**Samples:** 32,625 | **Time:** 2325.5s

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
| pvr_ec_ownership_top1_scale_schedule_1_to_8__aux__sparse_ce_0_03_plus_margin_0_03 | 482,690 | 0.2006 | 0.0000 | 0.420 | 0.2006 | 1.0 |
| pvr_ec_ownership_top1_scale_schedule_1_to_8__aux__sparse_ce_0_03_plus_wrong_suppress_0_03 | 482,690 | 0.1759 | 0.0000 | 0.411 | 0.1759 | 1.0 |
| pvr_ec_ownership_top1_scale_schedule_1_to_8__aux__sparse_ce_0_05_plus_wrong_suppress_0_01 | 482,690 | 0.2380 | 0.0000 | 0.399 | 0.2380 | 1.0 |
| pvr_ec_ownership_top1_scale_schedule_1_to_8__aux__sparse_ce_0_05_plus_logit_norm_penalty_light | 482,690 | 0.2473 | 0.0000 | 0.396 | 0.2473 | 1.0 |
| pvr_ec_ownership_top1_scale_schedule_1_to_8__aux__sparse_ce_0_05_plus_temperature_regularization | 482,690 | 0.2475 | 0.0000 | 0.401 | 0.2475 | 1.0 |
| pvr_ec_ownership_top1_scale_schedule_1_to_8__aux__sparse_ce_warmup_decay | 482,690 | 0.1793 | 0.0000 | 0.411 | 0.1793 | 1.0 |

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
