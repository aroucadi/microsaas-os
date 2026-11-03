---
name: microsaas-product
description: >-
  Product strategy, PR/FAQ, MVP definition, Spec-Driven Development (SDD), and UI/UX design architecture
  for micro-SaaS. Combines YC principles (Narrow ICP, Do Things That Don't Scale), Amazon Working Backwards,
  Shape Up Appetite, Walking Skeletons, and anti-AI-slop frontend aesthetics to define airtight specifications.
---

# Micro-SaaS Product Strategy, UI/UX Architecture & Spec-Driven Development (`microsaas-product`)

Use this skill to define the product from the customer's desired outcome backwards, eliminate feature bloat, craft distinctive **anti-AI-slop** interfaces, and produce actionable **Spec-Driven Development (SDD)** artifacts for AI coding agents.

> **Core Philosophy:** Evidence before specifications. Specifications before code. Working customer value before feature expansion.

---

## 🧭 Part 1: Product Definition (YC & Amazon Working Backwards)

Define the product with razor-sharp clarity before opening an editor or configuring databases.

### 1. The One-Sentence Product Pitch
Every micro-SaaS must be expressible in one unambiguous sentence:
> **"For [specific customer] who struggles with [specific problem], our product delivers [measurable outcome] without [existing frustration]."**

### 2. YC Core Principles:
* **Narrow Initial Customer Profile (ICP):** Target an extremely specific first customer segment (e.g., *"Shopify clothing brands doing $20k-$100k/mo"*, not *"E-commerce businesses"*).
* **Make Something People Want:** Focus on one painful problem and one measurable outcome.
* **Do Things That Don't Scale (Paul Graham):** Initially, manually onboard users, handle exceptions yourself, and deliver results by hand before writing automated background workers.

### 3. Lightweight PR/FAQ (Amazon Working Backwards):
Author a 1-page artifact capturing the customer perspective:
1. **Headline & Subhead:** Product name and primary benefit in plain English.
2. **Summary:** Who it is for and why it was created.
3. **The Problem:** The acute frustration customers faced before this existed.
4. **The Solution (The 3-Step Journey):** How the customer gets the result in 3 intuitive steps.
5. **Customer Quote:** A realistic testimonial highlighting time, stress, or money saved.
6. **5 Critical FAQs:** Direct answers to pricing, data privacy, integrations, refunds, and technical requirements.

---

## 🎯 Part 2: MVP Scoping — Core Workflow & Shape Up Appetite

> **An MVP is the smallest product that delivers a complete customer outcome, not the smallest collection of features.**

### 1. The Core Value-Delivery Workflow:
Define the single unbroken path from user trigger to delivered outcome:
```text
[User Trigger / Input] ──▶ [Core Engine Processing] ──▶ [Immediate Value Delivered]
```
If a proposed capability does not sit directly on this path, it is discarded for V1.

### 2. Shape Up Development Appetite:
Before coding, set a strict development time budget (e.g., **1 to 2 weeks maximum solo build**). Scope is tailored to fit the appetite—the appetite is never extended to fit the scope.

### 3. Scoping Boundaries:
* **MUST HAVE (Strictly $\le 3$ core capabilities):** The absolute minimum needed to deliver the complete core workflow and capture payment.
* **WON'T HAVE IN V1 (Explicitly Banned Scope):**
  * ❌ No multi-user teams, workspaces, or custom role-based access.
  * ❌ No custom dark mode toggle or theme pickers.
  * ❌ No AI chatbot if static inputs or structured forms suffice.
  * ❌ No custom authentication if magic links or Google OAuth suffice.
  * ❌ No complex analytics dashboards when a simple email summary delivers value.

---

## 🎨 Part 3: UI/UX Architecture & Anti-AI-Slop Aesthetics

> **Design Principle:** Don't Make Me Think (Steve Krug). A fast, obvious, clear interface is always more valuable than superficial visual complexity.

### 1. Usability First:
* **Jobs-to-be-Done (JTBD):** Design every screen around what the user is trying to accomplish, not what backend features you want to expose.
* **One Primary CTA:** Every important screen must have one obvious next action. Avoid competing buttons of equal visual weight.
* **Progressive Disclosure:** Show only the essentials needed for the current step. Hide advanced configuration in collapsible sections or post-onboarding settings.

### 2. Anti-AI-Slop Frontend Aesthetics (Web & Mobile):
AI coding assistants naturally converge to generic, lifeless outputs (Inter font, purple-on-white gradients, cookie-cutter 3-card grids). Enforce these aesthetic directives:

* **Distinctive Typography Pairings (Banish Generic Fonts):**
  * *Banned:* `Inter`, `Roboto`, `Arial`, system fonts. Do not default to `Space Grotesk`.
  * *DevTools & Technical:* `Syne` or `Cabinet Grotesk` (Headings) + `Plus Jakarta Sans` (Body) + `JetBrains Mono` (Code).
  * *Warm Editorial & Keepsakes:* `Instrument Serif` (Headings) + `Satoshi` or `Newsreader` (Body) + `DM Mono`.
  * *Fintech & Security:* `Clash Display` or `Archivo` (Headings) + `Switzer` or `General Sans` (Body).
* **Cohesive Theme Tokens:** Commit to a specific palette (*Obsidian & Phosphor*, *Warm Atelier*, *Midnight Cobalt*, or *Neo-Brutalist*).
* **Atmospheric Depth:** Layer subtle ambient lighting (`radial-gradient`), 28px masked micro-grids, or warm paper texture with subtle 1px rim lighting (`inset 0 1px 0 rgba(255, 255, 255, 0.08)`).
* **Orchestrated Motion:** Pure CSS staggered reveals on page load (`revealUp` with `80ms` delays and snappy `cubic-bezier(0.16, 1, 0.3, 1)` easing).
* **Mobile Ergonomics:** Pinned lower-third CTA in the thumb zone, sliding bottom sheets instead of centered modals, and minimum $44 \times 44\text{px}$ touch targets.

*Reference Guide:* See [`references/frontend_aesthetics_anti_slop.md`](references/frontend_aesthetics_anti_slop.md).

---

## 📐 Part 4: Spec-Driven Architecture (GitHub Spec Kit Protocol)

Living, version-controlled specifications in `.specs/`:

```text
.specs/
├── spec.md          # Functional specifications, UI design tokens & acceptance criteria
├── data-model.md    # Database schema, API contracts & payloads
└── tasks.md         # Sequential vertical-slice task checklist
```

### 1. `spec.md` (Functional Specs & Acceptance Criteria):
* Narrow ICP, one-sentence product pitch, and measurable customer outcome.
* UI design persona and design tokens.
* User stories with concrete Given-When-Then acceptance criteria and edge case handling.

### 2. `data-model.md` (Architecture & Data Contracts):
* Minimal stack: Next.js App Router, Tailwind CSS, Supabase/SQLite, Stripe Checkout.
* Database schemas, relationships, indexes, and external webhook structures.

### 3. `tasks.md` (Vertical Slicing & The Walking Skeleton):
* **Milestone 1 — The Walking Skeleton:** Build the smallest end-to-end working path (Database $\rightarrow$ Backend/API $\rightarrow$ Frontend UI) connecting user input to delivered outcome before refining details.
* **Vertical Slicing:** Each subsequent task delivers a working vertical slice of functionality rather than horizontal architectural layers.
* **Verifiable Outcomes:** Each task has a clear verifiable outcome with appropriate tests (unit test for logic, integration check for core flows).

---

## 🛡️ AI Coding Guardrails

When an AI coding agent executes `tasks.md`:
1. **Build the Walking Skeleton First:** Prove the end-to-end flow connects before spending time on secondary views.
2. **Execute One Vertical Slice at a Time:** Verify each task with tests or terminal checks before proceeding.
3. **No Dependency Sprawl:** Do not install heavy npm packages when native platform capabilities suffice.
4. **Anti-AI-Slop Enforcement:** Apply the distinctive typography, cohesive theme tokens, and staggered entrance rules.
5. **Simulated Transaction Test:** Perform a complete test-mode purchase and delivery before declaring the MVP complete.

---

## 📄 Required Output Artifacts

Save in the project repository:
1. `pr-faq.md` (1-page PR, 3-step journey, 5 FAQs, 1-sentence pitch, narrow ICP).
2. `.specs/spec.md` (Functional specs, UI design tokens, acceptance criteria).
3. `.specs/data-model.md` (Database schema & API contracts).
4. `.specs/tasks.md` (Walking skeleton & vertical-slice build list).
5. Pre-Mortem & Founder Sign-Off Checkpoint before initiating development.
