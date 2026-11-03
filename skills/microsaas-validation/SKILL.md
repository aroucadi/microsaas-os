---
name: microsaas-validation
description: >-
  Pre-code customer discovery, Riskiest Assumption Testing (RAT), and demand validation for micro-SaaS.
  Use when testing whether people actually want an idea before writing software, identifying the single
  assumption that could kill the business, running Mom Test interviews, designing Concierge/Wizard of Oz
  MVPs, or establishing pre-registered falsification gates.
---

# Micro-SaaS Idea Validation & Evidence Ledger (`microsaas-validation`)

Use this skill to convert theoretical hypotheses into **observable commercial facts**. Never write a single line of application code without tangible proof that target customers experience real pain and are willing to commit time, reputation, or money to solve it.

> **Core Principle:** Validate demand before validating your ability to build software.

---

## 🎯 Step 1: The Riskiest Assumption Test (RAT)

Before designing any experiment or writing code, isolate the single assumption that could kill the business if false.

### The 4 Assumption Categories:
1. **Problem Assumption:** Target users actually suffer from this pain repeatedly and care enough to fix it.
2. **Willingness-to-Pay (WTP) Assumption:** Users actively allocate budget or spend money on workarounds (not just looking for free tools).
3. **Distribution / Reachability Assumption:** We can cost-effectively reach these specific users where they already congregate.
4. **Feasibility / Dependency Assumption:** The core technical value can be delivered without violating platform terms or relying on fragile hacks.

### Separate Problem Fit from Solution Fit:
* **Problem Validation:** *"Do you have this specific headache, and how much did your last workaround cost?"*
* **Solution Validation:** *"Does our proposed approach actually solve it without introducing new friction?"*
* **Warning:** A prospect having a problem does *not* automatically mean they want your proposed software solution. Always validate both.

---

## 🛠️ Step 2: Choose the Cheapest Meaningful Experiment

Do not default to a rigid 14-day process. Select the experiment that directly tests your **Riskiest Assumption** with the least effort:

```text
┌────────────────────────────────────────────────────────────────────────┐
│                      THE 5 VALIDATION EXPERIMENTS                      │
├─────────────────────────┬──────────────────────────────────────────────┤
│ 1. THE MOM TEST         │ Best for: B2B workflow & productivity tools. │
│    (5–8 Interviews)     │ Validates past spending, frequency, and      │
│                         │ active workarounds without pitching.         │
├─────────────────────────┼──────────────────────────────────────────────┤
│ 2. CONCIERGE MVP        │ Best for: Data extraction, auditing, and     │
│    (Manual Delivery)    │ niche reporting. Manually deliver the result │
│                         │ for 3–5 clients before writing any code.     │
├─────────────────────────┼──────────────────────────────────────────────┤
│ 3. WIZARD OF OZ MVP     │ Best for: AI tools & interactive workflows.  │
│    (Simulated Backend)  │ Front-facing form / UI simulates automation, │
│                         │ while founder manually executes the logic.   │
├─────────────────────────┼──────────────────────────────────────────────┤
│ 4. PAID PILOT / PRE-PAY │ Best for: High-ticket B2B micro-SaaS.        │
│    (Letter of Intent)   │ Customer puts down a refundable deposit or   │
│                         │ signs a 3-month pilot agreement.             │
├─────────────────────────┼──────────────────────────────────────────────┤
│ 5. SMOKE TEST PAGE      │ Best for: Self-serve B2C/B2B & keepsakes.    │
│    (Real Price + Click) │ Landing page with exact price tag & Stripe   │
│                         │ checkout click tracking (zero backend code). │
└─────────────────────────┴──────────────────────────────────────────────┘
```

---

## 📋 The Mom Test Protocol (Customer Discovery)

When speaking with potential users, adhere strictly to Rob Fitzpatrick's rules:
1. **Talk about their life and past actions, not your idea.**
2. **Ask about specific instances in the past, never generalities or hypotheticals.**
3. **Listen 80% of the time, speak 20%.**

### The 5 Essential Mom Test Questions:
1. *"When was the last time you had to deal with [problem]?"* (`[VERIFIED]` recency & frequency).
2. *"Can you walk me through what you did step-by-step to handle it?"* (`[VERIFIED]` workflow & friction).
3. *"What other solutions or tools did you try before settling on this?"* (`[VERIFIED]` active search behavior).
4. *"What do you dislike about your current setup, and what does that workaround cost you in time or money?"* (`[VERIFIED]` severity).
5. *"In the past 12 months, have you paid for any software, freelancer, or tool to help fix this?"* (`[VERIFIED]` willingness to pay).

### The Commitment Ask at the End (Choose One):
* **Time Commitment:** *"I’m testing a manual workflow prototype next Tuesday. Would you spend 15 minutes reviewing it with your actual data?"*
* **Reputation Commitment:** *"Would you introduce me to the colleague who makes the purchasing decision for this workflow?"*
* **Financial Commitment:** *"We are onboarding 5 founding users at $X/month with direct priority support. Would you like to reserve a spot?"*

---

## 🛑 Pre-Registered Falsification Gates

Before spending money on ads or hours on interviews, pre-register the exact pass/fail criteria in `.microsaas/state.json`:

```markdown
# Riskiest Assumption & Falsification Plan

- **Riskiest Assumption:** [e.g., Shopify store owners will pay $29/mo for automated stock alerts]
- **Chosen Experiment:** [Mom Test / Concierge / Wizard of Oz / Smoke Page / Paid Pilot]
- **Sample Size / Target Quota:** [e.g., 8 interviews conducted OR 200 targeted visitors]

### Pass / Fail Falsification Thresholds:
- **PASS Criteria:** [e.g., At least 3 prospects show proof of paying for alternatives AND 2 agree to a paid pilot]
- **FAIL Criteria:** [e.g., Prospects claim interest but zero show past spending or commit to trial]
- **Action on Fail:** Stop development immediately. Revisit problem discovery or pivot ICP.
```

---

## 📈 Post-Beta Signal: Sean Ellis 40% Test

Once early users experience the core workflow (via Concierge, Wizard of Oz, or initial Walking Skeleton), ask:
> *"How would you feel if you could no longer use this product?"*
> 1. Very disappointed
> 2. Somewhat disappointed
> 3. Not disappointed (it isn't really that useful)
> 4. N/A – I no longer use it

*Benchmark:* If **$\ge 40\%$** answer **"Very disappointed"**, you have early signal of product-market fit. If $< 40\%$, do not scale marketing—iterate on the core workflow.

---

## 📄 Required Output Artifact

Save all observable outcomes in `validation-ledger.md`:
* The isolated Riskiest Assumption and chosen experiment.
* Exact quotes, past tools used, and dollars previously spent by prospects.
* Gate Results: Did the experiment meet the pre-registered PASS criteria?
* Final Recommendation: **PROCEED TO PRODUCT / PIVOT / KILL**.
* Human Sign-Off Checkpoint.
