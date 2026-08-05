# PVR Route Geometry Fine-Grain Audit

Status: `PVR_ROUTE_GEOMETRY_FINEGRAIN_NOT_SUPPORTED`

| metric | value |
|---|---:|
| owner/token-class NMI | 0.04417959406761065 |
| owner/loss-bucket NMI | 0.004674115322522816 |
| owner/syntax-region NMI | 0.025868563412186074 |
| benefit range by token class | 7.969029545831716 |
| margin/benefit correlation | -0.0309619211127246 |
| positive owner-token-class pair rate | 0.8253968253968254 |

```json
{
  "benchmark_evidence_caveat": "Local reduced-file fine-grained diagnostic; token classes are byte-level heuristic labels.",
  "candidate_config": "benchmark/reports/generated/ean_structured_delta_replay_retention_gated_seed_42/pvr_ec_o_ean_retention_gated_delta_replay_v1_300m_config.json",
  "created_at": "2026-06-18T14:13:04.363808+00:00",
  "decision_rule": "Support requires clean Top1 invariants, positive owner mutual information with token class, loss bucket, and syntax region, positive benefit for most owner/token-class pairs, and nontrivial variation in expert benefit by token class.",
  "device": "cuda",
  "experiment": "PVR_ROUTE_GEOMETRY_FINEGRAIN_AUDIT",
  "git_commit": "d18165e32bec94cea3ca836937c81f6a0f3dc5f7",
  "metrics": {
    "benefit_by_token_class": {
      "benefit_range": 7.969029545831716,
      "groups": {
        "brace_bracket_paren": {
          "count": 85,
          "dominant_owner_rate": 0.6,
          "mean_expert_benefit": 4.412798954458798,
          "mean_margin": 0.511128680170605,
          "owner_histogram": {
            "0": 2,
            "2": 14,
            "3": 51,
            "4": 1,
            "5": 10,
            "6": 3,
            "7": 4
          }
        },
        "comma_colon_semicolon": {
          "count": 115,
          "dominant_owner_rate": 0.4434782608695652,
          "mean_expert_benefit": 2.328733027499655,
          "mean_margin": 0.5118624140710937,
          "owner_histogram": {
            "0": 12,
            "1": 3,
            "2": 27,
            "3": 51,
            "4": 2,
            "5": 10,
            "6": 6,
            "7": 4
          }
        },
        "function_signature": {
          "count": 84,
          "dominant_owner_rate": 0.42857142857142855,
          "mean_expert_benefit": 2.6991934875647225,
          "mean_margin": 0.5100628757583243,
          "owner_histogram": {
            "0": 13,
            "1": 2,
            "2": 22,
            "3": 36,
            "4": 1,
            "5": 4,
            "6": 5,
            "7": 1
          }
        },
        "identifier": {
          "count": 903,
          "dominant_owner_rate": 0.5658914728682171,
          "mean_expert_benefit": 1.0253359207250219,
          "mean_margin": 0.5053737104939827,
          "owner_histogram": {
            "0": 82,
            "1": 13,
            "2": 144,
            "3": 511,
            "4": 15,
            "5": 69,
            "6": 44,
            "7": 25
          }
        },
        "indentation": {
          "count": 643,
          "dominant_owner_rate": 0.9066874027993779,
          "mean_expert_benefit": -0.29342777244341134,
          "mean_margin": 0.5210937485861663,
          "owner_histogram": {
            "0": 9,
            "2": 37,
            "3": 583,
            "5": 8,
            "6": 2,
            "7": 4
          }
        },
        "json_key": {
          "count": 153,
          "dominant_owner_rate": 0.5947712418300654,
          "mean_expert_benefit": 1.9876205068008572,
          "mean_margin": 0.5051929519627415,
          "owner_histogram": {
            "0": 6,
            "1": 6,
            "2": 23,
            "3": 91,
            "4": 2,
            "5": 15,
            "6": 6,
            "7": 4
          }
        },
        "json_value": {
          "count": 219,
          "dominant_owner_rate": 0.5981735159817352,
          "mean_expert_benefit": 1.4257047566751095,
          "mean_margin": 0.5093908581480134,
          "owner_histogram": {
            "0": 6,
            "1": 8,
            "2": 40,
            "3": 131,
            "4": 5,
            "5": 17,
            "6": 8,
            "7": 4
          }
        },
        "newline": {
          "count": 122,
          "dominant_owner_rate": 0.4918032786885246,
          "mean_expert_benefit": 3.9700772050232285,
          "mean_margin": 0.5148235701324795,
          "owner_histogram": {
            "0": 5,
            "1": 4,
            "2": 28,
            "3": 60,
            "4": 3,
            "5": 13,
            "6": 5,
            "7": 4
          }
        },
        "number": {
          "count": 79,
          "dominant_owner_rate": 0.6582278481012658,
          "mean_expert_benefit": 3.251296731490123,
          "mean_margin": 0.5069778515025974,
          "owner_histogram": {
            "0": 5,
            "1": 4,
            "2": 9,
            "3": 52,
            "4": 1,
            "5": 5,
            "7": 3
          }
        },
        "operator": {
          "count": 50,
          "dominant_owner_rate": 0.68,
          "mean_expert_benefit": 4.176980504989624,
          "mean_margin": 0.523792386551698,
          "owner_histogram": {
            "0": 2,
            "2": 11,
            "3": 34,
            "5": 2,
            "7": 1
          }
        },
        "other": {
          "count": 93,
          "dominant_owner_rate": 0.45161290322580644,
          "mean_expert_benefit": 4.160546956394839,
          "mean_margin": 0.5119748203397653,
          "owner_histogram": {
            "0": 7,
            "1": 1,
            "2": 20,
            "3": 42,
            "4": 2,
            "5": 12,
            "6": 2,
            "7": 7
          }
        },
        "prose_word": {
          "count": 1175,
          "dominant_owner_rate": 0.5659574468085107,
          "mean_expert_benefit": 1.1394741378962359,
          "mean_margin": 0.5131567364126599,
          "owner_histogram": {
            "0": 125,
            "1": 8,
            "2": 188,
            "3": 665,
            "4": 14,
            "5": 95,
            "6": 42,
            "7": 38
          }
        },
        "quote": {
          "count": 119,
          "dominant_owner_rate": 0.6722689075630253,
          "mean_expert_benefit": 7.455771790833032,
          "mean_margin": 0.5110845220450009,
          "owner_histogram": {
            "0": 11,
            "1": 1,
            "2": 18,
            "3": 80,
            "5": 6,
            "6": 1,
            "7": 2
          }
        },
        "space": {
          "count": 668,
          "dominant_owner_rate": 0.5014970059880239,
          "mean_expert_benefit": -0.5132577549986831,
          "mean_margin": 0.5112149212263085,
          "owner_histogram": {
            "0": 58,
            "1": 19,
            "2": 141,
            "3": 335,
            "4": 13,
            "5": 61,
            "6": 21,
            "7": 20
          }
        },
        "string_literal": {
          "count": 100,
          "dominant_owner_rate": 0.42,
          "mean_expert_benefit": 1.8679603278636931,
          "mean_margin": 0.53109050430047,
          "owner_histogram": {
            "0": 13,
            "1": 3,
            "2": 12,
            "3": 42,
            "4": 2,
            "5": 16,
            "6": 7,
            "7": 5
          }
        }
      },
      "mean_expert_benefit": 1.2218325913220633,
      "route_margin_vs_expert_benefit_correlation": -0.0309619211127246
    },
    "mutual_information": {
      "owner_loss_bucket_mi": 0.007408296557513813,
      "owner_loss_bucket_nmi": 0.004674115322522816,
      "owner_syntax_region_mi": 0.04939668672762663,
      "owner_syntax_region_nmi": 0.025868563412186074,
      "owner_token_class_mi": 0.08436207040718127,
      "owner_token_class_nmi": 0.04417959406761065
    },
    "owner_by_loss_bucket": {
      "high_loss": {
        "count": 1535,
        "dominant_owner_rate": 0.6013029315960912,
        "mean_expert_benefit": 2.592165030873948,
        "mean_margin": 0.507799640369787,
        "owner_histogram": {
          "0": 116,
          "1": 26,
          "2": 262,
          "3": 923,
          "4": 22,
          "5": 106,
          "6": 42,
          "7": 38
        }
      },
      "low_loss": {
        "count": 1537,
        "dominant_owner_rate": 0.6447625243981783,
        "mean_expert_benefit": 0.10208896244000847,
        "mean_margin": 0.518661668561613,
        "owner_histogram": {
          "0": 108,
          "1": 16,
          "2": 236,
          "3": 991,
          "4": 15,
          "5": 87,
          "6": 47,
          "7": 37
        }
      },
      "mid_loss": {
        "count": 1536,
        "dominant_owner_rate": 0.5533854166666666,
        "mean_expert_benefit": 0.9728649239259539,
        "mean_margin": 0.5102921026124637,
        "owner_histogram": {
          "0": 132,
          "1": 30,
          "2": 236,
          "3": 850,
          "4": 24,
          "5": 150,
          "6": 63,
          "7": 51
        }
      }
    },
    "owner_by_syntax_region": {
      "brace_bracket_paren": {
        "count": 85,
        "dominant_owner_rate": 0.6,
        "mean_expert_benefit": 4.412798954458798,
        "mean_margin": 0.511128680170605,
        "owner_histogram": {
          "0": 2,
          "2": 14,
          "3": 51,
          "4": 1,
          "5": 10,
          "6": 3,
          "7": 4
        }
      },
      "broad_lm": {
        "count": 1534,
        "dominant_owner_rate": 0.5352020860495437,
        "mean_expert_benefit": 0.9527622998683023,
        "mean_margin": 0.5120191995012178,
        "owner_histogram": {
          "0": 162,
          "1": 15,
          "2": 267,
          "3": 821,
          "4": 25,
          "5": 130,
          "6": 56,
          "7": 58
        }
      },
      "code_heavy": {
        "count": 491,
        "dominant_owner_rate": 0.5539714867617108,
        "mean_expert_benefit": 1.3517725045988127,
        "mean_margin": 0.5144928699069721,
        "owner_histogram": {
          "0": 36,
          "1": 15,
          "2": 92,
          "3": 272,
          "4": 6,
          "5": 42,
          "6": 14,
          "7": 14
        }
      },
      "function_signature": {
        "count": 84,
        "dominant_owner_rate": 0.42857142857142855,
        "mean_expert_benefit": 2.6991934875647225,
        "mean_margin": 0.5100628757583243,
        "owner_histogram": {
          "0": 13,
          "1": 2,
          "2": 22,
          "3": 36,
          "4": 1,
          "5": 4,
          "6": 5,
          "7": 1
        }
      },
      "identifier": {
        "count": 903,
        "dominant_owner_rate": 0.5658914728682171,
        "mean_expert_benefit": 1.0253359207250219,
        "mean_margin": 0.5053737104939827,
        "owner_histogram": {
          "0": 82,
          "1": 13,
          "2": 144,
          "3": 511,
          "4": 15,
          "5": 69,
          "6": 44,
          "7": 25
        }
      },
      "json_key": {
        "count": 153,
        "dominant_owner_rate": 0.5947712418300654,
        "mean_expert_benefit": 1.9876205068008572,
        "mean_margin": 0.5051929519627415,
        "owner_histogram": {
          "0": 6,
          "1": 6,
          "2": 23,
          "3": 91,
          "4": 2,
          "5": 15,
          "6": 6,
          "7": 4
        }
      },
      "json_schema": {
        "count": 989,
        "dominant_owner_rate": 0.7836198179979778,
        "mean_expert_benefit": 0.9760041205952635,
        "mean_margin": 0.5173075649178555,
        "owner_histogram": {
          "0": 34,
          "1": 10,
          "2": 109,
          "3": 775,
          "4": 4,
          "5": 38,
          "6": 9,
          "7": 10
        }
      },
      "json_value": {
        "count": 219,
        "dominant_owner_rate": 0.5981735159817352,
        "mean_expert_benefit": 1.4257047566751095,
        "mean_margin": 0.5093908581480134,
        "owner_histogram": {
          "0": 6,
          "1": 8,
          "2": 40,
          "3": 131,
          "4": 5,
          "5": 17,
          "6": 8,
          "7": 4
        }
      },
      "operator": {
        "count": 50,
        "dominant_owner_rate": 0.68,
        "mean_expert_benefit": 4.176980504989624,
        "mean_margin": 0.523792386551698,
        "owner_histogram": {
          "0": 2,
          "2": 11,
          "3": 34,
          "5": 2,
          "7": 1
        }
      },
      "string_literal": {
        "count": 100,
        "dominant_owner_rate": 0.42,
        "mean_expert_benefit": 1.8679603278636931,
        "mean_margin": 0.53109050430047,
        "owner_histogram": {
          "0": 13,
          "1": 3,
          "2": 12,
          "3": 42,
          "4": 2,
          "5": 16,
          "6": 7,
          "7": 5
        }
      }
    },
    "owner_by_token_class": {
      "brace_bracket_paren": {
        "count": 85,
        "dominant_owner_rate": 0.6,
        "mean_expert_benefit": 4.412798954458798,
        "mean_margin": 0.511128680170605,
        "owner_histogram": {
          "0": 2,
          "2": 14,
          "3": 51,
          "4": 1,
          "5": 10,
          "6": 3,
          "7": 4
        }
      },
      "comma_colon_semicolon": {
        "count": 115,
        "dominant_owner_rate": 0.4434782608695652,
        "mean_expert_benefit": 2.328733027499655,
        "mean_margin": 0.5118624140710937,
        "owner_histogram": {
          "0": 12,
          "1": 3,
          "2": 27,
          "3": 51,
          "4": 2,
          "5": 10,
          "6": 6,
          "7": 4
        }
      },
      "function_signature": {
        "count": 84,
        "dominant_owner_rate": 0.42857142857142855,
        "mean_expert_benefit": 2.6991934875647225,
        "mean_margin": 0.5100628757583243,
        "owner_histogram": {
          "0": 13,
          "1": 2,
          "2": 22,
          "3": 36,
          "4": 1,
          "5": 4,
          "6": 5,
          "7": 1
        }
      },
      "identifier": {
        "count": 903,
        "dominant_owner_rate": 0.5658914728682171,
        "mean_expert_benefit": 1.0253359207250219,
        "mean_margin": 0.5053737104939827,
        "owner_histogram": {
          "0": 82,
          "1": 13,
          "2": 144,
          "3": 511,
          "4": 15,
          "5": 69,
          "6": 44,
          "7": 25
        }
      },
      "indentation": {
        "count": 643,
        "dominant_owner_rate": 0.9066874027993779,
        "mean_expert_benefit": -0.29342777244341134,
        "mean_margin": 0.5210937485861663,
        "owner_histogram": {
          "0": 9,
          "2": 37,
          "3": 583,
          "5": 8,
          "6": 2,
          "7": 4
        }
      },
      "json_key": {
        "count": 153,
        "dominant_owner_rate": 0.5947712418300654,
        "mean_expert_benefit": 1.9876205068008572,
        "mean_margin": 0.5051929519627415,
        "owner_histogram": {
          "0": 6,
          "1": 6,
          "2": 23,
          "3": 91,
          "4": 2,
          "5": 15,
          "6": 6,
          "7": 4
        }
      },
      "json_value": {
        "count": 219,
        "dominant_owner_rate": 0.5981735159817352,
        "mean_expert_benefit": 1.4257047566751095,
        "mean_margin": 0.5093908581480134,
        "owner_histogram": {
          "0": 6,
          "1": 8,
          "2": 40,
          "3": 131,
          "4": 5,
          "5": 17,
          "6": 8,
          "7": 4
        }
      },
      "newline": {
        "count": 122,
        "dominant_owner_rate": 0.4918032786885246,
        "mean_expert_benefit": 3.9700772050232285,
        "mean_margin": 0.5148235701324795,
        "owner_histogram": {
          "0": 5,
          "1": 4,
          "2": 28,
          "3": 60,
          "4": 3,
          "5": 13,
          "6": 5,
          "7": 4
        }
      },
      "number": {
        "count": 79,
        "dominant_owner_rate": 0.6582278481012658,
        "mean_expert_benefit": 3.251296731490123,
        "mean_margin": 0.5069778515025974,
        "owner_histogram": {
          "0": 5,
          "1": 4,
          "2": 9,
          "3": 52,
          "4": 1,
          "5": 5,
          "7": 3
        }
      },
      "operator": {
        "count": 50,
        "dominant_owner_rate": 0.68,
        "mean_expert_benefit": 4.176980504989624,
        "mean_margin": 0.523792386551698,
        "owner_histogram": {
          "0": 2,
          "2": 11,
          "3": 34,
          "5": 2,
          "7": 1
        }
      },
      "other": {
        "count": 93,
        "dominant_owner_rate": 0.45161290322580644,
        "mean_expert_benefit": 4.160546956394839,
        "mean_margin": 0.5119748203397653,
        "owner_histogram": {
          "0": 7,
          "1": 1,
          "2": 20,
          "3": 42,
          "4": 2,
          "5": 12,
          "6": 2,
          "7": 7
        }
      },
      "prose_word": {
        "count": 1175,
        "dominant_owner_rate": 0.5659574468085107,
        "mean_expert_benefit": 1.1394741378962359,
        "mean_margin": 0.5131567364126599,
        "owner_histogram": {
          "0": 125,
          "1": 8,
          "2": 188,
          "3": 665,
          "4": 14,
          "5": 95,
          "6": 42,
          "7": 38
        }
      },
      "quote": {
        "count": 119,
        "dominant_owner_rate": 0.6722689075630253,
        "mean_expert_benefit": 7.455771790833032,
        "mean_margin": 0.5110845220450009,
        "owner_histogram": {
          "0": 11,
          "1": 1,
          "2": 18,
          "3": 80,
          "5": 6,
          "6": 1,
          "7": 2
        }
      },
      "space": {
        "count": 668,
        "dominant_owner_rate": 0.5014970059880239,
        "mean_expert_benefit": -0.5132577549986831,
        "mean_margin": 0.5112149212263085,
        "owner_histogram": {
          "0": 58,
          "1": 19,
          "2": 141,
          "3": 335,
          "4": 13,
          "5": 61,
          "6": 21,
          "7": 20
        }
      },
      "string_literal": {
        "count": 100,
        "dominant_owner_rate": 0.42,
        "mean_expert_benefit": 1.8679603278636931,
        "mean_margin": 0.53109050430047,
        "owner_histogram": {
          "0": 13,
          "1": 3,
          "2": 12,
          "3": 42,
          "4": 2,
          "5": 16,
          "6": 7,
          "7": 5
        }
      }
    },
    "owner_token_class_pairs": {
      "eligible_pair_count": 63,
      "pairs": {
        "owner_0::comma_colon_semicolon": {
          "count": 12,
          "mean_expert_benefit": 2.13545960187912,
          "mean_margin": 0.5028796875331965
        },
        "owner_0::function_signature": {
          "count": 13,
          "mean_expert_benefit": 3.0299308116619406,
          "mean_margin": 0.5209575069542879
        },
        "owner_0::identifier": {
          "count": 82,
          "mean_expert_benefit": 1.2991229979003347,
          "mean_margin": 0.5091257852926182
        },
        "owner_0::indentation": {
          "count": 9,
          "mean_expert_benefit": -0.21435334285100302,
          "mean_margin": 0.4976943828579452
        },
        "owner_0::prose_word": {
          "count": 125,
          "mean_expert_benefit": 1.1603907225131989,
          "mean_margin": 0.5145376750429471
        },
        "owner_0::quote": {
          "count": 11,
          "mean_expert_benefit": 7.485099792480469,
          "mean_margin": 0.5468122836089495
        },
        "owner_0::space": {
          "count": 58,
          "mean_expert_benefit": -0.4544940611411785,
          "mean_margin": 0.5138834936373022
        },
        "owner_0::string_literal": {
          "count": 13,
          "mean_expert_benefit": 1.1190293018634503,
          "mean_margin": 0.5267345121798989
        },
        "owner_1::identifier": {
          "count": 13,
          "mean_expert_benefit": 0.4621890691610483,
          "mean_margin": 0.5108769347843451
        },
        "owner_1::json_value": {
          "count": 8,
          "mean_expert_benefit": 1.155204400420189,
          "mean_margin": 0.49132434596928454
        },
        "owner_1::prose_word": {
          "count": 8,
          "mean_expert_benefit": 1.163379281759262,
          "mean_margin": 0.45977217478988075
        },
        "owner_1::space": {
          "count": 19,
          "mean_expert_benefit": -0.3431764284246846,
          "mean_margin": 0.5016039585073789
        },
        "owner_2::brace_bracket_paren": {
          "count": 14,
          "mean_expert_benefit": 4.196840524673462,
          "mean_margin": 0.5405001759174324
        },
        "owner_2::comma_colon_semicolon": {
          "count": 27,
          "mean_expert_benefit": 2.5024368498060436,
          "mean_margin": 0.5334693719345479
        },
        "owner_2::function_signature": {
          "count": 22,
          "mean_expert_benefit": 2.150041227990931,
          "mean_margin": 0.5128978867027344
        },
        "owner_2::identifier": {
          "count": 144,
          "mean_expert_benefit": 1.0045741519166365,
          "mean_margin": 0.5133131332684704
        },
        "owner_2::indentation": {
          "count": 37,
          "mean_expert_benefit": -0.3105060393745835,
          "mean_margin": 0.5026743535019523
        },
        "owner_2::json_key": {
          "count": 23,
          "mean_expert_benefit": 2.4835549515226614,
          "mean_margin": 0.5227642128702955
        },
        "owner_2::json_value": {
          "count": 40,
          "mean_expert_benefit": 1.3682402649894356,
          "mean_margin": 0.5186300305339198
        },
        "owner_2::newline": {
          "count": 28,
          "mean_expert_benefit": 4.404530167627123,
          "mean_margin": 0.5287531387460019
        },
        "owner_2::number": {
          "count": 9,
          "mean_expert_benefit": 2.2248000038994684,
          "mean_margin": 0.5224540924170502
        },
        "owner_2::operator": {
          "count": 11,
          "mean_expert_benefit": 4.343501871282404,
          "mean_margin": 0.5364981624438908
        },
        "owner_2::other": {
          "count": 20,
          "mean_expert_benefit": 5.315346737159416,
          "mean_margin": 0.5095332737080753
        },
        "owner_2::prose_word": {
          "count": 188,
          "mean_expert_benefit": 1.1007698074062453,
          "mean_margin": 0.5240998674160968
        },
        "owner_2::quote": {
          "count": 18,
          "mean_expert_benefit": 7.930685255262587,
          "mean_margin": 0.5085186018022122
        },
        "owner_2::space": {
          "count": 141,
          "mean_expert_benefit": -0.4472552646242135,
          "mean_margin": 0.5167459770993067
        },
        "owner_2::string_literal": {
          "count": 12,
          "mean_expert_benefit": 1.7834006150563557,
          "mean_margin": 0.5321205456534194
        },
        "owner_3::brace_bracket_paren": {
          "count": 51,
          "mean_expert_benefit": 4.472913966459386,
          "mean_margin": 0.5043916308558454
        },
        "owner_3::comma_colon_semicolon": {
          "count": 51,
          "mean_expert_benefit": 2.3828029866312064,
          "mean_margin": 0.5011041058726559
        },
        "owner_3::function_signature": {
          "count": 36,
          "mean_expert_benefit": 3.038936949438519,
          "mean_margin": 0.5066049784870336
        },
        "owner_3::identifier": {
          "count": 511,
          "mean_expert_benefit": 1.0347570340985655,
          "mean_margin": 0.5009872262461497
        },
        "owner_3::indentation": {
          "count": 583,
          "mean_expert_benefit": -0.2898214604852539,
          "mean_margin": 0.5226899773167875
        },
        "owner_3::json_key": {
          "count": 91,
          "mean_expert_benefit": 1.9150243355677679,
          "mean_margin": 0.506371276575949
        },
        "owner_3::json_value": {
          "count": 131,
          "mean_expert_benefit": 1.451176333546866,
          "mean_margin": 0.511027889070279
        },
        "owner_3::newline": {
          "count": 60,
          "mean_expert_benefit": 3.621187196389949,
          "mean_margin": 0.5038992350921034
        },
        "owner_3::number": {
          "count": 52,
          "mean_expert_benefit": 3.4283620760991025,
          "mean_margin": 0.5025127679348375
        },
        "owner_3::operator": {
          "count": 34,
          "mean_expert_benefit": 4.167838881997501,
          "mean_margin": 0.5196315453698238
        },
        "owner_3::other": {
          "count": 42,
          "mean_expert_benefit": 4.519990388015729,
          "mean_margin": 0.509561715691927
        },
        "owner_3::prose_word": {
          "count": 665,
          "mean_expert_benefit": 1.0632785841626555,
          "mean_margin": 0.5094714861442537
        },
        "owner_3::quote": {
          "count": 80,
          "mean_expert_benefit": 7.365566062927246,
          "mean_margin": 0.509550441840353
        },
        "owner_3::space": {
          "count": 335,
          "mean_expert_benefit": -0.5722900787368417,
          "mean_margin": 0.5058736633008987
        },
        "owner_3::string_literal": {
          "count": 42,
          "mean_expert_benefit": 2.108715080079578,
          "mean_margin": 0.5297871393462023
        },
        "owner_4::identifier": {
          "count": 15,
          "mean_expert_benefit": 2.576910456021627,
          "mean_margin": 0.48999883805712063
        },
        "owner_4::prose_word": {
          "count": 14,
          "mean_expert_benefit": 1.8354248574801855,
          "mean_margin": 0.4998012029876312
        },
        "owner_4::space": {
          "count": 13,
          "mean_expert_benefit": 0.24806191256413093,
          "mean_margin": 0.5178554990113927
        },
        "owner_5::brace_bracket_paren": {
          "count": 10,
          "mean_expert_benefit": 3.152910614013672,
          "mean_margin": 0.5085069169290364
        },
        "owner_5::comma_colon_semicolon": {
          "count": 10,
          "mean_expert_benefit": 2.4734946727752685,
          "mean_margin": 0.535733799636364
        },
        "owner_5::identifier": {
          "count": 69,
          "mean_expert_benefit": 0.8119883593441783,
          "mean_margin": 0.5093426624771908
        },
        "owner_5::indentation": {
          "count": 8,
          "mean_expert_benefit": -0.0445186928845942,
          "mean_margin": 0.5202377115686735
        },
        "owner_5::json_key": {
          "count": 15,
          "mean_expert_benefit": 2.003961435953776,
          "mean_margin": 0.49861608822312614
        },
        "owner_5::json_value": {
          "count": 17,
          "mean_expert_benefit": 1.5882427823894165,
          "mean_margin": 0.5029303561896087
        },
        "owner_5::newline": {
          "count": 13,
          "mean_expert_benefit": 5.024906259329048,
          "mean_margin": 0.5285815752517338
        },
        "owner_5::other": {
          "count": 12,
          "mean_expert_benefit": 2.571881065656877,
          "mean_margin": 0.5072343547621535
        },
        "owner_5::prose_word": {
          "count": 95,
          "mean_expert_benefit": 1.4813061769071378,
          "mean_margin": 0.5186242127235521
        },
        "owner_5::space": {
          "count": 61,
          "mean_expert_benefit": -0.4415355413907864,
          "mean_margin": 0.5187426790839336
        },
        "owner_5::string_literal": {
          "count": 16,
          "mean_expert_benefit": 2.0867529958486557,
          "mean_margin": 0.536400168008792
        },
        "owner_6::identifier": {
          "count": 44,
          "mean_expert_benefit": 0.3706070577556437,
          "mean_margin": 0.5227321430857322
        },
        "owner_6::json_value": {
          "count": 8,
          "mean_expert_benefit": 0.8402074426412582,
          "mean_margin": 0.4953845070364575
        },
        "owner_6::prose_word": {
          "count": 42,
          "mean_expert_benefit": 1.278141322590056,
          "mean_margin": 0.5142246829493649
        },
        "owner_6::space": {
          "count": 21,
          "mean_expert_benefit": -0.9718122198468163,
          "mean_margin": 0.5328167409059547
        },
        "owner_7::identifier": {
          "count": 25,
          "mean_expert_benefit": 1.1573882484436036,
          "mean_margin": 0.5018536659951012
        },
        "owner_7::prose_word": {
          "count": 38,
          "mean_expert_benefit": 1.3262969694639508,
          "mean_margin": 0.5202766160946338
        },
        "owner_7::space": {
          "count": 20,
          "mean_expert_benefit": -0.5539042092859745,
          "mean_margin": 0.513120654473702
        }
      },
      "positive_pair_count": 52,
      "positive_pair_rate": 0.8253968253968254
    },
    "routing_snapshots": [
      {
        "challenger_disagreement_rate": null,
        "descriptor_control_margin": 0.5183323635040628,
        "expert_utilization": [
          349,
          270,
          485,
          620,
          241,
          404,
          345,
          358
        ],
        "failure_mode_distribution": {},
        "high_gap_monopoly_rate": 0.20182291666666666,
        "operator_control_margin": 0.5183323635040628,
        "owner_churn": null,
        "owner_entropy": 2.037768461799472,
        "owners_per_token": 1.0,
        "production_map_mutated": false,
        "prototype_entropy": 2.037768461799472,
        "prototype_margin": 0.5183323635040628,
        "prototype_monopoly_rate": 0.20182291666666666,
        "runtime_dynamic_k_count": 0,
        "runtime_expert_choice_count": 0,
        "stale_owner_rate": null,
        "step": 0,
        "top2_execution_count": 0,
        "top4_execution_count": 0
      },
      {
        "challenger_disagreement_rate": null,
        "descriptor_control_margin": 0.5130888865387533,
        "expert_utilization": [
          302,
          329,
          512,
          701,
          223,
          409,
          272,
          324
        ],
        "failure_mode_distribution": {},
        "high_gap_monopoly_rate": 0.22819010416666666,
        "operator_control_margin": 0.5130888865387533,
        "owner_churn": null,
        "owner_entropy": 2.013830819174193,
        "owners_per_token": 1.0,
        "production_map_mutated": false,
        "prototype_entropy": 2.013830819174193,
        "prototype_margin": 0.5130888865387533,
        "prototype_monopoly_rate": 0.22819010416666666,
        "runtime_dynamic_k_count": 0,
        "runtime_expert_choice_count": 0,
        "stale_owner_rate": null,
        "step": 25,
        "top2_execution_count": 0,
        "top4_execution_count": 0
      },
      {
        "challenger_disagreement_rate": null,
        "descriptor_control_margin": 0.5152230673314383,
        "expert_utilization": [
          288,
          296,
          501,
          728,
          238,
          427,
          277,
          317
        ],
        "failure_mode_distribution": {},
        "high_gap_monopoly_rate": 0.23697916666666666,
        "operator_control_margin": 0.5152230673314383,
        "owner_churn": null,
        "owner_entropy": 2.0080757147085775,
        "owners_per_token": 1.0,
        "production_map_mutated": false,
        "prototype_entropy": 2.0080757147085775,
        "prototype_margin": 0.5152230673314383,
        "prototype_monopoly_rate": 0.23697916666666666,
        "runtime_dynamic_k_count": 0,
        "runtime_expert_choice_count": 0,
        "stale_owner_rate": null,
        "step": 50,
        "top2_execution_count": 0,
        "top4_execution_count": 0
      },
      {
        "challenger_disagreement_rate": null,
        "descriptor_control_margin": 0.5068799492582912,
        "expert_utilization": [
          372,
          274,
          519,
          631,
          242,
          375,
          321,
          338
        ],
        "failure_mode_distribution": {},
        "high_gap_monopoly_rate": 0.20540364583333334,
        "operator_control_margin": 0.5068799492582912,
        "owner_churn": null,
        "owner_entropy": 2.0325072608582655,
        "owners_per_token": 1.0,
        "production_map_mutated": false,
        "prototype_entropy": 2.0325072608582655,
        "prototype_margin": 0.5068799492582912,
        "prototype_monopoly_rate": 0.20540364583333334,
        "runtime_dynamic_k_count": 0,
        "runtime_expert_choice_count": 0,
        "stale_owner_rate": null,
        "step": 75,
        "top2_execution_count": 0,
        "top4_execution_count": 0
      }
    ],
    "token_count": 4608,
    "top1_invariants_clean": true
  },
  "schema_version": "1.0",
  "seq_len": 128,
  "spans_per_family": 12,
  "status": "PVR_ROUTE_GEOMETRY_FINEGRAIN_NOT_SUPPORTED",
  "supported_conditions": {
    "most_owner_token_pairs_have_positive_benefit": true,
    "owner_loss_bucket_nmi_positive": false,
    "owner_syntax_region_nmi_positive": true,
    "owner_token_class_nmi_positive": true,
    "token_class_benefit_varies": true,
    "top1_invariants_clean": true
  }
}
```
