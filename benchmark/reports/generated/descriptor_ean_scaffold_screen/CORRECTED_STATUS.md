# Descriptor Curriculum EAN Scaffold Screen — Corrected Status

**Status:** `PVR_DESCRIPTOR_CURRICULUM_GEOMETRY_BRIDGE_PROBE_COMPLETE`
**Date:** 2026-06-21

## What This Run Proved

The descriptor-curriculum bridge is mechanically viable:
- All six variants can train at 284M params
- Strict Top1 remains intact across all variants
- The 300M infrastructure is usable for this comparison
- Descriptor loss path runs successfully
- Combined descriptor+uniformity variant is functional

## What This Run Did NOT Prove

- `PVR_DESCRIPTOR_CURRICULUM_NARROWS_EAN_GAP`: **BLOCKED**
  - Teacher EAN checkpoint did not load (file not found at expected path)
  - The "teacher" row trained from scratch like all others
  - No valid EAN gap baseline exists in this run

- `PVR_DESCRIPTOR_CURRICULUM_REPLACES_EAN_SCAFFOLD`: **BLOCKED**
  - Same reason: no valid teacher reference

## Results (Curriculum Ablation Only)

| Variant | Eval Loss | Notes |
|---------|-----------|-------|
| pvr_shared_warmup_no_head | 2.983 | Best self-instilled |
| pvr_teacher_ean (NO REAL TEACHER) | 3.022 | Not a valid EAN reference |
| pvr_full_scratch | 3.108 | No warmup, no head |
| pvr_descriptor_plus_uniformity | 3.168 | Combined geometry head |
| pvr_descriptor_curriculum | 3.201 | Descriptor alone |
| pvr_uniformity_geometry_head | 3.221 | Uniformity alone |

## Ordering Within Self-Instilled Variants

```
descriptor + uniformity (3.168) > descriptor alone (3.201) > uniformity alone (3.221)
```

This suggests descriptor curriculum provides a slightly better routing basis than pure uniformity, and combining them is best.

## Required Fixes Before Promotion

The next run must verify before training starts:
```python
assert teacher_ean_checkpoint_exists == True
assert teacher_init_report["copy_scope"] == "embeddings_attention_norms"
assert teacher_init_report["copied_count"] > 0
assert teacher_init_report["teacher_checkpoint_loaded"] == True
```

The runner now includes these checks and will refuse to emit `NARROWS_EAN_GAP` if the teacher reference is invalid.

## Reference: Prior Valid EAN Comparison

From the prior 300M matched-volume screen (with real teacher load):
```
pvr_full_scratch_300m_matched:              4.1527
pvr_shared_warmup_no_geometry_head_300m:    4.1451
pvr_self_instilled_geometry_head_300m:      4.1465
pvr_teacher_ean_300m_matched:               3.1100  ← REAL EAN BASELINE
```

The real EAN gap is approximately **1.04** (scratch 4.15 → teacher 3.11).
The geometry head closed only 0.59% of that gap.
The question remains: can descriptor curriculum close more?
