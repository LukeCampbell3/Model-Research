# Repository Storage Cleanup

Status: `REPOSITORY_STORAGE_CLEANUP_COMPLETE`

Reports and configs were retained. Checkpoint pruning kept current authoritative evidence and removed intermediate, obsolete, empty, invalid, or duplicate model artifacts. Final scan found no model-like binaries outside `checkpoints`. Legacy `evaluation/benchmark_results` generated output was removed from local storage and ignored for future runs.

## Removed Groups

- Python __pycache__ and .pytest_cache directories
- pvr_router_regret_repair_screen 500K intermediate checkpoints
- non-winning pvr_shared_substrate_repair_screen checkpoint variants
- obsolete benchmark_100m, benchmark_300m, benchmark_500m checkpoint groups
- obsolete shared-trunk/dense-mimic/RBA checkpoint groups
- official_like_router_aux_sweep checkpoints
- empty benchmark_700m and official_300m_compute_matched checkpoint directories
- invalid pvr_teacher_independent_sparse_v2_300m_aux0005_long_curve checkpoint
- small stale evaluation/release .pt model artifacts outside checkpoints
- legacy evaluation/benchmark_results generated output tree
- empty directories left by checkpoint and generated-output pruning

## Remaining Checkpoint Groups

| group | GB | files | reason |
|---|---:|---:|---|
| pvr_router_regret_repair_1m_confirmation | 6.887 | 26 | kept: current no-regret baseline and regret0p01 diagnostic checkpoints for router-repair evidence. |
| pvr_shared_substrate_repair_screen | 3.443 | 13 | kept: only winner checkpoint remains, pvr_shared_substrate_full_transformer_random_ean_300m. |
| sparse_v2_300m_confirmation | 4.483 | 52 | kept: 300M sparse-v2 confirmation/official bounded comparator checkpoints. |
| sparse_v2_300m_long_curve_validation | 4.484 | 52 | kept: valid 5M long-curve comparator checkpoints; invalid aux0005 checkpoint removed. |
