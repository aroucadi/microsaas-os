---
name: microsaas-research
description: >-
  Market research, competitive intelligence, and opportunity evaluation for micro-SaaS.
  Use when analyzing competitors, evaluating market saturation, checking pricing benchmarks,
  identifying incumbent vulnerabilities, calibrating evidence confidence, or crafting a Red Team Decision Memo.
---

# Micro-SaaS Market Research & Adversarial Intelligence (`microsaas-research`)

Use this skill to rigorously audit competitors, detect contradictions with early assumptions, and determine whether entering a market is commercially viable. **Your primary duty here is to challenge the idea and attempt to disprove it**, not to confirm the founder's excitement.

> **Research Axiom:** An unverified competitor claim is worth 0. Ground all findings in accessible primary URLs using the 4D Evidence Model.

---

## 🔬 The 4-Part Research Protocol

### Part 1: Verify the Competitive Reality (4D Evidence Calibrated)
Search for 3 to 6 actual, verifiable alternatives across three tiers:
1. **Direct Competitors:** Software or services offering substantially the same solution.
2. **Free Workarounds / Platform Native Tools:** Free native features (e.g. AWS free tier, Google Sheets, Canva, Zapier free).
3. **Enterprise Goliaths:** Large VC-backed or public companies.

For each competitor, record in `source-ledger.md`:
* **Product Name & Live URL** (`[Reliability: High, Strength: Direct]`)
* **Pricing Model & Public Price Points** (cite live pricing page URL)
* **What Customers Complain About** (cite G2, Trustpilot, or Reddit complaints)
* **Recency & Independence:** Is the pricing fresh (< 6 months) and verified independently?

---

### Part 2: Contradiction Detection Check

Before crafting the strategic memo, cross-check newly discovered competitor facts against earlier discovery claims in `opportunity-brief.md`:
* **Check A (Competitor Non-Existence):** If discovery claimed *"No tool exists for this"*, but research found active competitors $\rightarrow$ Flag `⚠️ [CONTRADICTION DETECTED]`.
* **Check B (Pricing Feasibility):** If discovery assumed users will pay \$49/mo, but research shows incumbents offering it for free or \$5/mo $\rightarrow$ Flag `⚠️ [CONTRADICTION DETECTED]`.

*Rule:* If any fatal contradiction is uncovered, immediately trigger a [Strategic Reconciliation Memo](templates/strategic_reconciliation_memo.md) before issuing any GO recommendation.

---

### Part 3: The Red Team Strategic Decision Memo (No Arbitrary Score Cutoffs)

Instead of relying on an arbitrary numerical score (e.g. 18/30), the Adversarial Red Team produces a structured strategic decision memo answering four foundational questions:

#### 1. Fatal Risks (Mandatory Investigation):
* Can an established platform (Shopify, Google, Apple, AWS) wipe out this product as a minor quarterly release?
* Does the business rely on scraping, private APIs, or fragile platform hacks subject to sudden revocation?
* Are customer acquisition costs (Google Ads CPC $> \$20$) structurally higher than what a micro-SaaS can afford?

#### 2. Structural Incumbent Weaknesses (Where They Are Vulnerable):
* Are competitors bloated, enterprise-only, and forcing mandatory sales demos with 12-month lock-in?
* Are existing solutions complex, requiring hours of onboarding and developer setup?
* Do user reviews repeatedly complain about slow customer support, bug-ridden interfaces, or excessive price hikes?

#### 3. Asymmetric Wedge Definition (How We Win):
* **Speed Wedge:** Can the customer realize value in under 60 seconds without onboarding calls or configuration?
* **Micro-Niche Wedge:** Are we hyper-tailored to a neglected vertical (e.g. Shopify apparel stores with perishable batch tracking) that Goliaths ignore?
* **Monetization Wedge:** Do we offer transparent pay-as-you-go or flat micro-pricing without contracts?

#### 4. Unresolved Uncertainties (Targeted Experiments):
* What critical assumption remains unproven? (e.g. "Do merchants care enough about audit compliance to pay \$49/mo?").
* Formulate the exact Riskiest Assumption Test (RAT) needed to eliminate this uncertainty.

---

### Part 4: Strategic Recommendations (3-Tier Precision)

Synthesize the audit into one of four clear recommendations:

* 🟢 **PROCEED TO RAT VALIDATION (Green Light):**
  * Competitors verified with direct URLs. Incumbents have structural weaknesses.
  * Survived all 3 Red Team killer questions with an identifiable asymmetric wedge.
  * $\rightarrow$ **Action:** Route to `microsaas-validation` to test the single unresolved uncertainty.

* 🟡 **KILL THE WEDGE (Reposition ICP):**
  * The problem is valid, but the target customer segment is too price-sensitive or dominated by cheap clones.
  * $\rightarrow$ **Action:** Keep the core problem; pivot to an underserved niche with budget.

* 🟡 **KILL THE SOLUTION (Redesign Delivery):**
  * The customer pain is verified, but competitors have already commoditized the SaaS interface.
  * $\rightarrow$ **Action:** Shift from standalone software to a lightweight browser extension, API micro-service, or Concierge model.

* 🔴 **KILL THE VENTURE (Terminal Red Light):**
  * Platform native tools provide this for free, switching friction is near-impossible, or fatal legal/TOS blocks exist.
  * $\rightarrow$ **Action:** Halt the project immediately. Record findings in `.microsaas/decision-log.md` and return to the opportunity backlog.

---

## 📄 Required Output Artifact

Save the complete findings in `competitive-audit.md`:
1. Competitor Comparison Table (URLs, pricing, verified complaints, 4D evidence ratings).
2. Contradiction Check Summary (Verified or Reconciled).
3. The Red Team Strategic Decision Memo (Fatal Risks, Incumbent Weaknesses, Asymmetric Wedge).
4. Unresolved Uncertainties & Recommended RAT Experiment.
5. Action Verdict: **PROCEED TO RAT / KILL WEDGE / KILL SOLUTION / KILL VENTURE**.
6. Human Sign-Off Checkpoint.
