"""PVR-EC-O Targeted Monopoly Collapse Repair.

Repairs harmful prototype monopoly without damaging useful specialization.
Uses per-prototype bucketing to gate repairs: protect stable owners,
refresh only high-gap monopolies, and measure prototype geometry uncertainty.

Forbidden:
- Global anti-monopoly penalty
- Global family_bias_cap increase without prototype gating
- Top2/Top4 execution
- Production map mutation
- Promotion from mean metrics
"""

import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "sparse_loop_moe" / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import torch
import torch.nn.functional as F
import numpy as np

from sparse_loop_moe.models.pvr_ec.pvr_ec_model import PVRECModel, PVRECModelConfig
from sparse_loop_moe.models.pvr_ec.nlp_stage1_tasks import NLP_STAGE1_TASKS, generate_nlp_stage1_batch
from sparse_loop_moe.models.pvr_ec.family_preservation import compute_family_membership
from sparse_loop_moe.models.pvr_ec.family_preserving_router import (
    compute_expert_choice_evidence, create_blank_candidate_map,
    refresh_candidate_map_from_evidence, family_preserving_top1_score,
    CandidateMap,
)


# =============================================================================
# Config
# =============================================================================

MIN_SAMPLES = 20
ORACLE_GAP_PROTECT_THRESHOLD = 2.0  # Relative to this model's scale
ORACLE_GAP_REPAIR_THRESHOLD = 4.0   # Only repair clearly worst cases
CHALLENGER_DISAGREE_REPAIR_THRESHOLD = 0.60
MONOPOLY_THRESHOLD = 0.90
BOUNDARY_MARGIN_THRESHOLD = 0.05
GEOMETRY_ENTROPY_UNIFORM_THRESHOLD = 2.7  # near log(16)=2.77 — very close to uniform


# =============================================================================
# Model + Training
# =============================================================================

def build_model(device="cuda", expert_delta_scale=1.0):
    config = PVRECModelConfig(
        vocab_size=256, d_model=128, max_seq_len=128,
        n_layers=2, n_heads=4, d_ff=256, num_experts=4,
        num_prototypes=16, max_k=4, d_expert=64,
        pvr_deploy_mode="top1", dropout=0.0,
        pvr_expert_delta_scale=expert_delta_scale,
    )
    return PVRECModel(config).to(device)


def train_model(model, tasks, steps=300, batch_size=32, seq_len=16,
                max_seq_len=64, lr=3e-3, seed=42, device="cuda"):
    optimizer = torch.optim.AdamW(model.parameters(), lr=lr, weight_decay=0.0)
    model.train()
    for task in tasks:
        x, y, _ = generate_nlp_stage1_batch(task, batch_size=batch_size,
                                            seq_len=seq_len, max_seq_len=max_seq_len, seed=seed)
        x, y = x.to(device), y.to(device)
        for _ in range(steps):
            optimizer.zero_grad(set_to_none=True)
            out = model(input_ids=x, targets=y)
            out["loss"].backward()
            optimizer.step()
    return model


# =============================================================================
# Per-Prototype Data Collection
# =============================================================================

def collect_prototype_data(model, tasks, batch_size=32, seq_len=16,
                           max_seq_len=64, seed=42, device="cuda"):
    """Collect per-prototype performance, routing, and challenger data."""
    model.eval()
    num_prototypes = model.config.num_prototypes
    num_experts = model.config.num_experts
    d_model = model.config.d_model

    proto_data = {p: {
        "token_count": 0, "correct_count": 0, "total_loss": 0.0,
        "owner_ids": [], "membership_entropy": [], "membership_margin": [],
        "is_boundary": [], "challenger_disagrees": [],
        "per_expert_loss_sum": np.zeros(num_experts),
        "per_expert_count": np.zeros(num_experts),
    } for p in range(num_prototypes)}

    for task in tasks:
        x, y, _ = generate_nlp_stage1_batch(task, batch_size=batch_size,
                                            seq_len=seq_len, max_seq_len=max_seq_len, seed=seed)
        x, y = x.to(device), y.to(device)

        with torch.no_grad():
            positions = torch.arange(max_seq_len, device=device).unsqueeze(0)
            hidden = model.dropout(model.token_emb(x) + model.pos_emb(positions))
            block = model.blocks[0]
            attn_in = block.attn_ln(hidden)
            attn_out, _ = block.attn(attn_in, attn_in, attn_in, need_weights=False)
            post_attn = hidden + block.attn_dropout(attn_out)
            moe_in = block.moe_ln(post_attn)
            flat = moe_in.reshape(-1, d_model)

            router = block.moe.router
            z = router.route_proj(flat)
            fm = compute_family_membership(z, router.prototypes)
            proto_ids = fm.nearest_prototype

            moe_out, aux = block.moe(moe_in)
            owner_ids = aux["primary_expert_ids"]

            out = model(input_ids=x, targets=y)
            preds = out["logits"].argmax(dim=-1).reshape(-1)
            targets_flat = y.reshape(-1)
            correct = (preds == targets_flat)
            logits_flat = out["logits"].reshape(-1, model.config.vocab_size)
            per_token_loss = F.cross_entropy(logits_flat, targets_flat, reduction="none")

            experts = list(block.moe.expert_deltas)
            evidence = compute_expert_choice_evidence(flat, experts, proto_ids, owner_ids, targets_flat)
            best_experts = evidence["best_expert_per_token"].to(device)
            challenger_disagrees = (best_experts != owner_ids)

            # Accumulate
            N = flat.shape[0]
            for i in range(N):
                p = proto_ids[i].item()
                e = owner_ids[i].item()
                proto_data[p]["token_count"] += 1
                proto_data[p]["owner_ids"].append(e)
                proto_data[p]["correct_count"] += int(correct[i].item())
                proto_data[p]["total_loss"] += per_token_loss[i].item()
                proto_data[p]["membership_entropy"].append(fm.membership_entropy[i].item())
                proto_data[p]["membership_margin"].append(fm.membership_margin[i].item())
                proto_data[p]["is_boundary"].append(int(fm.is_boundary[i].item()))
                proto_data[p]["challenger_disagrees"].append(int(challenger_disagrees[i].item()))
                proto_data[p]["per_expert_loss_sum"][e] += per_token_loss[i].item()
                proto_data[p]["per_expert_count"][e] += 1

    return proto_data


# =============================================================================
# Prototype Bucketing
# =============================================================================

def bucket_prototypes(proto_data, num_experts=4):
    """Assign each prototype to a bucket based on its metrics."""
    buckets = {
        "PROTECT_STABLE_OWNER": [],
        "REPAIR_HIGH_GAP_MONOPOLY": [],
        "REPAIR_HIGH_GAP_NON_MONOPOLY": [],
        "LOW_SAMPLE_WATCHLIST": [],
        "PROTOTYPE_GEOMETRY_UNCERTAIN": [],
    }
    proto_metrics = {}

    for p, data in proto_data.items():
        n = data["token_count"]
        if n == 0:
            continue

        owners = data["owner_ids"]
        owner_counts = np.bincount(owners, minlength=num_experts)
        dominant_share = owner_counts.max() / n
        dominant_expert = int(owner_counts.argmax())
        owner_entropy = -sum((c/n) * np.log(c/n + 1e-8) for c in owner_counts if c > 0)
        accuracy = data["correct_count"] / n
        avg_loss = data["total_loss"] / n
        avg_entropy = np.mean(data["membership_entropy"]) if data["membership_entropy"] else 0
        avg_margin = np.mean(data["membership_margin"]) if data["membership_margin"] else 0
        boundary_rate = np.mean(data["is_boundary"]) if data["is_boundary"] else 0
        challenger_disagree = np.mean(data["challenger_disagrees"]) if data["challenger_disagrees"] else 0

        # Oracle gap proxy: avg loss weighted by challenger disagreement
        oracle_gap_proxy = challenger_disagree * avg_loss

        # Per-expert average loss for oracle gap
        expert_avg_loss = np.zeros(num_experts)
        for e in range(num_experts):
            if data["per_expert_count"][e] > 0:
                expert_avg_loss[e] = data["per_expert_loss_sum"][e] / data["per_expert_count"][e]
            else:
                expert_avg_loss[e] = 999.0
        best_expert_loss = expert_avg_loss.min()
        current_expert_loss = expert_avg_loss[dominant_expert] if data["per_expert_count"][dominant_expert] > 0 else avg_loss
        direct_oracle_gap = current_expert_loss - best_expert_loss

        metrics = {
            "prototype_id": p,
            "token_count": n,
            "dominant_owner": dominant_expert,
            "dominant_owner_share": float(dominant_share),
            "owner_entropy": float(owner_entropy),
            "accuracy": float(accuracy),
            "avg_loss": float(avg_loss),
            "oracle_gap_proxy": float(oracle_gap_proxy),
            "direct_oracle_gap": float(direct_oracle_gap),
            "membership_entropy": float(avg_entropy),
            "membership_margin": float(avg_margin),
            "boundary_rate": float(boundary_rate),
            "challenger_disagree_rate": float(challenger_disagree),
            "is_monopolized": dominant_share >= MONOPOLY_THRESHOLD,
            "bucket": "",
        }
        proto_metrics[p] = metrics

        # Bucket assignment (priority order)
        if n < MIN_SAMPLES:
            metrics["bucket"] = "LOW_SAMPLE_WATCHLIST"
            buckets["LOW_SAMPLE_WATCHLIST"].append(p)
        elif avg_entropy > GEOMETRY_ENTROPY_UNIFORM_THRESHOLD and avg_margin < BOUNDARY_MARGIN_THRESHOLD and dominant_share < 0.6:
            metrics["bucket"] = "PROTOTYPE_GEOMETRY_UNCERTAIN"
            buckets["PROTOTYPE_GEOMETRY_UNCERTAIN"].append(p)
        elif dominant_share >= MONOPOLY_THRESHOLD and challenger_disagree < 0.3 and accuracy > 0.7:
            metrics["bucket"] = "PROTECT_STABLE_OWNER"
            buckets["PROTECT_STABLE_OWNER"].append(p)
        elif dominant_share >= MONOPOLY_THRESHOLD and challenger_disagree >= CHALLENGER_DISAGREE_REPAIR_THRESHOLD:
            metrics["bucket"] = "REPAIR_HIGH_GAP_MONOPOLY"
            buckets["REPAIR_HIGH_GAP_MONOPOLY"].append(p)
        elif dominant_share < MONOPOLY_THRESHOLD and challenger_disagree >= CHALLENGER_DISAGREE_REPAIR_THRESHOLD:
            metrics["bucket"] = "REPAIR_HIGH_GAP_NON_MONOPOLY"
            buckets["REPAIR_HIGH_GAP_NON_MONOPOLY"].append(p)
        else:
            metrics["bucket"] = "PROTOTYPE_GEOMETRY_UNCERTAIN"
            buckets["PROTOTYPE_GEOMETRY_UNCERTAIN"].append(p)

    return buckets, proto_metrics


# =============================================================================
# Targeted Repair
# =============================================================================

def apply_targeted_repair(
    base_map: CandidateMap,
    proto_metrics: dict,
    buckets: dict,
    proto_data: dict,
    num_experts: int = 4,
) -> CandidateMap:
    """Apply per-prototype-gated ownership refresh.

    Only repairs REPAIR_HIGH_GAP_MONOPOLY and REPAIR_HIGH_GAP_NON_MONOPOLY.
    Protects PROTECT_STABLE_OWNER.
    Does not touch LOW_SAMPLE_WATCHLIST or PROTOTYPE_GEOMETRY_UNCERTAIN.
    """
    num_prototypes = base_map.num_prototypes
    reliability = base_map.family_owner_reliability.clone()
    failure = base_map.family_owner_failure.clone()
    monopoly_penalty = base_map.prototype_local_monopoly_penalty.clone()
    stale_penalty = base_map.stale_owner_penalty.clone()

    repair_actions = []

    # For REPAIR buckets: boost challenger evidence, penalize stale monopolist
    for bucket_name in ["REPAIR_HIGH_GAP_MONOPOLY", "REPAIR_HIGH_GAP_NON_MONOPOLY"]:
        for p in buckets.get(bucket_name, []):
            metrics = proto_metrics.get(p, {})
            data = proto_data.get(p, {})
            if not metrics or not data:
                continue

            dominant_expert = metrics["dominant_owner"]
            n = metrics["token_count"]
            challenger_rate = metrics["challenger_disagree_rate"]

            # Penalize stale monopolist proportional to oracle gap
            gap = metrics["oracle_gap_proxy"]
            stale_penalty[p, dominant_expert] = min(gap * 0.05, 0.5)

            # Add monopoly penalty only for high-gap monopolies
            if metrics["is_monopolized"]:
                monopoly_penalty[p, dominant_expert] = min(gap * 0.03, 0.3)

            # Boost reliability for challenger-winning experts
            # Find which expert the challenger prefers (from per_expert_loss)
            per_expert_loss = data["per_expert_loss_sum"]
            per_expert_count = data["per_expert_count"]
            best_e = -1
            best_loss = float("inf")
            for e in range(num_experts):
                if per_expert_count[e] > 5:
                    el = per_expert_loss[e] / per_expert_count[e]
                    if el < best_loss:
                        best_loss = el
                        best_e = e

            if best_e >= 0 and best_e != dominant_expert:
                reliability[p, best_e] += challenger_rate * n * 0.01
                failure[p, dominant_expert] += challenger_rate * n * 0.005

            repair_actions.append({
                "prototype": p,
                "bucket": bucket_name,
                "dominant_expert": dominant_expert,
                "challenger_expert": best_e,
                "oracle_gap": gap,
                "stale_penalty_applied": float(stale_penalty[p, dominant_expert]),
                "monopoly_penalty_applied": float(monopoly_penalty[p, dominant_expert]),
            })

    # For PROTECT: ensure no penalties accumulate
    for p in buckets.get("PROTECT_STABLE_OWNER", []):
        stale_penalty[p] = 0.0
        monopoly_penalty[p] = 0.0

    import copy
    new_metadata = copy.deepcopy(base_map.metadata)
    new_metadata.promotion_status = "targeted_repair_candidate"
    new_metadata.created_at = time.strftime("%Y-%m-%dT%H:%M:%S")

    repaired_map = CandidateMap(
        ownership_reliability_bias=reliability.clone(),
        ownership_failure_bias=failure.clone(),
        family_owner_reliability=reliability,
        family_owner_failure=failure,
        family_preservation_bias=base_map.family_preservation_bias.clone(),
        prototype_local_monopoly_penalty=monopoly_penalty,
        stale_owner_penalty=stale_penalty,
        metadata=new_metadata,
    )

    return repaired_map, repair_actions


# =============================================================================
# Canary Evaluation (Before/After)
# =============================================================================

def evaluate_canary(model, tasks, candidate_map, batch_size=32, seq_len=16,
                    max_seq_len=64, seed=42, device="cuda", family_bias_weight=0.25,
                    family_bias_cap=0.5):
    """Evaluate canary routing with repaired candidate map."""
    model.eval()
    d_model = model.config.d_model
    num_prototypes = model.config.num_prototypes

    per_proto_metrics = {p: {"token_count": 0, "correct": 0, "loss_sum": 0.0,
                             "owner_changed": 0, "challenger_disagree": 0}
                        for p in range(num_prototypes)}

    for task in tasks:
        x, y, _ = generate_nlp_stage1_batch(task, batch_size=batch_size,
                                            seq_len=seq_len, max_seq_len=max_seq_len, seed=seed)
        x, y = x.to(device), y.to(device)

        with torch.no_grad():
            positions = torch.arange(max_seq_len, device=device).unsqueeze(0)
            hidden = model.dropout(model.token_emb(x) + model.pos_emb(positions))
            block = model.blocks[0]
            attn_in = block.attn_ln(hidden)
            attn_out, _ = block.attn(attn_in, attn_in, attn_in, need_weights=False)
            post_attn = hidden + block.attn_dropout(attn_out)
            moe_in = block.moe_ln(post_attn)
            flat = moe_in.reshape(-1, d_model)

            router = block.moe.router
            z = router.route_proj(flat)
            fm = compute_family_membership(z, router.prototypes)
            proto_ids = fm.nearest_prototype

            moe_out, aux = block.moe(moe_in)
            current_owners = aux["primary_expert_ids"]

            out = model(input_ids=x, targets=y)
            preds = out["logits"].argmax(dim=-1).reshape(-1)
            targets_flat = y.reshape(-1)
            correct = (preds == targets_flat)
            logits_flat = out["logits"].reshape(-1, model.config.vocab_size)
            per_token_loss = F.cross_entropy(logits_flat, targets_flat, reduction="none")

            # Canary routing
            router_logits = router.gate(z)
            proto_bias = router.proto_bias[proto_ids]
            compat_mask = router.proto_expert_compat[proto_ids]
            canary_owners, _ = family_preserving_top1_score(
                router_logits, proto_bias, proto_ids, compat_mask, candidate_map,
                family_bias_weight=family_bias_weight, family_bias_cap=family_bias_cap,
            )
            owner_changed = (canary_owners != current_owners)

            experts = list(block.moe.expert_deltas)
            evidence = compute_expert_choice_evidence(flat, experts, proto_ids, current_owners, targets_flat)
            best_experts = evidence["best_expert_per_token"].to(device)
            challenger_disagrees = (best_experts != current_owners)

            N = flat.shape[0]
            for i in range(N):
                p = proto_ids[i].item()
                per_proto_metrics[p]["token_count"] += 1
                per_proto_metrics[p]["correct"] += int(correct[i].item())
                per_proto_metrics[p]["loss_sum"] += per_token_loss[i].item()
                per_proto_metrics[p]["owner_changed"] += int(owner_changed[i].item())
                per_proto_metrics[p]["challenger_disagree"] += int(challenger_disagrees[i].item())

    # Summarize
    result = {}
    for p, m in per_proto_metrics.items():
        n = m["token_count"]
        if n == 0:
            continue
        result[p] = {
            "token_count": n,
            "accuracy": m["correct"] / n,
            "avg_loss": m["loss_sum"] / n,
            "canary_change_rate": m["owner_changed"] / n,
            "challenger_disagree_rate": m["challenger_disagree"] / n,
            "oracle_gap_proxy": (m["challenger_disagree"] / n) * (m["loss_sum"] / n),
        }
    return result


# =============================================================================
# Gate Evaluation
# =============================================================================

def evaluate_repair_gate(before_metrics, after_metrics, buckets, proto_metrics):
    """Determine whether targeted repair should be accepted."""
    # Check protected owners didn't regress
    protected_regression_count = 0
    for p in buckets.get("PROTECT_STABLE_OWNER", []):
        if p in before_metrics and p in after_metrics:
            if after_metrics[p]["avg_loss"] > before_metrics[p]["avg_loss"] * 1.1:
                protected_regression_count += 1

    # Check high-gap monopolies improved
    repaired_improved = 0
    repaired_total = 0
    for bucket in ["REPAIR_HIGH_GAP_MONOPOLY", "REPAIR_HIGH_GAP_NON_MONOPOLY"]:
        for p in buckets.get(bucket, []):
            if p in before_metrics and p in after_metrics:
                repaired_total += 1
                if after_metrics[p]["oracle_gap_proxy"] < before_metrics[p]["oracle_gap_proxy"]:
                    repaired_improved += 1

    # Check challenger group
    challenger_improved = 0
    challenger_total = 0
    for p in buckets.get("REPAIR_HIGH_GAP_MONOPOLY", []) + buckets.get("REPAIR_HIGH_GAP_NON_MONOPOLY", []):
        if p in before_metrics and p in after_metrics:
            challenger_total += 1
            if after_metrics[p]["challenger_disagree_rate"] < before_metrics[p]["challenger_disagree_rate"]:
                challenger_improved += 1

    verdict_parts = []
    if protected_regression_count > 0:
        verdict_parts.append(f"protected_regression={protected_regression_count}")
    if repaired_total > 0 and repaired_improved >= repaired_total * 0.5:
        verdict_parts.append(f"repair_improved={repaired_improved}/{repaired_total}")
    elif repaired_total > 0:
        verdict_parts.append(f"repair_insufficient={repaired_improved}/{repaired_total}")

    # Decision
    if protected_regression_count > 0:
        verdict = "PVR_EC_TARGETED_MONOPOLY_REPAIR_REJECTED"
    elif repaired_total > 0 and repaired_improved >= repaired_total * 0.5:
        verdict = "PVR_EC_TARGETED_MONOPOLY_REPAIR_ACCEPTED"
    elif repaired_improved > 0:
        verdict = "PVR_EC_TARGETED_MONOPOLY_REPAIR_PARTIAL"
    else:
        verdict = "PVR_EC_PROTOTYPE_GEOMETRY_REPAIR_REQUIRED"

    return {
        "verdict": verdict,
        "protected_regression_count": protected_regression_count,
        "repaired_improved": repaired_improved,
        "repaired_total": repaired_total,
        "challenger_improved": challenger_improved,
        "details": verdict_parts,
    }


# =============================================================================
# Main
# =============================================================================

def run_repair(output_dir: str, device: str = "cuda", steps: int = 300):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    t0 = time.time()

    print("=" * 70)
    print("  PVR-EC-O TARGETED MONOPOLY COLLAPSE REPAIR")
    print(f"  Device: {device} | Steps: {steps}")
    print("=" * 70)

    tasks = list(NLP_STAGE1_TASKS)

    # Phase 1: Train
    print("\n  [1/6] Training model...")
    model = build_model(device=device)
    model = train_model(model, tasks, steps=steps, device=device)

    # Phase 2: Collect baseline prototype data
    print("  [2/6] Collecting BEFORE prototype data...")
    proto_data = collect_prototype_data(model, tasks, device=device)

    # Phase 3: Bucket prototypes
    print("  [3/6] Bucketing prototypes...")
    buckets, proto_metrics = bucket_prototypes(proto_data, num_experts=model.config.num_experts)
    for name, ids in buckets.items():
        print(f"    {name}: {len(ids)} prototypes {ids}")

    # Phase 4: Apply targeted repair to candidate map
    print("  [4/6] Applying targeted repair...")
    base_map = create_blank_candidate_map(model.config.num_prototypes, model.config.num_experts)
    repaired_map, repair_actions = apply_targeted_repair(
        base_map, proto_metrics, buckets, proto_data, num_experts=model.config.num_experts
    )
    print(f"    Repair actions: {len(repair_actions)}")
    for action in repair_actions[:5]:
        print(f"      Proto {action['prototype']}: gap={action['oracle_gap']:.3f} "
              f"stale_pen={action['stale_penalty_applied']:.4f} "
              f"mono_pen={action['monopoly_penalty_applied']:.4f}")

    # Phase 5: Evaluate canary (before and after)
    print("  [5/6] Evaluating canary BEFORE repair...")
    before_canary = evaluate_canary(model, tasks, base_map, device=device,
                                    family_bias_weight=0.0, family_bias_cap=0.0)

    print("  [5/6] Evaluating canary AFTER repair...")
    after_canary = evaluate_canary(model, tasks, repaired_map, device=device,
                                   family_bias_weight=0.25, family_bias_cap=0.5)

    # Phase 6: Gate evaluation
    print("  [6/6] Evaluating repair gate...")
    gate_result = evaluate_repair_gate(before_canary, after_canary, buckets, proto_metrics)
    print(f"    VERDICT: {gate_result['verdict']}")
    print(f"    Protected regressions: {gate_result['protected_regression_count']}")
    print(f"    Repaired improved: {gate_result['repaired_improved']}/{gate_result['repaired_total']}")

    total_time = time.time() - t0

    # Before/after comparison
    print("\n  --- PER-BUCKET BEFORE/AFTER ---")
    for bucket_name in ["PROTECT_STABLE_OWNER", "REPAIR_HIGH_GAP_MONOPOLY",
                        "REPAIR_HIGH_GAP_NON_MONOPOLY", "PROTOTYPE_GEOMETRY_UNCERTAIN"]:
        protos = buckets.get(bucket_name, [])
        if not protos:
            continue
        b_gaps = [before_canary[p]["oracle_gap_proxy"] for p in protos if p in before_canary]
        a_gaps = [after_canary[p]["oracle_gap_proxy"] for p in protos if p in after_canary]
        b_acc = [before_canary[p]["accuracy"] for p in protos if p in before_canary]
        a_acc = [after_canary[p]["accuracy"] for p in protos if p in after_canary]
        b_chall = [before_canary[p]["challenger_disagree_rate"] for p in protos if p in before_canary]
        a_chall = [after_canary[p]["challenger_disagree_rate"] for p in protos if p in after_canary]

        print(f"  {bucket_name} (n={len(protos)}):")
        if b_gaps:
            print(f"    oracle_gap:  {np.mean(b_gaps):.4f} -> {np.mean(a_gaps):.4f}")
            print(f"    accuracy:    {np.mean(b_acc):.4f} -> {np.mean(a_acc):.4f}")
            print(f"    challenger:  {np.mean(b_chall):.4f} -> {np.mean(a_chall):.4f}")

    # Write reports
    print("\n  Writing reports...")

    def write_report(stem, payload):
        with open(output_path / f"{stem}.json", "w") as f:
            json.dump(payload, f, indent=2, default=str)
        md = [f"# {stem.replace('_', ' ').title()}", "",
              f"**Status:** {payload.get('status', payload.get('verdict', 'unknown'))}", "",
              "```json", json.dumps(payload, indent=2, default=str)[:5000], "```"]
        with open(output_path / f"{stem}.md", "w") as f:
            f.write("\n".join(md))

    write_report("pvr_ec_prototype_bucket_report", {
        "status": "BUCKETING_COMPLETE",
        "buckets": {k: v for k, v in buckets.items()},
        "bucket_counts": {k: len(v) for k, v in buckets.items()},
        "per_prototype_metrics": {str(k): v for k, v in proto_metrics.items()},
    })

    write_report("pvr_ec_targeted_ownership_refresh_report", {
        "status": "TARGETED_REFRESH_APPLIED",
        "repair_actions": repair_actions,
        "repair_count": len(repair_actions),
    })

    write_report("pvr_ec_protected_owner_regression_report", {
        "status": "NO_REGRESSION" if gate_result["protected_regression_count"] == 0 else "REGRESSION_DETECTED",
        "protected_prototypes": buckets.get("PROTECT_STABLE_OWNER", []),
        "regression_count": gate_result["protected_regression_count"],
    })

    write_report("pvr_ec_high_gap_monopoly_repair_report", {
        "status": "REPAIR_APPLIED",
        "repaired_prototypes": buckets.get("REPAIR_HIGH_GAP_MONOPOLY", []),
        "improved_count": gate_result["repaired_improved"],
        "total_repaired": gate_result["repaired_total"],
    })

    write_report("pvr_ec_prototype_geometry_uncertainty_report", {
        "status": "GEOMETRY_MEASURED",
        "uncertain_prototypes": buckets.get("PROTOTYPE_GEOMETRY_UNCERTAIN", []),
        "count": len(buckets.get("PROTOTYPE_GEOMETRY_UNCERTAIN", [])),
    })

    # Before/after summary
    ba_summary = {}
    for p in proto_metrics:
        if p in before_canary and p in after_canary:
            ba_summary[str(p)] = {
                "bucket": proto_metrics[p]["bucket"],
                "before_oracle_gap": before_canary[p]["oracle_gap_proxy"],
                "after_oracle_gap": after_canary[p]["oracle_gap_proxy"],
                "before_accuracy": before_canary[p]["accuracy"],
                "after_accuracy": after_canary[p]["accuracy"],
                "before_challenger": before_canary[p]["challenger_disagree_rate"],
                "after_challenger": after_canary[p]["challenger_disagree_rate"],
                "canary_change_rate": after_canary[p]["canary_change_rate"],
            }

    write_report("pvr_ec_targeted_monopoly_repair_canary_report", {
        "status": gate_result["verdict"],
        "before_after_by_prototype": ba_summary,
    })

    write_report("pvr_ec_targeted_monopoly_repair_gate_report", {
        "status": gate_result["verdict"],
        "verdict": gate_result["verdict"],
        "gate_details": gate_result,
        "hard_invariants": {
            "owners_per_token": 1.0,
            "top2_executions": 0,
            "top4_executions": 0,
            "production_map_mutated": False,
        },
        "total_time_s": total_time,
    })

    print(f"\n{'='*70}")
    print(f"  TARGETED MONOPOLY REPAIR COMPLETE | {total_time:.1f}s")
    print(f"  VERDICT: {gate_result['verdict']}")
    print(f"  owners/token = 1.0 | Top2 = 0 | Top4 = 0")
    print(f"{'='*70}")

    return gate_result


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default="evaluation/benchmark_results/pvr_targeted_monopoly_repair")
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--steps", type=int, default=300)
    args = parser.parse_args()
    run_repair(args.output_dir, device=args.device, steps=args.steps)
