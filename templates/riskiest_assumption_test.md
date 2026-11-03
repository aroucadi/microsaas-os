# Riskiest Assumption Test (RAT) Template

> **Methodology:** Lean Startup + Y Combinator  
> **Mandate:** Identify and test the single assumption that could kill the business before writing software. Validate demand before validating your ability to build.

---

## 1. The Riskiest Assumption Audit

State the one assumption that, if proven false, makes everything else irrelevant:

* **Target Assumption:** [e.g., Independent physical therapy clinics will pay $49/mo for automated cancellation backfill notifications]
* **Assumption Category:**
  - [ ] **Problem Existence:** Do customers actively suffer from this pain repeatedly?
  - [ ] **Willingness to Pay (WTP):** Do they have budget and actively spend money on workarounds?
  - [ ] **Distribution / Acquisition:** Can we cost-effectively reach them where they hang out?
  - [ ] **Technical Feasibility:** Can we extract/deliver the data without fragile platform hacks?

### Problem vs. Solution Disambiguation:
* **The Problem Reality:** [Evidence that the problem exists today: e.g. Clinics lose 12% of revenue to same-day no-shows]
* **The Solution Reality:** [Why our specific solution is acceptable: e.g. Front desk staff can use SMS without replacing their EHR software]

---

## 2. The Selected Validation Experiment

Select the cheapest, fastest experiment that directly challenges this assumption:

| Experiment Type | When to Choose | Planned Execution |
| :--- | :--- | :--- |
| **[ ] The Mom Test Interviews** | B2B workflow & productivity | 5–8 calls investigating past spending and workarounds |
| **[ ] Concierge MVP** | Data extraction / niche analysis | Manually deliver the result behind the scenes for 3 buyers |
| **[ ] Wizard of Oz MVP** | Interactive micro-tools | Front-facing UI form with manual backend fulfillment |
| **[ ] Paid Pilot / Pre-Order** | High-ticket B2B / pre-launch | Refundable deposit or signed LOI |
| **[ ] Smoke Test Landing Page** | Self-serve B2C / Developer tools | Landing page with real price and Stripe intent click tracking |

---

## 3. Pre-Registered Pass / Fail Falsification Thresholds

Define what constitutes success and failure *before* running the experiment:

* **Experiment Duration:** [e.g., 7 days or 15 customer outreaches]
* **PASS Threshold:** [e.g., At least 3 clinic owners confirm they paid $\ge \$100$ last month for workaround software/staff AND 2 agree to a paid pilot trial]
* **FAIL Threshold:** [e.g., Clinic owners say "nice idea" but none can cite past dollars spent, or all refuse a paid trial]

---

## 4. Experiment Results & Verdict

* **Total Interactions / Traffic:** [e.g., 18 clinics contacted, 7 interviews completed]
* **Direct Evidence & Verbatim Quotes:**
  * Prospect 1: *"..."* (`[VERIFIED]` past spend: \$[Amount])
  * Prospect 2: *"..."* (`[VERIFIED]` past spend: \$[Amount])
* **Falsification Verdict:**
  - [ ] **PASS:** Riskiest assumption validated with observable evidence $\rightarrow$ Proceed to Product Definition (`microsaas-product`).
  - [ ] **FAIL:** Assumption falsified $\rightarrow$ **KILL OR PIVOT IMMEDIATELY** (Do not write code).
