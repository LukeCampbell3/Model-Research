# GPU Diagnostics

## Status: GPU_READY

| Check | Result |
|-------|--------|
| Host nvidia-smi | PASS: RTX 4080 SUPER, Driver 596.49, CUDA 13.2 |
| Docker image | PASS: sparse-loop-moe-gpu (sha256:59d288be87ff) |
| Docker nvidia-smi | PASS: GPU visible inside container |
| PyTorch CUDA | PASS: torch 2.2.0, CUDA 12.1, device_count=1 |
| GPU Name | NVIDIA GeForce RTX 4080 SUPER |
| GPU Memory | 16,376 MiB total |
| Workspace Mount | PASS: /workspace mounted correctly |

## Ready for GPU Benchmarks
All validation checks passed. Proceeding with GPU-backed benchmark runs.
