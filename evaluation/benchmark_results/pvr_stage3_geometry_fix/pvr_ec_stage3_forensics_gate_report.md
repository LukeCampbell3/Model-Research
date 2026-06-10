# Pvr Ec Stage3 Forensics Gate Report
**Status:** PVR_EC_STAGE3_HELDOUT_TASK_FAMILY_TRANSFER_BLOCKED

```json
{
  "status": "PVR_EC_STAGE3_HELDOUT_TASK_FAMILY_TRANSFER_BLOCKED",
  "verdict": "PVR_EC_STAGE3_HELDOUT_TASK_FAMILY_TRANSFER_BLOCKED",
  "reason": "Same-task templates transfer (0.832) but new task families don't (0.265)",
  "geometry_loaded": "True",
  "metrics_consistent": true,
  "contrastive_geometry": {
    "entropy": 0.2917430251836777,
    "margin": 0.9521952867507935,
    "boundary": 0.0003662109375
  },
  "baseline_geometry": {
    "entropy": 2.768761247396469,
    "margin": 0.0034541761269792914,
    "boundary": 1.0
  },
  "train6_geometry": {
    "entropy": 0.29638171941041946,
    "margin": 0.9453111886978149,
    "boundary": 0.0064697265625
  },
  "seen_task_accuracy": 0.8453239103158315,
  "seen_task_heldout_template_accuracy": 0.8322403430938721,
  "heldout_task_family_accuracy": 0.26456311345100403,
  "curriculum_results": {
    "single_task_multisentence_delimiter": 0.5454545617103577,
    "single_task_paraphrase_invariance": 0.6699029207229614,
    "all_task_uniform_holdout_acc": 0.891392707824707,
    "augmented_holdout_acc": 0.8027561604976654,
    "augmented_seen_acc": 0.8712919354438782
  },
  "hard_invariants": {
    "owners_per_token": 1.0,
    "top2": 0,
    "top4": 0,
    "map_mutated": false
  },
  "total_time_s": 83.71202778816223
}
```