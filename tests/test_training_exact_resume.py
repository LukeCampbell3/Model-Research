import json
from pathlib import Path

import torch

from benchmark.runners.run_training import run


def _write_config(root: Path, name: str, checkpoint_path: Path) -> Path:
    root.mkdir(parents=True, exist_ok=True)
    train = root / "train.txt"
    eval_file = root / "eval.txt"
    train.write_text(("abcdef0123456789\n" * 64), encoding="utf-8")
    eval_file.write_text(("0123abcdef9876\n" * 8), encoding="utf-8")
    config = {
        "model_variant": name,
        "model_family": "dense_transformer",
        "total_params": 10000,
        "vocab_size": 256,
        "hidden_size": 16,
        "num_layers": 1,
        "num_heads": 2,
        "context_length": 16,
        "materialization_ffn_size": 32,
        "num_experts_if_applicable": 0,
        "experts_active_per_token": 0,
        "training_data_paths": [str(train)],
        "eval_data_paths": [str(eval_file)],
        "checkpoint_path": str(checkpoint_path),
    }
    path = root / f"{name}.json"
    path.write_text(json.dumps(config), encoding="utf-8")
    return path


def _write_suite(root: Path, config_path: Path) -> Path:
    suite = root / f"{config_path.stem}_suite.json"
    suite.write_text(json.dumps({"model_configs": [str(config_path)]}), encoding="utf-8")
    return suite


def _state_dict(path: Path):
    checkpoint = torch.load(path, map_location="cpu", weights_only=False)
    return checkpoint["model_state_dict"], checkpoint


def test_exact_resume_matches_uninterrupted_cpu_run(tmp_path):
    full_config = _write_config(tmp_path / "full", "resume_smoke", tmp_path / "full" / "checkpoint.pt")
    resumed_config = _write_config(tmp_path / "resumed", "resume_smoke", tmp_path / "resumed" / "checkpoint.pt")
    full_suite = _write_suite(tmp_path / "full", full_config)
    resumed_suite = _write_suite(tmp_path / "resumed", resumed_config)

    torch.manual_seed(1234)
    full = run(
        str(full_suite),
        str(tmp_path / "full_report"),
        device="cpu",
        max_steps=4,
        batch_size=1,
        seq_len=8,
        lr=1e-3,
        eval_interval=1,
        checkpoint_mode="exact",
    )
    assert full["status"] == "GENUINE_REDUCED_TRAINING_COMPLETE"

    torch.manual_seed(1234)
    interrupted = run(
        str(resumed_suite),
        str(tmp_path / "interrupted_report"),
        device="cpu",
        max_steps=4,
        batch_size=1,
        seq_len=8,
        lr=1e-3,
        eval_interval=1,
        checkpoint_mode="exact",
        simulate_interrupt_after_steps=2,
    )
    assert interrupted["status"] == "TRAINING_FAILED"

    torch.manual_seed(9999)
    resumed = run(
        str(resumed_suite),
        str(tmp_path / "resumed_report"),
        device="cpu",
        max_steps=4,
        batch_size=1,
        seq_len=8,
        lr=1e-3,
        eval_interval=1,
        checkpoint_mode="exact",
    )
    assert resumed["status"] == "GENUINE_REDUCED_TRAINING_COMPLETE"

    full_state, full_checkpoint = _state_dict(tmp_path / "full" / "checkpoint.pt")
    resumed_state, resumed_checkpoint = _state_dict(tmp_path / "resumed" / "checkpoint.pt")
    assert full_checkpoint["checkpoint_kind"] == "EXACT_TRAINING_STATE"
    assert resumed_checkpoint["resume_mode"] == "EXACT_TRAINING_STATE_RESUME"
    assert resumed_checkpoint["optimizer_steps"] == 4
    assert resumed_checkpoint["training_tokens_seen"] == full_checkpoint["training_tokens_seen"]
    for key, value in full_state.items():
        assert torch.allclose(value, resumed_state[key], atol=1e-7, rtol=1e-7), key
