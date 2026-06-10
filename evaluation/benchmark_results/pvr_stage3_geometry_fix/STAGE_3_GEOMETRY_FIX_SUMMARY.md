# Stage 3 Geometry Fix Summary

## Root Cause Analysis

### Problem
Stage 3 forensics initially showed:
- **Contrastive geometry NOT loaded** (`contrastive_loaded: "False"`)
- **Entropy: 2.68** (vs Stage 2 validated 0.14)
- **Margin: 0.005** (vs Stage 2 validated 0.975)
- **Stage 3 train accuracy: 99.9%**, **holdout accuracy: 23.4%**

### Cause
The `contrastive_light` geometry from Stage 2 (trained with family alignment loss) was not being loaded into Stage 3. The model was re-initialized from scratch without inheriting the trained prototypes.

## Solution Implemented

### Changes to `run_stage3_forensics.py`

1. **Added `build_model(device, prototype_path)` function**
   - Loads prototype geometry from Stage 2 if provided
   - Copies `blocks.0.moe.router.prototypes` to new model

2. **Added `save_stage2_geometry(model, output_path)` function**
   - Saves trained prototype embeddings to disk
   - Stores prototype shape and config metadata

3. **Modified `train_interleaved()` function**
   - Changed from contrastive loss to family alignment loss
   - Added `family_align_weight` and `temperature` parameters
   - Uses temperature=0.5 to sharpen prototype assignments

4. **Updated all training calls**
   - All models now use family alignment training
   - Geometry-loaded models use prototypes from Stage 2

### Key Configuration

```python
# Family alignment loss (from Stage 2 contrastive_light candidate)
family_align_weight = 0.05
temperature = 0.5

# Loss computation:
soft = F.softmax(-dists / temperature, dim=-1)
entropy = -(soft * torch.log(soft + 1e-8)).sum(dim=-1).mean()
loss = loss + family_align_weight * entropy
```

## Results

### Geometry Comparison (100 steps)

| Metric | Baseline | With Family Alignment | Stage 2 (contrastive_light) |
|--------|----------|----------------------|-----------------------------|
| Entropy | 2.77 | 0.29 | 0.14 |
| Margin | 0.003 | 0.95 | 0.975 |
| Boundary Rate | 1.0 | 0.0004 | 0.003 |

### Holdout Split Decomposition

| Split | Accuracy |
|-------|----------|
| Seen task / seen template | 84.5% |
| Seen task / heldout template | 83.2% |
| Heldout task family | 26.5% |

### Verdict: `PVR_EC_STAGE3_HELDOUT_TASK_FAMILY_TRANSFER_BLOCKED`

**Reason:** Same-task templates transfer (83.2%) but new task families don't (26.5%)

This is the expected result - the geometry is now correctly loaded and maintained. The real blocker is task-family transfer failure, not geometry persistence.

## Files Generated

- `pvr_ec_stage3_geometry_load_audit_report.json/md` - Geometry loading verification
- `pvr_ec_stage3_geometry_metric_consistency_report.json/md` - Metric consistency check
- `pvr_ec_stage3_heldout_split_decomposition_report.json/md` - Split analysis
- `pvr_ec_stage3_mixed_task_curriculum_report.json/md` - Curriculum ablation
- `pvr_ec_stage3_forensics_gate_report.json/md` - Final verdict
- `stage2_contrastive_geometry.pt` - Stage 2 geometry for Stage 3 reuse

## Next Steps

1. Apply the prototype geometry fix to the actual Stage 3 training pipeline
2. Investigate task-family transfer failure modes
3. Consider expanding model capacity if family transfer remains blocked

## Hard Invariants Verified

- [x] `owners_per_token = 1.0`
- [x] `Top2 executions = 0`
- [x] `Top4 executions = 0`
- [x] `production_map_mutated = false`
