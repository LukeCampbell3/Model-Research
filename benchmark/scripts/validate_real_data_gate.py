"""Validate that the benchmark data layer is non-empty and manifest-backed."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from benchmark.common import write_json


REQUIRED_DIRS = [
    Path("data/broad_nlp_train"),
    Path("data/eval/broad_nlp"),
    Path("data/eval/coding"),
    Path("data/eval/routing_probes"),
]

REQUIRED_MANIFESTS = [
    Path("data/manifests/training_data_manifest.json"),
    Path("data/manifests/eval_manifest.json"),
    Path("data/manifests/contamination_scan_manifest.json"),
    Path("benchmark/manifests/training_data_manifest.json"),
    Path("benchmark/manifests/eval_manifest.json"),
    Path("benchmark/manifests/contamination_scan_manifest.json"),
]


def _token_count(path: Path) -> int:
    return len(path.read_text(encoding="utf-8", errors="replace").split())


def _files(path: Path) -> list[Path]:
    return sorted(child for child in path.rglob("*") if child.is_file()) if path.exists() else []


def run(min_train_tokens: int = 1000, min_eval_tokens: int = 200) -> dict:
    missing_dirs = [str(path) for path in REQUIRED_DIRS if not path.exists()]
    empty_dirs = [str(path) for path in REQUIRED_DIRS if path.exists() and not _files(path)]
    missing_manifests = [str(path) for path in REQUIRED_MANIFESTS if not path.exists()]
    train_tokens = sum(_token_count(path) for path in _files(Path("data/broad_nlp_train")))
    eval_tokens = sum(_token_count(path) for path in _files(Path("data/eval")))
    manifest_errors = []
    for path in REQUIRED_MANIFESTS:
        if path.exists():
            try:
                json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                manifest_errors.append(f"{path}: {exc}")
    errors = []
    errors.extend(f"missing_dir:{path}" for path in missing_dirs)
    errors.extend(f"empty_dir:{path}" for path in empty_dirs)
    errors.extend(f"missing_manifest:{path}" for path in missing_manifests)
    errors.extend(f"invalid_manifest:{item}" for item in manifest_errors)
    if train_tokens < min_train_tokens:
        errors.append(f"train_tokens_below_min:{train_tokens}<{min_train_tokens}")
    if eval_tokens < min_eval_tokens:
        errors.append(f"eval_tokens_below_min:{eval_tokens}<{min_eval_tokens}")
    status = "REAL_DATA_GATE_READY" if not errors else "NOT_RUN_MISSING_DATA"
    payload = {
        "schema_version": "1.0",
        "status": status,
        "required_dirs": [str(path) for path in REQUIRED_DIRS],
        "required_manifests": [str(path) for path in REQUIRED_MANIFESTS],
        "train_token_count_estimate": train_tokens,
        "eval_token_count_estimate": eval_tokens,
        "min_train_tokens": min_train_tokens,
        "min_eval_tokens": min_eval_tokens,
        "errors": errors,
    }
    write_json("data/manifests/real_data_gate_report.json", payload)
    if errors:
        raise SystemExit(json.dumps(payload, indent=2, sort_keys=True))
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate real benchmark data gate")
    parser.add_argument("--min-train-tokens", type=int, default=1000)
    parser.add_argument("--min-eval-tokens", type=int, default=200)
    args = parser.parse_args()
    payload = run(args.min_train_tokens, args.min_eval_tokens)
    print(payload["status"])


if __name__ == "__main__":
    main()
