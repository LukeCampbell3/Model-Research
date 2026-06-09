# Pvr Ec Prototype Bucket Report

**Status:** BUCKETING_COMPLETE

```json
{
  "status": "BUCKETING_COMPLETE",
  "buckets": {
    "PROTECT_STABLE_OWNER": [],
    "REPAIR_HIGH_GAP_MONOPOLY": [
      0,
      2,
      7,
      9,
      10,
      13
    ],
    "REPAIR_HIGH_GAP_NON_MONOPOLY": [
      5
    ],
    "LOW_SAMPLE_WATCHLIST": [
      1,
      3,
      6,
      12,
      14,
      15
    ],
    "PROTOTYPE_GEOMETRY_UNCERTAIN": [
      4,
      8
    ]
  },
  "bucket_counts": {
    "PROTECT_STABLE_OWNER": 0,
    "REPAIR_HIGH_GAP_MONOPOLY": 6,
    "REPAIR_HIGH_GAP_NON_MONOPOLY": 1,
    "LOW_SAMPLE_WATCHLIST": 6,
    "PROTOTYPE_GEOMETRY_UNCERTAIN": 2
  },
  "per_prototype_metrics": {
    "0": {
      "prototype_id": 0,
      "token_count": 606,
      "dominant_owner": 1,
      "dominant_owner_share": 1.0,
      "owner_entropy": -9.999999889225291e-09,
      "accuracy": 0.1188118811881188,
      "avg_loss": 11.684510825109731,
      "oracle_gap_proxy": 11.684510825109731,
      "direct_oracle_gap": 0.0,
      "membership_entropy": 2.7704110192780447,
      "membership_margin": 0.0014800101813703481,
      "boundary_rate": 1.0,
      "challenger_disagree_rate": 1.0,
      "is_monopolized": "True",
      "bucket": "REPAIR_HIGH_GAP_MONOPOLY"
    },
    "1": {
      "prototype_id": 1,
      "token_count": 8,
      "dominant_owner": 3,
      "dominant_owner_share": 1.0,
      "owner_entropy": -9.999999889225291e-09,
      "accuracy": 0.125,
      "avg_loss": 8.157021716237068,
      "oracle_gap_proxy": 8.157021716237068,
      "direct_oracle_gap": 0.0,
      "membership_entropy": 2.770341008901596,
      "membership_margin": 0.00016060099005699158,
      "boundary_rate": 1.0,
      "challenger_disagree_rate": 1.0,
      "is_monopolized": "True",
      "bucket": "LOW_SAMPLE_WATCHLIST"
    },
    "2": {
      "prototype_id": 2,
      "token_count": 2742,
      "dominant_owner": 3,
      "dominant_owner_share": 1.0,
      "owner_entropy": -9.999999889225291e-09,
      "accuracy": 0.10357403355215171,
      "avg_loss": 9.417355821107781,
      "oracle_gap_proxy": 9.389879947085586,
      "direct_oracle_gap": 0.0,
      "membership_entropy": 2.7683855142148195,
      "membership_margin": 0.0018311017549533552,
      "boundary_rate": 1.0,
      "challenger_disagree_rate": 0.9970824215900802,
      "is_monopolized": "True",
      "bucket": "REPAIR_HIGH_GAP_MONOPOLY"
    },
    "3": {
      "prototype_id": 3,
      "token_count": 5,
      "dominant_owner": 3,
      "dominant_owner_share": 1.0,
      "owner_entropy": -9.999999889225291e-09,
      "accuracy": 0.0,
      "avg_loss": 11.920523548126221,
      "oracle_gap_proxy": 4.768209419250488,
      "direct_oracle_gap": 0.0,
      "membership_entropy": 2.7704043865203856,
      "membership_margin": 0.0003995716571807861,
      "boundary_rate": 1.0,
      "challenger_disagree_rate": 0.4,
      "is_monopolized": "True",
      "bucket": "LOW_SAMPLE_WATCHLIST"
    },
    "4": {
      "prototype_id": 4,
      "token_count": 127,
      "dominant_owner": 3,
      "dominant_owner_share": 1.0,
      "owner_entropy": -9.999999889225291e-09,
      "accuracy": 0.07086614173228346,
      "avg_loss": 8.414343817504196,
      "oracle_gap_proxy": 2.5839323534068006,
      "direct_oracle_gap": 0.0,
      "membership_entropy": 2.7709594993140754,
      "membership_margin": 0.001192071365089867,
      "boundary_rate": 1.0,
      "challenger_disagree_rate": 0.30708661417322836,
      "is_monopolized": "True",
      "bucket": "PROTOTYPE_GEOMETRY_UNCERTAIN"
    },
    "5": {
      "prototype_id": 5,
      "token_count": 435,
      "dominant_owner": 1,
      "dominant_owner_share": 0.7540229885057471,
      "owner_entropy": 0.5578721057152979,
      "accuracy": 0.04597701149425287,
      "avg_loss": 9.57844615767485,
      "oracle_gap_proxy": 9.49036849185715,
      "direct_oracle_gap": 0.0,
      "membership_entropy": 2.769504244574185,
      "membership_margin": 0.0008273615062921897,
      "boundary_rate": 1.0,
      "challenger_disagree_rate": 0.9908045977011494,
      "is_monopolized": "False",
      "bucket": "REPAIR_HIGH_GAP_NON_MONOPOLY"
    },
    "6": {
      "prototype_id": 6,
      "token_count": 13,
      "dominant_owner": 1,
      "dominant_owner_share": 0.7692307692307693,
      "owner_entropy": 0.5402041223888612,
      "accuracy": 0.38461538461538464,
      "avg_loss": 6.3325072802030125,
      "oracle_gap_proxy": 5.35827539094101,
      "direct_oracle_gap": 0.0,
      "membership_entropy": 2.769992681650015,
      "membership_margin": 0.0022915813785332898,
      "boundary_rate": 1.0,
      "challenger_disagree_rate": 0.8461538461538461,
      "is_monopolized": "False",
      "bucket": "LOW_SAMPLE_WATCHLIST"
    },
    "7": {
      "prototype_id": 7,
      "token_count": 83,
      "dominant_owner": 3,
      "dominant_owner_share": 0.927710843373494,
      "owner_entropy": 0.25952041553030963,
      "accuracy": 0.0963855421686747,
      "avg_loss": 10.347236181777644,
      "oracle_gap_proxy": 9.973239693279657,
      "direct_oracle_gap": 2.9649916
```