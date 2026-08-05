# Dense Mimic 4000-Step Confirmation

Status: `PVR_DENSE_MIMIC_NOT_SUPPORTED`

Budget:
- optimizer steps: `4000`
- training tokens/model: `1024000`
- eval windows: `10`

Deltas are dense_mimic_w0001 minus baseline:
- final train loss delta: `-0.011478424072265625`
- mean eval loss delta: `0.020994186401367188`
- mean route margin delta: `-0.02785573575796052`
- owner entropy delta: `0.002763943315938544`
- prototype monopoly delta: `-0.002539062500000022`

Top1 and route-collapse checks remained clean, but mean eval loss worsened. The 1000-step gentle dense-mimic signal did not confirm at 4000 steps.

Decision: do not promote gentle dense mimic yet.


This supersedes the earlier 1000-step recommendation report.
