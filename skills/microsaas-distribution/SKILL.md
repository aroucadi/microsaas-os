---
name: microsaas-distribution
description: >-
  Go-to-market launch, viral short-form content creation, programmatic SEO, and monetization for micro-SaaS.
  Use when planning product launches, writing TikTok/Reels/Shorts video scripts, designing viral hooks,
  setting up programmatic SEO architectures, structuring pricing, or converting visitors into paying customers.
---

# Micro-SaaS Launch, Viral Content & Monetization (`microsaas-distribution`)

Use this skill to systematically drive targeted traffic, build viral distribution loops, and convert attention into predictable revenue without burning cash on expensive paid advertising.

---

## 🚀 Part 1: The Multi-Channel Launch Playbook

Select the primary launch channel based on your product archetype:

```text
┌─────────────────────────────────┬─────────────────────────────────┐
│ B2B DEVELOPER / CREATOR TOOLS   │ B2C KEEPSAKES / CONSUMER TOOLS  │
├─────────────────────────────────┼─────────────────────────────────┤
│ • Product Hunt (Tuesday/Thursday│ • TikTok & Instagram Reels      │
│   launch, badge, maker comment) │   (Organic short-form video)    │
│ • Hacker News ("Show HN: ...")  │ • Reddit Niche Communities      │
│ • Technical Twitter/X threads   │   (Value-first story post)      │
│ • Relevant subreddits (r/webdev,│ • Pinterest (High-intent gift   │
│   r/SaaS, r/selfhosted)         │   searches for anniversaries)   │
└─────────────────────────────────┴─────────────────────────────────┘
```

### The 4-Day Launch Sequence:
* **Day -2 (Asset Prep):** Record 30-second crisp demo video, take clean UI screenshots, draft the founding story post.
* **Day 0 (Launch Day):**
  * Publish on primary platform at 00:01 PST (for Product Hunt) or 08:00 EST (for Reddit/HN).
  * Post founding story on X/LinkedIn with a transparent "why I built this" hook.
* **Day +1 (Community Engagement):** Respond to every comment within 15 minutes. Offer instant troubleshooting.
* **Day +3 (Milestone & Learnings):** Share transparent day-1 revenue/traffic stats.

---

## 📱 Part 2: Viral Short-Form Video Engine (TikTok, Reels, Shorts)

Short-form video is the #1 distribution cheat code for visual and emotional micro-SaaS products.

### The "Hook-Retain-Reward" Script Formula:
Every high-converting video follows this 3-part structure (15 to 30 seconds total):

```text
[0:00 - 0:03] THE HOOK      ➔ Disrupt the scroll with visceral curiosity or controversy.
[0:04 - 0:18] THE RETENTION ➔ Show the screen/visual in action; build emotional tension.
[0:19 - 0:25] THE REWARD    ➔ The stunning finished artifact + direct call to action.
```

### 5 Proven Hook Archetypes for Micro-SaaS:
1. **The Relational / Call-Out Hook:** *"If you were born in the 90s, your birthday certificate is lying to you..."* / *"Send this to someone whose birthday is next month."*
2. **The Discovery / Secret Hook:** *"I built an app that shows what the moon looked like the exact night you met your partner."*
3. **The Nostalgia Shock Hook:** *"Look at what a gallon of milk and a movie ticket cost on the day you were born..."*
4. **The "Before & After" Frustration Hook:** *"Stop spending 3 hours doing [painful task] in Excel. Here is how I do it in 20 seconds."*
5. **The Secret Tool Hook:** *"Websites you didn’t know existed that feel illegal to know..."*

### Faceless Production Workflow (Zero On-Camera Presence):
1. **Visuals:** Clean desktop or mobile screen recording of the app generating the personalized output.
2. **Audio:** Trending background instrumental sound (trending TikTok audio) + ElevenLabs AI voiceover (or clean text-on-screen).
3. **Editing:** Use CapCut to add auto-captions with bold yellow/white highlighting and rapid cuts every 2–3 seconds.
4. **Cross-Posting Loop:** Post the clean (watermark-free) video to **TikTok**, then repurpose directly to **Instagram Reels**, **YouTube Shorts**, and **Pinterest Video Pins**.

---

## 🔍 Part 3: Programmatic SEO (pSEO) Architecture

For long-term passive traffic, generate thousands of long-tail landing pages targeting high-intent search queries:

### The Programmatic Matrix:
* **Keepsake / Time-Capsule Matrix:** `/{event}/{year}/{month}/{day}`
  * e.g. `domain.com/born/1995-october-24` $\rightarrow$ Target keyword: *"What happened on October 24, 1995"*, *"Moon phase October 24 1995"*.
  * Total pages generated: **36,525 static pages** (100 years of daily history).
* **Sports / Stadium Matrix:** `/{club}/stadium/{section}` or `/{race}/{circuit}/{year}`
  * e.g. `domain.com/f1/monaco/telemetry-2021`.

### Technical Rules for pSEO:
* Must have unique, dynamically fetched data on each page (e.g. real historical weather, moon illumination, top song) to avoid Google duplicate content penalties.
* Fast static generation (Next.js `generateStaticParams` / ISR).

---

## 💳 Part 4: Frictionless Monetization Architecture

A micro-SaaS must optimize for **zero-sales-call impulse checkout**:

```text
┌────────────────────────────────────────────────────────┐
│              THE 3 MICRO-SAAS PRICING TIERS            │
├────────────────────────┬───────────────────────────────┤
│ 1. The Impulse Unlock  │ $4.99 to $9.99 one-time.      │
│    (Digital Only)      │ Instant high-res PDF export   │
│                        │ or one-off report.            │
├────────────────────────┼───────────────────────────────┤
│ 2. The Physical Upsell │ $39.00 to $69.00 framed print.│
│    (Print-on-Demand)   │ Automated Gelato/Printful API.│
│                        │ High AOV, $20–$35 net margin. │
├────────────────────────┼───────────────────────────────┤
│ 3. The Micro-Sub       │ $9 to $29 / month.            │
│    (Utility / Sentinel)│ Recurring monitoring, ongoing │
│                        │ backups, or continuous alerts.│
└────────────────────────┴───────────────────────────────┘
```

### Checkout Optimization Checklist:
- [ ] Stripe Hosted Checkout enabled (Apple Pay, Google Pay, 1-click buy).
- [ ] Order bump / 1-click upsell offered before checkout confirmation:
  * e.g. *"Add a matching gift card for +$3.99"* or *"Unlock priority 24h printing for +$4.99"*.
- [ ] Zero mandatory account registration before payment (guest checkout via email).
- [ ] Automated receipt with download link and tracking number dispatched instantly.

---

## 📄 Required Output Artifacts

Save in the project repository:
1. `launch-plan.md` (Target platforms, post copy, founder story, asset links).
2. `content-calendar.md` (5 short-form video hooks, scripts, and audio directions).
3. `pricing-model.md` (Tiers, margins, Gelato/Printful cost breakdowns, Stripe config).
4. Human Sign-Off Checkpoint before publishing external posts or going live.
