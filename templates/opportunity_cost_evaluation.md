# Opportunity Cost & Experiment Prioritization Template

> **Core Question:** "Is this the best use of the founder's next 4 hours?"  
> **Mandate:** Maximize uncertainty reduction per hour invested. Never spend 3 weeks building something that a 2-day experiment could invalidate.

---

## 1. Initiative / Opportunity Candidate

* **Proposed Initiative:** [e.g., Build multi-tenant team dashboard vs. Run 5 Mom Test calls with compliance managers]
* **Target Uncertainty to Resolve:** [e.g., Will enterprise clinics pay $99/mo for team roles?]
* **Active Capability Domain:** `[Discovery | Research | Validation | Product | Engineering | Distribution]`

---

## 2. Priority Scoring Formula

$$\text{Priority Score} = \frac{\text{Expected Commercial Value} \times \text{Uncertainty Reduction}}{\text{Time to Evidence} \times \text{Resource Cost}}$$

| Scoring Metric | Range | Assessment for This Initiative | Score (1-5) |
| :--- | :---: | :--- | :---: |
| **1. Expected Commercial Value** | 1 (Low) - 5 (High) | How significantly does this impact revenue potential? | [Score] |
| **2. Uncertainty Reduction** | 1 (Minor) - 5 (Fatal) | Does this resolve an assumption that could kill the company? | [Score] |
| **3. Time to Evidence** | 1 (> 2 wks) - 5 (< 48 hrs) | How quickly will observable customer signal arrive? | [Score] |
| **4. Resource / Build Cost** | 1 (Heavy) - 5 (Near Zero) | How cheap is this in engineering hours and spend? | [Score] |

**Calculated Opportunity Score:** `[High / Medium / Low]`

---

## 3. The 4-Hour Acid Test

Can we get 80% of this signal in under 4 hours?

* **Proposed Heavy Path (e.g. 10 days):** [e.g. Build custom database sync worker and background cron jobs]
* **Lightweight 4-Hour Proxy:** [e.g. Manually export CSV, run python script locally, and email result to client via Concierge delivery]

---

## 4. Governance Verdict

- [ ] **EXECUTE IMMEDIATELY (Highest ROI on Time):** Fast-feedback, high uncertainty reduction.
- [ ] **DEFER / POSTPONE:** Good idea, but downstream of more fatal uncertainties.
- [ ] **REJECT (Low Leverage):** Heavy build time with low informational yield.
