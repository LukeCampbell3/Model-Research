# Algorithmic Benchmark Report

**Status:** VALID_ALGORITHMIC_BENCHMARK  
**Architecture:** DENSE_BASELINE_CURRENT_BEST  
**Mode:** benchmark-lite | **Scale:** small | **Steps:** 200  
**Families:** scan_style, dyck, listops, clrs_style  
**Samples:** 50,750 | **Time:** 368.4s

## Reason
4 respected benchmark families evaluated successfully. dense (0.0000) >= all MoE variants — MoE overhead not justified

## Validity

- This benchmark evaluates **algorithmic/compositional reasoning architecture**.
- It does NOT validate real NLP ability (ARC/GSM8K/HellaSwag blocked).
- Benchmark families are respected: CLRS-style, ListOps, SCAN, Dyck.

## Model Comparison

| Model | Params | Avg Acc | Avg EM | Avg Loss | Avg QPC | Avg Loops |
|-------|--------|---------|--------|----------|---------|-----------|
| fixed_moe_vectorized | 1,001,092 | 0.0422 | 0.0000 | 0.443 | 0.0211 | 1.0 |
| pvr_ec_deploy_top1 | 614,274 | 0.0727 | 0.0000 | 0.453 | 0.0727 | 1.0 |
| pvr_ec_ownership_top1_delta_small | 416,898 | 0.0452 | 0.0000 | 0.446 | 0.0452 | 1.0 |
| pvr_ec_ownership_top1_delta_medium | 482,690 | 0.0735 | 0.0000 | 0.454 | 0.0735 | 1.0 |
| pvr_ec_ownership_top1_delta_large | 614,274 | 0.0727 | 0.0000 | 0.453 | 0.0727 | 1.0 |
| pvr_ec_ownership_top1_full_expert_ffn_control | 877,442 | 0.0417 | 0.0000 | 0.445 | 0.0417 | 1.0 |
| pvr_ec_ownership_top1_micro_ffn_0_25x | 482,690 | 0.0735 | 0.0000 | 0.454 | 0.0735 | 1.0 |
| pvr_ec_ownership_top1_micro_ffn_0_5x | 614,274 | 0.0727 | 0.0000 | 0.453 | 0.0727 | 1.0 |
| pvr_ec_ownership_top1_micro_ffn_1_0x | 877,442 | 0.0517 | 0.0000 | 0.441 | 0.0517 | 1.0 |
| pvr_ec_ownership_top1_delta_rank_8 | 367,554 | 0.0686 | 0.0000 | 0.445 | 0.0686 | 1.0 |
| pvr_ec_ownership_top1_delta_rank_16 | 384,002 | 0.0687 | 0.0000 | 0.444 | 0.0687 | 1.0 |
| pvr_ec_ownership_top1_delta_rank_32 | 416,898 | 0.0452 | 0.0000 | 0.446 | 0.0452 | 1.0 |
| pvr_ec_ownership_top1_delta_rank_64 | 482,690 | 0.0735 | 0.0000 | 0.454 | 0.0735 | 1.0 |
| pvr_ec_ownership_top1_delta_rank_128 | 614,274 | 0.0727 | 0.0000 | 0.453 | 0.0727 | 1.0 |

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
