# Pvr Ec Stage3 Heldout Split Decomposition Report
**Status:** DECOMPOSED

```json
{
  "status": "DECOMPOSED",
  "seen_task_seen_template": {
    "avg_accuracy": 0.9988665481408437,
    "per_task": {
      "compositional_grammar": {
        "loss": 0.0019232380436733365,
        "accuracy": 0.9955357313156128
      },
      "agreement_dependency": {
        "loss": 0.00017249384836759418,
        "accuracy": 1.0
      },
      "negation_polarity": {
        "loss": 0.00028842530446127057,
        "accuracy": 1.0
      },
      "ambiguous_word_sense": {
        "loss": 0.0003271993191447109,
        "accuracy": 1.0
      },
      "coreference_memory": {
        "loss": 0.000673552043735981,
        "accuracy": 1.0
      },
      "instruction_micro": {
        "loss": 0.0060938941314816475,
        "accuracy": 0.9976635575294495
      }
    }
  },
  "seen_task_heldout_template": {
    "avg_accuracy": 0.9504934847354889,
    "per_task": {
      "compositional_grammar": {
        "loss": 0.04484274238348007,
        "accuracy": 0.8883928656578064
      },
      "agreement_dependency": {
        "loss": 0.0024048364721238613,
        "accuracy": 0.96875
      },
      "negation_polarity": {
        "loss": 0.0007092274609021842,
        "accuracy": 1.0
      },
      "ambiguous_word_sense": {
        "loss": 0.00034519084147177637,
        "accuracy": 1.0
      },
      "coreference_memory": {
        "loss": 0.02635662816464901,
        "accuracy": 0.94140625
      },
      "instruction_micro": {
        "loss": 0.08869737386703491,
        "accuracy": 0.904411792755127
      }
    }
  },
  "heldout_task_family": {
    "avg_accuracy": 0.23389232903718948,
    "per_task": {
      "multisentence_delimiter": {
        "loss": 3.170548439025879,
        "accuracy": 0.04545454680919647
      },
      "paraphrase_invariance": {
        "loss": 0.46601492166519165,
        "accuracy": 0.4223301112651825
      }
    }
  },
  "geometry_after_partial_training": {
    "entropy": 2.667545199394226,
    "margin": 0.006413224618881941,
    "boundary": 1.0
  }
}
```