# Expert Function Probe Audit

Status: `PVR_EXPERT_FUNCTION_PROBE_SUPPORTED`

| expert | activations | total benefit | structured benefit | prose benefit | top benefit classes |
|---|---:|---:|---:|---:|---|
| 0 | 16194 | 869.6990103281832 | 656.915130804759 | 171.0721426015759 | prose_word, identifier, quote, other, brace_bracket_paren |
| 1 | 13880 | 743.7477014779975 | 594.4802589720722 | 117.94023537352372 | prose_word, quote, identifier, newline, other |
| 2 | 24373 | 1309.202312840351 | 1027.8614858082503 | 223.19736113202464 | prose_word, quote, identifier, other, newline |
| 3 | 31521 | 1633.6947996090119 | 1292.6877477699402 | 269.89090842583454 | prose_word, quote, identifier, newline, other |
| 4 | 11609 | 666.9308264774496 | 515.3922927192868 | 123.17078125202667 | prose_word, quote, identifier, newline, other |
| 5 | 19432 | 1051.952560880993 | 831.4221370424815 | 167.4832967167421 | prose_word, quote, identifier, newline, other |
| 6 | 14796 | 785.1767857180005 | 612.6271134429616 | 134.89457851179202 | prose_word, quote, identifier, other, newline |
| 7 | 15651 | 863.7774698050682 | 670.9415690854551 | 153.2604973380684 | prose_word, quote, identifier, newline, other |

```json
{
  "attribution_caveat": "Token loss benefit is assigned across the selected Top1 experts along the layer path; this is post-hoc diagnostic attribution, not causal proof.",
  "benchmark_evidence_caveat": "Local reduced-file expert function probe.",
  "candidate_config": "benchmark/reports/generated/ean_structured_delta_replay_retention_gated_seed_42/pvr_ec_o_ean_retention_gated_delta_replay_v1_300m_config.json",
  "created_at": "2026-06-18T15:38:37.319990+00:00",
  "decision_rule": "Support requires clean Top1 invariants, all global experts activated, most global experts positive, at least two structured-role experts, positive aggregate assigned benefit, and generated examples.",
  "device": "cuda",
  "experiment": "PVR_EXPERT_FUNCTION_PROBE_AUDIT",
  "git_commit": "d18165e32bec94cea3ca836937c81f6a0f3dc5f7",
  "metrics": {
    "expected_global_experts": 8,
    "global_expert_cards": {
      "0": {
        "activation_count": 16194,
        "mean_assigned_benefit": 0.05370501484056955,
        "mean_delta_norm": 13.062255749720709,
        "mean_harm": -0.025727233276851284,
        "mean_positive_benefit": 0.09614162754868279,
        "mean_route_margin": 0.35207945049960176,
        "positive_benefit_rate": 0.6517846115845375,
        "prose_benefit": 171.0721426015759,
        "structured_benefit": 656.915130804759,
        "structured_prose_benefit_ratio": 3.8399889123660715,
        "token_class_benefit": {
          "brace_bracket_paren": 56.99294299725447,
          "comma_colon_semicolon": 45.22313547134404,
          "function_signature": 37.96993391960856,
          "identifier": 157.02121589798497,
          "indentation": -25.790789482804655,
          "json_key": 38.60124921550355,
          "json_value": 28.427181593608065,
          "newline": 53.08792705895738,
          "number": 25.67837285995483,
          "operator": 20.026878178119645,
          "other": 71.79091068980362,
          "prose_word": 223.5679409288185,
          "quote": 154.43051640192652,
          "space": -56.784182612396044,
          "string_literal": 39.455777210493856
        },
        "token_class_counts": {
          "brace_bracket_paren": 314,
          "comma_colon_semicolon": 466,
          "function_signature": 326,
          "identifier": 3023,
          "indentation": 2067,
          "json_key": 524,
          "json_value": 559,
          "newline": 288,
          "number": 193,
          "operator": 110,
          "other": 337,
          "prose_word": 4484,
          "quote": 497,
          "space": 2478,
          "string_literal": 528
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.17974231019616127,
            "delta_norm": 18.066368103027344,
            "family": "broad_lm",
            "route_margin": 0.24349337816238403,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -4.3138154447078705
          },
          {
            "assigned_benefit": -0.17974231019616127,
            "delta_norm": 14.914375305175781,
            "family": "broad_lm",
            "route_margin": 0.011456012725830078,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -4.3138154447078705
          },
          {
            "assigned_benefit": -0.14390301704406738,
            "delta_norm": 10.399097442626953,
            "family": "json_schema",
            "route_margin": 0.31355637311935425,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -3.453672409057617
          },
          {
            "assigned_benefit": -0.14390301704406738,
            "delta_norm": 9.670820236206055,
            "family": "json_schema",
            "route_margin": 0.5853359699249268,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -3.453672409057617
          },
          {
            "assigned_benefit": -0.14390301704406738,
            "delta_norm": 18.26600456237793,
            "family": "json_schema",
            "route_margin": 0.4235943555831909,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -3.453672409057617
          },
          {
            "assigned_benefit": -0.14381763339042664,
            "delta_norm": 8.90266227722168,
            "family": "broad_lm",
            "route_margin": 0.24095964431762695,
            "token": "c",
            "token_class": "prose_word",
            "token_total_benefit": -3.4516232013702393
          },
          {
            "assigned_benefit": -0.14381763339042664,
            "delta_norm": 18.070985794067383,
            "family": "broad_lm",
            "route_margin": 0.18828749656677246,
            "token": "c",
            "token_class": "prose_word",
            "token_total_benefit": -3.4516232013702393
          },
          {
            "assigned_benefit": -0.14381763339042664,
            "delta_norm": 14.921710968017578,
            "family": "broad_lm",
            "route_margin": 0.016796231269836426,
            "token": "c",
            "token_class": "prose_word",
            "token_total_benefit": -3.4516232013702393
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.4434954325358073,
            "delta_norm": 18.0870304107666,
            "family": "json_schema",
            "route_margin": 0.35745885968208313,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.643890380859375
          },
          {
            "assigned_benefit": 0.4434954325358073,
            "delta_norm": 14.868946075439453,
            "family": "json_schema",
            "route_margin": 0.012494087219238281,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.643890380859375
          },
          {
            "assigned_benefit": 0.4348748524983724,
            "delta_norm": 7.8735575675964355,
            "family": "json_schema",
            "route_margin": 0.14937710762023926,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.436996459960938
          },
          {
            "assigned_benefit": 0.4348748524983724,
            "delta_norm": 18.03725814819336,
            "family": "json_schema",
            "route_margin": 0.5126282572746277,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.436996459960938
          },
          {
            "assigned_benefit": 0.42559146881103516,
            "delta_norm": 17.872426986694336,
            "family": "json_schema",
            "route_margin": 0.25519827008247375,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.214195251464844
          },
          {
            "assigned_benefit": 0.42559146881103516,
            "delta_norm": 14.822091102600098,
            "family": "json_schema",
            "route_margin": 0.017566800117492676,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.214195251464844
          },
          {
            "assigned_benefit": 0.4194428126017253,
            "delta_norm": 7.303606033325195,
            "family": "json_schema",
            "route_margin": 0.04512906074523926,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.066627502441406
          },
          {
            "assigned_benefit": 0.4194428126017253,
            "delta_norm": 10.371100425720215,
            "family": "json_schema",
            "route_margin": 0.6119989156723022,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.066627502441406
          }
        ],
        "total_assigned_benefit": 869.6990103281832
      },
      "1": {
        "activation_count": 13880,
        "mean_assigned_benefit": 0.05358412834855889,
        "mean_delta_norm": 10.796895326935935,
        "mean_harm": -0.024083466979706526,
        "mean_positive_benefit": 0.09757619030009541,
        "mean_route_margin": 0.35888647763595327,
        "positive_benefit_rate": 0.638400576368876,
        "prose_benefit": 117.94023537352372,
        "structured_benefit": 594.4802589720722,
        "structured_prose_benefit_ratio": 5.040521218982801,
        "token_class_benefit": {
          "brace_bracket_paren": 54.84331373187406,
          "comma_colon_semicolon": 31.807471518715218,
          "function_signature": 30.15799604356287,
          "identifier": 123.64388394479928,
          "indentation": -25.671516255941253,
          "json_key": 42.566917161146804,
          "json_value": 27.818417216806335,
          "newline": 59.9441161163442,
          "number": 21.092705031236008,
          "operator": 17.143415490786214,
          "other": 56.11398442551405,
          "prose_word": 163.359797292544,
          "quote": 151.25674009323103,
          "space": -44.53482295619314,
          "string_literal": 34.20528262356919
        },
        "token_class_counts": {
          "brace_bracket_paren": 295,
          "comma_colon_semicolon": 335,
          "function_signature": 261,
          "identifier": 2460,
          "indentation": 2249,
          "json_key": 552,
          "json_value": 520,
          "newline": 316,
          "number": 150,
          "operator": 97,
          "other": 255,
          "prose_word": 3425,
          "quote": 488,
          "space": 2070,
          "string_literal": 407
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.17974231019616127,
            "delta_norm": 7.330848217010498,
            "family": "broad_lm",
            "route_margin": 0.29956305027008057,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -4.3138154447078705
          },
          {
            "assigned_benefit": -0.17974231019616127,
            "delta_norm": 14.366406440734863,
            "family": "broad_lm",
            "route_margin": 0.291988730430603,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -4.3138154447078705
          },
          {
            "assigned_benefit": -0.14390301704406738,
            "delta_norm": 14.313057899475098,
            "family": "json_schema",
            "route_margin": 0.38561248779296875,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -3.453672409057617
          },
          {
            "assigned_benefit": -0.14381763339042664,
            "delta_norm": 9.876863479614258,
            "family": "broad_lm",
            "route_margin": 0.11163318157196045,
            "token": "c",
            "token_class": "prose_word",
            "token_total_benefit": -3.4516232013702393
          },
          {
            "assigned_benefit": -0.14381763339042664,
            "delta_norm": 14.407355308532715,
            "family": "broad_lm",
            "route_margin": 0.26674365997314453,
            "token": "c",
            "token_class": "prose_word",
            "token_total_benefit": -3.4516232013702393
          },
          {
            "assigned_benefit": -0.13103054463863373,
            "delta_norm": 8.06817626953125,
            "family": "code_heavy",
            "route_margin": 0.7398184537887573,
            "token": "g",
            "token_class": "identifier",
            "token_total_benefit": -3.1447330713272095
          },
          {
            "assigned_benefit": -0.13103054463863373,
            "delta_norm": 14.3151216506958,
            "family": "code_heavy",
            "route_margin": 0.26368892192840576,
            "token": "g",
            "token_class": "identifier",
            "token_total_benefit": -3.1447330713272095
          },
          {
            "assigned_benefit": -0.12831215063730875,
            "delta_norm": 7.100924015045166,
            "family": "json_schema",
            "route_margin": 0.6002681255340576,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -3.07949161529541
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.4434954325358073,
            "delta_norm": 14.353534698486328,
            "family": "json_schema",
            "route_margin": 0.35987240076065063,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.643890380859375
          },
          {
            "assigned_benefit": 0.4348748524983724,
            "delta_norm": 7.676216125488281,
            "family": "json_schema",
            "route_margin": 0.28156864643096924,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.436996459960938
          },
          {
            "assigned_benefit": 0.4348748524983724,
            "delta_norm": 7.812159538269043,
            "family": "json_schema",
            "route_margin": 0.044027864933013916,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.436996459960938
          },
          {
            "assigned_benefit": 0.4348748524983724,
            "delta_norm": 14.38868522644043,
            "family": "json_schema",
            "route_margin": 0.3348906636238098,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.436996459960938
          },
          {
            "assigned_benefit": 0.42559146881103516,
            "delta_norm": 9.553960800170898,
            "family": "json_schema",
            "route_margin": 0.10610616207122803,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.214195251464844
          },
          {
            "assigned_benefit": 0.42559146881103516,
            "delta_norm": 14.35044002532959,
            "family": "json_schema",
            "route_margin": 0.27917373180389404,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.214195251464844
          },
          {
            "assigned_benefit": 0.4194428126017253,
            "delta_norm": 14.386540412902832,
            "family": "json_schema",
            "route_margin": 0.38532501459121704,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.066627502441406
          },
          {
            "assigned_benefit": 0.4192720651626587,
            "delta_norm": 9.062240600585938,
            "family": "code_heavy",
            "route_margin": 0.6131228804588318,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 10.062529563903809
          }
        ],
        "total_assigned_benefit": 743.7477014779975
      },
      "2": {
        "activation_count": 24373,
        "mean_assigned_benefit": 0.05371527152342145,
        "mean_delta_norm": 12.818348594641737,
        "mean_harm": -0.02524569046794252,
        "mean_positive_benefit": 0.09761663886144385,
        "mean_route_margin": 0.5045499488870622,
        "positive_benefit_rate": 0.6426783736101424,
        "prose_benefit": 223.19736113202464,
        "structured_benefit": 1027.8614858082503,
        "structured_prose_benefit_ratio": 4.605168630108734,
        "token_class_benefit": {
          "brace_bracket_paren": 88.797799543788,
          "comma_colon_semicolon": 68.02810121575983,
          "function_signature": 54.78257326036702,
          "identifier": 220.2482383629936,
          "indentation": -43.05156335715834,
          "json_key": 66.43380669504408,
          "json_value": 46.37499596768392,
          "newline": 104.58986664447768,
          "number": 38.72510836521784,
          "operator": 29.907237370808943,
          "other": 108.78297688924776,
          "prose_word": 296.87189562091004,
          "quote": 246.68985684712786,
          "space": -81.26248212088902,
          "string_literal": 63.28390153497452
        },
        "token_class_counts": {
          "brace_bracket_paren": 489,
          "comma_colon_semicolon": 706,
          "function_signature": 461,
          "identifier": 4362,
          "indentation": 3413,
          "json_key": 818,
          "json_value": 858,
          "newline": 570,
          "number": 290,
          "operator": 166,
          "other": 489,
          "prose_word": 6379,
          "quote": 790,
          "space": 3819,
          "string_literal": 763
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.17974231019616127,
            "delta_norm": 10.339085578918457,
            "family": "broad_lm",
            "route_margin": 0.3652651607990265,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -4.3138154447078705
          },
          {
            "assigned_benefit": -0.17974231019616127,
            "delta_norm": 11.604266166687012,
            "family": "broad_lm",
            "route_margin": 0.3444712162017822,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -4.3138154447078705
          },
          {
            "assigned_benefit": -0.17974231019616127,
            "delta_norm": 13.657981872558594,
            "family": "broad_lm",
            "route_margin": 0.4467126429080963,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -4.3138154447078705
          },
          {
            "assigned_benefit": -0.17974231019616127,
            "delta_norm": 8.987576484680176,
            "family": "broad_lm",
            "route_margin": 0.18856492638587952,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -4.3138154447078705
          },
          {
            "assigned_benefit": -0.17974231019616127,
            "delta_norm": 19.876901626586914,
            "family": "broad_lm",
            "route_margin": 1.0158721208572388,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -4.3138154447078705
          },
          {
            "assigned_benefit": -0.14390301704406738,
            "delta_norm": 9.999387741088867,
            "family": "json_schema",
            "route_margin": 0.9460335969924927,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -3.453672409057617
          },
          {
            "assigned_benefit": -0.14390301704406738,
            "delta_norm": 13.516756057739258,
            "family": "json_schema",
            "route_margin": 0.3731444478034973,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -3.453672409057617
          },
          {
            "assigned_benefit": -0.14390301704406738,
            "delta_norm": 8.984742164611816,
            "family": "json_schema",
            "route_margin": 0.14763560891151428,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -3.453672409057617
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.4434954325358073,
            "delta_norm": 12.206803321838379,
            "family": "json_schema",
            "route_margin": 0.679313600063324,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.643890380859375
          },
          {
            "assigned_benefit": 0.4434954325358073,
            "delta_norm": 10.230634689331055,
            "family": "json_schema",
            "route_margin": 0.6278300285339355,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.643890380859375
          },
          {
            "assigned_benefit": 0.4434954325358073,
            "delta_norm": 13.295406341552734,
            "family": "json_schema",
            "route_margin": 0.3220507502555847,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.643890380859375
          },
          {
            "assigned_benefit": 0.4434954325358073,
            "delta_norm": 8.837514877319336,
            "family": "json_schema",
            "route_margin": 0.1730024814605713,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.643890380859375
          },
          {
            "assigned_benefit": 0.4434954325358073,
            "delta_norm": 19.83881378173828,
            "family": "json_schema",
            "route_margin": 1.0311675071716309,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.643890380859375
          },
          {
            "assigned_benefit": 0.4348748524983724,
            "delta_norm": 9.999593734741211,
            "family": "json_schema",
            "route_margin": 0.007012426853179932,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.436996459960938
          },
          {
            "assigned_benefit": 0.4348748524983724,
            "delta_norm": 13.56424331665039,
            "family": "json_schema",
            "route_margin": 0.5517843961715698,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.436996459960938
          },
          {
            "assigned_benefit": 0.4348748524983724,
            "delta_norm": 8.800647735595703,
            "family": "json_schema",
            "route_margin": 0.257057785987854,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.436996459960938
          }
        ],
        "total_assigned_benefit": 1309.202312840351
      },
      "3": {
        "activation_count": 31521,
        "mean_assigned_benefit": 0.05182877445541106,
        "mean_delta_norm": 15.33122305269339,
        "mean_harm": -0.02401665415159867,
        "mean_positive_benefit": 0.09714921453835904,
        "mean_route_margin": 0.532087572774383,
        "positive_benefit_rate": 0.6259636432854288,
        "prose_benefit": 269.89090842583454,
        "structured_benefit": 1292.6877477699402,
        "structured_prose_benefit_ratio": 4.789667630190545,
        "token_class_benefit": {
          "brace_bracket_paren": 115.53666921084107,
          "comma_colon_semicolon": 79.41538390517233,
          "function_signature": 60.91461429744971,
          "identifier": 269.79287517815885,
          "indentation": -62.81851902945587,
          "json_key": 83.99254030982645,
          "json_value": 58.09949615101032,
          "newline": 129.19768036618694,
          "number": 50.37864041328433,
          "operator": 44.40598078568775,
          "other": 126.38592330851682,
          "prose_word": 377.9505207139716,
          "quote": 326.80464029312145,
          "space": -100.51087315396147,
          "string_literal": 74.14922685921186
        },
        "token_class_counts": {
          "brace_bracket_paren": 633,
          "comma_colon_semicolon": 848,
          "function_signature": 547,
          "identifier": 5449,
          "indentation": 5312,
          "json_key": 1101,
          "json_value": 1108,
          "newline": 690,
          "number": 362,
          "operator": 241,
          "other": 579,
          "prose_word": 8081,
          "quote": 1053,
          "space": 4586,
          "string_literal": 931
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.17974231019616127,
            "delta_norm": 8.273972511291504,
            "family": "broad_lm",
            "route_margin": 0.8679388761520386,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -4.3138154447078705
          },
          {
            "assigned_benefit": -0.17974231019616127,
            "delta_norm": 16.316221237182617,
            "family": "broad_lm",
            "route_margin": 0.7289800047874451,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -4.3138154447078705
          },
          {
            "assigned_benefit": -0.17974231019616127,
            "delta_norm": 22.630359649658203,
            "family": "broad_lm",
            "route_margin": 0.7522459030151367,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -4.3138154447078705
          },
          {
            "assigned_benefit": -0.17974231019616127,
            "delta_norm": 21.80191421508789,
            "family": "broad_lm",
            "route_margin": 0.6114027500152588,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -4.3138154447078705
          },
          {
            "assigned_benefit": -0.14390301704406738,
            "delta_norm": 16.190580368041992,
            "family": "json_schema",
            "route_margin": 0.7100922465324402,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -3.453672409057617
          },
          {
            "assigned_benefit": -0.14390301704406738,
            "delta_norm": 9.240883827209473,
            "family": "json_schema",
            "route_margin": 0.009511888027191162,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -3.453672409057617
          },
          {
            "assigned_benefit": -0.14390301704406738,
            "delta_norm": 22.549673080444336,
            "family": "json_schema",
            "route_margin": 0.7526525855064392,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -3.453672409057617
          },
          {
            "assigned_benefit": -0.14390301704406738,
            "delta_norm": 21.67888069152832,
            "family": "json_schema",
            "route_margin": 0.6771349906921387,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -3.453672409057617
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.4434954325358073,
            "delta_norm": 7.8891282081604,
            "family": "json_schema",
            "route_margin": 0.05824553966522217,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.643890380859375
          },
          {
            "assigned_benefit": 0.4434954325358073,
            "delta_norm": 7.6958909034729,
            "family": "json_schema",
            "route_margin": 0.7211551666259766,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.643890380859375
          },
          {
            "assigned_benefit": 0.4434954325358073,
            "delta_norm": 16.24778175354004,
            "family": "json_schema",
            "route_margin": 0.7649969458580017,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.643890380859375
          },
          {
            "assigned_benefit": 0.4434954325358073,
            "delta_norm": 22.538679122924805,
            "family": "json_schema",
            "route_margin": 0.6821215748786926,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.643890380859375
          },
          {
            "assigned_benefit": 0.4434954325358073,
            "delta_norm": 21.72295379638672,
            "family": "json_schema",
            "route_margin": 0.619948148727417,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.643890380859375
          },
          {
            "assigned_benefit": 0.4348748524983724,
            "delta_norm": 8.018074989318848,
            "family": "json_schema",
            "route_margin": 0.7703670859336853,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.436996459960938
          },
          {
            "assigned_benefit": 0.4348748524983724,
            "delta_norm": 7.337386131286621,
            "family": "json_schema",
            "route_margin": 0.10327064990997314,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.436996459960938
          },
          {
            "assigned_benefit": 0.4348748524983724,
            "delta_norm": 16.22728729248047,
            "family": "json_schema",
            "route_margin": 0.706093430519104,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.436996459960938
          }
        ],
        "total_assigned_benefit": 1633.6947996090119
      },
      "4": {
        "activation_count": 11609,
        "mean_assigned_benefit": 0.0574494639053708,
        "mean_delta_norm": 16.168970971917066,
        "mean_harm": -0.025520594585333744,
        "mean_positive_benefit": 0.10047017180035508,
        "mean_route_margin": 0.7820981349348406,
        "positive_benefit_rate": 0.6585407873201826,
        "prose_benefit": 123.17078125202667,
        "structured_benefit": 515.3922927192868,
        "structured_prose_benefit_ratio": 4.1843713864631065,
        "token_class_benefit": {
          "brace_bracket_paren": 43.88149103584392,
          "comma_colon_semicolon": 36.38375216225784,
          "function_signature": 26.495302634934564,
          "identifier": 111.11233570612933,
          "indentation": -18.76540925990174,
          "json_key": 38.270249019066505,
          "json_value": 21.3807941228151,
          "newline": 54.60028381268633,
          "number": 17.208223720391597,
          "operator": 14.538320938746132,
          "other": 52.81486257742049,
          "prose_word": 154.14674661432687,
          "quote": 114.22850751876823,
          "space": -36.65766617368581,
          "string_literal": 37.29303204764924
        },
        "token_class_counts": {
          "brace_bracket_paren": 226,
          "comma_colon_semicolon": 370,
          "function_signature": 222,
          "identifier": 2089,
          "indentation": 1469,
          "json_key": 454,
          "json_value": 405,
          "newline": 292,
          "number": 136,
          "operator": 83,
          "other": 240,
          "prose_word": 3046,
          "quote": 362,
          "space": 1801,
          "string_literal": 414
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.17974231019616127,
            "delta_norm": 8.011032104492188,
            "family": "broad_lm",
            "route_margin": 0.08765071630477905,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -4.3138154447078705
          },
          {
            "assigned_benefit": -0.17974231019616127,
            "delta_norm": 10.291979789733887,
            "family": "broad_lm",
            "route_margin": 0.1490834355354309,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -4.3138154447078705
          },
          {
            "assigned_benefit": -0.17974231019616127,
            "delta_norm": 22.74820899963379,
            "family": "broad_lm",
            "route_margin": 1.1534578800201416,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -4.3138154447078705
          },
          {
            "assigned_benefit": -0.14390301704406738,
            "delta_norm": 8.753653526306152,
            "family": "json_schema",
            "route_margin": 0.4778738021850586,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -3.453672409057617
          },
          {
            "assigned_benefit": -0.14390301704406738,
            "delta_norm": 22.87668800354004,
            "family": "json_schema",
            "route_margin": 1.0910704135894775,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -3.453672409057617
          },
          {
            "assigned_benefit": -0.14381763339042664,
            "delta_norm": 22.855714797973633,
            "family": "broad_lm",
            "route_margin": 1.1457725763320923,
            "token": "c",
            "token_class": "prose_word",
            "token_total_benefit": -3.4516232013702393
          },
          {
            "assigned_benefit": -0.13103054463863373,
            "delta_norm": 22.9853572845459,
            "family": "code_heavy",
            "route_margin": 1.067575216293335,
            "token": "g",
            "token_class": "identifier",
            "token_total_benefit": -3.1447330713272095
          },
          {
            "assigned_benefit": -0.12831215063730875,
            "delta_norm": 7.472707748413086,
            "family": "json_schema",
            "route_margin": 0.4091215133666992,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -3.07949161529541
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.4434954325358073,
            "delta_norm": 7.402981281280518,
            "family": "json_schema",
            "route_margin": 0.5643401145935059,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.643890380859375
          },
          {
            "assigned_benefit": 0.4434954325358073,
            "delta_norm": 8.556255340576172,
            "family": "json_schema",
            "route_margin": 0.33876097202301025,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.643890380859375
          },
          {
            "assigned_benefit": 0.4434954325358073,
            "delta_norm": 22.751602172851562,
            "family": "json_schema",
            "route_margin": 1.0363757610321045,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.643890380859375
          },
          {
            "assigned_benefit": 0.4348748524983724,
            "delta_norm": 10.959671974182129,
            "family": "json_schema",
            "route_margin": 0.1521834135055542,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.436996459960938
          },
          {
            "assigned_benefit": 0.4348748524983724,
            "delta_norm": 9.019441604614258,
            "family": "json_schema",
            "route_margin": 1.2289636135101318,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.436996459960938
          },
          {
            "assigned_benefit": 0.4348748524983724,
            "delta_norm": 22.683759689331055,
            "family": "json_schema",
            "route_margin": 1.157224178314209,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.436996459960938
          },
          {
            "assigned_benefit": 0.42559146881103516,
            "delta_norm": 8.307329177856445,
            "family": "json_schema",
            "route_margin": 0.00852745771408081,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.214195251464844
          },
          {
            "assigned_benefit": 0.42559146881103516,
            "delta_norm": 8.205501556396484,
            "family": "json_schema",
            "route_margin": 0.01650300621986389,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.214195251464844
          }
        ],
        "total_assigned_benefit": 666.9308264774496
      },
      "5": {
        "activation_count": 19432,
        "mean_assigned_benefit": 0.05413506385760564,
        "mean_delta_norm": 14.184252050419607,
        "mean_harm": -0.0235137974348626,
        "mean_positive_benefit": 0.0994587105223705,
        "mean_route_margin": 0.6196155940913302,
        "positive_benefit_rate": 0.6314326883491148,
        "prose_benefit": 167.4832967167421,
        "structured_benefit": 831.4221370424815,
        "structured_prose_benefit_ratio": 4.964209287381254,
        "token_class_benefit": {
          "brace_bracket_paren": 70.56145406079781,
          "comma_colon_semicolon": 50.758771215876,
          "function_signature": 41.80289016415678,
          "identifier": 166.03280864252437,
          "indentation": -35.60854034063707,
          "json_key": 57.125856354832685,
          "json_value": 33.73679759912199,
          "newline": 89.07491169463458,
          "number": 31.859657367070504,
          "operator": 27.46344043811164,
          "other": 87.11160759549415,
          "prose_word": 228.12142890815917,
          "quote": 213.69783115387,
          "space": -59.09407232449547,
          "string_literal": 49.30771835148336
        },
        "token_class_counts": {
          "brace_bracket_paren": 396,
          "comma_colon_semicolon": 551,
          "function_signature": 367,
          "identifier": 3363,
          "indentation": 3232,
          "json_key": 715,
          "json_value": 650,
          "newline": 457,
          "number": 235,
          "operator": 154,
          "other": 391,
          "prose_word": 4804,
          "quote": 690,
          "space": 2800,
          "string_literal": 627
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.17974231019616127,
            "delta_norm": 8.427087783813477,
            "family": "broad_lm",
            "route_margin": 0.5227410793304443,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -4.3138154447078705
          },
          {
            "assigned_benefit": -0.17974231019616127,
            "delta_norm": 14.634742736816406,
            "family": "broad_lm",
            "route_margin": 0.5854675769805908,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -4.3138154447078705
          },
          {
            "assigned_benefit": -0.17974231019616127,
            "delta_norm": 22.151559829711914,
            "family": "broad_lm",
            "route_margin": 0.76362544298172,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -4.3138154447078705
          },
          {
            "assigned_benefit": -0.14390301704406738,
            "delta_norm": 8.34851360321045,
            "family": "json_schema",
            "route_margin": 0.5195884704589844,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -3.453672409057617
          },
          {
            "assigned_benefit": -0.14390301704406738,
            "delta_norm": 9.063444137573242,
            "family": "json_schema",
            "route_margin": 0.07825720310211182,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -3.453672409057617
          },
          {
            "assigned_benefit": -0.14390301704406738,
            "delta_norm": 13.509611129760742,
            "family": "json_schema",
            "route_margin": 0.4197324514389038,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -3.453672409057617
          },
          {
            "assigned_benefit": -0.14390301704406738,
            "delta_norm": 22.20932388305664,
            "family": "json_schema",
            "route_margin": 0.7978883385658264,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -3.453672409057617
          },
          {
            "assigned_benefit": -0.14381763339042664,
            "delta_norm": 13.65746784210205,
            "family": "broad_lm",
            "route_margin": 1.3253791332244873,
            "token": "c",
            "token_class": "prose_word",
            "token_total_benefit": -3.4516232013702393
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.4434954325358073,
            "delta_norm": 8.657865524291992,
            "family": "json_schema",
            "route_margin": 1.075549840927124,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.643890380859375
          },
          {
            "assigned_benefit": 0.4434954325358073,
            "delta_norm": 13.558156967163086,
            "family": "json_schema",
            "route_margin": 1.1355760097503662,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.643890380859375
          },
          {
            "assigned_benefit": 0.4434954325358073,
            "delta_norm": 22.21358299255371,
            "family": "json_schema",
            "route_margin": 0.9126418232917786,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.643890380859375
          },
          {
            "assigned_benefit": 0.4348748524983724,
            "delta_norm": 7.750196933746338,
            "family": "json_schema",
            "route_margin": 0.5909568667411804,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.436996459960938
          },
          {
            "assigned_benefit": 0.4348748524983724,
            "delta_norm": 12.848854064941406,
            "family": "json_schema",
            "route_margin": 0.7649803757667542,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.436996459960938
          },
          {
            "assigned_benefit": 0.4348748524983724,
            "delta_norm": 22.1649227142334,
            "family": "json_schema",
            "route_margin": 0.8318861722946167,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.436996459960938
          },
          {
            "assigned_benefit": 0.42559146881103516,
            "delta_norm": 8.35921573638916,
            "family": "json_schema",
            "route_margin": 0.3625180125236511,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.214195251464844
          },
          {
            "assigned_benefit": 0.42559146881103516,
            "delta_norm": 9.128092765808105,
            "family": "json_schema",
            "route_margin": 0.10569411516189575,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.214195251464844
          }
        ],
        "total_assigned_benefit": 1051.952560880993
      },
      "6": {
        "activation_count": 14796,
        "mean_assigned_benefit": 0.05306682790740744,
        "mean_delta_norm": 15.07641079104182,
        "mean_harm": -0.026004055717967357,
        "mean_positive_benefit": 0.09655332895844618,
        "mean_route_margin": 0.497448254607781,
        "positive_benefit_rate": 0.6451743714517437,
        "prose_benefit": 134.89457851179202,
        "structured_benefit": 612.6271134429616,
        "structured_prose_benefit_ratio": 4.541525094645726,
        "token_class_benefit": {
          "brace_bracket_paren": 52.569064841605766,
          "comma_colon_semicolon": 39.94941848516464,
          "function_signature": 30.253139719366988,
          "identifier": 137.3830584504952,
          "indentation": -26.447583775346494,
          "json_key": 38.62100342164439,
          "json_value": 24.302093240121952,
          "newline": 55.566863244799876,
          "number": 20.523938616116833,
          "operator": 19.616864581902806,
          "other": 65.21751862678205,
          "prose_word": 184.55593682654793,
          "quote": 153.38968388239533,
          "space": -50.7761994029471,
          "string_literal": 40.45198495934404
        },
        "token_class_counts": {
          "brace_bracket_paren": 277,
          "comma_colon_semicolon": 426,
          "function_signature": 271,
          "identifier": 2713,
          "indentation": 2016,
          "json_key": 510,
          "json_value": 489,
          "newline": 305,
          "number": 159,
          "operator": 113,
          "other": 304,
          "prose_word": 3964,
          "quote": 493,
          "space": 2253,
          "string_literal": 503
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.17974231019616127,
            "delta_norm": 8.196810722351074,
            "family": "broad_lm",
            "route_margin": 0.46002432703971863,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -4.3138154447078705
          },
          {
            "assigned_benefit": -0.17974231019616127,
            "delta_norm": 13.150712013244629,
            "family": "broad_lm",
            "route_margin": 0.22599589824676514,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -4.3138154447078705
          },
          {
            "assigned_benefit": -0.17974231019616127,
            "delta_norm": 22.149934768676758,
            "family": "broad_lm",
            "route_margin": 0.7349434494972229,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -4.3138154447078705
          },
          {
            "assigned_benefit": -0.14390301704406738,
            "delta_norm": 7.6731038093566895,
            "family": "json_schema",
            "route_margin": 0.08606517314910889,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -3.453672409057617
          },
          {
            "assigned_benefit": -0.14390301704406738,
            "delta_norm": 12.516654968261719,
            "family": "json_schema",
            "route_margin": 0.725058913230896,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -3.453672409057617
          },
          {
            "assigned_benefit": -0.14390301704406738,
            "delta_norm": 22.132102966308594,
            "family": "json_schema",
            "route_margin": 0.7673704028129578,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -3.453672409057617
          },
          {
            "assigned_benefit": -0.14381763339042664,
            "delta_norm": 8.624125480651855,
            "family": "broad_lm",
            "route_margin": 0.474479615688324,
            "token": "c",
            "token_class": "prose_word",
            "token_total_benefit": -3.4516232013702393
          },
          {
            "assigned_benefit": -0.14381763339042664,
            "delta_norm": 12.931536674499512,
            "family": "broad_lm",
            "route_margin": 0.1681225299835205,
            "token": "c",
            "token_class": "prose_word",
            "token_total_benefit": -3.4516232013702393
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.4434954325358073,
            "delta_norm": 9.388772010803223,
            "family": "json_schema",
            "route_margin": 0.0019948482513427734,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.643890380859375
          },
          {
            "assigned_benefit": 0.4434954325358073,
            "delta_norm": 13.236690521240234,
            "family": "json_schema",
            "route_margin": 0.2555248737335205,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.643890380859375
          },
          {
            "assigned_benefit": 0.4434954325358073,
            "delta_norm": 22.152965545654297,
            "family": "json_schema",
            "route_margin": 0.7676111459732056,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.643890380859375
          },
          {
            "assigned_benefit": 0.4348748524983724,
            "delta_norm": 13.131726264953613,
            "family": "json_schema",
            "route_margin": 0.22252517938613892,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.436996459960938
          },
          {
            "assigned_benefit": 0.4348748524983724,
            "delta_norm": 22.164710998535156,
            "family": "json_schema",
            "route_margin": 0.7763402462005615,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.436996459960938
          },
          {
            "assigned_benefit": 0.42559146881103516,
            "delta_norm": 22.15597915649414,
            "family": "json_schema",
            "route_margin": 0.7732692956924438,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.214195251464844
          },
          {
            "assigned_benefit": 0.4194428126017253,
            "delta_norm": 13.026664733886719,
            "family": "json_schema",
            "route_margin": 0.3824976682662964,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.066627502441406
          },
          {
            "assigned_benefit": 0.4194428126017253,
            "delta_norm": 22.205413818359375,
            "family": "json_schema",
            "route_margin": 0.7676566243171692,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.066627502441406
          }
        ],
        "total_assigned_benefit": 785.1767857180005
      },
      "7": {
        "activation_count": 15651,
        "mean_assigned_benefit": 0.055189922037254376,
        "mean_delta_norm": 15.922613975819091,
        "mean_harm": -0.025743816057149805,
        "mean_positive_benefit": 0.09883269209740513,
        "mean_route_margin": 0.4619933549629165,
        "positive_benefit_rate": 0.649670947543288,
        "prose_benefit": 153.2604973380684,
        "structured_benefit": 670.9415690854551,
        "structured_prose_benefit_ratio": 4.3777854094096025,
        "token_class_benefit": {
          "brace_bracket_paren": 55.48728540415567,
          "comma_colon_semicolon": 42.41846965253358,
          "function_signature": 33.62580838054418,
          "identifier": 147.67876479402176,
          "indentation": -26.846155139152,
          "json_key": 41.186784602701714,
          "json_value": 28.3011601340646,
          "newline": 71.28128746732693,
          "number": 24.37033540010452,
          "operator": 20.75306393702823,
          "other": 70.58749644157677,
          "prose_word": 203.8924884625396,
          "quote": 163.19524367650357,
          "space": -54.79792904535609,
          "string_literal": 42.643365636467934
        },
        "token_class_counts": {
          "brace_bracket_paren": 298,
          "comma_colon_semicolon": 450,
          "function_signature": 305,
          "identifier": 2821,
          "indentation": 2058,
          "json_key": 534,
          "json_value": 547,
          "newline": 370,
          "number": 179,
          "operator": 116,
          "other": 333,
          "prose_word": 4121,
          "quote": 523,
          "space": 2465,
          "string_literal": 531
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.17974231019616127,
            "delta_norm": 12.893712043762207,
            "family": "broad_lm",
            "route_margin": 0.3393423557281494,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -4.3138154447078705
          },
          {
            "assigned_benefit": -0.17974231019616127,
            "delta_norm": 24.101839065551758,
            "family": "broad_lm",
            "route_margin": 0.7300772666931152,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -4.3138154447078705
          },
          {
            "assigned_benefit": -0.14390301704406738,
            "delta_norm": 7.465703964233398,
            "family": "json_schema",
            "route_margin": 0.15647178888320923,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -3.453672409057617
          },
          {
            "assigned_benefit": -0.14390301704406738,
            "delta_norm": 12.777634620666504,
            "family": "json_schema",
            "route_margin": 0.44136732816696167,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -3.453672409057617
          },
          {
            "assigned_benefit": -0.14390301704406738,
            "delta_norm": 24.134075164794922,
            "family": "json_schema",
            "route_margin": 0.7768314480781555,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -3.453672409057617
          },
          {
            "assigned_benefit": -0.14381763339042664,
            "delta_norm": 9.298227310180664,
            "family": "broad_lm",
            "route_margin": 0.1530340313911438,
            "token": "c",
            "token_class": "prose_word",
            "token_total_benefit": -3.4516232013702393
          },
          {
            "assigned_benefit": -0.14381763339042664,
            "delta_norm": 12.850318908691406,
            "family": "broad_lm",
            "route_margin": 0.39602017402648926,
            "token": "c",
            "token_class": "prose_word",
            "token_total_benefit": -3.4516232013702393
          },
          {
            "assigned_benefit": -0.14381763339042664,
            "delta_norm": 24.224767684936523,
            "family": "broad_lm",
            "route_margin": 0.7349515557289124,
            "token": "c",
            "token_class": "prose_word",
            "token_total_benefit": -3.4516232013702393
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.4434954325358073,
            "delta_norm": 12.9307279586792,
            "family": "json_schema",
            "route_margin": 0.38366442918777466,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.643890380859375
          },
          {
            "assigned_benefit": 0.4434954325358073,
            "delta_norm": 24.133909225463867,
            "family": "json_schema",
            "route_margin": 0.7520334720611572,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.643890380859375
          },
          {
            "assigned_benefit": 0.4348748524983724,
            "delta_norm": 12.863738059997559,
            "family": "json_schema",
            "route_margin": 0.2991443872451782,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.436996459960938
          },
          {
            "assigned_benefit": 0.4348748524983724,
            "delta_norm": 24.09161949157715,
            "family": "json_schema",
            "route_margin": 0.6932511925697327,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.436996459960938
          },
          {
            "assigned_benefit": 0.42559146881103516,
            "delta_norm": 12.8611421585083,
            "family": "json_schema",
            "route_margin": 0.3129814863204956,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.214195251464844
          },
          {
            "assigned_benefit": 0.42559146881103516,
            "delta_norm": 24.08146858215332,
            "family": "json_schema",
            "route_margin": 0.7480195760726929,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.214195251464844
          },
          {
            "assigned_benefit": 0.4194428126017253,
            "delta_norm": 12.947617530822754,
            "family": "json_schema",
            "route_margin": 0.5175976753234863,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.066627502441406
          },
          {
            "assigned_benefit": 0.4194428126017253,
            "delta_norm": 24.130971908569336,
            "family": "json_schema",
            "route_margin": 0.6954326629638672,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.066627502441406
          }
        ],
        "total_assigned_benefit": 863.7774698050682
      }
    },
    "layer_expert_cards": {
      "layer_0_expert_0": {
        "activation_count": 1525,
        "mean_assigned_benefit": 0.04490985902427921,
        "mean_delta_norm": 8.276492464659643,
        "mean_harm": -0.021789433891489556,
        "mean_positive_benefit": 0.09745607806225881,
        "mean_route_margin": 0.43231035028324755,
        "positive_benefit_rate": 0.5593442622950819,
        "prose_benefit": 7.580270872522558,
        "structured_benefit": 56.32418131457987,
        "structured_prose_benefit_ratio": 7.4303652549867705,
        "token_class_benefit": {
          "brace_bracket_paren": 5.777614136536916,
          "comma_colon_semicolon": 4.954257607460022,
          "function_signature": 4.121425847212474,
          "identifier": 10.502811423192416,
          "indentation": -4.109578302285325,
          "json_key": 2.139298230409622,
          "json_value": 3.4367281645536427,
          "newline": 2.118638406219323,
          "number": 3.673694948355357,
          "operator": 1.7157195409138997,
          "other": 6.778367169716149,
          "prose_word": 15.640157822519539,
          "quote": 15.177726109822594,
          "space": -6.145592992504437,
          "string_literal": 2.706266899903615
        },
        "token_class_counts": {
          "brace_bracket_paren": 33,
          "comma_colon_semicolon": 48,
          "function_signature": 33,
          "identifier": 221,
          "indentation": 361,
          "json_key": 29,
          "json_value": 53,
          "newline": 14,
          "number": 25,
          "operator": 8,
          "other": 30,
          "prose_word": 343,
          "quote": 50,
          "space": 233,
          "string_literal": 44
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.12130660812060039,
            "delta_norm": 6.604379653930664,
            "family": "json_schema",
            "route_margin": 0.4903629422187805,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.911358594894409
          },
          {
            "assigned_benefit": -0.10809943079948425,
            "delta_norm": 6.2483906745910645,
            "family": "json_schema",
            "route_margin": 0.03950667381286621,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.594386339187622
          },
          {
            "assigned_benefit": -0.10410678386688232,
            "delta_norm": 5.956540584564209,
            "family": "json_schema",
            "route_margin": 0.89411860704422,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.498562812805176
          },
          {
            "assigned_benefit": -0.10397198796272278,
            "delta_norm": 6.465369701385498,
            "family": "json_schema",
            "route_margin": 0.23440614342689514,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.4953277111053467
          },
          {
            "assigned_benefit": -0.10388837258021037,
            "delta_norm": 7.891136646270752,
            "family": "code_heavy",
            "route_margin": 0.06148719787597656,
            "token": "d",
            "token_class": "string_literal",
            "token_total_benefit": -2.493320941925049
          },
          {
            "assigned_benefit": -0.09784005582332611,
            "delta_norm": 7.942437171936035,
            "family": "code_heavy",
            "route_margin": 0.13920152187347412,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -2.3481613397598267
          },
          {
            "assigned_benefit": -0.09750870863596599,
            "delta_norm": 7.863005638122559,
            "family": "code_heavy",
            "route_margin": 0.7591955065727234,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -2.3402090072631836
          },
          {
            "assigned_benefit": -0.0962066650390625,
            "delta_norm": 6.182187080383301,
            "family": "json_schema",
            "route_margin": 0.37403738498687744,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.3089599609375
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.3989645640055339,
            "delta_norm": 7.758492469787598,
            "family": "json_schema",
            "route_margin": 0.5355339646339417,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.575149536132812
          },
          {
            "assigned_benefit": 0.38402652740478516,
            "delta_norm": 9.097352027893066,
            "family": "code_heavy",
            "route_margin": 0.45324981212615967,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 9.216636657714844
          },
          {
            "assigned_benefit": 0.3677576382954915,
            "delta_norm": 7.949248313903809,
            "family": "code_heavy",
            "route_margin": 1.3150949478149414,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.826183319091797
          },
          {
            "assigned_benefit": 0.35744380950927734,
            "delta_norm": 7.9202189445495605,
            "family": "code_heavy",
            "route_margin": 0.2192007303237915,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 8.578651428222656
          },
          {
            "assigned_benefit": 0.3566751480102539,
            "delta_norm": 8.97778034210205,
            "family": "code_heavy",
            "route_margin": 0.2007235288619995,
            "token": "\"",
            "token_class": "function_signature",
            "token_total_benefit": 8.560203552246094
          },
          {
            "assigned_benefit": 0.3564949035644531,
            "delta_norm": 7.949997901916504,
            "family": "code_heavy",
            "route_margin": 0.20150130987167358,
            "token": "\\",
            "token_class": "function_signature",
            "token_total_benefit": 8.555877685546875
          },
          {
            "assigned_benefit": 0.3549944559733073,
            "delta_norm": 7.8502092361450195,
            "family": "code_heavy",
            "route_margin": 1.2820630073547363,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 8.519866943359375
          },
          {
            "assigned_benefit": 0.35289955139160156,
            "delta_norm": 7.421342849731445,
            "family": "code_heavy",
            "route_margin": 0.3947070837020874,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.469589233398438
          }
        ],
        "total_assigned_benefit": 68.48753501202579
      },
      "layer_0_expert_1": {
        "activation_count": 1223,
        "mean_assigned_benefit": 0.04749054143268181,
        "mean_delta_norm": 8.219666474779805,
        "mean_harm": -0.024079731856780397,
        "mean_positive_benefit": 0.08828284097121998,
        "mean_route_margin": 0.36796991116476174,
        "positive_benefit_rate": 0.6369582992641046,
        "prose_benefit": 8.120977023770962,
        "structured_benefit": 48.302477263223935,
        "structured_prose_benefit_ratio": 5.947865278012419,
        "token_class_benefit": {
          "brace_bracket_paren": 4.856701821088792,
          "comma_colon_semicolon": 3.259343425432841,
          "function_signature": 1.6101170182228086,
          "identifier": 8.774273070196314,
          "indentation": -2.484336210880429,
          "json_key": 1.7477401097615564,
          "json_value": 1.6144871264696121,
          "newline": 8.89372797838031,
          "number": 1.437041521072388,
          "operator": 1.225802739461263,
          "other": 4.3411282896995536,
          "prose_word": 11.111603402843077,
          "quote": 11.43069823582967,
          "space": -3.1899405727162953,
          "string_literal": 3.4525442173083625
        },
        "token_class_counts": {
          "brace_bracket_paren": 30,
          "comma_colon_semicolon": 37,
          "function_signature": 23,
          "identifier": 220,
          "indentation": 221,
          "json_key": 39,
          "json_value": 41,
          "newline": 50,
          "number": 10,
          "operator": 6,
          "other": 17,
          "prose_word": 284,
          "quote": 38,
          "space": 171,
          "string_literal": 36
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.14381763339042664,
            "delta_norm": 9.876863479614258,
            "family": "broad_lm",
            "route_margin": 0.11163318157196045,
            "token": "c",
            "token_class": "prose_word",
            "token_total_benefit": -3.4516232013702393
          },
          {
            "assigned_benefit": -0.12831215063730875,
            "delta_norm": 7.100924015045166,
            "family": "json_schema",
            "route_margin": 0.6002681255340576,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -3.07949161529541
          },
          {
            "assigned_benefit": -0.11696084340413411,
            "delta_norm": 7.779766082763672,
            "family": "json_schema",
            "route_margin": 0.08343786001205444,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.8070602416992188
          },
          {
            "assigned_benefit": -0.11042344570159912,
            "delta_norm": 7.3479180335998535,
            "family": "json_schema",
            "route_margin": 0.1539241075515747,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.650162696838379
          },
          {
            "assigned_benefit": -0.1018477330605189,
            "delta_norm": 7.697700500488281,
            "family": "broad_lm",
            "route_margin": 0.11317026615142822,
            "token": " ",
            "token_class": "indentation",
            "token_total_benefit": -2.4443455934524536
          },
          {
            "assigned_benefit": -0.10102646052837372,
            "delta_norm": 10.459233283996582,
            "family": "code_heavy",
            "route_margin": 0.6603490114212036,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.4246350526809692
          },
          {
            "assigned_benefit": -0.10029297073682149,
            "delta_norm": 7.7914509773254395,
            "family": "json_schema",
            "route_margin": 0.20827221870422363,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.407031297683716
          },
          {
            "assigned_benefit": -0.09847732384999593,
            "delta_norm": 9.461091995239258,
            "family": "broad_lm",
            "route_margin": 0.5482609272003174,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -2.3634557723999023
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.3688637415568034,
            "delta_norm": 7.921705722808838,
            "family": "json_schema",
            "route_margin": 0.044175148010253906,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 8.852729797363281
          },
          {
            "assigned_benefit": 0.3683640956878662,
            "delta_norm": 9.36131763458252,
            "family": "json_schema",
            "route_margin": 0.0718832015991211,
            "token": "\\n",
            "token_class": "newline",
            "token_total_benefit": 8.840738296508789
          },
          {
            "assigned_benefit": 0.3612794876098633,
            "delta_norm": 9.517067909240723,
            "family": "json_schema",
            "route_margin": 0.9331783652305603,
            "token": "\\n",
            "token_class": "newline",
            "token_total_benefit": 8.670707702636719
          },
          {
            "assigned_benefit": 0.34745808442433673,
            "delta_norm": 6.873306751251221,
            "family": "code_heavy",
            "route_margin": 0.0538402795791626,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.338994026184082
          },
          {
            "assigned_benefit": 0.3438250223795573,
            "delta_norm": 7.2386674880981445,
            "family": "code_heavy",
            "route_margin": 0.3042123317718506,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 8.251800537109375
          },
          {
            "assigned_benefit": 0.3432128429412842,
            "delta_norm": 10.383746147155762,
            "family": "code_heavy",
            "route_margin": 0.23975622653961182,
            "token": "(",
            "token_class": "function_signature",
            "token_total_benefit": 8.23710823059082
          },
          {
            "assigned_benefit": 0.3410816192626953,
            "delta_norm": 7.6335129737854,
            "family": "code_heavy",
            "route_margin": 0.006400585174560547,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 8.185958862304688
          },
          {
            "assigned_benefit": 0.33861692746480304,
            "delta_norm": 9.717019081115723,
            "family": "json_schema",
            "route_margin": 0.5141880512237549,
            "token": "\\n",
            "token_class": "newline",
            "token_total_benefit": 8.126806259155273
          }
        ],
        "total_assigned_benefit": 58.08093217216985
      },
      "layer_0_expert_2": {
        "activation_count": 419,
        "mean_assigned_benefit": 0.045653283129668105,
        "mean_delta_norm": 7.683375043345522,
        "mean_harm": -0.023704838743677525,
        "mean_positive_benefit": 0.09688044368342542,
        "mean_route_margin": 0.2214733024521204,
        "positive_benefit_rate": 0.5751789976133651,
        "prose_benefit": 2.7255348111634703,
        "structured_benefit": 14.623156680428268,
        "structured_prose_benefit_ratio": 5.365243041671505,
        "token_class_benefit": {
          "brace_bracket_paren": 0.6957503333687782,
          "comma_colon_semicolon": 0.4868564506371816,
          "function_signature": 0.9423973113298415,
          "identifier": 3.704573797682921,
          "indentation": -1.234492393520971,
          "json_key": 1.2953489323457081,
          "json_value": 0.11338540787498157,
          "newline": 0.228601053370312,
          "number": 1.3116711576779685,
          "operator": 1.552300214767456,
          "other": 2.402234574158986,
          "prose_word": 4.6426430507563055,
          "quote": 3.759700298309326,
          "space": -1.30481628049165,
          "string_literal": 0.5325717230637868
        },
        "token_class_counts": {
          "brace_bracket_paren": 6,
          "comma_colon_semicolon": 5,
          "function_signature": 6,
          "identifier": 75,
          "indentation": 95,
          "json_key": 10,
          "json_value": 8,
          "newline": 3,
          "number": 9,
          "operator": 8,
          "other": 9,
          "prose_word": 100,
          "quote": 12,
          "space": 67,
          "string_literal": 6
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.10964437325795491,
            "delta_norm": 7.076123237609863,
            "family": "code_heavy",
            "route_margin": 0.26374438405036926,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -2.631464958190918
          },
          {
            "assigned_benefit": -0.0939420076707999,
            "delta_norm": 7.990327835083008,
            "family": "json_schema",
            "route_margin": 0.07741367816925049,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -2.2546081840991974
          },
          {
            "assigned_benefit": -0.08750950296719869,
            "delta_norm": 8.80435848236084,
            "family": "json_schema",
            "route_margin": 0.03619968891143799,
            "token": "l",
            "token_class": "identifier",
            "token_total_benefit": -2.1002280712127686
          },
          {
            "assigned_benefit": -0.08728645245234172,
            "delta_norm": 8.664735794067383,
            "family": "broad_lm",
            "route_margin": 0.23007416725158691,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -2.094874858856201
          },
          {
            "assigned_benefit": -0.07794865469137828,
            "delta_norm": 8.8689603805542,
            "family": "broad_lm",
            "route_margin": 0.5961955189704895,
            "token": "l",
            "token_class": "prose_word",
            "token_total_benefit": -1.8707677125930786
          },
          {
            "assigned_benefit": -0.0737869143486023,
            "delta_norm": 8.666003227233887,
            "family": "code_heavy",
            "route_margin": 0.17924129962921143,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -1.770885944366455
          },
          {
            "assigned_benefit": -0.07299053172270457,
            "delta_norm": 7.347919464111328,
            "family": "code_heavy",
            "route_margin": 0.025287725031375885,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -1.7517727613449097
          },
          {
            "assigned_benefit": -0.07161245743433635,
            "delta_norm": 8.786848068237305,
            "family": "code_heavy",
            "route_margin": 0.5731741189956665,
            "token": "l",
            "token_class": "string_literal",
            "token_total_benefit": -1.7186989784240723
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.40347035725911456,
            "delta_norm": 8.66384220123291,
            "family": "json_schema",
            "route_margin": 0.46452051401138306,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.68328857421875
          },
          {
            "assigned_benefit": 0.38709576924641925,
            "delta_norm": 8.205790519714355,
            "family": "code_heavy",
            "route_margin": 0.340528666973114,
            "token": "\\",
            "token_class": "function_signature",
            "token_total_benefit": 9.290298461914062
          },
          {
            "assigned_benefit": 0.3551967938741048,
            "delta_norm": 7.664566516876221,
            "family": "code_heavy",
            "route_margin": 0.21034395694732666,
            "token": "'",
            "token_class": "quote",
            "token_total_benefit": 8.524723052978516
          },
          {
            "assigned_benefit": 0.3346802393595378,
            "delta_norm": 7.403939247131348,
            "family": "json_schema",
            "route_margin": 0.11047941446304321,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 8.032325744628906
          },
          {
            "assigned_benefit": 0.3265867233276367,
            "delta_norm": 7.835551738739014,
            "family": "json_schema",
            "route_margin": 0.355583131313324,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 7.838081359863281
          },
          {
            "assigned_benefit": 0.3223867416381836,
            "delta_norm": 7.487722396850586,
            "family": "json_schema",
            "route_margin": 0.29049086570739746,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 7.737281799316406
          },
          {
            "assigned_benefit": 0.3215319315592448,
            "delta_norm": 7.822457790374756,
            "family": "code_heavy",
            "route_margin": 0.3904791474342346,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 7.716766357421875
          },
          {
            "assigned_benefit": 0.3159599304199219,
            "delta_norm": 8.372895240783691,
            "family": "code_heavy",
            "route_margin": 0.671478807926178,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 7.583038330078125
          }
        ],
        "total_assigned_benefit": 19.128725631330937
      },
      "layer_0_expert_3": {
        "activation_count": 478,
        "mean_assigned_benefit": 0.0640026808210104,
        "mean_delta_norm": 7.8142046000668195,
        "mean_harm": -0.030370794453968605,
        "mean_positive_benefit": 0.10114676001087099,
        "mean_route_margin": 0.3288530935396959,
        "positive_benefit_rate": 0.7175732217573222,
        "prose_benefit": 5.853060357350234,
        "structured_benefit": 23.179162027314298,
        "structured_prose_benefit_ratio": 3.960178199462109,
        "token_class_benefit": {
          "brace_bracket_paren": 1.869943221410116,
          "comma_colon_semicolon": 2.049654940764109,
          "function_signature": 1.649754544099172,
          "identifier": 6.183151063198843,
          "json_key": 1.4907986621061962,
          "json_value": 1.0802713980277379,
          "newline": 3.0330205261707306,
          "number": 0.08823593457539876,
          "operator": 0.9268609682718914,
          "other": 3.214055246595914,
          "prose_word": 6.449596914307525,
          "quote": 3.9775358835856123,
          "space": -2.2495327557747564,
          "string_literal": 0.8299348851044973
        },
        "token_class_counts": {
          "brace_bracket_paren": 8,
          "comma_colon_semicolon": 24,
          "function_signature": 7,
          "identifier": 115,
          "json_key": 15,
          "json_value": 20,
          "newline": 15,
          "number": 1,
          "operator": 5,
          "other": 18,
          "prose_word": 123,
          "quote": 12,
          "space": 96,
          "string_literal": 19
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.11193382243315379,
            "delta_norm": 8.022441864013672,
            "family": "broad_lm",
            "route_margin": 0.08693909645080566,
            "token": "e",
            "token_class": "prose_word",
            "token_total_benefit": -2.686411738395691
          },
          {
            "assigned_benefit": -0.0975755254427592,
            "delta_norm": 6.560188293457031,
            "family": "code_heavy",
            "route_margin": 0.03469502925872803,
            "token": "s",
            "token_class": "string_literal",
            "token_total_benefit": -2.3418126106262207
          },
          {
            "assigned_benefit": -0.09154083828131358,
            "delta_norm": 8.633506774902344,
            "family": "json_schema",
            "route_margin": 0.1386769711971283,
            "token": "d",
            "token_class": "json_value",
            "token_total_benefit": -2.196980118751526
          },
          {
            "assigned_benefit": -0.0898671845595042,
            "delta_norm": 7.657986164093018,
            "family": "broad_lm",
            "route_margin": 0.08871650695800781,
            "token": "e",
            "token_class": "prose_word",
            "token_total_benefit": -2.1568124294281006
          },
          {
            "assigned_benefit": -0.08743790785471599,
            "delta_norm": 8.662972450256348,
            "family": "code_heavy",
            "route_margin": 0.08001038432121277,
            "token": "d",
            "token_class": "string_literal",
            "token_total_benefit": -2.0985097885131836
          },
          {
            "assigned_benefit": -0.084659809867541,
            "delta_norm": 7.178381443023682,
            "family": "json_schema",
            "route_margin": 0.06111407279968262,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.031835436820984
          },
          {
            "assigned_benefit": -0.08465861777464549,
            "delta_norm": 7.17838191986084,
            "family": "json_schema",
            "route_margin": 0.06111407279968262,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.0318068265914917
          },
          {
            "assigned_benefit": -0.08353991309801738,
            "delta_norm": 6.462282180786133,
            "family": "json_schema",
            "route_margin": 0.02286684513092041,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -2.004957914352417
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.41413907210032147,
            "delta_norm": 7.698221206665039,
            "family": "code_heavy",
            "route_margin": 0.05715304613113403,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.939337730407715
          },
          {
            "assigned_benefit": 0.40207378069559735,
            "delta_norm": 8.178925514221191,
            "family": "code_heavy",
            "route_margin": 0.7633713483810425,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.649770736694336
          },
          {
            "assigned_benefit": 0.3999309539794922,
            "delta_norm": 7.924570560455322,
            "family": "json_schema",
            "route_margin": 0.25991594791412354,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.598342895507812
          },
          {
            "assigned_benefit": 0.3964542547861735,
            "delta_norm": 7.485819339752197,
            "family": "code_heavy",
            "route_margin": 0.5642314553260803,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.514902114868164
          },
          {
            "assigned_benefit": 0.3771365483601888,
            "delta_norm": 7.619781494140625,
            "family": "json_schema",
            "route_margin": 0.697057843208313,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.051277160644531
          },
          {
            "assigned_benefit": 0.3718280792236328,
            "delta_norm": 6.869251251220703,
            "family": "json_schema",
            "route_margin": 0.5350871086120605,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 8.923873901367188
          },
          {
            "assigned_benefit": 0.35584481557210285,
            "delta_norm": 6.53132963180542,
            "family": "json_schema",
            "route_margin": 0.053813397884368896,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 8.540275573730469
          },
          {
            "assigned_benefit": 0.35584449768066406,
            "delta_norm": 6.53132963180542,
            "family": "json_schema",
            "route_margin": 0.053813397884368896,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 8.540267944335938
          }
        ],
        "total_assigned_benefit": 30.59328143244297
      },
      "layer_0_expert_4": {
        "activation_count": 712,
        "mean_assigned_benefit": 0.07180196553094179,
        "mean_delta_norm": 8.293515751201115,
        "mean_harm": -0.02229059235852303,
        "mean_positive_benefit": 0.10293165290745628,
        "mean_route_margin": 0.45840933977553017,
        "positive_benefit_rate": 0.7514044943820225,
        "prose_benefit": 12.628986703619992,
        "structured_benefit": 36.976350735873005,
        "structured_prose_benefit_ratio": 2.9278952938697804,
        "token_class_benefit": {
          "brace_bracket_paren": 3.6446357145905486,
          "comma_colon_semicolon": 2.314827680587769,
          "function_signature": 2.150962640841802,
          "identifier": 8.780701633542774,
          "indentation": -0.0681316399325927,
          "json_key": 4.220872049530349,
          "json_value": 0.7663090204199154,
          "newline": 4.026051551103592,
          "number": 0.8459134896596272,
          "operator": 0.41185279687245685,
          "other": 3.312466661135356,
          "prose_word": 12.396988123034443,
          "quote": 7.4421485265096035,
          "space": -1.4946744220796977,
          "string_literal": 2.372075632214546
        },
        "token_class_counts": {
          "brace_bracket_paren": 16,
          "comma_colon_semicolon": 20,
          "function_signature": 16,
          "identifier": 148,
          "indentation": 7,
          "json_key": 42,
          "json_value": 13,
          "newline": 20,
          "number": 9,
          "operator": 4,
          "other": 14,
          "prose_word": 239,
          "quote": 22,
          "space": 119,
          "string_literal": 23
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.11974493662516277,
            "delta_norm": 7.197701930999756,
            "family": "code_heavy",
            "route_margin": 0.09770715236663818,
            "token": "5",
            "token_class": "number",
            "token_total_benefit": -2.8738784790039062
          },
          {
            "assigned_benefit": -0.109354833761851,
            "delta_norm": 8.014079093933105,
            "family": "code_heavy",
            "route_margin": 0.7288464307785034,
            "token": "-",
            "token_class": "operator",
            "token_total_benefit": -2.624516010284424
          },
          {
            "assigned_benefit": -0.10159913450479507,
            "delta_norm": 8.810613632202148,
            "family": "broad_lm",
            "route_margin": 0.9823266267776489,
            "token": "p",
            "token_class": "prose_word",
            "token_total_benefit": -2.438379228115082
          },
          {
            "assigned_benefit": -0.07303215439120929,
            "delta_norm": 8.289925575256348,
            "family": "code_heavy",
            "route_margin": 0.5827957987785339,
            "token": "p",
            "token_class": "identifier",
            "token_total_benefit": -1.7527717053890228
          },
          {
            "assigned_benefit": -0.06911597649256389,
            "delta_norm": 7.029455661773682,
            "family": "json_schema",
            "route_margin": 0.1706952452659607,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.6587834358215332
          },
          {
            "assigned_benefit": -0.065230593085289,
            "delta_norm": 7.796542167663574,
            "family": "broad_lm",
            "route_margin": 0.19977974891662598,
            "token": "p",
            "token_class": "prose_word",
            "token_total_benefit": -1.565534234046936
          },
          {
            "assigned_benefit": -0.0628610650698344,
            "delta_norm": 5.966010093688965,
            "family": "code_heavy",
            "route_margin": 0.18079614639282227,
            "token": "s",
            "token_class": "identifier",
            "token_total_benefit": -1.5086655616760254
          },
          {
            "assigned_benefit": -0.06268421808878581,
            "delta_norm": 7.610665321350098,
            "family": "json_schema",
            "route_margin": 0.45272496342658997,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.5044212341308594
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.4348748524983724,
            "delta_norm": 10.959671974182129,
            "family": "json_schema",
            "route_margin": 0.1521834135055542,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.436996459960938
          },
          {
            "assigned_benefit": 0.42559146881103516,
            "delta_norm": 8.307329177856445,
            "family": "json_schema",
            "route_margin": 0.00852745771408081,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.214195251464844
          },
          {
            "assigned_benefit": 0.4194428126017253,
            "delta_norm": 8.493782043457031,
            "family": "json_schema",
            "route_margin": 0.3256263732910156,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.066627502441406
          },
          {
            "assigned_benefit": 0.3995812733968099,
            "delta_norm": 8.493849754333496,
            "family": "json_schema",
            "route_margin": 1.0659480094909668,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.589950561523438
          },
          {
            "assigned_benefit": 0.3894158601760864,
            "delta_norm": 6.432291030883789,
            "family": "code_heavy",
            "route_margin": 0.6961833834648132,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.345980644226074
          },
          {
            "assigned_benefit": 0.38902703921000165,
            "delta_norm": 8.979360580444336,
            "family": "code_heavy",
            "route_margin": 0.12237071990966797,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.336648941040039
          },
          {
            "assigned_benefit": 0.3847957452138265,
            "delta_norm": 6.4818572998046875,
            "family": "code_heavy",
            "route_margin": 0.6426351070404053,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.235097885131836
          },
          {
            "assigned_benefit": 0.38037506739298504,
            "delta_norm": 6.05872106552124,
            "family": "code_heavy",
            "route_margin": 0.152570903301239,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.12900161743164
          }
        ],
        "total_assigned_benefit": 51.122999458030556
      },
      "layer_0_expert_5": {
        "activation_count": 470,
        "mean_assigned_benefit": 0.06696653526693987,
        "mean_delta_norm": 8.188925283513171,
        "mean_harm": -0.03752465129494913,
        "mean_positive_benefit": 0.09556710394648142,
        "mean_route_margin": 0.28874149332021143,
        "positive_benefit_rate": 0.7851063829787234,
        "prose_benefit": 6.645826812530235,
        "structured_benefit": 22.542619470669237,
        "structured_prose_benefit_ratio": 3.391996226589403,
        "token_class_benefit": {
          "brace_bracket_paren": 0.5252087513605754,
          "comma_colon_semicolon": 1.4213044544061026,
          "function_signature": 0.823767180244128,
          "identifier": 6.758807082970936,
          "json_key": 2.5947203040122986,
          "json_value": 1.0519608322841427,
          "newline": 0.860070258386107,
          "number": 1.2561132113138835,
          "operator": 0.3288588921229045,
          "other": 2.7389613489309945,
          "prose_word": 7.2454386583219,
          "quote": 4.5748880704243975,
          "space": -1.0527479024603963,
          "string_literal": 2.3469204331437745
        },
        "token_class_counts": {
          "brace_bracket_paren": 4,
          "comma_colon_semicolon": 16,
          "function_signature": 9,
          "identifier": 119,
          "json_key": 31,
          "json_value": 23,
          "newline": 5,
          "number": 10,
          "operator": 3,
          "other": 11,
          "prose_word": 137,
          "quote": 15,
          "space": 63,
          "string_literal": 24
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.1176329255104065,
            "delta_norm": 7.187260150909424,
            "family": "broad_lm",
            "route_margin": 0.13500535488128662,
            "token": "o",
            "token_class": "prose_word",
            "token_total_benefit": -2.823190212249756
          },
          {
            "assigned_benefit": -0.10848332444826762,
            "delta_norm": 7.168857097625732,
            "family": "code_heavy",
            "route_margin": 0.9562601447105408,
            "token": "n",
            "token_class": "identifier",
            "token_total_benefit": -2.603599786758423
          },
          {
            "assigned_benefit": -0.10358279943466187,
            "delta_norm": 8.354159355163574,
            "family": "json_schema",
            "route_margin": 0.07974052429199219,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.4859871864318848
          },
          {
            "assigned_benefit": -0.09491795673966408,
            "delta_norm": 10.097776412963867,
            "family": "broad_lm",
            "route_margin": 1.1896662712097168,
            "token": "l",
            "token_class": "prose_word",
            "token_total_benefit": -2.278030961751938
          },
          {
            "assigned_benefit": -0.08644822239875793,
            "delta_norm": 7.154183387756348,
            "family": "code_heavy",
            "route_margin": 0.7793089151382446,
            "token": "d",
            "token_class": "string_literal",
            "token_total_benefit": -2.0747573375701904
          },
          {
            "assigned_benefit": -0.08567521969477336,
            "delta_norm": 7.918954372406006,
            "family": "json_schema",
            "route_margin": 0.12886056303977966,
            "token": "d",
            "token_class": "json_key",
            "token_total_benefit": -2.0562052726745605
          },
          {
            "assigned_benefit": -0.08452899257342021,
            "delta_norm": 8.047100067138672,
            "family": "broad_lm",
            "route_margin": 0.3125133514404297,
            "token": "w",
            "token_class": "prose_word",
            "token_total_benefit": -2.028695821762085
          },
          {
            "assigned_benefit": -0.08370453119277954,
            "delta_norm": 8.248384475708008,
            "family": "json_schema",
            "route_margin": 0.022517025470733643,
            "token": "d",
            "token_class": "json_key",
            "token_total_benefit": -2.008908748626709
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.39834149678548175,
            "delta_norm": 10.298689842224121,
            "family": "json_schema",
            "route_margin": 0.3817097544670105,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.560195922851562
          },
          {
            "assigned_benefit": 0.3903733491897583,
            "delta_norm": 8.560127258300781,
            "family": "code_heavy",
            "route_margin": 0.1378093659877777,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.3689603805542
          },
          {
            "assigned_benefit": 0.35045115152994794,
            "delta_norm": 7.052292346954346,
            "family": "code_heavy",
            "route_margin": 0.15361344814300537,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 8.41082763671875
          },
          {
            "assigned_benefit": 0.3433542251586914,
            "delta_norm": 7.569024562835693,
            "family": "json_schema",
            "route_margin": 0.2862868905067444,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 8.240501403808594
          },
          {
            "assigned_benefit": 0.33442242940266925,
            "delta_norm": 7.538924694061279,
            "family": "json_schema",
            "route_margin": 0.19164836406707764,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 8.026138305664062
          },
          {
            "assigned_benefit": 0.32917070388793945,
            "delta_norm": 6.834974765777588,
            "family": "code_heavy",
            "route_margin": 0.37061238288879395,
            "token": "_",
            "token_class": "identifier",
            "token_total_benefit": 7.900096893310547
          },
          {
            "assigned_benefit": 0.32523314158121747,
            "delta_norm": 7.479437351226807,
            "family": "code_heavy",
            "route_margin": 0.297630250453949,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 7.805595397949219
          },
          {
            "assigned_benefit": 0.32491715749104816,
            "delta_norm": 7.358383655548096,
            "family": "json_schema",
            "route_margin": 0.3414149880409241,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 7.798011779785156
          }
        ],
        "total_assigned_benefit": 31.47427157546174
      },
      "layer_0_expert_6": {
        "activation_count": 766,
        "mean_assigned_benefit": 0.049244407133796624,
        "mean_delta_norm": 7.651875648423835,
        "mean_harm": -0.02464824876597509,
        "mean_positive_benefit": 0.10517233476435776,
        "mean_route_margin": 0.33320077631243217,
        "positive_benefit_rate": 0.5691906005221932,
        "prose_benefit": 2.2631898033432676,
        "structured_benefit": 33.42495940594623,
        "structured_prose_benefit_ratio": 14.768959879798702,
        "token_class_benefit": {
          "brace_bracket_paren": 2.899038513501485,
          "comma_colon_semicolon": 0.34067823489507043,
          "function_signature": 1.195397153496742,
          "identifier": 6.108099590986965,
          "indentation": -2.8234467206833265,
          "json_key": 1.9893883938590686,
          "json_value": 1.7081480234240494,
          "newline": 1.5783749570449195,
          "number": 0.8559368451436361,
          "operator": 1.5734657843907676,
          "other": 2.368895212809245,
          "prose_word": 6.904979700843493,
          "quote": 13.0529940923055,
          "space": -2.1541717344274116,
          "string_literal": 2.123437816898028
        },
        "token_class_counts": {
          "brace_bracket_paren": 16,
          "comma_colon_semicolon": 5,
          "function_signature": 14,
          "identifier": 109,
          "indentation": 203,
          "json_key": 24,
          "json_value": 30,
          "newline": 9,
          "number": 6,
          "operator": 9,
          "other": 8,
          "prose_word": 174,
          "quote": 42,
          "space": 92,
          "string_literal": 25
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.17974231019616127,
            "delta_norm": 8.196810722351074,
            "family": "broad_lm",
            "route_margin": 0.46002432703971863,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -4.3138154447078705
          },
          {
            "assigned_benefit": -0.14390301704406738,
            "delta_norm": 7.6731038093566895,
            "family": "json_schema",
            "route_margin": 0.08606517314910889,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -3.453672409057617
          },
          {
            "assigned_benefit": -0.1258842075864474,
            "delta_norm": 9.665914535522461,
            "family": "broad_lm",
            "route_margin": 0.2847093939781189,
            "token": "m",
            "token_class": "prose_word",
            "token_total_benefit": -3.0212209820747375
          },
          {
            "assigned_benefit": -0.11105093856652577,
            "delta_norm": 7.189866542816162,
            "family": "broad_lm",
            "route_margin": 0.41126811504364014,
            "token": "o",
            "token_class": "prose_word",
            "token_total_benefit": -2.6652225255966187
          },
          {
            "assigned_benefit": -0.10949698835611343,
            "delta_norm": 8.086050033569336,
            "family": "broad_lm",
            "route_margin": 0.40335559844970703,
            "token": "o",
            "token_class": "prose_word",
            "token_total_benefit": -2.6279277205467224
          },
          {
            "assigned_benefit": -0.10707541306813557,
            "delta_norm": 8.285356521606445,
            "family": "code_heavy",
            "route_margin": 0.060373544692993164,
            "token": "s",
            "token_class": "identifier",
            "token_total_benefit": -2.569809913635254
          },
          {
            "assigned_benefit": -0.09828927119572957,
            "delta_norm": 7.931220054626465,
            "family": "json_schema",
            "route_margin": 0.2759717106819153,
            "token": " ",
            "token_class": "indentation",
            "token_total_benefit": -2.3589425086975098
          },
          {
            "assigned_benefit": -0.0889308750629425,
            "delta_norm": 6.571300029754639,
            "family": "broad_lm",
            "route_margin": 0.2394627332687378,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -2.13434100151062
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.4434954325358073,
            "delta_norm": 9.388772010803223,
            "family": "json_schema",
            "route_margin": 0.0019948482513427734,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.643890380859375
          },
          {
            "assigned_benefit": 0.40491771697998047,
            "delta_norm": 7.510921478271484,
            "family": "json_schema",
            "route_margin": 0.6601836681365967,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.718025207519531
          },
          {
            "assigned_benefit": 0.3949778874715169,
            "delta_norm": 9.105159759521484,
            "family": "json_schema",
            "route_margin": 0.05875992774963379,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.479469299316406
          },
          {
            "assigned_benefit": 0.38860607147216797,
            "delta_norm": 9.125486373901367,
            "family": "json_schema",
            "route_margin": 0.06904208660125732,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.326545715332031
          },
          {
            "assigned_benefit": 0.38800891240437824,
            "delta_norm": 7.711520195007324,
            "family": "code_heavy",
            "route_margin": 0.26543647050857544,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.312213897705078
          },
          {
            "assigned_benefit": 0.36769771575927734,
            "delta_norm": 7.860241413116455,
            "family": "code_heavy",
            "route_margin": 0.5040015578269958,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 8.824745178222656
          },
          {
            "assigned_benefit": 0.3538846969604492,
            "delta_norm": 8.877388954162598,
            "family": "json_schema",
            "route_margin": 0.3013976216316223,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 8.493232727050781
          },
          {
            "assigned_benefit": 0.3502950270970662,
            "delta_norm": 6.549068927764893,
            "family": "json_schema",
            "route_margin": 0.40201836824417114,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.40708065032959
          }
        ],
        "total_assigned_benefit": 37.721215864488215
      },
      "layer_0_expert_7": {
        "activation_count": 551,
        "mean_assigned_benefit": 0.06091699936738117,
        "mean_delta_norm": 7.854702117006056,
        "mean_harm": -0.030927706192168142,
        "mean_positive_benefit": 0.10259850162659617,
        "mean_route_margin": 0.2985894305465875,
        "positive_benefit_rate": 0.6878402903811253,
        "prose_benefit": 10.886728672015424,
        "structured_benefit": 23.0574154205151,
        "structured_prose_benefit_ratio": 2.1179379146083335,
        "token_class_benefit": {
          "brace_bracket_paren": 2.175691709232827,
          "comma_colon_semicolon": 1.5890981902678807,
          "function_signature": 0.6729390720526377,
          "identifier": 4.725631545608241,
          "indentation": -0.32168459271391237,
          "json_key": 1.4717669337987898,
          "json_value": 1.4137490279972553,
          "newline": 4.984137619550286,
          "number": 0.10793379942576091,
          "operator": 0.3424391349156698,
          "other": 1.4607781867186231,
          "prose_word": 11.961373801032696,
          "quote": 4.0715179443359375,
          "space": -2.592616164125502,
          "string_literal": 1.502510443329811
        },
        "token_class_counts": {
          "brace_bracket_paren": 9,
          "comma_colon_semicolon": 18,
          "function_signature": 7,
          "identifier": 88,
          "indentation": 22,
          "json_key": 27,
          "json_value": 26,
          "newline": 21,
          "number": 1,
          "operator": 2,
          "other": 15,
          "prose_word": 196,
          "quote": 13,
          "space": 87,
          "string_literal": 19
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.13103054463863373,
            "delta_norm": 8.181652069091797,
            "family": "code_heavy",
            "route_margin": 0.03594017028808594,
            "token": "g",
            "token_class": "identifier",
            "token_total_benefit": -3.1447330713272095
          },
          {
            "assigned_benefit": -0.11034655446807544,
            "delta_norm": 8.407752990722656,
            "family": "code_heavy",
            "route_margin": 0.6465549468994141,
            "token": "o",
            "token_class": "identifier",
            "token_total_benefit": -2.6483173072338104
          },
          {
            "assigned_benefit": -0.10870074232419331,
            "delta_norm": 8.175882339477539,
            "family": "broad_lm",
            "route_margin": 0.08901679515838623,
            "token": "o",
            "token_class": "prose_word",
            "token_total_benefit": -2.6088178157806396
          },
          {
            "assigned_benefit": -0.10804811120033264,
            "delta_norm": 9.730475425720215,
            "family": "broad_lm",
            "route_margin": 0.11124414205551147,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -2.5931546688079834
          },
          {
            "assigned_benefit": -0.09698358178138733,
            "delta_norm": 6.55478048324585,
            "family": "broad_lm",
            "route_margin": 0.3801255524158478,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -2.327605962753296
          },
          {
            "assigned_benefit": -0.09626823663711548,
            "delta_norm": 8.500661849975586,
            "family": "broad_lm",
            "route_margin": 0.20438790321350098,
            "token": "o",
            "token_class": "prose_word",
            "token_total_benefit": -2.3104376792907715
          },
          {
            "assigned_benefit": -0.08985122044881184,
            "delta_norm": 6.043436527252197,
            "family": "broad_lm",
            "route_margin": 0.1599215865135193,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -2.1564292907714844
          },
          {
            "assigned_benefit": -0.08971371750036876,
            "delta_norm": 7.55438756942749,
            "family": "code_heavy",
            "route_margin": 0.006203055381774902,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -2.15312922000885
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.4192720651626587,
            "delta_norm": 8.982650756835938,
            "family": "code_heavy",
            "route_margin": 0.4619027376174927,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 10.062529563903809
          },
          {
            "assigned_benefit": 0.36609824498494464,
            "delta_norm": 7.825514316558838,
            "family": "code_heavy",
            "route_margin": 0.032878100872039795,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.786357879638672
          },
          {
            "assigned_benefit": 0.36562061309814453,
            "delta_norm": 6.45040225982666,
            "family": "json_schema",
            "route_margin": 0.3116372227668762,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 8.774894714355469
          },
          {
            "assigned_benefit": 0.3641868432362874,
            "delta_norm": 6.6631598472595215,
            "family": "code_heavy",
            "route_margin": 0.2454327940940857,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.740484237670898
          },
          {
            "assigned_benefit": 0.36353103319803876,
            "delta_norm": 7.397541522979736,
            "family": "code_heavy",
            "route_margin": 0.38832956552505493,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.72474479675293
          },
          {
            "assigned_benefit": 0.34815677007039386,
            "delta_norm": 6.753309726715088,
            "family": "code_heavy",
            "route_margin": 0.5917806029319763,
            "token": "'",
            "token_class": "quote",
            "token_total_benefit": 8.355762481689453
          },
          {
            "assigned_benefit": 0.3460699717203776,
            "delta_norm": 7.994667053222656,
            "family": "json_schema",
            "route_margin": 0.0458981990814209,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 8.305679321289062
          },
          {
            "assigned_benefit": 0.32812609275182086,
            "delta_norm": 7.347655773162842,
            "family": "json_schema",
            "route_margin": 0.0010985136032104492,
            "token": "\\n",
            "token_class": "newline",
            "token_total_benefit": 7.875026226043701
          }
        ],
        "total_assigned_benefit": 33.565266651427024
      },
      "layer_10_expert_3": {
        "activation_count": 2444,
        "mean_assigned_benefit": 0.042826877054222376,
        "mean_delta_norm": 7.821532010446789,
        "mean_harm": -0.0182625762458445,
        "mean_positive_benefit": 0.09694006562557776,
        "mean_route_margin": 0.15137204703449617,
        "positive_benefit_rate": 0.530278232405892,
        "prose_benefit": 6.5630657700821375,
        "structured_benefit": 91.74128489382564,
        "structured_prose_benefit_ratio": 13.9784192491305,
        "token_class_benefit": {
          "brace_bracket_paren": 9.809839007755121,
          "comma_colon_semicolon": 5.2030867735544835,
          "function_signature": 5.996179568270843,
          "identifier": 14.429144063964477,
          "indentation": -7.525266955140981,
          "json_key": 6.940249681472777,
          "json_value": 5.281054059664407,
          "newline": 4.384839708606402,
          "number": 5.180017193158468,
          "operator": 2.9478463729222613,
          "other": 7.827472077993057,
          "prose_word": 17.65430957094456,
          "quote": 29.350831826527905,
          "space": -5.0289120671028895,
          "string_literal": 2.218196637928486
        },
        "token_class_counts": {
          "brace_bracket_paren": 60,
          "comma_colon_semicolon": 56,
          "function_signature": 51,
          "identifier": 339,
          "indentation": 788,
          "json_key": 81,
          "json_value": 86,
          "newline": 21,
          "number": 32,
          "operator": 15,
          "other": 32,
          "prose_word": 442,
          "quote": 98,
          "space": 307,
          "string_literal": 36
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.11696084340413411,
            "delta_norm": 7.933488368988037,
            "family": "json_schema",
            "route_margin": 0.0598982572555542,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.8070602416992188
          },
          {
            "assigned_benefit": -0.11042344570159912,
            "delta_norm": 7.877246379852295,
            "family": "json_schema",
            "route_margin": 0.12033820152282715,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.650162696838379
          },
          {
            "assigned_benefit": -0.10809943079948425,
            "delta_norm": 7.646514892578125,
            "family": "json_schema",
            "route_margin": 0.01335209608078003,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.594386339187622
          },
          {
            "assigned_benefit": -0.10397198796272278,
            "delta_norm": 7.894042015075684,
            "family": "json_schema",
            "route_margin": 0.09459376335144043,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.4953277111053467
          },
          {
            "assigned_benefit": -0.10388837258021037,
            "delta_norm": 7.6007843017578125,
            "family": "code_heavy",
            "route_margin": 0.1739133596420288,
            "token": "d",
            "token_class": "string_literal",
            "token_total_benefit": -2.493320941925049
          },
          {
            "assigned_benefit": -0.10358279943466187,
            "delta_norm": 7.908493995666504,
            "family": "json_schema",
            "route_margin": 0.4173526167869568,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.4859871864318848
          },
          {
            "assigned_benefit": -0.10029297073682149,
            "delta_norm": 8.006976127624512,
            "family": "json_schema",
            "route_margin": 0.09475255012512207,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.407031297683716
          },
          {
            "assigned_benefit": -0.09623692433039348,
            "delta_norm": 7.981371879577637,
            "family": "json_schema",
            "route_margin": 0.061171650886535645,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.3096861839294434
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.42559146881103516,
            "delta_norm": 8.216680526733398,
            "family": "json_schema",
            "route_margin": 0.03258013725280762,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.214195251464844
          },
          {
            "assigned_benefit": 0.3999309539794922,
            "delta_norm": 8.084942817687988,
            "family": "json_schema",
            "route_margin": 0.10884690284729004,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.598342895507812
          },
          {
            "assigned_benefit": 0.3995812733968099,
            "delta_norm": 8.123564720153809,
            "family": "json_schema",
            "route_margin": 0.02567744255065918,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.589950561523438
          },
          {
            "assigned_benefit": 0.38709576924641925,
            "delta_norm": 8.151815414428711,
            "family": "code_heavy",
            "route_margin": 0.15109437704086304,
            "token": "\\",
            "token_class": "function_signature",
            "token_total_benefit": 9.290298461914062
          },
          {
            "assigned_benefit": 0.38402652740478516,
            "delta_norm": 7.830479621887207,
            "family": "code_heavy",
            "route_margin": 0.05510586500167847,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 9.216636657714844
          },
          {
            "assigned_benefit": 0.38011709849039715,
            "delta_norm": 8.000295639038086,
            "family": "json_schema",
            "route_margin": 0.03320908546447754,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.122810363769531
          },
          {
            "assigned_benefit": 0.3677576382954915,
            "delta_norm": 7.7138991355896,
            "family": "code_heavy",
            "route_margin": 0.12689030170440674,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.826183319091797
          },
          {
            "assigned_benefit": 0.3641868432362874,
            "delta_norm": 7.657344341278076,
            "family": "code_heavy",
            "route_margin": 0.22139650583267212,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.740484237670898
          }
        ],
        "total_assigned_benefit": 104.66888752051949
      },
      "layer_10_expert_4": {
        "activation_count": 7,
        "mean_assigned_benefit": 8.053514396860502e-05,
        "mean_delta_norm": 7.951243196214948,
        "mean_harm": -0.01811086751210193,
        "mean_positive_benefit": 0.024335738685395986,
        "mean_route_margin": 0.05446946620941162,
        "positive_benefit_rate": 0.42857142857142855,
        "prose_benefit": 0.013573671691119671,
        "structured_benefit": -0.013009925683339437,
        "structured_prose_benefit_ratio": -0.9584676850443455,
        "token_class_benefit": {
          "json_key": -0.02198214332262675,
          "json_value": 0.008972217639287313,
          "prose_word": -0.008263428695499897,
          "space": 0.02183710038661957
        },
        "token_class_counts": {
          "json_key": 1,
          "json_value": 1,
          "prose_word": 1,
          "space": 4
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.03931535283724467,
            "delta_norm": 7.974234580993652,
            "family": "code_heavy",
            "route_margin": 0.03739732503890991,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -0.9435684680938721
          },
          {
            "assigned_benefit": -0.02198214332262675,
            "delta_norm": 8.096039772033691,
            "family": "json_schema",
            "route_margin": 0.09502041339874268,
            "token": "o",
            "token_class": "json_key",
            "token_total_benefit": -0.527571439743042
          },
          {
            "assigned_benefit": -0.008263428695499897,
            "delta_norm": 8.228636741638184,
            "family": "broad_lm",
            "route_margin": 0.06418639421463013,
            "token": "e",
            "token_class": "prose_word",
            "token_total_benefit": -0.19832228869199753
          },
          {
            "assigned_benefit": -0.0028825451930363974,
            "delta_norm": 7.801119804382324,
            "family": "code_heavy",
            "route_margin": 0.02399003505706787,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -0.06918108463287354
          },
          {
            "assigned_benefit": 0.008972217639287313,
            "delta_norm": 7.746042728424072,
            "family": "json_schema",
            "route_margin": 0.029181182384490967,
            "token": "e",
            "token_class": "json_value",
            "token_total_benefit": 0.2153332233428955
          },
          {
            "assigned_benefit": 0.030975282192230225,
            "delta_norm": 8.022831916809082,
            "family": "code_heavy",
            "route_margin": 0.017046213150024414,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": 0.7434067726135254
          },
          {
            "assigned_benefit": 0.03305971622467041,
            "delta_norm": 7.789796829223633,
            "family": "json_schema",
            "route_margin": 0.11446470022201538,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": 0.7934331893920898
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.03305971622467041,
            "delta_norm": 7.789796829223633,
            "family": "json_schema",
            "route_margin": 0.11446470022201538,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": 0.7934331893920898
          },
          {
            "assigned_benefit": 0.030975282192230225,
            "delta_norm": 8.022831916809082,
            "family": "code_heavy",
            "route_margin": 0.017046213150024414,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": 0.7434067726135254
          },
          {
            "assigned_benefit": 0.008972217639287313,
            "delta_norm": 7.746042728424072,
            "family": "json_schema",
            "route_margin": 0.029181182384490967,
            "token": "e",
            "token_class": "json_value",
            "token_total_benefit": 0.2153332233428955
          },
          {
            "assigned_benefit": -0.0028825451930363974,
            "delta_norm": 7.801119804382324,
            "family": "code_heavy",
            "route_margin": 0.02399003505706787,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -0.06918108463287354
          },
          {
            "assigned_benefit": -0.008263428695499897,
            "delta_norm": 8.228636741638184,
            "family": "broad_lm",
            "route_margin": 0.06418639421463013,
            "token": "e",
            "token_class": "prose_word",
            "token_total_benefit": -0.19832228869199753
          },
          {
            "assigned_benefit": -0.02198214332262675,
            "delta_norm": 8.096039772033691,
            "family": "json_schema",
            "route_margin": 0.09502041339874268,
            "token": "o",
            "token_class": "json_key",
            "token_total_benefit": -0.527571439743042
          },
          {
            "assigned_benefit": -0.03931535283724467,
            "delta_norm": 7.974234580993652,
            "family": "code_heavy",
            "route_margin": 0.03739732503890991,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -0.9435684680938721
          }
        ],
        "total_assigned_benefit": 0.0005637460077802352
      },
      "layer_10_expert_6": {
        "activation_count": 3693,
        "mean_assigned_benefit": 0.06106276104274314,
        "mean_delta_norm": 12.687390645861528,
        "mean_harm": -0.03198150449663866,
        "mean_positive_benefit": 0.09837224081327664,
        "mean_route_margin": 0.2481988562725438,
        "positive_benefit_rate": 0.7137828323855944,
        "prose_benefit": 50.12793561454285,
        "structured_benefit": 166.70204735040792,
        "structured_prose_benefit_ratio": 3.325531867744524,
        "token_class_benefit": {
          "brace_bracket_paren": 12.634745193334917,
          "comma_colon_semicolon": 11.212934210896494,
          "function_signature": 7.17058119922876,
          "identifier": 41.10890514341497,
          "indentation": -3.5164029048755756,
          "json_key": 10.031666077673435,
          "json_value": 5.895012723747636,
          "newline": 21.337782641619185,
          "number": 4.396523714065552,
          "operator": 5.1294536987940464,
          "other": 18.789414611771768,
          "prose_word": 58.70673533140985,
          "quote": 34.13637733459472,
          "space": -15.177017857863882,
          "string_literal": 13.648065413037934
        },
        "token_class_counts": {
          "brace_bracket_paren": 62,
          "comma_colon_semicolon": 117,
          "function_signature": 64,
          "identifier": 756,
          "indentation": 121,
          "json_key": 135,
          "json_value": 127,
          "newline": 116,
          "number": 39,
          "operator": 30,
          "other": 90,
          "prose_word": 1153,
          "quote": 106,
          "space": 617,
          "string_literal": 160
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.17974231019616127,
            "delta_norm": 13.150712013244629,
            "family": "broad_lm",
            "route_margin": 0.22599589824676514,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -4.3138154447078705
          },
          {
            "assigned_benefit": -0.14390301704406738,
            "delta_norm": 12.516654968261719,
            "family": "json_schema",
            "route_margin": 0.725058913230896,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -3.453672409057617
          },
          {
            "assigned_benefit": -0.14381763339042664,
            "delta_norm": 12.931536674499512,
            "family": "broad_lm",
            "route_margin": 0.1681225299835205,
            "token": "c",
            "token_class": "prose_word",
            "token_total_benefit": -3.4516232013702393
          },
          {
            "assigned_benefit": -0.13103054463863373,
            "delta_norm": 12.849684715270996,
            "family": "code_heavy",
            "route_margin": 0.2905532717704773,
            "token": "g",
            "token_class": "identifier",
            "token_total_benefit": -3.1447330713272095
          },
          {
            "assigned_benefit": -0.12831215063730875,
            "delta_norm": 13.041942596435547,
            "family": "json_schema",
            "route_margin": 0.15699678659439087,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -3.07949161529541
          },
          {
            "assigned_benefit": -0.1258842075864474,
            "delta_norm": 12.363566398620605,
            "family": "broad_lm",
            "route_margin": 0.20470917224884033,
            "token": "m",
            "token_class": "prose_word",
            "token_total_benefit": -3.0212209820747375
          },
          {
            "assigned_benefit": -0.12130660812060039,
            "delta_norm": 13.058923721313477,
            "family": "json_schema",
            "route_margin": 0.0958135724067688,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.911358594894409
          },
          {
            "assigned_benefit": -0.11974493662516277,
            "delta_norm": 12.86640453338623,
            "family": "code_heavy",
            "route_margin": 0.19338339567184448,
            "token": "5",
            "token_class": "number",
            "token_total_benefit": -2.8738784790039062
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.4434954325358073,
            "delta_norm": 13.236690521240234,
            "family": "json_schema",
            "route_margin": 0.2555248737335205,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.643890380859375
          },
          {
            "assigned_benefit": 0.4348748524983724,
            "delta_norm": 13.131726264953613,
            "family": "json_schema",
            "route_margin": 0.22252517938613892,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.436996459960938
          },
          {
            "assigned_benefit": 0.4194428126017253,
            "delta_norm": 13.026664733886719,
            "family": "json_schema",
            "route_margin": 0.3824976682662964,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.066627502441406
          },
          {
            "assigned_benefit": 0.4192720651626587,
            "delta_norm": 12.482946395874023,
            "family": "code_heavy",
            "route_margin": 0.39147496223449707,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 10.062529563903809
          },
          {
            "assigned_benefit": 0.41413907210032147,
            "delta_norm": 12.731311798095703,
            "family": "code_heavy",
            "route_margin": 0.014028489589691162,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.939337730407715
          },
          {
            "assigned_benefit": 0.40491771697998047,
            "delta_norm": 12.744100570678711,
            "family": "json_schema",
            "route_margin": 0.1953127384185791,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.718025207519531
          },
          {
            "assigned_benefit": 0.40347035725911456,
            "delta_norm": 12.574848175048828,
            "family": "json_schema",
            "route_margin": 0.06692469120025635,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.68328857421875
          },
          {
            "assigned_benefit": 0.40207378069559735,
            "delta_norm": 12.622760772705078,
            "family": "code_heavy",
            "route_margin": 0.18480181694030762,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.649770736694336
          }
        ],
        "total_assigned_benefit": 225.50477653085042
      },
      "layer_11_expert_5": {
        "activation_count": 741,
        "mean_assigned_benefit": 0.035694548435797446,
        "mean_delta_norm": 8.773809405956191,
        "mean_harm": -0.019944378732042935,
        "mean_positive_benefit": 0.0857695828868538,
        "mean_route_margin": 0.07070732333882135,
        "positive_benefit_rate": 0.5263157894736842,
        "prose_benefit": 5.744563460660476,
        "structured_benefit": 18.95048379898072,
        "structured_prose_benefit_ratio": 3.2988553314374744,
        "token_class_benefit": {
          "brace_bracket_paren": 3.225802520910899,
          "comma_colon_semicolon": 0.19332072138786316,
          "identifier": 4.5494231283664694,
          "indentation": -2.5173419797793026,
          "json_key": 0.7731653650601706,
          "json_value": 0.1995814641316732,
          "newline": 1.0555922587712605,
          "number": 1.723741412162781,
          "operator": 0.9045544862747191,
          "other": 2.115232209364573,
          "prose_word": 9.760870556036627,
          "quote": 6.209345817565919,
          "space": -1.85958419367671,
          "string_literal": 0.11595662434895831
        },
        "token_class_counts": {
          "brace_bracket_paren": 19,
          "comma_colon_semicolon": 5,
          "identifier": 93,
          "indentation": 241,
          "json_key": 10,
          "json_value": 3,
          "newline": 6,
          "number": 12,
          "operator": 5,
          "other": 10,
          "prose_word": 253,
          "quote": 21,
          "space": 56,
          "string_literal": 7
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.1018477330605189,
            "delta_norm": 8.812163352966309,
            "family": "broad_lm",
            "route_margin": 0.06189072132110596,
            "token": " ",
            "token_class": "indentation",
            "token_total_benefit": -2.4443455934524536
          },
          {
            "assigned_benefit": -0.09179036815961202,
            "delta_norm": 8.805045127868652,
            "family": "broad_lm",
            "route_margin": 0.12053346633911133,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -2.2029688358306885
          },
          {
            "assigned_benefit": -0.0889308750629425,
            "delta_norm": 8.839122772216797,
            "family": "broad_lm",
            "route_margin": 0.003485441207885742,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -2.13434100151062
          },
          {
            "assigned_benefit": -0.08728645245234172,
            "delta_norm": 8.756814956665039,
            "family": "broad_lm",
            "route_margin": 0.011687517166137695,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -2.094874858856201
          },
          {
            "assigned_benefit": -0.08514145016670227,
            "delta_norm": 8.864501953125,
            "family": "broad_lm",
            "route_margin": 0.0055429935455322266,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -2.0433948040008545
          },
          {
            "assigned_benefit": -0.08080403010050456,
            "delta_norm": 8.788704872131348,
            "family": "code_heavy",
            "route_margin": 0.004049897193908691,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -1.9392967224121094
          },
          {
            "assigned_benefit": -0.07918460418780644,
            "delta_norm": 8.94941520690918,
            "family": "json_schema",
            "route_margin": 0.050701022148132324,
            "token": " ",
            "token_class": "indentation",
            "token_total_benefit": -1.9004305005073547
          },
          {
            "assigned_benefit": -0.07488320767879486,
            "delta_norm": 8.695552825927734,
            "family": "broad_lm",
            "route_margin": 0.028115272521972656,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -1.7971969842910767
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.34745808442433673,
            "delta_norm": 8.76328182220459,
            "family": "code_heavy",
            "route_margin": 0.12404882907867432,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.338994026184082
          },
          {
            "assigned_benefit": 0.3468109766642253,
            "delta_norm": 8.782177925109863,
            "family": "code_heavy",
            "route_margin": 0.05542933940887451,
            "token": "'",
            "token_class": "quote",
            "token_total_benefit": 8.323463439941406
          },
          {
            "assigned_benefit": 0.34638198216756183,
            "delta_norm": 8.626164436340332,
            "family": "code_heavy",
            "route_margin": 0.024620890617370605,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.313167572021484
          },
          {
            "assigned_benefit": 0.3197021484375,
            "delta_norm": 8.823670387268066,
            "family": "json_schema",
            "route_margin": 0.07156145572662354,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 7.6728515625
          },
          {
            "assigned_benefit": 0.3188056945800781,
            "delta_norm": 8.791345596313477,
            "family": "json_schema",
            "route_margin": 0.009918570518493652,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 7.651336669921875
          },
          {
            "assigned_benefit": 0.3152503967285156,
            "delta_norm": 8.787659645080566,
            "family": "json_schema",
            "route_margin": 0.032335638999938965,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 7.566009521484375
          },
          {
            "assigned_benefit": 0.3146959940592448,
            "delta_norm": 8.716227531433105,
            "family": "code_heavy",
            "route_margin": 0.09483158588409424,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 7.552703857421875
          },
          {
            "assigned_benefit": 0.30885366598765057,
            "delta_norm": 8.537050247192383,
            "family": "code_heavy",
            "route_margin": 0.15049517154693604,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 7.412487983703613
          }
        ],
        "total_assigned_benefit": 26.449660390925906
      },
      "layer_11_expert_7": {
        "activation_count": 5403,
        "mean_assigned_benefit": 0.05621406022699439,
        "mean_delta_norm": 12.701623230714743,
        "mean_harm": -0.025749114272485416,
        "mean_positive_benefit": 0.0991724743934356,
        "mean_route_margin": 0.2598608736746536,
        "positive_benefit_rate": 0.6561169720525634,
        "prose_benefit": 50.960011595655814,
        "structured_benefit": 239.47983851956957,
        "structured_prose_benefit_ratio": 4.699367818432453,
        "token_class_benefit": {
          "brace_bracket_paren": 19.218781680179138,
          "comma_colon_semicolon": 16.222700263063114,
          "function_signature": 13.16676076749961,
          "identifier": 50.988626079013,
          "indentation": -8.524327880237246,
          "json_key": 16.176768250763416,
          "json_value": 10.985457536919673,
          "newline": 24.66703009145432,
          "number": 7.852799495061238,
          "operator": 7.172745585441589,
          "other": 24.501654480400244,
          "prose_word": 66.59191091762236,
          "quote": 57.27786334355675,
          "space": -18.32450863090347,
          "string_literal": 15.75030542661746
        },
        "token_class_counts": {
          "brace_bracket_paren": 103,
          "comma_colon_semicolon": 168,
          "function_signature": 115,
          "identifier": 1002,
          "indentation": 668,
          "json_key": 207,
          "json_value": 211,
          "newline": 131,
          "number": 59,
          "operator": 40,
          "other": 112,
          "prose_word": 1343,
          "quote": 183,
          "space": 872,
          "string_literal": 189
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.17974231019616127,
            "delta_norm": 12.893712043762207,
            "family": "broad_lm",
            "route_margin": 0.3393423557281494,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -4.3138154447078705
          },
          {
            "assigned_benefit": -0.14390301704406738,
            "delta_norm": 12.777634620666504,
            "family": "json_schema",
            "route_margin": 0.44136732816696167,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -3.453672409057617
          },
          {
            "assigned_benefit": -0.14381763339042664,
            "delta_norm": 12.850318908691406,
            "family": "broad_lm",
            "route_margin": 0.39602017402648926,
            "token": "c",
            "token_class": "prose_word",
            "token_total_benefit": -3.4516232013702393
          },
          {
            "assigned_benefit": -0.13103054463863373,
            "delta_norm": 12.936612129211426,
            "family": "code_heavy",
            "route_margin": 0.36134541034698486,
            "token": "g",
            "token_class": "identifier",
            "token_total_benefit": -3.1447330713272095
          },
          {
            "assigned_benefit": -0.12831215063730875,
            "delta_norm": 12.862449645996094,
            "family": "json_schema",
            "route_margin": 0.6156917214393616,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -3.07949161529541
          },
          {
            "assigned_benefit": -0.1258842075864474,
            "delta_norm": 12.744318008422852,
            "family": "broad_lm",
            "route_margin": 0.29752057790756226,
            "token": "m",
            "token_class": "prose_word",
            "token_total_benefit": -3.0212209820747375
          },
          {
            "assigned_benefit": -0.12130660812060039,
            "delta_norm": 12.878005027770996,
            "family": "json_schema",
            "route_margin": 0.4906848669052124,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.911358594894409
          },
          {
            "assigned_benefit": -0.11974493662516277,
            "delta_norm": 12.653632164001465,
            "family": "code_heavy",
            "route_margin": 0.48839086294174194,
            "token": "5",
            "token_class": "number",
            "token_total_benefit": -2.8738784790039062
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.4434954325358073,
            "delta_norm": 12.9307279586792,
            "family": "json_schema",
            "route_margin": 0.38366442918777466,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.643890380859375
          },
          {
            "assigned_benefit": 0.4348748524983724,
            "delta_norm": 12.863738059997559,
            "family": "json_schema",
            "route_margin": 0.2991443872451782,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.436996459960938
          },
          {
            "assigned_benefit": 0.42559146881103516,
            "delta_norm": 12.8611421585083,
            "family": "json_schema",
            "route_margin": 0.3129814863204956,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.214195251464844
          },
          {
            "assigned_benefit": 0.4194428126017253,
            "delta_norm": 12.947617530822754,
            "family": "json_schema",
            "route_margin": 0.5175976753234863,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.066627502441406
          },
          {
            "assigned_benefit": 0.4192720651626587,
            "delta_norm": 12.794495582580566,
            "family": "code_heavy",
            "route_margin": 0.34432709217071533,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 10.062529563903809
          },
          {
            "assigned_benefit": 0.41413907210032147,
            "delta_norm": 12.645398139953613,
            "family": "code_heavy",
            "route_margin": 0.174493670463562,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.939337730407715
          },
          {
            "assigned_benefit": 0.40491771697998047,
            "delta_norm": 12.924742698669434,
            "family": "json_schema",
            "route_margin": 0.35488104820251465,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.718025207519531
          },
          {
            "assigned_benefit": 0.40347035725911456,
            "delta_norm": 12.479201316833496,
            "family": "json_schema",
            "route_margin": 0.3610612154006958,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.68328857421875
          }
        ],
        "total_assigned_benefit": 303.7245674064507
      },
      "layer_12_expert_0": {
        "activation_count": 6117,
        "mean_assigned_benefit": 0.053653873571155,
        "mean_delta_norm": 18.093502148199025,
        "mean_harm": -0.024751094881976105,
        "mean_positive_benefit": 0.09775291329881644,
        "mean_route_margin": 0.3660807834159554,
        "positive_benefit_rate": 0.640019617459539,
        "prose_benefit": 56.15695059496332,
        "structured_benefit": 257.0044636172816,
        "structured_prose_benefit_ratio": 4.576538805871916,
        "token_class_benefit": {
          "brace_bracket_paren": 22.444584201090027,
          "comma_colon_semicolon": 16.416020984450974,
          "function_signature": 13.16676076749961,
          "identifier": 54.823879819363405,
          "indentation": -11.041669860016562,
          "json_key": 16.94993361582359,
          "json_value": 11.185039001051349,
          "newline": 25.72262235022558,
          "number": 9.57654090722402,
          "operator": 8.07730007171631,
          "other": 26.445376887423354,
          "prose_word": 75.99146793192878,
          "quote": 62.77551984786991,
          "space": -20.198893941861296,
          "string_literal": 15.866262050966418
        },
        "token_class_counts": {
          "brace_bracket_paren": 122,
          "comma_colon_semicolon": 173,
          "function_signature": 115,
          "identifier": 1082,
          "indentation": 909,
          "json_key": 217,
          "json_value": 214,
          "newline": 137,
          "number": 71,
          "operator": 45,
          "other": 121,
          "prose_word": 1588,
          "quote": 202,
          "space": 925,
          "string_literal": 196
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.17974231019616127,
            "delta_norm": 18.066368103027344,
            "family": "broad_lm",
            "route_margin": 0.24349337816238403,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -4.3138154447078705
          },
          {
            "assigned_benefit": -0.14390301704406738,
            "delta_norm": 18.26600456237793,
            "family": "json_schema",
            "route_margin": 0.4235943555831909,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -3.453672409057617
          },
          {
            "assigned_benefit": -0.14381763339042664,
            "delta_norm": 18.070985794067383,
            "family": "broad_lm",
            "route_margin": 0.18828749656677246,
            "token": "c",
            "token_class": "prose_word",
            "token_total_benefit": -3.4516232013702393
          },
          {
            "assigned_benefit": -0.13103054463863373,
            "delta_norm": 18.06113624572754,
            "family": "code_heavy",
            "route_margin": 0.35212522745132446,
            "token": "g",
            "token_class": "identifier",
            "token_total_benefit": -3.1447330713272095
          },
          {
            "assigned_benefit": -0.12831215063730875,
            "delta_norm": 18.183197021484375,
            "family": "json_schema",
            "route_margin": 0.4698083996772766,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -3.07949161529541
          },
          {
            "assigned_benefit": -0.1258842075864474,
            "delta_norm": 18.27066993713379,
            "family": "broad_lm",
            "route_margin": 0.20243817567825317,
            "token": "m",
            "token_class": "prose_word",
            "token_total_benefit": -3.0212209820747375
          },
          {
            "assigned_benefit": -0.12130660812060039,
            "delta_norm": 18.00044822692871,
            "family": "json_schema",
            "route_margin": 0.35750818252563477,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.911358594894409
          },
          {
            "assigned_benefit": -0.11974493662516277,
            "delta_norm": 18.19757652282715,
            "family": "code_heavy",
            "route_margin": 0.3124940097332001,
            "token": "5",
            "token_class": "number",
            "token_total_benefit": -2.8738784790039062
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.4434954325358073,
            "delta_norm": 18.0870304107666,
            "family": "json_schema",
            "route_margin": 0.35745885968208313,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.643890380859375
          },
          {
            "assigned_benefit": 0.4348748524983724,
            "delta_norm": 18.03725814819336,
            "family": "json_schema",
            "route_margin": 0.5126282572746277,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.436996459960938
          },
          {
            "assigned_benefit": 0.42559146881103516,
            "delta_norm": 17.872426986694336,
            "family": "json_schema",
            "route_margin": 0.25519827008247375,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.214195251464844
          },
          {
            "assigned_benefit": 0.4194428126017253,
            "delta_norm": 18.201580047607422,
            "family": "json_schema",
            "route_margin": 0.3604685068130493,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.066627502441406
          },
          {
            "assigned_benefit": 0.4192720651626587,
            "delta_norm": 17.989830017089844,
            "family": "code_heavy",
            "route_margin": 0.3905385136604309,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 10.062529563903809
          },
          {
            "assigned_benefit": 0.41413907210032147,
            "delta_norm": 18.22857093811035,
            "family": "code_heavy",
            "route_margin": 0.22223444283008575,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.939337730407715
          },
          {
            "assigned_benefit": 0.40491771697998047,
            "delta_norm": 18.235313415527344,
            "family": "json_schema",
            "route_margin": 0.34051084518432617,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.718025207519531
          },
          {
            "assigned_benefit": 0.40347035725911456,
            "delta_norm": 18.30887794494629,
            "family": "json_schema",
            "route_margin": 0.4147983491420746,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.68328857421875
          }
        ],
        "total_assigned_benefit": 328.20074463475515
      },
      "layer_12_expert_6": {
        "activation_count": 27,
        "mean_assigned_benefit": 0.0730919689859873,
        "mean_delta_norm": 10.966682045548051,
        "mean_harm": -0.048631474730514344,
        "mean_positive_benefit": 0.11569517428676288,
        "mean_route_margin": 0.07106303947943228,
        "positive_benefit_rate": 0.7407407407407407,
        "prose_benefit": 0.5476244613528252,
        "structured_benefit": 1.4258587012688317,
        "structured_prose_benefit_ratio": 2.603716236025065,
        "token_class_benefit": {
          "identifier": 0.7141693880160649,
          "other": 0.17150980234146118,
          "prose_word": 0.36131354173024494,
          "quote": 0.7116893132527669,
          "space": 0.014801117281119026
        },
        "token_class_counts": {
          "identifier": 13,
          "other": 1,
          "prose_word": 8,
          "quote": 2,
          "space": 3
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.084659809867541,
            "delta_norm": 10.969902992248535,
            "family": "json_schema",
            "route_margin": 0.0032976865768432617,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.031835436820984
          },
          {
            "assigned_benefit": -0.08465861777464549,
            "delta_norm": 10.969903945922852,
            "family": "json_schema",
            "route_margin": 0.0032978355884552,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.0318068265914917
          },
          {
            "assigned_benefit": -0.04810711741447449,
            "delta_norm": 11.13128662109375,
            "family": "broad_lm",
            "route_margin": 0.07421362400054932,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -1.1545708179473877
          },
          {
            "assigned_benefit": -0.04780731598536173,
            "delta_norm": 10.96022891998291,
            "family": "broad_lm",
            "route_margin": 0.07657453417778015,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -1.1473755836486816
          },
          {
            "assigned_benefit": -0.04212679465611776,
            "delta_norm": 11.13128662109375,
            "family": "broad_lm",
            "route_margin": 0.0742136538028717,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.0110430717468262
          },
          {
            "assigned_benefit": -0.024774449567000072,
            "delta_norm": 11.053271293640137,
            "family": "broad_lm",
            "route_margin": 0.04963645339012146,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -0.5945867896080017
          },
          {
            "assigned_benefit": -0.008286217848459879,
            "delta_norm": 10.75226879119873,
            "family": "code_heavy",
            "route_margin": 0.1069648265838623,
            "token": "e",
            "token_class": "identifier",
            "token_total_benefit": -0.1988692283630371
          },
          {
            "assigned_benefit": 0.004752675692240397,
            "delta_norm": 10.99473762512207,
            "family": "json_schema",
            "route_margin": 0.013706356287002563,
            "token": "o",
            "token_class": "identifier",
            "token_total_benefit": 0.11406421661376953
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.35584481557210285,
            "delta_norm": 10.872716903686523,
            "family": "json_schema",
            "route_margin": 0.20911967754364014,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 8.540275573730469
          },
          {
            "assigned_benefit": 0.35584449768066406,
            "delta_norm": 10.872716903686523,
            "family": "json_schema",
            "route_margin": 0.209119975566864,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 8.540267944335938
          },
          {
            "assigned_benefit": 0.19265987475713095,
            "delta_norm": 10.969902038574219,
            "family": "broad_lm",
            "route_margin": 0.003297567367553711,
            "token": "v",
            "token_class": "prose_word",
            "token_total_benefit": 4.623836994171143
          },
          {
            "assigned_benefit": 0.17150980234146118,
            "delta_norm": 11.017438888549805,
            "family": "broad_lm",
            "route_margin": 0.021159827709197998,
            "token": ".",
            "token_class": "other",
            "token_total_benefit": 4.116235256195068
          },
          {
            "assigned_benefit": 0.13202581803003946,
            "delta_norm": 11.032302856445312,
            "family": "code_heavy",
            "route_margin": 0.022380322217941284,
            "token": "a",
            "token_class": "identifier",
            "token_total_benefit": 3.1686196327209473
          },
          {
            "assigned_benefit": 0.12117876609166463,
            "delta_norm": 10.95656967163086,
            "family": "json_schema",
            "route_margin": 0.013000518083572388,
            "token": "c",
            "token_class": "identifier",
            "token_total_benefit": 2.908290386199951
          },
          {
            "assigned_benefit": 0.12040218710899353,
            "delta_norm": 10.96022891998291,
            "family": "code_heavy",
            "route_margin": 0.07657492160797119,
            "token": "r",
            "token_class": "identifier",
            "token_total_benefit": 2.8896524906158447
          },
          {
            "assigned_benefit": 0.12040217717488606,
            "delta_norm": 10.960227966308594,
            "family": "broad_lm",
            "route_margin": 0.07657462358474731,
            "token": "r",
            "token_class": "prose_word",
            "token_total_benefit": 2.8896522521972656
          }
        ],
        "total_assigned_benefit": 1.973483162621657
      },
      "layer_13_expert_2": {
        "activation_count": 5431,
        "mean_assigned_benefit": 0.05211462106243594,
        "mean_delta_norm": 8.910455488627445,
        "mean_harm": -0.02405761078747901,
        "mean_positive_benefit": 0.0978314260943383,
        "mean_route_margin": 0.17763215470925328,
        "positive_benefit_rate": 0.624930951942552,
        "prose_benefit": 41.29931832568678,
        "structured_benefit": 229.22397610220148,
        "structured_prose_benefit_ratio": 5.550308949279483,
        "token_class_benefit": {
          "brace_bracket_paren": 19.884800861589614,
          "comma_colon_semicolon": 13.755876059333483,
          "function_signature": 10.89208460350832,
          "identifier": 45.64474812522534,
          "indentation": -11.041669860016562,
          "json_key": 16.302193122605487,
          "json_value": 10.470739297413584,
          "newline": 24.07321313055561,
          "number": 8.656783898671469,
          "operator": 6.908886810143789,
          "other": 22.46013152402459,
          "prose_word": 58.89047251874581,
          "quote": 60.73281510670983,
          "space": -16.498403294865657,
          "string_literal": 11.901835086445011
        },
        "token_class_counts": {
          "brace_bracket_paren": 110,
          "comma_colon_semicolon": 149,
          "function_signature": 93,
          "identifier": 949,
          "indentation": 909,
          "json_key": 212,
          "json_value": 203,
          "newline": 125,
          "number": 63,
          "operator": 39,
          "other": 105,
          "prose_word": 1315,
          "quote": 195,
          "space": 811,
          "string_literal": 153
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.17974231019616127,
            "delta_norm": 8.987576484680176,
            "family": "broad_lm",
            "route_margin": 0.18856492638587952,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -4.3138154447078705
          },
          {
            "assigned_benefit": -0.14390301704406738,
            "delta_norm": 8.984742164611816,
            "family": "json_schema",
            "route_margin": 0.14763560891151428,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -3.453672409057617
          },
          {
            "assigned_benefit": -0.14381763339042664,
            "delta_norm": 9.000264167785645,
            "family": "broad_lm",
            "route_margin": 0.040781646966934204,
            "token": "c",
            "token_class": "prose_word",
            "token_total_benefit": -3.4516232013702393
          },
          {
            "assigned_benefit": -0.13103054463863373,
            "delta_norm": 8.9207763671875,
            "family": "code_heavy",
            "route_margin": 0.03078332543373108,
            "token": "g",
            "token_class": "identifier",
            "token_total_benefit": -3.1447330713272095
          },
          {
            "assigned_benefit": -0.12831215063730875,
            "delta_norm": 8.71847915649414,
            "family": "json_schema",
            "route_margin": 0.23758503794670105,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -3.07949161529541
          },
          {
            "assigned_benefit": -0.1258842075864474,
            "delta_norm": 8.76350212097168,
            "family": "broad_lm",
            "route_margin": 0.2833724915981293,
            "token": "m",
            "token_class": "prose_word",
            "token_total_benefit": -3.0212209820747375
          },
          {
            "assigned_benefit": -0.12130660812060039,
            "delta_norm": 8.796605110168457,
            "family": "json_schema",
            "route_margin": 0.23237091302871704,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.911358594894409
          },
          {
            "assigned_benefit": -0.11974493662516277,
            "delta_norm": 8.941917419433594,
            "family": "code_heavy",
            "route_margin": 0.07833242416381836,
            "token": "5",
            "token_class": "number",
            "token_total_benefit": -2.8738784790039062
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.4434954325358073,
            "delta_norm": 8.837514877319336,
            "family": "json_schema",
            "route_margin": 0.1730024814605713,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.643890380859375
          },
          {
            "assigned_benefit": 0.4348748524983724,
            "delta_norm": 8.800647735595703,
            "family": "json_schema",
            "route_margin": 0.257057785987854,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.436996459960938
          },
          {
            "assigned_benefit": 0.42559146881103516,
            "delta_norm": 8.863917350769043,
            "family": "json_schema",
            "route_margin": 0.1273263692855835,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.214195251464844
          },
          {
            "assigned_benefit": 0.4194428126017253,
            "delta_norm": 8.917320251464844,
            "family": "json_schema",
            "route_margin": 0.1443253457546234,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.066627502441406
          },
          {
            "assigned_benefit": 0.4192720651626587,
            "delta_norm": 8.975712776184082,
            "family": "code_heavy",
            "route_margin": 0.10680675506591797,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 10.062529563903809
          },
          {
            "assigned_benefit": 0.41413907210032147,
            "delta_norm": 8.963048934936523,
            "family": "code_heavy",
            "route_margin": 0.004436314105987549,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.939337730407715
          },
          {
            "assigned_benefit": 0.40491771697998047,
            "delta_norm": 8.991743087768555,
            "family": "json_schema",
            "route_margin": 0.31273090839385986,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.718025207519531
          },
          {
            "assigned_benefit": 0.40347035725911456,
            "delta_norm": 8.79100227355957,
            "family": "json_schema",
            "route_margin": 0.09125512838363647,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.68328857421875
          }
        ],
        "total_assigned_benefit": 283.0345069900896
      },
      "layer_13_expert_4": {
        "activation_count": 8,
        "mean_assigned_benefit": 0.04804670515780648,
        "mean_delta_norm": 11.989322066307068,
        "mean_harm": -0.011517115351226596,
        "mean_positive_benefit": 0.08378499746322632,
        "mean_route_margin": 0.0147049929946661,
        "positive_benefit_rate": 0.625,
        "prose_benefit": 0.022456547866264984,
        "structured_benefit": 0.36191709339618683,
        "structured_prose_benefit_ratio": 16.11632809955939,
        "token_class_benefit": {
          "function_signature": 0.12267820040384929,
          "identifier": 0.23923889299233753,
          "prose_word": 0.05494506160418193,
          "space": -0.032488513737916946
        },
        "token_class_counts": {
          "function_signature": 1,
          "identifier": 2,
          "prose_word": 3,
          "space": 2
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.019533616801102955,
            "delta_norm": 11.911380767822266,
            "family": "broad_lm",
            "route_margin": 0.01734989881515503,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -0.46880680322647095
          },
          {
            "assigned_benefit": -0.01295489693681399,
            "delta_norm": 11.82947826385498,
            "family": "broad_lm",
            "route_margin": 0.02840632200241089,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -0.31091752648353577
          },
          {
            "assigned_benefit": -0.002062832315762838,
            "delta_norm": 11.968559265136719,
            "family": "broad_lm",
            "route_margin": 0.00042515993118286133,
            "token": "e",
            "token_class": "prose_word",
            "token_total_benefit": -0.049507975578308105
          },
          {
            "assigned_benefit": 0.005513812104860942,
            "delta_norm": 12.128469467163086,
            "family": "broad_lm",
            "route_margin": 0.0005263984203338623,
            "token": "n",
            "token_class": "prose_word",
            "token_total_benefit": 0.1323314905166626
          },
          {
            "assigned_benefit": 0.051494081815083824,
            "delta_norm": 11.904205322265625,
            "family": "broad_lm",
            "route_margin": 0.0008758902549743652,
            "token": "n",
            "token_class": "prose_word",
            "token_total_benefit": 1.2358579635620117
          },
          {
            "assigned_benefit": 0.05997603634993235,
            "delta_norm": 11.941676139831543,
            "family": "code_heavy",
            "route_margin": 0.033836498856544495,
            "token": "n",
            "token_class": "identifier",
            "token_total_benefit": 1.4394248723983765
          },
          {
            "assigned_benefit": 0.12267820040384929,
            "delta_norm": 11.968559265136719,
            "family": "code_heavy",
            "route_margin": 0.000425487756729126,
            "token": "p",
            "token_class": "function_signature",
            "token_total_benefit": 2.944276809692383
          },
          {
            "assigned_benefit": 0.17926285664240518,
            "delta_norm": 12.262248039245605,
            "family": "code_heavy",
            "route_margin": 0.03579428791999817,
            "token": "f",
            "token_class": "identifier",
            "token_total_benefit": 4.302308559417725
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.17926285664240518,
            "delta_norm": 12.262248039245605,
            "family": "code_heavy",
            "route_margin": 0.03579428791999817,
            "token": "f",
            "token_class": "identifier",
            "token_total_benefit": 4.302308559417725
          },
          {
            "assigned_benefit": 0.12267820040384929,
            "delta_norm": 11.968559265136719,
            "family": "code_heavy",
            "route_margin": 0.000425487756729126,
            "token": "p",
            "token_class": "function_signature",
            "token_total_benefit": 2.944276809692383
          },
          {
            "assigned_benefit": 0.05997603634993235,
            "delta_norm": 11.941676139831543,
            "family": "code_heavy",
            "route_margin": 0.033836498856544495,
            "token": "n",
            "token_class": "identifier",
            "token_total_benefit": 1.4394248723983765
          },
          {
            "assigned_benefit": 0.051494081815083824,
            "delta_norm": 11.904205322265625,
            "family": "broad_lm",
            "route_margin": 0.0008758902549743652,
            "token": "n",
            "token_class": "prose_word",
            "token_total_benefit": 1.2358579635620117
          },
          {
            "assigned_benefit": 0.005513812104860942,
            "delta_norm": 12.128469467163086,
            "family": "broad_lm",
            "route_margin": 0.0005263984203338623,
            "token": "n",
            "token_class": "prose_word",
            "token_total_benefit": 0.1323314905166626
          },
          {
            "assigned_benefit": -0.002062832315762838,
            "delta_norm": 11.968559265136719,
            "family": "broad_lm",
            "route_margin": 0.00042515993118286133,
            "token": "e",
            "token_class": "prose_word",
            "token_total_benefit": -0.049507975578308105
          },
          {
            "assigned_benefit": -0.01295489693681399,
            "delta_norm": 11.82947826385498,
            "family": "broad_lm",
            "route_margin": 0.02840632200241089,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -0.31091752648353577
          },
          {
            "assigned_benefit": -0.019533616801102955,
            "delta_norm": 11.911380767822266,
            "family": "broad_lm",
            "route_margin": 0.01734989881515503,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -0.46880680322647095
          }
        ],
        "total_assigned_benefit": 0.3843736412624518
      },
      "layer_13_expert_7": {
        "activation_count": 705,
        "mean_assigned_benefit": 0.06631964137024815,
        "mean_delta_norm": 7.134466505388842,
        "mean_harm": -0.034333885994535934,
        "mean_positive_benefit": 0.09805554831921927,
        "mean_route_margin": 0.05424760582176506,
        "positive_benefit_rate": 0.7602836879432624,
        "prose_benefit": 15.382800182763027,
        "structured_benefit": 28.844429122952292,
        "structured_prose_benefit_ratio": 1.8751091335941226,
        "token_class_benefit": {
          "brace_bracket_paren": 2.559783339500427,
          "comma_colon_semicolon": 2.660144925117493,
          "function_signature": 2.1519979635874433,
          "identifier": 9.654062189161777,
          "json_key": 0.6477404932181041,
          "json_value": 0.714299703637759,
          "newline": 1.6494092196699721,
          "number": 0.9197570085525513,
          "operator": 1.16841326157252,
          "other": 4.156755165740226,
          "prose_word": 17.407363893308982,
          "quote": 2.7543940544128422,
          "space": -3.6532010159765678,
          "string_literal": 3.9644269645214085
        },
        "token_class_counts": {
          "brace_bracket_paren": 12,
          "comma_colon_semicolon": 24,
          "function_signature": 21,
          "identifier": 144,
          "json_key": 5,
          "json_value": 11,
          "newline": 12,
          "number": 8,
          "operator": 6,
          "other": 17,
          "prose_word": 278,
          "quote": 9,
          "space": 115,
          "string_literal": 43
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.1176329255104065,
            "delta_norm": 7.113534927368164,
            "family": "broad_lm",
            "route_margin": 0.007608979940414429,
            "token": "o",
            "token_class": "prose_word",
            "token_total_benefit": -2.823190212249756
          },
          {
            "assigned_benefit": -0.11193382243315379,
            "delta_norm": 7.140011310577393,
            "family": "broad_lm",
            "route_margin": 0.0008465051651000977,
            "token": "e",
            "token_class": "prose_word",
            "token_total_benefit": -2.686411738395691
          },
          {
            "assigned_benefit": -0.10949698835611343,
            "delta_norm": 7.0547194480896,
            "family": "broad_lm",
            "route_margin": 0.07325488328933716,
            "token": "o",
            "token_class": "prose_word",
            "token_total_benefit": -2.6279277205467224
          },
          {
            "assigned_benefit": -0.10870074232419331,
            "delta_norm": 7.186583518981934,
            "family": "broad_lm",
            "route_margin": 0.008351564407348633,
            "token": "o",
            "token_class": "prose_word",
            "token_total_benefit": -2.6088178157806396
          },
          {
            "assigned_benefit": -0.10848332444826762,
            "delta_norm": 7.03702974319458,
            "family": "code_heavy",
            "route_margin": 0.014672040939331055,
            "token": "n",
            "token_class": "identifier",
            "token_total_benefit": -2.603599786758423
          },
          {
            "assigned_benefit": -0.10804811120033264,
            "delta_norm": 6.8963775634765625,
            "family": "broad_lm",
            "route_margin": 0.1022639274597168,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -2.5931546688079834
          },
          {
            "assigned_benefit": -0.09626823663711548,
            "delta_norm": 7.152135372161865,
            "family": "broad_lm",
            "route_margin": 0.06209850311279297,
            "token": "o",
            "token_class": "prose_word",
            "token_total_benefit": -2.3104376792907715
          },
          {
            "assigned_benefit": -0.08720193554957707,
            "delta_norm": 6.987269401550293,
            "family": "json_schema",
            "route_margin": 0.005709409713745117,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -2.09284645318985
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.38037506739298504,
            "delta_norm": 6.947681427001953,
            "family": "code_heavy",
            "route_margin": 0.057866185903549194,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.12900161743164
          },
          {
            "assigned_benefit": 0.3683640956878662,
            "delta_norm": 7.061542510986328,
            "family": "json_schema",
            "route_margin": 0.11834460496902466,
            "token": "\\n",
            "token_class": "newline",
            "token_total_benefit": 8.840738296508789
          },
          {
            "assigned_benefit": 0.3641868432362874,
            "delta_norm": 7.219394207000732,
            "family": "code_heavy",
            "route_margin": 0.06624047458171844,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.740484237670898
          },
          {
            "assigned_benefit": 0.3553175131479899,
            "delta_norm": 7.086981296539307,
            "family": "code_heavy",
            "route_margin": 0.04223525524139404,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.527620315551758
          },
          {
            "assigned_benefit": 0.3433542251586914,
            "delta_norm": 7.177680015563965,
            "family": "json_schema",
            "route_margin": 0.017719954252243042,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 8.240501403808594
          },
          {
            "assigned_benefit": 0.3432128429412842,
            "delta_norm": 7.171887397766113,
            "family": "code_heavy",
            "route_margin": 0.08705797791481018,
            "token": "(",
            "token_class": "function_signature",
            "token_total_benefit": 8.23710823059082
          },
          {
            "assigned_benefit": 0.3370199203491211,
            "delta_norm": 7.291573524475098,
            "family": "code_heavy",
            "route_margin": 0.09768208861351013,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 8.088478088378906
          },
          {
            "assigned_benefit": 0.3353669246037801,
            "delta_norm": 7.047154903411865,
            "family": "code_heavy",
            "route_margin": 0.08039560914039612,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.048806190490723
          }
        ],
        "total_assigned_benefit": 46.75534716602495
      },
      "layer_14_expert_4": {
        "activation_count": 6144,
        "mean_assigned_benefit": 0.05373929488889598,
        "mean_delta_norm": 22.72874137076239,
        "mean_harm": -0.024826768335547745,
        "mean_positive_benefit": 0.09784410649316432,
        "mean_route_margin": 1.12712490503327,
        "positive_benefit_rate": 0.6404622395833334,
        "prose_benefit": 56.70457505631623,
        "structured_benefit": 258.43032231855034,
        "structured_prose_benefit_ratio": 4.557486270938278,
        "token_class_benefit": {
          "brace_bracket_paren": 22.444584201090027,
          "comma_colon_semicolon": 16.416020984450974,
          "function_signature": 13.16676076749961,
          "identifier": 55.53804920737947,
          "indentation": -11.041669860016562,
          "json_key": 16.94993361582359,
          "json_value": 11.185039001051349,
          "newline": 25.72262235022558,
          "number": 9.57654090722402,
          "operator": 8.07730007171631,
          "other": 26.61688668976481,
          "prose_word": 76.35278147365904,
          "quote": 63.48720916112268,
          "space": -20.184092824580176,
          "string_literal": 15.866262050966418
        },
        "token_class_counts": {
          "brace_bracket_paren": 122,
          "comma_colon_semicolon": 173,
          "function_signature": 115,
          "identifier": 1095,
          "indentation": 909,
          "json_key": 217,
          "json_value": 214,
          "newline": 137,
          "number": 71,
          "operator": 45,
          "other": 122,
          "prose_word": 1596,
          "quote": 204,
          "space": 928,
          "string_literal": 196
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.17974231019616127,
            "delta_norm": 22.74820899963379,
            "family": "broad_lm",
            "route_margin": 1.1534578800201416,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -4.3138154447078705
          },
          {
            "assigned_benefit": -0.14390301704406738,
            "delta_norm": 22.87668800354004,
            "family": "json_schema",
            "route_margin": 1.0910704135894775,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -3.453672409057617
          },
          {
            "assigned_benefit": -0.14381763339042664,
            "delta_norm": 22.855714797973633,
            "family": "broad_lm",
            "route_margin": 1.1457725763320923,
            "token": "c",
            "token_class": "prose_word",
            "token_total_benefit": -3.4516232013702393
          },
          {
            "assigned_benefit": -0.13103054463863373,
            "delta_norm": 22.9853572845459,
            "family": "code_heavy",
            "route_margin": 1.067575216293335,
            "token": "g",
            "token_class": "identifier",
            "token_total_benefit": -3.1447330713272095
          },
          {
            "assigned_benefit": -0.12831215063730875,
            "delta_norm": 22.50309944152832,
            "family": "json_schema",
            "route_margin": 1.1128515005111694,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -3.07949161529541
          },
          {
            "assigned_benefit": -0.1258842075864474,
            "delta_norm": 22.83586311340332,
            "family": "broad_lm",
            "route_margin": 1.2812422513961792,
            "token": "m",
            "token_class": "prose_word",
            "token_total_benefit": -3.0212209820747375
          },
          {
            "assigned_benefit": -0.12130660812060039,
            "delta_norm": 22.507455825805664,
            "family": "json_schema",
            "route_margin": 0.9936895370483398,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.911358594894409
          },
          {
            "assigned_benefit": -0.11974493662516277,
            "delta_norm": 22.90280532836914,
            "family": "code_heavy",
            "route_margin": 1.1533117294311523,
            "token": "5",
            "token_class": "number",
            "token_total_benefit": -2.8738784790039062
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.4434954325358073,
            "delta_norm": 22.751602172851562,
            "family": "json_schema",
            "route_margin": 1.0363757610321045,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.643890380859375
          },
          {
            "assigned_benefit": 0.4348748524983724,
            "delta_norm": 22.683759689331055,
            "family": "json_schema",
            "route_margin": 1.157224178314209,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.436996459960938
          },
          {
            "assigned_benefit": 0.42559146881103516,
            "delta_norm": 22.691879272460938,
            "family": "json_schema",
            "route_margin": 1.1434277296066284,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.214195251464844
          },
          {
            "assigned_benefit": 0.4194428126017253,
            "delta_norm": 22.78414535522461,
            "family": "json_schema",
            "route_margin": 1.150710105895996,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.066627502441406
          },
          {
            "assigned_benefit": 0.4192720651626587,
            "delta_norm": 22.77241325378418,
            "family": "code_heavy",
            "route_margin": 1.1760190725326538,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 10.062529563903809
          },
          {
            "assigned_benefit": 0.41413907210032147,
            "delta_norm": 22.840124130249023,
            "family": "code_heavy",
            "route_margin": 1.2014665603637695,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.939337730407715
          },
          {
            "assigned_benefit": 0.40491771697998047,
            "delta_norm": 22.685148239135742,
            "family": "json_schema",
            "route_margin": 1.000770926475525,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.718025207519531
          },
          {
            "assigned_benefit": 0.40347035725911456,
            "delta_norm": 22.673038482666016,
            "family": "json_schema",
            "route_margin": 1.0834742784500122,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.68328857421875
          }
        ],
        "total_assigned_benefit": 330.1742277973769
      },
      "layer_15_expert_3": {
        "activation_count": 6144,
        "mean_assigned_benefit": 0.05373929488889598,
        "mean_delta_norm": 16.158643808060635,
        "mean_harm": -0.024826768335547745,
        "mean_positive_benefit": 0.09784410649316432,
        "mean_route_margin": 0.6923759704028877,
        "positive_benefit_rate": 0.6404622395833334,
        "prose_benefit": 56.70457505631623,
        "structured_benefit": 258.43032231855034,
        "structured_prose_benefit_ratio": 4.557486270938278,
        "token_class_benefit": {
          "brace_bracket_paren": 22.444584201090027,
          "comma_colon_semicolon": 16.416020984450974,
          "function_signature": 13.16676076749961,
          "identifier": 55.53804920737947,
          "indentation": -11.041669860016562,
          "json_key": 16.94993361582359,
          "json_value": 11.185039001051349,
          "newline": 25.72262235022558,
          "number": 9.57654090722402,
          "operator": 8.07730007171631,
          "other": 26.61688668976481,
          "prose_word": 76.35278147365904,
          "quote": 63.48720916112268,
          "space": -20.184092824580176,
          "string_literal": 15.866262050966418
        },
        "token_class_counts": {
          "brace_bracket_paren": 122,
          "comma_colon_semicolon": 173,
          "function_signature": 115,
          "identifier": 1095,
          "indentation": 909,
          "json_key": 217,
          "json_value": 214,
          "newline": 137,
          "number": 71,
          "operator": 45,
          "other": 122,
          "prose_word": 1596,
          "quote": 204,
          "space": 928,
          "string_literal": 196
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.17974231019616127,
            "delta_norm": 16.316221237182617,
            "family": "broad_lm",
            "route_margin": 0.7289800047874451,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -4.3138154447078705
          },
          {
            "assigned_benefit": -0.14390301704406738,
            "delta_norm": 16.190580368041992,
            "family": "json_schema",
            "route_margin": 0.7100922465324402,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -3.453672409057617
          },
          {
            "assigned_benefit": -0.14381763339042664,
            "delta_norm": 16.24898338317871,
            "family": "broad_lm",
            "route_margin": 0.5365042686462402,
            "token": "c",
            "token_class": "prose_word",
            "token_total_benefit": -3.4516232013702393
          },
          {
            "assigned_benefit": -0.13103054463863373,
            "delta_norm": 16.278425216674805,
            "family": "code_heavy",
            "route_margin": 0.7312617301940918,
            "token": "g",
            "token_class": "identifier",
            "token_total_benefit": -3.1447330713272095
          },
          {
            "assigned_benefit": -0.12831215063730875,
            "delta_norm": 16.095468521118164,
            "family": "json_schema",
            "route_margin": 0.7614515423774719,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -3.07949161529541
          },
          {
            "assigned_benefit": -0.1258842075864474,
            "delta_norm": 16.201753616333008,
            "family": "broad_lm",
            "route_margin": 0.6347878575325012,
            "token": "m",
            "token_class": "prose_word",
            "token_total_benefit": -3.0212209820747375
          },
          {
            "assigned_benefit": -0.12130660812060039,
            "delta_norm": 16.16628646850586,
            "family": "json_schema",
            "route_margin": 0.8287912011146545,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.911358594894409
          },
          {
            "assigned_benefit": -0.11974493662516277,
            "delta_norm": 16.156343460083008,
            "family": "code_heavy",
            "route_margin": 0.5829163789749146,
            "token": "5",
            "token_class": "number",
            "token_total_benefit": -2.8738784790039062
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.4434954325358073,
            "delta_norm": 16.24778175354004,
            "family": "json_schema",
            "route_margin": 0.7649969458580017,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.643890380859375
          },
          {
            "assigned_benefit": 0.4348748524983724,
            "delta_norm": 16.22728729248047,
            "family": "json_schema",
            "route_margin": 0.706093430519104,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.436996459960938
          },
          {
            "assigned_benefit": 0.42559146881103516,
            "delta_norm": 16.221237182617188,
            "family": "json_schema",
            "route_margin": 0.6986122727394104,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.214195251464844
          },
          {
            "assigned_benefit": 0.4194428126017253,
            "delta_norm": 16.14693832397461,
            "family": "json_schema",
            "route_margin": 0.7202000021934509,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.066627502441406
          },
          {
            "assigned_benefit": 0.4192720651626587,
            "delta_norm": 16.08673667907715,
            "family": "code_heavy",
            "route_margin": 0.6584316492080688,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 10.062529563903809
          },
          {
            "assigned_benefit": 0.41413907210032147,
            "delta_norm": 16.138212203979492,
            "family": "code_heavy",
            "route_margin": 0.6039937734603882,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.939337730407715
          },
          {
            "assigned_benefit": 0.40491771697998047,
            "delta_norm": 16.189313888549805,
            "family": "json_schema",
            "route_margin": 0.8521301746368408,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.718025207519531
          },
          {
            "assigned_benefit": 0.40347035725911456,
            "delta_norm": 16.11520004272461,
            "family": "json_schema",
            "route_margin": 0.7617906928062439,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.68328857421875
          }
        ],
        "total_assigned_benefit": 330.1742277973769
      },
      "layer_16_expert_0": {
        "activation_count": 1698,
        "mean_assigned_benefit": 0.0633303319859621,
        "mean_delta_norm": 14.914585930719813,
        "mean_harm": -0.030317898150150267,
        "mean_positive_benefit": 0.1000220155966684,
        "mean_route_margin": 0.03883147692511865,
        "positive_benefit_rate": 0.71849234393404,
        "prose_benefit": 24.490524510290914,
        "structured_benefit": 76.64879453415044,
        "structured_prose_benefit_ratio": 3.129732664645162,
        "token_class_benefit": {
          "brace_bracket_paren": 5.50879975159963,
          "comma_colon_semicolon": 6.520897492766379,
          "function_signature": 6.423857222000758,
          "identifier": 22.877290427374326,
          "indentation": -0.9846379963370664,
          "json_key": 3.9912509173154835,
          "json_value": 2.0530038825236265,
          "newline": 6.29031765460968,
          "number": 2.1047128041585283,
          "operator": 3.0030715862909947,
          "other": 10.024209078692971,
          "prose_word": 28.062515231780694,
          "quote": 12.238279501597086,
          "space": -6.215977136123307,
          "string_literal": 5.637313293914001
        },
        "token_class_counts": {
          "brace_bracket_paren": 29,
          "comma_colon_semicolon": 70,
          "function_signature": 47,
          "identifier": 401,
          "indentation": 62,
          "json_key": 38,
          "json_value": 44,
          "newline": 32,
          "number": 15,
          "operator": 17,
          "other": 48,
          "prose_word": 480,
          "quote": 37,
          "space": 306,
          "string_literal": 72
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.17974231019616127,
            "delta_norm": 14.914375305175781,
            "family": "broad_lm",
            "route_margin": 0.011456012725830078,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -4.3138154447078705
          },
          {
            "assigned_benefit": -0.14381763339042664,
            "delta_norm": 14.921710968017578,
            "family": "broad_lm",
            "route_margin": 0.016796231269836426,
            "token": "c",
            "token_class": "prose_word",
            "token_total_benefit": -3.4516232013702393
          },
          {
            "assigned_benefit": -0.11696084340413411,
            "delta_norm": 14.798659324645996,
            "family": "json_schema",
            "route_margin": 0.11329853534698486,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.8070602416992188
          },
          {
            "assigned_benefit": -0.11193382243315379,
            "delta_norm": 14.886679649353027,
            "family": "broad_lm",
            "route_margin": 0.003901183605194092,
            "token": "e",
            "token_class": "prose_word",
            "token_total_benefit": -2.686411738395691
          },
          {
            "assigned_benefit": -0.11105093856652577,
            "delta_norm": 14.891071319580078,
            "family": "broad_lm",
            "route_margin": 0.07280546426773071,
            "token": "o",
            "token_class": "prose_word",
            "token_total_benefit": -2.6652225255966187
          },
          {
            "assigned_benefit": -0.11042344570159912,
            "delta_norm": 14.902003288269043,
            "family": "json_schema",
            "route_margin": 0.02659749984741211,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.650162696838379
          },
          {
            "assigned_benefit": -0.10964437325795491,
            "delta_norm": 14.884298324584961,
            "family": "code_heavy",
            "route_margin": 0.0259895920753479,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -2.631464958190918
          },
          {
            "assigned_benefit": -0.10949698835611343,
            "delta_norm": 14.992206573486328,
            "family": "broad_lm",
            "route_margin": 0.05349266529083252,
            "token": "o",
            "token_class": "prose_word",
            "token_total_benefit": -2.6279277205467224
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.4434954325358073,
            "delta_norm": 14.868946075439453,
            "family": "json_schema",
            "route_margin": 0.012494087219238281,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.643890380859375
          },
          {
            "assigned_benefit": 0.42559146881103516,
            "delta_norm": 14.822091102600098,
            "family": "json_schema",
            "route_margin": 0.017566800117492676,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.214195251464844
          },
          {
            "assigned_benefit": 0.4194428126017253,
            "delta_norm": 14.871405601501465,
            "family": "json_schema",
            "route_margin": 0.030331850051879883,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.066627502441406
          },
          {
            "assigned_benefit": 0.41413907210032147,
            "delta_norm": 14.810589790344238,
            "family": "code_heavy",
            "route_margin": 0.04577767848968506,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.939337730407715
          },
          {
            "assigned_benefit": 0.40491771697998047,
            "delta_norm": 14.78283977508545,
            "family": "json_schema",
            "route_margin": 0.0644349455833435,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.718025207519531
          },
          {
            "assigned_benefit": 0.3964542547861735,
            "delta_norm": 14.844473838806152,
            "family": "code_heavy",
            "route_margin": 0.06219285726547241,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.514902114868164
          },
          {
            "assigned_benefit": 0.38709576924641925,
            "delta_norm": 14.864697456359863,
            "family": "code_heavy",
            "route_margin": 0.04638582468032837,
            "token": "\\",
            "token_class": "function_signature",
            "token_total_benefit": 9.290298461914062
          },
          {
            "assigned_benefit": 0.38402652740478516,
            "delta_norm": 14.968791961669922,
            "family": "code_heavy",
            "route_margin": 0.14600351452827454,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 9.216636657714844
          }
        ],
        "total_assigned_benefit": 107.53490371216363
      },
      "layer_16_expert_1": {
        "activation_count": 436,
        "mean_assigned_benefit": 0.079220814694471,
        "mean_delta_norm": 7.850781325900226,
        "mean_harm": -0.02775098797591293,
        "mean_positive_benefit": 0.105125667192997,
        "mean_route_margin": 0.02832527581704866,
        "positive_benefit_rate": 0.805045871559633,
        "prose_benefit": 1.6255378285422903,
        "structured_benefit": 31.691557541179147,
        "structured_prose_benefit_ratio": 19.496044315129055,
        "token_class_benefit": {
          "brace_bracket_paren": 2.6141997575759883,
          "comma_colon_semicolon": 1.6757659514745076,
          "function_signature": 1.7070232257246971,
          "identifier": 5.07627900938193,
          "indentation": -0.05882900425543387,
          "json_key": 6.989561587572097,
          "json_value": 3.5828364364181953,
          "newline": 3.9419917662938437,
          "number": 1.005910317103068,
          "other": 1.6368058919906614,
          "prose_word": 2.01253454418232,
          "quote": 4.287285010019939,
          "space": -0.7417937663073338,
          "string_literal": 0.8107044796148934
        },
        "token_class_counts": {
          "brace_bracket_paren": 11,
          "comma_colon_semicolon": 19,
          "function_signature": 19,
          "identifier": 79,
          "indentation": 12,
          "json_key": 81,
          "json_value": 53,
          "newline": 16,
          "number": 7,
          "other": 9,
          "prose_word": 26,
          "quote": 14,
          "space": 81,
          "string_literal": 9
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.08133397996425629,
            "delta_norm": 7.905548095703125,
            "family": "json_schema",
            "route_margin": 0.0045362114906311035,
            "token": "d",
            "token_class": "json_key",
            "token_total_benefit": -1.9520155191421509
          },
          {
            "assigned_benefit": -0.08086709181467693,
            "delta_norm": 7.7618536949157715,
            "family": "json_schema",
            "route_margin": 0.005061745643615723,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -1.940810203552246
          },
          {
            "assigned_benefit": -0.08007093518972397,
            "delta_norm": 7.780044078826904,
            "family": "code_heavy",
            "route_margin": 0.0014878511428833008,
            "token": "t",
            "token_class": "identifier",
            "token_total_benefit": -1.9217024445533752
          },
          {
            "assigned_benefit": -0.07861356933911641,
            "delta_norm": 7.852694511413574,
            "family": "code_heavy",
            "route_margin": 0.004333078861236572,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.886725664138794
          },
          {
            "assigned_benefit": -0.07780401067187388,
            "delta_norm": 7.944787979125977,
            "family": "json_schema",
            "route_margin": 0.08254873752593994,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -1.8672962561249733
          },
          {
            "assigned_benefit": -0.07646821935971577,
            "delta_norm": 7.755813121795654,
            "family": "json_schema",
            "route_margin": 0.02492809295654297,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.8352372646331787
          },
          {
            "assigned_benefit": -0.06350993116696675,
            "delta_norm": 7.82232666015625,
            "family": "json_schema",
            "route_margin": 0.03335583209991455,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.5242383480072021
          },
          {
            "assigned_benefit": -0.06213067720333735,
            "delta_norm": 7.929555416107178,
            "family": "code_heavy",
            "route_margin": 0.05662274360656738,
            "token": "s",
            "token_class": "function_signature",
            "token_total_benefit": -1.4911362528800964
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.4348748524983724,
            "delta_norm": 7.812159538269043,
            "family": "json_schema",
            "route_margin": 0.044027864933013916,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.436996459960938
          },
          {
            "assigned_benefit": 0.3894158601760864,
            "delta_norm": 7.878727912902832,
            "family": "code_heavy",
            "route_margin": 0.009988844394683838,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.345980644226074
          },
          {
            "assigned_benefit": 0.36609824498494464,
            "delta_norm": 7.881876468658447,
            "family": "code_heavy",
            "route_margin": 0.021388471126556396,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.786357879638672
          },
          {
            "assigned_benefit": 0.36353103319803876,
            "delta_norm": 7.824556350708008,
            "family": "code_heavy",
            "route_margin": 0.06330281496047974,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.72474479675293
          },
          {
            "assigned_benefit": 0.35521737734476727,
            "delta_norm": 7.878396987915039,
            "family": "code_heavy",
            "route_margin": 0.008893191814422607,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.525217056274414
          },
          {
            "assigned_benefit": 0.3433542251586914,
            "delta_norm": 7.877604007720947,
            "family": "json_schema",
            "route_margin": 0.024494647979736328,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 8.240501403808594
          },
          {
            "assigned_benefit": 0.33861692746480304,
            "delta_norm": 7.802855014801025,
            "family": "json_schema",
            "route_margin": 0.012069165706634521,
            "token": "\\n",
            "token_class": "newline",
            "token_total_benefit": 8.126806259155273
          },
          {
            "assigned_benefit": 0.32812609275182086,
            "delta_norm": 7.812803745269775,
            "family": "json_schema",
            "route_margin": 0.09294462203979492,
            "token": "\\n",
            "token_class": "newline",
            "token_total_benefit": 7.875026226043701
          }
        ],
        "total_assigned_benefit": 34.54027520678935
      },
      "layer_16_expert_3": {
        "activation_count": 4004,
        "mean_assigned_benefit": 0.04697302920754917,
        "mean_delta_norm": 9.153408859397743,
        "mean_harm": -0.023038690044080008,
        "mean_positive_benefit": 0.09569359453174515,
        "mean_route_margin": 0.05656676586125638,
        "positive_benefit_rate": 0.5896603396603397,
        "prose_benefit": 30.692656940517203,
        "structured_benefit": 149.9667860887893,
        "structured_prose_benefit_ratio": 4.8860802888269665,
        "token_class_benefit": {
          "brace_bracket_paren": 14.321584691914424,
          "comma_colon_semicolon": 8.21935754021009,
          "function_signature": 5.03588031977415,
          "identifier": 27.461295616192107,
          "indentation": -9.998202859424046,
          "json_key": 5.969121110936007,
          "json_value": 5.549198682109511,
          "newline": 15.490312929322057,
          "number": 6.4659177859624215,
          "operator": 5.074228485425311,
          "other": 14.95587171908119,
          "prose_word": 46.242901703653196,
          "quote": 46.96164464950562,
          "space": -13.087347705072409,
          "string_literal": 9.418244277437529
        },
        "token_class_counts": {
          "brace_bracket_paren": 82,
          "comma_colon_semicolon": 84,
          "function_signature": 49,
          "identifier": 613,
          "indentation": 835,
          "json_key": 98,
          "json_value": 117,
          "newline": 89,
          "number": 49,
          "operator": 28,
          "other": 65,
          "prose_word": 1089,
          "quote": 153,
          "space": 538,
          "string_literal": 115
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.14390301704406738,
            "delta_norm": 9.240883827209473,
            "family": "json_schema",
            "route_margin": 0.009511888027191162,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -3.453672409057617
          },
          {
            "assigned_benefit": -0.13103054463863373,
            "delta_norm": 9.087546348571777,
            "family": "code_heavy",
            "route_margin": 0.07070398330688477,
            "token": "g",
            "token_class": "identifier",
            "token_total_benefit": -3.1447330713272095
          },
          {
            "assigned_benefit": -0.12831215063730875,
            "delta_norm": 9.132436752319336,
            "family": "json_schema",
            "route_margin": 0.032395243644714355,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -3.07949161529541
          },
          {
            "assigned_benefit": -0.1258842075864474,
            "delta_norm": 9.15658187866211,
            "family": "broad_lm",
            "route_margin": 0.08443844318389893,
            "token": "m",
            "token_class": "prose_word",
            "token_total_benefit": -3.0212209820747375
          },
          {
            "assigned_benefit": -0.12130660812060039,
            "delta_norm": 9.095252990722656,
            "family": "json_schema",
            "route_margin": 0.08547437191009521,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.911358594894409
          },
          {
            "assigned_benefit": -0.11974493662516277,
            "delta_norm": 9.253315925598145,
            "family": "code_heavy",
            "route_margin": 0.10696691274642944,
            "token": "5",
            "token_class": "number",
            "token_total_benefit": -2.8738784790039062
          },
          {
            "assigned_benefit": -0.1176329255104065,
            "delta_norm": 9.209096908569336,
            "family": "broad_lm",
            "route_margin": 0.03769862651824951,
            "token": "o",
            "token_class": "prose_word",
            "token_total_benefit": -2.823190212249756
          },
          {
            "assigned_benefit": -0.11034655446807544,
            "delta_norm": 9.238201141357422,
            "family": "code_heavy",
            "route_margin": 0.038359999656677246,
            "token": "o",
            "token_class": "identifier",
            "token_total_benefit": -2.6483173072338104
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.4192720651626587,
            "delta_norm": 9.201525688171387,
            "family": "code_heavy",
            "route_margin": 0.04899561405181885,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 10.062529563903809
          },
          {
            "assigned_benefit": 0.40347035725911456,
            "delta_norm": 9.21784782409668,
            "family": "json_schema",
            "route_margin": 0.02152395248413086,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.68328857421875
          },
          {
            "assigned_benefit": 0.40207378069559735,
            "delta_norm": 9.191476821899414,
            "family": "code_heavy",
            "route_margin": 0.009104669094085693,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.649770736694336
          },
          {
            "assigned_benefit": 0.3999309539794922,
            "delta_norm": 9.087787628173828,
            "family": "json_schema",
            "route_margin": 0.016070425510406494,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.598342895507812
          },
          {
            "assigned_benefit": 0.3995812733968099,
            "delta_norm": 9.083252906799316,
            "family": "json_schema",
            "route_margin": 0.00939089059829712,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.589950561523438
          },
          {
            "assigned_benefit": 0.3989645640055339,
            "delta_norm": 9.169554710388184,
            "family": "json_schema",
            "route_margin": 0.05365109443664551,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.575149536132812
          },
          {
            "assigned_benefit": 0.39834149678548175,
            "delta_norm": 9.068293571472168,
            "family": "json_schema",
            "route_margin": 0.047488272190093994,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.560195922851562
          },
          {
            "assigned_benefit": 0.3949778874715169,
            "delta_norm": 9.09030532836914,
            "family": "json_schema",
            "route_margin": 0.010126352310180664,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.479469299316406
          }
        ],
        "total_assigned_benefit": 188.0800089470269
      },
      "layer_16_expert_7": {
        "activation_count": 6,
        "mean_assigned_benefit": 0.003173321899440553,
        "mean_delta_norm": 9.03045686086019,
        "mean_harm": -0.04632473902569877,
        "mean_positive_benefit": 0.05267138282457987,
        "mean_route_margin": 0.01888049642244975,
        "positive_benefit_rate": 0.5,
        "prose_benefit": -0.10414422303438187,
        "structured_benefit": 0.12318415443102519,
        "structured_prose_benefit_ratio": 1.1828227321870513,
        "token_class_benefit": {
          "identifier": 0.12318415443102519,
          "prose_word": 0.03482999404271444,
          "space": -0.1389742170770963
        },
        "token_class_counts": {
          "identifier": 2,
          "prose_word": 1,
          "space": 3
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.08187116185824077,
            "delta_norm": 9.145925521850586,
            "family": "json_schema",
            "route_margin": 0.04716849327087402,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.9649078845977783
          },
          {
            "assigned_benefit": -0.03232860565185547,
            "delta_norm": 9.001158714294434,
            "family": "code_heavy",
            "route_margin": 0.009338915348052979,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -0.7758865356445312
          },
          {
            "assigned_benefit": -0.024774449567000072,
            "delta_norm": 9.1035737991333,
            "family": "broad_lm",
            "route_margin": 0.020625174045562744,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -0.5945867896080017
          },
          {
            "assigned_benefit": 0.03482999404271444,
            "delta_norm": 8.929765701293945,
            "family": "broad_lm",
            "route_margin": 0.01747235655784607,
            "token": "l",
            "token_class": "prose_word",
            "token_total_benefit": 0.8359198570251465
          },
          {
            "assigned_benefit": 0.06110822161038717,
            "delta_norm": 9.001158714294434,
            "family": "code_heavy",
            "route_margin": 0.00933876633644104,
            "token": "n",
            "token_class": "identifier",
            "token_total_benefit": 1.466597318649292
          },
          {
            "assigned_benefit": 0.06207593282063802,
            "delta_norm": 9.001158714294434,
            "family": "json_schema",
            "route_margin": 0.00933927297592163,
            "token": "y",
            "token_class": "identifier",
            "token_total_benefit": 1.4898223876953125
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.06207593282063802,
            "delta_norm": 9.001158714294434,
            "family": "json_schema",
            "route_margin": 0.00933927297592163,
            "token": "y",
            "token_class": "identifier",
            "token_total_benefit": 1.4898223876953125
          },
          {
            "assigned_benefit": 0.06110822161038717,
            "delta_norm": 9.001158714294434,
            "family": "code_heavy",
            "route_margin": 0.00933876633644104,
            "token": "n",
            "token_class": "identifier",
            "token_total_benefit": 1.466597318649292
          },
          {
            "assigned_benefit": 0.03482999404271444,
            "delta_norm": 8.929765701293945,
            "family": "broad_lm",
            "route_margin": 0.01747235655784607,
            "token": "l",
            "token_class": "prose_word",
            "token_total_benefit": 0.8359198570251465
          },
          {
            "assigned_benefit": -0.024774449567000072,
            "delta_norm": 9.1035737991333,
            "family": "broad_lm",
            "route_margin": 0.020625174045562744,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -0.5945867896080017
          },
          {
            "assigned_benefit": -0.03232860565185547,
            "delta_norm": 9.001158714294434,
            "family": "code_heavy",
            "route_margin": 0.009338915348052979,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -0.7758865356445312
          },
          {
            "assigned_benefit": -0.08187116185824077,
            "delta_norm": 9.145925521850586,
            "family": "json_schema",
            "route_margin": 0.04716849327087402,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.9649078845977783
          }
        ],
        "total_assigned_benefit": 0.01903993139664332
      },
      "layer_17_expert_5": {
        "activation_count": 6144,
        "mean_assigned_benefit": 0.05373929488889598,
        "mean_delta_norm": 22.131455366499722,
        "mean_harm": -0.024826768335547745,
        "mean_positive_benefit": 0.09784410649316432,
        "mean_route_margin": 0.8236758920538705,
        "positive_benefit_rate": 0.6404622395833334,
        "prose_benefit": 56.70457505631623,
        "structured_benefit": 258.43032231855034,
        "structured_prose_benefit_ratio": 4.557486270938278,
        "token_class_benefit": {
          "brace_bracket_paren": 22.444584201090027,
          "comma_colon_semicolon": 16.416020984450974,
          "function_signature": 13.16676076749961,
          "identifier": 55.53804920737947,
          "indentation": -11.041669860016562,
          "json_key": 16.94993361582359,
          "json_value": 11.185039001051349,
          "newline": 25.72262235022558,
          "number": 9.57654090722402,
          "operator": 8.07730007171631,
          "other": 26.61688668976481,
          "prose_word": 76.35278147365904,
          "quote": 63.48720916112268,
          "space": -20.184092824580176,
          "string_literal": 15.866262050966418
        },
        "token_class_counts": {
          "brace_bracket_paren": 122,
          "comma_colon_semicolon": 173,
          "function_signature": 115,
          "identifier": 1095,
          "indentation": 909,
          "json_key": 217,
          "json_value": 214,
          "newline": 137,
          "number": 71,
          "operator": 45,
          "other": 122,
          "prose_word": 1596,
          "quote": 204,
          "space": 928,
          "string_literal": 196
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.17974231019616127,
            "delta_norm": 22.151559829711914,
            "family": "broad_lm",
            "route_margin": 0.76362544298172,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -4.3138154447078705
          },
          {
            "assigned_benefit": -0.14390301704406738,
            "delta_norm": 22.20932388305664,
            "family": "json_schema",
            "route_margin": 0.7978883385658264,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -3.453672409057617
          },
          {
            "assigned_benefit": -0.14381763339042664,
            "delta_norm": 22.2390079498291,
            "family": "broad_lm",
            "route_margin": 0.7386844754219055,
            "token": "c",
            "token_class": "prose_word",
            "token_total_benefit": -3.4516232013702393
          },
          {
            "assigned_benefit": -0.13103054463863373,
            "delta_norm": 22.301654815673828,
            "family": "code_heavy",
            "route_margin": 0.7802215218544006,
            "token": "g",
            "token_class": "identifier",
            "token_total_benefit": -3.1447330713272095
          },
          {
            "assigned_benefit": -0.12831215063730875,
            "delta_norm": 22.228464126586914,
            "family": "json_schema",
            "route_margin": 0.8471993207931519,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -3.07949161529541
          },
          {
            "assigned_benefit": -0.1258842075864474,
            "delta_norm": 22.30843734741211,
            "family": "broad_lm",
            "route_margin": 0.8046782612800598,
            "token": "m",
            "token_class": "prose_word",
            "token_total_benefit": -3.0212209820747375
          },
          {
            "assigned_benefit": -0.12130660812060039,
            "delta_norm": 22.219762802124023,
            "family": "json_schema",
            "route_margin": 0.7847346067428589,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.911358594894409
          },
          {
            "assigned_benefit": -0.11974493662516277,
            "delta_norm": 22.138036727905273,
            "family": "code_heavy",
            "route_margin": 0.7241777181625366,
            "token": "5",
            "token_class": "number",
            "token_total_benefit": -2.8738784790039062
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.4434954325358073,
            "delta_norm": 22.21358299255371,
            "family": "json_schema",
            "route_margin": 0.9126418232917786,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.643890380859375
          },
          {
            "assigned_benefit": 0.4348748524983724,
            "delta_norm": 22.1649227142334,
            "family": "json_schema",
            "route_margin": 0.8318861722946167,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.436996459960938
          },
          {
            "assigned_benefit": 0.42559146881103516,
            "delta_norm": 22.24420166015625,
            "family": "json_schema",
            "route_margin": 0.8507524728775024,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.214195251464844
          },
          {
            "assigned_benefit": 0.4194428126017253,
            "delta_norm": 22.22673988342285,
            "family": "json_schema",
            "route_margin": 0.8043043613433838,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.066627502441406
          },
          {
            "assigned_benefit": 0.4192720651626587,
            "delta_norm": 22.21144676208496,
            "family": "code_heavy",
            "route_margin": 0.8519283533096313,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 10.062529563903809
          },
          {
            "assigned_benefit": 0.41413907210032147,
            "delta_norm": 22.21843910217285,
            "family": "code_heavy",
            "route_margin": 0.8092859983444214,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.939337730407715
          },
          {
            "assigned_benefit": 0.40491771697998047,
            "delta_norm": 22.247549057006836,
            "family": "json_schema",
            "route_margin": 0.8814836740493774,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.718025207519531
          },
          {
            "assigned_benefit": 0.40347035725911456,
            "delta_norm": 22.17537498474121,
            "family": "json_schema",
            "route_margin": 0.8571363091468811,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.68328857421875
          }
        ],
        "total_assigned_benefit": 330.1742277973769
      },
      "layer_18_expert_2": {
        "activation_count": 6144,
        "mean_assigned_benefit": 0.05373929488889598,
        "mean_delta_norm": 19.87016569636762,
        "mean_harm": -0.024826768335547745,
        "mean_positive_benefit": 0.09784410649316432,
        "mean_route_margin": 1.047695749187066,
        "positive_benefit_rate": 0.6404622395833334,
        "prose_benefit": 56.70457505631623,
        "structured_benefit": 258.43032231855034,
        "structured_prose_benefit_ratio": 4.557486270938278,
        "token_class_benefit": {
          "brace_bracket_paren": 22.444584201090027,
          "comma_colon_semicolon": 16.416020984450974,
          "function_signature": 13.16676076749961,
          "identifier": 55.53804920737947,
          "indentation": -11.041669860016562,
          "json_key": 16.94993361582359,
          "json_value": 11.185039001051349,
          "newline": 25.72262235022558,
          "number": 9.57654090722402,
          "operator": 8.07730007171631,
          "other": 26.61688668976481,
          "prose_word": 76.35278147365904,
          "quote": 63.48720916112268,
          "space": -20.184092824580176,
          "string_literal": 15.866262050966418
        },
        "token_class_counts": {
          "brace_bracket_paren": 122,
          "comma_colon_semicolon": 173,
          "function_signature": 115,
          "identifier": 1095,
          "indentation": 909,
          "json_key": 217,
          "json_value": 214,
          "newline": 137,
          "number": 71,
          "operator": 45,
          "other": 122,
          "prose_word": 1596,
          "quote": 204,
          "space": 928,
          "string_literal": 196
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.17974231019616127,
            "delta_norm": 19.876901626586914,
            "family": "broad_lm",
            "route_margin": 1.0158721208572388,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -4.3138154447078705
          },
          {
            "assigned_benefit": -0.14390301704406738,
            "delta_norm": 19.96090316772461,
            "family": "json_schema",
            "route_margin": 1.0263921022415161,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -3.453672409057617
          },
          {
            "assigned_benefit": -0.14381763339042664,
            "delta_norm": 19.877731323242188,
            "family": "broad_lm",
            "route_margin": 1.074852705001831,
            "token": "c",
            "token_class": "prose_word",
            "token_total_benefit": -3.4516232013702393
          },
          {
            "assigned_benefit": -0.13103054463863373,
            "delta_norm": 19.809078216552734,
            "family": "code_heavy",
            "route_margin": 1.0952519178390503,
            "token": "g",
            "token_class": "identifier",
            "token_total_benefit": -3.1447330713272095
          },
          {
            "assigned_benefit": -0.12831215063730875,
            "delta_norm": 19.83299446105957,
            "family": "json_schema",
            "route_margin": 0.9873379468917847,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -3.07949161529541
          },
          {
            "assigned_benefit": -0.1258842075864474,
            "delta_norm": 19.938404083251953,
            "family": "broad_lm",
            "route_margin": 1.0856417417526245,
            "token": "m",
            "token_class": "prose_word",
            "token_total_benefit": -3.0212209820747375
          },
          {
            "assigned_benefit": -0.12130660812060039,
            "delta_norm": 19.874141693115234,
            "family": "json_schema",
            "route_margin": 1.0497777462005615,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.911358594894409
          },
          {
            "assigned_benefit": -0.11974493662516277,
            "delta_norm": 19.84254264831543,
            "family": "code_heavy",
            "route_margin": 0.9962435960769653,
            "token": "5",
            "token_class": "number",
            "token_total_benefit": -2.8738784790039062
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.4434954325358073,
            "delta_norm": 19.83881378173828,
            "family": "json_schema",
            "route_margin": 1.0311675071716309,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.643890380859375
          },
          {
            "assigned_benefit": 0.4348748524983724,
            "delta_norm": 19.86912727355957,
            "family": "json_schema",
            "route_margin": 1.0784870386123657,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.436996459960938
          },
          {
            "assigned_benefit": 0.42559146881103516,
            "delta_norm": 19.82309341430664,
            "family": "json_schema",
            "route_margin": 1.0780483484268188,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.214195251464844
          },
          {
            "assigned_benefit": 0.4194428126017253,
            "delta_norm": 19.919261932373047,
            "family": "json_schema",
            "route_margin": 0.996612548828125,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.066627502441406
          },
          {
            "assigned_benefit": 0.4192720651626587,
            "delta_norm": 19.90134048461914,
            "family": "code_heavy",
            "route_margin": 0.9807640314102173,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 10.062529563903809
          },
          {
            "assigned_benefit": 0.41413907210032147,
            "delta_norm": 19.94481658935547,
            "family": "code_heavy",
            "route_margin": 1.0852477550506592,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.939337730407715
          },
          {
            "assigned_benefit": 0.40491771697998047,
            "delta_norm": 19.820728302001953,
            "family": "json_schema",
            "route_margin": 1.0887054204940796,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.718025207519531
          },
          {
            "assigned_benefit": 0.40347035725911456,
            "delta_norm": 19.886669158935547,
            "family": "json_schema",
            "route_margin": 0.960951566696167,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.68328857421875
          }
        ],
        "total_assigned_benefit": 330.1742277973769
      },
      "layer_19_expert_1": {
        "activation_count": 6144,
        "mean_assigned_benefit": 0.05373929488889598,
        "mean_delta_norm": 14.339676395058632,
        "mean_harm": -0.024826768335547745,
        "mean_positive_benefit": 0.09784410649316432,
        "mean_route_margin": 0.3637650806388895,
        "positive_benefit_rate": 0.6404622395833334,
        "prose_benefit": 56.70457505631623,
        "structured_benefit": 258.43032231855034,
        "structured_prose_benefit_ratio": 4.557486270938278,
        "token_class_benefit": {
          "brace_bracket_paren": 22.444584201090027,
          "comma_colon_semicolon": 16.416020984450974,
          "function_signature": 13.16676076749961,
          "identifier": 55.53804920737947,
          "indentation": -11.041669860016562,
          "json_key": 16.94993361582359,
          "json_value": 11.185039001051349,
          "newline": 25.72262235022558,
          "number": 9.57654090722402,
          "operator": 8.07730007171631,
          "other": 26.61688668976481,
          "prose_word": 76.35278147365904,
          "quote": 63.48720916112268,
          "space": -20.184092824580176,
          "string_literal": 15.866262050966418
        },
        "token_class_counts": {
          "brace_bracket_paren": 122,
          "comma_colon_semicolon": 173,
          "function_signature": 115,
          "identifier": 1095,
          "indentation": 909,
          "json_key": 217,
          "json_value": 214,
          "newline": 137,
          "number": 71,
          "operator": 45,
          "other": 122,
          "prose_word": 1596,
          "quote": 204,
          "space": 928,
          "string_literal": 196
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.17974231019616127,
            "delta_norm": 14.366406440734863,
            "family": "broad_lm",
            "route_margin": 0.291988730430603,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -4.3138154447078705
          },
          {
            "assigned_benefit": -0.14390301704406738,
            "delta_norm": 14.313057899475098,
            "family": "json_schema",
            "route_margin": 0.38561248779296875,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -3.453672409057617
          },
          {
            "assigned_benefit": -0.14381763339042664,
            "delta_norm": 14.407355308532715,
            "family": "broad_lm",
            "route_margin": 0.26674365997314453,
            "token": "c",
            "token_class": "prose_word",
            "token_total_benefit": -3.4516232013702393
          },
          {
            "assigned_benefit": -0.13103054463863373,
            "delta_norm": 14.3151216506958,
            "family": "code_heavy",
            "route_margin": 0.26368892192840576,
            "token": "g",
            "token_class": "identifier",
            "token_total_benefit": -3.1447330713272095
          },
          {
            "assigned_benefit": -0.12831215063730875,
            "delta_norm": 14.296895027160645,
            "family": "json_schema",
            "route_margin": 0.4213097095489502,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -3.07949161529541
          },
          {
            "assigned_benefit": -0.1258842075864474,
            "delta_norm": 14.398934364318848,
            "family": "broad_lm",
            "route_margin": 0.31491464376449585,
            "token": "m",
            "token_class": "prose_word",
            "token_total_benefit": -3.0212209820747375
          },
          {
            "assigned_benefit": -0.12130660812060039,
            "delta_norm": 14.287544250488281,
            "family": "json_schema",
            "route_margin": 0.31664901971817017,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.911358594894409
          },
          {
            "assigned_benefit": -0.11974493662516277,
            "delta_norm": 14.355504035949707,
            "family": "code_heavy",
            "route_margin": 0.28216099739074707,
            "token": "5",
            "token_class": "number",
            "token_total_benefit": -2.8738784790039062
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.4434954325358073,
            "delta_norm": 14.353534698486328,
            "family": "json_schema",
            "route_margin": 0.35987240076065063,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.643890380859375
          },
          {
            "assigned_benefit": 0.4348748524983724,
            "delta_norm": 14.38868522644043,
            "family": "json_schema",
            "route_margin": 0.3348906636238098,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.436996459960938
          },
          {
            "assigned_benefit": 0.42559146881103516,
            "delta_norm": 14.35044002532959,
            "family": "json_schema",
            "route_margin": 0.27917373180389404,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.214195251464844
          },
          {
            "assigned_benefit": 0.4194428126017253,
            "delta_norm": 14.386540412902832,
            "family": "json_schema",
            "route_margin": 0.38532501459121704,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.066627502441406
          },
          {
            "assigned_benefit": 0.4192720651626587,
            "delta_norm": 14.404455184936523,
            "family": "code_heavy",
            "route_margin": 0.32831746339797974,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 10.062529563903809
          },
          {
            "assigned_benefit": 0.41413907210032147,
            "delta_norm": 14.413911819458008,
            "family": "code_heavy",
            "route_margin": 0.33236628770828247,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.939337730407715
          },
          {
            "assigned_benefit": 0.40491771697998047,
            "delta_norm": 14.268999099731445,
            "family": "json_schema",
            "route_margin": 0.3577524721622467,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.718025207519531
          },
          {
            "assigned_benefit": 0.40347035725911456,
            "delta_norm": 14.350101470947266,
            "family": "json_schema",
            "route_margin": 0.482115238904953,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.68328857421875
          }
        ],
        "total_assigned_benefit": 330.1742277973769
      },
      "layer_1_expert_0": {
        "activation_count": 780,
        "mean_assigned_benefit": 0.07783074693452834,
        "mean_delta_norm": 8.776963414901342,
        "mean_harm": -0.03515907350513971,
        "mean_positive_benefit": 0.11003377648323104,
        "mean_route_margin": 0.44907594374739207,
        "positive_benefit_rate": 0.7782051282051282,
        "prose_benefit": 13.936986101985283,
        "structured_benefit": 43.97640880538776,
        "structured_prose_benefit_ratio": 3.1553743746019416,
        "token_class_benefit": {
          "brace_bracket_paren": 2.598598599433899,
          "comma_colon_semicolon": 4.1115958491961155,
          "function_signature": 3.4871990134318667,
          "identifier": 9.52229009040942,
          "json_key": 3.2100752741098404,
          "json_value": 2.367456330607335,
          "newline": 1.5916046301523845,
          "number": 0.1646265983581543,
          "operator": 0.4178590774536133,
          "other": 4.2808037896951046,
          "prose_word": 14.604538475628935,
          "quote": 15.07142194112142,
          "space": -2.153768461779691,
          "string_literal": 1.433681401113669
        },
        "token_class_counts": {
          "brace_bracket_paren": 13,
          "comma_colon_semicolon": 37,
          "function_signature": 27,
          "identifier": 171,
          "json_key": 37,
          "json_value": 40,
          "newline": 10,
          "number": 2,
          "operator": 2,
          "other": 18,
          "prose_word": 235,
          "quote": 49,
          "space": 106,
          "string_literal": 33
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.14390301704406738,
            "delta_norm": 10.399097442626953,
            "family": "json_schema",
            "route_margin": 0.31355637311935425,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -3.453672409057617
          },
          {
            "assigned_benefit": -0.12831215063730875,
            "delta_norm": 8.696763038635254,
            "family": "json_schema",
            "route_margin": 0.8326489925384521,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -3.07949161529541
          },
          {
            "assigned_benefit": -0.1176329255104065,
            "delta_norm": 9.97636604309082,
            "family": "broad_lm",
            "route_margin": 0.23989415168762207,
            "token": "o",
            "token_class": "prose_word",
            "token_total_benefit": -2.823190212249756
          },
          {
            "assigned_benefit": -0.11105093856652577,
            "delta_norm": 9.583436965942383,
            "family": "broad_lm",
            "route_margin": 0.6075855493545532,
            "token": "o",
            "token_class": "prose_word",
            "token_total_benefit": -2.6652225255966187
          },
          {
            "assigned_benefit": -0.10949698835611343,
            "delta_norm": 10.070667266845703,
            "family": "broad_lm",
            "route_margin": 0.6319069862365723,
            "token": "o",
            "token_class": "prose_word",
            "token_total_benefit": -2.6279277205467224
          },
          {
            "assigned_benefit": -0.10870074232419331,
            "delta_norm": 9.582876205444336,
            "family": "broad_lm",
            "route_margin": 1.6915316581726074,
            "token": "o",
            "token_class": "prose_word",
            "token_total_benefit": -2.6088178157806396
          },
          {
            "assigned_benefit": -0.10809943079948425,
            "delta_norm": 7.3827805519104,
            "family": "json_schema",
            "route_margin": 0.8024575710296631,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.594386339187622
          },
          {
            "assigned_benefit": -0.10410678386688232,
            "delta_norm": 7.620447635650635,
            "family": "json_schema",
            "route_margin": 0.3265950083732605,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.498562812805176
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.38402652740478516,
            "delta_norm": 9.339630126953125,
            "family": "code_heavy",
            "route_margin": 0.9360202550888062,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 9.216636657714844
          },
          {
            "assigned_benefit": 0.36609824498494464,
            "delta_norm": 6.263526439666748,
            "family": "code_heavy",
            "route_margin": 0.54010009765625,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.786357879638672
          },
          {
            "assigned_benefit": 0.3605623245239258,
            "delta_norm": 7.117668151855469,
            "family": "code_heavy",
            "route_margin": 0.06502655148506165,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 8.653495788574219
          },
          {
            "assigned_benefit": 0.3566751480102539,
            "delta_norm": 9.883378982543945,
            "family": "code_heavy",
            "route_margin": 0.17397665977478027,
            "token": "\"",
            "token_class": "function_signature",
            "token_total_benefit": 8.560203552246094
          },
          {
            "assigned_benefit": 0.3564949035644531,
            "delta_norm": 9.231597900390625,
            "family": "code_heavy",
            "route_margin": 0.43014854192733765,
            "token": "\\",
            "token_class": "function_signature",
            "token_total_benefit": 8.555877685546875
          },
          {
            "assigned_benefit": 0.3549944559733073,
            "delta_norm": 10.187993049621582,
            "family": "code_heavy",
            "route_margin": 0.6529145240783691,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 8.519866943359375
          },
          {
            "assigned_benefit": 0.35045115152994794,
            "delta_norm": 10.12736701965332,
            "family": "code_heavy",
            "route_margin": 0.3135470747947693,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 8.41082763671875
          },
          {
            "assigned_benefit": 0.3501269022623698,
            "delta_norm": 7.090063571929932,
            "family": "code_heavy",
            "route_margin": 0.11433267593383789,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 8.403045654296875
          }
        ],
        "total_assigned_benefit": 60.7079826089321
      },
      "layer_1_expert_1": {
        "activation_count": 186,
        "mean_assigned_benefit": 0.07813368520819339,
        "mean_delta_norm": 8.75080995405874,
        "mean_harm": -0.029090134019928948,
        "mean_positive_benefit": 0.11235405304695587,
        "mean_route_margin": 0.26325885855382486,
        "positive_benefit_rate": 0.7580645161290323,
        "prose_benefit": 1.015506591827412,
        "structured_benefit": 13.619935609424598,
        "structured_prose_benefit_ratio": 13.411961792306457,
        "token_class_benefit": {
          "brace_bracket_paren": 0.5384463046987851,
          "comma_colon_semicolon": 0.20948043465614316,
          "function_signature": -0.04466720422108968,
          "identifier": 1.3844027866919837,
          "json_key": 0.4189275801181793,
          "json_value": 0.16849923133850098,
          "newline": 5.3362731139108455,
          "number": 0.5002750953038534,
          "operator": 0.9668024579683939,
          "other": 0.8043775729214151,
          "prose_word": 0.5483775956866642,
          "quote": 3.5589590072631836,
          "space": -0.43982532930870855,
          "string_literal": 0.5825368016958237
        },
        "token_class_counts": {
          "brace_bracket_paren": 5,
          "comma_colon_semicolon": 3,
          "function_signature": 1,
          "identifier": 24,
          "json_key": 6,
          "json_value": 3,
          "newline": 24,
          "number": 5,
          "operator": 8,
          "other": 4,
          "prose_word": 26,
          "quote": 11,
          "space": 59,
          "string_literal": 7
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.109354833761851,
            "delta_norm": 7.18292236328125,
            "family": "code_heavy",
            "route_margin": 0.002853870391845703,
            "token": "-",
            "token_class": "operator",
            "token_total_benefit": -2.624516010284424
          },
          {
            "assigned_benefit": -0.10804811120033264,
            "delta_norm": 11.918046951293945,
            "family": "broad_lm",
            "route_margin": 0.34844034910202026,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -2.5931546688079834
          },
          {
            "assigned_benefit": -0.0890117771923542,
            "delta_norm": 9.327352523803711,
            "family": "json_schema",
            "route_margin": 0.31232941150665283,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -2.136282652616501
          },
          {
            "assigned_benefit": -0.08452899257342021,
            "delta_norm": 8.818594932556152,
            "family": "broad_lm",
            "route_margin": 0.2532644271850586,
            "token": "w",
            "token_class": "prose_word",
            "token_total_benefit": -2.028695821762085
          },
          {
            "assigned_benefit": -0.08154816304643948,
            "delta_norm": 9.59578800201416,
            "family": "json_schema",
            "route_margin": 0.23515117168426514,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.9571559131145477
          },
          {
            "assigned_benefit": -0.06074541310469309,
            "delta_norm": 9.585844039916992,
            "family": "json_schema",
            "route_margin": 0.22826546430587769,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.4578899145126343
          },
          {
            "assigned_benefit": -0.05799669027328491,
            "delta_norm": 8.643351554870605,
            "family": "code_heavy",
            "route_margin": 0.029060274362564087,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.391920566558838
          },
          {
            "assigned_benefit": -0.05399461587270101,
            "delta_norm": 11.63779354095459,
            "family": "json_schema",
            "route_margin": 0.7084710597991943,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.2958707809448242
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.3795582453409831,
            "delta_norm": 8.203532218933105,
            "family": "json_schema",
            "route_margin": 0.4346606433391571,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.109397888183594
          },
          {
            "assigned_benefit": 0.3621540069580078,
            "delta_norm": 7.5341901779174805,
            "family": "code_heavy",
            "route_margin": 0.010898113250732422,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.691696166992188
          },
          {
            "assigned_benefit": 0.3612794876098633,
            "delta_norm": 9.553977012634277,
            "family": "json_schema",
            "route_margin": 0.053105056285858154,
            "token": "\\n",
            "token_class": "newline",
            "token_total_benefit": 8.670707702636719
          },
          {
            "assigned_benefit": 0.3417193094889323,
            "delta_norm": 6.584573268890381,
            "family": "code_heavy",
            "route_margin": 0.597378134727478,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 8.201263427734375
          },
          {
            "assigned_benefit": 0.3318033218383789,
            "delta_norm": 7.074286460876465,
            "family": "code_heavy",
            "route_margin": 0.27015650272369385,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 7.963279724121094
          },
          {
            "assigned_benefit": 0.32523314158121747,
            "delta_norm": 7.519792079925537,
            "family": "code_heavy",
            "route_margin": 0.31782087683677673,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 7.805595397949219
          },
          {
            "assigned_benefit": 0.31995201110839844,
            "delta_norm": 7.09335994720459,
            "family": "code_heavy",
            "route_margin": 0.38645851612091064,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 7.6788482666015625
          },
          {
            "assigned_benefit": 0.3188015619913737,
            "delta_norm": 7.80371618270874,
            "family": "code_heavy",
            "route_margin": 0.49043869972229004,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 7.651237487792969
          }
        ],
        "total_assigned_benefit": 14.532865448723971
      },
      "layer_1_expert_2": {
        "activation_count": 557,
        "mean_assigned_benefit": 0.06272230042342443,
        "mean_delta_norm": 8.939743075379349,
        "mean_harm": -0.022919384233871874,
        "mean_positive_benefit": 0.10428706471043224,
        "mean_route_margin": 0.3208977498742794,
        "positive_benefit_rate": 0.6732495511669659,
        "prose_benefit": 5.530540890063094,
        "structured_benefit": 28.911711247019724,
        "structured_prose_benefit_ratio": 5.227646232390462,
        "token_class_benefit": {
          "brace_bracket_paren": 1.9511118928591409,
          "comma_colon_semicolon": 1.2006901204586027,
          "function_signature": 1.3924724558989205,
          "identifier": 5.684446733444928,
          "indentation": -0.862949804092447,
          "json_key": 3.016136556863785,
          "json_value": 1.7178994367520013,
          "newline": 3.143770406646278,
          "number": 0.9977268775304158,
          "operator": 1.1293128331502278,
          "other": 1.8011082808176675,
          "prose_word": 6.710052977936966,
          "quote": 6.330782254536947,
          "space": -1.6236013658344755,
          "string_literal": 2.347361678878466
        },
        "token_class_counts": {
          "brace_bracket_paren": 9,
          "comma_colon_semicolon": 10,
          "function_signature": 10,
          "identifier": 99,
          "indentation": 79,
          "json_key": 27,
          "json_value": 17,
          "newline": 15,
          "number": 8,
          "operator": 5,
          "other": 8,
          "prose_word": 135,
          "quote": 18,
          "space": 100,
          "string_literal": 17
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.17974231019616127,
            "delta_norm": 10.339085578918457,
            "family": "broad_lm",
            "route_margin": 0.3652651607990265,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -4.3138154447078705
          },
          {
            "assigned_benefit": -0.11974493662516277,
            "delta_norm": 6.7320122718811035,
            "family": "code_heavy",
            "route_margin": 0.08474349975585938,
            "token": "5",
            "token_class": "number",
            "token_total_benefit": -2.8738784790039062
          },
          {
            "assigned_benefit": -0.09847732384999593,
            "delta_norm": 7.449283599853516,
            "family": "broad_lm",
            "route_margin": 0.10151985287666321,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -2.3634557723999023
          },
          {
            "assigned_benefit": -0.08843611180782318,
            "delta_norm": 6.798035621643066,
            "family": "broad_lm",
            "route_margin": 0.09827530384063721,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -2.1224666833877563
          },
          {
            "assigned_benefit": -0.08514145016670227,
            "delta_norm": 6.763930797576904,
            "family": "broad_lm",
            "route_margin": 0.07557106018066406,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -2.0433948040008545
          },
          {
            "assigned_benefit": -0.07365793486436208,
            "delta_norm": 7.023229598999023,
            "family": "code_heavy",
            "route_margin": 0.2121737003326416,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.76779043674469
          },
          {
            "assigned_benefit": -0.06990201274553935,
            "delta_norm": 6.95292854309082,
            "family": "json_schema",
            "route_margin": 0.27698472142219543,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.6776483058929443
          },
          {
            "assigned_benefit": -0.0657743513584137,
            "delta_norm": 6.726838111877441,
            "family": "json_schema",
            "route_margin": 0.010713458061218262,
            "token": " ",
            "token_class": "indentation",
            "token_total_benefit": -1.5785844326019287
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.4434954325358073,
            "delta_norm": 12.206803321838379,
            "family": "json_schema",
            "route_margin": 0.679313600063324,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.643890380859375
          },
          {
            "assigned_benefit": 0.42559146881103516,
            "delta_norm": 10.418274879455566,
            "family": "json_schema",
            "route_margin": 0.30499398708343506,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.214195251464844
          },
          {
            "assigned_benefit": 0.4194428126017253,
            "delta_norm": 10.47254467010498,
            "family": "json_schema",
            "route_margin": 0.625379204750061,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.066627502441406
          },
          {
            "assigned_benefit": 0.3989645640055339,
            "delta_norm": 10.372982025146484,
            "family": "json_schema",
            "route_margin": 1.0077615976333618,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.575149536132812
          },
          {
            "assigned_benefit": 0.3949778874715169,
            "delta_norm": 11.541535377502441,
            "family": "json_schema",
            "route_margin": 0.08290517330169678,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.479469299316406
          },
          {
            "assigned_benefit": 0.38902703921000165,
            "delta_norm": 11.583098411560059,
            "family": "code_heavy",
            "route_margin": 0.2697110176086426,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.336648941040039
          },
          {
            "assigned_benefit": 0.38860607147216797,
            "delta_norm": 11.565093994140625,
            "family": "json_schema",
            "route_margin": 0.08010861277580261,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.326545715332031
          },
          {
            "assigned_benefit": 0.38709576924641925,
            "delta_norm": 8.077591896057129,
            "family": "code_heavy",
            "route_margin": 0.030235975980758667,
            "token": "\\",
            "token_class": "function_signature",
            "token_total_benefit": 9.290298461914062
          }
        ],
        "total_assigned_benefit": 34.93632133584741
      },
      "layer_1_expert_3": {
        "activation_count": 755,
        "mean_assigned_benefit": 0.060513413419787276,
        "mean_delta_norm": 7.860695544615487,
        "mean_harm": -0.027814047795624307,
        "mean_positive_benefit": 0.0945478480165514,
        "mean_route_margin": 0.39015373570832196,
        "positive_benefit_rate": 0.7218543046357616,
        "prose_benefit": 11.466008413782214,
        "structured_benefit": 32.386796381562526,
        "structured_prose_benefit_ratio": 2.8245920648927303,
        "token_class_benefit": {
          "brace_bracket_paren": 2.3650246063868203,
          "comma_colon_semicolon": 1.5694637447595594,
          "function_signature": 1.2644284218549728,
          "identifier": 6.567649800640843,
          "indentation": -0.008661639566222826,
          "json_key": 3.336263467868169,
          "json_value": 1.3294307164226968,
          "newline": 4.339043374100883,
          "number": 0.4819179375966389,
          "operator": 0.21190802256266275,
          "other": 3.652627021074295,
          "prose_word": 12.652616120874876,
          "quote": 7.544834454854328,
          "space": -2.995750752006036,
          "string_literal": 3.3768318345149355
        },
        "token_class_counts": {
          "brace_bracket_paren": 10,
          "comma_colon_semicolon": 18,
          "function_signature": 20,
          "identifier": 142,
          "indentation": 5,
          "json_key": 38,
          "json_value": 27,
          "newline": 24,
          "number": 6,
          "operator": 1,
          "other": 17,
          "prose_word": 239,
          "quote": 23,
          "space": 148,
          "string_literal": 37
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.14381763339042664,
            "delta_norm": 6.743832588195801,
            "family": "broad_lm",
            "route_margin": 0.2647472620010376,
            "token": "c",
            "token_class": "prose_word",
            "token_total_benefit": -3.4516232013702393
          },
          {
            "assigned_benefit": -0.12130660812060039,
            "delta_norm": 7.143562316894531,
            "family": "json_schema",
            "route_margin": 0.05161130428314209,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.911358594894409
          },
          {
            "assigned_benefit": -0.11193382243315379,
            "delta_norm": 7.814388751983643,
            "family": "broad_lm",
            "route_margin": 0.5470263957977295,
            "token": "e",
            "token_class": "prose_word",
            "token_total_benefit": -2.686411738395691
          },
          {
            "assigned_benefit": -0.11034655446807544,
            "delta_norm": 7.8003950119018555,
            "family": "code_heavy",
            "route_margin": 0.4814704656600952,
            "token": "o",
            "token_class": "identifier",
            "token_total_benefit": -2.6483173072338104
          },
          {
            "assigned_benefit": -0.0962066650390625,
            "delta_norm": 6.817654609680176,
            "family": "json_schema",
            "route_margin": 0.108024001121521,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.3089599609375
          },
          {
            "assigned_benefit": -0.09053297837575276,
            "delta_norm": 7.525801181793213,
            "family": "json_schema",
            "route_margin": 0.7091443538665771,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.1727914810180664
          },
          {
            "assigned_benefit": -0.0898671845595042,
            "delta_norm": 7.19208288192749,
            "family": "broad_lm",
            "route_margin": 0.01517486572265625,
            "token": "e",
            "token_class": "prose_word",
            "token_total_benefit": -2.1568124294281006
          },
          {
            "assigned_benefit": -0.0860140969355901,
            "delta_norm": 9.131482124328613,
            "family": "code_heavy",
            "route_margin": 0.044188737869262695,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -2.0643383264541626
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.4348748524983724,
            "delta_norm": 8.018074989318848,
            "family": "json_schema",
            "route_margin": 0.7703670859336853,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.436996459960938
          },
          {
            "assigned_benefit": 0.41413907210032147,
            "delta_norm": 7.208895206451416,
            "family": "code_heavy",
            "route_margin": 0.08928000926971436,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.939337730407715
          },
          {
            "assigned_benefit": 0.3999309539794922,
            "delta_norm": 8.025225639343262,
            "family": "json_schema",
            "route_margin": 1.1318275928497314,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.598342895507812
          },
          {
            "assigned_benefit": 0.3995812733968099,
            "delta_norm": 7.88909387588501,
            "family": "json_schema",
            "route_margin": 0.11773455142974854,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.589950561523438
          },
          {
            "assigned_benefit": 0.3964542547861735,
            "delta_norm": 7.51240873336792,
            "family": "code_heavy",
            "route_margin": 0.3554719090461731,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.514902114868164
          },
          {
            "assigned_benefit": 0.38011709849039715,
            "delta_norm": 7.745084285736084,
            "family": "json_schema",
            "route_margin": 0.004353344440460205,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.122810363769531
          },
          {
            "assigned_benefit": 0.3771365483601888,
            "delta_norm": 7.204405307769775,
            "family": "json_schema",
            "route_margin": 0.7390360236167908,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.051277160644531
          },
          {
            "assigned_benefit": 0.36769771575927734,
            "delta_norm": 7.712922096252441,
            "family": "code_heavy",
            "route_margin": 0.6520746946334839,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 8.824745178222656
          }
        ],
        "total_assigned_benefit": 45.687627131939394
      },
      "layer_1_expert_4": {
        "activation_count": 1434,
        "mean_assigned_benefit": 0.045564610500790526,
        "mean_delta_norm": 8.52469997259696,
        "mean_harm": -0.023589043425428762,
        "mean_positive_benefit": 0.10536588470226771,
        "mean_route_margin": 0.4152878868592334,
        "positive_benefit_rate": 0.5362622036262203,
        "prose_benefit": 6.248009452919936,
        "structured_benefit": 55.46897274055288,
        "structured_prose_benefit_ratio": 8.877863127212473,
        "token_class_benefit": {
          "brace_bracket_paren": 5.931266248226167,
          "comma_colon_semicolon": 5.723270306984584,
          "function_signature": 1.89894200861454,
          "identifier": 13.3586584404111,
          "indentation": -5.376648797808838,
          "json_key": 2.28577911357085,
          "json_value": 2.929804812340687,
          "newline": 2.9397251159084745,
          "number": 2.304598649342855,
          "operator": 1.6561011672019958,
          "other": 5.19323225816091,
          "prose_word": 14.347763606657573,
          "quote": 12.288716952006023,
          "space": -4.293668349428722,
          "string_literal": 4.152109925945599
        },
        "token_class_counts": {
          "brace_bracket_paren": 33,
          "comma_colon_semicolon": 54,
          "function_signature": 12,
          "identifier": 233,
          "indentation": 412,
          "json_key": 41,
          "json_value": 52,
          "newline": 18,
          "number": 17,
          "operator": 8,
          "other": 21,
          "prose_word": 311,
          "quote": 40,
          "space": 140,
          "string_literal": 42
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.11042344570159912,
            "delta_norm": 7.228189945220947,
            "family": "json_schema",
            "route_margin": 0.39654701948165894,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.650162696838379
          },
          {
            "assigned_benefit": -0.10964437325795491,
            "delta_norm": 6.942185878753662,
            "family": "code_heavy",
            "route_margin": 0.1705755591392517,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -2.631464958190918
          },
          {
            "assigned_benefit": -0.1018477330605189,
            "delta_norm": 9.82070255279541,
            "family": "broad_lm",
            "route_margin": 0.5894767045974731,
            "token": " ",
            "token_class": "indentation",
            "token_total_benefit": -2.4443455934524536
          },
          {
            "assigned_benefit": -0.10029297073682149,
            "delta_norm": 6.996946334838867,
            "family": "json_schema",
            "route_margin": 0.317729651927948,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.407031297683716
          },
          {
            "assigned_benefit": -0.09828927119572957,
            "delta_norm": 8.902960777282715,
            "family": "json_schema",
            "route_margin": 0.613492488861084,
            "token": " ",
            "token_class": "indentation",
            "token_total_benefit": -2.3589425086975098
          },
          {
            "assigned_benefit": -0.09623692433039348,
            "delta_norm": 6.992712497711182,
            "family": "json_schema",
            "route_margin": 0.32081103324890137,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.3096861839294434
          },
          {
            "assigned_benefit": -0.09491795673966408,
            "delta_norm": 8.047748565673828,
            "family": "broad_lm",
            "route_margin": 0.6504159569740295,
            "token": "l",
            "token_class": "prose_word",
            "token_total_benefit": -2.278030961751938
          },
          {
            "assigned_benefit": -0.09417232871055603,
            "delta_norm": 7.189696788787842,
            "family": "code_heavy",
            "route_margin": 0.04587048292160034,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.2601358890533447
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.40347035725911456,
            "delta_norm": 8.641624450683594,
            "family": "json_schema",
            "route_margin": 0.30432605743408203,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.68328857421875
          },
          {
            "assigned_benefit": 0.40207378069559735,
            "delta_norm": 8.480376243591309,
            "family": "code_heavy",
            "route_margin": 1.0147730112075806,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.649770736694336
          },
          {
            "assigned_benefit": 0.39834149678548175,
            "delta_norm": 8.463189125061035,
            "family": "json_schema",
            "route_margin": 0.5135285258293152,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.560195922851562
          },
          {
            "assigned_benefit": 0.3903733491897583,
            "delta_norm": 8.952787399291992,
            "family": "code_heavy",
            "route_margin": 0.22501146793365479,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.3689603805542
          },
          {
            "assigned_benefit": 0.37155044078826904,
            "delta_norm": 8.309605598449707,
            "family": "code_heavy",
            "route_margin": 1.0368576049804688,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.917210578918457
          },
          {
            "assigned_benefit": 0.3553175131479899,
            "delta_norm": 9.706472396850586,
            "family": "code_heavy",
            "route_margin": 0.5575536489486694,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.527620315551758
          },
          {
            "assigned_benefit": 0.35521737734476727,
            "delta_norm": 7.905012130737305,
            "family": "code_heavy",
            "route_margin": 0.10906052589416504,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.525217056274414
          },
          {
            "assigned_benefit": 0.35106754302978516,
            "delta_norm": 9.508785247802734,
            "family": "code_heavy",
            "route_margin": 0.49645185470581055,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 8.425621032714844
          }
        ],
        "total_assigned_benefit": 65.33965145813362
      },
      "layer_1_expert_5": {
        "activation_count": 897,
        "mean_assigned_benefit": 0.05128373494562442,
        "mean_delta_norm": 7.709144609296069,
        "mean_harm": -0.02343545637050663,
        "mean_positive_benefit": 0.09864671960503003,
        "mean_route_margin": 0.3334057076336814,
        "positive_benefit_rate": 0.6120401337792643,
        "prose_benefit": 6.057985144546056,
        "structured_benefit": 36.38340417143868,
        "structured_prose_benefit_ratio": 6.005858928887321,
        "token_class_benefit": {
          "brace_bracket_paren": 3.250119924545288,
          "comma_colon_semicolon": 1.8087592422962187,
          "function_signature": 2.2104354153076806,
          "identifier": 7.794417344033718,
          "indentation": -1.8680538682577512,
          "json_key": 1.7019676764806113,
          "json_value": 0.8529664014155667,
          "newline": 4.0658394893350005,
          "number": 1.9725634256998696,
          "operator": 2.49669357140859,
          "other": 5.1245950261751805,
          "prose_word": 10.0035500905166,
          "quote": 8.628105481465656,
          "space": -3.6419851736476025,
          "string_literal": 1.6015361994504926
        },
        "token_class_counts": {
          "brace_bracket_paren": 20,
          "comma_colon_semicolon": 27,
          "function_signature": 19,
          "identifier": 167,
          "indentation": 146,
          "json_key": 24,
          "json_value": 25,
          "newline": 18,
          "number": 15,
          "operator": 14,
          "other": 20,
          "prose_word": 209,
          "quote": 29,
          "space": 140,
          "string_literal": 24
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.13103054463863373,
            "delta_norm": 11.739056587219238,
            "family": "code_heavy",
            "route_margin": 0.3078151047229767,
            "token": "g",
            "token_class": "identifier",
            "token_total_benefit": -3.1447330713272095
          },
          {
            "assigned_benefit": -0.11696084340413411,
            "delta_norm": 8.014986991882324,
            "family": "json_schema",
            "route_margin": 0.39243218302726746,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.8070602416992188
          },
          {
            "assigned_benefit": -0.10102646052837372,
            "delta_norm": 8.086732864379883,
            "family": "code_heavy",
            "route_margin": 0.07699847221374512,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.4246350526809692
          },
          {
            "assigned_benefit": -0.0975755254427592,
            "delta_norm": 9.285619735717773,
            "family": "code_heavy",
            "route_margin": 0.027499914169311523,
            "token": "s",
            "token_class": "string_literal",
            "token_total_benefit": -2.3418126106262207
          },
          {
            "assigned_benefit": -0.08971371750036876,
            "delta_norm": 6.630326271057129,
            "family": "code_heavy",
            "route_margin": 0.6370744109153748,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -2.15312922000885
          },
          {
            "assigned_benefit": -0.08489630619684856,
            "delta_norm": 7.330201625823975,
            "family": "code_heavy",
            "route_margin": 0.19813621044158936,
            "token": "w",
            "token_class": "identifier",
            "token_total_benefit": -2.0375113487243652
          },
          {
            "assigned_benefit": -0.0805702159802119,
            "delta_norm": 6.543650150299072,
            "family": "code_heavy",
            "route_margin": 0.2160213589668274,
            "token": "t",
            "token_class": "identifier",
            "token_total_benefit": -1.9336851835250854
          },
          {
            "assigned_benefit": -0.07861356933911641,
            "delta_norm": 7.481710433959961,
            "family": "code_heavy",
            "route_margin": 0.05854177474975586,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.886725664138794
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.40491771697998047,
            "delta_norm": 7.1980299949646,
            "family": "json_schema",
            "route_margin": 0.03648754954338074,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.718025207519531
          },
          {
            "assigned_benefit": 0.3688637415568034,
            "delta_norm": 6.685783386230469,
            "family": "json_schema",
            "route_margin": 0.41018468141555786,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 8.852729797363281
          },
          {
            "assigned_benefit": 0.3677576382954915,
            "delta_norm": 7.775369167327881,
            "family": "code_heavy",
            "route_margin": 0.7313407063484192,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.826183319091797
          },
          {
            "assigned_benefit": 0.35744380950927734,
            "delta_norm": 7.877445220947266,
            "family": "code_heavy",
            "route_margin": 0.06613755226135254,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 8.578651428222656
          },
          {
            "assigned_benefit": 0.3503510157267253,
            "delta_norm": 8.787259101867676,
            "family": "code_heavy",
            "route_margin": 0.10829770565032959,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 8.408424377441406
          },
          {
            "assigned_benefit": 0.3432128429412842,
            "delta_norm": 7.137111663818359,
            "family": "code_heavy",
            "route_margin": 0.04089081287384033,
            "token": "(",
            "token_class": "function_signature",
            "token_total_benefit": 8.23710823059082
          },
          {
            "assigned_benefit": 0.33861692746480304,
            "delta_norm": 7.901985168457031,
            "family": "json_schema",
            "route_margin": 0.11444675922393799,
            "token": "\\n",
            "token_class": "newline",
            "token_total_benefit": 8.126806259155273
          },
          {
            "assigned_benefit": 0.3370218276977539,
            "delta_norm": 8.950640678405762,
            "family": "code_heavy",
            "route_margin": 0.5238958597183228,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 8.088523864746094
          }
        ],
        "total_assigned_benefit": 46.0015102462251
      },
      "layer_1_expert_6": {
        "activation_count": 1232,
        "mean_assigned_benefit": 0.03784444077650496,
        "mean_delta_norm": 8.661909298463302,
        "mean_harm": -0.022970732260175007,
        "mean_positive_benefit": 0.07910596144716793,
        "mean_route_margin": 0.4340766286054118,
        "positive_benefit_rate": 0.5957792207792207,
        "prose_benefit": 8.74859588057411,
        "structured_benefit": 36.197366630062916,
        "structured_prose_benefit_ratio": 4.137505849417236,
        "token_class_benefit": {
          "brace_bracket_paren": 4.319470922152201,
          "comma_colon_semicolon": 1.2479213178157804,
          "function_signature": 2.637105231483778,
          "identifier": 8.98231018831333,
          "indentation": -2.9194419258274156,
          "json_key": 2.302830219268799,
          "json_value": 1.387281400461991,
          "newline": 1.2720452050620754,
          "number": 2.391196966171264,
          "operator": 0.7967689832051595,
          "other": 3.403651860669319,
          "prose_word": 14.11123410363992,
          "quote": 8.94905296961466,
          "space": -4.1684596318906815,
          "string_literal": 1.9113832265138626
        },
        "token_class_counts": {
          "brace_bracket_paren": 21,
          "comma_colon_semicolon": 15,
          "function_signature": 22,
          "identifier": 203,
          "indentation": 261,
          "json_key": 35,
          "json_value": 34,
          "newline": 9,
          "number": 14,
          "operator": 4,
          "other": 23,
          "prose_word": 351,
          "quote": 30,
          "space": 182,
          "string_literal": 28
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.1258842075864474,
            "delta_norm": 8.875365257263184,
            "family": "broad_lm",
            "route_margin": 0.5992207527160645,
            "token": "m",
            "token_class": "prose_word",
            "token_total_benefit": -3.0212209820747375
          },
          {
            "assigned_benefit": -0.10848332444826762,
            "delta_norm": 8.653738021850586,
            "family": "code_heavy",
            "route_margin": 0.37220174074172974,
            "token": "n",
            "token_class": "identifier",
            "token_total_benefit": -2.603599786758423
          },
          {
            "assigned_benefit": -0.10707541306813557,
            "delta_norm": 10.606585502624512,
            "family": "code_heavy",
            "route_margin": 1.062824010848999,
            "token": "s",
            "token_class": "identifier",
            "token_total_benefit": -2.569809913635254
          },
          {
            "assigned_benefit": -0.09784005582332611,
            "delta_norm": 8.858545303344727,
            "family": "code_heavy",
            "route_margin": 0.08566164970397949,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -2.3481613397598267
          },
          {
            "assigned_benefit": -0.09750870863596599,
            "delta_norm": 7.435679912567139,
            "family": "code_heavy",
            "route_margin": 0.6217138767242432,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -2.3402090072631836
          },
          {
            "assigned_benefit": -0.09179036815961202,
            "delta_norm": 7.901697158813477,
            "family": "broad_lm",
            "route_margin": 0.3926999568939209,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -2.2029688358306885
          },
          {
            "assigned_benefit": -0.08728645245234172,
            "delta_norm": 7.788169860839844,
            "family": "broad_lm",
            "route_margin": 0.7464202642440796,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -2.094874858856201
          },
          {
            "assigned_benefit": -0.08720193554957707,
            "delta_norm": 7.636633396148682,
            "family": "json_schema",
            "route_margin": 0.04461228847503662,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -2.09284645318985
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.4192720651626587,
            "delta_norm": 9.627641677856445,
            "family": "code_heavy",
            "route_margin": 0.043702006340026855,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 10.062529563903809
          },
          {
            "assigned_benefit": 0.3894158601760864,
            "delta_norm": 6.361048221588135,
            "family": "code_heavy",
            "route_margin": 0.4029497504234314,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.345980644226074
          },
          {
            "assigned_benefit": 0.3847957452138265,
            "delta_norm": 6.182657241821289,
            "family": "code_heavy",
            "route_margin": 0.3388792872428894,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.235097885131836
          },
          {
            "assigned_benefit": 0.38037506739298504,
            "delta_norm": 5.914298057556152,
            "family": "code_heavy",
            "route_margin": 0.3579610586166382,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.12900161743164
          },
          {
            "assigned_benefit": 0.3551967938741048,
            "delta_norm": 7.601349830627441,
            "family": "code_heavy",
            "route_margin": 0.9201059937477112,
            "token": "'",
            "token_class": "quote",
            "token_total_benefit": 8.524723052978516
          },
          {
            "assigned_benefit": 0.3502950270970662,
            "delta_norm": 7.560885906219482,
            "family": "json_schema",
            "route_margin": 0.6352180242538452,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.40708065032959
          },
          {
            "assigned_benefit": 0.34815677007039386,
            "delta_norm": 8.361369132995605,
            "family": "code_heavy",
            "route_margin": 0.7740745544433594,
            "token": "'",
            "token_class": "quote",
            "token_total_benefit": 8.355762481689453
          },
          {
            "assigned_benefit": 0.3468109766642253,
            "delta_norm": 8.380128860473633,
            "family": "code_heavy",
            "route_margin": 0.8881531953811646,
            "token": "'",
            "token_class": "quote",
            "token_total_benefit": 8.323463439941406
          }
        ],
        "total_assigned_benefit": 46.624351036654105
      },
      "layer_1_expert_7": {
        "activation_count": 303,
        "mean_assigned_benefit": 0.05394032518455831,
        "mean_delta_norm": 8.377519989957904,
        "mean_harm": -0.024509092930450362,
        "mean_positive_benefit": 0.08604985445953867,
        "mean_route_margin": 0.3544859191027805,
        "positive_benefit_rate": 0.7095709570957096,
        "prose_benefit": 3.700942580617991,
        "structured_benefit": 11.485726733100934,
        "structured_prose_benefit_ratio": 3.1034598572947933,
        "token_class_benefit": {
          "brace_bracket_paren": 1.4905457027877371,
          "comma_colon_semicolon": 0.5448399682839711,
          "function_signature": 0.32084542512893677,
          "identifier": 2.243873823434115,
          "indentation": -0.005913824463884036,
          "json_key": 0.6779537275433541,
          "json_value": 0.4317006717125575,
          "newline": 3.0343210151096445,
          "number": 0.7636353572209676,
          "operator": 0.4018539587656657,
          "other": 2.356490880250931,
          "prose_word": 3.374648502717415,
          "quote": 1.1153361002604167,
          "space": -0.8670337606842321,
          "string_literal": 0.4608209828535716
        },
        "token_class_counts": {
          "brace_bracket_paren": 11,
          "comma_colon_semicolon": 9,
          "function_signature": 4,
          "identifier": 56,
          "indentation": 6,
          "json_key": 9,
          "json_value": 16,
          "newline": 19,
          "number": 4,
          "operator": 3,
          "other": 11,
          "prose_word": 90,
          "quote": 4,
          "space": 53,
          "string_literal": 8
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.10159913450479507,
            "delta_norm": 9.849246978759766,
            "family": "broad_lm",
            "route_margin": 0.9883719682693481,
            "token": "p",
            "token_class": "prose_word",
            "token_total_benefit": -2.438379228115082
          },
          {
            "assigned_benefit": -0.09698358178138733,
            "delta_norm": 7.987293243408203,
            "family": "broad_lm",
            "route_margin": 0.7203863263130188,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -2.327605962753296
          },
          {
            "assigned_benefit": -0.08985122044881184,
            "delta_norm": 7.588008403778076,
            "family": "broad_lm",
            "route_margin": 0.677435040473938,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -2.1564292907714844
          },
          {
            "assigned_benefit": -0.08007093518972397,
            "delta_norm": 7.473260402679443,
            "family": "code_heavy",
            "route_margin": 0.2804999053478241,
            "token": "t",
            "token_class": "identifier",
            "token_total_benefit": -1.9217024445533752
          },
          {
            "assigned_benefit": -0.07303215439120929,
            "delta_norm": 9.958306312561035,
            "family": "code_heavy",
            "route_margin": 0.2869452238082886,
            "token": "p",
            "token_class": "identifier",
            "token_total_benefit": -1.7527717053890228
          },
          {
            "assigned_benefit": -0.06984764834245046,
            "delta_norm": 7.625823497772217,
            "family": "broad_lm",
            "route_margin": 0.19792383909225464,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -1.676343560218811
          },
          {
            "assigned_benefit": -0.06819106638431549,
            "delta_norm": 9.465511322021484,
            "family": "code_heavy",
            "route_margin": 0.7451909184455872,
            "token": "p",
            "token_class": "identifier",
            "token_total_benefit": -1.6365855932235718
          },
          {
            "assigned_benefit": -0.0659417857726415,
            "delta_norm": 7.848275661468506,
            "family": "broad_lm",
            "route_margin": 0.7089410424232483,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.582602858543396
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.38800891240437824,
            "delta_norm": 6.664642810821533,
            "family": "code_heavy",
            "route_margin": 0.07800638675689697,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.312213897705078
          },
          {
            "assigned_benefit": 0.3353669246037801,
            "delta_norm": 8.353078842163086,
            "family": "code_heavy",
            "route_margin": 0.6103642582893372,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.048806190490723
          },
          {
            "assigned_benefit": 0.30034224192301434,
            "delta_norm": 8.189716339111328,
            "family": "code_heavy",
            "route_margin": 0.027908504009246826,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 7.208213806152344
          },
          {
            "assigned_benefit": 0.2923320134480794,
            "delta_norm": 7.038879871368408,
            "family": "code_heavy",
            "route_margin": 0.3384009003639221,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 7.015968322753906
          },
          {
            "assigned_benefit": 0.2919797897338867,
            "delta_norm": 7.058428764343262,
            "family": "code_heavy",
            "route_margin": 0.3422536253929138,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 7.007514953613281
          },
          {
            "assigned_benefit": 0.2917188008626302,
            "delta_norm": 8.476365089416504,
            "family": "code_heavy",
            "route_margin": 1.1964538097381592,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 7.001251220703125
          },
          {
            "assigned_benefit": 0.2791096369425456,
            "delta_norm": 7.309287071228027,
            "family": "code_heavy",
            "route_margin": 0.8575567603111267,
            "token": "1",
            "token_class": "number",
            "token_total_benefit": 6.698631286621094
          },
          {
            "assigned_benefit": 0.27871958414713544,
            "delta_norm": 8.016877174377441,
            "family": "json_schema",
            "route_margin": 0.14206135272979736,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 6.68927001953125
          }
        ],
        "total_assigned_benefit": 16.34391853092117
      },
      "layer_20_expert_3": {
        "activation_count": 6144,
        "mean_assigned_benefit": 0.05373929488889598,
        "mean_delta_norm": 22.55770985999455,
        "mean_harm": -0.024826768335547745,
        "mean_positive_benefit": 0.09784410649316432,
        "mean_route_margin": 0.7626883490108108,
        "positive_benefit_rate": 0.6404622395833334,
        "prose_benefit": 56.70457505631623,
        "structured_benefit": 258.43032231855034,
        "structured_prose_benefit_ratio": 4.557486270938278,
        "token_class_benefit": {
          "brace_bracket_paren": 22.444584201090027,
          "comma_colon_semicolon": 16.416020984450974,
          "function_signature": 13.16676076749961,
          "identifier": 55.53804920737947,
          "indentation": -11.041669860016562,
          "json_key": 16.94993361582359,
          "json_value": 11.185039001051349,
          "newline": 25.72262235022558,
          "number": 9.57654090722402,
          "operator": 8.07730007171631,
          "other": 26.61688668976481,
          "prose_word": 76.35278147365904,
          "quote": 63.48720916112268,
          "space": -20.184092824580176,
          "string_literal": 15.866262050966418
        },
        "token_class_counts": {
          "brace_bracket_paren": 122,
          "comma_colon_semicolon": 173,
          "function_signature": 115,
          "identifier": 1095,
          "indentation": 909,
          "json_key": 217,
          "json_value": 214,
          "newline": 137,
          "number": 71,
          "operator": 45,
          "other": 122,
          "prose_word": 1596,
          "quote": 204,
          "space": 928,
          "string_literal": 196
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.17974231019616127,
            "delta_norm": 22.630359649658203,
            "family": "broad_lm",
            "route_margin": 0.7522459030151367,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -4.3138154447078705
          },
          {
            "assigned_benefit": -0.14390301704406738,
            "delta_norm": 22.549673080444336,
            "family": "json_schema",
            "route_margin": 0.7526525855064392,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -3.453672409057617
          },
          {
            "assigned_benefit": -0.14381763339042664,
            "delta_norm": 22.557416915893555,
            "family": "broad_lm",
            "route_margin": 0.8163696527481079,
            "token": "c",
            "token_class": "prose_word",
            "token_total_benefit": -3.4516232013702393
          },
          {
            "assigned_benefit": -0.13103054463863373,
            "delta_norm": 22.571565628051758,
            "family": "code_heavy",
            "route_margin": 0.7044984102249146,
            "token": "g",
            "token_class": "identifier",
            "token_total_benefit": -3.1447330713272095
          },
          {
            "assigned_benefit": -0.12831215063730875,
            "delta_norm": 22.56909942626953,
            "family": "json_schema",
            "route_margin": 0.6611111760139465,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -3.07949161529541
          },
          {
            "assigned_benefit": -0.1258842075864474,
            "delta_norm": 22.57769012451172,
            "family": "broad_lm",
            "route_margin": 0.7464016675949097,
            "token": "m",
            "token_class": "prose_word",
            "token_total_benefit": -3.0212209820747375
          },
          {
            "assigned_benefit": -0.12130660812060039,
            "delta_norm": 22.589506149291992,
            "family": "json_schema",
            "route_margin": 0.7489410638809204,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.911358594894409
          },
          {
            "assigned_benefit": -0.11974493662516277,
            "delta_norm": 22.521656036376953,
            "family": "code_heavy",
            "route_margin": 0.7273810505867004,
            "token": "5",
            "token_class": "number",
            "token_total_benefit": -2.8738784790039062
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.4434954325358073,
            "delta_norm": 22.538679122924805,
            "family": "json_schema",
            "route_margin": 0.6821215748786926,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.643890380859375
          },
          {
            "assigned_benefit": 0.4348748524983724,
            "delta_norm": 22.588642120361328,
            "family": "json_schema",
            "route_margin": 0.7610617876052856,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.436996459960938
          },
          {
            "assigned_benefit": 0.42559146881103516,
            "delta_norm": 22.574594497680664,
            "family": "json_schema",
            "route_margin": 0.7043313980102539,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.214195251464844
          },
          {
            "assigned_benefit": 0.4194428126017253,
            "delta_norm": 22.665422439575195,
            "family": "json_schema",
            "route_margin": 0.7545937895774841,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.066627502441406
          },
          {
            "assigned_benefit": 0.4192720651626587,
            "delta_norm": 22.55851173400879,
            "family": "code_heavy",
            "route_margin": 0.7145121693611145,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 10.062529563903809
          },
          {
            "assigned_benefit": 0.41413907210032147,
            "delta_norm": 22.557058334350586,
            "family": "code_heavy",
            "route_margin": 0.7075859308242798,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.939337730407715
          },
          {
            "assigned_benefit": 0.40491771697998047,
            "delta_norm": 22.602371215820312,
            "family": "json_schema",
            "route_margin": 0.7192484140396118,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.718025207519531
          },
          {
            "assigned_benefit": 0.40347035725911456,
            "delta_norm": 22.536399841308594,
            "family": "json_schema",
            "route_margin": 0.7637007236480713,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.68328857421875
          }
        ],
        "total_assigned_benefit": 330.1742277973769
      },
      "layer_21_expert_3": {
        "activation_count": 6144,
        "mean_assigned_benefit": 0.05373929488889598,
        "mean_delta_norm": 21.7522662046055,
        "mean_harm": -0.024826768335547745,
        "mean_positive_benefit": 0.09784410649316432,
        "mean_route_margin": 0.6834307850610154,
        "positive_benefit_rate": 0.6404622395833334,
        "prose_benefit": 56.70457505631623,
        "structured_benefit": 258.43032231855034,
        "structured_prose_benefit_ratio": 4.557486270938278,
        "token_class_benefit": {
          "brace_bracket_paren": 22.444584201090027,
          "comma_colon_semicolon": 16.416020984450974,
          "function_signature": 13.16676076749961,
          "identifier": 55.53804920737947,
          "indentation": -11.041669860016562,
          "json_key": 16.94993361582359,
          "json_value": 11.185039001051349,
          "newline": 25.72262235022558,
          "number": 9.57654090722402,
          "operator": 8.07730007171631,
          "other": 26.61688668976481,
          "prose_word": 76.35278147365904,
          "quote": 63.48720916112268,
          "space": -20.184092824580176,
          "string_literal": 15.866262050966418
        },
        "token_class_counts": {
          "brace_bracket_paren": 122,
          "comma_colon_semicolon": 173,
          "function_signature": 115,
          "identifier": 1095,
          "indentation": 909,
          "json_key": 217,
          "json_value": 214,
          "newline": 137,
          "number": 71,
          "operator": 45,
          "other": 122,
          "prose_word": 1596,
          "quote": 204,
          "space": 928,
          "string_literal": 196
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.17974231019616127,
            "delta_norm": 21.80191421508789,
            "family": "broad_lm",
            "route_margin": 0.6114027500152588,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -4.3138154447078705
          },
          {
            "assigned_benefit": -0.14390301704406738,
            "delta_norm": 21.67888069152832,
            "family": "json_schema",
            "route_margin": 0.6771349906921387,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -3.453672409057617
          },
          {
            "assigned_benefit": -0.14381763339042664,
            "delta_norm": 21.710432052612305,
            "family": "broad_lm",
            "route_margin": 0.6713982224464417,
            "token": "c",
            "token_class": "prose_word",
            "token_total_benefit": -3.4516232013702393
          },
          {
            "assigned_benefit": -0.13103054463863373,
            "delta_norm": 21.7945613861084,
            "family": "code_heavy",
            "route_margin": 0.6189509034156799,
            "token": "g",
            "token_class": "identifier",
            "token_total_benefit": -3.1447330713272095
          },
          {
            "assigned_benefit": -0.12831215063730875,
            "delta_norm": 21.77176856994629,
            "family": "json_schema",
            "route_margin": 0.6352849006652832,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -3.07949161529541
          },
          {
            "assigned_benefit": -0.1258842075864474,
            "delta_norm": 21.739561080932617,
            "family": "broad_lm",
            "route_margin": 0.6503593921661377,
            "token": "m",
            "token_class": "prose_word",
            "token_total_benefit": -3.0212209820747375
          },
          {
            "assigned_benefit": -0.12130660812060039,
            "delta_norm": 21.721439361572266,
            "family": "json_schema",
            "route_margin": 0.6341890096664429,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.911358594894409
          },
          {
            "assigned_benefit": -0.11974493662516277,
            "delta_norm": 21.81842803955078,
            "family": "code_heavy",
            "route_margin": 0.7446736097335815,
            "token": "5",
            "token_class": "number",
            "token_total_benefit": -2.8738784790039062
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.4434954325358073,
            "delta_norm": 21.72295379638672,
            "family": "json_schema",
            "route_margin": 0.619948148727417,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.643890380859375
          },
          {
            "assigned_benefit": 0.4348748524983724,
            "delta_norm": 21.767576217651367,
            "family": "json_schema",
            "route_margin": 0.6594862937927246,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.436996459960938
          },
          {
            "assigned_benefit": 0.42559146881103516,
            "delta_norm": 21.727779388427734,
            "family": "json_schema",
            "route_margin": 0.6628418564796448,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.214195251464844
          },
          {
            "assigned_benefit": 0.4194428126017253,
            "delta_norm": 21.722558975219727,
            "family": "json_schema",
            "route_margin": 0.6379161477088928,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.066627502441406
          },
          {
            "assigned_benefit": 0.4192720651626587,
            "delta_norm": 21.707828521728516,
            "family": "code_heavy",
            "route_margin": 0.6529066562652588,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 10.062529563903809
          },
          {
            "assigned_benefit": 0.41413907210032147,
            "delta_norm": 21.860389709472656,
            "family": "code_heavy",
            "route_margin": 0.617277204990387,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.939337730407715
          },
          {
            "assigned_benefit": 0.40491771697998047,
            "delta_norm": 21.71573829650879,
            "family": "json_schema",
            "route_margin": 0.6040302515029907,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.718025207519531
          },
          {
            "assigned_benefit": 0.40347035725911456,
            "delta_norm": 21.80299949645996,
            "family": "json_schema",
            "route_margin": 0.6821829676628113,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.68328857421875
          }
        ],
        "total_assigned_benefit": 330.1742277973769
      },
      "layer_22_expert_7": {
        "activation_count": 6144,
        "mean_assigned_benefit": 0.05373929488889598,
        "mean_delta_norm": 24.133554900996387,
        "mean_harm": -0.024826768335547745,
        "mean_positive_benefit": 0.09784410649316432,
        "mean_route_margin": 0.7567447210603859,
        "positive_benefit_rate": 0.6404622395833334,
        "prose_benefit": 56.70457505631623,
        "structured_benefit": 258.43032231855034,
        "structured_prose_benefit_ratio": 4.557486270938278,
        "token_class_benefit": {
          "brace_bracket_paren": 22.444584201090027,
          "comma_colon_semicolon": 16.416020984450974,
          "function_signature": 13.16676076749961,
          "identifier": 55.53804920737947,
          "indentation": -11.041669860016562,
          "json_key": 16.94993361582359,
          "json_value": 11.185039001051349,
          "newline": 25.72262235022558,
          "number": 9.57654090722402,
          "operator": 8.07730007171631,
          "other": 26.61688668976481,
          "prose_word": 76.35278147365904,
          "quote": 63.48720916112268,
          "space": -20.184092824580176,
          "string_literal": 15.866262050966418
        },
        "token_class_counts": {
          "brace_bracket_paren": 122,
          "comma_colon_semicolon": 173,
          "function_signature": 115,
          "identifier": 1095,
          "indentation": 909,
          "json_key": 217,
          "json_value": 214,
          "newline": 137,
          "number": 71,
          "operator": 45,
          "other": 122,
          "prose_word": 1596,
          "quote": 204,
          "space": 928,
          "string_literal": 196
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.17974231019616127,
            "delta_norm": 24.101839065551758,
            "family": "broad_lm",
            "route_margin": 0.7300772666931152,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -4.3138154447078705
          },
          {
            "assigned_benefit": -0.14390301704406738,
            "delta_norm": 24.134075164794922,
            "family": "json_schema",
            "route_margin": 0.7768314480781555,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -3.453672409057617
          },
          {
            "assigned_benefit": -0.14381763339042664,
            "delta_norm": 24.224767684936523,
            "family": "broad_lm",
            "route_margin": 0.7349515557289124,
            "token": "c",
            "token_class": "prose_word",
            "token_total_benefit": -3.4516232013702393
          },
          {
            "assigned_benefit": -0.13103054463863373,
            "delta_norm": 24.195650100708008,
            "family": "code_heavy",
            "route_margin": 0.7804027199745178,
            "token": "g",
            "token_class": "identifier",
            "token_total_benefit": -3.1447330713272095
          },
          {
            "assigned_benefit": -0.12831215063730875,
            "delta_norm": 24.162019729614258,
            "family": "json_schema",
            "route_margin": 0.8046963810920715,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -3.07949161529541
          },
          {
            "assigned_benefit": -0.1258842075864474,
            "delta_norm": 24.165084838867188,
            "family": "broad_lm",
            "route_margin": 0.7832563519477844,
            "token": "m",
            "token_class": "prose_word",
            "token_total_benefit": -3.0212209820747375
          },
          {
            "assigned_benefit": -0.12130660812060039,
            "delta_norm": 24.149633407592773,
            "family": "json_schema",
            "route_margin": 0.8188002109527588,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.911358594894409
          },
          {
            "assigned_benefit": -0.11974493662516277,
            "delta_norm": 24.105287551879883,
            "family": "code_heavy",
            "route_margin": 0.7175719141960144,
            "token": "5",
            "token_class": "number",
            "token_total_benefit": -2.8738784790039062
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.4434954325358073,
            "delta_norm": 24.133909225463867,
            "family": "json_schema",
            "route_margin": 0.7520334720611572,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.643890380859375
          },
          {
            "assigned_benefit": 0.4348748524983724,
            "delta_norm": 24.09161949157715,
            "family": "json_schema",
            "route_margin": 0.6932511925697327,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.436996459960938
          },
          {
            "assigned_benefit": 0.42559146881103516,
            "delta_norm": 24.08146858215332,
            "family": "json_schema",
            "route_margin": 0.7480195760726929,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.214195251464844
          },
          {
            "assigned_benefit": 0.4194428126017253,
            "delta_norm": 24.130971908569336,
            "family": "json_schema",
            "route_margin": 0.6954326629638672,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.066627502441406
          },
          {
            "assigned_benefit": 0.4192720651626587,
            "delta_norm": 24.12613296508789,
            "family": "code_heavy",
            "route_margin": 0.7638970613479614,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 10.062529563903809
          },
          {
            "assigned_benefit": 0.41413907210032147,
            "delta_norm": 24.13548469543457,
            "family": "code_heavy",
            "route_margin": 0.8184803128242493,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.939337730407715
          },
          {
            "assigned_benefit": 0.40491771697998047,
            "delta_norm": 24.129364013671875,
            "family": "json_schema",
            "route_margin": 0.7745760083198547,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.718025207519531
          },
          {
            "assigned_benefit": 0.40347035725911456,
            "delta_norm": 24.036354064941406,
            "family": "json_schema",
            "route_margin": 0.7366173267364502,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.68328857421875
          }
        ],
        "total_assigned_benefit": 330.1742277973769
      },
      "layer_23_expert_6": {
        "activation_count": 6144,
        "mean_assigned_benefit": 0.05373929488889598,
        "mean_delta_norm": 22.136859925153356,
        "mean_harm": -0.024826768335547745,
        "mean_positive_benefit": 0.09784410649316432,
        "mean_route_margin": 0.7755179187030686,
        "positive_benefit_rate": 0.6404622395833334,
        "prose_benefit": 56.70457505631623,
        "structured_benefit": 258.43032231855034,
        "structured_prose_benefit_ratio": 4.557486270938278,
        "token_class_benefit": {
          "brace_bracket_paren": 22.444584201090027,
          "comma_colon_semicolon": 16.416020984450974,
          "function_signature": 13.16676076749961,
          "identifier": 55.53804920737947,
          "indentation": -11.041669860016562,
          "json_key": 16.94993361582359,
          "json_value": 11.185039001051349,
          "newline": 25.72262235022558,
          "number": 9.57654090722402,
          "operator": 8.07730007171631,
          "other": 26.61688668976481,
          "prose_word": 76.35278147365904,
          "quote": 63.48720916112268,
          "space": -20.184092824580176,
          "string_literal": 15.866262050966418
        },
        "token_class_counts": {
          "brace_bracket_paren": 122,
          "comma_colon_semicolon": 173,
          "function_signature": 115,
          "identifier": 1095,
          "indentation": 909,
          "json_key": 217,
          "json_value": 214,
          "newline": 137,
          "number": 71,
          "operator": 45,
          "other": 122,
          "prose_word": 1596,
          "quote": 204,
          "space": 928,
          "string_literal": 196
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.17974231019616127,
            "delta_norm": 22.149934768676758,
            "family": "broad_lm",
            "route_margin": 0.7349434494972229,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -4.3138154447078705
          },
          {
            "assigned_benefit": -0.14390301704406738,
            "delta_norm": 22.132102966308594,
            "family": "json_schema",
            "route_margin": 0.7673704028129578,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -3.453672409057617
          },
          {
            "assigned_benefit": -0.14381763339042664,
            "delta_norm": 22.177980422973633,
            "family": "broad_lm",
            "route_margin": 0.7758121490478516,
            "token": "c",
            "token_class": "prose_word",
            "token_total_benefit": -3.4516232013702393
          },
          {
            "assigned_benefit": -0.13103054463863373,
            "delta_norm": 22.10748863220215,
            "family": "code_heavy",
            "route_margin": 0.7736138701438904,
            "token": "g",
            "token_class": "identifier",
            "token_total_benefit": -3.1447330713272095
          },
          {
            "assigned_benefit": -0.12831215063730875,
            "delta_norm": 22.162839889526367,
            "family": "json_schema",
            "route_margin": 0.7037225365638733,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -3.07949161529541
          },
          {
            "assigned_benefit": -0.1258842075864474,
            "delta_norm": 22.152753829956055,
            "family": "broad_lm",
            "route_margin": 0.72364342212677,
            "token": "m",
            "token_class": "prose_word",
            "token_total_benefit": -3.0212209820747375
          },
          {
            "assigned_benefit": -0.12130660812060039,
            "delta_norm": 22.030941009521484,
            "family": "json_schema",
            "route_margin": 0.7273052930831909,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.911358594894409
          },
          {
            "assigned_benefit": -0.11974493662516277,
            "delta_norm": 22.177715301513672,
            "family": "code_heavy",
            "route_margin": 0.7762693762779236,
            "token": "5",
            "token_class": "number",
            "token_total_benefit": -2.8738784790039062
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.4434954325358073,
            "delta_norm": 22.152965545654297,
            "family": "json_schema",
            "route_margin": 0.7676111459732056,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.643890380859375
          },
          {
            "assigned_benefit": 0.4348748524983724,
            "delta_norm": 22.164710998535156,
            "family": "json_schema",
            "route_margin": 0.7763402462005615,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.436996459960938
          },
          {
            "assigned_benefit": 0.42559146881103516,
            "delta_norm": 22.15597915649414,
            "family": "json_schema",
            "route_margin": 0.7732692956924438,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.214195251464844
          },
          {
            "assigned_benefit": 0.4194428126017253,
            "delta_norm": 22.205413818359375,
            "family": "json_schema",
            "route_margin": 0.7676566243171692,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.066627502441406
          },
          {
            "assigned_benefit": 0.4192720651626587,
            "delta_norm": 22.148916244506836,
            "family": "code_heavy",
            "route_margin": 0.7787128686904907,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 10.062529563903809
          },
          {
            "assigned_benefit": 0.41413907210032147,
            "delta_norm": 22.125823974609375,
            "family": "code_heavy",
            "route_margin": 0.7710303068161011,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.939337730407715
          },
          {
            "assigned_benefit": 0.40491771697998047,
            "delta_norm": 22.187353134155273,
            "family": "json_schema",
            "route_margin": 0.7627841830253601,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.718025207519531
          },
          {
            "assigned_benefit": 0.40347035725911456,
            "delta_norm": 22.08957862854004,
            "family": "json_schema",
            "route_margin": 0.811398446559906,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.68328857421875
          }
        ],
        "total_assigned_benefit": 330.1742277973769
      },
      "layer_2_expert_0": {
        "activation_count": 194,
        "mean_assigned_benefit": 0.04425788888246893,
        "mean_delta_norm": 8.62648786220354,
        "mean_harm": -0.03390107771021223,
        "mean_positive_benefit": 0.08096891864569797,
        "mean_route_margin": 0.2665024931091316,
        "positive_benefit_rate": 0.6804123711340206,
        "prose_benefit": 1.6160311934848623,
        "structured_benefit": 4.228790666597584,
        "structured_prose_benefit_ratio": 2.616775396196705,
        "token_class_benefit": {
          "brace_bracket_paren": 0.46452013651529944,
          "comma_colon_semicolon": 0.722207138935725,
          "function_signature": 0.03574700653553008,
          "identifier": 1.7370306725303335,
          "indentation": -0.1369512751698494,
          "json_key": -0.026986703276634223,
          "json_value": -0.04548874652634064,
          "newline": 0.16813541452089945,
          "number": 0.2451643943786621,
          "other": 3.260388880968094,
          "prose_word": 2.0133954109624024,
          "quote": 0.6010554631551106,
          "space": -0.7795932401592532,
          "string_literal": 0.32740588982899976
        },
        "token_class_counts": {
          "brace_bracket_paren": 3,
          "comma_colon_semicolon": 10,
          "function_signature": 2,
          "identifier": 47,
          "indentation": 4,
          "json_key": 4,
          "json_value": 4,
          "newline": 2,
          "number": 2,
          "other": 11,
          "prose_word": 54,
          "quote": 2,
          "space": 41,
          "string_literal": 8
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.14381763339042664,
            "delta_norm": 8.90266227722168,
            "family": "broad_lm",
            "route_margin": 0.24095964431762695,
            "token": "c",
            "token_class": "prose_word",
            "token_total_benefit": -3.4516232013702393
          },
          {
            "assigned_benefit": -0.08644822239875793,
            "delta_norm": 9.36164379119873,
            "family": "code_heavy",
            "route_margin": 0.14340431988239288,
            "token": "d",
            "token_class": "string_literal",
            "token_total_benefit": -2.0747573375701904
          },
          {
            "assigned_benefit": -0.07812918225924174,
            "delta_norm": 10.948381423950195,
            "family": "code_heavy",
            "route_margin": 0.3840975761413574,
            "token": "d",
            "token_class": "string_literal",
            "token_total_benefit": -1.8751003742218018
          },
          {
            "assigned_benefit": -0.07780401067187388,
            "delta_norm": 7.770808219909668,
            "family": "json_schema",
            "route_margin": 0.05859565734863281,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -1.8672962561249733
          },
          {
            "assigned_benefit": -0.07732878128687541,
            "delta_norm": 10.3114013671875,
            "family": "json_schema",
            "route_margin": 0.5363103151321411,
            "token": "d",
            "token_class": "json_key",
            "token_total_benefit": -1.8558907508850098
          },
          {
            "assigned_benefit": -0.06984764834245046,
            "delta_norm": 10.656752586364746,
            "family": "broad_lm",
            "route_margin": 0.6874790191650391,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -1.676343560218811
          },
          {
            "assigned_benefit": -0.06572231153647105,
            "delta_norm": 10.628451347351074,
            "family": "json_schema",
            "route_margin": 0.0002229064702987671,
            "token": "d",
            "token_class": "json_key",
            "token_total_benefit": -1.5773354768753052
          },
          {
            "assigned_benefit": -0.05948411673307419,
            "delta_norm": 7.386307716369629,
            "family": "code_heavy",
            "route_margin": 0.031736791133880615,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.4276188015937805
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.36769771575927734,
            "delta_norm": 9.7236328125,
            "family": "code_heavy",
            "route_margin": 0.8939499855041504,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 8.824745178222656
          },
          {
            "assigned_benefit": 0.3503510157267253,
            "delta_norm": 6.980423450469971,
            "family": "code_heavy",
            "route_margin": 0.8672363758087158,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 8.408424377441406
          },
          {
            "assigned_benefit": 0.3410816192626953,
            "delta_norm": 8.877938270568848,
            "family": "code_heavy",
            "route_margin": 0.6227837204933167,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 8.185958862304688
          },
          {
            "assigned_benefit": 0.3320792516072591,
            "delta_norm": 10.473950386047363,
            "family": "code_heavy",
            "route_margin": 0.22800230979919434,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 7.969902038574219
          },
          {
            "assigned_benefit": 0.32137107849121094,
            "delta_norm": 8.709920883178711,
            "family": "code_heavy",
            "route_margin": 0.15461379289627075,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 7.7129058837890625
          },
          {
            "assigned_benefit": 0.31327184041341144,
            "delta_norm": 9.1997709274292,
            "family": "code_heavy",
            "route_margin": 1.1955673694610596,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 7.518524169921875
          },
          {
            "assigned_benefit": 0.30634339650472003,
            "delta_norm": 8.719945907592773,
            "family": "json_schema",
            "route_margin": 0.017306983470916748,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 7.352241516113281
          },
          {
            "assigned_benefit": 0.2998482386271159,
            "delta_norm": 10.286237716674805,
            "family": "code_heavy",
            "route_margin": 0.7038916349411011,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 7.196357727050781
          }
        ],
        "total_assigned_benefit": 8.586030443198974
      },
      "layer_2_expert_1": {
        "activation_count": 897,
        "mean_assigned_benefit": 0.0688917511680957,
        "mean_delta_norm": 7.696266559188316,
        "mean_harm": -0.03242506146262488,
        "mean_positive_benefit": 0.09777720347971945,
        "mean_route_margin": 0.41424666306496066,
        "positive_benefit_rate": 0.778149386845039,
        "prose_benefit": 16.92879509025565,
        "structured_benefit": 41.68818159898124,
        "structured_prose_benefit_ratio": 2.4625604702946218,
        "token_class_benefit": {
          "brace_bracket_paren": 3.2664094939827915,
          "comma_colon_semicolon": 1.5976195832093558,
          "function_signature": 2.8310433079799013,
          "identifier": 12.46620223422845,
          "indentation": -0.0063403019060691195,
          "json_key": 3.388084823886553,
          "json_value": 2.250238873064518,
          "newline": 2.8966549684604015,
          "number": 0.942090670267741,
          "operator": 1.0632329384485881,
          "other": 4.696607897679011,
          "prose_word": 18.947848691294595,
          "quote": 7.556960741678874,
          "space": -3.5303970882669105,
          "string_literal": 3.429643963774045
        },
        "token_class_counts": {
          "brace_bracket_paren": 14,
          "comma_colon_semicolon": 13,
          "function_signature": 21,
          "identifier": 198,
          "indentation": 1,
          "json_key": 45,
          "json_value": 40,
          "newline": 13,
          "number": 7,
          "operator": 6,
          "other": 20,
          "prose_word": 319,
          "quote": 25,
          "space": 139,
          "string_literal": 36
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.13103054463863373,
            "delta_norm": 8.06817626953125,
            "family": "code_heavy",
            "route_margin": 0.7398184537887573,
            "token": "g",
            "token_class": "identifier",
            "token_total_benefit": -3.1447330713272095
          },
          {
            "assigned_benefit": -0.11974493662516277,
            "delta_norm": 6.8971052169799805,
            "family": "code_heavy",
            "route_margin": 0.23931032419204712,
            "token": "5",
            "token_class": "number",
            "token_total_benefit": -2.8738784790039062
          },
          {
            "assigned_benefit": -0.1176329255104065,
            "delta_norm": 8.352887153625488,
            "family": "broad_lm",
            "route_margin": 0.32298749685287476,
            "token": "o",
            "token_class": "prose_word",
            "token_total_benefit": -2.823190212249756
          },
          {
            "assigned_benefit": -0.10949698835611343,
            "delta_norm": 8.140703201293945,
            "family": "broad_lm",
            "route_margin": 0.591320812702179,
            "token": "o",
            "token_class": "prose_word",
            "token_total_benefit": -2.6279277205467224
          },
          {
            "assigned_benefit": -0.10159913450479507,
            "delta_norm": 7.942838668823242,
            "family": "broad_lm",
            "route_margin": 0.33756864070892334,
            "token": "p",
            "token_class": "prose_word",
            "token_total_benefit": -2.438379228115082
          },
          {
            "assigned_benefit": -0.08720193554957707,
            "delta_norm": 7.322363376617432,
            "family": "json_schema",
            "route_margin": 0.2744295597076416,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -2.09284645318985
          },
          {
            "assigned_benefit": -0.08567521969477336,
            "delta_norm": 8.774703979492188,
            "family": "json_schema",
            "route_margin": 0.7601031064987183,
            "token": "d",
            "token_class": "json_key",
            "token_total_benefit": -2.0562052726745605
          },
          {
            "assigned_benefit": -0.08501575887203217,
            "delta_norm": 8.599231719970703,
            "family": "broad_lm",
            "route_margin": 0.36181217432022095,
            "token": "o",
            "token_class": "prose_word",
            "token_total_benefit": -2.040378212928772
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.40207378069559735,
            "delta_norm": 6.581741809844971,
            "family": "code_heavy",
            "route_margin": 0.8617209792137146,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.649770736694336
          },
          {
            "assigned_benefit": 0.38037506739298504,
            "delta_norm": 6.57490873336792,
            "family": "code_heavy",
            "route_margin": 0.3369673490524292,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.12900161743164
          },
          {
            "assigned_benefit": 0.37155044078826904,
            "delta_norm": 6.885687351226807,
            "family": "code_heavy",
            "route_margin": 0.5167742967605591,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.917210578918457
          },
          {
            "assigned_benefit": 0.3677576382954915,
            "delta_norm": 7.955839157104492,
            "family": "code_heavy",
            "route_margin": 1.0974500179290771,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.826183319091797
          },
          {
            "assigned_benefit": 0.3641868432362874,
            "delta_norm": 6.232391357421875,
            "family": "code_heavy",
            "route_margin": 1.1716092824935913,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.740484237670898
          },
          {
            "assigned_benefit": 0.3605623245239258,
            "delta_norm": 7.864248275756836,
            "family": "code_heavy",
            "route_margin": 0.9394442439079285,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 8.653495788574219
          },
          {
            "assigned_benefit": 0.3566751480102539,
            "delta_norm": 7.723876953125,
            "family": "code_heavy",
            "route_margin": 0.003469228744506836,
            "token": "\"",
            "token_class": "function_signature",
            "token_total_benefit": 8.560203552246094
          },
          {
            "assigned_benefit": 0.3553175131479899,
            "delta_norm": 7.460234642028809,
            "family": "code_heavy",
            "route_margin": 1.012459397315979,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.527620315551758
          }
        ],
        "total_assigned_benefit": 61.79590079778185
      },
      "layer_2_expert_2": {
        "activation_count": 1561,
        "mean_assigned_benefit": 0.05015470669102696,
        "mean_delta_norm": 8.035286630902972,
        "mean_harm": -0.02066947125226872,
        "mean_positive_benefit": 0.10626111631315532,
        "mean_route_margin": 0.39254794355474704,
        "positive_benefit_rate": 0.5579756566303652,
        "prose_benefit": 5.609782425686752,
        "structured_benefit": 67.87855768747008,
        "structured_prose_benefit_ratio": 12.10003392941935,
        "token_class_benefit": {
          "brace_bracket_paren": 7.825482666492462,
          "comma_colon_semicolon": 5.235575834910075,
          "function_signature": 2.931565158069134,
          "identifier": 10.6337320903937,
          "indentation": -4.3872537376980025,
          "json_key": 1.7389657845099769,
          "json_value": 3.735087536741049,
          "newline": 4.0625968376795445,
          "number": 3.3310173153877267,
          "operator": 1.6244666973749797,
          "other": 5.742930163939794,
          "prose_word": 13.384896020094557,
          "quote": 24.02958583831787,
          "space": -4.327632989113532,
          "string_literal": 2.730481927593549
        },
        "token_class_counts": {
          "brace_bracket_paren": 50,
          "comma_colon_semicolon": 48,
          "function_signature": 26,
          "identifier": 220,
          "indentation": 435,
          "json_key": 29,
          "json_value": 65,
          "newline": 20,
          "number": 22,
          "operator": 8,
          "other": 23,
          "prose_word": 315,
          "quote": 80,
          "space": 182,
          "string_literal": 38
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.11105093856652577,
            "delta_norm": 6.452820777893066,
            "family": "broad_lm",
            "route_margin": 0.3788106441497803,
            "token": "o",
            "token_class": "prose_word",
            "token_total_benefit": -2.6652225255966187
          },
          {
            "assigned_benefit": -0.11042344570159912,
            "delta_norm": 6.8941545486450195,
            "family": "json_schema",
            "route_margin": 0.3146248459815979,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.650162696838379
          },
          {
            "assigned_benefit": -0.10964437325795491,
            "delta_norm": 8.523232460021973,
            "family": "code_heavy",
            "route_margin": 0.40171152353286743,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -2.631464958190918
          },
          {
            "assigned_benefit": -0.10410678386688232,
            "delta_norm": 6.713677406311035,
            "family": "json_schema",
            "route_margin": 0.601701021194458,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.498562812805176
          },
          {
            "assigned_benefit": -0.10358279943466187,
            "delta_norm": 5.9365315437316895,
            "family": "json_schema",
            "route_margin": 1.0639255046844482,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.4859871864318848
          },
          {
            "assigned_benefit": -0.09847732384999593,
            "delta_norm": 8.08690071105957,
            "family": "broad_lm",
            "route_margin": 0.359615683555603,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -2.3634557723999023
          },
          {
            "assigned_benefit": -0.09828927119572957,
            "delta_norm": 8.517337799072266,
            "family": "json_schema",
            "route_margin": 0.16070345044136047,
            "token": " ",
            "token_class": "indentation",
            "token_total_benefit": -2.3589425086975098
          },
          {
            "assigned_benefit": -0.0962066650390625,
            "delta_norm": 6.608145713806152,
            "family": "json_schema",
            "route_margin": 0.46738773584365845,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.3089599609375
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.39834149678548175,
            "delta_norm": 7.753988265991211,
            "family": "json_schema",
            "route_margin": 0.15203171968460083,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.560195922851562
          },
          {
            "assigned_benefit": 0.38402652740478516,
            "delta_norm": 8.416997909545898,
            "family": "code_heavy",
            "route_margin": 0.6489741206169128,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 9.216636657714844
          },
          {
            "assigned_benefit": 0.35744380950927734,
            "delta_norm": 7.629981517791748,
            "family": "code_heavy",
            "route_margin": 0.13632738590240479,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 8.578651428222656
          },
          {
            "assigned_benefit": 0.3564949035644531,
            "delta_norm": 8.900008201599121,
            "family": "code_heavy",
            "route_margin": 0.9284290075302124,
            "token": "\\",
            "token_class": "function_signature",
            "token_total_benefit": 8.555877685546875
          },
          {
            "assigned_benefit": 0.35289955139160156,
            "delta_norm": 8.398326873779297,
            "family": "code_heavy",
            "route_margin": 0.4384360909461975,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.469589233398438
          },
          {
            "assigned_benefit": 0.3502950270970662,
            "delta_norm": 8.39512825012207,
            "family": "json_schema",
            "route_margin": 0.07801856100559235,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.40708065032959
          },
          {
            "assigned_benefit": 0.3464348316192627,
            "delta_norm": 8.181252479553223,
            "family": "code_heavy",
            "route_margin": 0.6424225568771362,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.314435958862305
          },
          {
            "assigned_benefit": 0.34638198216756183,
            "delta_norm": 8.137537956237793,
            "family": "code_heavy",
            "route_margin": 0.384457528591156,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.313167572021484
          }
        ],
        "total_assigned_benefit": 78.29149714469308
      },
      "layer_2_expert_3": {
        "activation_count": 361,
        "mean_assigned_benefit": 0.07021763672988031,
        "mean_delta_norm": 7.961717797118211,
        "mean_harm": -0.030691421837092475,
        "mean_positive_benefit": 0.10323567427569123,
        "mean_route_margin": 0.2975182379299254,
        "positive_benefit_rate": 0.7534626038781164,
        "prose_benefit": 4.544476592439508,
        "structured_benefit": 19.93973074421873,
        "structured_prose_benefit_ratio": 4.387684772629655,
        "token_class_benefit": {
          "brace_bracket_paren": 0.7843848839402199,
          "comma_colon_semicolon": 2.9174797534942627,
          "function_signature": 0.9300435384114585,
          "identifier": 4.8684708631287,
          "json_key": 0.2962079842885335,
          "json_value": 0.7626678968469303,
          "newline": 5.700534179837412,
          "number": 0.3832587003707886,
          "operator": 0.18774970372517905,
          "other": 1.8573800921440127,
          "prose_word": 4.708768084645271,
          "quote": 1.6467595100402832,
          "space": -1.1573120615212247,
          "string_literal": 1.462173730134964
        },
        "token_class_counts": {
          "brace_bracket_paren": 7,
          "comma_colon_semicolon": 29,
          "function_signature": 6,
          "identifier": 81,
          "json_key": 5,
          "json_value": 13,
          "newline": 24,
          "number": 4,
          "operator": 1,
          "other": 11,
          "prose_word": 75,
          "quote": 5,
          "space": 86,
          "string_literal": 14
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.12130660812060039,
            "delta_norm": 8.422697067260742,
            "family": "json_schema",
            "route_margin": 0.355557918548584,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.911358594894409
          },
          {
            "assigned_benefit": -0.10804811120033264,
            "delta_norm": 9.329718589782715,
            "family": "broad_lm",
            "route_margin": 0.061133235692977905,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -2.5931546688079834
          },
          {
            "assigned_benefit": -0.10029297073682149,
            "delta_norm": 7.880789279937744,
            "family": "json_schema",
            "route_margin": 0.1352716088294983,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.407031297683716
          },
          {
            "assigned_benefit": -0.0975755254427592,
            "delta_norm": 8.682368278503418,
            "family": "code_heavy",
            "route_margin": 0.40796270966529846,
            "token": "s",
            "token_class": "string_literal",
            "token_total_benefit": -2.3418126106262207
          },
          {
            "assigned_benefit": -0.09623692433039348,
            "delta_norm": 7.873798370361328,
            "family": "json_schema",
            "route_margin": 0.1472833752632141,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.3096861839294434
          },
          {
            "assigned_benefit": -0.08750950296719869,
            "delta_norm": 8.543371200561523,
            "family": "json_schema",
            "route_margin": 0.19766998291015625,
            "token": "l",
            "token_class": "identifier",
            "token_total_benefit": -2.1002280712127686
          },
          {
            "assigned_benefit": -0.07416436572869618,
            "delta_norm": 7.010087013244629,
            "family": "code_heavy",
            "route_margin": 0.0027900338172912598,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.7799447774887085
          },
          {
            "assigned_benefit": -0.07303215439120929,
            "delta_norm": 7.052556991577148,
            "family": "code_heavy",
            "route_margin": 0.031602442264556885,
            "token": "p",
            "token_class": "identifier",
            "token_total_benefit": -1.7527717053890228
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.3718280792236328,
            "delta_norm": 8.82459545135498,
            "family": "json_schema",
            "route_margin": 0.4482160210609436,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 8.923873901367188
          },
          {
            "assigned_benefit": 0.3683640956878662,
            "delta_norm": 8.106549263000488,
            "family": "json_schema",
            "route_margin": 0.19294673204421997,
            "token": "\\n",
            "token_class": "newline",
            "token_total_benefit": 8.840738296508789
          },
          {
            "assigned_benefit": 0.3460699717203776,
            "delta_norm": 9.540903091430664,
            "family": "json_schema",
            "route_margin": 0.02725386619567871,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 8.305679321289062
          },
          {
            "assigned_benefit": 0.3337658842404683,
            "delta_norm": 9.054666519165039,
            "family": "json_schema",
            "route_margin": 0.1974824070930481,
            "token": "\\n",
            "token_class": "newline",
            "token_total_benefit": 8.01038122177124
          },
          {
            "assigned_benefit": 0.32466332117716473,
            "delta_norm": 6.81207799911499,
            "family": "code_heavy",
            "route_margin": 0.21746718883514404,
            "token": "'",
            "token_class": "quote",
            "token_total_benefit": 7.791919708251953
          },
          {
            "assigned_benefit": 0.32006919384002686,
            "delta_norm": 8.244819641113281,
            "family": "json_schema",
            "route_margin": 0.7286407947540283,
            "token": "\\n",
            "token_class": "newline",
            "token_total_benefit": 7.6816606521606445
          },
          {
            "assigned_benefit": 0.31861527760823566,
            "delta_norm": 8.98292350769043,
            "family": "code_heavy",
            "route_margin": 0.6376681923866272,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 7.646766662597656
          },
          {
            "assigned_benefit": 0.31577354669570923,
            "delta_norm": 10.057205200195312,
            "family": "json_schema",
            "route_margin": 0.15654194355010986,
            "token": "\\n",
            "token_class": "newline",
            "token_total_benefit": 7.5785651206970215
          }
        ],
        "total_assigned_benefit": 25.34856685948679
      },
      "layer_2_expert_4": {
        "activation_count": 736,
        "mean_assigned_benefit": 0.06537100675165852,
        "mean_delta_norm": 8.372449883948201,
        "mean_harm": -0.027198245274279317,
        "mean_positive_benefit": 0.09212044034934633,
        "mean_route_margin": 0.4135789157134359,
        "positive_benefit_rate": 0.7758152173913043,
        "prose_benefit": 12.398224995764172,
        "structured_benefit": 34.89355096431588,
        "structured_prose_benefit_ratio": 2.8143989140572288,
        "token_class_benefit": {
          "brace_bracket_paren": 2.051795522371928,
          "comma_colon_semicolon": 1.8759644230206811,
          "function_signature": 1.9572395508488019,
          "identifier": 6.251583116129037,
          "indentation": -0.12804058194160464,
          "json_key": 5.9484342460831,
          "json_value": 1.1739043071866035,
          "newline": 2.284815381214154,
          "number": 0.7063560485839844,
          "operator": 1.0358265240987141,
          "other": 2.841601667121116,
          "prose_word": 11.388429803463323,
          "quote": 8.042313734690348,
          "space": -0.882480883738026,
          "string_literal": 3.5653181100885076
        },
        "token_class_counts": {
          "brace_bracket_paren": 10,
          "comma_colon_semicolon": 19,
          "function_signature": 14,
          "identifier": 150,
          "indentation": 18,
          "json_key": 58,
          "json_value": 21,
          "newline": 15,
          "number": 6,
          "operator": 6,
          "other": 19,
          "prose_word": 239,
          "quote": 22,
          "space": 105,
          "string_literal": 34
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.17974231019616127,
            "delta_norm": 8.011032104492188,
            "family": "broad_lm",
            "route_margin": 0.08765071630477905,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -4.3138154447078705
          },
          {
            "assigned_benefit": -0.12831215063730875,
            "delta_norm": 7.472707748413086,
            "family": "json_schema",
            "route_margin": 0.4091215133666992,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -3.07949161529541
          },
          {
            "assigned_benefit": -0.1258842075864474,
            "delta_norm": 10.814807891845703,
            "family": "broad_lm",
            "route_margin": 0.5509945154190063,
            "token": "m",
            "token_class": "prose_word",
            "token_total_benefit": -3.0212209820747375
          },
          {
            "assigned_benefit": -0.11696084340413411,
            "delta_norm": 8.45773983001709,
            "family": "json_schema",
            "route_margin": 0.0976749062538147,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.8070602416992188
          },
          {
            "assigned_benefit": -0.10809943079948425,
            "delta_norm": 7.797860622406006,
            "family": "json_schema",
            "route_margin": 0.24574202299118042,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.594386339187622
          },
          {
            "assigned_benefit": -0.10397198796272278,
            "delta_norm": 7.772404670715332,
            "family": "json_schema",
            "route_margin": 0.2279897928237915,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.4953277111053467
          },
          {
            "assigned_benefit": -0.09491795673966408,
            "delta_norm": 6.979679584503174,
            "family": "broad_lm",
            "route_margin": 0.2995142340660095,
            "token": "l",
            "token_class": "prose_word",
            "token_total_benefit": -2.278030961751938
          },
          {
            "assigned_benefit": -0.09417232871055603,
            "delta_norm": 6.595762252807617,
            "family": "code_heavy",
            "route_margin": 0.02219054102897644,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.2601358890533447
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.4434954325358073,
            "delta_norm": 7.402981281280518,
            "family": "json_schema",
            "route_margin": 0.5643401145935059,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.643890380859375
          },
          {
            "assigned_benefit": 0.4348748524983724,
            "delta_norm": 9.019441604614258,
            "family": "json_schema",
            "route_margin": 1.2289636135101318,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.436996459960938
          },
          {
            "assigned_benefit": 0.42559146881103516,
            "delta_norm": 8.205501556396484,
            "family": "json_schema",
            "route_margin": 0.01650300621986389,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.214195251464844
          },
          {
            "assigned_benefit": 0.4194428126017253,
            "delta_norm": 8.722970962524414,
            "family": "json_schema",
            "route_margin": 0.3161008954048157,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.066627502441406
          },
          {
            "assigned_benefit": 0.40491771697998047,
            "delta_norm": 8.346173286437988,
            "family": "json_schema",
            "route_margin": 0.40655088424682617,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.718025207519531
          },
          {
            "assigned_benefit": 0.3999309539794922,
            "delta_norm": 8.123727798461914,
            "family": "json_schema",
            "route_margin": 0.2786793112754822,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.598342895507812
          },
          {
            "assigned_benefit": 0.3989645640055339,
            "delta_norm": 7.863856792449951,
            "family": "json_schema",
            "route_margin": 1.0240343809127808,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.575149536132812
          },
          {
            "assigned_benefit": 0.3949778874715169,
            "delta_norm": 7.36226224899292,
            "family": "json_schema",
            "route_margin": 1.5501866340637207,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.479469299316406
          }
        ],
        "total_assigned_benefit": 48.113060969220676
      },
      "layer_2_expert_5": {
        "activation_count": 593,
        "mean_assigned_benefit": 0.058942464327095635,
        "mean_delta_norm": 8.115107624768005,
        "mean_harm": -0.02640773738763017,
        "mean_positive_benefit": 0.09918201352262396,
        "mean_route_margin": 0.358502046096737,
        "positive_benefit_rate": 0.6795952782462057,
        "prose_benefit": 8.614128542574989,
        "structured_benefit": 25.76109373299401,
        "structured_prose_benefit_ratio": 2.9905629577816057,
        "token_class_benefit": {
          "brace_bracket_paren": 1.0725344816843667,
          "comma_colon_semicolon": 2.3168775240580244,
          "function_signature": 1.8890543232361474,
          "identifier": 5.327398182203373,
          "indentation": -0.06391690733532111,
          "json_key": 1.9226324657599132,
          "json_value": 0.5443066218867898,
          "newline": 6.933190157109198,
          "number": 0.576611042022705,
          "operator": 1.5238329569498696,
          "other": 3.905111670494079,
          "prose_word": 7.764711023618778,
          "quote": 2.385250091552735,
          "space": -2.414118173803823,
          "string_literal": 1.2694058865308762
        },
        "token_class_counts": {
          "brace_bracket_paren": 7,
          "comma_colon_semicolon": 26,
          "function_signature": 17,
          "identifier": 111,
          "indentation": 18,
          "json_key": 20,
          "json_value": 17,
          "newline": 44,
          "number": 5,
          "operator": 8,
          "other": 16,
          "prose_word": 170,
          "quote": 8,
          "space": 105,
          "string_literal": 21
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.10388837258021037,
            "delta_norm": 8.05263614654541,
            "family": "code_heavy",
            "route_margin": 0.22134709358215332,
            "token": "d",
            "token_class": "string_literal",
            "token_total_benefit": -2.493320941925049
          },
          {
            "assigned_benefit": -0.09750870863596599,
            "delta_norm": 6.962503910064697,
            "family": "code_heavy",
            "route_margin": 0.29880809783935547,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -2.3402090072631836
          },
          {
            "assigned_benefit": -0.09053297837575276,
            "delta_norm": 7.702376842498779,
            "family": "json_schema",
            "route_margin": 0.34272387623786926,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.1727914810180664
          },
          {
            "assigned_benefit": -0.08801374832789104,
            "delta_norm": 7.535809516906738,
            "family": "json_schema",
            "route_margin": 0.261349081993103,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.1123299598693848
          },
          {
            "assigned_benefit": -0.08776763081550598,
            "delta_norm": 7.80244779586792,
            "family": "broad_lm",
            "route_margin": 0.30535101890563965,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -2.1064231395721436
          },
          {
            "assigned_benefit": -0.08452899257342021,
            "delta_norm": 7.865149021148682,
            "family": "broad_lm",
            "route_margin": 0.09322410821914673,
            "token": "w",
            "token_class": "prose_word",
            "token_total_benefit": -2.028695821762085
          },
          {
            "assigned_benefit": -0.08353991309801738,
            "delta_norm": 8.80456256866455,
            "family": "json_schema",
            "route_margin": 0.6889135837554932,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -2.004957914352417
          },
          {
            "assigned_benefit": -0.08353975415229797,
            "delta_norm": 8.80456256866455,
            "family": "json_schema",
            "route_margin": 0.6889135837554932,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -2.0049540996551514
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.40347035725911456,
            "delta_norm": 7.839893341064453,
            "family": "json_schema",
            "route_margin": 0.4241269826889038,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.68328857421875
          },
          {
            "assigned_benefit": 0.3612794876098633,
            "delta_norm": 6.719119071960449,
            "family": "json_schema",
            "route_margin": 0.12475866079330444,
            "token": "\\n",
            "token_class": "newline",
            "token_total_benefit": 8.670707702636719
          },
          {
            "assigned_benefit": 0.35521737734476727,
            "delta_norm": 6.599315643310547,
            "family": "code_heavy",
            "route_margin": 0.10168808698654175,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.525217056274414
          },
          {
            "assigned_benefit": 0.3352521260579427,
            "delta_norm": 8.316479682922363,
            "family": "code_heavy",
            "route_margin": 0.2741578221321106,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 8.046051025390625
          },
          {
            "assigned_benefit": 0.3335253397623698,
            "delta_norm": 8.348312377929688,
            "family": "code_heavy",
            "route_margin": 0.11031617224216461,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 8.004608154296875
          },
          {
            "assigned_benefit": 0.32363001505533856,
            "delta_norm": 8.519909858703613,
            "family": "code_heavy",
            "route_margin": 0.06755185127258301,
            "token": "\"",
            "token_class": "function_signature",
            "token_total_benefit": 7.767120361328125
          },
          {
            "assigned_benefit": 0.32234636942545575,
            "delta_norm": 8.070022583007812,
            "family": "code_heavy",
            "route_margin": 0.25389671325683594,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 7.7363128662109375
          },
          {
            "assigned_benefit": 0.3219327926635742,
            "delta_norm": 9.121596336364746,
            "family": "code_heavy",
            "route_margin": 0.13277912139892578,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 7.726387023925781
          }
        ],
        "total_assigned_benefit": 34.95288134596771
      },
      "layer_2_expert_6": {
        "activation_count": 512,
        "mean_assigned_benefit": 0.04625938741871015,
        "mean_delta_norm": 7.986649916507304,
        "mean_harm": -0.031230087279144576,
        "mean_positive_benefit": 0.07959284860158622,
        "mean_route_margin": 0.358668876637239,
        "positive_benefit_rate": 0.69921875,
        "prose_benefit": 4.653233777731655,
        "structured_benefit": 18.038944180123504,
        "structured_prose_benefit_ratio": 3.876646874362946,
        "token_class_benefit": {
          "brace_bracket_paren": 1.5524486157422264,
          "comma_colon_semicolon": 1.0828347653150558,
          "function_signature": 0.9758038173119228,
          "identifier": 5.365884443124135,
          "indentation": -0.18137831613421437,
          "json_key": 1.7359576622645059,
          "json_value": 0.6773846199115118,
          "newline": 0.5734229981899261,
          "number": 0.356950044631958,
          "operator": 0.5687401294708252,
          "other": 1.6299515763918557,
          "prose_word": 6.586021891484658,
          "quote": 3.9277733167012534,
          "space": -2.3887329734861855,
          "string_literal": 1.2217437674601872
        },
        "token_class_counts": {
          "brace_bracket_paren": 5,
          "comma_colon_semicolon": 18,
          "function_signature": 14,
          "identifier": 117,
          "indentation": 10,
          "json_key": 25,
          "json_value": 18,
          "newline": 4,
          "number": 6,
          "operator": 4,
          "other": 6,
          "prose_word": 170,
          "quote": 13,
          "space": 84,
          "string_literal": 18
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.10870074232419331,
            "delta_norm": 6.67305850982666,
            "family": "broad_lm",
            "route_margin": 0.014704465866088867,
            "token": "o",
            "token_class": "prose_word",
            "token_total_benefit": -2.6088178157806396
          },
          {
            "assigned_benefit": -0.10707541306813557,
            "delta_norm": 8.576883316040039,
            "family": "code_heavy",
            "route_margin": 0.013331949710845947,
            "token": "s",
            "token_class": "identifier",
            "token_total_benefit": -2.569809913635254
          },
          {
            "assigned_benefit": -0.10102646052837372,
            "delta_norm": 8.743880271911621,
            "family": "code_heavy",
            "route_margin": 0.046484410762786865,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.4246350526809692
          },
          {
            "assigned_benefit": -0.09698358178138733,
            "delta_norm": 7.444784641265869,
            "family": "broad_lm",
            "route_margin": 0.9868746995925903,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -2.327605962753296
          },
          {
            "assigned_benefit": -0.09626823663711548,
            "delta_norm": 7.520732879638672,
            "family": "broad_lm",
            "route_margin": 0.40717315673828125,
            "token": "o",
            "token_class": "prose_word",
            "token_total_benefit": -2.3104376792907715
          },
          {
            "assigned_benefit": -0.08985122044881184,
            "delta_norm": 5.831257343292236,
            "family": "broad_lm",
            "route_margin": 0.6959385275840759,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -2.1564292907714844
          },
          {
            "assigned_benefit": -0.0860140969355901,
            "delta_norm": 8.374255180358887,
            "family": "code_heavy",
            "route_margin": 0.29957956075668335,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -2.0643383264541626
          },
          {
            "assigned_benefit": -0.08489630619684856,
            "delta_norm": 7.109153747558594,
            "family": "code_heavy",
            "route_margin": 0.42553842067718506,
            "token": "w",
            "token_class": "identifier",
            "token_total_benefit": -2.0375113487243652
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.4192720651626587,
            "delta_norm": 7.483043193817139,
            "family": "code_heavy",
            "route_margin": 0.4552016258239746,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 10.062529563903809
          },
          {
            "assigned_benefit": 0.3964542547861735,
            "delta_norm": 7.545830726623535,
            "family": "code_heavy",
            "route_margin": 0.172027587890625,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.514902114868164
          },
          {
            "assigned_benefit": 0.38800891240437824,
            "delta_norm": 7.796440124511719,
            "family": "code_heavy",
            "route_margin": 0.3694186210632324,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.312213897705078
          },
          {
            "assigned_benefit": 0.3370218276977539,
            "delta_norm": 6.888159275054932,
            "family": "code_heavy",
            "route_margin": 0.5720033645629883,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 8.088523864746094
          },
          {
            "assigned_benefit": 0.33125050862630206,
            "delta_norm": 7.608863353729248,
            "family": "code_heavy",
            "route_margin": 0.20810467004776,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 7.95001220703125
          },
          {
            "assigned_benefit": 0.3214457829793294,
            "delta_norm": 7.1584014892578125,
            "family": "code_heavy",
            "route_margin": 0.4972362220287323,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 7.714698791503906
          },
          {
            "assigned_benefit": 0.32082366943359375,
            "delta_norm": 7.830575466156006,
            "family": "json_schema",
            "route_margin": 0.5443286895751953,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 7.69976806640625
          },
          {
            "assigned_benefit": 0.3180085817972819,
            "delta_norm": 10.745064735412598,
            "family": "code_heavy",
            "route_margin": 0.4123820662498474,
            "token": "'",
            "token_class": "quote",
            "token_total_benefit": 7.632205963134766
          }
        ],
        "total_assigned_benefit": 23.684806358379596
      },
      "layer_2_expert_7": {
        "activation_count": 1290,
        "mean_assigned_benefit": 0.03829572393693689,
        "mean_delta_norm": 7.464700270438379,
        "mean_harm": -0.022696653760104168,
        "mean_positive_benefit": 0.10219250057193226,
        "mean_route_margin": 0.415436087236848,
        "positive_benefit_rate": 0.4883720930232558,
        "prose_benefit": 2.3399024383785805,
        "structured_benefit": 46.001472743849,
        "structured_prose_benefit_ratio": 19.659568702242733,
        "token_class_benefit": {
          "brace_bracket_paren": 5.427008400360743,
          "comma_colon_semicolon": 0.6674619615077974,
          "function_signature": 1.6162640651067095,
          "identifier": 8.887747605641684,
          "indentation": -6.137788739831507,
          "json_key": 1.946637352307637,
          "json_value": 2.086937891940276,
          "newline": 3.103272413214048,
          "number": 3.0350926915804544,
          "operator": 2.073451121648153,
          "other": 2.682914741026859,
          "prose_word": 11.558710548095398,
          "quote": 15.297510464986164,
          "space": -4.703825414491197,
          "string_literal": 1.860088775555293
        },
        "token_class_counts": {
          "brace_bracket_paren": 26,
          "comma_colon_semicolon": 10,
          "function_signature": 15,
          "identifier": 171,
          "indentation": 423,
          "json_key": 31,
          "json_value": 36,
          "newline": 15,
          "number": 19,
          "operator": 12,
          "other": 16,
          "prose_word": 254,
          "quote": 49,
          "space": 186,
          "string_literal": 27
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.14390301704406738,
            "delta_norm": 7.465703964233398,
            "family": "json_schema",
            "route_margin": 0.15647178888320923,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -3.453672409057617
          },
          {
            "assigned_benefit": -0.11193382243315379,
            "delta_norm": 7.675222396850586,
            "family": "broad_lm",
            "route_margin": 0.19006913900375366,
            "token": "e",
            "token_class": "prose_word",
            "token_total_benefit": -2.686411738395691
          },
          {
            "assigned_benefit": -0.11034655446807544,
            "delta_norm": 6.639651298522949,
            "family": "code_heavy",
            "route_margin": 0.12276756763458252,
            "token": "o",
            "token_class": "identifier",
            "token_total_benefit": -2.6483173072338104
          },
          {
            "assigned_benefit": -0.109354833761851,
            "delta_norm": 8.609621047973633,
            "family": "code_heavy",
            "route_margin": 0.24691545963287354,
            "token": "-",
            "token_class": "operator",
            "token_total_benefit": -2.624516010284424
          },
          {
            "assigned_benefit": -0.10848332444826762,
            "delta_norm": 8.52377700805664,
            "family": "code_heavy",
            "route_margin": 0.944280207157135,
            "token": "n",
            "token_class": "identifier",
            "token_total_benefit": -2.603599786758423
          },
          {
            "assigned_benefit": -0.1018477330605189,
            "delta_norm": 7.966983318328857,
            "family": "broad_lm",
            "route_margin": 0.31964343786239624,
            "token": " ",
            "token_class": "indentation",
            "token_total_benefit": -2.4443455934524536
          },
          {
            "assigned_benefit": -0.09784005582332611,
            "delta_norm": 6.8296613693237305,
            "family": "code_heavy",
            "route_margin": 0.0883103609085083,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -2.3481613397598267
          },
          {
            "assigned_benefit": -0.0939420076707999,
            "delta_norm": 7.553253650665283,
            "family": "json_schema",
            "route_margin": 0.28828567266464233,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -2.2546081840991974
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.41413907210032147,
            "delta_norm": 7.776263236999512,
            "family": "code_heavy",
            "route_margin": 0.006965845823287964,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.939337730407715
          },
          {
            "assigned_benefit": 0.3995812733968099,
            "delta_norm": 7.709362030029297,
            "family": "json_schema",
            "route_margin": 0.06358170509338379,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.589950561523438
          },
          {
            "assigned_benefit": 0.3894158601760864,
            "delta_norm": 7.551911354064941,
            "family": "code_heavy",
            "route_margin": 0.217756450176239,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.345980644226074
          },
          {
            "assigned_benefit": 0.3847957452138265,
            "delta_norm": 7.391668319702148,
            "family": "code_heavy",
            "route_margin": 0.1892814040184021,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.235097885131836
          },
          {
            "assigned_benefit": 0.38011709849039715,
            "delta_norm": 6.733295440673828,
            "family": "json_schema",
            "route_margin": 0.17917686700820923,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.122810363769531
          },
          {
            "assigned_benefit": 0.3688637415568034,
            "delta_norm": 7.301908493041992,
            "family": "json_schema",
            "route_margin": 0.7814710736274719,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 8.852729797363281
          },
          {
            "assigned_benefit": 0.36609824498494464,
            "delta_norm": 8.844752311706543,
            "family": "code_heavy",
            "route_margin": 0.448361337184906,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.786357879638672
          },
          {
            "assigned_benefit": 0.36353103319803876,
            "delta_norm": 7.700839042663574,
            "family": "code_heavy",
            "route_margin": 1.117037296295166,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.72474479675293
          }
        ],
        "total_assigned_benefit": 49.40148387864859
      },
      "layer_3_expert_0": {
        "activation_count": 2070,
        "mean_assigned_benefit": 0.03893428552144426,
        "mean_delta_norm": 8.811003652747702,
        "mean_harm": -0.02310424310892189,
        "mean_positive_benefit": 0.09342910921853542,
        "mean_route_margin": 0.40717654645730905,
        "positive_benefit_rate": 0.5323671497584541,
        "prose_benefit": 5.962422954384256,
        "structured_benefit": 70.61437747192885,
        "structured_prose_benefit_ratio": 11.843235210277236,
        "token_class_benefit": {
          "brace_bracket_paren": 10.397719567331173,
          "comma_colon_semicolon": 2.106917381286621,
          "function_signature": 3.3120972414811467,
          "identifier": 14.482549408450724,
          "indentation": -7.9895992261978535,
          "json_key": 3.472168644269307,
          "json_value": 4.542203414874772,
          "newline": 0.5538041343291601,
          "number": 3.979995429515839,
          "operator": 2.1823563377062474,
          "other": 5.6212494870026894,
          "prose_word": 19.30251772049815,
          "quote": 22.803907394409187,
          "space": -6.954574423842131,
          "string_literal": 2.7806585182746253
        },
        "token_class_counts": {
          "brace_bracket_paren": 58,
          "comma_colon_semicolon": 22,
          "function_signature": 33,
          "identifier": 312,
          "indentation": 595,
          "json_key": 62,
          "json_value": 88,
          "newline": 5,
          "number": 27,
          "operator": 11,
          "other": 27,
          "prose_word": 478,
          "quote": 74,
          "space": 244,
          "string_literal": 34
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.12130660812060039,
            "delta_norm": 8.252374649047852,
            "family": "json_schema",
            "route_margin": 0.03964638710021973,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.911358594894409
          },
          {
            "assigned_benefit": -0.11974493662516277,
            "delta_norm": 7.980572700500488,
            "family": "code_heavy",
            "route_margin": 0.029857546091079712,
            "token": "5",
            "token_class": "number",
            "token_total_benefit": -2.8738784790039062
          },
          {
            "assigned_benefit": -0.11042344570159912,
            "delta_norm": 7.441285133361816,
            "family": "json_schema",
            "route_margin": 0.4117715358734131,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.650162696838379
          },
          {
            "assigned_benefit": -0.10964437325795491,
            "delta_norm": 8.827506065368652,
            "family": "code_heavy",
            "route_margin": 0.7315264940261841,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -2.631464958190918
          },
          {
            "assigned_benefit": -0.109354833761851,
            "delta_norm": 8.833199501037598,
            "family": "code_heavy",
            "route_margin": 0.4523024260997772,
            "token": "-",
            "token_class": "operator",
            "token_total_benefit": -2.624516010284424
          },
          {
            "assigned_benefit": -0.10848332444826762,
            "delta_norm": 7.606450080871582,
            "family": "code_heavy",
            "route_margin": 0.31898146867752075,
            "token": "n",
            "token_class": "identifier",
            "token_total_benefit": -2.603599786758423
          },
          {
            "assigned_benefit": -0.09847732384999593,
            "delta_norm": 6.747142791748047,
            "family": "broad_lm",
            "route_margin": 0.20751899480819702,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -2.3634557723999023
          },
          {
            "assigned_benefit": -0.09784005582332611,
            "delta_norm": 8.916084289550781,
            "family": "code_heavy",
            "route_margin": 0.7592385411262512,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -2.3481613397598267
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.4194428126017253,
            "delta_norm": 7.303606033325195,
            "family": "json_schema",
            "route_margin": 0.04512906074523926,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.066627502441406
          },
          {
            "assigned_benefit": 0.41413907210032147,
            "delta_norm": 8.009446144104004,
            "family": "code_heavy",
            "route_margin": 0.4171554148197174,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.939337730407715
          },
          {
            "assigned_benefit": 0.3894158601760864,
            "delta_norm": 8.00074577331543,
            "family": "code_heavy",
            "route_margin": 0.016542255878448486,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.345980644226074
          },
          {
            "assigned_benefit": 0.38902703921000165,
            "delta_norm": 7.4277167320251465,
            "family": "code_heavy",
            "route_margin": 0.09862160682678223,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.336648941040039
          },
          {
            "assigned_benefit": 0.38800891240437824,
            "delta_norm": 9.22846794128418,
            "family": "code_heavy",
            "route_margin": 0.12327295541763306,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.312213897705078
          },
          {
            "assigned_benefit": 0.3847957452138265,
            "delta_norm": 8.262009620666504,
            "family": "code_heavy",
            "route_margin": 0.20858263969421387,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.235097885131836
          },
          {
            "assigned_benefit": 0.38402652740478516,
            "delta_norm": 8.50648021697998,
            "family": "code_heavy",
            "route_margin": 0.007353007793426514,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 9.216636657714844
          },
          {
            "assigned_benefit": 0.3795582453409831,
            "delta_norm": 7.600737571716309,
            "family": "json_schema",
            "route_margin": 0.17969012260437012,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.109397888183594
          }
        ],
        "total_assigned_benefit": 80.59397102938962
      },
      "layer_3_expert_1": {
        "activation_count": 471,
        "mean_assigned_benefit": 0.05795475986284729,
        "mean_delta_norm": 7.98193334672608,
        "mean_harm": -0.025528444349144894,
        "mean_positive_benefit": 0.08811487699145715,
        "mean_route_margin": 0.4230627254948748,
        "positive_benefit_rate": 0.7346072186836518,
        "prose_benefit": 8.781155665343606,
        "structured_benefit": 17.6078126592102,
        "structured_prose_benefit_ratio": 2.0051817016184517,
        "token_class_benefit": {
          "brace_bracket_paren": 1.6275055011113484,
          "comma_colon_semicolon": 1.1135438978672028,
          "function_signature": 1.3366601069768267,
          "identifier": 4.896727687368791,
          "json_key": 0.8022953768571218,
          "json_value": 0.5757999569177628,
          "newline": 2.436728740748,
          "number": 0.7385225296020508,
          "operator": 0.6251324415206909,
          "other": 3.120125363270442,
          "prose_word": 8.316672003517548,
          "quote": 2.3668793042500815,
          "space": -1.7479181305970992,
          "string_literal": 1.088017115990321
        },
        "token_class_counts": {
          "brace_bracket_paren": 7,
          "comma_colon_semicolon": 12,
          "function_signature": 8,
          "identifier": 90,
          "json_key": 8,
          "json_value": 10,
          "newline": 15,
          "number": 6,
          "operator": 5,
          "other": 14,
          "prose_word": 168,
          "quote": 8,
          "space": 104,
          "string_literal": 16
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.10804811120033264,
            "delta_norm": 8.664281845092773,
            "family": "broad_lm",
            "route_margin": 0.49586254358291626,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -2.5931546688079834
          },
          {
            "assigned_benefit": -0.10159913450479507,
            "delta_norm": 10.860763549804688,
            "family": "broad_lm",
            "route_margin": 0.7780467867851257,
            "token": "p",
            "token_class": "prose_word",
            "token_total_benefit": -2.438379228115082
          },
          {
            "assigned_benefit": -0.0805702159802119,
            "delta_norm": 7.437509536743164,
            "family": "code_heavy",
            "route_margin": 0.40356874465942383,
            "token": "t",
            "token_class": "identifier",
            "token_total_benefit": -1.9336851835250854
          },
          {
            "assigned_benefit": -0.07861356933911641,
            "delta_norm": 8.283802032470703,
            "family": "code_heavy",
            "route_margin": 0.11946266889572144,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.886725664138794
          },
          {
            "assigned_benefit": -0.07303215439120929,
            "delta_norm": 10.657631874084473,
            "family": "code_heavy",
            "route_margin": 0.7232619524002075,
            "token": "p",
            "token_class": "identifier",
            "token_total_benefit": -1.7527717053890228
          },
          {
            "assigned_benefit": -0.07064068565766017,
            "delta_norm": 7.387406826019287,
            "family": "broad_lm",
            "route_margin": 0.21851465106010437,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -1.695376455783844
          },
          {
            "assigned_benefit": -0.06819106638431549,
            "delta_norm": 10.947892189025879,
            "family": "code_heavy",
            "route_margin": 0.3458364009857178,
            "token": "p",
            "token_class": "identifier",
            "token_total_benefit": -1.6365855932235718
          },
          {
            "assigned_benefit": -0.06702599922815959,
            "delta_norm": 7.70506477355957,
            "family": "broad_lm",
            "route_margin": 0.27120059728622437,
            "token": "n",
            "token_class": "prose_word",
            "token_total_benefit": -1.60862398147583
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.3964542547861735,
            "delta_norm": 8.768668174743652,
            "family": "code_heavy",
            "route_margin": 0.9270601868629456,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.514902114868164
          },
          {
            "assigned_benefit": 0.3903733491897583,
            "delta_norm": 6.7276716232299805,
            "family": "code_heavy",
            "route_margin": 0.18599975109100342,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.3689603805542
          },
          {
            "assigned_benefit": 0.36769771575927734,
            "delta_norm": 7.936587810516357,
            "family": "code_heavy",
            "route_margin": 0.23808833956718445,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 8.824745178222656
          },
          {
            "assigned_benefit": 0.3460699717203776,
            "delta_norm": 6.8492231369018555,
            "family": "json_schema",
            "route_margin": 0.1686118245124817,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 8.305679321289062
          },
          {
            "assigned_benefit": 0.33899720509847003,
            "delta_norm": 7.511991500854492,
            "family": "code_heavy",
            "route_margin": 0.420383095741272,
            "token": "\"",
            "token_class": "function_signature",
            "token_total_benefit": 8.135932922363281
          },
          {
            "assigned_benefit": 0.33125050862630206,
            "delta_norm": 9.046415328979492,
            "family": "code_heavy",
            "route_margin": 0.7166216373443604,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 7.95001220703125
          },
          {
            "assigned_benefit": 0.33030128479003906,
            "delta_norm": 5.953181266784668,
            "family": "code_heavy",
            "route_margin": 1.4657111167907715,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 7.9272308349609375
          },
          {
            "assigned_benefit": 0.32466332117716473,
            "delta_norm": 8.061431884765625,
            "family": "code_heavy",
            "route_margin": 0.06529347598552704,
            "token": "'",
            "token_class": "quote",
            "token_total_benefit": 7.791919708251953
          }
        ],
        "total_assigned_benefit": 27.29669189540107
      },
      "layer_3_expert_2": {
        "activation_count": 750,
        "mean_assigned_benefit": 0.05372585981339218,
        "mean_delta_norm": 9.532571313222249,
        "mean_harm": -0.03570899749001374,
        "mean_positive_benefit": 0.08558601693594367,
        "mean_route_margin": 0.5089952653547128,
        "positive_benefit_rate": 0.7373333333333333,
        "prose_benefit": 11.965622098806012,
        "structured_benefit": 27.14419192355125,
        "structured_prose_benefit_ratio": 2.2685148920305473,
        "token_class_benefit": {
          "brace_bracket_paren": 1.700449069341024,
          "comma_colon_semicolon": 1.1907209654649096,
          "function_signature": 1.3947980304559071,
          "identifier": 8.797783754145094,
          "json_key": 3.3875656127929683,
          "json_value": 1.1859715093548098,
          "newline": 1.6376650681098304,
          "number": 0.48278693358103436,
          "operator": 0.14273675282796225,
          "other": 2.2994805773099265,
          "prose_word": 14.693712011600534,
          "quote": 3.615577220916748,
          "space": -3.8429896524176,
          "string_literal": 3.6081370065609617
        },
        "token_class_counts": {
          "brace_bracket_paren": 9,
          "comma_colon_semicolon": 17,
          "function_signature": 16,
          "identifier": 161,
          "json_key": 35,
          "json_value": 26,
          "newline": 11,
          "number": 4,
          "operator": 1,
          "other": 9,
          "prose_word": 278,
          "quote": 12,
          "space": 131,
          "string_literal": 40
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.14390301704406738,
            "delta_norm": 9.999387741088867,
            "family": "json_schema",
            "route_margin": 0.9460335969924927,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -3.453672409057617
          },
          {
            "assigned_benefit": -0.14381763339042664,
            "delta_norm": 12.409355163574219,
            "family": "broad_lm",
            "route_margin": 1.2961673736572266,
            "token": "c",
            "token_class": "prose_word",
            "token_total_benefit": -3.4516232013702393
          },
          {
            "assigned_benefit": -0.1176329255104065,
            "delta_norm": 10.687642097473145,
            "family": "broad_lm",
            "route_margin": 1.3751041889190674,
            "token": "o",
            "token_class": "prose_word",
            "token_total_benefit": -2.823190212249756
          },
          {
            "assigned_benefit": -0.11105093856652577,
            "delta_norm": 11.308865547180176,
            "family": "broad_lm",
            "route_margin": 0.42738986015319824,
            "token": "o",
            "token_class": "prose_word",
            "token_total_benefit": -2.6652225255966187
          },
          {
            "assigned_benefit": -0.11034655446807544,
            "delta_norm": 10.673539161682129,
            "family": "code_heavy",
            "route_margin": 0.7438687682151794,
            "token": "o",
            "token_class": "identifier",
            "token_total_benefit": -2.6483173072338104
          },
          {
            "assigned_benefit": -0.10949698835611343,
            "delta_norm": 10.199074745178223,
            "family": "broad_lm",
            "route_margin": 1.645320177078247,
            "token": "o",
            "token_class": "prose_word",
            "token_total_benefit": -2.6279277205467224
          },
          {
            "assigned_benefit": -0.10870074232419331,
            "delta_norm": 10.518208503723145,
            "family": "broad_lm",
            "route_margin": 0.9195699095726013,
            "token": "o",
            "token_class": "prose_word",
            "token_total_benefit": -2.6088178157806396
          },
          {
            "assigned_benefit": -0.10707541306813557,
            "delta_norm": 8.356225967407227,
            "family": "code_heavy",
            "route_margin": 0.6485642194747925,
            "token": "s",
            "token_class": "identifier",
            "token_total_benefit": -2.569809913635254
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.4192720651626587,
            "delta_norm": 6.862532615661621,
            "family": "code_heavy",
            "route_margin": 0.18006806075572968,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 10.062529563903809
          },
          {
            "assigned_benefit": 0.3464348316192627,
            "delta_norm": 7.909874439239502,
            "family": "code_heavy",
            "route_margin": 0.3039291799068451,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.314435958862305
          },
          {
            "assigned_benefit": 0.3433542251586914,
            "delta_norm": 9.999225616455078,
            "family": "json_schema",
            "route_margin": 0.755993127822876,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 8.240501403808594
          },
          {
            "assigned_benefit": 0.3432128429412842,
            "delta_norm": 9.687456130981445,
            "family": "code_heavy",
            "route_margin": 0.45701244473457336,
            "token": "(",
            "token_class": "function_signature",
            "token_total_benefit": 8.23710823059082
          },
          {
            "assigned_benefit": 0.3410816192626953,
            "delta_norm": 9.275177001953125,
            "family": "code_heavy",
            "route_margin": 0.152665376663208,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 8.185958862304688
          },
          {
            "assigned_benefit": 0.3353669246037801,
            "delta_norm": 10.411092758178711,
            "family": "code_heavy",
            "route_margin": 0.5497925877571106,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.048806190490723
          },
          {
            "assigned_benefit": 0.3318033218383789,
            "delta_norm": 8.040169715881348,
            "family": "code_heavy",
            "route_margin": 0.09681069850921631,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 7.963279724121094
          },
          {
            "assigned_benefit": 0.3223867416381836,
            "delta_norm": 8.583456039428711,
            "family": "json_schema",
            "route_margin": 0.07994639873504639,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 7.737281799316406
          }
        ],
        "total_assigned_benefit": 40.294394860044136
      },
      "layer_3_expert_3": {
        "activation_count": 372,
        "mean_assigned_benefit": 0.060008447044946796,
        "mean_delta_norm": 8.973569212421294,
        "mean_harm": -0.025546709811964694,
        "mean_positive_benefit": 0.08573482288303907,
        "mean_route_margin": 0.3690774227262184,
        "positive_benefit_rate": 0.7688172043010753,
        "prose_benefit": 6.5788146537296,
        "structured_benefit": 16.137644512007835,
        "structured_prose_benefit_ratio": 2.4529714487182326,
        "token_class_benefit": {
          "brace_bracket_paren": 0.6011368830998739,
          "comma_colon_semicolon": 1.513443370660146,
          "function_signature": 0.32094569007555646,
          "identifier": 3.716395594179628,
          "json_key": 2.2923933664957685,
          "json_value": 0.5394516537586848,
          "newline": 2.1496382753553007,
          "number": 0.6112292210261028,
          "operator": 1.5520130793253581,
          "other": 0.6255557735761006,
          "prose_word": 6.280604901413126,
          "quote": 2.1729408899943037,
          "space": -0.7206628862768412,
          "string_literal": 0.6680564880371095
        },
        "token_class_counts": {
          "brace_bracket_paren": 3,
          "comma_colon_semicolon": 15,
          "function_signature": 3,
          "identifier": 76,
          "json_key": 25,
          "json_value": 15,
          "newline": 14,
          "number": 5,
          "operator": 8,
          "other": 4,
          "prose_word": 137,
          "quote": 6,
          "space": 49,
          "string_literal": 12
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.17974231019616127,
            "delta_norm": 8.273972511291504,
            "family": "broad_lm",
            "route_margin": 0.8679388761520386,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -4.3138154447078705
          },
          {
            "assigned_benefit": -0.10358279943466187,
            "delta_norm": 8.585789680480957,
            "family": "json_schema",
            "route_margin": 0.23407089710235596,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.4859871864318848
          },
          {
            "assigned_benefit": -0.09525191783905029,
            "delta_norm": 7.64438533782959,
            "family": "json_schema",
            "route_margin": 0.011203765869140625,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.286046028137207
          },
          {
            "assigned_benefit": -0.09491795673966408,
            "delta_norm": 8.109350204467773,
            "family": "broad_lm",
            "route_margin": 0.11820083856582642,
            "token": "l",
            "token_class": "prose_word",
            "token_total_benefit": -2.278030961751938
          },
          {
            "assigned_benefit": -0.07676849762598674,
            "delta_norm": 8.79094123840332,
            "family": "code_heavy",
            "route_margin": 0.06642603874206543,
            "token": "a",
            "token_class": "identifier",
            "token_total_benefit": -1.8424439430236816
          },
          {
            "assigned_benefit": -0.06532086928685506,
            "delta_norm": 8.540253639221191,
            "family": "code_heavy",
            "route_margin": 0.3340195417404175,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.5677008628845215
          },
          {
            "assigned_benefit": -0.06350993116696675,
            "delta_norm": 8.338022232055664,
            "family": "json_schema",
            "route_margin": 0.35001954436302185,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.5242383480072021
          },
          {
            "assigned_benefit": -0.06282715996106465,
            "delta_norm": 8.768672943115234,
            "family": "code_heavy",
            "route_margin": 0.6019534468650818,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.5078518390655518
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.4434954325358073,
            "delta_norm": 7.8891282081604,
            "family": "json_schema",
            "route_margin": 0.05824553966522217,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.643890380859375
          },
          {
            "assigned_benefit": 0.3949778874715169,
            "delta_norm": 7.557074546813965,
            "family": "json_schema",
            "route_margin": 0.023997902870178223,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.479469299316406
          },
          {
            "assigned_benefit": 0.38860607147216797,
            "delta_norm": 7.819101810455322,
            "family": "json_schema",
            "route_margin": 0.0019383430480957031,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.326545715332031
          },
          {
            "assigned_benefit": 0.3718280792236328,
            "delta_norm": 8.371795654296875,
            "family": "json_schema",
            "route_margin": 0.5413706302642822,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 8.923873901367188
          },
          {
            "assigned_benefit": 0.3553175131479899,
            "delta_norm": 8.491011619567871,
            "family": "code_heavy",
            "route_margin": 0.14462560415267944,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.527620315551758
          },
          {
            "assigned_benefit": 0.3087804714838664,
            "delta_norm": 8.37692642211914,
            "family": "code_heavy",
            "route_margin": 0.040099263191223145,
            "token": "_",
            "token_class": "identifier",
            "token_total_benefit": 7.410731315612793
          },
          {
            "assigned_benefit": 0.3042612075805664,
            "delta_norm": 8.44124984741211,
            "family": "json_schema",
            "route_margin": 0.26766061782836914,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 7.302268981933594
          },
          {
            "assigned_benefit": 0.30092716217041016,
            "delta_norm": 8.47551155090332,
            "family": "code_heavy",
            "route_margin": 0.2530134916305542,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 7.222251892089844
          }
        ],
        "total_assigned_benefit": 22.323142300720207
      },
      "layer_3_expert_4": {
        "activation_count": 456,
        "mean_assigned_benefit": 0.07149809099253904,
        "mean_delta_norm": 10.452424072382742,
        "mean_harm": -0.026890545690623234,
        "mean_positive_benefit": 0.11073282341220507,
        "mean_route_margin": 0.40559164557213845,
        "positive_benefit_rate": 0.7149122807017544,
        "prose_benefit": 5.912434638934381,
        "structured_benefit": 25.04445983996322,
        "structured_prose_benefit_ratio": 4.235896271062553,
        "token_class_benefit": {
          "brace_bracket_paren": 0.6341927324732145,
          "comma_colon_semicolon": 2.419017627835274,
          "function_signature": 0.9794717406233152,
          "identifier": 4.261112158497175,
          "json_key": 0.4040878117084503,
          "json_value": 0.36847363909085584,
          "newline": 9.388673097196522,
          "number": 0.792477329572042,
          "operator": 0.3680493036905924,
          "other": 4.7762632143373285,
          "prose_word": 4.341103636970123,
          "quote": 3.1839526494344077,
          "space": -1.5586971986728415,
          "string_literal": 2.2449517498413725
        },
        "token_class_counts": {
          "brace_bracket_paren": 6,
          "comma_colon_semicolon": 25,
          "function_signature": 13,
          "identifier": 88,
          "json_key": 5,
          "json_value": 8,
          "newline": 47,
          "number": 9,
          "operator": 2,
          "other": 20,
          "prose_word": 89,
          "quote": 11,
          "space": 112,
          "string_literal": 21
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.12831215063730875,
            "delta_norm": 8.396484375,
            "family": "json_schema",
            "route_margin": 0.11808717250823975,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -3.07949161529541
          },
          {
            "assigned_benefit": -0.10410678386688232,
            "delta_norm": 8.60232925415039,
            "family": "json_schema",
            "route_margin": 0.07224392890930176,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.498562812805176
          },
          {
            "assigned_benefit": -0.10388837258021037,
            "delta_norm": 7.509316444396973,
            "family": "code_heavy",
            "route_margin": 0.18458545207977295,
            "token": "d",
            "token_class": "string_literal",
            "token_total_benefit": -2.493320941925049
          },
          {
            "assigned_benefit": -0.08489630619684856,
            "delta_norm": 9.376387596130371,
            "family": "code_heavy",
            "route_margin": 0.22671163082122803,
            "token": "w",
            "token_class": "identifier",
            "token_total_benefit": -2.0375113487243652
          },
          {
            "assigned_benefit": -0.07794865469137828,
            "delta_norm": 9.40460205078125,
            "family": "broad_lm",
            "route_margin": 0.1104581356048584,
            "token": "l",
            "token_class": "prose_word",
            "token_total_benefit": -1.8707677125930786
          },
          {
            "assigned_benefit": -0.07568599780400594,
            "delta_norm": 8.281218528747559,
            "family": "json_schema",
            "route_margin": 0.04729534685611725,
            "token": "a",
            "token_class": "json_value",
            "token_total_benefit": -1.8164639472961426
          },
          {
            "assigned_benefit": -0.07461561759312947,
            "delta_norm": 7.492528915405273,
            "family": "code_heavy",
            "route_margin": 0.14273083209991455,
            "token": "d",
            "token_class": "string_literal",
            "token_total_benefit": -1.7907748222351074
          },
          {
            "assigned_benefit": -0.07431606451670329,
            "delta_norm": 8.607940673828125,
            "family": "json_schema",
            "route_margin": 0.14598870277404785,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -1.783585548400879
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.3683640956878662,
            "delta_norm": 14.276128768920898,
            "family": "json_schema",
            "route_margin": 1.269972801208496,
            "token": "\\n",
            "token_class": "newline",
            "token_total_benefit": 8.840738296508789
          },
          {
            "assigned_benefit": 0.33861692746480304,
            "delta_norm": 13.757223129272461,
            "family": "json_schema",
            "route_margin": 0.699894905090332,
            "token": "\\n",
            "token_class": "newline",
            "token_total_benefit": 8.126806259155273
          },
          {
            "assigned_benefit": 0.3352521260579427,
            "delta_norm": 9.338180541992188,
            "family": "code_heavy",
            "route_margin": 0.020670413970947266,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 8.046051025390625
          },
          {
            "assigned_benefit": 0.33243274688720703,
            "delta_norm": 8.798748970031738,
            "family": "code_heavy",
            "route_margin": 0.31873929500579834,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 7.978385925292969
          },
          {
            "assigned_benefit": 0.3320792516072591,
            "delta_norm": 10.429634094238281,
            "family": "code_heavy",
            "route_margin": 0.6644102334976196,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 7.969902038574219
          },
          {
            "assigned_benefit": 0.32963212331136066,
            "delta_norm": 8.182143211364746,
            "family": "code_heavy",
            "route_margin": 0.38765668869018555,
            "token": "\\",
            "token_class": "string_literal",
            "token_total_benefit": 7.911170959472656
          },
          {
            "assigned_benefit": 0.32633060216903687,
            "delta_norm": 14.557840347290039,
            "family": "json_schema",
            "route_margin": 1.0988227128982544,
            "token": "\\n",
            "token_class": "newline",
            "token_total_benefit": 7.831934452056885
          },
          {
            "assigned_benefit": 0.32611862818400067,
            "delta_norm": 14.207818031311035,
            "family": "json_schema",
            "route_margin": 0.3939740061759949,
            "token": "\\n",
            "token_class": "newline",
            "token_total_benefit": 7.826847076416016
          }
        ],
        "total_assigned_benefit": 32.6031294925978
      },
      "layer_3_expert_5": {
        "activation_count": 1139,
        "mean_assigned_benefit": 0.06317236440733837,
        "mean_delta_norm": 7.480017335923541,
        "mean_harm": -0.017023961324032326,
        "mean_positive_benefit": 0.12054172392902676,
        "mean_route_margin": 0.3410983780976238,
        "positive_benefit_rate": 0.5829675153643546,
        "prose_benefit": 9.437337512703975,
        "structured_benefit": 59.218912277370734,
        "structured_prose_benefit_ratio": 6.274959669255636,
        "token_class_benefit": {
          "brace_bracket_paren": 5.835907317698001,
          "comma_colon_semicolon": 1.7035525639851883,
          "function_signature": 3.5777244766553244,
          "identifier": 9.571965487053003,
          "indentation": -2.662692644943793,
          "json_key": 4.230175259212653,
          "json_value": 2.8510278860727944,
          "newline": 6.70838296910127,
          "number": 1.5833816329638164,
          "operator": 2.2513385017712912,
          "other": 4.9689557433309055,
          "prose_word": 13.110766937335324,
          "quote": 18.87928915023804,
          "space": -2.682619253134666,
          "string_literal": 2.0261670326193175
        },
        "token_class_counts": {
          "brace_bracket_paren": 28,
          "comma_colon_semicolon": 21,
          "function_signature": 22,
          "identifier": 157,
          "indentation": 300,
          "json_key": 44,
          "json_value": 38,
          "newline": 31,
          "number": 10,
          "operator": 12,
          "other": 23,
          "prose_word": 210,
          "quote": 60,
          "space": 155,
          "string_literal": 28
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.11193382243315379,
            "delta_norm": 8.820598602294922,
            "family": "broad_lm",
            "route_margin": 0.7156295776367188,
            "token": "e",
            "token_class": "prose_word",
            "token_total_benefit": -2.686411738395691
          },
          {
            "assigned_benefit": -0.10397198796272278,
            "delta_norm": 8.148430824279785,
            "family": "json_schema",
            "route_margin": 0.08107906579971313,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.4953277111053467
          },
          {
            "assigned_benefit": -0.1018477330605189,
            "delta_norm": 6.846462726593018,
            "family": "broad_lm",
            "route_margin": 0.42246365547180176,
            "token": " ",
            "token_class": "indentation",
            "token_total_benefit": -2.4443455934524536
          },
          {
            "assigned_benefit": -0.09138673543930054,
            "delta_norm": 7.256458759307861,
            "family": "json_schema",
            "route_margin": 0.14697158336639404,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.193281650543213
          },
          {
            "assigned_benefit": -0.08751490712165833,
            "delta_norm": 7.218775749206543,
            "family": "json_schema",
            "route_margin": 0.34795546531677246,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.1003577709198
          },
          {
            "assigned_benefit": -0.08452899257342021,
            "delta_norm": 7.673430442810059,
            "family": "broad_lm",
            "route_margin": 0.13792651891708374,
            "token": "w",
            "token_class": "prose_word",
            "token_total_benefit": -2.028695821762085
          },
          {
            "assigned_benefit": -0.08133397996425629,
            "delta_norm": 7.447453498840332,
            "family": "json_schema",
            "route_margin": 0.302304744720459,
            "token": "d",
            "token_class": "json_key",
            "token_total_benefit": -1.9520155191421509
          },
          {
            "assigned_benefit": -0.07646821935971577,
            "delta_norm": 8.29313850402832,
            "family": "json_schema",
            "route_margin": 0.27698367834091187,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.8352372646331787
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.4348748524983724,
            "delta_norm": 7.750196933746338,
            "family": "json_schema",
            "route_margin": 0.5909568667411804,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.436996459960938
          },
          {
            "assigned_benefit": 0.42559146881103516,
            "delta_norm": 8.35921573638916,
            "family": "json_schema",
            "route_margin": 0.3625180125236511,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.214195251464844
          },
          {
            "assigned_benefit": 0.40491771697998047,
            "delta_norm": 7.929327964782715,
            "family": "json_schema",
            "route_margin": 0.011515915393829346,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.718025207519531
          },
          {
            "assigned_benefit": 0.40347035725911456,
            "delta_norm": 7.436077117919922,
            "family": "json_schema",
            "route_margin": 1.426112413406372,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.68328857421875
          },
          {
            "assigned_benefit": 0.40207378069559735,
            "delta_norm": 9.332077026367188,
            "family": "code_heavy",
            "route_margin": 0.5744197964668274,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.649770736694336
          },
          {
            "assigned_benefit": 0.3999309539794922,
            "delta_norm": 8.381733894348145,
            "family": "json_schema",
            "route_margin": 0.16331183910369873,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.598342895507812
          },
          {
            "assigned_benefit": 0.3989645640055339,
            "delta_norm": 7.587557792663574,
            "family": "json_schema",
            "route_margin": 0.06410789489746094,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.575149536132812
          },
          {
            "assigned_benefit": 0.39834149678548175,
            "delta_norm": 8.432167053222656,
            "family": "json_schema",
            "route_margin": 0.07534313201904297,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.560195922851562
          }
        ],
        "total_assigned_benefit": 71.9533230599584
      },
      "layer_3_expert_6": {
        "activation_count": 551,
        "mean_assigned_benefit": 0.05846710273700483,
        "mean_delta_norm": 7.773139533892734,
        "mean_harm": -0.03540582566225349,
        "mean_positive_benefit": 0.09262383658524988,
        "mean_route_margin": 0.33904724066465175,
        "positive_benefit_rate": 0.7332123411978222,
        "prose_benefit": 4.159655684876875,
        "structured_benefit": 27.001970919935637,
        "structured_prose_benefit_ratio": 6.491395674431859,
        "token_class_benefit": {
          "brace_bracket_paren": 0.8582569360733033,
          "comma_colon_semicolon": 4.120403528213501,
          "function_signature": 1.6002659673492114,
          "identifier": 5.756446483234562,
          "indentation": -0.04300150523583094,
          "json_key": 1.6969722509384153,
          "json_value": 0.7259352733381093,
          "newline": 1.1631858994563422,
          "number": 0.3578778107961019,
          "operator": 0.6544168392817179,
          "other": 1.5798747738202414,
          "prose_word": 5.058351072172324,
          "quote": 8.416081110636394,
          "space": -1.3818216526027152,
          "string_literal": 1.6521288206179938
        },
        "token_class_counts": {
          "brace_bracket_paren": 6,
          "comma_colon_semicolon": 39,
          "function_signature": 14,
          "identifier": 142,
          "indentation": 5,
          "json_key": 29,
          "json_value": 18,
          "newline": 6,
          "number": 3,
          "operator": 4,
          "other": 9,
          "prose_word": 135,
          "quote": 27,
          "space": 88,
          "string_literal": 26
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.10809943079948425,
            "delta_norm": 7.750304222106934,
            "family": "json_schema",
            "route_margin": 0.14229488372802734,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.594386339187622
          },
          {
            "assigned_benefit": -0.10029297073682149,
            "delta_norm": 6.372035026550293,
            "family": "json_schema",
            "route_margin": 0.043302297592163086,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.407031297683716
          },
          {
            "assigned_benefit": -0.09623692433039348,
            "delta_norm": 6.259110927581787,
            "family": "json_schema",
            "route_margin": 0.06005978584289551,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.3096861839294434
          },
          {
            "assigned_benefit": -0.0962066650390625,
            "delta_norm": 7.023671627044678,
            "family": "json_schema",
            "route_margin": 0.27488458156585693,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.3089599609375
          },
          {
            "assigned_benefit": -0.0938494602839152,
            "delta_norm": 6.4772138595581055,
            "family": "json_schema",
            "route_margin": 0.019411206245422363,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.252387046813965
          },
          {
            "assigned_benefit": -0.0938490629196167,
            "delta_norm": 6.4772138595581055,
            "family": "json_schema",
            "route_margin": 0.019411325454711914,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.252377510070801
          },
          {
            "assigned_benefit": -0.09053297837575276,
            "delta_norm": 6.39699649810791,
            "family": "json_schema",
            "route_margin": 0.587954044342041,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.1727914810180664
          },
          {
            "assigned_benefit": -0.09014518062273662,
            "delta_norm": 7.208906173706055,
            "family": "json_schema",
            "route_margin": 0.16213321685791016,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.1634843349456787
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.3612794876098633,
            "delta_norm": 8.085132598876953,
            "family": "json_schema",
            "route_margin": 0.02410408854484558,
            "token": "\\n",
            "token_class": "newline",
            "token_total_benefit": 8.670707702636719
          },
          {
            "assigned_benefit": 0.3590370814005534,
            "delta_norm": 6.03034782409668,
            "family": "code_heavy",
            "route_margin": 0.11183929443359375,
            "token": "'",
            "token_class": "quote",
            "token_total_benefit": 8.616889953613281
          },
          {
            "assigned_benefit": 0.3566751480102539,
            "delta_norm": 6.823914051055908,
            "family": "code_heavy",
            "route_margin": 0.26915204524993896,
            "token": "\"",
            "token_class": "function_signature",
            "token_total_benefit": 8.560203552246094
          },
          {
            "assigned_benefit": 0.3564949035644531,
            "delta_norm": 6.033674716949463,
            "family": "code_heavy",
            "route_margin": 0.5051040649414062,
            "token": "\\",
            "token_class": "function_signature",
            "token_total_benefit": 8.555877685546875
          },
          {
            "assigned_benefit": 0.3438250223795573,
            "delta_norm": 7.972209930419922,
            "family": "code_heavy",
            "route_margin": 0.29077112674713135,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 8.251800537109375
          },
          {
            "assigned_benefit": 0.33671798308690387,
            "delta_norm": 6.942943572998047,
            "family": "code_heavy",
            "route_margin": 0.46016716957092285,
            "token": "_",
            "token_class": "identifier",
            "token_total_benefit": 8.081231594085693
          },
          {
            "assigned_benefit": 0.33442242940266925,
            "delta_norm": 8.392389297485352,
            "family": "json_schema",
            "route_margin": 0.37287139892578125,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 8.026138305664062
          },
          {
            "assigned_benefit": 0.32794443766276044,
            "delta_norm": 8.349067687988281,
            "family": "code_heavy",
            "route_margin": 0.5580799579620361,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 7.87066650390625
          }
        ],
        "total_assigned_benefit": 32.21537360808966
      },
      "layer_3_expert_7": {
        "activation_count": 335,
        "mean_assigned_benefit": 0.06834090015276413,
        "mean_delta_norm": 8.23869971659646,
        "mean_harm": -0.040344072712792285,
        "mean_positive_benefit": 0.10300028126343369,
        "mean_route_margin": 0.32496319542180246,
        "positive_benefit_rate": 0.7582089552238805,
        "prose_benefit": 3.907131847537434,
        "structured_benefit": 15.660952714582288,
        "structured_prose_benefit_ratio": 4.008299009528687,
        "token_class_benefit": {
          "brace_bracket_paren": 0.7894161939620972,
          "comma_colon_semicolon": 2.248421649138133,
          "function_signature": 0.6447975138823192,
          "identifier": 4.055068634450437,
          "indentation": -0.3463764836390813,
          "json_key": 0.6642752935489019,
          "json_value": 0.396175667643547,
          "newline": 1.6845441659291585,
          "number": 1.0302700201670327,
          "operator": 0.30125681559244794,
          "other": 3.625381757117187,
          "prose_word": 5.24905319015185,
          "quote": 2.0485814412434897,
          "space": -1.2948096270362535,
          "string_literal": 1.798145319024722
        },
        "token_class_counts": {
          "brace_bracket_paren": 5,
          "comma_colon_semicolon": 22,
          "function_signature": 6,
          "identifier": 69,
          "indentation": 9,
          "json_key": 9,
          "json_value": 11,
          "newline": 8,
          "number": 7,
          "operator": 2,
          "other": 16,
          "prose_word": 101,
          "quote": 6,
          "space": 45,
          "string_literal": 19
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.13103054463863373,
            "delta_norm": 8.384095191955566,
            "family": "code_heavy",
            "route_margin": 0.131553053855896,
            "token": "g",
            "token_class": "identifier",
            "token_total_benefit": -3.1447330713272095
          },
          {
            "assigned_benefit": -0.1258842075864474,
            "delta_norm": 7.831441879272461,
            "family": "broad_lm",
            "route_margin": 0.2539209723472595,
            "token": "m",
            "token_class": "prose_word",
            "token_total_benefit": -3.0212209820747375
          },
          {
            "assigned_benefit": -0.11696084340413411,
            "delta_norm": 7.810133934020996,
            "family": "json_schema",
            "route_margin": 0.37337493896484375,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.8070602416992188
          },
          {
            "assigned_benefit": -0.09828927119572957,
            "delta_norm": 7.563308238983154,
            "family": "json_schema",
            "route_margin": 0.12307751178741455,
            "token": " ",
            "token_class": "indentation",
            "token_total_benefit": -2.3589425086975098
          },
          {
            "assigned_benefit": -0.09154083828131358,
            "delta_norm": 7.8717827796936035,
            "family": "json_schema",
            "route_margin": 0.05617201328277588,
            "token": "d",
            "token_class": "json_value",
            "token_total_benefit": -2.196980118751526
          },
          {
            "assigned_benefit": -0.08743790785471599,
            "delta_norm": 7.860574722290039,
            "family": "code_heavy",
            "route_margin": 0.09831416606903076,
            "token": "d",
            "token_class": "string_literal",
            "token_total_benefit": -2.0985097885131836
          },
          {
            "assigned_benefit": -0.084659809867541,
            "delta_norm": 8.273591041564941,
            "family": "json_schema",
            "route_margin": 0.36901283264160156,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.031835436820984
          },
          {
            "assigned_benefit": -0.08465861777464549,
            "delta_norm": 8.273590087890625,
            "family": "json_schema",
            "route_margin": 0.36901259422302246,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.0318068265914917
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.3995812733968099,
            "delta_norm": 8.682563781738281,
            "family": "json_schema",
            "route_margin": 0.25406181812286377,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.589950561523438
          },
          {
            "assigned_benefit": 0.38011709849039715,
            "delta_norm": 8.517992973327637,
            "family": "json_schema",
            "route_margin": 0.384344220161438,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.122810363769531
          },
          {
            "assigned_benefit": 0.3771365483601888,
            "delta_norm": 9.099066734313965,
            "family": "json_schema",
            "route_margin": 0.30506783723831177,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.051277160644531
          },
          {
            "assigned_benefit": 0.3370199203491211,
            "delta_norm": 8.078592300415039,
            "family": "code_heavy",
            "route_margin": 0.061024248600006104,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 8.088478088378906
          },
          {
            "assigned_benefit": 0.32917070388793945,
            "delta_norm": 9.101635932922363,
            "family": "code_heavy",
            "route_margin": 0.48696255683898926,
            "token": "_",
            "token_class": "identifier",
            "token_total_benefit": 7.900096893310547
          },
          {
            "assigned_benefit": 0.3219327926635742,
            "delta_norm": 9.801393508911133,
            "family": "code_heavy",
            "route_margin": 0.2681978940963745,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 7.726387023925781
          },
          {
            "assigned_benefit": 0.3109825650850932,
            "delta_norm": 9.795296669006348,
            "family": "json_schema",
            "route_margin": 1.0302274227142334,
            "token": "\\n",
            "token_class": "newline",
            "token_total_benefit": 7.463581562042236
          },
          {
            "assigned_benefit": 0.30414072672526044,
            "delta_norm": 7.437285423278809,
            "family": "code_heavy",
            "route_margin": 0.296673059463501,
            "token": "\\",
            "token_class": "string_literal",
            "token_total_benefit": 7.29937744140625
          }
        ],
        "total_assigned_benefit": 22.894201551175986
      },
      "layer_4_expert_0": {
        "activation_count": 1066,
        "mean_assigned_benefit": 0.0560607473263261,
        "mean_delta_norm": 8.217725783754245,
        "mean_harm": -0.03219967889040816,
        "mean_positive_benefit": 0.08780748226652886,
        "mean_route_margin": 0.417756174346799,
        "positive_benefit_rate": 0.7354596622889306,
        "prose_benefit": 16.02070260188666,
        "structured_benefit": 44.639788455640556,
        "structured_prose_benefit_ratio": 2.7863814443683386,
        "token_class_benefit": {
          "brace_bracket_paren": 3.754080732663472,
          "comma_colon_semicolon": 2.369299824039142,
          "function_signature": 2.059435335298379,
          "identifier": 12.409845280771458,
          "json_key": 4.216892823576927,
          "json_value": 2.5206636699537435,
          "newline": 6.7196153849365485,
          "number": 1.1124037901560464,
          "operator": 0.8039665818214417,
          "other": 1.8697441967384898,
          "prose_word": 18.0735553627213,
          "quote": 6.285764217376708,
          "space": -4.822331365236705,
          "string_literal": 2.387820815046627
        },
        "token_class_counts": {
          "brace_bracket_paren": 16,
          "comma_colon_semicolon": 29,
          "function_signature": 22,
          "identifier": 241,
          "json_key": 74,
          "json_value": 48,
          "newline": 33,
          "number": 11,
          "operator": 4,
          "other": 17,
          "prose_word": 353,
          "quote": 20,
          "space": 155,
          "string_literal": 43
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.1258842075864474,
            "delta_norm": 7.389493465423584,
            "family": "broad_lm",
            "route_margin": 0.24548983573913574,
            "token": "m",
            "token_class": "prose_word",
            "token_total_benefit": -3.0212209820747375
          },
          {
            "assigned_benefit": -0.10964437325795491,
            "delta_norm": 7.895854473114014,
            "family": "code_heavy",
            "route_margin": 0.17022448778152466,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -2.631464958190918
          },
          {
            "assigned_benefit": -0.10848332444826762,
            "delta_norm": 8.353082656860352,
            "family": "code_heavy",
            "route_margin": 0.2616928219795227,
            "token": "n",
            "token_class": "identifier",
            "token_total_benefit": -2.603599786758423
          },
          {
            "assigned_benefit": -0.09847732384999593,
            "delta_norm": 8.177716255187988,
            "family": "broad_lm",
            "route_margin": 0.8380196690559387,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -2.3634557723999023
          },
          {
            "assigned_benefit": -0.0975755254427592,
            "delta_norm": 8.810248374938965,
            "family": "code_heavy",
            "route_margin": 0.4591531753540039,
            "token": "s",
            "token_class": "string_literal",
            "token_total_benefit": -2.3418126106262207
          },
          {
            "assigned_benefit": -0.09626823663711548,
            "delta_norm": 8.04516887664795,
            "family": "broad_lm",
            "route_margin": 0.6543362140655518,
            "token": "o",
            "token_class": "prose_word",
            "token_total_benefit": -2.3104376792907715
          },
          {
            "assigned_benefit": -0.0939420076707999,
            "delta_norm": 8.716288566589355,
            "family": "json_schema",
            "route_margin": 0.8492482304573059,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -2.2546081840991974
          },
          {
            "assigned_benefit": -0.09154083828131358,
            "delta_norm": 8.819113731384277,
            "family": "json_schema",
            "route_margin": 1.1660873889923096,
            "token": "d",
            "token_class": "json_value",
            "token_total_benefit": -2.196980118751526
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.4348748524983724,
            "delta_norm": 7.8735575675964355,
            "family": "json_schema",
            "route_margin": 0.14937710762023926,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.436996459960938
          },
          {
            "assigned_benefit": 0.4192720651626587,
            "delta_norm": 8.184983253479004,
            "family": "code_heavy",
            "route_margin": 0.30271685123443604,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 10.062529563903809
          },
          {
            "assigned_benefit": 0.3964542547861735,
            "delta_norm": 8.028182029724121,
            "family": "code_heavy",
            "route_margin": 1.1705269813537598,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.514902114868164
          },
          {
            "assigned_benefit": 0.38800891240437824,
            "delta_norm": 8.491046905517578,
            "family": "code_heavy",
            "route_margin": 0.1892523169517517,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.312213897705078
          },
          {
            "assigned_benefit": 0.3795582453409831,
            "delta_norm": 7.826969146728516,
            "family": "json_schema",
            "route_margin": 0.02821528911590576,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.109397888183594
          },
          {
            "assigned_benefit": 0.37155044078826904,
            "delta_norm": 7.266879081726074,
            "family": "code_heavy",
            "route_margin": 0.11093610525131226,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.917210578918457
          },
          {
            "assigned_benefit": 0.36562061309814453,
            "delta_norm": 7.43617057800293,
            "family": "json_schema",
            "route_margin": 0.6961798071861267,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 8.774894714355469
          },
          {
            "assigned_benefit": 0.3553175131479899,
            "delta_norm": 8.483682632446289,
            "family": "code_heavy",
            "route_margin": 0.24722838401794434,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.527620315551758
          }
        ],
        "total_assigned_benefit": 59.76075664986362
      },
      "layer_4_expert_1": {
        "activation_count": 1138,
        "mean_assigned_benefit": 0.04501041942118367,
        "mean_delta_norm": 7.8713356254389915,
        "mean_harm": -0.02090832225941777,
        "mean_positive_benefit": 0.09521478615006279,
        "mean_route_margin": 0.3180021580262846,
        "positive_benefit_rate": 0.5676625659050967,
        "prose_benefit": 3.7121004484343274,
        "structured_benefit": 43.65117881668084,
        "structured_prose_benefit_ratio": 11.759158843638467,
        "token_class_benefit": {
          "brace_bracket_paren": 4.089873018674552,
          "comma_colon_semicolon": 0.9526306887467704,
          "function_signature": 1.91047461827596,
          "identifier": 8.923263025159633,
          "indentation": -3.7392249273446696,
          "json_key": 2.04022782544295,
          "json_value": 2.0989671846230826,
          "newline": 1.9908015331002817,
          "number": 2.705943624178569,
          "operator": 1.0538879831631978,
          "other": 5.018488248189289,
          "prose_word": 9.513199470626814,
          "quote": 15.929248015085856,
          "space": -3.2217843068453162,
          "string_literal": 1.9558613002300262
        },
        "token_class_counts": {
          "brace_bracket_paren": 29,
          "comma_colon_semicolon": 11,
          "function_signature": 20,
          "identifier": 183,
          "indentation": 323,
          "json_key": 30,
          "json_value": 40,
          "newline": 15,
          "number": 16,
          "operator": 6,
          "other": 18,
          "prose_word": 226,
          "quote": 51,
          "space": 153,
          "string_literal": 17
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.109354833761851,
            "delta_norm": 8.02380657196045,
            "family": "code_heavy",
            "route_margin": 0.7423365116119385,
            "token": "-",
            "token_class": "operator",
            "token_total_benefit": -2.624516010284424
          },
          {
            "assigned_benefit": -0.10159913450479507,
            "delta_norm": 9.493680953979492,
            "family": "broad_lm",
            "route_margin": 0.31202298402786255,
            "token": "p",
            "token_class": "prose_word",
            "token_total_benefit": -2.438379228115082
          },
          {
            "assigned_benefit": -0.10102646052837372,
            "delta_norm": 8.645722389221191,
            "family": "code_heavy",
            "route_margin": 0.16485214233398438,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.4246350526809692
          },
          {
            "assigned_benefit": -0.09750870863596599,
            "delta_norm": 7.610886096954346,
            "family": "code_heavy",
            "route_margin": 0.3390235900878906,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -2.3402090072631836
          },
          {
            "assigned_benefit": -0.09698358178138733,
            "delta_norm": 8.039971351623535,
            "family": "broad_lm",
            "route_margin": 0.2526233196258545,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -2.327605962753296
          },
          {
            "assigned_benefit": -0.09417232871055603,
            "delta_norm": 8.09618854522705,
            "family": "code_heavy",
            "route_margin": 0.5606693029403687,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.2601358890533447
          },
          {
            "assigned_benefit": -0.08971371750036876,
            "delta_norm": 7.832481384277344,
            "family": "code_heavy",
            "route_margin": 0.19483733177185059,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -2.15312922000885
          },
          {
            "assigned_benefit": -0.0860140969355901,
            "delta_norm": 8.030335426330566,
            "family": "code_heavy",
            "route_margin": 0.05203425884246826,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -2.0643383264541626
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.42559146881103516,
            "delta_norm": 9.553960800170898,
            "family": "json_schema",
            "route_margin": 0.10610616207122803,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.214195251464844
          },
          {
            "assigned_benefit": 0.3995812733968099,
            "delta_norm": 8.124539375305176,
            "family": "json_schema",
            "route_margin": 0.2731724977493286,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.589950561523438
          },
          {
            "assigned_benefit": 0.3949778874715169,
            "delta_norm": 8.685494422912598,
            "family": "json_schema",
            "route_margin": 0.562274694442749,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.479469299316406
          },
          {
            "assigned_benefit": 0.38860607147216797,
            "delta_norm": 8.473816871643066,
            "family": "json_schema",
            "route_margin": 0.4227604866027832,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.326545715332031
          },
          {
            "assigned_benefit": 0.38011709849039715,
            "delta_norm": 8.762104988098145,
            "family": "json_schema",
            "route_margin": 0.2838393449783325,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.122810363769531
          },
          {
            "assigned_benefit": 0.3688637415568034,
            "delta_norm": 7.699320316314697,
            "family": "json_schema",
            "route_margin": 0.2297949492931366,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 8.852729797363281
          },
          {
            "assigned_benefit": 0.3590370814005534,
            "delta_norm": 8.529781341552734,
            "family": "code_heavy",
            "route_margin": 0.14862480759620667,
            "token": "'",
            "token_class": "quote",
            "token_total_benefit": 8.616889953613281
          },
          {
            "assigned_benefit": 0.3551967938741048,
            "delta_norm": 6.861227989196777,
            "family": "code_heavy",
            "route_margin": 0.5067250728607178,
            "token": "'",
            "token_class": "quote",
            "token_total_benefit": 8.524723052978516
          }
        ],
        "total_assigned_benefit": 51.22185730130701
      },
      "layer_4_expert_2": {
        "activation_count": 68,
        "mean_assigned_benefit": 0.07255237829885791,
        "mean_delta_norm": 8.658313288408166,
        "mean_harm": -0.034587825687291726,
        "mean_positive_benefit": 0.10551859490998085,
        "mean_route_margin": 0.36480307359905806,
        "positive_benefit_rate": 0.7647058823529411,
        "prose_benefit": 2.0831962743374692,
        "structured_benefit": 3.1114785919808323,
        "structured_prose_benefit_ratio": 1.493607986107979,
        "token_class_benefit": {
          "brace_bracket_paren": -0.016478024423122406,
          "comma_colon_semicolon": 0.16481194893519086,
          "function_signature": 0.10819093386332194,
          "identifier": 0.4409117400646209,
          "json_key": 0.2225273847579956,
          "json_value": 0.06462317953507106,
          "newline": 1.4014403571906662,
          "operator": 0.06128887335459391,
          "other": 1.0432190001010895,
          "prose_word": 1.1268302251895268,
          "quote": 0.24510510762532553,
          "space": -0.34796609294911235,
          "string_literal": 0.41905709107716876
        },
        "token_class_counts": {
          "brace_bracket_paren": 1,
          "comma_colon_semicolon": 2,
          "function_signature": 1,
          "identifier": 8,
          "json_key": 1,
          "json_value": 2,
          "newline": 12,
          "operator": 1,
          "other": 4,
          "prose_word": 13,
          "quote": 1,
          "space": 20,
          "string_literal": 2
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.10804811120033264,
            "delta_norm": 8.50854206085205,
            "family": "broad_lm",
            "route_margin": 0.4163137674331665,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -2.5931546688079834
          },
          {
            "assigned_benefit": -0.08750950296719869,
            "delta_norm": 8.354801177978516,
            "family": "json_schema",
            "route_margin": 1.2583863735198975,
            "token": "l",
            "token_class": "identifier",
            "token_total_benefit": -2.1002280712127686
          },
          {
            "assigned_benefit": -0.061008572578430176,
            "delta_norm": 8.14952278137207,
            "family": "json_schema",
            "route_margin": 0.2923707664012909,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.4642057418823242
          },
          {
            "assigned_benefit": -0.0456084410349528,
            "delta_norm": 8.491700172424316,
            "family": "code_heavy",
            "route_margin": 0.8979276418685913,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.0946025848388672
          },
          {
            "assigned_benefit": -0.04096344858407974,
            "delta_norm": 7.08117151260376,
            "family": "json_schema",
            "route_margin": 0.39663130044937134,
            "token": "l",
            "token_class": "json_value",
            "token_total_benefit": -0.9831227660179138
          },
          {
            "assigned_benefit": -0.03931535283724467,
            "delta_norm": 9.670361518859863,
            "family": "code_heavy",
            "route_margin": 0.21630233526229858,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -0.9435684680938721
          },
          {
            "assigned_benefit": -0.03292870273192724,
            "delta_norm": 8.885222434997559,
            "family": "broad_lm",
            "route_margin": 0.4483412504196167,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -0.7902888655662537
          },
          {
            "assigned_benefit": -0.021770159403483074,
            "delta_norm": 8.242204666137695,
            "family": "code_heavy",
            "route_margin": 0.2445216178894043,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -0.5224838256835938
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.31830819447835285,
            "delta_norm": 7.976858139038086,
            "family": "code_heavy",
            "route_margin": 0.48145753145217896,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 7.639396667480469
          },
          {
            "assigned_benefit": 0.31336021423339844,
            "delta_norm": 7.161550998687744,
            "family": "code_heavy",
            "route_margin": 0.01494365930557251,
            "token": "\\",
            "token_class": "string_literal",
            "token_total_benefit": 7.5206451416015625
          },
          {
            "assigned_benefit": 0.3037249843279521,
            "delta_norm": 7.427712917327881,
            "family": "code_heavy",
            "route_margin": 0.01759517192840576,
            "token": "_",
            "token_class": "identifier",
            "token_total_benefit": 7.28939962387085
          },
          {
            "assigned_benefit": 0.29892826080322266,
            "delta_norm": 8.16929817199707,
            "family": "code_heavy",
            "route_margin": 0.25559866428375244,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 7.174278259277344
          },
          {
            "assigned_benefit": 0.26278122266133624,
            "delta_norm": 8.605575561523438,
            "family": "json_schema",
            "route_margin": 0.043344080448150635,
            "token": "\\n",
            "token_class": "newline",
            "token_total_benefit": 6.30674934387207
          },
          {
            "assigned_benefit": 0.26030953725179035,
            "delta_norm": 8.371119499206543,
            "family": "code_heavy",
            "route_margin": 1.0385332107543945,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 6.247428894042969
          },
          {
            "assigned_benefit": 0.24510510762532553,
            "delta_norm": 8.984516143798828,
            "family": "json_schema",
            "route_margin": 0.030667006969451904,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 5.8825225830078125
          },
          {
            "assigned_benefit": 0.2225273847579956,
            "delta_norm": 7.701735496520996,
            "family": "json_schema",
            "route_margin": 0.5029888153076172,
            "token": "i",
            "token_class": "json_key",
            "token_total_benefit": 5.3406572341918945
          }
        ],
        "total_assigned_benefit": 4.933561724322338
      },
      "layer_4_expert_3": {
        "activation_count": 495,
        "mean_assigned_benefit": 0.038619385986760624,
        "mean_delta_norm": 7.760698329077827,
        "mean_harm": -0.025236058172323102,
        "mean_positive_benefit": 0.08375857927163011,
        "mean_route_margin": 0.2631198597375793,
        "positive_benefit_rate": 0.5858585858585859,
        "prose_benefit": 4.300043710975844,
        "structured_benefit": 13.02038027004922,
        "structured_prose_benefit_ratio": 3.027964631339619,
        "token_class_benefit": {
          "brace_bracket_paren": 1.3935197989145913,
          "comma_colon_semicolon": 0.0607822338740031,
          "function_signature": 0.6967694511016209,
          "identifier": 3.771506715876361,
          "indentation": -1.3802023900983236,
          "json_key": 0.09531457225481668,
          "json_value": 0.6805192207296691,
          "newline": 1.2143777211534446,
          "number": 1.7115193208058677,
          "operator": 1.2048347393671672,
          "other": 2.34544575214386,
          "prose_word": 7.099590852546196,
          "quote": 2.1140921910603843,
          "space": -1.9686184211944544,
          "string_literal": 0.07714430491129555
        },
        "token_class_counts": {
          "brace_bracket_paren": 6,
          "comma_colon_semicolon": 3,
          "function_signature": 8,
          "identifier": 80,
          "indentation": 79,
          "json_key": 7,
          "json_value": 15,
          "newline": 6,
          "number": 11,
          "operator": 7,
          "other": 10,
          "prose_word": 177,
          "quote": 7,
          "space": 73,
          "string_literal": 6
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.1018477330605189,
            "delta_norm": 8.246489524841309,
            "family": "broad_lm",
            "route_margin": 0.5293079018592834,
            "token": " ",
            "token_class": "indentation",
            "token_total_benefit": -2.4443455934524536
          },
          {
            "assigned_benefit": -0.09828927119572957,
            "delta_norm": 7.533923625946045,
            "family": "json_schema",
            "route_margin": 0.203965425491333,
            "token": " ",
            "token_class": "indentation",
            "token_total_benefit": -2.3589425086975098
          },
          {
            "assigned_benefit": -0.09049346546332042,
            "delta_norm": 8.418715476989746,
            "family": "code_heavy",
            "route_margin": 0.10202667117118835,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -2.17184317111969
          },
          {
            "assigned_benefit": -0.0889308750629425,
            "delta_norm": 8.157651901245117,
            "family": "broad_lm",
            "route_margin": 0.11660075187683105,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -2.13434100151062
          },
          {
            "assigned_benefit": -0.08728645245234172,
            "delta_norm": 7.193899154663086,
            "family": "broad_lm",
            "route_margin": 0.09613931179046631,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -2.094874858856201
          },
          {
            "assigned_benefit": -0.08370453119277954,
            "delta_norm": 8.101922035217285,
            "family": "json_schema",
            "route_margin": 0.32766056060791016,
            "token": "d",
            "token_class": "json_key",
            "token_total_benefit": -2.008908748626709
          },
          {
            "assigned_benefit": -0.08222424983978271,
            "delta_norm": 7.392409324645996,
            "family": "code_heavy",
            "route_margin": 0.23698484897613525,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.9733819961547852
          },
          {
            "assigned_benefit": -0.07812918225924174,
            "delta_norm": 7.692095756530762,
            "family": "code_heavy",
            "route_margin": 0.3361005187034607,
            "token": "d",
            "token_class": "string_literal",
            "token_total_benefit": -1.8751003742218018
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.36609824498494464,
            "delta_norm": 8.448562622070312,
            "family": "code_heavy",
            "route_margin": 0.2612118721008301,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.786357879638672
          },
          {
            "assigned_benefit": 0.34638198216756183,
            "delta_norm": 6.987856388092041,
            "family": "code_heavy",
            "route_margin": 0.021615326404571533,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.313167572021484
          },
          {
            "assigned_benefit": 0.33861692746480304,
            "delta_norm": 7.670663356781006,
            "family": "json_schema",
            "route_margin": 0.08233201503753662,
            "token": "\\n",
            "token_class": "newline",
            "token_total_benefit": 8.126806259155273
          },
          {
            "assigned_benefit": 0.3370218276977539,
            "delta_norm": 7.5452046394348145,
            "family": "code_heavy",
            "route_margin": 0.446641206741333,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 8.088523864746094
          },
          {
            "assigned_benefit": 0.3350486755371094,
            "delta_norm": 7.466932773590088,
            "family": "code_heavy",
            "route_margin": 0.07322686910629272,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 8.041168212890625
          },
          {
            "assigned_benefit": 0.3311882019042969,
            "delta_norm": 7.55414342880249,
            "family": "code_heavy",
            "route_margin": 0.3995988965034485,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 7.948516845703125
          },
          {
            "assigned_benefit": 0.3223867416381836,
            "delta_norm": 8.166633605957031,
            "family": "json_schema",
            "route_margin": 0.06517022848129272,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 7.737281799316406
          },
          {
            "assigned_benefit": 0.32006919384002686,
            "delta_norm": 8.231687545776367,
            "family": "json_schema",
            "route_margin": 0.4754564166069031,
            "token": "\\n",
            "token_class": "newline",
            "token_total_benefit": 7.6816606521606445
          }
        ],
        "total_assigned_benefit": 19.116596063446508
      },
      "layer_4_expert_4": {
        "activation_count": 774,
        "mean_assigned_benefit": 0.06900842284332606,
        "mean_delta_norm": 8.76603627266502,
        "mean_harm": -0.03350132046766129,
        "mean_positive_benefit": 0.10075001848784496,
        "mean_route_margin": 0.459790201188674,
        "positive_benefit_rate": 0.7635658914728682,
        "prose_benefit": 18.777813512767523,
        "structured_benefit": 34.40935159817412,
        "structured_prose_benefit_ratio": 1.8324471895930965,
        "token_class_benefit": {
          "brace_bracket_paren": 3.883562088012695,
          "comma_colon_semicolon": 2.291115502516429,
          "function_signature": 2.3558384180068974,
          "identifier": 9.702474825084211,
          "json_key": 2.7347062081098557,
          "json_value": 2.1645748028531666,
          "newline": 2.1956513275834673,
          "number": 0.086997389793396,
          "operator": 0.5828237533569336,
          "other": 2.3734098069835454,
          "prose_word": 19.47039353599152,
          "quote": 6.055064837137858,
          "space": -2.840635660414895,
          "string_literal": 2.356542445719242
        },
        "token_class_counts": {
          "brace_bracket_paren": 14,
          "comma_colon_semicolon": 21,
          "function_signature": 14,
          "identifier": 146,
          "json_key": 26,
          "json_value": 41,
          "newline": 14,
          "number": 1,
          "operator": 3,
          "other": 13,
          "prose_word": 296,
          "quote": 19,
          "space": 136,
          "string_literal": 30
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.14390301704406738,
            "delta_norm": 8.753653526306152,
            "family": "json_schema",
            "route_margin": 0.4778738021850586,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -3.453672409057617
          },
          {
            "assigned_benefit": -0.1176329255104065,
            "delta_norm": 8.1527738571167,
            "family": "broad_lm",
            "route_margin": 0.08278048038482666,
            "token": "o",
            "token_class": "prose_word",
            "token_total_benefit": -2.823190212249756
          },
          {
            "assigned_benefit": -0.11193382243315379,
            "delta_norm": 7.161365032196045,
            "family": "broad_lm",
            "route_margin": 0.20192408561706543,
            "token": "e",
            "token_class": "prose_word",
            "token_total_benefit": -2.686411738395691
          },
          {
            "assigned_benefit": -0.11105093856652577,
            "delta_norm": 7.741726875305176,
            "family": "broad_lm",
            "route_margin": 0.7984395027160645,
            "token": "o",
            "token_class": "prose_word",
            "token_total_benefit": -2.6652225255966187
          },
          {
            "assigned_benefit": -0.11034655446807544,
            "delta_norm": 9.874554634094238,
            "family": "code_heavy",
            "route_margin": 0.9224605560302734,
            "token": "o",
            "token_class": "identifier",
            "token_total_benefit": -2.6483173072338104
          },
          {
            "assigned_benefit": -0.10949698835611343,
            "delta_norm": 8.585000038146973,
            "family": "broad_lm",
            "route_margin": 1.8676636219024658,
            "token": "o",
            "token_class": "prose_word",
            "token_total_benefit": -2.6279277205467224
          },
          {
            "assigned_benefit": -0.0898671845595042,
            "delta_norm": 8.133631706237793,
            "family": "broad_lm",
            "route_margin": 0.2354481816291809,
            "token": "e",
            "token_class": "prose_word",
            "token_total_benefit": -2.1568124294281006
          },
          {
            "assigned_benefit": -0.08720193554957707,
            "delta_norm": 8.288406372070312,
            "family": "json_schema",
            "route_margin": 0.35504841804504395,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -2.09284645318985
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.41413907210032147,
            "delta_norm": 8.019343376159668,
            "family": "code_heavy",
            "route_margin": 0.35659265518188477,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.939337730407715
          },
          {
            "assigned_benefit": 0.40491771697998047,
            "delta_norm": 8.349364280700684,
            "family": "json_schema",
            "route_margin": 0.11786597967147827,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.718025207519531
          },
          {
            "assigned_benefit": 0.40207378069559735,
            "delta_norm": 8.354876518249512,
            "family": "code_heavy",
            "route_margin": 0.35985589027404785,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.649770736694336
          },
          {
            "assigned_benefit": 0.3894158601760864,
            "delta_norm": 7.381861686706543,
            "family": "code_heavy",
            "route_margin": 0.8246299028396606,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.345980644226074
          },
          {
            "assigned_benefit": 0.38709576924641925,
            "delta_norm": 8.386699676513672,
            "family": "code_heavy",
            "route_margin": 0.0940282940864563,
            "token": "\\",
            "token_class": "function_signature",
            "token_total_benefit": 9.290298461914062
          },
          {
            "assigned_benefit": 0.3847957452138265,
            "delta_norm": 7.5084123611450195,
            "family": "code_heavy",
            "route_margin": 0.8247914910316467,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.235097885131836
          },
          {
            "assigned_benefit": 0.38037506739298504,
            "delta_norm": 8.803703308105469,
            "family": "code_heavy",
            "route_margin": 0.499509334564209,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.12900161743164
          },
          {
            "assigned_benefit": 0.3641868432362874,
            "delta_norm": 7.890396595001221,
            "family": "code_heavy",
            "route_margin": 0.7138289213180542,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.740484237670898
          }
        ],
        "total_assigned_benefit": 53.41251928073437
      },
      "layer_4_expert_5": {
        "activation_count": 1013,
        "mean_assigned_benefit": 0.07147857276579463,
        "mean_delta_norm": 8.756746789192283,
        "mean_harm": -0.03120591437533549,
        "mean_positive_benefit": 0.10730192247415171,
        "mean_route_margin": 0.41424512624122783,
        "positive_benefit_rate": 0.7413622902270484,
        "prose_benefit": 9.004206879444181,
        "structured_benefit": 56.53991524474642,
        "structured_prose_benefit_ratio": 6.279277675618728,
        "token_class_benefit": {
          "brace_bracket_paren": 3.6567675968011217,
          "comma_colon_semicolon": 6.163512984911602,
          "function_signature": 3.326720299820106,
          "identifier": 9.156471336570883,
          "json_key": 4.316263856987159,
          "json_value": 1.2062609704832234,
          "newline": 8.016312678685495,
          "number": 1.2774700721104941,
          "operator": 1.6467518409093218,
          "other": 9.072218696276346,
          "prose_word": 9.418401268310843,
          "quote": 11.566068013509115,
          "space": -2.622740997583605,
          "string_literal": 6.207315593957899
        },
        "token_class_counts": {
          "brace_bracket_paren": 20,
          "comma_colon_semicolon": 62,
          "function_signature": 29,
          "identifier": 217,
          "json_key": 42,
          "json_value": 29,
          "newline": 35,
          "number": 15,
          "operator": 10,
          "other": 40,
          "prose_word": 251,
          "quote": 35,
          "space": 164,
          "string_literal": 64
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.17974231019616127,
            "delta_norm": 8.427087783813477,
            "family": "broad_lm",
            "route_margin": 0.5227410793304443,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -4.3138154447078705
          },
          {
            "assigned_benefit": -0.13103054463863373,
            "delta_norm": 10.600316047668457,
            "family": "code_heavy",
            "route_margin": 0.3499338626861572,
            "token": "g",
            "token_class": "identifier",
            "token_total_benefit": -3.1447330713272095
          },
          {
            "assigned_benefit": -0.12130660812060039,
            "delta_norm": 7.624361515045166,
            "family": "json_schema",
            "route_margin": 0.027232766151428223,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.911358594894409
          },
          {
            "assigned_benefit": -0.11974493662516277,
            "delta_norm": 8.355707168579102,
            "family": "code_heavy",
            "route_margin": 0.20099467039108276,
            "token": "5",
            "token_class": "number",
            "token_total_benefit": -2.8738784790039062
          },
          {
            "assigned_benefit": -0.11696084340413411,
            "delta_norm": 9.193750381469727,
            "family": "json_schema",
            "route_margin": 0.42336201667785645,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.8070602416992188
          },
          {
            "assigned_benefit": -0.11042344570159912,
            "delta_norm": 7.393818378448486,
            "family": "json_schema",
            "route_margin": 0.2590399384498596,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.650162696838379
          },
          {
            "assigned_benefit": -0.10870074232419331,
            "delta_norm": 8.323286056518555,
            "family": "broad_lm",
            "route_margin": 0.4205334186553955,
            "token": "o",
            "token_class": "prose_word",
            "token_total_benefit": -2.6088178157806396
          },
          {
            "assigned_benefit": -0.10707541306813557,
            "delta_norm": 7.844151020050049,
            "family": "code_heavy",
            "route_margin": 0.2218717336654663,
            "token": "s",
            "token_class": "identifier",
            "token_total_benefit": -2.569809913635254
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.4434954325358073,
            "delta_norm": 8.657865524291992,
            "family": "json_schema",
            "route_margin": 1.075549840927124,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.643890380859375
          },
          {
            "assigned_benefit": 0.4194428126017253,
            "delta_norm": 9.250693321228027,
            "family": "json_schema",
            "route_margin": 0.21531176567077637,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.066627502441406
          },
          {
            "assigned_benefit": 0.3999309539794922,
            "delta_norm": 8.364933967590332,
            "family": "json_schema",
            "route_margin": 0.5203547477722168,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.598342895507812
          },
          {
            "assigned_benefit": 0.3989645640055339,
            "delta_norm": 8.086466789245605,
            "family": "json_schema",
            "route_margin": 0.1987931728363037,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.575149536132812
          },
          {
            "assigned_benefit": 0.39834149678548175,
            "delta_norm": 7.39945650100708,
            "family": "json_schema",
            "route_margin": 0.2036876678466797,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.560195922851562
          },
          {
            "assigned_benefit": 0.3903733491897583,
            "delta_norm": 9.125889778137207,
            "family": "code_heavy",
            "route_margin": 0.07623469829559326,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.3689603805542
          },
          {
            "assigned_benefit": 0.38902703921000165,
            "delta_norm": 9.027426719665527,
            "family": "code_heavy",
            "route_margin": 0.32002973556518555,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.336648941040039
          },
          {
            "assigned_benefit": 0.38402652740478516,
            "delta_norm": 7.090157508850098,
            "family": "code_heavy",
            "route_margin": 0.09230911731719971,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 9.216636657714844
          }
        ],
        "total_assigned_benefit": 72.40779421174996
      },
      "layer_4_expert_6": {
        "activation_count": 1387,
        "mean_assigned_benefit": 0.041041291938113504,
        "mean_delta_norm": 7.640514423285102,
        "mean_harm": -0.020089764762783006,
        "mean_positive_benefit": 0.1057096056291212,
        "mean_route_margin": 0.29550631725710763,
        "positive_benefit_rate": 0.4859408795962509,
        "prose_benefit": -0.152294416805641,
        "structured_benefit": 53.95409047272753,
        "structured_prose_benefit_ratio": 354.274907802983,
        "token_class_benefit": {
          "brace_bracket_paren": 5.683258990446726,
          "comma_colon_semicolon": 3.9314966499805446,
          "function_signature": 2.0587031841278076,
          "identifier": 9.459022286037607,
          "indentation": -5.922242542573563,
          "json_key": 3.324000944693884,
          "json_value": 2.4622945625645425,
          "newline": 1.0557192665966493,
          "number": 2.245735208193461,
          "operator": 2.723746299743652,
          "other": 4.027532070875168,
          "prose_word": 8.570899445563551,
          "quote": 19.125882943471275,
          "space": -3.7060075284292298,
          "string_literal": 1.884230136871338
        },
        "token_class_counts": {
          "brace_bracket_paren": 36,
          "comma_colon_semicolon": 41,
          "function_signature": 18,
          "identifier": 187,
          "indentation": 507,
          "json_key": 37,
          "json_value": 38,
          "newline": 10,
          "number": 14,
          "operator": 14,
          "other": 17,
          "prose_word": 216,
          "quote": 64,
          "space": 168,
          "string_literal": 20
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.14381763339042664,
            "delta_norm": 8.624125480651855,
            "family": "broad_lm",
            "route_margin": 0.474479615688324,
            "token": "c",
            "token_class": "prose_word",
            "token_total_benefit": -3.4516232013702393
          },
          {
            "assigned_benefit": -0.12831215063730875,
            "delta_norm": 7.140353679656982,
            "family": "json_schema",
            "route_margin": 0.16834312677383423,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -3.07949161529541
          },
          {
            "assigned_benefit": -0.10809943079948425,
            "delta_norm": 6.1238532066345215,
            "family": "json_schema",
            "route_margin": 0.5264369249343872,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.594386339187622
          },
          {
            "assigned_benefit": -0.10358279943466187,
            "delta_norm": 6.741664886474609,
            "family": "json_schema",
            "route_margin": 0.03965115547180176,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.4859871864318848
          },
          {
            "assigned_benefit": -0.09784005582332611,
            "delta_norm": 7.312478065490723,
            "family": "code_heavy",
            "route_margin": 0.09784972667694092,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -2.3481613397598267
          },
          {
            "assigned_benefit": -0.09491795673966408,
            "delta_norm": 7.947942733764648,
            "family": "broad_lm",
            "route_margin": 0.23207297921180725,
            "token": "l",
            "token_class": "prose_word",
            "token_total_benefit": -2.278030961751938
          },
          {
            "assigned_benefit": -0.09179036815961202,
            "delta_norm": 6.937878131866455,
            "family": "broad_lm",
            "route_margin": 0.4298420548439026,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -2.2029688358306885
          },
          {
            "assigned_benefit": -0.09138673543930054,
            "delta_norm": 6.129973888397217,
            "family": "json_schema",
            "route_margin": 0.42510437965393066,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.193281650543213
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.40347035725911456,
            "delta_norm": 7.438281059265137,
            "family": "json_schema",
            "route_margin": 0.5881246328353882,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.68328857421875
          },
          {
            "assigned_benefit": 0.35289955139160156,
            "delta_norm": 7.850286960601807,
            "family": "code_heavy",
            "route_margin": 0.31390684843063354,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.469589233398438
          },
          {
            "assigned_benefit": 0.34815677007039386,
            "delta_norm": 6.431756496429443,
            "family": "code_heavy",
            "route_margin": 0.08433997631072998,
            "token": "'",
            "token_class": "quote",
            "token_total_benefit": 8.355762481689453
          },
          {
            "assigned_benefit": 0.34745808442433673,
            "delta_norm": 8.521904945373535,
            "family": "code_heavy",
            "route_margin": 0.28275012969970703,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.338994026184082
          },
          {
            "assigned_benefit": 0.3417193094889323,
            "delta_norm": 7.025396823883057,
            "family": "code_heavy",
            "route_margin": 0.37002402544021606,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 8.201263427734375
          },
          {
            "assigned_benefit": 0.3387260437011719,
            "delta_norm": 7.671433448791504,
            "family": "code_heavy",
            "route_margin": 0.33850419521331787,
            "token": "'",
            "token_class": "quote",
            "token_total_benefit": 8.129425048828125
          },
          {
            "assigned_benefit": 0.3320792516072591,
            "delta_norm": 7.413461685180664,
            "family": "code_heavy",
            "route_margin": 0.18173766136169434,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 7.969902038574219
          },
          {
            "assigned_benefit": 0.3318033218383789,
            "delta_norm": 6.495326995849609,
            "family": "code_heavy",
            "route_margin": 0.3884572684764862,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 7.963279724121094
          }
        ],
        "total_assigned_benefit": 56.924271918163434
      },
      "layer_4_expert_7": {
        "activation_count": 203,
        "mean_assigned_benefit": 0.061068328314235996,
        "mean_delta_norm": 8.821669757072561,
        "mean_harm": -0.019957796971236043,
        "mean_positive_benefit": 0.0919354236610825,
        "mean_route_margin": 0.30520550249685796,
        "positive_benefit_rate": 0.7241379310344828,
        "prose_benefit": 2.958806045275803,
        "structured_benefit": 9.10413886855046,
        "structured_prose_benefit_ratio": 3.0769637242990777,
        "token_class_benefit": {
          "comma_colon_semicolon": 0.48237115144729614,
          "function_signature": 0.6506285270055134,
          "identifier": 1.6745539978146553,
          "json_value": -0.01286458969116211,
          "newline": 3.128704080979029,
          "number": 0.4364715019861857,
          "other": 0.8668289184570312,
          "prose_word": 3.079911312709252,
          "quote": 2.16598383585612,
          "space": -0.6540084519268324,
          "string_literal": 0.5782903631528218
        },
        "token_class_counts": {
          "comma_colon_semicolon": 4,
          "function_signature": 3,
          "identifier": 33,
          "json_value": 1,
          "newline": 12,
          "number": 3,
          "other": 3,
          "prose_word": 64,
          "quote": 7,
          "space": 59,
          "string_literal": 14
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.07094074289004008,
            "delta_norm": 6.572556495666504,
            "family": "code_heavy",
            "route_margin": 0.6271732449531555,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.702577829360962
          },
          {
            "assigned_benefit": -0.06649886071681976,
            "delta_norm": 7.633424282073975,
            "family": "broad_lm",
            "route_margin": 0.18570446968078613,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -1.5959726572036743
          },
          {
            "assigned_benefit": -0.05815319220225016,
            "delta_norm": 8.670923233032227,
            "family": "broad_lm",
            "route_margin": 0.036250412464141846,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.395676612854004
          },
          {
            "assigned_benefit": -0.05203923831383387,
            "delta_norm": 7.7117414474487305,
            "family": "broad_lm",
            "route_margin": 0.2963722348213196,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.248941719532013
          },
          {
            "assigned_benefit": -0.05180441836516062,
            "delta_norm": 7.584239482879639,
            "family": "code_heavy",
            "route_margin": 0.30781471729278564,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -1.243306040763855
          },
          {
            "assigned_benefit": -0.04688771410534779,
            "delta_norm": 7.87979793548584,
            "family": "broad_lm",
            "route_margin": 0.3661012053489685,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.125305138528347
          },
          {
            "assigned_benefit": -0.04369117319583893,
            "delta_norm": 7.863572120666504,
            "family": "broad_lm",
            "route_margin": 0.35018572211265564,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -1.0485881567001343
          },
          {
            "assigned_benefit": -0.042652408281962075,
            "delta_norm": 7.775324821472168,
            "family": "broad_lm",
            "route_margin": 0.09501397609710693,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.0236577987670898
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.3683640956878662,
            "delta_norm": 10.14680004119873,
            "family": "json_schema",
            "route_margin": 0.17018461227416992,
            "token": "\\n",
            "token_class": "newline",
            "token_total_benefit": 8.840738296508789
          },
          {
            "assigned_benefit": 0.3438250223795573,
            "delta_norm": 8.774285316467285,
            "family": "code_heavy",
            "route_margin": 0.14126265048980713,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 8.251800537109375
          },
          {
            "assigned_benefit": 0.3432128429412842,
            "delta_norm": 7.733017921447754,
            "family": "code_heavy",
            "route_margin": 0.5115437507629395,
            "token": "(",
            "token_class": "function_signature",
            "token_total_benefit": 8.23710823059082
          },
          {
            "assigned_benefit": 0.31595611572265625,
            "delta_norm": 8.984014511108398,
            "family": "code_heavy",
            "route_margin": 0.06707876920700073,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 7.58294677734375
          },
          {
            "assigned_benefit": 0.30992984771728516,
            "delta_norm": 8.047393798828125,
            "family": "code_heavy",
            "route_margin": 0.8005103468894958,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 7.438316345214844
          },
          {
            "assigned_benefit": 0.3087577819824219,
            "delta_norm": 8.467938423156738,
            "family": "code_heavy",
            "route_margin": 0.4207683801651001,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 7.410186767578125
          },
          {
            "assigned_benefit": 0.3051092028617859,
            "delta_norm": 12.15621280670166,
            "family": "json_schema",
            "route_margin": 0.19639664888381958,
            "token": "\\n",
            "token_class": "newline",
            "token_total_benefit": 7.322620868682861
          },
          {
            "assigned_benefit": 0.30479780832926434,
            "delta_norm": 8.948440551757812,
            "family": "code_heavy",
            "route_margin": 0.05463206768035889,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 7.315147399902344
          }
        ],
        "total_assigned_benefit": 12.396870647789907
      },
      "layer_5_expert_0": {
        "activation_count": 1739,
        "mean_assigned_benefit": 0.055461841821365064,
        "mean_delta_norm": 10.337045443613272,
        "mean_harm": -0.028428382907077592,
        "mean_positive_benefit": 0.08572271318272037,
        "mean_route_margin": 0.5278235841467506,
        "positive_benefit_rate": 0.7349051178838413,
        "prose_benefit": 34.09226666909,
        "structured_benefit": 58.083642975737696,
        "structured_prose_benefit_ratio": 1.7037190146233265,
        "token_class_benefit": {
          "brace_bracket_paren": 2.716280016116798,
          "comma_colon_semicolon": 4.951865538954736,
          "function_signature": 3.672830308477084,
          "identifier": 21.447497918891397,
          "indentation": -0.20705272754033405,
          "json_key": 1.9321221311887105,
          "json_value": 1.4461394237975274,
          "newline": 5.308252563079198,
          "number": 2.474144101142883,
          "operator": 1.2589044570922852,
          "other": 8.676186438941535,
          "prose_word": 35.716675254671536,
          "quote": 7.665642420450846,
          "space": -5.821309014456344,
          "string_literal": 5.209964096546171
        },
        "token_class_counts": {
          "brace_bracket_paren": 22,
          "comma_colon_semicolon": 44,
          "function_signature": 30,
          "identifier": 359,
          "indentation": 3,
          "json_key": 25,
          "json_value": 43,
          "newline": 31,
          "number": 22,
          "operator": 7,
          "other": 41,
          "prose_word": 698,
          "quote": 24,
          "space": 324,
          "string_literal": 66
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.14390301704406738,
            "delta_norm": 9.670820236206055,
            "family": "json_schema",
            "route_margin": 0.5853359699249268,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -3.453672409057617
          },
          {
            "assigned_benefit": -0.1258842075864474,
            "delta_norm": 10.562549591064453,
            "family": "broad_lm",
            "route_margin": 0.18260818719863892,
            "token": "m",
            "token_class": "prose_word",
            "token_total_benefit": -3.0212209820747375
          },
          {
            "assigned_benefit": -0.12130660812060039,
            "delta_norm": 9.187204360961914,
            "family": "json_schema",
            "route_margin": 0.011832118034362793,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.911358594894409
          },
          {
            "assigned_benefit": -0.1176329255104065,
            "delta_norm": 9.512564659118652,
            "family": "broad_lm",
            "route_margin": 0.3141120672225952,
            "token": "o",
            "token_class": "prose_word",
            "token_total_benefit": -2.823190212249756
          },
          {
            "assigned_benefit": -0.10964437325795491,
            "delta_norm": 10.32974624633789,
            "family": "code_heavy",
            "route_margin": 0.11204135417938232,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -2.631464958190918
          },
          {
            "assigned_benefit": -0.10949698835611343,
            "delta_norm": 9.21790885925293,
            "family": "broad_lm",
            "route_margin": 0.22815847396850586,
            "token": "o",
            "token_class": "prose_word",
            "token_total_benefit": -2.6279277205467224
          },
          {
            "assigned_benefit": -0.10870074232419331,
            "delta_norm": 9.046805381774902,
            "family": "broad_lm",
            "route_margin": 0.7843979001045227,
            "token": "o",
            "token_class": "prose_word",
            "token_total_benefit": -2.6088178157806396
          },
          {
            "assigned_benefit": -0.10388837258021037,
            "delta_norm": 9.28209400177002,
            "family": "code_heavy",
            "route_margin": 0.13576734066009521,
            "token": "d",
            "token_class": "string_literal",
            "token_total_benefit": -2.493320941925049
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.4194428126017253,
            "delta_norm": 10.371100425720215,
            "family": "json_schema",
            "route_margin": 0.6119989156723022,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.066627502441406
          },
          {
            "assigned_benefit": 0.3949778874715169,
            "delta_norm": 9.744935035705566,
            "family": "json_schema",
            "route_margin": 0.09941673278808594,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.479469299316406
          },
          {
            "assigned_benefit": 0.3771365483601888,
            "delta_norm": 9.602014541625977,
            "family": "json_schema",
            "route_margin": 0.5510971546173096,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.051277160644531
          },
          {
            "assigned_benefit": 0.3718280792236328,
            "delta_norm": 8.955562591552734,
            "family": "json_schema",
            "route_margin": 0.08070743083953857,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 8.923873901367188
          },
          {
            "assigned_benefit": 0.36562061309814453,
            "delta_norm": 10.274303436279297,
            "family": "json_schema",
            "route_margin": 0.5434973239898682,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 8.774894714355469
          },
          {
            "assigned_benefit": 0.35744380950927734,
            "delta_norm": 9.29753589630127,
            "family": "code_heavy",
            "route_margin": 0.5031863451004028,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 8.578651428222656
          },
          {
            "assigned_benefit": 0.35584481557210285,
            "delta_norm": 10.433491706848145,
            "family": "json_schema",
            "route_margin": 0.8342182636260986,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 8.540275573730469
          },
          {
            "assigned_benefit": 0.35584449768066406,
            "delta_norm": 10.433492660522461,
            "family": "json_schema",
            "route_margin": 0.8342177867889404,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 8.540267944335938
          }
        ],
        "total_assigned_benefit": 96.44814292735384
      },
      "layer_5_expert_1": {
        "activation_count": 680,
        "mean_assigned_benefit": 0.0718255111739792,
        "mean_delta_norm": 7.634098675671746,
        "mean_harm": -0.030824020160582666,
        "mean_positive_benefit": 0.10962201868751,
        "mean_route_margin": 0.38330253507284556,
        "positive_benefit_rate": 0.7308823529411764,
        "prose_benefit": 10.629979595066597,
        "structured_benefit": 36.97904001052185,
        "structured_prose_benefit_ratio": 3.4787498583425243,
        "token_class_benefit": {
          "brace_bracket_paren": 4.803224285443623,
          "comma_colon_semicolon": 2.711069673299789,
          "function_signature": 2.452068443099658,
          "identifier": 8.371327031403776,
          "indentation": -0.19560374598950148,
          "json_key": 3.353822390238445,
          "json_value": 2.114699617028236,
          "newline": 3.4224469810724263,
          "number": 0.3373140494028727,
          "operator": 0.5477844874064127,
          "other": 2.9219622194359545,
          "prose_word": 12.48355230533828,
          "quote": 6.111848990122477,
          "space": -3.347603191000719,
          "string_literal": 2.7534340620040894
        },
        "token_class_counts": {
          "brace_bracket_paren": 15,
          "comma_colon_semicolon": 26,
          "function_signature": 13,
          "identifier": 136,
          "indentation": 26,
          "json_key": 41,
          "json_value": 32,
          "newline": 16,
          "number": 3,
          "operator": 3,
          "other": 17,
          "prose_word": 191,
          "quote": 20,
          "space": 116,
          "string_literal": 25
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.17974231019616127,
            "delta_norm": 7.330848217010498,
            "family": "broad_lm",
            "route_margin": 0.29956305027008057,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -4.3138154447078705
          },
          {
            "assigned_benefit": -0.11696084340413411,
            "delta_norm": 7.148948669433594,
            "family": "json_schema",
            "route_margin": 0.2146700620651245,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.8070602416992188
          },
          {
            "assigned_benefit": -0.11105093856652577,
            "delta_norm": 6.927520275115967,
            "family": "broad_lm",
            "route_margin": 0.014992713928222656,
            "token": "o",
            "token_class": "prose_word",
            "token_total_benefit": -2.6652225255966187
          },
          {
            "assigned_benefit": -0.09138673543930054,
            "delta_norm": 7.864107131958008,
            "family": "json_schema",
            "route_margin": 0.13674011826515198,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.193281650543213
          },
          {
            "assigned_benefit": -0.0898671845595042,
            "delta_norm": 7.32539701461792,
            "family": "broad_lm",
            "route_margin": 1.3088979721069336,
            "token": "e",
            "token_class": "prose_word",
            "token_total_benefit": -2.1568124294281006
          },
          {
            "assigned_benefit": -0.0860140969355901,
            "delta_norm": 7.896066188812256,
            "family": "code_heavy",
            "route_margin": 0.23981302976608276,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -2.0643383264541626
          },
          {
            "assigned_benefit": -0.08389122287432353,
            "delta_norm": 7.784203052520752,
            "family": "code_heavy",
            "route_margin": 0.3825743794441223,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -2.0133893489837646
          },
          {
            "assigned_benefit": -0.08112131555875142,
            "delta_norm": 7.341672420501709,
            "family": "json_schema",
            "route_margin": 0.2721426486968994,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.9469115734100342
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.41413907210032147,
            "delta_norm": 7.5230536460876465,
            "family": "code_heavy",
            "route_margin": 1.1177518367767334,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.939337730407715
          },
          {
            "assigned_benefit": 0.40207378069559735,
            "delta_norm": 6.900964260101318,
            "family": "code_heavy",
            "route_margin": 0.48656272888183594,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.649770736694336
          },
          {
            "assigned_benefit": 0.39834149678548175,
            "delta_norm": 7.1905436515808105,
            "family": "json_schema",
            "route_margin": 0.5494929552078247,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.560195922851562
          },
          {
            "assigned_benefit": 0.3903733491897583,
            "delta_norm": 6.154618740081787,
            "family": "code_heavy",
            "route_margin": 0.7204625606536865,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.3689603805542
          },
          {
            "assigned_benefit": 0.3894158601760864,
            "delta_norm": 7.8488945960998535,
            "family": "code_heavy",
            "route_margin": 0.8306827545166016,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.345980644226074
          },
          {
            "assigned_benefit": 0.38709576924641925,
            "delta_norm": 7.123656749725342,
            "family": "code_heavy",
            "route_margin": 0.4036943316459656,
            "token": "\\",
            "token_class": "function_signature",
            "token_total_benefit": 9.290298461914062
          },
          {
            "assigned_benefit": 0.3847957452138265,
            "delta_norm": 8.264626502990723,
            "family": "code_heavy",
            "route_margin": 0.9471830129623413,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.235097885131836
          },
          {
            "assigned_benefit": 0.38037506739298504,
            "delta_norm": 9.142560005187988,
            "family": "code_heavy",
            "route_margin": 0.0617716908454895,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.12900161743164
          }
        ],
        "total_assigned_benefit": 48.84134759830586
      },
      "layer_5_expert_2": {
        "activation_count": 394,
        "mean_assigned_benefit": 0.05953450277772265,
        "mean_delta_norm": 8.756121075092839,
        "mean_harm": -0.029623309052164565,
        "mean_positive_benefit": 0.09719321752175447,
        "mean_route_margin": 0.297512247628972,
        "positive_benefit_rate": 0.7030456852791879,
        "prose_benefit": 7.041143556845481,
        "structured_benefit": 18.38937179692068,
        "structured_prose_benefit_ratio": 2.6117024384543788,
        "token_class_benefit": {
          "brace_bracket_paren": 2.152543107668559,
          "comma_colon_semicolon": 1.3815738260746002,
          "function_signature": 1.0470522940158844,
          "identifier": 3.965209560468792,
          "indentation": -0.2805546798432867,
          "json_key": 0.11291907479365668,
          "json_value": 0.7430611327290536,
          "newline": 3.6285039684174345,
          "number": 0.3843221664428711,
          "operator": 0.2928490440050761,
          "other": 1.2504611512025197,
          "prose_word": 5.359985870619618,
          "quote": 3.4723896980285645,
          "space": -1.2626700444767875,
          "string_literal": 1.2089479242761931
        },
        "token_class_counts": {
          "brace_bracket_paren": 7,
          "comma_colon_semicolon": 14,
          "function_signature": 10,
          "identifier": 74,
          "indentation": 17,
          "json_key": 7,
          "json_value": 13,
          "newline": 28,
          "number": 2,
          "operator": 2,
          "other": 6,
          "prose_word": 129,
          "quote": 11,
          "space": 63,
          "string_literal": 11
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.14381763339042664,
            "delta_norm": 8.951623916625977,
            "family": "broad_lm",
            "route_margin": 0.21860164403915405,
            "token": "c",
            "token_class": "prose_word",
            "token_total_benefit": -3.4516232013702393
          },
          {
            "assigned_benefit": -0.10707541306813557,
            "delta_norm": 8.782181739807129,
            "family": "code_heavy",
            "route_margin": 0.025757312774658203,
            "token": "s",
            "token_class": "identifier",
            "token_total_benefit": -2.569809913635254
          },
          {
            "assigned_benefit": -0.08985122044881184,
            "delta_norm": 8.6588134765625,
            "family": "broad_lm",
            "route_margin": 0.07404285669326782,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -2.1564292907714844
          },
          {
            "assigned_benefit": -0.08644822239875793,
            "delta_norm": 7.396280765533447,
            "family": "code_heavy",
            "route_margin": 0.6544162034988403,
            "token": "d",
            "token_class": "string_literal",
            "token_total_benefit": -2.0747573375701904
          },
          {
            "assigned_benefit": -0.08009380102157593,
            "delta_norm": 10.448981285095215,
            "family": "code_heavy",
            "route_margin": 0.23070746660232544,
            "token": "d",
            "token_class": "function_signature",
            "token_total_benefit": -1.9222512245178223
          },
          {
            "assigned_benefit": -0.07598444322745006,
            "delta_norm": 7.619622230529785,
            "family": "json_schema",
            "route_margin": 0.0757896900177002,
            "token": "d",
            "token_class": "json_key",
            "token_total_benefit": -1.8236266374588013
          },
          {
            "assigned_benefit": -0.06769264303147793,
            "delta_norm": 8.246664047241211,
            "family": "code_heavy",
            "route_margin": 0.15677747130393982,
            "token": "l",
            "token_class": "identifier",
            "token_total_benefit": -1.6246234327554703
          },
          {
            "assigned_benefit": -0.06758605192104976,
            "delta_norm": 7.2389655113220215,
            "family": "code_heavy",
            "route_margin": 0.6403883099555969,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.622065246105194
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.3964542547861735,
            "delta_norm": 9.133648872375488,
            "family": "code_heavy",
            "route_margin": 0.01810932159423828,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.514902114868164
          },
          {
            "assigned_benefit": 0.38402652740478516,
            "delta_norm": 8.912996292114258,
            "family": "code_heavy",
            "route_margin": 0.08045327663421631,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 9.216636657714844
          },
          {
            "assigned_benefit": 0.3683640956878662,
            "delta_norm": 9.518763542175293,
            "family": "json_schema",
            "route_margin": 0.42227691411972046,
            "token": "\\n",
            "token_class": "newline",
            "token_total_benefit": 8.840738296508789
          },
          {
            "assigned_benefit": 0.36609824498494464,
            "delta_norm": 8.933442115783691,
            "family": "code_heavy",
            "route_margin": 0.25875717401504517,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.786357879638672
          },
          {
            "assigned_benefit": 0.36353103319803876,
            "delta_norm": 7.048449993133545,
            "family": "code_heavy",
            "route_margin": 0.032087504863739014,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.72474479675293
          },
          {
            "assigned_benefit": 0.3468109766642253,
            "delta_norm": 7.31561803817749,
            "family": "code_heavy",
            "route_margin": 0.2387438416481018,
            "token": "'",
            "token_class": "quote",
            "token_total_benefit": 8.323463439941406
          },
          {
            "assigned_benefit": 0.34638198216756183,
            "delta_norm": 7.457850933074951,
            "family": "code_heavy",
            "route_margin": 0.08656591176986694,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.313167572021484
          },
          {
            "assigned_benefit": 0.3361193339029948,
            "delta_norm": 8.506921768188477,
            "family": "json_schema",
            "route_margin": 0.1147828996181488,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 8.066864013671875
          }
        ],
        "total_assigned_benefit": 23.456594094422726
      },
      "layer_5_expert_3": {
        "activation_count": 2822,
        "mean_assigned_benefit": 0.044558286483197845,
        "mean_delta_norm": 8.582332322649885,
        "mean_harm": -0.021709133309359908,
        "mean_positive_benefit": 0.10115989340193954,
        "mean_route_margin": 0.6142403408040146,
        "positive_benefit_rate": 0.5393338058114813,
        "prose_benefit": 0.4540152685914881,
        "structured_benefit": 119.04216417153793,
        "structured_prose_benefit_ratio": 262.1985920007663,
        "token_class_benefit": {
          "brace_bracket_paren": 11.073692719141642,
          "comma_colon_semicolon": 5.673142810662589,
          "function_signature": 4.166497580707075,
          "identifier": 17.81885198472688,
          "indentation": -10.35845870664343,
          "json_key": 10.044678861896195,
          "json_value": 5.86088079695279,
          "newline": 10.705860396494415,
          "number": 5.736690958340962,
          "operator": 5.734869201978048,
          "other": 7.0919576684633885,
          "prose_word": 17.205102758326884,
          "quote": 37.26971705754596,
          "space": -7.237281436100605,
          "string_literal": 4.957281803091366
        },
        "token_class_counts": {
          "brace_bracket_paren": 70,
          "comma_colon_semicolon": 66,
          "function_signature": 48,
          "identifier": 431,
          "indentation": 863,
          "json_key": 127,
          "json_value": 109,
          "newline": 50,
          "number": 34,
          "operator": 30,
          "other": 28,
          "prose_word": 462,
          "quote": 120,
          "space": 314,
          "string_literal": 70
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.13103054463863373,
            "delta_norm": 9.080863952636719,
            "family": "code_heavy",
            "route_margin": 0.7888226509094238,
            "token": "g",
            "token_class": "identifier",
            "token_total_benefit": -3.1447330713272095
          },
          {
            "assigned_benefit": -0.12831215063730875,
            "delta_norm": 7.634757995605469,
            "family": "json_schema",
            "route_margin": 0.5621022582054138,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -3.07949161529541
          },
          {
            "assigned_benefit": -0.11042344570159912,
            "delta_norm": 7.226682662963867,
            "family": "json_schema",
            "route_margin": 1.0036678314208984,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.650162696838379
          },
          {
            "assigned_benefit": -0.10809943079948425,
            "delta_norm": 8.007893562316895,
            "family": "json_schema",
            "route_margin": 0.7792143225669861,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.594386339187622
          },
          {
            "assigned_benefit": -0.10410678386688232,
            "delta_norm": 7.31412935256958,
            "family": "json_schema",
            "route_margin": 0.7656174898147583,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.498562812805176
          },
          {
            "assigned_benefit": -0.10397198796272278,
            "delta_norm": 8.175979614257812,
            "family": "json_schema",
            "route_margin": 0.9984462261199951,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.4953277111053467
          },
          {
            "assigned_benefit": -0.10358279943466187,
            "delta_norm": 7.3525495529174805,
            "family": "json_schema",
            "route_margin": 0.6937137842178345,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.4859871864318848
          },
          {
            "assigned_benefit": -0.1018477330605189,
            "delta_norm": 8.077892303466797,
            "family": "broad_lm",
            "route_margin": 0.6887856721878052,
            "token": " ",
            "token_class": "indentation",
            "token_total_benefit": -2.4443455934524536
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.4434954325358073,
            "delta_norm": 7.6958909034729,
            "family": "json_schema",
            "route_margin": 0.7211551666259766,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.643890380859375
          },
          {
            "assigned_benefit": 0.4348748524983724,
            "delta_norm": 7.337386131286621,
            "family": "json_schema",
            "route_margin": 0.10327064990997314,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.436996459960938
          },
          {
            "assigned_benefit": 0.42559146881103516,
            "delta_norm": 7.933230876922607,
            "family": "json_schema",
            "route_margin": 0.2543184757232666,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.214195251464844
          },
          {
            "assigned_benefit": 0.40491771697998047,
            "delta_norm": 8.317554473876953,
            "family": "json_schema",
            "route_margin": 0.46882164478302,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.718025207519531
          },
          {
            "assigned_benefit": 0.40347035725911456,
            "delta_norm": 7.71356725692749,
            "family": "json_schema",
            "route_margin": 0.4473304748535156,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.68328857421875
          },
          {
            "assigned_benefit": 0.3999309539794922,
            "delta_norm": 7.910841464996338,
            "family": "json_schema",
            "route_margin": 0.6685733199119568,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.598342895507812
          },
          {
            "assigned_benefit": 0.3995812733968099,
            "delta_norm": 8.50065803527832,
            "family": "json_schema",
            "route_margin": 1.2183740139007568,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.589950561523438
          },
          {
            "assigned_benefit": 0.3989645640055339,
            "delta_norm": 8.366265296936035,
            "family": "json_schema",
            "route_margin": 0.24688708782196045,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.575149536132812
          }
        ],
        "total_assigned_benefit": 125.74348445558432
      },
      "layer_5_expert_4": {
        "activation_count": 99,
        "mean_assigned_benefit": 0.06025433798104222,
        "mean_delta_norm": 7.414476760710128,
        "mean_harm": -0.026630747194091475,
        "mean_positive_benefit": 0.10776961893619345,
        "mean_route_margin": 0.22197980968037037,
        "positive_benefit_rate": 0.6464646464646465,
        "prose_benefit": 0.4546990313877663,
        "structured_benefit": 5.24370842675368,
        "structured_prose_benefit_ratio": 11.532262144367442,
        "token_class_benefit": {
          "brace_bracket_paren": 0.5154111782709757,
          "comma_colon_semicolon": 0.1092000106970469,
          "function_signature": 0.4905656973520915,
          "identifier": 0.29368800421555835,
          "json_key": 0.679109439253807,
          "json_value": 0.6104569087425867,
          "other": 0.3197024663289388,
          "prose_word": 1.0169011851151784,
          "quote": 2.1840216318766275,
          "space": -0.6151326180746157,
          "string_literal": 0.3612555563449859
        },
        "token_class_counts": {
          "brace_bracket_paren": 2,
          "comma_colon_semicolon": 3,
          "function_signature": 3,
          "identifier": 14,
          "json_key": 8,
          "json_value": 10,
          "other": 1,
          "prose_word": 17,
          "quote": 7,
          "space": 29,
          "string_literal": 5
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.08720193554957707,
            "delta_norm": 7.988656520843506,
            "family": "json_schema",
            "route_margin": 0.22340106964111328,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -2.09284645318985
          },
          {
            "assigned_benefit": -0.07468355695406596,
            "delta_norm": 8.396219253540039,
            "family": "json_schema",
            "route_margin": 0.2237950563430786,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.792405366897583
          },
          {
            "assigned_benefit": -0.04966080188751221,
            "delta_norm": 7.38762092590332,
            "family": "code_heavy",
            "route_margin": 0.07902771234512329,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -1.191859245300293
          },
          {
            "assigned_benefit": -0.0456084410349528,
            "delta_norm": 6.94061279296875,
            "family": "code_heavy",
            "route_margin": 0.0028072595596313477,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.0946025848388672
          },
          {
            "assigned_benefit": -0.04185766478379568,
            "delta_norm": 6.964484214782715,
            "family": "json_schema",
            "route_margin": 0.10126468539237976,
            "token": "d",
            "token_class": "json_value",
            "token_total_benefit": -1.0045839548110962
          },
          {
            "assigned_benefit": -0.03862995902697245,
            "delta_norm": 7.253628730773926,
            "family": "code_heavy",
            "route_margin": 0.22049611806869507,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -0.9271190166473389
          },
          {
            "assigned_benefit": -0.038063292702039085,
            "delta_norm": 7.09114933013916,
            "family": "code_heavy",
            "route_margin": 0.9276294112205505,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -0.913519024848938
          },
          {
            "assigned_benefit": -0.03692644089460373,
            "delta_norm": 7.31633186340332,
            "family": "broad_lm",
            "route_margin": 0.230826735496521,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -0.8862345814704895
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.3677576382954915,
            "delta_norm": 8.146347999572754,
            "family": "code_heavy",
            "route_margin": 0.03494638204574585,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.826183319091797
          },
          {
            "assigned_benefit": 0.3564949035644531,
            "delta_norm": 7.014503479003906,
            "family": "code_heavy",
            "route_margin": 0.04298555850982666,
            "token": "\\",
            "token_class": "function_signature",
            "token_total_benefit": 8.555877685546875
          },
          {
            "assigned_benefit": 0.3225291570027669,
            "delta_norm": 7.098679065704346,
            "family": "json_schema",
            "route_margin": 0.6678286790847778,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 7.740699768066406
          },
          {
            "assigned_benefit": 0.3197024663289388,
            "delta_norm": 7.619176387786865,
            "family": "code_heavy",
            "route_margin": 0.0976477861404419,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 7.672859191894531
          },
          {
            "assigned_benefit": 0.3181145985921224,
            "delta_norm": 7.537457466125488,
            "family": "json_schema",
            "route_margin": 0.13190168142318726,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 7.6347503662109375
          },
          {
            "assigned_benefit": 0.3172038396199544,
            "delta_norm": 7.342232704162598,
            "family": "json_schema",
            "route_margin": 0.06603533029556274,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 7.612892150878906
          },
          {
            "assigned_benefit": 0.3146959940592448,
            "delta_norm": 6.650507926940918,
            "family": "code_heavy",
            "route_margin": 0.18342256546020508,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 7.552703857421875
          },
          {
            "assigned_benefit": 0.3101921081542969,
            "delta_norm": 7.238528728485107,
            "family": "json_schema",
            "route_margin": 0.1296144425868988,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 7.444610595703125
          }
        ],
        "total_assigned_benefit": 5.96517946012318
      },
      "layer_5_expert_5": {
        "activation_count": 10,
        "mean_assigned_benefit": 0.019581282759706182,
        "mean_delta_norm": 7.64417200088501,
        "mean_harm": -0.02343927603214979,
        "mean_positive_benefit": 0.048261655287610165,
        "mean_route_margin": 0.07015654444694519,
        "positive_benefit_rate": 0.6,
        "prose_benefit": 0.023437486340602255,
        "structured_benefit": 0.17237534125645956,
        "structured_prose_benefit_ratio": 7.354685513260129,
        "token_class_benefit": {
          "prose_word": 0.11206398904323579,
          "space": -0.08862650270263353,
          "string_literal": 0.17237534125645956
        },
        "token_class_counts": {
          "prose_word": 4,
          "space": 4,
          "string_literal": 2
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.04606493562459946,
            "delta_norm": 7.328732967376709,
            "family": "broad_lm",
            "route_margin": 0.009487152099609375,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.105558454990387
          },
          {
            "assigned_benefit": -0.024836437155803043,
            "delta_norm": 7.448501110076904,
            "family": "broad_lm",
            "route_margin": 0.026199281215667725,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -0.5960744917392731
          },
          {
            "assigned_benefit": -0.01957003523906072,
            "delta_norm": 7.740623474121094,
            "family": "broad_lm",
            "route_margin": 0.09580916166305542,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -0.4696808457374573
          },
          {
            "assigned_benefit": -0.0032856961091359458,
            "delta_norm": 7.0585150718688965,
            "family": "broad_lm",
            "route_margin": 0.10573816299438477,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -0.0788567066192627
          },
          {
            "assigned_benefit": 0.0018449053168296814,
            "delta_norm": 6.859206676483154,
            "family": "code_heavy",
            "route_margin": 0.045997023582458496,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": 0.044277727603912354
          },
          {
            "assigned_benefit": 0.014100650946299234,
            "delta_norm": 9.07684326171875,
            "family": "broad_lm",
            "route_margin": 0.09841740131378174,
            "token": "e",
            "token_class": "prose_word",
            "token_total_benefit": 0.33841562271118164
          },
          {
            "assigned_benefit": 0.026663273572921753,
            "delta_norm": 7.123056888580322,
            "family": "broad_lm",
            "route_margin": 0.10741937160491943,
            "token": "w",
            "token_class": "prose_word",
            "token_total_benefit": 0.6399185657501221
          },
          {
            "assigned_benefit": 0.03672417004903158,
            "delta_norm": 8.113779067993164,
            "family": "code_heavy",
            "route_margin": 0.04305189847946167,
            "token": "u",
            "token_class": "string_literal",
            "token_total_benefit": 0.8813800811767578
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.13565117120742798,
            "delta_norm": 7.64795446395874,
            "family": "code_heavy",
            "route_margin": 0.1404072642326355,
            "token": "r",
            "token_class": "string_literal",
            "token_total_benefit": 3.2556281089782715
          },
          {
            "assigned_benefit": 0.07458576063315074,
            "delta_norm": 8.044507026672363,
            "family": "broad_lm",
            "route_margin": 0.029038727283477783,
            "token": "n",
            "token_class": "prose_word",
            "token_total_benefit": 1.7900582551956177
          },
          {
            "assigned_benefit": 0.03672417004903158,
            "delta_norm": 8.113779067993164,
            "family": "code_heavy",
            "route_margin": 0.04305189847946167,
            "token": "u",
            "token_class": "string_literal",
            "token_total_benefit": 0.8813800811767578
          },
          {
            "assigned_benefit": 0.026663273572921753,
            "delta_norm": 7.123056888580322,
            "family": "broad_lm",
            "route_margin": 0.10741937160491943,
            "token": "w",
            "token_class": "prose_word",
            "token_total_benefit": 0.6399185657501221
          },
          {
            "assigned_benefit": 0.014100650946299234,
            "delta_norm": 9.07684326171875,
            "family": "broad_lm",
            "route_margin": 0.09841740131378174,
            "token": "e",
            "token_class": "prose_word",
            "token_total_benefit": 0.33841562271118164
          },
          {
            "assigned_benefit": 0.0018449053168296814,
            "delta_norm": 6.859206676483154,
            "family": "code_heavy",
            "route_margin": 0.045997023582458496,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": 0.044277727603912354
          },
          {
            "assigned_benefit": -0.0032856961091359458,
            "delta_norm": 7.0585150718688965,
            "family": "broad_lm",
            "route_margin": 0.10573816299438477,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -0.0788567066192627
          },
          {
            "assigned_benefit": -0.01957003523906072,
            "delta_norm": 7.740623474121094,
            "family": "broad_lm",
            "route_margin": 0.09580916166305542,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -0.4696808457374573
          }
        ],
        "total_assigned_benefit": 0.1958128275970618
      },
      "layer_5_expert_6": {
        "activation_count": 156,
        "mean_assigned_benefit": 0.06613224194361232,
        "mean_delta_norm": 8.472826881286425,
        "mean_harm": -0.0338792603255974,
        "mean_positive_benefit": 0.11907950785084101,
        "mean_route_margin": 0.2815989368619063,
        "positive_benefit_rate": 0.6538461538461539,
        "prose_benefit": 1.3346513925741113,
        "structured_benefit": 5.371509198099375,
        "structured_prose_benefit_ratio": 4.024653349920438,
        "token_class_benefit": {
          "brace_bracket_paren": 0.7908029531439145,
          "comma_colon_semicolon": 0.6185386578241984,
          "function_signature": 0.5728152592976887,
          "identifier": 0.2455908469855785,
          "json_key": 0.05992389718691508,
          "json_value": 0.03238067030906677,
          "newline": 1.2967626651128132,
          "number": 0.2669828732808431,
          "operator": 0.03168390194574992,
          "other": 4.579616725444793,
          "prose_word": 1.2815296997626622,
          "quote": 0.6652777989705404,
          "space": -0.91602588010331,
          "string_literal": 0.790749674042066
        },
        "token_class_counts": {
          "brace_bracket_paren": 3,
          "comma_colon_semicolon": 6,
          "function_signature": 2,
          "identifier": 20,
          "json_key": 1,
          "json_value": 1,
          "newline": 7,
          "number": 5,
          "operator": 2,
          "other": 20,
          "prose_word": 29,
          "quote": 2,
          "space": 46,
          "string_literal": 12
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.11974493662516277,
            "delta_norm": 8.15692138671875,
            "family": "code_heavy",
            "route_margin": 0.8241028189659119,
            "token": "5",
            "token_class": "number",
            "token_total_benefit": -2.8738784790039062
          },
          {
            "assigned_benefit": -0.11034655446807544,
            "delta_norm": 8.907612800598145,
            "family": "code_heavy",
            "route_margin": 0.15737587213516235,
            "token": "o",
            "token_class": "identifier",
            "token_total_benefit": -2.6483173072338104
          },
          {
            "assigned_benefit": -0.109354833761851,
            "delta_norm": 7.956670761108398,
            "family": "code_heavy",
            "route_margin": 0.4312193989753723,
            "token": "-",
            "token_class": "operator",
            "token_total_benefit": -2.624516010284424
          },
          {
            "assigned_benefit": -0.10848332444826762,
            "delta_norm": 8.54874324798584,
            "family": "code_heavy",
            "route_margin": 0.21273386478424072,
            "token": "n",
            "token_class": "identifier",
            "token_total_benefit": -2.603599786758423
          },
          {
            "assigned_benefit": -0.10804811120033264,
            "delta_norm": 8.989295959472656,
            "family": "broad_lm",
            "route_margin": 0.08619415760040283,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -2.5931546688079834
          },
          {
            "assigned_benefit": -0.07457296053568523,
            "delta_norm": 6.773540019989014,
            "family": "code_heavy",
            "route_margin": 0.22608911991119385,
            "token": "s",
            "token_class": "identifier",
            "token_total_benefit": -1.7897510528564453
          },
          {
            "assigned_benefit": -0.07094074289004008,
            "delta_norm": 8.732621192932129,
            "family": "code_heavy",
            "route_margin": 0.3444344401359558,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.702577829360962
          },
          {
            "assigned_benefit": -0.060935149590174355,
            "delta_norm": 9.381660461425781,
            "family": "broad_lm",
            "route_margin": 0.35137444734573364,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.4624435901641846
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.4192720651626587,
            "delta_norm": 7.539392471313477,
            "family": "code_heavy",
            "route_margin": 0.6011800765991211,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 10.062529563903809
          },
          {
            "assigned_benefit": 0.38800891240437824,
            "delta_norm": 8.283223152160645,
            "family": "code_heavy",
            "route_margin": 0.06573069095611572,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.312213897705078
          },
          {
            "assigned_benefit": 0.3501269022623698,
            "delta_norm": 7.814321517944336,
            "family": "code_heavy",
            "route_margin": 0.10696524381637573,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 8.403045654296875
          },
          {
            "assigned_benefit": 0.3320792516072591,
            "delta_norm": 9.273311614990234,
            "family": "code_heavy",
            "route_margin": 0.20663130283355713,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 7.969902038574219
          },
          {
            "assigned_benefit": 0.33030128479003906,
            "delta_norm": 9.411198616027832,
            "family": "code_heavy",
            "route_margin": 0.8621888160705566,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 7.9272308349609375
          },
          {
            "assigned_benefit": 0.3259466489156087,
            "delta_norm": 10.430754661560059,
            "family": "json_schema",
            "route_margin": 0.3158003091812134,
            "token": "\\n",
            "token_class": "newline",
            "token_total_benefit": 7.822719573974609
          },
          {
            "assigned_benefit": 0.32006919384002686,
            "delta_norm": 10.500125885009766,
            "family": "json_schema",
            "route_margin": 0.6248213052749634,
            "token": "\\n",
            "token_class": "newline",
            "token_total_benefit": 7.6816606521606445
          },
          {
            "assigned_benefit": 0.3151508967081706,
            "delta_norm": 7.580313682556152,
            "family": "code_heavy",
            "route_margin": 0.26595890522003174,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 7.563621520996094
          }
        ],
        "total_assigned_benefit": 10.316629743203523
      },
      "layer_5_expert_7": {
        "activation_count": 244,
        "mean_assigned_benefit": 0.07871736348682982,
        "mean_delta_norm": 9.653520679864727,
        "mean_harm": -0.028235223070915902,
        "mean_positive_benefit": 0.10984113206183517,
        "mean_route_margin": 0.26428335550867144,
        "positive_benefit_rate": 0.7745901639344263,
        "prose_benefit": 2.674382056420048,
        "structured_benefit": 15.148510397722324,
        "structured_prose_benefit_ratio": 5.664303034548571,
        "token_class_benefit": {
          "brace_bracket_paren": 0.3926299413045248,
          "comma_colon_semicolon": 0.9706304669380189,
          "function_signature": 0.7649311845501264,
          "identifier": 3.3958838606874155,
          "json_key": 0.7673578212658564,
          "json_value": 0.37742045149207115,
          "newline": 1.3607957760492961,
          "number": 0.3770867586135864,
          "operator": 0.21120897928873697,
          "other": 1.777000019947688,
          "prose_word": 3.1769704107816015,
          "quote": 6.118311564127604,
          "space": -0.8954441376651326,
          "string_literal": 0.41225359340508777
        },
        "token_class_counts": {
          "brace_bracket_paren": 3,
          "comma_colon_semicolon": 14,
          "function_signature": 9,
          "identifier": 61,
          "json_key": 8,
          "json_value": 6,
          "newline": 5,
          "number": 5,
          "operator": 1,
          "other": 9,
          "prose_word": 66,
          "quote": 20,
          "space": 32,
          "string_literal": 5
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.11193382243315379,
            "delta_norm": 8.593674659729004,
            "family": "broad_lm",
            "route_margin": 0.30181992053985596,
            "token": "e",
            "token_class": "prose_word",
            "token_total_benefit": -2.686411738395691
          },
          {
            "assigned_benefit": -0.10102646052837372,
            "delta_norm": 10.162944793701172,
            "family": "code_heavy",
            "route_margin": 0.14643186330795288,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.4246350526809692
          },
          {
            "assigned_benefit": -0.07416436572869618,
            "delta_norm": 11.965644836425781,
            "family": "code_heavy",
            "route_margin": 0.4737449586391449,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.7799447774887085
          },
          {
            "assigned_benefit": -0.05815319220225016,
            "delta_norm": 11.504498481750488,
            "family": "broad_lm",
            "route_margin": 0.7154122591018677,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.395676612854004
          },
          {
            "assigned_benefit": -0.05553016314903895,
            "delta_norm": 9.044493675231934,
            "family": "code_heavy",
            "route_margin": 0.4424186944961548,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.3327239155769348
          },
          {
            "assigned_benefit": -0.055422733227411904,
            "delta_norm": 11.183370590209961,
            "family": "json_schema",
            "route_margin": 0.2014697790145874,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.3301455974578857
          },
          {
            "assigned_benefit": -0.05261427412430445,
            "delta_norm": 9.530130386352539,
            "family": "code_heavy",
            "route_margin": 0.04314088821411133,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.2627425789833069
          },
          {
            "assigned_benefit": -0.05062445377310117,
            "delta_norm": 10.150609016418457,
            "family": "json_schema",
            "route_margin": 0.39731717109680176,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -1.214986890554428
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.3538846969604492,
            "delta_norm": 9.521524429321289,
            "family": "json_schema",
            "route_margin": 0.0011162757873535156,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 8.493232727050781
          },
          {
            "assigned_benefit": 0.3438250223795573,
            "delta_norm": 9.594633102416992,
            "family": "code_heavy",
            "route_margin": 0.055827558040618896,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 8.251800537109375
          },
          {
            "assigned_benefit": 0.3410816192626953,
            "delta_norm": 10.456084251403809,
            "family": "code_heavy",
            "route_margin": 0.2337249517440796,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 8.185958862304688
          },
          {
            "assigned_benefit": 0.3352521260579427,
            "delta_norm": 10.543792724609375,
            "family": "code_heavy",
            "route_margin": 0.028185665607452393,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 8.046051025390625
          },
          {
            "assigned_benefit": 0.33243274688720703,
            "delta_norm": 9.178699493408203,
            "family": "code_heavy",
            "route_margin": 0.7448012828826904,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 7.978385925292969
          },
          {
            "assigned_benefit": 0.3318033218383789,
            "delta_norm": 8.681195259094238,
            "family": "code_heavy",
            "route_margin": 0.1361958384513855,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 7.963279724121094
          },
          {
            "assigned_benefit": 0.32611862818400067,
            "delta_norm": 9.169637680053711,
            "family": "json_schema",
            "route_margin": 0.42329394817352295,
            "token": "\\n",
            "token_class": "newline",
            "token_total_benefit": 7.826847076416016
          },
          {
            "assigned_benefit": 0.3237965901692708,
            "delta_norm": 8.88083553314209,
            "family": "code_heavy",
            "route_margin": 0.01938760280609131,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 7.7711181640625
          }
        ],
        "total_assigned_benefit": 19.207036690786477
      },
      "layer_6_expert_0": {
        "activation_count": 88,
        "mean_assigned_benefit": 0.044712125750569015,
        "mean_delta_norm": 7.818682085384022,
        "mean_harm": -0.019962079259624455,
        "mean_positive_benefit": 0.07333841321409722,
        "mean_route_margin": 0.17765485512262041,
        "positive_benefit_rate": 0.6931818181818182,
        "prose_benefit": 2.0850019774710136,
        "structured_benefit": 2.263189125185211,
        "structured_prose_benefit_ratio": 1.0854613806795177,
        "token_class_benefit": {
          "brace_bracket_paren": 0.1520169973373413,
          "comma_colon_semicolon": 0.13193978865941366,
          "function_signature": 0.6439742048581442,
          "identifier": 1.0382483433932068,
          "newline": 0.2815842479467392,
          "number": -0.047960917154947914,
          "prose_word": 1.8430880280211568,
          "space": -0.17161008715629578,
          "string_literal": 0.06338646014531453
        },
        "token_class_counts": {
          "brace_bracket_paren": 1,
          "comma_colon_semicolon": 1,
          "function_signature": 4,
          "identifier": 23,
          "newline": 2,
          "number": 1,
          "prose_word": 40,
          "space": 14,
          "string_literal": 2
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.05253798762957255,
            "delta_norm": 7.589599609375,
            "family": "code_heavy",
            "route_margin": 0.46849602460861206,
            "token": "r",
            "token_class": "identifier",
            "token_total_benefit": -1.2609117031097412
          },
          {
            "assigned_benefit": -0.047960917154947914,
            "delta_norm": 7.996909141540527,
            "family": "code_heavy",
            "route_margin": 0.004544287919998169,
            "token": "7",
            "token_class": "number",
            "token_total_benefit": -1.15106201171875
          },
          {
            "assigned_benefit": -0.04590752969185511,
            "delta_norm": 7.199739456176758,
            "family": "broad_lm",
            "route_margin": 0.10869491100311279,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.1017807126045227
          },
          {
            "assigned_benefit": -0.036021401484807335,
            "delta_norm": 8.302377700805664,
            "family": "broad_lm",
            "route_margin": 0.045945972204208374,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -0.864513635635376
          },
          {
            "assigned_benefit": -0.03563376019398371,
            "delta_norm": 8.282944679260254,
            "family": "code_heavy",
            "route_margin": 0.10901570320129395,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -0.8552102446556091
          },
          {
            "assigned_benefit": -0.03521106640497843,
            "delta_norm": 8.577851295471191,
            "family": "broad_lm",
            "route_margin": 0.0008783936500549316,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -0.8450655937194824
          },
          {
            "assigned_benefit": -0.03369841476281484,
            "delta_norm": 7.402703285217285,
            "family": "broad_lm",
            "route_margin": 0.6279592514038086,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -0.8087619543075562
          },
          {
            "assigned_benefit": -0.026568233966827393,
            "delta_norm": 7.877625465393066,
            "family": "broad_lm",
            "route_margin": 0.20850247144699097,
            "token": "u",
            "token_class": "prose_word",
            "token_total_benefit": -0.6376376152038574
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.33899720509847003,
            "delta_norm": 8.015220642089844,
            "family": "code_heavy",
            "route_margin": 0.049766719341278076,
            "token": "\"",
            "token_class": "function_signature",
            "token_total_benefit": 8.135932922363281
          },
          {
            "assigned_benefit": 0.18324036399523416,
            "delta_norm": 7.978236675262451,
            "family": "broad_lm",
            "route_margin": 0.5229619741439819,
            "token": "i",
            "token_class": "prose_word",
            "token_total_benefit": 4.39776873588562
          },
          {
            "assigned_benefit": 0.17835324009259543,
            "delta_norm": 7.419998645782471,
            "family": "broad_lm",
            "route_margin": 0.2406156063079834,
            "token": "i",
            "token_class": "prose_word",
            "token_total_benefit": 4.28047776222229
          },
          {
            "assigned_benefit": 0.15743468205134073,
            "delta_norm": 7.873260974884033,
            "family": "code_heavy",
            "route_margin": 0.09381794929504395,
            "token": ":",
            "token_class": "function_signature",
            "token_total_benefit": 3.7784323692321777
          },
          {
            "assigned_benefit": 0.15597114463647208,
            "delta_norm": 8.265265464782715,
            "family": "broad_lm",
            "route_margin": 0.002710580825805664,
            "token": "byte_13",
            "token_class": "newline",
            "token_total_benefit": 3.7433074712753296
          },
          {
            "assigned_benefit": 0.1520169973373413,
            "delta_norm": 7.2465291023254395,
            "family": "code_heavy",
            "route_margin": 0.12314280867576599,
            "token": ")",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 3.6484079360961914
          },
          {
            "assigned_benefit": 0.14099750916163126,
            "delta_norm": 8.433695793151855,
            "family": "code_heavy",
            "route_margin": 0.24307850003242493,
            "token": "k",
            "token_class": "identifier",
            "token_total_benefit": 3.3839402198791504
          },
          {
            "assigned_benefit": 0.13193978865941366,
            "delta_norm": 7.258214473724365,
            "family": "broad_lm",
            "route_margin": 0.009322643280029297,
            "token": ",",
            "token_class": "comma_colon_semicolon",
            "token_total_benefit": 3.1665549278259277
          }
        ],
        "total_assigned_benefit": 3.934667066050073
      },
      "layer_6_expert_1": {
        "activation_count": 2540,
        "mean_assigned_benefit": 0.04415461903272519,
        "mean_delta_norm": 7.950529342561256,
        "mean_harm": -0.020475747859440188,
        "mean_positive_benefit": 0.10103508256698468,
        "mean_route_margin": 0.39498403314941044,
        "positive_benefit_rate": 0.5318897637795276,
        "prose_benefit": 8.36300616371855,
        "structured_benefit": 99.37895659266137,
        "structured_prose_benefit_ratio": 11.883161945258358,
        "token_class_benefit": {
          "brace_bracket_paren": 10.602369348208109,
          "comma_colon_semicolon": 3.5582560300827026,
          "function_signature": 5.18851576000452,
          "identifier": 17.33942305855453,
          "indentation": -8.145512205548586,
          "json_key": 6.740736308197182,
          "json_value": 4.3415311534578604,
          "newline": 4.146945451716314,
          "number": 3.849066317081452,
          "operator": 3.583472371101379,
          "other": 6.9576022525628405,
          "prose_word": 21.89487395435572,
          "quote": 36.52765162785846,
          "space": -7.933188250909246,
          "string_literal": 3.5009891663988415
        },
        "token_class_counts": {
          "brace_bracket_paren": 62,
          "comma_colon_semicolon": 38,
          "function_signature": 41,
          "identifier": 394,
          "indentation": 757,
          "json_key": 73,
          "json_value": 74,
          "newline": 25,
          "number": 25,
          "operator": 18,
          "other": 34,
          "prose_word": 512,
          "quote": 117,
          "space": 313,
          "string_literal": 57
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.11974493662516277,
            "delta_norm": 7.962776184082031,
            "family": "code_heavy",
            "route_margin": 0.30684834718704224,
            "token": "5",
            "token_class": "number",
            "token_total_benefit": -2.8738784790039062
          },
          {
            "assigned_benefit": -0.10707541306813557,
            "delta_norm": 8.3117094039917,
            "family": "code_heavy",
            "route_margin": 0.5134329199790955,
            "token": "s",
            "token_class": "identifier",
            "token_total_benefit": -2.569809913635254
          },
          {
            "assigned_benefit": -0.10358279943466187,
            "delta_norm": 6.506479263305664,
            "family": "json_schema",
            "route_margin": 0.17195656895637512,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.4859871864318848
          },
          {
            "assigned_benefit": -0.1018477330605189,
            "delta_norm": 7.774506092071533,
            "family": "broad_lm",
            "route_margin": 0.2562510371208191,
            "token": " ",
            "token_class": "indentation",
            "token_total_benefit": -2.4443455934524536
          },
          {
            "assigned_benefit": -0.10029297073682149,
            "delta_norm": 6.809975624084473,
            "family": "json_schema",
            "route_margin": 0.34665071964263916,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.407031297683716
          },
          {
            "assigned_benefit": -0.09784005582332611,
            "delta_norm": 7.896010398864746,
            "family": "code_heavy",
            "route_margin": 0.67920982837677,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -2.3481613397598267
          },
          {
            "assigned_benefit": -0.0975755254427592,
            "delta_norm": 6.870985984802246,
            "family": "code_heavy",
            "route_margin": 0.06514501571655273,
            "token": "s",
            "token_class": "string_literal",
            "token_total_benefit": -2.3418126106262207
          },
          {
            "assigned_benefit": -0.09750870863596599,
            "delta_norm": 8.496889114379883,
            "family": "code_heavy",
            "route_margin": 0.22588026523590088,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -2.3402090072631836
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.4348748524983724,
            "delta_norm": 7.676216125488281,
            "family": "json_schema",
            "route_margin": 0.28156864643096924,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.436996459960938
          },
          {
            "assigned_benefit": 0.4192720651626587,
            "delta_norm": 9.062240600585938,
            "family": "code_heavy",
            "route_margin": 0.6131228804588318,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 10.062529563903809
          },
          {
            "assigned_benefit": 0.40491771697998047,
            "delta_norm": 7.674118995666504,
            "family": "json_schema",
            "route_margin": 0.10107791423797607,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.718025207519531
          },
          {
            "assigned_benefit": 0.40347035725911456,
            "delta_norm": 8.517319679260254,
            "family": "json_schema",
            "route_margin": 0.02306535840034485,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.68328857421875
          },
          {
            "assigned_benefit": 0.3989645640055339,
            "delta_norm": 7.3019795417785645,
            "family": "json_schema",
            "route_margin": 0.08959197998046875,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.575149536132812
          },
          {
            "assigned_benefit": 0.39834149678548175,
            "delta_norm": 8.36829948425293,
            "family": "json_schema",
            "route_margin": 0.02532869577407837,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.560195922851562
          },
          {
            "assigned_benefit": 0.3949778874715169,
            "delta_norm": 6.984790802001953,
            "family": "json_schema",
            "route_margin": 0.19107937812805176,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.479469299316406
          },
          {
            "assigned_benefit": 0.38902703921000165,
            "delta_norm": 7.806856155395508,
            "family": "code_heavy",
            "route_margin": 0.5448755025863647,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.336648941040039
          }
        ],
        "total_assigned_benefit": 112.15273234312198
      },
      "layer_6_expert_2": {
        "activation_count": 213,
        "mean_assigned_benefit": 0.05568558435462796,
        "mean_delta_norm": 8.331206379921783,
        "mean_harm": -0.025672155333107658,
        "mean_positive_benefit": 0.09383955882887635,
        "mean_route_margin": 0.2559591121097126,
        "positive_benefit_rate": 0.6807511737089202,
        "prose_benefit": 4.1770573938168445,
        "structured_benefit": 7.400770190482334,
        "structured_prose_benefit_ratio": 1.7717664596702554,
        "token_class_benefit": {
          "comma_colon_semicolon": 0.7943330009778341,
          "function_signature": 0.8277038087447484,
          "identifier": 2.143765487397711,
          "json_value": 0.27239150802294415,
          "newline": 0.568512499332428,
          "number": 0.20653796195983887,
          "other": 1.2931407563446555,
          "prose_word": 4.1195060003859325,
          "quote": 1.510057767232259,
          "space": -0.9523874796771756,
          "string_literal": 1.0774681568145752
        },
        "token_class_counts": {
          "comma_colon_semicolon": 6,
          "function_signature": 5,
          "identifier": 38,
          "json_value": 3,
          "newline": 3,
          "number": 3,
          "other": 7,
          "prose_word": 82,
          "quote": 5,
          "space": 52,
          "string_literal": 9
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.09491795673966408,
            "delta_norm": 8.089835166931152,
            "family": "broad_lm",
            "route_margin": 0.03342097997665405,
            "token": "l",
            "token_class": "prose_word",
            "token_total_benefit": -2.278030961751938
          },
          {
            "assigned_benefit": -0.084659809867541,
            "delta_norm": 8.5264253616333,
            "family": "json_schema",
            "route_margin": 0.06827539205551147,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.031835436820984
          },
          {
            "assigned_benefit": -0.08465861777464549,
            "delta_norm": 8.5264253616333,
            "family": "json_schema",
            "route_margin": 0.06827479600906372,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.0318068265914917
          },
          {
            "assigned_benefit": -0.07861356933911641,
            "delta_norm": 9.625563621520996,
            "family": "code_heavy",
            "route_margin": 0.4123387932777405,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.886725664138794
          },
          {
            "assigned_benefit": -0.07094074289004008,
            "delta_norm": 7.8045654296875,
            "family": "code_heavy",
            "route_margin": 0.07619619369506836,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.702577829360962
          },
          {
            "assigned_benefit": -0.06990201274553935,
            "delta_norm": 9.143348693847656,
            "family": "json_schema",
            "route_margin": 0.08671489357948303,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.6776483058929443
          },
          {
            "assigned_benefit": -0.06702599922815959,
            "delta_norm": 8.252337455749512,
            "family": "broad_lm",
            "route_margin": 0.14202415943145752,
            "token": "n",
            "token_class": "prose_word",
            "token_total_benefit": -1.60862398147583
          },
          {
            "assigned_benefit": -0.0561104342341423,
            "delta_norm": 6.995944023132324,
            "family": "code_heavy",
            "route_margin": 0.04808694124221802,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -1.3466504216194153
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.36769771575927734,
            "delta_norm": 9.268434524536133,
            "family": "code_heavy",
            "route_margin": 0.286008358001709,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 8.824745178222656
          },
          {
            "assigned_benefit": 0.35744380950927734,
            "delta_norm": 7.323844909667969,
            "family": "code_heavy",
            "route_margin": 0.05898714065551758,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 8.578651428222656
          },
          {
            "assigned_benefit": 0.3417193094889323,
            "delta_norm": 7.634602069854736,
            "family": "code_heavy",
            "route_margin": 0.030006110668182373,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 8.201263427734375
          },
          {
            "assigned_benefit": 0.3145589828491211,
            "delta_norm": 7.255947113037109,
            "family": "code_heavy",
            "route_margin": 0.015940368175506592,
            "token": "\\",
            "token_class": "string_literal",
            "token_total_benefit": 7.549415588378906
          },
          {
            "assigned_benefit": 0.30634339650472003,
            "delta_norm": 8.537121772766113,
            "family": "json_schema",
            "route_margin": 0.4985279142856598,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 7.352241516113281
          },
          {
            "assigned_benefit": 0.30479780832926434,
            "delta_norm": 8.720519065856934,
            "family": "code_heavy",
            "route_margin": 0.06109827756881714,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 7.315147399902344
          },
          {
            "assigned_benefit": 0.291195551554362,
            "delta_norm": 7.796774864196777,
            "family": "code_heavy",
            "route_margin": 0.5272693634033203,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 6.9886932373046875
          },
          {
            "assigned_benefit": 0.27970584233601886,
            "delta_norm": 7.455248832702637,
            "family": "code_heavy",
            "route_margin": 0.3669489622116089,
            "token": "_",
            "token_class": "function_signature",
            "token_total_benefit": 6.712940216064453
          }
        ],
        "total_assigned_benefit": 11.861029467535756
      },
      "layer_6_expert_3": {
        "activation_count": 1082,
        "mean_assigned_benefit": 0.05585395307272498,
        "mean_delta_norm": 9.128272540467945,
        "mean_harm": -0.032657100995642604,
        "mean_positive_benefit": 0.086162949254945,
        "mean_route_margin": 0.37409829742201156,
        "positive_benefit_rate": 0.744916820702403,
        "prose_benefit": 22.278000920835282,
        "structured_benefit": 37.271160864347166,
        "structured_prose_benefit_ratio": 1.6730029322105682,
        "token_class_benefit": {
          "brace_bracket_paren": 4.077004313468933,
          "comma_colon_semicolon": 1.8349930842717488,
          "function_signature": 0.760093073050181,
          "identifier": 13.403233615060653,
          "indentation": -0.2940380812312165,
          "json_key": 1.8757851223150879,
          "json_value": 2.4774874706442165,
          "newline": 2.7169787238800636,
          "number": 0.990230639775594,
          "operator": 1.8591939012209575,
          "other": 4.586720026777887,
          "prose_word": 22.849132659534643,
          "quote": 4.392459233601888,
          "space": -3.978998244740069,
          "string_literal": 2.8837016870578127
        },
        "token_class_counts": {
          "brace_bracket_paren": 15,
          "comma_colon_semicolon": 24,
          "function_signature": 5,
          "identifier": 231,
          "indentation": 11,
          "json_key": 47,
          "json_value": 55,
          "newline": 25,
          "number": 7,
          "operator": 9,
          "other": 24,
          "prose_word": 447,
          "quote": 14,
          "space": 140,
          "string_literal": 28
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.1176329255104065,
            "delta_norm": 9.788725852966309,
            "family": "broad_lm",
            "route_margin": 0.4464530944824219,
            "token": "o",
            "token_class": "prose_word",
            "token_total_benefit": -2.823190212249756
          },
          {
            "assigned_benefit": -0.11193382243315379,
            "delta_norm": 8.833525657653809,
            "family": "broad_lm",
            "route_margin": 0.5078842639923096,
            "token": "e",
            "token_class": "prose_word",
            "token_total_benefit": -2.686411738395691
          },
          {
            "assigned_benefit": -0.11105093856652577,
            "delta_norm": 9.540979385375977,
            "family": "broad_lm",
            "route_margin": 0.7806714177131653,
            "token": "o",
            "token_class": "prose_word",
            "token_total_benefit": -2.6652225255966187
          },
          {
            "assigned_benefit": -0.11034655446807544,
            "delta_norm": 9.158174514770508,
            "family": "code_heavy",
            "route_margin": 0.4754577875137329,
            "token": "o",
            "token_class": "identifier",
            "token_total_benefit": -2.6483173072338104
          },
          {
            "assigned_benefit": -0.10964437325795491,
            "delta_norm": 7.682583332061768,
            "family": "code_heavy",
            "route_margin": 0.3013201951980591,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -2.631464958190918
          },
          {
            "assigned_benefit": -0.10870074232419331,
            "delta_norm": 9.70616626739502,
            "family": "broad_lm",
            "route_margin": 0.7287104725837708,
            "token": "o",
            "token_class": "prose_word",
            "token_total_benefit": -2.6088178157806396
          },
          {
            "assigned_benefit": -0.10804811120033264,
            "delta_norm": 8.054665565490723,
            "family": "broad_lm",
            "route_margin": 0.048385024070739746,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -2.5931546688079834
          },
          {
            "assigned_benefit": -0.10159913450479507,
            "delta_norm": 10.433250427246094,
            "family": "broad_lm",
            "route_margin": 0.42037004232406616,
            "token": "p",
            "token_class": "prose_word",
            "token_total_benefit": -2.438379228115082
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.4194428126017253,
            "delta_norm": 9.945106506347656,
            "family": "json_schema",
            "route_margin": 0.3236631751060486,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.066627502441406
          },
          {
            "assigned_benefit": 0.40207378069559735,
            "delta_norm": 8.882009506225586,
            "family": "code_heavy",
            "route_margin": 0.5394994020462036,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.649770736694336
          },
          {
            "assigned_benefit": 0.3964542547861735,
            "delta_norm": 8.847498893737793,
            "family": "code_heavy",
            "route_margin": 0.6081336736679077,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.514902114868164
          },
          {
            "assigned_benefit": 0.38709576924641925,
            "delta_norm": 9.574865341186523,
            "family": "code_heavy",
            "route_margin": 0.02839958667755127,
            "token": "\\",
            "token_class": "function_signature",
            "token_total_benefit": 9.290298461914062
          },
          {
            "assigned_benefit": 0.38402652740478516,
            "delta_norm": 8.90258502960205,
            "family": "code_heavy",
            "route_margin": 0.40688270330429077,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 9.216636657714844
          },
          {
            "assigned_benefit": 0.38037506739298504,
            "delta_norm": 8.704069137573242,
            "family": "code_heavy",
            "route_margin": 0.009760141372680664,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.12900161743164
          },
          {
            "assigned_benefit": 0.37155044078826904,
            "delta_norm": 8.379066467285156,
            "family": "code_heavy",
            "route_margin": 0.5351663827896118,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.917210578918457
          },
          {
            "assigned_benefit": 0.36609824498494464,
            "delta_norm": 9.090102195739746,
            "family": "code_heavy",
            "route_margin": 0.21823930740356445,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.786357879638672
          }
        ],
        "total_assigned_benefit": 60.43397722468843
      },
      "layer_6_expert_4": {
        "activation_count": 1235,
        "mean_assigned_benefit": 0.06443460182711143,
        "mean_delta_norm": 9.152175916833917,
        "mean_harm": -0.029409823448992775,
        "mean_positive_benefit": 0.10807281619037692,
        "mean_route_margin": 0.29514356040761536,
        "positive_benefit_rate": 0.682591093117409,
        "prose_benefit": 9.872314339916947,
        "structured_benefit": 64.475974310758,
        "structured_prose_benefit_ratio": 6.530988792573274,
        "token_class_benefit": {
          "brace_bracket_paren": 4.776043350808322,
          "comma_colon_semicolon": 5.234335626165073,
          "function_signature": 3.3728436107436823,
          "identifier": 12.686829427878072,
          "indentation": -2.150918380202104,
          "json_key": 4.968614061673482,
          "json_value": 2.1732594134906935,
          "newline": 8.042744989454533,
          "number": 2.8953399062156677,
          "operator": 2.406367321809133,
          "other": 7.38129981358846,
          "prose_word": 14.706950790869692,
          "quote": 11.545080025990803,
          "space": -4.836573278531433,
          "string_literal": 6.37451657652855
        },
        "token_class_counts": {
          "brace_bracket_paren": 23,
          "comma_colon_semicolon": 55,
          "function_signature": 34,
          "identifier": 213,
          "indentation": 123,
          "json_key": 55,
          "json_value": 45,
          "newline": 41,
          "number": 23,
          "operator": 15,
          "other": 30,
          "prose_word": 253,
          "quote": 37,
          "space": 225,
          "string_literal": 63
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.17974231019616127,
            "delta_norm": 10.291979789733887,
            "family": "broad_lm",
            "route_margin": 0.1490834355354309,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -4.3138154447078705
          },
          {
            "assigned_benefit": -0.12831215063730875,
            "delta_norm": 9.657597541809082,
            "family": "json_schema",
            "route_margin": 0.552362322807312,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -3.07949161529541
          },
          {
            "assigned_benefit": -0.1258842075864474,
            "delta_norm": 9.800804138183594,
            "family": "broad_lm",
            "route_margin": 0.28655317425727844,
            "token": "m",
            "token_class": "prose_word",
            "token_total_benefit": -3.0212209820747375
          },
          {
            "assigned_benefit": -0.12130660812060039,
            "delta_norm": 9.355781555175781,
            "family": "json_schema",
            "route_margin": 0.0037116408348083496,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.911358594894409
          },
          {
            "assigned_benefit": -0.11696084340413411,
            "delta_norm": 9.574816703796387,
            "family": "json_schema",
            "route_margin": 0.35374167561531067,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.8070602416992188
          },
          {
            "assigned_benefit": -0.11042344570159912,
            "delta_norm": 8.473154067993164,
            "family": "json_schema",
            "route_margin": 0.22652041912078857,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.650162696838379
          },
          {
            "assigned_benefit": -0.109354833761851,
            "delta_norm": 9.104754447937012,
            "family": "code_heavy",
            "route_margin": 0.26094532012939453,
            "token": "-",
            "token_class": "operator",
            "token_total_benefit": -2.624516010284424
          },
          {
            "assigned_benefit": -0.10848332444826762,
            "delta_norm": 8.059155464172363,
            "family": "code_heavy",
            "route_margin": 0.20047527551651,
            "token": "n",
            "token_class": "identifier",
            "token_total_benefit": -2.603599786758423
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.4434954325358073,
            "delta_norm": 8.556255340576172,
            "family": "json_schema",
            "route_margin": 0.33876097202301025,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.643890380859375
          },
          {
            "assigned_benefit": 0.42559146881103516,
            "delta_norm": 9.591582298278809,
            "family": "json_schema",
            "route_margin": 0.7515382170677185,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.214195251464844
          },
          {
            "assigned_benefit": 0.41413907210032147,
            "delta_norm": 8.516375541687012,
            "family": "code_heavy",
            "route_margin": 0.8303594589233398,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.939337730407715
          },
          {
            "assigned_benefit": 0.3999309539794922,
            "delta_norm": 9.389115333557129,
            "family": "json_schema",
            "route_margin": 0.5127784609794617,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.598342895507812
          },
          {
            "assigned_benefit": 0.3995812733968099,
            "delta_norm": 9.59988021850586,
            "family": "json_schema",
            "route_margin": 0.24375930428504944,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.589950561523438
          },
          {
            "assigned_benefit": 0.3903733491897583,
            "delta_norm": 8.587285041809082,
            "family": "code_heavy",
            "route_margin": 0.6150321364402771,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.3689603805542
          },
          {
            "assigned_benefit": 0.3894158601760864,
            "delta_norm": 8.607975006103516,
            "family": "code_heavy",
            "route_margin": 0.7441513538360596,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.345980644226074
          },
          {
            "assigned_benefit": 0.3847957452138265,
            "delta_norm": 8.86337947845459,
            "family": "code_heavy",
            "route_margin": 0.7773919105529785,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.235097885131836
          }
        ],
        "total_assigned_benefit": 79.57673325648261
      },
      "layer_6_expert_5": {
        "activation_count": 602,
        "mean_assigned_benefit": 0.06513397838143738,
        "mean_delta_norm": 8.038602828979492,
        "mean_harm": -0.03158239045669922,
        "mean_positive_benefit": 0.09896302219029227,
        "mean_route_margin": 0.2487462991941411,
        "positive_benefit_rate": 0.7408637873754153,
        "prose_benefit": 5.545625665535531,
        "structured_benefit": 30.701941125560555,
        "structured_prose_benefit_ratio": 5.536244776917471,
        "token_class_benefit": {
          "brace_bracket_paren": 1.4424988577763238,
          "comma_colon_semicolon": 4.263758371273677,
          "function_signature": 1.8840378175179162,
          "identifier": 4.349982466548681,
          "json_key": 2.3731056600809093,
          "json_value": 1.343914778747906,
          "newline": 8.092675348122917,
          "number": 1.336384892463684,
          "operator": 0.22826647758483887,
          "other": 4.2026496430238085,
          "prose_word": 5.8873258565242095,
          "quote": 4.232961813608806,
          "space": -1.5812616394832733,
          "string_literal": 1.154354641834895
        },
        "token_class_counts": {
          "brace_bracket_paren": 11,
          "comma_colon_semicolon": 42,
          "function_signature": 15,
          "identifier": 116,
          "json_key": 31,
          "json_value": 30,
          "newline": 32,
          "number": 9,
          "operator": 3,
          "other": 17,
          "prose_word": 126,
          "quote": 14,
          "space": 134,
          "string_literal": 22
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.14390301704406738,
            "delta_norm": 8.34851360321045,
            "family": "json_schema",
            "route_margin": 0.5195884704589844,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -3.453672409057617
          },
          {
            "assigned_benefit": -0.13103054463863373,
            "delta_norm": 8.286983489990234,
            "family": "code_heavy",
            "route_margin": 0.6003637909889221,
            "token": "g",
            "token_class": "identifier",
            "token_total_benefit": -3.1447330713272095
          },
          {
            "assigned_benefit": -0.10949698835611343,
            "delta_norm": 8.928153038024902,
            "family": "broad_lm",
            "route_margin": 0.0004296302795410156,
            "token": "o",
            "token_class": "prose_word",
            "token_total_benefit": -2.6279277205467224
          },
          {
            "assigned_benefit": -0.10410678386688232,
            "delta_norm": 8.168941497802734,
            "family": "json_schema",
            "route_margin": 0.22638893127441406,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.498562812805176
          },
          {
            "assigned_benefit": -0.09626823663711548,
            "delta_norm": 7.0411200523376465,
            "family": "broad_lm",
            "route_margin": 0.2793067693710327,
            "token": "o",
            "token_class": "prose_word",
            "token_total_benefit": -2.3104376792907715
          },
          {
            "assigned_benefit": -0.09525191783905029,
            "delta_norm": 8.215378761291504,
            "family": "json_schema",
            "route_margin": 0.11349445581436157,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.286046028137207
          },
          {
            "assigned_benefit": -0.0939420076707999,
            "delta_norm": 7.507795333862305,
            "family": "json_schema",
            "route_margin": 0.21290552616119385,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -2.2546081840991974
          },
          {
            "assigned_benefit": -0.09014518062273662,
            "delta_norm": 9.154180526733398,
            "family": "json_schema",
            "route_margin": 0.11142703890800476,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.1634843349456787
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.3683640956878662,
            "delta_norm": 10.637124061584473,
            "family": "json_schema",
            "route_margin": 0.425925076007843,
            "token": "\\n",
            "token_class": "newline",
            "token_total_benefit": 8.840738296508789
          },
          {
            "assigned_benefit": 0.3612794876098633,
            "delta_norm": 9.03235149383545,
            "family": "json_schema",
            "route_margin": 0.8352305293083191,
            "token": "\\n",
            "token_class": "newline",
            "token_total_benefit": 8.670707702636719
          },
          {
            "assigned_benefit": 0.3433542251586914,
            "delta_norm": 8.75714111328125,
            "family": "json_schema",
            "route_margin": 0.08073985576629639,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 8.240501403808594
          },
          {
            "assigned_benefit": 0.3353669246037801,
            "delta_norm": 6.714348316192627,
            "family": "code_heavy",
            "route_margin": 0.28660744428634644,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.048806190490723
          },
          {
            "assigned_benefit": 0.3337658842404683,
            "delta_norm": 8.884112358093262,
            "family": "json_schema",
            "route_margin": 0.3000009059906006,
            "token": "\\n",
            "token_class": "newline",
            "token_total_benefit": 8.01038122177124
          },
          {
            "assigned_benefit": 0.32812609275182086,
            "delta_norm": 7.508248805999756,
            "family": "json_schema",
            "route_margin": 0.11431348323822021,
            "token": "\\n",
            "token_class": "newline",
            "token_total_benefit": 7.875026226043701
          },
          {
            "assigned_benefit": 0.3259466489156087,
            "delta_norm": 10.604063987731934,
            "family": "json_schema",
            "route_margin": 0.8707398176193237,
            "token": "\\n",
            "token_class": "newline",
            "token_total_benefit": 7.822719573974609
          },
          {
            "assigned_benefit": 0.32491715749104816,
            "delta_norm": 8.046700477600098,
            "family": "json_schema",
            "route_margin": 0.27197104692459106,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 7.798011779785156
          }
        ],
        "total_assigned_benefit": 39.210654985625304
      },
      "layer_6_expert_6": {
        "activation_count": 110,
        "mean_assigned_benefit": 0.05315389748324047,
        "mean_delta_norm": 8.18676740472967,
        "mean_harm": -0.011070287248326675,
        "mean_positive_benefit": 0.07723796675757814,
        "mean_route_margin": 0.2615840646353635,
        "positive_benefit_rate": 0.7272727272727273,
        "prose_benefit": 1.990940586974223,
        "structured_benefit": 3.022937726229429,
        "structured_prose_benefit_ratio": 1.5183465272681025,
        "token_class_benefit": {
          "brace_bracket_paren": 0.405807097752889,
          "comma_colon_semicolon": 0.10566226641337077,
          "function_signature": 0.18026649951934814,
          "identifier": 0.6245479670663675,
          "json_key": 0.05967957774798075,
          "json_value": 0.009228698909282684,
          "newline": 0.8871388832728069,
          "number": 0.07619424661000569,
          "other": 0.8330504099527994,
          "prose_word": 2.0649097617715593,
          "space": -0.07396917479733627,
          "string_literal": 0.6744124889373779
        },
        "token_class_counts": {
          "brace_bracket_paren": 3,
          "comma_colon_semicolon": 1,
          "function_signature": 4,
          "identifier": 17,
          "json_key": 1,
          "json_value": 2,
          "newline": 3,
          "number": 1,
          "other": 3,
          "prose_word": 57,
          "space": 8,
          "string_literal": 10
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.04466720422108968,
            "delta_norm": 8.134963989257812,
            "family": "code_heavy",
            "route_margin": 0.28561967611312866,
            "token": "a",
            "token_class": "function_signature",
            "token_total_benefit": -1.0720129013061523
          },
          {
            "assigned_benefit": -0.04110099871953329,
            "delta_norm": 7.8581743240356445,
            "family": "code_heavy",
            "route_margin": 0.20251944661140442,
            "token": "d",
            "token_class": "string_literal",
            "token_total_benefit": -0.9864239692687988
          },
          {
            "assigned_benefit": -0.02204131583372752,
            "delta_norm": 8.40340518951416,
            "family": "code_heavy",
            "route_margin": 0.24654901027679443,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -0.5289915800094604
          },
          {
            "assigned_benefit": -0.018857359886169434,
            "delta_norm": 7.928022384643555,
            "family": "broad_lm",
            "route_margin": 0.26596522331237793,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -0.4525766372680664
          },
          {
            "assigned_benefit": -0.018108924229939777,
            "delta_norm": 8.014461517333984,
            "family": "broad_lm",
            "route_margin": 0.16227298974990845,
            "token": "e",
            "token_class": "prose_word",
            "token_total_benefit": -0.4346141815185547
          },
          {
            "assigned_benefit": -0.01710745443900426,
            "delta_norm": 8.452668190002441,
            "family": "broad_lm",
            "route_margin": 0.15519481897354126,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -0.4105789065361023
          },
          {
            "assigned_benefit": -0.013693584750096003,
            "delta_norm": 8.848060607910156,
            "family": "broad_lm",
            "route_margin": 0.9539815783500671,
            "token": "e",
            "token_class": "prose_word",
            "token_total_benefit": -0.3286460340023041
          },
          {
            "assigned_benefit": -0.012998394668102264,
            "delta_norm": 8.167616844177246,
            "family": "broad_lm",
            "route_margin": 0.5222158432006836,
            "token": "e",
            "token_class": "prose_word",
            "token_total_benefit": -0.31196147203445435
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.3219327926635742,
            "delta_norm": 8.815878868103027,
            "family": "code_heavy",
            "route_margin": 0.181901752948761,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 7.726387023925781
          },
          {
            "assigned_benefit": 0.315925399462382,
            "delta_norm": 8.338040351867676,
            "family": "json_schema",
            "route_margin": 0.05611222982406616,
            "token": "\\n",
            "token_class": "newline",
            "token_total_benefit": 7.582209587097168
          },
          {
            "assigned_benefit": 0.31577354669570923,
            "delta_norm": 8.395349502563477,
            "family": "json_schema",
            "route_margin": 0.1991105079650879,
            "token": "\\n",
            "token_class": "newline",
            "token_total_benefit": 7.5785651206970215
          },
          {
            "assigned_benefit": 0.2941783269246419,
            "delta_norm": 7.421395778656006,
            "family": "code_heavy",
            "route_margin": 0.23676979541778564,
            "token": "\\",
            "token_class": "string_literal",
            "token_total_benefit": 7.060279846191406
          },
          {
            "assigned_benefit": 0.2659972508748372,
            "delta_norm": 8.452654838562012,
            "family": "code_heavy",
            "route_margin": 0.5330383777618408,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 6.383934020996094
          },
          {
            "assigned_benefit": 0.2554399371147156,
            "delta_norm": 7.8932695388793945,
            "family": "json_schema",
            "route_margin": 0.18097758293151855,
            "token": "\\n",
            "token_class": "newline",
            "token_total_benefit": 6.130558490753174
          },
          {
            "assigned_benefit": 0.24512036641438803,
            "delta_norm": 8.400272369384766,
            "family": "code_heavy",
            "route_margin": 0.07076802849769592,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 5.8828887939453125
          },
          {
            "assigned_benefit": 0.2002115249633789,
            "delta_norm": 7.900450706481934,
            "family": "code_heavy",
            "route_margin": 0.0298386812210083,
            "token": ")",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 4.805076599121094
          }
        ],
        "total_assigned_benefit": 5.846928723156451
      },
      "layer_6_expert_7": {
        "activation_count": 274,
        "mean_assigned_benefit": 0.06261863040407444,
        "mean_delta_norm": 8.548061252510461,
        "mean_harm": -0.033957917608338196,
        "mean_positive_benefit": 0.09639663488132227,
        "mean_route_margin": 0.19574017336007452,
        "positive_benefit_rate": 0.7408759124087592,
        "prose_benefit": 2.3926280080478,
        "structured_benefit": 13.9153923833259,
        "structured_prose_benefit_ratio": 5.8159447839448255,
        "token_class_benefit": {
          "brace_bracket_paren": 0.9888442357381185,
          "comma_colon_semicolon": 0.4927428166071574,
          "function_signature": 0.3093259930610657,
          "identifier": 3.952018841480216,
          "indentation": -0.45120119303464895,
          "json_key": 0.9320128858089445,
          "json_value": 0.5672259777784348,
          "newline": 0.9860422064997845,
          "number": 0.2707478602727254,
          "other": 1.3624237875143688,
          "prose_word": 2.9869944221961005,
          "quote": 5.278998692830403,
          "space": -0.6561046692853172,
          "string_literal": 0.13743287324905396
        },
        "token_class_counts": {
          "brace_bracket_paren": 7,
          "comma_colon_semicolon": 6,
          "function_signature": 7,
          "identifier": 63,
          "indentation": 18,
          "json_key": 10,
          "json_value": 5,
          "newline": 6,
          "number": 2,
          "other": 7,
          "prose_word": 79,
          "quote": 17,
          "space": 42,
          "string_literal": 5
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.14381763339042664,
            "delta_norm": 9.298227310180664,
            "family": "broad_lm",
            "route_margin": 0.1530340313911438,
            "token": "c",
            "token_class": "prose_word",
            "token_total_benefit": -3.4516232013702393
          },
          {
            "assigned_benefit": -0.10809943079948425,
            "delta_norm": 8.423624038696289,
            "family": "json_schema",
            "route_margin": 0.13755613565444946,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.594386339187622
          },
          {
            "assigned_benefit": -0.09847732384999593,
            "delta_norm": 8.521519660949707,
            "family": "broad_lm",
            "route_margin": 0.11692476272583008,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -2.3634557723999023
          },
          {
            "assigned_benefit": -0.09698358178138733,
            "delta_norm": 8.676441192626953,
            "family": "broad_lm",
            "route_margin": 0.013932943344116211,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -2.327605962753296
          },
          {
            "assigned_benefit": -0.08489630619684856,
            "delta_norm": 9.409568786621094,
            "family": "code_heavy",
            "route_margin": 0.10361337661743164,
            "token": "w",
            "token_class": "identifier",
            "token_total_benefit": -2.0375113487243652
          },
          {
            "assigned_benefit": -0.08353991309801738,
            "delta_norm": 7.983991622924805,
            "family": "json_schema",
            "route_margin": 0.4643712043762207,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -2.004957914352417
          },
          {
            "assigned_benefit": -0.08353975415229797,
            "delta_norm": 7.9839911460876465,
            "family": "json_schema",
            "route_margin": 0.4643709659576416,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -2.0049540996551514
          },
          {
            "assigned_benefit": -0.0676362117131551,
            "delta_norm": 9.321044921875,
            "family": "broad_lm",
            "route_margin": 0.16924446821212769,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -1.6232690811157227
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.33628082275390625,
            "delta_norm": 7.81779146194458,
            "family": "json_schema",
            "route_margin": 0.41930902004241943,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 8.07073974609375
          },
          {
            "assigned_benefit": 0.33243274688720703,
            "delta_norm": 7.972072124481201,
            "family": "code_heavy",
            "route_margin": 0.5332698822021484,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 7.978385925292969
          },
          {
            "assigned_benefit": 0.3278465270996094,
            "delta_norm": 8.40522289276123,
            "family": "code_heavy",
            "route_margin": 0.41379523277282715,
            "token": "'",
            "token_class": "quote",
            "token_total_benefit": 7.868316650390625
          },
          {
            "assigned_benefit": 0.3272164662679036,
            "delta_norm": 8.637068748474121,
            "family": "code_heavy",
            "route_margin": 0.10997211933135986,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 7.8531951904296875
          },
          {
            "assigned_benefit": 0.32633060216903687,
            "delta_norm": 9.316276550292969,
            "family": "json_schema",
            "route_margin": 0.08258192986249924,
            "token": "\\n",
            "token_class": "newline",
            "token_total_benefit": 7.831934452056885
          },
          {
            "assigned_benefit": 0.3237965901692708,
            "delta_norm": 7.525115013122559,
            "family": "code_heavy",
            "route_margin": 0.3718416392803192,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 7.7711181640625
          },
          {
            "assigned_benefit": 0.3214457829793294,
            "delta_norm": 7.579422950744629,
            "family": "code_heavy",
            "route_margin": 0.22685277462005615,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 7.714698791503906
          },
          {
            "assigned_benefit": 0.3151508967081706,
            "delta_norm": 9.100988388061523,
            "family": "code_heavy",
            "route_margin": 0.15109646320343018,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 7.563621520996094
          }
        ],
        "total_assigned_benefit": 17.157504730716397
      },
      "layer_7_expert_0": {
        "activation_count": 182,
        "mean_assigned_benefit": 0.05653845100414569,
        "mean_delta_norm": 9.492912470639407,
        "mean_harm": -0.0326122522280462,
        "mean_positive_benefit": 0.09930179645698566,
        "mean_route_margin": 0.20347760912481244,
        "positive_benefit_rate": 0.6758241758241759,
        "prose_benefit": 2.231904291547836,
        "structured_benefit": 7.152413601676624,
        "structured_prose_benefit_ratio": 3.2046237953673145,
        "token_class_benefit": {
          "brace_bracket_paren": 0.3254578510920207,
          "comma_colon_semicolon": 0.72263037165006,
          "function_signature": 0.21184985339641574,
          "identifier": 1.0609903037548065,
          "indentation": -0.2580371949200828,
          "json_key": 0.07818804184595744,
          "json_value": 0.1874856253465017,
          "newline": 0.03630606333414713,
          "number": 0.8043245077133179,
          "operator": 0.5479291081428528,
          "other": 1.3715790808200838,
          "prose_word": 2.9651816884676623,
          "quote": 1.2507166862487793,
          "space": -0.9411390932897725,
          "string_literal": 1.9265351891517637
        },
        "token_class_counts": {
          "brace_bracket_paren": 3,
          "comma_colon_semicolon": 8,
          "function_signature": 4,
          "identifier": 23,
          "indentation": 15,
          "json_key": 1,
          "json_value": 3,
          "newline": 1,
          "number": 6,
          "operator": 6,
          "other": 6,
          "prose_word": 51,
          "quote": 4,
          "space": 37,
          "string_literal": 14
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.109354833761851,
            "delta_norm": 10.086499214172363,
            "family": "code_heavy",
            "route_margin": 0.16335642337799072,
            "token": "-",
            "token_class": "operator",
            "token_total_benefit": -2.624516010284424
          },
          {
            "assigned_benefit": -0.08776763081550598,
            "delta_norm": 8.549734115600586,
            "family": "broad_lm",
            "route_margin": 0.10307729244232178,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -2.1064231395721436
          },
          {
            "assigned_benefit": -0.07807752986749013,
            "delta_norm": 8.283062934875488,
            "family": "code_heavy",
            "route_margin": 0.10679018497467041,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.8738607168197632
          },
          {
            "assigned_benefit": -0.07618690530459087,
            "delta_norm": 8.61596965789795,
            "family": "broad_lm",
            "route_margin": 0.02356410026550293,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -1.8284857273101807
          },
          {
            "assigned_benefit": -0.07568599780400594,
            "delta_norm": 10.272224426269531,
            "family": "json_schema",
            "route_margin": 0.7141194343566895,
            "token": "a",
            "token_class": "json_value",
            "token_total_benefit": -1.8164639472961426
          },
          {
            "assigned_benefit": -0.06990201274553935,
            "delta_norm": 10.534475326538086,
            "family": "json_schema",
            "route_margin": 0.39023900032043457,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.6776483058929443
          },
          {
            "assigned_benefit": -0.06965599457422893,
            "delta_norm": 8.683030128479004,
            "family": "broad_lm",
            "route_margin": 0.3627204895019531,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -1.6717438697814941
          },
          {
            "assigned_benefit": -0.06830919782320659,
            "delta_norm": 8.626891136169434,
            "family": "json_schema",
            "route_margin": 0.02271968126296997,
            "token": " ",
            "token_class": "indentation",
            "token_total_benefit": -1.639420747756958
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.3551967938741048,
            "delta_norm": 8.703503608703613,
            "family": "code_heavy",
            "route_margin": 0.005333125591278076,
            "token": "'",
            "token_class": "quote",
            "token_total_benefit": 8.524723052978516
          },
          {
            "assigned_benefit": 0.32963212331136066,
            "delta_norm": 9.471391677856445,
            "family": "code_heavy",
            "route_margin": 0.0027971267700195312,
            "token": "\\",
            "token_class": "string_literal",
            "token_total_benefit": 7.911170959472656
          },
          {
            "assigned_benefit": 0.31663767496744794,
            "delta_norm": 10.248433113098145,
            "family": "code_heavy",
            "route_margin": 0.08014100790023804,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 7.59930419921875
          },
          {
            "assigned_benefit": 0.3159599304199219,
            "delta_norm": 9.962112426757812,
            "family": "code_heavy",
            "route_margin": 0.07699716091156006,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 7.583038330078125
          },
          {
            "assigned_benefit": 0.3010571797688802,
            "delta_norm": 10.010425567626953,
            "family": "code_heavy",
            "route_margin": 0.5240833759307861,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 7.225372314453125
          },
          {
            "assigned_benefit": 0.2956549326578776,
            "delta_norm": 10.370880126953125,
            "family": "code_heavy",
            "route_margin": 0.12216627597808838,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 7.0957183837890625
          },
          {
            "assigned_benefit": 0.28188133239746094,
            "delta_norm": 8.974268913269043,
            "family": "code_heavy",
            "route_margin": 0.24387580156326294,
            "token": "\\",
            "token_class": "string_literal",
            "token_total_benefit": 6.7651519775390625
          },
          {
            "assigned_benefit": 0.2808081309000651,
            "delta_norm": 10.2288179397583,
            "family": "code_heavy",
            "route_margin": 0.0236968994140625,
            "token": "\\",
            "token_class": "string_literal",
            "token_total_benefit": 6.7393951416015625
          }
        ],
        "total_assigned_benefit": 10.289998082754515
      },
      "layer_7_expert_1": {
        "activation_count": 9,
        "mean_assigned_benefit": 0.05722594702685321,
        "mean_delta_norm": 7.536191357506646,
        "mean_harm": -0.014785890777905781,
        "mean_positive_benefit": 0.07780075782821293,
        "mean_route_margin": 0.05171963903639051,
        "positive_benefit_rate": 0.7777777777777778,
        "prose_benefit": 0.2258078455924988,
        "structured_benefit": 0.2892256776491801,
        "structured_prose_benefit_ratio": 1.2808486653343634,
        "token_class_benefit": {
          "comma_colon_semicolon": 0.3137408494949341,
          "identifier": -0.024515171845753986,
          "prose_word": 0.2258078455924988
        },
        "token_class_counts": {
          "comma_colon_semicolon": 3,
          "identifier": 1,
          "prose_word": 5
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.024515171845753986,
            "delta_norm": 7.8629302978515625,
            "family": "code_heavy",
            "route_margin": 0.02110755443572998,
            "token": "e",
            "token_class": "identifier",
            "token_total_benefit": -0.5883641242980957
          },
          {
            "assigned_benefit": -0.005056609710057576,
            "delta_norm": 7.693392753601074,
            "family": "broad_lm",
            "route_margin": 0.0240212082862854,
            "token": "o",
            "token_class": "prose_word",
            "token_total_benefit": -0.12135863304138184
          },
          {
            "assigned_benefit": 0.012245357036590576,
            "delta_norm": 7.569165229797363,
            "family": "broad_lm",
            "route_margin": 0.004209160804748535,
            "token": "h",
            "token_class": "prose_word",
            "token_total_benefit": 0.29388856887817383
          },
          {
            "assigned_benefit": 0.025523602962493896,
            "delta_norm": 7.45229959487915,
            "family": "broad_lm",
            "route_margin": 0.01560211181640625,
            "token": "o",
            "token_class": "prose_word",
            "token_total_benefit": 0.6125664710998535
          },
          {
            "assigned_benefit": 0.07115320364634196,
            "delta_norm": 7.283779621124268,
            "family": "broad_lm",
            "route_margin": 0.031180262565612793,
            "token": "s",
            "token_class": "prose_word",
            "token_total_benefit": 1.707676887512207
          },
          {
            "assigned_benefit": 0.09751443068186443,
            "delta_norm": 7.541776180267334,
            "family": "json_schema",
            "route_margin": 0.07884043455123901,
            "token": ":",
            "token_class": "comma_colon_semicolon",
            "token_total_benefit": 2.340346336364746
          },
          {
            "assigned_benefit": 0.0995492935180664,
            "delta_norm": 7.801633834838867,
            "family": "code_heavy",
            "route_margin": 0.2141503095626831,
            "token": ":",
            "token_class": "comma_colon_semicolon",
            "token_total_benefit": 2.3891830444335938
          },
          {
            "assigned_benefit": 0.11667712529500325,
            "delta_norm": 7.552852630615234,
            "family": "json_schema",
            "route_margin": 0.051489055156707764,
            "token": ":",
            "token_class": "comma_colon_semicolon",
            "token_total_benefit": 2.800251007080078
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.12194229165712993,
            "delta_norm": 7.067892074584961,
            "family": "broad_lm",
            "route_margin": 0.024876654148101807,
            "token": "i",
            "token_class": "prose_word",
            "token_total_benefit": 2.926614999771118
          },
          {
            "assigned_benefit": 0.11667712529500325,
            "delta_norm": 7.552852630615234,
            "family": "json_schema",
            "route_margin": 0.051489055156707764,
            "token": ":",
            "token_class": "comma_colon_semicolon",
            "token_total_benefit": 2.800251007080078
          },
          {
            "assigned_benefit": 0.0995492935180664,
            "delta_norm": 7.801633834838867,
            "family": "code_heavy",
            "route_margin": 0.2141503095626831,
            "token": ":",
            "token_class": "comma_colon_semicolon",
            "token_total_benefit": 2.3891830444335938
          },
          {
            "assigned_benefit": 0.09751443068186443,
            "delta_norm": 7.541776180267334,
            "family": "json_schema",
            "route_margin": 0.07884043455123901,
            "token": ":",
            "token_class": "comma_colon_semicolon",
            "token_total_benefit": 2.340346336364746
          },
          {
            "assigned_benefit": 0.07115320364634196,
            "delta_norm": 7.283779621124268,
            "family": "broad_lm",
            "route_margin": 0.031180262565612793,
            "token": "s",
            "token_class": "prose_word",
            "token_total_benefit": 1.707676887512207
          },
          {
            "assigned_benefit": 0.025523602962493896,
            "delta_norm": 7.45229959487915,
            "family": "broad_lm",
            "route_margin": 0.01560211181640625,
            "token": "o",
            "token_class": "prose_word",
            "token_total_benefit": 0.6125664710998535
          },
          {
            "assigned_benefit": 0.012245357036590576,
            "delta_norm": 7.569165229797363,
            "family": "broad_lm",
            "route_margin": 0.004209160804748535,
            "token": "h",
            "token_class": "prose_word",
            "token_total_benefit": 0.29388856887817383
          },
          {
            "assigned_benefit": -0.005056609710057576,
            "delta_norm": 7.693392753601074,
            "family": "broad_lm",
            "route_margin": 0.0240212082862854,
            "token": "o",
            "token_class": "prose_word",
            "token_total_benefit": -0.12135863304138184
          }
        ],
        "total_assigned_benefit": 0.515033523241679
      },
      "layer_7_expert_2": {
        "activation_count": 3471,
        "mean_assigned_benefit": 0.05811115770960477,
        "mean_delta_norm": 10.489070012706119,
        "mean_harm": -0.0303416579095528,
        "mean_positive_benefit": 0.09758322667965376,
        "mean_route_margin": 0.4936086331791714,
        "positive_benefit_rate": 0.6914433880726015,
        "prose_benefit": 36.69623425256167,
        "structured_benefit": 153.56642081795675,
        "structured_prose_benefit_ratio": 4.184800537325888,
        "token_class_benefit": {
          "brace_bracket_paren": 12.56824224224935,
          "comma_colon_semicolon": 13.34414864083131,
          "function_signature": 9.796571999788283,
          "identifier": 35.22087849055731,
          "indentation": -4.224537385006746,
          "json_key": 10.085067518055443,
          "json_value": 6.609750747835881,
          "newline": 19.853288064764286,
          "number": 5.791906535625458,
          "operator": 4.060567418734232,
          "other": 20.719503161624136,
          "prose_word": 44.92329759305961,
          "quote": 26.86227289835611,
          "space": -13.280855777595805,
          "string_literal": 9.373726261158785
        },
        "token_class_counts": {
          "brace_bracket_paren": 67,
          "comma_colon_semicolon": 135,
          "function_signature": 74,
          "identifier": 699,
          "indentation": 179,
          "json_key": 111,
          "json_value": 118,
          "newline": 105,
          "number": 48,
          "operator": 22,
          "other": 92,
          "prose_word": 988,
          "quote": 84,
          "space": 635,
          "string_literal": 114
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.17974231019616127,
            "delta_norm": 11.604266166687012,
            "family": "broad_lm",
            "route_margin": 0.3444712162017822,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -4.3138154447078705
          },
          {
            "assigned_benefit": -0.14381763339042664,
            "delta_norm": 11.527758598327637,
            "family": "broad_lm",
            "route_margin": 0.3818182945251465,
            "token": "c",
            "token_class": "prose_word",
            "token_total_benefit": -3.4516232013702393
          },
          {
            "assigned_benefit": -0.12831215063730875,
            "delta_norm": 10.038162231445312,
            "family": "json_schema",
            "route_margin": 0.6845676302909851,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -3.07949161529541
          },
          {
            "assigned_benefit": -0.1258842075864474,
            "delta_norm": 11.557771682739258,
            "family": "broad_lm",
            "route_margin": 1.031848669052124,
            "token": "m",
            "token_class": "prose_word",
            "token_total_benefit": -3.0212209820747375
          },
          {
            "assigned_benefit": -0.12130660812060039,
            "delta_norm": 9.820180892944336,
            "family": "json_schema",
            "route_margin": 0.7133538126945496,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.911358594894409
          },
          {
            "assigned_benefit": -0.11974493662516277,
            "delta_norm": 10.436383247375488,
            "family": "code_heavy",
            "route_margin": 0.5848171710968018,
            "token": "5",
            "token_class": "number",
            "token_total_benefit": -2.8738784790039062
          },
          {
            "assigned_benefit": -0.11696084340413411,
            "delta_norm": 10.682389259338379,
            "family": "json_schema",
            "route_margin": 0.3894997835159302,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.8070602416992188
          },
          {
            "assigned_benefit": -0.11193382243315379,
            "delta_norm": 10.318203926086426,
            "family": "broad_lm",
            "route_margin": 0.2001359462738037,
            "token": "e",
            "token_class": "prose_word",
            "token_total_benefit": -2.686411738395691
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.4434954325358073,
            "delta_norm": 10.230634689331055,
            "family": "json_schema",
            "route_margin": 0.6278300285339355,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.643890380859375
          },
          {
            "assigned_benefit": 0.4348748524983724,
            "delta_norm": 9.999593734741211,
            "family": "json_schema",
            "route_margin": 0.007012426853179932,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.436996459960938
          },
          {
            "assigned_benefit": 0.4194428126017253,
            "delta_norm": 11.373065948486328,
            "family": "json_schema",
            "route_margin": 0.293265163898468,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.066627502441406
          },
          {
            "assigned_benefit": 0.4192720651626587,
            "delta_norm": 12.660926818847656,
            "family": "code_heavy",
            "route_margin": 0.48953527212142944,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 10.062529563903809
          },
          {
            "assigned_benefit": 0.40491771697998047,
            "delta_norm": 10.123507499694824,
            "family": "json_schema",
            "route_margin": 0.16513794660568237,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.718025207519531
          },
          {
            "assigned_benefit": 0.40347035725911456,
            "delta_norm": 9.916581153869629,
            "family": "json_schema",
            "route_margin": 0.5222394466400146,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.68328857421875
          },
          {
            "assigned_benefit": 0.40207378069559735,
            "delta_norm": 9.030159950256348,
            "family": "code_heavy",
            "route_margin": 0.0658423900604248,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.649770736694336
          },
          {
            "assigned_benefit": 0.3999309539794922,
            "delta_norm": 9.622645378112793,
            "family": "json_schema",
            "route_margin": 0.44824445247650146,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.598342895507812
          }
        ],
        "total_assigned_benefit": 201.70382841003814
      },
      "layer_7_expert_3": {
        "activation_count": 276,
        "mean_assigned_benefit": 0.07672660971388831,
        "mean_delta_norm": 7.790459625962852,
        "mean_harm": -0.03567841460604763,
        "mean_positive_benefit": 0.11565713033201244,
        "mean_route_margin": 0.2598122522450875,
        "positive_benefit_rate": 0.7427536231884058,
        "prose_benefit": 7.047040628579752,
        "structured_benefit": 14.711670860648152,
        "structured_prose_benefit_ratio": 2.0876381499751786,
        "token_class_benefit": {
          "brace_bracket_paren": 1.9067864815394084,
          "comma_colon_semicolon": 1.1259166995684304,
          "function_signature": 0.5937398076057434,
          "identifier": 4.959028239051501,
          "indentation": -0.1286788173019886,
          "json_key": 0.8019266327222189,
          "json_value": 0.9834172526995341,
          "newline": 2.2952074805895486,
          "operator": 0.4745760957400004,
          "other": 0.3781778613726298,
          "prose_word": 7.749552726745604,
          "quote": 0.9121971130371094,
          "space": -1.5341783504312234,
          "string_literal": 0.6588750580946604
        },
        "token_class_counts": {
          "brace_bracket_paren": 6,
          "comma_colon_semicolon": 10,
          "function_signature": 5,
          "identifier": 56,
          "indentation": 4,
          "json_key": 7,
          "json_value": 9,
          "newline": 11,
          "operator": 2,
          "other": 4,
          "prose_word": 102,
          "quote": 3,
          "space": 51,
          "string_literal": 6
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.13103054463863373,
            "delta_norm": 7.5452561378479,
            "family": "code_heavy",
            "route_margin": 0.06891751289367676,
            "token": "g",
            "token_class": "identifier",
            "token_total_benefit": -3.1447330713272095
          },
          {
            "assigned_benefit": -0.11105093856652577,
            "delta_norm": 7.752397537231445,
            "family": "broad_lm",
            "route_margin": 0.4747266173362732,
            "token": "o",
            "token_class": "prose_word",
            "token_total_benefit": -2.6652225255966187
          },
          {
            "assigned_benefit": -0.09049346546332042,
            "delta_norm": 7.493154048919678,
            "family": "code_heavy",
            "route_margin": 0.023054659366607666,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -2.17184317111969
          },
          {
            "assigned_benefit": -0.0898671845595042,
            "delta_norm": 8.296611785888672,
            "family": "broad_lm",
            "route_margin": 0.37361764907836914,
            "token": "e",
            "token_class": "prose_word",
            "token_total_benefit": -2.1568124294281006
          },
          {
            "assigned_benefit": -0.0805702159802119,
            "delta_norm": 7.44912576675415,
            "family": "code_heavy",
            "route_margin": 0.28509414196014404,
            "token": "t",
            "token_class": "identifier",
            "token_total_benefit": -1.9336851835250854
          },
          {
            "assigned_benefit": -0.07165794571240743,
            "delta_norm": 7.470027446746826,
            "family": "broad_lm",
            "route_margin": 0.2834492325782776,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -1.7197906970977783
          },
          {
            "assigned_benefit": -0.05738865832487742,
            "delta_norm": 8.117703437805176,
            "family": "broad_lm",
            "route_margin": 0.11295360326766968,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.377327799797058
          },
          {
            "assigned_benefit": -0.05644424011309942,
            "delta_norm": 7.754026412963867,
            "family": "code_heavy",
            "route_margin": 0.25701582431793213,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.354661762714386
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.41413907210032147,
            "delta_norm": 8.194645881652832,
            "family": "code_heavy",
            "route_margin": 0.5505274534225464,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.939337730407715
          },
          {
            "assigned_benefit": 0.38037506739298504,
            "delta_norm": 6.843005657196045,
            "family": "code_heavy",
            "route_margin": 0.08447158336639404,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.12900161743164
          },
          {
            "assigned_benefit": 0.36609824498494464,
            "delta_norm": 8.307698249816895,
            "family": "code_heavy",
            "route_margin": 0.00396120548248291,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.786357879638672
          },
          {
            "assigned_benefit": 0.3641868432362874,
            "delta_norm": 7.839848041534424,
            "family": "code_heavy",
            "route_margin": 0.35379648208618164,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.740484237670898
          },
          {
            "assigned_benefit": 0.32917070388793945,
            "delta_norm": 7.707570552825928,
            "family": "code_heavy",
            "route_margin": 0.1672688126564026,
            "token": "_",
            "token_class": "identifier",
            "token_total_benefit": 7.900096893310547
          },
          {
            "assigned_benefit": 0.32812609275182086,
            "delta_norm": 7.819571495056152,
            "family": "json_schema",
            "route_margin": 0.022191941738128662,
            "token": "\\n",
            "token_class": "newline",
            "token_total_benefit": 7.875026226043701
          },
          {
            "assigned_benefit": 0.3278465270996094,
            "delta_norm": 7.575399398803711,
            "family": "code_heavy",
            "route_margin": 0.26927709579467773,
            "token": "'",
            "token_class": "quote",
            "token_total_benefit": 7.868316650390625
          },
          {
            "assigned_benefit": 0.31175031264623004,
            "delta_norm": 7.835484981536865,
            "family": "json_schema",
            "route_margin": 0.014330625534057617,
            "token": "\\n",
            "token_class": "newline",
            "token_total_benefit": 7.4820075035095215
          }
        ],
        "total_assigned_benefit": 21.176544281033173
      },
      "layer_7_expert_4": {
        "activation_count": 2,
        "mean_assigned_benefit": 0.03937641282876332,
        "mean_delta_norm": 6.683046102523804,
        "mean_harm": -0.007212142149607341,
        "mean_positive_benefit": 0.08596496780713399,
        "mean_route_margin": 0.09967494010925293,
        "positive_benefit_rate": 0.5,
        "prose_benefit": 0.07875282565752664,
        "structured_benefit": 0,
        "structured_prose_benefit_ratio": 0.0,
        "token_class_benefit": {
          "prose_word": 0.07875282565752664
        },
        "token_class_counts": {
          "prose_word": 2
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.007212142149607341,
            "delta_norm": 6.748727321624756,
            "family": "broad_lm",
            "route_margin": 0.08132225275039673,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -0.17309141159057617
          },
          {
            "assigned_benefit": 0.08596496780713399,
            "delta_norm": 6.617364883422852,
            "family": "broad_lm",
            "route_margin": 0.11802762746810913,
            "token": "s",
            "token_class": "prose_word",
            "token_total_benefit": 2.063159227371216
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.08596496780713399,
            "delta_norm": 6.617364883422852,
            "family": "broad_lm",
            "route_margin": 0.11802762746810913,
            "token": "s",
            "token_class": "prose_word",
            "token_total_benefit": 2.063159227371216
          },
          {
            "assigned_benefit": -0.007212142149607341,
            "delta_norm": 6.748727321624756,
            "family": "broad_lm",
            "route_margin": 0.08132225275039673,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -0.17309141159057617
          }
        ],
        "total_assigned_benefit": 0.07875282565752664
      },
      "layer_7_expert_5": {
        "activation_count": 2011,
        "mean_assigned_benefit": 0.04190555238801921,
        "mean_delta_norm": 8.657007839121313,
        "mean_harm": -0.017087073658927122,
        "mean_positive_benefit": 0.0940977163883165,
        "mean_route_margin": 0.339642520503047,
        "positive_benefit_rate": 0.530581800099453,
        "prose_benefit": 8.968102134301896,
        "structured_benefit": 73.0204056523153,
        "structured_prose_benefit_ratio": 8.142236178714018,
        "token_class_benefit": {
          "brace_bracket_paren": 7.644097626209257,
          "comma_colon_semicolon": 0.7855471471945445,
          "function_signature": 2.4040420055389404,
          "identifier": 11.881602490941681,
          "indentation": -6.413223897572605,
          "json_key": 5.0324131945768995,
          "json_value": 3.2483665815865006,
          "newline": 2.5774122128917725,
          "number": 2.980309863885243,
          "operator": 1.9898324410120647,
          "other": 2.9672447713091974,
          "prose_word": 18.292248797913405,
          "quote": 30.88248538970947,
          "space": -3.5946094716588655,
          "string_literal": 3.594296698768932
        },
        "token_class_counts": {
          "brace_bracket_paren": 46,
          "comma_colon_semicolon": 15,
          "function_signature": 29,
          "identifier": 279,
          "indentation": 708,
          "json_key": 87,
          "json_value": 74,
          "newline": 16,
          "number": 17,
          "operator": 10,
          "other": 15,
          "prose_word": 395,
          "quote": 102,
          "space": 162,
          "string_literal": 56
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.14390301704406738,
            "delta_norm": 9.063444137573242,
            "family": "json_schema",
            "route_margin": 0.07825720310211182,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -3.453672409057617
          },
          {
            "assigned_benefit": -0.1176329255104065,
            "delta_norm": 9.49392032623291,
            "family": "broad_lm",
            "route_margin": 0.7717688083648682,
            "token": "o",
            "token_class": "prose_word",
            "token_total_benefit": -2.823190212249756
          },
          {
            "assigned_benefit": -0.11034655446807544,
            "delta_norm": 9.507099151611328,
            "family": "code_heavy",
            "route_margin": 0.6743570566177368,
            "token": "o",
            "token_class": "identifier",
            "token_total_benefit": -2.6483173072338104
          },
          {
            "assigned_benefit": -0.10964437325795491,
            "delta_norm": 8.74879264831543,
            "family": "code_heavy",
            "route_margin": 0.09765052795410156,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -2.631464958190918
          },
          {
            "assigned_benefit": -0.10949698835611343,
            "delta_norm": 9.596410751342773,
            "family": "broad_lm",
            "route_margin": 0.7461711764335632,
            "token": "o",
            "token_class": "prose_word",
            "token_total_benefit": -2.6279277205467224
          },
          {
            "assigned_benefit": -0.10870074232419331,
            "delta_norm": 9.885072708129883,
            "family": "broad_lm",
            "route_margin": 0.573518693447113,
            "token": "o",
            "token_class": "prose_word",
            "token_total_benefit": -2.6088178157806396
          },
          {
            "assigned_benefit": -0.1018477330605189,
            "delta_norm": 8.255505561828613,
            "family": "broad_lm",
            "route_margin": 0.4152907729148865,
            "token": " ",
            "token_class": "indentation",
            "token_total_benefit": -2.4443455934524536
          },
          {
            "assigned_benefit": -0.10159913450479507,
            "delta_norm": 10.406402587890625,
            "family": "broad_lm",
            "route_margin": 0.5889453887939453,
            "token": "p",
            "token_class": "prose_word",
            "token_total_benefit": -2.438379228115082
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.42559146881103516,
            "delta_norm": 9.128092765808105,
            "family": "json_schema",
            "route_margin": 0.10569411516189575,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.214195251464844
          },
          {
            "assigned_benefit": 0.3995812733968099,
            "delta_norm": 9.317132949829102,
            "family": "json_schema",
            "route_margin": 0.31120848655700684,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.589950561523438
          },
          {
            "assigned_benefit": 0.3894158601760864,
            "delta_norm": 9.265015602111816,
            "family": "code_heavy",
            "route_margin": 0.1820206642150879,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.345980644226074
          },
          {
            "assigned_benefit": 0.3847957452138265,
            "delta_norm": 9.220890045166016,
            "family": "code_heavy",
            "route_margin": 0.00911414623260498,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.235097885131836
          },
          {
            "assigned_benefit": 0.38011709849039715,
            "delta_norm": 9.283378601074219,
            "family": "json_schema",
            "route_margin": 0.14380478858947754,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.122810363769531
          },
          {
            "assigned_benefit": 0.3795582453409831,
            "delta_norm": 9.424397468566895,
            "family": "json_schema",
            "route_margin": 0.3890010118484497,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.109397888183594
          },
          {
            "assigned_benefit": 0.3718280792236328,
            "delta_norm": 9.465102195739746,
            "family": "json_schema",
            "route_margin": 0.37116867303848267,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 8.923873901367188
          },
          {
            "assigned_benefit": 0.3590370814005534,
            "delta_norm": 9.961577415466309,
            "family": "code_heavy",
            "route_margin": 0.02641606330871582,
            "token": "'",
            "token_class": "quote",
            "token_total_benefit": 8.616889953613281
          }
        ],
        "total_assigned_benefit": 84.27206585230664
      },
      "layer_7_expert_7": {
        "activation_count": 193,
        "mean_assigned_benefit": 0.06289121669609365,
        "mean_delta_norm": 7.633337376648898,
        "mean_harm": -0.028231866489790494,
        "mean_positive_benefit": 0.10500112635017647,
        "mean_route_margin": 0.21787767258950466,
        "positive_benefit_rate": 0.6839378238341969,
        "prose_benefit": 1.4567330780749514,
        "structured_benefit": 9.690185708304243,
        "structured_prose_benefit_ratio": 6.651998127968414,
        "token_class_benefit": {
          "comma_colon_semicolon": 0.12403727571169534,
          "function_signature": 0.16055710117022198,
          "identifier": 2.4400648549199104,
          "indentation": -0.01719256521513065,
          "json_key": 0.9523382286230725,
          "json_value": 0.1560187935829163,
          "newline": 0.9604085286458334,
          "operator": 1.0043950080871582,
          "other": 1.1803818146387737,
          "prose_word": 2.1179399962226557,
          "quote": 3.5795370737711587,
          "space": -0.8333101316044728,
          "string_literal": 0.3128288437922796
        },
        "token_class_counts": {
          "comma_colon_semicolon": 2,
          "function_signature": 3,
          "identifier": 37,
          "indentation": 3,
          "json_key": 11,
          "json_value": 10,
          "newline": 4,
          "operator": 5,
          "other": 5,
          "prose_word": 53,
          "quote": 11,
          "space": 43,
          "string_literal": 6
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.08985122044881184,
            "delta_norm": 7.6892595291137695,
            "family": "broad_lm",
            "route_margin": 0.18961608409881592,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -2.1564292907714844
          },
          {
            "assigned_benefit": -0.08112131555875142,
            "delta_norm": 8.397960662841797,
            "family": "json_schema",
            "route_margin": 0.3395804166793823,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.9469115734100342
          },
          {
            "assigned_benefit": -0.06400749087333679,
            "delta_norm": 6.847965717315674,
            "family": "code_heavy",
            "route_margin": 0.03289914131164551,
            "token": "s",
            "token_class": "string_literal",
            "token_total_benefit": -1.536179780960083
          },
          {
            "assigned_benefit": -0.060935149590174355,
            "delta_norm": 7.607226371765137,
            "family": "broad_lm",
            "route_margin": 0.11906498670578003,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.4624435901641846
          },
          {
            "assigned_benefit": -0.059396132826805115,
            "delta_norm": 8.225654602050781,
            "family": "code_heavy",
            "route_margin": 0.06635147333145142,
            "token": "s",
            "token_class": "identifier",
            "token_total_benefit": -1.4255071878433228
          },
          {
            "assigned_benefit": -0.05253798762957255,
            "delta_norm": 7.624460220336914,
            "family": "code_heavy",
            "route_margin": 0.41453826427459717,
            "token": "r",
            "token_class": "identifier",
            "token_total_benefit": -1.2609117031097412
          },
          {
            "assigned_benefit": -0.051067481438318886,
            "delta_norm": 8.149373054504395,
            "family": "broad_lm",
            "route_margin": 0.8207624554634094,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.2256195545196533
          },
          {
            "assigned_benefit": -0.04966080188751221,
            "delta_norm": 7.588504791259766,
            "family": "code_heavy",
            "route_margin": 0.22126245498657227,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -1.191859245300293
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.3989645640055339,
            "delta_norm": 7.922652721405029,
            "family": "json_schema",
            "route_margin": 0.08713358640670776,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.575149536132812
          },
          {
            "assigned_benefit": 0.38402652740478516,
            "delta_norm": 8.069329261779785,
            "family": "code_heavy",
            "route_margin": 0.2182602882385254,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 9.216636657714844
          },
          {
            "assigned_benefit": 0.3549944559733073,
            "delta_norm": 7.000377178192139,
            "family": "code_heavy",
            "route_margin": 0.43481457233428955,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 8.519866943359375
          },
          {
            "assigned_benefit": 0.35045115152994794,
            "delta_norm": 7.012119770050049,
            "family": "code_heavy",
            "route_margin": 0.03127485513687134,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 8.41082763671875
          },
          {
            "assigned_benefit": 0.33628082275390625,
            "delta_norm": 7.55155611038208,
            "family": "json_schema",
            "route_margin": 0.10403412580490112,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 8.07073974609375
          },
          {
            "assigned_benefit": 0.3361193339029948,
            "delta_norm": 7.207021713256836,
            "family": "json_schema",
            "route_margin": 0.2922346591949463,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 8.066864013671875
          },
          {
            "assigned_benefit": 0.3265867233276367,
            "delta_norm": 7.4972147941589355,
            "family": "json_schema",
            "route_margin": 0.46435296535491943,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 7.838081359863281
          },
          {
            "assigned_benefit": 0.3215319315592448,
            "delta_norm": 7.3540496826171875,
            "family": "code_heavy",
            "route_margin": 0.34498947858810425,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 7.716766357421875
          }
        ],
        "total_assigned_benefit": 12.138004822346074
      },
      "layer_8_expert_0": {
        "activation_count": 2,
        "mean_assigned_benefit": 0.03985199083884557,
        "mean_delta_norm": 7.491489887237549,
        "mean_harm": null,
        "mean_positive_benefit": 0.03985199083884557,
        "mean_route_margin": 0.08589008450508118,
        "positive_benefit_rate": 1.0,
        "prose_benefit": 0,
        "structured_benefit": 0.07970398167769115,
        "structured_prose_benefit_ratio": null,
        "token_class_benefit": {
          "identifier": 0.07970398167769115
        },
        "token_class_counts": {
          "identifier": 2
        },
        "top_negative_examples": [
          {
            "assigned_benefit": 0.023674498001734417,
            "delta_norm": 7.460242748260498,
            "family": "code_heavy",
            "route_margin": 0.10516887903213501,
            "token": "s",
            "token_class": "identifier",
            "token_total_benefit": 0.568187952041626
          },
          {
            "assigned_benefit": 0.056029483675956726,
            "delta_norm": 7.5227370262146,
            "family": "code_heavy",
            "route_margin": 0.06661128997802734,
            "token": "t",
            "token_class": "identifier",
            "token_total_benefit": 1.3447076082229614
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.056029483675956726,
            "delta_norm": 7.5227370262146,
            "family": "code_heavy",
            "route_margin": 0.06661128997802734,
            "token": "t",
            "token_class": "identifier",
            "token_total_benefit": 1.3447076082229614
          },
          {
            "assigned_benefit": 0.023674498001734417,
            "delta_norm": 7.460242748260498,
            "family": "code_heavy",
            "route_margin": 0.10516887903213501,
            "token": "s",
            "token_class": "identifier",
            "token_total_benefit": 0.568187952041626
          }
        ],
        "total_assigned_benefit": 0.07970398167769115
      },
      "layer_8_expert_1": {
        "activation_count": 136,
        "mean_assigned_benefit": 0.019448553956132014,
        "mean_delta_norm": 10.43632813762216,
        "mean_harm": -0.03263866272944261,
        "mean_positive_benefit": 0.04192830010464317,
        "mean_route_margin": 0.27130065025652156,
        "positive_benefit_rate": 0.6985294117647058,
        "prose_benefit": 1.6877616588026285,
        "structured_benefit": 0.9572416792313262,
        "structured_prose_benefit_ratio": 0.5671663852764821,
        "token_class_benefit": {
          "identifier": 1.0676837687691052,
          "json_key": -0.3421135743459066,
          "json_value": -0.11368136356274287,
          "prose_word": 1.8376297156016035,
          "space": -0.1498680567989747,
          "string_literal": 0.34535284837086994
        },
        "token_class_counts": {
          "identifier": 34,
          "json_key": 7,
          "json_value": 13,
          "prose_word": 71,
          "space": 5,
          "string_literal": 6
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.08370453119277954,
            "delta_norm": 10.278992652893066,
            "family": "json_schema",
            "route_margin": 0.18115264177322388,
            "token": "d",
            "token_class": "json_key",
            "token_total_benefit": -2.008908748626709
          },
          {
            "assigned_benefit": -0.08076659838358562,
            "delta_norm": 10.556069374084473,
            "family": "code_heavy",
            "route_margin": 0.16269993782043457,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.9383983612060547
          },
          {
            "assigned_benefit": -0.06701003511746724,
            "delta_norm": 10.779500961303711,
            "family": "broad_lm",
            "route_margin": 0.43184149265289307,
            "token": "l",
            "token_class": "prose_word",
            "token_total_benefit": -1.6082408428192139
          },
          {
            "assigned_benefit": -0.06572231153647105,
            "delta_norm": 10.642827033996582,
            "family": "json_schema",
            "route_margin": 0.15267086029052734,
            "token": "d",
            "token_class": "json_key",
            "token_total_benefit": -1.5773354768753052
          },
          {
            "assigned_benefit": -0.06378033757209778,
            "delta_norm": 10.297065734863281,
            "family": "json_schema",
            "route_margin": 0.03488260507583618,
            "token": "d",
            "token_class": "json_key",
            "token_total_benefit": -1.5307281017303467
          },
          {
            "assigned_benefit": -0.061329285303751625,
            "delta_norm": 10.731355667114258,
            "family": "code_heavy",
            "route_margin": 0.2765146493911743,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -1.471902847290039
          },
          {
            "assigned_benefit": -0.060406903425852455,
            "delta_norm": 10.891539573669434,
            "family": "json_schema",
            "route_margin": 0.1515120267868042,
            "token": "d",
            "token_class": "json_value",
            "token_total_benefit": -1.449765682220459
          },
          {
            "assigned_benefit": -0.06029342611630758,
            "delta_norm": 11.069477081298828,
            "family": "code_heavy",
            "route_margin": 0.21069711446762085,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -1.4470422267913818
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.17948500315348306,
            "delta_norm": 10.43310260772705,
            "family": "code_heavy",
            "route_margin": 0.3656049966812134,
            "token": "\\",
            "token_class": "string_literal",
            "token_total_benefit": 4.307640075683594
          },
          {
            "assigned_benefit": 0.1686234970887502,
            "delta_norm": 10.475135803222656,
            "family": "code_heavy",
            "route_margin": 0.13566172122955322,
            "token": "v",
            "token_class": "identifier",
            "token_total_benefit": 4.046963930130005
          },
          {
            "assigned_benefit": 0.16688183943430582,
            "delta_norm": 9.956160545349121,
            "family": "broad_lm",
            "route_margin": 0.21632736921310425,
            "token": "v",
            "token_class": "prose_word",
            "token_total_benefit": 4.00516414642334
          },
          {
            "assigned_benefit": 0.15848531325658163,
            "delta_norm": 11.01175594329834,
            "family": "code_heavy",
            "route_margin": 0.5077979564666748,
            "token": "v",
            "token_class": "identifier",
            "token_total_benefit": 3.803647518157959
          },
          {
            "assigned_benefit": 0.1494600772857666,
            "delta_norm": 10.41940975189209,
            "family": "code_heavy",
            "route_margin": 0.4336874485015869,
            "token": "v",
            "token_class": "identifier",
            "token_total_benefit": 3.5870418548583984
          },
          {
            "assigned_benefit": 0.14600624640782675,
            "delta_norm": 10.859945297241211,
            "family": "broad_lm",
            "route_margin": 0.6155858039855957,
            "token": "v",
            "token_class": "prose_word",
            "token_total_benefit": 3.504149913787842
          },
          {
            "assigned_benefit": 0.12441627184549968,
            "delta_norm": 11.245241165161133,
            "family": "code_heavy",
            "route_margin": 0.10183870792388916,
            "token": "v",
            "token_class": "identifier",
            "token_total_benefit": 2.985990524291992
          },
          {
            "assigned_benefit": 0.12440139055252075,
            "delta_norm": 10.905896186828613,
            "family": "code_heavy",
            "route_margin": 0.08225345611572266,
            "token": "v",
            "token_class": "identifier",
            "token_total_benefit": 2.985633373260498
          }
        ],
        "total_assigned_benefit": 2.6450033380339537
      },
      "layer_8_expert_5": {
        "activation_count": 5811,
        "mean_assigned_benefit": 0.05418350196360704,
        "mean_delta_norm": 13.397560947098516,
        "mean_harm": -0.02459324768816386,
        "mean_positive_benefit": 0.09949775047568561,
        "mean_route_margin": 0.7981988411724331,
        "positive_benefit_rate": 0.6348304938908966,
        "prose_benefit": 50.73747934450447,
        "structured_benefit": 249.70066390859725,
        "structured_prose_benefit_ratio": 4.9214243027948745,
        "token_class_benefit": {
          "brace_bracket_paren": 21.463932782722015,
          "comma_colon_semicolon": 15.68611722191175,
          "function_signature": 12.520347878336912,
          "identifier": 51.10469191645584,
          "indentation": -11.041669860016562,
          "json_key": 17.23147895683845,
          "json_value": 11.253373061462003,
          "newline": 25.04281397200598,
          "number": 9.57654090722402,
          "operator": 8.016011198361717,
          "other": 25.399751796824294,
          "prose_word": 70.17327025687952,
          "quote": 62.85222816467289,
          "space": -19.37168619176376,
          "string_literal": 14.95312784860531
        },
        "token_class_counts": {
          "brace_bracket_paren": 119,
          "comma_colon_semicolon": 164,
          "function_signature": 112,
          "identifier": 1009,
          "indentation": 909,
          "json_key": 209,
          "json_value": 197,
          "newline": 133,
          "number": 71,
          "operator": 44,
          "other": 117,
          "prose_word": 1453,
          "quote": 202,
          "space": 889,
          "string_literal": 183
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.17974231019616127,
            "delta_norm": 14.634742736816406,
            "family": "broad_lm",
            "route_margin": 0.5854675769805908,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -4.3138154447078705
          },
          {
            "assigned_benefit": -0.14390301704406738,
            "delta_norm": 13.509611129760742,
            "family": "json_schema",
            "route_margin": 0.4197324514389038,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -3.453672409057617
          },
          {
            "assigned_benefit": -0.14381763339042664,
            "delta_norm": 13.65746784210205,
            "family": "broad_lm",
            "route_margin": 1.3253791332244873,
            "token": "c",
            "token_class": "prose_word",
            "token_total_benefit": -3.4516232013702393
          },
          {
            "assigned_benefit": -0.13103054463863373,
            "delta_norm": 14.09956169128418,
            "family": "code_heavy",
            "route_margin": 0.8379199504852295,
            "token": "g",
            "token_class": "identifier",
            "token_total_benefit": -3.1447330713272095
          },
          {
            "assigned_benefit": -0.12831215063730875,
            "delta_norm": 13.327230453491211,
            "family": "json_schema",
            "route_margin": 0.6322788000106812,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -3.07949161529541
          },
          {
            "assigned_benefit": -0.1258842075864474,
            "delta_norm": 15.084177017211914,
            "family": "broad_lm",
            "route_margin": 1.3853830099105835,
            "token": "m",
            "token_class": "prose_word",
            "token_total_benefit": -3.0212209820747375
          },
          {
            "assigned_benefit": -0.12130660812060039,
            "delta_norm": 12.666010856628418,
            "family": "json_schema",
            "route_margin": 1.3272643089294434,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.911358594894409
          },
          {
            "assigned_benefit": -0.11974493662516277,
            "delta_norm": 14.007559776306152,
            "family": "code_heavy",
            "route_margin": 0.9655065536499023,
            "token": "5",
            "token_class": "number",
            "token_total_benefit": -2.8738784790039062
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.4434954325358073,
            "delta_norm": 13.558156967163086,
            "family": "json_schema",
            "route_margin": 1.1355760097503662,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.643890380859375
          },
          {
            "assigned_benefit": 0.4348748524983724,
            "delta_norm": 12.848854064941406,
            "family": "json_schema",
            "route_margin": 0.7649803757667542,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.436996459960938
          },
          {
            "assigned_benefit": 0.42559146881103516,
            "delta_norm": 13.349756240844727,
            "family": "json_schema",
            "route_margin": 0.6049920916557312,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.214195251464844
          },
          {
            "assigned_benefit": 0.4194428126017253,
            "delta_norm": 14.159188270568848,
            "family": "json_schema",
            "route_margin": 0.14749109745025635,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.066627502441406
          },
          {
            "assigned_benefit": 0.4192720651626587,
            "delta_norm": 13.368534088134766,
            "family": "code_heavy",
            "route_margin": 0.6071184277534485,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 10.062529563903809
          },
          {
            "assigned_benefit": 0.41413907210032147,
            "delta_norm": 13.678683280944824,
            "family": "code_heavy",
            "route_margin": 0.3593413829803467,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.939337730407715
          },
          {
            "assigned_benefit": 0.40491771697998047,
            "delta_norm": 13.064817428588867,
            "family": "json_schema",
            "route_margin": 0.8097929954528809,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.718025207519531
          },
          {
            "assigned_benefit": 0.40347035725911456,
            "delta_norm": 13.358765602111816,
            "family": "json_schema",
            "route_margin": 0.734326183795929,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.68328857421875
          }
        ],
        "total_assigned_benefit": 314.86032991052053
      },
      "layer_8_expert_6": {
        "activation_count": 195,
        "mean_assigned_benefit": 0.06455995162638527,
        "mean_delta_norm": 10.277026489453439,
        "mean_harm": -0.02863640189204581,
        "mean_positive_benefit": 0.09333198022939083,
        "mean_route_margin": 0.16887438771052238,
        "positive_benefit_rate": 0.764102564102564,
        "prose_benefit": 4.279334053009127,
        "structured_benefit": 7.692712749044097,
        "structured_prose_benefit_ratio": 1.7976424961810966,
        "token_class_benefit": {
          "brace_bracket_paren": 0.9806514183680217,
          "comma_colon_semicolon": 0.7299037625392278,
          "function_signature": 0.6464128891626993,
          "identifier": 3.2859695404768003,
          "json_key": 0.06056823333104452,
          "json_value": 0.04534730315208434,
          "newline": 0.6798083782196045,
          "operator": 0.06128887335459391,
          "other": 1.2171348929405212,
          "prose_word": 4.341881501177947,
          "quote": 0.6349809964497884,
          "space": -0.6625385760174441,
          "string_literal": 0.5677813539902369
        },
        "token_class_counts": {
          "brace_bracket_paren": 3,
          "comma_colon_semicolon": 9,
          "function_signature": 3,
          "identifier": 50,
          "json_key": 1,
          "json_value": 4,
          "newline": 4,
          "operator": 1,
          "other": 5,
          "prose_word": 72,
          "quote": 2,
          "space": 34,
          "string_literal": 7
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.09154083828131358,
            "delta_norm": 9.672952651977539,
            "family": "json_schema",
            "route_margin": 0.029261231422424316,
            "token": "d",
            "token_class": "json_value",
            "token_total_benefit": -2.196980118751526
          },
          {
            "assigned_benefit": -0.08743790785471599,
            "delta_norm": 9.410194396972656,
            "family": "code_heavy",
            "route_margin": 0.010846257209777832,
            "token": "d",
            "token_class": "string_literal",
            "token_total_benefit": -2.0985097885131836
          },
          {
            "assigned_benefit": -0.084659809867541,
            "delta_norm": 10.045101165771484,
            "family": "json_schema",
            "route_margin": 0.17815566062927246,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.031835436820984
          },
          {
            "assigned_benefit": -0.08465861777464549,
            "delta_norm": 10.0451021194458,
            "family": "json_schema",
            "route_margin": 0.17815494537353516,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.0318068265914917
          },
          {
            "assigned_benefit": -0.06883759796619415,
            "delta_norm": 10.110380172729492,
            "family": "json_schema",
            "route_margin": 0.03397488594055176,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.6521023511886597
          },
          {
            "assigned_benefit": -0.05808728809158007,
            "delta_norm": 9.843283653259277,
            "family": "broad_lm",
            "route_margin": 0.11114537715911865,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.3940949141979218
          },
          {
            "assigned_benefit": -0.05440836648146311,
            "delta_norm": 10.756836891174316,
            "family": "json_schema",
            "route_margin": 0.07790815830230713,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.3058007955551147
          },
          {
            "assigned_benefit": -0.05298296610514323,
            "delta_norm": 9.718286514282227,
            "family": "broad_lm",
            "route_margin": 0.345822811126709,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -1.2715911865234375
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.40207378069559735,
            "delta_norm": 10.130192756652832,
            "family": "code_heavy",
            "route_margin": 0.06621861457824707,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.649770736694336
          },
          {
            "assigned_benefit": 0.3553175131479899,
            "delta_norm": 9.701637268066406,
            "family": "code_heavy",
            "route_margin": 0.04655194282531738,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.527620315551758
          },
          {
            "assigned_benefit": 0.33899720509847003,
            "delta_norm": 10.083311080932617,
            "family": "code_heavy",
            "route_margin": 0.001168966293334961,
            "token": "\"",
            "token_class": "function_signature",
            "token_total_benefit": 8.135932922363281
          },
          {
            "assigned_benefit": 0.3301831881205241,
            "delta_norm": 10.148324012756348,
            "family": "code_heavy",
            "route_margin": 0.06938028335571289,
            "token": "'",
            "token_class": "quote",
            "token_total_benefit": 7.924396514892578
          },
          {
            "assigned_benefit": 0.31830819447835285,
            "delta_norm": 10.721653938293457,
            "family": "code_heavy",
            "route_margin": 0.030462026596069336,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 7.639396667480469
          },
          {
            "assigned_benefit": 0.3087804714838664,
            "delta_norm": 10.353020668029785,
            "family": "code_heavy",
            "route_margin": 0.08253538608551025,
            "token": "_",
            "token_class": "identifier",
            "token_total_benefit": 7.410731315612793
          },
          {
            "assigned_benefit": 0.3049144744873047,
            "delta_norm": 11.182428359985352,
            "family": "code_heavy",
            "route_margin": 0.03809559345245361,
            "token": "\\",
            "token_class": "string_literal",
            "token_total_benefit": 7.3179473876953125
          },
          {
            "assigned_benefit": 0.30479780832926434,
            "delta_norm": 9.808198928833008,
            "family": "code_heavy",
            "route_margin": 0.1236034631729126,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 7.315147399902344
          }
        ],
        "total_assigned_benefit": 12.589190567145128
      },
      "layer_9_expert_0": {
        "activation_count": 733,
        "mean_assigned_benefit": 0.06149327991815969,
        "mean_delta_norm": 9.522914865657707,
        "mean_harm": -0.02447574813576305,
        "mean_positive_benefit": 0.10735541831512688,
        "mean_route_margin": 0.10390387355549437,
        "positive_benefit_rate": 0.6521145975443383,
        "prose_benefit": 6.899080833949519,
        "structured_benefit": 35.899376254912596,
        "structured_prose_benefit_ratio": 5.203501324155564,
        "token_class_benefit": {
          "brace_bracket_paren": 2.8532710075378422,
          "comma_colon_semicolon": 2.215503493944804,
          "function_signature": 0.8347571194171904,
          "identifier": 7.039078228175639,
          "indentation": -1.0632629003375766,
          "json_key": 2.6383062402407322,
          "json_value": 0.7339508274259666,
          "newline": 4.2970462096036925,
          "number": 1.5907262961069744,
          "operator": 2.019771416982015,
          "other": 3.463005679805064,
          "prose_word": 9.354848001617937,
          "quote": 10.560482819875082,
          "space": -2.5793928559869532,
          "string_literal": 1.1164825956026714
        },
        "token_class_counts": {
          "brace_bracket_paren": 14,
          "comma_colon_semicolon": 24,
          "function_signature": 9,
          "identifier": 141,
          "indentation": 118,
          "json_key": 37,
          "json_value": 22,
          "newline": 21,
          "number": 11,
          "operator": 10,
          "other": 18,
          "prose_word": 164,
          "quote": 35,
          "space": 93,
          "string_literal": 16
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.12831215063730875,
            "delta_norm": 9.682025909423828,
            "family": "json_schema",
            "route_margin": 0.07054316997528076,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -3.07949161529541
          },
          {
            "assigned_benefit": -0.11042344570159912,
            "delta_norm": 9.630352973937988,
            "family": "json_schema",
            "route_margin": 0.17939496040344238,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.650162696838379
          },
          {
            "assigned_benefit": -0.10809943079948425,
            "delta_norm": 9.756316184997559,
            "family": "json_schema",
            "route_margin": 0.1236177384853363,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.594386339187622
          },
          {
            "assigned_benefit": -0.09138673543930054,
            "delta_norm": 9.480456352233887,
            "family": "json_schema",
            "route_margin": 0.11708259582519531,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.193281650543213
          },
          {
            "assigned_benefit": -0.09053297837575276,
            "delta_norm": 9.696833610534668,
            "family": "json_schema",
            "route_margin": 0.14027616381645203,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.1727914810180664
          },
          {
            "assigned_benefit": -0.0898671845595042,
            "delta_norm": 9.137983322143555,
            "family": "broad_lm",
            "route_margin": 0.0735921859741211,
            "token": "e",
            "token_class": "prose_word",
            "token_total_benefit": -2.1568124294281006
          },
          {
            "assigned_benefit": -0.08720193554957707,
            "delta_norm": 9.903801918029785,
            "family": "json_schema",
            "route_margin": 0.02560359239578247,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -2.09284645318985
          },
          {
            "assigned_benefit": -0.08489630619684856,
            "delta_norm": 9.8290433883667,
            "family": "code_heavy",
            "route_margin": 0.3637208640575409,
            "token": "w",
            "token_class": "identifier",
            "token_total_benefit": -2.0375113487243652
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.3964542547861735,
            "delta_norm": 9.555205345153809,
            "family": "code_heavy",
            "route_margin": 0.37883543968200684,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.514902114868164
          },
          {
            "assigned_benefit": 0.38860607147216797,
            "delta_norm": 9.93353271484375,
            "family": "json_schema",
            "route_margin": 0.031720876693725586,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.326545715332031
          },
          {
            "assigned_benefit": 0.37155044078826904,
            "delta_norm": 9.113840103149414,
            "family": "code_heavy",
            "route_margin": 0.003908663988113403,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.917210578918457
          },
          {
            "assigned_benefit": 0.35521737734476727,
            "delta_norm": 9.311173439025879,
            "family": "code_heavy",
            "route_margin": 0.420207679271698,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.525217056274414
          },
          {
            "assigned_benefit": 0.35289955139160156,
            "delta_norm": 9.236516952514648,
            "family": "code_heavy",
            "route_margin": 0.05928400158882141,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 8.469589233398438
          },
          {
            "assigned_benefit": 0.33861692746480304,
            "delta_norm": 9.64712905883789,
            "family": "json_schema",
            "route_margin": 0.14300057291984558,
            "token": "\\n",
            "token_class": "newline",
            "token_total_benefit": 8.126806259155273
          },
          {
            "assigned_benefit": 0.3335253397623698,
            "delta_norm": 10.029979705810547,
            "family": "code_heavy",
            "route_margin": 0.3981589674949646,
            "token": "\\",
            "token_class": "other",
            "token_total_benefit": 8.004608154296875
          },
          {
            "assigned_benefit": 0.32794443766276044,
            "delta_norm": 9.249502182006836,
            "family": "code_heavy",
            "route_margin": 0.013460904359817505,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 7.87066650390625
          }
        ],
        "total_assigned_benefit": 45.074574180011055
      },
      "layer_9_expert_1": {
        "activation_count": 20,
        "mean_assigned_benefit": 0.09754170278708175,
        "mean_delta_norm": 8.06861641407013,
        "mean_harm": -0.07770887811978658,
        "mean_positive_benefit": 0.15595856308937117,
        "mean_route_margin": 0.05163476467132568,
        "positive_benefit_rate": 0.75,
        "prose_benefit": 0.14503240585327862,
        "structured_benefit": 1.8843292047580156,
        "structured_prose_benefit_ratio": 12.992470156388972,
        "token_class_benefit": {
          "identifier": -0.1692317624886831,
          "json_key": 0.47770111759503686,
          "newline": 1.1559232324361872,
          "prose_word": 0.1149162898461024,
          "space": -0.048411438862482704,
          "string_literal": 0.41993661721547443
        },
        "token_class_counts": {
          "identifier": 6,
          "json_key": 5,
          "newline": 5,
          "prose_word": 1,
          "space": 1,
          "string_literal": 2
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.0962066650390625,
            "delta_norm": 8.226415634155273,
            "family": "json_schema",
            "route_margin": 0.04534119367599487,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.3089599609375
          },
          {
            "assigned_benefit": -0.0938494602839152,
            "delta_norm": 8.117659568786621,
            "family": "json_schema",
            "route_margin": 0.011706769466400146,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.252387046813965
          },
          {
            "assigned_benefit": -0.0938490629196167,
            "delta_norm": 8.117659568786621,
            "family": "json_schema",
            "route_margin": 0.011707067489624023,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.252377510070801
          },
          {
            "assigned_benefit": -0.0562277634938558,
            "delta_norm": 8.230914115905762,
            "family": "json_schema",
            "route_margin": 0.12492132186889648,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -1.349466323852539
          },
          {
            "assigned_benefit": -0.048411438862482704,
            "delta_norm": 7.945947647094727,
            "family": "json_schema",
            "route_margin": 0.018882781267166138,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -1.161874532699585
          },
          {
            "assigned_benefit": 0.046706090370814,
            "delta_norm": 7.924731254577637,
            "family": "json_schema",
            "route_margin": 0.016897350549697876,
            "token": "a",
            "token_class": "json_key",
            "token_total_benefit": 1.1209461688995361
          },
          {
            "assigned_benefit": 0.0729740560054779,
            "delta_norm": 8.107023239135742,
            "family": "json_schema",
            "route_margin": 0.1320166289806366,
            "token": "a",
            "token_class": "json_key",
            "token_total_benefit": 1.7513773441314697
          },
          {
            "assigned_benefit": 0.0785275548696589,
            "delta_norm": 8.073936462402344,
            "family": "broad_lm",
            "route_margin": 0.052798330783843994,
            "token": "\\n",
            "token_class": "newline",
            "token_total_benefit": 1.8846613168718136
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.3110353151957194,
            "delta_norm": 8.217626571655273,
            "family": "json_schema",
            "route_margin": 0.0025506019592285156,
            "token": "\\n",
            "token_class": "newline",
            "token_total_benefit": 7.464847564697266
          },
          {
            "assigned_benefit": 0.30917199452718097,
            "delta_norm": 8.228669166564941,
            "family": "code_heavy",
            "route_margin": 0.10365830361843109,
            "token": "\\",
            "token_class": "string_literal",
            "token_total_benefit": 7.420127868652344
          },
          {
            "assigned_benefit": 0.3045363823572795,
            "delta_norm": 7.950865268707275,
            "family": "json_schema",
            "route_margin": 0.05460059642791748,
            "token": "\\n",
            "token_class": "newline",
            "token_total_benefit": 7.308873176574707
          },
          {
            "assigned_benefit": 0.23937038580576578,
            "delta_norm": 7.873998165130615,
            "family": "json_schema",
            "route_margin": 0.08685153722763062,
            "token": "\\n",
            "token_class": "newline",
            "token_total_benefit": 5.744889259338379
          },
          {
            "assigned_benefit": 0.22245359420776367,
            "delta_norm": 8.002351760864258,
            "family": "json_schema",
            "route_margin": 0.003798961639404297,
            "token": "\\n",
            "token_class": "newline",
            "token_total_benefit": 5.338886260986328
          },
          {
            "assigned_benefit": 0.14407959580421448,
            "delta_norm": 7.874058246612549,
            "family": "json_schema",
            "route_margin": 0.03280726075172424,
            "token": "s",
            "token_class": "json_key",
            "token_total_benefit": 3.4579102993011475
          },
          {
            "assigned_benefit": 0.13531871636708578,
            "delta_norm": 7.824440002441406,
            "family": "json_schema",
            "route_margin": 0.05519986152648926,
            "token": "s",
            "token_class": "json_key",
            "token_total_benefit": 3.2476491928100586
          },
          {
            "assigned_benefit": 0.1149162898461024,
            "delta_norm": 8.417776107788086,
            "family": "broad_lm",
            "route_margin": 0.05099838972091675,
            "token": "a",
            "token_class": "prose_word",
            "token_total_benefit": 2.7579909563064575
          }
        ],
        "total_assigned_benefit": 1.950834055741635
      },
      "layer_9_expert_2": {
        "activation_count": 5365,
        "mean_assigned_benefit": 0.05244876521615138,
        "mean_delta_norm": 13.38948006856586,
        "mean_harm": -0.024726688481261427,
        "mean_positive_benefit": 0.0963040946484141,
        "mean_route_margin": 0.32054437063669117,
        "positive_benefit_rate": 0.6376514445479963,
        "prose_benefit": 49.36435604674013,
        "structured_benefit": 219.18152845168078,
        "structured_prose_benefit_ratio": 4.4400767275106565,
        "token_class_benefit": {
          "brace_bracket_paren": 19.5913131935522,
          "comma_colon_semicolon": 14.057493383685747,
          "function_signature": 12.28297589719296,
          "identifier": 48.474139376233055,
          "indentation": -9.978435636963688,
          "json_key": 13.323149092495449,
          "json_value": 10.277047210372992,
          "newline": 20.2696529081857,
          "number": 7.9858146111170445,
          "operator": 6.057528654734295,
          "other": 23.153881009959747,
          "prose_word": 66.667717878862,
          "quote": 52.64436149597168,
          "space": -17.637066318886383,
          "string_literal": 14.218052628139649
        },
        "token_class_counts": {
          "brace_bracket_paren": 108,
          "comma_colon_semicolon": 147,
          "function_signature": 105,
          "identifier": 944,
          "indentation": 790,
          "json_key": 169,
          "json_value": 189,
          "newline": 111,
          "number": 60,
          "operator": 35,
          "other": 104,
          "prose_word": 1428,
          "quote": 168,
          "space": 830,
          "string_literal": 177
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.17974231019616127,
            "delta_norm": 13.657981872558594,
            "family": "broad_lm",
            "route_margin": 0.4467126429080963,
            "token": "d",
            "token_class": "prose_word",
            "token_total_benefit": -4.3138154447078705
          },
          {
            "assigned_benefit": -0.14390301704406738,
            "delta_norm": 13.516756057739258,
            "family": "json_schema",
            "route_margin": 0.3731444478034973,
            "token": "o",
            "token_class": "json_value",
            "token_total_benefit": -3.453672409057617
          },
          {
            "assigned_benefit": -0.14381763339042664,
            "delta_norm": 13.894718170166016,
            "family": "broad_lm",
            "route_margin": 0.4393405020236969,
            "token": "c",
            "token_class": "prose_word",
            "token_total_benefit": -3.4516232013702393
          },
          {
            "assigned_benefit": -0.13103054463863373,
            "delta_norm": 13.70285701751709,
            "family": "code_heavy",
            "route_margin": 0.23572911322116852,
            "token": "g",
            "token_class": "identifier",
            "token_total_benefit": -3.1447330713272095
          },
          {
            "assigned_benefit": -0.1258842075864474,
            "delta_norm": 13.792675018310547,
            "family": "broad_lm",
            "route_margin": 0.006278812885284424,
            "token": "m",
            "token_class": "prose_word",
            "token_total_benefit": -3.0212209820747375
          },
          {
            "assigned_benefit": -0.12130660812060039,
            "delta_norm": 12.488980293273926,
            "family": "json_schema",
            "route_margin": 0.42870593070983887,
            "token": "d",
            "token_class": "identifier",
            "token_total_benefit": -2.911358594894409
          },
          {
            "assigned_benefit": -0.11974493662516277,
            "delta_norm": 13.012935638427734,
            "family": "code_heavy",
            "route_margin": 0.43020620942115784,
            "token": "5",
            "token_class": "number",
            "token_total_benefit": -2.8738784790039062
          },
          {
            "assigned_benefit": -0.1176329255104065,
            "delta_norm": 13.582592010498047,
            "family": "broad_lm",
            "route_margin": 0.1031571626663208,
            "token": "o",
            "token_class": "prose_word",
            "token_total_benefit": -2.823190212249756
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.4434954325358073,
            "delta_norm": 13.295406341552734,
            "family": "json_schema",
            "route_margin": 0.3220507502555847,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.643890380859375
          },
          {
            "assigned_benefit": 0.4348748524983724,
            "delta_norm": 13.56424331665039,
            "family": "json_schema",
            "route_margin": 0.5517843961715698,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.436996459960938
          },
          {
            "assigned_benefit": 0.42559146881103516,
            "delta_norm": 12.881815910339355,
            "family": "json_schema",
            "route_margin": 0.6741249561309814,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.214195251464844
          },
          {
            "assigned_benefit": 0.4194428126017253,
            "delta_norm": 13.297640800476074,
            "family": "json_schema",
            "route_margin": 0.7506534457206726,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 10.066627502441406
          },
          {
            "assigned_benefit": 0.4192720651626587,
            "delta_norm": 13.928282737731934,
            "family": "code_heavy",
            "route_margin": 0.8650410771369934,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 10.062529563903809
          },
          {
            "assigned_benefit": 0.41413907210032147,
            "delta_norm": 13.393442153930664,
            "family": "code_heavy",
            "route_margin": 0.0023502111434936523,
            "token": "(",
            "token_class": "brace_bracket_paren",
            "token_total_benefit": 9.939337730407715
          },
          {
            "assigned_benefit": 0.40491771697998047,
            "delta_norm": 13.300599098205566,
            "family": "json_schema",
            "route_margin": 0.31499698758125305,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.718025207519531
          },
          {
            "assigned_benefit": 0.40347035725911456,
            "delta_norm": 13.258857727050781,
            "family": "json_schema",
            "route_margin": 0.40700072050094604,
            "token": "\"",
            "token_class": "quote",
            "token_total_benefit": 9.68328857421875
          }
        ],
        "total_assigned_benefit": 281.38762538465215
      },
      "layer_9_expert_4": {
        "activation_count": 2,
        "mean_assigned_benefit": 0.07981754591067632,
        "mean_delta_norm": 7.7718305587768555,
        "mean_harm": null,
        "mean_positive_benefit": 0.07981754591067632,
        "mean_route_margin": 0.0067449212074279785,
        "positive_benefit_rate": 1.0,
        "prose_benefit": 0.05894047518571218,
        "structured_benefit": 0.10069461663564046,
        "structured_prose_benefit_ratio": 1.7084120261733136,
        "token_class_benefit": {
          "json_key": 0.10069461663564046,
          "space": 0.05894047518571218
        },
        "token_class_counts": {
          "json_key": 1,
          "space": 1
        },
        "top_negative_examples": [
          {
            "assigned_benefit": 0.05894047518571218,
            "delta_norm": 7.9751739501953125,
            "family": "json_schema",
            "route_margin": 0.010565996170043945,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": 1.4145714044570923
          },
          {
            "assigned_benefit": 0.10069461663564046,
            "delta_norm": 7.568487167358398,
            "family": "json_schema",
            "route_margin": 0.0029238462448120117,
            "token": "t",
            "token_class": "json_key",
            "token_total_benefit": 2.416670799255371
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.10069461663564046,
            "delta_norm": 7.568487167358398,
            "family": "json_schema",
            "route_margin": 0.0029238462448120117,
            "token": "t",
            "token_class": "json_key",
            "token_total_benefit": 2.416670799255371
          },
          {
            "assigned_benefit": 0.05894047518571218,
            "delta_norm": 7.9751739501953125,
            "family": "json_schema",
            "route_margin": 0.010565996170043945,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": 1.4145714044570923
          }
        ],
        "total_assigned_benefit": 0.15963509182135263
      },
      "layer_9_expert_5": {
        "activation_count": 1,
        "mean_assigned_benefit": 2.8677284717559814e-05,
        "mean_delta_norm": 6.700588703155518,
        "mean_harm": null,
        "mean_positive_benefit": 2.8677284717559814e-05,
        "mean_route_margin": 0.0035041868686676025,
        "positive_benefit_rate": 1.0,
        "prose_benefit": 2.8677284717559814e-05,
        "structured_benefit": 0,
        "structured_prose_benefit_ratio": 0.0,
        "token_class_benefit": {
          "indentation": 2.8677284717559814e-05
        },
        "token_class_counts": {
          "indentation": 1
        },
        "top_negative_examples": [
          {
            "assigned_benefit": 2.8677284717559814e-05,
            "delta_norm": 6.700588703155518,
            "family": "json_schema",
            "route_margin": 0.0035041868686676025,
            "token": " ",
            "token_class": "indentation",
            "token_total_benefit": 0.0006882548332214355
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 2.8677284717559814e-05,
            "delta_norm": 6.700588703155518,
            "family": "json_schema",
            "route_margin": 0.0035041868686676025,
            "token": " ",
            "token_class": "indentation",
            "token_total_benefit": 0.0006882548332214355
          }
        ],
        "total_assigned_benefit": 2.8677284717559814e-05
      },
      "layer_9_expert_6": {
        "activation_count": 23,
        "mean_assigned_benefit": 0.06963175686373227,
        "mean_delta_norm": 7.929560536923616,
        "mean_harm": -0.028757736086845398,
        "mean_positive_benefit": 0.09696217157222607,
        "mean_route_margin": 0.042437388845112015,
        "positive_benefit_rate": 0.782608695652174,
        "prose_benefit": 0.23713661730289462,
        "structured_benefit": 1.364393790562948,
        "structured_prose_benefit_ratio": 5.75361918408496,
        "token_class_benefit": {
          "comma_colon_semicolon": 0.1430241068204244,
          "function_signature": 0.04902775088946024,
          "identifier": 0.19406336545944214,
          "json_key": 0.41008254885673523,
          "json_value": 0.17404096325238544,
          "prose_word": 0.21529930333296457,
          "quote": 0.2823648452758789,
          "space": 0.021837313969930022,
          "string_literal": 0.11179021000862122
        },
        "token_class_counts": {
          "comma_colon_semicolon": 2,
          "function_signature": 1,
          "identifier": 4,
          "json_key": 5,
          "json_value": 3,
          "prose_word": 3,
          "quote": 1,
          "space": 3,
          "string_literal": 1
        },
        "top_negative_examples": [
          {
            "assigned_benefit": -0.08370453119277954,
            "delta_norm": 7.8330512046813965,
            "family": "json_schema",
            "route_margin": 0.07027286291122437,
            "token": "d",
            "token_class": "json_key",
            "token_total_benefit": -2.008908748626709
          },
          {
            "assigned_benefit": -0.03870187203089396,
            "delta_norm": 8.100049018859863,
            "family": "json_schema",
            "route_margin": 0.03158709406852722,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -0.9288449287414551
          },
          {
            "assigned_benefit": -0.015099863211313883,
            "delta_norm": 8.273736000061035,
            "family": "json_schema",
            "route_margin": 0.17595386505126953,
            "token": " ",
            "token_class": "space",
            "token_total_benefit": -0.3623967170715332
          },
          {
            "assigned_benefit": -0.004744509855906169,
            "delta_norm": 7.803741931915283,
            "family": "json_schema",
            "route_margin": 0.004727482795715332,
            "token": "l",
            "token_class": "identifier",
            "token_total_benefit": -0.11386823654174805
          },
          {
            "assigned_benefit": -0.001537904143333435,
            "delta_norm": 7.909633159637451,
            "family": "broad_lm",
            "route_margin": 0.0018337070941925049,
            "token": "n",
            "token_class": "prose_word",
            "token_total_benefit": -0.03690969944000244
          },
          {
            "assigned_benefit": 0.008972217639287313,
            "delta_norm": 8.090387344360352,
            "family": "json_schema",
            "route_margin": 0.012382984161376953,
            "token": "e",
            "token_class": "json_value",
            "token_total_benefit": 0.2153332233428955
          },
          {
            "assigned_benefit": 0.01669977108637492,
            "delta_norm": 8.251279830932617,
            "family": "code_heavy",
            "route_margin": 0.03784465789794922,
            "token": "l",
            "token_class": "identifier",
            "token_total_benefit": 0.40079450607299805
          },
          {
            "assigned_benefit": 0.017162173986434937,
            "delta_norm": 7.952333927154541,
            "family": "json_schema",
            "route_margin": 0.03928378224372864,
            "token": "l",
            "token_class": "json_key",
            "token_total_benefit": 0.4118921756744385
          }
        ],
        "top_positive_examples": [
          {
            "assigned_benefit": 0.2823648452758789,
            "delta_norm": 7.95038366317749,
            "family": "code_heavy",
            "route_margin": 0.002584606409072876,
            "token": "'",
            "token_class": "quote",
            "token_total_benefit": 6.776756286621094
          },
          {
            "assigned_benefit": 0.16540884971618652,
            "delta_norm": 7.993849754333496,
            "family": "broad_lm",
            "route_margin": 0.06816625595092773,
            "token": "i",
            "token_class": "prose_word",
            "token_total_benefit": 3.9698123931884766
          },
          {
            "assigned_benefit": 0.16065263748168945,
            "delta_norm": 8.152909278869629,
            "family": "json_schema",
            "route_margin": 0.08269402384757996,
            "token": "n",
            "token_class": "json_key",
            "token_total_benefit": 3.855663299560547
          },
          {
            "assigned_benefit": 0.15893723567326865,
            "delta_norm": 8.202790260314941,
            "family": "json_schema",
            "route_margin": 0.07849964499473572,
            "token": "n",
            "token_class": "json_key",
            "token_total_benefit": 3.8144936561584473
          },
          {
            "assigned_benefit": 0.15703503290812174,
            "delta_norm": 7.831442832946777,
            "family": "json_schema",
            "route_margin": 0.014072239398956299,
            "token": "n",
            "token_class": "json_key",
            "token_total_benefit": 3.768840789794922
          },
          {
            "assigned_benefit": 0.11179021000862122,
            "delta_norm": 7.79295015335083,
            "family": "code_heavy",
            "route_margin": 0.07715487480163574,
            "token": "r",
            "token_class": "string_literal",
            "token_total_benefit": 2.682965040206909
          },
          {
            "assigned_benefit": 0.09803493817647298,
            "delta_norm": 7.72549295425415,
            "family": "code_heavy",
            "route_margin": 0.023286372423171997,
            "token": "m",
            "token_class": "identifier",
            "token_total_benefit": 2.3528385162353516
          },
          {
            "assigned_benefit": 0.09388552109400432,
            "delta_norm": 7.368331432342529,
            "family": "json_schema",
            "route_margin": 0.020189255475997925,
            "token": "r",
            "token_class": "json_value",
            "token_total_benefit": 2.2532525062561035
          }
        ],
        "total_assigned_benefit": 1.6015304078658423
      }
    },
    "overall": {
      "assignment_count": 147456,
      "mean_assigned_benefit": 0.05373929488889463,
      "mean_delta_norm": 14.191877876427801,
      "mean_route_margin": 0.5117655237031108,
      "positive_assignment_rate": 0.6404622395833334,
      "total_assigned_benefit": 7924.181467136847
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
    "top1_invariants_clean": true
  },
  "schema_version": "1.0",
  "seq_len": 128,
  "spans_per_family": 16,
  "status": "PVR_EXPERT_FUNCTION_PROBE_SUPPORTED",
  "supported_conditions": {
    "all_global_experts_activated": true,
    "examples_generated": true,
    "most_global_experts_positive": true,
    "overall_assigned_benefit_positive": true,
    "structured_role_experts_present": true,
    "top1_invariants_clean": true
  },
  "top_k": 8
}
```
