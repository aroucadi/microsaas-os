# Spec-Driven Development (SDD) Template (GitHub Spec Kit)

> **File:** `spec_kit_sdd_template.md`  
> **Purpose:** Prevents premature coding and feature creep by defining exact product scope, data models, and atomic tasks before writing a single line of application code.

---

## 1. Specification (`spec.md`)

### 1.1 Product Summary & User Journey
* **Product Name:** [Name]
* **Target User (ICP):** [Specific persona experiencing an acute, unaddressed pain]
* **Core Job-to-be-Done (JTBD):** When [situation], I want to [action], so I can [desired outcome].
* **3-Step Critical Flow:**
  1. **Input:** User does [Step 1: e.g., pastes API webhook URL / enters birthdate and location]
  2. **Processing:** System executes [Step 2: parses payload / fetches astronomical ephemeris / calls template engine]
  3. **Output/Value Realization:** User receives [Step 3: instant Slack alert / high-resolution vector print ready for checkout]

### 1.2 Scope Boundaries (Strict MoSCoW)
* **MUST HAVE (Strict limit $\le 3$ core features):**
  1. [Feature 1: Direct core value realization]
  2. [Feature 2: Minimal configuration or persistence]
  3. [Feature 3: Checkout / export mechanism]
* **WON'T HAVE IN V1 (Explicitly forbidden scope):**
  * ❌ No multi-tenant enterprise user roles or team permissions
  * ❌ No custom dark mode toggle or dashboard themes
  * ❌ No AI chatbot if static logic or forms suffice
  * ❌ No custom OAuth providers beyond Google/Email magic links

### 1.3 Architecture & Stack Selection
* **Frontend:** [e.g., Next.js 15 App Router / Tailwind CSS / Lucide Icons]
* **Backend / API:** [e.g., Next.js Server Actions or FastAPI]
* **Database / Cache:** [e.g., Supabase PostgreSQL or Upstash Redis]
* **Fulfillment / Billing:** [e.g., Stripe Checkout / Gelato Print-on-Demand Webhooks]
* **Hosting:** [e.g., Vercel / Cloudflare Workers]

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

## 3. Atomic Task Breakdown (`tasks.md`)

Each task represents 1-2 hours of autonomous AI or founder coding, fully verifiable with unit/integration tests.

- [ ] **Phase 1: Project Scaffolding & Setup**
  - [ ] Initialize repository with clean directory structure, linter, and environment configuration.
  - [ ] Configure database schema, migrations, and local seed data.
- [ ] **Phase 2: Core Value Engine**
  - [ ] Implement data extraction/processing pipeline.
  - [ ] Implement unit tests validating data accuracy on edge cases.
- [ ] **Phase 3: Critical User Interface**
  - [ ] Build minimal user input screen with inline validation.
  - [ ] Build preview/results display screen.
- [ ] **Phase 4: Monetization & Integration**
  - [ ] Integrate Stripe Checkout session creation and success/cancel routes.
  - [ ] Implement Stripe webhook endpoint with signature verification.
- [ ] **Phase 5: Production Deployment & Verification**
  - [ ] Deploy to production hosting with production SSL and domain.
  - [ ] Execute live $1 test transaction to verify payment-to-fulfillment loop.
