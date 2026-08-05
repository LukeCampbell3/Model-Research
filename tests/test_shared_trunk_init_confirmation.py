from benchmark.common import write_json
from benchmark.runners.run_shared_trunk_init_confirmation import (
    CANDIDATE_STATUS,
    CONFIRMED_STATUS,
    STATUS_300M_DENSE_GAP_CLOSED,
    STATUS_300M_INVARIANT_FAILED,
    STATUS_300M_NOT_SUPPORTED,
    STATUS_300M_REPAIR_SUPPORTED,
    _status_for_size,
    aggregate,
)


def _seed_report(path, seed, status):
    write_json(path, {
        "seed": seed,
        "status": status,
        "summary": {
            "rows": {
                "shared_trunk_init_from_dense": {
                    "route_stable": True,
                    "deltas": {
                        "final_train_loss_delta_vs_baseline": -0.1,
                        "mean_eval_loss_delta_vs_baseline": -1.0,
                    },
                }
            }
        },
    })


def test_shared_trunk_init_aggregate_requires_repeat_seed(tmp_path):
    one = tmp_path / "seed1.json"
    _seed_report(one, 1, "PVR_SHARED_TRUNK_INIT_SUPPORTED")
    payload = aggregate([str(one)], output=str(tmp_path / "one"))
    assert payload["status"] == CANDIDATE_STATUS
    two = tmp_path / "seed2.json"
    _seed_report(two, 2, "PVR_SHARED_TRUNK_INIT_SUPPORTED")
    payload = aggregate([str(one), str(two)], output=str(tmp_path / "two"))
    assert payload["status"] == CONFIRMED_STATUS


def test_300m_status_mapping_uses_dense_gap_and_invariants():
    summary = {
        "status": "PVR_SHARED_TRUNK_INIT_SUPPORTED",
        "rows": {
            "shared_trunk_init_from_dense": {
                "top1_invariants_clean": True,
                "route_stable": True,
                "loss_supported": True,
                "mean_eval_loss": 3.0,
            }
        },
    }
    assert _status_for_size("300m", summary, {"mean_eval_loss": 3.5}) == STATUS_300M_DENSE_GAP_CLOSED
    assert _status_for_size("300m", summary, {"mean_eval_loss": 2.5}) == STATUS_300M_REPAIR_SUPPORTED
    summary["rows"]["shared_trunk_init_from_dense"]["loss_supported"] = False
    assert _status_for_size("300m", summary, {"mean_eval_loss": 3.5}) == STATUS_300M_NOT_SUPPORTED
    summary["rows"]["shared_trunk_init_from_dense"]["loss_supported"] = True
    summary["rows"]["shared_trunk_init_from_dense"]["top1_invariants_clean"] = False
    assert _status_for_size("300m", summary, {"mean_eval_loss": 3.5}) == STATUS_300M_INVARIANT_FAILED
