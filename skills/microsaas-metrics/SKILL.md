---
name: microsaas-metrics
description: >-
  Analytics, unit economics, conversion funnels, and the objective Kill/Pivot/Scale decision framework for micro-SaaS.
  Use when tracking business performance, auditing true net margins after fulfillment and Stripe fees,
  measuring the North Star Metric and Sean Ellis PMF test, or enforcing the 30-day Double Down, Pivot, or Kill protocol.
---

# Micro-SaaS Analytics, Unit Economics & Kill Switch (`microsaas-metrics`)

Use this skill to strip emotion away from business performance, track true net cash collected, identify funnel leaks, and enforce the **Double Down, Pivot, or Kill** protocol.

> **Core Principle:** Track customer value delivered, not vanity traffic.

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

## 🛑 Part 5: The 30-Day "Double Down, Pivot, or Kill" Protocol

After 30 days of live operation and at least **500 unique visitors**, run the objective audit:

### Rule 1: DOUBLE DOWN (The Winner Signal)
* **Metrics:**
  * $\ge 20$ paid orders closed OR $\ge \$1,000$ in gross revenue.
  * Customer complaints / refund requests $< 3\%$.
  * Sean Ellis test $\ge 40\%$ "Very disappointed".
* **Action:**
  * Build out full programmatic SEO (pSEO) matrix.
  * Reinvest profits into higher-volume short-form video production.
  * Add automated Print-on-Demand upsells if digital-only.

### Rule 2: PIVOT (The Near-Miss Signal)
* **Metrics:**
  * High activation rate ($\ge 50\%$ test the generator), but low payment conversion ($< 1\%$).
  * Feedback says: *"I love the preview, but $X is too high"* OR *"I need integration with Y"*.
* **Action:**
  * Test lower-friction pricing (e.g. drop from \$19/mo sub to \$6.99 one-time).
  * Shift emotional niche or ICP segment.
  * Run 1 additional 14-day test cycle.

### Rule 3: KILL (The Zero-Delusion Kill Switch)
* **Metrics:**
  * $< 3$ paid sales after $\ge 500$ targeted visitors and 10 published video hooks.
  * Zero organic shares, zero word-of-mouth referral.
  * High customer support friction or high refund rate ($> 15\%$).
* **Action:**
  * **SHUT IT DOWN.** Do not spend another hour optimizing CSS or adding features.
  * Archive codebase, cancel dedicated third-party subscriptions, log learnings in `.microsaas/decision-log.md`.
  * Move immediately to the next opportunity in the backlog.

---

## 📄 Required Output Artifact

Save performance reviews in `performance-review.md`:
1. North Star Metric & Weekly trend.
2. Funnel Metrics Summary Table (Visitors $\rightarrow$ Previews $\rightarrow$ Sales $\rightarrow$ Cash).
3. Net Profit Calculation (Post-fees and fulfillment).
4. Sean Ellis PMF Test Result.
5. Objective Audit Verdict: **DOUBLE DOWN / PIVOT / KILL**.
