# Pre-Mortem & Pre-Registered Kill Criteria Template

> **Methodology:** Gary Klein (Cognitive Psychology) + Eric Ries (Lean Startup)  
> **Mandate:** Prevent founder delusion, enthusiasm bias, and sunk-cost fallacies before a single line of software is written. Pre-register objective termination thresholds calibrated to your specific venture archetype.

---

## 💀 1. The Pre-Mortem (Gary Klein)

> *"Fast forward 6 months from today. The product launched, burned 200 hours of development time, and failed completely. Nobody is renewing, revenue is near zero, and the business is dead."*

Identify the **top 3 most realistic root causes** of this failure:

### Root Cause 1: [e.g. Distribution Failure / Channel Collapse]
* **Failure Scenario:** [e.g. Cold email response rates collapsed to < 0.5% due to Google spam filter crackdowns, making customer acquisition prohibitively expensive].
* **Pre-Code Mitigation:** [e.g. Validate organic Reddit community demand or build an upfront audience before building].

### Root Cause 2: [e.g. Incumbent Feature Extension / Platform Risk]
* **Failure Scenario:** [e.g. Loom or Stripe shipped this exact utility as a free checkbox in their core dashboard during a quarterly release].
* **Pre-Code Mitigation:** [e.g. Confirm we have an asymmetric workflow wedge or proprietary data integration that incumbents cannot justify building].

### Root Cause 3: [e.g. Lack of Retention / Churn]
* **Failure Scenario:** [e.g. Users got value once on day 1, but experienced no recurring trigger to open the product in month 2, leading to 90% monthly churn].
* **Pre-Code Mitigation:** [e.g. Switch from subscription pricing to pay-per-use, or anchor to a weekly compliance/reporting cycle].

---

## 🛑 2. Venture-Specific Pre-Registered Kill Criteria

Do NOT use a generic, one-size-fits-all threshold. Select your **Venture Archetype** and pre-register explicit pass/fail conditions:

### Select Venture Archetype:
- [ ] **Archetype A: B2C Impulse / Keepsake / Micro-Utility ($5 – $29 one-off)**
- [ ] **Archetype B: Prosumer / Indie B2B Tool ($19 – $79/mo subscription)**
- [ ] **Archetype C: High-Ticket B2B Workflow / Compliance ($99 – $500+/mo)**

---

### Pre-Registered Termination Thresholds by Archetype:

| Archetype | Evaluation Horizon | Minimum Volume Required | Objective KILL / PIVOT Trigger |
| :--- | :---: | :---: | :--- |
| **A: B2C Impulse ($5–$29)** | 14 – 21 Days | 500 Unique Visitors + 10 Published Video Hooks | • $< 5$ paid checkouts ($< 0.8\%$ visitor conversion)<br/>• Zero organic shares or viral referrals<br/>• Refund rate $> 10\%$ |
| **B: Prosumer / Indie B2B ($19–$79/mo)** | 30 – 45 Days | 200 Activated Users (completed onboarding / preview) | • $< 5$ active paying subscribers<br/>• Month-1 Retention $< 50\%$<br/>• Sean Ellis PMF test $< 25\%$ "Very disappointed" |
| **C: High-Ticket B2B ($99–$500+/mo)** | 45 – 60 Days | 15 Qualified Mom Test Interviews + 5 Pilot Deployments | • $< 2$ paid pilots / signed Letters of Intent (LOIs)<br/>• Sales cycle stall ($> 60$ days with 0 conversions)<br/>• Zero client referrals or internal champion advocacy |

---

## 📋 3. Specific Pre-Registered Commitments for This Venture

```json
{
  "venture_id": "[VENTURE_ID]",
  "archetype": "[A_B2C | B_PROSUMER | C_B2B_HIGHTICKET]",
  "evaluation_deadline": "YYYY-MM-DD",
  "min_sample_size": 0,
  "kill_thresholds": {
    "min_paid_customers": 0,
    "min_gross_revenue": 0.0,
    "max_acceptable_cac": 0.0,
    "min_retention_rate_pct": 0.0,
    "min_sean_ellis_pmf_pct": 0.0
  },
  "action_if_failed": "[KILL_SOLUTION | KILL_WEDGE | KILL_VENTURE]"
}
```

---

## ✍️ 4. Founder Sign-Off Checkpoint

* **Product Name:** `[Product Name]`
* **Date:** `[YYYY-MM-DD]`
* **Review Checklist:**
  - [ ] Riskiest Assumption Test (RAT) verified with observable 4D data.
  - [ ] PR/FAQ completed with narrow ICP and 1-sentence pitch.
  - [ ] Scope locked to 1 core workflow and $\le 3$ MUST-HAVE capabilities.
  - [ ] Anti-AI-slop UI tokens and Walking Skeleton defined.
  - [ ] Top 3 failure modes analyzed; venture-specific kill criteria pre-registered.
* **Final Verdict:**
  - [ ] **PROCEED TO CODING:** Build Walking Skeleton first.
  - [ ] **REVISE SCOPE:** Re-trim features to fit appetite.
  - [ ] **KILL / PIVOT:** Do not write code; log learnings in `.microsaas/decision-log.md`.
