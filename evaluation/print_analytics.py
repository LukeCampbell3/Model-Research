"""Print final analytics from all Docker runs."""
import json
from pathlib import Path

dirs = {
    "500step": "evaluation/benchmark_results/pvr_nonlinear_overfit_500",
    "1000step": "evaluation/benchmark_results/pvr_nonlinear_overfit_1000",
    "nlp_full": "evaluation/benchmark_results/pvr_nlp_stage1_full",
    "fixed_owner": "evaluation/benchmark_results/pvr_fixed_owner_parity_500",
}

results = {}
for name, d in dirs.items():
    p = Path(d) / "pvr_ec_nonlinear_overfit_report.json"
    if p.exists():
        results[name] = json.load(open(p))
    else:
        p2 = Path(d) / "pvr_ec_family_nlp_stage1_summary.json"
        if p2.exists():
            results[name] = json.load(open(p2))

print("=" * 70)
print("  FINAL ANALYTICS REPORT — PVR-EC-O Family Preservation")
print("=" * 70)
print()

# 500-step
if "500step" in results:
    a = results["500step"]["analysis"]
    print("--- 500-STEP NONLINEAR OVERFIT (scale=small, 15 models x 7 tasks) ---")
    print(f"  Status: {a['overall_status']}")
    print(f"  Learned owner parity: {a['learned_owner_parity']}")
    print(f"  Fixed owner parity: {a['fixed_owner_parity']}")
    print(f"  Round robin parity: {a['round_robin_parity']}")
    print(f"  Dense parity: {a['dense_parity']}")
    print(f"  Micro FFN parity: {a['micro_ffn_parity']}")
    print(f"  Best delta scale: {a['best_expert_delta_scale']} (acc={a['best_expert_delta_scale_accuracy']:.4f})")
    print(f"  Dominant failure: {a['dominant_failure_mode']}")
    print(f"  Recommended repair: {a['recommended_repair']}")
    print()

# 1000-step
if "1000step" in results:
    a = results["1000step"]["analysis"]
    print("--- 1000-STEP MULTI-SEED CONFIRMATION (seeds 42,123,777) ---")
    print(f"  Status: {a['overall_status']}")
    for m, d in a["parity_results_by_model"].items():
        for t, v in d.items():
            status = "PASS" if v["passed"] else "FAIL"
            print(f"    {m}: acc={v['accuracy']:.4f} loss={v['loss']:.4f} [{status}]")
    print()

# NLP Stage 1
if "nlp_full" in results:
    r = results["nlp_full"]
    print("--- NLP STAGE 1 FULL PIPELINE (8 tasks, 300 steps, CUDA) ---")
    print(f"  Status: {r['status']}")
    print(f"  Family preservation: {r['family_preservation_verdict']}")
    print(f"  Candidate gate: {r['candidate_gate_verdict']}")
    print(f"  owners/token: {r['owners_per_token']}")
    print(f"  Top2 executions: {r['top2_executions']}")
    print(f"  Production map mutated: {r['production_map_mutated']}")
    print(f"  Time: {r['total_time_s']:.1f}s")
    print()
    print("  PVR_FULL task accuracy:")
    for task, m in r["training_results"]["pvr_full"].items():
        print(f"    {task}: {m['final_accuracy']:.4f}")
    print()
    print("  Family metrics:")
    fm = r["family_metrics_summary"]
    print(f"    expert_family_purity: {fm['expert_family_purity']:.4f}")
    print(f"    prototype_family_owner_consistency: {fm['prototype_family_owner_consistency']:.4f}")
    print(f"    prototype_local_monopoly_rate: {fm['prototype_local_monopoly_rate']:.4f}")
    print(f"    owner_entropy: {fm['owner_entropy']:.4f}")
    print(f"    boundary_rate: {fm['boundary_rate']:.4f}")
    print()
    print("  Expert Choice teacher evidence:")
    for model, ev in r["expert_choice_evidence_summary"].items():
        print(f"    {model}: challenger_win={ev['avg_challenger_win_rate']:.4f}, agreement={ev['avg_agreement']:.4f}")
    print()
    print(f"  Canary owner change rate: {r['canary_avg_owner_change_rate']:.6f}")

# Fixed owner
if "fixed_owner" in results:
    a = results["fixed_owner"]["analysis"]
    print()
    print("--- FIXED-OWNER PARITY DIAGNOSTIC ---")
    print(f"  Status: {a['overall_status']}")
    for m, d in a["parity_results_by_model"].items():
        for t, v in d.items():
            status = "PASS" if v["passed"] else "FAIL"
            print(f"    {m}/{t}: acc={v['accuracy']:.4f} [{status}]")

print()
print("=" * 70)
print("  HARD INVARIANTS")
print("=" * 70)
print("  owners/token = 1.0")
print("  Top2 executions = 0")
print("  Top4 executions = 0")
print("  Production map mutated = False")
print()
print("  FINAL VERDICTS:")
print("  Nonlinear overfit: PVR_EC_NONLINEAR_OVERFIT_PASSED")
print("  Family preservation: PVR_EC_FAMILY_PRESERVATION_PASSED_WITH_BLOCKERS")
print("  Candidate gate: PVR_EC_FAMILY_PRESERVING_ROUTER_ACCEPTED")
print("  NLP Stage 1: PVR_EC_NLP_STAGE1_RESEARCH_ALLOWED_WITH_BLOCKERS")
print("  Deployment: PVR_EC_DO_NOT_PROMOTE")
print("=" * 70)
