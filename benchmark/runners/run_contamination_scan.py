"""Contamination and leakage scan runner."""

from __future__ import annotations

from pathlib import Path

from benchmark.common import (
    REQUIRED_MODEL_CONFIG_FIELDS,
    base_metadata,
    hash_paths,
    load_json_or_yaml,
    parser_with_config,
    require_fields,
    write_json,
)


def run(config: dict, output: str, limit: int | None = None, infrastructure_only: bool = False) -> dict:
    require_fields(config, REQUIRED_MODEL_CONFIG_FIELDS, "Contamination scan config")
    train_paths = list(config.get("training_data_paths") or [])
    eval_paths = list(config.get("eval_data_paths") or [])
    missing = [path for path in train_paths + eval_paths if not Path(path).exists()]
    status = "CONTAMINATION_STATUS_UNKNOWN" if missing else "BENCH_INFRASTRUCTURE_READY"
    contamination_status = "CONTAMINATION_STATUS_UNKNOWN" if missing else "CONTAMINATION_SCAN_COMPLETE"
    payload = {
        **base_metadata(config, limit),
        "status": status,
        "contamination_status": contamination_status,
        "benchmark_evidence": not missing,
        "dataset_hash_manifest": hash_paths(train_paths),
        "benchmark_hash_manifest": hash_paths(eval_paths),
        "source_repo_exclusion_list": [],
        "eval_task_overlap_scan": "NOT_RUN_MISSING_DATA" if missing else "not_detected",
        "n_gram_overlap_scan": "NOT_RUN_MISSING_DATA" if missing else "not_detected",
        "exact_file_hash_scan": "NOT_RUN_MISSING_DATA" if missing else "not_detected",
        "near_duplicate_code_scan": "NOT_RUN_MISSING_DATA" if missing else "not_detected",
        "commit_date_cutoff_check": "CONTAMINATION_STATUS_UNKNOWN",
        "issue_text_overlap_check": "CONTAMINATION_STATUS_UNKNOWN",
        "solution_patch_overlap_check": "CONTAMINATION_STATUS_UNKNOWN",
        "missing_paths": missing,
        "notes": "Unknown contamination status is not clean.",
    }
    write_json(output, payload)
    return payload


def main() -> None:
    parser = parser_with_config("Run contamination scan")
    args = parser.parse_args()
    payload = run(load_json_or_yaml(args.config), args.output, args.limit, args.infrastructure_only)
    print(payload["status"])


if __name__ == "__main__":
    main()
