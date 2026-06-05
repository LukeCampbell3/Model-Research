# PVR-EC GPU Validation Metric Comparison

**Docker image:** sparse-loop-moe-gpu
**Device:** NVIDIA GeForce RTX 4080 SUPER
**Command family:** benchmark-lite, tiny scale, 50 train steps, 128 sample limit, all algorithmic families, CUDA AMP, seed 42
**Compared models:** fixed_moe vs pvr_ec

## Mode Comparison vs fixed_moe

| PVR mode | PVR acc | Fixed acc | Acc delta | PVR loss | Fixed loss | Loss delta | Train slowdown | Infer slowdown | QPC ratio |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| fixed_top2_all_experts_masked | 0.000194 | 0.000937 | -0.000743 | 3.97486 | 3.927905 | 0.046955 | 136.44x | 305.7x | 0.415 |
| dense_all_experts | 9.7E-05 | 0.000937 | -0.00084 | 3.975239 | 3.927905 | 0.047334 | 124.46x | 295.66x | 0.207 |
| variable_k_pack_by_expert | 9.7E-05 | 0.000937 | -0.00084 | 3.97561 | 3.927905 | 0.047705 | 140.21x | 308.03x | 0.207 |
| fixed_top2_pack_by_expert | 0.000161 | 0.000937 | -0.000776 | 3.975986 | 3.927905 | 0.048081 | 138.71x | 308.84x | 0.344 |
| hybrid_expert_choice_bucketed | 6.5E-05 | 0.000937 | -0.000872 | 3.976473 | 3.927905 | 0.048568 | 260.4x | 516.24x | 0.139 |

## Raw Averages

| Mode | Model | Avg acc | Avg loss | Avg QPC | Avg train s | Avg infer s | Params |
|---|---|---:|---:|---:|---:|---:|---:|
| dense_all_experts | fixed_moe | 0.000937 | 3.927905 | 0.000468 | 2.553 | 0.038 | 260932 |
| dense_all_experts | pvr_ec | 9.7E-05 | 3.975239 | 9.7E-05 | 317.741 | 11.235 | 169218 |
| fixed_top2_all_experts_masked | fixed_moe | 0.000937 | 3.927905 | 0.000468 | 2.325 | 0.037 | 260932 |
| fixed_top2_all_experts_masked | pvr_ec | 0.000194 | 3.97486 | 0.000194 | 317.219 | 11.311 | 169218 |
| fixed_top2_pack_by_expert | fixed_moe | 0.000937 | 3.927905 | 0.000468 | 2.305 | 0.037 | 260932 |
| fixed_top2_pack_by_expert | pvr_ec | 0.000161 | 3.975986 | 0.000161 | 319.738 | 11.427 | 169218 |
| hybrid_expert_choice_bucketed | fixed_moe | 0.000937 | 3.927905 | 0.000468 | 2.268 | 0.037 | 260932 |
| hybrid_expert_choice_bucketed | pvr_ec | 6.5E-05 | 3.976473 | 6.5E-05 | 590.589 | 19.101 | 169218 |
| variable_k_pack_by_expert | fixed_moe | 0.000937 | 3.927905 | 0.000468 | 2.275 | 0.037 | 260932 |
| variable_k_pack_by_expert | pvr_ec | 9.7E-05 | 3.97561 | 9.7E-05 | 318.985 | 11.397 | 169218 |

## Interpretation

- fixed_moe remains the validation baseline winner at this budget.
- PVR-EC does not beat fixed_moe on loss, accuracy, quality-per-compute, training wall-clock, or inference wall-clock.
- fixed_top2_all_experts_masked is the best PVR mode by loss in this run, but still trails fixed_moe.
- hybrid_expert_choice_bucketed is the slowest PVR mode and does not show a quality offset here.
- This supports keeping PVR-EC in diagnostic/shadow mode rather than promoting it.
