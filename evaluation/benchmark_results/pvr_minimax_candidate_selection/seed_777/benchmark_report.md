# Algorithmic Benchmark Report

**Status:** VALID_ALGORITHMIC_BENCHMARK  
**Architecture:** DENSE_BASELINE_CURRENT_BEST  
**Mode:** benchmark-lite | **Scale:** small | **Steps:** 500  
**Families:** scan_style, dyck, clrs_style, listops  
**Samples:** 39,875 | **Time:** 295.1s

## Reason
4 respected benchmark families evaluated successfully. dense (0.0000) >= all MoE variants — MoE overhead not justified

## Validity

- This benchmark evaluates **algorithmic/compositional reasoning architecture**.
- It does NOT validate real NLP ability (ARC/GSM8K/HellaSwag blocked).
- Benchmark families are respected: CLRS-style, ListOps, SCAN, Dyck.

## Model Comparison

| Model | Params | Avg Acc | Avg EM | Avg Loss | Avg QPC | Avg Loops |
|-------|--------|---------|--------|----------|---------|-----------|
| fixed_moe_vectorized | 1,001,092 | 0.1531 | 0.0037 | 0.414 | 0.0765 | 1.0 |
| pvr_ec_deploy_top1 | 614,274 | 0.0972 | 0.0000 | 0.445 | 0.0972 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__v1 | 482,690 | 0.2636 | 0.0000 | 0.420 | 0.2636 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium | 482,690 | 0.2034 | 0.0000 | 0.422 | 0.2034 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light | 482,690 | 0.0781 | 0.0000 | 0.451 | 0.0781 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light | 482,690 | 0.2636 | 0.0000 | 0.420 | 0.2636 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium | 482,690 | 0.2034 | 0.0000 | 0.422 | 0.2034 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light | 482,690 | 0.0722 | 0.0000 | 0.438 | 0.0722 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light | 482,690 | 0.1928 | 0.0000 | 0.424 | 0.1928 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2 | 482,690 | 0.0781 | 0.0000 | 0.463 | 0.0781 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2 | 482,690 | 0.2636 | 0.0000 | 0.438 | 0.2636 | 1.0 |

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
