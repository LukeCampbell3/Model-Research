# Paired LM Significance

Status: `PVR_SPARSE_V2_LOCAL_SIGNIFICANCE_SUPPORTED`

| baseline | loss delta | 95% CI | active delta | significant |
|---|---:|---:|---:|---|
| dense_v2_100m_matched | 0.3648565043695271 | [0.3220788692124188, 0.41136553045362234] | -70078464 | False |
| switch_top1_sparse_v2_100m_matched | -0.6706014820374548 | [-0.705924276728183, -0.6360938283614814] | 8345472 | True |
| generic_top2_sparse_v2_100m_matched | -0.49484658846631646 | [-0.5298057002946734, -0.45891587948426604] | -2877696 | True |
