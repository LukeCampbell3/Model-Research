# Pvr Ec Stage3 Forensics Gate Report
**Status:** PVR_EC_STAGE3_GEOMETRY_NOT_LOADED

```json
{
  "status": "PVR_EC_STAGE3_GEOMETRY_NOT_LOADED",
  "verdict": "PVR_EC_STAGE3_GEOMETRY_NOT_LOADED",
  "reason": "Contrastive geometry was not successfully loaded/maintained",
  "geometry_loaded": "False",
  "metrics_consistent": true,
  "contrastive_geometry": {
    "entropy": 2.6840157508850098,
    "margin": 0.01762241101823747,
    "boundary": 1.0
  },
  "baseline_geometry": {
    "entropy": 2.7686714231967926,
    "margin": 0.0017898039950523525,
    "boundary": 1.0
  },
  "train6_geometry": {
    "entropy": 2.667545199394226,
    "margin": 0.006413224618881941,
    "boundary": 1.0
  },
  "seen_task_accuracy": 0.9988665481408437,
  "seen_task_heldout_template_accuracy": 0.9504934847354889,
  "heldout_task_family_accuracy": 0.23389232903718948,
  "curriculum_results": {
    "single_task_multisentence_delimiter": 1.0,
    "single_task_paraphrase_invariance": 0.9029126167297363,
    "all_task_uniform_holdout_acc": 0.9943181872367859,
    "augmented_holdout_acc": 0.8883587718009949,
    "augmented_seen_acc": 0.9598075151443481
  },
  "hard_invariants": {
    "owners_per_token": 1.0,
    "top2": 0,
    "top4": 0,
    "map_mutated": false
  },
  "total_time_s": 176.7632577419281
}
```