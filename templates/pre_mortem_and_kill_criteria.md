# Pre-Mortem & Kill Criteria Template

> **Methodology:** Gary Klein (Cognitive Psychology) + Eric Ries (Lean Startup)  
> **Mandate:** Prevent founder delusion, enthusiasm bias, and sunk-cost fallacies before a single line of software is written.

---

## 💀 1. The Pre-Mortem (Gary Klein)

> *"Fast forward 6 months from today. The product launched, burned 200 hours of development time, and failed completely. Nobody is renewing, revenue is near zero, and the business is dead."*

Identify the **top 3 most realistic root causes** of this failure:

### Root Cause 1: [e.g. Distribution Failure]
* **Failure Scenario:** [e.g. Cold email response rates collapsed to < 0.5% due to Google spam filter crackdowns, making customer acquisition prohibitively expensive].
* **Pre-Code Mitigation:** [e.g. Validate organic Reddit community demand or build an upfront audience before building].

### Root Cause 2: [e.g. Incumbent Feature Extension]
* **Failure Scenario:** [e.g. Loom or Stripe shipped this exact utility as a free checkbox in their core dashboard during a quarterly release].
* **Pre-Code Mitigation:** [e.g. Confirm we have an asymmetric workflow wedge or proprietary data integration that incumbents cannot justify building].

### Root Cause 3: [e.g. Lack of Retention / Churn]
* **Failure Scenario:** [e.g. Users got value once on day 1, but experienced no recurring trigger to open the product in month 2, leading to 90% monthly churn].
* **Pre-Code Mitigation:** [e.g. Switch from subscription pricing to pay-per-use, or anchor to a weekly compliance/reporting cycle].

---

## 🛑 2. Pre-Registered Kill Criteria (Lean Startup)

Establish immutable, objective conditions under which the founder commits to **stop investing time and kill or pivot the project**:

| Dimension | Threshold to KILL or PIVOT | Measurement Method |
| :--- | :--- | :--- |
| **Willingness to Pay** | 0 paid commitments after 10 demo calls or 300 page visitors | Stripe Checkout / deposit ledger |
| **Customer Acquisition** | Blended CAC $> 50\%$ of Year-1 LTV | Ad spend & conversion logs |
| **User Activation** | $< 20\%$ of signups reach the "Aha!" moment in the walking skeleton | Product telemetry / event logs |
| **Time-to-Build** | Core walking skeleton takes $> 3$ weeks (exceeding Shape Up appetite) | GitHub commit timeline |

---

## ✍️ 3. Founder Sign-Off Checkpoint

* **Product Name:** [Product Name]
* **Date:** [YYYY-MM-DD]
* **Review Checklist:**
  - [ ] Riskiest Assumption Test (RAT) verified with observable data.
  - [ ] PR/FAQ completed with narrow ICP and 1-sentence pitch.
  - [ ] Scope locked to 1 core workflow and $\le 3$ MUST-HAVE capabilities.
  - [ ] Anti-AI-slop UI tokens and Walking Skeleton defined.
  - [ ] Top 3 failure modes analyzed; kill criteria registered.
* **Final Verdict:**
  - [ ] **PROCEED TO CODING:** Build Walking Skeleton first.
  - [ ] **REVISE SCOPE:** Re-trim features to fit appetite.
  - [ ] **KILL / PIVOT:** Do not write code; log learnings.
