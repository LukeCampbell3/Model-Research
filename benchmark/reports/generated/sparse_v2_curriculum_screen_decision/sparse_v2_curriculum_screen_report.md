# Sparse-v2 Teacher-Free Curriculum Screen

Status: `PVR_SPARSE_V2_CURRICULUM_SCREEN_NOT_SUPPORTED`

| variant | curriculum | aux | prototypes | LM loss | router grad | Top1 |
|---|---|---:|---|---:|---:|---|
| pvr_sparse_v2_full_from_start_aux001_100m | full_training | 0.001 | True | 6.310050904750824 | 23.57001367211342 | True |
| pvr_sparse_v2_shared_then_top1_aux001_100m | shared_then_strict_top1 | 0.01 | True | 6.396109540015459 | 2.41434558480978 | True |
| pvr_sparse_v2_shared_then_top1_no_prototypes_100m | shared_then_strict_top1 | 0.001 | False | 6.417736355215311 | 2.898661883082241 | True |
| pvr_sparse_v2_shared_then_top1_aux0001_100m | shared_then_strict_top1 | 0.001 | True | 6.423189491033554 | 2.9624860994517803 | True |
| pvr_sparse_v2_shared_then_top1_aux0_100m | shared_then_strict_top1 | 0.0 | True | 6.424094211310148 | 3.0931234606541693 | True |
