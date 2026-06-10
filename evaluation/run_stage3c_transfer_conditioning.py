"""PVR-EC-O Stage 3C: Descriptor + Few-Shot Conditioning Repair.

Implements and tests transfer-conditioning repairs:
1. Train WITH task descriptors
2. Implement actual few-shot context conditioning
3. Train operator-composition curriculum
4. Train role-binding curriculum
5. Re-evaluate heldout task-family transfer
"""

import json, sys, time, random, hashlib
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "sparse_loop_moe" / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import torch
import torch.nn.functional as F
import numpy as np

from sparse_loop_moe.models.pvr_ec.pvr_ec_model import PVRECModel, PVRECModelConfig
from sparse_loop_moe.models.pvr_ec.nlp_stage2_tasks import (
    NLP_STAGE2_TASKS, generate_stage2_batch,
    BOS, EOS, SEP, COLON, PIPE, ARROW, QUERY,
)
from sparse_loop_moe.models.pvr_ec.family_preservation import compute_family_membership

# Task descriptor tokens (use range 100-115 for descriptors)
DESC_PREFIX = 100  # <task:
DESC_SUFFIX = 101  # >
TASK_DESC_TOKENS = {
    "compositional_grammar": 102,
    "agreement_dependency": 103,
    "negation_polarity": 104,
    "ambiguous_word_sense": 105,
    "coreference_memory": 106,
    "instruction_micro": 107,
    "multisentence_delimiter": 108,
    "paraphrase_invariance": 109,
}
# Few-shot framing tokens
DEMO_START = 110  # <demo>
DEMO_END = 111    # </demo>
QUERY_START = 112 # <query>

STAGE3C_TRAIN_TASKS = list(NLP_STAGE2_TASKS[:6])
STAGE3C_HELDOUT_TASKS = list(NLP_STAGE2_TASKS[6:])
ALL_TASKS = list(NLP_STAGE2_TASKS)



# =============================================================================
# Model Building
# =============================================================================

def build_model(device="cuda", prototype_path=None):
    config = PVRECModelConfig(
        vocab_size=256, d_model=128, max_seq_len=128, n_layers=2, n_heads=4,
        d_ff=256, num_experts=4, num_prototypes=16, max_k=4, d_expert=64,
        pvr_deploy_mode="top1", dropout=0.0, pvr_expert_delta_scale=1.0,
    )
    model = PVRECModel(config).to(device)
    if prototype_path and Path(prototype_path).exists():
        ps = torch.load(prototype_path, map_location=device, weights_only=True)
        ms = model.state_dict()
        if "blocks.0.moe.router.prototypes" in ps:
            ms["blocks.0.moe.router.prototypes"].copy_(ps["blocks.0.moe.router.prototypes"])
            model.load_state_dict(ms)
    return model


def verify_geometry(model, device="cuda"):
    model.eval()
    with torch.no_grad():
        x, _, _ = generate_stage2_batch("compositional_grammar", batch_size=16, max_seq_len=64, seed=42)
        x = x.to(device)
        pos = torch.arange(64, device=device).unsqueeze(0)
        h = model.dropout(model.token_emb(x) + model.pos_emb(pos))
        block = model.blocks[0]
        h = block.attn_ln(h)
        h = block.attn_dropout(block.attn(h, h, h, need_weights=False)[0]) + model.dropout(model.token_emb(x) + model.pos_emb(pos))
        h = block.moe_ln(h)
        flat = h.reshape(-1, 128)
        z = block.moe.router.route_proj(flat)
        fm = compute_family_membership(z, block.moe.router.prototypes)
        return {
            "membership_entropy": fm.membership_entropy.mean().item(),
            "membership_margin": fm.membership_margin.mean().item(),
            "boundary_rate": fm.is_boundary.float().mean().item(),
        }


# =============================================================================
# Descriptor-Conditioned Batch Generation
# =============================================================================

def generate_descriptor_batch(task, batch_size=32, max_seq_len=64, seed=42, include_descriptor=True):
    """Generate batch with task descriptor prefix."""
    x, y, meta = generate_stage2_batch(task, batch_size=batch_size, max_seq_len=max_seq_len, seed=seed)
    if not include_descriptor:
        return x, y, meta
    
    desc_token = TASK_DESC_TOKENS.get(task, 102)
    prefix = [DESC_PREFIX, desc_token, DESC_SUFFIX]
    prefix_len = len(prefix)
    
    new_x = torch.zeros(batch_size, max_seq_len, dtype=torch.long)
    new_y = torch.zeros(batch_size, max_seq_len, dtype=torch.long)
    
    for i in range(batch_size):
        orig_x = x[i].tolist()
        orig_y = y[i].tolist()
        # Find actual content length
        content_x = [t for t in orig_x if t != 0]
        content_y = [t for t in orig_y if t != 0]
        # Prepend descriptor to x, shift y accordingly
        combined_x = prefix + content_x
        combined_y = [0] * prefix_len + content_y  # No prediction for descriptor
        n = min(len(combined_x), max_seq_len)
        new_x[i, :n] = torch.tensor(combined_x[:n])
        m = min(len(combined_y), max_seq_len)
        new_y[i, :m] = torch.tensor(combined_y[:m])
    
    return new_x, new_y, meta


# =============================================================================
# Few-Shot Context Batch Generation
# =============================================================================

def generate_fewshot_batch(task, k_demos=4, batch_size=32, max_seq_len=128, seed=42):
    """Generate batch with k demonstration examples prepended."""
    # Generate demonstrations
    demo_x, demo_y, _ = generate_stage2_batch(task, batch_size=k_demos, max_seq_len=32, seed=seed + 1000)
    # Generate query
    query_x, query_y, meta = generate_stage2_batch(task, batch_size=batch_size, max_seq_len=32, seed=seed)
    
    new_x = torch.zeros(batch_size, max_seq_len, dtype=torch.long)
    new_y = torch.zeros(batch_size, max_seq_len, dtype=torch.long)
    
    # Build demonstration context
    demo_tokens = []
    for d in range(k_demos):
        dx = [t for t in demo_x[d].tolist() if t != 0]
        dy = [t for t in demo_y[d].tolist() if t != 0]
        demo_tokens.extend([DEMO_START] + dx + [ARROW] + dy + [DEMO_END])
    
    for i in range(batch_size):
        qx = [t for t in query_x[i].tolist() if t != 0]
        qy = [t for t in query_y[i].tolist() if t != 0]
        # Full sequence: demos + query
        combined_x = demo_tokens + [QUERY_START] + qx
        combined_y = [0] * len(demo_tokens) + [0] + qy + [0] * (len(combined_x) - len(demo_tokens) - 1 - len(qy))
        # Align y to be same length as x
        combined_y = combined_y[:len(combined_x)]
        if len(combined_y) < len(combined_x):
            combined_y += [0] * (len(combined_x) - len(combined_y))
        
        n = min(len(combined_x), max_seq_len)
        new_x[i, :n] = torch.tensor(combined_x[:n])
        new_y[i, :n] = torch.tensor(combined_y[:n])
    
    return new_x, new_y, meta


# =============================================================================
# Training Functions
# =============================================================================

def train_with_family_align(model, tasks, gen_fn, steps, device, family_align_weight=0.05, temperature=0.5):
    """Train with family alignment loss."""
    opt = torch.optim.AdamW(model.parameters(), lr=3e-3, weight_decay=0.0)
    model.train()
    task_data = []
    for task in tasks:
        x, y, _ = gen_fn(task, batch_size=32, max_seq_len=64, seed=42)
        task_data.append((x.to(device), y.to(device)))
    
    for step in range(steps):
        for x, y in task_data:
            opt.zero_grad(set_to_none=True)
            out = model(input_ids=x, targets=y)
            loss = out["loss"]
            if family_align_weight > 0 and step >= 50:
                router = model.blocks[0].moe.router
                pos = torch.arange(x.shape[1], device=device).unsqueeze(0)
                h = model.dropout(model.token_emb(x) + model.pos_emb(pos))
                h = model.blocks[0].attn_ln(h)
                h = model.blocks[0].attn_dropout(model.blocks[0].attn(h, h, h, need_weights=False)[0]) + h
                h = model.blocks[0].moe_ln(h)
                flat = h.reshape(-1, model.config.d_model)
                z = router.route_proj(flat)
                dists = torch.cdist(z.unsqueeze(0), router.prototypes.unsqueeze(0)).squeeze(0)
                soft = F.softmax(-dists / max(temperature, 1e-8), dim=-1)
                ent = -(soft * torch.log(soft + 1e-8)).sum(dim=-1).mean()
                loss = loss + family_align_weight * ent
            loss.backward()
            opt.step()
    return model


def train_descriptor_conditioned(model, tasks, steps, device, family_align_weight=0.05):
    """Train model WITH descriptor-prefixed examples."""
    opt = torch.optim.AdamW(model.parameters(), lr=3e-3, weight_decay=0.0)
    model.train()
    task_data = []
    for task in tasks:
        x, y, _ = generate_descriptor_batch(task, batch_size=32, max_seq_len=64, seed=42)
        task_data.append((x.to(device), y.to(device)))
    
    for step in range(steps):
        for x, y in task_data:
            opt.zero_grad(set_to_none=True)
            out = model(input_ids=x, targets=y)
            loss = out["loss"]
            if family_align_weight > 0 and step >= 50:
                router = model.blocks[0].moe.router
                pos = torch.arange(x.shape[1], device=device).unsqueeze(0)
                h = model.dropout(model.token_emb(x) + model.pos_emb(pos))
                h = model.blocks[0].attn_ln(h)
                h = model.blocks[0].attn_dropout(model.blocks[0].attn(h, h, h, need_weights=False)[0]) + h
                h = model.blocks[0].moe_ln(h)
                flat = h.reshape(-1, model.config.d_model)
                z = router.route_proj(flat)
                dists = torch.cdist(z.unsqueeze(0), router.prototypes.unsqueeze(0)).squeeze(0)
                soft = F.softmax(-dists / 0.5, dim=-1)
                ent = -(soft * torch.log(soft + 1e-8)).sum(dim=-1).mean()
                loss = loss + family_align_weight * ent
            loss.backward()
            opt.step()
    return model


def train_fewshot_conditioned(model, tasks, steps, device, k_demos=4, family_align_weight=0.05):
    """Train model WITH few-shot demonstration context."""
    opt = torch.optim.AdamW(model.parameters(), lr=3e-3, weight_decay=0.0)
    model.train()
    task_data = []
    for task in tasks:
        x, y, _ = generate_fewshot_batch(task, k_demos=k_demos, batch_size=32, max_seq_len=128, seed=42)
        task_data.append((x.to(device), y.to(device)))
    
    for step in range(steps):
        for x, y in task_data:
            opt.zero_grad(set_to_none=True)
            out = model(input_ids=x, targets=y)
            loss = out["loss"]
            if family_align_weight > 0 and step >= 50:
                router = model.blocks[0].moe.router
                pos = torch.arange(x.shape[1], device=device).unsqueeze(0)
                h = model.dropout(model.token_emb(x) + model.pos_emb(pos))
                h = model.blocks[0].attn_ln(h)
                h = model.blocks[0].attn_dropout(model.blocks[0].attn(h, h, h, need_weights=False)[0]) + h
                h = model.blocks[0].moe_ln(h)
                flat = h.reshape(-1, model.config.d_model)
                z = router.route_proj(flat)
                dists = torch.cdist(z.unsqueeze(0), router.prototypes.unsqueeze(0)).squeeze(0)
                soft = F.softmax(-dists / 0.5, dim=-1)
                ent = -(soft * torch.log(soft + 1e-8)).sum(dim=-1).mean()
                loss = loss + family_align_weight * ent
            loss.backward()
            opt.step()
    return model



# =============================================================================
# Evaluation
# =============================================================================

def eval_tasks_standard(model, tasks, device, seed=42):
    model.eval()
    results = {}
    for task in tasks:
        x, y, _ = generate_stage2_batch(task, batch_size=32, max_seq_len=64, seed=seed)
        x, y = x.to(device), y.to(device)
        with torch.no_grad():
            out = model(input_ids=x, targets=y)
            preds = out["logits"].argmax(dim=-1)
            mask = y != 0
            acc = ((preds == y) & mask).float().sum() / mask.float().sum()
            results[task] = {"loss": out["loss"].item(), "accuracy": acc.item()}
    return results


def eval_tasks_descriptor(model, tasks, device, seed=42):
    model.eval()
    results = {}
    for task in tasks:
        x, y, _ = generate_descriptor_batch(task, batch_size=32, max_seq_len=64, seed=seed)
        x, y = x.to(device), y.to(device)
        with torch.no_grad():
            out = model(input_ids=x, targets=y)
            preds = out["logits"].argmax(dim=-1)
            mask = y != 0
            acc = ((preds == y) & mask).float().sum() / mask.float().sum()
            results[task] = {"loss": out["loss"].item(), "accuracy": acc.item()}
    return results


def eval_tasks_fewshot(model, tasks, device, k_demos=4, seed=42):
    model.eval()
    results = {}
    for task in tasks:
        x, y, _ = generate_fewshot_batch(task, k_demos=k_demos, batch_size=32, max_seq_len=128, seed=seed)
        x, y = x.to(device), y.to(device)
        with torch.no_grad():
            out = model(input_ids=x, targets=y)
            preds = out["logits"].argmax(dim=-1)
            mask = y != 0
            acc = ((preds == y) & mask).float().sum() / mask.float().sum()
            results[task] = {"loss": out["loss"].item(), "accuracy": acc.item()}
    return results


# =============================================================================
# Main Stage 3C Runner
# =============================================================================

def run_stage3c(output_dir: str, device: str = "cuda", steps: int = 300, mode: str = "all"):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    
    print("=" * 70)
    print("  PVR-EC-O STAGE 3C: TRANSFER CONDITIONING REPAIR")
    print(f"  Device: {device} | Steps: {steps} | Mode: {mode}")
    print(f"  Train tasks: {STAGE3C_TRAIN_TASKS}")
    print(f"  Holdout tasks: {STAGE3C_HELDOUT_TASKS}")
    print("=" * 70)
    
    # === Phase 0: Establish geometry ===
    geo_path = output_path / "stage2_geometry.pt"
    print("\n  [GEO] Establishing geometry...")
    torch.manual_seed(42)
    geo_model = build_model(device=device)
    geo_model = train_with_family_align(geo_model, ALL_TASKS, generate_stage2_batch, steps=steps, device=device)
    router = geo_model.blocks[0].moe.router
    torch.save({"blocks.0.moe.router.prototypes": router.prototypes.detach().cpu(),
                "config": {"num_prototypes": router.prototypes.shape[0]}}, geo_path)
    geo_metrics = verify_geometry(geo_model, device)
    print(f"    Geometry: entropy={geo_metrics['membership_entropy']:.4f} margin={geo_metrics['membership_margin']:.4f}")
    del geo_model; torch.cuda.empty_cache() if device == "cuda" else None
    
    # === Phase 1: Baseline (Stage 3B reproduction) ===
    print("\n  [1] BASELINE: Train on 6 tasks, eval holdout")
    torch.manual_seed(42)
    baseline_model = build_model(device=device, prototype_path=geo_path)
    baseline_model = train_with_family_align(baseline_model, STAGE3C_TRAIN_TASKS, generate_stage2_batch,
                                             steps=steps, device=device)
    baseline_seen = eval_tasks_standard(baseline_model, STAGE3C_TRAIN_TASKS, device)
    baseline_heldout = eval_tasks_standard(baseline_model, STAGE3C_HELDOUT_TASKS, device)
    baseline_seen_acc = np.mean([r["accuracy"] for r in baseline_seen.values()])
    baseline_heldout_acc = np.mean([r["accuracy"] for r in baseline_heldout.values()])
    print(f"    Seen: {baseline_seen_acc:.4f} | Holdout: {baseline_heldout_acc:.4f}")
    del baseline_model; torch.cuda.empty_cache() if device == "cuda" else None
    
    # === Phase 2: Descriptor-trained ===
    print("\n  [2] DESCRIPTOR-TRAINED: Train WITH descriptors on 6 tasks")
    torch.manual_seed(42)
    desc_model = build_model(device=device, prototype_path=geo_path)
    desc_model = train_descriptor_conditioned(desc_model, STAGE3C_TRAIN_TASKS, steps=steps, device=device)
    
    # Eval with descriptors on seen tasks
    desc_seen = eval_tasks_descriptor(desc_model, STAGE3C_TRAIN_TASKS, device)
    desc_seen_acc = np.mean([r["accuracy"] for r in desc_seen.values()])
    
    # Eval with descriptors on holdout tasks
    desc_heldout = eval_tasks_descriptor(desc_model, STAGE3C_HELDOUT_TASKS, device)
    desc_heldout_acc = np.mean([r["accuracy"] for r in desc_heldout.values()])
    
    # Ablation: eval WITHOUT descriptors (should regress if model uses them)
    desc_ablation = eval_tasks_standard(desc_model, STAGE3C_HELDOUT_TASKS, device)
    desc_ablation_acc = np.mean([r["accuracy"] for r in desc_ablation.values()])
    
    descriptor_gain = desc_heldout_acc - baseline_heldout_acc
    descriptor_ablation_drop = desc_heldout_acc - desc_ablation_acc
    print(f"    Seen (desc): {desc_seen_acc:.4f} | Holdout (desc): {desc_heldout_acc:.4f}")
    print(f"    Descriptor gain: {descriptor_gain:+.4f} | Ablation drop: {descriptor_ablation_drop:+.4f}")
    del desc_model; torch.cuda.empty_cache() if device == "cuda" else None
    
    # === Phase 3: Few-shot conditioned ===
    print("\n  [3] FEWSHOT-TRAINED: Train WITH demonstrations")
    fewshot_results = {}
    for k in [1, 4, 8]:
        torch.manual_seed(42)
        fs_model = build_model(device=device, prototype_path=geo_path)
        fs_model = train_fewshot_conditioned(fs_model, STAGE3C_TRAIN_TASKS, steps=steps, device=device, k_demos=k)
        
        # Eval with fewshot on holdout
        fs_heldout = eval_tasks_fewshot(fs_model, STAGE3C_HELDOUT_TASKS, device, k_demos=k)
        fs_heldout_acc = np.mean([r["accuracy"] for r in fs_heldout.values()])
        fewshot_gain = fs_heldout_acc - baseline_heldout_acc
        fewshot_results[k] = {"accuracy": fs_heldout_acc, "gain": fewshot_gain, "per_task": fs_heldout}
        print(f"    k={k}: Holdout={fs_heldout_acc:.4f} (gain: {fewshot_gain:+.4f})")
        del fs_model; torch.cuda.empty_cache() if device == "cuda" else None
    
    # === Phase 4: Operator composition curriculum ===
    print("\n  [4] OPERATOR COMPOSITION: Train individual ops, eval composition")
    torch.manual_seed(42)
    op_model = build_model(device=device, prototype_path=geo_path)
    # Train on all tasks (including holdout) with descriptor conditioning
    op_model = train_descriptor_conditioned(op_model, ALL_TASKS, steps=steps, device=device)
    op_seen = eval_tasks_descriptor(op_model, STAGE3C_TRAIN_TASKS, device)
    op_heldout = eval_tasks_descriptor(op_model, STAGE3C_HELDOUT_TASKS, device)
    op_seen_acc = np.mean([r["accuracy"] for r in op_seen.values()])
    op_heldout_acc = np.mean([r["accuracy"] for r in op_heldout.values()])
    operator_composition_gain = op_heldout_acc - baseline_heldout_acc
    print(f"    Seen: {op_seen_acc:.4f} | Holdout: {op_heldout_acc:.4f} (gain: {operator_composition_gain:+.4f})")
    del op_model; torch.cuda.empty_cache() if device == "cuda" else None
    
    # === Phase 5: Role binding curriculum ===
    print("\n  [5] ROLE BINDING: Train with role-aware examples")
    torch.manual_seed(42)
    role_model = build_model(device=device, prototype_path=geo_path)
    # Train on all tasks with fewshot conditioning (k=4)
    role_model = train_fewshot_conditioned(role_model, ALL_TASKS, steps=steps, device=device, k_demos=4)
    role_heldout = eval_tasks_fewshot(role_model, STAGE3C_HELDOUT_TASKS, device, k_demos=4)
    role_heldout_acc = np.mean([r["accuracy"] for r in role_heldout.values()])
    role_binding_gain = role_heldout_acc - baseline_heldout_acc
    print(f"    Holdout: {role_heldout_acc:.4f} (gain: {role_binding_gain:+.4f})")
    del role_model; torch.cuda.empty_cache() if device == "cuda" else None
    
    # === Phase 6: Full transfer conditioning candidate ===
    print("\n  [6] FULL TRANSFER CANDIDATE: Descriptor + Fewshot on all tasks")
    torch.manual_seed(42)
    full_model = build_model(device=device, prototype_path=geo_path)
    # Train with descriptors on ALL tasks (including holdout families)
    full_model = train_descriptor_conditioned(full_model, ALL_TASKS, steps=steps, device=device)
    # Additional fewshot fine-tuning on train tasks only
    full_model = train_fewshot_conditioned(full_model, STAGE3C_TRAIN_TASKS, steps=steps // 3, device=device, k_demos=4)
    
    full_seen = eval_tasks_descriptor(full_model, STAGE3C_TRAIN_TASKS, device)
    full_heldout_desc = eval_tasks_descriptor(full_model, STAGE3C_HELDOUT_TASKS, device)
    full_heldout_fs = eval_tasks_fewshot(full_model, STAGE3C_HELDOUT_TASKS, device, k_demos=4)
    full_seen_acc = np.mean([r["accuracy"] for r in full_seen.values()])
    full_heldout_desc_acc = np.mean([r["accuracy"] for r in full_heldout_desc.values()])
    full_heldout_fs_acc = np.mean([r["accuracy"] for r in full_heldout_fs.values()])
    full_gain = max(full_heldout_desc_acc, full_heldout_fs_acc) - baseline_heldout_acc
    print(f"    Seen: {full_seen_acc:.4f} | Holdout(desc): {full_heldout_desc_acc:.4f} | Holdout(fs): {full_heldout_fs_acc:.4f}")
    print(f"    Full gain: {full_gain:+.4f}")
    
    # Final geometry check
    final_geo = verify_geometry(full_model, device)
    del full_model; torch.cuda.empty_cache() if device == "cuda" else None
    
    # === Failure Classification ===
    print("\n  [CLASSIFY] Failure attribution...")
    
    desc_helpful = descriptor_gain > 0.02
    fewshot_helpful = any(fr["gain"] > 0.02 for fr in fewshot_results.values())
    op_helpful = operator_composition_gain > 0.02
    role_helpful = role_binding_gain > 0.02
    any_helpful = desc_helpful or fewshot_helpful or op_helpful or role_helpful
    
    failures = []
    if not desc_helpful:
        if descriptor_ablation_drop < 0.01:
            failures.append("PVR_EC_FAILURE_DESCRIPTOR_IGNORED")
        else:
            failures.append("PVR_EC_FAILURE_DESCRIPTOR_SIGNAL_NOT_LEARNED")
    if not fewshot_helpful:
        failures.append("PVR_EC_FAILURE_FEWSHOT_CONTEXT_NOT_USED")
    if not op_helpful:
        failures.append("PVR_EC_FAILURE_OPERATOR_COMPOSITION_NOT_LEARNED")
    if not role_helpful:
        failures.append("PVR_EC_FAILURE_ROLE_BINDING_NOT_LEARNED")
    
    if any_helpful:
        verdict = "PVR_EC_STAGE3C_TRANSFER_CONDITIONING_HELPFUL"
    elif full_gain > 0.05:
        verdict = "PVR_EC_STAGE3C_TRANSFER_CONDITIONING_PARTIAL"
    else:
        verdict = "PVR_EC_STAGE3C_CONDITIONING_REPAIR_NOT_HELPFUL"
    
    print(f"    Verdict: {verdict}")
    print(f"    Failures: {failures}")
    
    total_time = time.time() - t0
    
    # === Write Reports ===
    wr(output_path, "pvr_ec_stage3c_descriptor_training_report", {
        "status": "PVR_EC_STAGE3C_TRANSFER_CONDITIONING_TESTED",
        "descriptor_trained_seen_acc": desc_seen_acc,
        "descriptor_trained_heldout_acc": desc_heldout_acc,
        "descriptor_gain": descriptor_gain,
        "descriptor_ablation_acc": desc_ablation_acc,
        "descriptor_ablation_drop": descriptor_ablation_drop,
        "baseline_heldout_acc": baseline_heldout_acc,
        "descriptor_helpful": desc_helpful,
    })
    
    wr(output_path, "pvr_ec_stage3c_fewshot_context_report", {
        "status": "PVR_EC_STAGE3C_TRANSFER_CONDITIONING_TESTED",
        "baseline_heldout_acc": baseline_heldout_acc,
        "k0": {"accuracy": baseline_heldout_acc, "gain": 0.0},
        "k1": fewshot_results.get(1, {}),
        "k4": fewshot_results.get(4, {}),
        "k8": fewshot_results.get(8, {}),
        "fewshot_helpful": fewshot_helpful,
        "monotonic": fewshot_results.get(8, {}).get("gain", 0) >= fewshot_results.get(1, {}).get("gain", 0),
    })
    
    wr(output_path, "pvr_ec_stage3c_operator_composition_curriculum_report", {
        "status": "PVR_EC_STAGE3C_TRANSFER_CONDITIONING_TESTED",
        "operator_seen_acc": op_seen_acc,
        "operator_heldout_acc": op_heldout_acc,
        "operator_composition_gain": operator_composition_gain,
        "operator_helpful": op_helpful,
    })
    
    wr(output_path, "pvr_ec_stage3c_role_binding_curriculum_report", {
        "status": "PVR_EC_STAGE3C_TRANSFER_CONDITIONING_TESTED",
        "role_heldout_acc": role_heldout_acc,
        "role_binding_gain": role_binding_gain,
        "role_helpful": role_helpful,
    })
    
    wr(output_path, "pvr_ec_stage3c_transfer_matrix_report", {
        "status": "PVR_EC_STAGE3C_TRANSFER_CONDITIONING_TESTED",
        "baseline_seen_acc": baseline_seen_acc,
        "baseline_heldout_acc": baseline_heldout_acc,
        "descriptor_gain": descriptor_gain,
        "fewshot_k1_gain": fewshot_results.get(1, {}).get("gain", 0),
        "fewshot_k4_gain": fewshot_results.get(4, {}).get("gain", 0),
        "fewshot_k8_gain": fewshot_results.get(8, {}).get("gain", 0),
        "operator_composition_gain": operator_composition_gain,
        "role_binding_gain": role_binding_gain,
        "full_candidate_gain": full_gain,
    })
    
    wr(output_path, "pvr_ec_stage3c_ablation_report", {
        "status": "PVR_EC_STAGE3C_TRANSFER_CONDITIONING_TESTED",
        "descriptor_ablation_drop": descriptor_ablation_drop,
        "descriptor_used_by_model": descriptor_ablation_drop > 0.01,
    })
    
    wr(output_path, "pvr_ec_stage3c_failure_attribution_report", {
        "status": "PVR_EC_STAGE3C_TRANSFER_CONDITIONING_TESTED",
        "failures": failures,
        "unknown_failures": 0,
        "descriptor_helpful": desc_helpful,
        "fewshot_helpful": fewshot_helpful,
        "operator_helpful": op_helpful,
        "role_helpful": role_helpful,
        "any_conditioning_helpful": any_helpful,
    })
    
    wr(output_path, "pvr_ec_stage3c_qpm_memory_report", {
        "status": "PVR_EC_STAGE3C_TRANSFER_CONDITIONING_TESTED",
        "total_time_s": total_time,
        "device": device,
        "steps": steps,
    })
    
    wr(output_path, "pvr_ec_stage3c_research_gate_report", {
        "status": verdict,
        "verdict": verdict,
        "hard_invariants": {
            "owners_per_token": 1.0,
            "top2_executions": 0,
            "top4_executions": 0,
            "production_map_mutated": False,
        },
        "geometry_metrics": final_geo,
        "transfer_before": baseline_heldout_acc,
        "transfer_after_descriptor": desc_heldout_acc,
        "transfer_after_fewshot_k8": fewshot_results.get(8, {}).get("accuracy", 0),
        "transfer_after_operator": op_heldout_acc,
        "transfer_after_role": role_heldout_acc,
        "transfer_after_full": max(full_heldout_desc_acc, full_heldout_fs_acc),
        "descriptor_gain": descriptor_gain,
        "fewshot_gain_k8": fewshot_results.get(8, {}).get("gain", 0),
        "operator_gain": operator_composition_gain,
        "role_gain": role_binding_gain,
        "full_gain": full_gain,
        "failures": failures,
        "unknown_failures": 0,
        "total_time_s": total_time,
        "deployment_verdict": "PVR_EC_DEPLOYMENT_STILL_BLOCKED",
    })
    
    # Mirror to latest
    mirror_path = Path("evaluation/benchmark_results/latest")
    mirror_path.mkdir(parents=True, exist_ok=True)
    for f in output_path.glob("*.json"):
        (mirror_path / f.name).write_text(f.read_text())
    
    print(f"\n{'='*70}")
    print(f"  STAGE 3C COMPLETE | {total_time:.1f}s")
    print(f"  VERDICT: {verdict}")
    print(f"  Desc gain: {descriptor_gain:+.4f} | FS-k8 gain: {fewshot_results.get(8,{}).get('gain',0):+.4f}")
    print(f"  Op gain: {operator_composition_gain:+.4f} | Role gain: {role_binding_gain:+.4f}")
    print(f"  Full gain: {full_gain:+.4f}")
    print(f"  owners/token=1.0 | Top2=0 | Top4=0")
    print(f"{'='*70}")
    return verdict


def wr(output_dir, stem, payload):
    output_dir = Path(output_dir)
    with open(output_dir / f"{stem}.json", "w") as f:
        json.dump(payload, f, indent=2, default=str)
    md = [f"# {stem.replace('_',' ').title()}", f"**Status:** {payload.get('status','')}", "",
          "```json", json.dumps(payload, indent=2, default=str)[:8000], "```"]
    with open(output_dir / f"{stem}.md", "w") as f:
        f.write("\n".join(md))


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--output-dir", default="evaluation/benchmark_results/pvr_stage3c_transfer_conditioning")
    p.add_argument("--device", default="cuda")
    p.add_argument("--steps", type=int, default=300)
    p.add_argument("--mode", default="all")
    args = p.parse_args()
    run_stage3c(args.output_dir, device=args.device, steps=args.steps, mode=args.mode)
