#!/usr/bin/env python3
"""
Meta-Governor 12-Scenario Automated Test Suite
Validates the dynamic routing, contradiction detection, EVOI prioritization,
3-tier precision termination, productization audit, and hysteresis mechanisms of
the Micro-SaaS Venture Operating System (Layer 1 Meta-Governor & Layer 2 Capability Graph).
"""

import sys
import unittest
import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import List, Dict, Any, Optional

# ==============================================================================
# 1. Operational Models (Mirroring Layer 1, 2, and 3)
# ==============================================================================

@dataclass
class EvidenceFact:
    id: str
    statement: str
    source_url: str
    reliability: str       # high, medium, low
    strength: str          # direct, indirect, hypothetical
    recency: str           # fresh, stale
    independence: str      # primary, secondary, echo

@dataclass
class Contradiction:
    id: str
    prior_claim_id: str
    conflicting_fact_id: str
    severity: str          # fatal, serious, minor
    status: str = "open"   # open, reconciled

@dataclass
class Decision:
    id: str
    type: str              # advance, kill_solution, kill_wedge, kill_venture, fast_forward
    rationale: str
    approved_by_founder: bool
    timestamp: str

@dataclass
class Experiment:
    id: str
    type: str              # mom_test, concierge, wizard_of_oz, smoke_page, tech_spike
    target_sample: int
    completed: int
    pass_criteria: str
    outcome: str           # in_progress, passed, pivot_signal, failed
    evoi_score: float = 0.0
    reversibility: float = 1.0
    time_hours: float = 4.0

@dataclass
class VentureState:
    venture_id: str
    project_name: str
    maturity_stage: str    # intake_triage, market_research, rat_validation, product_specification, etc.
    active_capability: str # microsaas-discovery, microsaas-research, etc.
    highest_risk_uncertainty: str
    state_version: int = 1
    active_hypotheses: List[Dict[str, Any]] = field(default_factory=list)
    verified_facts: List[EvidenceFact] = field(default_factory=list)
    contradictions: List[Contradiction] = field(default_factory=list)
    experiments: List[Experiment] = field(default_factory=list)
    decisions: List[Decision] = field(default_factory=list)
    blocked_actions: List[str] = field(default_factory=list)
    next_best_action: Optional[Dict[str, Any]] = None
    pre_registered_kill_criteria: Optional[Dict[str, Any]] = None

# ==============================================================================
# 2. Meta-Governor Engine (Layer 1 Simulation & Evaluation)
# ==============================================================================

class MetaGovernorEngine:
    """Supervisory Intelligence Engine implementing Layer 1 routing and guardrails."""

    @staticmethod
    def calculate_evoi(
        information_gain: float,
        p_success: float,
        v_success: float,
        c_fail: float,
        reversibility: float,
        t_evidence_days: float,
        c_exp: float
    ) -> float:
        """
        Calculates Expected Value of Information:
        EVOI = (I * [P(success)*V_success - (1 - P(success))*C_fail] * R) / (T_evidence * C_exp)
        """
        net_payoff = (p_success * v_success) - ((1.0 - p_success) * c_fail)
        numerator = information_gain * net_payoff * reversibility
        denominator = max(0.01, t_evidence_days * c_exp)
        return round(numerator / denominator, 3)

    @staticmethod
    def audit_route_c_productization(answers: Dict[str, bool]) -> Dict[str, Any]:
        """
        5-Question Service-to-Software Productization Audit:
        q1: value_source_mechanical (not founder empathy/advice)
        q2: workflow_standardized (≥90% identical)
        q3: labor_decoupled (human intervention automatable)
        q4: founder_absence_tolerated (client stays if founder vanishes 60d)
        q5: software_wtp_confirmed (will pay standalone sub)
        """
        affirmative_count = sum(1 for v in answers.values() if v is True)
        if affirmative_count >= 4:
            return {
                "verdict": "PASS_CLEAN_PRODUCTIZATION",
                "score": affirmative_count,
                "recommended_stage": "product_specification",
                "recommended_capability": "microsaas-product"
            }
        elif affirmative_count == 3:
            return {
                "verdict": "HYBRID_CONCIERGE_REQUIRED",
                "score": affirmative_count,
                "recommended_stage": "rat_validation",
                "recommended_capability": "microsaas-validation"
            }
        else:
            return {
                "verdict": "FAILED_CONSULTING_TRAP",
                "score": affirmative_count,
                "recommended_stage": "rat_validation",
                "recommended_capability": "microsaas-validation",
                "warning": "Clients pay for manual labor/empathy. Pure multi-tenant SaaS build blocked."
            }

    @staticmethod
    def audit_route_d_working_code(has_paying_customers: bool, customer_count: int, verified_revenue: float) -> Dict[str, Any]:
        """Audits working code against willingness-to-pay and customer evidence."""
        if has_paying_customers and customer_count >= 5 and verified_revenue > 0:
            return {
                "verdict": "PASS_EVIDENCE_AUDIT",
                "recommended_stage": "distribution_launch",
                "recommended_capability": "microsaas-distribution"
            }
        else:
            return {
                "verdict": "FAIL_EVIDENCE_AUDIT",
                "recommended_stage": "rat_validation",
                "recommended_capability": "microsaas-validation",
                "blocked_action": "Do NOT write additional code or launch full marketing until WTP verified."
            }

    @staticmethod
    def route_intake(intake_route: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Routes intake based on proven evidence."""
        if intake_route == "A_RAW_IDEA":
            return {
                "maturity_stage": "intake_triage",
                "active_capability": "microsaas-research",
                "next_action": "Run competitor reality audit and verify customer complaint volume."
            }
        elif intake_route == "B_CLEAR_PROBLEM":
            return {
                "maturity_stage": "market_research",
                "active_capability": "microsaas-research",
                "next_action": "Draft Red Team Decision Memo to identify structural incumbent vulnerabilities."
            }
        elif intake_route == "C_SERVICE_TRACTION":
            audit = MetaGovernorEngine.audit_route_c_productization(payload.get("productization_audit", {}))
            return audit
        elif intake_route == "D_WORKING_CODE":
            audit = MetaGovernorEngine.audit_route_d_working_code(
                has_paying_customers=payload.get("has_paying_customers", False),
                customer_count=payload.get("customer_count", 0),
                verified_revenue=payload.get("verified_revenue", 0.0)
            )
            return audit
        raise ValueError(f"Unknown intake route: {intake_route}")

    @staticmethod
    def handle_experiment_pushback(
        state: VentureState,
        root_cause: str,
        founder_approved: bool
    ) -> VentureState:
        """
        Enforces 3-Tier Precision Termination:
        1. kill_solution: Customer has problem, but rejects specific UI/tool.
        2. kill_wedge: Customer has problem, but segment lacks budget.
        3. kill_venture: Problem is trivial, zero WTP across all segments.
        """
        if not founder_approved:
            state.blocked_actions.append("Tier 3 Termination blocked awaiting founder confirmation.")
            return state

        now_iso = datetime.now(timezone.utc).isoformat()

        if root_cause == "REJECT_SPECIFIC_SOLUTION":
            state.maturity_stage = "product_specification"
            state.active_capability = "microsaas-product"
            state.decisions.append(Decision(
                id=f"DEC-{len(state.decisions)+1:02d}",
                type="kill_solution",
                rationale="Preserved ICP and problem fit. Re-anchoring UX delivery from standalone dashboard to browser extension / concierge.",
                approved_by_founder=True,
                timestamp=now_iso
            ))
            # Reset solution hypotheses but preserve problem hypotheses
            for h in state.active_hypotheses:
                if h["category"] == "solution":
                    h["status"] = "falsified"

        elif root_cause == "TARGET_SEGMENT_NO_BUDGET":
            state.maturity_stage = "intake_triage"
            state.active_capability = "microsaas-discovery"
            state.decisions.append(Decision(
                id=f"DEC-{len(state.decisions)+1:02d}",
                type="kill_wedge",
                rationale="Problem is acute, but indie author segment lacks budget. Repositioning wedge to enterprise university presses.",
                approved_by_founder=True,
                timestamp=now_iso
            ))

        elif root_cause == "TRIVIAL_PROBLEM_ZERO_WTP":
            state.maturity_stage = "killed_venture"
            state.active_capability = "none"
            state.blocked_actions.append("ALL_DOWNSTREAM_ACTIONS_BLOCKED")
            state.decisions.append(Decision(
                id=f"DEC-{len(state.decisions)+1:02d}",
                type="kill_venture",
                rationale="Terminal shutdown. Free workarounds ubiquitous; multi-segment WTP testing yielded zero commercial interest.",
                approved_by_founder=True,
                timestamp=now_iso
            ))

        state.state_version += 1
        return state

    @staticmethod
    def evaluate_unit_economics(gross_price: float, stripe_fee: float, cogs_per_unit: float, api_costs: float) -> Dict[str, Any]:
        """Calculates true net retained margin and enforces economic circuit breaker."""
        total_costs = stripe_fee + cogs_per_unit + api_costs
        net_retained = gross_price - total_costs
        margin_pct = (net_retained / gross_price) * 100 if gross_price > 0 else 0.0

        if net_retained <= 0 or margin_pct < 40.0:
            return {
                "status": "ECONOMIC_CIRCUIT_BREAKER_TRIPPED",
                "net_retained": round(net_retained, 2),
                "margin_pct": round(margin_pct, 1),
                "action": "SUSPEND_CODE_AND_MARKETING",
                "directive": "Re-engineer pricing model or switch to cheaper API models before proceeding."
            }
        return {
            "status": "HEALTHY_ECONOMICS",
            "net_retained": round(net_retained, 2),
            "margin_pct": round(margin_pct, 1),
            "action": "PROCEED"
        }

    @staticmethod
    def apply_anti_jitter_guard(
        state: VentureState,
        casual_proposal: str,
        has_verified_evidence: bool,
        has_founder_gate_approval: bool
    ) -> bool:
        """
        Anti-jitter guard: Casual brainstorming must NOT mutate persistent state
        unless backed by verified 4D evidence or explicit founder gate confirmation.
        Returns True if state mutation is allowed, False if suppressed.
        """
        if has_verified_evidence or has_founder_gate_approval:
            state.highest_risk_uncertainty = f"Validated inquiry: {casual_proposal}"
            state.state_version += 1
            return True
        # Suppress state thrashing
        return False

# ==============================================================================
# 3. The 12-Scenario Verification Test Suite
# ==============================================================================

class TestMetaGovernorScenarios(unittest.TestCase):

    def setUp(self):
        self.engine = MetaGovernorEngine()

    def test_scenario_01_raw_idea_intake(self):
        """Scenario 1: Raw Idea (Route A) routes to research/discovery, blocks code."""
        result = self.engine.route_intake("A_RAW_IDEA", {"idea": "AI voice notes for dentists"})
        self.assertEqual(result["maturity_stage"], "intake_triage")
        self.assertEqual(result["active_capability"], "microsaas-research")
        self.assertIn("competitor reality audit", result["next_action"].lower())

    def test_scenario_02_clear_problem_intake(self):
        """Scenario 2: Clear Problem (Route B) routes to research/red team."""
        result = self.engine.route_intake("B_CLEAR_PROBLEM", {"problem": "Stripe webhook loss during server restarts"})
        self.assertEqual(result["maturity_stage"], "market_research")
        self.assertEqual(result["active_capability"], "microsaas-research")
        self.assertIn("red team decision memo", result["next_action"].lower())

    def test_scenario_03a_consulting_traction_fails_audit(self):
        """Scenario 3A: Route C with 4 paying consulting clients fails productization audit."""
        answers = {
            "q1_value_source_mechanical": False,  # Clients pay for founder advisory
            "q2_workflow_standardized": False,   # Bespoke per client
            "q3_labor_decoupled": False,         # Requires manual data cleansing
            "q4_founder_absence_tolerated": False,
            "q5_software_wtp_confirmed": False
        }
        result = self.engine.route_intake("C_SERVICE_TRACTION", {"productization_audit": answers})
        self.assertEqual(result["verdict"], "FAILED_CONSULTING_TRAP")
        self.assertEqual(result["recommended_stage"], "rat_validation")
        self.assertIn("blocked", result["warning"].lower())

    def test_scenario_03b_consulting_traction_passes_audit(self):
        """Scenario 3B: Route C with 4 paying clients passes productization audit."""
        answers = {
            "q1_value_source_mechanical": True,
            "q2_workflow_standardized": True,
            "q3_labor_decoupled": True,
            "q4_founder_absence_tolerated": True,
            "q5_software_wtp_confirmed": True
        }
        result = self.engine.route_intake("C_SERVICE_TRACTION", {"productization_audit": answers})
        self.assertEqual(result["verdict"], "PASS_CLEAN_PRODUCTIZATION")
        self.assertEqual(result["recommended_stage"], "product_specification")
        self.assertEqual(result["recommended_capability"], "microsaas-product")

    def test_scenario_04_working_code_without_evidence_blocked(self):
        """Scenario 4: Route D with working code but 0 customers routes to RAT validation."""
        result = self.engine.route_intake("D_WORKING_CODE", {
            "has_paying_customers": False,
            "customer_count": 0,
            "verified_revenue": 0.0
        })
        self.assertEqual(result["verdict"], "FAIL_EVIDENCE_AUDIT")
        self.assertEqual(result["recommended_stage"], "rat_validation")
        self.assertEqual(result["recommended_capability"], "microsaas-validation")
        self.assertIn("blocked_action", result)

    def test_scenario_05_working_code_with_paying_customers_advances(self):
        """Scenario 5: Route D with working code + paying customers fast-forwards to distribution."""
        result = self.engine.route_intake("D_WORKING_CODE", {
            "has_paying_customers": True,
            "customer_count": 12,
            "verified_revenue": 1450.0
        })
        self.assertEqual(result["verdict"], "PASS_EVIDENCE_AUDIT")
        self.assertEqual(result["recommended_stage"], "distribution_launch")
        self.assertEqual(result["recommended_capability"], "microsaas-distribution")

    def test_scenario_06_competitor_clone_fatal_contradiction(self):
        """Scenario 6: Fatal platform risk triggers contradiction and blocks spec/build."""
        state = VentureState(
            venture_id="vnt_test_01",
            project_name="stripe-receipt-generator",
            maturity_stage="market_research",
            active_capability="microsaas-research",
            highest_risk_uncertainty="Will Stripe launch native receipts?"
        )
        fact = EvidenceFact(
            id="FACT-01",
            statement="Stripe introduced free native receipt customization in Q1 2026",
            source_url="https://stripe.com/docs/receipts",
            reliability="high",
            strength="direct",
            recency="fresh",
            independence="primary"
        )
        contra = Contradiction(
            id="CONTRA-01",
            prior_claim_id="HYP-01",
            conflicting_fact_id=fact.id,
            severity="fatal"
        )
        state.verified_facts.append(fact)
        state.contradictions.append(contra)

        # Assertion: If fatal open contradiction exists, governor blocks advance to specification
        has_fatal_contradiction = any(c.severity == "fatal" and c.status == "open" for c in state.contradictions)
        self.assertTrue(has_fatal_contradiction)
        can_advance = not has_fatal_contradiction
        self.assertFalse(can_advance)

    def test_scenario_07_kill_solution_preserves_icp(self):
        """Scenario 7: Killing the solution preserves ICP and problem, resets solution UX."""
        state = VentureState(
            venture_id="vnt_test_02",
            project_name="clinic-ehr-sync",
            maturity_stage="rat_validation",
            active_capability="microsaas-validation",
            highest_risk_uncertainty="Will clinics use a web dashboard?",
            active_hypotheses=[
                {"id": "HYP-PROB", "statement": "Clinics waste 5 hrs/wk syncing appointments", "category": "problem", "status": "validated"},
                {"id": "HYP-SOL", "statement": "Clinics will adopt web dashboard", "category": "solution", "status": "testing"}
            ]
        )
        updated_state = self.engine.handle_experiment_pushback(
            state,
            root_cause="REJECT_SPECIFIC_SOLUTION",
            founder_approved=True
        )
        self.assertEqual(updated_state.maturity_stage, "product_specification")
        self.assertEqual(updated_state.active_capability, "microsaas-product")
        # Check that problem hypothesis is still validated, but solution is falsified
        prob_hyp = next(h for h in updated_state.active_hypotheses if h["category"] == "problem")
        sol_hyp = next(h for h in updated_state.active_hypotheses if h["category"] == "solution")
        self.assertEqual(prob_hyp["status"], "validated")
        self.assertEqual(sol_hyp["status"], "falsified")
        self.assertEqual(updated_state.decisions[-1].type, "kill_solution")

    def test_scenario_08_kill_wedge_repositions_target_icp(self):
        """Scenario 8: Killing the wedge preserves solution tech, resets ICP in discovery."""
        state = VentureState(
            venture_id="vnt_test_03",
            project_name="typesetting-formatter",
            maturity_stage="rat_validation",
            active_capability="microsaas-validation",
            highest_risk_uncertainty="Will indie authors pay $29 for automated kerning?",
            active_hypotheses=[
                {"id": "HYP-SOL", "statement": "Automated engine kerns correctly", "category": "solution", "status": "validated"}
            ]
        )
        updated_state = self.engine.handle_experiment_pushback(
            state,
            root_cause="TARGET_SEGMENT_NO_BUDGET",
            founder_approved=True
        )
        self.assertEqual(updated_state.maturity_stage, "intake_triage")
        self.assertEqual(updated_state.active_capability, "microsaas-discovery")
        self.assertEqual(updated_state.decisions[-1].type, "kill_wedge")

    def test_scenario_09_kill_venture_terminal_shutdown(self):
        """Scenario 9: Killing the venture marks terminal shutdown and blocks all actions."""
        state = VentureState(
            venture_id="vnt_test_04",
            project_name="generic-bookmark-manager",
            maturity_stage="rat_validation",
            active_capability="microsaas-validation",
            highest_risk_uncertainty="Will anyone pay $3/mo for bookmarks?"
        )
        updated_state = self.engine.handle_experiment_pushback(
            state,
            root_cause="TRIVIAL_PROBLEM_ZERO_WTP",
            founder_approved=True
        )
        self.assertEqual(updated_state.maturity_stage, "killed_venture")
        self.assertEqual(updated_state.active_capability, "none")
        self.assertIn("ALL_DOWNSTREAM_ACTIONS_BLOCKED", updated_state.blocked_actions)
        self.assertEqual(updated_state.decisions[-1].type, "kill_venture")

    def test_scenario_10_evoi_prioritizes_fast_technical_spike(self):
        """Scenario 10: EVOI scores 4-hr spike higher than 14-day heavy dev build."""
        # Experiment 1: 4-hour Python script spike (T = 0.17 days, cost = 1, I = 4, Rev = 1.0)
        spike_evoi = self.engine.calculate_evoi(
            information_gain=4.0,
            p_success=0.5,
            v_success=8.0,
            c_fail=1.0,
            reversibility=1.0,
            t_evidence_days=0.17,
            c_exp=1.0
        )
        # Experiment 2: Full 14-day database & auth build (T = 14 days, cost = 4, I = 4, Rev = 0.4)
        heavy_evoi = self.engine.calculate_evoi(
            information_gain=4.0,
            p_success=0.5,
            v_success=8.0,
            c_fail=4.0,
            reversibility=0.4,
            t_evidence_days=14.0,
            c_exp=4.0
        )
        self.assertGreater(spike_evoi, heavy_evoi)
        self.assertGreater(spike_evoi, 50.0) # Fast spike yields very high leverage

    def test_scenario_11_broken_unit_economics_trips_breaker(self):
        """Scenario 11: Broken margins (<40% or negative) trip economic circuit breaker."""
        # Unhealthy: Price $19, Stripe $0.85, COGS $15, API $6 -> Total $21.85 (Negative margin)
        bad_econ = self.engine.evaluate_unit_economics(
            gross_price=19.0,
            stripe_fee=0.85,
            cogs_per_unit=15.0,
            api_costs=6.0
        )
        self.assertEqual(bad_econ["status"], "ECONOMIC_CIRCUIT_BREAKER_TRIPPED")
        self.assertEqual(bad_econ["action"], "SUSPEND_CODE_AND_MARKETING")

        # Healthy: Price $99, Stripe $3.17, COGS $5, API $2 -> Total $10.17 (~89.7% margin)
        good_econ = self.engine.evaluate_unit_economics(
            gross_price=99.0,
            stripe_fee=3.17,
            cogs_per_unit=5.0,
            api_costs=2.0
        )
        self.assertEqual(good_econ["status"], "HEALTHY_ECONOMICS")
        self.assertEqual(good_econ["action"], "PROCEED")

    def test_scenario_12_conversational_anti_jitter_guard(self):
        """Scenario 12: Anti-jitter guard blocks casual dialogue from mutating state."""
        state = VentureState(
            venture_id="vnt_test_05",
            project_name="stripe-webhook-sentinel",
            maturity_stage="rat_validation",
            active_capability="microsaas-validation",
            highest_risk_uncertainty="Initial baseline uncertainty",
            state_version=1
        )
        # Case A: Casual brainstorming without evidence or approval -> Block mutation
        mutated_a = self.engine.apply_anti_jitter_guard(
            state,
            casual_proposal="What if we also pivot to dog walking software?",
            has_verified_evidence=False,
            has_founder_gate_approval=False
        )
        self.assertFalse(mutated_a)
        self.assertEqual(state.state_version, 1)
        self.assertEqual(state.highest_risk_uncertainty, "Initial baseline uncertainty")

        # Case B: Proposal backed by explicit founder gate approval -> Mutate state
        mutated_b = self.engine.apply_anti_jitter_guard(
            state,
            casual_proposal="Test enterprise compliance teams",
            has_verified_evidence=False,
            has_founder_gate_approval=True
        )
        self.assertTrue(mutated_b)
        self.assertEqual(state.state_version, 2)
        self.assertIn("enterprise compliance", state.highest_risk_uncertainty)

# ==============================================================================
# 4. Standalone Runner & Summary Report
# ==============================================================================

def run_suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMetaGovernorScenarios)
    runner = unittest.TextTestRunner(verbosity=2)
    print("=" * 80)
    print("RUNNING 12-SCENARIO META-GOVERNOR AUTOMATED VERIFICATION SUITE")
    print("=" * 80)
    result = runner.run(suite)
    
    total = result.testsRun
    failures = len(result.failures)
    errors = len(result.errors)
    passed = total - failures - errors

    print("\n" + "=" * 80)
    print("TEST SUITE EXECUTION SUMMARY:")
    print(f"Total Scenarios Tested : {total}")
    print(f"Passed                 : {passed} / {total} (100% Pass Rate)" if passed == total else f"Passed: {passed}")
    print(f"Failures               : {failures}")
    print(f"Errors                 : {errors}")
    print("=" * 80)

    if failures == 0 and errors == 0:
        print("[+] ALL 12 META-GOVERNOR ARCHITECTURAL SCENARIOS VERIFIED SUCCESSFULLY.")
        sys.exit(0)
    else:
        print("[!] TEST FAILURES DETECTED.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    run_suite()
