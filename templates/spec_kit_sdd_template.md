# Spec-Driven Development (SDD) Template (GitHub Spec Kit)

> **File:** `spec_kit_sdd_template.md`  
> **Methodology:** GitHub Spec Kit + YC Principles + Shape Up Appetite + Vertical Slicing  
> **Mandate:** An MVP is the smallest product that delivers a complete customer outcome, not the smallest collection of features.

---

## 1. Specification (`spec.md`)

### 1.1 Product Summary & Strategic Boundary
* **Product Name:** [Name]
* **One-Sentence Pitch:** For **[Narrow ICP]** who struggles with **[acute pain]**, our product delivers **[measurable outcome]** without **[frustrating status-quo compromise]**.
* **Narrow Initial Customer Profile (ICP):** [e.g. Solo Shopify apparel founders doing $20k–$50k/mo]
* **Development Appetite (Shape Up):** [e.g. 1–2 weeks maximum solo sprint]
* **Core Job-to-be-Done (JTBD):** When [situation], I want to [action], so I can [desired outcome].

### 1.2 The Single Core Value-Delivery Workflow
```text
[Step 1: Input / Trigger] ──▶ [Step 2: Processing Engine] ──▶ [Step 3: Outcome Realization & Checkout]
```
*Any proposed feature not directly sitting on this workflow is discarded for V1.*

### 1.3 Scope Boundaries (Strict MoSCoW & Appetite)
* **MUST HAVE (Strict limit $\le 3$ core capabilities):**
  1. [Feature 1: Direct core value realization]
  2. [Feature 2: Minimal configuration or persistence]
  3. [Feature 3: Checkout / export mechanism]
* **WON'T HAVE IN V1 (Explicitly forbidden scope):**
  * ❌ No multi-tenant enterprise user roles or team permissions
  * ❌ No custom dark mode toggle or dashboard themes
  * ❌ No AI chatbot if static logic or forms suffice
  * ❌ No custom OAuth providers beyond Google/Email magic links
  * ❌ No complex dashboards when an automated email or PDF delivers value

### 1.4 Architecture & Stack Selection
* **Frontend:** [e.g., Next.js 15 App Router / Tailwind CSS / Lucide Icons]
* **Backend / API:** [e.g., Next.js Server Actions or FastAPI]
* **Database / Cache:** [e.g., Supabase PostgreSQL or Upstash Redis]
* **Fulfillment / Billing:** [e.g., Stripe Checkout / Gelato Print-on-Demand Webhooks]
* **Hosting:** [e.g., Vercel / Cloudflare Workers]

### 1.5 Distinctive UI/UX Architecture & Aesthetics (Anti-AI-Slop)
* **Design Archetype:** [Obsidian & Phosphor | Warm Atelier | Midnight Cobalt | Neo-Brutalist Studio]
* **Typography Pairing:**
  * **Headings:** [e.g., Cabinet Grotesk / Syne / Instrument Serif / Clash Display]
  * **Body / UI:** [e.g., Plus Jakarta Sans / General Sans / Satoshi / Switzer]
  * **Code / Numbers:** [e.g., JetBrains Mono / Fragment Mono / DM Mono]
* **Usability First:** Single Primary CTA per screen, Jobs-to-be-Done hierarchy, Progressive Disclosure of advanced settings.
* **Atmospheric Depth:** Subtle radial spotlight `rgba(var(--accent-rgb), 0.12)` or 28px masked microgrid; top rim light `inset 0 1px 0 rgba(255,255,255,0.08)`.
* **Page Entrance Motion:** Pure CSS staggered reveals (`revealUp` with 80ms increments, `cubic-bezier(0.16, 1, 0.3, 1)` easing).
* **Mobile Ergonomics:** Pinned bottom-third primary CTA, sliding bottom sheets with drag handles for modals ($< 768\text{px}$), minimum $44 \times 44\text{px}$ touch targets.

---

## 2. Data Models (`data-model.md`)

```sql
-- Schema Definition
CREATE TABLE projects (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('draft', 'active', 'archived')),
    metadata JSONB DEFAULT '{}'::jsonb
);

CREATE TABLE transactions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    project_id UUID REFERENCES projects(id) ON DELETE CASCADE,
    stripe_session_id TEXT UNIQUE NOT NULL,
    amount_cents INTEGER NOT NULL,
    currency VARCHAR(3) NOT NULL DEFAULT 'usd',
    status TEXT NOT NULL CHECK (status IN ('pending', 'succeeded', 'failed', 'refunded'))
);

CREATE INDEX idx_projects_user ON projects(user_id);
CREATE INDEX idx_transactions_session ON transactions(stripe_session_id);
```

---

## 3. Tasks & Vertical Slices (`tasks.md`)

Organized into working vertical slices with an early **Walking Skeleton**:

- [ ] **Milestone 1: The Walking Skeleton (End-to-End Tracer Bullet)**
  - [ ] Initialize repository with Next.js, Tailwind, and theme tokens.
  - [ ] Scaffold database connection and minimal table schema.
  - [ ] Implement bare-minimum end-to-end path: user submits dummy input $\rightarrow$ server processes $\rightarrow$ preview renders on screen.
  - [ ] *Verification:* Verify complete user journey runs locally end-to-end.
- [ ] **Milestone 2: Core Vertical Slices**
  - [ ] **Slice A (Core Calculation / Extraction Engine):** Build real engine logic with automated unit tests for edge cases.
  - [ ] **Slice B (User Input & Dynamic Preview UI):** Build distinctive input screen with inline validation and staggered entrance reveal.
  - [ ] **Slice C (Checkout & Monetization):** Integrate Stripe Checkout session and verify webhook fulfillment handler.
- [ ] **Milestone 3: First Customer Verification & Deployment**
  - [ ] Deploy to production hosting with custom domain and SSL.
  - [ ] Execute real \$1 test transaction to verify payment-to-fulfillment loop.
  - [ ] Onboard first customer manually (*Do Things That Don't Scale*).
