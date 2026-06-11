"""Python-focused model training configurations.

Three tiers:
- PYTHON_24M_DEBUG: Fast iteration, debug runs (24M params)
- PYTHON_60M_MINI: Moderate training (60M params)
- PYTHON_100M_MICRO: Full micro training (100M params)
"""

PYTHON_24M_DEBUG = {
    "name": "debug",
    "description": "24M param debug config for fast iteration",
    "model": {
        "vocab_size": 50176,
        "d_model": 192,
        "n_layers": 4,
        "n_heads": 6,
        "d_ff": 768,
        "max_seq_len": 1024,
        "dropout": 0.1,
    },
    "training": {
        "batch_size": 4,
        "grad_accum_steps": 1,
        "lr": 3e-4,
        "warmup_steps": 50,
        "max_steps": 500,
        "weight_decay": 0.01,
        "max_grad_norm": 1.0,
        "eval_every": 50,
        "save_every": 100,
        "log_every": 10,
    },
    "data": {
        "max_seq_len": 1024,
        "curriculum_stage": "C",
        "num_examples": 200,
        "eval_split_ratio": 0.1,
    },
    "runtime": {
        "schema_hash_required": True,
        "runtime_contract_version": "1.0",
        "target_kind": "python",
    },
}

PYTHON_60M_MINI = {
    "name": "mini",
    "description": "60M param mini config for moderate training",
    "model": {
        "vocab_size": 50176,
        "d_model": 384,
        "n_layers": 8,
        "n_heads": 8,
        "d_ff": 1536,
        "max_seq_len": 2048,
        "dropout": 0.1,
    },
    "training": {
        "batch_size": 8,
        "grad_accum_steps": 2,
        "lr": 2e-4,
        "warmup_steps": 100,
        "max_steps": 2000,
        "weight_decay": 0.01,
        "max_grad_norm": 1.0,
        "eval_every": 100,
        "save_every": 500,
        "log_every": 20,
    },
    "data": {
        "max_seq_len": 2048,
        "curriculum_stage": "C",
        "num_examples": 1000,
        "eval_split_ratio": 0.1,
    },
    "runtime": {
        "schema_hash_required": True,
        "runtime_contract_version": "1.0",
        "target_kind": "python",
    },
}

PYTHON_100M_MICRO = {
    "name": "micro",
    "description": "100M param micro config for full training",
    "model": {
        "vocab_size": 50176,
        "d_model": 512,
        "n_layers": 12,
        "n_heads": 8,
        "d_ff": 2048,
        "max_seq_len": 2048,
        "dropout": 0.1,
    },
    "training": {
        "batch_size": 16,
        "grad_accum_steps": 4,
        "lr": 1e-4,
        "warmup_steps": 200,
        "max_steps": 5000,
        "weight_decay": 0.01,
        "max_grad_norm": 1.0,
        "eval_every": 200,
        "save_every": 1000,
        "log_every": 50,
    },
    "data": {
        "max_seq_len": 2048,
        "curriculum_stage": "C",
        "num_examples": 5000,
        "eval_split_ratio": 0.1,
    },
    "runtime": {
        "schema_hash_required": True,
        "runtime_contract_version": "1.0",
        "target_kind": "python",
    },
}

_CONFIGS = {
    "debug": PYTHON_24M_DEBUG,
    "mini": PYTHON_60M_MINI,
    "micro": PYTHON_100M_MICRO,
}


def get_config(name: str) -> dict:
    """Get config by name. Raises KeyError if not found."""
    if name not in _CONFIGS:
        raise KeyError(f"Unknown config '{name}'. Available: {list(_CONFIGS.keys())}")
    return _CONFIGS[name]
