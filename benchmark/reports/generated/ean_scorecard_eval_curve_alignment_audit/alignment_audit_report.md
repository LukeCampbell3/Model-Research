# EAN Scorecard/Eval-Curve Alignment Audit

Status: `PVR_EAN_SCORECARD_EVAL_CURVE_ALIGNMENT_AUDIT_COMPLETE`
Detail: `EVAL_PATH_MISMATCH_OR_NOISE_REMAINS`

| model | scorecard-style mean | final training-window mean | recorded eval mean | scorecard delta | final-window delta | recorded delta |
|---|---:|---:|---:|---:|---:|---:|
| dense_300m | 3.305846790075302 | 4.929005718231201 | 5.800183653831482 | -0.11637555360794094 | 0.8468944311141966 | 0.943506813049316 |
| pvr_baseline_seed42 | 3.422222343683243 | 4.082111287117004 | 4.856676840782166 | 0.0 | 0.0 | 0.0 |
| full_copy_seed42 | 3.0127717781066896 | 4.624425411224365 | 4.987879157066345 | -0.40945056557655324 | 0.542314124107361 | 0.13120231628417933 |
| ean_seed42 | 3.010810148715973 | 4.6154529571533205 | 4.985433840751648 | -0.4114121949672698 | 0.5333416700363163 | 0.12875699996948242 |

```json
{
  "correlations": {
    "scorecard_delta_vs_final_training_window_delta_vs_baseline": 0.9998126206249922,
    "scorecard_delta_vs_recorded_training_curve_delta_vs_baseline": 0.9999949627700085,
    "scorecard_style_vs_final_training_window_mean_across_models": -0.4060783987708795,
    "scorecard_style_vs_recorded_training_curve_mean_across_models": 0.24151866899016702
  },
  "created_at": "2026-06-17T02:10:14.457339+00:00",
  "device": "cuda",
  "eval_steps": [
    400,
    800,
    1200,
    1600,
    2000,
    2400,
    2800,
    3200,
    3600,
    4000
  ],
  "experiment": "PVR_EAN_SCORECARD_EVAL_CURVE_ALIGNMENT_AUDIT",
  "git_commit": "d18165e32bec94cea3ca836937c81f6a0f3dc5f7",
  "interpretation": "This audit distinguishes final-checkpoint evaluation path mismatch from genuine during-training eval-curve instability by evaluating the same checkpoints on both scorecard-style heldout windows and training-style eval offsets.",
  "rows": {
    "dense_300m": {
      "checkpoint_path": "checkpoints/benchmark_300m/dense_transformer_300m/checkpoint.pt",
      "deltas_vs_pvr_baseline": {
        "recorded_during_training_eval_curve_mean": 0.943506813049316,
        "scorecard_style_final_checkpoint_mean": -0.11637555360794094,
        "training_window_style_final_checkpoint_mean": 0.8468944311141966
      },
      "label": "dense_300m",
      "model_variant": "dense_transformer_300m",
      "per_window_deltas_vs_pvr_baseline": {
        "scorecard_style_general": [
          {
            "baseline_loss": 3.3696975708007812,
            "delta_vs_baseline": -0.011776924133300781,
            "loss": 3.3579206466674805,
            "window_index": 0
          },
          {
            "baseline_loss": 3.7571780681610107,
            "delta_vs_baseline": -0.3577158451080322,
            "loss": 3.3994622230529785,
            "window_index": 1
          },
          {
            "baseline_loss": 2.744732618331909,
            "delta_vs_baseline": -0.0989842414855957,
            "loss": 2.6457483768463135,
            "window_index": 2
          },
          {
            "baseline_loss": 3.1212172508239746,
            "delta_vs_baseline": -0.068328857421875,
            "loss": 3.0528883934020996,
            "window_index": 3
          },
          {
            "baseline_loss": 3.1811468601226807,
            "delta_vs_baseline": -0.1647346019744873,
            "loss": 3.0164122581481934,
            "window_index": 4
          },
          {
            "baseline_loss": 3.6319479942321777,
            "delta_vs_baseline": -0.32506513595581055,
            "loss": 3.306882858276367,
            "window_index": 5
          },
          {
            "baseline_loss": 3.136638641357422,
            "delta_vs_baseline": -0.3171520233154297,
            "loss": 2.819486618041992,
            "window_index": 6
          },
          {
            "baseline_loss": 2.6240248680114746,
            "delta_vs_baseline": -0.06364560127258301,
            "loss": 2.5603792667388916,
            "window_index": 7
          },
          {
            "baseline_loss": 4.648166179656982,
            "delta_vs_baseline": -0.32541418075561523,
            "loss": 4.322751998901367,
            "window_index": 8
          },
          {
            "baseline_loss": 5.14591121673584,
            "delta_vs_baseline": -0.06856393814086914,
            "loss": 5.077347278594971,
            "window_index": 9
          },
          {
            "baseline_loss": 10.665205001831055,
            "delta_vs_baseline": -1.59832763671875,
            "loss": 9.066877365112305,
            "window_index": 10
          },
          {
            "baseline_loss": 9.66199779510498,
            "delta_vs_baseline": 1.6696643829345703,
            "loss": 11.33166217803955,
            "window_index": 11
          },
          {
            "baseline_loss": 7.029171943664551,
            "delta_vs_baseline": 0.7577633857727051,
            "loss": 7.786935329437256,
            "window_index": 12
          },
          {
            "baseline_loss": 4.451816082000732,
            "delta_vs_baseline": -0.18727970123291016,
            "loss": 4.264536380767822,
            "window_index": 13
          },
          {
            "baseline_loss": 9.882694244384766,
            "delta_vs_baseline": -3.837541103363037,
            "loss": 6.0451531410217285,
            "window_index": 14
          },
          {
            "baseline_loss": 15.704546928405762,
            "delta_vs_baseline": -1.6625299453735352,
            "loss": 14.042016983032227,
            "window_index": 15
          },
          {
            "baseline_loss": 7.221086502075195,
            "delta_vs_baseline": -2.489321231842041,
            "loss": 4.731765270233154,
            "window_index": 16
          },
          {
            "baseline_loss": 8.873090744018555,
            "delta_vs_baseline": -0.1646718978881836,
            "loss": 8.708418846130371,
            "window_index": 17
          },
          {
            "baseline_loss": 6.848356246948242,
            "delta_vs_baseline": -0.34917354583740234,
            "loss": 6.49918270111084,
            "window_index": 18
          },
          {
            "baseline_loss": 10.50163459777832,
            "delta_vs_baseline": 2.314793586730957,
            "loss": 12.816428184509277,
            "window_index": 19
          },
          {
            "baseline_loss": 8.044512748718262,
            "delta_vs_baseline": 1.7013225555419922,
            "loss": 9.745835304260254,
            "window_index": 20
          },
          {
            "baseline_loss": 12.315536499023438,
            "delta_vs_baseline": 1.0220251083374023,
            "loss": 13.33756160736084,
            "window_index": 21
          },
          {
            "baseline_loss": 7.905089378356934,
            "delta_vs_baseline": -0.20990228652954102,
            "loss": 7.695187091827393,
            "window_index": 22
          },
          {
            "baseline_loss": 6.56272029876709,
            "delta_vs_baseline": 0.418428897857666,
            "loss": 6.981149196624756,
            "window_index": 23
          },
          {
            "baseline_loss": 2.7679688930511475,
            "delta_vs_baseline": -0.10586380958557129,
            "loss": 2.662105083465576,
            "window_index": 24
          },
          {
            "baseline_loss": 2.9374938011169434,
            "delta_vs_baseline": -0.09927248954772949,
            "loss": 2.838221311569214,
            "window_index": 25
          },
          {
            "baseline_loss": 2.6757943630218506,
            "delta_vs_baseline": -0.08405470848083496,
            "loss": 2.5917396545410156,
            "window_index": 26
          },
          {
            "baseline_loss": 2.6266438961029053,
            "delta_vs_baseline": -0.11996936798095703,
            "loss": 2.5066745281219482,
            "window_index": 27
          },
          {
            "baseline_loss": 3.199479103088379,
            "delta_vs_baseline": -0.1476731300354004,
            "loss": 3.0518059730529785,
            "window_index": 28
          },
          {
            "baseline_loss": 3.1571550369262695,
            "delta_vs_baseline": -0.2404623031616211,
            "loss": 2.9166927337646484,
            "window_index": 29
          },
          {
            "baseline_loss": 2.9776811599731445,
            "delta_vs_baseline": -0.007242918014526367,
            "loss": 2.970438241958618,
            "window_index": 30
          },
          {
            "baseline_loss": 3.1856303215026855,
            "delta_vs_baseline": -0.18481206893920898,
            "loss": 3.0008182525634766,
            "window_index": 31
          },
          {
            "baseline_loss": 2.8611888885498047,
            "delta_vs_baseline": -0.20305395126342773,
            "loss": 2.658134937286377,
            "window_index": 32
          },
          {
            "baseline_loss": 2.986649751663208,
            "delta_vs_baseline": -0.14943313598632812,
            "loss": 2.83721661567688,
            "window_index": 33
          },
          {
            "baseline_loss": 3.02950119972229,
            "delta_vs_baseline": -0.03390979766845703,
            "loss": 2.995591402053833,
            "window_index": 34
          },
          {
            "baseline_loss": 2.630702018737793,
            "delta_vs_baseline": -0.1611320972442627,
            "loss": 2.4695699214935303,
            "window_index": 35
          },
          {
            "baseline_loss": 3.0871145725250244,
            "delta_vs_baseline": -0.15445184707641602,
            "loss": 2.9326627254486084,
            "window_index": 36
          },
          {
            "baseline_loss": 2.9280953407287598,
            "delta_vs_baseline": -0.026551246643066406,
            "loss": 2.9015440940856934,
            "window_index": 37
          },
          {
            "baseline_loss": 3.1325175762176514,
            "delta_vs_baseline": -0.18144822120666504,
            "loss": 2.9510693550109863,
            "window_index": 38
          },
          {
            "baseline_loss": 2.935246229171753,
            "delta_vs_baseline": -0.07570195198059082,
            "loss": 2.859544277191162,
            "window_index": 39
          },
          {
            "baseline_loss": 3.286637306213379,
            "delta_vs_baseline": -0.1786937713623047,
            "loss": 3.107943534851074,
            "window_index": 40
          },
          {
            "baseline_loss": 3.0057811737060547,
            "delta_vs_baseline": -0.04801201820373535,
            "loss": 2.9577691555023193,
            "window_index": 41
          },
          {
            "baseline_loss": 2.738572597503662,
            "delta_vs_baseline": -0.11290311813354492,
            "loss": 2.625669479370117,
            "window_index": 42
          },
          {
            "baseline_loss": 3.141986131668091,
            "delta_vs_baseline": -0.15887188911437988,
            "loss": 2.983114242553711,
            "window_index": 43
          },
          {
            "baseline_loss": 2.8448073863983154,
            "delta_vs_baseline": -0.13117599487304688,
            "loss": 2.7136313915252686,
            "window_index": 44
          },
          {
            "baseline_loss": 3.004800796508789,
            "delta_vs_baseline": -0.06905293464660645,
            "loss": 2.9357478618621826,
            "window_index": 45
          },
          {
            "baseline_loss": 2.9838449954986572,
            "delta_vs_baseline": -0.38998842239379883,
            "loss": 2.5938565731048584,
            "window_index": 46
          },
          {
            "baseline_loss": 2.9386417865753174,
            "delta_vs_baseline": -0.2993428707122803,
            "loss": 2.639298915863037,
            "window_index": 47
          },
          {
            "baseline_loss": 3.1059365272521973,
            "delta_vs_baseline": -0.05245161056518555,
            "loss": 3.0534849166870117,
            "window_index": 48
          },
          {
            "baseline_loss": 3.168769359588623,
            "delta_vs_baseline": -0.19101929664611816,
            "loss": 2.977750062942505,
            "window_index": 49
          },
          {
            "baseline_loss": 2.639850378036499,
            "delta_vs_baseline": 0.049715280532836914,
            "loss": 2.689565658569336,
            "window_index": 50
          },
          {
            "baseline_loss": 2.487496852874756,
            "delta_vs_baseline": -0.059439897537231445,
            "loss": 2.4280569553375244,
            "window_index": 51
          },
          {
            "baseline_loss": 2.708131790161133,
            "delta_vs_baseline": -0.1834125518798828,
            "loss": 2.52471923828125,
            "window_index": 52
          },
          {
            "baseline_loss": 2.8870315551757812,
            "delta_vs_baseline": -0.18401527404785156,
            "loss": 2.7030162811279297,
            "window_index": 53
          },
          {
            "baseline_loss": 3.0955796241760254,
            "delta_vs_baseline": -0.14870023727416992,
            "loss": 2.9468793869018555,
            "window_index": 54
          },
          {
            "baseline_loss": 2.8854877948760986,
            "delta_vs_baseline": -0.06789541244506836,
            "loss": 2.8175923824310303,
            "window_index": 55
          },
          {
            "baseline_loss": 2.886323928833008,
            "delta_vs_baseline": -0.1612565517425537,
            "loss": 2.725067377090454,
            "window_index": 56
          },
          {
            "baseline_loss": 2.957814931869507,
            "delta_vs_baseline": -0.1397380828857422,
            "loss": 2.8180768489837646,
            "window_index": 57
          },
          {
            "baseline_loss": 2.8409440517425537,
            "delta_vs_baseline": -0.07951831817626953,
            "loss": 2.761425733566284,
            "window_index": 58
          },
          {
            "baseline_loss": 2.849606513977051,
            "delta_vs_baseline": -0.09067916870117188,
            "loss": 2.758927345275879,
            "window_index": 59
          },
          {
            "baseline_loss": 2.8881561756134033,
            "delta_vs_baseline": -0.11740374565124512,
            "loss": 2.770752429962158,
            "window_index": 60
          },
          {
            "baseline_loss": 2.9310176372528076,
            "delta_vs_baseline": -0.06433606147766113,
            "loss": 2.8666815757751465,
            "window_index": 61
          },
          {
            "baseline_loss": 3.1954236030578613,
            "delta_vs_baseline": -0.199326753616333,
            "loss": 2.9960968494415283,
            "window_index": 62
          },
          {
            "baseline_loss": 2.7894527912139893,
            "delta_vs_baseline": -0.12302947044372559,
            "loss": 2.6664233207702637,
            "window_index": 63
          },
          {
            "baseline_loss": 2.7355093955993652,
            "delta_vs_baseline": -0.017805099487304688,
            "loss": 2.7177042961120605,
            "window_index": 64
          },
          {
            "baseline_loss": 2.6845948696136475,
            "delta_vs_baseline": -0.0726315975189209,
            "loss": 2.6119632720947266,
            "window_index": 65
          },
          {
            "baseline_loss": 3.225579261779785,
            "delta_vs_baseline": -0.1594405174255371,
            "loss": 3.066138744354248,
            "window_index": 66
          },
          {
            "baseline_loss": 2.9965693950653076,
            "delta_vs_baseline": 0.07053208351135254,
            "loss": 3.06710147857666,
            "window_index": 67
          },
          {
            "baseline_loss": 2.7195029258728027,
            "delta_vs_baseline": -0.21366024017333984,
            "loss": 2.505842685699463,
            "window_index": 68
          },
          {
            "baseline_loss": 2.9124796390533447,
            "delta_vs_baseline": -0.13102293014526367,
            "loss": 2.781456708908081,
            "window_index": 69
          },
          {
            "baseline_loss": 3.2319014072418213,
            "delta_vs_baseline": -0.14305448532104492,
            "loss": 3.0888469219207764,
            "window_index": 70
          },
          {
            "baseline_loss": 2.8929831981658936,
            "delta_vs_baseline": 0.07847452163696289,
            "loss": 2.9714577198028564,
            "window_index": 71
          },
          {
            "baseline_loss": 3.253342866897583,
            "delta_vs_baseline": -0.07825708389282227,
            "loss": 3.1750857830047607,
            "window_index": 72
          },
          {
            "baseline_loss": 3.1915409564971924,
            "delta_vs_baseline": -0.1855177879333496,
            "loss": 3.0060231685638428,
            "window_index": 73
          },
          {
            "baseline_loss": 2.7452118396759033,
            "delta_vs_baseline": -0.17170333862304688,
            "loss": 2.5735085010528564,
            "window_index": 74
          },
          {
            "baseline_loss": 2.888545513153076,
            "delta_vs_baseline": -0.12222766876220703,
            "loss": 2.766317844390869,
            "window_index": 75
          },
          {
            "baseline_loss": 2.8269476890563965,
            "delta_vs_baseline": -0.05058860778808594,
            "loss": 2.7763590812683105,
            "window_index": 76
          },
          {
            "baseline_loss": 3.2102153301239014,
            "delta_vs_baseline": -0.043474435806274414,
            "loss": 3.166740894317627,
            "window_index": 77
          },
          {
            "baseline_loss": 2.439115285873413,
            "delta_vs_baseline": 0.09793257713317871,
            "loss": 2.537047863006592,
            "window_index": 78
          },
          {
            "baseline_loss": 3.13478684425354,
            "delta_vs_baseline": 0.01154780387878418,
            "loss": 3.146334648132324,
            "window_index": 79
          },
          {
            "baseline_loss": 2.9935171604156494,
            "delta_vs_baseline": -0.1985769271850586,
            "loss": 2.794940233230591,
            "window_index": 80
          },
          {
            "baseline_loss": 3.124610662460327,
            "delta_vs_baseline": -0.22373270988464355,
            "loss": 2.9008779525756836,
            "window_index": 81
          },
          {
            "baseline_loss": 2.723752498626709,
            "delta_vs_baseline": -0.04267382621765137,
            "loss": 2.6810786724090576,
            "window_index": 82
          },
          {
            "baseline_loss": 2.757559299468994,
            "delta_vs_baseline": 0.08765363693237305,
            "loss": 2.845212936401367,
            "window_index": 83
          },
          {
            "baseline_loss": 2.790419340133667,
            "delta_vs_baseline": 0.08158469200134277,
            "loss": 2.8720040321350098,
            "window_index": 84
          },
          {
            "baseline_loss": 2.5810930728912354,
            "delta_vs_baseline": -0.24719619750976562,
            "loss": 2.3338968753814697,
            "window_index": 85
          },
          {
            "baseline_loss": 3.3501040935516357,
            "delta_vs_baseline": -0.12887072563171387,
            "loss": 3.221233367919922,
            "window_index": 86
          },
          {
            "baseline_loss": 2.985410213470459,
            "delta_vs_baseline": -0.26637887954711914,
            "loss": 2.71903133392334,
            "window_index": 87
          },
          {
            "baseline_loss": 2.7511179447174072,
            "delta_vs_baseline": -0.15234088897705078,
            "loss": 2.5987770557403564,
            "window_index": 88
          },
          {
            "baseline_loss": 3.147357225418091,
            "delta_vs_baseline": -0.2721519470214844,
            "loss": 2.8752052783966064,
            "window_index": 89
          },
          {
            "baseline_loss": 3.229327917098999,
            "delta_vs_baseline": -0.13863921165466309,
            "loss": 3.090688705444336,
            "window_index": 90
          },
          {
            "baseline_loss": 2.8613240718841553,
            "delta_vs_baseline": -0.1609363555908203,
            "loss": 2.700387716293335,
            "window_index": 91
          },
          {
            "baseline_loss": 2.696187734603882,
            "delta_vs_baseline": -0.15316367149353027,
            "loss": 2.5430240631103516,
            "window_index": 92
          },
          {
            "baseline_loss": 2.9458367824554443,
            "delta_vs_baseline": -0.21683716773986816,
            "loss": 2.728999614715576,
            "window_index": 93
          },
          {
            "baseline_loss": 2.9736671447753906,
            "delta_vs_baseline": 0.014123916625976562,
            "loss": 2.987791061401367,
            "window_index": 94
          },
          {
            "baseline_loss": 2.747361660003662,
            "delta_vs_baseline": -0.11565065383911133,
            "loss": 2.631711006164551,
            "window_index": 95
          },
          {
            "baseline_loss": 2.9285504817962646,
            "delta_vs_baseline": -0.03984570503234863,
            "loss": 2.888704776763916,
            "window_index": 96
          },
          {
            "baseline_loss": 3.183176279067993,
            "delta_vs_baseline": -0.20923709869384766,
            "loss": 2.9739391803741455,
            "window_index": 97
          },
          {
            "baseline_loss": 2.5617079734802246,
            "delta_vs_baseline": 0.014005899429321289,
            "loss": 2.575713872909546,
            "window_index": 98
          },
          {
            "baseline_loss": 3.026214599609375,
            "delta_vs_baseline": -0.05622148513793945,
            "loss": 2.9699931144714355,
            "window_index": 99
          },
          {
            "baseline_loss": 3.2600483894348145,
            "delta_vs_baseline": -0.15008807182312012,
            "loss": 3.1099603176116943,
            "window_index": 100
          },
          {
            "baseline_loss": 2.9374611377716064,
            "delta_vs_baseline": -0.09290814399719238,
            "loss": 2.844552993774414,
            "window_index": 101
          },
          {
            "baseline_loss": 2.9559378623962402,
            "delta_vs_baseline": -0.005678415298461914,
            "loss": 2.9502594470977783,
            "window_index": 102
          },
          {
            "baseline_loss": 3.020036220550537,
            "delta_vs_baseline": -0.15275001525878906,
            "loss": 2.867286205291748,
            "window_index": 103
          },
          {
            "baseline_loss": 3.088770866394043,
            "delta_vs_baseline": -0.11788129806518555,
            "loss": 2.9708895683288574,
            "window_index": 104
          },
          {
            "baseline_loss": 2.8664493560791016,
            "delta_vs_baseline": 0.03737998008728027,
            "loss": 2.903829336166382,
            "window_index": 105
          },
          {
            "baseline_loss": 2.9487314224243164,
            "delta_vs_baseline": -0.19403862953186035,
            "loss": 2.754692792892456,
            "window_index": 106
          },
          {
            "baseline_loss": 2.9448704719543457,
            "delta_vs_baseline": -0.18714165687561035,
            "loss": 2.7577288150787354,
            "window_index": 107
          },
          {
            "baseline_loss": 2.833847761154175,
            "delta_vs_baseline": 0.0031065940856933594,
            "loss": 2.836954355239868,
            "window_index": 108
          },
          {
            "baseline_loss": 3.0840413570404053,
            "delta_vs_baseline": -0.14859771728515625,
            "loss": 2.935443639755249,
            "window_index": 109
          },
          {
            "baseline_loss": 3.0566482543945312,
            "delta_vs_baseline": 0.013943672180175781,
            "loss": 3.070591926574707,
            "window_index": 110
          },
          {
            "baseline_loss": 3.0592665672302246,
            "delta_vs_baseline": -0.030553102493286133,
            "loss": 3.0287134647369385,
            "window_index": 111
          },
          {
            "baseline_loss": 2.9259722232818604,
            "delta_vs_baseline": -0.10312604904174805,
            "loss": 2.8228461742401123,
            "window_index": 112
          },
          {
            "baseline_loss": 3.1105833053588867,
            "delta_vs_baseline": -0.22454524040222168,
            "loss": 2.886038064956665,
            "window_index": 113
          },
          {
            "baseline_loss": 2.762549877166748,
            "delta_vs_baseline": -0.06427836418151855,
            "loss": 2.6982715129852295,
            "window_index": 114
          },
          {
            "baseline_loss": 3.0378577709198,
            "delta_vs_baseline": -0.11095428466796875,
            "loss": 2.926903486251831,
            "window_index": 115
          },
          {
            "baseline_loss": 3.0677103996276855,
            "delta_vs_baseline": -0.05248594284057617,
            "loss": 3.0152244567871094,
            "window_index": 116
          },
          {
            "baseline_loss": 2.8927221298217773,
            "delta_vs_baseline": 0.029085636138916016,
            "loss": 2.9218077659606934,
            "window_index": 117
          },
          {
            "baseline_loss": 3.42633056640625,
            "delta_vs_baseline": -0.11641621589660645,
            "loss": 3.3099143505096436,
            "window_index": 118
          },
          {
            "baseline_loss": 2.779985189437866,
            "delta_vs_baseline": -0.1553955078125,
            "loss": 2.624589681625366,
            "window_index": 119
          },
          {
            "baseline_loss": 2.5664048194885254,
            "delta_vs_baseline": -0.10246157646179199,
            "loss": 2.4639432430267334,
            "window_index": 120
          },
          {
            "baseline_loss": 2.9053828716278076,
            "delta_vs_baseline": -0.08870220184326172,
            "loss": 2.816680669784546,
            "window_index": 121
          },
          {
            "baseline_loss": 2.8783071041107178,
            "delta_vs_baseline": -0.08247518539428711,
            "loss": 2.7958319187164307,
            "window_index": 122
          },
          {
            "baseline_loss": 2.7440104484558105,
            "delta_vs_baseline": -0.01692509651184082,
            "loss": 2.7270853519439697,
            "window_index": 123
          },
          {
            "baseline_loss": 3.080070734024048,
            "delta_vs_baseline": -0.042968034744262695,
            "loss": 3.037102699279785,
            "window_index": 124
          },
          {
            "baseline_loss": 2.944106101989746,
            "delta_vs_baseline": -0.11289191246032715,
            "loss": 2.831214189529419,
            "window_index": 125
          },
          {
            "baseline_loss": 3.7518718242645264,
            "delta_vs_baseline": -0.25611233711242676,
            "loss": 3.4957594871520996,
            "window_index": 126
          },
          {
            "baseline_loss": 2.967647075653076,
            "delta_vs_baseline": -0.2431621551513672,
            "loss": 2.724484920501709,
            "window_index": 127
          },
          {
            "baseline_loss": 2.798103094100952,
            "delta_vs_baseline": -0.12318682670593262,
            "loss": 2.6749162673950195,
            "window_index": 128
          },
          {
            "baseline_loss": 4.579283237457275,
            "delta_vs_baseline": -0.23078584671020508,
            "loss": 4.34849739074707,
            "window_index": 129
          },
          {
            "baseline_loss": 8.379351615905762,
            "delta_vs_baseline": -0.35565662384033203,
            "loss": 8.02369499206543,
            "window_index": 130
          },
          {
            "baseline_loss": 2.477597713470459,
            "delta_vs_baseline": 0.010415792465209961,
            "loss": 2.488013505935669,
            "window_index": 131
          },
          {
            "baseline_loss": 3.072523832321167,
            "delta_vs_baseline": 0.10532832145690918,
            "loss": 3.177852153778076,
            "window_index": 132
          },
          {
            "baseline_loss": 2.88889479637146,
            "delta_vs_baseline": -0.02711343765258789,
            "loss": 2.861781358718872,
            "window_index": 133
          },
          {
            "baseline_loss": 2.657388210296631,
            "delta_vs_baseline": -0.050159454345703125,
            "loss": 2.6072287559509277,
            "window_index": 134
          },
          {
            "baseline_loss": 3.222710132598877,
            "delta_vs_baseline": -0.1612095832824707,
            "loss": 3.0615005493164062,
            "window_index": 135
          },
          {
            "baseline_loss": 2.594160318374634,
            "delta_vs_baseline": -0.09332132339477539,
            "loss": 2.5008389949798584,
            "window_index": 136
          },
          {
            "baseline_loss": 2.761676549911499,
            "delta_vs_baseline": -0.20692801475524902,
            "loss": 2.55474853515625,
            "window_index": 137
          },
          {
            "baseline_loss": 3.063735246658325,
            "delta_vs_baseline": -0.15094685554504395,
            "loss": 2.9127883911132812,
            "window_index": 138
          },
          {
            "baseline_loss": 3.095252275466919,
            "delta_vs_baseline": -0.2338392734527588,
            "loss": 2.86141300201416,
            "window_index": 139
          },
          {
            "baseline_loss": 3.001328706741333,
            "delta_vs_baseline": -0.02857828140258789,
            "loss": 2.972750425338745,
            "window_index": 140
          },
          {
            "baseline_loss": 3.124728202819824,
            "delta_vs_baseline": -0.17152786254882812,
            "loss": 2.953200340270996,
            "window_index": 141
          },
          {
            "baseline_loss": 3.071362257003784,
            "delta_vs_baseline": -0.2122030258178711,
            "loss": 2.859159231185913,
            "window_index": 142
          },
          {
            "baseline_loss": 2.8115036487579346,
            "delta_vs_baseline": -0.11630558967590332,
            "loss": 2.6951980590820312,
            "window_index": 143
          },
          {
            "baseline_loss": 2.6746327877044678,
            "delta_vs_baseline": 0.025200605392456055,
            "loss": 2.699833393096924,
            "window_index": 144
          },
          {
            "baseline_loss": 2.9380056858062744,
            "delta_vs_baseline": -0.2909276485443115,
            "loss": 2.647078037261963,
            "window_index": 145
          },
          {
            "baseline_loss": 3.0988097190856934,
            "delta_vs_baseline": -0.09033036231994629,
            "loss": 3.008479356765747,
            "window_index": 146
          },
          {
            "baseline_loss": 2.920891761779785,
            "delta_vs_baseline": -0.12318730354309082,
            "loss": 2.7977044582366943,
            "window_index": 147
          },
          {
            "baseline_loss": 3.0000956058502197,
            "delta_vs_baseline": -0.1462852954864502,
            "loss": 2.8538103103637695,
            "window_index": 148
          },
          {
            "baseline_loss": 3.14078688621521,
            "delta_vs_baseline": -0.19067025184631348,
            "loss": 2.9501166343688965,
            "window_index": 149
          },
          {
            "baseline_loss": 3.0242533683776855,
            "delta_vs_baseline": -0.17378878593444824,
            "loss": 2.8504645824432373,
            "window_index": 150
          },
          {
            "baseline_loss": 3.2188079357147217,
            "delta_vs_baseline": -0.10358881950378418,
            "loss": 3.1152191162109375,
            "window_index": 151
          },
          {
            "baseline_loss": 2.875241756439209,
            "delta_vs_baseline": -0.031672000885009766,
            "loss": 2.843569755554199,
            "window_index": 152
          },
          {
            "baseline_loss": 2.890204668045044,
            "delta_vs_baseline": 0.11593174934387207,
            "loss": 3.006136417388916,
            "window_index": 153
          },
          {
            "baseline_loss": 2.5632436275482178,
            "delta_vs_baseline": -0.030359506607055664,
            "loss": 2.532884120941162,
            "window_index": 154
          },
          {
            "baseline_loss": 3.276603937149048,
            "delta_vs_baseline": -0.2078239917755127,
            "loss": 3.068779945373535,
            "window_index": 155
          },
          {
            "baseline_loss": 2.8790481090545654,
            "delta_vs_baseline": -0.13016939163208008,
            "loss": 2.7488787174224854,
            "window_index": 156
          },
          {
            "baseline_loss": 3.015944242477417,
            "delta_vs_baseline": -0.14049220085144043,
            "loss": 2.8754520416259766,
            "window_index": 157
          },
          {
            "baseline_loss": 3.1061058044433594,
            "delta_vs_baseline": -0.16247344017028809,
            "loss": 2.9436323642730713,
            "window_index": 158
          },
          {
            "baseline_loss": 2.731477975845337,
            "delta_vs_baseline": -0.11578631401062012,
            "loss": 2.615691661834717,
            "window_index": 159
          },
          {
            "baseline_loss": 2.7437946796417236,
            "delta_vs_baseline": 0.2241675853729248,
            "loss": 2.9679622650146484,
            "window_index": 160
          },
          {
            "baseline_loss": 3.6713614463806152,
            "delta_vs_baseline": -0.25021815299987793,
            "loss": 3.4211432933807373,
            "window_index": 161
          },
          {
            "baseline_loss": 3.0516977310180664,
            "delta_vs_baseline": -0.1538233757019043,
            "loss": 2.897874355316162,
            "window_index": 162
          },
          {
            "baseline_loss": 3.183318614959717,
            "delta_vs_baseline": -0.10477566719055176,
            "loss": 3.078542947769165,
            "window_index": 163
          },
          {
            "baseline_loss": 2.829756021499634,
            "delta_vs_baseline": 0.04268980026245117,
            "loss": 2.872445821762085,
            "window_index": 164
          },
          {
            "baseline_loss": 2.694065809249878,
            "delta_vs_baseline": 0.04968690872192383,
            "loss": 2.7437527179718018,
            "window_index": 165
          },
          {
            "baseline_loss": 3.1200010776519775,
            "delta_vs_baseline": -0.02495551109313965,
            "loss": 3.095045566558838,
            "window_index": 166
          },
          {
            "baseline_loss": 3.0029048919677734,
            "delta_vs_baseline": -0.0069468021392822266,
            "loss": 2.995958089828491,
            "window_index": 167
          },
          {
            "baseline_loss": 3.049888849258423,
            "delta_vs_baseline": -0.1815958023071289,
            "loss": 2.868293046951294,
            "window_index": 168
          },
          {
            "baseline_loss": 2.74784255027771,
            "delta_vs_baseline": -0.19348669052124023,
            "loss": 2.5543558597564697,
            "window_index": 169
          },
          {
            "baseline_loss": 2.7892608642578125,
            "delta_vs_baseline": 0.003635883331298828,
            "loss": 2.7928967475891113,
            "window_index": 170
          },
          {
            "baseline_loss": 3.56272029876709,
            "delta_vs_baseline": -0.2422945499420166,
            "loss": 3.3204257488250732,
            "window_index": 171
          },
          {
            "baseline_loss": 3.123473644256592,
            "delta_vs_baseline": -0.08536672592163086,
            "loss": 3.038106918334961,
            "window_index": 172
          },
          {
            "baseline_loss": 3.0645110607147217,
            "delta_vs_baseline": -0.15923404693603516,
            "loss": 2.9052770137786865,
            "window_index": 173
          },
          {
            "baseline_loss": 2.488665819168091,
            "delta_vs_baseline": 0.00406956672668457,
            "loss": 2.4927353858947754,
            "window_index": 174
          },
          {
            "baseline_loss": 3.198608875274658,
            "delta_vs_baseline": -0.04686260223388672,
            "loss": 3.1517462730407715,
            "window_index": 175
          },
          {
            "baseline_loss": 2.749643325805664,
            "delta_vs_baseline": -0.047286033630371094,
            "loss": 2.702357292175293,
            "window_index": 176
          },
          {
            "baseline_loss": 3.1345784664154053,
            "delta_vs_baseline": -0.20639467239379883,
            "loss": 2.9281837940216064,
            "window_index": 177
          },
          {
            "baseline_loss": 3.0150883197784424,
            "delta_vs_baseline": -0.0064487457275390625,
            "loss": 3.0086395740509033,
            "window_index": 178
          },
          {
            "baseline_loss": 2.964832305908203,
            "delta_vs_baseline": -0.07430839538574219,
            "loss": 2.890523910522461,
            "window_index": 179
          },
          {
            "baseline_loss": 2.8198471069335938,
            "delta_vs_baseline": -0.0906982421875,
            "loss": 2.7291488647460938,
            "window_index": 180
          },
          {
            "baseline_loss": 2.734243869781494,
            "delta_vs_baseline": -0.14383244514465332,
            "loss": 2.590411424636841,
            "window_index": 181
          },
          {
            "baseline_loss": 3.057004451751709,
            "delta_vs_baseline": -0.06946539878845215,
            "loss": 2.987539052963257,
            "window_index": 182
          },
          {
            "baseline_loss": 2.6313588619232178,
            "delta_vs_baseline": -0.05649852752685547,
            "loss": 2.5748603343963623,
            "window_index": 183
          },
          {
            "baseline_loss": 2.712092161178589,
            "delta_vs_baseline": -0.08122611045837402,
            "loss": 2.630866050720215,
            "window_index": 184
          },
          {
            "baseline_loss": 3.1154446601867676,
            "delta_vs_baseline": -0.2005143165588379,
            "loss": 2.9149303436279297,
            "window_index": 185
          },
          {
            "baseline_loss": 2.9323294162750244,
            "delta_vs_baseline": -0.2611992359161377,
            "loss": 2.6711301803588867,
            "window_index": 186
          },
          {
            "baseline_loss": 2.799142837524414,
            "delta_vs_baseline": -0.03508758544921875,
            "loss": 2.7640552520751953,
            "window_index": 187
          },
          {
            "baseline_loss": 2.6941280364990234,
            "delta_vs_baseline": -0.003130197525024414,
            "loss": 2.690997838973999,
            "window_index": 188
          },
          {
            "baseline_loss": 2.839932441711426,
            "delta_vs_baseline": -0.003941774368286133,
            "loss": 2.8359906673431396,
            "window_index": 189
          },
          {
            "baseline_loss": 3.0761919021606445,
            "delta_vs_baseline": -0.1875321865081787,
            "loss": 2.888659715652466,
            "window_index": 190
          },
          {
            "baseline_loss": 2.7878189086914062,
            "delta_vs_baseline": -0.1823582649230957,
            "loss": 2.6054606437683105,
            "window_index": 191
          },
          {
            "baseline_loss": 2.6268908977508545,
            "delta_vs_baseline": 0.0685586929321289,
            "loss": 2.6954495906829834,
            "window_index": 192
          },
          {
            "baseline_loss": 2.9380271434783936,
            "delta_vs_baseline": -0.22115159034729004,
            "loss": 2.7168755531311035,
            "window_index": 193
          },
          {
            "baseline_loss": 2.3056321144104004,
            "delta_vs_baseline": -0.06746149063110352,
            "loss": 2.238170623779297,
            "window_index": 194
          },
          {
            "baseline_loss": 2.9026896953582764,
            "delta_vs_baseline": -0.0911412239074707,
            "loss": 2.8115484714508057,
            "window_index": 195
          },
          {
            "baseline_loss": 2.7789411544799805,
            "delta_vs_baseline": -0.22042465209960938,
            "loss": 2.558516502380371,
            "window_index": 196
          },
          {
            "baseline_loss": 2.5273962020874023,
            "delta_vs_baseline": 0.04696798324584961,
            "loss": 2.574364185333252,
            "window_index": 197
          },
          {
            "baseline_loss": 2.603788137435913,
            "delta_vs_baseline": -0.17856383323669434,
            "loss": 2.4252243041992188,
            "window_index": 198
          },
          {
            "baseline_loss": 2.6679775714874268,
            "delta_vs_baseline": -0.07750606536865234,
            "loss": 2.5904715061187744,
            "window_index": 199
          }
        ],
        "training_window_style_final_checkpoint": [
          {
            "baseline_loss": 2.488567590713501,
            "delta_vs_baseline": 0.010659456253051758,
            "loss": 2.4992270469665527,
            "step": 400
          },
          {
            "baseline_loss": 2.6633172035217285,
            "delta_vs_baseline": -0.0885469913482666,
            "loss": 2.574770212173462,
            "step": 800
          },
          {
            "baseline_loss": 2.646700859069824,
            "delta_vs_baseline": 0.004887104034423828,
            "loss": 2.651587963104248,
            "step": 1200
          },
          {
            "baseline_loss": 2.646510124206543,
            "delta_vs_baseline": -0.017916440963745117,
            "loss": 2.628593683242798,
            "step": 1600
          },
          {
            "baseline_loss": 2.54093074798584,
            "delta_vs_baseline": -0.017042875289916992,
            "loss": 2.523887872695923,
            "step": 2000
          },
          {
            "baseline_loss": 2.822401523590088,
            "delta_vs_baseline": -0.1245737075805664,
            "loss": 2.6978278160095215,
            "step": 2400
          },
          {
            "baseline_loss": 2.4011733531951904,
            "delta_vs_baseline": -0.04287576675415039,
            "loss": 2.35829758644104,
            "step": 2800
          },
          {
            "baseline_loss": 2.6783716678619385,
            "delta_vs_baseline": -0.006315946578979492,
            "loss": 2.672055721282959,
            "step": 3200
          },
          {
            "baseline_loss": 8.865436553955078,
            "delta_vs_baseline": 3.492197036743164,
            "loss": 12.357633590698242,
            "step": 3600
          },
          {
            "baseline_loss": 11.067703247070312,
            "delta_vs_baseline": 5.258472442626953,
            "loss": 16.326175689697266,
            "step": 4000
          }
        ]
      },
      "recorded_during_training_eval_curve": {
        "loss_variance": 24.754916675251437,
        "mean_loss": 5.800183653831482,
        "path": "benchmark/reports/generated/training_300m_real_4k/dense_transformer_300m/eval_curve.json",
        "window_count": 10,
        "windows": [
          {
            "eval_loss": 4.764504432678223,
            "eval_tokens": 128,
            "optimizer_step": 400,
            "step": 400,
            "training_tokens_seen": 102400
          },
          {
            "eval_loss": 5.215051174163818,
            "eval_tokens": 128,
            "optimizer_step": 800,
            "step": 800,
            "training_tokens_seen": 204800
          },
          {
            "eval_loss": 3.254971981048584,
            "eval_tokens": 128,
            "optimizer_step": 1200,
            "step": 1200,
            "training_tokens_seen": 307200
          },
          {
            "eval_loss": 2.758665084838867,
            "eval_tokens": 128,
            "optimizer_step": 1600,
            "step": 1600,
            "training_tokens_seen": 409600
          },
          {
            "eval_loss": 2.6123461723327637,
            "eval_tokens": 128,
            "optimizer_step": 2000,
            "step": 2000,
            "training_tokens_seen": 512000
          },
          {
            "eval_loss": 2.93515944480896,
            "eval_tokens": 128,
            "optimizer_step": 2400,
            "step": 2400,
            "training_tokens_seen": 614400
          },
          {
            "eval_loss": 2.523310422897339,
            "eval_tokens": 128,
            "optimizer_step": 2800,
            "step": 2800,
            "training_tokens_seen": 716800
          },
          {
            "eval_loss": 2.7878377437591553,
            "eval_tokens": 128,
            "optimizer_step": 3200,
            "step": 3200,
            "training_tokens_seen": 819200
          },
          {
            "eval_loss": 14.823814392089844,
            "eval_tokens": 128,
            "optimizer_step": 3600,
            "step": 3600,
            "training_tokens_seen": 921600
          },
          {
            "eval_loss": 16.326175689697266,
            "eval_tokens": 128,
            "optimizer_step": 4000,
            "step": 4000,
            "training_tokens_seen": 1024000
          }
        ]
      },
      "same_heldout_tokens": {
        "loss_variance": 3.1206734749589566,
        "mean_loss": 3.305846790075302,
        "scorecard_seq_len": 64,
        "window_count": 200
      },
      "scorecard_lm_loss_recorded": null,
      "scorecard_style_final_checkpoint": {
        "loss_variance": 3.1206734749589566,
        "max_loss": 14.042016983032227,
        "mean_loss": 3.305846790075302,
        "min_loss": 2.238170623779297,
        "window_count": 200
      },
      "training_window_style_final_checkpoint": {
        "loss_variance": 22.946988206733582,
        "max_loss": 16.326175689697266,
        "mean_loss": 4.929005718231201,
        "min_loss": 2.35829758644104,
        "window_count": 10
      }
    },
    "ean_seed42": {
      "checkpoint_path": "checkpoints/ean_init_300m_repeat_seed_42/pvr_ec_o_full_300m_shared_trunk_init_v1_scope_embeddings_attention_norms_seed_42/checkpoint.pt",
      "deltas_vs_pvr_baseline": {
        "recorded_during_training_eval_curve_mean": 0.12875699996948242,
        "scorecard_style_final_checkpoint_mean": -0.4114121949672698,
        "training_window_style_final_checkpoint_mean": 0.5333416700363163
      },
      "label": "ean_seed42",
      "model_variant": "pvr_ec_o_full_300m_shared_trunk_init_v1_scope_embeddings_attention_norms_seed_42",
      "per_window_deltas_vs_pvr_baseline": {
        "scorecard_style_general": [
          {
            "baseline_loss": 3.3696975708007812,
            "delta_vs_baseline": -0.35199642181396484,
            "loss": 3.0177011489868164,
            "window_index": 0
          },
          {
            "baseline_loss": 3.7571780681610107,
            "delta_vs_baseline": -0.6467947959899902,
            "loss": 3.1103832721710205,
            "window_index": 1
          },
          {
            "baseline_loss": 2.744732618331909,
            "delta_vs_baseline": -0.24497151374816895,
            "loss": 2.4997611045837402,
            "window_index": 2
          },
          {
            "baseline_loss": 3.1212172508239746,
            "delta_vs_baseline": -0.2739369869232178,
            "loss": 2.847280263900757,
            "window_index": 3
          },
          {
            "baseline_loss": 3.1811468601226807,
            "delta_vs_baseline": -0.30361461639404297,
            "loss": 2.8775322437286377,
            "window_index": 4
          },
          {
            "baseline_loss": 3.6319479942321777,
            "delta_vs_baseline": -0.48298144340515137,
            "loss": 3.1489665508270264,
            "window_index": 5
          },
          {
            "baseline_loss": 3.136638641357422,
            "delta_vs_baseline": -0.5565152168273926,
            "loss": 2.5801234245300293,
            "window_index": 6
          },
          {
            "baseline_loss": 2.6240248680114746,
            "delta_vs_baseline": -0.14942669868469238,
            "loss": 2.4745981693267822,
            "window_index": 7
          },
          {
            "baseline_loss": 4.648166179656982,
            "delta_vs_baseline": -0.7354874610900879,
            "loss": 3.9126787185668945,
            "window_index": 8
          },
          {
            "baseline_loss": 5.14591121673584,
            "delta_vs_baseline": -0.7495722770690918,
            "loss": 4.396338939666748,
            "window_index": 9
          },
          {
            "baseline_loss": 10.665205001831055,
            "delta_vs_baseline": -3.899498462677002,
            "loss": 6.765706539154053,
            "window_index": 10
          },
          {
            "baseline_loss": 9.66199779510498,
            "delta_vs_baseline": -0.017914772033691406,
            "loss": 9.644083023071289,
            "window_index": 11
          },
          {
            "baseline_loss": 7.029171943664551,
            "delta_vs_baseline": -0.6325607299804688,
            "loss": 6.396611213684082,
            "window_index": 12
          },
          {
            "baseline_loss": 4.451816082000732,
            "delta_vs_baseline": -0.557570219039917,
            "loss": 3.8942458629608154,
            "window_index": 13
          },
          {
            "baseline_loss": 9.882694244384766,
            "delta_vs_baseline": -5.386396884918213,
            "loss": 4.496297359466553,
            "window_index": 14
          },
          {
            "baseline_loss": 15.704546928405762,
            "delta_vs_baseline": -7.054422378540039,
            "loss": 8.650124549865723,
            "window_index": 15
          },
          {
            "baseline_loss": 7.221086502075195,
            "delta_vs_baseline": -3.457592725753784,
            "loss": 3.763493776321411,
            "window_index": 16
          },
          {
            "baseline_loss": 8.873090744018555,
            "delta_vs_baseline": -2.216982364654541,
            "loss": 6.656108379364014,
            "window_index": 17
          },
          {
            "baseline_loss": 6.848356246948242,
            "delta_vs_baseline": -1.6360044479370117,
            "loss": 5.2123517990112305,
            "window_index": 18
          },
          {
            "baseline_loss": 10.50163459777832,
            "delta_vs_baseline": 0.3143186569213867,
            "loss": 10.815953254699707,
            "window_index": 19
          },
          {
            "baseline_loss": 8.044512748718262,
            "delta_vs_baseline": -1.2602100372314453,
            "loss": 6.784302711486816,
            "window_index": 20
          },
          {
            "baseline_loss": 12.315536499023438,
            "delta_vs_baseline": -2.147976875305176,
            "loss": 10.167559623718262,
            "window_index": 21
          },
          {
            "baseline_loss": 7.905089378356934,
            "delta_vs_baseline": -2.211487293243408,
            "loss": 5.693602085113525,
            "window_index": 22
          },
          {
            "baseline_loss": 6.56272029876709,
            "delta_vs_baseline": -1.141657829284668,
            "loss": 5.421062469482422,
            "window_index": 23
          },
          {
            "baseline_loss": 2.7679688930511475,
            "delta_vs_baseline": -0.24880051612854004,
            "loss": 2.5191683769226074,
            "window_index": 24
          },
          {
            "baseline_loss": 2.9374938011169434,
            "delta_vs_baseline": -0.29775166511535645,
            "loss": 2.639742136001587,
            "window_index": 25
          },
          {
            "baseline_loss": 2.6757943630218506,
            "delta_vs_baseline": -0.1560063362121582,
            "loss": 2.5197880268096924,
            "window_index": 26
          },
          {
            "baseline_loss": 2.6266438961029053,
            "delta_vs_baseline": -0.19240474700927734,
            "loss": 2.434239149093628,
            "window_index": 27
          },
          {
            "baseline_loss": 3.199479103088379,
            "delta_vs_baseline": -0.2508060932159424,
            "loss": 2.9486730098724365,
            "window_index": 28
          },
          {
            "baseline_loss": 3.1571550369262695,
            "delta_vs_baseline": -0.34757447242736816,
            "loss": 2.8095805644989014,
            "window_index": 29
          },
          {
            "baseline_loss": 2.9776811599731445,
            "delta_vs_baseline": -0.2089376449584961,
            "loss": 2.7687435150146484,
            "window_index": 30
          },
          {
            "baseline_loss": 3.1856303215026855,
            "delta_vs_baseline": -0.4589273929595947,
            "loss": 2.726702928543091,
            "window_index": 31
          },
          {
            "baseline_loss": 2.8611888885498047,
            "delta_vs_baseline": -0.25812554359436035,
            "loss": 2.6030633449554443,
            "window_index": 32
          },
          {
            "baseline_loss": 2.986649751663208,
            "delta_vs_baseline": -0.2707085609436035,
            "loss": 2.7159411907196045,
            "window_index": 33
          },
          {
            "baseline_loss": 3.02950119972229,
            "delta_vs_baseline": -0.19907283782958984,
            "loss": 2.8304283618927,
            "window_index": 34
          },
          {
            "baseline_loss": 2.630702018737793,
            "delta_vs_baseline": -0.2946603298187256,
            "loss": 2.3360416889190674,
            "window_index": 35
          },
          {
            "baseline_loss": 3.0871145725250244,
            "delta_vs_baseline": -0.30752015113830566,
            "loss": 2.7795944213867188,
            "window_index": 36
          },
          {
            "baseline_loss": 2.9280953407287598,
            "delta_vs_baseline": -0.19867348670959473,
            "loss": 2.729421854019165,
            "window_index": 37
          },
          {
            "baseline_loss": 3.1325175762176514,
            "delta_vs_baseline": -0.2755110263824463,
            "loss": 2.857006549835205,
            "window_index": 38
          },
          {
            "baseline_loss": 2.935246229171753,
            "delta_vs_baseline": -0.2096545696258545,
            "loss": 2.7255916595458984,
            "window_index": 39
          },
          {
            "baseline_loss": 3.286637306213379,
            "delta_vs_baseline": -0.48260068893432617,
            "loss": 2.8040366172790527,
            "window_index": 40
          },
          {
            "baseline_loss": 3.0057811737060547,
            "delta_vs_baseline": -0.21808981895446777,
            "loss": 2.787691354751587,
            "window_index": 41
          },
          {
            "baseline_loss": 2.738572597503662,
            "delta_vs_baseline": -0.3473398685455322,
            "loss": 2.39123272895813,
            "window_index": 42
          },
          {
            "baseline_loss": 3.141986131668091,
            "delta_vs_baseline": -0.30890798568725586,
            "loss": 2.833078145980835,
            "window_index": 43
          },
          {
            "baseline_loss": 2.8448073863983154,
            "delta_vs_baseline": -0.3057873249053955,
            "loss": 2.53902006149292,
            "window_index": 44
          },
          {
            "baseline_loss": 3.004800796508789,
            "delta_vs_baseline": -0.2885420322418213,
            "loss": 2.7162587642669678,
            "window_index": 45
          },
          {
            "baseline_loss": 2.9838449954986572,
            "delta_vs_baseline": -0.45570969581604004,
            "loss": 2.528135299682617,
            "window_index": 46
          },
          {
            "baseline_loss": 2.9386417865753174,
            "delta_vs_baseline": -0.30762648582458496,
            "loss": 2.6310153007507324,
            "window_index": 47
          },
          {
            "baseline_loss": 3.1059365272521973,
            "delta_vs_baseline": -0.2045142650604248,
            "loss": 2.9014222621917725,
            "window_index": 48
          },
          {
            "baseline_loss": 3.168769359588623,
            "delta_vs_baseline": -0.3737473487854004,
            "loss": 2.7950220108032227,
            "window_index": 49
          },
          {
            "baseline_loss": 2.639850378036499,
            "delta_vs_baseline": -0.1931140422821045,
            "loss": 2.4467363357543945,
            "window_index": 50
          },
          {
            "baseline_loss": 2.487496852874756,
            "delta_vs_baseline": -0.13882970809936523,
            "loss": 2.3486671447753906,
            "window_index": 51
          },
          {
            "baseline_loss": 2.708131790161133,
            "delta_vs_baseline": -0.29099464416503906,
            "loss": 2.4171371459960938,
            "window_index": 52
          },
          {
            "baseline_loss": 2.8870315551757812,
            "delta_vs_baseline": -0.2884495258331299,
            "loss": 2.5985820293426514,
            "window_index": 53
          },
          {
            "baseline_loss": 3.0955796241760254,
            "delta_vs_baseline": -0.23436403274536133,
            "loss": 2.861215591430664,
            "window_index": 54
          },
          {
            "baseline_loss": 2.8854877948760986,
            "delta_vs_baseline": -0.20693421363830566,
            "loss": 2.678553581237793,
            "window_index": 55
          },
          {
            "baseline_loss": 2.886323928833008,
            "delta_vs_baseline": -0.275388240814209,
            "loss": 2.610935688018799,
            "window_index": 56
          },
          {
            "baseline_loss": 2.957814931869507,
            "delta_vs_baseline": -0.38639187812805176,
            "loss": 2.571423053741455,
            "window_index": 57
          },
          {
            "baseline_loss": 2.8409440517425537,
            "delta_vs_baseline": -0.13218903541564941,
            "loss": 2.7087550163269043,
            "window_index": 58
          },
          {
            "baseline_loss": 2.849606513977051,
            "delta_vs_baseline": -0.25376462936401367,
            "loss": 2.595841884613037,
            "window_index": 59
          },
          {
            "baseline_loss": 2.8881561756134033,
            "delta_vs_baseline": -0.3677175045013428,
            "loss": 2.5204386711120605,
            "window_index": 60
          },
          {
            "baseline_loss": 2.9310176372528076,
            "delta_vs_baseline": -0.2365267276763916,
            "loss": 2.694490909576416,
            "window_index": 61
          },
          {
            "baseline_loss": 3.1954236030578613,
            "delta_vs_baseline": -0.28293275833129883,
            "loss": 2.9124908447265625,
            "window_index": 62
          },
          {
            "baseline_loss": 2.7894527912139893,
            "delta_vs_baseline": -0.3583564758300781,
            "loss": 2.431096315383911,
            "window_index": 63
          },
          {
            "baseline_loss": 2.7355093955993652,
            "delta_vs_baseline": -0.0127716064453125,
            "loss": 2.7227377891540527,
            "window_index": 64
          },
          {
            "baseline_loss": 2.6845948696136475,
            "delta_vs_baseline": -0.16730690002441406,
            "loss": 2.5172879695892334,
            "window_index": 65
          },
          {
            "baseline_loss": 3.225579261779785,
            "delta_vs_baseline": -0.480576753616333,
            "loss": 2.745002508163452,
            "window_index": 66
          },
          {
            "baseline_loss": 2.9965693950653076,
            "delta_vs_baseline": -0.11898231506347656,
            "loss": 2.877587080001831,
            "window_index": 67
          },
          {
            "baseline_loss": 2.7195029258728027,
            "delta_vs_baseline": -0.3126382827758789,
            "loss": 2.406864643096924,
            "window_index": 68
          },
          {
            "baseline_loss": 2.9124796390533447,
            "delta_vs_baseline": -0.17789196968078613,
            "loss": 2.7345876693725586,
            "window_index": 69
          },
          {
            "baseline_loss": 3.2319014072418213,
            "delta_vs_baseline": -0.3599512577056885,
            "loss": 2.871950149536133,
            "window_index": 70
          },
          {
            "baseline_loss": 2.8929831981658936,
            "delta_vs_baseline": -0.1766529083251953,
            "loss": 2.7163302898406982,
            "window_index": 71
          },
          {
            "baseline_loss": 3.253342866897583,
            "delta_vs_baseline": -0.37687087059020996,
            "loss": 2.876471996307373,
            "window_index": 72
          },
          {
            "baseline_loss": 3.1915409564971924,
            "delta_vs_baseline": -0.23905515670776367,
            "loss": 2.9524857997894287,
            "window_index": 73
          },
          {
            "baseline_loss": 2.7452118396759033,
            "delta_vs_baseline": -0.2935831546783447,
            "loss": 2.4516286849975586,
            "window_index": 74
          },
          {
            "baseline_loss": 2.888545513153076,
            "delta_vs_baseline": -0.23366498947143555,
            "loss": 2.6548805236816406,
            "window_index": 75
          },
          {
            "baseline_loss": 2.8269476890563965,
            "delta_vs_baseline": -0.2542836666107178,
            "loss": 2.5726640224456787,
            "window_index": 76
          },
          {
            "baseline_loss": 3.2102153301239014,
            "delta_vs_baseline": -0.0653533935546875,
            "loss": 3.144861936569214,
            "window_index": 77
          },
          {
            "baseline_loss": 2.439115285873413,
            "delta_vs_baseline": -0.06631183624267578,
            "loss": 2.3728034496307373,
            "window_index": 78
          },
          {
            "baseline_loss": 3.13478684425354,
            "delta_vs_baseline": -0.24906158447265625,
            "loss": 2.885725259780884,
            "window_index": 79
          },
          {
            "baseline_loss": 2.9935171604156494,
            "delta_vs_baseline": -0.1947484016418457,
            "loss": 2.7987687587738037,
            "window_index": 80
          },
          {
            "baseline_loss": 3.124610662460327,
            "delta_vs_baseline": -0.33664369583129883,
            "loss": 2.7879669666290283,
            "window_index": 81
          },
          {
            "baseline_loss": 2.723752498626709,
            "delta_vs_baseline": -0.13193941116333008,
            "loss": 2.591813087463379,
            "window_index": 82
          },
          {
            "baseline_loss": 2.757559299468994,
            "delta_vs_baseline": -0.10305428504943848,
            "loss": 2.6545050144195557,
            "window_index": 83
          },
          {
            "baseline_loss": 2.790419340133667,
            "delta_vs_baseline": -0.23160433769226074,
            "loss": 2.5588150024414062,
            "window_index": 84
          },
          {
            "baseline_loss": 2.5810930728912354,
            "delta_vs_baseline": -0.2807762622833252,
            "loss": 2.30031681060791,
            "window_index": 85
          },
          {
            "baseline_loss": 3.3501040935516357,
            "delta_vs_baseline": -0.39803242683410645,
            "loss": 2.9520716667175293,
            "window_index": 86
          },
          {
            "baseline_loss": 2.985410213470459,
            "delta_vs_baseline": -0.3316807746887207,
            "loss": 2.6537294387817383,
            "window_index": 87
          },
          {
            "baseline_loss": 2.7511179447174072,
            "delta_vs_baseline": -0.2991359233856201,
            "loss": 2.451982021331787,
            "window_index": 88
          },
          {
            "baseline_loss": 3.147357225418091,
            "delta_vs_baseline": -0.3830573558807373,
            "loss": 2.7642998695373535,
            "window_index": 89
          },
          {
            "baseline_loss": 3.229327917098999,
            "delta_vs_baseline": -0.29132676124572754,
            "loss": 2.9380011558532715,
            "window_index": 90
          },
          {
            "baseline_loss": 2.8613240718841553,
            "delta_vs_baseline": -0.2797660827636719,
            "loss": 2.5815579891204834,
            "window_index": 91
          },
          {
            "baseline_loss": 2.696187734603882,
            "delta_vs_baseline": -0.3500814437866211,
            "loss": 2.3461062908172607,
            "window_index": 92
          },
          {
            "baseline_loss": 2.9458367824554443,
            "delta_vs_baseline": -0.3338925838470459,
            "loss": 2.6119441986083984,
            "window_index": 93
          },
          {
            "baseline_loss": 2.9736671447753906,
            "delta_vs_baseline": -0.07702994346618652,
            "loss": 2.896637201309204,
            "window_index": 94
          },
          {
            "baseline_loss": 2.747361660003662,
            "delta_vs_baseline": -0.045456886291503906,
            "loss": 2.701904773712158,
            "window_index": 95
          },
          {
            "baseline_loss": 2.9285504817962646,
            "delta_vs_baseline": -0.2531437873840332,
            "loss": 2.6754066944122314,
            "window_index": 96
          },
          {
            "baseline_loss": 3.183176279067993,
            "delta_vs_baseline": -0.20314359664916992,
            "loss": 2.9800326824188232,
            "window_index": 97
          },
          {
            "baseline_loss": 2.5617079734802246,
            "delta_vs_baseline": -0.19913244247436523,
            "loss": 2.3625755310058594,
            "window_index": 98
          },
          {
            "baseline_loss": 3.026214599609375,
            "delta_vs_baseline": -0.2880704402923584,
            "loss": 2.7381441593170166,
            "window_index": 99
          },
          {
            "baseline_loss": 3.2600483894348145,
            "delta_vs_baseline": -0.37528443336486816,
            "loss": 2.8847639560699463,
            "window_index": 100
          },
          {
            "baseline_loss": 2.9374611377716064,
            "delta_vs_baseline": -0.25940752029418945,
            "loss": 2.678053617477417,
            "window_index": 101
          },
          {
            "baseline_loss": 2.9559378623962402,
            "delta_vs_baseline": -0.26925110816955566,
            "loss": 2.6866867542266846,
            "window_index": 102
          },
          {
            "baseline_loss": 3.020036220550537,
            "delta_vs_baseline": -0.351794958114624,
            "loss": 2.668241262435913,
            "window_index": 103
          },
          {
            "baseline_loss": 3.088770866394043,
            "delta_vs_baseline": -0.23656344413757324,
            "loss": 2.8522074222564697,
            "window_index": 104
          },
          {
            "baseline_loss": 2.8664493560791016,
            "delta_vs_baseline": -0.12566256523132324,
            "loss": 2.7407867908477783,
            "window_index": 105
          },
          {
            "baseline_loss": 2.9487314224243164,
            "delta_vs_baseline": -0.23132991790771484,
            "loss": 2.7174015045166016,
            "window_index": 106
          },
          {
            "baseline_loss": 2.9448704719543457,
            "delta_vs_baseline": -0.22147798538208008,
            "loss": 2.7233924865722656,
            "window_index": 107
          },
          {
            "baseline_loss": 2.833847761154175,
            "delta_vs_baseline": -0.22725677490234375,
            "loss": 2.606590986251831,
            "window_index": 108
          },
          {
            "baseline_loss": 3.0840413570404053,
            "delta_vs_baseline": -0.2811086177825928,
            "loss": 2.8029327392578125,
            "window_index": 109
          },
          {
            "baseline_loss": 3.0566482543945312,
            "delta_vs_baseline": -0.03704690933227539,
            "loss": 3.019601345062256,
            "window_index": 110
          },
          {
            "baseline_loss": 3.0592665672302246,
            "delta_vs_baseline": -0.28273987770080566,
            "loss": 2.776526689529419,
            "window_index": 111
          },
          {
            "baseline_loss": 2.9259722232818604,
            "delta_vs_baseline": -0.3109090328216553,
            "loss": 2.615063190460205,
            "window_index": 112
          },
          {
            "baseline_loss": 3.1105833053588867,
            "delta_vs_baseline": -0.3133103847503662,
            "loss": 2.7972729206085205,
            "window_index": 113
          },
          {
            "baseline_loss": 2.762549877166748,
            "delta_vs_baseline": -0.21126818656921387,
            "loss": 2.551281690597534,
            "window_index": 114
          },
          {
            "baseline_loss": 3.0378577709198,
            "delta_vs_baseline": -0.3056325912475586,
            "loss": 2.732225179672241,
            "window_index": 115
          },
          {
            "baseline_loss": 3.0677103996276855,
            "delta_vs_baseline": -0.17482280731201172,
            "loss": 2.892887592315674,
            "window_index": 116
          },
          {
            "baseline_loss": 2.8927221298217773,
            "delta_vs_baseline": -0.11218976974487305,
            "loss": 2.7805323600769043,
            "window_index": 117
          },
          {
            "baseline_loss": 3.42633056640625,
            "delta_vs_baseline": -0.3778359889984131,
            "loss": 3.048494577407837,
            "window_index": 118
          },
          {
            "baseline_loss": 2.779985189437866,
            "delta_vs_baseline": -0.25911664962768555,
            "loss": 2.5208685398101807,
            "window_index": 119
          },
          {
            "baseline_loss": 2.5664048194885254,
            "delta_vs_baseline": -0.2324385643005371,
            "loss": 2.3339662551879883,
            "window_index": 120
          },
          {
            "baseline_loss": 2.9053828716278076,
            "delta_vs_baseline": -0.17789149284362793,
            "loss": 2.7274913787841797,
            "window_index": 121
          },
          {
            "baseline_loss": 2.8783071041107178,
            "delta_vs_baseline": -0.22568130493164062,
            "loss": 2.652625799179077,
            "window_index": 122
          },
          {
            "baseline_loss": 2.7440104484558105,
            "delta_vs_baseline": -0.1193077564239502,
            "loss": 2.6247026920318604,
            "window_index": 123
          },
          {
            "baseline_loss": 3.080070734024048,
            "delta_vs_baseline": -0.26351070404052734,
            "loss": 2.8165600299835205,
            "window_index": 124
          },
          {
            "baseline_loss": 2.944106101989746,
            "delta_vs_baseline": -0.16456103324890137,
            "loss": 2.7795450687408447,
            "window_index": 125
          },
          {
            "baseline_loss": 3.7518718242645264,
            "delta_vs_baseline": -0.5036787986755371,
            "loss": 3.2481930255889893,
            "window_index": 126
          },
          {
            "baseline_loss": 2.967647075653076,
            "delta_vs_baseline": -0.3581821918487549,
            "loss": 2.6094648838043213,
            "window_index": 127
          },
          {
            "baseline_loss": 2.798103094100952,
            "delta_vs_baseline": -0.09517168998718262,
            "loss": 2.7029314041137695,
            "window_index": 128
          },
          {
            "baseline_loss": 4.579283237457275,
            "delta_vs_baseline": -0.5597448348999023,
            "loss": 4.019538402557373,
            "window_index": 129
          },
          {
            "baseline_loss": 8.379351615905762,
            "delta_vs_baseline": -2.3135175704956055,
            "loss": 6.065834045410156,
            "window_index": 130
          },
          {
            "baseline_loss": 2.477597713470459,
            "delta_vs_baseline": -0.13090014457702637,
            "loss": 2.3466975688934326,
            "window_index": 131
          },
          {
            "baseline_loss": 3.072523832321167,
            "delta_vs_baseline": -0.26721978187561035,
            "loss": 2.8053040504455566,
            "window_index": 132
          },
          {
            "baseline_loss": 2.88889479637146,
            "delta_vs_baseline": -0.05999612808227539,
            "loss": 2.8288986682891846,
            "window_index": 133
          },
          {
            "baseline_loss": 2.657388210296631,
            "delta_vs_baseline": -0.07555484771728516,
            "loss": 2.5818333625793457,
            "window_index": 134
          },
          {
            "baseline_loss": 3.222710132598877,
            "delta_vs_baseline": -0.3464493751525879,
            "loss": 2.876260757446289,
            "window_index": 135
          },
          {
            "baseline_loss": 2.594160318374634,
            "delta_vs_baseline": -0.19405007362365723,
            "loss": 2.4001102447509766,
            "window_index": 136
          },
          {
            "baseline_loss": 2.761676549911499,
            "delta_vs_baseline": -0.20832419395446777,
            "loss": 2.5533523559570312,
            "window_index": 137
          },
          {
            "baseline_loss": 3.063735246658325,
            "delta_vs_baseline": -0.3472411632537842,
            "loss": 2.716494083404541,
            "window_index": 138
          },
          {
            "baseline_loss": 3.095252275466919,
            "delta_vs_baseline": -0.32677197456359863,
            "loss": 2.7684803009033203,
            "window_index": 139
          },
          {
            "baseline_loss": 3.001328706741333,
            "delta_vs_baseline": -0.14543414115905762,
            "loss": 2.8558945655822754,
            "window_index": 140
          },
          {
            "baseline_loss": 3.124728202819824,
            "delta_vs_baseline": -0.32863783836364746,
            "loss": 2.7960903644561768,
            "window_index": 141
          },
          {
            "baseline_loss": 3.071362257003784,
            "delta_vs_baseline": -0.25243616104125977,
            "loss": 2.8189260959625244,
            "window_index": 142
          },
          {
            "baseline_loss": 2.8115036487579346,
            "delta_vs_baseline": -0.2495410442352295,
            "loss": 2.561962604522705,
            "window_index": 143
          },
          {
            "baseline_loss": 2.6746327877044678,
            "delta_vs_baseline": -0.11381840705871582,
            "loss": 2.560814380645752,
            "window_index": 144
          },
          {
            "baseline_loss": 2.9380056858062744,
            "delta_vs_baseline": -0.34433817863464355,
            "loss": 2.593667507171631,
            "window_index": 145
          },
          {
            "baseline_loss": 3.0988097190856934,
            "delta_vs_baseline": -0.16121530532836914,
            "loss": 2.937594413757324,
            "window_index": 146
          },
          {
            "baseline_loss": 2.920891761779785,
            "delta_vs_baseline": -0.1380019187927246,
            "loss": 2.7828898429870605,
            "window_index": 147
          },
          {
            "baseline_loss": 3.0000956058502197,
            "delta_vs_baseline": -0.18489885330200195,
            "loss": 2.8151967525482178,
            "window_index": 148
          },
          {
            "baseline_loss": 3.14078688621521,
            "delta_vs_baseline": -0.3547632694244385,
            "loss": 2.7860236167907715,
            "window_index": 149
          },
          {
            "baseline_loss": 3.0242533683776855,
            "delta_vs_baseline": -0.07145023345947266,
            "loss": 2.952803134918213,
            "window_index": 150
          },
          {
            "baseline_loss": 3.2188079357147217,
            "delta_vs_baseline": -0.19174480438232422,
            "loss": 3.0270631313323975,
            "window_index": 151
          },
          {
            "baseline_loss": 2.875241756439209,
            "delta_vs_baseline": -0.30200958251953125,
            "loss": 2.5732321739196777,
            "window_index": 152
          },
          {
            "baseline_loss": 2.890204668045044,
            "delta_vs_baseline": -0.10086774826049805,
            "loss": 2.789336919784546,
            "window_index": 153
          },
          {
            "baseline_loss": 2.5632436275482178,
            "delta_vs_baseline": -0.18002009391784668,
            "loss": 2.383223533630371,
            "window_index": 154
          },
          {
            "baseline_loss": 3.276603937149048,
            "delta_vs_baseline": -0.2922687530517578,
            "loss": 2.98433518409729,
            "window_index": 155
          },
          {
            "baseline_loss": 2.8790481090545654,
            "delta_vs_baseline": -0.33109402656555176,
            "loss": 2.5479540824890137,
            "window_index": 156
          },
          {
            "baseline_loss": 3.015944242477417,
            "delta_vs_baseline": -0.1938004493713379,
            "loss": 2.822143793106079,
            "window_index": 157
          },
          {
            "baseline_loss": 3.1061058044433594,
            "delta_vs_baseline": -0.27899932861328125,
            "loss": 2.827106475830078,
            "window_index": 158
          },
          {
            "baseline_loss": 2.731477975845337,
            "delta_vs_baseline": -0.21410632133483887,
            "loss": 2.517371654510498,
            "window_index": 159
          },
          {
            "baseline_loss": 2.7437946796417236,
            "delta_vs_baseline": -0.3022482395172119,
            "loss": 2.4415464401245117,
            "window_index": 160
          },
          {
            "baseline_loss": 3.6713614463806152,
            "delta_vs_baseline": -0.617048978805542,
            "loss": 3.0543124675750732,
            "window_index": 161
          },
          {
            "baseline_loss": 3.0516977310180664,
            "delta_vs_baseline": -0.4199991226196289,
            "loss": 2.6316986083984375,
            "window_index": 162
          },
          {
            "baseline_loss": 3.183318614959717,
            "delta_vs_baseline": -0.2781507968902588,
            "loss": 2.905167818069458,
            "window_index": 163
          },
          {
            "baseline_loss": 2.829756021499634,
            "delta_vs_baseline": -0.10513997077941895,
            "loss": 2.724616050720215,
            "window_index": 164
          },
          {
            "baseline_loss": 2.694065809249878,
            "delta_vs_baseline": -0.07249236106872559,
            "loss": 2.6215734481811523,
            "window_index": 165
          },
          {
            "baseline_loss": 3.1200010776519775,
            "delta_vs_baseline": -0.2686166763305664,
            "loss": 2.851384401321411,
            "window_index": 166
          },
          {
            "baseline_loss": 3.0029048919677734,
            "delta_vs_baseline": -0.20938706398010254,
            "loss": 2.793517827987671,
            "window_index": 167
          },
          {
            "baseline_loss": 3.049888849258423,
            "delta_vs_baseline": -0.16392874717712402,
            "loss": 2.885960102081299,
            "window_index": 168
          },
          {
            "baseline_loss": 2.74784255027771,
            "delta_vs_baseline": -0.2016010284423828,
            "loss": 2.546241521835327,
            "window_index": 169
          },
          {
            "baseline_loss": 2.7892608642578125,
            "delta_vs_baseline": -0.24160170555114746,
            "loss": 2.547659158706665,
            "window_index": 170
          },
          {
            "baseline_loss": 3.56272029876709,
            "delta_vs_baseline": -0.4287717342376709,
            "loss": 3.133948564529419,
            "window_index": 171
          },
          {
            "baseline_loss": 3.123473644256592,
            "delta_vs_baseline": -0.28661656379699707,
            "loss": 2.8368570804595947,
            "window_index": 172
          },
          {
            "baseline_loss": 3.0645110607147217,
            "delta_vs_baseline": -0.42151951789855957,
            "loss": 2.642991542816162,
            "window_index": 173
          },
          {
            "baseline_loss": 2.488665819168091,
            "delta_vs_baseline": -0.08430314064025879,
            "loss": 2.404362678527832,
            "window_index": 174
          },
          {
            "baseline_loss": 3.198608875274658,
            "delta_vs_baseline": -0.2577476501464844,
            "loss": 2.940861225128174,
            "window_index": 175
          },
          {
            "baseline_loss": 2.749643325805664,
            "delta_vs_baseline": -0.21956706047058105,
            "loss": 2.530076265335083,
            "window_index": 176
          },
          {
            "baseline_loss": 3.1345784664154053,
            "delta_vs_baseline": -0.3661024570465088,
            "loss": 2.7684760093688965,
            "window_index": 177
          },
          {
            "baseline_loss": 3.0150883197784424,
            "delta_vs_baseline": -0.12660932540893555,
            "loss": 2.888478994369507,
            "window_index": 178
          },
          {
            "baseline_loss": 2.964832305908203,
            "delta_vs_baseline": -0.22452163696289062,
            "loss": 2.7403106689453125,
            "window_index": 179
          },
          {
            "baseline_loss": 2.8198471069335938,
            "delta_vs_baseline": -0.16181492805480957,
            "loss": 2.658032178878784,
            "window_index": 180
          },
          {
            "baseline_loss": 2.734243869781494,
            "delta_vs_baseline": -0.2075943946838379,
            "loss": 2.5266494750976562,
            "window_index": 181
          },
          {
            "baseline_loss": 3.057004451751709,
            "delta_vs_baseline": -0.18724918365478516,
            "loss": 2.869755268096924,
            "window_index": 182
          },
          {
            "baseline_loss": 2.6313588619232178,
            "delta_vs_baseline": -0.1671137809753418,
            "loss": 2.464245080947876,
            "window_index": 183
          },
          {
            "baseline_loss": 2.712092161178589,
            "delta_vs_baseline": -0.31253504753112793,
            "loss": 2.399557113647461,
            "window_index": 184
          },
          {
            "baseline_loss": 3.1154446601867676,
            "delta_vs_baseline": -0.27259159088134766,
            "loss": 2.84285306930542,
            "window_index": 185
          },
          {
            "baseline_loss": 2.9323294162750244,
            "delta_vs_baseline": -0.3515298366546631,
            "loss": 2.5807995796203613,
            "window_index": 186
          },
          {
            "baseline_loss": 2.799142837524414,
            "delta_vs_baseline": -0.22760844230651855,
            "loss": 2.5715343952178955,
            "window_index": 187
          },
          {
            "baseline_loss": 2.6941280364990234,
            "delta_vs_baseline": -0.0376591682434082,
            "loss": 2.6564688682556152,
            "window_index": 188
          },
          {
            "baseline_loss": 2.839932441711426,
            "delta_vs_baseline": -0.16369056701660156,
            "loss": 2.676241874694824,
            "window_index": 189
          },
          {
            "baseline_loss": 3.0761919021606445,
            "delta_vs_baseline": -0.2910473346710205,
            "loss": 2.785144567489624,
            "window_index": 190
          },
          {
            "baseline_loss": 2.7878189086914062,
            "delta_vs_baseline": -0.4246993064880371,
            "loss": 2.363119602203369,
            "window_index": 191
          },
          {
            "baseline_loss": 2.6268908977508545,
            "delta_vs_baseline": -0.1884324550628662,
            "loss": 2.4384584426879883,
            "window_index": 192
          },
          {
            "baseline_loss": 2.9380271434783936,
            "delta_vs_baseline": -0.4652884006500244,
            "loss": 2.472738742828369,
            "window_index": 193
          },
          {
            "baseline_loss": 2.3056321144104004,
            "delta_vs_baseline": -0.2568080425262451,
            "loss": 2.0488240718841553,
            "window_index": 194
          },
          {
            "baseline_loss": 2.9026896953582764,
            "delta_vs_baseline": -0.33960413932800293,
            "loss": 2.5630855560302734,
            "window_index": 195
          },
          {
            "baseline_loss": 2.7789411544799805,
            "delta_vs_baseline": -0.439528226852417,
            "loss": 2.3394129276275635,
            "window_index": 196
          },
          {
            "baseline_loss": 2.5273962020874023,
            "delta_vs_baseline": -0.03116917610168457,
            "loss": 2.4962270259857178,
            "window_index": 197
          },
          {
            "baseline_loss": 2.603788137435913,
            "delta_vs_baseline": -0.3622710704803467,
            "loss": 2.2415170669555664,
            "window_index": 198
          },
          {
            "baseline_loss": 2.6679775714874268,
            "delta_vs_baseline": -0.22269892692565918,
            "loss": 2.4452786445617676,
            "window_index": 199
          }
        ],
        "training_window_style_final_checkpoint": [
          {
            "baseline_loss": 2.488567590713501,
            "delta_vs_baseline": -0.12622833251953125,
            "loss": 2.3623392581939697,
            "step": 400
          },
          {
            "baseline_loss": 2.6633172035217285,
            "delta_vs_baseline": -0.16783785820007324,
            "loss": 2.4954793453216553,
            "step": 800
          },
          {
            "baseline_loss": 2.646700859069824,
            "delta_vs_baseline": -0.13427257537841797,
            "loss": 2.5124282836914062,
            "step": 1200
          },
          {
            "baseline_loss": 2.646510124206543,
            "delta_vs_baseline": -0.1245412826538086,
            "loss": 2.5219688415527344,
            "step": 1600
          },
          {
            "baseline_loss": 2.54093074798584,
            "delta_vs_baseline": -0.19237279891967773,
            "loss": 2.348557949066162,
            "step": 2000
          },
          {
            "baseline_loss": 2.822401523590088,
            "delta_vs_baseline": -0.23374342918395996,
            "loss": 2.588658094406128,
            "step": 2400
          },
          {
            "baseline_loss": 2.4011733531951904,
            "delta_vs_baseline": -0.16025781631469727,
            "loss": 2.240915536880493,
            "step": 2800
          },
          {
            "baseline_loss": 2.6783716678619385,
            "delta_vs_baseline": -0.10412192344665527,
            "loss": 2.574249744415283,
            "step": 3200
          },
          {
            "baseline_loss": 8.865436553955078,
            "delta_vs_baseline": 2.7385520935058594,
            "loss": 11.603988647460938,
            "step": 3600
          },
          {
            "baseline_loss": 11.067703247070312,
            "delta_vs_baseline": 3.838240623474121,
            "loss": 14.905943870544434,
            "step": 4000
          }
        ]
      },
      "recorded_during_training_eval_curve": {
        "loss_variance": 19.522144046013256,
        "mean_loss": 4.985433840751648,
        "path": "benchmark/reports/generated/ean_init_300m_repeat_seed_42/pvr_ec_o_full_300m_shared_trunk_init_v1_scope_embeddings_attention_norms_seed_42/eval_curve.json",
        "window_count": 10,
        "windows": [
          {
            "eval_loss": 3.1041862964630127,
            "eval_tokens": 128,
            "optimizer_step": 400,
            "step": 400,
            "training_tokens_seen": 102400
          },
          {
            "eval_loss": 3.461364984512329,
            "eval_tokens": 128,
            "optimizer_step": 800,
            "step": 800,
            "training_tokens_seen": 204800
          },
          {
            "eval_loss": 2.7160325050354004,
            "eval_tokens": 128,
            "optimizer_step": 1200,
            "step": 1200,
            "training_tokens_seen": 307200
          },
          {
            "eval_loss": 2.6781907081604004,
            "eval_tokens": 128,
            "optimizer_step": 1600,
            "step": 1600,
            "training_tokens_seen": 409600
          },
          {
            "eval_loss": 2.6258883476257324,
            "eval_tokens": 128,
            "optimizer_step": 2000,
            "step": 2000,
            "training_tokens_seen": 512000
          },
          {
            "eval_loss": 2.7640178203582764,
            "eval_tokens": 128,
            "optimizer_step": 2400,
            "step": 2400,
            "training_tokens_seen": 614400
          },
          {
            "eval_loss": 2.4241716861724854,
            "eval_tokens": 128,
            "optimizer_step": 2800,
            "step": 2800,
            "training_tokens_seen": 716800
          },
          {
            "eval_loss": 2.593867063522339,
            "eval_tokens": 128,
            "optimizer_step": 3200,
            "step": 3200,
            "training_tokens_seen": 819200
          },
          {
            "eval_loss": 12.58067512512207,
            "eval_tokens": 128,
            "optimizer_step": 3600,
            "step": 3600,
            "training_tokens_seen": 921600
          },
          {
            "eval_loss": 14.905943870544434,
            "eval_tokens": 128,
            "optimizer_step": 4000,
            "step": 4000,
            "training_tokens_seen": 1024000
          }
        ]
      },
      "same_heldout_tokens": {
        "loss_variance": 1.5081209934039201,
        "mean_loss": 3.010810148715973,
        "scorecard_seq_len": 64,
        "window_count": 200
      },
      "scorecard_lm_loss_recorded": 3.010810148715973,
      "scorecard_style_final_checkpoint": {
        "loss_variance": 1.5081209934039201,
        "max_loss": 10.815953254699707,
        "mean_loss": 3.010810148715973,
        "min_loss": 2.0488240718841553,
        "window_count": 200
      },
      "training_window_style_final_checkpoint": {
        "loss_variance": 19.21616812173678,
        "max_loss": 14.905943870544434,
        "mean_loss": 4.6154529571533205,
        "min_loss": 2.240915536880493,
        "window_count": 10
      }
    },
    "full_copy_seed42": {
      "checkpoint_path": "checkpoints/shared_trunk_init_300m_repeat_seed_42/pvr_ec_o_full_300m_shared_trunk_init_from_dense_seed_42/checkpoint.pt",
      "deltas_vs_pvr_baseline": {
        "recorded_during_training_eval_curve_mean": 0.13120231628417933,
        "scorecard_style_final_checkpoint_mean": -0.40945056557655324,
        "training_window_style_final_checkpoint_mean": 0.542314124107361
      },
      "label": "full_copy_seed42",
      "model_variant": "pvr_ec_o_full_300m_shared_trunk_init_from_dense_seed_42",
      "per_window_deltas_vs_pvr_baseline": {
        "scorecard_style_general": [
          {
            "baseline_loss": 3.3696975708007812,
            "delta_vs_baseline": -0.35471534729003906,
            "loss": 3.014982223510742,
            "window_index": 0
          },
          {
            "baseline_loss": 3.7571780681610107,
            "delta_vs_baseline": -0.6107821464538574,
            "loss": 3.1463959217071533,
            "window_index": 1
          },
          {
            "baseline_loss": 2.744732618331909,
            "delta_vs_baseline": -0.23463773727416992,
            "loss": 2.5100948810577393,
            "window_index": 2
          },
          {
            "baseline_loss": 3.1212172508239746,
            "delta_vs_baseline": -0.270033597946167,
            "loss": 2.8511836528778076,
            "window_index": 3
          },
          {
            "baseline_loss": 3.1811468601226807,
            "delta_vs_baseline": -0.2929701805114746,
            "loss": 2.888176679611206,
            "window_index": 4
          },
          {
            "baseline_loss": 3.6319479942321777,
            "delta_vs_baseline": -0.48581624031066895,
            "loss": 3.146131753921509,
            "window_index": 5
          },
          {
            "baseline_loss": 3.136638641357422,
            "delta_vs_baseline": -0.5376405715942383,
            "loss": 2.5989980697631836,
            "window_index": 6
          },
          {
            "baseline_loss": 2.6240248680114746,
            "delta_vs_baseline": -0.1611948013305664,
            "loss": 2.462830066680908,
            "window_index": 7
          },
          {
            "baseline_loss": 4.648166179656982,
            "delta_vs_baseline": -0.7324855327606201,
            "loss": 3.9156806468963623,
            "window_index": 8
          },
          {
            "baseline_loss": 5.14591121673584,
            "delta_vs_baseline": -0.7613658905029297,
            "loss": 4.38454532623291,
            "window_index": 9
          },
          {
            "baseline_loss": 10.665205001831055,
            "delta_vs_baseline": -3.886838436126709,
            "loss": 6.778366565704346,
            "window_index": 10
          },
          {
            "baseline_loss": 9.66199779510498,
            "delta_vs_baseline": -0.007277488708496094,
            "loss": 9.654720306396484,
            "window_index": 11
          },
          {
            "baseline_loss": 7.029171943664551,
            "delta_vs_baseline": -0.5690884590148926,
            "loss": 6.460083484649658,
            "window_index": 12
          },
          {
            "baseline_loss": 4.451816082000732,
            "delta_vs_baseline": -0.5736100673675537,
            "loss": 3.8782060146331787,
            "window_index": 13
          },
          {
            "baseline_loss": 9.882694244384766,
            "delta_vs_baseline": -5.385023593902588,
            "loss": 4.497670650482178,
            "window_index": 14
          },
          {
            "baseline_loss": 15.704546928405762,
            "delta_vs_baseline": -7.016213417053223,
            "loss": 8.688333511352539,
            "window_index": 15
          },
          {
            "baseline_loss": 7.221086502075195,
            "delta_vs_baseline": -3.43393611907959,
            "loss": 3.7871503829956055,
            "window_index": 16
          },
          {
            "baseline_loss": 8.873090744018555,
            "delta_vs_baseline": -2.1966662406921387,
            "loss": 6.676424503326416,
            "window_index": 17
          },
          {
            "baseline_loss": 6.848356246948242,
            "delta_vs_baseline": -1.6457328796386719,
            "loss": 5.20262336730957,
            "window_index": 18
          },
          {
            "baseline_loss": 10.50163459777832,
            "delta_vs_baseline": 0.3156709671020508,
            "loss": 10.817305564880371,
            "window_index": 19
          },
          {
            "baseline_loss": 8.044512748718262,
            "delta_vs_baseline": -1.294053077697754,
            "loss": 6.750459671020508,
            "window_index": 20
          },
          {
            "baseline_loss": 12.315536499023438,
            "delta_vs_baseline": -2.1446380615234375,
            "loss": 10.1708984375,
            "window_index": 21
          },
          {
            "baseline_loss": 7.905089378356934,
            "delta_vs_baseline": -2.2027978897094727,
            "loss": 5.702291488647461,
            "window_index": 22
          },
          {
            "baseline_loss": 6.56272029876709,
            "delta_vs_baseline": -1.140993595123291,
            "loss": 5.421726703643799,
            "window_index": 23
          },
          {
            "baseline_loss": 2.7679688930511475,
            "delta_vs_baseline": -0.25785088539123535,
            "loss": 2.510118007659912,
            "window_index": 24
          },
          {
            "baseline_loss": 2.9374938011169434,
            "delta_vs_baseline": -0.28359436988830566,
            "loss": 2.6538994312286377,
            "window_index": 25
          },
          {
            "baseline_loss": 2.6757943630218506,
            "delta_vs_baseline": -0.16925692558288574,
            "loss": 2.506537437438965,
            "window_index": 26
          },
          {
            "baseline_loss": 2.6266438961029053,
            "delta_vs_baseline": -0.20677685737609863,
            "loss": 2.4198670387268066,
            "window_index": 27
          },
          {
            "baseline_loss": 3.199479103088379,
            "delta_vs_baseline": -0.24264979362487793,
            "loss": 2.956829309463501,
            "window_index": 28
          },
          {
            "baseline_loss": 3.1571550369262695,
            "delta_vs_baseline": -0.3538978099822998,
            "loss": 2.8032572269439697,
            "window_index": 29
          },
          {
            "baseline_loss": 2.9776811599731445,
            "delta_vs_baseline": -0.22481822967529297,
            "loss": 2.7528629302978516,
            "window_index": 30
          },
          {
            "baseline_loss": 3.1856303215026855,
            "delta_vs_baseline": -0.44065403938293457,
            "loss": 2.744976282119751,
            "window_index": 31
          },
          {
            "baseline_loss": 2.8611888885498047,
            "delta_vs_baseline": -0.24077701568603516,
            "loss": 2.6204118728637695,
            "window_index": 32
          },
          {
            "baseline_loss": 2.986649751663208,
            "delta_vs_baseline": -0.27456235885620117,
            "loss": 2.712087392807007,
            "window_index": 33
          },
          {
            "baseline_loss": 3.02950119972229,
            "delta_vs_baseline": -0.19025778770446777,
            "loss": 2.8392434120178223,
            "window_index": 34
          },
          {
            "baseline_loss": 2.630702018737793,
            "delta_vs_baseline": -0.29190492630004883,
            "loss": 2.338797092437744,
            "window_index": 35
          },
          {
            "baseline_loss": 3.0871145725250244,
            "delta_vs_baseline": -0.320514440536499,
            "loss": 2.7666001319885254,
            "window_index": 36
          },
          {
            "baseline_loss": 2.9280953407287598,
            "delta_vs_baseline": -0.20157432556152344,
            "loss": 2.7265210151672363,
            "window_index": 37
          },
          {
            "baseline_loss": 3.1325175762176514,
            "delta_vs_baseline": -0.2741365432739258,
            "loss": 2.8583810329437256,
            "window_index": 38
          },
          {
            "baseline_loss": 2.935246229171753,
            "delta_vs_baseline": -0.2133955955505371,
            "loss": 2.721850633621216,
            "window_index": 39
          },
          {
            "baseline_loss": 3.286637306213379,
            "delta_vs_baseline": -0.45655107498168945,
            "loss": 2.8300862312316895,
            "window_index": 40
          },
          {
            "baseline_loss": 3.0057811737060547,
            "delta_vs_baseline": -0.21694040298461914,
            "loss": 2.7888407707214355,
            "window_index": 41
          },
          {
            "baseline_loss": 2.738572597503662,
            "delta_vs_baseline": -0.33849644660949707,
            "loss": 2.400076150894165,
            "window_index": 42
          },
          {
            "baseline_loss": 3.141986131668091,
            "delta_vs_baseline": -0.30457544326782227,
            "loss": 2.8374106884002686,
            "window_index": 43
          },
          {
            "baseline_loss": 2.8448073863983154,
            "delta_vs_baseline": -0.2912874221801758,
            "loss": 2.5535199642181396,
            "window_index": 44
          },
          {
            "baseline_loss": 3.004800796508789,
            "delta_vs_baseline": -0.2714269161224365,
            "loss": 2.7333738803863525,
            "window_index": 45
          },
          {
            "baseline_loss": 2.9838449954986572,
            "delta_vs_baseline": -0.4635484218597412,
            "loss": 2.520296573638916,
            "window_index": 46
          },
          {
            "baseline_loss": 2.9386417865753174,
            "delta_vs_baseline": -0.30786776542663574,
            "loss": 2.6307740211486816,
            "window_index": 47
          },
          {
            "baseline_loss": 3.1059365272521973,
            "delta_vs_baseline": -0.17507410049438477,
            "loss": 2.9308624267578125,
            "window_index": 48
          },
          {
            "baseline_loss": 3.168769359588623,
            "delta_vs_baseline": -0.3621037006378174,
            "loss": 2.8066656589508057,
            "window_index": 49
          },
          {
            "baseline_loss": 2.639850378036499,
            "delta_vs_baseline": -0.15623950958251953,
            "loss": 2.4836108684539795,
            "window_index": 50
          },
          {
            "baseline_loss": 2.487496852874756,
            "delta_vs_baseline": -0.12542510032653809,
            "loss": 2.3620717525482178,
            "window_index": 51
          },
          {
            "baseline_loss": 2.708131790161133,
            "delta_vs_baseline": -0.2818598747253418,
            "loss": 2.426271915435791,
            "window_index": 52
          },
          {
            "baseline_loss": 2.8870315551757812,
            "delta_vs_baseline": -0.293027400970459,
            "loss": 2.5940041542053223,
            "window_index": 53
          },
          {
            "baseline_loss": 3.0955796241760254,
            "delta_vs_baseline": -0.2406008243560791,
            "loss": 2.8549787998199463,
            "window_index": 54
          },
          {
            "baseline_loss": 2.8854877948760986,
            "delta_vs_baseline": -0.18547511100769043,
            "loss": 2.700012683868408,
            "window_index": 55
          },
          {
            "baseline_loss": 2.886323928833008,
            "delta_vs_baseline": -0.26546573638916016,
            "loss": 2.6208581924438477,
            "window_index": 56
          },
          {
            "baseline_loss": 2.957814931869507,
            "delta_vs_baseline": -0.37847018241882324,
            "loss": 2.5793447494506836,
            "window_index": 57
          },
          {
            "baseline_loss": 2.8409440517425537,
            "delta_vs_baseline": -0.1195533275604248,
            "loss": 2.721390724182129,
            "window_index": 58
          },
          {
            "baseline_loss": 2.849606513977051,
            "delta_vs_baseline": -0.24794363975524902,
            "loss": 2.6016628742218018,
            "window_index": 59
          },
          {
            "baseline_loss": 2.8881561756134033,
            "delta_vs_baseline": -0.365708589553833,
            "loss": 2.5224475860595703,
            "window_index": 60
          },
          {
            "baseline_loss": 2.9310176372528076,
            "delta_vs_baseline": -0.24349474906921387,
            "loss": 2.6875228881835938,
            "window_index": 61
          },
          {
            "baseline_loss": 3.1954236030578613,
            "delta_vs_baseline": -0.30341601371765137,
            "loss": 2.89200758934021,
            "window_index": 62
          },
          {
            "baseline_loss": 2.7894527912139893,
            "delta_vs_baseline": -0.3685128688812256,
            "loss": 2.4209399223327637,
            "window_index": 63
          },
          {
            "baseline_loss": 2.7355093955993652,
            "delta_vs_baseline": -0.019027233123779297,
            "loss": 2.716482162475586,
            "window_index": 64
          },
          {
            "baseline_loss": 2.6845948696136475,
            "delta_vs_baseline": -0.16627120971679688,
            "loss": 2.5183236598968506,
            "window_index": 65
          },
          {
            "baseline_loss": 3.225579261779785,
            "delta_vs_baseline": -0.4642472267150879,
            "loss": 2.7613320350646973,
            "window_index": 66
          },
          {
            "baseline_loss": 2.9965693950653076,
            "delta_vs_baseline": -0.11696600914001465,
            "loss": 2.879603385925293,
            "window_index": 67
          },
          {
            "baseline_loss": 2.7195029258728027,
            "delta_vs_baseline": -0.32524871826171875,
            "loss": 2.394254207611084,
            "window_index": 68
          },
          {
            "baseline_loss": 2.9124796390533447,
            "delta_vs_baseline": -0.18148207664489746,
            "loss": 2.7309975624084473,
            "window_index": 69
          },
          {
            "baseline_loss": 3.2319014072418213,
            "delta_vs_baseline": -0.3711509704589844,
            "loss": 2.860750436782837,
            "window_index": 70
          },
          {
            "baseline_loss": 2.8929831981658936,
            "delta_vs_baseline": -0.18003344535827637,
            "loss": 2.712949752807617,
            "window_index": 71
          },
          {
            "baseline_loss": 3.253342866897583,
            "delta_vs_baseline": -0.3509237766265869,
            "loss": 2.902419090270996,
            "window_index": 72
          },
          {
            "baseline_loss": 3.1915409564971924,
            "delta_vs_baseline": -0.22723698616027832,
            "loss": 2.964303970336914,
            "window_index": 73
          },
          {
            "baseline_loss": 2.7452118396759033,
            "delta_vs_baseline": -0.31055712699890137,
            "loss": 2.434654712677002,
            "window_index": 74
          },
          {
            "baseline_loss": 2.888545513153076,
            "delta_vs_baseline": -0.22687387466430664,
            "loss": 2.6616716384887695,
            "window_index": 75
          },
          {
            "baseline_loss": 2.8269476890563965,
            "delta_vs_baseline": -0.2618222236633301,
            "loss": 2.5651254653930664,
            "window_index": 76
          },
          {
            "baseline_loss": 3.2102153301239014,
            "delta_vs_baseline": -0.06484436988830566,
            "loss": 3.1453709602355957,
            "window_index": 77
          },
          {
            "baseline_loss": 2.439115285873413,
            "delta_vs_baseline": -0.04629111289978027,
            "loss": 2.392824172973633,
            "window_index": 78
          },
          {
            "baseline_loss": 3.13478684425354,
            "delta_vs_baseline": -0.24477934837341309,
            "loss": 2.890007495880127,
            "window_index": 79
          },
          {
            "baseline_loss": 2.9935171604156494,
            "delta_vs_baseline": -0.2320573329925537,
            "loss": 2.7614598274230957,
            "window_index": 80
          },
          {
            "baseline_loss": 3.124610662460327,
            "delta_vs_baseline": -0.3407707214355469,
            "loss": 2.7838399410247803,
            "window_index": 81
          },
          {
            "baseline_loss": 2.723752498626709,
            "delta_vs_baseline": -0.15384268760681152,
            "loss": 2.5699098110198975,
            "window_index": 82
          },
          {
            "baseline_loss": 2.757559299468994,
            "delta_vs_baseline": -0.08045578002929688,
            "loss": 2.6771035194396973,
            "window_index": 83
          },
          {
            "baseline_loss": 2.790419340133667,
            "delta_vs_baseline": -0.21120142936706543,
            "loss": 2.5792179107666016,
            "window_index": 84
          },
          {
            "baseline_loss": 2.5810930728912354,
            "delta_vs_baseline": -0.2751429080963135,
            "loss": 2.305950164794922,
            "window_index": 85
          },
          {
            "baseline_loss": 3.3501040935516357,
            "delta_vs_baseline": -0.399524450302124,
            "loss": 2.9505796432495117,
            "window_index": 86
          },
          {
            "baseline_loss": 2.985410213470459,
            "delta_vs_baseline": -0.3193533420562744,
            "loss": 2.6660568714141846,
            "window_index": 87
          },
          {
            "baseline_loss": 2.7511179447174072,
            "delta_vs_baseline": -0.29903364181518555,
            "loss": 2.4520843029022217,
            "window_index": 88
          },
          {
            "baseline_loss": 3.147357225418091,
            "delta_vs_baseline": -0.39698195457458496,
            "loss": 2.750375270843506,
            "window_index": 89
          },
          {
            "baseline_loss": 3.229327917098999,
            "delta_vs_baseline": -0.2880072593688965,
            "loss": 2.9413206577301025,
            "window_index": 90
          },
          {
            "baseline_loss": 2.8613240718841553,
            "delta_vs_baseline": -0.2829930782318115,
            "loss": 2.5783309936523438,
            "window_index": 91
          },
          {
            "baseline_loss": 2.696187734603882,
            "delta_vs_baseline": -0.34902024269104004,
            "loss": 2.347167491912842,
            "window_index": 92
          },
          {
            "baseline_loss": 2.9458367824554443,
            "delta_vs_baseline": -0.32915544509887695,
            "loss": 2.6166813373565674,
            "window_index": 93
          },
          {
            "baseline_loss": 2.9736671447753906,
            "delta_vs_baseline": -0.09641003608703613,
            "loss": 2.8772571086883545,
            "window_index": 94
          },
          {
            "baseline_loss": 2.747361660003662,
            "delta_vs_baseline": -0.05240774154663086,
            "loss": 2.6949539184570312,
            "window_index": 95
          },
          {
            "baseline_loss": 2.9285504817962646,
            "delta_vs_baseline": -0.2671806812286377,
            "loss": 2.661369800567627,
            "window_index": 96
          },
          {
            "baseline_loss": 3.183176279067993,
            "delta_vs_baseline": -0.22191643714904785,
            "loss": 2.9612598419189453,
            "window_index": 97
          },
          {
            "baseline_loss": 2.5617079734802246,
            "delta_vs_baseline": -0.1918025016784668,
            "loss": 2.369905471801758,
            "window_index": 98
          },
          {
            "baseline_loss": 3.026214599609375,
            "delta_vs_baseline": -0.2896761894226074,
            "loss": 2.7365384101867676,
            "window_index": 99
          },
          {
            "baseline_loss": 3.2600483894348145,
            "delta_vs_baseline": -0.3742332458496094,
            "loss": 2.885815143585205,
            "window_index": 100
          },
          {
            "baseline_loss": 2.9374611377716064,
            "delta_vs_baseline": -0.2572464942932129,
            "loss": 2.6802146434783936,
            "window_index": 101
          },
          {
            "baseline_loss": 2.9559378623962402,
            "delta_vs_baseline": -0.2642066478729248,
            "loss": 2.6917312145233154,
            "window_index": 102
          },
          {
            "baseline_loss": 3.020036220550537,
            "delta_vs_baseline": -0.33997416496276855,
            "loss": 2.6800620555877686,
            "window_index": 103
          },
          {
            "baseline_loss": 3.088770866394043,
            "delta_vs_baseline": -0.22660303115844727,
            "loss": 2.8621678352355957,
            "window_index": 104
          },
          {
            "baseline_loss": 2.8664493560791016,
            "delta_vs_baseline": -0.12925267219543457,
            "loss": 2.737196683883667,
            "window_index": 105
          },
          {
            "baseline_loss": 2.9487314224243164,
            "delta_vs_baseline": -0.2490701675415039,
            "loss": 2.6996612548828125,
            "window_index": 106
          },
          {
            "baseline_loss": 2.9448704719543457,
            "delta_vs_baseline": -0.20678472518920898,
            "loss": 2.7380857467651367,
            "window_index": 107
          },
          {
            "baseline_loss": 2.833847761154175,
            "delta_vs_baseline": -0.2338547706604004,
            "loss": 2.5999929904937744,
            "window_index": 108
          },
          {
            "baseline_loss": 3.0840413570404053,
            "delta_vs_baseline": -0.27107715606689453,
            "loss": 2.8129642009735107,
            "window_index": 109
          },
          {
            "baseline_loss": 3.0566482543945312,
            "delta_vs_baseline": -0.04051971435546875,
            "loss": 3.0161285400390625,
            "window_index": 110
          },
          {
            "baseline_loss": 3.0592665672302246,
            "delta_vs_baseline": -0.2964010238647461,
            "loss": 2.7628655433654785,
            "window_index": 111
          },
          {
            "baseline_loss": 2.9259722232818604,
            "delta_vs_baseline": -0.28707313537597656,
            "loss": 2.638899087905884,
            "window_index": 112
          },
          {
            "baseline_loss": 3.1105833053588867,
            "delta_vs_baseline": -0.3187532424926758,
            "loss": 2.791830062866211,
            "window_index": 113
          },
          {
            "baseline_loss": 2.762549877166748,
            "delta_vs_baseline": -0.22661662101745605,
            "loss": 2.535933256149292,
            "window_index": 114
          },
          {
            "baseline_loss": 3.0378577709198,
            "delta_vs_baseline": -0.2985517978668213,
            "loss": 2.7393059730529785,
            "window_index": 115
          },
          {
            "baseline_loss": 3.0677103996276855,
            "delta_vs_baseline": -0.17935609817504883,
            "loss": 2.8883543014526367,
            "window_index": 116
          },
          {
            "baseline_loss": 2.8927221298217773,
            "delta_vs_baseline": -0.09973692893981934,
            "loss": 2.792985200881958,
            "window_index": 117
          },
          {
            "baseline_loss": 3.42633056640625,
            "delta_vs_baseline": -0.37685489654541016,
            "loss": 3.04947566986084,
            "window_index": 118
          },
          {
            "baseline_loss": 2.779985189437866,
            "delta_vs_baseline": -0.24872899055480957,
            "loss": 2.5312561988830566,
            "window_index": 119
          },
          {
            "baseline_loss": 2.5664048194885254,
            "delta_vs_baseline": -0.2391374111175537,
            "loss": 2.3272674083709717,
            "window_index": 120
          },
          {
            "baseline_loss": 2.9053828716278076,
            "delta_vs_baseline": -0.15979719161987305,
            "loss": 2.7455856800079346,
            "window_index": 121
          },
          {
            "baseline_loss": 2.8783071041107178,
            "delta_vs_baseline": -0.2161705493927002,
            "loss": 2.6621365547180176,
            "window_index": 122
          },
          {
            "baseline_loss": 2.7440104484558105,
            "delta_vs_baseline": -0.13451004028320312,
            "loss": 2.6095004081726074,
            "window_index": 123
          },
          {
            "baseline_loss": 3.080070734024048,
            "delta_vs_baseline": -0.26039671897888184,
            "loss": 2.819674015045166,
            "window_index": 124
          },
          {
            "baseline_loss": 2.944106101989746,
            "delta_vs_baseline": -0.15142607688903809,
            "loss": 2.792680025100708,
            "window_index": 125
          },
          {
            "baseline_loss": 3.7518718242645264,
            "delta_vs_baseline": -0.5070705413818359,
            "loss": 3.2448012828826904,
            "window_index": 126
          },
          {
            "baseline_loss": 2.967647075653076,
            "delta_vs_baseline": -0.3429558277130127,
            "loss": 2.6246912479400635,
            "window_index": 127
          },
          {
            "baseline_loss": 2.798103094100952,
            "delta_vs_baseline": -0.09809374809265137,
            "loss": 2.700009346008301,
            "window_index": 128
          },
          {
            "baseline_loss": 4.579283237457275,
            "delta_vs_baseline": -0.5700016021728516,
            "loss": 4.009281635284424,
            "window_index": 129
          },
          {
            "baseline_loss": 8.379351615905762,
            "delta_vs_baseline": -2.329017162322998,
            "loss": 6.050334453582764,
            "window_index": 130
          },
          {
            "baseline_loss": 2.477597713470459,
            "delta_vs_baseline": -0.1341233253479004,
            "loss": 2.3434743881225586,
            "window_index": 131
          },
          {
            "baseline_loss": 3.072523832321167,
            "delta_vs_baseline": -0.2526376247406006,
            "loss": 2.8198862075805664,
            "window_index": 132
          },
          {
            "baseline_loss": 2.88889479637146,
            "delta_vs_baseline": -0.1007239818572998,
            "loss": 2.78817081451416,
            "window_index": 133
          },
          {
            "baseline_loss": 2.657388210296631,
            "delta_vs_baseline": -0.0825190544128418,
            "loss": 2.574869155883789,
            "window_index": 134
          },
          {
            "baseline_loss": 3.222710132598877,
            "delta_vs_baseline": -0.36500048637390137,
            "loss": 2.8577096462249756,
            "window_index": 135
          },
          {
            "baseline_loss": 2.594160318374634,
            "delta_vs_baseline": -0.17980384826660156,
            "loss": 2.4143564701080322,
            "window_index": 136
          },
          {
            "baseline_loss": 2.761676549911499,
            "delta_vs_baseline": -0.2113349437713623,
            "loss": 2.5503416061401367,
            "window_index": 137
          },
          {
            "baseline_loss": 3.063735246658325,
            "delta_vs_baseline": -0.33713269233703613,
            "loss": 2.726602554321289,
            "window_index": 138
          },
          {
            "baseline_loss": 3.095252275466919,
            "delta_vs_baseline": -0.3207864761352539,
            "loss": 2.774465799331665,
            "window_index": 139
          },
          {
            "baseline_loss": 3.001328706741333,
            "delta_vs_baseline": -0.13927793502807617,
            "loss": 2.862050771713257,
            "window_index": 140
          },
          {
            "baseline_loss": 3.124728202819824,
            "delta_vs_baseline": -0.306063175201416,
            "loss": 2.818665027618408,
            "window_index": 141
          },
          {
            "baseline_loss": 3.071362257003784,
            "delta_vs_baseline": -0.25191307067871094,
            "loss": 2.8194491863250732,
            "window_index": 142
          },
          {
            "baseline_loss": 2.8115036487579346,
            "delta_vs_baseline": -0.25005435943603516,
            "loss": 2.5614492893218994,
            "window_index": 143
          },
          {
            "baseline_loss": 2.6746327877044678,
            "delta_vs_baseline": -0.1082761287689209,
            "loss": 2.566356658935547,
            "window_index": 144
          },
          {
            "baseline_loss": 2.9380056858062744,
            "delta_vs_baseline": -0.3274228572845459,
            "loss": 2.6105828285217285,
            "window_index": 145
          },
          {
            "baseline_loss": 3.0988097190856934,
            "delta_vs_baseline": -0.1691141128540039,
            "loss": 2.9296956062316895,
            "window_index": 146
          },
          {
            "baseline_loss": 2.920891761779785,
            "delta_vs_baseline": -0.13552331924438477,
            "loss": 2.7853684425354004,
            "window_index": 147
          },
          {
            "baseline_loss": 3.0000956058502197,
            "delta_vs_baseline": -0.19333863258361816,
            "loss": 2.8067569732666016,
            "window_index": 148
          },
          {
            "baseline_loss": 3.14078688621521,
            "delta_vs_baseline": -0.3601198196411133,
            "loss": 2.7806670665740967,
            "window_index": 149
          },
          {
            "baseline_loss": 3.0242533683776855,
            "delta_vs_baseline": -0.06882262229919434,
            "loss": 2.955430746078491,
            "window_index": 150
          },
          {
            "baseline_loss": 3.2188079357147217,
            "delta_vs_baseline": -0.18231964111328125,
            "loss": 3.0364882946014404,
            "window_index": 151
          },
          {
            "baseline_loss": 2.875241756439209,
            "delta_vs_baseline": -0.30678415298461914,
            "loss": 2.56845760345459,
            "window_index": 152
          },
          {
            "baseline_loss": 2.890204668045044,
            "delta_vs_baseline": -0.12458515167236328,
            "loss": 2.7656195163726807,
            "window_index": 153
          },
          {
            "baseline_loss": 2.5632436275482178,
            "delta_vs_baseline": -0.19693565368652344,
            "loss": 2.3663079738616943,
            "window_index": 154
          },
          {
            "baseline_loss": 3.276603937149048,
            "delta_vs_baseline": -0.2997877597808838,
            "loss": 2.976816177368164,
            "window_index": 155
          },
          {
            "baseline_loss": 2.8790481090545654,
            "delta_vs_baseline": -0.3274261951446533,
            "loss": 2.551621913909912,
            "window_index": 156
          },
          {
            "baseline_loss": 3.015944242477417,
            "delta_vs_baseline": -0.20937752723693848,
            "loss": 2.8065667152404785,
            "window_index": 157
          },
          {
            "baseline_loss": 3.1061058044433594,
            "delta_vs_baseline": -0.2851526737213135,
            "loss": 2.820953130722046,
            "window_index": 158
          },
          {
            "baseline_loss": 2.731477975845337,
            "delta_vs_baseline": -0.2137742042541504,
            "loss": 2.5177037715911865,
            "window_index": 159
          },
          {
            "baseline_loss": 2.7437946796417236,
            "delta_vs_baseline": -0.30676817893981934,
            "loss": 2.4370265007019043,
            "window_index": 160
          },
          {
            "baseline_loss": 3.6713614463806152,
            "delta_vs_baseline": -0.6320719718933105,
            "loss": 3.0392894744873047,
            "window_index": 161
          },
          {
            "baseline_loss": 3.0516977310180664,
            "delta_vs_baseline": -0.40810441970825195,
            "loss": 2.6435933113098145,
            "window_index": 162
          },
          {
            "baseline_loss": 3.183318614959717,
            "delta_vs_baseline": -0.28694605827331543,
            "loss": 2.8963725566864014,
            "window_index": 163
          },
          {
            "baseline_loss": 2.829756021499634,
            "delta_vs_baseline": -0.09842395782470703,
            "loss": 2.7313320636749268,
            "window_index": 164
          },
          {
            "baseline_loss": 2.694065809249878,
            "delta_vs_baseline": -0.08181452751159668,
            "loss": 2.6122512817382812,
            "window_index": 165
          },
          {
            "baseline_loss": 3.1200010776519775,
            "delta_vs_baseline": -0.2451462745666504,
            "loss": 2.874854803085327,
            "window_index": 166
          },
          {
            "baseline_loss": 3.0029048919677734,
            "delta_vs_baseline": -0.22314977645874023,
            "loss": 2.779755115509033,
            "window_index": 167
          },
          {
            "baseline_loss": 3.049888849258423,
            "delta_vs_baseline": -0.17039060592651367,
            "loss": 2.879498243331909,
            "window_index": 168
          },
          {
            "baseline_loss": 2.74784255027771,
            "delta_vs_baseline": -0.2036299705505371,
            "loss": 2.544212579727173,
            "window_index": 169
          },
          {
            "baseline_loss": 2.7892608642578125,
            "delta_vs_baseline": -0.22438335418701172,
            "loss": 2.564877510070801,
            "window_index": 170
          },
          {
            "baseline_loss": 3.56272029876709,
            "delta_vs_baseline": -0.43016576766967773,
            "loss": 3.132554531097412,
            "window_index": 171
          },
          {
            "baseline_loss": 3.123473644256592,
            "delta_vs_baseline": -0.29709959030151367,
            "loss": 2.826374053955078,
            "window_index": 172
          },
          {
            "baseline_loss": 3.0645110607147217,
            "delta_vs_baseline": -0.4318513870239258,
            "loss": 2.632659673690796,
            "window_index": 173
          },
          {
            "baseline_loss": 2.488665819168091,
            "delta_vs_baseline": -0.07101583480834961,
            "loss": 2.417649984359741,
            "window_index": 174
          },
          {
            "baseline_loss": 3.198608875274658,
            "delta_vs_baseline": -0.23266100883483887,
            "loss": 2.9659478664398193,
            "window_index": 175
          },
          {
            "baseline_loss": 2.749643325805664,
            "delta_vs_baseline": -0.2217874526977539,
            "loss": 2.52785587310791,
            "window_index": 176
          },
          {
            "baseline_loss": 3.1345784664154053,
            "delta_vs_baseline": -0.38274145126342773,
            "loss": 2.7518370151519775,
            "window_index": 177
          },
          {
            "baseline_loss": 3.0150883197784424,
            "delta_vs_baseline": -0.13125848770141602,
            "loss": 2.8838298320770264,
            "window_index": 178
          },
          {
            "baseline_loss": 2.964832305908203,
            "delta_vs_baseline": -0.22992873191833496,
            "loss": 2.734903573989868,
            "window_index": 179
          },
          {
            "baseline_loss": 2.8198471069335938,
            "delta_vs_baseline": -0.16660785675048828,
            "loss": 2.6532392501831055,
            "window_index": 180
          },
          {
            "baseline_loss": 2.734243869781494,
            "delta_vs_baseline": -0.2135787010192871,
            "loss": 2.520665168762207,
            "window_index": 181
          },
          {
            "baseline_loss": 3.057004451751709,
            "delta_vs_baseline": -0.18900465965270996,
            "loss": 2.867999792098999,
            "window_index": 182
          },
          {
            "baseline_loss": 2.6313588619232178,
            "delta_vs_baseline": -0.15635395050048828,
            "loss": 2.4750049114227295,
            "window_index": 183
          },
          {
            "baseline_loss": 2.712092161178589,
            "delta_vs_baseline": -0.3218495845794678,
            "loss": 2.390242576599121,
            "window_index": 184
          },
          {
            "baseline_loss": 3.1154446601867676,
            "delta_vs_baseline": -0.27205491065979004,
            "loss": 2.8433897495269775,
            "window_index": 185
          },
          {
            "baseline_loss": 2.9323294162750244,
            "delta_vs_baseline": -0.3410789966583252,
            "loss": 2.591250419616699,
            "window_index": 186
          },
          {
            "baseline_loss": 2.799142837524414,
            "delta_vs_baseline": -0.18660855293273926,
            "loss": 2.612534284591675,
            "window_index": 187
          },
          {
            "baseline_loss": 2.6941280364990234,
            "delta_vs_baseline": -0.060204267501831055,
            "loss": 2.6339237689971924,
            "window_index": 188
          },
          {
            "baseline_loss": 2.839932441711426,
            "delta_vs_baseline": -0.19399094581604004,
            "loss": 2.6459414958953857,
            "window_index": 189
          },
          {
            "baseline_loss": 3.0761919021606445,
            "delta_vs_baseline": -0.27392101287841797,
            "loss": 2.8022708892822266,
            "window_index": 190
          },
          {
            "baseline_loss": 2.7878189086914062,
            "delta_vs_baseline": -0.402374267578125,
            "loss": 2.3854446411132812,
            "window_index": 191
          },
          {
            "baseline_loss": 2.6268908977508545,
            "delta_vs_baseline": -0.17862820625305176,
            "loss": 2.4482626914978027,
            "window_index": 192
          },
          {
            "baseline_loss": 2.9380271434783936,
            "delta_vs_baseline": -0.4518392086029053,
            "loss": 2.4861879348754883,
            "window_index": 193
          },
          {
            "baseline_loss": 2.3056321144104004,
            "delta_vs_baseline": -0.23032379150390625,
            "loss": 2.075308322906494,
            "window_index": 194
          },
          {
            "baseline_loss": 2.9026896953582764,
            "delta_vs_baseline": -0.33031630516052246,
            "loss": 2.572373390197754,
            "window_index": 195
          },
          {
            "baseline_loss": 2.7789411544799805,
            "delta_vs_baseline": -0.4165959358215332,
            "loss": 2.3623452186584473,
            "window_index": 196
          },
          {
            "baseline_loss": 2.5273962020874023,
            "delta_vs_baseline": -0.05002760887145996,
            "loss": 2.4773685932159424,
            "window_index": 197
          },
          {
            "baseline_loss": 2.603788137435913,
            "delta_vs_baseline": -0.34702157974243164,
            "loss": 2.2567665576934814,
            "window_index": 198
          },
          {
            "baseline_loss": 2.6679775714874268,
            "delta_vs_baseline": -0.2175736427307129,
            "loss": 2.450403928756714,
            "window_index": 199
          }
        ],
        "training_window_style_final_checkpoint": [
          {
            "baseline_loss": 2.488567590713501,
            "delta_vs_baseline": -0.1361701488494873,
            "loss": 2.3523974418640137,
            "step": 400
          },
          {
            "baseline_loss": 2.6633172035217285,
            "delta_vs_baseline": -0.15686392784118652,
            "loss": 2.506453275680542,
            "step": 800
          },
          {
            "baseline_loss": 2.646700859069824,
            "delta_vs_baseline": -0.13668441772460938,
            "loss": 2.510016441345215,
            "step": 1200
          },
          {
            "baseline_loss": 2.646510124206543,
            "delta_vs_baseline": -0.11836028099060059,
            "loss": 2.5281498432159424,
            "step": 1600
          },
          {
            "baseline_loss": 2.54093074798584,
            "delta_vs_baseline": -0.18681883811950684,
            "loss": 2.354111909866333,
            "step": 2000
          },
          {
            "baseline_loss": 2.822401523590088,
            "delta_vs_baseline": -0.241074800491333,
            "loss": 2.581326723098755,
            "step": 2400
          },
          {
            "baseline_loss": 2.4011733531951904,
            "delta_vs_baseline": -0.155869722366333,
            "loss": 2.2453036308288574,
            "step": 2800
          },
          {
            "baseline_loss": 2.6783716678619385,
            "delta_vs_baseline": -0.08675265312194824,
            "loss": 2.5916190147399902,
            "step": 3200
          },
          {
            "baseline_loss": 8.865436553955078,
            "delta_vs_baseline": 2.768160820007324,
            "loss": 11.633597373962402,
            "step": 3600
          },
          {
            "baseline_loss": 11.067703247070312,
            "delta_vs_baseline": 3.873575210571289,
            "loss": 14.941278457641602,
            "step": 4000
          }
        ]
      },
      "recorded_during_training_eval_curve": {
        "loss_variance": 19.62883443633425,
        "mean_loss": 4.987879157066345,
        "path": "benchmark/reports/generated/shared_trunk_init_300m_repeat_seed_42/pvr_ec_o_full_300m_shared_trunk_init_from_dense_seed_42/eval_curve.json",
        "window_count": 10,
        "windows": [
          {
            "eval_loss": 3.082045793533325,
            "eval_tokens": 128,
            "optimizer_step": 400,
            "step": 400,
            "training_tokens_seen": 102400
          },
          {
            "eval_loss": 3.4829788208007812,
            "eval_tokens": 128,
            "optimizer_step": 800,
            "step": 800,
            "training_tokens_seen": 204800
          },
          {
            "eval_loss": 2.720137119293213,
            "eval_tokens": 128,
            "optimizer_step": 1200,
            "step": 1200,
            "training_tokens_seen": 307200
          },
          {
            "eval_loss": 2.661188840866089,
            "eval_tokens": 128,
            "optimizer_step": 1600,
            "step": 1600,
            "training_tokens_seen": 409600
          },
          {
            "eval_loss": 2.622964859008789,
            "eval_tokens": 128,
            "optimizer_step": 2000,
            "step": 2000,
            "training_tokens_seen": 512000
          },
          {
            "eval_loss": 2.7599267959594727,
            "eval_tokens": 128,
            "optimizer_step": 2400,
            "step": 2400,
            "training_tokens_seen": 614400
          },
          {
            "eval_loss": 2.428654432296753,
            "eval_tokens": 128,
            "optimizer_step": 2800,
            "step": 2800,
            "training_tokens_seen": 716800
          },
          {
            "eval_loss": 2.5838704109191895,
            "eval_tokens": 128,
            "optimizer_step": 3200,
            "step": 3200,
            "training_tokens_seen": 819200
          },
          {
            "eval_loss": 12.595746040344238,
            "eval_tokens": 128,
            "optimizer_step": 3600,
            "step": 3600,
            "training_tokens_seen": 921600
          },
          {
            "eval_loss": 14.941278457641602,
            "eval_tokens": 128,
            "optimizer_step": 4000,
            "step": 4000,
            "training_tokens_seen": 1024000
          }
        ]
      },
      "same_heldout_tokens": {
        "loss_variance": 1.5113617506917025,
        "mean_loss": 3.0127717781066896,
        "scorecard_seq_len": 64,
        "window_count": 200
      },
      "scorecard_lm_loss_recorded": 3.0127717781066896,
      "scorecard_style_final_checkpoint": {
        "loss_variance": 1.5113617506917025,
        "max_loss": 10.817305564880371,
        "mean_loss": 3.0127717781066896,
        "min_loss": 2.075308322906494,
        "window_count": 200
      },
      "training_window_style_final_checkpoint": {
        "loss_variance": 19.320005992944107,
        "max_loss": 14.941278457641602,
        "mean_loss": 4.624425411224365,
        "min_loss": 2.2453036308288574,
        "window_count": 10
      }
    },
    "pvr_baseline_seed42": {
      "checkpoint_path": "checkpoints/shared_trunk_init_300m_repeat_seed_42/pvr_ec_o_full_300m_baseline_seed_42/checkpoint.pt",
      "deltas_vs_pvr_baseline": {
        "recorded_during_training_eval_curve_mean": 0.0,
        "scorecard_style_final_checkpoint_mean": 0.0,
        "training_window_style_final_checkpoint_mean": 0.0
      },
      "label": "pvr_baseline_seed42",
      "model_variant": "pvr_ec_o_full_300m_baseline_seed_42",
      "per_window_deltas_vs_pvr_baseline": {
        "scorecard_style_general": [
          {
            "baseline_loss": 3.3696975708007812,
            "delta_vs_baseline": 0.0,
            "loss": 3.3696975708007812,
            "window_index": 0
          },
          {
            "baseline_loss": 3.7571780681610107,
            "delta_vs_baseline": 0.0,
            "loss": 3.7571780681610107,
            "window_index": 1
          },
          {
            "baseline_loss": 2.744732618331909,
            "delta_vs_baseline": 0.0,
            "loss": 2.744732618331909,
            "window_index": 2
          },
          {
            "baseline_loss": 3.1212172508239746,
            "delta_vs_baseline": 0.0,
            "loss": 3.1212172508239746,
            "window_index": 3
          },
          {
            "baseline_loss": 3.1811468601226807,
            "delta_vs_baseline": 0.0,
            "loss": 3.1811468601226807,
            "window_index": 4
          },
          {
            "baseline_loss": 3.6319479942321777,
            "delta_vs_baseline": 0.0,
            "loss": 3.6319479942321777,
            "window_index": 5
          },
          {
            "baseline_loss": 3.136638641357422,
            "delta_vs_baseline": 0.0,
            "loss": 3.136638641357422,
            "window_index": 6
          },
          {
            "baseline_loss": 2.6240248680114746,
            "delta_vs_baseline": 0.0,
            "loss": 2.6240248680114746,
            "window_index": 7
          },
          {
            "baseline_loss": 4.648166179656982,
            "delta_vs_baseline": 0.0,
            "loss": 4.648166179656982,
            "window_index": 8
          },
          {
            "baseline_loss": 5.14591121673584,
            "delta_vs_baseline": 0.0,
            "loss": 5.14591121673584,
            "window_index": 9
          },
          {
            "baseline_loss": 10.665205001831055,
            "delta_vs_baseline": 0.0,
            "loss": 10.665205001831055,
            "window_index": 10
          },
          {
            "baseline_loss": 9.66199779510498,
            "delta_vs_baseline": 0.0,
            "loss": 9.66199779510498,
            "window_index": 11
          },
          {
            "baseline_loss": 7.029171943664551,
            "delta_vs_baseline": 0.0,
            "loss": 7.029171943664551,
            "window_index": 12
          },
          {
            "baseline_loss": 4.451816082000732,
            "delta_vs_baseline": 0.0,
            "loss": 4.451816082000732,
            "window_index": 13
          },
          {
            "baseline_loss": 9.882694244384766,
            "delta_vs_baseline": 0.0,
            "loss": 9.882694244384766,
            "window_index": 14
          },
          {
            "baseline_loss": 15.704546928405762,
            "delta_vs_baseline": 0.0,
            "loss": 15.704546928405762,
            "window_index": 15
          },
          {
            "baseline_loss": 7.221086502075195,
            "delta_vs_baseline": 0.0,
            "loss": 7.221086502075195,
            "window_index": 16
          },
          {
            "baseline_loss": 8.873090744018555,
            "delta_vs_baseline": 0.0,
            "loss": 8.873090744018555,
            "window_index": 17
          },
          {
            "baseline_loss": 6.848356246948242,
            "delta_vs_baseline": 0.0,
            "loss": 6.848356246948242,
            "window_index": 18
          },
          {
            "baseline_loss": 10.50163459777832,
            "delta_vs_baseline": 0.0,
            "loss": 10.50163459777832,
            "window_index": 19
          },
          {
            "baseline_loss": 8.044512748718262,
            "delta_vs_baseline": 0.0,
            "loss": 8.044512748718262,
            "window_index": 20
          },
          {
            "baseline_loss": 12.315536499023438,
            "delta_vs_baseline": 0.0,
            "loss": 12.315536499023438,
            "window_index": 21
          },
          {
            "baseline_loss": 7.905089378356934,
            "delta_vs_baseline": 0.0,
            "loss": 7.905089378356934,
            "window_index": 22
          },
          {
            "baseline_loss": 6.56272029876709,
            "delta_vs_baseline": 0.0,
            "loss": 6.56272029876709,
            "window_index": 23
          },
          {
            "baseline_loss": 2.7679688930511475,
            "delta_vs_baseline": 0.0,
            "loss": 2.7679688930511475,
            "window_index": 24
          },
          {
            "baseline_loss": 2.9374938011169434,
            "delta_vs_baseline": 0.0,
            "loss": 2.9374938011169434,
            "window_index": 25
          },
          {
            "baseline_loss": 2.6757943630218506,
            "delta_vs_baseline": 0.0,
            "loss": 2.6757943630218506,
            "window_index": 26
          },
          {
            "baseline_loss": 2.6266438961029053,
            "delta_vs_baseline": 0.0,
            "loss": 2.6266438961029053,
            "window_index": 27
          },
          {
            "baseline_loss": 3.199479103088379,
            "delta_vs_baseline": 0.0,
            "loss": 3.199479103088379,
            "window_index": 28
          },
          {
            "baseline_loss": 3.1571550369262695,
            "delta_vs_baseline": 0.0,
            "loss": 3.1571550369262695,
            "window_index": 29
          },
          {
            "baseline_loss": 2.9776811599731445,
            "delta_vs_baseline": 0.0,
            "loss": 2.9776811599731445,
            "window_index": 30
          },
          {
            "baseline_loss": 3.1856303215026855,
            "delta_vs_baseline": 0.0,
            "loss": 3.1856303215026855,
            "window_index": 31
          },
          {
            "baseline_loss": 2.8611888885498047,
            "delta_vs_baseline": 0.0,
            "loss": 2.8611888885498047,
            "window_index": 32
          },
          {
            "baseline_loss": 2.986649751663208,
            "delta_vs_baseline": 0.0,
            "loss": 2.986649751663208,
            "window_index": 33
          },
          {
            "baseline_loss": 3.02950119972229,
            "delta_vs_baseline": 0.0,
            "loss": 3.02950119972229,
            "window_index": 34
          },
          {
            "baseline_loss": 2.630702018737793,
            "delta_vs_baseline": 0.0,
            "loss": 2.630702018737793,
            "window_index": 35
          },
          {
            "baseline_loss": 3.0871145725250244,
            "delta_vs_baseline": 0.0,
            "loss": 3.0871145725250244,
            "window_index": 36
          },
          {
            "baseline_loss": 2.9280953407287598,
            "delta_vs_baseline": 0.0,
            "loss": 2.9280953407287598,
            "window_index": 37
          },
          {
            "baseline_loss": 3.1325175762176514,
            "delta_vs_baseline": 0.0,
            "loss": 3.1325175762176514,
            "window_index": 38
          },
          {
            "baseline_loss": 2.935246229171753,
            "delta_vs_baseline": 0.0,
            "loss": 2.935246229171753,
            "window_index": 39
          },
          {
            "baseline_loss": 3.286637306213379,
            "delta_vs_baseline": 0.0,
            "loss": 3.286637306213379,
            "window_index": 40
          },
          {
            "baseline_loss": 3.0057811737060547,
            "delta_vs_baseline": 0.0,
            "loss": 3.0057811737060547,
            "window_index": 41
          },
          {
            "baseline_loss": 2.738572597503662,
            "delta_vs_baseline": 0.0,
            "loss": 2.738572597503662,
            "window_index": 42
          },
          {
            "baseline_loss": 3.141986131668091,
            "delta_vs_baseline": 0.0,
            "loss": 3.141986131668091,
            "window_index": 43
          },
          {
            "baseline_loss": 2.8448073863983154,
            "delta_vs_baseline": 0.0,
            "loss": 2.8448073863983154,
            "window_index": 44
          },
          {
            "baseline_loss": 3.004800796508789,
            "delta_vs_baseline": 0.0,
            "loss": 3.004800796508789,
            "window_index": 45
          },
          {
            "baseline_loss": 2.9838449954986572,
            "delta_vs_baseline": 0.0,
            "loss": 2.9838449954986572,
            "window_index": 46
          },
          {
            "baseline_loss": 2.9386417865753174,
            "delta_vs_baseline": 0.0,
            "loss": 2.9386417865753174,
            "window_index": 47
          },
          {
            "baseline_loss": 3.1059365272521973,
            "delta_vs_baseline": 0.0,
            "loss": 3.1059365272521973,
            "window_index": 48
          },
          {
            "baseline_loss": 3.168769359588623,
            "delta_vs_baseline": 0.0,
            "loss": 3.168769359588623,
            "window_index": 49
          },
          {
            "baseline_loss": 2.639850378036499,
            "delta_vs_baseline": 0.0,
            "loss": 2.639850378036499,
            "window_index": 50
          },
          {
            "baseline_loss": 2.487496852874756,
            "delta_vs_baseline": 0.0,
            "loss": 2.487496852874756,
            "window_index": 51
          },
          {
            "baseline_loss": 2.708131790161133,
            "delta_vs_baseline": 0.0,
            "loss": 2.708131790161133,
            "window_index": 52
          },
          {
            "baseline_loss": 2.8870315551757812,
            "delta_vs_baseline": 0.0,
            "loss": 2.8870315551757812,
            "window_index": 53
          },
          {
            "baseline_loss": 3.0955796241760254,
            "delta_vs_baseline": 0.0,
            "loss": 3.0955796241760254,
            "window_index": 54
          },
          {
            "baseline_loss": 2.8854877948760986,
            "delta_vs_baseline": 0.0,
            "loss": 2.8854877948760986,
            "window_index": 55
          },
          {
            "baseline_loss": 2.886323928833008,
            "delta_vs_baseline": 0.0,
            "loss": 2.886323928833008,
            "window_index": 56
          },
          {
            "baseline_loss": 2.957814931869507,
            "delta_vs_baseline": 0.0,
            "loss": 2.957814931869507,
            "window_index": 57
          },
          {
            "baseline_loss": 2.8409440517425537,
            "delta_vs_baseline": 0.0,
            "loss": 2.8409440517425537,
            "window_index": 58
          },
          {
            "baseline_loss": 2.849606513977051,
            "delta_vs_baseline": 0.0,
            "loss": 2.849606513977051,
            "window_index": 59
          },
          {
            "baseline_loss": 2.8881561756134033,
            "delta_vs_baseline": 0.0,
            "loss": 2.8881561756134033,
            "window_index": 60
          },
          {
            "baseline_loss": 2.9310176372528076,
            "delta_vs_baseline": 0.0,
            "loss": 2.9310176372528076,
            "window_index": 61
          },
          {
            "baseline_loss": 3.1954236030578613,
            "delta_vs_baseline": 0.0,
            "loss": 3.1954236030578613,
            "window_index": 62
          },
          {
            "baseline_loss": 2.7894527912139893,
            "delta_vs_baseline": 0.0,
            "loss": 2.7894527912139893,
            "window_index": 63
          },
          {
            "baseline_loss": 2.7355093955993652,
            "delta_vs_baseline": 0.0,
            "loss": 2.7355093955993652,
            "window_index": 64
          },
          {
            "baseline_loss": 2.6845948696136475,
            "delta_vs_baseline": 0.0,
            "loss": 2.6845948696136475,
            "window_index": 65
          },
          {
            "baseline_loss": 3.225579261779785,
            "delta_vs_baseline": 0.0,
            "loss": 3.225579261779785,
            "window_index": 66
          },
          {
            "baseline_loss": 2.9965693950653076,
            "delta_vs_baseline": 0.0,
            "loss": 2.9965693950653076,
            "window_index": 67
          },
          {
            "baseline_loss": 2.7195029258728027,
            "delta_vs_baseline": 0.0,
            "loss": 2.7195029258728027,
            "window_index": 68
          },
          {
            "baseline_loss": 2.9124796390533447,
            "delta_vs_baseline": 0.0,
            "loss": 2.9124796390533447,
            "window_index": 69
          },
          {
            "baseline_loss": 3.2319014072418213,
            "delta_vs_baseline": 0.0,
            "loss": 3.2319014072418213,
            "window_index": 70
          },
          {
            "baseline_loss": 2.8929831981658936,
            "delta_vs_baseline": 0.0,
            "loss": 2.8929831981658936,
            "window_index": 71
          },
          {
            "baseline_loss": 3.253342866897583,
            "delta_vs_baseline": 0.0,
            "loss": 3.253342866897583,
            "window_index": 72
          },
          {
            "baseline_loss": 3.1915409564971924,
            "delta_vs_baseline": 0.0,
            "loss": 3.1915409564971924,
            "window_index": 73
          },
          {
            "baseline_loss": 2.7452118396759033,
            "delta_vs_baseline": 0.0,
            "loss": 2.7452118396759033,
            "window_index": 74
          },
          {
            "baseline_loss": 2.888545513153076,
            "delta_vs_baseline": 0.0,
            "loss": 2.888545513153076,
            "window_index": 75
          },
          {
            "baseline_loss": 2.8269476890563965,
            "delta_vs_baseline": 0.0,
            "loss": 2.8269476890563965,
            "window_index": 76
          },
          {
            "baseline_loss": 3.2102153301239014,
            "delta_vs_baseline": 0.0,
            "loss": 3.2102153301239014,
            "window_index": 77
          },
          {
            "baseline_loss": 2.439115285873413,
            "delta_vs_baseline": 0.0,
            "loss": 2.439115285873413,
            "window_index": 78
          },
          {
            "baseline_loss": 3.13478684425354,
            "delta_vs_baseline": 0.0,
            "loss": 3.13478684425354,
            "window_index": 79
          },
          {
            "baseline_loss": 2.9935171604156494,
            "delta_vs_baseline": 0.0,
            "loss": 2.9935171604156494,
            "window_index": 80
          },
          {
            "baseline_loss": 3.124610662460327,
            "delta_vs_baseline": 0.0,
            "loss": 3.124610662460327,
            "window_index": 81
          },
          {
            "baseline_loss": 2.723752498626709,
            "delta_vs_baseline": 0.0,
            "loss": 2.723752498626709,
            "window_index": 82
          },
          {
            "baseline_loss": 2.757559299468994,
            "delta_vs_baseline": 0.0,
            "loss": 2.757559299468994,
            "window_index": 83
          },
          {
            "baseline_loss": 2.790419340133667,
            "delta_vs_baseline": 0.0,
            "loss": 2.790419340133667,
            "window_index": 84
          },
          {
            "baseline_loss": 2.5810930728912354,
            "delta_vs_baseline": 0.0,
            "loss": 2.5810930728912354,
            "window_index": 85
          },
          {
            "baseline_loss": 3.3501040935516357,
            "delta_vs_baseline": 0.0,
            "loss": 3.3501040935516357,
            "window_index": 86
          },
          {
            "baseline_loss": 2.985410213470459,
            "delta_vs_baseline": 0.0,
            "loss": 2.985410213470459,
            "window_index": 87
          },
          {
            "baseline_loss": 2.7511179447174072,
            "delta_vs_baseline": 0.0,
            "loss": 2.7511179447174072,
            "window_index": 88
          },
          {
            "baseline_loss": 3.147357225418091,
            "delta_vs_baseline": 0.0,
            "loss": 3.147357225418091,
            "window_index": 89
          },
          {
            "baseline_loss": 3.229327917098999,
            "delta_vs_baseline": 0.0,
            "loss": 3.229327917098999,
            "window_index": 90
          },
          {
            "baseline_loss": 2.8613240718841553,
            "delta_vs_baseline": 0.0,
            "loss": 2.8613240718841553,
            "window_index": 91
          },
          {
            "baseline_loss": 2.696187734603882,
            "delta_vs_baseline": 0.0,
            "loss": 2.696187734603882,
            "window_index": 92
          },
          {
            "baseline_loss": 2.9458367824554443,
            "delta_vs_baseline": 0.0,
            "loss": 2.9458367824554443,
            "window_index": 93
          },
          {
            "baseline_loss": 2.9736671447753906,
            "delta_vs_baseline": 0.0,
            "loss": 2.9736671447753906,
            "window_index": 94
          },
          {
            "baseline_loss": 2.747361660003662,
            "delta_vs_baseline": 0.0,
            "loss": 2.747361660003662,
            "window_index": 95
          },
          {
            "baseline_loss": 2.9285504817962646,
            "delta_vs_baseline": 0.0,
            "loss": 2.9285504817962646,
            "window_index": 96
          },
          {
            "baseline_loss": 3.183176279067993,
            "delta_vs_baseline": 0.0,
            "loss": 3.183176279067993,
            "window_index": 97
          },
          {
            "baseline_loss": 2.5617079734802246,
            "delta_vs_baseline": 0.0,
            "loss": 2.5617079734802246,
            "window_index": 98
          },
          {
            "baseline_loss": 3.026214599609375,
            "delta_vs_baseline": 0.0,
            "loss": 3.026214599609375,
            "window_index": 99
          },
          {
            "baseline_loss": 3.2600483894348145,
            "delta_vs_baseline": 0.0,
            "loss": 3.2600483894348145,
            "window_index": 100
          },
          {
            "baseline_loss": 2.9374611377716064,
            "delta_vs_baseline": 0.0,
            "loss": 2.9374611377716064,
            "window_index": 101
          },
          {
            "baseline_loss": 2.9559378623962402,
            "delta_vs_baseline": 0.0,
            "loss": 2.9559378623962402,
            "window_index": 102
          },
          {
            "baseline_loss": 3.020036220550537,
            "delta_vs_baseline": 0.0,
            "loss": 3.020036220550537,
            "window_index": 103
          },
          {
            "baseline_loss": 3.088770866394043,
            "delta_vs_baseline": 0.0,
            "loss": 3.088770866394043,
            "window_index": 104
          },
          {
            "baseline_loss": 2.8664493560791016,
            "delta_vs_baseline": 0.0,
            "loss": 2.8664493560791016,
            "window_index": 105
          },
          {
            "baseline_loss": 2.9487314224243164,
            "delta_vs_baseline": 0.0,
            "loss": 2.9487314224243164,
            "window_index": 106
          },
          {
            "baseline_loss": 2.9448704719543457,
            "delta_vs_baseline": 0.0,
            "loss": 2.9448704719543457,
            "window_index": 107
          },
          {
            "baseline_loss": 2.833847761154175,
            "delta_vs_baseline": 0.0,
            "loss": 2.833847761154175,
            "window_index": 108
          },
          {
            "baseline_loss": 3.0840413570404053,
            "delta_vs_baseline": 0.0,
            "loss": 3.0840413570404053,
            "window_index": 109
          },
          {
            "baseline_loss": 3.0566482543945312,
            "delta_vs_baseline": 0.0,
            "loss": 3.0566482543945312,
            "window_index": 110
          },
          {
            "baseline_loss": 3.0592665672302246,
            "delta_vs_baseline": 0.0,
            "loss": 3.0592665672302246,
            "window_index": 111
          },
          {
            "baseline_loss": 2.9259722232818604,
            "delta_vs_baseline": 0.0,
            "loss": 2.9259722232818604,
            "window_index": 112
          },
          {
            "baseline_loss": 3.1105833053588867,
            "delta_vs_baseline": 0.0,
            "loss": 3.1105833053588867,
            "window_index": 113
          },
          {
            "baseline_loss": 2.762549877166748,
            "delta_vs_baseline": 0.0,
            "loss": 2.762549877166748,
            "window_index": 114
          },
          {
            "baseline_loss": 3.0378577709198,
            "delta_vs_baseline": 0.0,
            "loss": 3.0378577709198,
            "window_index": 115
          },
          {
            "baseline_loss": 3.0677103996276855,
            "delta_vs_baseline": 0.0,
            "loss": 3.0677103996276855,
            "window_index": 116
          },
          {
            "baseline_loss": 2.8927221298217773,
            "delta_vs_baseline": 0.0,
            "loss": 2.8927221298217773,
            "window_index": 117
          },
          {
            "baseline_loss": 3.42633056640625,
            "delta_vs_baseline": 0.0,
            "loss": 3.42633056640625,
            "window_index": 118
          },
          {
            "baseline_loss": 2.779985189437866,
            "delta_vs_baseline": 0.0,
            "loss": 2.779985189437866,
            "window_index": 119
          },
          {
            "baseline_loss": 2.5664048194885254,
            "delta_vs_baseline": 0.0,
            "loss": 2.5664048194885254,
            "window_index": 120
          },
          {
            "baseline_loss": 2.9053828716278076,
            "delta_vs_baseline": 0.0,
            "loss": 2.9053828716278076,
            "window_index": 121
          },
          {
            "baseline_loss": 2.8783071041107178,
            "delta_vs_baseline": 0.0,
            "loss": 2.8783071041107178,
            "window_index": 122
          },
          {
            "baseline_loss": 2.7440104484558105,
            "delta_vs_baseline": 0.0,
            "loss": 2.7440104484558105,
            "window_index": 123
          },
          {
            "baseline_loss": 3.080070734024048,
            "delta_vs_baseline": 0.0,
            "loss": 3.080070734024048,
            "window_index": 124
          },
          {
            "baseline_loss": 2.944106101989746,
            "delta_vs_baseline": 0.0,
            "loss": 2.944106101989746,
            "window_index": 125
          },
          {
            "baseline_loss": 3.7518718242645264,
            "delta_vs_baseline": 0.0,
            "loss": 3.7518718242645264,
            "window_index": 126
          },
          {
            "baseline_loss": 2.967647075653076,
            "delta_vs_baseline": 0.0,
            "loss": 2.967647075653076,
            "window_index": 127
          },
          {
            "baseline_loss": 2.798103094100952,
            "delta_vs_baseline": 0.0,
            "loss": 2.798103094100952,
            "window_index": 128
          },
          {
            "baseline_loss": 4.579283237457275,
            "delta_vs_baseline": 0.0,
            "loss": 4.579283237457275,
            "window_index": 129
          },
          {
            "baseline_loss": 8.379351615905762,
            "delta_vs_baseline": 0.0,
            "loss": 8.379351615905762,
            "window_index": 130
          },
          {
            "baseline_loss": 2.477597713470459,
            "delta_vs_baseline": 0.0,
            "loss": 2.477597713470459,
            "window_index": 131
          },
          {
            "baseline_loss": 3.072523832321167,
            "delta_vs_baseline": 0.0,
            "loss": 3.072523832321167,
            "window_index": 132
          },
          {
            "baseline_loss": 2.88889479637146,
            "delta_vs_baseline": 0.0,
            "loss": 2.88889479637146,
            "window_index": 133
          },
          {
            "baseline_loss": 2.657388210296631,
            "delta_vs_baseline": 0.0,
            "loss": 2.657388210296631,
            "window_index": 134
          },
          {
            "baseline_loss": 3.222710132598877,
            "delta_vs_baseline": 0.0,
            "loss": 3.222710132598877,
            "window_index": 135
          },
          {
            "baseline_loss": 2.594160318374634,
            "delta_vs_baseline": 0.0,
            "loss": 2.594160318374634,
            "window_index": 136
          },
          {
            "baseline_loss": 2.761676549911499,
            "delta_vs_baseline": 0.0,
            "loss": 2.761676549911499,
            "window_index": 137
          },
          {
            "baseline_loss": 3.063735246658325,
            "delta_vs_baseline": 0.0,
            "loss": 3.063735246658325,
            "window_index": 138
          },
          {
            "baseline_loss": 3.095252275466919,
            "delta_vs_baseline": 0.0,
            "loss": 3.095252275466919,
            "window_index": 139
          },
          {
            "baseline_loss": 3.001328706741333,
            "delta_vs_baseline": 0.0,
            "loss": 3.001328706741333,
            "window_index": 140
          },
          {
            "baseline_loss": 3.124728202819824,
            "delta_vs_baseline": 0.0,
            "loss": 3.124728202819824,
            "window_index": 141
          },
          {
            "baseline_loss": 3.071362257003784,
            "delta_vs_baseline": 0.0,
            "loss": 3.071362257003784,
            "window_index": 142
          },
          {
            "baseline_loss": 2.8115036487579346,
            "delta_vs_baseline": 0.0,
            "loss": 2.8115036487579346,
            "window_index": 143
          },
          {
            "baseline_loss": 2.6746327877044678,
            "delta_vs_baseline": 0.0,
            "loss": 2.6746327877044678,
            "window_index": 144
          },
          {
            "baseline_loss": 2.9380056858062744,
            "delta_vs_baseline": 0.0,
            "loss": 2.9380056858062744,
            "window_index": 145
          },
          {
            "baseline_loss": 3.0988097190856934,
            "delta_vs_baseline": 0.0,
            "loss": 3.0988097190856934,
            "window_index": 146
          },
          {
            "baseline_loss": 2.920891761779785,
            "delta_vs_baseline": 0.0,
            "loss": 2.920891761779785,
            "window_index": 147
          },
          {
            "baseline_loss": 3.0000956058502197,
            "delta_vs_baseline": 0.0,
            "loss": 3.0000956058502197,
            "window_index": 148
          },
          {
            "baseline_loss": 3.14078688621521,
            "delta_vs_baseline": 0.0,
            "loss": 3.14078688621521,
            "window_index": 149
          },
          {
            "baseline_loss": 3.0242533683776855,
            "delta_vs_baseline": 0.0,
            "loss": 3.0242533683776855,
            "window_index": 150
          },
          {
            "baseline_loss": 3.2188079357147217,
            "delta_vs_baseline": 0.0,
            "loss": 3.2188079357147217,
            "window_index": 151
          },
          {
            "baseline_loss": 2.875241756439209,
            "delta_vs_baseline": 0.0,
            "loss": 2.875241756439209,
            "window_index": 152
          },
          {
            "baseline_loss": 2.890204668045044,
            "delta_vs_baseline": 0.0,
            "loss": 2.890204668045044,
            "window_index": 153
          },
          {
            "baseline_loss": 2.5632436275482178,
            "delta_vs_baseline": 0.0,
            "loss": 2.5632436275482178,
            "window_index": 154
          },
          {
            "baseline_loss": 3.276603937149048,
            "delta_vs_baseline": 0.0,
            "loss": 3.276603937149048,
            "window_index": 155
          },
          {
            "baseline_loss": 2.8790481090545654,
            "delta_vs_baseline": 0.0,
            "loss": 2.8790481090545654,
            "window_index": 156
          },
          {
            "baseline_loss": 3.015944242477417,
            "delta_vs_baseline": 0.0,
            "loss": 3.015944242477417,
            "window_index": 157
          },
          {
            "baseline_loss": 3.1061058044433594,
            "delta_vs_baseline": 0.0,
            "loss": 3.1061058044433594,
            "window_index": 158
          },
          {
            "baseline_loss": 2.731477975845337,
            "delta_vs_baseline": 0.0,
            "loss": 2.731477975845337,
            "window_index": 159
          },
          {
            "baseline_loss": 2.7437946796417236,
            "delta_vs_baseline": 0.0,
            "loss": 2.7437946796417236,
            "window_index": 160
          },
          {
            "baseline_loss": 3.6713614463806152,
            "delta_vs_baseline": 0.0,
            "loss": 3.6713614463806152,
            "window_index": 161
          },
          {
            "baseline_loss": 3.0516977310180664,
            "delta_vs_baseline": 0.0,
            "loss": 3.0516977310180664,
            "window_index": 162
          },
          {
            "baseline_loss": 3.183318614959717,
            "delta_vs_baseline": 0.0,
            "loss": 3.183318614959717,
            "window_index": 163
          },
          {
            "baseline_loss": 2.829756021499634,
            "delta_vs_baseline": 0.0,
            "loss": 2.829756021499634,
            "window_index": 164
          },
          {
            "baseline_loss": 2.694065809249878,
            "delta_vs_baseline": 0.0,
            "loss": 2.694065809249878,
            "window_index": 165
          },
          {
            "baseline_loss": 3.1200010776519775,
            "delta_vs_baseline": 0.0,
            "loss": 3.1200010776519775,
            "window_index": 166
          },
          {
            "baseline_loss": 3.0029048919677734,
            "delta_vs_baseline": 0.0,
            "loss": 3.0029048919677734,
            "window_index": 167
          },
          {
            "baseline_loss": 3.049888849258423,
            "delta_vs_baseline": 0.0,
            "loss": 3.049888849258423,
            "window_index": 168
          },
          {
            "baseline_loss": 2.74784255027771,
            "delta_vs_baseline": 0.0,
            "loss": 2.74784255027771,
            "window_index": 169
          },
          {
            "baseline_loss": 2.7892608642578125,
            "delta_vs_baseline": 0.0,
            "loss": 2.7892608642578125,
            "window_index": 170
          },
          {
            "baseline_loss": 3.56272029876709,
            "delta_vs_baseline": 0.0,
            "loss": 3.56272029876709,
            "window_index": 171
          },
          {
            "baseline_loss": 3.123473644256592,
            "delta_vs_baseline": 0.0,
            "loss": 3.123473644256592,
            "window_index": 172
          },
          {
            "baseline_loss": 3.0645110607147217,
            "delta_vs_baseline": 0.0,
            "loss": 3.0645110607147217,
            "window_index": 173
          },
          {
            "baseline_loss": 2.488665819168091,
            "delta_vs_baseline": 0.0,
            "loss": 2.488665819168091,
            "window_index": 174
          },
          {
            "baseline_loss": 3.198608875274658,
            "delta_vs_baseline": 0.0,
            "loss": 3.198608875274658,
            "window_index": 175
          },
          {
            "baseline_loss": 2.749643325805664,
            "delta_vs_baseline": 0.0,
            "loss": 2.749643325805664,
            "window_index": 176
          },
          {
            "baseline_loss": 3.1345784664154053,
            "delta_vs_baseline": 0.0,
            "loss": 3.1345784664154053,
            "window_index": 177
          },
          {
            "baseline_loss": 3.0150883197784424,
            "delta_vs_baseline": 0.0,
            "loss": 3.0150883197784424,
            "window_index": 178
          },
          {
            "baseline_loss": 2.964832305908203,
            "delta_vs_baseline": 0.0,
            "loss": 2.964832305908203,
            "window_index": 179
          },
          {
            "baseline_loss": 2.8198471069335938,
            "delta_vs_baseline": 0.0,
            "loss": 2.8198471069335938,
            "window_index": 180
          },
          {
            "baseline_loss": 2.734243869781494,
            "delta_vs_baseline": 0.0,
            "loss": 2.734243869781494,
            "window_index": 181
          },
          {
            "baseline_loss": 3.057004451751709,
            "delta_vs_baseline": 0.0,
            "loss": 3.057004451751709,
            "window_index": 182
          },
          {
            "baseline_loss": 2.6313588619232178,
            "delta_vs_baseline": 0.0,
            "loss": 2.6313588619232178,
            "window_index": 183
          },
          {
            "baseline_loss": 2.712092161178589,
            "delta_vs_baseline": 0.0,
            "loss": 2.712092161178589,
            "window_index": 184
          },
          {
            "baseline_loss": 3.1154446601867676,
            "delta_vs_baseline": 0.0,
            "loss": 3.1154446601867676,
            "window_index": 185
          },
          {
            "baseline_loss": 2.9323294162750244,
            "delta_vs_baseline": 0.0,
            "loss": 2.9323294162750244,
            "window_index": 186
          },
          {
            "baseline_loss": 2.799142837524414,
            "delta_vs_baseline": 0.0,
            "loss": 2.799142837524414,
            "window_index": 187
          },
          {
            "baseline_loss": 2.6941280364990234,
            "delta_vs_baseline": 0.0,
            "loss": 2.6941280364990234,
            "window_index": 188
          },
          {
            "baseline_loss": 2.839932441711426,
            "delta_vs_baseline": 0.0,
            "loss": 2.839932441711426,
            "window_index": 189
          },
          {
            "baseline_loss": 3.0761919021606445,
            "delta_vs_baseline": 0.0,
            "loss": 3.0761919021606445,
            "window_index": 190
          },
          {
            "baseline_loss": 2.7878189086914062,
            "delta_vs_baseline": 0.0,
            "loss": 2.7878189086914062,
            "window_index": 191
          },
          {
            "baseline_loss": 2.6268908977508545,
            "delta_vs_baseline": 0.0,
            "loss": 2.6268908977508545,
            "window_index": 192
          },
          {
            "baseline_loss": 2.9380271434783936,
            "delta_vs_baseline": 0.0,
            "loss": 2.9380271434783936,
            "window_index": 193
          },
          {
            "baseline_loss": 2.3056321144104004,
            "delta_vs_baseline": 0.0,
            "loss": 2.3056321144104004,
            "window_index": 194
          },
          {
            "baseline_loss": 2.9026896953582764,
            "delta_vs_baseline": 0.0,
            "loss": 2.9026896953582764,
            "window_index": 195
          },
          {
            "baseline_loss": 2.7789411544799805,
            "delta_vs_baseline": 0.0,
            "loss": 2.7789411544799805,
            "window_index": 196
          },
          {
            "baseline_loss": 2.5273962020874023,
            "delta_vs_baseline": 0.0,
            "loss": 2.5273962020874023,
            "window_index": 197
          },
          {
            "baseline_loss": 2.603788137435913,
            "delta_vs_baseline": 0.0,
            "loss": 2.603788137435913,
            "window_index": 198
          },
          {
            "baseline_loss": 2.6679775714874268,
            "delta_vs_baseline": 0.0,
            "loss": 2.6679775714874268,
            "window_index": 199
          }
        ],
        "training_window_style_final_checkpoint": [
          {
            "baseline_loss": 2.488567590713501,
            "delta_vs_baseline": 0.0,
            "loss": 2.488567590713501,
            "step": 400
          },
          {
            "baseline_loss": 2.6633172035217285,
            "delta_vs_baseline": 0.0,
            "loss": 2.6633172035217285,
            "step": 800
          },
          {
            "baseline_loss": 2.646700859069824,
            "delta_vs_baseline": 0.0,
            "loss": 2.646700859069824,
            "step": 1200
          },
          {
            "baseline_loss": 2.646510124206543,
            "delta_vs_baseline": 0.0,
            "loss": 2.646510124206543,
            "step": 1600
          },
          {
            "baseline_loss": 2.54093074798584,
            "delta_vs_baseline": 0.0,
            "loss": 2.54093074798584,
            "step": 2000
          },
          {
            "baseline_loss": 2.822401523590088,
            "delta_vs_baseline": 0.0,
            "loss": 2.822401523590088,
            "step": 2400
          },
          {
            "baseline_loss": 2.4011733531951904,
            "delta_vs_baseline": 0.0,
            "loss": 2.4011733531951904,
            "step": 2800
          },
          {
            "baseline_loss": 2.6783716678619385,
            "delta_vs_baseline": 0.0,
            "loss": 2.6783716678619385,
            "step": 3200
          },
          {
            "baseline_loss": 8.865436553955078,
            "delta_vs_baseline": 0.0,
            "loss": 8.865436553955078,
            "step": 3600
          },
          {
            "baseline_loss": 11.067703247070312,
            "delta_vs_baseline": 0.0,
            "loss": 11.067703247070312,
            "step": 4000
          }
        ]
      },
      "recorded_during_training_eval_curve": {
        "loss_variance": 9.73886244214379,
        "mean_loss": 4.856676840782166,
        "path": "benchmark/reports/generated/shared_trunk_init_300m_repeat_seed_42/pvr_ec_o_full_300m_baseline_seed_42/eval_curve.json",
        "window_count": 10,
        "windows": [
          {
            "eval_loss": 5.555481910705566,
            "eval_tokens": 128,
            "optimizer_step": 400,
            "step": 400,
            "training_tokens_seen": 102400
          },
          {
            "eval_loss": 4.806666374206543,
            "eval_tokens": 128,
            "optimizer_step": 800,
            "step": 800,
            "training_tokens_seen": 204800
          },
          {
            "eval_loss": 3.1982131004333496,
            "eval_tokens": 128,
            "optimizer_step": 1200,
            "step": 1200,
            "training_tokens_seen": 307200
          },
          {
            "eval_loss": 2.7147812843322754,
            "eval_tokens": 128,
            "optimizer_step": 1600,
            "step": 1600,
            "training_tokens_seen": 409600
          },
          {
            "eval_loss": 2.549985647201538,
            "eval_tokens": 128,
            "optimizer_step": 2000,
            "step": 2000,
            "training_tokens_seen": 512000
          },
          {
            "eval_loss": 2.994072198867798,
            "eval_tokens": 128,
            "optimizer_step": 2400,
            "step": 2400,
            "training_tokens_seen": 614400
          },
          {
            "eval_loss": 2.4728047847747803,
            "eval_tokens": 128,
            "optimizer_step": 2800,
            "step": 2800,
            "training_tokens_seen": 716800
          },
          {
            "eval_loss": 2.704378128051758,
            "eval_tokens": 128,
            "optimizer_step": 3200,
            "step": 3200,
            "training_tokens_seen": 819200
          },
          {
            "eval_loss": 10.502681732177734,
            "eval_tokens": 128,
            "optimizer_step": 3600,
            "step": 3600,
            "training_tokens_seen": 921600
          },
          {
            "eval_loss": 11.067703247070312,
            "eval_tokens": 128,
            "optimizer_step": 4000,
            "step": 4000,
            "training_tokens_seen": 1024000
          }
        ]
      },
      "same_heldout_tokens": {
        "loss_variance": 3.0827959869135775,
        "mean_loss": 3.422222343683243,
        "scorecard_seq_len": 64,
        "window_count": 200
      },
      "scorecard_lm_loss_recorded": 3.422222343683243,
      "scorecard_style_final_checkpoint": {
        "loss_variance": 3.0827959869135775,
        "max_loss": 15.704546928405762,
        "mean_loss": 3.422222343683243,
        "min_loss": 2.3056321144104004,
        "window_count": 200
      },
      "training_window_style_final_checkpoint": {
        "loss_variance": 8.911055099810994,
        "max_loss": 11.067703247070312,
        "mean_loss": 4.082111287117004,
        "min_loss": 2.4011733531951904,
        "window_count": 10
      }
    }
  },
  "schema_version": "1.0",
  "scorecard_seq_len": 64,
  "scorecard_windows": 200,
  "status": "PVR_EAN_SCORECARD_EVAL_CURVE_ALIGNMENT_AUDIT_COMPLETE",
  "status_detail": "EVAL_PATH_MISMATCH_OR_NOISE_REMAINS",
  "training_seq_len": 128
}
```
