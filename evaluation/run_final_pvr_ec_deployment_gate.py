"""PVR-EC-O Final Deployment-Candidate Gate.

Validates: repeatability, QPM/memory, calibration, descriptor control,
task regression, failure observatory, and forward purity.
"""

import json, sys, time, math, hashlib
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "sparse_loop_moe" / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import torch
import torch.nn.functional as F
import numpy as np

from sparse_loop_moe.models.pvr_ec.pvr_ec_model import PVRECModel, PVRECModelConfig
from sparse_loop_moe.models.pvr_ec.nlp_stage2_tasks import NLP_STAGE2_TASKS, generate_stage2_batch
from sparse_loop_moe.models.pvr_ec.family_preservation import compute_family_membership

ALL_TASKS = list(NLP_STAGE2_TASKS)
DESC_START, DESC_END = 100, 101
TASK_TOKENS = {t: 102+i for i, t in enumerate(ALL_TASKS)}

def safe_mean(v):
    f=[x for x in v if not math.isnan(x) and not math.isinf(x)]
    return float(np.mean(f)) if f else float("nan")

def build_model(device, max_seq_len=256):
    config = PVRECModelConfig(vocab_size=256, d_model=128, max_seq_len=max_seq_len,
        n_layers=2, n_heads=4, d_ff=256, num_experts=4, num_prototypes=16,
        max_k=4, d_expert=64, pvr_deploy_mode="top1", dropout=0.0, pvr_expert_delta_scale=1.0)
    return PVRECModel(config).to(device)

def gen_desc(task, bs=32, msl=256, seed=42, include_desc=True):
    x, y, m = generate_stage2_batch(task, batch_size=bs, max_seq_len=min(msl-4,60), seed=seed)
    if not include_desc:
        px=torch.zeros(bs,msl,dtype=torch.long); px[:,:x.shape[1]]=x
        py=torch.zeros(bs,msl,dtype=torch.long); py[:,:y.shape[1]]=y
        return px,py,m
    prefix=[DESC_START,TASK_TOKENS.get(task,102),DESC_END]
    nx=torch.zeros(bs,msl,dtype=torch.long); ny=torch.zeros(bs,msl,dtype=torch.long)
    for i in range(bs):
        cx=[t for t in x[i].tolist() if t!=0]; cy=[t for t in y[i].tolist() if t!=0]
        sx=prefix+cx; sy=[0]*3+cy
        while len(sy)<len(sx): sy.append(0)
        n=min(len(sx),msl); nx[i,:n]=torch.tensor(sx[:n]); ny[i,:n]=torch.tensor(sy[:n])
    return nx,ny,m

def gen_wrong_desc(task, bs=32, msl=256, seed=42):
    """Same input content, wrong descriptor token."""
    x, y, m = generate_stage2_batch(task, batch_size=bs, max_seq_len=min(msl-4,60), seed=seed)
    # Use a different task's descriptor
    wrong_task = [t for t in ALL_TASKS if t != task][0]
    prefix=[DESC_START,TASK_TOKENS[wrong_task],DESC_END]
    nx=torch.zeros(bs,msl,dtype=torch.long); ny=torch.zeros(bs,msl,dtype=torch.long)
    for i in range(bs):
        cx=[t for t in x[i].tolist() if t!=0]; cy=[t for t in y[i].tolist() if t!=0]
        sx=prefix+cx; sy=[0]*3+cy
        while len(sy)<len(sx): sy.append(0)
        n=min(len(sx),msl); nx[i,:n]=torch.tensor(sx[:n]); ny[i,:n]=torch.tensor(sy[:n])
    return nx,ny,m

def train_descriptor(model, tasks, steps, device, seed=42):
    torch.manual_seed(seed)
    opt = torch.optim.AdamW(model.parameters(), lr=3e-3)
    model.train()
    data = [(gen_desc(t, seed=seed)[0].to(device), gen_desc(t, seed=seed)[1].to(device)) for t in tasks]
    for step in range(steps):
        for x, y in data:
            opt.zero_grad(set_to_none=True)
            model(input_ids=x, targets=y)["loss"].backward()
            opt.step()
    return model

def eval_acc(model, tasks, gen_fn, device):
    model.eval(); results={}
    for task in tasks:
        x, y, _ = gen_fn(task)
        x, y = x.to(device), y.to(device)
        with torch.no_grad():
            o=model(input_ids=x, targets=y)
            mask=y!=0
            if not mask.any(): results[task]={"loss":o["loss"].item(),"accuracy":0.0}; continue
            acc=((o["logits"].argmax(-1)==y)&mask).float().sum()/mask.float().sum()
            results[task]={"loss":o["loss"].item(),"accuracy":acc.item()}
    return results

