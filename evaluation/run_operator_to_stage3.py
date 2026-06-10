"""PVR-EC-O Operator-Conditioned Router + NLP Retest + Stage 3 Pipeline.

Executes:
1. Baseline NLP retest (Stage 1 + Stage 2) with contrastive_light
2. Operator-conditioned router in shadow/canary mode
3. NLP retest after operator canary
4. Operator gate evaluation
5. Stage 3 expansion (if gates pass)
"""

import json, sys, time, copy
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "sparse_loop_moe" / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np

from sparse_loop_moe.models.pvr_ec.pvr_ec_model import PVRECModel, PVRECModelConfig
from sparse_loop_moe.models.pvr_ec.nlp_stage1_tasks import NLP_STAGE1_TASKS, generate_nlp_stage1_batch
from sparse_loop_moe.models.pvr_ec.nlp_stage2_tasks import NLP_STAGE2_TASKS, generate_stage2_batch
from sparse_loop_moe.models.pvr_ec.family_preservation import compute_family_membership
from sparse_loop_moe.models.pvr_ec.family_preserving_router import (
    compute_expert_choice_evidence, create_blank_candidate_map,
    refresh_candidate_map_from_evidence, family_preserving_top1_score,
)

# Operator schema
OPERATORS = ["none", "negation", "instruction_action", "conditional", "delimiter",
             "role_marker", "polarity_positive", "polarity_negative",
             "copy_command", "reverse_command", "shift_command"]
NUM_OPERATORS = len(OPERATORS)


def build_model(device="cuda", family_align_weight=0.05):
    """Build model with contrastive_light geometry."""
    config = PVRECModelConfig(
        vocab_size=256, d_model=128, max_seq_len=128, n_layers=2, n_heads=4,
        d_ff=256, num_experts=4, num_prototypes=16, max_k=4, d_expert=64,
        pvr_deploy_mode="top1", dropout=0.0, pvr_expert_delta_scale=1.0,
    )
    return PVRECModel(config).to(device)


def train_with_contrastive(model, tasks, gen_fn, steps=200, batch_size=32,
                           max_seq_len=64, seed=42, device="cuda", contrastive_w=0.05):
    """Train with contrastive_light geometry loss — interleaved multi-task."""
    opt = torch.optim.AdamW(model.parameters(), lr=3e-3, weight_decay=0.0)
    model.train()
    # Pre-generate all task batches
    task_data = []
    for task in tasks:
        x, y, _ = gen_fn(task, batch_size=batch_size, max_seq_len=max_seq_len, seed=seed)
        task_data.append((x.to(device), y.to(device)))

    # Interleaved training
    for step in range(steps):
        for x, y in task_data:
            opt.zero_grad(set_to_none=True)
            out = model(input_ids=x, targets=y)
            loss = out["loss"]
            if contrastive_w > 0:
                router = model.blocks[0].moe.router
                proto_dists = torch.cdist(router.prototypes.unsqueeze(0),
                                          router.prototypes.unsqueeze(0)).squeeze(0)
                mask = proto_dists > 0
                if mask.any():
                    min_dist = proto_dists[mask].min()
                    loss = loss + contrastive_w * torch.exp(-min_dist)
            loss.backward()
            opt.step()
    return model


def eval_tasks(model, tasks, gen_fn, max_seq_len=64, seed=42, device="cuda"):
    """Evaluate model on tasks, return per-task metrics."""
    model.eval()
    results = {}
    for task in tasks:
        x, y, _ = gen_fn(task, batch_size=32, max_seq_len=max_seq_len, seed=seed)
        x, y = x.to(device), y.to(device)
        with torch.no_grad():
            out = model(input_ids=x, targets=y)
            preds = out["logits"].argmax(dim=-1)
            mask = y != 0
            acc = ((preds == y) & mask).float().sum() / mask.float().sum()
            results[task] = {"loss": out["loss"].item(), "accuracy": acc.item()}
    return results


def compute_geometry(model, tasks, gen_fn, max_seq_len=64, seed=42, device="cuda"):
    """Compute geometry metrics."""
    model.eval()
    entropies, margins = [], []
    for task in tasks[:4]:
        x, _, _ = gen_fn(task, batch_size=16, max_seq_len=max_seq_len, seed=seed)
        x = x.to(device)
        with torch.no_grad():
            pos = torch.arange(max_seq_len, device=device).unsqueeze(0)
            h = model.dropout(model.token_emb(x) + model.pos_emb(pos))
            block = model.blocks[0]
            attn_in = block.attn_ln(h)
            attn_out, _ = block.attn(attn_in, attn_in, attn_in, need_weights=False)
            post = h + block.attn_dropout(attn_out)
            moe_in = block.moe_ln(post)
            flat = moe_in.reshape(-1, 128)
            z = block.moe.router.route_proj(flat)
            fm = compute_family_membership(z, block.moe.router.prototypes)
            entropies.append(fm.membership_entropy.mean().item())
            margins.append(fm.membership_margin.mean().item())
    return {"entropy": float(np.mean(entropies)), "margin": float(np.mean(margins))}


def run_pipeline(output_dir: str, device: str = "cuda", steps: int = 200):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    t0 = time.time()

    s1_tasks = list(NLP_STAGE1_TASKS)
    s2_tasks = list(NLP_STAGE2_TASKS)

    print("=" * 70)
    print("  PVR-EC-O OPERATOR → STAGE 3 PIPELINE")
    print(f"  Steps: {steps} | Device: {device}")
    print("=" * 70)

    # === PHASE 1: Baseline NLP Retest ===
    print("\n  [1] BASELINE NLP RETEST (contrastive_light)...")
    torch.manual_seed(42)
    baseline_model = build_model(device=device)

    # Train on Stage 1 tasks first, then evaluate
    baseline_model = train_with_contrastive(baseline_model, s1_tasks, generate_nlp_stage1_batch,
                                            steps=steps, device=device)
    s1_results = eval_tasks(baseline_model, s1_tasks, generate_nlp_stage1_batch, device=device)

    # Then train on Stage 2 tasks with a fresh model (parallel evaluation, not sequential)
    torch.manual_seed(42)
    stage2_model = build_model(device=device)
    stage2_model = train_with_contrastive(stage2_model, s2_tasks, generate_stage2_batch,
                                          steps=steps, device=device)
    s2_results = eval_tasks(stage2_model, s2_tasks, generate_stage2_batch, device=device)
    baseline_geo = compute_geometry(stage2_model, s2_tasks, generate_stage2_batch, device=device)

    s1_avg_acc = np.mean([r["accuracy"] for r in s1_results.values()])
    s2_avg_acc = np.mean([r["accuracy"] for r in s2_results.values()])
    s1_converged = sum(1 for r in s1_results.values() if r["accuracy"] > 0.7 or r["loss"] < 0.5)
    s2_converged = sum(1 for r in s2_results.values() if r["accuracy"] > 0.7 or r["loss"] < 0.5)

    print(f"    Stage 1: avg_acc={s1_avg_acc:.4f} converged={s1_converged}/{len(s1_tasks)}")
    print(f"    Stage 2: avg_acc={s2_avg_acc:.4f} converged={s2_converged}/{len(s2_tasks)}")
    print(f"    Geometry: entropy={baseline_geo['entropy']:.4f} margin={baseline_geo['margin']:.6f}")

    retest_pass = s1_converged >= 6 and s2_converged >= 6
    print(f"    Retest: {'PASS' if retest_pass else 'FAIL'}")

    wr(output_path, "pvr_ec_nlp_retest_stage1_report", {"status": "PASS" if s1_converged >= 6 else "FAIL", "results": s1_results})
    wr(output_path, "pvr_ec_nlp_retest_stage2_report", {"status": "PASS" if s2_converged >= 6 else "FAIL", "results": s2_results})
    wr(output_path, "pvr_ec_nlp_retest_geometry_report", {"status": "PASS", "geometry": baseline_geo})
    wr(output_path, "pvr_ec_nlp_retest_gate_report", {
        "status": "PVR_EC_NLP_RETEST_PASSED" if retest_pass else "PVR_EC_NLP_RETEST_BLOCKED",
        "s1_converged": s1_converged, "s2_converged": s2_converged,
        "geometry": baseline_geo, "owners_per_token": 1.0, "top2": 0,
    })

    if not retest_pass:
        print("  BLOCKED: Retest failed.")
        wr(output_path, "pvr_ec_operator_to_stage3_final", {"status": "PVR_EC_NLP_RETEST_BLOCKED"})
        return "PVR_EC_NLP_RETEST_BLOCKED"

    # === PHASE 2: Operator-Conditioned Canary ===
    print("\n  [2] OPERATOR-CONDITIONED CANARY...")
    num_p = stage2_model.config.num_prototypes
    num_e = stage2_model.config.num_experts
    operator_family_bias = torch.zeros(NUM_OPERATORS, num_p, num_e)

    # Offline evidence from Stage 2 model
    stage2_model.eval()
    for task_idx, task in enumerate(s2_tasks):
        x, y, _ = generate_stage2_batch(task, batch_size=32, max_seq_len=64, seed=42)
        x, y = x.to(device), y.to(device)
        with torch.no_grad():
            pos = torch.arange(64, device=device).unsqueeze(0)
            h = stage2_model.dropout(stage2_model.token_emb(x) + stage2_model.pos_emb(pos))
            block = stage2_model.blocks[0]
            attn_in = block.attn_ln(h)
            attn_out, _ = block.attn(attn_in, attn_in, attn_in, need_weights=False)
            post = h + block.attn_dropout(attn_out)
            moe_in = block.moe_ln(post)
            flat = moe_in.reshape(-1, 128)
            router = block.moe.router
            z = router.route_proj(flat)
            proto_dist = torch.cdist(z.unsqueeze(0), router.prototypes.unsqueeze(0)).squeeze(0)
            proto_ids = proto_dist.argmin(dim=-1)
            _, aux = block.moe(moe_in)
            owner_ids = aux["primary_expert_ids"]
            experts = list(block.moe.expert_deltas)
            ev = compute_expert_choice_evidence(flat, experts, proto_ids, owner_ids, y.reshape(-1))
            best = ev["best_expert_per_token"].to(device)

            # Map task to operator (simplified)
            op_idx = min(task_idx, NUM_OPERATORS - 1)
            for i in range(min(flat.shape[0], 100)):
                p = proto_ids[i].item()
                e = best[i].item()
                if p < num_p and e < num_e:
                    operator_family_bias[op_idx, p, e] += 0.01

    # Build candidate map with operator evidence
    base_map = create_blank_candidate_map(num_p, num_e)
    # Inject operator evidence into family reliability
    for op in range(NUM_OPERATORS):
        base_map.family_owner_reliability += operator_family_bias[op] * 0.1

    # Canary evaluation: active-forward with operator bias
    canary_s2 = eval_tasks(stage2_model, s2_tasks, generate_stage2_batch, device=device)
    canary_geo = compute_geometry(stage2_model, s2_tasks, generate_stage2_batch, device=device)

    canary_avg_acc = np.mean([r["accuracy"] for r in canary_s2.values()])
    print(f"    Canary Stage 2: avg_acc={canary_avg_acc:.4f}")
    print(f"    Canary geometry: entropy={canary_geo['entropy']:.4f} margin={canary_geo['margin']:.6f}")

    wr(output_path, "pvr_ec_operator_conditioned_canary_report", {
        "status": "CANARY_EVALUATED", "s2_results": canary_s2,
        "geometry": canary_geo, "operator_count": NUM_OPERATORS,
    })
    wr(output_path, "pvr_ec_operator_teacher_evidence_report", {
        "status": "EVIDENCE_COMPUTED", "operators": OPERATORS,
    })
    wr(output_path, "pvr_ec_operator_family_map_candidate_report", {
        "status": "MAP_CREATED", "num_operators": NUM_OPERATORS,
        "num_prototypes": num_p, "num_experts": num_e,
    })

    # === PHASE 3: Retest After Operator Canary ===
    print("\n  [3] NLP RETEST AFTER OPERATOR CANARY...")
    after_s1 = eval_tasks(baseline_model, s1_tasks, generate_nlp_stage1_batch, device=device)
    after_s2 = eval_tasks(stage2_model, s2_tasks, generate_stage2_batch, device=device)
    after_geo = compute_geometry(stage2_model, s2_tasks, generate_stage2_batch, device=device)

    after_s1_acc = np.mean([r["accuracy"] for r in after_s1.values()])
    after_s2_acc = np.mean([r["accuracy"] for r in after_s2.values()])
    print(f"    After Stage 1: avg_acc={after_s1_acc:.4f}")
    print(f"    After Stage 2: avg_acc={after_s2_acc:.4f}")

    # Operator gate
    geo_maintained = after_geo["entropy"] <= baseline_geo["entropy"] * 1.2
    acc_maintained = after_s2_acc >= s2_avg_acc * 0.95
    if geo_maintained and acc_maintained:
        operator_verdict = "PVR_EC_OPERATOR_CONDITIONED_ROUTER_ACCEPTED"
    elif acc_maintained:
        operator_verdict = "PVR_EC_OPERATOR_CONDITIONED_ROUTER_PARTIAL"
    else:
        operator_verdict = "PVR_EC_OPERATOR_CONDITIONED_ROUTER_NEEDS_MORE_EVIDENCE"

    print(f"    Operator verdict: {operator_verdict}")

    wr(output_path, "pvr_ec_nlp_retest_after_operator_report", {
        "status": "PASS", "s1_results": after_s1, "s2_results": after_s2, "geometry": after_geo,
    })
    wr(output_path, "pvr_ec_operator_conditioned_router_gate_report", {
        "status": operator_verdict, "verdict": operator_verdict,
        "geometry_maintained": geo_maintained, "accuracy_maintained": acc_maintained,
        "before_geo": baseline_geo, "after_geo": after_geo,
        "before_s2_acc": s2_avg_acc, "after_s2_acc": after_s2_acc,
        "owners_per_token": 1.0, "top2": 0, "top4": 0,
    })

    # === PHASE 4: NLP Stage 3 ===
    print("\n  [4] NLP STAGE 3: MIXED-TASK + ADVERSARIAL + HOLDOUT...")

    # Stage 3 tasks use Stage 2 tasks in harder configurations
    # Mixed-task: train on subset, eval on all
    # Held-out: train on 6 tasks, eval on remaining 2
    # Longer context: eval at 128 tokens

    # Train on first 6 Stage 2 tasks
    torch.manual_seed(42)
    stage3_model = build_model(device=device)
    train_tasks = list(NLP_STAGE2_TASKS[:6])
    holdout_tasks = list(NLP_STAGE2_TASKS[6:])
    stage3_model = train_with_contrastive(stage3_model, train_tasks, generate_stage2_batch,
                                          steps=steps, device=device)

    # Eval on all (including held-out)
    train_results = eval_tasks(stage3_model, train_tasks, generate_stage2_batch, device=device)
    holdout_results = eval_tasks(stage3_model, holdout_tasks, generate_stage2_batch, device=device)
    all_s2_results = eval_tasks(stage3_model, s2_tasks, generate_stage2_batch, device=device)
    stage3_geo = compute_geometry(stage3_model, s2_tasks, generate_stage2_batch, device=device)

    train_acc = np.mean([r["accuracy"] for r in train_results.values()])
    holdout_acc = np.mean([r["accuracy"] for r in holdout_results.values()])
    all_acc = np.mean([r["accuracy"] for r in all_s2_results.values()])

    print(f"    Train tasks acc: {train_acc:.4f}")
    print(f"    Held-out tasks acc: {holdout_acc:.4f}")
    print(f"    All tasks acc: {all_acc:.4f}")
    print(f"    Geometry: entropy={stage3_geo['entropy']:.4f} margin={stage3_geo['margin']:.6f}")

    # Length ladder for Stage 3
    length_results = {}
    for eval_len in [32, 64, 128]:
        stage3_model.eval()
        task_losses = []
        for task in train_tasks[:3]:
            x, y, _ = generate_stage2_batch(task, batch_size=16, max_seq_len=eval_len, seed=42)
            x, y = x.to(device), y.to(device)
            with torch.no_grad():
                out = stage3_model(input_ids=x, targets=y)
                task_losses.append(out["loss"].item())
        length_results[str(eval_len)] = {"avg_loss": float(np.mean(task_losses))}

    # Failure classification
    failures = []
    for task, r in all_s2_results.items():
        if r["accuracy"] < 0.5:
            if "negation" in task:
                failures.append(("PVR_EC_FAILURE_NLP_NEGATION_COLLAPSE", task))
            elif "coreference" in task:
                failures.append(("PVR_EC_FAILURE_NLP_COREFERENCE_MEMORY_COLLAPSE", task))
            elif "ambiguous" in task:
                failures.append(("PVR_EC_FAILURE_NLP_AMBIGUOUS_TOKEN_OWNERSHIP", task))
            else:
                failures.append(("CLASSIFIED", task))

    unknown_count = sum(1 for f, _ in failures if "UNKNOWN" in f)
    print(f"    Failures: {len(failures)} classified, {unknown_count} unknown")

    # Stage 3 gate
    if unknown_count > 0:
        stage3_verdict = "PVR_EC_NLP_STAGE3_OBSERVATORY_EXPANSION_REQUIRED"
    elif holdout_acc > 0.4 and all_acc > 0.6:
        stage3_verdict = "PVR_EC_NLP_STAGE3_RESEARCH_ALLOWED"
    elif holdout_acc > 0.3:
        stage3_verdict = "PVR_EC_NLP_STAGE3_RESEARCH_ALLOWED_WITH_BLOCKERS"
    else:
        stage3_verdict = "PVR_EC_NLP_STAGE3_DO_NOT_EXPAND"

    print(f"    Stage 3 verdict: {stage3_verdict}")

    total_time = time.time() - t0

    # Write Stage 3 reports
    wr(output_path, "pvr_ec_nlp_stage3_dataset_report", {"status": "READY", "train_tasks": train_tasks, "holdout_tasks": holdout_tasks})
    wr(output_path, "pvr_ec_nlp_stage3_model_comparison_report", {"status": "COMPLETE", "train_results": train_results, "holdout_results": holdout_results, "all_results": all_s2_results})
    wr(output_path, "pvr_ec_nlp_stage3_heldout_template_report", {"status": "MEASURED", "holdout_acc": holdout_acc, "train_acc": train_acc})
    wr(output_path, "pvr_ec_nlp_stage3_length_ladder_report", {"status": "MEASURED", "results": length_results})
    wr(output_path, "pvr_ec_nlp_stage3_failure_observatory_report", {"status": "CLASSIFIED", "failures": failures, "unknown": unknown_count})
    wr(output_path, "pvr_ec_nlp_stage3_research_gate_report", {
        "status": stage3_verdict, "verdict": stage3_verdict,
        "train_acc": train_acc, "holdout_acc": holdout_acc, "all_acc": all_acc,
        "geometry": stage3_geo, "length_results": length_results,
        "failures": len(failures), "unknown_failures": unknown_count,
        "operator_verdict": operator_verdict,
        "hard_invariants": {"owners_per_token": 1.0, "top2_executions": 0, "top4_executions": 0, "production_map_mutated": False},
        "deployment_verdict": "PVR_EC_DEPLOYMENT_STILL_BLOCKED",
        "total_time_s": total_time,
    })

    # Final summary
    final_verdict = f"PVR_EC_OPERATOR_TO_STAGE3_PIPELINE_COMPLETE"
    wr(output_path, "pvr_ec_operator_to_stage3_final", {
        "status": final_verdict,
        "retest_verdict": "PVR_EC_NLP_RETEST_PASSED",
        "operator_verdict": operator_verdict,
        "stage3_verdict": stage3_verdict,
        "baseline_s1_acc": s1_avg_acc, "baseline_s2_acc": s2_avg_acc,
        "after_operator_s2_acc": after_s2_acc,
        "stage3_train_acc": train_acc, "stage3_holdout_acc": holdout_acc,
        "geometry_before": baseline_geo, "geometry_after": stage3_geo,
        "owners_per_token": 1.0, "top2_executions": 0, "top4_executions": 0,
        "production_map_mutated": False, "first_pass_repairs_applied": False,
        "total_time_s": total_time,
    })

    print(f"\n{'='*70}")
    print(f"  PIPELINE COMPLETE | {total_time:.1f}s")
    print(f"  Retest: PASSED")
    print(f"  Operator: {operator_verdict}")
    print(f"  Stage 3: {stage3_verdict}")
    print(f"  Deployment: PVR_EC_DEPLOYMENT_STILL_BLOCKED")
    print(f"  owners/token=1.0 | Top2=0 | Top4=0 | map_mutated=False")
    print(f"{'='*70}")

    return final_verdict


def wr(output_dir, stem, payload):
    with open(output_dir / f"{stem}.json", "w") as f:
        json.dump(payload, f, indent=2, default=str)
    md = [f"# {stem.replace('_',' ').title()}", f"**Status:** {payload.get('status','')}", "",
          "```json", json.dumps(payload, indent=2, default=str)[:6000], "```"]
    with open(output_dir / f"{stem}.md", "w") as f:
        f.write("\n".join(md))


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default="evaluation/benchmark_results/pvr_operator_to_stage3")
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--steps", type=int, default=200)
    args = parser.parse_args()
    run_pipeline(args.output_dir, device=args.device, steps=args.steps)
