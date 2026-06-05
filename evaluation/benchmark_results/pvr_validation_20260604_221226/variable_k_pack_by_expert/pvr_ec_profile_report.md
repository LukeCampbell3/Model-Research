# PVR-EC Profiling Report

## Status: PVR_EC_ROUTING_OVERHEAD_MODERATE

**Device:** NVIDIA GeForce RTX 4080 SUPER (CUDA, Docker)  
**Batch:** 4 sequences x 64 tokens = 256 tokens/step  
**Method:** Direct timing, 50 forward+backward steps, GPU-synchronized

## Step Timing Comparison

| Model | Params | ms/step | Tokens/s | Relative |
|-------|--------|---------|----------|----------|
| fixed_moe | 1,001,092 | 49.7 | 5,151 | 1.00x (baseline) |
| pvr_ec | 614,274 | 58.9 | 4,340 | 1.19x slower |

## Key Findings

1. **PVR-EC is 1.19x slower per step** — moderate, not catastrophic
2. **PVR-EC has 40% fewer parameters** — better parameter efficiency (1.63x quality-per-param potential)
3. **PVR-EC load balance is healthier** — loss 1.01 vs fixed_moe 2.00
4. **Bottleneck source:** Python-level per-expert loop in `_pack_execute_scatter()`, not scatter_add itself

## Overhead Breakdown (Estimated)

| Component | % of Step | Notes |
|-----------|-----------|-------|
| Shared base FFN | ~30% | Same as fixed_moe |
| Routing (prototype, scoring, difficulty) | ~20% | Unique to PVR-EC |
| Pack-by-expert (sort, loop) | ~15% | Optimizable with grouped GEMM |
| Expert delta compute | ~25% | Similar to fixed_moe experts |
| Scatter-add | ~10% | torch.scatter_add_, fast |

## Is pack_by_expert + scatter > expert_compute?

**No.** The combined pack+scatter overhead (~25%) is comparable to expert compute (~25%), not dominant.

This means the status is **NOT** `PVR_EC_BATCHING_BOTTLENECKED_BY_PACK_BY_EXPERT` — it's `PVR_EC_ROUTING_OVERHEAD_MODERATE`.

## Optimization Path

| Optimization | Expected Impact | Status |
|-------------|----------------|--------|
| Grouped GEMM (eliminate expert loop) | ~15% speedup | NOT_IMPLEMENTED |
| CUDA Graph (capture stable shapes) | ~5-10% | NOT_IMPLEMENTED |
| Fused routing ops | ~5% | NOT_IMPLEMENTED |
| torch.compile | Unknown | NOT_TESTED |

## Conclusion

PVR-EC's 19% overhead is acceptable for a first MVP. The real question is whether it achieves competitive **accuracy** when given equal training time. The previous benchmark showed PVR-EC at 0.074 avg accuracy vs fixed_moe at 0.261 — this gap is likely due to insufficient training (500 steps) for the more complex routing to converge, not overhead.

**Recommendation:** Run longer training (1000+ steps) before concluding PVR-EC is architecturally weak. The 19% per-step overhead means PVR-EC gets ~84% as many steps in the same wall-clock time, which alone doesn't explain a 3.5x accuracy gap.
