# Pvr Ec Stage3C Fewshot Context Report
**Status:** PVR_EC_STAGE3C_TRANSFER_CONDITIONING_TESTED

```json
{
  "status": "PVR_EC_STAGE3C_TRANSFER_CONDITIONING_TESTED",
  "baseline_heldout_acc": 0.26722013764083385,
  "k0": {
    "accuracy": 0.26722013764083385,
    "gain": 0.0
  },
  "k1": {
    "accuracy": 0.1754652066156268,
    "gain": -0.09175493102520704,
    "per_task": {
      "multisentence_delimiter": {
        "loss": 2.051335334777832,
        "accuracy": 0.02083333395421505
      },
      "paraphrase_invariance": {
        "loss": 0.26256680488586426,
        "accuracy": 0.3300970792770386
      }
    }
  },
  "k4": {
    "accuracy": NaN,
    "gain": NaN,
    "per_task": {
      "multisentence_delimiter": {
        "loss": 0.2419130951166153,
        "accuracy": NaN
      },
      "paraphrase_invariance": {
        "loss": 0.6875688433647156,
        "accuracy": 0.1553398072719574
      }
    }
  },
  "k8": {
    "accuracy": NaN,
    "gain": NaN,
    "per_task": {
      "multisentence_delimiter": {
        "loss": 0.07871858030557632,
        "accuracy": NaN
      },
      "paraphrase_invariance": {
        "loss": 0.13287395238876343,
        "accuracy": NaN
      }
    }
  },
  "fewshot_helpful": false,
  "monotonic": "False"
}
```