# PVR-EC Failure Mode Scoreboard

**Status:** PVR_EC_FAILURE_OBSERVATORY_READY

```json
{
  "status": "PVR_EC_FAILURE_OBSERVATORY_READY",
  "mode_count": 3,
  "scoreboard": [
    {
      "failure_mode": "PVR_EC_FAILURE_QPM_SHAPE_REGRESSION",
      "count": 22,
      "repeatable_count": 22,
      "unexplained_count": 0,
      "repaired_count": 0,
      "partial_repair_count": 0,
      "blocked_count": 22,
      "affected_seeds": [
        "123",
        "777"
      ],
      "affected_families": [
        "clrs_style",
        "listops"
      ],
      "affected_tasks": [
        "clrs_lcs",
        "clrs_searching",
        "clrs_sorting",
        "listops"
      ],
      "affected_shapes": [
        "b16-s128",
        "b16-s64",
        "b32-s128",
        "b32-s16",
        "b32-s64",
        "b64-s128",
        "b64-s16",
        "b64-s64",
        "b8-s64"
      ],
      "most_common_primary_metric": "loss_gap_vs_fixed",
      "current_status": "blocked",
      "recommended_next_action": "run bounded repair validation"
    },
    {
      "failure_mode": "PVR_EC_FAILURE_OWNER_PROTOTYPE_COLLAPSE",
      "count": 14,
      "repeatable_count": 14,
      "unexplained_count": 0,
      "repaired_count": 0,
      "partial_repair_count": 0,
      "blocked_count": 14,
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
      "count": 12,
      "repeatable_count": 12,
      "unexplained_count": 0,
      "repaired_count": 0,
      "partial_repair_count": 0,
      "blocked_count": 12,
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
      "affected_shapes": [
        "b1-s16",
        "b1-s64",
        "b32-s16",
        "b8-s16"
      ],
      "most_common_primary_metric": "loss_gap_vs_fixed",
      "current_status": "blocked",
      "recommended_next_action": "run bounded repair validation"
    }
  ]
}
```