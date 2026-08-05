# EAN Delta Replay Promotion Audit

Status: `PVR_EAN_DELTA_REPLAY_PROMOTION_AUDIT_NOT_SUPPORTED`
Candidate: `pvr_ec_o_ean_delta_replay_v1`

| model | broad LM | code-heavy | json/schema | unseen structured | Top1 clean |
|---|---:|---:|---:|---:|---|
| dense_300m | 2.776603478938341 | 15.14897346496582 | 14.023216485977173 | 14.586094975471497 | None |
| switch_top1_300m | 2.781601406633854 | 12.925040006637573 | 10.560967445373535 | 11.743003726005554 | None |
| pvr_baseline_300m | 2.824210923165083 | 10.372926354408264 | 10.401772260665894 | 10.387349307537079 | True |
| pvr_ean_300m | 2.595274433493614 | 12.958750128746033 | 12.983597993850708 | 12.97117406129837 | True |
| pvr_ean_delta_replay_300m | 2.8265555687248707 | 10.417477488517761 | 10.136144638061523 | 10.276811063289642 | True |

```json
{
  "benchmark_evidence_caveat": "This is an official-style reduced holdout audit over local reduced eval files. It is stronger than the diagnostic repair run, but it is not official broad benchmark promotion evidence until full benchmark adapters are implemented.",
  "broad_windows": 64,
  "candidate": "pvr_ec_o_ean_delta_replay_v1",
  "created_at": "2026-06-17T03:41:31.576979+00:00",
  "decision_rule": "Promote only if broad/prose LM does not regress versus EAN, structured heldout slices improve, reduced LM beats dense/Switch/PVR baseline, Top1 stays clean, and replay examples are excluded from final structured evaluation.",
  "device": "cuda",
  "do_not_promote": [
    "PVR_EAN_DELTA_REPLAY_OFFICIAL_PROMOTION_SUPPORTED",
    "PVR_EAN_FULL_REPEAT_CLEAN",
    "PVR_FROM_SCRATCH_DENSE_GAP_CLOSED",
    "PVR_TEACHER_INDEPENDENCE_SUPPORTED"
  ],
  "eval_plan": {
    "broad_lm": [
      {
        "end": 7032,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_0",
        "start": 6903
      },
      {
        "end": 13936,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_1",
        "start": 13807
      },
      {
        "end": 20840,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_2",
        "start": 20711
      },
      {
        "end": 27744,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_3",
        "start": 27615
      },
      {
        "end": 34648,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_4",
        "start": 34519
      },
      {
        "end": 41552,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_5",
        "start": 41423
      },
      {
        "end": 48456,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_6",
        "start": 48327
      },
      {
        "end": 55360,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_7",
        "start": 55231
      },
      {
        "end": 62264,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_8",
        "start": 62135
      },
      {
        "end": 69168,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_9",
        "start": 69039
      },
      {
        "end": 76072,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_10",
        "start": 75943
      },
      {
        "end": 82976,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_11",
        "start": 82847
      },
      {
        "end": 89880,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_12",
        "start": 89751
      },
      {
        "end": 96784,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_13",
        "start": 96655
      },
      {
        "end": 103688,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_14",
        "start": 103559
      },
      {
        "end": 110592,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_15",
        "start": 110463
      },
      {
        "end": 117495,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_16",
        "start": 117366
      },
      {
        "end": 124399,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_17",
        "start": 124270
      },
      {
        "end": 131303,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_18",
        "start": 131174
      },
      {
        "end": 138207,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_19",
        "start": 138078
      },
      {
        "end": 145111,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_20",
        "start": 144982
      },
      {
        "end": 152015,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_21",
        "start": 151886
      },
      {
        "end": 158919,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_22",
        "start": 158790
      },
      {
        "end": 165823,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_23",
        "start": 165694
      },
      {
        "end": 172727,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_24",
        "start": 172598
      },
      {
        "end": 179631,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_25",
        "start": 179502
      },
      {
        "end": 186535,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_26",
        "start": 186406
      },
      {
        "end": 193439,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_27",
        "start": 193310
      },
      {
        "end": 200343,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_28",
        "start": 200214
      },
      {
        "end": 207247,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_29",
        "start": 207118
      },
      {
        "end": 214151,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_30",
        "start": 214022
      },
      {
        "end": 221055,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_31",
        "start": 220926
      },
      {
        "end": 227958,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_32",
        "start": 227829
      },
      {
        "end": 234862,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_33",
        "start": 234733
      },
      {
        "end": 241766,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_34",
        "start": 241637
      },
      {
        "end": 248670,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_35",
        "start": 248541
      },
      {
        "end": 255574,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_36",
        "start": 255445
      },
      {
        "end": 262478,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_37",
        "start": 262349
      },
      {
        "end": 269382,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_38",
        "start": 269253
      },
      {
        "end": 276286,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_39",
        "start": 276157
      },
      {
        "end": 283190,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_40",
        "start": 283061
      },
      {
        "end": 290094,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_41",
        "start": 289965
      },
      {
        "end": 296998,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_42",
        "start": 296869
      },
      {
        "end": 303902,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_43",
        "start": 303773
      },
      {
        "end": 310806,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_44",
        "start": 310677
      },
      {
        "end": 317710,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_45",
        "start": 317581
      },
      {
        "end": 324614,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_46",
        "start": 324485
      },
      {
        "end": 331518,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_47",
        "start": 331389
      },
      {
        "end": 338421,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_48",
        "start": 338292
      },
      {
        "end": 345325,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_49",
        "start": 345196
      },
      {
        "end": 352229,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_50",
        "start": 352100
      },
      {
        "end": 359133,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_51",
        "start": 359004
      },
      {
        "end": 366037,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_52",
        "start": 365908
      },
      {
        "end": 372941,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_53",
        "start": 372812
      },
      {
        "end": 379845,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_54",
        "start": 379716
      },
      {
        "end": 386749,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_55",
        "start": 386620
      },
      {
        "end": 393653,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_56",
        "start": 393524
      },
      {
        "end": 400557,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_57",
        "start": 400428
      },
      {
        "end": 407461,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_58",
        "start": 407332
      },
      {
        "end": 414365,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_59",
        "start": 414236
      },
      {
        "end": 421269,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_60",
        "start": 421140
      },
      {
        "end": 428173,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_61",
        "start": 428044
      },
      {
        "end": 435077,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_62",
        "start": 434948
      },
      {
        "end": 441981,
        "family": "broad_lm",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "broad_lm_63",
        "start": 441852
      }
    ],
    "code_heavy": [
      {
        "end": 42990,
        "family": "humaneval_like",
        "path": "data/eval/coding/humaneval_base.jsonl",
        "span_id": "humaneval_like_0",
        "start": 42861
      },
      {
        "end": 85852,
        "family": "humaneval_like",
        "path": "data/eval/coding/humaneval_base.jsonl",
        "span_id": "humaneval_like_1",
        "start": 85723
      },
      {
        "end": 128714,
        "family": "humaneval_like",
        "path": "data/eval/coding/humaneval_base.jsonl",
        "span_id": "humaneval_like_2",
        "start": 128585
      },
      {
        "end": 171576,
        "family": "humaneval_like",
        "path": "data/eval/coding/humaneval_base.jsonl",
        "span_id": "humaneval_like_3",
        "start": 171447
      }
    ],
    "gutenberg_prose": [
      {
        "end": 7032,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_0",
        "start": 6903
      },
      {
        "end": 13936,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_1",
        "start": 13807
      },
      {
        "end": 20840,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_2",
        "start": 20711
      },
      {
        "end": 27744,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_3",
        "start": 27615
      },
      {
        "end": 34648,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_4",
        "start": 34519
      },
      {
        "end": 41552,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_5",
        "start": 41423
      },
      {
        "end": 48456,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_6",
        "start": 48327
      },
      {
        "end": 55360,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_7",
        "start": 55231
      },
      {
        "end": 62264,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_8",
        "start": 62135
      },
      {
        "end": 69168,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_9",
        "start": 69039
      },
      {
        "end": 76072,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_10",
        "start": 75943
      },
      {
        "end": 82976,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_11",
        "start": 82847
      },
      {
        "end": 89880,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_12",
        "start": 89751
      },
      {
        "end": 96784,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_13",
        "start": 96655
      },
      {
        "end": 103688,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_14",
        "start": 103559
      },
      {
        "end": 110592,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_15",
        "start": 110463
      },
      {
        "end": 117495,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_16",
        "start": 117366
      },
      {
        "end": 124399,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_17",
        "start": 124270
      },
      {
        "end": 131303,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_18",
        "start": 131174
      },
      {
        "end": 138207,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_19",
        "start": 138078
      },
      {
        "end": 145111,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_20",
        "start": 144982
      },
      {
        "end": 152015,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_21",
        "start": 151886
      },
      {
        "end": 158919,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_22",
        "start": 158790
      },
      {
        "end": 165823,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_23",
        "start": 165694
      },
      {
        "end": 172727,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_24",
        "start": 172598
      },
      {
        "end": 179631,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_25",
        "start": 179502
      },
      {
        "end": 186535,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_26",
        "start": 186406
      },
      {
        "end": 193439,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_27",
        "start": 193310
      },
      {
        "end": 200343,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_28",
        "start": 200214
      },
      {
        "end": 207247,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_29",
        "start": 207118
      },
      {
        "end": 214151,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_30",
        "start": 214022
      },
      {
        "end": 221055,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_31",
        "start": 220926
      },
      {
        "end": 227958,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_32",
        "start": 227829
      },
      {
        "end": 234862,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_33",
        "start": 234733
      },
      {
        "end": 241766,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_34",
        "start": 241637
      },
      {
        "end": 248670,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_35",
        "start": 248541
      },
      {
        "end": 255574,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_36",
        "start": 255445
      },
      {
        "end": 262478,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_37",
        "start": 262349
      },
      {
        "end": 269382,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_38",
        "start": 269253
      },
      {
        "end": 276286,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_39",
        "start": 276157
      },
      {
        "end": 283190,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_40",
        "start": 283061
      },
      {
        "end": 290094,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_41",
        "start": 289965
      },
      {
        "end": 296998,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_42",
        "start": 296869
      },
      {
        "end": 303902,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_43",
        "start": 303773
      },
      {
        "end": 310806,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_44",
        "start": 310677
      },
      {
        "end": 317710,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_45",
        "start": 317581
      },
      {
        "end": 324614,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_46",
        "start": 324485
      },
      {
        "end": 331518,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_47",
        "start": 331389
      },
      {
        "end": 338421,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_48",
        "start": 338292
      },
      {
        "end": 345325,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_49",
        "start": 345196
      },
      {
        "end": 352229,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_50",
        "start": 352100
      },
      {
        "end": 359133,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_51",
        "start": 359004
      },
      {
        "end": 366037,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_52",
        "start": 365908
      },
      {
        "end": 372941,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_53",
        "start": 372812
      },
      {
        "end": 379845,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_54",
        "start": 379716
      },
      {
        "end": 386749,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_55",
        "start": 386620
      },
      {
        "end": 393653,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_56",
        "start": 393524
      },
      {
        "end": 400557,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_57",
        "start": 400428
      },
      {
        "end": 407461,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_58",
        "start": 407332
      },
      {
        "end": 414365,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_59",
        "start": 414236
      },
      {
        "end": 421269,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_60",
        "start": 421140
      },
      {
        "end": 428173,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_61",
        "start": 428044
      },
      {
        "end": 435077,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_62",
        "start": 434948
      },
      {
        "end": 441981,
        "family": "gutenberg_prose",
        "path": "data/eval/broad_nlp/gutenberg_frankenstein_heldout.txt",
        "span_id": "gutenberg_prose_63",
        "start": 441852
      }
    ],
    "humaneval_like_heldout": [
      {
        "end": 42990,
        "family": "humaneval_like",
        "path": "data/eval/coding/humaneval_base.jsonl",
        "span_id": "humaneval_like_0",
        "start": 42861
      },
      {
        "end": 85852,
        "family": "humaneval_like",
        "path": "data/eval/coding/humaneval_base.jsonl",
        "span_id": "humaneval_like_1",
        "start": 85723
      },
      {
        "end": 128714,
        "family": "humaneval_like",
        "path": "data/eval/coding/humaneval_base.jsonl",
        "span_id": "humaneval_like_2",
        "start": 128585
      },
      {
        "end": 171576,
        "family": "humaneval_like",
        "path": "data/eval/coding/humaneval_base.jsonl",
        "span_id": "humaneval_like_3",
        "start": 171447
      }
    ],
    "json_schema": [
      {
        "end": 2784,
        "family": "json_schema",
        "path": "data/eval/broad_nlp/json_schema_test_suite_type.txt",
        "span_id": "json_schema_0",
        "start": 2655
      },
      {
        "end": 5440,
        "family": "json_schema",
        "path": "data/eval/broad_nlp/json_schema_test_suite_type.txt",
        "span_id": "json_schema_1",
        "start": 5311
      },
      {
        "end": 8096,
        "family": "json_schema",
        "path": "data/eval/broad_nlp/json_schema_test_suite_type.txt",
        "span_id": "json_schema_2",
        "start": 7967
      },
      {
        "end": 10752,
        "family": "json_schema",
        "path": "data/eval/broad_nlp/json_schema_test_suite_type.txt",
        "span_id": "json_schema_3",
        "start": 10623
      }
    ],
    "unseen_structured_spans": [
      {
        "end": 42990,
        "family": "humaneval_like",
        "path": "data/eval/coding/humaneval_base.jsonl",
        "span_id": "humaneval_like_0",
        "start": 42861
      },
      {
        "end": 85852,
        "family": "humaneval_like",
        "path": "data/eval/coding/humaneval_base.jsonl",
        "span_id": "humaneval_like_1",
        "start": 85723
      },
      {
        "end": 128714,
        "family": "humaneval_like",
        "path": "data/eval/coding/humaneval_base.jsonl",
        "span_id": "humaneval_like_2",
        "start": 128585
      },
      {
        "end": 171576,
        "family": "humaneval_like",
        "path": "data/eval/coding/humaneval_base.jsonl",
        "span_id": "humaneval_like_3",
        "start": 171447
      },
      {
        "end": 2784,
        "family": "json_schema",
        "path": "data/eval/broad_nlp/json_schema_test_suite_type.txt",
        "span_id": "json_schema_0",
        "start": 2655
      },
      {
        "end": 5440,
        "family": "json_schema",
        "path": "data/eval/broad_nlp/json_schema_test_suite_type.txt",
        "span_id": "json_schema_1",
        "start": 5311
      },
      {
        "end": 8096,
        "family": "json_schema",
        "path": "data/eval/broad_nlp/json_schema_test_suite_type.txt",
        "span_id": "json_schema_2",
        "start": 7967
      },
      {
        "end": 10752,
        "family": "json_schema",
        "path": "data/eval/broad_nlp/json_schema_test_suite_type.txt",
        "span_id": "json_schema_3",
        "start": 10623
      }
    ]
  },
  "experiment": "PVR_EAN_DELTA_REPLAY_PROMOTION_AUDIT",
  "git_commit": "d18165e32bec94cea3ca836937c81f6a0f3dc5f7",
  "models": [
    "dense_300m",
    "switch_top1_300m",
    "pvr_baseline_300m",
    "pvr_ean_300m",
    "pvr_ean_delta_replay_300m"
  ],
  "replay_exclusion_policy": {
    "excluded_span_count": 8,
    "final_structured_eval_uses_only_excluded_humaneval_json_spans": true,
    "structured_replay_training_used_all_non_heldout_bytes": true
  },
  "rows": {
    "dense_300m": {
      "active_flops_estimate": 1800000000,
      "active_params_per_token": 300000000,
      "checkpoint_path": "checkpoints/benchmark_300m/dense_transformer_300m/checkpoint.pt",
      "config_path": "benchmark/reports/generated/training_300m_real_4k/dense_transformer_300m/run_config.yaml",
      "label": "dense_300m",
      "model_family": "dense_transformer",
      "model_variant": "dense_transformer_300m",
      "routing_snapshots": [],
      "slice_summary": {
        "broad_lm": {
          "max_loss": 10.864638328552246,
          "mean_delta_vs_candidate": -0.04995208978652954,
          "mean_loss": 2.776603478938341,
          "min_loss": 2.2984459400177,
          "win_rate_vs_candidate": 0.140625,
          "window_count": 64,
          "wins_vs_candidate": 9
        },
        "code_heavy": {
          "max_loss": 19.473281860351562,
          "mean_delta_vs_candidate": 4.731495976448059,
          "mean_loss": 15.14897346496582,
          "min_loss": 9.624191284179688,
          "win_rate_vs_candidate": 1.0,
          "window_count": 4,
          "wins_vs_candidate": 4
        },
        "gutenberg_prose": {
          "max_loss": 10.864638328552246,
          "mean_delta_vs_candidate": -0.04995208978652954,
          "mean_loss": 2.776603478938341,
          "min_loss": 2.2984459400177,
          "win_rate_vs_candidate": 0.140625,
          "window_count": 64,
          "wins_vs_candidate": 9
        },
        "humaneval_like_heldout": {
          "max_loss": 19.473281860351562,
          "mean_delta_vs_candidate": 4.731495976448059,
          "mean_loss": 15.14897346496582,
          "min_loss": 9.624191284179688,
          "win_rate_vs_candidate": 1.0,
          "window_count": 4,
          "wins_vs_candidate": 4
        },
        "json_schema": {
          "max_loss": 16.16033935546875,
          "mean_delta_vs_candidate": 3.8870718479156494,
          "mean_loss": 14.023216485977173,
          "min_loss": 13.100582122802734,
          "win_rate_vs_candidate": 1.0,
          "window_count": 4,
          "wins_vs_candidate": 4
        },
        "unseen_structured_spans": {
          "max_loss": 19.473281860351562,
          "mean_delta_vs_candidate": 4.309283912181854,
          "mean_loss": 14.586094975471497,
          "min_loss": 9.624191284179688,
          "win_rate_vs_candidate": 1.0,
          "window_count": 8,
          "wins_vs_candidate": 8
        }
      },
      "top1_invariants_clean": null
    },
    "pvr_baseline_300m": {
      "active_flops_estimate": 630000000,
      "active_params_per_token": 105000000,
      "checkpoint_path": "checkpoints/shared_trunk_init_300m_repeat_seed_42/pvr_ec_o_full_300m_baseline_seed_42/checkpoint.pt",
      "config_path": "benchmark/reports/generated/shared_trunk_init_300m_repeat_seed_42/pvr_ec_o_full_300m_baseline_seed_42/run_config.yaml",
      "label": "pvr_baseline_300m",
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
          "mean_delta_vs_candidate": -0.0023446455597877502,
          "mean_loss": 2.824210923165083,
          "min_loss": 2.3216283321380615,
          "win_rate_vs_candidate": 0.21875,
          "window_count": 64,
          "wins_vs_candidate": 14
        },
        "code_heavy": {
          "max_loss": 13.306273460388184,
          "mean_delta_vs_candidate": -0.04455113410949707,
          "mean_loss": 10.372926354408264,
          "min_loss": 7.083217144012451,
          "win_rate_vs_candidate": 0.75,
          "window_count": 4,
          "wins_vs_candidate": 3
        },
        "gutenberg_prose": {
          "max_loss": 12.159866333007812,
          "mean_delta_vs_candidate": -0.0023446455597877502,
          "mean_loss": 2.824210923165083,
          "min_loss": 2.3216283321380615,
          "win_rate_vs_candidate": 0.21875,
          "window_count": 64,
          "wins_vs_candidate": 14
        },
        "humaneval_like_heldout": {
          "max_loss": 13.306273460388184,
          "mean_delta_vs_candidate": -0.04455113410949707,
          "mean_loss": 10.372926354408264,
          "min_loss": 7.083217144012451,
          "win_rate_vs_candidate": 0.75,
          "window_count": 4,
          "wins_vs_candidate": 3
        },
        "json_schema": {
          "max_loss": 11.232419967651367,
          "mean_delta_vs_candidate": 0.2656276226043701,
          "mean_loss": 10.401772260665894,
          "min_loss": 9.930900573730469,
          "win_rate_vs_candidate": 0.5,
          "window_count": 4,
          "wins_vs_candidate": 2
        },
        "unseen_structured_spans": {
          "max_loss": 13.306273460388184,
          "mean_delta_vs_candidate": 0.11053824424743652,
          "mean_loss": 10.387349307537079,
          "min_loss": 7.083217144012451,
          "win_rate_vs_candidate": 0.625,
          "window_count": 8,
          "wins_vs_candidate": 5
        }
      },
      "top1_invariants_clean": true
    },
    "pvr_ean_300m": {
      "active_flops_estimate": 630000000,
      "active_params_per_token": 105000000,
      "checkpoint_path": "checkpoints/ean_init_300m_repeat_seed_42/pvr_ec_o_full_300m_shared_trunk_init_v1_scope_embeddings_attention_norms_seed_42/checkpoint.pt",
      "config_path": "benchmark/reports/generated/ean_init_300m_repeat_seed_42/pvr_ec_o_full_300m_shared_trunk_init_v1_scope_embeddings_attention_norms_seed_42/run_config.yaml",
      "label": "pvr_ean_300m",
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
          "mean_delta_vs_candidate": -0.23128113523125648,
          "mean_loss": 2.595274433493614,
          "min_loss": 2.263871908187866,
          "win_rate_vs_candidate": 0.015625,
          "window_count": 64,
          "wins_vs_candidate": 1
        },
        "code_heavy": {
          "max_loss": 16.904939651489258,
          "mean_delta_vs_candidate": 2.5412726402282715,
          "mean_loss": 12.958750128746033,
          "min_loss": 7.81622838973999,
          "win_rate_vs_candidate": 1.0,
          "window_count": 4,
          "wins_vs_candidate": 4
        },
        "gutenberg_prose": {
          "max_loss": 7.311913013458252,
          "mean_delta_vs_candidate": -0.23128113523125648,
          "mean_loss": 2.595274433493614,
          "min_loss": 2.263871908187866,
          "win_rate_vs_candidate": 0.015625,
          "window_count": 64,
          "wins_vs_candidate": 1
        },
        "humaneval_like_heldout": {
          "max_loss": 16.904939651489258,
          "mean_delta_vs_candidate": 2.5412726402282715,
          "mean_loss": 12.958750128746033,
          "min_loss": 7.81622838973999,
          "win_rate_vs_candidate": 1.0,
          "window_count": 4,
          "wins_vs_candidate": 4
        },
        "json_schema": {
          "max_loss": 15.211018562316895,
          "mean_delta_vs_candidate": 2.8474533557891846,
          "mean_loss": 12.983597993850708,
          "min_loss": 12.034255027770996,
          "win_rate_vs_candidate": 1.0,
          "window_count": 4,
          "wins_vs_candidate": 4
        },
        "unseen_structured_spans": {
          "max_loss": 16.904939651489258,
          "mean_delta_vs_candidate": 2.694362998008728,
          "mean_loss": 12.97117406129837,
          "min_loss": 7.81622838973999,
          "win_rate_vs_candidate": 1.0,
          "window_count": 8,
          "wins_vs_candidate": 8
        }
      },
      "top1_invariants_clean": true
    },
    "pvr_ean_delta_replay_300m": {
      "active_flops_estimate": 630000000,
      "active_params_per_token": 105000000,
      "checkpoint_path": "checkpoints/ean_delta_replay_generalization_audit_seed_42/pvr_ec_o_embeddings_attention_norms_init_v1_delta_replay_generalization_seed_42/checkpoint.pt",
      "config_path": "benchmark/configs/generated/pvr_ec_o_ean_delta_replay_v1_300m.yaml",
      "label": "pvr_ean_delta_replay_300m",
      "model_family": "pvr_ec_o",
      "model_variant": "pvr_ec_o_ean_delta_replay_v1_300m",
      "routing_snapshots": [
        {
          "challenger_disagreement_rate": null,
          "descriptor_control_margin": 0.5185521709427121,
          "expert_utilization": [
            328,
            269,
            474,
            645,
            244,
            398,
            345,
            369
          ],
          "failure_mode_distribution": {},
          "high_gap_monopoly_rate": 0.2099609375,
          "operator_control_margin": 0.5185521709427121,
          "owner_churn": null,
          "owner_entropy": 2.034254576011979,
          "owners_per_token": 1.0,
          "production_map_mutated": false,
          "prototype_entropy": 2.034254576011979,
          "prototype_margin": 0.5185521709427121,
          "prototype_monopoly_rate": 0.2099609375,
          "runtime_dynamic_k_count": 0,
          "runtime_expert_choice_count": 0,
          "stale_owner_rate": null,
          "step": 0,
          "top2_execution_count": 0,
          "top4_execution_count": 0
        },
        {
          "challenger_disagreement_rate": null,
          "descriptor_control_margin": 0.5182241541915573,
          "expert_utilization": [
            292,
            311,
            512,
            731,
            224,
            396,
            268,
            338
          ],
          "failure_mode_distribution": {},
          "high_gap_monopoly_rate": 0.23795572916666666,
          "operator_control_margin": 0.5182241541915573,
          "owner_churn": null,
          "owner_entropy": 2.0064353573633085,
          "owners_per_token": 1.0,
          "production_map_mutated": false,
          "prototype_entropy": 2.0064353573633085,
          "prototype_margin": 0.5182241541915573,
          "prototype_monopoly_rate": 0.23795572916666666,
          "runtime_dynamic_k_count": 0,
          "runtime_expert_choice_count": 0,
          "stale_owner_rate": null,
          "step": 25,
          "top2_execution_count": 0,
          "top4_execution_count": 0
        },
        {
          "challenger_disagreement_rate": null,
          "descriptor_control_margin": 0.5200993601768763,
          "expert_utilization": [
            279,
            275,
            511,
            752,
            237,
            414,
            276,
            328
          ],
          "failure_mode_distribution": {},
          "high_gap_monopoly_rate": 0.24479166666666666,
          "operator_control_margin": 0.5200993601768763,
          "owner_churn": null,
          "owner_entropy": 1.999882081151847,
          "owners_per_token": 1.0,
          "production_map_mutated": false,
          "prototype_entropy": 1.999882081151847,
          "prototype_margin": 0.5200993601768763,
          "prototype_monopoly_rate": 0.24479166666666666,
          "runtime_dynamic_k_count": 0,
          "runtime_expert_choice_count": 0,
          "stale_owner_rate": null,
          "step": 50,
          "top2_execution_count": 0,
          "top4_execution_count": 0
        },
        {
          "challenger_disagreement_rate": null,
          "descriptor_control_margin": 0.5077122714671228,
          "expert_utilization": [
            354,
            268,
            507,
            657,
            246,
            363,
            322,
            355
          ],
          "failure_mode_distribution": {},
          "high_gap_monopoly_rate": 0.2138671875,
          "operator_control_margin": 0.5077122714671228,
          "owner_churn": null,
          "owner_entropy": 2.0293138154270816,
          "owners_per_token": 1.0,
          "production_map_mutated": false,
          "prototype_entropy": 2.0293138154270816,
          "prototype_margin": 0.5077122714671228,
          "prototype_monopoly_rate": 0.2138671875,
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
          "max_loss": 6.883093357086182,
          "mean_delta_vs_candidate": 0.0,
          "mean_loss": 2.8265555687248707,
          "min_loss": 2.5174946784973145,
          "win_rate_vs_candidate": 0.0,
          "window_count": 64,
          "wins_vs_candidate": 0
        },
        "code_heavy": {
          "max_loss": 13.202263832092285,
          "mean_delta_vs_candidate": 0.0,
          "mean_loss": 10.417477488517761,
          "min_loss": 6.23173189163208,
          "win_rate_vs_candidate": 0.0,
          "window_count": 4,
          "wins_vs_candidate": 0
        },
        "gutenberg_prose": {
          "max_loss": 6.883093357086182,
          "mean_delta_vs_candidate": 0.0,
          "mean_loss": 2.8265555687248707,
          "min_loss": 2.5174946784973145,
          "win_rate_vs_candidate": 0.0,
          "window_count": 64,
          "wins_vs_candidate": 0
        },
        "humaneval_like_heldout": {
          "max_loss": 13.202263832092285,
          "mean_delta_vs_candidate": 0.0,
          "mean_loss": 10.417477488517761,
          "min_loss": 6.23173189163208,
          "win_rate_vs_candidate": 0.0,
          "window_count": 4,
          "wins_vs_candidate": 0
        },
        "json_schema": {
          "max_loss": 12.566546440124512,
          "mean_delta_vs_candidate": 0.0,
          "mean_loss": 10.136144638061523,
          "min_loss": 8.980449676513672,
          "win_rate_vs_candidate": 0.0,
          "window_count": 4,
          "wins_vs_candidate": 0
        },
        "unseen_structured_spans": {
          "max_loss": 13.202263832092285,
          "mean_delta_vs_candidate": 0.0,
          "mean_loss": 10.276811063289642,
          "min_loss": 6.23173189163208,
          "win_rate_vs_candidate": 0.0,
          "window_count": 8,
          "wins_vs_candidate": 0
        }
      },
      "top1_invariants_clean": true
    },
    "switch_top1_300m": {
      "active_flops_estimate": 630000000,
      "active_params_per_token": 105000000,
      "checkpoint_path": "checkpoints/benchmark_300m/vanilla_switch_top1_reference_300m/checkpoint.pt",
      "config_path": "benchmark/reports/generated/training_300m_real_4k/vanilla_switch_top1_reference_300m/run_config.yaml",
      "label": "switch_top1_300m",
      "model_family": "vanilla_switch_top1_reference",
      "model_variant": "vanilla_switch_top1_reference_300m",
      "routing_snapshots": [],
      "slice_summary": {
        "broad_lm": {
          "max_loss": 12.778247833251953,
          "mean_delta_vs_candidate": -0.04495416209101677,
          "mean_loss": 2.781601406633854,
          "min_loss": 2.336674690246582,
          "win_rate_vs_candidate": 0.109375,
          "window_count": 64,
          "wins_vs_candidate": 7
        },
        "code_heavy": {
          "max_loss": 15.58360767364502,
          "mean_delta_vs_candidate": 2.507562518119812,
          "mean_loss": 12.925040006637573,
          "min_loss": 9.247726440429688,
          "win_rate_vs_candidate": 1.0,
          "window_count": 4,
          "wins_vs_candidate": 4
        },
        "gutenberg_prose": {
          "max_loss": 12.778247833251953,
          "mean_delta_vs_candidate": -0.04495416209101677,
          "mean_loss": 2.781601406633854,
          "min_loss": 2.336674690246582,
          "win_rate_vs_candidate": 0.109375,
          "window_count": 64,
          "wins_vs_candidate": 7
        },
        "humaneval_like_heldout": {
          "max_loss": 15.58360767364502,
          "mean_delta_vs_candidate": 2.507562518119812,
          "mean_loss": 12.925040006637573,
          "min_loss": 9.247726440429688,
          "win_rate_vs_candidate": 1.0,
          "window_count": 4,
          "wins_vs_candidate": 4
        },
        "json_schema": {
          "max_loss": 11.368138313293457,
          "mean_delta_vs_candidate": 0.4248228073120117,
          "mean_loss": 10.560967445373535,
          "min_loss": 10.17562198638916,
          "win_rate_vs_candidate": 0.75,
          "window_count": 4,
          "wins_vs_candidate": 3
        },
        "unseen_structured_spans": {
          "max_loss": 15.58360767364502,
          "mean_delta_vs_candidate": 1.4661926627159119,
          "mean_loss": 11.743003726005554,
          "min_loss": 9.247726440429688,
          "win_rate_vs_candidate": 0.875,
          "window_count": 8,
          "wins_vs_candidate": 7
        }
      },
      "top1_invariants_clean": null
    }
  },
  "schema_version": "1.0",
  "seq_len": 128,
  "status": "PVR_EAN_DELTA_REPLAY_PROMOTION_AUDIT_NOT_SUPPORTED",
  "supported_conditions": {
    "broad_lm_does_not_regress_vs_ean": false,
    "code_heavy_improves_vs_ean": true,
    "gutenberg_prose_does_not_regress_vs_ean": false,
    "humaneval_like_heldout_improves_vs_ean": true,
    "json_schema_improves_vs_ean": true,
    "reduced_lm_beats_dense": false,
    "reduced_lm_beats_pvr_baseline": false,
    "reduced_lm_beats_switch_top1": false,
    "replay_examples_excluded_from_final_structured_eval": true,
    "top1_invariants_clean": true,
    "unseen_structured_spans_improve_vs_ean": true
  }
}
```
