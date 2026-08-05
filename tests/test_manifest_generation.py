import hashlib
import json
from pathlib import Path

from benchmark.scripts.generate_model_size_matrix import generate


REQUIRED_MANIFEST_FIELDS = {"schema_version", "created_at", "git_commit", "source_paths", "hashes", "environment", "notes"}


def test_manifests_are_generated_and_hashable(tmp_path):
    generate(tmp_path)
    manifest_dir = tmp_path / "benchmark" / "manifests"
    expected = [
        "training_data_manifest.json",
        "eval_manifest.json",
        "contamination_scan_manifest.json",
        "hardware_manifest.json",
        "reproducibility_manifest.json",
        "model_registry_manifest.json",
        "model_size_matrix_manifest.json",
    ]
    for name in expected:
        path = manifest_dir / name
        assert path.exists()
        payload = json.loads(path.read_text())
        if name != "model_size_matrix_manifest.json":
            assert REQUIRED_MANIFEST_FIELDS <= set(payload)
        assert hashlib.sha256(path.read_bytes()).hexdigest()

