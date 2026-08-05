# Retention Replay Cross-Architecture Control

Status: `PVR_REPLAY_ARCHITECTURE_SPECIFIC_ADVANTAGE_NOT_SUPPORTED`

| model | broad delta | structured gain | gain / broad regression | code delta | json delta | Top1 clean |
|---|---:|---:|---:|---:|---:|---|
| dense_300m | -0.04975154250860214 | 2.283872961997986 | 2283872.961997986 | -1.7702319622039795 | -2.797513961791992 | None |
| switch_top1_300m | -0.03817594423890114 | 2.0706578493118286 | 2070657.8493118286 | -1.5889215469360352 | -2.552394151687622 | None |
| pvr_baseline_300m | -0.06232965737581253 | 2.586464762687683 | 2586464.762687683 | -1.9880378246307373 | -3.184891700744629 | True |
| pvr_ean_300m | -0.023355387151241302 | 1.7389227151870728 | 1738922.7151870728 | -1.3145437240600586 | -2.163301706314087 | True |

```json
{
  "architecture_metrics": {
    "dense_300m": {
      "broad_delta": -0.04975154250860214,
      "broad_regression": 0.0,
      "code_delta": -1.7702319622039795,
      "json_delta": -2.797513961791992,
      "structured_delta": -2.283872961997986,
      "structured_gain": 2.283872961997986,
      "structured_gain_per_broad_regression": 2283872.961997986,
      "top1_invariants_clean": null
    },
    "pvr_baseline_300m": {
      "broad_delta": -0.06232965737581253,
      "broad_regression": 0.0,
      "code_delta": -1.9880378246307373,
      "json_delta": -3.184891700744629,
      "structured_delta": -2.586464762687683,
      "structured_gain": 2.586464762687683,
      "structured_gain_per_broad_regression": 2586464.762687683,
      "top1_invariants_clean": true
    },
    "pvr_ean_300m": {
      "broad_delta": -0.023355387151241302,
      "broad_regression": 0.0,
      "code_delta": -1.3145437240600586,
      "json_delta": -2.163301706314087,
      "structured_delta": -1.7389227151870728,
      "structured_gain": 1.7389227151870728,
      "structured_gain_per_broad_regression": 1738922.7151870728,
      "top1_invariants_clean": true
    },
    "switch_top1_300m": {
      "broad_delta": -0.03817594423890114,
      "broad_regression": 0.0,
      "code_delta": -1.5889215469360352,
      "json_delta": -2.552394151687622,
      "structured_delta": -2.0706578493118286,
      "structured_gain": 2.0706578493118286,
      "structured_gain_per_broad_regression": 2070657.8493118286,
      "top1_invariants_clean": null
    }
  },
  "benchmark_evidence_caveat": "Cross-architecture control over local reduced files; official benchmark adapters remain separate.",
  "broad_tolerance": 0.03,
  "broad_windows": 64,
  "created_at": "2026-06-17T20:36:42.700254+00:00",
  "decision_rule": "Support requires PVR EAN retention replay to have positive structured gain, clean Top1 invariants, and higher structured gain per broad-LM regression than dense and Switch controls.",
  "device": "cuda",
  "experiment": "PVR_RETENTION_REPLAY_CROSS_ARCHITECTURE_CONTROL",
  "git_commit": "d18165e32bec94cea3ca836937c81f6a0f3dc5f7",
  "lrs": {
    "dense_lr": 1e-06,
    "expert_lr": 1e-05,
    "router_lr": 0.0,
    "trunk_lr": 0.0
  },
  "max_steps": 100,
  "results": {
    "dense_300m": {
      "adapted_config": "benchmark/reports/generated/retention_replay_cross_architecture_control_seed_42/dense_300m/adapted_config.json",
      "adapted_row": {
        "active_flops_estimate": 1800000000,
        "active_params_per_token": 300000000,
        "checkpoint_path": "checkpoints/retention_replay_cross_architecture_control_seed_42/dense_300m/checkpoint.pt",
        "model_family": "dense_transformer",
        "model_variant": "dense_transformer_300m_retention_replay_control_seed_42",
        "routing_snapshots": [],
        "slice_summary": {
          "broad_lm": {
            "max_loss": 10.46955680847168,
            "mean_loss": 2.726851936429739,
            "min_loss": 2.3639283180236816,
            "window_count": 64
          },
          "code_heavy": {
            "max_loss": 16.76173973083496,
            "mean_loss": 13.37874150276184,
            "min_loss": 8.5480375289917,
            "window_count": 4
          },
          "gutenberg_prose": {
            "max_loss": 10.46955680847168,
            "mean_loss": 2.726851936429739,
            "min_loss": 2.3639283180236816,
            "window_count": 64
          },
          "humaneval_like_heldout": {
            "max_loss": 16.76173973083496,
            "mean_loss": 13.37874150276184,
            "min_loss": 8.5480375289917,
            "window_count": 4
          },
          "json_schema": {
            "max_loss": 13.613184928894043,
            "mean_loss": 11.22570252418518,
            "min_loss": 10.171309471130371,
            "window_count": 4
          },
          "unseen_structured_spans": {
            "max_loss": 16.76173973083496,
            "mean_loss": 12.30222201347351,
            "min_loss": 8.5480375289917,
            "window_count": 8
          }
        },
        "top1_invariants_clean": null
      },
      "base_config": "benchmark/reports/generated/training_300m_real_4k/dense_transformer_300m/run_config.yaml",
      "base_row": {
        "active_flops_estimate": 1800000000,
        "active_params_per_token": 300000000,
        "checkpoint_path": "checkpoints/benchmark_300m/dense_transformer_300m/checkpoint.pt",
        "model_family": "dense_transformer",
        "model_variant": "dense_transformer_300m",
        "routing_snapshots": [],
        "slice_summary": {
          "broad_lm": {
            "max_loss": 10.864638328552246,
            "mean_loss": 2.776603478938341,
            "min_loss": 2.2984459400177,
            "window_count": 64
          },
          "code_heavy": {
            "max_loss": 19.473281860351562,
            "mean_loss": 15.14897346496582,
            "min_loss": 9.624191284179688,
            "window_count": 4
          },
          "gutenberg_prose": {
            "max_loss": 10.864638328552246,
            "mean_loss": 2.776603478938341,
            "min_loss": 2.2984459400177,
            "window_count": 64
          },
          "humaneval_like_heldout": {
            "max_loss": 19.473281860351562,
            "mean_loss": 15.14897346496582,
            "min_loss": 9.624191284179688,
            "window_count": 4
          },
          "json_schema": {
            "max_loss": 16.16033935546875,
            "mean_loss": 14.023216485977173,
            "min_loss": 13.100582122802734,
            "window_count": 4
          },
          "unseen_structured_spans": {
            "max_loss": 19.473281860351562,
            "mean_loss": 14.586094975471497,
            "min_loss": 9.624191284179688,
            "window_count": 8
          }
        },
        "top1_invariants_clean": null
      },
      "best_gate": {
        "accepted": true,
        "broad_delta_vs_base": -0.04975154250860214,
        "broad_limit": 2.806603478938341,
        "broad_lm": 2.726851936429739,
        "reason": "retention_gate_passed",
        "step": 100,
        "structured_delta_vs_base": -2.283872961997986,
        "structured_unseen": 12.30222201347351
      },
      "best_step": 100,
      "checkpoint_path": "checkpoints/retention_replay_cross_architecture_control_seed_42/dense_300m/checkpoint.pt",
      "elapsed_seconds": 26.071810483932495,
      "family": "dense_transformer",
      "gate_curve": [
        {
          "accepted": true,
          "broad_delta_vs_base": -0.0036002695560455322,
          "broad_limit": 2.806603478938341,
          "broad_lm": 2.7730032093822956,
          "step": 10,
          "structured_delta_vs_base": -0.6599699258804321,
          "structured_unseen": 13.926125049591064
        },
        {
          "accepted": false,
          "broad_delta_vs_base": 0.04745930805802345,
          "broad_limit": 2.806603478938341,
          "broad_lm": 2.8240627869963646,
          "step": 20,
          "structured_delta_vs_base": -1.1711543798446655,
          "structured_unseen": 13.414940595626831
        },
        {
          "accepted": true,
          "broad_delta_vs_base": -0.061183858662843704,
          "broad_limit": 2.806603478938341,
          "broad_lm": 2.7154196202754974,
          "step": 30,
          "structured_delta_vs_base": -1.2781418561935425,
          "structured_unseen": 13.307953119277954
        },
        {
          "accepted": true,
          "broad_delta_vs_base": -0.013561241328716278,
          "broad_limit": 2.806603478938341,
          "broad_lm": 2.763042237609625,
          "step": 40,
          "structured_delta_vs_base": -1.4090204238891602,
          "structured_unseen": 13.177074551582336
        },
        {
          "accepted": true,
          "broad_delta_vs_base": -0.05305534601211548,
          "broad_limit": 2.806603478938341,
          "broad_lm": 2.7235481329262257,
          "step": 50,
          "structured_delta_vs_base": -1.6164809465408325,
          "structured_unseen": 12.969614028930664
        },
        {
          "accepted": true,
          "broad_delta_vs_base": -0.04652790725231171,
          "broad_limit": 2.806603478938341,
          "broad_lm": 2.7300755716860294,
          "step": 60,
          "structured_delta_vs_base": -1.6554780006408691,
          "structured_unseen": 12.930616974830627
        },
        {
          "accepted": true,
          "broad_delta_vs_base": -0.04397169500589371,
          "broad_limit": 2.806603478938341,
          "broad_lm": 2.7326317839324474,
          "step": 70,
          "structured_delta_vs_base": -1.8308178186416626,
          "structured_unseen": 12.755277156829834
        },
        {
          "accepted": true,
          "broad_delta_vs_base": -0.06079145893454552,
          "broad_limit": 2.806603478938341,
          "broad_lm": 2.7158120200037956,
          "step": 80,
          "structured_delta_vs_base": -1.893733263015747,
          "structured_unseen": 12.69236171245575
        },
        {
          "accepted": true,
          "broad_delta_vs_base": -0.031800996512174606,
          "broad_limit": 2.806603478938341,
          "broad_lm": 2.7448024824261665,
          "step": 90,
          "structured_delta_vs_base": -2.097574472427368,
          "structured_unseen": 12.488520503044128
        },
        {
          "accepted": true,
          "broad_delta_vs_base": -0.04975154250860214,
          "broad_limit": 2.806603478938341,
          "broad_lm": 2.726851936429739,
          "step": 100,
          "structured_delta_vs_base": -2.283872961997986,
          "structured_unseen": 12.30222201347351
        }
      ],
      "key": "dense_300m",
      "parameter_counts": {
        "dense_all": 248355592,
        "expert": 0,
        "frozen": 0,
        "router": 0,
        "trunk": 0
      },
      "training_curve": [
        {
          "loss": 12.492525100708008,
          "retention_loss": 2.7069220542907715,
          "step": 1,
          "structured_loss": 7.078680992126465
        },
        {
          "loss": 10.24949836730957,
          "retention_loss": 2.6164026260375977,
          "step": 2,
          "structured_loss": 5.016693592071533
        },
        {
          "loss": 12.651224136352539,
          "retention_loss": 2.502535104751587,
          "step": 3,
          "structured_loss": 7.646153926849365
        },
        {
          "loss": 10.646480560302734,
          "retention_loss": 3.156381130218506,
          "step": 4,
          "structured_loss": 4.3337178230285645
        },
        {
          "loss": 17.310400009155273,
          "retention_loss": 2.7166907787323,
          "step": 5,
          "structured_loss": 11.877017974853516
        },
        {
          "loss": 12.303792953491211,
          "retention_loss": 2.6434648036956787,
          "step": 6,
          "structured_loss": 7.016863822937012
        },
        {
          "loss": 13.939757347106934,
          "retention_loss": 2.7714791297912598,
          "step": 7,
          "structured_loss": 8.396799087524414
        },
        {
          "loss": 18.994186401367188,
          "retention_loss": 2.6453003883361816,
          "step": 8,
          "structured_loss": 13.70358657836914
        },
        {
          "loss": 24.22748565673828,
          "retention_loss": 2.5781636238098145,
          "step": 9,
          "structured_loss": 19.071157455444336
        },
        {
          "loss": 16.191131591796875,
          "retention_loss": 2.8456263542175293,
          "step": 10,
          "structured_loss": 10.499879837036133
        },
        {
          "loss": 12.512840270996094,
          "retention_loss": 2.506063222885132,
          "step": 11,
          "structured_loss": 7.500714302062988
        },
        {
          "loss": 13.460185050964355,
          "retention_loss": 2.5721230506896973,
          "step": 12,
          "structured_loss": 8.315938949584961
        },
        {
          "loss": 13.564812660217285,
          "retention_loss": 2.585721015930176,
          "step": 13,
          "structured_loss": 8.393370628356934
        },
        {
          "loss": 13.03532886505127,
          "retention_loss": 2.4188108444213867,
          "step": 14,
          "structured_loss": 8.197707176208496
        },
        {
          "loss": 13.397420883178711,
          "retention_loss": 2.4337825775146484,
          "step": 15,
          "structured_loss": 8.529855728149414
        },
        {
          "loss": 14.738508224487305,
          "retention_loss": 2.537865400314331,
          "step": 16,
          "structured_loss": 9.6627779006958
        },
        {
          "loss": 11.684087753295898,
          "retention_loss": 2.3323822021484375,
          "step": 17,
          "structured_loss": 7.019323825836182
        },
        {
          "loss": 11.30343246459961,
          "retention_loss": 2.4816372394561768,
          "step": 18,
          "structured_loss": 6.340158462524414
        },
        {
          "loss": 14.740640640258789,
          "retention_loss": 2.446171522140503,
          "step": 19,
          "structured_loss": 9.848297119140625
        },
        {
          "loss": 13.831543922424316,
          "retention_loss": 2.6102352142333984,
          "step": 20,
          "structured_loss": 8.61107349395752
        },
        {
          "loss": 10.398660659790039,
          "retention_loss": 2.431994676589966,
          "step": 21,
          "structured_loss": 5.534671306610107
        },
        {
          "loss": 14.677021980285645,
          "retention_loss": 2.610788345336914,
          "step": 22,
          "structured_loss": 9.455445289611816
        },
        {
          "loss": 10.680099487304688,
          "retention_loss": 2.506608724594116,
          "step": 23,
          "structured_loss": 5.666882514953613
        },
        {
          "loss": 12.290071487426758,
          "retention_loss": 2.480530261993408,
          "step": 24,
          "structured_loss": 7.329010963439941
        },
        {
          "loss": 14.01323127746582,
          "retention_loss": 2.49101185798645,
          "step": 25,
          "structured_loss": 9.031208038330078
        },
        {
          "loss": 12.765092849731445,
          "retention_loss": 2.501429557800293,
          "step": 26,
          "structured_loss": 7.762233257293701
        },
        {
          "loss": 12.826093673706055,
          "retention_loss": 2.574551582336426,
          "step": 27,
          "structured_loss": 7.676990985870361
        },
        {
          "loss": 22.610177993774414,
          "retention_loss": 2.6531355381011963,
          "step": 28,
          "structured_loss": 17.30390739440918
        },
        {
          "loss": 17.5037841796875,
          "retention_loss": 2.441657543182373,
          "step": 29,
          "structured_loss": 12.620469093322754
        },
        {
          "loss": 16.9103946685791,
          "retention_loss": 2.6427292823791504,
          "step": 30,
          "structured_loss": 11.6249361038208
        },
        {
          "loss": 17.84131622314453,
          "retention_loss": 3.1487982273101807,
          "step": 31,
          "structured_loss": 11.543720245361328
        },
        {
          "loss": 12.209081649780273,
          "retention_loss": 2.5015416145324707,
          "step": 32,
          "structured_loss": 7.205998420715332
        },
        {
          "loss": 11.412580490112305,
          "retention_loss": 2.8873069286346436,
          "step": 33,
          "structured_loss": 5.637966156005859
        },
        {
          "loss": 11.852535247802734,
          "retention_loss": 2.547166585922241,
          "step": 34,
          "structured_loss": 6.75820255279541
        },
        {
          "loss": 11.31777572631836,
          "retention_loss": 2.6241118907928467,
          "step": 35,
          "structured_loss": 6.069551467895508
        },
        {
          "loss": 12.540143013000488,
          "retention_loss": 2.6276988983154297,
          "step": 36,
          "structured_loss": 7.284745216369629
        },
        {
          "loss": 9.665348052978516,
          "retention_loss": 2.4839272499084473,
          "step": 37,
          "structured_loss": 4.697493553161621
        },
        {
          "loss": 10.103693008422852,
          "retention_loss": 2.705869436264038,
          "step": 38,
          "structured_loss": 4.691953659057617
        },
        {
          "loss": 10.649410247802734,
          "retention_loss": 2.6434590816497803,
          "step": 39,
          "structured_loss": 5.362491607666016
        },
        {
          "loss": 17.318763732910156,
          "retention_loss": 2.374885320663452,
          "step": 40,
          "structured_loss": 12.56899356842041
        },
        {
          "loss": 11.187941551208496,
          "retention_loss": 2.6080119609832764,
          "step": 41,
          "structured_loss": 5.971917629241943
        },
        {
          "loss": 11.351318359375,
          "retention_loss": 2.44863224029541,
          "step": 42,
          "structured_loss": 6.45405387878418
        },
        {
          "loss": 16.20287322998047,
          "retention_loss": 2.508511543273926,
          "step": 43,
          "structured_loss": 11.185851097106934
        },
        {
          "loss": 15.277786254882812,
          "retention_loss": 2.6096460819244385,
          "step": 44,
          "structured_loss": 10.058494567871094
        },
        {
          "loss": 10.636411666870117,
          "retention_loss": 2.5554091930389404,
          "step": 45,
          "structured_loss": 5.525592803955078
        },
        {
          "loss": 10.600019454956055,
          "retention_loss": 2.3407506942749023,
          "step": 46,
          "structured_loss": 5.918517589569092
        },
        {
          "loss": 19.464385986328125,
          "retention_loss": 2.4703590869903564,
          "step": 47,
          "structured_loss": 14.52366828918457
        },
        {
          "loss": 20.625898361206055,
          "retention_loss": 2.4629743099212646,
          "step": 48,
          "structured_loss": 15.699949264526367
        },
        {
          "loss": 14.312522888183594,
          "retention_loss": 2.610379457473755,
          "step": 49,
          "structured_loss": 9.091764450073242
        },
        {
          "loss": 24.609128952026367,
          "retention_loss": 2.443495035171509,
          "step": 50,
          "structured_loss": 19.722139358520508
        },
        {
          "loss": 13.85228157043457,
          "retention_loss": 2.3792035579681396,
          "step": 51,
          "structured_loss": 9.093873977661133
        },
        {
          "loss": 14.266169548034668,
          "retention_loss": 2.508486747741699,
          "step": 52,
          "structured_loss": 9.24919605255127
        },
        {
          "loss": 22.622482299804688,
          "retention_loss": 2.3400986194610596,
          "step": 53,
          "structured_loss": 17.942285537719727
        },
        {
          "loss": 14.408350944519043,
          "retention_loss": 2.420901298522949,
          "step": 54,
          "structured_loss": 9.566548347473145
        },
        {
          "loss": 11.789310455322266,
          "retention_loss": 2.3782448768615723,
          "step": 55,
          "structured_loss": 7.032821178436279
        },
        {
          "loss": 18.771671295166016,
          "retention_loss": 2.4354352951049805,
          "step": 56,
          "structured_loss": 13.900801658630371
        },
        {
          "loss": 31.656089782714844,
          "retention_loss": 2.4203031063079834,
          "step": 57,
          "structured_loss": 26.81548309326172
        },
        {
          "loss": 17.350358963012695,
          "retention_loss": 2.3834030628204346,
          "step": 58,
          "structured_loss": 12.583553314208984
        },
        {
          "loss": 23.191448211669922,
          "retention_loss": 2.4183905124664307,
          "step": 59,
          "structured_loss": 18.35466766357422
        },
        {
          "loss": 19.52475357055664,
          "retention_loss": 2.5521321296691895,
          "step": 60,
          "structured_loss": 14.420490264892578
        },
        {
          "loss": 28.103954315185547,
          "retention_loss": 2.900254011154175,
          "step": 61,
          "structured_loss": 22.30344581604004
        },
        {
          "loss": 27.116031646728516,
          "retention_loss": 2.650172710418701,
          "step": 62,
          "structured_loss": 21.815685272216797
        },
        {
          "loss": 13.321260452270508,
          "retention_loss": 2.58530330657959,
          "step": 63,
          "structured_loss": 8.150653839111328
        },
        {
          "loss": 16.993751525878906,
          "retention_loss": 2.1612253189086914,
          "step": 64,
          "structured_loss": 12.67130184173584
        },
        {
          "loss": 17.57455825805664,
          "retention_loss": 2.444645881652832,
          "step": 65,
          "structured_loss": 12.68526554107666
        },
        {
          "loss": 16.5113468170166,
          "retention_loss": 2.346630811691284,
          "step": 66,
          "structured_loss": 11.818084716796875
        },
        {
          "loss": 22.76247787475586,
          "retention_loss": 2.5360541343688965,
          "step": 67,
          "structured_loss": 17.69036865234375
        },
        {
          "loss": 24.860294342041016,
          "retention_loss": 2.29481840133667,
          "step": 68,
          "structured_loss": 20.270658493041992
        },
        {
          "loss": 13.611661911010742,
          "retention_loss": 2.549334764480591,
          "step": 69,
          "structured_loss": 8.512992858886719
        },
        {
          "loss": 28.131853103637695,
          "retention_loss": 2.629096746444702,
          "step": 70,
          "structured_loss": 22.873659133911133
        },
        {
          "loss": 27.67380142211914,
          "retention_loss": 2.431537389755249,
          "step": 71,
          "structured_loss": 22.810726165771484
        },
        {
          "loss": 10.594532012939453,
          "retention_loss": 2.496788263320923,
          "step": 72,
          "structured_loss": 5.600955009460449
        },
        {
          "loss": 22.268030166625977,
          "retention_loss": 2.279492139816284,
          "step": 73,
          "structured_loss": 17.70904541015625
        },
        {
          "loss": 21.846792221069336,
          "retention_loss": 2.5277645587921143,
          "step": 74,
          "structured_loss": 16.791263580322266
        },
        {
          "loss": 22.923898696899414,
          "retention_loss": 2.4689035415649414,
          "step": 75,
          "structured_loss": 17.98609161376953
        },
        {
          "loss": 14.439720153808594,
          "retention_loss": 2.419048547744751,
          "step": 76,
          "structured_loss": 9.60162353515625
        },
        {
          "loss": 21.342037200927734,
          "retention_loss": 2.4504058361053467,
          "step": 77,
          "structured_loss": 16.441225051879883
        },
        {
          "loss": 22.171951293945312,
          "retention_loss": 2.3788161277770996,
          "step": 78,
          "structured_loss": 17.41431999206543
        },
        {
          "loss": 30.760360717773438,
          "retention_loss": 2.368058681488037,
          "step": 79,
          "structured_loss": 26.024242401123047
        },
        {
          "loss": 22.01262092590332,
          "retention_loss": 2.2151715755462646,
          "step": 80,
          "structured_loss": 17.582277297973633
        },
        {
          "loss": 18.708988189697266,
          "retention_loss": 2.459523916244507,
          "step": 81,
          "structured_loss": 13.78994083404541
        },
        {
          "loss": 24.433523178100586,
          "retention_loss": 2.5153510570526123,
          "step": 82,
          "structured_loss": 19.402820587158203
        },
        {
          "loss": 16.265399932861328,
          "retention_loss": 2.614521026611328,
          "step": 83,
          "structured_loss": 11.036357879638672
        },
        {
          "loss": 19.36629295349121,
          "retention_loss": 2.5541131496429443,
          "step": 84,
          "structured_loss": 14.25806713104248
        },
        {
          "loss": 16.281282424926758,
          "retention_loss": 2.7829792499542236,
          "step": 85,
          "structured_loss": 10.715324401855469
        },
        {
          "loss": 20.560977935791016,
          "retention_loss": 2.619459390640259,
          "step": 86,
          "structured_loss": 15.32205867767334
        },
        {
          "loss": 22.861631393432617,
          "retention_loss": 2.724088430404663,
          "step": 87,
          "structured_loss": 17.413454055786133
        },
        {
          "loss": 18.330692291259766,
          "retention_loss": 2.6294679641723633,
          "step": 88,
          "structured_loss": 13.071755409240723
        },
        {
          "loss": 23.550251007080078,
          "retention_loss": 2.5603537559509277,
          "step": 89,
          "structured_loss": 18.42954444885254
        },
        {
          "loss": 18.17697525024414,
          "retention_loss": 2.3741519451141357,
          "step": 90,
          "structured_loss": 13.428671836853027
        },
        {
          "loss": 21.21394920349121,
          "retention_loss": 2.387425422668457,
          "step": 91,
          "structured_loss": 16.439098358154297
        },
        {
          "loss": 18.40862464904785,
          "retention_loss": 2.420938014984131,
          "step": 92,
          "structured_loss": 13.56674861907959
        },
        {
          "loss": 20.94186019897461,
          "retention_loss": 2.5644567012786865,
          "step": 93,
          "structured_loss": 15.812947273254395
        },
        {
          "loss": 24.7945499420166,
          "retention_loss": 2.4400317668914795,
          "step": 94,
          "structured_loss": 19.914485931396484
        },
        {
          "loss": 19.216930389404297,
          "retention_loss": 2.383084774017334,
          "step": 95,
          "structured_loss": 14.450761795043945
        },
        {
          "loss": 21.631736755371094,
          "retention_loss": 2.5203537940979004,
          "step": 96,
          "structured_loss": 16.591028213500977
        },
        {
          "loss": 18.911426544189453,
          "retention_loss": 2.3161609172821045,
          "step": 97,
          "structured_loss": 14.279104232788086
        },
        {
          "loss": 24.908740997314453,
          "retention_loss": 2.4646763801574707,
          "step": 98,
          "structured_loss": 19.979389190673828
        },
        {
          "loss": 19.236644744873047,
          "retention_loss": 2.4335741996765137,
          "step": 99,
          "structured_loss": 14.369497299194336
        },
        {
          "loss": 12.171770095825195,
          "retention_loss": 2.34218430519104,
          "step": 100,
          "structured_loss": 7.487401008605957
        }
      ]
    },
    "pvr_baseline_300m": {
      "adapted_config": "benchmark/reports/generated/retention_replay_cross_architecture_control_seed_42/pvr_baseline_300m/adapted_config.json",
      "adapted_row": {
        "active_flops_estimate": 630000000,
        "active_params_per_token": 105000000,
        "checkpoint_path": "checkpoints/retention_replay_cross_architecture_control_seed_42/pvr_baseline_300m/checkpoint.pt",
        "model_family": "pvr_ec_o",
        "model_variant": "pvr_ec_o_full_300m_baseline_seed_42_retention_replay_control_seed_42",
        "routing_snapshots": [
          {
            "challenger_disagreement_rate": null,
            "descriptor_control_margin": 0.4759409075510727,
            "expert_utilization": [
              253,
              400,
              368,
              158,
              548,
              332,
              391,
              622
            ],
            "failure_mode_distribution": {},
            "high_gap_monopoly_rate": 0.20247395833333334,
            "operator_control_margin": 0.4759409075510727,
            "owner_churn": null,
            "owner_entropy": 2.0115961526915482,
            "owners_per_token": 1.0,
            "production_map_mutated": false,
            "prototype_entropy": 2.0115961526915482,
            "prototype_margin": 0.4759409075510727,
            "prototype_monopoly_rate": 0.20247395833333334,
            "runtime_dynamic_k_count": 0,
            "runtime_expert_choice_count": 0,
            "stale_owner_rate": null,
            "step": 0,
            "top2_execution_count": 0,
            "top4_execution_count": 0
          },
          {
            "challenger_disagreement_rate": null,
            "descriptor_control_margin": 0.4759619871644342,
            "expert_utilization": [
              262,
              391,
              370,
              130,
              549,
              398,
              400,
              572
            ],
            "failure_mode_distribution": {},
            "high_gap_monopoly_rate": 0.18619791666666666,
            "operator_control_margin": 0.4759619871644342,
            "owner_churn": null,
            "owner_entropy": 2.012019715690269,
            "owners_per_token": 1.0,
            "production_map_mutated": false,
            "prototype_entropy": 2.012019715690269,
            "prototype_margin": 0.4759619871644342,
            "prototype_monopoly_rate": 0.18619791666666666,
            "runtime_dynamic_k_count": 0,
            "runtime_expert_choice_count": 0,
            "stale_owner_rate": null,
            "step": 25,
            "top2_execution_count": 0,
            "top4_execution_count": 0
          },
          {
            "challenger_disagreement_rate": null,
            "descriptor_control_margin": 0.4776543127312228,
            "expert_utilization": [
              280,
              399,
              367,
              141,
              571,
              382,
              384,
              548
            ],
            "failure_mode_distribution": {},
            "high_gap_monopoly_rate": 0.18587239583333334,
            "operator_control_margin": 0.4776543127312228,
            "owner_churn": null,
            "owner_entropy": 2.0181130182101774,
            "owners_per_token": 1.0,
            "production_map_mutated": false,
            "prototype_entropy": 2.0181130182101774,
            "prototype_margin": 0.4776543127312228,
            "prototype_monopoly_rate": 0.18587239583333334,
            "runtime_dynamic_k_count": 0,
            "runtime_expert_choice_count": 0,
            "stale_owner_rate": null,
            "step": 50,
            "top2_execution_count": 0,
            "top4_execution_count": 0
          },
          {
            "challenger_disagreement_rate": null,
            "descriptor_control_margin": 0.46896375770666054,
            "expert_utilization": [
              279,
              410,
              349,
              138,
              545,
              339,
              394,
              618
            ],
            "failure_mode_distribution": {},
            "high_gap_monopoly_rate": 0.201171875,
            "operator_control_margin": 0.46896375770666054,
            "owner_churn": null,
            "owner_entropy": 2.0091504837628404,
            "owners_per_token": 1.0,
            "production_map_mutated": false,
            "prototype_entropy": 2.0091504837628404,
            "prototype_margin": 0.46896375770666054,
            "prototype_monopoly_rate": 0.201171875,
            "runtime_dynamic_k_count": 0,
            "runtime_expert_choice_count": 0,
            "stale_owner_rate": null,
            "step": 75,
            "top2_execution_count": 0,
            "top4_execution_count": 0
          }
        ],
        "slice_summary": {
          "broad_lm": {
            "max_loss": 11.76966381072998,
            "mean_loss": 2.7618812657892704,
            "min_loss": 2.360419273376465,
            "window_count": 64
          },
          "code_heavy": {
            "max_loss": 10.185291290283203,
            "mean_loss": 8.384888529777527,
            "min_loss": 5.888158321380615,
            "window_count": 4
          },
          "gutenberg_prose": {
            "max_loss": 11.76966381072998,
            "mean_loss": 2.7618812657892704,
            "min_loss": 2.360419273376465,
            "window_count": 64
          },
          "humaneval_like_heldout": {
            "max_loss": 10.185291290283203,
            "mean_loss": 8.384888529777527,
            "min_loss": 5.888158321380615,
            "window_count": 4
          },
          "json_schema": {
            "max_loss": 8.400888442993164,
            "mean_loss": 7.216880559921265,
            "min_loss": 6.754478454589844,
            "window_count": 4
          },
          "unseen_structured_spans": {
            "max_loss": 10.185291290283203,
            "mean_loss": 7.800884544849396,
            "min_loss": 5.888158321380615,
            "window_count": 8
          }
        },
        "top1_invariants_clean": true
      },
      "base_config": "benchmark/reports/generated/shared_trunk_init_300m_repeat_seed_42/pvr_ec_o_full_300m_baseline_seed_42/run_config.yaml",
      "base_row": {
        "active_flops_estimate": 630000000,
        "active_params_per_token": 105000000,
        "checkpoint_path": "checkpoints/shared_trunk_init_300m_repeat_seed_42/pvr_ec_o_full_300m_baseline_seed_42/checkpoint.pt",
        "model_family": "pvr_ec_o",
        "model_variant": "pvr_ec_o_full_300m_baseline_seed_42",
        "routing_snapshots": [
          {
            "challenger_disagreement_rate": null,
            "descriptor_control_margin": 0.4764863158367613,
            "expert_utilization": [
              265,
              400,
              363,
              158,
              546,
              323,
              389,
              628
            ],
            "failure_mode_distribution": {},
            "high_gap_monopoly_rate": 0.20442708333333334,
            "operator_control_margin": 0.4764863158367613,
            "owner_churn": null,
            "owner_entropy": 2.0118771550900942,
            "owners_per_token": 1.0,
            "production_map_mutated": false,
            "prototype_entropy": 2.0118771550900942,
            "prototype_margin": 0.4764863158367613,
            "prototype_monopoly_rate": 0.20442708333333334,
            "runtime_dynamic_k_count": 0,
            "runtime_expert_choice_count": 0,
            "stale_owner_rate": null,
            "step": 0,
            "top2_execution_count": 0,
            "top4_execution_count": 0
          },
          {
            "challenger_disagreement_rate": null,
            "descriptor_control_margin": 0.47544338050526375,
            "expert_utilization": [
              275,
              389,
              362,
              135,
              547,
              393,
              398,
              573
            ],
            "failure_mode_distribution": {},
            "high_gap_monopoly_rate": 0.1865234375,
            "operator_control_margin": 0.47544338050526375,
            "owner_churn": null,
            "owner_entropy": 2.015325695027265,
            "owners_per_token": 1.0,
            "production_map_mutated": false,
            "prototype_entropy": 2.015325695027265,
            "prototype_margin": 0.47544338050526375,
            "prototype_monopoly_rate": 0.1865234375,
            "runtime_dynamic_k_count": 0,
            "runtime_expert_choice_count": 0,
            "stale_owner_rate": null,
            "step": 25,
            "top2_execution_count": 0,
            "top4_execution_count": 0
          },
          {
            "challenger_disagreement_rate": null,
            "descriptor_control_margin": 0.477010672443915,
            "expert_utilization": [
              288,
              399,
              363,
              149,
              571,
              374,
              388,
              540
            ],
            "failure_mode_distribution": {},
            "high_gap_monopoly_rate": 0.18587239583333334,
            "operator_control_margin": 0.477010672443915,
            "owner_churn": null,
            "owner_entropy": 2.022228376128187,
            "owners_per_token": 1.0,
            "production_map_mutated": false,
            "prototype_entropy": 2.022228376128187,
            "prototype_margin": 0.477010672443915,
            "prototype_monopoly_rate": 0.18587239583333334,
            "runtime_dynamic_k_count": 0,
            "runtime_expert_choice_count": 0,
            "stale_owner_rate": null,
            "step": 50,
            "top2_execution_count": 0,
            "top4_execution_count": 0
          },
          {
            "challenger_disagreement_rate": null,
            "descriptor_control_margin": 0.46924798957722186,
            "expert_utilization": [
              285,
              409,
              347,
              145,
              540,
              330,
              393,
              623
            ],
            "failure_mode_distribution": {},
            "high_gap_monopoly_rate": 0.20279947916666666,
            "operator_control_margin": 0.46924798957722186,
            "owner_churn": null,
            "owner_entropy": 2.011370364940322,
            "owners_per_token": 1.0,
            "production_map_mutated": false,
            "prototype_entropy": 2.011370364940322,
            "prototype_margin": 0.46924798957722186,
            "prototype_monopoly_rate": 0.20279947916666666,
            "runtime_dynamic_k_count": 0,
            "runtime_expert_choice_count": 0,
            "stale_owner_rate": null,
            "step": 75,
            "top2_execution_count": 0,
            "top4_execution_count": 0
          }
        ],
        "slice_summary": {
          "broad_lm": {
            "max_loss": 12.159866333007812,
            "mean_loss": 2.824210923165083,
            "min_loss": 2.3216283321380615,
            "window_count": 64
          },
          "code_heavy": {
            "max_loss": 13.306273460388184,
            "mean_loss": 10.372926354408264,
            "min_loss": 7.083217144012451,
            "window_count": 4
          },
          "gutenberg_prose": {
            "max_loss": 12.159866333007812,
            "mean_loss": 2.824210923165083,
            "min_loss": 2.3216283321380615,
            "window_count": 64
          },
          "humaneval_like_heldout": {
            "max_loss": 13.306273460388184,
            "mean_loss": 10.372926354408264,
            "min_loss": 7.083217144012451,
            "window_count": 4
          },
          "json_schema": {
            "max_loss": 11.232419967651367,
            "mean_loss": 10.401772260665894,
            "min_loss": 9.930900573730469,
            "window_count": 4
          },
          "unseen_structured_spans": {
            "max_loss": 13.306273460388184,
            "mean_loss": 10.387349307537079,
            "min_loss": 7.083217144012451,
            "window_count": 8
          }
        },
        "top1_invariants_clean": true
      },
      "best_gate": {
        "accepted": true,
        "broad_delta_vs_base": -0.06232965737581253,
        "broad_limit": 2.8542109231650827,
        "broad_lm": 2.7618812657892704,
        "reason": "retention_gate_passed",
        "step": 100,
        "structured_delta_vs_base": -2.586464762687683,
        "structured_unseen": 7.800884544849396
      },
      "best_step": 100,
      "checkpoint_path": "checkpoints/retention_replay_cross_architecture_control_seed_42/pvr_baseline_300m/checkpoint.pt",
      "elapsed_seconds": 93.23450040817261,
      "family": "pvr_ec_o",
      "gate_curve": [
        {
          "accepted": true,
          "broad_delta_vs_base": -0.047276560217142105,
          "broad_limit": 2.8542109231650827,
          "broad_lm": 2.776934362947941,
          "step": 10,
          "structured_delta_vs_base": -1.2223522067070007,
          "structured_unseen": 9.164997100830078
        },
        {
          "accepted": false,
          "broad_delta_vs_base": 0.034792497754096985,
          "broad_limit": 2.8542109231650827,
          "broad_lm": 2.85900342091918,
          "step": 20,
          "structured_delta_vs_base": -1.5874683260917664,
          "structured_unseen": 8.799880981445312
        },
        {
          "accepted": true,
          "broad_delta_vs_base": -0.02721676602959633,
          "broad_limit": 2.8542109231650827,
          "broad_lm": 2.7969941571354866,
          "step": 30,
          "structured_delta_vs_base": -1.6555017232894897,
          "structured_unseen": 8.731847584247589
        },
        {
          "accepted": false,
          "broad_delta_vs_base": -0.024393796920776367,
          "broad_limit": 2.8542109231650827,
          "broad_lm": 2.7998171262443066,
          "step": 40,
          "structured_delta_vs_base": -1.5600181221961975,
          "structured_unseen": 8.827331185340881
        },
        {
          "accepted": true,
          "broad_delta_vs_base": -0.08826158195734024,
          "broad_limit": 2.8542109231650827,
          "broad_lm": 2.7359493412077427,
          "step": 50,
          "structured_delta_vs_base": -1.6764621138572693,
          "structured_unseen": 8.71088719367981
        },
        {
          "accepted": true,
          "broad_delta_vs_base": -0.04956473410129547,
          "broad_limit": 2.8542109231650827,
          "broad_lm": 2.7746461890637875,
          "step": 60,
          "structured_delta_vs_base": -1.7822410464286804,
          "structured_unseen": 8.605108261108398
        },
        {
          "accepted": true,
          "broad_delta_vs_base": -0.06218794733285904,
          "broad_limit": 2.8542109231650827,
          "broad_lm": 2.762022975832224,
          "step": 70,
          "structured_delta_vs_base": -1.9772855639457703,
          "structured_unseen": 8.410063743591309
        },
        {
          "accepted": true,
          "broad_delta_vs_base": -0.0853903777897358,
          "broad_limit": 2.8542109231650827,
          "broad_lm": 2.738820545375347,
          "step": 80,
          "structured_delta_vs_base": -2.083505153656006,
          "structured_unseen": 8.303844153881073
        },
        {
          "accepted": true,
          "broad_delta_vs_base": -0.04260174185037613,
          "broad_limit": 2.8542109231650827,
          "broad_lm": 2.781609181314707,
          "step": 90,
          "structured_delta_vs_base": -2.334336042404175,
          "structured_unseen": 8.053013265132904
        },
        {
          "accepted": true,
          "broad_delta_vs_base": -0.06232965737581253,
          "broad_limit": 2.8542109231650827,
          "broad_lm": 2.7618812657892704,
          "step": 100,
          "structured_delta_vs_base": -2.586464762687683,
          "structured_unseen": 7.800884544849396
        }
      ],
      "key": "pvr_baseline_300m",
      "parameter_counts": {
        "dense_all": 0,
        "expert": 81632064,
        "frozen": 202928848,
        "router": 196608,
        "trunk": 0
      },
      "training_curve": [
        {
          "loss": 11.998953819274902,
          "retention_loss": 2.729537010192871,
          "step": 1,
          "structured_loss": 6.53987979888916
        },
        {
          "loss": 9.9298095703125,
          "retention_loss": 2.6124627590179443,
          "step": 2,
          "structured_loss": 4.704883575439453
        },
        {
          "loss": 12.793111801147461,
          "retention_loss": 2.557802438735962,
          "step": 3,
          "structured_loss": 7.677507400512695
        },
        {
          "loss": 10.631080627441406,
          "retention_loss": 3.121786117553711,
          "step": 4,
          "structured_loss": 4.387508869171143
        },
        {
          "loss": 17.27695083618164,
          "retention_loss": 2.791315793991089,
          "step": 5,
          "structured_loss": 11.694318771362305
        },
        {
          "loss": 12.016447067260742,
          "retention_loss": 2.7537243366241455,
          "step": 6,
          "structured_loss": 6.508998394012451
        },
        {
          "loss": 13.375574111938477,
          "retention_loss": 2.9499332904815674,
          "step": 7,
          "structured_loss": 7.4757080078125
        },
        {
          "loss": 17.939390182495117,
          "retention_loss": 2.693248748779297,
          "step": 8,
          "structured_loss": 12.552892684936523
        },
        {
          "loss": 21.980276107788086,
          "retention_loss": 2.637946844100952,
          "step": 9,
          "structured_loss": 16.704381942749023
        },
        {
          "loss": 17.249610900878906,
          "retention_loss": 2.8048908710479736,
          "step": 10,
          "structured_loss": 11.639829635620117
        },
        {
          "loss": 13.004497528076172,
          "retention_loss": 2.4927542209625244,
          "step": 11,
          "structured_loss": 8.018988609313965
        },
        {
          "loss": 14.180976867675781,
          "retention_loss": 2.565187454223633,
          "step": 12,
          "structured_loss": 9.050601959228516
        },
        {
          "loss": 13.405293464660645,
          "retention_loss": 2.670626640319824,
          "step": 13,
          "structured_loss": 8.064040184020996
        },
        {
          "loss": 12.50393295288086,
          "retention_loss": 2.586134672164917,
          "step": 14,
          "structured_loss": 7.331663608551025
        },
        {
          "loss": 13.078584671020508,
          "retention_loss": 2.5317108631134033,
          "step": 15,
          "structured_loss": 8.01516342163086
        },
        {
          "loss": 14.507429122924805,
          "retention_loss": 2.547325372695923,
          "step": 16,
          "structured_loss": 9.412778854370117
        },
        {
          "loss": 10.576478958129883,
          "retention_loss": 2.395127296447754,
          "step": 17,
          "structured_loss": 5.786224842071533
        },
        {
          "loss": 11.78425407409668,
          "retention_loss": 2.6226208209991455,
          "step": 18,
          "structured_loss": 6.5390119552612305
        },
        {
          "loss": 16.091867446899414,
          "retention_loss": 2.57088303565979,
          "step": 19,
          "structured_loss": 10.950100898742676
        },
        {
          "loss": 14.29167652130127,
          "retention_loss": 2.7960710525512695,
          "step": 20,
          "structured_loss": 8.69953441619873
        },
        {
          "loss": 10.368537902832031,
          "retention_loss": 2.4656431674957275,
          "step": 21,
          "structured_loss": 5.437251567840576
        },
        {
          "loss": 14.841320991516113,
          "retention_loss": 2.519245147705078,
          "step": 22,
          "structured_loss": 9.802830696105957
        },
        {
          "loss": 11.302689552307129,
          "retention_loss": 2.4920477867126465,
          "step": 23,
          "structured_loss": 6.318593978881836
        },
        {
          "loss": 11.308860778808594,
          "retention_loss": 2.4955179691314697,
          "step": 24,
          "structured_loss": 6.3178253173828125
        },
        {
          "loss": 15.445829391479492,
          "retention_loss": 2.467820167541504,
          "step": 25,
          "structured_loss": 10.510189056396484
        },
        {
          "loss": 13.067302703857422,
          "retention_loss": 2.600208044052124,
          "step": 26,
          "structured_loss": 7.866886615753174
        },
        {
          "loss": 11.423053741455078,
          "retention_loss": 2.5752062797546387,
          "step": 27,
          "structured_loss": 6.272641181945801
        },
        {
          "loss": 20.408279418945312,
          "retention_loss": 2.6713380813598633,
          "step": 28,
          "structured_loss": 15.065603256225586
        },
        {
          "loss": 12.811677932739258,
          "retention_loss": 2.5344598293304443,
          "step": 29,
          "structured_loss": 7.742758750915527
        },
        {
          "loss": 12.161578178405762,
          "retention_loss": 2.6295042037963867,
          "step": 30,
          "structured_loss": 6.902569770812988
        },
        {
          "loss": 16.194377899169922,
          "retention_loss": 3.2738037109375,
          "step": 31,
          "structured_loss": 9.646770477294922
        },
        {
          "loss": 11.804426193237305,
          "retention_loss": 2.5677852630615234,
          "step": 32,
          "structured_loss": 6.668855667114258
        },
        {
          "loss": 11.558294296264648,
          "retention_loss": 3.0939133167266846,
          "step": 33,
          "structured_loss": 5.370467662811279
        },
        {
          "loss": 11.755160331726074,
          "retention_loss": 2.7972347736358643,
          "step": 34,
          "structured_loss": 6.160690784454346
        },
        {
          "loss": 10.845726013183594,
          "retention_loss": 2.668048858642578,
          "step": 35,
          "structured_loss": 5.509628772735596
        },
        {
          "loss": 12.068429946899414,
          "retention_loss": 2.6866824626922607,
          "step": 36,
          "structured_loss": 6.695064544677734
        },
        {
          "loss": 9.510223388671875,
          "retention_loss": 2.482191801071167,
          "step": 37,
          "structured_loss": 4.545839309692383
        },
        {
          "loss": 9.898600578308105,
          "retention_loss": 2.7044451236724854,
          "step": 38,
          "structured_loss": 4.489710330963135
        },
        {
          "loss": 10.384785652160645,
          "retention_loss": 2.714421510696411,
          "step": 39,
          "structured_loss": 4.955942630767822
        },
        {
          "loss": 16.955459594726562,
          "retention_loss": 2.404468059539795,
          "step": 40,
          "structured_loss": 12.146522521972656
        },
        {
          "loss": 10.833126068115234,
          "retention_loss": 2.5958738327026367,
          "step": 41,
          "structured_loss": 5.641378879547119
        },
        {
          "loss": 11.806642532348633,
          "retention_loss": 2.4820985794067383,
          "step": 42,
          "structured_loss": 6.842444896697998
        },
        {
          "loss": 14.504603385925293,
          "retention_loss": 2.4701342582702637,
          "step": 43,
          "structured_loss": 9.564334869384766
        },
        {
          "loss": 14.0984468460083,
          "retention_loss": 2.596588134765625,
          "step": 44,
          "structured_loss": 8.90527057647705
        },
        {
          "loss": 9.982047080993652,
          "retention_loss": 2.63032603263855,
          "step": 45,
          "structured_loss": 4.721395015716553
        },
        {
          "loss": 10.419218063354492,
          "retention_loss": 2.376828670501709,
          "step": 46,
          "structured_loss": 5.665560245513916
        },
        {
          "loss": 17.120689392089844,
          "retention_loss": 2.430652618408203,
          "step": 47,
          "structured_loss": 12.259385108947754
        },
        {
          "loss": 18.372390747070312,
          "retention_loss": 2.5511887073516846,
          "step": 48,
          "structured_loss": 13.270012855529785
        },
        {
          "loss": 13.674689292907715,
          "retention_loss": 2.612072467803955,
          "step": 49,
          "structured_loss": 8.450544357299805
        },
        {
          "loss": 21.56047821044922,
          "retention_loss": 2.394777774810791,
          "step": 50,
          "structured_loss": 16.770923614501953
        },
        {
          "loss": 12.826059341430664,
          "retention_loss": 2.38318133354187,
          "step": 51,
          "structured_loss": 8.059697151184082
        },
        {
          "loss": 13.740452766418457,
          "retention_loss": 2.5662970542907715,
          "step": 52,
          "structured_loss": 8.607858657836914
        },
        {
          "loss": 19.686172485351562,
          "retention_loss": 2.33241868019104,
          "step": 53,
          "structured_loss": 15.02133560180664
        },
        {
          "loss": 14.185567855834961,
          "retention_loss": 2.4611194133758545,
          "step": 54,
          "structured_loss": 9.26332950592041
        },
        {
          "loss": 12.06217098236084,
          "retention_loss": 2.3910439014434814,
          "step": 55,
          "structured_loss": 7.280083179473877
        },
        {
          "loss": 15.968570709228516,
          "retention_loss": 2.4167520999908447,
          "step": 56,
          "structured_loss": 11.135066986083984
        },
        {
          "loss": 28.437538146972656,
          "retention_loss": 2.4935405254364014,
          "step": 57,
          "structured_loss": 23.450456619262695
        },
        {
          "loss": 14.386061668395996,
          "retention_loss": 2.4338183403015137,
          "step": 58,
          "structured_loss": 9.518424987792969
        },
        {
          "loss": 18.20987892150879,
          "retention_loss": 2.4674434661865234,
          "step": 59,
          "structured_loss": 13.274991989135742
        },
        {
          "loss": 17.61709213256836,
          "retention_loss": 2.5423741340637207,
          "step": 60,
          "structured_loss": 12.532344818115234
        },
        {
          "loss": 26.342910766601562,
          "retention_loss": 3.0907845497131348,
          "step": 61,
          "structured_loss": 20.16134262084961
        },
        {
          "loss": 23.243438720703125,
          "retention_loss": 2.6169075965881348,
          "step": 62,
          "structured_loss": 18.00962257385254
        },
        {
          "loss": 10.987485885620117,
          "retention_loss": 2.649649143218994,
          "step": 63,
          "structured_loss": 5.688187122344971
        },
        {
          "loss": 15.707231521606445,
          "retention_loss": 2.144648790359497,
          "step": 64,
          "structured_loss": 11.417933464050293
        },
        {
          "loss": 15.05235481262207,
          "retention_loss": 2.411571741104126,
          "step": 65,
          "structured_loss": 10.229211807250977
        },
        {
          "loss": 14.655808448791504,
          "retention_loss": 2.354386806488037,
          "step": 66,
          "structured_loss": 9.94703483581543
        },
        {
          "loss": 24.72844886779785,
          "retention_loss": 2.525675058364868,
          "step": 67,
          "structured_loss": 19.677099227905273
        },
        {
          "loss": 25.560646057128906,
          "retention_loss": 2.307129383087158,
          "step": 68,
          "structured_loss": 20.946388244628906
        },
        {
          "loss": 11.003067016601562,
          "retention_loss": 2.615938186645508,
          "step": 69,
          "structured_loss": 5.771190166473389
        },
        {
          "loss": 22.27838134765625,
          "retention_loss": 2.7769508361816406,
          "step": 70,
          "structured_loss": 16.72447967529297
        },
        {
          "loss": 18.998157501220703,
          "retention_loss": 2.426670551300049,
          "step": 71,
          "structured_loss": 14.144815444946289
        },
        {
          "loss": 9.221967697143555,
          "retention_loss": 2.4703285694122314,
          "step": 72,
          "structured_loss": 4.281310081481934
        },
        {
          "loss": 16.526243209838867,
          "retention_loss": 2.2744176387786865,
          "step": 73,
          "structured_loss": 11.977407455444336
        },
        {
          "loss": 19.800996780395508,
          "retention_loss": 2.57364559173584,
          "step": 74,
          "structured_loss": 14.653705596923828
        },
        {
          "loss": 18.209247589111328,
          "retention_loss": 2.398592948913574,
          "step": 75,
          "structured_loss": 13.412060737609863
        },
        {
          "loss": 11.3342924118042,
          "retention_loss": 2.393627643585205,
          "step": 76,
          "structured_loss": 6.547037124633789
        },
        {
          "loss": 16.674610137939453,
          "retention_loss": 2.487121105194092,
          "step": 77,
          "structured_loss": 11.700368881225586
        },
        {
          "loss": 19.665189743041992,
          "retention_loss": 2.385974884033203,
          "step": 78,
          "structured_loss": 14.893239974975586
        },
        {
          "loss": 22.342655181884766,
          "retention_loss": 2.3276329040527344,
          "step": 79,
          "structured_loss": 17.687389373779297
        },
        {
          "loss": 17.44390296936035,
          "retention_loss": 2.2095654010772705,
          "step": 80,
          "structured_loss": 13.024771690368652
        },
        {
          "loss": 14.164445877075195,
          "retention_loss": 2.3984270095825195,
          "step": 81,
          "structured_loss": 9.367591857910156
        },
        {
          "loss": 22.804473876953125,
          "retention_loss": 2.4835171699523926,
          "step": 82,
          "structured_loss": 17.837440490722656
        },
        {
          "loss": 12.185158729553223,
          "retention_loss": 2.6390302181243896,
          "step": 83,
          "structured_loss": 6.907098293304443
        },
        {
          "loss": 15.130810737609863,
          "retention_loss": 2.5369787216186523,
          "step": 84,
          "structured_loss": 10.056853294372559
        },
        {
          "loss": 14.367345809936523,
          "retention_loss": 2.738065719604492,
          "step": 85,
          "structured_loss": 8.891214370727539
        },
        {
          "loss": 19.641403198242188,
          "retention_loss": 2.856412887573242,
          "step": 86,
          "structured_loss": 13.928577423095703
        },
        {
          "loss": 20.089378356933594,
          "retention_loss": 2.791879892349243,
          "step": 87,
          "structured_loss": 14.505619049072266
        },
        {
          "loss": 21.338241577148438,
          "retention_loss": 2.9103057384490967,
          "step": 88,
          "structured_loss": 15.517629623413086
        },
        {
          "loss": 18.80853271484375,
          "retention_loss": 2.554731845855713,
          "step": 89,
          "structured_loss": 13.699068069458008
        },
        {
          "loss": 30.286455154418945,
          "retention_loss": 2.36977481842041,
          "step": 90,
          "structured_loss": 25.546905517578125
        },
        {
          "loss": 20.686813354492188,
          "retention_loss": 2.400217294692993,
          "step": 91,
          "structured_loss": 15.886378288269043
        },
        {
          "loss": 14.416316986083984,
          "retention_loss": 2.3905320167541504,
          "step": 92,
          "structured_loss": 9.635252952575684
        },
        {
          "loss": 17.240530014038086,
          "retention_loss": 2.553112745285034,
          "step": 93,
          "structured_loss": 12.13430404663086
        },
        {
          "loss": 22.65121078491211,
          "retention_loss": 2.419408082962036,
          "step": 94,
          "structured_loss": 17.812395095825195
        },
        {
          "loss": 14.080090522766113,
          "retention_loss": 2.346676826477051,
          "step": 95,
          "structured_loss": 9.386736869812012
        },
        {
          "loss": 15.917638778686523,
          "retention_loss": 2.4291839599609375,
          "step": 96,
          "structured_loss": 11.059270858764648
        },
        {
          "loss": 16.289627075195312,
          "retention_loss": 2.3194339275360107,
          "step": 97,
          "structured_loss": 11.65075969696045
        },
        {
          "loss": 21.09379005432129,
          "retention_loss": 2.3591842651367188,
          "step": 98,
          "structured_loss": 16.37542152404785
        },
        {
          "loss": 13.281627655029297,
          "retention_loss": 2.3745920658111572,
          "step": 99,
          "structured_loss": 8.532443046569824
        },
        {
          "loss": 12.237171173095703,
          "retention_loss": 2.3789145946502686,
          "step": 100,
          "structured_loss": 7.479341983795166
        }
      ]
    },
    "pvr_ean_300m": {
      "adapted_config": "benchmark/reports/generated/retention_replay_cross_architecture_control_seed_42/pvr_ean_300m/adapted_config.json",
      "adapted_row": {
        "active_flops_estimate": 630000000,
        "active_params_per_token": 105000000,
        "checkpoint_path": "checkpoints/retention_replay_cross_architecture_control_seed_42/pvr_ean_300m/checkpoint.pt",
        "model_family": "pvr_ec_o",
        "model_variant": "pvr_ec_o_full_300m_shared_trunk_init_v1_scope_embeddings_attention_norms_seed_42_retention_replay_control_seed_42",
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
        "slice_summary": {
          "broad_lm": {
            "max_loss": 6.863420009613037,
            "mean_loss": 2.571919046342373,
            "min_loss": 2.273947238922119,
            "window_count": 64
          },
          "code_heavy": {
            "max_loss": 14.813945770263672,
            "mean_loss": 11.644206404685974,
            "min_loss": 6.976099491119385,
            "window_count": 4
          },
          "gutenberg_prose": {
            "max_loss": 6.863420009613037,
            "mean_loss": 2.571919046342373,
            "min_loss": 2.273947238922119,
            "window_count": 64
          },
          "humaneval_like_heldout": {
            "max_loss": 14.813945770263672,
            "mean_loss": 11.644206404685974,
            "min_loss": 6.976099491119385,
            "window_count": 4
          },
          "json_schema": {
            "max_loss": 13.323134422302246,
            "mean_loss": 10.820296287536621,
            "min_loss": 9.668989181518555,
            "window_count": 4
          },
          "unseen_structured_spans": {
            "max_loss": 14.813945770263672,
            "mean_loss": 11.232251346111298,
            "min_loss": 6.976099491119385,
            "window_count": 8
          }
        },
        "top1_invariants_clean": true
      },
      "base_config": "benchmark/reports/generated/ean_init_300m_repeat_seed_42/pvr_ec_o_full_300m_shared_trunk_init_v1_scope_embeddings_attention_norms_seed_42/run_config.yaml",
      "base_row": {
        "active_flops_estimate": 630000000,
        "active_params_per_token": 105000000,
        "checkpoint_path": "checkpoints/ean_init_300m_repeat_seed_42/pvr_ec_o_full_300m_shared_trunk_init_v1_scope_embeddings_attention_norms_seed_42/checkpoint.pt",
        "model_family": "pvr_ec_o",
        "model_variant": "pvr_ec_o_full_300m_shared_trunk_init_v1_scope_embeddings_attention_norms_seed_42",
        "routing_snapshots": [
          {
            "challenger_disagreement_rate": null,
            "descriptor_control_margin": 0.5172737978258132,
            "expert_utilization": [
              360,
              274,
              487,
              602,
              243,
              406,
              348,
              352
            ],
            "failure_mode_distribution": {},
            "high_gap_monopoly_rate": 0.19596354166666666,
            "operator_control_margin": 0.5172737978258132,
            "owner_churn": null,
            "owner_entropy": 2.0412845783848734,
            "owners_per_token": 1.0,
            "production_map_mutated": false,
            "prototype_entropy": 2.0412845783848734,
            "prototype_margin": 0.5172737978258132,
            "prototype_monopoly_rate": 0.19596354166666666,
            "runtime_dynamic_k_count": 0,
            "runtime_expert_choice_count": 0,
            "stale_owner_rate": null,
            "step": 0,
            "top2_execution_count": 0,
            "top4_execution_count": 0
          },
          {
            "challenger_disagreement_rate": null,
            "descriptor_control_margin": 0.5109380982272947,
            "expert_utilization": [
              313,
              353,
              509,
              665,
              219,
              411,
              280,
              322
            ],
            "failure_mode_distribution": {},
            "high_gap_monopoly_rate": 0.21647135416666666,
            "operator_control_margin": 0.5109380982272947,
            "owner_churn": null,
            "owner_entropy": 2.0225663690926488,
            "owners_per_token": 1.0,
            "production_map_mutated": false,
            "prototype_entropy": 2.0225663690926488,
            "prototype_margin": 0.5109380982272947,
            "prototype_monopoly_rate": 0.21647135416666666,
            "runtime_dynamic_k_count": 0,
            "runtime_expert_choice_count": 0,
            "stale_owner_rate": null,
            "step": 25,
            "top2_execution_count": 0,
            "top4_execution_count": 0
          },
          {
            "challenger_disagreement_rate": null,
            "descriptor_control_margin": 0.5111386253023132,
            "expert_utilization": [
              295,
              323,
              503,
              702,
              235,
              421,
              278,
              315
            ],
            "failure_mode_distribution": {},
            "high_gap_monopoly_rate": 0.228515625,
            "operator_control_margin": 0.5111386253023132,
            "owner_churn": null,
            "owner_entropy": 2.01538760815178,
            "owners_per_token": 1.0,
            "production_map_mutated": false,
            "prototype_entropy": 2.01538760815178,
            "prototype_margin": 0.5111386253023132,
            "prototype_monopoly_rate": 0.228515625,
            "runtime_dynamic_k_count": 0,
            "runtime_expert_choice_count": 0,
            "stale_owner_rate": null,
            "step": 50,
            "top2_execution_count": 0,
            "top4_execution_count": 0
          },
          {
            "challenger_disagreement_rate": null,
            "descriptor_control_margin": 0.5051761796882298,
            "expert_utilization": [
              391,
              276,
              527,
              609,
              242,
              373,
              332,
              322
            ],
            "failure_mode_distribution": {},
            "high_gap_monopoly_rate": 0.1982421875,
            "operator_control_margin": 0.5051761796882298,
            "owner_churn": null,
            "owner_entropy": 2.0351656708914323,
            "owners_per_token": 1.0,
            "production_map_mutated": false,
            "prototype_entropy": 2.0351656708914323,
            "prototype_margin": 0.5051761796882298,
            "prototype_monopoly_rate": 0.1982421875,
            "runtime_dynamic_k_count": 0,
            "runtime_expert_choice_count": 0,
            "stale_owner_rate": null,
            "step": 75,
            "top2_execution_count": 0,
            "top4_execution_count": 0
          }
        ],
        "slice_summary": {
          "broad_lm": {
            "max_loss": 7.311913013458252,
            "mean_loss": 2.595274433493614,
            "min_loss": 2.263871908187866,
            "window_count": 64
          },
          "code_heavy": {
            "max_loss": 16.904939651489258,
            "mean_loss": 12.958750128746033,
            "min_loss": 7.81622838973999,
            "window_count": 4
          },
          "gutenberg_prose": {
            "max_loss": 7.311913013458252,
            "mean_loss": 2.595274433493614,
            "min_loss": 2.263871908187866,
            "window_count": 64
          },
          "humaneval_like_heldout": {
            "max_loss": 16.904939651489258,
            "mean_loss": 12.958750128746033,
            "min_loss": 7.81622838973999,
            "window_count": 4
          },
          "json_schema": {
            "max_loss": 15.211018562316895,
            "mean_loss": 12.983597993850708,
            "min_loss": 12.034255027770996,
            "window_count": 4
          },
          "unseen_structured_spans": {
            "max_loss": 16.904939651489258,
            "mean_loss": 12.97117406129837,
            "min_loss": 7.81622838973999,
            "window_count": 8
          }
        },
        "top1_invariants_clean": true
      },
      "best_gate": {
        "accepted": true,
        "broad_delta_vs_base": -0.023355387151241302,
        "broad_limit": 2.625274433493614,
        "broad_lm": 2.571919046342373,
        "reason": "retention_gate_passed",
        "step": 100,
        "structured_delta_vs_base": -1.7389227151870728,
        "structured_unseen": 11.232251346111298
      },
      "best_step": 100,
      "checkpoint_path": "checkpoints/retention_replay_cross_architecture_control_seed_42/pvr_ean_300m/checkpoint.pt",
      "elapsed_seconds": 85.26003527641296,
      "family": "pvr_ec_o",
      "gate_curve": [
        {
          "accepted": true,
          "broad_delta_vs_base": 0.010610491037368774,
          "broad_limit": 2.625274433493614,
          "broad_lm": 2.605884924530983,
          "step": 10,
          "structured_delta_vs_base": -0.8168269395828247,
          "structured_unseen": 12.154347121715546
        },
        {
          "accepted": true,
          "broad_delta_vs_base": -0.02459278702735901,
          "broad_limit": 2.625274433493614,
          "broad_lm": 2.570681646466255,
          "step": 20,
          "structured_delta_vs_base": -1.143365204334259,
          "structured_unseen": 11.827808856964111
        },
        {
          "accepted": true,
          "broad_delta_vs_base": -0.018382050096988678,
          "broad_limit": 2.625274433493614,
          "broad_lm": 2.5768923833966255,
          "step": 30,
          "structured_delta_vs_base": -1.2706230878829956,
          "structured_unseen": 11.700550973415375
        },
        {
          "accepted": true,
          "broad_delta_vs_base": 0.0032692179083824158,
          "broad_limit": 2.625274433493614,
          "broad_lm": 2.5985436514019966,
          "step": 40,
          "structured_delta_vs_base": -1.300184726715088,
          "structured_unseen": 11.670989334583282
        },
        {
          "accepted": true,
          "broad_delta_vs_base": -0.007941212505102158,
          "broad_limit": 2.625274433493614,
          "broad_lm": 2.587333220988512,
          "step": 50,
          "structured_delta_vs_base": -1.3612546920776367,
          "structured_unseen": 11.609919369220734
        },
        {
          "accepted": true,
          "broad_delta_vs_base": -0.007302585989236832,
          "broad_limit": 2.625274433493614,
          "broad_lm": 2.5879718475043774,
          "step": 60,
          "structured_delta_vs_base": -1.4109246134757996,
          "structured_unseen": 11.56024944782257
        },
        {
          "accepted": true,
          "broad_delta_vs_base": -0.025155480951070786,
          "broad_limit": 2.625274433493614,
          "broad_lm": 2.5701189525425434,
          "step": 70,
          "structured_delta_vs_base": -1.4599303603172302,
          "structured_unseen": 11.51124370098114
        },
        {
          "accepted": true,
          "broad_delta_vs_base": -0.028540417551994324,
          "broad_limit": 2.625274433493614,
          "broad_lm": 2.56673401594162,
          "step": 80,
          "structured_delta_vs_base": -1.5017138123512268,
          "structured_unseen": 11.469460248947144
        },
        {
          "accepted": true,
          "broad_delta_vs_base": -0.020785152912139893,
          "broad_limit": 2.625274433493614,
          "broad_lm": 2.5744892805814743,
          "step": 90,
          "structured_delta_vs_base": -1.633427381515503,
          "structured_unseen": 11.337746679782867
        },
        {
          "accepted": true,
          "broad_delta_vs_base": -0.023355387151241302,
          "broad_limit": 2.625274433493614,
          "broad_lm": 2.571919046342373,
          "step": 100,
          "structured_delta_vs_base": -1.7389227151870728,
          "structured_unseen": 11.232251346111298
        }
      ],
      "key": "pvr_ean_300m",
      "parameter_counts": {
        "dense_all": 0,
        "expert": 81632064,
        "frozen": 202928848,
        "router": 196608,
        "trunk": 0
      },
      "training_curve": [
        {
          "loss": 11.054584503173828,
          "retention_loss": 2.5979745388031006,
          "step": 1,
          "structured_loss": 5.858635902404785
        },
        {
          "loss": 9.814125061035156,
          "retention_loss": 2.4781596660614014,
          "step": 2,
          "structured_loss": 4.857806205749512
        },
        {
          "loss": 11.201696395874023,
          "retention_loss": 2.476783514022827,
          "step": 3,
          "structured_loss": 6.248129844665527
        },
        {
          "loss": 9.413658142089844,
          "retention_loss": 2.7471306324005127,
          "step": 4,
          "structured_loss": 3.9193971157073975
        },
        {
          "loss": 15.648344039916992,
          "retention_loss": 2.597485303878784,
          "step": 5,
          "structured_loss": 10.453372955322266
        },
        {
          "loss": 10.616622924804688,
          "retention_loss": 2.4953396320343018,
          "step": 6,
          "structured_loss": 5.625943183898926
        },
        {
          "loss": 12.240039825439453,
          "retention_loss": 2.594404697418213,
          "step": 7,
          "structured_loss": 7.051230430603027
        },
        {
          "loss": 16.14777374267578,
          "retention_loss": 2.4894471168518066,
          "step": 8,
          "structured_loss": 11.168878555297852
        },
        {
          "loss": 20.62407875061035,
          "retention_loss": 2.419295310974121,
          "step": 9,
          "structured_loss": 15.78548812866211
        },
        {
          "loss": 13.871898651123047,
          "retention_loss": 2.6350982189178467,
          "step": 10,
          "structured_loss": 8.601701736450195
        },
        {
          "loss": 11.08706283569336,
          "retention_loss": 2.3737847805023193,
          "step": 11,
          "structured_loss": 6.3394927978515625
        },
        {
          "loss": 12.060074806213379,
          "retention_loss": 2.472658157348633,
          "step": 12,
          "structured_loss": 7.114758491516113
        },
        {
          "loss": 11.944389343261719,
          "retention_loss": 2.4912383556365967,
          "step": 13,
          "structured_loss": 6.961912155151367
        },
        {
          "loss": 11.651582717895508,
          "retention_loss": 2.371502637863159,
          "step": 14,
          "structured_loss": 6.9085774421691895
        },
        {
          "loss": 12.21496868133545,
          "retention_loss": 2.3704257011413574,
          "step": 15,
          "structured_loss": 7.474117279052734
        },
        {
          "loss": 12.559356689453125,
          "retention_loss": 2.4283690452575684,
          "step": 16,
          "structured_loss": 7.70261812210083
        },
        {
          "loss": 10.084053039550781,
          "retention_loss": 2.2888801097869873,
          "step": 17,
          "structured_loss": 5.506292819976807
        },
        {
          "loss": 9.800007820129395,
          "retention_loss": 2.3892903327941895,
          "step": 18,
          "structured_loss": 5.021427154541016
        },
        {
          "loss": 12.843116760253906,
          "retention_loss": 2.3021345138549805,
          "step": 19,
          "structured_loss": 8.238847732543945
        },
        {
          "loss": 12.481327056884766,
          "retention_loss": 2.4333488941192627,
          "step": 20,
          "structured_loss": 7.61462926864624
        },
        {
          "loss": 9.179162979125977,
          "retention_loss": 2.2485930919647217,
          "step": 21,
          "structured_loss": 4.681977272033691
        },
        {
          "loss": 12.176679611206055,
          "retention_loss": 2.3575077056884766,
          "step": 22,
          "structured_loss": 7.461663722991943
        },
        {
          "loss": 9.537699699401855,
          "retention_loss": 2.362542152404785,
          "step": 23,
          "structured_loss": 4.812615394592285
        },
        {
          "loss": 10.676451683044434,
          "retention_loss": 2.37298321723938,
          "step": 24,
          "structured_loss": 5.930485248565674
        },
        {
          "loss": 12.308570861816406,
          "retention_loss": 2.3925793170928955,
          "step": 25,
          "structured_loss": 7.523411750793457
        },
        {
          "loss": 11.261850357055664,
          "retention_loss": 2.50002384185791,
          "step": 26,
          "structured_loss": 6.261802673339844
        },
        {
          "loss": 11.804662704467773,
          "retention_loss": 2.523374557495117,
          "step": 27,
          "structured_loss": 6.757914066314697
        },
        {
          "loss": 19.27913475036621,
          "retention_loss": 2.6003646850585938,
          "step": 28,
          "structured_loss": 14.078405380249023
        },
        {
          "loss": 14.968082427978516,
          "retention_loss": 2.2611196041107178,
          "step": 29,
          "structured_loss": 10.445843696594238
        },
        {
          "loss": 15.027971267700195,
          "retention_loss": 2.5325067043304443,
          "step": 30,
          "structured_loss": 9.962957382202148
        },
        {
          "loss": 16.691024780273438,
          "retention_loss": 2.750530242919922,
          "step": 31,
          "structured_loss": 11.18996524810791
        },
        {
          "loss": 11.33270263671875,
          "retention_loss": 2.363318681716919,
          "step": 32,
          "structured_loss": 6.606065273284912
        },
        {
          "loss": 10.646017074584961,
          "retention_loss": 2.646946668624878,
          "step": 33,
          "structured_loss": 5.352124214172363
        },
        {
          "loss": 11.90297794342041,
          "retention_loss": 2.4296185970306396,
          "step": 34,
          "structured_loss": 7.043740749359131
        },
        {
          "loss": 11.084053039550781,
          "retention_loss": 2.4652092456817627,
          "step": 35,
          "structured_loss": 6.153635025024414
        },
        {
          "loss": 12.637392044067383,
          "retention_loss": 2.5261967182159424,
          "step": 36,
          "structured_loss": 7.584999084472656
        },
        {
          "loss": 9.060754776000977,
          "retention_loss": 2.3470284938812256,
          "step": 37,
          "structured_loss": 4.366697788238525
        },
        {
          "loss": 9.262100219726562,
          "retention_loss": 2.478140354156494,
          "step": 38,
          "structured_loss": 4.305819988250732
        },
        {
          "loss": 10.33863353729248,
          "retention_loss": 2.576429605484009,
          "step": 39,
          "structured_loss": 5.185774326324463
        },
        {
          "loss": 16.770938873291016,
          "retention_loss": 2.31868839263916,
          "step": 40,
          "structured_loss": 12.133563041687012
        },
        {
          "loss": 10.342178344726562,
          "retention_loss": 2.4118032455444336,
          "step": 41,
          "structured_loss": 5.518571853637695
        },
        {
          "loss": 10.204947471618652,
          "retention_loss": 2.3515326976776123,
          "step": 42,
          "structured_loss": 5.501882076263428
        },
        {
          "loss": 14.855631828308105,
          "retention_loss": 2.403454303741455,
          "step": 43,
          "structured_loss": 10.048723220825195
        },
        {
          "loss": 13.971563339233398,
          "retention_loss": 2.46956467628479,
          "step": 44,
          "structured_loss": 9.032434463500977
        },
        {
          "loss": 10.285274505615234,
          "retention_loss": 2.493083953857422,
          "step": 45,
          "structured_loss": 5.299106121063232
        },
        {
          "loss": 9.578110694885254,
          "retention_loss": 2.2921483516693115,
          "step": 46,
          "structured_loss": 4.993813991546631
        },
        {
          "loss": 16.266340255737305,
          "retention_loss": 2.2941949367523193,
          "step": 47,
          "structured_loss": 11.677949905395508
        },
        {
          "loss": 17.09323501586914,
          "retention_loss": 2.3916409015655518,
          "step": 48,
          "structured_loss": 12.309952735900879
        },
        {
          "loss": 12.756858825683594,
          "retention_loss": 2.3829240798950195,
          "step": 49,
          "structured_loss": 7.991010665893555
        },
        {
          "loss": 19.732769012451172,
          "retention_loss": 2.315009117126465,
          "step": 50,
          "structured_loss": 15.102749824523926
        },
        {
          "loss": 11.865256309509277,
          "retention_loss": 2.2446186542510986,
          "step": 51,
          "structured_loss": 7.37601900100708
        },
        {
          "loss": 12.900314331054688,
          "retention_loss": 2.3990752696990967,
          "step": 52,
          "structured_loss": 8.102163314819336
        },
        {
          "loss": 18.114017486572266,
          "retention_loss": 2.2301411628723145,
          "step": 53,
          "structured_loss": 13.653735160827637
        },
        {
          "loss": 12.708526611328125,
          "retention_loss": 2.3196661472320557,
          "step": 54,
          "structured_loss": 8.069194793701172
        },
        {
          "loss": 10.465164184570312,
          "retention_loss": 2.3396201133728027,
          "step": 55,
          "structured_loss": 5.785924434661865
        },
        {
          "loss": 17.601959228515625,
          "retention_loss": 2.2895092964172363,
          "step": 56,
          "structured_loss": 13.022941589355469
        },
        {
          "loss": 29.02578353881836,
          "retention_loss": 2.364346981048584,
          "step": 57,
          "structured_loss": 24.297088623046875
        },
        {
          "loss": 15.743856430053711,
          "retention_loss": 2.3013126850128174,
          "step": 58,
          "structured_loss": 11.141231536865234
        },
        {
          "loss": 20.955671310424805,
          "retention_loss": 2.3504257202148438,
          "step": 59,
          "structured_loss": 16.254819869995117
        },
        {
          "loss": 17.701969146728516,
          "retention_loss": 2.45947265625,
          "step": 60,
          "structured_loss": 12.783023834228516
        },
        {
          "loss": 23.2863826751709,
          "retention_loss": 2.619288206100464,
          "step": 61,
          "structured_loss": 18.047805786132812
        },
        {
          "loss": 23.08550453186035,
          "retention_loss": 2.4788825511932373,
          "step": 62,
          "structured_loss": 18.12773895263672
        },
        {
          "loss": 12.333341598510742,
          "retention_loss": 2.488715887069702,
          "step": 63,
          "structured_loss": 7.355910301208496
        },
        {
          "loss": 14.74968147277832,
          "retention_loss": 2.0791988372802734,
          "step": 64,
          "structured_loss": 10.591283798217773
        },
        {
          "loss": 16.114450454711914,
          "retention_loss": 2.348698616027832,
          "step": 65,
          "structured_loss": 11.41705322265625
        },
        {
          "loss": 15.052654266357422,
          "retention_loss": 2.3067445755004883,
          "step": 66,
          "structured_loss": 10.439165115356445
        },
        {
          "loss": 18.062854766845703,
          "retention_loss": 2.472116470336914,
          "step": 67,
          "structured_loss": 13.118620872497559
        },
        {
          "loss": 20.446304321289062,
          "retention_loss": 2.188408851623535,
          "step": 68,
          "structured_loss": 16.069486618041992
        },
        {
          "loss": 11.843482971191406,
          "retention_loss": 2.233771800994873,
          "step": 69,
          "structured_loss": 7.375938892364502
        },
        {
          "loss": 25.663122177124023,
          "retention_loss": 2.3477399349212646,
          "step": 70,
          "structured_loss": 20.967641830444336
        },
        {
          "loss": 23.91151237487793,
          "retention_loss": 2.2454349994659424,
          "step": 71,
          "structured_loss": 19.420642852783203
        },
        {
          "loss": 9.806203842163086,
          "retention_loss": 2.344817638397217,
          "step": 72,
          "structured_loss": 5.1165690422058105
        },
        {
          "loss": 20.26431655883789,
          "retention_loss": 2.1941890716552734,
          "step": 73,
          "structured_loss": 15.875937461853027
        },
        {
          "loss": 19.304861068725586,
          "retention_loss": 2.4127347469329834,
          "step": 74,
          "structured_loss": 14.479392051696777
        },
        {
          "loss": 19.01361656188965,
          "retention_loss": 2.3579609394073486,
          "step": 75,
          "structured_loss": 14.297694206237793
        },
        {
          "loss": 13.420487403869629,
          "retention_loss": 2.305936336517334,
          "step": 76,
          "structured_loss": 8.808614730834961
        },
        {
          "loss": 19.543306350708008,
          "retention_loss": 2.3436367511749268,
          "step": 77,
          "structured_loss": 14.856033325195312
        },
        {
          "loss": 19.485553741455078,
          "retention_loss": 2.2993030548095703,
          "step": 78,
          "structured_loss": 14.886946678161621
        },
        {
          "loss": 26.97398567199707,
          "retention_loss": 2.2753403186798096,
          "step": 79,
          "structured_loss": 22.42330551147461
        },
        {
          "loss": 19.881450653076172,
          "retention_loss": 2.1264681816101074,
          "step": 80,
          "structured_loss": 15.62851333618164
        },
        {
          "loss": 16.805437088012695,
          "retention_loss": 2.2791550159454346,
          "step": 81,
          "structured_loss": 12.247127532958984
        },
        {
          "loss": 20.749935150146484,
          "retention_loss": 2.4059247970581055,
          "step": 82,
          "structured_loss": 15.938085556030273
        },
        {
          "loss": 15.072832107543945,
          "retention_loss": 2.4747493267059326,
          "step": 83,
          "structured_loss": 10.123332977294922
        },
        {
          "loss": 16.73267936706543,
          "retention_loss": 2.372103691101074,
          "step": 84,
          "structured_loss": 11.988471984863281
        },
        {
          "loss": 14.388203620910645,
          "retention_loss": 2.4588584899902344,
          "step": 85,
          "structured_loss": 9.470486640930176
        },
        {
          "loss": 17.955284118652344,
          "retention_loss": 2.4081990718841553,
          "step": 86,
          "structured_loss": 13.138885498046875
        },
        {
          "loss": 18.786033630371094,
          "retention_loss": 2.425689935684204,
          "step": 87,
          "structured_loss": 13.934654235839844
        },
        {
          "loss": 17.104976654052734,
          "retention_loss": 2.4498276710510254,
          "step": 88,
          "structured_loss": 12.205322265625
        },
        {
          "loss": 21.653823852539062,
          "retention_loss": 2.3918492794036865,
          "step": 89,
          "structured_loss": 16.87012481689453
        },
        {
          "loss": 17.163318634033203,
          "retention_loss": 2.253723382949829,
          "step": 90,
          "structured_loss": 12.655871391296387
        },
        {
          "loss": 19.833703994750977,
          "retention_loss": 2.2486016750335693,
          "step": 91,
          "structured_loss": 15.33650016784668
        },
        {
          "loss": 16.343536376953125,
          "retention_loss": 2.275059223175049,
          "step": 92,
          "structured_loss": 11.793416976928711
        },
        {
          "loss": 19.298254013061523,
          "retention_loss": 2.4224209785461426,
          "step": 93,
          "structured_loss": 14.453412055969238
        },
        {
          "loss": 20.731409072875977,
          "retention_loss": 2.3819777965545654,
          "step": 94,
          "structured_loss": 15.967453956604004
        },
        {
          "loss": 17.610305786132812,
          "retention_loss": 2.2417421340942383,
          "step": 95,
          "structured_loss": 13.126822471618652
        },
        {
          "loss": 19.315345764160156,
          "retention_loss": 2.3118293285369873,
          "step": 96,
          "structured_loss": 14.69168758392334
        },
        {
          "loss": 17.198707580566406,
          "retention_loss": 2.2224223613739014,
          "step": 97,
          "structured_loss": 12.753862380981445
        },
        {
          "loss": 21.358749389648438,
          "retention_loss": 2.35646653175354,
          "step": 98,
          "structured_loss": 16.645816802978516
        },
        {
          "loss": 17.580045700073242,
          "retention_loss": 2.2902374267578125,
          "step": 99,
          "structured_loss": 12.999570846557617
        },
        {
          "loss": 11.55847454071045,
          "retention_loss": 2.239574909210205,
          "step": 100,
          "structured_loss": 7.079324722290039
        }
      ]
    },
    "switch_top1_300m": {
      "adapted_config": "benchmark/reports/generated/retention_replay_cross_architecture_control_seed_42/switch_top1_300m/adapted_config.json",
      "adapted_row": {
        "active_flops_estimate": 630000000,
        "active_params_per_token": 105000000,
        "checkpoint_path": "checkpoints/retention_replay_cross_architecture_control_seed_42/switch_top1_300m/checkpoint.pt",
        "model_family": "vanilla_switch_top1_reference",
        "model_variant": "vanilla_switch_top1_reference_300m_retention_replay_control_seed_42",
        "routing_snapshots": [],
        "slice_summary": {
          "broad_lm": {
            "max_loss": 12.29637336730957,
            "mean_loss": 2.7434254623949528,
            "min_loss": 2.355579376220703,
            "window_count": 64
          },
          "code_heavy": {
            "max_loss": 13.154718399047852,
            "mean_loss": 11.336118459701538,
            "min_loss": 8.234943389892578,
            "window_count": 4
          },
          "gutenberg_prose": {
            "max_loss": 12.29637336730957,
            "mean_loss": 2.7434254623949528,
            "min_loss": 2.355579376220703,
            "window_count": 64
          },
          "humaneval_like_heldout": {
            "max_loss": 13.154718399047852,
            "mean_loss": 11.336118459701538,
            "min_loss": 8.234943389892578,
            "window_count": 4
          },
          "json_schema": {
            "max_loss": 9.146282196044922,
            "mean_loss": 8.008573293685913,
            "min_loss": 7.370716094970703,
            "window_count": 4
          },
          "unseen_structured_spans": {
            "max_loss": 13.154718399047852,
            "mean_loss": 9.672345876693726,
            "min_loss": 7.370716094970703,
            "window_count": 8
          }
        },
        "top1_invariants_clean": null
      },
      "base_config": "benchmark/reports/generated/training_300m_real_4k/vanilla_switch_top1_reference_300m/run_config.yaml",
      "base_row": {
        "active_flops_estimate": 630000000,
        "active_params_per_token": 105000000,
        "checkpoint_path": "checkpoints/benchmark_300m/vanilla_switch_top1_reference_300m/checkpoint.pt",
        "model_family": "vanilla_switch_top1_reference",
        "model_variant": "vanilla_switch_top1_reference_300m",
        "routing_snapshots": [],
        "slice_summary": {
          "broad_lm": {
            "max_loss": 12.778247833251953,
            "mean_loss": 2.781601406633854,
            "min_loss": 2.336674690246582,
            "window_count": 64
          },
          "code_heavy": {
            "max_loss": 15.58360767364502,
            "mean_loss": 12.925040006637573,
            "min_loss": 9.247726440429688,
            "window_count": 4
          },
          "gutenberg_prose": {
            "max_loss": 12.778247833251953,
            "mean_loss": 2.781601406633854,
            "min_loss": 2.336674690246582,
            "window_count": 64
          },
          "humaneval_like_heldout": {
            "max_loss": 15.58360767364502,
            "mean_loss": 12.925040006637573,
            "min_loss": 9.247726440429688,
            "window_count": 4
          },
          "json_schema": {
            "max_loss": 11.368138313293457,
            "mean_loss": 10.560967445373535,
            "min_loss": 10.17562198638916,
            "window_count": 4
          },
          "unseen_structured_spans": {
            "max_loss": 15.58360767364502,
            "mean_loss": 11.743003726005554,
            "min_loss": 9.247726440429688,
            "window_count": 8
          }
        },
        "top1_invariants_clean": null
      },
      "best_gate": {
        "accepted": true,
        "broad_delta_vs_base": -0.03817594423890114,
        "broad_limit": 2.8116014066338537,
        "broad_lm": 2.7434254623949528,
        "reason": "retention_gate_passed",
        "step": 100,
        "structured_delta_vs_base": -2.0706578493118286,
        "structured_unseen": 9.672345876693726
      },
      "best_step": 100,
      "checkpoint_path": "checkpoints/retention_replay_cross_architecture_control_seed_42/switch_top1_300m/checkpoint.pt",
      "elapsed_seconds": 114.42718195915222,
      "family": "vanilla_switch_top1_reference",
      "gate_curve": [
        {
          "accepted": true,
          "broad_delta_vs_base": 0.008089154958724976,
          "broad_limit": 2.8116014066338537,
          "broad_lm": 2.789690561592579,
          "step": 10,
          "structured_delta_vs_base": -1.0738670825958252,
          "structured_unseen": 10.669136643409729
        },
        {
          "accepted": true,
          "broad_delta_vs_base": 0.019275136291980743,
          "broad_limit": 2.8116014066338537,
          "broad_lm": 2.8008765429258347,
          "step": 20,
          "structured_delta_vs_base": -1.3515996932983398,
          "structured_unseen": 10.391404032707214
        },
        {
          "accepted": true,
          "broad_delta_vs_base": -0.015309758484363556,
          "broad_limit": 2.8116014066338537,
          "broad_lm": 2.7662916481494904,
          "step": 30,
          "structured_delta_vs_base": -1.356917381286621,
          "structured_unseen": 10.386086344718933
        },
        {
          "accepted": true,
          "broad_delta_vs_base": -0.01710069179534912,
          "broad_limit": 2.8116014066338537,
          "broad_lm": 2.764500714838505,
          "step": 40,
          "structured_delta_vs_base": -1.3931129574775696,
          "structured_unseen": 10.349890768527985
        },
        {
          "accepted": true,
          "broad_delta_vs_base": -0.054713960736989975,
          "broad_limit": 2.8116014066338537,
          "broad_lm": 2.726887445896864,
          "step": 50,
          "structured_delta_vs_base": -1.419032871723175,
          "structured_unseen": 10.32397085428238
        },
        {
          "accepted": true,
          "broad_delta_vs_base": -0.02239489182829857,
          "broad_limit": 2.8116014066338537,
          "broad_lm": 2.7592065148055553,
          "step": 60,
          "structured_delta_vs_base": -1.501569151878357,
          "structured_unseen": 10.241434574127197
        },
        {
          "accepted": true,
          "broad_delta_vs_base": -0.03690837323665619,
          "broad_limit": 2.8116014066338537,
          "broad_lm": 2.7446930333971977,
          "step": 70,
          "structured_delta_vs_base": -1.636227011680603,
          "structured_unseen": 10.106776714324951
        },
        {
          "accepted": true,
          "broad_delta_vs_base": -0.057953085750341415,
          "broad_limit": 2.8116014066338537,
          "broad_lm": 2.7236483208835125,
          "step": 80,
          "structured_delta_vs_base": -1.6563823819160461,
          "structured_unseen": 10.086621344089508
        },
        {
          "accepted": true,
          "broad_delta_vs_base": -0.026899810880422592,
          "broad_limit": 2.8116014066338537,
          "broad_lm": 2.7547015957534313,
          "step": 90,
          "structured_delta_vs_base": -1.905606985092163,
          "structured_unseen": 9.837396740913391
        },
        {
          "accepted": true,
          "broad_delta_vs_base": -0.03817594423890114,
          "broad_limit": 2.8116014066338537,
          "broad_lm": 2.7434254623949528,
          "step": 100,
          "structured_delta_vs_base": -2.0706578493118286,
          "structured_unseen": 9.672345876693726
        }
      ],
      "key": "switch_top1_300m",
      "parameter_counts": {
        "dense_all": 0,
        "expert": 91860672,
        "frozen": 168051160,
        "router": 196608,
        "trunk": 0
      },
      "training_curve": [
        {
          "loss": 11.880574226379395,
          "retention_loss": 2.729396104812622,
          "step": 1,
          "structured_loss": 6.42178201675415
        },
        {
          "loss": 10.139164924621582,
          "retention_loss": 2.633699417114258,
          "step": 2,
          "structured_loss": 4.871766090393066
        },
        {
          "loss": 12.133968353271484,
          "retention_loss": 2.5278983116149902,
          "step": 3,
          "structured_loss": 7.078171253204346
        },
        {
          "loss": 11.064409255981445,
          "retention_loss": 3.2739241123199463,
          "step": 4,
          "structured_loss": 4.516561508178711
        },
        {
          "loss": 16.080875396728516,
          "retention_loss": 2.7646684646606445,
          "step": 5,
          "structured_loss": 10.55153751373291
        },
        {
          "loss": 11.363489151000977,
          "retention_loss": 2.6450448036193848,
          "step": 6,
          "structured_loss": 6.073400020599365
        },
        {
          "loss": 12.958139419555664,
          "retention_loss": 2.8270578384399414,
          "step": 7,
          "structured_loss": 7.3040242195129395
        },
        {
          "loss": 16.55657386779785,
          "retention_loss": 2.596989154815674,
          "step": 8,
          "structured_loss": 11.362595558166504
        },
        {
          "loss": 16.640119552612305,
          "retention_loss": 2.5877602100372314,
          "step": 9,
          "structured_loss": 11.464598655700684
        },
        {
          "loss": 17.213085174560547,
          "retention_loss": 2.7701947689056396,
          "step": 10,
          "structured_loss": 11.67269515991211
        },
        {
          "loss": 12.60134220123291,
          "retention_loss": 2.4826278686523438,
          "step": 11,
          "structured_loss": 7.636086463928223
        },
        {
          "loss": 14.380521774291992,
          "retention_loss": 2.5677902698516846,
          "step": 12,
          "structured_loss": 9.244940757751465
        },
        {
          "loss": 13.120929718017578,
          "retention_loss": 2.6533145904541016,
          "step": 13,
          "structured_loss": 7.814300537109375
        },
        {
          "loss": 12.448806762695312,
          "retention_loss": 2.5957255363464355,
          "step": 14,
          "structured_loss": 7.257355213165283
        },
        {
          "loss": 13.311552047729492,
          "retention_loss": 2.484666585922241,
          "step": 15,
          "structured_loss": 8.342219352722168
        },
        {
          "loss": 14.617769241333008,
          "retention_loss": 2.574840545654297,
          "step": 16,
          "structured_loss": 9.468088150024414
        },
        {
          "loss": 10.443269729614258,
          "retention_loss": 2.4337656497955322,
          "step": 17,
          "structured_loss": 5.575738430023193
        },
        {
          "loss": 11.457863807678223,
          "retention_loss": 2.5293920040130615,
          "step": 18,
          "structured_loss": 6.3990797996521
        },
        {
          "loss": 15.505455017089844,
          "retention_loss": 2.4908623695373535,
          "step": 19,
          "structured_loss": 10.523730278015137
        },
        {
          "loss": 13.444452285766602,
          "retention_loss": 2.5926058292388916,
          "step": 20,
          "structured_loss": 8.25924015045166
        },
        {
          "loss": 9.864473342895508,
          "retention_loss": 2.4067513942718506,
          "step": 21,
          "structured_loss": 5.050970554351807
        },
        {
          "loss": 14.997962951660156,
          "retention_loss": 2.597569704055786,
          "step": 22,
          "structured_loss": 9.802823066711426
        },
        {
          "loss": 11.24075698852539,
          "retention_loss": 2.5477054119110107,
          "step": 23,
          "structured_loss": 6.145346641540527
        },
        {
          "loss": 11.481916427612305,
          "retention_loss": 2.609286308288574,
          "step": 24,
          "structured_loss": 6.2633442878723145
        },
        {
          "loss": 15.380096435546875,
          "retention_loss": 2.4875285625457764,
          "step": 25,
          "structured_loss": 10.40503978729248
        },
        {
          "loss": 13.207664489746094,
          "retention_loss": 2.6497066020965576,
          "step": 26,
          "structured_loss": 7.908251762390137
        },
        {
          "loss": 11.618972778320312,
          "retention_loss": 2.553666591644287,
          "step": 27,
          "structured_loss": 6.5116400718688965
        },
        {
          "loss": 18.782955169677734,
          "retention_loss": 2.7517900466918945,
          "step": 28,
          "structured_loss": 13.279375076293945
        },
        {
          "loss": 12.288668632507324,
          "retention_loss": 2.4859447479248047,
          "step": 29,
          "structured_loss": 7.316779136657715
        },
        {
          "loss": 12.289308547973633,
          "retention_loss": 2.7541000843048096,
          "step": 30,
          "structured_loss": 6.781108856201172
        },
        {
          "loss": 18.639759063720703,
          "retention_loss": 3.1252400875091553,
          "step": 31,
          "structured_loss": 12.38927936553955
        },
        {
          "loss": 12.316385269165039,
          "retention_loss": 2.4946279525756836,
          "step": 32,
          "structured_loss": 7.32712984085083
        },
        {
          "loss": 12.576327323913574,
          "retention_loss": 2.9573330879211426,
          "step": 33,
          "structured_loss": 6.661661148071289
        },
        {
          "loss": 14.532453536987305,
          "retention_loss": 2.727766275405884,
          "step": 34,
          "structured_loss": 9.076920509338379
        },
        {
          "loss": 12.804256439208984,
          "retention_loss": 2.5854880809783936,
          "step": 35,
          "structured_loss": 7.633279800415039
        },
        {
          "loss": 14.822221755981445,
          "retention_loss": 2.5992066860198975,
          "step": 36,
          "structured_loss": 9.623808860778809
        },
        {
          "loss": 10.005965232849121,
          "retention_loss": 2.4824368953704834,
          "step": 37,
          "structured_loss": 5.041091442108154
        },
        {
          "loss": 10.171465873718262,
          "retention_loss": 2.6103506088256836,
          "step": 38,
          "structured_loss": 4.9507646560668945
        },
        {
          "loss": 11.624835968017578,
          "retention_loss": 2.639026403427124,
          "step": 39,
          "structured_loss": 6.346782684326172
        },
        {
          "loss": 20.642959594726562,
          "retention_loss": 2.4970550537109375,
          "step": 40,
          "structured_loss": 15.648848533630371
        },
        {
          "loss": 10.603928565979004,
          "retention_loss": 2.502924680709839,
          "step": 41,
          "structured_loss": 5.598079204559326
        },
        {
          "loss": 11.042200088500977,
          "retention_loss": 2.428084135055542,
          "step": 42,
          "structured_loss": 6.186031818389893
        },
        {
          "loss": 15.5581636428833,
          "retention_loss": 2.516953945159912,
          "step": 43,
          "structured_loss": 10.524255752563477
        },
        {
          "loss": 14.881893157958984,
          "retention_loss": 2.5693154335021973,
          "step": 44,
          "structured_loss": 9.74326229095459
        },
        {
          "loss": 10.568119049072266,
          "retention_loss": 2.5324020385742188,
          "step": 45,
          "structured_loss": 5.50331449508667
        },
        {
          "loss": 10.270009994506836,
          "retention_loss": 2.3524599075317383,
          "step": 46,
          "structured_loss": 5.565090656280518
        },
        {
          "loss": 19.2188720703125,
          "retention_loss": 2.4864020347595215,
          "step": 47,
          "structured_loss": 14.246068954467773
        },
        {
          "loss": 19.780136108398438,
          "retention_loss": 2.5071473121643066,
          "step": 48,
          "structured_loss": 14.765840530395508
        },
        {
          "loss": 13.842854499816895,
          "retention_loss": 2.772520065307617,
          "step": 49,
          "structured_loss": 8.29781436920166
        },
        {
          "loss": 24.07654571533203,
          "retention_loss": 2.4954075813293457,
          "step": 50,
          "structured_loss": 19.085731506347656
        },
        {
          "loss": 13.470030784606934,
          "retention_loss": 2.4691076278686523,
          "step": 51,
          "structured_loss": 8.531815528869629
        },
        {
          "loss": 13.406702041625977,
          "retention_loss": 2.5910282135009766,
          "step": 52,
          "structured_loss": 8.224645614624023
        },
        {
          "loss": 23.15557098388672,
          "retention_loss": 2.336293935775757,
          "step": 53,
          "structured_loss": 18.482982635498047
        },
        {
          "loss": 14.365544319152832,
          "retention_loss": 2.4576592445373535,
          "step": 54,
          "structured_loss": 9.450225830078125
        },
        {
          "loss": 11.10405445098877,
          "retention_loss": 2.3760757446289062,
          "step": 55,
          "structured_loss": 6.351902961730957
        },
        {
          "loss": 12.713052749633789,
          "retention_loss": 2.4254560470581055,
          "step": 56,
          "structured_loss": 7.86214017868042
        },
        {
          "loss": 14.784271240234375,
          "retention_loss": 2.462193727493286,
          "step": 57,
          "structured_loss": 9.859883308410645
        },
        {
          "loss": 15.25383186340332,
          "retention_loss": 2.4387011528015137,
          "step": 58,
          "structured_loss": 10.376429557800293
        },
        {
          "loss": 19.020858764648438,
          "retention_loss": 2.412729501724243,
          "step": 59,
          "structured_loss": 14.19540023803711
        },
        {
          "loss": 19.750652313232422,
          "retention_loss": 2.524252414703369,
          "step": 60,
          "structured_loss": 14.702146530151367
        },
        {
          "loss": 24.90380096435547,
          "retention_loss": 3.2841200828552246,
          "step": 61,
          "structured_loss": 18.335559844970703
        },
        {
          "loss": 24.01232147216797,
          "retention_loss": 2.8365602493286133,
          "step": 62,
          "structured_loss": 18.339200973510742
        },
        {
          "loss": 12.370777130126953,
          "retention_loss": 2.6814167499542236,
          "step": 63,
          "structured_loss": 7.007943153381348
        },
        {
          "loss": 17.207111358642578,
          "retention_loss": 2.1718475818634033,
          "step": 64,
          "structured_loss": 12.863415718078613
        },
        {
          "loss": 16.11539649963379,
          "retention_loss": 2.4130022525787354,
          "step": 65,
          "structured_loss": 11.28939151763916
        },
        {
          "loss": 15.65434741973877,
          "retention_loss": 2.4025025367736816,
          "step": 66,
          "structured_loss": 10.849342346191406
        },
        {
          "loss": 25.684768676757812,
          "retention_loss": 2.7186989784240723,
          "step": 67,
          "structured_loss": 20.24736976623535
        },
        {
          "loss": 26.78122901916504,
          "retention_loss": 2.339177131652832,
          "step": 68,
          "structured_loss": 22.102874755859375
        },
        {
          "loss": 12.036896705627441,
          "retention_loss": 2.60070538520813,
          "step": 69,
          "structured_loss": 6.835485935211182
        },
        {
          "loss": 25.10415267944336,
          "retention_loss": 2.74308180809021,
          "step": 70,
          "structured_loss": 19.61798858642578
        },
        {
          "loss": 22.358150482177734,
          "retention_loss": 2.4673078060150146,
          "step": 71,
          "structured_loss": 17.423534393310547
        },
        {
          "loss": 10.011409759521484,
          "retention_loss": 2.5341949462890625,
          "step": 72,
          "structured_loss": 4.943019390106201
        },
        {
          "loss": 19.982303619384766,
          "retention_loss": 2.2964017391204834,
          "step": 73,
          "structured_loss": 15.389500617980957
        },
        {
          "loss": 21.839027404785156,
          "retention_loss": 2.58457350730896,
          "step": 74,
          "structured_loss": 16.669879913330078
        },
        {
          "loss": 24.500978469848633,
          "retention_loss": 2.4489943981170654,
          "step": 75,
          "structured_loss": 19.602989196777344
        },
        {
          "loss": 12.886871337890625,
          "retention_loss": 2.4483611583709717,
          "step": 76,
          "structured_loss": 7.990149021148682
        },
        {
          "loss": 17.08517074584961,
          "retention_loss": 2.486440896987915,
          "step": 77,
          "structured_loss": 12.112288475036621
        },
        {
          "loss": 20.466495513916016,
          "retention_loss": 2.3848695755004883,
          "step": 78,
          "structured_loss": 15.696757316589355
        },
        {
          "loss": 22.350419998168945,
          "retention_loss": 2.4667844772338867,
          "step": 79,
          "structured_loss": 17.416851043701172
        },
        {
          "loss": 22.455551147460938,
          "retention_loss": 2.277153491973877,
          "step": 80,
          "structured_loss": 17.901243209838867
        },
        {
          "loss": 16.51900863647461,
          "retention_loss": 2.475358009338379,
          "step": 81,
          "structured_loss": 11.568291664123535
        },
        {
          "loss": 26.71953010559082,
          "retention_loss": 2.452782392501831,
          "step": 82,
          "structured_loss": 21.81396484375
        },
        {
          "loss": 14.032100677490234,
          "retention_loss": 2.675604820251465,
          "step": 83,
          "structured_loss": 8.680891036987305
        },
        {
          "loss": 17.0063419342041,
          "retention_loss": 2.5954811573028564,
          "step": 84,
          "structured_loss": 11.81537914276123
        },
        {
          "loss": 14.829566955566406,
          "retention_loss": 2.7695536613464355,
          "step": 85,
          "structured_loss": 9.290459632873535
        },
        {
          "loss": 21.22268295288086,
          "retention_loss": 2.719895362854004,
          "step": 86,
          "structured_loss": 15.782891273498535
        },
        {
          "loss": 21.59152603149414,
          "retention_loss": 2.6512999534606934,
          "step": 87,
          "structured_loss": 16.288925170898438
        },
        {
          "loss": 24.005558013916016,
          "retention_loss": 2.726578950881958,
          "step": 88,
          "structured_loss": 18.552400588989258
        },
        {
          "loss": 21.99685287475586,
          "retention_loss": 2.6603055000305176,
          "step": 89,
          "structured_loss": 16.676240921020508
        },
        {
          "loss": 31.60003662109375,
          "retention_loss": 2.342996597290039,
          "step": 90,
          "structured_loss": 26.914043426513672
        },
        {
          "loss": 23.131637573242188,
          "retention_loss": 2.370814085006714,
          "step": 91,
          "structured_loss": 18.3900089263916
        },
        {
          "loss": 16.605438232421875,
          "retention_loss": 2.4333736896514893,
          "step": 92,
          "structured_loss": 11.738690376281738
        },
        {
          "loss": 19.07345962524414,
          "retention_loss": 2.5213818550109863,
          "step": 93,
          "structured_loss": 14.030694961547852
        },
        {
          "loss": 21.04464340209961,
          "retention_loss": 2.4279773235321045,
          "step": 94,
          "structured_loss": 16.188688278198242
        },
        {
          "loss": 15.80025863647461,
          "retention_loss": 2.3536391258239746,
          "step": 95,
          "structured_loss": 11.09298038482666
        },
        {
          "loss": 20.268218994140625,
          "retention_loss": 2.508065700531006,
          "step": 96,
          "structured_loss": 15.252086639404297
        },
        {
          "loss": 18.87178611755371,
          "retention_loss": 2.393373966217041,
          "step": 97,
          "structured_loss": 14.085038185119629
        },
        {
          "loss": 23.252065658569336,
          "retention_loss": 2.5769779682159424,
          "step": 98,
          "structured_loss": 18.09811019897461
        },
        {
          "loss": 16.117952346801758,
          "retention_loss": 2.436192750930786,
          "step": 99,
          "structured_loss": 11.245567321777344
        },
        {
          "loss": 14.170795440673828,
          "retention_loss": 2.4261386394500732,
          "step": 100,
          "structured_loss": 9.318517684936523
        }
      ]
    }
  },
  "retention_weight": 2.0,
  "schema_version": "1.0",
  "seed": 42,
  "status": "PVR_REPLAY_ARCHITECTURE_SPECIFIC_ADVANTAGE_NOT_SUPPORTED",
  "supported_conditions": {
    "pvr_ean_efficiency_beats_dense": false,
    "pvr_ean_efficiency_beats_switch": false,
    "pvr_ean_structured_gain_positive": true,
    "pvr_ean_top1_clean": true
  }
}
```
