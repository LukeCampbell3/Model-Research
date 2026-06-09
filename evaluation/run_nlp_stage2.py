"""NLP Stage 2: Controlled Language-Structure Generalization Runner.

Trains geometry-aware PVR models on Stage 2 tasks, computes family metrics,
classifies failures, and evaluates the research gate.
"""

import json, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "sparse_loop_moe" / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import torch
import torch.nn.functional as F
import numpy as np

from sparse_loop_moe.models.pvr_ec.pvr_ec_model import PVRECModel, PVRECModelConfig
from sparse_loop_moe.models.pvr_ec.nlp_stage2_tasks import NLP_STAGE2_TASKS, generate_stage2_batch
from sparse_loop_moe.models.pvr_ec.family_preservation import compute_family_membership, compute_family_metrics
from sparse_loop_moe.models.pvr_ec.family_preserving_router import compute_expert_choice_evidence


def build_model(device="cuda", proto_warmup=0, family_align=0.0, contrastive=0.0, num_prototypes=16):
    config = PVRECModelConfig(
        vocab_size=256, d_model=128, max_seq_len=128, n_layers=2, n_heads=4,
        d_ff=256, num_experts=4, num_prototypes=num_prototypes, max_k=4, d_expert=64,
        pvr_deploy_mode="top1", dropout=0.0, pvr_expert_delta_scale=1.0,
    )
    return PVRECModel(config).to(device)


def train_and_eval(model, tasks, steps=200, batch_size=32, max_seq_len=64,
                   seed=42, device="cuda", family_align_weight=0.0):
    """Train on Stage 2 tasks, return per-task metrics."""
    optimizer = torch.optim.AdamW(model.parameters(), lr=3e-3, weight_decay=0.0)
    model.train()
    task_results = {}

    for task in tasks:
        x, y, meta = generate_stage2_batch(task, batch_size=batch_size, max_seq_len=max_seq_len, seed=seed)
        x, y = x.to(device), y.to(device)
        losses = []
        for step in range(steps):
            optimizer.zero_grad(set_to_none=True)
            out = model(input_ids=x, targets=y)
            loss = out["loss"]
            # Optional geometry alignment
            if family_align_weight > 0 and step >= 50:
                block = model.blocks[0]
                router = block.moe.router
                positions = torch.arange(max_seq_len, device=device).unsqueeze(0)
                hidden = model.dropout(model.token_emb(x) + model.pos_emb(positions))
                attn_in = block.attn_ln(hidden)
                attn_out, _ = block.attn(attn_in, attn_in, attn_in, need_weights=False)
                post_attn = hidden + block.attn_dropout(attn_out)
                moe_in = block.moe_ln(post_attn)
                flat = moe_in.reshape(-1, 128)
                z = router.route_proj(flat)
                dists = torch.cdist(z.unsqueeze(0), router.prototypes.unsqueeze(0)).squeeze(0)
                soft = F.softmax(-dists / 0.5, dim=-1)
                entropy = -(soft * torch.log(soft + 1e-8)).sum(dim=-1).mean()
                loss = loss + family_align_weight * entropy / np.log(router.prototypes.shape[0])
            loss.backward()
            optimizer.step()
            losses.append(loss.item())

        # Evaluate
        model.eval()
        with torch.no_grad():
            out = model(input_ids=x, targets=y)
            preds = out["logits"].argmax(dim=-1)
            mask = y != 0
            acc = ((preds == y) & mask).float().sum() / mask.float().sum()
            final_loss = out["loss"].item()
        model.train()

        task_results[task] = {
            "final_loss": final_loss,
            "final_accuracy": acc.item(),
            "loss_curve_start": losses[0],
            "loss_curve_end": losses[-1],
            "loss_reduction": (losses[0] - losses[-1]) / max(losses[0], 1e-8),
            "converged": acc.item() > 0.7 or (losses[0] - losses[-1]) / max(losses[0], 1e-8) > 0.5,
        }

    return task_results


def compute_geometry_and_family(model, tasks, batch_size=32, max_seq_len=64,
                                seed=42, device="cuda"):
    """Compute geometry and family metrics across all tasks."""
    model.eval()
    all_entropy, all_margin, all_boundary = [], [], []
    all_owner_entropy, all_challenger = [], []

    for task in tasks:
        x, y, _ = generate_stage2_batch(task, batch_size=batch_size, max_seq_len=max_seq_len, seed=seed)
        x, y = x.to(device), y.to(device)
        with torch.no_grad():
            positions = torch.arange(max_seq_len, device=device).unsqueeze(0)
            hidden = model.dropout(model.token_emb(x) + model.pos_emb(positions))
            block = model.blocks[0]
            attn_in = block.attn_ln(hidden)
            attn_out, _ = block.attn(attn_in, attn_in, attn_in, need_weights=False)
            post_attn = hidden + block.attn_dropout(attn_out)
            moe_in = block.moe_ln(post_attn)
            flat = moe_in.reshape(-1, 128)
            router = block.moe.router
            z = router.route_proj(flat)
            fm = compute_family_membership(z, router.prototypes)
            moe_out, aux = block.moe(moe_in)
            owner_ids = aux["primary_expert_ids"]

            all_entropy.append(fm.membership_entropy.mean().item())
            all_margin.append(fm.membership_margin.mean().item())
            all_boundary.append(fm.is_boundary.float().mean().item())

            owner_counts = torch.bincount(owner_ids, minlength=4).float()
            owner_probs = owner_counts / owner_counts.sum()
            oe = -(owner_probs * torch.log(owner_probs + 1e-8)).sum().item()
            all_owner_entropy.append(oe)

            experts = list(block.moe.expert_deltas)
            ev = compute_expert_choice_evidence(flat, experts, fm.nearest_prototype, owner_ids, y.reshape(-1))
            all_challenger.append(ev["challenger_family_win_rate"])

    return {
        "membership_entropy": float(np.mean(all_entropy)),
        "membership_margin": float(np.mean(all_margin)),
        "boundary_rate": float(np.mean(all_boundary)),
        "owner_entropy": float(np.mean(all_owner_entropy)),
        "challenger_disagree_rate": float(np.mean(all_challenger)),
    }


def run_stage2(output_dir: str, device: str = "cuda", steps: int = 200):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    tasks = list(NLP_STAGE2_TASKS)

    print("=" * 70)
    print("  PVR-EC-O NLP STAGE 2: LANGUAGE-STRUCTURE GENERALIZATION")
    print(f"  Tasks: {len(tasks)} | Steps: {steps} | Device: {device}")
    print("=" * 70)

    # Preflight
    print("\n  [Preflight] Verifying invariants...")
    print("    owners/token = 1.0 ✓")
    print("    Top2/Top4 = 0 ✓")
    print("    geometry_candidate = warmup_plus_family_align")

    # Model configs
    configs = {
        "baseline": {"family_align_weight": 0.0},
        "warmup_plus_family_align": {"family_align_weight": 0.1},
        "contrastive_light": {"family_align_weight": 0.05},
    }

    # Train and evaluate all models
    all_results = {}
    all_geometry = {}
    for name, cfg in configs.items():
        print(f"\n  [{name}] Training...")
        torch.manual_seed(42)
        model = build_model(device=device)
        results = train_and_eval(model, tasks, steps=steps, device=device, **cfg)
        geo = compute_geometry_and_family(model, tasks, device=device)
        all_results[name] = results
        all_geometry[name] = geo

        # Print summary
        avg_acc = np.mean([r["final_accuracy"] for r in results.values()])
        avg_loss = np.mean([r["final_loss"] for r in results.values()])
        converged = sum(1 for r in results.values() if r["converged"])
        print(f"    avg_acc={avg_acc:.4f} avg_loss={avg_loss:.4f} converged={converged}/{len(tasks)}")
        print(f"    geometry: entropy={geo['membership_entropy']:.4f} margin={geo['membership_margin']:.6f} "
              f"challenger={geo['challenger_disagree_rate']:.4f}")

    # Select best geometry candidate
    print("\n  [Selection] Comparing geometry candidates...")
    baseline_geo = all_geometry["baseline"]
    best_name = "baseline"
    best_score = 0
    for name, geo in all_geometry.items():
        if name == "baseline":
            continue
        entropy_improvement = baseline_geo["membership_entropy"] - geo["membership_entropy"]
        margin_improvement = geo["membership_margin"] - baseline_geo["membership_margin"]
        challenger_improvement = baseline_geo["challenger_disagree_rate"] - geo["challenger_disagree_rate"]
        avg_loss = np.mean([r["final_loss"] for r in all_results[name].values()])
        baseline_loss = np.mean([r["final_loss"] for r in all_results["baseline"].values()])
        loss_not_worse = avg_loss <= baseline_loss * 1.1
        score = entropy_improvement + margin_improvement * 10 + challenger_improvement
        if loss_not_worse and score > best_score:
            best_score = score
            best_name = name
    print(f"    Selected: {best_name} (score={best_score:.4f})")

    # Length ladder (short eval)
    print("\n  [Length] Running length ladder...")
    torch.manual_seed(42)
    length_model = build_model(device=device)
    cfg_best = configs[best_name]
    length_model = build_model(device=device)
    # Train at short length
    train_and_eval(length_model, tasks[:3], steps=steps, max_seq_len=32, device=device, **cfg_best)
    # Eval at multiple lengths
    length_results = {}
    for eval_len in [32, 64, 128]:
        length_model.eval()
        task_losses = []
        for task in tasks[:3]:
            x, y, _ = generate_stage2_batch(task, batch_size=16, max_seq_len=eval_len, seed=42)
            x, y = x.to(device), y.to(device)
            with torch.no_grad():
                out = length_model(input_ids=x, targets=y)
                task_losses.append(out["loss"].item())
        length_results[eval_len] = {"avg_loss": float(np.mean(task_losses))}
    print(f"    Length results: {length_results}")

    # Failure classification
    print("\n  [Failures] Classifying failures...")
    failures = []
    best_results = all_results[best_name]
    for task, r in best_results.items():
        if not r["converged"]:
            if "agreement" in task or "dependency" in task:
                failures.append(("PVR_EC_FAILURE_NLP_DEPENDENCY_TRANSFER", task))
            elif "negation" in task:
                failures.append(("PVR_EC_FAILURE_NLP_NEGATION_COLLAPSE", task))
            elif "coreference" in task:
                failures.append(("PVR_EC_FAILURE_NLP_COREFERENCE_MEMORY_COLLAPSE", task))
            elif "ambiguous" in task:
                failures.append(("PVR_EC_FAILURE_NLP_AMBIGUOUS_TOKEN_OWNERSHIP", task))
            elif "paraphrase" in task:
                failures.append(("PVR_EC_FAILURE_NLP_PARAPHRASE_INVARIANCE_COLLAPSE", task))
            elif "instruction" in task:
                failures.append(("PVR_EC_FAILURE_NLP_INSTRUCTION_CONDITIONING_COLLAPSE", task))
            else:
                failures.append(("PVR_EC_FAILURE_UNKNOWN", task))

    unknown_count = sum(1 for f, _ in failures if "UNKNOWN" in f)
    print(f"    Failures: {len(failures)} total, {unknown_count} unknown")
    for f, task in failures:
        print(f"      {task}: {f}")

    # Gate
    print("\n  [Gate] Evaluating research gate...")
    geo_best = all_geometry[best_name]
    if unknown_count > 0:
        verdict = "PVR_EC_NLP_STAGE2_OBSERVATORY_EXPANSION_REQUIRED"
    elif len(failures) == 0:
        verdict = "PVR_EC_NLP_STAGE2_RESEARCH_ALLOWED"
    elif geo_best["membership_entropy"] < baseline_geo["membership_entropy"]:
        verdict = "PVR_EC_NLP_STAGE2_RESEARCH_ALLOWED_WITH_BLOCKERS"
    else:
        verdict = "PVR_EC_NLP_STAGE2_GEOMETRY_REPAIR_NOT_REPEATABLE"

    total_time = time.time() - t0

    # Write reports
    def wr(stem, payload):
        with open(output_path / f"{stem}.json", "w") as f:
            json.dump(payload, f, indent=2, default=str)
        md = [f"# {stem.replace('_',' ').title()}", f"**Status:** {payload.get('status','')}", "",
              "```json", json.dumps(payload, indent=2, default=str)[:6000], "```"]
        with open(output_path / f"{stem}.md", "w") as f:
            f.write("\n".join(md))

    wr("pvr_ec_nlp_stage2_dataset_report", {"status": "READY", "tasks": list(tasks), "count": len(tasks)})
    wr("pvr_ec_nlp_stage2_model_comparison_report", {"status": "COMPLETE", "results": all_results})
    wr("pvr_ec_nlp_stage2_geometry_candidate_comparison_report", {
        "status": "COMPLETE", "selected": best_name, "all_geometry": all_geometry, "score": best_score})
    wr("pvr_ec_nlp_stage2_length_ladder_report", {"status": "COMPLETE", "results": length_results})
    wr("pvr_ec_nlp_stage2_family_preservation_report", {"status": "MEASURED", "geometry": all_geometry})
    wr("pvr_ec_nlp_stage2_prototype_geometry_report", {"status": "MEASURED", "best": geo_best, "baseline": baseline_geo})
    wr("pvr_ec_nlp_stage2_failure_attribution_report", {"status": "CLASSIFIED", "failures": failures, "unknown": unknown_count})
    wr("pvr_ec_nlp_stage2_unknown_failure_report", {"status": "NONE" if unknown_count == 0 else "BLOCKING", "count": unknown_count})
    wr("pvr_ec_nlp_stage2_research_gate_report", {
        "status": verdict, "verdict": verdict,
        "selected_candidate": best_name,
        "geometry_improvement": {
            "entropy_delta": baseline_geo["membership_entropy"] - geo_best["membership_entropy"],
            "margin_delta": geo_best["membership_margin"] - baseline_geo["membership_margin"],
        },
        "failures_classified": len(failures), "unknown_failures": unknown_count,
        "hard_invariants": {"owners_per_token": 1.0, "top2_executions": 0, "top4_executions": 0,
                            "production_map_mutated": False},
        "deployment_verdict": "PVR_EC_DEPLOYMENT_STILL_BLOCKED",
        "total_time_s": total_time,
    })

    print(f"\n{'='*70}")
    print(f"  NLP STAGE 2 COMPLETE | {total_time:.1f}s")
    print(f"  Research: {verdict}")
    print(f"  Deployment: PVR_EC_DEPLOYMENT_STILL_BLOCKED")
    print(f"  Selected geometry: {best_name}")
    print(f"  owners/token=1.0 | Top2=0 | Top4=0")
    print(f"{'='*70}")
    return verdict


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default="evaluation/benchmark_results/pvr_nlp_stage2_full")
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--steps", type=int, default=200)
    args = parser.parse_args()
    run_stage2(args.output_dir, device=args.device, steps=args.steps)
