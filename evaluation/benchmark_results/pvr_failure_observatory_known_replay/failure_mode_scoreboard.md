# PVR-EC Failure Mode Scoreboard

**Status:** PVR_EC_FAILURE_OBSERVATORY_READY

```json
{
  "status": "PVR_EC_FAILURE_OBSERVATORY_READY",
  "mode_count": 2,
  "scoreboard": [
    {
      "failure_mode": "PVR_EC_FAILURE_OWNER_PROTOTYPE_COLLAPSE",
      "count": 18,
      "repeatable_count": 18,
      "unexplained_count": 0,
      "repaired_count": 0,
      "partial_repair_count": 0,
      "blocked_count": 18,
      "affected_seeds": [
        "123",
        "777"
      ],
      "affected_families": [
        "clrs_style"
      ],
      "affected_tasks": [
        "clrs_lcs",
        "clrs_searching",
        "clrs_sorting"
      ],
      "affected_shapes": [],
      "most_common_primary_metric": "loss_gap_vs_fixed",
      "current_status": "blocked",
      "recommended_next_action": "run bounded repair validation"
    },
    {
      "failure_mode": "PVR_EC_FAILURE_DATA_SPLIT_DIFFICULTY",
      "count": 6,
      "repeatable_count": 6,
      "unexplained_count": 0,
      "repaired_count": 0,
      "partial_repair_count": 0,
      "blocked_count": 6,
      "affected_seeds": [
        "123",
        "777"
      ],
      "affected_families": [
        "listops"
      ],
      "affected_tasks": [
        "listops"
      ],
      "affected_shapes": [],
      "most_common_primary_metric": "loss_gap_vs_fixed",
      "current_status": "blocked",
      "recommended_next_action": "run bounded repair validation"
    }
  ]
}
```