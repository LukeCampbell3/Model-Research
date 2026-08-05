"""Download deterministic bounded slices from official benchmark datasets.

The Hugging Face datasets server is used as a transport for upstream datasets.
Every selected row, source endpoint, and generated file is hashed so the
bounded suite can be reproduced and audited without installing datasets/Arrow.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

from benchmark.common import git_commit, sha256_file, utc_now, write_json


DATASETS: dict[str, dict[str, Any]] = {
    "arc_challenge": {"dataset": "allenai/ai2_arc", "config": "ARC-Challenge", "split": "test", "limit": 64},
    "mmlu": {"dataset": "cais/mmlu", "config": "all", "split": "test", "limit": 64},
    "hellaswag": {"dataset": "Rowan/hellaswag", "config": "default", "split": "validation", "limit": 64},
    "boolq": {"dataset": "google/boolq", "config": "default", "split": "validation", "limit": 64},
    "winogrande": {"dataset": "allenai/winogrande", "config": "winogrande_xl", "split": "validation", "limit": 64},
    "gsm8k": {"dataset": "openai/gsm8k", "config": "main", "split": "test", "limit": 16},
    "humaneval": {"dataset": "openai/openai_humaneval", "config": "openai_humaneval", "split": "test", "limit": 8},
    "mbpp": {"dataset": "google-research-datasets/mbpp", "config": "full", "split": "test", "limit": 8},
}

SERVER = "https://datasets-server.huggingface.co"


def _url(path: str, spec: dict[str, Any], **extra: Any) -> str:
    query = {
        "dataset": spec["dataset"],
        "config": spec["config"],
        "split": spec["split"],
        **extra,
    }
    return f"{SERVER}/{path}?{urllib.parse.urlencode(query)}"


def _json_get(url: str) -> tuple[dict[str, Any], dict[str, str]]:
    request = urllib.request.Request(url, headers={"User-Agent": "pvr-ec-o-benchmark/1.0"})
    for attempt in range(8):
        try:
            with urllib.request.urlopen(request, timeout=90) as response:
                payload = json.loads(response.read().decode("utf-8"))
                headers = {key.lower(): value for key, value in response.headers.items()}
            time.sleep(0.20)
            return payload, headers
        except urllib.error.HTTPError as exc:
            if exc.code not in {429, 500, 502, 503, 504} or attempt == 7:
                raise
            retry_after = float(exc.headers.get("Retry-After", 0) or 0)
            time.sleep(max(retry_after, min(30.0, 1.5 * (2**attempt))))
    raise RuntimeError(f"Dataset request retries exhausted: {url}")


def _split_size(spec: dict[str, Any]) -> tuple[int, str, dict[str, str]]:
    url = _url("size", spec)
    payload, headers = _json_get(url)
    rows = payload.get("size", {}).get("splits", [])
    match = next((row for row in rows if row.get("split") == spec["split"]), None)
    if not match or not match.get("num_rows"):
        raise RuntimeError(f"Dataset server did not report a split size for {spec}")
    return int(match["num_rows"]), url, headers


def _select_indices(name: str, count: int, limit: int, seed: int) -> list[int]:
    rng = random.Random(f"{seed}:{name}:{count}")
    limit = min(limit, count)
    page_count = max(1, (count + 99) // 100)
    selected_page_count = min(page_count, max(1, math.ceil(limit / 8)))
    pages = sorted(rng.sample(range(page_count), selected_page_count))
    indices: list[int] = []
    remaining = limit
    for page_index, page in enumerate(pages):
        available = list(range(page * 100, min(count, page * 100 + 100)))
        pages_left = len(pages) - page_index
        take = min(len(available), math.ceil(remaining / pages_left))
        indices.extend(rng.sample(available, take))
        remaining -= take
    return sorted(indices)


def _fetch_selected(spec: dict[str, Any], indices: list[int]) -> tuple[list[dict[str, Any]], list[str], list[dict[str, str]]]:
    selected: dict[int, dict[str, Any]] = {}
    urls: list[str] = []
    headers: list[dict[str, str]] = []
    pages = sorted({index // 100 for index in indices})
    for page in pages:
        offset = page * 100
        url = _url("rows", spec, offset=offset, length=100)
        payload, response_headers = _json_get(url)
        urls.append(url)
        headers.append({key: response_headers[key] for key in ("etag", "last-modified", "x-revision") if key in response_headers})
        for item in payload.get("rows", []):
            row_index = int(item["row_idx"])
            if row_index in indices:
                selected[row_index] = item["row"]
    missing = sorted(set(indices) - set(selected))
    if missing:
        raise RuntimeError(f"Missing selected rows for {spec['dataset']}: {missing[:10]}")
    return [{"source_row_index": index, **selected[index]} for index in indices], urls, headers


def _row_hash(row: dict[str, Any]) -> str:
    raw = json.dumps(row, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def _write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(row, sort_keys=True, ensure_ascii=False) + "\n")


def _contamination_scan(rows_by_task: dict[str, list[dict[str, Any]]], train_paths: list[str]) -> dict[str, Any]:
    training = bytearray()
    source_files: list[str] = []
    for item in train_paths:
        path = Path(item)
        files = [path] if path.is_file() else sorted(p for p in path.rglob("*") if p.is_file()) if path.is_dir() else []
        for file_path in files:
            training.extend(file_path.read_bytes())
            training.extend(b"\n")
            source_files.append(str(file_path))
    corpus = bytes(training).lower()
    matches: list[dict[str, Any]] = []
    scanned = 0
    for task, rows in rows_by_task.items():
        for row in rows:
            text = json.dumps(row, sort_keys=True, ensure_ascii=False)
            normalized = " ".join(text.split()).encode("utf-8", errors="replace").lower()
            fingerprints = [normalized[pos : pos + 96] for pos in range(0, max(1, len(normalized) - 95), 96)]
            fingerprints = [value for value in fingerprints if len(value) >= 48]
            scanned += len(fingerprints)
            for value in fingerprints:
                if value in corpus:
                    matches.append({
                        "task": task,
                        "source_row_index": row["source_row_index"],
                        "fingerprint_sha256": hashlib.sha256(value).hexdigest(),
                    })
    return {
        "status": "CONTAMINATION_SCAN_CLEAR" if not matches else "CONTAMINATION_POSSIBLE_EXACT_FINGERPRINT_MATCH",
        "method": "Exact lowercased 96-byte fingerprints sampled from normalized official rows.",
        "training_source_files": source_files,
        "fingerprints_scanned": scanned,
        "match_count": len(matches),
        "matches": matches,
    }


def prepare(output: str, *, seed: int = 20260620, train_paths: list[str] | None = None) -> dict[str, Any]:
    root = Path(output)
    root.mkdir(parents=True, exist_ok=True)
    rows_by_task: dict[str, list[dict[str, Any]]] = {}
    task_manifest: dict[str, Any] = {}
    for name, spec in DATASETS.items():
        count, size_url, size_headers = _split_size(spec)
        indices = _select_indices(name, count, int(spec["limit"]), seed)
        rows, row_urls, row_headers = _fetch_selected(spec, indices)
        rows_by_task[name] = rows
        path = root / f"{name}.jsonl"
        _write_jsonl(path, rows)
        task_manifest[name] = {
            **spec,
            "transport": "Hugging Face datasets server",
            "source_split_row_count": count,
            "selected_row_count": len(rows),
            "selection_seed": seed,
            "selected_indices": indices,
            "size_endpoint": size_url,
            "row_endpoints": row_urls,
            "response_headers": {"size": size_headers, "rows": row_headers},
            "row_hashes": [_row_hash(row) for row in rows],
            "output_path": str(path),
            "output_sha256": sha256_file(path),
        }
    contamination = _contamination_scan(rows_by_task, train_paths or ["data/broad_nlp_train"])
    manifest = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "git_commit": git_commit(),
        "suite": "PVR_300M_OFFICIAL_DATASET_BOUNDED_SUITE",
        "scope": "deterministic bounded slices of official dataset splits; not full official leaderboard evaluation",
        "selection_seed": seed,
        "tasks": task_manifest,
        "contamination_scan": contamination,
    }
    write_json(root / "official_300m_data_manifest.json", manifest)
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="data/eval/official_300m_bounded")
    parser.add_argument("--seed", type=int, default=20260620)
    parser.add_argument("--train-paths", nargs="*", default=["data/broad_nlp_train"])
    args = parser.parse_args()
    payload = prepare(args.output, seed=args.seed, train_paths=args.train_paths)
    print(json.dumps({"suite": payload["suite"], "tasks": {k: v["selected_row_count"] for k, v in payload["tasks"].items()}}, indent=2))


if __name__ == "__main__":
    main()
