# Algorithmic Benchmark Report

**Status:** VALID_ALGORITHMIC_BENCHMARK  
**Architecture:** DENSE_BASELINE_CURRENT_BEST  
**Mode:** benchmark-lite | **Scale:** small | **Steps:** 500  
**Families:** scan_style, dyck, clrs_style, listops  
**Samples:** 50,750 | **Time:** 365.8s

## Reason
4 respected benchmark families evaluated successfully. dense (0.0000) >= all MoE variants — MoE overhead not justified

## Validity

- This benchmark evaluates **algorithmic/compositional reasoning architecture**.
- It does NOT validate real NLP ability (ARC/GSM8K/HellaSwag blocked).
- Benchmark families are respected: CLRS-style, ListOps, SCAN, Dyck.

## Model Comparison

| Model | Params | Avg Acc | Avg EM | Avg Loss | Avg QPC | Avg Loops |
|-------|--------|---------|--------|----------|---------|-----------|
| fixed_moe_vectorized | 1,001,092 | 0.2466 | 0.0000 | 0.413 | 0.1233 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1 | 482,690 | 0.2340 | 0.0000 | 0.401 | 0.2340 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1_1 | 482,690 | 0.2134 | 0.0000 | 0.399 | 0.2134 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_sampling | 482,690 | 0.2340 | 0.0000 | 0.401 | 0.2340 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_loss_light | 482,690 | 0.2340 | 0.0000 | 0.401 | 0.2340 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_1_0 | 482,690 | 0.2340 | 0.0000 | 0.401 | 0.2340 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_0_5 | 482,690 | 0.3126 | 0.0000 | 0.386 | 0.3126 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_light | 482,690 | 0.2593 | 0.0000 | 0.400 | 0.2593 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_medium | 482,690 | 0.2134 | 0.0000 | 0.399 | 0.2134 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_01 | 482,690 | 0.2496 | 0.0000 | 0.398 | 0.2496 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_03 | 482,690 | 0.2641 | 0.0000 | 0.392 | 0.2641 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_instead_of_0_05 | 482,690 | 0.1828 | 0.0000 | 0.412 | 0.1828 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_03 | 482,690 | 0.2014 | 0.0000 | 0.416 | 0.2014 | 1.0 |
| pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_01 | 482,690 | 0.1968 | 0.0000 | 0.416 | 0.1968 | 1.0 |

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
