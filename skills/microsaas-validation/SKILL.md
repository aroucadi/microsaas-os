---
name: microsaas-validation
description: >-
  Pre-code customer discovery, willingness-to-pay testing, and demand validation for micro-SaaS.
  Use when testing whether people actually want an idea before writing software, running Mom Test
  interviews, creating smoke test landing pages, or establishing pre-registered falsification gates.
---

# Micro-SaaS Idea Validation & Evidence Ledger (`microsaas-validation`)

Use this skill to convert theoretical hypotheses into **observable commercial facts**. Never write a line of application code without tangible proof that target customers experience real pain and are willing to commit time, reputation, or money to solve it.

---

## 🚫 The 3 Deadly Validation Sins

1. **Asking for Opinions:** *"Do you think this is a good idea?"* (Everyone lies to be supportive).
2. **Asking Future Hypotheticals:** *"Would you buy this if we built it for $20?"* (Future promises cost nothing).
3. **Treating Vanity Signups as Customers:** An email waitlist is curiosity, not commercial validation.

---

## 🛠️ The 3 Validation Paths (Choose Based on Archetype)

```text
┌────────────────────────────────────────────────────────┐
│               CHOOSE YOUR VALIDATION PATH              │
├────────────────────────┬───────────────────────────────┤
│ PATH A: THE MOM TEST   │ Best for: B2B micro-utilities │
│ (5–8 Buyer Interviews) │ & workflow tools.             │
│                        │ Focuses on past purchasing and│
│                        │ active workaround costs.      │
├────────────────────────┼───────────────────────────────┤
│ PATH B: THE SMOKE TEST │ Best for: Self-serve B2C/B2B  │
│ (Landing Page + Stripe)│ micro-SaaS & keepsakes.       │
│                        │ Real traffic ➔ "Pre-Order" or │
│                        │ "Buy Now" checkout click.     │
├────────────────────────┼───────────────────────────────┤
│ PATH C: THE CONCIERGE  │ Best for: AI extractors and   │
│ (Manual Delivery)      │ niche parsing services.       │
│                        │ Deliver the outcome manually  │
│                        │ behind the scenes for 3 buyers│
└────────────────────────┴───────────────────────────────┘
```

---

## 📋 Path A: The Mom Test Protocol (Customer Discovery)

When interviewing prospects, adhere strictly to Rob Fitzpatrick's rules:
1. **Talk about their life and past actions, not your idea.**
2. **Ask about specific instances in the past, never generalities.**
3. **Talk less, listen more.**

### The 5 Essential Mom Test Questions:
1. *"When was the last time you had to deal with [problem]?"* (`[VERIFIED]` frequency).
2. *"Can you walk me through what you did step-by-step to handle it?"* (`[VERIFIED]` workflow).
3. *"What other solutions or tools did you try before settling on this?"* (`[VERIFIED]` active search).
4. *"What do you dislike about your current setup, and what does that workaround cost you in time or money?"* (`[VERIFIED]` severity).
5. *"In the past 12 months, have you paid for any software, freelancer, or tool to help fix this?"* (`[VERIFIED]` willingness to pay).

### The Commitment Ask at the End (Choose One):
* **Time Commitment:** *"I’m testing an early prototype next Tuesday. Would you be willing to spend 15 minutes testing it with your live data?"*
* **Reputation Commitment:** *"Would you introduce me to the colleague who handles this part of your workflow?"*
* **Financial Commitment:** *"We are offering early access for $X. You can lock in founding pricing today."*

---

## 🌐 Path B: The Smoke Test Protocol (Landing Page Experiment)

For self-serve apps (keepsakes, consumer micro-tools, developer utilities):

1. **Build a 1-Page High-Converting Landing Page (Zero backend):**
   * Clear headline stating the outcome in 5 seconds (StoryBrand Grunt Test).
   * Visual mockup or interactive preview (using static images or mock data).
   * Transparent pricing with a direct **"Pre-Order"** or **"Get Instant Access"** button.
2. **The "Paywall Moment":**
   * Real Stripe Checkout modal capturing high-intent clicks.
   * If live software is pending: *"We are onboarding early users in batches. Your card has not been charged—we'll notify you in 48 hours when your spot opens."*
3. **Traffic Test:**
   * Drive 200–500 targeted visitors via Reddit, Twitter/X, or short-form video.
   * Target Benchmark: **$\ge 3\%$ conversion rate on high-intent click-through**.

---

## 🛑 Pre-Registered 14-Day Falsification Gates

To prevent endless validation without clarity, pre-register exact failure conditions in `.microsaas/state.json`:

```markdown
# 14-Day Validation Plan & Stop Gates

- **Experiment Type:** [Path A: Interviews / Path B: Smoke Test / Path C: Concierge]
- **Target Audience:** [Exact role/community]
- **Outreach / Traffic Quota:** [e.g. 25 outreaches OR 300 page visitors]

### Pre-Registered Gates:
- **Gate 1 (Day 5 - Initial Signal):**
  - PASS: [e.g. $\ge 3$ interview bookings OR $\ge 5\%$ click-through rate]
  - FAIL: [< threshold] ➔ Action: Audit hook & copy.
- **Gate 2 (Day 10 - Commercial Intent):**
  - PASS: [e.g. $\ge 2$ prospects confirm paying for past solutions OR $\ge 5$ pre-orders]
  - FAIL: [< threshold] ➔ Action: Re-evaluate price/value equation.
- **Gate 3 (Day 14 - Definitive Go/No-Go):**
  - PASS: [e.g. $\ge 1$ paid pre-order / paid concierge client closed]
  - FAIL: Zero financial commitments. ➔ Action: **ABANDON OR PIVOT IMMEDIATELY**.
```

---

## 📄 Required Output Artifact

Save all observable outcomes in `validation-ledger.md`:
* List of interviews conducted or smoke test traffic metrics.
* Exact quotes, past tools used, and dollars previously spent by prospects.
* Gate Results: Did it pass Gate 1, 2, and 3?
* Final Recommendation: **PROCEED TO PRODUCT / PIVOT / ABANDON**.
* Human Sign-Off Checkpoint.
