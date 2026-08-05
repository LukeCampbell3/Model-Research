# Shared-Trunk Init Copy-Scope Ablation

Status: `PVR_SHARED_TRUNK_COPY_SCOPE_ABLATION_COMPLETE`

Best scope by LM loss: `embeddings_attention_norms`

| scope | LM loss | mean eval | train delta | LM delta | route stable |
|---|---:|---:|---:|---:|---|
| embeddings_only | 3.403685820102692 | 5.471221661567688 | -0.04696035385131836 | -0.1030181169509885 | True |
| attention_only | 3.384330289363861 | 5.751970911026001 | 0.028476238250732422 | -0.12237364768981918 | True |
| norms_only | 3.4968364417552946 | 5.513810610771179 | -0.001220703125 | -0.009867495298385709 | True |
| shared_ffn_bias_only | 3.4958942592144013 | 5.410947728157043 | -0.013668298721313477 | -0.010809677839278997 | True |
| embeddings_attention_norms | 3.0279019391536712 | 4.97853536605835 | -0.28342533111572266 | -0.4788019979000091 | True |
| full_compatible_shared_copy | 3.0312132823467253 | 4.987043190002441 | -0.2915973663330078 | -0.47549065470695506 | True |