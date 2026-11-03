---
name: microsaas-product
description: >-
  Product strategy, Amazon PR/FAQ, MVP definition, Spec-Driven Development (SDD), and distinctive
  anti-AI-slop UI/UX design architecture for micro-SaaS. Use when defining product scope, writing PR/FAQs,
  designing lean user journeys, establishing bespoke web/mobile aesthetics, and creating complete
  GitHub Spec Kit specifications before coding.
---

# Micro-SaaS Product Strategy, UI/UX Aesthetics & Spec-Driven Development (`microsaas-product`)

Use this skill to design the product from the customer's desired outcome backwards, eliminate feature bloat, craft distinctive **anti-AI-slop** web and mobile interfaces, and produce airtight **Spec-Driven Development (SDD)** artifacts for AI coding agents.

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

## 🎨 Part 3: Distinctive UI/UX Architecture & Anti-AI-Slop Aesthetics (Web & Mobile)

> **Mandate:** AI coding assistants tend to converge toward generic, "on-distribution" outputs—resulting in predictable, lifeless "AI slop" interfaces (generic Inter fonts, purple-on-white gradients, and cookie-cutter 3-card grids).  
> **Reference:** See [`references/frontend_aesthetics_anti_slop.md`](references/frontend_aesthetics_anti_slop.md) for full design archetypes, token recipes, and motion curves.

When creating any UI, landing page, web dashboard, or mobile screen, enforce these 5 design directives:

### 1. Distinctive Typography Pairings (Banish Generic Fonts)
* **Never use:** `Inter`, `Roboto`, `Arial`, or generic `system-ui`. Do not reflexively default to `Space Grotesk`.
* **Select a high-character pairing suited to the product domain:**
  * *DevTools & Technical:* `Syne` or `Cabinet Grotesk` (Headings) + `Plus Jakarta Sans` (Body) + `JetBrains Mono` (Code).
  * *Fintech & Trust:* `Clash Display` or `Archivo` (Headings) + `Switzer` or `General Sans` (Body).
  * *Warm Editorial & Keepsakes:* `Instrument Serif` (Headings) + `Satoshi` or `Newsreader` (Body) + `DM Mono`.
  * *High-Energy SaaS:* `Outfit` or `Cabinet Grotesk` (Headings) + `Figtree` (Body).
* **Implementation:** Use fluid typography (`clamp()`) and tight tracking (`tracking-tight` / `-0.03em`) on headings.

### 2. Cohesive Color Themes & Dominant Accents
* **Never use:** The clichéd purple/indigo gradient on flat white.
* **Commit to a specific aesthetic archetype:**
  * *Obsidian & Phosphor:* `#090a0f` canvas, `#11131b` surface, `#00ff88` emerald accent, `#00b4d8` secondary.
  * *Warm Atelier:* `#fbf9f5` warm paper canvas, `#ffffff` surface, `#1c1a17` espresso text, `#d94826` terracotta accent.
  * *Midnight Cobalt:* `#0b0f19` deep slate, `#111827` surface, `#2563eb` royal cobalt accent.
  * *Neo-Brutalist:* `#fafafa` canvas, `#000000` hard 2px borders, `#ffdf00` yellow accent, crisp hard shadows (`4px 4px 0px #000`).
* **Tokens:** Define all colors as CSS custom properties (`--bg-canvas`, `--bg-surface`, `--accent-dominant`, `--text-primary`, `--border-subtle`).

### 3. Atmospheric Backgrounds & Tactile Depth
* Never allow screens to float on a flat solid `#ffffff` or flat `#000000`.
* Add subtle ambient lighting with multi-stop radial gradients:
  ```css
  radial-gradient(circle at 50% 0%, rgba(var(--accent-rgb), 0.12) 0%, transparent 65%)
  ```
* Use subtle micro-grids (`28px 28px`), dot matrices, or grain textures masked by radial fades.
* Elevate cards with tactile top rim lighting (`inset 0 1px 0 rgba(255, 255, 255, 0.08)`) and subtle borders rather than heavy blurry drop shadows.

### 4. Orchestrated Staggered Entrance Motion
* One well-orchestrated page reveal creates 10x more delight than scattered hover jumps.
* Animate page elements sequentially using pure CSS keyframes with snappy cubic-bezier easing (`cubic-bezier(0.16, 1, 0.3, 1)`):
  ```css
  .reveal-item { opacity: 0; animation: revealUp 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards; }
  .stagger-1 { animation-delay: 80ms; }
  .stagger-2 { animation-delay: 160ms; }
  .stagger-3 { animation-delay: 240ms; }
  ```
* Provide tactile button compression: `active:scale-[0.98] transition-transform duration-100`.

### 5. Mobile & Responsive Refinements
* **Thumb-Zone Navigation:** Place primary CTAs and filters in the lower third of mobile screens.
* **Bottom Sheets Over Modal Dialogs:** Slide up interactive dialogs from the bottom with drag handles on mobile ($<768\text{px}$).
* **Touch Targets:** Minimum $44 \times 44\text{px}$ tap area for all interactive elements.

---

## 📐 Part 4: Spec-Driven Development (GitHub Spec Kit Protocol)

Once the PR/FAQ, MVP scope, and UI/UX design tokens are locked, author the technical blueprint in `.specs/`:

```text
.specs/
├── spec.md          # Functional specifications, UI aesthetics & acceptance criteria
├── data-model.md    # Schema, database tables, API payloads & state
└── tasks.md         # Step-by-step sequential implementation checklist
```

### 1. `spec.md` (Functional Specifications):
* **UI Design Persona & Design Tokens:**
  * Selected aesthetic archetype, heading font, body font, code font, and primary CSS variables.
* **User Stories & Given-When-Then Acceptance Criteria:**
  ```gherkin
  Scenario: Customer completes instant order
    Given an anonymous user on the landing page
    When they enter valid inputs (date, city, or API key)
    Then a real-time preview renders in < 2 seconds with staggered reveals
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
  - [ ] Task 1: Initialize Next.js project with Tailwind, custom font imports, and CSS theme tokens.
  - [ ] Task 2: Implement core calculation / parsing engine with unit tests.
  - [ ] Task 3: Build distinctive UI layout with atmospheric background and staggered entrance motion.
  - [ ] Task 4: Connect Stripe Checkout webhook for order fulfillment.
  - [ ] Task 5: Implement automated deliverable generator (PDF/Webhook/Email).
  - [ ] Task 6: End-to-end user journey test (from landing page to confirmed order).

---

## 🛡️ AI Coding Guardrails (For Coding Agents)

When an AI coding agent executes `tasks.md`:
1. **Anti-AI-Slop Enforcement:** Strictly apply the distinctive typography, cohesive theme tokens, atmospheric lighting, and staggered entrance rules. Never ship generic Inter/purple-gradient slop.
2. **Single-Task Execution:** Complete one task at a time and verify it with automated tests or terminal checks before proceeding.
3. **No Dependency Sprawl:** Do not install heavy or obscure npm packages when standard native libraries or pure CSS suffice.
4. **Preserve Simplicity:** Resist the urge to add abstractions, microservices, or complex state management until proven necessary.
5. **End-to-End Verification:** Before declaring the MVP complete, run a full simulated purchase using Stripe Test Mode to verify that money is captured and the deliverable is generated.

---

## 📄 Required Output Artifacts

Save in the project repository:
1. `pr-faq.md` (Amazon-style Press Release & Customer FAQ).
2. `.specs/spec.md` (Functional specs, UI design tokens & acceptance criteria).
3. `.specs/data-model.md` (Database schema & API contracts).
4. `.specs/tasks.md` (Sequential build task list).
5. Human Sign-Off Checkpoint before initiating development.
