---
name: microsaas-metrics
description: >-
  Analytics, unit economics, conversion funnels, and the objective Kill/Pivot/Scale decision framework for micro-SaaS.
  Use when tracking business performance, calculating true net margins after fulfillment and Stripe fees,
  auditing churn, analyzing activation bottlenecks, or deciding whether to scale, pivot, or shut down a product.
---

# Micro-SaaS Analytics, Unit Economics & Kill Switch (`microsaas-metrics`)

Use this skill to strip emotion away from business performance, track true net cash collected, identify funnel leaks, and enforce the **Double Down, Pivot, or Kill** protocol.

---

## 📊 Part 1: The Micro-SaaS Pirate Metrics (AARRR)

Track these 5 funnel conversion numbers weekly:

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
│ 4. RETENTION       │ Recurring usage OR repeat gift    │
│                    │ purchase within 90 days           │
├────────────────────┼───────────────────────────────────┤
│ 5. REFERRAL        │ % who share finished artifact on  │
│                    │ social / word of mouth (Virality) │
└────────────────────┴───────────────────────────────────┘
```

---

## 💰 Part 2: True Net Cash Accounting

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

## 🛑 Part 3: The 30-Day "Double Down, Pivot, or Kill" Protocol

After 30 days of live operation and at least **500 unique visitors**, run the performance audit:

### Rule 1: DOUBLE DOWN (The Winner Signal)
* **Metrics:**
  * $\ge 20$ paid orders closed OR $\ge \$1,000$ in gross revenue.
  * Customer complaints / refund requests $< 3\%$.
  * Visitors actively sharing or asking for custom variations.
* **Action:**
  * Build out full programmatic SEO (pSEO) matrix.
  * Reinvest profits into higher-volume short-form video production.
  * Add automated Print-on-Demand upsells if digital-only.

### Rule 2: PIVOT (The Near-Miss Signal)
* **Metrics:**
  * High activation rate ($\ge 50\%$ test the generator), but low payment conversion ($< 1\%$).
  * Feedback says: *"I love the preview, but $X is too high"* OR *"I wish you had this other specific style/theme"*.
* **Action:**
  * Test lower-friction pricing (e.g. drop from \$19/mo sub to \$6.99 one-time).
  * Shift emotional niche (e.g. reposition from generic birthday to wedding anniversary).
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
1. Funnel Metrics Summary Table (Visitors $\rightarrow$ Previews $\rightarrow$ Sales $\rightarrow$ Cash).
2. Net Profit Calculation (Post-fees and fulfillment).
3. Objective Audit Verdict: **DOUBLE DOWN / PIVOT / KILL**.
4. Action plan for next 30 days.
