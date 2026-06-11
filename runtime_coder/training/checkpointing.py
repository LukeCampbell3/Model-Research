"""Checkpoint save/load utilities for RuntimeCoder training.

Supports saving and loading model, optimizer, and training state.
"""

import os
from typing import Dict, Any, Optional

import torch
import torch.nn as nn


def save_checkpoint(
    model: nn.Module,
    optimizer: torch.optim.Optimizer,
    step: int,
    path: str,
    extra_state: Optional[Dict[str, Any]] = None,
) -> str:
    """Save a training checkpoint.

    Args:
        model: Model to save.
        optimizer: Optimizer to save.
        step: Current training step.
        path: Directory or file path for checkpoint.
        extra_state: Optional additional state to save.

    Returns:
        Path where checkpoint was saved.
    """
    # Ensure directory exists
    if path.endswith(".pt") or path.endswith(".pth"):
        save_path = path
        os.makedirs(os.path.dirname(path), exist_ok=True)
    else:
        os.makedirs(path, exist_ok=True)
        save_path = os.path.join(path, f"checkpoint_step_{step}.pt")

    checkpoint = {
        "step": step,
        "model_state_dict": model.state_dict(),
        "optimizer_state_dict": optimizer.state_dict(),
    }

    if extra_state:
        checkpoint["extra_state"] = extra_state

    torch.save(checkpoint, save_path)
    return save_path


def load_checkpoint(
    path: str,
    model: nn.Module,
    optimizer: Optional[torch.optim.Optimizer] = None,
    device: str = "cpu",
) -> Dict[str, Any]:
    """Load a training checkpoint.

    Args:
        path: Path to checkpoint file.
        model: Model to load state into.
        optimizer: Optional optimizer to load state into.
        device: Device to map tensors to.

    Returns:
        Dict with 'step' and optionally 'extra_state'.

    Raises:
        FileNotFoundError: If checkpoint path doesn't exist.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Checkpoint not found: {path}")

    checkpoint = torch.load(path, map_location=device, weights_only=False)

    model.load_state_dict(checkpoint["model_state_dict"])

    if optimizer is not None and "optimizer_state_dict" in checkpoint:
        optimizer.load_state_dict(checkpoint["optimizer_state_dict"])

    result = {"step": checkpoint["step"]}
    if "extra_state" in checkpoint:
        result["extra_state"] = checkpoint["extra_state"]

    return result


def find_latest_checkpoint(directory: str) -> Optional[str]:
    """Find the latest checkpoint in a directory.

    Args:
        directory: Directory to search for checkpoints.

    Returns:
        Path to latest checkpoint, or None if none found.
    """
    if not os.path.isdir(directory):
        return None

    checkpoints = []
    for f in os.listdir(directory):
        if f.startswith("checkpoint_step_") and f.endswith(".pt"):
            try:
                step = int(f.replace("checkpoint_step_", "").replace(".pt", ""))
                checkpoints.append((step, os.path.join(directory, f)))
            except ValueError:
                continue

    if not checkpoints:
        return None

    # Return the one with highest step number
    checkpoints.sort(key=lambda x: x[0], reverse=True)
    return checkpoints[0][1]
