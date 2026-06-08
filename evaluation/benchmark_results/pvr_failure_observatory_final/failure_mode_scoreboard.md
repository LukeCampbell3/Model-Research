# PVR-EC Failure Mode Scoreboard

**Status:** PVR_EC_FAILURE_OBSERVATORY_READY

```json
{
  "status": "PVR_EC_FAILURE_OBSERVATORY_READY",
  "mode_count": 3,
  "scoreboard": [
    {
      "failure_mode": "PVR_EC_FAILURE_OWNER_PROTOTYPE_COLLAPSE",
      "count": 79,
      "repeatable_count": 79,
      "unexplained_count": 0,
      "repaired_count": 0,
      "partial_repair_count": 0,
      "blocked_count": 79,
      "affected_seeds": [
        "123",
        "777"
      ],
      "affected_families": [
        "clrs_style",
        "scan_style"
      ],
      "affected_tasks": [
        "clrs_lcs",
        "clrs_searching",
        "clrs_sorting",
        "scan_random",
        "sort"
      ],
      "affected_shapes": [],
      "most_common_primary_metric": "loss_gap_vs_fixed",
      "current_status": "blocked",
      "recommended_next_action": "run bounded repair validation"
    },
    {
      "failure_mode": "PVR_EC_FAILURE_QPM_SHAPE_REGRESSION",
      "count": 28,
      "repeatable_count": 28,
      "unexplained_count": 0,
      "repaired_count": 0,
      "partial_repair_count": 0,
      "blocked_count": 28,
      "affected_seeds": [
        "123",
        "42",
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
      "failure_mode": "PVR_EC_FAILURE_DATA_SPLIT_DIFFICULTY",
      "count": 87,
      "repeatable_count": 87,
      "unexplained_count": 0,
      "repaired_count": 0,
      "partial_repair_count": 0,
      "blocked_count": 87,
      "affected_seeds": [
        "123",
        "777"
      ],
      "affected_families": [
        "dyck",
        "listops",
        "scan_style"
      ],
      "affected_tasks": [
        "dyck_completion",
        "dyck_validation",
        "listops",
        "scan_length",
        "scan_random"
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