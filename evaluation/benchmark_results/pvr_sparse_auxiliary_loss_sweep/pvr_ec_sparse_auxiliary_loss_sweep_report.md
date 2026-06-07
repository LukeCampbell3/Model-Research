# PVR-EC Sparse Auxiliary Loss Sweep Report

**Status:** PVR_EC_SPARSE_AUXILIARY_LOSS_HELPFUL

**Statuses:** PVR_EC_DO_NOT_PROMOTE, PVR_EC_SPARSE_AUXILIARY_LOSS_HELPFUL, PVR_EC_SPARSE_AUXILIARY_LOSS_IMPLEMENTED

```json
{
  "metadata": {
    "timestamp": "2026-06-07T03:18:03.818607",
    "run_id": "algo_20260607_031408_benchmark-lite",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 42,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode benchmark-lite --scale small --sample-limit 1000 --train-steps 500 --device cuda --amp --models pvr_ec_ownership_top1_scale_schedule_1_to_8 --enable-ownership-map --ownership-map-mode frozen --run-sparse-auxiliary-loss-sweep --sparse-aux-loss-variants baseline_main_loss,sparse_ce_0_03,sparse_ce_0_05,margin_align_0_03_m0_5,margin_align_0_05_m0_5,wrong_suppress_0_03_t0_25,sparse_ce_0_03_plus_margin_0_03,margin_0_03_plus_wrong_suppress_0_03,sparse_ce_0_03_plus_harm_0_03 --output-dir evaluation/benchmark_results/pvr_sparse_auxiliary_loss_sweep",
    "model_variants": [
      "pvr_ec_ownership_top1_scale_schedule_1_to_8"
    ],
    "batch_sizes": [
      1,
      32
    ],
    "sequence_lengths": [
      64
    ],
    "train_steps": 500,
    "sample_limit": 1000,
    "mode": "benchmark-lite",
    "scale": "small",
    "families": [
      "clrs",
      "listops",
      "scan",
      "dyck"
    ],
    "pvr_expert_delta_scale": null,
    "pvr_expert_delta_scale_schedule": "constant",
    "pvr_expert_delta_scale_start": null,
    "pvr_expert_delta_scale_end": null,
    "pvr_expert_delta_scale_warmup_steps": null,
    "pvr_expert_delta_scale_hold_steps": null,
    "pvr_expert_delta_scale_decay": null
  },
  "status": "PVR_EC_SPARSE_AUXILIARY_LOSS_HELPFUL",
  "statuses": [
    "PVR_EC_DO_NOT_PROMOTE",
    "PVR_EC_SPARSE_AUXILIARY_LOSS_HELPFUL",
    "PVR_EC_SPARSE_AUXILIARY_LOSS_IMPLEMENTED"
  ],
  "promotion_ready": false,
  "model_table": {
    "pvr_ec_ownership_top1_scale_schedule_1_to_8__aux__baseline_main_loss": {
      "params": 482690,
      "avg_accuracy": 0.06054665483850138,
      "avg_exact_match": 0.0,
      "avg_loss": 0.46348366168482846,
      "avg_qpc": 0.06054665483850138,
      "avg_loops": 1.0
    },
    "pvr_ec_ownership_top1_scale_schedule_1_to_8__aux__sparse_ce_0_03": {
      "params": 482690,
      "avg_accuracy": 0.17268744165371785,
      "avg_exact_match": 0.0,
      "avg_loss": 0.41296596180958056,
      "avg_qpc": 0.17268744165371785,
      "avg_loops": 1.0
    },
    "pvr_ec_ownership_top1_scale_schedule_1_to_8__aux__sparse_ce_0_05": {
      "params": 482690,
      "avg_accuracy": 0.24243722927027295,
      "avg_exact_match": 0.0,
      "avg_loss": 0.4004437902864689,
      "avg_qpc": 0.24243722927027295,
      "avg_loops": 1.0
    },
    "pvr_ec_ownership_top1_scale_schedule_1_to_8__aux__margin_align_0_03_m0_5": {
      "params": 482690,
      "avg_accuracy": 0.10121606180580317,
      "avg_exact_match": 0.0,
      "avg_loss": 0.446313688182272,
      "avg_qpc": 0.10121606180580317,
      "avg_loops": 1.0
    },
    "pvr_ec_ownership_top1_scale_schedule_1_to_8__aux__margin_align_0_05_m0_5": {
      "params": 482690,
      "avg_accuracy": 0.11243111735688467,
      "avg_exact_match": 0.0,
      "avg_loss": 0.4407933249215906,
      "avg_qpc": 0.11243111735688467,
      "avg_loops": 1.0
    },
    "pvr_ec_ownership_top1_scale_schedule_1_to_8__aux__wrong_suppress_0_03_t0_25": {
      "params": 482690,
      "avg_accuracy": 0.06802156528639025,
      "avg_exact_match": 0.0,
      "avg_loss": 0.44242214163144433,
      "avg_qpc": 0.06802156528639025,
      "avg_loops": 1.0
    },
    "pvr_ec_ownership_top1_scale_schedule_1_to_8__aux__sparse_ce_0_03_plus_margin_0_03": {
      "params": 482690,
      "avg_accuracy": 0.2102302618601088,
      "avg_exact_match": 0.0,
      "avg_loss": 0.4218268555123359,
      "avg_qpc": 0.2102302618601088,
      "avg_loops": 1.0
    },
    "pvr_ec_ownership_top1_scale_schedule_1_to_8__aux__margin_0_03_plus_wrong_suppress_0_03": {
      "params": 482690,
      "avg_accuracy": 0.11535639563864514,
      "avg_exact_match": 0.0,
      "avg_loss": 0.42275461923175806,
      "avg_qpc": 0.11535639563864514,
      "avg_loops": 1.0
    },
    "pvr_ec_ownership_top1_scale_schedule_1_to_8__aux__sparse_ce_0_03_plus_harm_0_03": {
      "params": 482690,
      "avg_accuracy": 0.17619962371543163,
      "avg_exact_match": 0.0,
      "avg_loss": 0.4157806743557254,
      "avg_qpc": 0.17619962371543163,
      "avg_loops": 1.0
    }
  },
  "variants": [
    "baseline_main_loss",
    "sparse_ce_0_03",
    "sparse_ce_0_05",
    "margin_align_0_03_m0_5",
    "margin_align_0_05_m0_5",
    "wrong_suppress_0_03_t0_25",
    "sparse_ce_0_03_plus_margin_0_03",
    "margin_0_03_plus_wrong_suppress_0_03",
    "sparse_ce_0_03_plus_harm_0_03"
  ],
  "variant_metrics": {
    "baseline_main_loss": {
      "avg_loss": 0.46348366168482846,
      "avg_accuracy": 0.06054665483850138,
      "calibration_proxy": 0.08361891197652371,
      "latency_p50": 0.6177078485488892,
      "latency_p95": 0.6177078485488892,
      "correct_class_logit_delta": 0.540522301584133,
      "incorrect_class_logit_delta_max": 3.297521810978651,
      "delta_correct_minus_top_wrong": -2.756999489851296,
      "residual_help_rate": 0.6453027786531795,
      "residual_harm_rate": 0.3544546033566197,
      "token_to_sequence_transfer_ratio": 0.06254858933453986,
      "scopes": [
        "aux_all_tokens"
      ]
    },
    "margin_0_03_plus_wrong_suppress_0_03": {
      "avg_loss": 0.42275461923175806,
      "avg_accuracy": 0.11535639563864514,
      "calibration_proxy": 0.05763913365952253,
      "latency_p50": 0.5350645482540131,
      "latency_p95": 0.5350645482540131,
      "correct_class_logit_delta": 0.39967639162042207,
      "incorrect_class_logit_delta_max": 3.4177649368842444,
      "delta_correct_minus_top_wrong": -3.018088563500593,
      "residual_help_rate": 0.5777212926962724,
      "residual_harm_rate": 0.42215531315499294,
      "token_to_sequence_transfer_ratio": 0.1188094002412659,
      "scopes": [
        "aux_all_tokens"
      ]
    },
    "margin_align_0_03_m0_5": {
      "avg_loss": 0.446313688182272,
      "avg_accuracy": 0.10121606180580317,
      "calibration_proxy": 0.05245952956926203,
      "latency_p50": 0.5160909295082092,
      "latency_p95": 0.5160909295082092,
      "correct_class_logit_delta": 2.781071110783766,
      "incorrect_class_logit_delta_max": 4.514456058541933,
      "delta_correct_minus_top_wrong": -1.7333849702651303,
      "residual_help_rate": 0.8768548307319481,
      "residual_harm_rate": 0.12310918517565975,
      "token_to_sequence_transfer_ratio": 0.12189220793409718,
      "scopes": [
        "aux_all_tokens"
      ]
    },
    "margin_align_0_05_m0_5": {
      "avg_loss": 0.4407933249215906,
      "avg_accuracy": 0.11243111735688467,
      "calibration_proxy": 0.07011225576509231,
      "latency_p50": 0.523300290107727,
      "latency_p95": 0.523300290107727,
      "correct_class_logit_delta": 3.686697710615893,
      "incorrect_class_logit_delta_max": 4.8530382681638,
      "delta_correct_minus_top_wrong": -1.1663405845562616,
      "residual_help_rate": 0.952981111748765,
      "residual_harm_rate": 0.04692040958131353,
      "token_to_sequence_transfer_ratio": 0.10785271299396335,
      "scopes": [
        "aux_all_tokens"
      ]
    },
    "sparse_ce_0_03": {
      "avg_loss": 0.41296596180958056,
      "avg_accuracy": 0.17268744165371785,
      "calibration_proxy": 0.08300109208044587,
      "latency_p50": 0.5333220362663269,
      "latency_p95": 0.5333220362663269,
      "correct_class_logit_delta": 4.751050369193157,
      "incorrect_class_logit_delta_max": 6.5552301829059925,
      "delta_correct_minus_top_wrong": -1.8041798576402168,
      "residual_help_rate": 0.9830370093695819,
      "residual_harm_rate": 0.01695336303419026,
      "token_to_sequence_transfer_ratio": 0.04880798835564186,
      "scopes": [
        "aux_all_tokens"
      ]
    },
    "sparse_ce_0_03_plus_harm_0_03": {
      "avg_loss": 0.4157806743557254,
      "avg_accuracy": 0.17619962371543163,
      "calibration_proxy": 0.09222920605720397,
      "latency_p50": 0.5391393899917603,
      "latency_p95": 0.5391393899917603,
      "correct_class_logit_delta": 4.217234650161117,
      "incorrect_class_logit_delta_max": 5.849618592609962,
      "delta_correct_minus_top_wrong": -1.6323839634036026,
      "residual_help_rate": 0.9711906107453008,
      "residual_harm_rate": 0.0287963145010508,
      "token_to_sequence_transfer_ratio": 0.050173301827684924,
      "scopes": [
        "aux_all_tokens"
      ]
    },
    "sparse_ce_0_03_plus_margin_0_03": {
      "avg_loss": 0.4218268555123359,
      "avg_accuracy": 0.2102302618601088,
      "calibration_proxy": 0.13456367188118393,
      "latency_p50": 0.5374113917350769,
      "latency_p95": 0.5374113917350769,
      "correct_class_logit_delta": 2.852629416195365,
      "incorrect_class_logit_delta_max": 4.801322711010774,
      "delta_correct_minus_top_wrong": -1.9486932827470203,
      "residual_help_rate": 0.8613265755896766,
      "residual_harm_rate": 0.13852425626464537,
      "token_to_sequence_transfer_ratio": 0.19108395974623343,
      "scopes": [
        "aux_all_tokens"
      ]
    },
    "sparse_ce_0_05": {
      "avg_loss": 0.4004437902864689,
      "avg_accuracy": 0.24243722927027295,
      "calibration_proxy": 0.129966046250579,
      "latency_p50": 0.5428085327148438,
      "latency_p95": 0.5428085327148438,
      "correct_class_logit_delta": 4.7784558494264875,
      "incorrect_class_logit_delta_max": 5.837446682155132,
      "delta_correct_minus_top_wrong": -1.058990823570639,
      "residual_help_rate": 0.9835581281222403,
      "residual_harm_rate": 0.016441862707324617,
      "token_to_sequence_transfer_ratio": 0.05323877146522142,
      "scopes": [
        "aux_all_tokens"
      ]
    },
    "wrong_suppress_0_03_t0_25": {
      "avg_loss": 0.44242214163144433,
      "avg_accuracy": 0.06802156528639025,
      "calibration_proxy": 0.11289403978065461,
      "latency_p50": 0.5414538979530334,
      "latency_p95": 0.5414538979530334,
      "correct_class_logit_delta": 1.0772574462813889,
      "incorrect_class_logit_delta_max": 2.6490566538025933,
      "delta_correct_minus_top_wrong": -1.5717992161711059,
      "residual_help_rate": 0.7839202222724755,
      "residual_harm_rate": 0.21606187428308962,
      "token_to_sequence_transfer_ratio": 0.0635509976466126,
      "scopes": [
        "aux_all_tokens"
      ]
    }
  },
  "best_auxiliary_loss": "sparse_ce_0_05",
  "baseline_variant": "baseline_main_loss",
  "helpful": true,
  "harmful": false
}
```