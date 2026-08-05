"""Language-modeling evaluation runner for genuine PVR-EC-O benchmarks."""

from __future__ import annotations

import math
import time
from pathlib import Path

import torch
import torch.nn.functional as F

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


NLP_METRICS = {
    "lm_loss": None,
    "perplexity": None,
    "bits_per_byte": None,
    "long_context_loss_by_position": None,
    "copy_span_loss": None,
    "rare_token_loss": None,
    "code_token_loss": None,
    "math_token_loss": None,
    "json_token_loss": None,
    "loss_by_descriptor_family": None,
    "loss_by_operator_family": None,
    "mmlu_pro": None,
    "gpqa": None,
    "bbh": None,
    "musr": None,
    "math_lvl_5": None,
    "ifeval": None,
    "truthfulqa": None,
    "calibration_ece": None,
    "brier_score": None,
    "prompt_sensitivity": None,
}


def _files(paths: list[str]) -> list[Path]:
    out: list[Path] = []
    for item in paths:
        path = Path(item)
        if path.is_file():
            out.append(path)
        elif path.is_dir():
            out.extend(sorted(child for child in path.rglob("*") if child.is_file()))
    return out


def _text_for(paths: list[Path], hints: list[str]) -> str:
    selected = [path for path in paths if any(hint in path.name.lower() for hint in hints)]
    if not selected:
        selected = paths
    chunks = []
    for path in selected:
        chunks.append(path.read_text(encoding="utf-8", errors="replace"))
    return "\n".join(chunks)


def _loss_on_text(model, text: str, device: str, seq_len: int, max_batches: int) -> tuple[float | None, int, float]:
    data = list(text.encode("utf-8", errors="replace"))
    if len(data) < seq_len + 1:
        return None, 0, 0.0
    tokens = torch.tensor(data, dtype=torch.long)
    losses = []
    token_count = 0
    start = time.time()
    with torch.no_grad():
        for batch_idx in range(max_batches):
            offset = batch_idx * seq_len
            if offset + seq_len + 1 > len(tokens):
                break
            block = tokens[offset : offset + seq_len + 1].unsqueeze(0).to(device)
            logits = model(block[:, :-1])
            loss = F.cross_entropy(logits.reshape(-1, logits.shape[-1]), block[:, 1:].reshape(-1))
            losses.append(float(loss.detach().cpu().item()))
            token_count += seq_len
    elapsed = max(0.0, time.time() - start)
    if not losses:
        return None, token_count, elapsed
    return sum(losses) / len(losses), token_count, elapsed


def _load_model(config: dict, device: str):
    materialized = build_model(config, device=device)
    checkpoint = torch.load(config["checkpoint_path"], map_location=device)
    state = checkpoint.get("model_state_dict", checkpoint)
    materialized.model.load_state_dict(state, strict=False)
    materialized.model.eval()
    return materialized


def _evaluate(config: dict, limit: int | None) -> dict:
    device = "cuda" if torch.cuda.is_available() else "cpu"
    materialized = _load_model(config, device)
    files = _files(list(config.get("eval_data_paths") or []))
    seq_len = min(64, max(4, int(config.get("context_length", 128)) - 1))
    max_batches = limit or 8
    if device == "cuda":
        torch.cuda.reset_peak_memory_stats()
    general_loss, tokens, elapsed = _loss_on_text(materialized.model, _text_for(files, ["heldout", "gutenberg", "frankenstein"]), device, seq_len, max_batches)
    code_loss, code_tokens, code_elapsed = _loss_on_text(materialized.model, _text_for(files, ["code", "decoder", "humaneval"]), device, seq_len, max_batches)
    math_loss, math_tokens, math_elapsed = _loss_on_text(materialized.model, _text_for(files, ["math", "euler"]), device, seq_len, max_batches)
    json_loss, json_tokens, json_elapsed = _loss_on_text(materialized.model, _text_for(files, ["json", "schema"]), device, seq_len, max_batches)
    total_tokens = tokens + code_tokens + math_tokens + json_tokens
    total_elapsed = elapsed + code_elapsed + math_elapsed + json_elapsed
    latency_ms = (total_elapsed * 1000.0 / total_tokens) if total_tokens else None
    vram_peak = torch.cuda.max_memory_allocated() if device == "cuda" and torch.cuda.is_available() else None
    return {
        "lm_loss": general_loss,
        "perplexity": math.exp(general_loss) if general_loss is not None and general_loss < 700 else None,
        "code_token_loss": code_loss,
        "math_token_loss": math_loss,
        "json_token_loss": json_loss,
        "long_context_loss_by_position": "NOT_RUN_NOT_IMPLEMENTED",
        "rare_token_loss": "NOT_RUN_NOT_IMPLEMENTED",
        "tokens_evaluated": total_tokens,
        "eval_token_count": total_tokens,
        "heldout_eval_token_count": tokens,
        "code_eval_token_count": code_tokens,
        "math_eval_token_count": math_tokens,
        "json_schema_eval_token_count": json_tokens,
        "eval_latency_ms_per_token": latency_ms,
        "vram_peak": vram_peak,
        "throughput": (total_tokens / total_elapsed) if total_elapsed > 0 else None,
        "official_broad_nlp": {
            "mmlu_pro": "NOT_RUN_NOT_IMPLEMENTED",
            "gpqa": "NOT_RUN_NOT_IMPLEMENTED",
            "bbh": "NOT_RUN_NOT_IMPLEMENTED",
            "musr": "NOT_RUN_NOT_IMPLEMENTED",
            "math_lvl_5": "NOT_RUN_NOT_IMPLEMENTED",
            "ifeval": "NOT_RUN_NOT_IMPLEMENTED",
            "arc_challenge": "NOT_RUN_NOT_IMPLEMENTED",
            "hellaswag": "NOT_RUN_NOT_IMPLEMENTED",
            "truthfulqa": "NOT_RUN_NOT_IMPLEMENTED",
            "winogrande": "NOT_RUN_NOT_IMPLEMENTED",
            "boolq": "NOT_RUN_NOT_IMPLEMENTED",
            "gsm8k": "NOT_RUN_NOT_IMPLEMENTED",
        },
    }


def run(config: dict, output: str, limit: int | None = None, infrastructure_only: bool = False) -> dict:
    require_fields(config, REQUIRED_MODEL_CONFIG_FIELDS, "LM config")
    status = status_for_config(config, infrastructure_only=infrastructure_only)
    metrics = dict(NLP_METRICS)
    benchmark_evidence = False
    error = None
    if status == "BENCH_INFRASTRUCTURE_READY" and not infrastructure_only:
        try:
            metrics.update(_evaluate(config, limit))
            status = "GENUINE_REDUCED_EVAL"
            benchmark_evidence = metrics.get("lm_loss") is not None
        except Exception as exc:
            status = "EVAL_FAILED"
            error = repr(exc)
    payload = {
        **base_metadata(config, limit),
        "status": status,
        "benchmark_evidence": benchmark_evidence,
        "scorecard_type": "nlp",
        "scorecard": {**common_scorecard(config), **metrics},
        "error": error,
    }
    write_json(output, payload)
    return payload


def main() -> None:
    parser = parser_with_config("Run LM evaluation")
    args = parser.parse_args()
    payload = run(load_json_or_yaml(args.config), args.output, args.limit, args.infrastructure_only)
    print(payload["status"])


if __name__ == "__main__":
    main()
