# Strategic Reconciliation Memo Template

> **Purpose:** Triggered when the Meta-Governance Engine detects a contradiction between new evidence and previous assumptions or decisions. Prevents agent amnesia and ensures strategic coherence.

---

## 1. Contradiction Identification

* **Project Name:** [Project Name]
* **Detection Date:** [YYYY-MM-DD]
* **Active Stage:** [e.g., Stage 2: Research / Stage 3: Validation]

### Conflicting Claims:
* **Prior Claim / Assumption (`source-ledger.md`):**
  * **Claim ID:** [e.g., CLM-008]
  * **Statement:** [e.g., "No self-serve tool exists for Shopify multi-location inventory syncing."]
  * **Confidence Level:** `[CONF=0.4]`
  * **Source / Context:** [e.g., Initial discovery Reddit search]
* **New Observable Finding (`source-ledger.md`):**
  * **Claim ID:** [e.g., CLM-031]
  * **Statement:** [e.g., "Shopify rolled out native Stocky multi-location transfer alerts on all standard plans."]
  * **Confidence Level:** `[CONF=0.7]`
  * **Source / URL:** [https://help.shopify.com/en/manual/products/inventory/transfers]

---

## 2. Impact Assessment & Friction Analysis

* **Severity:** `[FATAL | SERIOUS | MINOR]`
* **Strategic Implication:**
  * Does this eliminate our competitive wedge? `[YES / NO]`
  * Does this invalidate customer willingness to pay? `[YES / NO]`
  * Does this make customer acquisition cost unviable? `[YES / NO]`
* **Root Cause Analysis:** Why was the prior assumption incorrect? [e.g., Relied on outdated 2023 forum discussions prior to platform update].

---

## 3. Reconciliation Decision & Action Path

Select one strategic resolution:

- [ ] **Option A: PIVOT THE WEDGE**
  * Shift from general multi-location alerts to a specific under-served niche (e.g. perishable bakery inventory with batch expiration dates).
- [ ] **Option B: KILL THE OPPORTUNITY**
  * Concede that the problem is natively solved. Stop development, record learnings in `.microsaas/decision-log.md`, and save weeks of wasted coding.
- [ ] **Option C: REVISE SCOPE & RE-VALIDATE**
  * Formulate an urgent Riskiest Assumption Test (RAT) to test if users still have unaddressed pain despite the native feature.

### Final Reconciliation Rationale:
[Provide 2-3 sentences explaining why this resolution protects capital, time, and focus.]

### Governance Sign-Off:
* **Superseded Claims Updated in `source-ledger.md`:** `[YES]`
* **Decision Appended to `decision-log.md`:** `[YES]`
* **Founder Approval:** `[APPROVED on YYYY-MM-DD]`
