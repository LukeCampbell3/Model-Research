"""Prepare the real data layer for the 100M benchmark tier.

The default sources are small public-domain/open public files. They are not
toy examples and are suitable for unblocking the harness as a genuine reduced
data layer, but they are intentionally reported as reduced data rather than a
full pretraining corpus.
"""

from __future__ import annotations

import argparse
import gzip
import json
import shutil
from pathlib import Path
from urllib.request import Request, urlopen

from benchmark.common import sha256_file, utc_now, write_json


DATA_ROOT = Path("data")
MANIFEST_ROOT = DATA_ROOT / "manifests"
BENCHMARK_MANIFEST_ROOT = Path("benchmark/manifests")

TRAIN_SOURCES = [
    {
        "name": "gutenberg_alice_wonderland",
        "url": "https://www.gutenberg.org/cache/epub/11/pg11.txt",
        "license_or_usage_note": "Project Gutenberg public domain text; obey Gutenberg terms for redistribution.",
    },
    {
        "name": "gutenberg_sherlock_holmes",
        "url": "https://www.gutenberg.org/cache/epub/1661/pg1661.txt",
        "license_or_usage_note": "Project Gutenberg public domain text; obey Gutenberg terms for redistribution.",
    },
    {
        "name": "gutenberg_pride_and_prejudice",
        "url": "https://www.gutenberg.org/cache/epub/1342/pg1342.txt",
        "license_or_usage_note": "Project Gutenberg public domain text; obey Gutenberg terms for redistribution.",
    },
]

EVAL_SOURCES = [
    {
        "split": "broad_nlp_heldout",
        "directory": "broad_nlp",
        "name": "gutenberg_frankenstein_heldout",
        "url": "https://www.gutenberg.org/cache/epub/84/pg84.txt",
        "license_or_usage_note": "Project Gutenberg public domain text; obey Gutenberg terms for redistribution.",
    },
    {
        "split": "code_heavy_heldout",
        "directory": "broad_nlp",
        "name": "cpython_json_decoder",
        "url": "https://raw.githubusercontent.com/python/cpython/main/Lib/json/decoder.py",
        "license_or_usage_note": "CPython source under PSF license.",
    },
    {
        "split": "math_heavy_heldout",
        "directory": "broad_nlp",
        "name": "the_algorithms_prime_numbers",
        "url": "https://raw.githubusercontent.com/TheAlgorithms/Python/master/maths/prime_numbers.py",
        "license_or_usage_note": "TheAlgorithms/Python public repository; inspect upstream MIT license before redistribution.",
    },
    {
        "split": "json_schema_heldout",
        "directory": "broad_nlp",
        "name": "json_schema_test_suite_type",
        "url": "https://raw.githubusercontent.com/json-schema-org/JSON-Schema-Test-Suite/main/tests/draft7/type.json",
        "license_or_usage_note": "JSON Schema Test Suite under upstream public repository license.",
    },
    {
        "split": "coding_function_eval",
        "directory": "coding",
        "name": "humaneval_base",
        "url": "https://raw.githubusercontent.com/openai/human-eval/master/data/HumanEval.jsonl.gz",
        "license_or_usage_note": "OpenAI HumanEval public repository; used as reduced coding function eval, not HumanEval+.",
        "gzip": True,
    },
]

ROUTING_PROBES = [
    {
        "id": "same_question_different_descriptor",
        "descriptor": "math",
        "operator": "solve",
        "prompt": "Descriptor: math\nOperator: solve\nQuestion: If x + 7 = 12, what is x?",
        "expected_route_hint": "math_solve",
    },
    {
        "id": "same_input_wrong_descriptor",
        "descriptor": "json_schema",
        "operator": "validate",
        "prompt": "Descriptor: json_schema\nOperator: validate\nInput: {\"name\": \"Ada\", \"age\": 37}",
        "expected_route_hint": "json_validate",
    },
    {
        "id": "negation_flip",
        "descriptor": "logic",
        "operator": "negation",
        "prompt": "Descriptor: logic\nOperator: negation\nStatement: All tests passed. Negate the statement.",
        "expected_route_hint": "logic_negation",
    },
    {
        "id": "delimiter_scope",
        "descriptor": "instruction",
        "operator": "scope",
        "prompt": "Use only text inside <answer> tags. <ignore>red</ignore><answer>blue</answer>",
        "expected_route_hint": "instruction_scope",
    },
]


def _download(url: str, *, timeout: int = 60) -> bytes:
    request = Request(url, headers={"User-Agent": "pvr-ec-o-benchmark-data-prep/1.0"})
    with urlopen(request, timeout=timeout) as response:
        return response.read()


def _write_source(source: dict, target: Path) -> dict:
    raw = _download(source["url"])
    if source.get("gzip"):
        raw = gzip.decompress(raw)
    text = raw.decode("utf-8", errors="replace")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")
    return _split_manifest(source, target, text)


def _token_count(text: str) -> int:
    return len(text.split())


def _document_count(text: str) -> int:
    chunks = [chunk for chunk in text.split("\n\n") if chunk.strip()]
    return max(1, len(chunks))


def _split_manifest(source: dict, path: Path, text: str) -> dict:
    return {
        "dataset_name": source["name"],
        "split": source.get("split", "broad_nlp_train"),
        "source": source["url"],
        "license_or_usage_note": source["license_or_usage_note"],
        "created_at": utc_now(),
        "path": str(path),
        "document_count": _document_count(text),
        "token_count_estimate": _token_count(text),
        "hash": sha256_file(path),
        "split_method": "fixed public reduced benchmark split by source file",
        "contamination_notes": "Source is public and hashed; overlap scan must be run before claiming clean contamination.",
    }


def _write_routing_probes() -> list[dict]:
    target = DATA_ROOT / "eval" / "routing_probes" / "routing_sensitive_eval.jsonl"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("\n".join(json.dumps(row, sort_keys=True) for row in ROUTING_PROBES) + "\n", encoding="utf-8")
    return [{
        "dataset_name": "routing_sensitive_eval",
        "split": "routing_sensitive_eval",
        "source": "repo-authored structured routing probes",
        "license_or_usage_note": "Synthetic probes are allowed for routing-control diagnostics only, not broad NLP/coding substitution.",
        "created_at": utc_now(),
        "path": str(target),
        "document_count": len(ROUTING_PROBES),
        "token_count_estimate": _token_count(target.read_text(encoding="utf-8")),
        "hash": sha256_file(target),
        "split_method": "fixed deterministic routing-control probe set",
        "contamination_notes": "Synthetic routing probes are excluded from broad capability evidence.",
    }]


def _write_manifests(train_rows: list[dict], eval_rows: list[dict]) -> dict:
    MANIFEST_ROOT.mkdir(parents=True, exist_ok=True)
    BENCHMARK_MANIFEST_ROOT.mkdir(parents=True, exist_ok=True)
    training = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "status": "REAL_REDUCED_DATA_READY",
        "subset_label": "GENUINE_REDUCED_TRAINING_DATA",
        "splits": train_rows,
        "total_document_count": sum(row["document_count"] for row in train_rows),
        "total_token_count_estimate": sum(row["token_count_estimate"] for row in train_rows),
    }
    eval_manifest = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "status": "REAL_REDUCED_EVAL_READY",
        "subset_label": "GENUINE_REDUCED_EVAL",
        "splits": eval_rows,
        "total_document_count": sum(row["document_count"] for row in eval_rows),
        "total_token_count_estimate": sum(row["token_count_estimate"] for row in eval_rows),
    }
    contamination = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "status": "CONTAMINATION_SCAN_REQUIRED",
        "contamination_status": "CONTAMINATION_STATUS_UNKNOWN",
        "training_hashes": {row["path"]: row["hash"] for row in train_rows},
        "eval_hashes": {row["path"]: row["hash"] for row in eval_rows},
        "notes": "Run benchmark.scripts.run_data_contamination_scan before claiming clean contamination.",
    }
    outputs = {
        "training_data_manifest": training,
        "eval_manifest": eval_manifest,
        "contamination_scan_manifest": contamination,
    }
    for name, payload in [
        ("training_data_manifest.json", training),
        ("eval_manifest.json", eval_manifest),
        ("contamination_scan_manifest.json", contamination),
    ]:
        write_json(MANIFEST_ROOT / name, payload)
        write_json(BENCHMARK_MANIFEST_ROOT / name, payload)
    return outputs


def run() -> dict:
    for path in [
        DATA_ROOT / "broad_nlp_train",
        DATA_ROOT / "eval" / "broad_nlp",
        DATA_ROOT / "eval" / "coding",
        DATA_ROOT / "eval" / "routing_probes",
        MANIFEST_ROOT,
    ]:
        path.mkdir(parents=True, exist_ok=True)

    train_rows = []
    for source in TRAIN_SOURCES:
        train_rows.append(_write_source(source, DATA_ROOT / "broad_nlp_train" / f"{source['name']}.txt"))

    eval_rows = []
    for source in EVAL_SOURCES:
        suffix = ".jsonl" if source["name"] == "humaneval_base" else ".txt"
        eval_rows.append(_write_source(source, DATA_ROOT / "eval" / source["directory"] / f"{source['name']}{suffix}"))
    eval_rows.extend(_write_routing_probes())
    manifests = _write_manifests(train_rows, eval_rows)
    result = {
        "status": "REAL_REDUCED_DATA_READY",
        "created_at": utc_now(),
        "data_root": str(DATA_ROOT),
        "training_split_count": len(train_rows),
        "eval_split_count": len(eval_rows),
        "training_token_count_estimate": manifests["training_data_manifest"]["total_token_count_estimate"],
        "eval_token_count_estimate": manifests["eval_manifest"]["total_token_count_estimate"],
        "manifests": {
            "training": str(MANIFEST_ROOT / "training_data_manifest.json"),
            "eval": str(MANIFEST_ROOT / "eval_manifest.json"),
            "contamination": str(MANIFEST_ROOT / "contamination_scan_manifest.json"),
        },
    }
    write_json(DATA_ROOT / "manifests" / "prepare_real_data_report.json", result)
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description="Prepare real reduced public data for PVR-EC-O benchmarks")
    parser.parse_args()
    payload = run()
    print(payload["status"])


if __name__ == "__main__":
    main()
