# Sparse Comparator Runtime Integrity Audit

Status: `SPARSE_COMPARATOR_RUNTIME_INTEGRITY_AUDIT_COMPLETE`

| variant | family | configured K | actual K/token | valid | drops | overflow | fallback |
|---|---|---:|---:|---|---:|---:|---:|
| dense_sparse_v2_300m_matched | dense_transformer | 0 | 0.0 | True | 0 | 0 | 0 |
| switch_top1_sparse_v2_300m_matched | vanilla_switch_top1_reference | 1 | 1.0 | True | 0 | 0 | 0 |
| generic_top2_sparse_v2_300m_matched | generic_top2_moe_reference | 2 | 2.0 | True | 0 | 0 | 0 |
| pvr_teacher_independent_sparse_v2_300m | pvr_ec_o | 1 | 1.0 | True | 0 | 0 | 0 |
