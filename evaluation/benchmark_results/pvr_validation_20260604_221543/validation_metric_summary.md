# PVR-EC GPU Validation Metric Comparison

**Docker image:** sparse-loop-moe-gpu
**Device:** NVIDIA GeForce RTX 4080 SUPER
**Command family:** benchmark-lite, tiny scale, 10 train steps, 64 sample limit, Dyck family, CUDA AMP, seed 42
**Compared models:** fixed_moe vs pvr_ec
**Validation note:** This is a wall-clock regression check, not a promotion-quality benchmark.

## Mode Comparison vs fixed_moe

| PVR mode | PVR loss | Fixed loss | Loss delta | Train slowdown | Inference slowdown | PVR train s | Fixed train s | PVR infer s | Fixed infer s | Dispatch overhead | Avg K |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| dense_all_experts | 4.606745 | 4.578053 | 0.028692 | 0.98x | 2.65x | 0.965 | 0.986 | 0.09 | 0.034 | 0.910429 | 3.455139 |
| fixed_top2_pack_by_expert | 4.605988 | 4.578053 | 0.027935 | 1.06x | 2.87x | 0.943 | 0.887 | 0.089 | 0.031 | 0.825103 | 2 |
| fixed_top2_all_experts_masked | 4.602884 | 4.578053 | 0.024831 | 1.08x | 2.81x | 0.933 | 0.861 | 0.09 | 0.032 | 0.859756 | 2 |
| variable_k_pack_by_expert | 4.606796 | 4.578053 | 0.028743 | 1.19x | 2.97x | 1.072 | 0.904 | 0.095 | 0.032 | 0.872998 | 3.454142 |
| hybrid_expert_choice_bucketed | 4.607866 | 4.578053 | 0.029813 | 1.23x | 3.26x | 1.024 | 0.83 | 0.101 | 0.031 | 0.867059 | 3.513407 |

## Interpretation

- The prior pathological training slowdowns are gone in this validation setup.
- PVR-EC training wall-clock is now comparable to fixed_moe across the tested execution modes.
- Inference is still slower than fixed_moe, around 2.65x to 3.26x in this small run.
- PVR-EC still trails fixed_moe on loss in this short validation run, so this is not a promotion signal.
- Hard runtime branching remains disabled; branch tickets remain shadow-only and capped.

## Raw Averages

| Mode | Model | Avg acc | Avg loss | Avg QPC | Avg train s | Avg infer s | Params | Dispatch overhead | Avg K |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| dense_all_experts | fixed_moe | 0 | 4.578053 | 0 | 0.986 | 0.034 | 260932 | 0 | 0 |
| dense_all_experts | pvr_ec | 0 | 4.606745 | 0 | 0.965 | 0.09 | 136194 | 0.910429 | 3.455139 |
| fixed_top2_all_experts_masked | fixed_moe | 0 | 4.578053 | 0 | 0.861 | 0.032 | 260932 | 0 | 0 |
| fixed_top2_all_experts_masked | pvr_ec | 0 | 4.602884 | 0 | 0.933 | 0.09 | 136194 | 0.859756 | 2 |
| fixed_top2_pack_by_expert | fixed_moe | 0 | 4.578053 | 0 | 0.887 | 0.031 | 260932 | 0 | 0 |
| fixed_top2_pack_by_expert | pvr_ec | 0 | 4.605988 | 0 | 0.943 | 0.089 | 136194 | 0.825103 | 2 |
| hybrid_expert_choice_bucketed | fixed_moe | 0 | 4.578053 | 0 | 0.83 | 0.031 | 260932 | 0 | 0 |
| hybrid_expert_choice_bucketed | pvr_ec | 0 | 4.607866 | 0 | 1.024 | 0.101 | 136194 | 0.867059 | 3.513407 |
| variable_k_pack_by_expert | fixed_moe | 0 | 4.578053 | 0 | 0.904 | 0.032 | 260932 | 0 | 0 |
| variable_k_pack_by_expert | pvr_ec | 0 | 4.606796 | 0 | 1.072 | 0.095 | 136194 | 0.872998 | 3.454142 |
