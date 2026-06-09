# Pvr Ec Prototype Geometry Repair Sweep Report

**Status:** SWEEP_COMPLETE

```json
{
  "status": "SWEEP_COMPLETE",
  "variants": {
    "baseline": {
      "config": {},
      "global_membership_entropy": 2.7697904065631533,
      "global_membership_margin": 0.001603067149509909,
      "dead_prototype_count": 1,
      "low_sample_count": 4,
      "classification_counts": {
        "STABLE_SPECIALIST": 0,
        "HIGH_GAP_MONOPOLY": 6,
        "HIGH_GAP_NON_MONOPOLY": 2,
        "LOW_SAMPLE": 4,
        "GEOMETRY_UNCERTAIN": 0,
        "DEAD_PROTOTYPE": 1,
        "BOUNDARY_EVERYWHERE": 3
      },
      "avg_oracle_gap": 2.2366040034697283,
      "avg_accuracy": 0.6075970235377116
    },
    "temperature_sharpen_0_5": {
      "config": {
        "proto_temperature": 0.5
      },
      "global_membership_entropy": 2.7697904065631533,
      "global_membership_margin": 0.001603067149509909,
      "dead_prototype_count": 1,
      "low_sample_count": 4,
      "classification_counts": {
        "STABLE_SPECIALIST": 0,
        "HIGH_GAP_MONOPOLY": 6,
        "HIGH_GAP_NON_MONOPOLY": 2,
        "LOW_SAMPLE": 4,
        "GEOMETRY_UNCERTAIN": 0,
        "DEAD_PROTOTYPE": 1,
        "BOUNDARY_EVERYWHERE": 3
      },
      "avg_oracle_gap": 2.2366040034697283,
      "avg_accuracy": 0.6075970235377116
    },
    "temperature_sharpen_0_7": {
      "config": {
        "proto_temperature": 0.7
      },
      "global_membership_entropy": 2.7697904065631533,
      "global_membership_margin": 0.001603067149509909,
      "dead_prototype_count": 1,
      "low_sample_count": 4,
      "classification_counts": {
        "STABLE_SPECIALIST": 0,
        "HIGH_GAP_MONOPOLY": 6,
        "HIGH_GAP_NON_MONOPOLY": 2,
        "LOW_SAMPLE": 4,
        "GEOMETRY_UNCERTAIN": 0,
        "DEAD_PROTOTYPE": 1,
        "BOUNDARY_EVERYWHERE": 3
      },
      "avg_oracle_gap": 2.2366040034697283,
      "avg_accuracy": 0.6075970235377116
    },
    "distance_scale_2": {
      "config": {
        "proto_distance_scale": 2.0
      },
      "global_membership_entropy": 2.7697904065631533,
      "global_membership_margin": 0.001603067149509909,
      "dead_prototype_count": 1,
      "low_sample_count": 4,
      "classification_counts": {
        "STABLE_SPECIALIST": 0,
        "HIGH_GAP_MONOPOLY": 6,
        "HIGH_GAP_NON_MONOPOLY": 2,
        "LOW_SAMPLE": 4,
        "GEOMETRY_UNCERTAIN": 0,
        "DEAD_PROTOTYPE": 1,
        "BOUNDARY_EVERYWHERE": 3
      },
      "avg_oracle_gap": 2.2366040034697283,
      "avg_accuracy": 0.6075970235377116
    },
    "distance_scale_4": {
      "config": {
        "proto_distance_scale": 4.0
      },
      "global_membership_entropy": 2.7697904065631533,
      "global_membership_margin": 0.001603067149509909,
      "dead_prototype_count": 1,
      "low_sample_count": 4,
      "classification_counts": {
        "STABLE_SPECIALIST": 0,
        "HIGH_GAP_MONOPOLY": 6,
        "HIGH_GAP_NON_MONOPOLY": 2,
        "LOW_SAMPLE": 4,
        "GEOMETRY_UNCERTAIN": 0,
        "DEAD_PROTOTYPE": 1,
        "BOUNDARY_EVERYWHERE": 3
      },
      "avg_oracle_gap": 2.2366040034697283,
      "avg_accuracy": 0.6075970235377116
    },
    "contrastive_loss_light": {
      "config": {
        "proto_contrastive_weight": 0.01
      },
      "global_membership_entropy": 2.7095776407728485,
      "global_membership_margin": 0.011796157063729421,
      "dead_prototype_count": 2,
      "low_sample_count": 4,
      "classification_counts": {
        "STABLE_SPECIALIST": 1,
        "HIGH_GAP_MONOPOLY": 6,
        "HIGH_GAP_NON_MONOPOLY": 2,
        "LOW_SAMPLE": 4,
        "GEOMETRY_UNCERTAIN": 1,
        "DEAD_PROTOTYPE": 2,
        "BOUNDARY_EVERYWHERE": 0
      },
      "avg_oracle_gap": 1.7845653277566897,
      "avg_accuracy": 0.7353865896592918
    },
    "family_alignment_loss_light": {
      "config": {
        "proto_family_align_weight": 0.1
      },
      "global_membership_entropy": 1.8568849502806102,
      "global_membership_margin": 0.28778788737516975,
      "dead_prototype_count": 9,
      "low_sample_count": 5,
      "classification_counts": {
        "STABLE_SPECIALIST": 0,
        "HIGH_GAP_MONOPOLY": 0,
        "HIGH_GAP_NON_MONOPOLY": 1,
        "LOW_SAMPLE": 5,
        "GEOMETRY_UNCERTAIN": 1,
        "DEAD_PROTOTYPE": 9,
        "BOUNDARY_EVERYWHERE": 0
      },
      "avg_oracle_gap": 3.1695504840020625,
      "avg_accuracy": 0.7375062418834762
    },
    "usage_balance_light": {
      "config": {
        "proto_usage_balance_weight": 0.05
      },
      "global_membership_entropy": 2.771679784693065,
      "global_membership_margin": 0.001220789837263585,
      "dead_prototype_count": 4,
      "low_sample_count": 3,
      "classification_counts": {
        "STABLE_SPECIALIST": 1,
        "HIGH_GAP_MONOPOLY": 6,
        "HIGH_GAP_NON_MONOPOLY": 1,
        "LOW_SAMPLE": 3,
        "GEOMETRY_UNCERTAIN": 0,
        "DEAD_PROTOTYPE": 4,
        "BOUNDARY_EVERYWHERE": 1
      },
      "avg_oracle_gap": 2.3043829698765714,
      "avg_accuracy": 0.7517848472848098
    },
    "warmup_then_route": {
      "config": {
        "proto_warmup_steps": 100
      },
      "global_membership_entropy": 2.7697904065631533,
      "global_membership_margin": 0.001603067149509909,
      "dead_prototype_count": 1,
      "low_sample_count": 4,
      "classification_counts": {
        "STABLE_SPECIALIST": 0,
        "HIGH_GAP_MONOPOLY": 6,
        "HIGH_GAP_NON_MONOPOLY": 2,
        "LOW_SAMPLE": 4,
        "GEOMETRY_UNCERTAIN": 0,
        "DEAD_PROTOTYPE": 1,
        "BOUNDARY_EVERYWHERE": 3
      },
      "avg_oracle_gap": 2.2366040034697283,
      "avg_accuracy": 0.6075970235377116
    },
    "warmup_plus_family_align": {
      "config": {
        "proto_warmup_steps": 100,
        "proto_family_align_weight": 0.1
      },
      "global_membership_entropy": 2.097964437069629,
      "global_membership_margin": 0.20905814149831242,
      "dead_prototype_count": 6,
      "low_sample_count": 5,
      "classification_counts": {
        "STABLE_SPECIALIST": 0,
        "HIGH_GAP_MONOPOLY": 3,
        "HIGH_GAP_NON_MONOPOLY": 0,
        "LOW_SAMPLE": 5,
        "GEOMETRY_UNCERTAIN": 1,
        "DEAD_PROTOTYPE": 6,
        "BOUNDARY_EVERYWHERE": 1
      },
      "avg_oracle_gap": 1.9815059801192767,
      "avg_accuracy": 0.608750087411144
    }
  }
}
```