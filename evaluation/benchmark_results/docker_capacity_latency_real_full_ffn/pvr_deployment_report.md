# PVR-EC Deployment Report

**Status:** PARTIAL_PVR_EC_FAIR_DEPLOYMENT_VALIDATION

| Model | Mode | Batch | Seq | p50 ms | p95 ms | Slowdown vs fixed_vec | Loss | QPM | Q/Mem | Expert Exec |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| fixed_moe_vectorized | off | 32 | 64 | 41.633 | 43.547 | 1.00x | 5.5686 | 0.000082 | 0.000002 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_delta_large | top1 | 32 | 64 | 20.684 | 129.525 | 0.84x | 5.5773 | 0.000111 | 0.000014 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_full_expert_ffn_control | top1 | 32 | 64 | 134.351 | 210.790 | 3.21x | 5.5685 | 0.000033 | 0.000008 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_micro_ffn_1_0x | top1 | 32 | 64 | 138.934 | 174.808 | 3.38x | 5.5726 | 0.000028 | 0.000007 | FULLY_VECTORIZED |

Hard runtime branching is disabled. Branch tickets are disabled in the deployment hot path.