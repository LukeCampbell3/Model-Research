# Failure Analysis

**Run:** algo_20260606_183305_benchmark-lite

## Model Failures

- **pvr_ec_ownership_top1_delta_large**: float division by zero
- **pvr_ec_ownership_top1_full_expert_ffn_control**: float division by zero

## NLP Benchmark Status: BLOCKED

- No text tokenizer exists (custom 256-token symbolic vocab)
- ARC-Challenge, GSM8K, HellaSwag: accessible but incompatible
- Required: BPE tokenizer, 32K+ vocab, language pretraining
