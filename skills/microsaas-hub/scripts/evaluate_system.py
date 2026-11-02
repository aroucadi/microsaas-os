#!/usr/bin/env python3
"""
AI Skill System Evaluation Scorecard
Measures the AI System's Auditing Performance (The Judge) on a specific business opportunity.
Explicitly separates the Business Idea's Viability Verdict from the AI Auditor's Competence Score.
"""

import sys
import argparse
import json
from pathlib import Path
from datetime import datetime

DIMENSIONS = [
    {
        "id": "correctness",
        "name": "Correctness",
        "weight": 0.20,
        "question": "Does the AI produce factually correct outputs without hallucination?"
    },
    {
        "id": "evidence_quality",
        "name": "Evidence Quality",
        "weight": 0.20,
        "question": "Are all market claims, pricing, and competitors grounded in verifiable sources?"
    },
    {
        "id": "decision_quality",
        "name": "Decision Quality",
        "weight": 0.20,
        "question": "Did the AI make the right GO / NO-GO / PIVOT call (especially killing bad ideas)?"
    },
    {
        "id": "execution_quality",
        "name": "Execution Quality",
        "weight": 0.15,
        "question": "Can the generated deliverables (brief, specs, scripts) actually be used in production?"
    },
    {
        "id": "consistency",
        "name": "Consistency",
        "weight": 0.10,
        "question": "Does the system apply the same rigorous standards across different business models?"
    },
    {
        "id": "state_management",
        "name": "State Management",
        "weight": 0.05,
        "question": "Does the system maintain decisions and evidence across sessions without context loss?"
    },
    {
        "id": "commercial_outcomes",
        "name": "Commercial Realism",
        "weight": 0.10,
        "question": "Are unit economics, monetization models, and conversion assumptions realistic?"
    }
]

def calculate_score(scores):
    weighted_total = 0.0
    breakdown = []
    
    for d in DIMENSIONS:
        val = scores.get(d["id"])
        score = float(val) if val is not None else 0.0
        score = max(0.0, min(10.0, score))
        weighted = score * d["weight"]
        weighted_total += weighted
        breakdown.append({
            "name": d["name"],
            "weight_pct": int(d["weight"] * 100),
            "question": d["question"],
            "score": score,
            "weighted": weighted
        })
        
    return weighted_total, breakdown

def generate_markdown(project_name, idea_verdict, idea_score, weighted_total, breakdown, notes=""):
    auditor_grade = "PASSED / HIGH RIGOR" if weighted_total >= 8.0 else ("PROVISIONAL / NEEDS SCRUTINY" if weighted_total >= 6.5 else "FAILED / UNRELIABLE")
    
    verdict_badge = {
        "NO-GO": "🔴 REJECTED / NO-GO (Idea Terminated)",
        "KILL": "🔴 REJECTED / NO-GO (Idea Terminated)",
        "PIVOT": "🟡 CONDITIONAL PIVOT (Repackaging Required)",
        "GO": "🟢 APPROVED / GO (Proceed to Validation/Build)"
    }.get(idea_verdict.upper(), f"⚪ {idea_verdict}")

    lines = [
        f"# AI Skill System Evaluation Scorecard",
        f"",
        f"> **Important Distinction:**",
        f"> 1. **Commercial Idea Verdict:** Evaluates whether the *business idea* is worth building.",
        f"> 2. **AI Auditor Competence Score:** Evaluates how well the *AI system* performed its job as an unyielding, evidence-based co-founder.",
        f"",
        f"---",
        f"",
        f"### 1. Business Opportunity Outcome",
        f"- **Subject Idea:** {project_name}",
        f"- **Commercial Verdict:** **{verdict_badge}**",
        f"- **Idea Moat / Viability Score:** {idea_score if idea_score else 'Audited via Moat Scorecard'}",
        f"",
        f"---",
        f"",
        f"### 2. AI Auditor Competence Assessment",
        f"- **AI Auditor Quality Score:** **{weighted_total:.2f} / 10.00**",
        f"- **System Evaluation Status:** **{auditor_grade}**",
        f"- **Evaluation Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"",
        f"| Dimension | Weight | AI Score (0–10) | Weighted Points | Evaluation Question |",
        f"| :--- | :---: | :---: | :---: | :--- |"
    ]
    
    for b in breakdown:
        lines.append(f"| **{b['name']}** | {b['weight_pct']}% | {b['score']:.1f} / 10 | {b['weighted']:.2f} | {b['question']} |")
        
    lines.extend([
        f"",
        f"**Total Weighted Competence:** **{weighted_total:.2f} / 10.00**",
        f"",
        f"---",
        f"",
        f"### 3. Evaluator Findings & Observations",
        f"{notes if notes else 'System evaluated against observable evidence, competitive benchmarks, and decision integrity.'}",
        f""
    ])
    
    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(description="Evaluate the AI Micro-SaaS Skill System")
    parser.add_argument("--project", default="Micro-SaaS Project", help="Name of evaluated project")
    parser.add_argument("--idea-verdict", default="NO-GO", choices=["GO", "PIVOT", "NO-GO", "KILL"], help="Commercial verdict of the idea")
    parser.add_argument("--idea-score", default="", help="Score of the idea (e.g. '11/30 (Fails Threshold)')")
    parser.add_argument("--correctness", type=float, default=None, help="Score 0-10")
    parser.add_argument("--evidence", type=float, default=None, help="Evidence quality 0-10")
    parser.add_argument("--decision", type=float, default=None, help="Decision quality 0-10")
    parser.add_argument("--execution", type=float, default=None, help="Execution quality 0-10")
    parser.add_argument("--consistency", type=float, default=None, help="Consistency 0-10")
    parser.add_argument("--state", type=float, default=None, help="State management 0-10")
    parser.add_argument("--commercial", type=float, default=None, help="Commercial realism 0-10")
    parser.add_argument("--input-json", help="Path to JSON file containing scores")
    parser.add_argument("--output-md", help="Path to write the markdown scorecard report")
    parser.add_argument("--notes", default="", help="Optional notes")

    args = parser.parse_args()

    scores = {}
    if args.input_json and Path(args.input_json).exists():
        with open(args.input_json, "r", encoding="utf-8") as f:
            scores = json.load(f)

    # CLI args override JSON
    if args.correctness is not None: scores["correctness"] = args.correctness
    if args.evidence is not None: scores["evidence_quality"] = args.evidence
    if args.decision is not None: scores["decision_quality"] = args.decision
    if args.execution is not None: scores["execution_quality"] = args.execution
    if args.consistency is not None: scores["consistency"] = args.consistency
    if args.state is not None: scores["state_management"] = args.state
    if args.commercial is not None: scores["commercial_outcomes"] = args.commercial

    weighted_total, breakdown = calculate_score(scores)
    md_report = generate_markdown(args.project, args.idea_verdict, args.idea_score, weighted_total, breakdown, args.notes)

    print(md_report)

    if args.output_md:
        out_path = Path(args.output_md)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(md_report)
        print(f"\n[+] Saved evaluation scorecard to: {out_path.resolve()}", file=sys.stderr)

if __name__ == "__main__":
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    main()
