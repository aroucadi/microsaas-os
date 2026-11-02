---
name: microsaas-product
description: >-
  Product strategy, Amazon PR/FAQ, MVP definition, and Spec-Driven Development (SDD) for micro-SaaS.
  Use when defining product scope, writing PR/FAQs, designing lean user journeys, preventing feature bloat,
  and creating complete GitHub Spec Kit technical specifications before coding.
---

# Micro-SaaS Product Strategy & Spec-Driven Development (`microsaas-product`)

Use this skill to design the product from the customer's desired outcome backwards, eliminate feature bloat, and produce airtight **Spec-Driven Development (SDD)** artifacts for AI coding agents.

---

## 📦 Part 1: Amazon Working Backwards (PR/FAQ)

Before writing any code or technical architecture, author a 1-page **Press Release & FAQ (PR/FAQ)** as if the product has already successfully launched.

### Structure of the PR/FAQ:
1. **Headline:** Name the product in a way the target customer immediately understands.
2. **Subheadline:** One sentence describing who it is for and the primary benefit.
3. **Summary Paragraph:** City, Date — Briefly state what the product is and why it was released.
4. **The Problem:** Describe the specific, painful frustration customers had before this product existed.
5. **The Solution (How It Works):** Explain simply how the product solves the problem in 3 steps.
6. **Customer Quote:** A realistic quote from an early customer describing how much time, money, or stress they saved.
7. **Call to Action:** Where to get it, pricing, and how to get started in 60 seconds.
8. **Customer FAQ:** 5 questions addressing pricing, data privacy, integrations, refunds, and technical requirements.

---

## 🎯 Part 2: Jobs To Be Done (JTBD) & MoSCoW MVP Boundary

Define the core job:
> *"When **[trigger situation]**, I want to **[perform action]**, so I can **[achieve desired outcome]**."*

### The Strict MoSCoW MVP Rule:
A micro-SaaS MVP must contain **at most 3 core capabilities**. Everything else is discarded for V1.

* **MUST HAVE (Strictly $\le 3$ items):** The absolute minimum technical path needed for the user to experience the "Aha!" moment and pay.
* **SHOULD HAVE:** Important features reserved for V1.1 (after first 10 paying customers).
* **COULD HAVE:** Nice-to-have ideas logged in the backlog.
* **WON'T HAVE (This Sprint):** Features explicitly banned from the MVP (e.g. multi-user teams, dark mode toggle, complex custom settings, native mobile apps, custom dashboard widgets).

---

## 📐 Part 3: Spec-Driven Development (GitHub Spec Kit Protocol)

Once the PR/FAQ and MVP scope are locked, create the technical blueprint in `.specs/`:

```text
.specs/
├── spec.md          # Functional specifications, user stories & acceptance criteria
├── data-model.md    # Schema, database tables, API payloads & state
└── tasks.md         # Step-by-step sequential implementation checklist
```

### 1. `spec.md` (Functional Specifications):
* **User Stories & Given-When-Then Acceptance Criteria:**
  ```gherkin
  Scenario: Customer completes instant order
    Given an anonymous user on the landing page
    When they enter valid inputs (date, city, or API key)
    Then a real-time preview renders in < 2 seconds
    And a Stripe Checkout session is created upon clicking "Buy Now"
  ```
* **Error Handling & Edge Cases:** How the system handles empty inputs, third-party API timeouts, failed card payments, or invalid formats.

### 2. `data-model.md` (Architecture & Data Contracts):
* **Tech Stack Selection:** Prefer simple, robust, well-supported stacks:
  * Frontend/Backend: Next.js (App Router) + Tailwind CSS + TypeScript.
  * Database: Supabase (PostgreSQL) or SQLite / simple cloud KV.
  * Payment: Stripe Checkout (Hosted payment page, zero custom credit card UI).
  * Storage/Fulfillment: Cloudflare R2 / AWS S3 + Gelato/Printful Webhook API.
* **Database Tables & Types:** Table schemas, foreign keys, and indexes.
* **API Endpoints:** Request/response schemas for all internal API routes.

### 3. `tasks.md` (Sequential Implementation Checklist):
* Break the build into small, verifiable chunks (each task executable in 30–60 minutes):
  - [ ] Task 1: Initialize Next.js project with Tailwind and core layout.
  - [ ] Task 2: Implement core calculation / parsing engine with unit tests.
  - [ ] Task 3: Build interactive canvas / output preview component.
  - [ ] Task 4: Connect Stripe Checkout webhook for order fulfillment.
  - [ ] Task 5: Implement automated deliverable generator (PDF/Webhook/Email).
  - [ ] Task 6: End-to-end user journey test (from landing page to confirmed order).

---

## 🛡️ AI Coding Guardrails (For Coding Agents)

When an AI coding agent executes `tasks.md`:
1. **Single-Task Execution:** Complete one task at a time and verify it with automated tests or terminal checks before proceeding.
2. **No Dependency Sprawl:** Do not install heavy or obscure npm packages when standard native libraries suffice.
3. **Preserve Simplicity:** Resist the urge to add abstractions, microservices, or complex state management until proven necessary.
4. **End-to-End Verification:** Before declaring the MVP complete, run a full simulated purchase using Stripe Test Mode to verify that money is captured and the deliverable is generated.

---

## 📄 Required Output Artifacts

Save in the project repository:
1. `pr-faq.md` (Amazon-style Press Release & Customer FAQ).
2. `.specs/spec.md` (Functional specs & acceptance criteria).
3. `.specs/data-model.md` (Database schema & API contracts).
4. `.specs/tasks.md` (Sequential build task list).
5. Human Sign-Off Checkpoint before initiating development.
