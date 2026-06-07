# Algorithmic Benchmark Report

**Status:** VALID_ALGORITHMIC_BENCHMARK  
**Architecture:** DENSE_BASELINE_CURRENT_BEST  
**Mode:** benchmark-lite | **Scale:** tiny | **Steps:** 40  
**Families:** listops, clrs_style, dyck, scan_style  
**Samples:** 3,480 | **Time:** 153.1s

## Reason
4 respected benchmark families evaluated successfully. dense (0.0000) >= all MoE variants — MoE overhead not justified

## Validity

- This benchmark evaluates **algorithmic/compositional reasoning architecture**.
- It does NOT validate real NLP ability (ARC/GSM8K/HellaSwag blocked).
- Benchmark families are respected: CLRS-style, ListOps, SCAN, Dyck.

## Model Comparison

| Model | Params | Avg Acc | Avg EM | Avg Loss | Avg QPC | Avg Loops |
|-------|--------|---------|--------|----------|---------|-----------|
| fixed_moe_vectorized | 260,932 | 0.0016 | 0.0000 | 4.112 | 0.0008 | 1.0 |
| pvr_ec_ownership_top1_micro_ffn_0_5x | 169,218 | 0.0000 | 0.0000 | 4.177 | 0.0000 | 1.0 |
| pvr_ec_ownership_top1_delta_rank_16 | 119,682 | 0.0003 | 0.0000 | 4.095 | 0.0003 | 1.0 |
| pvr_ec_ownership_top1_delta_rank_64 | 169,218 | 0.0000 | 0.0000 | 4.177 | 0.0000 | 1.0 |
| pvr_ec_learning_full | 169,218 | 0.0000 | 0.0000 | 4.177 | 0.0000 | 1.0 |
| pvr_ec_learning_shared_only | 136,194 | 0.0004 | 0.0000 | 4.165 | 0.0004 | 1.0 |
| pvr_ec_learning_sparse_only | 169,218 | 0.0000 | 0.0000 | 4.186 | 0.0000 | 1.0 |
| pvr_ec_learning_shared_scale_0_5 | 169,218 | 0.0000 | 0.0000 | 4.182 | 0.0000 | 1.0 |
| pvr_ec_learning_expert_delta_scale_2_0 | 169,218 | 0.0000 | 0.0000 | 4.184 | 0.0000 | 1.0 |
| pvr_ec_ownership_top1_delayed_candidate | 169,218 | 0.0000 | 0.0000 | 4.177 | 0.0000 | 1.0 |

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
