# Official Evaluation Boundary Freeze

Status: `OFFICIAL_EVALUATION_BOUNDARY_FROZEN`

## Tiers

| tier | may guide training | status/root | purpose |
|---|---|---|---|
| local heldout | true | `data/eval/broad_nlp, data/eval/coding, data/eval/routing_probes` | Fast regression and screening only. |
| official-like development | true | `data/eval/official_like_dev` / `READY` | Router/substrate development; final official examples excluded. |
| final official bounded | false | `data/eval/official_300m_bounded` | Final untouched evaluation only. |

## Assertions

- final_official_files_present: `True`
- final_official_may_guide_training: `False`
- current_local_roots_have_no_exact_line_overlap_with_final: `True`
- official_like_development_set_ready: `True`

## Final Official Files

| path | bytes | lines | sha256 |
|---|---:|---:|---|
| data/eval/official_300m_bounded/arc_challenge.jsonl | 27321 | 64 | `634a846c5bc74ec68aefb7ec406761007fecdcd5459578170de943c6bef5fb77` |
| data/eval/official_300m_bounded/boolq.jsonl | 45054 | 64 | `02bf9efaf51420cde39cdacb3d43599744cf55dc63459ae2ad515005faa604ae` |
| data/eval/official_300m_bounded/gsm8k.jsonl | 8839 | 16 | `dd6f8e7327263a60b372e4e41982864c98c8a5c7d06242a0b53bad66d78e9762` |
| data/eval/official_300m_bounded/hellaswag.jsonl | 85171 | 64 | `8816236184840f2f3ddc0f2b8675da598f6f50c1eb293d053c7755942de941a8` |
| data/eval/official_300m_bounded/humaneval.jsonl | 12532 | 8 | `f61186f43e80a033c9268d1188a0f4420c83cc911cccdd20e539f321fdc4e984` |
| data/eval/official_300m_bounded/mbpp.jsonl | 5294 | 8 | `8c968039acb9ee9564bd78167a365010a3e4f243ff988106facceefd38f963c1` |
| data/eval/official_300m_bounded/mmlu.jsonl | 55203 | 64 | `7260aaebf8f8ea2849e437abaee646eef3dacd35c5bba394abc4d32baaf844c7` |
| data/eval/official_300m_bounded/official_300m_data_manifest.json | 53243 | 1198 | `9d73220d712170b26673508c12a2f754eca216212274b2f04a8aae6de202ce70` |
| data/eval/official_300m_bounded/winogrande.jsonl | 12603 | 64 | `ff083be668d5fe3dfe39b73123e946e043c61733ba76a34031506c6a39c36db5` |

## Exact Line-Hash Overlap With Current Local Roots

| root | overlap with final lines |
|---|---:|
| data/eval/broad_nlp | 0 |
| data/eval/coding | 0 |
| data/eval/routing_probes | 0 |
| data/eval/official_like_dev | 0 |

Do not use the final eight official files for router repair, checkpoint selection, or hyperparameter search.
