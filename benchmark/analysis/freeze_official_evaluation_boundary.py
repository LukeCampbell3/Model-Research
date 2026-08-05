"""Freeze the current official evaluation boundary.

This creates a manifest for the final eight bounded official files and records
which existing local pools are allowed to guide development. It does not create
a new official-like development corpus; it marks that as a required follow-up so
future repair work does not silently tune on the final files.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from benchmark.common import utc_now, write_json


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _line_hashes(path: Path) -> set[str]:
    hashes = set()
    try:
        lines = path.read_bytes().splitlines()
    except OSError:
        return hashes
    for line in lines:
        normalized = line.strip()
        if normalized:
            hashes.add(hashlib.sha256(normalized).hexdigest())
    return hashes


def _manifest_files(root: Path) -> list[dict[str, Any]]:
    if not root.exists():
        return []
    rows = []
    for path in sorted(p for p in root.rglob("*") if p.is_file()):
        rows.append(
            {
                "path": str(path.as_posix()),
                "bytes": path.stat().st_size,
                "sha256": _sha256(path),
                "line_count": len(path.read_bytes().splitlines()),
            }
        )
    return rows


def _overlap(final_files: list[Path], candidate_roots: list[Path]) -> dict[str, Any]:
    final_line_hashes = set()
    for path in final_files:
        final_line_hashes.update(_line_hashes(path))
    rows = []
    total_overlap = 0
    for root in candidate_roots:
        root_hashes = set()
        if root.exists():
            for path in root.rglob("*"):
                if path.is_file():
                    root_hashes.update(_line_hashes(path))
        overlap = len(final_line_hashes & root_hashes)
        total_overlap += overlap
        rows.append({"root": str(root.as_posix()), "line_hash_overlap_with_final": overlap})
    return {"total_line_hash_overlap": total_overlap, "rows": rows}


def run(
    *,
    official_root: str = "data/eval/official_300m_bounded",
    local_roots: list[str] | None = None,
    official_like_root: str = "data/eval/official_like_dev",
    output: str = "benchmark/reports/generated/official_evaluation_boundary_frozen",
) -> dict[str, Any]:
    local_roots = local_roots or ["data/eval/broad_nlp", "data/eval/coding", "data/eval/routing_probes"]
    official = Path(official_root)
    final_files = sorted(official.glob("*.jsonl"))
    official_like = Path(official_like_root)
    official_like_manifest = official_like / "official_like_dev_manifest.json"
    official_like_ready = official_like_manifest.exists()
    local_paths = [Path(root) for root in [*local_roots, official_like_root]]
    overlap = _overlap(final_files, local_paths)
    final_file_count = len(final_files)
    expected_file_count = 8
    status = "OFFICIAL_EVALUATION_BOUNDARY_FROZEN" if final_file_count == expected_file_count else "OFFICIAL_EVALUATION_BOUNDARY_INCOMPLETE"
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "experiment": "OFFICIAL_EVALUATION_BOUNDARY_FREEZE",
        "status": status,
        "tiers": {
            "local_heldout": {
                "may_guide_training": True,
                "roots": local_roots,
                "purpose": "Fast regression and screening only.",
            },
            "official_like_development": {
                "may_guide_training": True,
                "status": "OFFICIAL_LIKE_DEVELOPMENT_SET_MATERIALIZED" if official_like_ready else "NOT_YET_MATERIALIZED",
                "root": official_like_root,
                "required_categories": [
                    "multiple_choice_reasoning",
                    "boolean_qa",
                    "mathematics",
                    "commonsense_completion",
                    "code_generation",
                    "general_knowledge",
                    "pronoun_coreference",
                ],
                "purpose": "Router and substrate development; must exclude final official examples.",
            },
            "final_official_bounded": {
                "may_guide_training": False,
                "root": official_root,
                "file_count": final_file_count,
                "expected_file_count": expected_file_count,
                "purpose": "Final untouched evaluation only; not for checkpoint selection or hyperparameter search.",
            },
        },
        "final_official_files": _manifest_files(official),
        "exact_line_overlap_audit": overlap,
        "assertions": {
            "final_official_files_present": final_file_count == expected_file_count,
            "final_official_may_guide_training": False,
            "current_local_roots_have_no_exact_line_overlap_with_final": overlap["total_line_hash_overlap"] == 0,
            "official_like_development_set_ready": official_like_ready,
        },
        "blocked_until_dev_set_exists": [
            "router_regret_training_on_official_like_dev",
            "checkpoint_selection_by_official_like_macro_score",
            "official_like_development_generalization_claim",
        ],
    }
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    write_json(out / "official_evaluation_boundary_frozen.json", payload)
    lines = [
        "# Official Evaluation Boundary Freeze",
        "",
        f"Status: `{status}`",
        "",
        "## Tiers",
        "",
        "| tier | may guide training | status/root | purpose |",
        "|---|---|---|---|",
        f"| local heldout | true | `{', '.join(local_roots)}` | Fast regression and screening only. |",
        f"| official-like development | true | `{official_like_root}` / `{'READY' if official_like_ready else 'NOT_YET_MATERIALIZED'}` | Router/substrate development; final official examples excluded. |",
        f"| final official bounded | false | `{official_root}` | Final untouched evaluation only. |",
        "",
        "## Assertions",
        "",
        *[f"- {key}: `{value}`" for key, value in payload["assertions"].items()],
        "",
        "## Final Official Files",
        "",
        "| path | bytes | lines | sha256 |",
        "|---|---:|---:|---|",
    ]
    for row in payload["final_official_files"]:
        lines.append(f"| {row['path']} | {row['bytes']} | {row['line_count']} | `{row['sha256']}` |")
    lines.extend([
        "",
        "## Exact Line-Hash Overlap With Current Local Roots",
        "",
        "| root | overlap with final lines |",
        "|---|---:|",
    ])
    for row in overlap["rows"]:
        lines.append(f"| {row['root']} | {row['line_hash_overlap_with_final']} |")
    lines.extend([
        "",
        "Do not use the final eight official files for router repair, checkpoint selection, or hyperparameter search.",
    ])
    (out / "official_evaluation_boundary_frozen.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--official-root", default="data/eval/official_300m_bounded")
    parser.add_argument("--official-like-root", default="data/eval/official_like_dev")
    parser.add_argument("--output", default="benchmark/reports/generated/official_evaluation_boundary_frozen")
    parser.add_argument("--local-root", action="append", dest="local_roots")
    args = parser.parse_args()
    payload = run(official_root=args.official_root, official_like_root=args.official_like_root, local_roots=args.local_roots, output=args.output)
    print(json.dumps({"status": payload["status"], "assertions": payload["assertions"]}, indent=2))


if __name__ == "__main__":
    main()
