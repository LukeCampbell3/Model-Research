# PVR Shared Substrate Repair Screen

Status: `PVR_SHARED_SUBSTRATE_REPAIR_SCREEN_COMPLETE`
Decision: `PVR_SHARED_SUBSTRATE_REPAIR_CANDIDATE_IDENTIFIED`
Git commit: `bce74c6d7a7bd91cbe8b197f6bc5d37b6b22c457`

Teacher-independent substrate screen on broad_nlp_train with official_like_dev evaluation. Final official bounded files are not used.

## Claim Gates

- all_variants_completed: `True`
- all_rung_eval_windows_present: `True`
- strict_top1_clean_for_completed_pvr: `True`
- final_block_oracle_audits_present: `True`
- official_final_files_used: `False`

## Result Table

| variant | substrate | curriculum | tokens | eval windows | final eval | final train | owner entropy | margin | monopoly |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| pvr_shared_substrate_attention_norms_current_300m | attention_norms | full_training | 1000448 | 4 | 12.47580623626709 | 4.6837897300720215 | 2.5607893665681427 | 0.4293489806053306 | 0.16259765625 |
| pvr_shared_substrate_embeddings_only_300m | embeddings_only | full_training | 1000448 | 4 | 19.63642120361328 | 7.0918707847595215 | 2.621898451476946 | 1.425149407691303 | 0.11962890625 |
| pvr_shared_substrate_embeddings_attention_300m | embeddings_attention | full_training | 1000448 | 4 | 14.690733909606934 | 4.7353129386901855 | 2.573044943319622 | 0.27261210469562985 | 0.14664713541666666 |
| pvr_shared_substrate_embeddings_norms_300m | embeddings_norms | full_training | 1000448 | 4 | 14.062399864196777 | 3.476972818374634 | 2.626422655428844 | 0.4520951272000578 | 0.14778645833333334 |
| pvr_shared_substrate_full_transformer_random_ean_300m | full_transformer_random_ean | full_training | 1000448 | 4 | 11.720563888549805 | 4.7035932540893555 | 2.5487222421403612 | 2.616085254444139 | 0.13981119791666666 |
| pvr_shared_substrate_wider_attention_norms_300m | attention_norms | full_training | 1000448 | 4 | 18.186853408813477 | 4.359861373901367 | 2.6350372053960633 | 0.3339781586934502 | 0.1259765625 |
| pvr_shared_substrate_deeper_attention_norms_300m | attention_norms | full_training | 1000448 | 4 | 16.337766647338867 | 4.26588249206543 | 2.64971511650856 | 0.26265684109447257 | 0.15387834821428573 |
| pvr_shared_substrate_staged_warmup_attention_norms_300m | attention_norms | shared_warmup_then_top1 | 1000448 | 4 | 12.96926212310791 | 3.483107805252075 | 2.6770063988442723 | 0.31404117641917156 | 0.12044270833333333 |

## Rung Eval Losses

### pvr_shared_substrate_attention_norms_current_300m
- `249856` tokens: step `244`, eval loss `20.738529205322266`
- `499712` tokens: step `488`, eval loss `18.943742752075195`
- `749568` tokens: step `732`, eval loss `10.079568862915039`
- `999424` tokens: step `976`, eval loss `12.47580623626709`

### pvr_shared_substrate_embeddings_only_300m
- `249856` tokens: step `244`, eval loss `49.57918930053711`
- `499712` tokens: step `488`, eval loss `34.583251953125`
- `749568` tokens: step `732`, eval loss `19.326231002807617`
- `999424` tokens: step `976`, eval loss `19.63642120361328`

### pvr_shared_substrate_embeddings_attention_300m
- `249856` tokens: step `244`, eval loss `19.151533126831055`
- `499712` tokens: step `488`, eval loss `19.39459800720215`
- `749568` tokens: step `732`, eval loss `11.304469108581543`
- `999424` tokens: step `976`, eval loss `14.690733909606934`

### pvr_shared_substrate_embeddings_norms_300m
- `249856` tokens: step `244`, eval loss `22.84304428100586`
- `499712` tokens: step `488`, eval loss `21.407127380371094`
- `749568` tokens: step `732`, eval loss `11.917950630187988`
- `999424` tokens: step `976`, eval loss `14.062399864196777`

### pvr_shared_substrate_full_transformer_random_ean_300m
- `249856` tokens: step `244`, eval loss `25.2797908782959`
- `499712` tokens: step `488`, eval loss `19.653305053710938`
- `749568` tokens: step `732`, eval loss `12.012409210205078`
- `999424` tokens: step `976`, eval loss `11.720563888549805`

### pvr_shared_substrate_wider_attention_norms_300m
- `249856` tokens: step `244`, eval loss `26.696693420410156`
- `499712` tokens: step `488`, eval loss `25.256181716918945`
- `749568` tokens: step `732`, eval loss `14.40093994140625`
- `999424` tokens: step `976`, eval loss `18.186853408813477`

### pvr_shared_substrate_deeper_attention_norms_300m
- `249856` tokens: step `244`, eval loss `25.1055908203125`
- `499712` tokens: step `488`, eval loss `23.598554611206055`
- `749568` tokens: step `732`, eval loss `13.501855850219727`
- `999424` tokens: step `976`, eval loss `16.337766647338867`

### pvr_shared_substrate_staged_warmup_attention_norms_300m
- `249856` tokens: step `244`, eval loss `15.376222610473633`
- `499712` tokens: step `488`, eval loss `18.31639862060547`
- `749568` tokens: step `732`, eval loss `11.391924858093262`
- `999424` tokens: step `976`, eval loss `12.96926212310791`

## Winner

Winner: `pvr_shared_substrate_full_transformer_random_ean_300m`
Delta vs current attention+norms baseline: `-0.7552423477172852`

## Final-Block Oracle / Regret

| variant | selected | shared-only | oracle | regret | oracle rate | top2 rate | mean wrong | wrong harm |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| pvr_shared_substrate_attention_norms_current_300m | 13.060628754752022 | 16.537790298461914 | 10.6698397227696 | 2.3907891116146596 | 0.20758928571428573 | 0.4263392857142857 | 19.861526216779435 | 6.800897462027413 |
| pvr_shared_substrate_embeddings_only_300m | 23.61526189531599 | 27.74079159327916 | 23.260616030011857 | 0.35464565304573625 | 0.8102678571428571 | 0.84375 | 27.91482707432338 | 4.299565179007391 |
| pvr_shared_substrate_embeddings_attention_300m | 16.76168414524623 | 16.76308740888323 | 16.73219530923026 | 0.02948880514928273 | 0.026785714285714284 | 0.10044642857142858 | 16.763585908072336 | 0.0019017628261046582 |
| pvr_shared_substrate_embeddings_norms_300m | 17.04397882734026 | 21.732930864606583 | 14.523618970598493 | 2.5203601606897013 | 0.24330357142857142 | 0.5357142857142857 | 26.887859344482422 | 9.84388051714216 |
| pvr_shared_substrate_full_transformer_random_ean_300m | 13.453469412667411 | 13.7130400793893 | 12.826674461364746 | 0.6267948352864811 | 0.3013392857142857 | 0.3638392857142857 | 13.763294492449079 | 0.3098250797816675 |
| pvr_shared_substrate_wider_attention_norms_300m | 23.644671031406947 | 29.635169982910156 | 21.801632744925364 | 1.8430385900927442 | 0.25223214285714285 | 0.6183035714285714 | 33.187565667288645 | 9.542894635881698 |
| pvr_shared_substrate_deeper_attention_norms_300m | 20.515610013689315 | 22.412247794015066 | 18.396947179521835 | 2.118663217606289 | 0.17410714285714285 | 0.40625 | 27.016403198242188 | 6.500793184552872 |
| pvr_shared_substrate_staged_warmup_attention_norms_300m | 15.438885688781738 | 17.38714095524379 | 13.770956039428711 | 1.6679293577575922 | 0.12053571428571429 | 0.28125 | 20.854692186628068 | 5.415806497846329 |
