"""Run a deterministic overlap scan between train and eval data files."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from benchmark.common import sha256_file, utc_now, write_json


TRAIN_DIR = Path("data/broad_nlp_train")
EVAL_DIRS = [Path("data/eval/broad_nlp"), Path("data/eval/coding"), Path("data/eval/routing_probes")]
DATA_MANIFEST_DIR = Path("data/manifests")
BENCHMARK_MANIFEST_DIR = Path("benchmark/manifests")


def _files(paths: list[Path]) -> list[Path]:
    out: list[Path] = []
    for path in paths:
        if path.exists():
            out.extend(sorted(child for child in path.rglob("*") if child.is_file()))
    return out


def _ngrams(text: str, n: int = 13) -> set[tuple[str, ...]]:
    words = text.lower().split()
    if len(words) < n:
        return set()
    return {tuple(words[i : i + n]) for i in range(0, len(words) - n + 1)}


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def run() -> dict:
    train_files = _files([TRAIN_DIR])
    eval_files = _files(EVAL_DIRS)
    missing = []
    if not train_files:
        missing.append(str(TRAIN_DIR))
    for path in EVAL_DIRS:
        if not _files([path]):
            missing.append(str(path))

    exact_hash_overlaps = []
    train_hashes = {str(path): sha256_file(path) for path in train_files}
    eval_hashes = {str(path): sha256_file(path) for path in eval_files}
    for train_path, train_hash in train_hashes.items():
        for eval_path, eval_hash in eval_hashes.items():
            if train_hash == eval_hash:
                exact_hash_overlaps.append({"train_file": train_path, "eval_file": eval_path, "hash": train_hash})

    train_ngrams = {}
    for path in train_files:
        train_ngrams[str(path)] = _ngrams(_read(path))
    ngram_overlaps = []
    for eval_path in eval_files:
        eval_set = _ngrams(_read(eval_path))
        for train_path, train_set in train_ngrams.items():
            overlap_count = len(eval_set & train_set)
            if overlap_count:
                ngram_overlaps.append({"train_file": train_path, "eval_file": str(eval_path), "overlap_13gram_count": overlap_count})

    clean = not missing and not exact_hash_overlaps and not ngram_overlaps
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "status": "CONTAMINATION_SCAN_COMPLETE" if not missing else "NOT_RUN_MISSING_DATA",
        "contamination_status": "CONTAMINATION_NOT_DETECTED" if clean else "CONTAMINATION_STATUS_UNKNOWN" if missing else "CONTAMINATION_OVERLAP_DETECTED",
        "train_file_count": len(train_files),
        "eval_file_count": len(eval_files),
        "missing_paths": missing,
        "training_hashes": train_hashes,
        "eval_hashes": eval_hashes,
        "exact_hash_overlaps": exact_hash_overlaps,
        "ngram_overlap_scan": ngram_overlaps,
        "notes": "This is a deterministic file hash and 13-gram overlap scan, not a guarantee against all pretraining contamination.",
    }
    DATA_MANIFEST_DIR.mkdir(parents=True, exist_ok=True)
    BENCHMARK_MANIFEST_DIR.mkdir(parents=True, exist_ok=True)
    write_json(DATA_MANIFEST_DIR / "contamination_scan_manifest.json", payload)
    write_json(BENCHMARK_MANIFEST_DIR / "contamination_scan_manifest.json", payload)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description="Run data contamination scan")
    parser.parse_args()
    payload = run()
    print(payload["status"])


if __name__ == "__main__":
    main()
