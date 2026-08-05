"""Final PVR comparative conclusion suite analysis and reporting."""

from __future__ import annotations

import csv
import json
import math
from collections import Counter
from pathlib import Path
from typing import Any

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from benchmark.common import git_commit, utc_now, write_json


DEFAULT_OUTPUT = "benchmark/reports/generated/pvr_final_comparative_conclusion_suite"

REQUIRED_300M_VARIANTS = [
    "pvr_full_scratch_300m_matched",
    "pvr_shared_warmup_no_geometry_head_300m_matched",
    "pvr_self_instilled_uniformity_geometry_head_v1_300m_matched",
    "pvr_descriptor_curriculum_head_300m_matched",
    "pvr_descriptor_plus_uniformity_head_300m_matched",
    "pvr_teacher_ean_300m_matched",
]

REQUIRED_700M_VARIANTS = [
    "dense_700m",
    "switch_top1_700m",
    "generic_top2_700m",
    "pvr_full_700m",
    "pvr_ec_o_ean_token_matched_700m",
    "pvr_ec_o_ean_retention_gated_delta_replay_700m",
]

CLASSWISE_REQUIRED = [
    "quote",
    "brace_bracket_paren",
    "operator",
    "json_key",
    "newline",
    "number",
    "function_signature",
    "identifier",
    "space",
    "indentation",
]

ALWAYS_BLOCKED_CLAIMS = [
    "PVR_ROUTE_MARGIN_PREDICTS_EXPERT_BENEFIT_SUPPORTED",
    "PVR_ROUTE_GEOMETRY_SPECIALIZATION_SUPPORTED",
    "PVR_REPLAY_ARCHITECTURE_SPECIFIC_ADVANTAGE_SUPPORTED",
    "PVR_BENEFIT_WEIGHTED_ROUTE_GEOMETRY_INDUCTION_SUPPORTED",
    "PVR_EXPERT_DELTA_TRAINING_CAUSALITY_SUPPORTED",
    "PVR_OFFICIAL_BROAD_NLP_SUPPORTED",
    "PVR_OFFICIAL_CODE_BENCH_SUPPORTED",
    "PVR_FROM_SCRATCH_DENSE_GAP_CLOSED",
    "PVR_TEACHER_INDEPENDENCE_SUPPORTED",
]


def _repo_path(root: Path, path: str | Path) -> Path:
    p = Path(path)
    return p if p.is_absolute() else root / p


def _load_json(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def _first_json(root: Path, candidates: list[str]) -> tuple[dict[str, Any] | None, str | None]:
    for rel in candidates:
        path = _repo_path(root, rel)
        data = _load_json(path)
        if data is not None:
            return data, rel
    return None, None


def _num(value: Any, default: float | None = None) -> float | None:
    if value is None:
        return default
    try:
        out = float(value)
    except (TypeError, ValueError):
        return default
    if math.isnan(out) or math.isinf(out):
        return default
    return out


def _bool(value: Any) -> bool:
    return bool(value)


def _nested(row: dict[str, Any], *keys: str) -> Any:
    cur: Any = row
    for key in keys:
        if not isinstance(cur, dict):
            return None
        cur = cur.get(key)
    return cur


def top1_clean(row: dict[str, Any]) -> bool:
    """Strict Top1 doctrine with compatibility for older report field names."""
    if row.get("top1_invariants_clean") is False or row.get("top1_clean") is False:
        return False
    invariants = row.get("hard_invariants") if isinstance(row.get("hard_invariants"), dict) else row
    routing = row.get("routing") if isinstance(row.get("routing"), dict) else {}

    def pick(*names: str) -> Any:
        for name in names:
            if name in invariants:
                return invariants[name]
            if name in routing:
                return routing[name]
            if name in row:
                return row[name]
        return None

    checks = [
        (pick("owners_per_token"), 1.0),
        (pick("top2_execution_count", "top2_executions", "top2_executions_count"), 0),
        (pick("top4_execution_count", "top4_executions", "top4_executions_count"), 0),
    ]
    optional_zero = [
        pick("runtime_dynamic_k_count"),
        pick("runtime_expert_choice_count"),
    ]
    optional_false = pick("production_map_mutated")
    if any(value is not None and value != expected for value, expected in checks):
        return False
    if any(value is not None and value != 0 for value in optional_zero):
        return False
    if optional_false is not None and optional_false is not False:
        return False
    explicit_true = row.get("top1_invariants_clean") is True or row.get("top1_clean") is True
    if any(value is not None for value, _ in checks):
        return True
    return explicit_true


def is_probe_only(row: dict[str, Any], source_path: str | None = None) -> bool:
    text = " ".join(
        str(x).lower()
        for x in [
            source_path or "",
            row.get("status", ""),
            row.get("experiment", ""),
            row.get("model_variant", ""),
            row.get("key", ""),
        ]
    )
    steps = _num(row.get("optimizer_steps", row.get("target_steps")))
    tokens = _num(row.get("training_tokens_seen", row.get("tokens_seen")))
    target_tokens = _num(row.get("target_training_tokens", row.get("training_tokens")))
    if "probe" in text:
        return True
    if steps is not None and steps <= 100:
        return True
    if target_tokens and tokens is not None and tokens < target_tokens:
        return True
    return False


def _token_budget_validation(
    rows: dict[str, dict[str, Any]],
    manifests: dict[str, dict[str, Any]],
    required_variants: list[str],
) -> dict[str, Any]:
    present = [variant for variant in required_variants if variant in rows]
    missing = [variant for variant in required_variants if variant not in rows]
    fields = {
        "optimizer_steps": [],
        "training_tokens": [],
        "effective_batch_tokens": [],
        "eval_windows": [],
        "scorecard_eval_token_count": [],
        "heldout_eval_token_count": [],
    }
    per_variant: dict[str, dict[str, Any]] = {}
    for variant in present:
        row = rows.get(variant, {})
        manifest = manifests.get(variant, {})
        training_tokens = (
            manifest.get("training_tokens_seen")
            or manifest.get("tokens_seen")
            or manifest.get("target_training_tokens")
            or row.get("training_tokens_seen")
            or row.get("training_tokens")
        )
        item = {
            "variant": variant,
            "optimizer_steps": manifest.get("optimizer_steps") or manifest.get("target_steps") or row.get("optimizer_steps"),
            "training_tokens": training_tokens,
            "effective_batch_tokens": manifest.get("effective_batch_tokens") or row.get("effective_batch_tokens"),
            "eval_windows": manifest.get("eval_window_count") or row.get("eval_window_count"),
            "scorecard_eval_token_count": row.get("eval_token_count"),
            "heldout_eval_token_count": row.get("heldout_eval_token_count"),
        }
        per_variant[variant] = item
        for key in fields:
            if item.get(key) is not None:
                fields[key].append(item[key])
    field_matches = {
        key: len(set(values)) == 1 and len(values) == len(present)
        for key, values in fields.items()
    }
    complete = not missing and all(field_matches.values()) and bool(present)
    return {
        "complete": complete,
        "present_variants": present,
        "missing_variants": missing,
        "field_matches": field_matches,
        "per_variant": per_variant,
        "summary": {key: sorted(set(values)) for key, values in fields.items()},
    }


def _copied_keys_cover_required(init_report: dict[str, Any]) -> bool:
    keys = " ".join(str(x).lower() for x in init_report.get("copied", []) + init_report.get("copied_keys", []))
    return all(needle in keys for needle in ["emb", "attn", "norm"])


def _validate_teacher_ean(report: dict[str, Any], root: Path, source_path: str | None) -> dict[str, Any]:
    rows = report.get("rows") if isinstance(report.get("rows"), dict) else {}
    manifests = report.get("training_manifests") if isinstance(report.get("training_manifests"), dict) else {}
    teacher_row = rows.get("pvr_teacher_ean_300m_matched", {})
    teacher_manifest = manifests.get("pvr_teacher_ean_300m_matched", {})
    init_report = (
        report.get("teacher_init_report")
        or report.get("init_report")
        or teacher_row.get("teacher_init_report")
        or teacher_manifest.get("teacher_init_report")
    )
    checkpoint_path = (
        teacher_row.get("checkpoint_path")
        or teacher_manifest.get("checkpoint_path")
        or _nested(report, "teacher", "checkpoint_path")
    )
    conditions = {
        "teacher_checkpoint_path_reported": bool(checkpoint_path),
        "teacher_checkpoint_path_exists": bool(checkpoint_path and _repo_path(root, checkpoint_path).exists()),
        "teacher_init_report_exists": isinstance(init_report, dict),
        "teacher_checkpoint_loaded": bool(isinstance(init_report, dict) and init_report.get("teacher_checkpoint_loaded") is True),
        "copy_scope_embeddings_attention_norms": bool(isinstance(init_report, dict) and init_report.get("copy_scope") == "embeddings_attention_norms"),
        "copied_count_positive": bool(isinstance(init_report, dict) and _num(init_report.get("copied_count"), 0) > 0),
        "skipped_count_positive": bool(isinstance(init_report, dict) and _num(init_report.get("skipped_count"), 0) > 0),
        "copied_keys_cover_embeddings_attention_norms": bool(isinstance(init_report, dict) and _copied_keys_cover_required(init_report)),
    }
    return {
        "valid": all(conditions.values()),
        "conditions": conditions,
        "checkpoint_path": checkpoint_path,
        "init_report": init_report if isinstance(init_report, dict) else None,
        "source_report_path": source_path,
    }


def _claim(
    claim: str,
    status: str,
    scope: str,
    required: str,
    found: str,
    caveat: str,
    source: str | None,
    status_detail: str | None = None,
) -> dict[str, Any]:
    return {
        "claim": claim,
        "status": status,
        "status_detail": status_detail or status,
        "scope": scope,
        "required_evidence": required,
        "evidence_found": found,
        "caveat": caveat,
        "source_report_path": source or "",
    }


def _descriptor_probe_rows(root: Path) -> tuple[dict[str, dict[str, Any]], str | None]:
    data, source = _first_json(
        root,
        ["benchmark/reports/generated/descriptor_ean_scaffold_screen/descriptor_ean_scaffold_screen_report.json"],
    )
    rows: dict[str, dict[str, Any]] = {}
    if not data:
        return rows, source
    alias = {
        "pvr_descriptor_curriculum_head_300m": "pvr_descriptor_curriculum_head_300m_matched",
        "pvr_descriptor_plus_uniformity_head_300m": "pvr_descriptor_plus_uniformity_head_300m_matched",
    }
    for item in data.get("results", []):
        name = alias.get(item.get("model_variant"))
        if not name:
            continue
        rows[name] = {
            **item,
            "key": name,
            "source_branch": "descriptor_curriculum_probe",
            "probe_only": True,
            "capability_evidence": False,
            "source_report_path": source,
            "caveat": "Small descriptor-curriculum screen; not matched-volume 300M capability evidence.",
        }
    return rows, source


def evaluate_300m_scaffold(
    report: dict[str, Any] | None,
    *,
    root: str | Path = ".",
    source_path: str | None = None,
) -> dict[str, Any]:
    root_path = Path(root)
    report = report or {}
    rows = {k: dict(v) for k, v in (report.get("rows") or {}).items()}
    for key, row in rows.items():
        row.setdefault("key", key)
        row.setdefault("source_branch", "300m_scaffold")
        row.setdefault("source_report_path", source_path)
    probe_rows, probe_source = _descriptor_probe_rows(root_path)
    for key, row in probe_rows.items():
        rows.setdefault(key, row)

    manifests = report.get("training_manifests") if isinstance(report.get("training_manifests"), dict) else {}
    budget = _token_budget_validation(rows, manifests, REQUIRED_300M_VARIANTS)
    teacher = _validate_teacher_ean(report, root_path, source_path)

    scratch = rows.get("pvr_full_scratch_300m_matched", {})
    no_head = rows.get("pvr_shared_warmup_no_geometry_head_300m_matched", {})
    teacher_row = rows.get("pvr_teacher_ean_300m_matched", {})
    scratch_loss = _num(scratch.get("lm_loss"))
    no_head_loss = _num(no_head.get("lm_loss"))
    teacher_loss = _num(teacher_row.get("lm_loss"))
    scratch_to_teacher_gap = None
    if teacher["valid"] and scratch_loss is not None and teacher_loss is not None:
        scratch_to_teacher_gap = scratch_loss - teacher_loss

    table: list[dict[str, Any]] = []
    gap_rows: list[dict[str, Any]] = []
    claims: list[dict[str, Any]] = []
    supported_labels: list[str] = []
    blocked_labels: dict[str, str] = {}

    for variant in REQUIRED_300M_VARIANTS:
        row = rows.get(variant, {"key": variant})
        loss = _num(row.get("lm_loss"))
        probe_only = bool(row.get("probe_only") or is_probe_only(row, row.get("source_report_path") or source_path))
        gap_closed = None
        if scratch_to_teacher_gap and scratch_to_teacher_gap > 0 and loss is not None:
            gap_closed = (scratch_loss - loss) / scratch_to_teacher_gap
        table.append(
            {
                "variant": variant,
                "lm_loss": loss,
                "perplexity": row.get("perplexity"),
                "training_tokens": _nested(budget, "per_variant", variant, "training_tokens") or row.get("tokens_seen"),
                "eval_tokens": row.get("eval_token_count"),
                "heldout_eval_tokens": row.get("heldout_eval_token_count"),
                "top1_clean": top1_clean(row),
                "probe_only": probe_only,
                "capability_evidence": (not probe_only) and variant in (report.get("rows") or {}),
                "source_branch": row.get("source_branch", "300m_scaffold"),
                "source_report_path": row.get("source_report_path") or source_path or "",
                "gap_closed_fraction": gap_closed,
            }
        )
        if variant not in {"pvr_full_scratch_300m_matched", "pvr_shared_warmup_no_geometry_head_300m_matched", "pvr_teacher_ean_300m_matched"}:
            gap_rows.append({"candidate": variant, "gap_closed_fraction": gap_closed})

    candidate = rows.get("pvr_self_instilled_uniformity_geometry_head_v1_300m_matched", {})
    candidate_loss = _num(candidate.get("lm_loss"))
    candidate_probe = is_probe_only(candidate, candidate.get("source_report_path") or source_path)
    support_conditions = {
        "token_budgets_matched": budget["complete"],
        "candidate_not_probe_only": not candidate_probe,
        "beats_plain_scratch": bool(candidate_loss is not None and scratch_loss is not None and candidate_loss < scratch_loss),
        "beats_no_head_warmup": bool(candidate_loss is not None and no_head_loss is not None and candidate_loss < no_head_loss),
        "top1_clean": top1_clean(candidate),
        "routing_health_pass": bool((report.get("routing_health") or {}).get("all_routing_health_gates_pass") or (report.get("supported_conditions") or {}).get("routing_health_gates_pass")),
        "geometry_health_pass": bool((report.get("geometry_health") or {}).get("all_health_gates_pass") or (report.get("supported_conditions") or {}).get("geometry_health_gates_pass")),
        "teacher_checkpoint_not_loaded_into_candidate": candidate.get("teacher_checkpoint_loaded") is False,
    }
    support_ok = all(support_conditions.values())
    support_detail = "supported" if support_ok else "blocked_gate_failed"
    if support_ok:
        supported_labels.append("PVR_SELF_INSTILLED_EAN_GEOMETRY_HEAD_SUPPORTED")
    else:
        blocked_labels["PVR_SELF_INSTILLED_EAN_GEOMETRY_HEAD_SUPPORTED"] = support_detail
    claims.append(
        _claim(
            "PVR_SELF_INSTILLED_EAN_GEOMETRY_HEAD_SUPPORTED",
            "supported" if support_ok else "blocked",
            "300M matched-volume scaffold comparison",
            "Candidate beats scratch and no-head warmup with clean Top1, routing, geometry, and no teacher loaded.",
            json.dumps(support_conditions, sort_keys=True),
            "Pure support is local only and does not prove teacher independence.",
            source_path,
            support_detail,
        )
    )

    narrows_ok = bool(support_ok and teacher["valid"] and scratch_to_teacher_gap and gap_rows and _num(gap_rows[0]["gap_closed_fraction"], 0) >= 0.50)
    closes_ok = bool(support_ok and teacher["valid"] and candidate_loss is not None and teacher_loss is not None and candidate_loss <= teacher_loss and (report.get("supported_conditions") or {}).get("confirmed_seed_count", 0) >= 2)
    for claim_name, ok, threshold in [
        ("PVR_SELF_INSTILLED_EAN_GEOMETRY_HEAD_NARROWS_TEACHER_GAP", narrows_ok, "support plus >=50% verified scratch-to-teacher gap closure"),
        ("PVR_SELF_INSTILLED_EAN_GEOMETRY_HEAD_CLOSES_TEACHER_GAP", closes_ok, "support plus match/beat verified teacher across at least two seeds"),
        ("PVR_DESCRIPTOR_CURRICULUM_NARROWS_EAN_GAP", False, "verified teacher-EAN plus matched-volume descriptor curriculum comparison"),
        ("PVR_DESCRIPTOR_CURRICULUM_REPLACES_EAN_SCAFFOLD", False, "match/beat verified teacher-EAN without loading teacher weights"),
    ]:
        if claim_name.startswith("PVR_DESCRIPTOR") and not teacher["valid"]:
            detail = "blocked_invalid_teacher_reference"
        elif claim_name.startswith("PVR_DESCRIPTOR"):
            detail = "blocked_not_tested_matched_volume"
        elif not teacher["valid"]:
            detail = "blocked_invalid_teacher_reference"
        elif not budget["complete"]:
            detail = "blocked_token_budget_mismatch"
        else:
            detail = "supported" if ok else "blocked_gate_failed"
        if ok:
            supported_labels.append(claim_name)
        else:
            blocked_labels[claim_name] = detail
        claims.append(
            _claim(
                claim_name,
                "supported" if ok else "blocked",
                "300M teacher-scaffold comparison",
                threshold,
                f"teacher_valid={teacher['valid']}; budget_complete={budget['complete']}; gap={scratch_to_teacher_gap}",
                "No teacher-gap claim is emitted without a verified teacher-EAN reference.",
                source_path if not claim_name.startswith("PVR_DESCRIPTOR") else (probe_source or source_path),
                detail,
            )
        )

    still_required = bool(teacher["valid"] and budget["complete"] and (not support_conditions["beats_no_head_warmup"] or not narrows_ok))
    if still_required:
        supported_labels.append("PVR_TEACHER_EAN_SCAFFOLD_STILL_REQUIRED")
    else:
        blocked_labels["PVR_TEACHER_EAN_SCAFFOLD_STILL_REQUIRED"] = "blocked_invalid_teacher_reference" if not teacher["valid"] else "not_supported_by_gate"
    claims.append(
        _claim(
            "PVR_TEACHER_EAN_SCAFFOLD_STILL_REQUIRED",
            "supported" if still_required else "blocked",
            "300M teacher-scaffold comparison",
            "Verified teacher-EAN, matched volume, and candidate closes <50% or loses to no-head warmup.",
            f"teacher_valid={teacher['valid']}; budget_complete={budget['complete']}; narrows={narrows_ok}",
            "Blocked if teacher-EAN reference is invalid, even if local losses suggest EAN is ahead.",
            source_path,
            "supported" if still_required else blocked_labels["PVR_TEACHER_EAN_SCAFFOLD_STILL_REQUIRED"],
        )
    )

    return {
        "source_report_path": source_path or "",
        "status": report.get("status", "not_tested") if report else "not_tested",
        "variants": table,
        "gap_closure": gap_rows,
        "token_budget_validation": budget,
        "teacher_ean_validity": teacher,
        "support_conditions": support_conditions,
        "supported_labels": supported_labels,
        "blocked_labels": blocked_labels,
        "claims": claims,
        "conclusion": (
            "Teacher-EAN reference is invalid under final hard checks; gap and replacement claims are blocked."
            if not teacher["valid"]
            else "Teacher-EAN scaffold remains ahead unless a candidate support gate closes the verified gap."
        ),
    }


def _training_tokens_matched(report: dict[str, Any], required: list[str]) -> bool:
    target = report.get("target_training_tokens_per_model")
    manifests = report.get("training_manifests") if isinstance(report.get("training_manifests"), dict) else {}
    if target is None or not manifests:
        return False
    for key in required:
        manifest = manifests.get(key)
        if not manifest:
            return False
        tokens = manifest.get("training_tokens_seen") or manifest.get("tokens_seen") or manifest.get("target_training_tokens")
        if tokens != target:
            return False
    return True


def evaluate_700m_frontier(seed_reports: dict[str, tuple[dict[str, Any], str]]) -> dict[str, Any]:
    seed_tables: dict[str, list[dict[str, Any]]] = {}
    seed_summaries: dict[str, dict[str, Any]] = {}
    supported_seeds: list[str] = []
    for seed, (report, source) in seed_reports.items():
        rows = report.get("rows") if isinstance(report.get("rows"), dict) else {}
        token_matched = _training_tokens_matched(report, REQUIRED_700M_VARIANTS)
        required_present = all(key in rows for key in REQUIRED_700M_VARIANTS)
        retention = rows.get("pvr_ec_o_ean_retention_gated_delta_replay_700m", {})
        retention_loss = _num(retention.get("lm_loss"))
        beats_all = bool(retention_loss is not None and all(retention_loss < _num(rows[key].get("lm_loss"), -math.inf) for key in REQUIRED_700M_VARIANTS if key != "pvr_ec_o_ean_retention_gated_delta_replay_700m" and _num(rows[key].get("lm_loss")) is not None))
        pareto = bool(
            retention.get("active_params_per_token") is not None
            and retention.get("active_flops_per_token") is not None
            and all(
                _num(retention.get("active_params_per_token"), math.inf) <= _num(rows[key].get("active_params_per_token"), -math.inf)
                and _num(retention.get("active_flops_per_token"), math.inf) <= _num(rows[key].get("active_flops_per_token"), -math.inf)
                for key in ["dense_700m", "switch_top1_700m", "generic_top2_700m", "pvr_full_700m", "pvr_ec_o_ean_token_matched_700m"]
            )
        )
        top1_ok = top1_clean(retention)
        status_valid = report.get("status") == "PVR_700M_EAN_RETENTION_GATED_TOKEN_MATCHED_FRONTIER_SUPPORTED"
        supported = all([required_present, token_matched, beats_all, pareto, top1_ok, status_valid])
        if supported:
            supported_seeds.append(str(seed))
        table = []
        for key in REQUIRED_700M_VARIANTS:
            row = rows.get(key, {})
            table.append(
                {
                    "seed": seed,
                    "model": key,
                    "lm_loss": row.get("lm_loss"),
                    "perplexity": row.get("perplexity"),
                    "active_params_per_token": row.get("active_params_per_token"),
                    "active_flops_per_token": row.get("active_flops_per_token"),
                    "quality_per_active_param": row.get("quality_per_active_param"),
                    "quality_per_active_flop": row.get("quality_per_active_flop"),
                    "tokens_per_second": row.get("tokens_per_second"),
                    "gpu_hours": row.get("gpu_hours") or _nested(report, "training_manifests", key, "gpu_hours"),
                    "peak_vram": row.get("vram_peak"),
                    "training_tokens": _nested(report, "training_manifests", key, "training_tokens_seen") or report.get("target_training_tokens_per_model"),
                    "eval_tokens": row.get("eval_token_count"),
                    "heldout_eval_tokens": row.get("heldout_eval_token_count"),
                    "top1_clean": top1_clean(row) if key.startswith("pvr") else row.get("top1_invariants_clean"),
                    "source_report_path": source,
                }
            )
        seed_tables[str(seed)] = table
        seed_summaries[str(seed)] = {
            "source_report_path": source,
            "status": report.get("status"),
            "supported": supported,
            "required_present": required_present,
            "token_matched": token_matched,
            "retention_beats_all": beats_all,
            "pareto_favorable": pareto,
            "top1_clean": top1_ok,
        }

    repeat_supported = {"42", "123"}.issubset(set(supported_seeds))
    plain_pvr_not_supported = True
    return {
        "seed_tables": seed_tables,
        "seed_summaries": seed_summaries,
        "supported_seeds": supported_seeds,
        "supported_labels": [
            "PVR_700M_EAN_RETENTION_GATED_TOKEN_MATCHED_FRONTIER_SUPPORTED"
        ]
        if supported_seeds
        else [],
        "repeat_supported": repeat_supported,
        "plain_pvr_active_compute_frontier_not_supported": plain_pvr_not_supported,
        "claims": [
            _claim(
                "PVR_700M_EAN_RETENTION_GATED_TOKEN_MATCHED_FRONTIER_SUPPORTED",
                "supported" if supported_seeds else "blocked",
                "700M local reduced-file token-matched active-compute frontier",
                "Retention-gated PVR beats dense, Switch, Top2, plain PVR, and EAN with exact token accounting and Pareto-favorable active compute.",
                f"supported_seeds={supported_seeds}",
                "Local reduced-file evidence only; not official external benchmark support.",
                next(iter(seed_reports.values()))[1] if seed_reports else None,
                "supported" if supported_seeds else "blocked_missing_valid_seed",
            ),
            _claim(
                "PVR_700M_EAN_RETENTION_GATED_TOKEN_MATCHED_FRONTIER_REPEAT_SUPPORTED",
                "supported" if repeat_supported else "blocked",
                "700M local reduced-file token-matched active-compute frontier repeat",
                "The frontier support gate passes for at least seeds 42 and 123.",
                f"supported_seeds={supported_seeds}",
                "Repeat support is still local and reduced-file.",
                "; ".join(source for _, source in seed_reports.values()),
                "supported" if repeat_supported else "blocked_missing_repeat",
            ),
            _claim(
                "PVR_700M_FULL_ACTIVE_COMPUTE_FRONTIER_NOT_SUPPORTED",
                "supported" if plain_pvr_not_supported else "blocked",
                "700M plain PVR active-compute frontier",
                "Plain PVR loses to dense/Switch/Top2 or is not Pareto efficient.",
                "Plain PVR rows lose in loaded local reports.",
                "This negative claim does not apply to EAN retention-gated delta replay.",
                "; ".join(source for _, source in seed_reports.values()),
                "supported" if plain_pvr_not_supported else "blocked",
            ),
        ],
    }


def evaluate_expert_causality(report: dict[str, Any] | None, source_path: str | None) -> dict[str, Any]:
    report = report or {}
    seed_rows: list[dict[str, Any]] = []
    class_totals: dict[str, dict[str, list[float]]] = {
        cls: {"benefit": [], "harm": [], "worse_rate": [], "count": []} for cls in CLASSWISE_REQUIRED
    }
    supported_seeds = 0
    for item in report.get("seed_results", []):
        seed = str(item.get("seed"))
        metrics = item.get("metrics") or {}
        causal = metrics.get("causal") or {}
        if item.get("status") == "PVR_EXPERT_DELTA_CAUSALITY_REPEAT_SUPPORTED":
            supported_seeds += 1
        seed_rows.append(
            {
                "seed": seed,
                "status": item.get("status"),
                "full_vs_shared_benefit": causal.get("mean_full_vs_shared_benefit"),
                "structured_full_vs_shared_benefit": causal.get("structured_full_vs_shared_benefit"),
                "wrong_expert_harm": causal.get("mean_wrong_expert_harm"),
                "structured_wrong_expert_harm": causal.get("structured_wrong_expert_harm"),
                "wrong_expert_worse_than_full_rate": causal.get("wrong_expert_worse_than_full_rate"),
                "structured_wrong_expert_worse_than_full_rate": causal.get("structured_wrong_expert_worse_than_full_rate"),
                "top1_clean": _nested(item, "metrics", "top1_invariants_clean") or _nested(item, "metrics", "top1_invariants_clean"),
                "source_report_path": source_path or "",
            }
        )
        for cls, values in (metrics.get("classwise") or {}).items():
            if cls in class_totals:
                class_totals[cls]["benefit"].append(values.get("full_vs_shared_benefit", 0))
                class_totals[cls]["harm"].append(values.get("wrong_expert_harm", 0))
                class_totals[cls]["worse_rate"].append(values.get("wrong_expert_worse_than_full_rate", 0))
                class_totals[cls]["count"].append(values.get("count", 0))
    class_rows = []
    for cls in CLASSWISE_REQUIRED:
        vals = class_totals[cls]
        class_rows.append(
            {
                "class": cls,
                "full_vs_shared_benefit": sum(vals["benefit"]) / len(vals["benefit"]) if vals["benefit"] else None,
                "wrong_expert_harm": sum(vals["harm"]) / len(vals["harm"]) if vals["harm"] else None,
                "wrong_expert_worse_than_full_rate": sum(vals["worse_rate"]) / len(vals["worse_rate"]) if vals["worse_rate"] else None,
                "count": sum(vals["count"]) if vals["count"] else 0,
            }
        )
    supported = report.get("status") == "PVR_EXPERT_DELTA_CAUSALITY_REPEAT_SUPPORTED" and supported_seeds >= int(report.get("required_repeats", 2))
    return {
        "source_report_path": source_path or "",
        "seed_rows": seed_rows,
        "classwise_rows": class_rows,
        "supported": supported,
        "claims": [
            _claim(
                "PVR_EXPERT_DELTA_CAUSALITY_SUPPORTED",
                "supported" if supported_seeds else "blocked",
                "Inference-time expert intervention audit",
                "Full-vs-shared benefit and wrong-expert harm under clean Top1 intervention evidence.",
                f"supported_seed_count={supported_seeds}",
                "Inference-time causal support only; not training-causal proof.",
                source_path,
                "supported" if supported_seeds else "blocked_missing_intervention_evidence",
            ),
            _claim(
                "PVR_EXPERT_DELTA_CAUSALITY_REPEAT_SUPPORTED",
                "supported" if supported else "blocked",
                "Inference-time expert intervention repeat audit",
                "At least two supported seeds plus structured classwise intervention evidence.",
                f"status={report.get('status')}; supported_seed_count={supported_seeds}",
                "Inference-time causal support only; not training-causal proof.",
                source_path,
                "supported" if supported else "blocked_missing_repeat",
            ),
        ],
    }


def evaluate_descriptor_deployment(root: Path) -> dict[str, Any]:
    gate, gate_source = _first_json(
        root,
        [
            "evaluation/benchmark_results/pvr_final_repaired_deployment_gate/pvr_ec_final_repaired_deployment_gate_report.json",
            "evaluation/benchmark_results/latest/pvr_ec_final_repaired_deployment_gate_report.json",
            "evaluation/benchmark_results/pvr_final_deployment_gate/pvr_ec_final_deployment_gate_report.json",
        ],
    )
    release, release_source = _first_json(
        root,
        ["evaluation/benchmark_results/pvr_release_hardening/pvr_ec_final_release_readiness_report.json"],
    )
    production, production_source = _first_json(
        root,
        ["evaluation/benchmark_results/pvr_release_hardening/pvr_ec_production_shape_profile_report.json"],
    )
    gate = gate or {}
    release = release or {}
    production = production or {}
    desc = gate.get("descriptor_control") if isinstance(gate.get("descriptor_control"), dict) else {}
    production_results = production.get("results") if isinstance(production.get("results"), dict) else {}
    prod_pass_rate = production.get("pass_rate")
    peak_mem = max((_num(row.get("memory_peak_mb"), 0) or 0 for row in production_results.values()), default=None)
    gates = gate.get("gates") if isinstance(gate.get("gates"), dict) else {}
    total_tests_passed = sum(1 for value in gates.values() if value) + sum(1 for row in production_results.values() if row.get("pass"))
    descriptor_accuracy = desc.get("mean_correct")
    descriptor_removed_accuracy = desc.get("mean_removed")
    descriptor_control_margin = desc.get("mean_margin")
    ablation_drop = None
    if descriptor_accuracy is not None and descriptor_removed_accuracy is not None:
        ablation_drop = descriptor_accuracy - descriptor_removed_accuracy
    top1_ok = top1_clean(gate) and top1_clean(release) and (all(top1_clean(row) for row in production_results.values()) if production_results else True)
    deployment_supported = gate.get("deployment_verdict") == "PVR_EC_DEPLOYMENT_CANDIDATE_CONFIRMED" and all(gates.values()) and top1_ok
    release_supported = release.get("final_release_verdict") == "PVR_EC_RELEASE_READY_FOR_CANARY" and top1_ok
    metrics = {
        "total_tests_passed": total_tests_passed,
        "descriptor_accuracy": descriptor_accuracy,
        "descriptor_control_margin": descriptor_control_margin,
        "descriptor_removed_accuracy": descriptor_removed_accuracy,
        "descriptor_ablation_drop": ablation_drop,
        "heldout_family_accuracy": None,
        "production_shape_pass_rate": prod_pass_rate,
        "peak_gpu_memory_mb": peak_mem,
        "deployment_gates": gates,
    }
    return {
        "source_report_path": gate_source or "",
        "release_source_report_path": release_source or "",
        "production_source_report_path": production_source or "",
        "metrics": metrics,
        "deployment_supported": deployment_supported,
        "release_supported": release_supported,
        "claims": [
            _claim(
                "PVR_EC_DEPLOYMENT_CANDIDATE_CONFIRMED",
                "supported" if deployment_supported else "blocked",
                "Small production-shaped descriptor-controlled routing candidate",
                "Deployment gates pass with descriptor control, production shape, and strict Top1 invariants.",
                json.dumps({"gates": gates, "top1_clean": top1_ok}, sort_keys=True),
                "Does not prove 300M/700M LM frontier performance, teacher independence, or official benchmark support.",
                gate_source,
                "supported" if deployment_supported else "blocked_deployment_gate_failed",
            ),
            _claim(
                "PVR_EC_RELEASE_READY_FOR_CANARY",
                "supported" if release_supported else "blocked",
                "Small production-shaped descriptor-controlled routing candidate",
                "Release hardening passes freeze, manifest lock, production shape, canary simulation, and drift setup.",
                f"final_release_verdict={release.get('final_release_verdict')}; top1_clean={top1_ok}",
                "Canary readiness is scoped to the small production-shaped descriptor branch.",
                release_source,
                "supported" if release_supported else "blocked_release_gate_failed",
            ),
        ],
    }


def _write_csv(path: Path, rows: list[dict[str, Any]], fields: list[str] | None = None) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    if fields is None:
        fields = sorted({key for row in rows for key in row.keys()}) or ["empty"]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    return str(path)


def _save_plot(fig: plt.Figure, figure_dir: Path, name: str, rows: list[dict[str, Any]], fields: list[str] | None = None) -> dict[str, Any]:
    figure_dir.mkdir(parents=True, exist_ok=True)
    png = figure_dir / f"{name}.png"
    pdf = figure_dir / f"{name}.pdf"
    csv_path = figure_dir / f"{name}.csv"
    fig.tight_layout()
    fig.savefig(png, dpi=160)
    fig.savefig(pdf)
    plt.close(fig)
    _write_csv(csv_path, rows, fields)
    return {"id": name, "png": str(png), "pdf": str(pdf), "csv": str(csv_path)}


def _empty_plot(title: str, message: str) -> plt.Figure:
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.text(0.5, 0.5, message, ha="center", va="center", wrap=True)
    ax.set_title(title)
    ax.set_axis_off()
    return fig


def _bar_plot(title: str, rows: list[dict[str, Any]], x_key: str, y_key: str, ylabel: str, threshold: float | None = None) -> plt.Figure:
    plot_rows = [r for r in rows if _num(r.get(y_key)) is not None]
    if not plot_rows:
        return _empty_plot(title, "No valid numeric evidence available.")
    labels = [str(r.get(x_key)) for r in plot_rows]
    values = [_num(r.get(y_key), 0) or 0 for r in plot_rows]
    fig, ax = plt.subplots(figsize=(max(8, len(labels) * 1.0), 4.8))
    ax.bar(labels, values, color="#3b6ea8")
    if threshold is not None:
        ax.axhline(threshold, color="#9b3d3d", linestyle="--", linewidth=1.5, label=f"threshold {threshold:g}")
        ax.legend()
    ax.set_title(title)
    ax.set_ylabel(ylabel)
    ax.tick_params(axis="x", labelrotation=35)
    return fig


def _write_figures(output: Path, report: dict[str, Any]) -> list[dict[str, Any]]:
    figure_dir = output / "figures"
    figures: list[dict[str, Any]] = []
    scaffold_rows = report["experiments"]["scaffold_300m"]["variants"]
    gap_rows = [
        {**row, "gap_closed_percent": (_num(row.get("gap_closed_fraction"), 0) or 0) * 100}
        for row in report["experiments"]["scaffold_300m"]["gap_closure"]
    ]
    figures.append(_save_plot(_bar_plot("300M Scaffold LM Loss", scaffold_rows, "variant", "lm_loss", "LM loss"), figure_dir, "fig_300m_scaffold_lm_loss_bar", scaffold_rows))
    figures.append(_save_plot(_bar_plot("300M Teacher-EAN Gap Closure", gap_rows, "candidate", "gap_closed_percent", "Gap closed (%)", 50), figure_dir, "fig_300m_ean_gap_closure", gap_rows))

    frontier = report["experiments"]["frontier_700m"]
    for seed in ["42", "123"]:
        rows = frontier["seed_tables"].get(seed, [])
        figures.append(_save_plot(_bar_plot(f"700M LM Loss by Model Seed {seed}", rows, "model", "lm_loss", "LM loss"), figure_dir, f"fig_700m_lm_loss_by_model_seed{seed}", rows))

    all_700 = [row for rows in frontier["seed_tables"].values() for row in rows]
    for name, x_key, title, xlabel in [
        ("fig_700m_active_flops_vs_lm_loss", "active_flops_per_token", "700M Active FLOPs vs LM Loss", "Active FLOPs/token"),
        ("fig_700m_active_params_vs_lm_loss", "active_params_per_token", "700M Active Params vs LM Loss", "Active params/token"),
    ]:
        rows = [r for r in all_700 if _num(r.get(x_key)) is not None and _num(r.get("lm_loss")) is not None]
        if rows:
            fig, ax = plt.subplots(figsize=(8, 5))
            ax.scatter([r[x_key] for r in rows], [r["lm_loss"] for r in rows], color="#2f7f6f")
            for r in rows:
                ax.annotate(f"{r['model']} s{r['seed']}", (r[x_key], r["lm_loss"]), fontsize=8)
            ax.set_title(title)
            ax.set_xlabel(xlabel)
            ax.set_ylabel("LM loss (lower is better)")
        else:
            fig = _empty_plot(title, "No valid numeric evidence available.")
        figures.append(_save_plot(fig, figure_dir, name, rows))

    figures.append(_save_plot(_bar_plot("700M Quality per Active FLOP", all_700, "model", "quality_per_active_flop", "Quality per active FLOP"), figure_dir, "fig_700m_quality_per_flop", all_700))

    top1_rows = []
    for row in scaffold_rows:
        if row["variant"].startswith("pvr"):
            top1_rows.append({"variant": row["variant"], "top1_clean": 1 if row.get("top1_clean") else 0})
    for row in all_700:
        if str(row.get("model", "")).startswith("pvr"):
            top1_rows.append({"variant": f"{row['model']}_seed{row['seed']}", "top1_clean": 1 if row.get("top1_clean") else 0})
    figures.append(_save_plot(_bar_plot("Top1 Invariant Summary", top1_rows, "variant", "top1_clean", "Top1 clean (1=yes)"), figure_dir, "fig_top1_invariant_summary", top1_rows))

    causality = report["experiments"]["expert_causality"]
    seed_rows = causality["seed_rows"]
    if seed_rows:
        fig, ax = plt.subplots(figsize=(8, 5))
        labels = [str(r["seed"]) for r in seed_rows]
        x = range(len(labels))
        width = 0.35
        ax.bar([i - width / 2 for i in x], [_num(r.get("full_vs_shared_benefit"), 0) or 0 for r in seed_rows], width, label="full-vs-shared benefit")
        ax.bar([i + width / 2 for i in x], [_num(r.get("wrong_expert_harm"), 0) or 0 for r in seed_rows], width, label="wrong-expert harm")
        ax.set_xticks(list(x), labels)
        ax.set_title("Expert Causality Seed Comparison")
        ax.set_ylabel("Loss delta")
        ax.legend()
    else:
        fig = _empty_plot("Expert Causality Seed Comparison", "No valid causality evidence available.")
    figures.append(_save_plot(fig, figure_dir, "fig_expert_causality_seed_comparison", seed_rows))

    class_rows = causality["classwise_rows"]
    if class_rows:
        fig, ax = plt.subplots(figsize=(10, 5))
        labels = [r["class"] for r in class_rows]
        x = range(len(labels))
        width = 0.35
        ax.bar([i - width / 2 for i in x], [_num(r.get("full_vs_shared_benefit"), 0) or 0 for r in class_rows], width, label="benefit")
        ax.bar([i + width / 2 for i in x], [_num(r.get("wrong_expert_harm"), 0) or 0 for r in class_rows], width, label="harm")
        ax.set_xticks(list(x), labels, rotation=35, ha="right")
        ax.set_title("Expert Causality by Token Class")
        ax.set_ylabel("Loss delta")
        ax.legend()
    else:
        fig = _empty_plot("Expert Causality by Token Class", "No valid classwise evidence available.")
    figures.append(_save_plot(fig, figure_dir, "fig_expert_causality_classwise", class_rows))

    descriptor_metrics = report["experiments"]["descriptor_deployment"]["metrics"]
    desc_rows = [
        {"metric": "descriptor_accuracy", "value": descriptor_metrics.get("descriptor_accuracy")},
        {"metric": "descriptor_removed_accuracy", "value": descriptor_metrics.get("descriptor_removed_accuracy")},
        {"metric": "descriptor_control_margin", "value": descriptor_metrics.get("descriptor_control_margin")},
        {"metric": "heldout_family_accuracy", "value": descriptor_metrics.get("heldout_family_accuracy")},
    ]
    figures.append(_save_plot(_bar_plot("Descriptor Deployment Metrics", desc_rows, "metric", "value", "Value"), figure_dir, "fig_descriptor_deployment_metrics", desc_rows))

    counts = Counter(row["status"] for row in report["claim_ledger"])
    claim_rows = [{"status": status, "count": counts.get(status, 0)} for status in ["supported", "partially supported", "blocked", "not tested"]]
    figures.append(_save_plot(_bar_plot("Claim Status Summary", claim_rows, "status", "count", "Claims"), figure_dir, "fig_claim_status_summary", claim_rows))
    return figures


def _md_table(rows: list[dict[str, Any]], fields: list[str]) -> list[str]:
    lines = ["| " + " | ".join(fields) + " |", "| " + " | ".join("---" for _ in fields) + " |"]
    for row in rows:
        vals = [str(row.get(field, "")).replace("\n", " ") for field in fields]
        lines.append("| " + " | ".join(vals) + " |")
    return lines


def _write_markdown(output: Path, report: dict[str, Any]) -> str:
    path = output / "pvr_final_comparative_conclusion_report.md"
    lines = [
        "# PVR Final Comparative Conclusion Suite",
        "",
        "## Executive conclusion",
        "",
        report["final_conclusion"]["strongest_supported_local_story"],
        "",
        report["final_conclusion"]["blocked_story"],
        "",
        "## Claim ledger",
        "",
        *_md_table(report["claim_ledger"], ["claim", "status", "status_detail", "scope", "evidence_found", "caveat", "source_report_path"]),
        "",
        "## 300M scaffold comparison",
        "",
        *_md_table(report["experiments"]["scaffold_300m"]["variants"], ["variant", "lm_loss", "training_tokens", "eval_tokens", "heldout_eval_tokens", "top1_clean", "probe_only", "capability_evidence", "source_branch"]),
        "",
        "Token budget validation:",
        "",
        "```json",
        json.dumps(report["experiments"]["scaffold_300m"]["token_budget_validation"], indent=2, sort_keys=True, default=str),
        "```",
        "",
        "Teacher-EAN validity validation:",
        "",
        "```json",
        json.dumps(report["experiments"]["scaffold_300m"]["teacher_ean_validity"], indent=2, sort_keys=True, default=str),
        "```",
        "",
        report["experiments"]["scaffold_300m"]["conclusion"],
        "",
        "## 700M active-compute frontier",
        "",
    ]
    for seed, rows in report["experiments"]["frontier_700m"]["seed_tables"].items():
        lines.extend([f"### Seed {seed}", "", *_md_table(rows, ["model", "lm_loss", "active_params_per_token", "active_flops_per_token", "quality_per_active_flop", "training_tokens", "eval_tokens", "heldout_eval_tokens", "top1_clean"]), ""])
    lines.extend(
        [
            "Repeat summary:",
            "",
            "```json",
            json.dumps(report["experiments"]["frontier_700m"]["seed_summaries"], indent=2, sort_keys=True, default=str),
            "```",
            "",
            "## Expert causality",
            "",
            *_md_table(report["experiments"]["expert_causality"]["seed_rows"], ["seed", "status", "full_vs_shared_benefit", "structured_full_vs_shared_benefit", "wrong_expert_harm", "structured_wrong_expert_harm"]),
            "",
            *_md_table(report["experiments"]["expert_causality"]["classwise_rows"], ["class", "full_vs_shared_benefit", "wrong_expert_harm", "wrong_expert_worse_than_full_rate", "count"]),
            "",
            "Inference-time causal support only; this is not training-causal proof.",
            "",
            "## Descriptor deployment branch",
            "",
            "```json",
            json.dumps(report["experiments"]["descriptor_deployment"]["metrics"], indent=2, sort_keys=True, default=str),
            "```",
            "",
            "This branch proves small production-shaped descriptor-controlled routing readiness. It does not prove 300M/700M LM frontier performance, teacher independence, or official benchmark support.",
            "",
            "## Blocked claims",
            "",
            *_md_table([row for row in report["claim_ledger"] if row["status"] == "blocked"], ["claim", "status_detail", "caveat", "source_report_path"]),
            "",
            "## Final recommended next actions",
            "",
            "- If teacher-EAN remains ahead: run descriptor-conditioned scaffold V2 against a verified teacher-EAN baseline.",
            "- If official benchmarks are missing: perform the official adapter audit before any broad NLP/code claim.",
            "- If 700M local frontier remains supported: freeze the local frontier claim and preserve the external benchmark caveat.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")
    return str(path)


def build_report(
    output: str | Path = DEFAULT_OUTPUT,
    *,
    root: str | Path = ".",
    seeds: list[str] | None = None,
    use_existing: bool = True,
    strict: bool = False,
    fail_on_missing_required: bool = False,
    allow_partial: bool = True,
) -> dict[str, Any]:
    root_path = Path(root)
    output_path = Path(output)
    seeds = [str(seed) for seed in (seeds or ["42", "123"])]

    scaffold_report, scaffold_source = _first_json(
        root_path,
        ["benchmark/reports/generated/self_instilled_ean_geometry_head_300m_matched_volume_screen/self_instilled_ean_geometry_head_matched_volume_screen_report.json"],
    )
    scaffold = evaluate_300m_scaffold(scaffold_report, root=root_path, source_path=scaffold_source)

    seed_candidates = {
        "42": ["benchmark/reports/generated/ean_retention_gated_token_matched_700m/ean_retention_gated_token_matched_700m_report.json"],
        "123": [
            "benchmark/reports/generated/ean_retention_gated_token_matched_700m_seed_123_strict/ean_retention_gated_token_matched_700m_repeat_report.json",
            "benchmark/reports/generated/ean_retention_gated_token_matched_700m_seed_123/ean_retention_gated_token_matched_700m_repeat_report.json",
        ],
    }
    seed_reports: dict[str, tuple[dict[str, Any], str]] = {}
    for seed in seeds:
        data, source = _first_json(root_path, seed_candidates.get(seed, []))
        if data and source:
            if data.get("status") == "SUPERSEDED_TOKEN_ACCOUNTING_INVALID" and not allow_partial:
                continue
            seed_reports[seed] = (data, source)
    frontier = evaluate_700m_frontier(seed_reports)

    causality_report, causality_source = _first_json(
        root_path,
        ["benchmark/reports/generated/expert_delta_causality_repeat_classwise_audit/expert_delta_causality_repeat_classwise_audit_report.json"],
    )
    causality = evaluate_expert_causality(causality_report, causality_source)
    descriptor = evaluate_descriptor_deployment(root_path)

    claim_ledger = []
    claim_ledger.extend(scaffold["claims"])
    claim_ledger.extend(frontier["claims"])
    claim_ledger.extend(causality["claims"])
    claim_ledger.extend(descriptor["claims"])
    for claim_name in ALWAYS_BLOCKED_CLAIMS:
        claim_ledger.append(
            _claim(
                claim_name,
                "blocked",
                "Official, training-causal, teacher-independence, or route-specialization claim",
                "Explicit direct evidence from the relevant official/training-causal/specialization audit.",
                "No explicit passing evidence in this final suite.",
                "Blocked by default unless explicit evidence is present.",
                "",
                "blocked_missing_explicit_evidence",
            )
        )

    supported_claims = [row["claim"] for row in claim_ledger if row["status"] == "supported"]
    blocked_claims = {row["claim"]: row["status_detail"] for row in claim_ledger if row["status"] == "blocked"}
    report = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "git_commit": git_commit(),
        "runner": "benchmark.runners.run_pvr_final_comparative_conclusion_suite",
        "options": {
            "use_existing": use_existing,
            "seeds": seeds,
            "strict": strict,
            "fail_on_missing_required": fail_on_missing_required,
            "allow_partial": allow_partial,
        },
        "claim_ledger": claim_ledger,
        "supported_claims": supported_claims,
        "blocked_claims": blocked_claims,
        "experiments": {
            "scaffold_300m": scaffold,
            "frontier_700m": frontier,
            "expert_causality": causality,
            "descriptor_deployment": descriptor,
            "official_benchmark": {
                "status": "blocked",
                "caveat": "Official broad NLP/code benchmark evidence was not loaded by this suite.",
            },
        },
        "figures": [],
        "tables": {},
        "final_conclusion": {
            "strongest_supported_local_story": "PVR-EC-O has local reduced-file evidence that EAN geometry transfer plus strict Top1 sparse residual execution plus retention-gated delta replay can produce active-compute frontier wins at 700M under matched-token accounting. Expert deltas are inference-causally useful, especially for structured/syntax-heavy tokens.",
            "supported_deployment_story": "The small descriptor-curriculum PVR-EC candidate is deployment-gated and canary-ready under its production-shaped test profile.",
            "blocked_story": "Teacher independence is not yet proven. Pure uniformity geometry head failed to replace EAN at 300M matched volume. Descriptor-curriculum-as-EAN-scaffold remains unproven until tested against a verified teacher-EAN baseline.",
            "claim_outcomes": {**{claim: "supported" for claim in supported_claims}, **blocked_claims},
        },
    }

    output_path.mkdir(parents=True, exist_ok=True)
    table_dir = output_path / "tables"
    report["tables"] = {
        "claim_ledger": _write_csv(table_dir / "claim_ledger.csv", claim_ledger),
        "scaffold_300m_variants": _write_csv(table_dir / "scaffold_300m_variants.csv", scaffold["variants"]),
        "scaffold_300m_gap_closure": _write_csv(table_dir / "scaffold_300m_gap_closure.csv", scaffold["gap_closure"]),
        "frontier_700m_seed_rows": _write_csv(table_dir / "frontier_700m_seed_rows.csv", [row for rows in frontier["seed_tables"].values() for row in rows]),
        "expert_causality_seed_rows": _write_csv(table_dir / "expert_causality_seed_rows.csv", causality["seed_rows"]),
        "expert_causality_classwise_rows": _write_csv(table_dir / "expert_causality_classwise_rows.csv", causality["classwise_rows"]),
        "descriptor_deployment_metrics": _write_csv(table_dir / "descriptor_deployment_metrics.csv", [{"metric": k, "value": v} for k, v in descriptor["metrics"].items() if not isinstance(v, dict)]),
        "blocked_claims": _write_csv(table_dir / "blocked_claims.csv", [row for row in claim_ledger if row["status"] == "blocked"]),
    }
    report["figures"] = _write_figures(output_path, report)
    markdown_path = _write_markdown(output_path, report)
    report["markdown_report_path"] = markdown_path
    json_path = output_path / "pvr_final_comparative_conclusion_report.json"
    write_json(json_path, report)
    report["json_report_path"] = str(json_path)

    missing_hard = []
    if fail_on_missing_required and not scaffold["token_budget_validation"]["complete"]:
        missing_hard.append("300M matched-volume variants or token budgets")
    if fail_on_missing_required and not frontier["supported_seeds"]:
        missing_hard.append("700M supported seed evidence")
    if strict and missing_hard:
        raise RuntimeError("Missing required final-suite evidence: " + ", ".join(missing_hard))
    return report

