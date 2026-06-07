# Algorithmic Benchmark Report

**Status:** VALID_ALGORITHMIC_BENCHMARK  
**Architecture:** DENSE_BASELINE_CURRENT_BEST  
**Mode:** benchmark-lite | **Scale:** small | **Steps:** 500  
**Families:** clrs_style, listops, dyck, scan_style  
**Samples:** 39,875 | **Time:** 348.2s

## Reason
4 respected benchmark families evaluated successfully. dense (0.0000) >= all MoE variants — MoE overhead not justified

## Validity

- This benchmark evaluates **algorithmic/compositional reasoning architecture**.
- It does NOT validate real NLP ability (ARC/GSM8K/HellaSwag blocked).
- Benchmark families are respected: CLRS-style, ListOps, SCAN, Dyck.

## Model Comparison

| Model | Params | Avg Acc | Avg EM | Avg Loss | Avg QPC | Avg Loops |
|-------|--------|---------|--------|----------|---------|-----------|
| fixed_moe_vectorized | 1,001,092 | 0.2580 | 0.0092 | 0.389 | 0.1290 | 1.0 |
| pvr_ec_deploy_top1 | 614,274 | 0.0772 | 0.0000 | 0.451 | 0.0772 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__final_candidate_v1 | 482,690 | 0.2466 | 0.0000 | 0.396 | 0.2466 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__posthoc_temperature_T_1_1 | 482,690 | 0.2466 | 0.0000 | 0.402 | 0.2466 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__posthoc_temperature_T_1_2 | 482,690 | 0.2466 | 0.0000 | 0.416 | 0.2466 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__posthoc_temperature_T_1_3 | 482,690 | 0.2466 | 0.0000 | 0.439 | 0.2466 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__posthoc_temperature_T_1_5 | 482,690 | 0.2472 | 0.0000 | 0.526 | 0.2472 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_penalty_medium | 482,690 | 0.2356 | 0.0000 | 0.394 | 0.2356 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_01_plus_logit_norm_light | 482,690 | 0.2340 | 0.0000 | 0.397 | 0.2340 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light | 482,690 | 0.1893 | 0.0000 | 0.408 | 0.1893 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light | 482,690 | 0.1823 | 0.0000 | 0.409 | 0.1823 | 1.0 |

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
