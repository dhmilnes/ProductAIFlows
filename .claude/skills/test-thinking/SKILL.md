---
name: test-thinking
description: Lightweight reference for designing meaningful test variations.
---

# A/B Test Mindset

Build strong variations that create signal. We don't need to isolate a single variable — we need distinct experiences that break through the noise.

---

## Variation Design Framework

### Step 1: Understand Context & Mechanisms

**Who is the primary persona?** Name them. What's their intent, mindset, and journey stage? What do they care about vs. ignore? Different personas respond to different levers.

**What mechanisms are available?** Usability fixes, layout changes, copy rewrites, flow restructuring, social proof, urgency — what can we actually change?

**What psychological lever are we pulling?** Name the principle (see reference below). If you can't name one, you're guessing.

### Step 2: Design Distinct Variants

**Bad:** Control vs slightly different version
**Good:** Control vs fundamentally different approaches to the same goal

### Step 3: Validate Each Variant

For each variant, answer:
1. What evidence supports this approach?
2. Why might this win?
3. Why might this lose?

If you can't answer #1, it's not a real test — it's a guess. If it "can't lose," you're not testing anything.

### Step 4: Prioritize (PXL Binary Scoring)

When multiple ideas compete for roadmap space, score each with yes/no questions — no subjective ratings.

| Question |
|----------|
| Is the change above the fold? |
| Is it noticeable within 5 seconds? |
| Does it target the primary persona's core motivation? |
| Is there existing evidence (data, research, usability) supporting it? |
| Does it address a known friction point or drop-off? |
| Can we measure the impact with current instrumentation? |

Each "yes" = 1 point. Rank by total. Tiebreaker: evidence > persona relevance > visibility.

```
| Idea | Above fold? | 5s notice? | Persona fit? | Evidence? | Known friction? | Measurable? | Score |
|------|:-----------:|:----------:|:------------:|:---------:|:---------------:|:-----------:|:-----:|
| A    | Y           | Y          | Y            | N         | Y               | Y           | 5     |
| B    | Y           | N          | Y            | Y         | N               | Y           | 4     |
```

If the top idea scores ≤ 2, reconsider whether you have a testable hypothesis.

---

## Behavioral Science Quick Reference

| Principle | Definition | Example |
|-----------|------------|---------|
| **Goal Gradient** | Effort increases as goal approaches | Progress bar, "You're 80% there!" |
| **Endowed Progress** | People value progress they "received" | Start bar at 20%, show completed steps |
| **Sunk Cost** | Past investment influences future decisions | "You've already completed 2 steps" |
| **Fresh Start Effect** | New beginnings motivate change | "Start your year strong" |
| **Loss Aversion** | Losses feel ~2x stronger than gains | "Don't lose your saved items" |
| **Anchoring** | First number influences perception | Show competitor price first |
| **Framing Effect** | Same info, different presentation | "$3/day" vs "$90/month" |
| **Social Proof** | People follow what others do | "12,847 users joined this month" |
| **Authority** | People trust credible experts | Certifications, expert endorsements |
| **Default Effect** | People stick with pre-selected options | Pre-select annual plan |
| **Choice Overload** | Too many options = paralysis | Show 3 plans, not 7 |
| **Friction/Sludge** | Small barriers dramatically reduce completion | One-click vs multi-step |
| **Ambiguity Aversion** | People avoid unknown probabilities | Clear "What happens next" steps |
| **Zero Risk Bias** | Preference for eliminating risk entirely | "30-day money-back guarantee" |

---

## Output Format

```
| Variant | What User Sees | Persona Impact | Principle | Why It Might Win | Why It Might Lose |
|---------|----------------|----------------|-----------|------------------|-------------------|
| Control | [Current state] | [How persona experiences this] | Baseline | - | - |
| B | [Description] | [How persona experiences this] | [Named principle] | [Evidence/logic] | [Risk] |
| C | [Description] | [How persona experiences this] | [Named principle] | [Evidence/logic] | [Risk] |
```

Then ask:
- "Does this capture meaningful variation? Any variants to add or modify?"
- "Do we have enough sample to test this many variants in a reasonable timeframe?"
