---
name: microsaas-discovery
description: >-
  Systematic opportunity hunting and idea discovery for micro-SaaS.
  Use when brainstorming new product concepts, looking for profitable niches, mining customer complaints
  from Reddit/forums, unbundling monolithic software, or discovering programmatic keepsake opportunities.
---

# Micro-SaaS Idea Discovery & Opportunity Hunting (`microsaas-discovery`)

Use this skill to systematically identify, score, and shortlist high-probability micro-SaaS opportunities before committing research or development hours. Every opportunity must be grounded in **observable evidence**, not founder daydreaming.

---

## 🎯 The 4 Discovery Archetypes

Identify which archetype the idea belongs to:

```text
┌─────────────────────────────────┬─────────────────────────────────┐
│ 1. THE WORKFLOW AUTOMATOR       │ 2. THE NICHE UNBUNDLER          │
│ Takes a multi-step manual       │ Takes one specific feature      │
│ process (Excel/PDF/Zapier)      │ of a bloated enterprise tool    │
│ and turns it into a 1-click app │ and makes it 10x faster for     │
│ Example: PDF tender bid         │ one vertical or tribe.          │
│ leveling for contractors.       │ Example: CRM for tattoo artists.│
├─────────────────────────────────┼─────────────────────────────────┤
│ 3. THE PROGRAMMATIC KEEPSAKE    │ 4. THE API WRAPPER / SENTINEL   │
│ Takes public data + narcissism  │ Monitors an API, cron job, or   │
│ or love/tribalism to generate   │ critical SaaS event and alerts/ │
│ instant custom gifts & posters. │ heals when things break.        │
│ Example: The Night We Met /     │ Example: Webhook dead-letter    │
│ BornHere / Sports stadium maps. │ alert desk for Stripe stores.   │
└─────────────────────────────────┴─────────────────────────────────┘
```

---

## 🔍 The 5-Step Discovery Protocol

### Step 1: Mine Observable Pain Signals (Web Search Mandatory)
Do not brainstorm in a vacuum. Execute real web searches to verify active frustration:
1. **Reddit & Forum Mining:**
   * Search queries:
     * `"site:reddit.com/r/SaaS 'how do I automate'"`
     * `"site:reddit.com 'is there an alternative to' [tool]"`
     * `"site:reddit.com 'I hate [software] because'"`
   * Record the exact Reddit post URL and quote in `source-ledger.md`.
2. **Review Mining (G2, Capterra, Shopify App Store):**
   * Filter for **2-star and 3-star reviews** of established market leaders.
   * Look for recurring complaints: *"Too bloated"*, *"Support takes 4 days"*, *"Overpriced for my simple use case"*.
3. **The "Messy Spreadsheet" Signal:**
   * Look for businesses managing mission-critical operations inside an unstable Google Sheet or Airtable base.

### Step 2: The Solo Founder Viability Filter (Hard Gates)
If an idea fails ANY of these 5 criteria, **DISCARD IT IMMEDIATELY**:
* [ ] **Build Time:** Can a solo developer build the core value loop in $\le 10$ business days?
* [ ] **Operational Passivity:** Can delivery and billing run 100% automated without human consulting hours?
* [ ] **Liability Boundary:** Does it avoid high-risk legal, medical, or life-critical compliance certifications?
* [ ] **Time-to-Value:** Can the user see an interactive preview or experience the "Aha!" moment in $< 60$ seconds?
* [ ] **Accessible Distribution:** Can we reach the first 50 customers without a direct enterprise outbound sales team?

### Step 3: Define the Epistemic Breakdown
Break down the core problem into facts vs. assumptions:
* **`[VERIFIED]`:** *"Competitor X charges $49/mo and has 500 reviews on G2 [URL]."*
* **`[SECONDARY]`:** *"Reddit users complain about feature Y in thread [URL]."*
* **`[ASSUMPTION]`:** *"Users will pay $15/mo for a stripped-down standalone tool."* (Must be validated in Stage 3).

### Step 4: Complete the Opportunity Brief
For every shortlisted idea, produce a standardized `opportunity-brief.md` in the project directory:

```markdown
# Opportunity Brief: [Product Name / Working Title]

- **Discovery Archetype:** [Workflow Automator / Niche Unbundler / Programmatic Keepsake / API Sentinel]
- **Target User:** [Specific human role and context]
- **The Hair-on-Fire Pain / Emotional Trigger:** [What urgent problem or emotional desire triggers purchase?]
- **Evidence of Pain (`[VERIFIED]` / `[SECONDARY]`):** [Quote & URL from Reddit, G2, or industry source]
- **Current Workarounds:** [What do they do right now? (e.g. 3 hours in Excel, Photoshop templates)]
- **Proposed Solution (in 1 sentence):** [What the micro-SaaS does in 30 seconds]
- **Monetization Angle:** [$X one-time impulse / $Y physical POD / $Z recurring micro-sub]
- **Distribution Wedge:** [Programmatic SEO, Short-form viral video, Niche subreddit]
- **Key Unverified Assumptions (`[ASSUMPTION]`):** [List 1–3 critical hypotheses to test]
```

### Step 5: Opportunity Scorecard Audit
Score the idea using [`opportunity_scoring_rubric.md`](./references/opportunity_scoring_rubric.md):
* **$\ge 28$ / 35 Points:** **TIER 1 WINNER** $\rightarrow$ Proceed to `microsaas-research`.
* **21–27 Points:** **TIER 2 RESERVE** $\rightarrow$ Keep in backlog.
* **$< 21$ Points:** **REJECT** $\rightarrow$ Discard.
