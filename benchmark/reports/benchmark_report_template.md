# PVR-EC-O Benchmark Report Template

Status: `BENCH_INFRASTRUCTURE_READY`, `NOT_RUN_MISSING_CHECKPOINT`, `NOT_RUN_MISSING_DATA`, or a genuine benchmark stage status.

This report separates:

- Primary generalized baseline result
- Public model external positioning result
- Internal strong-router control result
- Single-size result
- Multi-size scaling result

Required scorecard fields:

- Model
- Checkpoint
- Training tokens
- Total params
- Active params/token
- Context length
- Tokenizer
- Training data manifest hash
- Eval manifest hash
- Contamination scan
- Hardware
- Wall clock
- GPU hours
- VRAM peak
- Throughput

Allowed conclusion language:

- PVR-EC-O does not yet beat generalized baselines.
- PVR-EC-O beats generalized baselines but lags internal strong-router control.
- PVR-EC-O matches internal strong-router control.
- PVR-EC-O beats internal strong-router control.

Infrastructure execution alone is not benchmark evidence.

