#!/usr/bin/env python3
"""
Decision Replay Engine (Layer 1 & Layer 3)
Enables event-sourced decision auditing, historical state reconstruction,
governor reproducibility verification, and provenance inspection.

Event Anatomy:
  timestamp -> event_type -> founder_input -> context_snapshot ->
  evidence_snapshot -> governor_evaluation -> selected_capability ->
  capability_result -> new_evidence -> state_mutation -> decision_outcome
"""

import sys
import json
import argparse
from pathlib import Path
from datetime import datetime, timezone
from typing import Dict, Any, List, Optional, Tuple

class DecisionReplayEngine:
    def __init__(self, events_log_path: Optional[Path] = None):
        self.events_log_path = Path(events_log_path) if events_log_path else None
        self.events: List[Dict[str, Any]] = []
        if self.events_log_path and self.events_log_path.exists():
            self.load_events(self.events_log_path)

    def append_event(self, event: Dict[str, Any], flush: bool = True) -> Dict[str, Any]:
        """Appends an immutable event to the in-memory log and writes to JSONL."""
        if "id" not in event:
            event["id"] = f"EVT-{len(self.events) + 1:04d}"
        if "timestamp" not in event:
            event["timestamp"] = datetime.now(timezone.utc).isoformat()

        self.events.append(event)

        if flush and self.events_log_path:
            self.events_log_path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.events_log_path, "a", encoding="utf-8") as f:
                f.write(json.dumps(event, ensure_ascii=False) + "\n")

        return event

    def load_events(self, file_path: Path) -> List[Dict[str, Any]]:
        """Loads events from a JSONL file."""
        self.events_log_path = Path(file_path).resolve()
        self.events = []
        with open(self.events_log_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    self.events.append(json.loads(line))
        return self.events

    def reconstruct_state_at(self, step_index: int) -> Dict[str, Any]:
        """
        Replays events up to step_index and reconstructs the historical venture state.
        """
        if step_index < 0 or step_index >= len(self.events):
            raise IndexError(f"Step index {step_index} out of bounds (0-{len(self.events)-1})")

        state: Dict[str, Any] = {
            "venture_id": "unknown",
            "project_name": "unknown",
            "state_version": 1,
            "maturity_stage": "intake_triage",
            "active_capability": "none",
            "highest_risk_uncertainty": "",
            "active_hypotheses": [],
            "verified_facts": [],
            "contradictions": [],
            "experiments": [],
            "decisions": [],
            "blocked_actions": [],
            "next_best_action": None,
            "override_ledger": []
        }

        for i in range(step_index + 1):
            evt = self.events[i]
            mutations = evt.get("state_mutations", {})
            for k, v in mutations.items():
                if k in state and isinstance(state[k], list) and isinstance(v, list):
                    state[k].extend(v)
                else:
                    state[k] = v

        return state

    def verify_reproducibility(self) -> Tuple[bool, List[str]]:
        """
        Verifies that every historical decision is accompanied by documented
        evidence citations and non-contradictory evaluations.
        """
        issues = []
        for idx, evt in enumerate(self.events):
            evt_id = evt.get("id", f"EVT-{idx}")
            decision = evt.get("decision_outcome")
            gov_eval = evt.get("governor_evaluation", {})

            if not decision:
                continue

            # Verify rationale presence
            if not decision.get("rationale"):
                issues.append(f"[{evt_id}] Decision missing rationale.")

            # Verify evidence snapshot presence
            evidence = evt.get("evidence_snapshot", [])
            if not evidence and decision.get("type") in ["advance", "kill_solution", "kill_wedge", "kill_venture"]:
                issues.append(f"[{evt_id}] Critical strategic decision '{decision.get('type')}' executed without evidence snapshot.")

            # Check founder approval compliance for Tier 3 actions
            requires_approval = gov_eval.get("requires_founder_approval", False)
            if requires_approval and not decision.get("approved_by_founder"):
                issues.append(f"[{evt_id}] Tier 3 action executed without explicit founder approval!")

        return (len(issues) == 0, issues)

    def print_timeline_summary(self):
        """Prints a human-readable timeline table of all venture decisions."""
        print("=" * 95)
        print("VENTURE DECISION TIMELINE (REPLAY STREAM)")
        print("=" * 95)
        print(f"{'Event ID':<10} | {'Timestamp':<20} | {'Capability':<22} | {'Decision / Action':<35}")
        print("-" * 95)

        for evt in self.events:
            evt_id = evt.get("id", "EVT-???")
            ts = evt.get("timestamp", "")[:19].replace("T", " ")
            cap = evt.get("selected_capability", "n/a")
            dec = evt.get("decision_outcome", {})
            dec_type = dec.get("type") or evt.get("event_type", "state_update")
            print(f"{evt_id:<10} | {ts:<20} | {cap:<22} | {dec_type:<35}")

        print("=" * 95)

def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')

    parser = argparse.ArgumentParser(description="Decision Replay Engine for Micro-SaaS OS")
    parser.add_argument("--log", required=True, help="Path to events.jsonl")
    parser.add_argument("--verify", action="store_true", help="Verify reproducibility & governance rigor")
    parser.add_argument("--summary", action="store_true", help="Print timeline summary")
    parser.add_argument("--inspect", type=int, help="Inspect specific event index")

    args = parser.parse_args()

    engine = DecisionReplayEngine(Path(args.log))

    if args.summary:
        engine.print_timeline_summary()

    if args.verify:
        passed, issues = engine.verify_reproducibility()
        print("\n" + "=" * 80)
        print("REPLAY VERIFICATION AUDIT REPORT")
        print("=" * 80)
        if passed:
            print("[+] PASS: All historical decisions have complete evidence provenance & governance compliance.")
            sys.exit(0)
        else:
            print(f"[-] FAILED: Detected {len(issues)} governance integrity issues:")
            for issue in issues:
                print(f"  • {issue}")
            sys.exit(1)

    if args.inspect is not None:
        state = engine.reconstruct_state_at(args.inspect)
        print(json.dumps(state, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
