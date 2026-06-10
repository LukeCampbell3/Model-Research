# Descriptor Convergence
```json
{
  "status": "CONVERGENCE_TESTED",
  "results": {
    "s300_seed42": {
      "correct": 0.9336433040764383,
      "wrong": 0.8817352511918229,
      "removed": 0.34543026220227285,
      "corrupt": 0.8880829074418229,
      "margin": 0.05190805288461531
    },
    "s300_seed123": {
      "correct": 0.9555535397516529,
      "wrong": 0.7966375112476427,
      "removed": 0.22797729104599362,
      "corrupt": 0.7807176170163488,
      "margin": 0.1589160285040102
    },
    "s300_seed777": {
      "correct": 0.9764163534671347,
      "wrong": 0.44939468764641366,
      "removed": 0.23388159519609375,
      "corrupt": 0.7755138633973258,
      "margin": 0.5270216658207211
    },
    "s300_seed2026": {
      "correct": 0.8995652406941959,
      "wrong": 0.8037207797023772,
      "removed": 0.2075771295997743,
      "corrupt": 0.6361775403783669,
      "margin": 0.09584446099181865
    },
    "s300_seed9001": {
      "correct": 0.9893983725644064,
      "wrong": 0.8861836491750507,
      "removed": 0.3138988517961301,
      "corrupt": 0.9120776005055828,
      "margin": 0.10321472338935578
    }
  },
  "best_key": "s300_seed777",
  "best_margin": 0.5270216658207211,
  "best_correct": 0.9764163534671347,
  "passes_threshold": true,
  "hard_invariants": {
    "owners_per_token": 1.0,
    "top2_executions": 0,
    "top4_executions": 0,
    "production_map_mutated": false
  },
  "total_time_s": 558.3764541149139
}
```