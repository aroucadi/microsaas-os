# Micro-SaaS Founder OS 🚀

> **The Idea-to-Market Agentic Operating System for Google Antigravity.**  
> *Transforming AI coding agents from reactive code generators into disciplined, evidence-driven startup co-founders.*

[![Antigravity Compatible](https://img.shields.io/badge/Antigravity-Agent_Skills-blue.svg)](https://antigravity.google)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-3776AB.svg?logo=python&logoColor=white)](https://python.org)
[![Methodology: Lean + YC](https://img.shields.io/badge/Methodology-YC%20%7C%20Lean%20Startup%20%7C%20Mom%20Test-orange.svg)](#the-9-stage-lifecycle)
[![Stage Gated: 100%](https://img.shields.io/badge/Stage_Gates-Strict_Falsification-emerald.svg)](#epistemic-rigor--evidence-hierarchy)

---

## 💡 The Manifesto: Zero Premature Code

The #1 reason micro-SaaS projects fail is not bad software engineering—it is **building things nobody wants or is willing to pay for**.

Traditional AI coding assistants eagerly write thousands of lines of boilerplate, scaffolding, databases, and OAuth flows for ideas that should have been killed in under 15 minutes of competitive research.

**Micro-SaaS Founder OS** enforces an unyielding discipline: **Zero code is generated until an opportunity survives adversarial red teaming, customer discovery, and willingness-to-pay validation.**

---

## 🏛️ System Architecture

Micro-SaaS Founder OS organizes the startup journey into a 9-stage disciplined pipeline orchestrated by `microsaas-hub` and executed across 7 specialized Antigravity skills.

```mermaid
flowchart TD
    subgraph Discovery & Research
        S1["Stage 1: Opportunity Hunting<br/><code>microsaas-discovery</code>"] -->|"Score >= 24/35"| S2["Stage 2: Competitive Intelligence & Moat Audit<br/><code>microsaas-research</code>"]
        S1 -.->|"Score < 24"| DROP1["❌ REJECT (Drop Idea)"]
        S2 -->|"Moat >= 18/30 + Red Team Clear"| S3["Stage 3: Customer Discovery & WTP Validation<br/><code>microsaas-validation</code>"]
        S2 -.->|"Fatal Red Team Trap"| DROP2["🔴 REJECT / NO-GO"]
    end

    subgraph Product & Definition
        S3 -->|"Commitment Gate Passed"| S4["Stage 4: PR/FAQ & Spec-Driven Development (SDD)<br/><code>microsaas-product</code>"]
        S3 -.->|"Fluff / Zero WTP"| DROP3["🔄 PIVOT or KILL"]
        S4 --> S5["Stage 5: High-Converting Smoke Page<br/>(Value Prop, Pricing, CTA)"]
    end

    subgraph Build & Launch
        S5 --> S6["Stage 6: Minimal MVP Build<br/>(&le; 3 Must-Have Features)"]
        S6 --> S7["Stage 7: Multi-Channel Launch & Viral Video<br/><code>microsaas-distribution</code>"]
        S7 --> S8["Stage 8: Checkout & True Net Cash Accounting"]
    end

    subgraph Audit & Lifecycle
        S8 --> S9["Stage 9: 30-Day Performance Audit<br/><code>microsaas-metrics</code>"]
        S9 -->|"Traction >= Threshold"| DD["🚀 DOUBLE DOWN"]
        S9 -->|"Mixed Signal"| PV["🔄 PIVOT"]
        S9 -->|"0 Traction / Negative Margin"| KL["🛑 KILL (Cut Cloud Burn)"]
    end

    HUB[("🧠 microsaas-hub<br/>State Manager & Gatekeeper<br/><code>.microsaas/state.json</code>")] <---> S1
    HUB <---> S2
    HUB <---> S3
    HUB <---> S4
    HUB <---> S7
    HUB <---> S9
```

---

## 🧩 The 7 Specialized Skills

| Skill | Role & Domain | Primary Frameworks | Strict Output / Gate |
| :--- | :--- | :--- | :--- |
| [**`microsaas-hub`**](skills/microsaas-hub/) | Master Orchestrator & State Manager | Stage-Gate Process, Memory Persistence | Enforces evidence gates; manages `.microsaas/state.json` |
| [**`microsaas-discovery`**](skills/microsaas-discovery/) | Opportunity Hunting & Idea Scoring | 4 Archetypes, Complaint Mining, JTBD | Rubric $\ge 24/35$ to advance; kills low-signal ideas |
| [**`microsaas-research`**](skills/microsaas-research/) | Competitive Moats & Red Teaming | Porter's 5 Forces, Moat Scorecard, Red Team | Moat $\ge 18/30$; exposes platform risk & incumbent traps |
| [**`microsaas-validation`**](skills/microsaas-validation/) | Customer Discovery & Mom Test | Rob Fitzpatrick's Mom Test, Smoke Testing | Pre-registered 14-day falsification gates |
| [**`microsaas-product`**](skills/microsaas-product/) | Amazon PR/FAQ & Spec-Driven Dev (SDD) | Working Backwards, MoSCoW ($\le 3$ feats), SDD | Full GitHub Spec Kit (`spec.md`, `data-model.md`, `tasks.md`) |
| [**`microsaas-distribution`**](skills/microsaas-distribution/) | GTM, Viral Video & Programmatic SEO | Hook-Retain-Reward scripts, pSEO matrix | 3 viral video scripts + pSEO database architecture |
| [**`microsaas-metrics`**](skills/microsaas-metrics/) | Unit Economics & Double Down / Kill | AARRR Pirate Metrics, Net Margin Accounting | 30-day decision memo: `DOUBLE DOWN`, `PIVOT`, or `KILL` |

---

## 🔍 Epistemic Rigor & Evidence Hierarchy

To eliminate hallucinations and unwarranted founder optimism, all skills must categorize every statement into four evidence tiers:

```text
[FACT]       ──▶ Verified empirical data (API docs, platform TOS, company registry).
[RESEARCH]   ──▶ Secondary research (G2 reviews, public pricing pages, search volume).
[SIGNAL]     ──▶ Indirect indicators (Reddit threads, founder discussions, forum rants).
[ASSUMPTION] ──▶ Founder hypothesis requiring empirical falsification before coding.
```

### ⚔️ Adversarial Red Team Rules
Before any idea receives a **GO** recommendation:
1. **The Incumbent Feature Trap:** If an established SaaS can clone the core functionality as a minor Friday sprint feature, the idea is **REJECTED**.
2. **The Platform Dependency Trap:** If the idea violates platform TOS or relies on scraping/APIs that can be revoked overnight, it is **REJECTED**.
3. **The Low Willingness-to-Pay (WTP) Trap:** If target users are accustomed to free open-source tools or complain about \$5/mo prices, it is **REJECTED**.

---

## ⚡ Quickstart & Installation

### Option 1: 1-Click Install to Global Antigravity Config (Recommended)

Run the included installer to copy all 7 skills directly into your global Antigravity skills directory (`~/.gemini/config/skills/`):

```bash
# On Windows / macOS / Linux
py install.py
# or
python3 install.py
```

Check installation status anytime:
```bash
py install.py --list
```

### Option 2: Project-Local Workspace Install

Install the skills strictly within your active project workspace (`.gemini/skills/`):

```bash
py install.py --workspace .
```

---

## 🛠️ Usage Walkthrough

Once installed, simply converse naturally with Antigravity. The skills activate based on your intent:

### 1. Initialize a Project & Hunt Opportunities
```text
User: "I want to explore micro-SaaS opportunities for Shopify dropshippers or physical therapists."
Agent activates: microsaas-hub -> microsaas-discovery
Output: Mined complaints, 4 archetypes evaluation, and opportunity scorecard.
```

### 2. Run Competitive Moat & Red Team Audit
```text
User: "Let's research the competition for an AI cold email personalization generator."
Agent activates: microsaas-research
Output: Competitive audit matrix, Moat Score (11/30), Adversarial Red Team verdict: NO-GO (Incumbent feature trap + TOS risk).
```

### 3. Conduct Pre-Code Customer Validation
```text
User: "How do I validate willingness-to-pay for an anniversary celestial star map keepsake?"
Agent activates: microsaas-validation
Output: Mom Test interview script, \$100 smoke-test protocol, and 14-day falsification gate.
```

### 4. Create Product Spec & PR/FAQ (Before Coding)
```text
User: "The keepsake idea validated! Let's write the spec before coding."
Agent activates: microsaas-product
Output: Amazon PR/FAQ, strict MoSCoW scope (&le; 3 features), and GitHub Spec Kit (spec.md, data-model.md, tasks.md).
```

### 5. Launch & Viral Distribution
```text
User: "We are ready to launch. Help me write TikTok/Reels video scripts and setup SEO."
Agent activates: microsaas-distribution
Output: 3 viral short-form video scripts (Hook-Retain-Reward framework) + 500-page pSEO matrix.
```

### 6. 30-Day Post-Launch Audit
```text
User: "Here are our numbers after 30 days: $2,840 GMV, $1,120 COGS, $85 Stripe fees. What's next?"
Agent activates: microsaas-metrics
Output: True Net Profit calculation ($1,635 / 57.5% net margin), Pirate metrics review, and DOUBLE DOWN roadmap.
```

---

## 📊 Scorecard & Independent Evaluation CLI

Micro-SaaS Founder OS includes a built-in evaluation engine (`tools/evaluate_system.py`) that audits project deliverables across **7 weighted dimensions**:

| Evaluation Dimension | Weight | Description |
| :--- | :---: | :--- |
| **Correctness** | 20% | Factual and technical accuracy of findings |
| **Evidence Quality** | 20% | Clear separation of facts vs assumptions with citations |
| **Decision Quality** | 20% | Soundness of GO / PIVOT / NO-GO recommendations |
| **Execution Quality** | 15% | Practical usability of templates, specs, and scripts |
| **Consistency** | 10% | Reproducible rigor across B2B, DevTools, and B2C projects |
| **State Management** | 5% | Preservation of state and decisions in `.microsaas/` |
| **Commercial Realism** | 10% | Viability of CAC, pricing, margins, and distribution channels |

### Running the Evaluator CLI
```bash
py tools/evaluate_system.py \
  --project "Stripe Webhook Sentinel" \
  --idea-verdict PIVOT \
  --idea-score "16/30 (Differentiation Gap)" \
  --correctness 9.0 \
  --evidence 8.5 \
  --decision 9.0 \
  --execution 8.5 \
  --consistency 8.5 \
  --state 8.5 \
  --commercial 8.5 \
  --output-md "scorecard.md"
```

> [!NOTE]
> The evaluator enforces a strict two-tier separation between the **Commercial Opportunity Verdict** (whether the business idea is good) and the **AI Auditor Competence Assessment** (whether the AI analyzed it correctly). An idea can be rejected (NO-GO) while the analysis receives an EXCELLENT (9.0/10) score for catching fatal flaws early.

---

## 📚 Included Examples & Benchmarks

The repository includes three real-world stress test case studies across distinct business archetypes:

* [**Case A: AI Cold Email Personalization SaaS**](examples/case_a_ai_cold_email_rejected.md) (B2B Sales)  
  *Outcome:* **🔴 REJECTED / NO-GO** (Score: 11/30). Caught in the incumbent feature trap against Instantly/Apollo and Google/Yahoo spam policy crackdowns.
* [**Case B: Stripe Webhook Reliability Sentinel**](examples/case_b_stripe_sentinel_pivoted.md) (Developer Tools)  
  *Outcome:* **🔄 PIVOT** (Score: 16/30). Pivoted from open-source clone into specialized PCI DSS audit trail for mid-market merchants.
* [**Case C: "The Night We Met" Celestial Star Map**](examples/case_c_anniversary_keepsake_approved.md) (B2C Physical Keepsake)  
  *Outcome:* **🟢 APPROVED / GO** (Score: 26/30). Validated with 58% net cash margin, zero inventory risk via print-on-demand API, and emotional gifting moat.

Also explore the [**40 Micro-SaaS Vetted Ideas Catalog**](docs/40_micro_saas_ideas_catalog.md) covering B2B workflow automation, programmatic keepsakes, niche marketplaces, and developer tools.

---

## 📑 Ready-to-Use Founder Templates

Copy-paste templates located in [`templates/`](templates/):
* `opportunity_scoring_rubric.md`: 7-dimension opportunity evaluation (/35).
* `competitive_audit_template.md`: Competitor matrix and 6-moat scorecard (/30).
* `mom_test_script_template.md`: Customer discovery interview script.
* `pr_faq_template.md`: Amazon-style press release and FAQ.
* `spec_kit_sdd_template.md`: GitHub Spec Kit for Spec-Driven Development.
* `short_form_video_script_template.md`: Hook-Retain-Reward TikTok/Reels script.
* `performance_review_template.md`: 30-day post-launch metrics review.

---

## 🤝 Contributing

Contributions, bug reports, and new niche templates are welcome! Please submit a pull request or open an issue.

## 📄 License

This project is licensed under the [MIT License](LICENSE).
