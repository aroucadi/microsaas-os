---
name: microsaas-research
description: >-
  Market research, competitive intelligence, and opportunity evaluation for micro-SaaS.
  Use when analyzing competitors, evaluating market saturation, checking pricing benchmarks,
  identifying incumbent vulnerabilities, or making a GO / NO-GO decision before coding.
---

# Micro-SaaS Market Research & Adversarial Intelligence (`microsaas-research`)

Use this skill to rigorously audit competitors and determine whether entering a market is commercially viable. **Your primary duty here is to challenge the idea and attempt to disprove it**, not to confirm the founder's excitement.

---

## 🔬 The 4-Part Research Protocol

### Part 1: Verify the Competitive Reality (No Guesses)
Search for 3 to 6 actual, verifiable alternatives across three tiers:
1. **Direct Competitors:** Software or services offering substantially the same solution.
2. **Free Workarounds / Platform Native Tools:** Free native features (e.g. AWS free tier, Google Sheets, Canva, Zapier free).
3. **Enterprise Goliaths:** Large VC-backed or public companies.

For each competitor, verify:
* **Product Name & Live URL** (`[VERIFIED]`)
* **Pricing Model & Public Price Points** (`[VERIFIED]` — cite the pricing page URL)
* **What Customers Complain About** (`[SECONDARY]` — cite G2, Trustpilot, or Reddit complaints)
* **Market Position:** Bootstrapped micro-SaaS or funded scale-up?

---

### Part 2: The Competitive Intensity & Moat Assessment

Score the market across these 6 dimensions (1 to 5 points each):

| Dimension | Favorable (Score = 5) | Unfavorable (Score = 1) |
| :--- | :--- | :--- |
| **1. Incumbent Bloat** | Competitors are complex, enterprise-only, and require sales calls. | Competitors have clean, self-serve $9/mo tools with instant onboarding. |
| **2. Free Alternative Threat** | No free tool exists; manual workarounds take hours. | Big tech / platform vendors provide this natively for free. |
| **3. Switching Friction** | Users can adopt our tool alongside existing tools in 60s. | Requires database migrations, DNS changes, or team retraining. |
| **4. Distribution Accessibility** | Clear organic channels (niche Reddit, programmatic SEO, TikTok). | Dominated by competitors with $30+ Google Ads CPCs and enterprise sales reps. |
| **5. Pricing Power** | High willingness to pay relative to cost (clear positive ROI). | Extreme price compression; race to the bottom by cheap clones. |
| **6. Build Feasibility** | Solo founder can build and maintain the core value loop in $\le 10$ days. | Requires complex infrastructure, enterprise compliance (SOC2), or heavy ops. |

*Passing Threshold:* Must score **$\ge 22 / 30$** to proceed to the Red Team challenge.

---

### Part 3: The Adversarial Red Team Challenge (Mandatory Falsification)

Before issuing a recommendation, you must assume the persona of an **adversarial venture partner and skeptical competitor**. Forcefully answer these 3 killer questions:

1. **The Goliath Kill Question:** *"If an established incumbent (or Google/Shopify/AWS) added this as a minor feature update next quarter, does our business die overnight?"*
2. **The Payment Resistance Question:** *"Why will a rational customer refuse to pay us $X and simply stick with their current free workaround (even if messy)?"*
3. **The Hidden Nightmare Question:** *"What is the hidden technical, customer support, or legal landmine that will destroy the solo founder's lifestyle?"*

---

### Part 4: The GO / PIVOT / NO-GO Decision Rules

Synthesize the audit and output an unyielding verdict:

* 🟢 **GO (Green Light):**
  * Moat Score $\ge 22/30$.
  * Incumbents have verified, structural weaknesses (bloat, enterprise sales friction, or high prices).
  * The idea survived all 3 Red Team killer questions with a clear asymmetric wedge (Speed, Micro-Niche, or Pricing Model).
  * $\rightarrow$ **Action:** Proceed to `microsaas-validation`.

* 🟡 **PIVOT (Yellow Light):**
  * Moat Score $16–21/30$.
  * Demand is verified, but head-to-head competition is too intense or commodity risk is high.
  * $\rightarrow$ **Action:** Narrow the target ICP, shift to an underserved vertical, or change the monetization format.

* 🔴 **NO-GO / KILL (Red Light):**
  * Moat Score $< 16/30$, OR the idea fails any of the 3 Red Team killer questions.
  * Platform native tools provide this for free, or customer acquisition costs will exceed lifetime value.
  * $\rightarrow$ **Action:** Terminate the idea immediately. Document the exact rationale in `.microsaas/decision-log.md` and return to `microsaas-discovery`.

---

## 📄 Required Output Artifact

Save the complete findings in `competitive-audit.md`:
1. Competitor Comparison Table (URLs, pricing, verified complaints).
2. Moat Assessment Scorecard (/30).
3. The Adversarial Red Team Audit (The 3 answers).
4. Asymmetric Wedge Definition.
5. Blunt Verdict: **GO / PIVOT / NO-GO**.
6. Human Sign-Off Checkpoint.
