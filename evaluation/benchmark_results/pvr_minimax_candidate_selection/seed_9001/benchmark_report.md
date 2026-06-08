# Algorithmic Benchmark Report

**Status:** VALID_ALGORITHMIC_BENCHMARK  
**Architecture:** DENSE_BASELINE_CURRENT_BEST  
**Mode:** benchmark-lite | **Scale:** small | **Steps:** 500  
**Families:** scan_style, dyck, clrs_style, listops  
**Samples:** 39,875 | **Time:** 293.7s

## Reason
4 respected benchmark families evaluated successfully. dense (0.0000) >= all MoE variants — MoE overhead not justified

## Validity

- This benchmark evaluates **algorithmic/compositional reasoning architecture**.
- It does NOT validate real NLP ability (ARC/GSM8K/HellaSwag blocked).
- Benchmark families are respected: CLRS-style, ListOps, SCAN, Dyck.

## Model Comparison

| Model | Params | Avg Acc | Avg EM | Avg Loss | Avg QPC | Avg Loops |
|-------|--------|---------|--------|----------|---------|-----------|
| fixed_moe_vectorized | 1,001,092 | 0.0959 | 0.0000 | 0.434 | 0.0479 | 1.0 |
| pvr_ec_deploy_top1 | 614,274 | 0.0637 | 0.0000 | 0.444 | 0.0637 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__v1 | 482,690 | 0.3360 | 0.0000 | 0.377 | 0.3360 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium | 482,690 | 0.3403 | 0.0000 | 0.374 | 0.3403 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light | 482,690 | 0.2545 | 0.0000 | 0.395 | 0.2545 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light | 482,690 | 0.3360 | 0.0000 | 0.377 | 0.3360 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium | 482,690 | 0.3403 | 0.0000 | 0.374 | 0.3403 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light | 482,690 | 0.2458 | 0.0000 | 0.399 | 0.2458 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light | 482,690 | 0.3394 | 0.0000 | 0.369 | 0.3394 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2 | 482,690 | 0.2545 | 0.0000 | 0.414 | 0.2545 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2 | 482,690 | 0.3360 | 0.0000 | 0.400 | 0.3360 | 1.0 |

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
