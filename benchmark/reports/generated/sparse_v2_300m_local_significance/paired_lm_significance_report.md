# Paired LM Significance

Status: `PVR_SPARSE_V2_LOCAL_SIGNIFICANCE_SUPPORTED`

| baseline | loss delta | 95% CI | active delta | significant |
|---|---:|---:|---:|---|
| dense_sparse_v2_300m_matched | 0.10677952994592488 | [0.08234965684823692, 0.13011069991625845] | -110278176 | False |
| switch_top1_sparse_v2_300m_matched | -0.07805347559042275 | [-0.1025221892632544, -0.051330351969227195] | 16350144 | True |
| generic_top2_sparse_v2_300m_matched | -0.13574328343383968 | [-0.1553028777707368, -0.11656093806959689] | -1574496 | True |
