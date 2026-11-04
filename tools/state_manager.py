#!/usr/bin/env python3
"""
Persistent State Integrity Engine (Layer 3)
Provides atomic disk writes, automated backup & recovery, schema validation,
schema migration, and human decision/override tracking for `.microsaas/state.json`.
"""

import os
import sys
import json
import shutil
from pathlib import Path
from datetime import datetime, timezone
from typing import Dict, Any, Tuple, Optional, List

CURRENT_STATE_VERSION = 6

def get_iso_now() -> str:
    return datetime.now(timezone.utc).isoformat()

def validate_state_dict(data: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """
    Validates state dictionary against required fields and structure
    without requiring third-party libraries.
    """
    errors = []
    required_top = [
        "venture_id", "project_name", "state_version", "last_updated",
        "maturity_stage", "active_capability", "highest_risk_uncertainty",
        "active_hypotheses", "verified_facts", "contradictions",
        "experiments", "decisions", "blocked_actions", "next_best_action"
    ]
    for field in required_top:
        if field not in data:
            errors.append(f"Missing required top-level field: '{field}'")

    if "state_version" in data and not isinstance(data["state_version"], int):
        errors.append("Field 'state_version' must be an integer.")

    if "active_hypotheses" in data and not isinstance(data["active_hypotheses"], list):
        errors.append("Field 'active_hypotheses' must be a list.")

    if "verified_facts" in data and not isinstance(data["verified_facts"], list):
        errors.append("Field 'verified_facts' must be a list.")

    if "contradictions" in data and not isinstance(data["contradictions"], list):
        errors.append("Field 'contradictions' must be a list.")

    if "experiments" in data and not isinstance(data["experiments"], list):
        errors.append("Field 'experiments' must be a list.")

    if "decisions" in data and not isinstance(data["decisions"], list):
        errors.append("Field 'decisions' must be a list.")

    return (len(errors) == 0, errors)

def migrate_state(data: Dict[str, Any], target_version: int = CURRENT_STATE_VERSION) -> Dict[str, Any]:
    """
    Migrates state dictionary across schema versions forward to target_version.
    Ensures backwards compatibility.
    """
    version = data.get("state_version", 1)

    # Version 1 -> 4 additions
    if version < 4:
        if "pre_registered_kill_criteria" not in data:
            data["pre_registered_kill_criteria"] = {
                "archetype": "B_PROSUMER",
                "evaluation_horizon_days": 30,
                "min_sample_size": 200,
                "kill_thresholds": {
                    "min_paid_customers": 5,
                    "min_retention_rate_pct": 50.0,
                    "min_sean_ellis_pmf_pct": 25.0
                }
            }
        version = 4

    # Version 4 -> 5 additions (EVOI and proxy fields in experiments)
    if version < 5:
        for exp in data.get("experiments", []):
            if "evoi_score" not in exp:
                exp["evoi_score"] = 0.0
            if "reversibility" not in exp:
                exp["reversibility"] = 1.0
            if "time_hours" not in exp:
                exp["time_hours"] = 4.0
        version = 5

    # Version 5 -> 6 additions (Override Ledger and provenance citations)
    if version < 6:
        if "override_ledger" not in data:
            data["override_ledger"] = []
        if "events_stream_ref" not in data:
            data["events_stream_ref"] = ".microsaas/events.jsonl"
        version = 6

    data["state_version"] = target_version
    data["last_updated"] = get_iso_now()
    return data

def write_state_atomic(file_path: Path, state_dict: Dict[str, Any]) -> bool:
    """
    Atomically writes state to file_path using temporary file + replace.
    Maintains a .bak copy for disaster recovery.
    """
    file_path = Path(file_path).resolve()
    file_path.parent.mkdir(parents=True, exist_ok=True)

    # Validate before writing
    valid, errors = validate_state_dict(state_dict)
    if not valid:
        raise ValueError(f"State validation failed before write: {', '.join(errors)}")

    temp_path = file_path.with_suffix(".json.tmp")
    bak_path = file_path.with_suffix(".json.bak")

    # Serialize to temp
    with open(temp_path, "w", encoding="utf-8") as f:
        json.dump(state_dict, f, indent=2, ensure_ascii=False)

    # Create backup of current file if it exists
    if file_path.exists():
        try:
            shutil.copy2(file_path, bak_path)
        except Exception:
            pass

    # Atomic replace
    try:
        os.replace(temp_path, file_path)
    except Exception as e:
        if temp_path.exists():
            temp_path.unlink()
        raise IOError(f"Atomic state replace failed: {e}")

    return True

def load_state_safe(file_path: Path) -> Tuple[Dict[str, Any], str]:
    """
    Loads state JSON safely. If corrupt or truncated, recovers from .bak.
    Returns (state_dict, status_message).
    """
    file_path = Path(file_path).resolve()
    bak_path = file_path.with_suffix(".json.bak")

    if not file_path.exists():
        if bak_path.exists():
            shutil.copy2(bak_path, file_path)
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            return (data, "RECOVERED_FROM_BACKUP_PRIMARY_MISSING")
        raise FileNotFoundError(f"State file not found at {file_path}")

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        valid, errors = validate_state_dict(data)
        if not valid:
            raise ValueError(f"Invalid state schema: {errors}")
        return (data, "LOADED_OK")
    except Exception as err:
        # Attempt recovery from backup
        if bak_path.exists():
            try:
                with open(bak_path, "r", encoding="utf-8") as bf:
                    bak_data = json.load(bf)
                valid, _ = validate_state_dict(bak_data)
                if valid:
                    shutil.copy2(bak_path, file_path)
                    return (bak_data, f"RECOVERED_FROM_BACKUP_CORRUPTION: {err}")
            except Exception:
                pass
        raise IOError(f"Failed to load state and backup recovery failed: {err}")

def record_founder_override(
    state_dict: Dict[str, Any],
    recommended_action: str,
    founder_decision: str,
    rationale: str
) -> Dict[str, Any]:
    """
    Appends a founder override record into state_dict['override_ledger'].
    """
    if "override_ledger" not in state_dict:
        state_dict["override_ledger"] = []

    override_record = {
        "id": f"OVR-{len(state_dict['override_ledger']) + 1:03d}",
        "timestamp": get_iso_now(),
        "recommended_action": recommended_action,
        "founder_decision": founder_decision,
        "rationale": rationale
    }
    state_dict["override_ledger"].append(override_record)
    state_dict["last_updated"] = get_iso_now()
    return state_dict

if __name__ == "__main__":
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    print("State Manager module loaded.")
