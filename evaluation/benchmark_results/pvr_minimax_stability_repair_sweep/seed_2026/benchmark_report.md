# Algorithmic Benchmark Report

**Status:** VALID_ALGORITHMIC_BENCHMARK  
**Architecture:** DENSE_BASELINE_CURRENT_BEST  
**Mode:** benchmark-lite | **Scale:** small | **Steps:** 500  
**Families:** scan_style, dyck, clrs_style, listops  
**Samples:** 50,750 | **Time:** 375.5s

## Reason
4 respected benchmark families evaluated successfully. dense (0.0000) >= all MoE variants — MoE overhead not justified

## Validity

- This benchmark evaluates **algorithmic/compositional reasoning architecture**.
- It does NOT validate real NLP ability (ARC/GSM8K/HellaSwag blocked).
- Benchmark families are respected: CLRS-style, ListOps, SCAN, Dyck.

## Model Comparison

| Model | Params | Avg Acc | Avg EM | Avg Loss | Avg QPC | Avg Loops |
|-------|--------|---------|--------|----------|---------|-----------|
| fixed_moe_vectorized | 1,001,092 | 0.2179 | 0.0000 | 0.405 | 0.1090 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1 | 482,690 | 0.3133 | 0.0000 | 0.374 | 0.3133 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1_1 | 482,690 | 0.3098 | 0.0032 | 0.375 | 0.3098 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_sampling | 482,690 | 0.3133 | 0.0000 | 0.374 | 0.3133 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_loss_light | 482,690 | 0.3133 | 0.0000 | 0.374 | 0.3133 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_1_0 | 482,690 | 0.3133 | 0.0000 | 0.374 | 0.3133 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_0_5 | 482,690 | 0.3380 | 0.0000 | 0.364 | 0.3380 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_light | 482,690 | 0.3159 | 0.0000 | 0.374 | 0.3159 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_medium | 482,690 | 0.3098 | 0.0032 | 0.375 | 0.3098 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_01 | 482,690 | 0.3075 | 0.0000 | 0.376 | 0.3075 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_03 | 482,690 | 0.3181 | 0.0000 | 0.369 | 0.3181 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_instead_of_0_05 | 482,690 | 0.2671 | 0.0040 | 0.382 | 0.2671 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_03 | 482,690 | 0.2844 | 0.0000 | 0.391 | 0.2844 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_01 | 482,690 | 0.2848 | 0.0000 | 0.391 | 0.2848 | 1.0 |

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
