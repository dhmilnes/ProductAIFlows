---
name: pm-style
description: Style guide for product management writing - PRDs, strategy docs, test plans, roadmap entries, and product briefs. Use when drafting or reviewing any PM document meant for execs, stakeholders, or cross-functional partners.
---

# Product Management Writing Style Guide

PM writing has three jobs: enable decisions, present evidence, be scannable.

This guide covers principles, structure, and standards for PRDs and strategy docs. Use it for PRDs, strategy docs, roadmap entries, test plans, and product briefs.

**Not covered:** Technical specs, API docs, engineering design docs.

---

## Core Principles

### 1. Decision-Enabling, Not Comprehensive
**What it means:** PM documents are **arguments for bets**, not comprehensive specs or requirements docs. Every sentence should help your audience (exec, stakeholder, team) make a decision.

### 2. Evidence-Driven Claims
**What it means:** Every assertion must be backed by data, research, or documented precedent.

### 3. Clear Over Clever
**What it means:** PM writing is read by busy people (execs, cross-functional partners, leadership). Optimize for scanning speed and comprehension.

**Apply it:**
- Use active voice: "This test increases LTV" not "LTV is increased by this test"
- Write at a lower reading level without sacrificing clarity or precision.
- Front-load key information: Lead with the insight, then support it
- Avoid jargon unless it's standard company vocabulary (KPI, LTV, NPS are fine; obscure acronyms are not)
- Write for your actual audience: execs scanning 10+ docs, engineers implementing, stakeholders evaluating tradeoffs

### 4. Framed for the end reader
**What it means:** PM writing is not a discussion thread. It should be addressed to the end reader, not the author or co-authors. Avoid shorthand references to other documents or writing as if it's updating a document from discussion.

---

## Register: Match the Gold Passages

Before drafting anything longer than a paragraph, read `personal/gold-passages.md` if it exists - verbatim excerpts from the author's approved PRDs and strategy docs. Match that register: complete plain sentences, every number with its comparison attached, claims stated once and directly, stakes made specific instead of dramatic. Shown examples beat described rules; when a draft drifts, re-read the passages rather than the rule list.

---

## Document Flow

**Flow rules:**
1. **Inverted pyramid** - Summary/Hypothesis state the claim, later sections support it
2. **Front-load conclusions** - Lead with the insight, evidence follows
3. **Progressive detail** - Summary (high-level) → Hypothesis (theory) → Justification (details)
4. **Each section builds** - Later sections deepen understanding of opening claim
5. **Avoid redundancy** - Don't repeat the same point verbatim across sections

**Example:**
> **✅ Good flow:**
> The checkout test increased registrations by 0.2% (13,022 vs 12,992). While not statistically significant (95% CI: -1.8% to +2.3%), the directionality supports our hypothesis. This warrants a follow-up test with higher power.

## Writing Quality Standards

### Clarity: Pass the Skim Test
A busy reader skimming your doc should grasp key points.

- **Concrete numbers:** "12% increase" not "significant improvement"
- **Define acronyms once:** "DAU (Daily Active Users)"
- **Lead with conclusions:** "Test failed" before explaining why
- **Break up text:** Bullets, tables, toggles
- **Avoid jargon:** "We need to pivot" → "We should change our approach"
- **Don't protest too much or restate:** Don't restate the point in a different way. "We should do this thing" stands on its own. "We should do this thing, not that thing" is excess. It's OK to explain why not the other thing, but as a writing device you don't need to add the "not that thing" to the original point.

---

### Concision: Cut Ruthlessly
If it doesn't support the decision, it's noise.

**Kill these phrases:**
- ❌ "It's worth noting that..."
- ❌ "We believe that it's important to..."
- ❌ "Based on our analysis, we have determined that..."
- ❌ Meaningless magnitude: "critical," "huge," "enormous," "massive"
- ❌ Bureaucratic verbosity: "utilize" → use, "leverage" → use, "facilitate" → help, "in order to" → to, "the fact that" → that. And "there is/are + noun" → let the noun do the verb ("There are three tests that failed" → "Three tests failed")
- ❌ Em dashes (—) - use hyphens (-), a comma, or rewrite. This is a full ban, deliberately stricter than external style guides that only caution against overuse: a density rule isn't checkable by an editing pass, and em-dash overuse is the most reliable tell of machine-drafted prose. Don't relax it by citing a guide written for human writers.
- ❌ Contrast frames: "It's not X, it's Y" / "This isn't about X" - state the point directly. (A real distinction that carries information is fine: "directional targets, not A/B thresholds.")
- ❌ Dramatic pivots: "This is the moment...", "the one thing that matters", "changes everything"
- ❌ Rule-of-three flourishes: three parallel phrases for rhythm where one precise one would do

**Say it directly:**
- ✅ "Test results show..."
- ✅ "This matters because..."
- ✅ "Data indicates..."

---

### Tone: Professional, Not Formal
Brief a smart colleague, not a legal document.

**Active voice:**
- ✅ "This test increases LTV by $5"
- ❌ "LTV is increased by $5 through this test"

**Be direct:**
- ✅ "We should launch this"
- ❌ "We might want to consider possibly launching this"

**Hedge only when genuinely uncertain:**
- ✅ "Results suggest 2-5% lift, though sample size limits precision"
- ❌ "We think this could potentially maybe improve things somewhat"

---

### Formatting: Aid Scanning

**Use:**
- **Bullets** for lists (not paragraphs)
- **Tables** for comparisons (requirements, variants, features)
- **Toggles** for supporting detail
- **Bold** for key metrics, decisions, actions only

**Avoid:**
- ❌ Paragraph-only sections
- ❌ Walls of bullets
- ❌ Over-formatting every other word

---

## Common Pitfalls

| Pitfall | Looks Like | Fix |
|---------|------------|-----|
| **Solution in search of problem** | "Add AI recommendations because AI is strategic" | Lead with problem, then propose solution |
| **Sandbagging metrics** | "This will improve engagement, or we'll learn something" | Define success/failure thresholds before launch |
| **Death by edge cases** | "What if user has 3 accounts, 2 expired, mobile web, incognito, leap year?" | Focus on 80% case. Document edge cases, don't design for them |
| **Burying the lede** | Three paragraphs of context before the recommendation | Conclusion first, evidence after |
| **False precision** | "Increase LTV by $4.73" | Round appropriately, include CIs: "$4-5 increase (95% CI: $2-8)" |
| **Scope creep** | Summary says "test checkout," Requirements says "rebuild payments" | Keep Summary ↔ Requirements aligned |

---

## Evidence Standards

| Evidence Type | Include | Example |
|---------------|---------|---------|
| **Quantitative (A/B tests)** | Control vs treatment, CI, p-value, sample size | "Checkout test: 13,022 vs 12,992 registrations (0.2% lift, 95% CI: -1.8% to +2.3%, p=0.81, n=27.4M)" |
| **Qualitative (User research)** | Methodology, sample, key findings, link | "12 churned users interviewed. 9/12 cited 'not enough time to see value.' [Full doc](link)" |
| **Precedent (Internal)** | Past test name, result, link | "Onboarding email test: 22% email capture lift (CI: -2% to +1%). [Results](link)" |
| **Precedent (External)** | Company, year, result, link | "Duolingo 2019: 18% conversion lift from 7-day trial. [Case study](link)" |

**Never:**
- ❌ Cherry-pick subgroups without pre-registration
- ❌ Claim significance when CI includes zero
- ❌ Cite "user feedback" without methodology
- ❌ Assume external precedent guarantees your success
- ❌ Generalize about a group of people ("enterprise buyers want...", "admins care about...", "new users expect...") without the same citation any other claim needs. These read as background rather than as assertions, which is exactly why they travel uncorrected

### Interpreting Observational Data

**Correlation ≠ Causation.** When presenting observational data (not randomized tests), state what the data CAN and CANNOT conclude.

- ✅ "Users who paused have +22 higher NPS at cancel. This could reflect selection effect, goal completion, or goodwill from the option itself. An A/B test would isolate causation."

### Cite Sources Inline

Link evidence in the same sentence you reference it.

- ✅ "The pricing-page test showed +23.8% revenue lift ([Results](link))."

**For BI research:** Include SQL queries in an Appendix so others can verify.

---

## Final Pass: Prose Editor (Required)

ALWAYS finish a deliverable longer than ~half a page by spawning the `prose-editor` agent (`.claude/agents/prose-editor.md`) on the draft file before it ships or gets written to Notion. Give it the draft path and audience; it applies the de-slop checklist (contrast frames, hedging filler, premature closure, fragments) directly to the file and returns a change summary. A `/simplify-doc` run on the same draft already includes this pass - don't run both.

---

## Notion Formatting

See `docs/notion-formatting-guide.md` for full syntax reference. Key gotcha: tables use XML, not Markdown pipes.

---

## When to Deviate

These are guidelines, not laws. Deviate when it serves clarity or the specific document's needs.

**Valid reasons to break rules:**
- The user explicitly requested a different structure
- Domain-specific conventions (e.g., a PRD for a regulated product includes a compliance section)
- Unique circumstances require additional context

---

## Glossary

- **KPI:** Key Performance Indicator
- **LTV:** Lifetime Value (revenue per user over their lifetime)
- **NPS:** Net Promoter Score (user satisfaction metric)
- **DAU/MAU:** Daily/Monthly Active Users
- **CI:** Confidence Interval (range of plausible values for a metric)
- **Insurance test:** Protects against revenue loss rather than seeking gain

Company-specific terms (product lines, internal tools, goal frameworks) belong in `personal/aboutme.md`, not here.

---

## Further Resources

- **Notion Formatting Guide:** `docs/notion-formatting-guide.md`
