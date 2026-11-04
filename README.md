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

> **The Central Axiom:** Evidence before specifications. Specifications before code. Working customer value before feature expansion.

---

## 🏛️ The Master Two-Layer Architecture

Micro-SaaS Founder OS is structured as two interacting layers:
* **Layer 1: Meta-Orchestration & Governance (The Supervisory Brain):** Continuously senses founder input, evaluates evidence confidence, checks for strategic contradictions, filters conversational noise via hysteresis, and dynamically routes to the highest-risk uncertainty.
* **Layer 2: Venture Execution State Graph (The Topographical Map):** The full, rich startup state machine with nested states, multi-route intake, explicit evidence gates, development feedback loops, and commercial metrics.

> **The Architectural Rule:** The Execution Graph determines what states and transitions are possible. The Meta-Governor determines which transition makes sense right now.

```mermaid
flowchart TD
    INPUT["Founder Input / External Event"] --> SENSOR

    subgraph GOV["LAYER 1: META-ORCHESTRATION & GOVERNANCE (Supervisory Brain)"]
        SENSOR["Context & Epistemic Sensor"]
        CONF["Confidence Calibration<br/><code>[CONF=0.1 - 1.0]</code>"]
        CONTRA{"Contradiction<br/>Detected?"}
        RECON["Strategic Reconciliation<br/><i>(Pivot / Trim / Kill)</i>"]
        RISK["Highest-Risk Uncertainty Ranker"]
        HYST["Routing Hysteresis & Damping"]
        ROUTER["Dynamic Skill Router"]

        SENSOR --> CONF --> CONTRA
        CONTRA -->|"Yes (Conflict)"| RECON --> SENSOR
        CONTRA -->|"No (Clear)"| RISK --> HYST --> ROUTER
    end

    subgraph EXEC["LAYER 2: VENTURE EXECUTION STATE GRAPH (Topological Map)"]
        subgraph S_TRIAGE["Intake & Triage"]
            T1["Route A: Raw Idea"]
            T2["Route B: Clear Problem"]
            T3["Route C: Existing Traction"]
            T4["Route D: Working Code"]
        end

        subgraph S_RESEARCH["Competitive Red Team"]
            MOAT["Moat Analysis (/30)"]
            RED_PASS["Moat >= 18 + Red Team Clear"]
            RED_TRAP["Platform Trap / Incumbent Bloat"]
        end

        subgraph S_RAT["Riskiest Assumption Test (RAT)"]
            EXP_MOM["The Mom Test"]
            EXP_CON["Concierge MVP"]
            EXP_SMK["Smoke Page"]
            EXP_SPK["Technical Spike"]
        end

        subgraph S_EVID["Evidence Gate"]
            EVAL["Evaluate Confidence & WTP"]
            GATE_PASS["RAT Passed (Skin in Game)"]
            GATE_PIVOT["Pivot Signal (Re-anchor)"]
            GATE_FAIL["RAT Failed (Zero WTP)"]
        end

        subgraph S_PROD["Product & UX Architecture"]
            PRFAQ["Lightweight PR/FAQ"]
            WORKFLOW["One Core Workflow & Appetite"]
            ANTISLOP["Anti-AI-Slop UX Tokens"]
            WALK_SPEC["Walking Skeleton Spec"]
        end

        subgraph S_PRE["Pre-Mortem Gate"]
            PRE_MORTEM["3 Failure Modes & Kill Criteria"]
        end

        subgraph S_BUILD["In-Development Loop"]
            WALK_BUILD["Walking Skeleton Build"]
            FIRST_CUST["First Customer Gate"]
            ITER_SLICE["Iterate Vertical Slice"]
        end

        subgraph S_GROWTH["Distribution & Metrics"]
            GROWTH["Distribution Engine (pSEO / Viral)"]
            METRICS["Metrics & Cash Loop"]
        end

        TERMINAL_KILL(["🛑 TERMINAL: KILL"])
        TERMINAL_SCALE(["🚀 SCALE: DOUBLE DOWN"])
    end

    %% Internal execution graph flows
    T1 --> S_RESEARCH
    T2 --> S_RESEARCH
    T3 --> S_PROD
    T4 --> S_GROWTH

    MOAT --> RED_PASS
    MOAT --> RED_TRAP
    RED_TRAP -->|"Backtrack & Pivot Wedge"| S_TRIAGE
    RED_PASS --> S_RAT

    EXP_MOM --> EVAL
    EXP_CON --> EVAL
    EXP_SMK --> EVAL
    EXP_SPK --> EVAL

    EVAL --> GATE_PASS
    EVAL --> GATE_PIVOT
    EVAL --> GATE_FAIL

    GATE_FAIL --> TERMINAL_KILL
    GATE_PIVOT -->|"Re-anchor Solution"| S_TRIAGE
    GATE_PASS --> S_PROD

    PRFAQ --> WORKFLOW --> ANTISLOP --> WALK_SPEC --> PRE_MORTEM --> WALK_BUILD
    WALK_BUILD --> FIRST_CUST
    FIRST_CUST <-->|"Customer Feedback Loop"| ITER_SLICE
    FIRST_CUST -->|"Core Value Realized"| GROWTH

    GROWTH --> METRICS
    METRICS -->|"Double Down"| TERMINAL_SCALE
    METRICS -->|"Pivot"| S_TRIAGE
    METRICS -->|"Kill"| TERMINAL_KILL

    %% Governor Supervisory Routing (Downlink)
    ROUTER -.->|"Direct Route"| S_TRIAGE
    ROUTER -.->|"Direct Route"| S_RESEARCH
    ROUTER -.->|"Direct Route"| S_RAT
    ROUTER -.->|"Direct Route"| S_PROD
    ROUTER -.->|"Direct Route"| S_BUILD
    ROUTER -.->|"Direct Route"| S_GROWTH

    %% Execution Graph State/Evidence Streaming (Uplink)
    EXEC -.->|"Evidence Updates & Living Memory (.microsaas/)"| SENSOR
    EXEC -.->|"Strategic Contradictions & Platform Shifts"| CONTRA
```

---

## 🗺️ Master Venture Execution State Machine

The complete topological map governing transitions, sub-states, and loops across the venture lifecycle:

```mermaid
stateDiagram-v2
    [*] --> IntakeAndTriage: User brings idea, problem, or prototype

    state IntakeAndTriage {
        [*] --> ContextSensing
        ContextSensing --> RouteA_VagueIdea: Raw pain / No clarity
        ContextSensing --> RouteB_KnownProblem: Clear pain / No solution
        ContextSensing --> RouteC_ExistingTraction: Already paying users / Productizing service
        ContextSensing --> RouteD_WorkingCode: Existing code / Needs distribution
    }

    RouteA_VagueIdea --> DiscoveryEngine: Explore JTBD & Mine Complaints
    RouteB_KnownProblem --> CompetitiveRedTeam: Audit Moats & Platform Traps
    RouteC_ExistingTraction --> OutcomeFraming: Fast-Forward to PR/FAQ & Scope
    RouteD_WorkingCode --> GrowthEngine: Jump to Distribution & pSEO

    state CompetitiveRedTeam {
        [*] --> MoatAnalysis
        MoatAnalysis --> PassClear: Moat >= 18/30
        MoatAnalysis --> FatalTrapDetected: Platform TOS / Incumbent Feature Trap
    }

    FatalTrapDetected --> DiscoveryEngine: Backtrack & Pivot the Wedge
    PassClear --> RiskiestAssumptionTest: Formulate RAT

    state RiskiestAssumptionTest {
        [*] --> SelectCheapestExperiment
        SelectCheapestExperiment --> MomTest: B2B Interviews
        SelectCheapestExperiment --> Concierge: Manual Delivery
        SelectCheapestExperiment --> SmokePage: Self-Serve Demand Test
        SelectCheapestExperiment --> TechSpike: Feasibility Test
    }

    MomTest --> EvidenceGate
    Concierge --> EvidenceGate
    SmokePage --> EvidenceGate
    TechSpike --> EvidenceGate

    state EvidenceGate {
        [*] --> EvaluateEvidence
        EvaluateEvidence --> RAT_Failed: Zero WTP / Indifference
        EvaluateEvidence --> RAT_Passed: Real spending / Skin in the game
        EvaluateEvidence --> PivotSignal: Love problem, hate proposed solution
    }

    RAT_Failed --> [*]: KILL (Save months of wasted code)
    PivotSignal --> DiscoveryEngine: Re-anchor Solution
    RAT_Passed --> OutcomeFraming: Define Product & Appetite

    state OutcomeFraming {
        [*] --> PRFAQ
        PRFAQ --> OneCoreWorkflow
        OneCoreWorkflow --> AntiSlopDesign
        AntiSlopDesign --> WalkingSkeletonSpec
    }

    WalkingSkeletonSpec --> PreMortemGate: 3 Failure Modes & Kill Criteria
    PreMortemGate --> WalkingSkeletonBuild: Build Task 0 (End-to-End Tracer)

    state InDevelopmentLoop {
        WalkingSkeletonBuild --> FirstCustomerGate: Hand to real user
        FirstCustomerGate --> IterateSlice: Feedback received
        IterateSlice --> FirstCustomerGate
    }

    FirstCustomerGate --> GrowthEngine: Core workflow delivers real value
    GrowthEngine --> MetricsLoop: Double Down, Pivot, or Kill
    MetricsLoop --> [*]
```

---

## ⚖️ Meta-Governance & Decision Engine (Elite 10/10 Architecture)

To ensure execution matches architectural intent, `microsaas-hub` enforces four advanced governance systems:

### 1. Calibrated Confidence Scoring (L1–L4)
Distinguishes empirical financial proof from casual internet comments:
* **`[CONF=1.0]` (L4 - Empirical Reality):** Live Stripe payouts, verified bank transactions, executed test suites (exit code 0), signed pilot contracts.
* **`[CONF=0.7]` (L3 - High Primary Signal):** Direct quotes from *Mom Test* interviews on past spending, official platform API docs/TOS, competitor checkout prices.
* **`[CONF=0.4]` (L2 - Secondary Market Signal):** G2/Trustpilot reviews, Reddit complaint threads, search volume trends.
* **`[CONF=0.1]` (L1 - Hypothesis / Fluff):** Survey promises ("I would buy this"), founder assumptions, LLM speculation.
* *Rule:* No strategic **GO** recommendation can be grounded on evidence with aggregated confidence $< 0.70$.

### 2. Contradiction Detection & Strategic Reconciliation
When newly discovered research or test data conflicts with earlier premises (e.g. Discovery assumed zero competitors, but Research uncovered an active \$1M ARR incumbent):
* The Hub flags `⚠️ [CONTRADICTION DETECTED]`.
* Progression is immediately frozen until an explicit [Strategic Reconciliation Memo](templates/strategic_reconciliation_memo.md) is appended to `.microsaas/decision-log.md` detailing whether to pivot the wedge, trim scope, or kill the idea.

### 3. Tool Execution Verification Guardrails
Prevents hallucinated execution:
* Research claims must link directly to primary URLs recorded in `source-ledger.md`.
* Terminal commands and test suites must return exit code `0` with verified output logs.
* Generated deliverables must exist on disk before state transitions are confirmed.

### 4. Routing Hysteresis & Anti-Oscillation Damping
Prevents chaotic skill jumping on minor conversational noise:
* **Contextual Inertia:** Clarifying questions and "what-if" musings are answered within the active skill without resetting state.
* **Materiality Threshold:** Changing the active lifecycle stage requires completing a gate artifact or verifying a high-confidence ($\ge 0.7$) pivot/kill trigger.
* **Circuit Breaker:** If an idea bounces between any two skills $\ge 3$ times without producing new evidence, the Hub halts the loop and forces a binary 48-hour resolution decision.

---

## 🧩 The 7 Specialized Skills

| Skill | Role & Domain | Primary Frameworks | Strict Output / Gate |
| :--- | :--- | :--- | :--- |
| [**`microsaas-hub`**](skills/microsaas-hub/) | Master Orchestrator & State Manager | Stage-Gate, Pre-Mortem, Kill Criteria | Enforces gates, manages `.microsaas/`, stops bad builds |
| [**`microsaas-discovery`**](skills/microsaas-discovery/) | Opportunity Hunting & Idea Scoring | 4 Archetypes, Complaint Mining, JTBD | Rubric $\ge 24/35$ to advance; kills low-signal ideas |
| [**`microsaas-research`**](skills/microsaas-research/) | Competitive Moats & Red Teaming | Porter's 5 Forces, Moat Scorecard, Red Team | Moat $\ge 18/30$; exposes platform risk & incumbent traps |
| [**`microsaas-validation`**](skills/microsaas-validation/) | Riskiest Assumption Testing & Evidence | RAT, Mom Test, Concierge/Wizard of Oz | Pre-registered pass/fail falsification gates |
| [**`microsaas-product`**](skills/microsaas-product/) | PR/FAQ, Shape Up Appetite & Anti-AI-Slop UI | YC Principles, Walking Skeleton, Spec Kit | 1-Sentence Pitch, Walking Skeleton & vertical slices |
| [**`microsaas-distribution`**](skills/microsaas-distribution/) | GTM, Viral Video & Programmatic SEO | Hook-Retain-Reward scripts, pSEO matrix | 3 viral video scripts + pSEO database architecture |
| [**`microsaas-metrics`**](skills/microsaas-metrics/) | North Star Metric & 30-Day Kill Switch | AARRR Pirate Metrics, Sean Ellis PMF, Net Margin | 30-day decision memo: `DOUBLE DOWN`, `PIVOT`, or `KILL` |

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

## 🎨 Distinctive UI/UX Architecture: Banishing "AI Slop"

Most AI coding agents produce apps that look like 99% of generated software: identical centered hero sections, generic `Inter` typography, clichéd purple gradients on white cards, and predictable 3-card grids.

Micro-SaaS Founder OS incorporates **[Hashim Warren's Frontend Aesthetics Directive](https://gist.github.com/hashimwarren/b544f89bdb50e4877d0e603ad547e18f)** directly into the build pipeline so generated web and mobile interfaces look bespoke, tactile, and memorable.

* **Distinctive Typography Pairings:** Ban generic `Inter`, `Roboto`, and `Arial`. Pair high-character headings (`Syne`, `Cabinet Grotesk`, `Instrument Serif`, `Clash Display`, or `Fraunces`) with refined body fonts (`Plus Jakarta Sans`, `General Sans`, `Satoshi`).
* **Cohesive Aesthetic Archetypes:** Commit to a bold, context-specific theme (*Obsidian & Phosphor* for DevTools, *Warm Atelier* for Keepsakes, *Midnight Cobalt* for Fintech, *Neo-Brutalist* for Creative tools) with defined CSS variables.
* **Atmospheric Depth & Tactile Lighting:** Layer subtle radial lighting gradients (`radial-gradient`), 28px micro-grids, or warm paper textures with crisp top rim light (`inset 0 1px 0 rgba(255,255,255,0.08)`).
* **Orchestrated Staggered Reveals:** Avoid scattered hover effects. Use pure CSS staggered page reveals on load (`animation-delay: calc(var(--index) * 80ms)`) with snappy cubic-bezier easing (`cubic-bezier(0.16, 1, 0.3, 1)`).
* **Mobile Ergonomics:** Thumb-zone CTA placement in lower third, sliding bottom sheets instead of centered modal popups, and $44 \times 44\text{px}$ minimum touch targets.

*Reference Guide:* See [`templates/frontend_aesthetics_anti_slop.md`](templates/frontend_aesthetics_anti_slop.md).

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
* `strategic_reconciliation_memo.md`: Framework for resolving contradictions between new data and prior assumptions.
* `riskiest_assumption_test.md`: Riskiest Assumption Testing (RAT) and experiment selector.
* `mom_test_script_template.md`: Customer discovery interview script.
* `pr_faq_template.md`: Amazon-style press release and FAQ with 1-sentence pitch.
* `spec_kit_sdd_template.md`: GitHub Spec Kit for Spec-Driven Development with Walking Skeleton.
* `frontend_aesthetics_anti_slop.md`: Anti-AI-slop design directives, typography pairings, and theme tokens.
* `pre_mortem_and_kill_criteria.md`: Gary Klein Pre-Mortem (top 3 failure modes) and kill criteria.
* `short_form_video_script_template.md`: Hook-Retain-Reward TikTok/Reels script.
* `performance_review_template.md`: 30-day post-launch metrics review.

---

## 🤝 Contributing

Contributions, bug reports, and new niche templates are welcome! Please submit a pull request or open an issue.

## 📄 License

This project is licensed under the [MIT License](LICENSE).
