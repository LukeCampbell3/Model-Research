# PVR-EC Deployment Report

**Status:** PVR_EC_READY_FOR_LONGER_CAPABILITY_RUN

| Model | Mode | Batch | Seq | p50 ms | p95 ms | Slowdown | Loss | QPM | Max MB | Expert Exec |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| fixed_moe | off | 1 | 64 | 10.874 | 11.281 | 1.00x | 5.5383 | 0.000000 | 10.4 | LOOPED |
| fixed_moe | off | 32 | 64 | 11.049 | 12.059 | 1.00x | 5.5639 | 0.000352 | 19.2 | LOOPED |
| pvr_ec_deploy_top1 | top1 | 1 | 64 | 2.483 | 2.915 | 0.23x | 5.5653 | 0.000000 | 12.4 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 32 | 64 | 2.436 | 2.825 | 0.22x | 5.5614 | 0.001367 | 48.3 | FULLY_VECTORIZED |
| pvr_ec_deploy_top2 | top2 | 1 | 64 | 2.586 | 2.966 | 0.24x | 5.5663 | 0.000000 | 14.4 | FULLY_VECTORIZED |
| pvr_ec_deploy_top2 | top2 | 32 | 64 | 2.777 | 2.910 | 0.25x | 5.5610 | 0.001216 | 112.3 | FULLY_VECTORIZED |
| pvr_ec_deploy_bucketed | bucketed | 1 | 64 | 2.798 | 2.901 | 0.26x | 5.5642 | 0.000000 | 17.5 | FULLY_VECTORIZED |
| pvr_ec_deploy_bucketed | bucketed | 32 | 64 | 3.265 | 3.772 | 0.30x | 5.5606 | 0.000876 | 210.4 | FULLY_VECTORIZED |
| pvr_ec_deploy_dense_masked_control | dense_masked_control | 1 | 64 | 2.602 | 2.998 | 0.24x | 5.5654 | 0.000000 | 17.5 | FULLY_VECTORIZED |
| pvr_ec_deploy_dense_masked_control | dense_masked_control | 32 | 64 | 3.492 | 4.003 | 0.32x | 5.5607 | 0.000685 | 210.3 | FULLY_VECTORIZED |

Hard runtime branching is disabled. Branch tickets are disabled in the deployment hot path.

## Aux Alpha Sweep

| Alpha | Avg p50 ms | Avg p95 ms | Avg loss | Avg QPM | Avg slowdown |
|---:|---:|---:|---:|---:|---:|
| 0 | 2.722352 | 3.034113 | 5.563355 | 0.000607805 | 0.247974x |
| 0.25 | 2.698216 | 2.911473 | 5.563279 | 0.000604068 | 0.242003x |
| 0.5 | 2.702688 | 2.951677 | 5.563665 | 0.00060146 | 0.246953x |
| 1 | 2.70016 | 3.142346 | 5.563051 | 0.000427696 | 0.249583x |

Best alpha by quality_per_ms in this random-target inference sweep: 0.

## Capability Check

Command: `benchmark-lite --families clrs,listops,scan,dyck --sample-limit 128 --train-steps 50 --scale tiny --device cuda --amp --models fixed_moe,pvr_ec_deploy_top2`

- fixed_moe avg eval loss: 3.928
- pvr_ec_deploy_top2 avg eval loss: 3.987125
- loss delta: 0.059125
- fixed_moe train time: 2.4s
- pvr_ec_deploy_top2 train time: 1.2s
- Verdict: latency path is tight enough for longer capability testing, but fixed_moe still has better loss in the 50-step check.
