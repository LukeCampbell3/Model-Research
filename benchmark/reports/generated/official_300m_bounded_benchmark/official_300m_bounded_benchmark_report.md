# Official-Dataset Bounded 300M Benchmark

Status: `PVR_300M_OFFICIAL_DATASET_BOUNDED_BENCHMARK_COMPLETE`
Decision: `PVR_300M_OFFICIAL_DATASET_BOUNDED_ADVANTAGE_NOT_SUPPORTED`

> This is a deterministic bounded evaluation on official dataset splits, not a full official leaderboard run.

Training-token gate matched: `True`
Contamination scan: `CONTAMINATION_SCAN_CLEAR`

| model | broad macro | code pass@1 macro | overall macro | active params/token | active FLOPs/token | Top1 clean |
|---|---:|---:|---:|---:|---:|---|
| generic_top2_moe_reference_300m_official_compute_matched | 0.3021 | 0.0000 | 0.2266 | 191212936 | 1147277616 | None |
| pvr_teacher_ean_300m_matched | 0.2943 | 0.0000 | 0.2207 | 213329464 | 1279976784 | True |
| vanilla_switch_top1_reference_300m_official_compute_matched | 0.2917 | 0.0000 | 0.2188 | 179730352 | 1078382112 | None |
| pvr_self_instilled_ean_trunk_stage_matched_300m | 0.2917 | 0.0000 | 0.2188 | 213329464 | 1279976784 | True |
| pvr_full_scratch_300m_total_compute_matched | 0.2786 | 0.0000 | 0.2090 | 213329464 | 1279976784 | True |
| dense_transformer_300m_official_compute_matched | 0.2734 | 0.0000 | 0.2051 | 248355592 | 1490133552 | None |

## Task Scores

| model | mmlu | arc_challenge | hellaswag | boolq | winogrande | gsm8k | humaneval | mbpp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| generic_top2_moe_reference_300m_official_compute_matched | 0.3750 | 0.2656 | 0.2344 | 0.4375 | 0.5000 | 0.0000 | 0.0000 | 0.0000 |
| pvr_teacher_ean_300m_matched | 0.2969 | 0.2656 | 0.3281 | 0.4375 | 0.4375 | 0.0000 | 0.0000 | 0.0000 |
| vanilla_switch_top1_reference_300m_official_compute_matched | 0.3594 | 0.2344 | 0.2188 | 0.4375 | 0.5000 | 0.0000 | 0.0000 | 0.0000 |
| pvr_self_instilled_ean_trunk_stage_matched_300m | 0.2969 | 0.1875 | 0.2656 | 0.4531 | 0.5469 | 0.0000 | 0.0000 | 0.0000 |
| pvr_full_scratch_300m_total_compute_matched | 0.2812 | 0.2188 | 0.2656 | 0.4219 | 0.4844 | 0.0000 | 0.0000 | 0.0000 |
| dense_transformer_300m_official_compute_matched | 0.2969 | 0.2500 | 0.2031 | 0.4219 | 0.4688 | 0.0000 | 0.0000 | 0.0000 |

## Paired Candidate Comparisons

| baseline | macro delta | paired 95% CI | P(delta > 0) |
|---|---:|---:|---:|
| dense_transformer_300m_official_compute_matched | 0.0137 | [-0.0176, 0.0449] | 0.7926 |
| vanilla_switch_top1_reference_300m_official_compute_matched | 0.0000 | [-0.0254, 0.0254] | 0.4730 |
| generic_top2_moe_reference_300m_official_compute_matched | -0.0078 | [-0.0332, 0.0176] | 0.2310 |

## Claim Boundaries

- `PVR_OFFICIAL_BROAD_NLP_SUPPORTED`
- `PVR_OFFICIAL_CODE_BENCH_SUPPORTED`
- `PVR_FULL_OFFICIAL_LEADERBOARD_SUPPORTED`

Full per-example predictions, confidence intervals, checkpoint hashes, and provenance are in `official_300m_bounded_benchmark_report.json`.
