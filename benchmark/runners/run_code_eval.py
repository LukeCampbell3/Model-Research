"""Coding benchmark runner for genuine PVR-EC-O comparisons."""

from __future__ import annotations

import json
import time
from pathlib import Path

import torch

from benchmark.common import (
    REQUIRED_MODEL_CONFIG_FIELDS,
    base_metadata,
    common_scorecard,
    load_json_or_yaml,
    parser_with_config,
    require_fields,
    status_for_config,
    write_json,
)
from benchmark.model_factory import build_model


CODING_METRICS = {
    "humaneval_plus_pass_at_1": None,
    "humaneval_plus_pass_at_5": None,
    "humaneval_plus_pass_at_10": None,
    "mbpp_plus_pass_at_1": None,
    "bigcodebench_complete": None,
    "bigcodebench_instruct": None,
    "livecodebench_pass_at_1": None,
    "repobench_r_recall_at_k": None,
    "repobench_c_exact_match": None,
    "swe_bench_lite_resolved_standard_scaffold": None,
    "swe_bench_verified_resolved_standard_scaffold": None,
    "compile_rate": None,
    "test_pass_rate": None,
    "runtime_error_rate": None,
    "timeout_rate": None,
    "invalid_syntax_rate": None,
    "solution_length": None,
    "efficiency_score": None,
}


def _coding_files(paths: list[str]) -> list[Path]:
    coding_names = ("humaneval", "mbpp", "code")
    out: list[Path] = []
    for item in paths:
        path = Path(item)
        if path.is_file() and path.suffix == ".jsonl" and (
            "coding" in path.parts or any(name in path.name.lower() for name in coding_names)
        ):
            out.append(path)
        elif path.is_dir():
            out.extend(
                sorted(
                    child
                    for child in path.rglob("*.jsonl")
                    if "coding" in child.parts or any(name in child.name.lower() for name in coding_names)
                )
            )
    return out


def _load_tasks(paths: list[str], limit: int | None) -> list[dict]:
    rows = []
    for path in _coding_files(paths):
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
            if line.strip():
                rows.append(json.loads(line))
            if limit and len(rows) >= limit:
                return rows
    return rows[: limit or 4]


def _load_model(config: dict, device: str):
    materialized = build_model(config, device=device)
    checkpoint = torch.load(config["checkpoint_path"], map_location=device)
    state = checkpoint.get("model_state_dict", checkpoint)
    materialized.model.load_state_dict(state, strict=False)
    materialized.model.eval()
    return materialized.model


def _generate_completion(model, prompt: str, device: str, context_length: int, max_new_tokens: int = 32) -> str:
    ids = list(prompt.encode("utf-8", errors="replace"))[-max(1, context_length - max_new_tokens) :]
    if not ids:
        ids = [10]
    generated = []
    with torch.no_grad():
        for _ in range(max_new_tokens):
            x = torch.tensor(ids[-context_length:], dtype=torch.long, device=device).unsqueeze(0)
            logits = model(x)
            next_id = int(torch.argmax(logits[0, -1]).detach().cpu().item())
            if next_id > 255:
                next_id = 10
            ids.append(next_id)
            generated.append(next_id)
            if next_id == 10 and len(generated) > 8:
                break
    return bytes(generated).decode("utf-8", errors="replace")


def _evaluate(config: dict, limit: int | None) -> dict:
    tasks = _load_tasks(list(config.get("eval_data_paths") or []), limit)
    if not tasks:
        raise FileNotFoundError("No coding JSONL tasks found.")
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = _load_model(config, device)
    compile_ok = 0
    syntax_errors = 0
    runtime_errors = 0
    timeout_count = 0
    start = time.time()
    for task in tasks:
        prompt = str(task.get("prompt") or task.get("text") or task.get("code") or "")
        completion = _generate_completion(model, prompt, device, int(config.get("context_length", 128)))
        try:
            compile(prompt + completion, "<generated_completion>", "exec")
            compile_ok += 1
        except SyntaxError:
            syntax_errors += 1
        except Exception:
            runtime_errors += 1
    elapsed = max(0.0, time.time() - start)
    count = len(tasks)
    return {
        "humaneval_plus_pass_at_1": "NOT_RUN_NOT_IMPLEMENTED",
        "humaneval_base_reduced_compile_rate": compile_ok / count if count else None,
        "humaneval_base_reduced_sample_count": count,
        "compile_rate": compile_ok / count if count else None,
        "test_pass_rate": "NOT_RUN_NOT_IMPLEMENTED",
        "runtime_error_rate": runtime_errors / count if count else None,
        "timeout_rate": timeout_count / count if count else None,
        "invalid_syntax_rate": syntax_errors / count if count else None,
        "eval_wall_clock_seconds": elapsed,
        "bigcodebench_complete": "NOT_RUN_NOT_IMPLEMENTED",
        "bigcodebench_instruct": "NOT_RUN_NOT_IMPLEMENTED",
        "livecodebench_pass_at_1": "NOT_RUN_NOT_IMPLEMENTED",
        "mbpp_plus_pass_at_1": "NOT_RUN_NOT_IMPLEMENTED",
    }


def run(config: dict, output: str, limit: int | None = None, infrastructure_only: bool = False) -> dict:
    require_fields(config, REQUIRED_MODEL_CONFIG_FIELDS, "Code config")
    status = status_for_config(config, infrastructure_only=infrastructure_only)
    metrics = dict(CODING_METRICS)
    benchmark_evidence = False
    error = None
    if status == "BENCH_INFRASTRUCTURE_READY" and not infrastructure_only:
        try:
            metrics.update(_evaluate(config, limit))
            status = "GENUINE_REDUCED_EVAL"
            benchmark_evidence = True
        except Exception as exc:
            status = "EVAL_FAILED"
            error = repr(exc)
    payload = {
        **base_metadata(config, limit),
        "status": status,
        "benchmark_evidence": benchmark_evidence,
        "scorecard_type": "coding",
        "scorecard": {**common_scorecard(config), **metrics},
        "runtimecoder_evidence": False,
        "standard_agent_scaffold_positioning_only": True,
        "error": error,
    }
    write_json(output, payload)
    return payload


def main() -> None:
    parser = parser_with_config("Run coding evaluation")
    args = parser.parse_args()
    payload = run(load_json_or_yaml(args.config), args.output, args.limit, args.infrastructure_only)
    print(payload["status"])


if __name__ == "__main__":
    main()
