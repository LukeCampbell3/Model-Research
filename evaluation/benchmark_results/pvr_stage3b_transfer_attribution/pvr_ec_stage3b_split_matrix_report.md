# Pvr Ec Stage3B Split Matrix Report
**Status:** PVR_EC_STAGE3B_TRANSFER_ATTRIBUTION_COMPLETE

```json
{
  "status": "PVR_EC_STAGE3B_TRANSFER_ATTRIBUTION_COMPLETE",
  "splits": {
    "seen_task_seen_template": {
      "accuracy": 0.9595772425333658
    },
    "seen_task_heldout_template": {
      "accuracy": 0.8899407982826233
    },
    "all_task_uniform_heldout_template": {
      "accuracy": 0.7864879663102329
    },
    "heldout_task_family_zero_shot_no_descriptor": {
      "accuracy": 0.26722013764083385
    },
    "heldout_task_family_zero_shot_with_descriptor": {
      "accuracy": 0.05919020250439644,
      "gain": -0.20802993513643742
    },
    "heldout_task_family_fewshot_1": {
      "accuracy": 0.26722013764083385,
      "gain": 0.0
    },
    "heldout_task_family_fewshot_4": {
      "accuracy": 0.26722013764083385,
      "gain": 0.0
    },
    "heldout_task_family_fewshot_8": {
      "accuracy": 0.26722013764083385,
      "gain": 0.0
    },
    "heldout_operator_composition": {
      "accuracy": 0.26722013764083385
    },
    "heldout_role_binding": {
      "accuracy": 0.26722013764083385
    }
  },
  "results": {
    "seen_task_seen_template": {
      "compositional_grammar": {
        "loss": 0.00607989402487874,
        "accuracy": 0.9910714030265808,
        "exact_match": 0.0
      },
      "agreement_dependency": {
        "loss": 0.0007313513197004795,
        "accuracy": 1.0,
        "exact_match": 0.0
      },
      "negation_polarity": {
        "loss": 0.012611485086381435,
        "accuracy": 0.949438214302063,
        "exact_match": 0.0
      },
      "ambiguous_word_sense": {
        "loss": 0.0010763757163658738,
        "accuracy": 1.0,
        "exact_match": 0.0
      },
      "coreference_memory": {
        "loss": 0.004611761309206486,
        "accuracy": 0.9921875,
        "exact_match": 0.0
      },
      "instruction_micro": {
        "loss": 0.11138026416301727,
        "accuracy": 0.8247663378715515,
        "exact_match": 0.0
      }
    },
    "seen_task_heldout_template": {
      "compositional_grammar": {
        "loss": 0.04726698249578476,
        "accuracy": 0.8883928656578064,
        "exact_match": 0.0
      },
      "agreement_dependency": {
        "loss": 0.004530634731054306,
        "accuracy": 0.96875,
        "exact_match": 0.0
      },
      "negation_polarity": {
        "loss": 0.026872599497437477,
        "accuracy": 0.8920454382896423,
        "exact_match": 0.0
      },
      "ambiguous_word_sense": {
        "loss": 0.0010215011425316334,
        "accuracy": 1.0,
        "exact_match": 0.0
      },
      "coreference_memory": {
        "loss": 0.0389057993888855,
        "accuracy": 0.93359375,
        "exact_match": 0.0
      },
      "instruction_micro": {
        "loss": 0.23771266639232635,
        "accuracy": 0.656862735748291,
        "exact_match": 0.0
      }
    },
    "all_task_uniform_heldout_template": {
      "compositional_grammar": {
        "loss": 0.00607989402487874,
        "accuracy": 0.9910714030265808,
        "exact_match": 0.0
      },
      "agreement_dependency": {
        "loss": 0.0007313513197004795,
        "accuracy": 1.0,
        "exact_match": 0.0
      },
      "negation_polarity": {
        "loss": 0.012611485086381435,
        "accuracy": 0.949438214302063,
        "exact_match": 0.0
      },
      "ambiguous_word_sense": {
        "loss": 0.0010763757163658738,
        "accuracy": 1.0,
        "exact_match": 0.0
      },
      "coreference_memory": {
        "loss": 0.004611761309206486,
        "accuracy": 0.9921875,
        "exact_match": 0.0
      },
      "instruction_micro": {
        "loss": 0.11138026416301727,
        "accuracy": 0.8247663378715515,
        "exact_match": 0.0
      },
      "multisentence_delimiter": {
        "loss": 2.658726215362549,
        "accuracy": 0.05871212109923363,
        "exact_match": 0.0
      },
      "paraphrase_invariance": {
        "loss": 0.3310430347919464,
        "accuracy": 0.4757281541824341,
        "exact_match": 0.0
      }
    },
    "heldout_task_family_zero_shot_no_descriptor": {
      "multisentence_delimiter": {
        "loss": 2.658726215362549,
        "accuracy": 0.05871212109923363,
        "exact_match": 0.0
      },
      "paraphrase_invariance": {
        "loss": 0.3310430347919464,
        "accuracy": 0.4757281541824341,
        "exact_match": 0.0
      }
    },
    "heldout_task_family_zero_shot_with_descriptor": {
      "multisentence_delimiter": {
        "loss": 2.903611183166504,
        "accuracy": 0.07954545319080353,
        "exact_match": 0.0
      },
      "paraphrase_invariance": {
        "loss": 1.3131734132766724,
        "accuracy": 0.03883495181798935,
        "exact_match": 0.0
      }
    },
    "heldout_task_family_fewshot_1": {
      "multisentence_delimiter": {
        "loss": 2.658726215362549,
        "accuracy": 0.05871212109923363,
        "exact_match": 0.0
      },
      "paraphrase_invariance": {
        "loss": 0.3310430347919464,
        "accuracy": 0.4757281541824341,
        "exact_match": 0.0
      }
    },
    "heldout_task_family_fewshot_4": {
      "multisentence_delimiter": {
        "loss": 2.658726215362549,
        "accuracy": 0.05871212109923363,
        "exact_match": 0.0
      },
      "paraphrase_invariance": {
        "loss": 0.3310430347919464,
        "accuracy": 0.4757281541824341,
        "exact_match": 0.0
      }
    },
    "heldout_task_family_fewshot_8": {
      "multisentence_delimiter": {
        "loss": 2.658726215362549,
        "accuracy": 0.05871212109923363,
        "exact_match": 0.0
      },
      "paraphrase_invariance": {
        "loss": 0.3310430347919464,
        "accuracy": 0.4757281541824341,
        "exact_match": 0.0
      }
    },
    "heldout_operator_composition": {
      "multisentence_delimiter": {
        "loss": 2.658726215362549,
        "accuracy": 0.05871212109923363,
        "exact_match": 0.0
      },
      "paraphrase_invariance": {
        "loss": 0.3310430347919464,
        "accuracy": 0.4757281541824341,
        "exact_match": 0.0
      }
    },
    "heldout_role_binding": {
      "multisentence_delimiter": {
        "loss": 2.658726215362549,
        "accuracy": 0.05871212109923363,
        "exact_match": 0.0
      },
      "paraphrase_invariance": {
        "loss": 0.3310430347919464,
        "accuracy": 0.4757281541824341,
        "exact_match": 0.0
      }
    }
  }
}
```