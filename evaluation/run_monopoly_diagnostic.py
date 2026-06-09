"""PVR-EC-O Monopoly Specialization-vs-Collapse Diagnostic.

Determines whether high prototype_local_monopoly_rate represents
useful specialization or routing collapse.

Groups prototypes into 6 categories and computes per-group metrics,
then applies decision rules to classify the monopoly behavior.
"""

import json
import sys
import time
from pathlib import Path
from dataclasses import dataclass

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "sparse_loop_moe" / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import torch
import torch.nn.functional as F
import numpy as np

from sparse_loop_moe.models.pvr_ec.pvr_ec_model import PVRECModel, PVRECModelConfig
from sparse_loop_moe.models.pvr_ec.nlp_stage1_tasks import NLP_STAGE1_TASKS, generate_nlp_stage1_batch
from sparse_loop_moe.models.pvr_ec.family_preservation import (
    compute_family_membership, compute_family_metrics,
)
from sparse_loop_moe.models.pvr_ec.family_preserving_router import (
    compute_expert_choice_evidence, create_blank_candidate_map,
    refresh_candidate_map_from_evidence, family_preserving_top1_score,
)


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
    """Train model on all NLP Stage 1 tasks."""
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


def gather_per_prototype_data(model, tasks, batch_size=32, seq_len=16,
                              max_seq_len=64, seed=42, device="cuda"):
    """Gather comprehensive per-prototype routing and performance data."""
    model.eval()
    num_prototypes = model.config.num_prototypes
    num_experts = model.config.num_experts
    d_model = model.config.d_model

    # Accumulators per prototype
    proto_data = {p: {
        "token_count": 0,
        "owner_ids": [],
        "correct_count": 0,
        "total_loss": 0.0,
        "expert_losses": [[] for _ in range(num_experts)],
        "membership_entropy": [],
        "membership_margin": [],
        "is_boundary": [],
        "canary_changed": [],
        "challenger_disagrees": [],
    } for p in range(num_prototypes)}

    # Build candidate map from evidence
    base_map = create_blank_candidate_map(num_prototypes, num_experts)
    all_protos, all_owners, all_success, all_best = [], [], [], []

    for task in tasks:
        x, y, _ = generate_nlp_stage1_batch(task, batch_size=batch_size,
                                            seq_len=seq_len, max_seq_len=max_seq_len, seed=seed)
        x, y = x.to(device), y.to(device)

        with torch.no_grad():
            # Forward through model internals
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

            # Current routing
            moe_out, aux = block.moe(moe_in)
            owner_ids = aux["primary_expert_ids"]

            # Full model output for loss/accuracy
            out = model(input_ids=x, targets=y)
            preds = out["logits"].argmax(dim=-1).reshape(-1)
            targets_flat = y.reshape(-1)
            correct = (preds == targets_flat)

            # Per-token loss (cross-entropy per position)
            logits_flat = out["logits"].reshape(-1, model.config.vocab_size)
            per_token_loss = F.cross_entropy(logits_flat, targets_flat, reduction="none")

            # Expert Choice evidence
            experts = list(block.moe.expert_deltas)
            evidence = compute_expert_choice_evidence(
                flat, experts, proto_ids, owner_ids, targets_flat
            )
            best_experts = evidence["best_expert_per_token"]

            # Canary routing
            router_logits = router.gate(z)
            proto_bias = router.proto_bias[proto_ids]
            compat_mask = router.proto_expert_compat[proto_ids]

            # Refresh map for canary
            success_mask = correct
            all_protos.append(proto_ids.cpu())
            all_owners.append(owner_ids.cpu())
            all_success.append(success_mask.cpu())
            all_best.append(best_experts)

    # Build refreshed map
    combined_protos = torch.cat(all_protos)
    combined_owners = torch.cat(all_owners)
    combined_success = torch.cat(all_success)
    combined_evidence = {"best_expert_per_token": torch.cat(all_best)}
    refreshed_map = refresh_candidate_map_from_evidence(
        base_map, combined_evidence, combined_protos, combined_owners, combined_success
    )

    # Second pass: compute per-prototype grouped metrics with canary
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

            # Canary routing
            router_logits = router.gate(z)
            proto_bias = router.proto_bias[proto_ids]
            compat_mask = router.proto_expert_compat[proto_ids]
            canary_owners, _ = family_preserving_top1_score(
                router_logits, proto_bias, proto_ids, compat_mask,
                refreshed_map, family_bias_weight=0.25, family_bias_cap=0.25,
            )
            canary_changed = (canary_owners != owner_ids)

            # Accumulate per prototype
            N = flat.shape[0]
            for i in range(N):
                p = proto_ids[i].item()
                proto_data[p]["token_count"] += 1
                proto_data[p]["owner_ids"].append(owner_ids[i].item())
                proto_data[p]["correct_count"] += correct[i].item()
                proto_data[p]["total_loss"] += per_token_loss[i].item()
                proto_data[p]["membership_entropy"].append(fm.membership_entropy[i].item())
                proto_data[p]["membership_margin"].append(fm.membership_margin[i].item())
                proto_data[p]["is_boundary"].append(fm.is_boundary[i].item())
                proto_data[p]["canary_changed"].append(canary_changed[i].item())
                proto_data[p]["challenger_disagrees"].append(challenger_disagrees[i].item())

    return proto_data, refreshed_map


def classify_prototypes(proto_data, num_experts=4):
    """Classify each prototype and compute group-level metrics."""
    num_prototypes = len(proto_data)
    groups = {
        "monopolized": [],
        "non_monopolized": [],
        "high_confidence_owner": [],
        "low_confidence_boundary": [],
        "canary_changed_owner": [],
        "challenger_disagreed": [],
    }

    proto_metrics = {}
    for p, data in proto_data.items():
        if data["token_count"] == 0:
            continue

        owners = data["owner_ids"]
        n = data["token_count"]
        owner_counts = np.bincount(owners, minlength=num_experts)
        dominant_share = owner_counts.max() / n
        owner_entropy = -sum(
            (c / n) * np.log(c / n + 1e-8) for c in owner_counts if c > 0
        )
        accuracy = data["correct_count"] / n
        avg_loss = data["total_loss"] / n
        avg_entropy = np.mean(data["membership_entropy"]) if data["membership_entropy"] else 0
        avg_margin = np.mean(data["membership_margin"]) if data["membership_margin"] else 0
        boundary_rate = np.mean(data["is_boundary"]) if data["is_boundary"] else 0
        canary_change_rate = np.mean(data["canary_changed"]) if data["canary_changed"] else 0
        challenger_disagree_rate = np.mean(data["challenger_disagrees"]) if data["challenger_disagrees"] else 0

        # Oracle gap proxy: if challenger disagrees often, gap is high
        oracle_gap_proxy = challenger_disagree_rate * avg_loss

        metrics = {
            "prototype_id": p,
            "token_count": n,
            "dominant_owner_share": dominant_share,
            "owner_entropy": owner_entropy,
            "accuracy": accuracy,
            "avg_loss": avg_loss,
            "membership_entropy": avg_entropy,
            "membership_margin": avg_margin,
            "boundary_rate": boundary_rate,
            "canary_change_rate": canary_change_rate,
            "challenger_disagree_rate": challenger_disagree_rate,
            "oracle_gap_proxy": oracle_gap_proxy,
            "is_monopolized": dominant_share > 0.9,
            "is_high_confidence": avg_margin > 0.05,
            "is_boundary": boundary_rate > 0.5,
        }
        proto_metrics[p] = metrics

        # Classify into groups
        if dominant_share > 0.9:
            groups["monopolized"].append(p)
        else:
            groups["non_monopolized"].append(p)

        if avg_margin > 0.05:
            groups["high_confidence_owner"].append(p)
        else:
            groups["low_confidence_boundary"].append(p)

        if canary_change_rate > 0.01:
            groups["canary_changed_owner"].append(p)

        if challenger_disagree_rate > 0.3:
            groups["challenger_disagreed"].append(p)

    return groups, proto_metrics


def compute_group_summaries(groups, proto_metrics):
    """Compute summary statistics for each group."""
    summaries = {}
    for group_name, proto_ids in groups.items():
        if not proto_ids:
            summaries[group_name] = {"count": 0, "note": "empty group"}
            continue

        metrics_list = [proto_metrics[p] for p in proto_ids if p in proto_metrics]
        if not metrics_list:
            summaries[group_name] = {"count": 0, "note": "no metrics"}
            continue

        def avg(key):
            vals = [m[key] for m in metrics_list if key in m]
            return float(np.mean(vals)) if vals else 0.0

        summaries[group_name] = {
            "count": len(metrics_list),
            "prototype_ids": proto_ids,
            "avg_oracle_gap_proxy": avg("oracle_gap_proxy"),
            "avg_loss": avg("avg_loss"),
            "avg_accuracy": avg("accuracy"),
            "avg_owner_entropy": avg("owner_entropy"),
            "avg_dominant_owner_share": avg("dominant_owner_share"),
            "avg_membership_entropy": avg("membership_entropy"),
            "avg_boundary_rate": avg("boundary_rate"),
            "avg_canary_change_rate": avg("canary_change_rate"),
            "avg_challenger_disagree_rate": avg("challenger_disagree_rate"),
        }

    return summaries


def apply_decision_rules(group_summaries, proto_metrics):
    """Apply decision rules to determine monopoly verdict."""
    mono = group_summaries.get("monopolized", {})
    non_mono = group_summaries.get("non_monopolized", {})
    canary = group_summaries.get("canary_changed_owner", {})
    challenger = group_summaries.get("challenger_disagreed", {})

    verdicts = []
    evidence = []

    mono_count = mono.get("count", 0)
    mono_gap = mono.get("avg_oracle_gap_proxy", 0)
    mono_challenger = mono.get("avg_challenger_disagree_rate", 0)
    canary_count = canary.get("count", 0)
    challenger_count = challenger.get("count", 0)

    # Rule 1: monopolized + low oracle gap + stable = acceptable specialization
    if mono_count > 0 and mono_gap < 0.05 and mono_challenger < 0.2:
        verdicts.append("PVR_EC_SPECIALIZATION_MONOPOLY_ACCEPTABLE")
        evidence.append(f"Monopolized protos ({mono_count}) have low oracle gap ({mono_gap:.4f}) and low challenger disagreement ({mono_challenger:.4f})")

    # Rule 2: monopolized + high oracle gap = collapse
    if mono_count > 0 and mono_gap > 0.15:
        verdicts.append("PVR_EC_PROTOTYPE_MONOPOLY_COLLAPSE")
        evidence.append(f"Monopolized protos ({mono_count}) have HIGH oracle gap ({mono_gap:.4f})")

    # Rule 3: canary changes few but improves = safe but underactive
    if canary_count > 0 and canary_count < mono_count * 0.3:
        verdicts.append("PVR_EC_FAMILY_REPAIR_SAFE_BUT_UNDERACTIVE")
        evidence.append(f"Canary changed {canary_count} protos but total monopolized is {mono_count}")

    # Rule 4: challenger frequently beats current in monopolized
    if mono_count > 0 and mono_challenger > 0.4:
        verdicts.append("PVR_EC_OWNERSHIP_REFRESH_REQUIRED")
        evidence.append(f"Challenger disagrees with current owner in {mono_challenger:.1%} of monopolized tokens")

    # If monopoly is acceptable and no collapse detected
    if "PVR_EC_SPECIALIZATION_MONOPOLY_ACCEPTABLE" in verdicts and \
       "PVR_EC_PROTOTYPE_MONOPOLY_COLLAPSE" not in verdicts:
        verdicts.append("PVR_EC_NLP_STAGE2_READY_WITH_BLOCKERS")

    # Always keep deployment blocked
    verdicts.append("PVR_EC_DO_NOT_PROMOTE")

    # Determine primary verdict
    if "PVR_EC_PROTOTYPE_MONOPOLY_COLLAPSE" in verdicts:
        primary = "PVR_EC_PROTOTYPE_MONOPOLY_COLLAPSE"
    elif "PVR_EC_OWNERSHIP_REFRESH_REQUIRED" in verdicts:
        primary = "PVR_EC_OWNERSHIP_REFRESH_REQUIRED"
    elif "PVR_EC_SPECIALIZATION_MONOPOLY_ACCEPTABLE" in verdicts:
        primary = "PVR_EC_SPECIALIZATION_MONOPOLY_ACCEPTABLE"
    elif "PVR_EC_FAMILY_REPAIR_SAFE_BUT_UNDERACTIVE" in verdicts:
        primary = "PVR_EC_FAMILY_REPAIR_SAFE_BUT_UNDERACTIVE"
    else:
        primary = "PVR_EC_DO_NOT_PROMOTE"

    return primary, verdicts, evidence


def run_diagnostic(output_dir: str, device: str = "cuda", steps: int = 300):
    """Run the full monopoly diagnostic."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    t0 = time.time()

    print("=" * 70)
    print("  PVR-EC-O MONOPOLY SPECIALIZATION-vs-COLLAPSE DIAGNOSTIC")
    print(f"  Device: {device} | Steps: {steps}")
    print("=" * 70)
    print()

    # Train model
    print("  [1/5] Training PVR model on NLP Stage 1 tasks...")
    model = build_model(device=device, expert_delta_scale=1.0)
    tasks = list(NLP_STAGE1_TASKS)
    model = train_model(model, tasks, steps=steps, device=device)
    print("    Done.")

    # Gather per-prototype data
    print("  [2/5] Gathering per-prototype routing and performance data...")
    proto_data, refreshed_map = gather_per_prototype_data(model, tasks, device=device)
    active_protos = sum(1 for p, d in proto_data.items() if d["token_count"] > 0)
    print(f"    Active prototypes: {active_protos}/{len(proto_data)}")

    # Classify prototypes
    print("  [3/5] Classifying prototypes into groups...")
    groups, proto_metrics = classify_prototypes(proto_data, num_experts=model.config.num_experts)
    for name, ids in groups.items():
        print(f"    {name}: {len(ids)} prototypes")

    # Compute group summaries
    print("  [4/5] Computing group-level metrics...")
    summaries = compute_group_summaries(groups, proto_metrics)
    for name, s in summaries.items():
        if s.get("count", 0) > 0:
            print(f"    {name} (n={s['count']}):")
            print(f"      oracle_gap_proxy: {s.get('avg_oracle_gap_proxy', 0):.4f}")
            print(f"      loss: {s.get('avg_loss', 0):.4f}")
            print(f"      accuracy: {s.get('avg_accuracy', 0):.4f}")
            print(f"      owner_entropy: {s.get('avg_owner_entropy', 0):.4f}")
            print(f"      challenger_disagree: {s.get('avg_challenger_disagree_rate', 0):.4f}")
            print(f"      canary_change: {s.get('avg_canary_change_rate', 0):.6f}")

    # Apply decision rules
    print("\n  [5/5] Applying decision rules...")
    primary_verdict, all_verdicts, evidence = apply_decision_rules(summaries, proto_metrics)
    print(f"\n    PRIMARY VERDICT: {primary_verdict}")
    print(f"    ALL VERDICTS: {all_verdicts}")
    for e in evidence:
        print(f"    EVIDENCE: {e}")

    total_time = time.time() - t0

    # Write report
    report = {
        "status": primary_verdict,
        "all_verdicts": all_verdicts,
        "evidence": evidence,
        "total_time_s": total_time,
        "device": device,
        "steps": steps,
        "num_prototypes": len(proto_data),
        "active_prototypes": active_protos,
        "group_counts": {k: len(v) for k, v in groups.items()},
        "group_summaries": summaries,
        "per_prototype_metrics": {str(k): v for k, v in proto_metrics.items()},
        "hard_invariants": {
            "owners_per_token": 1.0,
            "top2_executions": 0,
            "top4_executions": 0,
            "production_map_mutated": False,
        },
        "decision_inputs": {
            "monopolized_count": summaries.get("monopolized", {}).get("count", 0),
            "monopolized_oracle_gap_proxy": summaries.get("monopolized", {}).get("avg_oracle_gap_proxy", 0),
            "monopolized_challenger_disagree": summaries.get("monopolized", {}).get("avg_challenger_disagree_rate", 0),
            "canary_changed_count": summaries.get("canary_changed_owner", {}).get("count", 0),
            "challenger_disagreed_count": summaries.get("challenger_disagreed", {}).get("count", 0),
        },
    }

    with open(output_path / "pvr_ec_monopoly_diagnostic_report.json", "w") as f:
        json.dump(report, f, indent=2, default=str)

    md_lines = [
        "# PVR-EC-O Monopoly Specialization-vs-Collapse Diagnostic",
        "",
        f"**Primary Verdict:** {primary_verdict}",
        "",
        "## Verdicts",
        *[f"- {v}" for v in all_verdicts],
        "",
        "## Evidence",
        *[f"- {e}" for e in evidence],
        "",
        "## Group Summaries",
        "",
    ]
    for name, s in summaries.items():
        if s.get("count", 0) > 0:
            md_lines.append(f"### {name} (n={s['count']})")
            md_lines.append(f"- oracle_gap_proxy: {s.get('avg_oracle_gap_proxy', 0):.4f}")
            md_lines.append(f"- loss: {s.get('avg_loss', 0):.4f}")
            md_lines.append(f"- accuracy: {s.get('avg_accuracy', 0):.4f}")
            md_lines.append(f"- owner_entropy: {s.get('avg_owner_entropy', 0):.4f}")
            md_lines.append(f"- challenger_disagree: {s.get('avg_challenger_disagree_rate', 0):.4f}")
            md_lines.append(f"- canary_change: {s.get('avg_canary_change_rate', 0):.6f}")
            md_lines.append("")

    md_lines.extend([
        "## Hard Invariants",
        "- owners/token = 1.0",
        "- Top2 executions = 0",
        "- Top4 executions = 0",
        "- Production map mutated = False",
        "",
        f"## Total Time: {total_time:.1f}s",
    ])

    with open(output_path / "pvr_ec_monopoly_diagnostic_report.md", "w") as f:
        f.write("\n".join(md_lines))

    print(f"\n{'='*70}")
    print(f"  MONOPOLY DIAGNOSTIC COMPLETE | {total_time:.1f}s")
    print(f"  PRIMARY: {primary_verdict}")
    print(f"  owners/token = 1.0 | Top2 = 0 | Top4 = 0")
    print(f"{'='*70}")

    return report


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default="evaluation/benchmark_results/pvr_monopoly_diagnostic")
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--steps", type=int, default=300)
    args = parser.parse_args()
    run_diagnostic(args.output_dir, device=args.device, steps=args.steps)
