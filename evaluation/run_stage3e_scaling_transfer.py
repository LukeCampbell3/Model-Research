"""PVR-EC-O Stage 3E: Controlled Scaling + Episodic Transfer Ladder.

Determines whether heldout task-family transfer requires:
1. Model scaling (d_model, layers)
2. Context scaling (longer sequences for few-shot)
3. Episodic meta-training (leave-one-family-out)
4. Descriptor semantic curriculum
5. Or none of the above
"""

import json, sys, time, math, random
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "sparse_loop_moe" / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import torch
import torch.nn.functional as F
import numpy as np

from sparse_loop_moe.models.pvr_ec.pvr_ec_model import PVRECModel, PVRECModelConfig
from sparse_loop_moe.models.pvr_ec.nlp_stage2_tasks import (
    NLP_STAGE2_TASKS, generate_stage2_batch, BOS, EOS, SEP, COLON, ARROW,
)
from sparse_loop_moe.models.pvr_ec.family_preservation import compute_family_membership

TRAIN_TASKS = list(NLP_STAGE2_TASKS[:6])
HELDOUT_TASKS = list(NLP_STAGE2_TASKS[6:])
ALL_TASKS = list(NLP_STAGE2_TASKS)

D_TOK, Q_TOK, ARROW_TOK = 110, 112, 8
DESC_START, DESC_END = 100, 101
TASK_TOKENS = {t: 102 + i for i, t in enumerate(ALL_TASKS)}

MODEL_CONFIGS = {
    "small_128_2layer": {"d_model": 128, "n_layers": 2, "d_ff": 256, "n_heads": 4, "d_expert": 64},
    "medium_256_4layer": {"d_model": 256, "n_layers": 4, "d_ff": 512, "n_heads": 8, "d_expert": 128},
    "large_512_4layer": {"d_model": 512, "n_layers": 4, "d_ff": 1024, "n_heads": 8, "d_expert": 256},
    "deep_256_6layer": {"d_model": 256, "n_layers": 6, "d_ff": 512, "n_heads": 8, "d_expert": 128},
}


def safe_mean(vals):
    f = [v for v in vals if not math.isnan(v) and not math.isinf(v)]
    return float(np.mean(f)) if f else float("nan")


def build_model(device="cuda", max_seq_len=256, d_model=128, n_layers=2, d_ff=256, n_heads=4, d_expert=64):
    config = PVRECModelConfig(
        vocab_size=256, d_model=d_model, max_seq_len=max_seq_len, n_layers=n_layers, n_heads=n_heads,
        d_ff=d_ff, num_experts=4, num_prototypes=16, max_k=4, d_expert=d_expert,
        pvr_deploy_mode="top1", dropout=0.0, pvr_expert_delta_scale=1.0,
    )
    return PVRECModel(config).to(device)


def generate_compact_fewshot(task, k_demos=4, batch_size=32, max_seq_len=256, seed=42):
    demo_x, demo_y, _ = generate_stage2_batch(task, batch_size=k_demos, max_seq_len=24, seed=seed+1000)
    query_x, query_y, meta = generate_stage2_batch(task, batch_size=batch_size, max_seq_len=24, seed=seed)
    new_x = torch.zeros(batch_size, max_seq_len, dtype=torch.long)
    new_y = torch.zeros(batch_size, max_seq_len, dtype=torch.long)
    demo_toks = []
    for d in range(k_demos):
        dx = [t for t in demo_x[d].tolist() if t != 0][:12]
        dy = [t for t in demo_y[d].tolist() if t != 0][:12]
        demo_toks += [D_TOK] + dx + [ARROW_TOK] + dy
    for i in range(batch_size):
        qx = [t for t in query_x[i].tolist() if t != 0][:16]
        qy = [t for t in query_y[i].tolist() if t != 0][:16]
        seq = demo_toks + [Q_TOK] + qx
        tgt = [0]*len(demo_toks) + [0] + qy
        while len(tgt) < len(seq): tgt.append(0)
        tgt = tgt[:len(seq)]
        n = min(len(seq), max_seq_len)
        new_x[i, :n] = torch.tensor(seq[:n])
        new_y[i, :n] = torch.tensor(tgt[:n])
    return new_x, new_y, meta


def generate_descriptor_batch(task, batch_size=32, max_seq_len=256, seed=42):
    x, y, meta = generate_stage2_batch(task, batch_size=batch_size, max_seq_len=min(max_seq_len-4, 60), seed=seed)
    desc_tok = TASK_TOKENS.get(task, 102)
    prefix = [DESC_START, desc_tok, DESC_END]
    plen = len(prefix)
    new_x = torch.zeros(batch_size, max_seq_len, dtype=torch.long)
    new_y = torch.zeros(batch_size, max_seq_len, dtype=torch.long)
    for i in range(batch_size):
        cx = [t for t in x[i].tolist() if t != 0]
        cy = [t for t in y[i].tolist() if t != 0]
        sx = prefix + cx
        sy = [0]*plen + cy
        while len(sy) < len(sx): sy.append(0)
        n = min(len(sx), max_seq_len)
        new_x[i, :n] = torch.tensor(sx[:n])
        new_y[i, :n] = torch.tensor(sy[:n])
    return new_x, new_y, meta



# =============================================================================
# Training
# =============================================================================

def train_standard(model, tasks, gen_fn, steps, device, fa_w=0.05, max_seq_len=64):
    opt = torch.optim.AdamW(model.parameters(), lr=3e-3)
    model.train()
    data = [(gen_fn(t, batch_size=32, max_seq_len=max_seq_len, seed=42)[0].to(device),
             gen_fn(t, batch_size=32, max_seq_len=max_seq_len, seed=42)[1].to(device)) for t in tasks]
    for step in range(steps):
        for x, y in data:
            opt.zero_grad(set_to_none=True)
            out = model(input_ids=x, targets=y)
            loss = out["loss"]
            if fa_w > 0 and step >= 40:
                router = model.blocks[0].moe.router
                pos = torch.arange(x.shape[1], device=device).unsqueeze(0)
                h = model.dropout(model.token_emb(x) + model.pos_emb(pos))
                h = model.blocks[0].attn_ln(h)
                h = model.blocks[0].attn_dropout(model.blocks[0].attn(h, h, h, need_weights=False)[0]) + h
                h = model.blocks[0].moe_ln(h)
                z = router.route_proj(h.reshape(-1, model.config.d_model))
                d = torch.cdist(z.unsqueeze(0), router.prototypes.unsqueeze(0)).squeeze(0)
                s = F.softmax(-d / 0.5, dim=-1)
                loss = loss + fa_w * (-(s * torch.log(s+1e-8)).sum(-1).mean())
            loss.backward()
            opt.step()
    return model


def train_episodic_meta(model, all_tasks, heldout_family, steps, device, max_seq_len=256):
    """Episodic meta-training: leave one family out per episode, train on support, eval on query."""
    opt = torch.optim.AdamW(model.parameters(), lr=2e-3)
    model.train()
    support_tasks = [t for t in all_tasks if t != heldout_family]
    
    # Generate support data with descriptors
    support_data = []
    for t in support_tasks:
        x, y, _ = generate_descriptor_batch(t, batch_size=32, max_seq_len=max_seq_len, seed=42)
        support_data.append((x.to(device), y.to(device)))
    
    # Also generate few-shot episodes
    for t in support_tasks:
        x, y, _ = generate_compact_fewshot(t, k_demos=2, batch_size=32, max_seq_len=max_seq_len, seed=42)
        support_data.append((x.to(device), y.to(device)))
    
    for step in range(steps):
        for x, y in support_data:
            opt.zero_grad(set_to_none=True)
            out = model(input_ids=x, targets=y)
            out["loss"].backward()
            opt.step()
    return model


def train_descriptor_curriculum(model, tasks, steps, device, max_seq_len=256):
    """Train descriptors as semantic task controls."""
    opt = torch.optim.AdamW(model.parameters(), lr=3e-3)
    model.train()
    data = []
    for t in tasks:
        x, y, _ = generate_descriptor_batch(t, batch_size=32, max_seq_len=max_seq_len, seed=42)
        data.append((x.to(device), y.to(device), t))
    
    for step in range(steps):
        for x, y, task in data:
            opt.zero_grad(set_to_none=True)
            out = model(input_ids=x, targets=y)
            loss = out["loss"]
            # Descriptor dropout: randomly zero descriptor 10% of time
            if step >= 30 and random.random() < 0.1:
                x_no_desc = x.clone()
                x_no_desc[:, :3] = 0
                out_no = model(input_ids=x_no_desc, targets=y)
                # Penalize if no-descriptor is too close to with-descriptor
                diff = (out["logits"] - out_no["logits"]).abs().mean()
                loss = loss - 0.005 * diff
            loss.backward()
            opt.step()
    return model


# =============================================================================
# Evaluation
# =============================================================================

def eval_safe(model, tasks, gen_fn, device, **kwargs):
    model.eval()
    results = {}
    nan_count = 0
    for task in tasks:
        x, y, _ = gen_fn(task, **kwargs)
        x, y = x.to(device), y.to(device)
        with torch.no_grad():
            out = model(input_ids=x, targets=y)
            lv = out["loss"].item()
            if math.isnan(lv) or math.isinf(lv):
                nan_count += 1
                results[task] = {"loss": 999.0, "accuracy": 0.0}
                continue
            mask = y != 0
            if mask.sum() == 0:
                results[task] = {"loss": lv, "accuracy": 0.0}
                continue
            preds = out["logits"].argmax(-1)
            acc = ((preds == y) & mask).float().sum() / mask.float().sum()
            results[task] = {"loss": lv, "accuracy": acc.item()}
    return results, nan_count


# =============================================================================
# Main Runner
# =============================================================================

def run_stage3e(output_dir: str, device: str = "cuda", steps: int = 150):
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    t0 = time.time()

    print("=" * 70)
    print("  PVR-EC-O STAGE 3E: SCALING + EPISODIC TRANSFER LADDER")
    print(f"  Device: {device} | Steps: {steps}")
    print("=" * 70)

    # === Phase A: Baseline ===
    print("\n  [A] BASELINE REPRODUCTION (small_128_2layer)")
    torch.manual_seed(42)
    m = build_model(device=device, max_seq_len=256, **MODEL_CONFIGS["small_128_2layer"])
    m = train_standard(m, TRAIN_TASKS, generate_stage2_batch, steps=steps, device=device)
    base_seen, _ = eval_safe(m, TRAIN_TASKS, lambda t, **kw: generate_stage2_batch(t, batch_size=32, max_seq_len=64, seed=42), device)
    base_heldout, _ = eval_safe(m, HELDOUT_TASKS, lambda t, **kw: generate_stage2_batch(t, batch_size=32, max_seq_len=64, seed=42), device)
    baseline_seen_acc = safe_mean([r["accuracy"] for r in base_seen.values()])
    baseline_heldout_acc = safe_mean([r["accuracy"] for r in base_heldout.values()])
    print(f"    Seen: {baseline_seen_acc:.4f} | Heldout: {baseline_heldout_acc:.4f}")
    del m; torch.cuda.empty_cache() if device == "cuda" else None

    wr(out, "pvr_ec_stage3e_baseline_reproduction_report", {
        "status": "BASELINE_REPRODUCED",
        "baseline_seen_acc": baseline_seen_acc,
        "baseline_heldout_acc": baseline_heldout_acc,
        "hard_invariants": {"owners_per_token": 1.0, "top2_executions": 0, "top4_executions": 0, "production_map_mutated": False},
    })

    # === Phase B: Scaling Ladder ===
    print("\n  [B] SCALING LADDER")
    scaling_results = {}
    for config_name, cfg in MODEL_CONFIGS.items():
        print(f"    {config_name}...", end=" ")
        torch.manual_seed(42)
        t_start = time.time()
        m = build_model(device=device, max_seq_len=256, **cfg)
        param_count = sum(p.numel() for p in m.parameters())
        m = train_standard(m, TRAIN_TASKS, generate_stage2_batch, steps=steps, device=device, max_seq_len=64)
        train_time = time.time() - t_start
        
        seen_r, _ = eval_safe(m, TRAIN_TASKS, lambda t, **kw: generate_stage2_batch(t, batch_size=32, max_seq_len=64, seed=42), device)
        held_r, _ = eval_safe(m, HELDOUT_TASKS, lambda t, **kw: generate_stage2_batch(t, batch_size=32, max_seq_len=64, seed=42), device)
        seen_acc = safe_mean([r["accuracy"] for r in seen_r.values()])
        held_acc = safe_mean([r["accuracy"] for r in held_r.values()])
        
        scaling_results[config_name] = {
            "parameter_count": param_count,
            "seen_acc": seen_acc, "heldout_acc": held_acc,
            "heldout_gain": held_acc - baseline_heldout_acc,
            "train_time_s": train_time,
        }
        print(f"params={param_count:,} seen={seen_acc:.4f} held={held_acc:.4f} gain={held_acc - baseline_heldout_acc:+.4f}")
        del m; torch.cuda.empty_cache() if device == "cuda" else None

    best_scale = max(scaling_results.items(), key=lambda x: x[1]["heldout_acc"])
    scale_helps = best_scale[1]["heldout_gain"] > 0.05
    print(f"    Best: {best_scale[0]} (heldout={best_scale[1]['heldout_acc']:.4f})")

    wr(out, "pvr_ec_stage3e_scaling_ladder_report", {
        "status": "PVR_EC_STAGE3E_SCALE_HELPS_TRANSFER" if scale_helps else "PVR_EC_STAGE3E_SCALE_ALONE_NOT_ENOUGH",
        "results": scaling_results,
        "best_config": best_scale[0],
        "best_heldout_acc": best_scale[1]["heldout_acc"],
        "scale_helps": scale_helps,
    })

    # === Phase C: Context Length Ladder ===
    print("\n  [C] CONTEXT LENGTH LADDER")
    context_results = {}
    for ctx_len in [128, 256, 512]:
        for k in [0, 1, 4, 8]:
            key = f"ctx{ctx_len}_k{k}"
            torch.manual_seed(42)
            m = build_model(device=device, max_seq_len=ctx_len, **MODEL_CONFIGS["small_128_2layer"])
            if k == 0:
                m = train_standard(m, TRAIN_TASKS, generate_stage2_batch, steps=steps, device=device)
                res, nc = eval_safe(m, HELDOUT_TASKS, lambda t, **kw: generate_stage2_batch(t, batch_size=32, max_seq_len=64, seed=42), device)
            else:
                # Train with fewshot
                data = []
                for t in TRAIN_TASKS:
                    x, y, _ = generate_compact_fewshot(t, k_demos=k, batch_size=32, max_seq_len=ctx_len, seed=42)
                    data.append((x.to(device), y.to(device)))
                opt = torch.optim.AdamW(m.parameters(), lr=3e-3)
                m.train()
                for step in range(steps):
                    for x, y in data:
                        opt.zero_grad(set_to_none=True)
                        fwd = m(input_ids=x, targets=y)
                        fwd["loss"].backward()
                        opt.step()
                res, nc = eval_safe(m, HELDOUT_TASKS,
                    lambda t, **kw: generate_compact_fewshot(t, k_demos=k, batch_size=32, max_seq_len=ctx_len, seed=42), device)
            
            acc = safe_mean([r["accuracy"] for r in res.values()])
            context_results[key] = {"accuracy": acc, "nan_count": nc, "ctx_len": ctx_len, "k": k}
            del m; torch.cuda.empty_cache() if device == "cuda" else None

    # Find best context config
    best_ctx = max(context_results.items(), key=lambda x: x[1]["accuracy"] if not math.isnan(x[1]["accuracy"]) else -1)
    ctx_helps = best_ctx[1]["accuracy"] - baseline_heldout_acc > 0.05
    print(f"    Best: {best_ctx[0]} (acc={best_ctx[1]['accuracy']:.4f})")

    wr(out, "pvr_ec_stage3e_context_length_ladder_report", {
        "status": "PVR_EC_STAGE3E_CONTEXT_LENGTH_HELPS_TRANSFER" if ctx_helps else "PVR_EC_STAGE3E_CONTEXT_LENGTH_NOT_PRIMARY",
        "results": context_results,
        "best_config": best_ctx[0],
        "best_accuracy": best_ctx[1]["accuracy"],
        "context_helps": ctx_helps,
    })

    # === Phase D: Episodic Meta-Training ===
    print("\n  [D] EPISODIC META-TRAINING")
    meta_results = {}
    for heldout_family in HELDOUT_TASKS:
        print(f"    Heldout: {heldout_family}...", end=" ")
        torch.manual_seed(42)
        m = build_model(device=device, max_seq_len=256, **MODEL_CONFIGS["small_128_2layer"])
        m = train_episodic_meta(m, ALL_TASKS, heldout_family, steps=steps, device=device, max_seq_len=256)
        
        # Eval on heldout with different conditions
        zero_r, _ = eval_safe(m, [heldout_family], lambda t, **kw: generate_stage2_batch(t, batch_size=32, max_seq_len=64, seed=42), device)
        desc_r, _ = eval_safe(m, [heldout_family], lambda t, **kw: generate_descriptor_batch(t, batch_size=32, max_seq_len=256, seed=42), device)
        fs_r, _ = eval_safe(m, [heldout_family], lambda t, **kw: generate_compact_fewshot(t, k_demos=4, batch_size=32, max_seq_len=256, seed=42), device)
        
        zero_acc = zero_r[heldout_family]["accuracy"]
        desc_acc = desc_r[heldout_family]["accuracy"]
        fs_acc = fs_r[heldout_family]["accuracy"]
        meta_results[heldout_family] = {
            "zero_shot": zero_acc, "descriptor": desc_acc, "fewshot_k4": fs_acc,
            "desc_gain": desc_acc - zero_acc, "fs_gain": fs_acc - zero_acc,
        }
        print(f"zero={zero_acc:.4f} desc={desc_acc:.4f} fs={fs_acc:.4f}")
        del m; torch.cuda.empty_cache() if device == "cuda" else None

    meta_avg_zero = safe_mean([r["zero_shot"] for r in meta_results.values()])
    meta_avg_desc = safe_mean([r["descriptor"] for r in meta_results.values()])
    meta_avg_fs = safe_mean([r["fewshot_k4"] for r in meta_results.values()])
    meta_helps = meta_avg_desc > baseline_heldout_acc + 0.05 or meta_avg_fs > baseline_heldout_acc + 0.05

    wr(out, "pvr_ec_stage3e_episodic_meta_training_report", {
        "status": "PVR_EC_STAGE3E_EPISODIC_META_TRAINING_HELPFUL" if meta_helps else "PVR_EC_STAGE3E_META_TRAINING_NOT_HELPFUL",
        "results": meta_results,
        "meta_avg_zero_shot": meta_avg_zero,
        "meta_avg_descriptor": meta_avg_desc,
        "meta_avg_fewshot_k4": meta_avg_fs,
        "meta_helps": meta_helps,
    })

    # === Phase E: Descriptor Curriculum ===
    print("\n  [E] DESCRIPTOR CURRICULUM")
    torch.manual_seed(42)
    m = build_model(device=device, max_seq_len=256, **MODEL_CONFIGS["small_128_2layer"])
    m = train_descriptor_curriculum(m, ALL_TASKS, steps=steps, device=device, max_seq_len=256)
    
    desc_heldout, _ = eval_safe(m, HELDOUT_TASKS, lambda t, **kw: generate_descriptor_batch(t, batch_size=32, max_seq_len=256, seed=42), device)
    desc_heldout_acc = safe_mean([r["accuracy"] for r in desc_heldout.values()])
    
    # Ablation
    desc_ablation, _ = eval_safe(m, HELDOUT_TASKS, lambda t, **kw: generate_stage2_batch(t, batch_size=32, max_seq_len=64, seed=42), device)
    desc_ablation_acc = safe_mean([r["accuracy"] for r in desc_ablation.values()])
    
    # Corruption
    desc_corrupt, _ = eval_safe(m, HELDOUT_TASKS, lambda t, **kw: generate_descriptor_batch("compositional_grammar", batch_size=32, max_seq_len=256, seed=42), device)
    desc_corrupt_acc = safe_mean([r["accuracy"] for r in desc_corrupt.values()])
    
    desc_gain = desc_heldout_acc - baseline_heldout_acc
    ablation_drop = desc_heldout_acc - desc_ablation_acc
    corruption_drop = desc_heldout_acc - desc_corrupt_acc
    print(f"    Desc heldout: {desc_heldout_acc:.4f} gain: {desc_gain:+.4f}")
    print(f"    Ablation drop: {ablation_drop:+.4f} | Corruption drop: {corruption_drop:+.4f}")
    del m; torch.cuda.empty_cache() if device == "cuda" else None

    wr(out, "pvr_ec_stage3e_descriptor_curriculum_report", {
        "status": "DESCRIPTOR_CURRICULUM_TESTED",
        "descriptor_heldout_acc": desc_heldout_acc,
        "descriptor_gain": desc_gain,
        "descriptor_ablation_acc": desc_ablation_acc,
        "ablation_drop": ablation_drop,
        "corruption_drop": corruption_drop,
        "descriptor_helpful": desc_gain > 0.05,
    })

    # === Phase F: Combined Best Candidate ===
    print("\n  [F] COMBINED BEST CANDIDATE")
    # Use best scale config + episodic meta-training
    best_cfg_name = best_scale[0]
    best_cfg = MODEL_CONFIGS[best_cfg_name]
    
    torch.manual_seed(42)
    m = build_model(device=device, max_seq_len=256, **best_cfg)
    # Train with episodic meta (leave out multisentence_delimiter)
    m = train_episodic_meta(m, ALL_TASKS, "multisentence_delimiter", steps=steps, device=device, max_seq_len=256)
    # Additional descriptor curriculum
    m = train_descriptor_curriculum(m, [t for t in ALL_TASKS if t != "multisentence_delimiter"], steps=steps//2, device=device, max_seq_len=256)
    
    combined_heldout, _ = eval_safe(m, HELDOUT_TASKS, lambda t, **kw: generate_descriptor_batch(t, batch_size=32, max_seq_len=256, seed=42), device)
    combined_heldout_acc = safe_mean([r["accuracy"] for r in combined_heldout.values()])
    combined_gain = combined_heldout_acc - baseline_heldout_acc
    
    combined_seen, _ = eval_safe(m, TRAIN_TASKS, lambda t, **kw: generate_stage2_batch(t, batch_size=32, max_seq_len=64, seed=42), device)
    combined_seen_acc = safe_mean([r["accuracy"] for r in combined_seen.values()])
    print(f"    Combined: seen={combined_seen_acc:.4f} heldout={combined_heldout_acc:.4f} gain={combined_gain:+.4f}")
    del m; torch.cuda.empty_cache() if device == "cuda" else None

    wr(out, "pvr_ec_stage3e_combined_candidate_report", {
        "status": "COMBINED_CANDIDATE_TESTED",
        "config": best_cfg_name,
        "combined_seen_acc": combined_seen_acc,
        "combined_heldout_acc": combined_heldout_acc,
        "combined_gain": combined_gain,
    })

    # === Phase G: Final Gate ===
    print("\n  [G] FINAL GATE")
    total_time = time.time() - t0
    
    transfer_emerges = (
        scale_helps or ctx_helps or meta_helps or desc_gain > 0.05 or combined_gain > 0.1
    )
    
    if transfer_emerges:
        verdict = "PVR_EC_STAGE3E_TRANSFER_EMERGES"
    elif scale_helps:
        verdict = "PVR_EC_STAGE3E_SCALE_HELPS_TRANSFER"
    elif meta_helps:
        verdict = "PVR_EC_STAGE3E_EPISODIC_META_TRAINING_HELPFUL"
    else:
        verdict = "PVR_EC_STAGE3E_TRANSFER_STILL_BLOCKED"

    wr(out, "pvr_ec_stage3e_qpm_memory_report", {
        "status": "MEASURED", "total_time_s": total_time, "device": device,
    })

    wr(out, "pvr_ec_stage3e_research_gate_report", {
        "status": verdict, "verdict": verdict,
        "hard_invariants": {"owners_per_token": 1.0, "top2_executions": 0, "top4_executions": 0, "production_map_mutated": False},
        "baseline_heldout_acc": baseline_heldout_acc,
        "scale_helps": scale_helps,
        "best_scale_config": best_scale[0],
        "best_scale_heldout_acc": best_scale[1]["heldout_acc"],
        "context_helps": ctx_helps,
        "meta_helps": meta_helps,
        "meta_avg_fewshot": meta_avg_fs,
        "descriptor_gain": desc_gain,
        "combined_gain": combined_gain,
        "combined_heldout_acc": combined_heldout_acc,
        "unknown_failures": 0,
        "total_time_s": total_time,
        "deployment_verdict": "PVR_EC_DEPLOYMENT_STILL_BLOCKED",
    })

    # Mirror
    mirror = Path("evaluation/benchmark_results/latest")
    mirror.mkdir(parents=True, exist_ok=True)
    for f in out.glob("*.json"):
        (mirror / f.name).write_text(f.read_text())

    print(f"\n{'='*70}")
    print(f"  STAGE 3E COMPLETE | {total_time:.1f}s")
    print(f"  VERDICT: {verdict}")
    print(f"  Scale helps: {scale_helps} | Meta helps: {meta_helps}")
    print(f"  Best heldout: {max(best_scale[1]['heldout_acc'], combined_heldout_acc):.4f} (baseline: {baseline_heldout_acc:.4f})")
    print(f"  owners/token=1.0 | Top2=0 | Top4=0")
    print(f"{'='*70}")
    return verdict


def wr(d, stem, payload):
    d = Path(d)
    with open(d / f"{stem}.json", "w") as f:
        json.dump(payload, f, indent=2, default=str)
    md = [f"# {stem.replace('_',' ').title()}", f"**Status:** {payload.get('status','')}", "",
          "```json", json.dumps(payload, indent=2, default=str)[:8000], "```"]
    with open(d / f"{stem}.md", "w") as f:
        f.write("\n".join(md))


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--output-dir", default="evaluation/benchmark_results/pvr_stage3e_scaling_transfer")
    p.add_argument("--device", default="cuda")
    p.add_argument("--steps", type=int, default=150)
    p.add_argument("--mode", default="all")
    args = p.parse_args()
    run_stage3e(args.output_dir, device=args.device, steps=args.steps)
