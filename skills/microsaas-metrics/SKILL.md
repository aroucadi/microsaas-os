---
name: microsaas-metrics
description: >-
  Analytics, unit economics, conversion funnels, and the objective Kill/Pivot/Scale decision framework for micro-SaaS.
  Use when tracking business performance, auditing true net margins after fulfillment and Stripe fees,
  measuring the North Star Metric and Sean Ellis PMF test, or enforcing archetype-calibrated pre-registered kill criteria.
---

# Micro-SaaS Analytics, Unit Economics & Kill Switch (`microsaas-metrics`)

Use this skill to strip emotion away from business performance, track true net cash collected, identify funnel leaks, and enforce the **Double Down, Pivot, or Kill** protocol based on **venture-specific pre-registered hypotheses**.

> **Core Principle:** Track customer value delivered and net retained cash, not vanity traffic.

---

## 🌟 Part 1: The North Star Metric & Weekly Build-Measure-Learn

Avoid getting distracted by page views, signup counts, or social impressions. Pick **one North Star Metric** that directly measures customer value delivered:

* **Document Processing:** Number of invoices / PDFs successfully parsed and verified.
* **Keepsakes:** Number of high-resolution customized prints ordered and delivered.
* **Developer Utilities:** Number of webhooks reliably delivered or alerts successfully routed.
* **Compliance / Auditing:** Hours of manual preparation saved per weekly audit.

### The Weekly Build-Measure-Learn Loop:
Every Friday, audit:
1. What was the North Star Metric count this week?
2. What was the single biggest bottleneck preventing users from getting value?
3. What is the one small adjustment to build or test next week?

---

## 📊 Part 2: The Micro-SaaS Pirate Metrics (AARRR)

Track these 5 funnel conversion gates:

```text
┌────────────────────────────────────────────────────────┐
│                   THE 5 CRITICAL FUNNEL GATES          │
├────────────────────┬───────────────────────────────────┤
│ 1. ACQUISITION     │ Unique visitors landing on page   │
├────────────────────┼───────────────────────────────────┤
│ 2. ACTIVATION      │ % who generate a preview / enter  │
│                    │ inputs (Target: ≥ 40%)            │
├────────────────────┼───────────────────────────────────┤
│ 3. REVENUE         │ % of activated users who pay      │
│                    │ (Target: ≥ 2.5% of total visitors)│
├────────────────────┼───────────────────────────────────┤
│ 4. RETENTION       │ Recurring usage OR repeat order   │
│                    │ within 90 days                    │
├────────────────────┼───────────────────────────────────┤
│ 5. REFERRAL        │ % who share finished artifact on  │
│                    │ social / word of mouth (Virality) │
└────────────────────┴───────────────────────────────────┘
```

---

## 💰 Part 3: True Net Cash Accounting

Never confuse top-line Stripe gross volume with founder take-home profit.

### The Micro-SaaS Profit Formula:
$$\text{Net Retained Cash} = \text{Gross Revenue} - \text{Stripe Fees} - \text{Fulfillment COGS} - \text{Server/API Costs} - \text{Taxes}$$

### Benchmark Economics per Unit:

| Model | Gross Price | Stripe Fee | Fulfillment / API Cost | Server & Domains | Net Cash Margin |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Digital Unlock (PDF)** | \$6.99 | \$0.50 | \$0.05 | \$0.05 | **\$6.39 (~91%)** |
| **Framed Poster (Gelato)** | \$49.00 | \$1.72 | \$21.50 *(Print & Ship)* | \$0.10 | **\$25.68 (~52%)** |
| **Micro-Sub (SaaS)** | \$19.00/mo | \$0.85 | \$0.80 *(Compute/AI API)* | \$0.20 | **\$17.15 (~90%)** |
| **High-Ticket B2B Utility** | \$199.00/mo | \$6.07 | \$5.00 *(Dedicated Worker)* | \$2.00 | **\$185.93 (~93%)** |

> [!WARNING] **Economic Circuit Breaker:** If Net Cash Margin drops below 40% (or unit margin is negative after API fees), the Meta-Governor trips a mandatory **Economic Pause**. Software feature development is suspended until pricing or COGS are re-engineered.

---

## 📈 Part 4: Sean Ellis 40% PMF Test

Survey active users who have experienced the core workflow at least twice:
> *"How would you feel if you could no longer use this product?"*
> - **Very disappointed**
> - **Somewhat disappointed**
> - **Not disappointed**

* **$\ge 40\%$ "Very disappointed":** Strong early Product-Market Fit. Proceed to scale distribution (pSEO, paid experiments, viral pipelines).
* **$< 40\%$ "Very disappointed":** Do NOT pour money into acquisition. Iterate on the core workflow or interview users to understand why the value didn't stick.

---

## 🛑 Part 5: Archetype-Calibrated Pre-Registered Kill Protocol

Universal 30-day / 500-visitor rules fail because low-ticket impulse tools require fast turnaround, while B2B compliance workflows require longer sales evaluation. Every venture pre-registers its termination thresholds based on its **Go-To-Market Archetype**:

### 1. Archetype A: B2C Impulse & Keepsakes ($5 – $29 one-off)
* **Horizon & Sample:** 14 – 21 Days \| $\ge 500$ unique visitors \| 10 published creative hooks.
* **Double Down:** $\ge 20$ orders ($> \$400$ net cash), organic video shares $> 5\%$.
* **Pivot:** High preview generation ($\ge 50\%$) but checkout dropoff ($< 0.5\%$) $\rightarrow$ discount or test bundle pricing.
* **Kill:** $< 5$ sales after 500 targeted visitors; zero organic shares; refund rate $> 10\%$.

### 2. Archetype B: Prosumer & Indie B2B ($19 – $79/mo subscription)
* **Horizon & Sample:** 30 – 45 Days \| $\ge 200$ activated users (completed core setup / preview).
* **Double Down:** $\ge 10$ paid subscribers ($> \$500$ MRR), Month-1 retention $\ge 70\%$, Sean Ellis $\ge 40\%$.
* **Pivot:** Users love tool but balk at subscription $\rightarrow$ test one-time lifetime deal (LTD) or annual pass.
* **Kill:** $< 5$ paying subscribers after 45 days, Month-1 retention $< 40\%$, Sean Ellis $< 25\%$.

### 3. Archetype C: High-Ticket B2B & Compliance ($99 – $500+/mo)
* **Horizon & Sample:** 45 – 60 Days \| 15 Mom Test discovery calls \| 5 pilot deployments.
* **Double Down:** $\ge 2$ paid production pilots / signed LOIs ($> \$500$ MRR), customer requests enterprise terms.
* **Pivot:** Decision maker expresses need but security/integration blockers $\rightarrow$ pivot to on-prem / webhook proxy.
* **Kill:** 0 paid pilots and 0 LOIs after 15 qualified calls; problem rated $< 7/10$ urgency by leads.

---

## 📄 Required Output Artifact

Save performance reviews in `performance-review.md`:
1. North Star Metric & Weekly trend.
2. Funnel Metrics Summary Table (Visitors $\rightarrow$ Previews $\rightarrow$ Sales $\rightarrow$ Cash).
3. Net Profit Calculation (Post-fees and fulfillment).
4. Sean Ellis PMF Test Result.
5. Pre-registered Archetype Threshold Audit.
6. Objective Audit Verdict: **DOUBLE DOWN / PIVOT (Solution or Wedge) / KILL VENTURE**.
