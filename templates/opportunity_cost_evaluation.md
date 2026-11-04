# Expected Value of Information (EVOI) & Opportunity Cost Framework

> **The Meta-Governor Mandate:** "Is this the best use of the founder's next 4 hours?"  
> Maximize uncertainty reduction per hour invested. Never spend weeks writing speculative code when a 2-day or 4-hour experiment can invalidate the fatal premise.

---

## 1. Mathematical Grounding: True EVSI vs. Operational Heuristic

In classical decision theory and Bayesian experimental design, the **Expected Value of Sample Information (EVSI)** measures the expected increase in decision utility resulting from observing experimental evidence $E$:

$$\text{EVSI} = \mathbb{E}_{E}\left[ \max_{a \in \mathcal{A}} \mathbb{E}_{X|E}[U(a, X)] \right] - \max_{a \in \mathcal{A}} \mathbb{E}_{X}[U(a, X)]$$

Where:
* $\mathcal{A}$ is the set of possible strategic decisions (e.g. advance to build, pivot ICP, kill venture).
* $X$ is the true state of the market (e.g. real willingness-to-pay, platform policy stability).
* $U(a, X)$ is the net commercial payoff of decision $a$ under market state $X$.
* $E$ is the observable experimental outcome from the test (e.g. customer interviews, smoke test conversions).

### The Operational Heuristic: EVOI-Inspired Prioritization Heuristic (EIPH)
Because calculating full continuous probability distributions over market states is intractable in conversational agent workflows, the Meta-Governor evaluates an **EVOI-Inspired Prioritization Heuristic (EIPH)** for ranking competing initiatives:

$$\text{EIPH Score} = \frac{I \times \left[ P(\text{success}) \times V_{\text{success}} - (1 - P(\text{success})) \times C_{\text{fail}} \right] \times R}{T_{\text{evidence}} \times C_{\text{exp}}}$$

---

## 2. Metric Definitions & Scoring Rubric

| Variable | Description | Scale / Units | Evaluation Guide |
| :--- | :--- | :---: | :--- |
| **$I$ (Information Gain)** | How decisively does this experiment eliminate the focal uncertainty? | 1.0 – 5.0 | **5.0:** Binary proof (payment collected or rejected).<br/>**3.0:** Strong signal (5 in-depth user interviews).<br/>**1.0:** Ambiguous noisy signal (social poll). |
| **$P(\text{success})$** | Prior probability that the hypothesis is true | 0.05 – 0.95 | Based on existing 4D evidence (default: 0.30 for unproven assumptions). |
| **$V_{\text{success}}$** | Commercial value if hypothesis is validated | Normalized ($1 – $10) | Projected annualized gross margin if verified. |
| **$C_{\text{fail}}$** | Downside loss if hypothesis is false | Normalized ($1 – $10) | Cost of building without knowing (wasted engineering sprints). |
| **$R$ (Reversibility Factor)** | Two-way door vs. One-way door discount | 0.2 – 1.0 | **1.0:** Easily reversible 2-way door (Concierge, Mom Test, Smoke page).<br/>**0.5:** Moderately difficult to undo (custom data model, brand name).<br/>**0.2:** Irreversible 1-way door (long-term contract, patent, hardware tooling). |
| **$T_{\text{evidence}}$** | Wall-clock time to receive conclusive signal | Days (or Hours / 24) | **0.17:** $\le 4$ hours.<br/>**1.0:** 1 day.<br/>**7.0:** 1 week.<br/>**21.0:** 3 weeks. |
| **$C_{\text{exp}}$** | Direct financial and opportunity cost of running experiment | Normalized ($1 – $5) | **1.0:** Founder time only ($0 cash).<br/>**3.0:** Ad spend / software fees ($50-$200).<br/>**5.0:** Heavy outsource or dev build ($500+). |

---

## 3. The 4-Hour Acid Test (Proxy Experimentation)

Before committing to any experiment requiring $> 48$ hours ($T_{\text{evidence}} > 2$):

> **Can we get 80% of this information in under 4 hours?**

* **Heavy Path ($> 5$ days):**  
  *Example:* Write backend webhooks processor, database migrations, authentication, billing integration.
* **4-Hour Proxy Path ($\le 4$ hours):**  
  *Example:* Build a 1-page static mock, manually trigger 3 Stripe test webhooks in CLI, export JSON report, and email it to 3 target leads with a Stripe payment link.
* **Proxy Test Verdict:**  
  *If proxy yields negative signal $\rightarrow$ save 3 weeks of code immediately.*

---

## 4. Operational Prioritization Ranking

When comparing multiple potential initiatives in `.microsaas/state.json`:

| Rank | Initiative | Type | Est. Time ($T$) | Reversibility ($R$) | EIPH Score | Action |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| **#1** | [Mom Test 5 Calls] | RAT | 4 hrs | 1.0 (2-way) | **High** | **Execute First** |
| **#2** | [Smoke Page Test] | RAT | 6 hrs | 1.0 (2-way) | **Medium** | Queue next |
| **#3** | [Build Full Auth & DB] | Code | 80 hrs | 0.4 (1-way) | **Low** | **Blocked** by #1 & #2 |

---

## 5. Meta-Governor Execution Directive

- [ ] **EXECUTE IMMEDIATELY:** Highest EIPH, low time-to-evidence, highly reversible.
- [ ] **CHALLENGE FOR PROXY:** Good hypothesis, but proposed implementation is too heavy ($T > 2$ days). Replace with 4-hour proxy.
- [ ] **BLOCK / REJECT:** Downstream engineering tasks masquerading as validation.
