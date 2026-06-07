# Algorithmic Benchmark Report

**Status:** VALID_ALGORITHMIC_BENCHMARK  
**Architecture:** DENSE_BASELINE_CURRENT_BEST  
**Mode:** benchmark-lite | **Scale:** small | **Steps:** 500  
**Families:** listops, dyck, clrs_style, scan_style  
**Samples:** 25,375 | **Time:** 182.5s

## Reason
4 respected benchmark families evaluated successfully. dense (0.0000) >= all MoE variants — MoE overhead not justified

## Validity

- This benchmark evaluates **algorithmic/compositional reasoning architecture**.
- It does NOT validate real NLP ability (ARC/GSM8K/HellaSwag blocked).
- Benchmark families are respected: CLRS-style, ListOps, SCAN, Dyck.

## Model Comparison

| Model | Params | Avg Acc | Avg EM | Avg Loss | Avg QPC | Avg Loops |
|-------|--------|---------|--------|----------|---------|-----------|
| pvr_ec_ownership_top1_final_candidate_v1__aux__sparse_ce_0_05_plus_logit_norm_penalty_light | 482,690 | 0.2466 | 0.0000 | 0.396 | 0.2466 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__aux__sparse_ce_0_03_plus_logit_norm_penalty_light | 482,690 | 0.1893 | 0.0000 | 0.408 | 0.1893 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__aux__sparse_ce_0_07_plus_logit_norm_penalty_light | 482,690 | 0.2545 | 0.0103 | 0.396 | 0.2545 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__aux__sparse_ce_0_05_plus_logit_norm_penalty_medium | 482,690 | 0.2356 | 0.0000 | 0.394 | 0.2356 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__aux__sparse_ce_0_05_plus_temperature_regularization | 482,690 | 0.2476 | 0.0000 | 0.401 | 0.2476 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__aux__sparse_ce_0_05_plus_posthoc_temperature_calibration | 482,690 | 0.2449 | 0.0000 | 0.400 | 0.2449 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__aux__sparse_ce_0_05_plus_logit_norm_light_plus_wrong_suppress_0_01 | 482,690 | 0.2340 | 0.0000 | 0.397 | 0.2340 | 1.0 |

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
