---
name: assumption-mapping
description: >
  Decomposes a proposed product solution (feature, PRD, GTM idea) into its
  underlying leap-of-faith assumptions before any build or solution-testing
  happens, using Cagan's four risks (value, usability, feasibility, viability)
  and Torres's assumption-mapping method (importance × evidence). Use this
  whenever a solution, feature idea, or PRD is on the table and the user wants
  to validate it, or says "what are we assuming here," "leap of faith," "before
  we build this," "what would have to be true," "how do we de-risk this," or
  wants to test the assumptions instead of testing the solution itself. Reach
  for it early — as soon as an idea is proposed and someone starts reasoning
  about whether it'll work — not only when the word "assumption" appears.
---

# Assumption Mapping

## Core principle

A proposed solution is really a stack of unproven beliefs. Testing the solution as a whole — a prototype, an A/B test, a launch — tests all of those beliefs at once, expensively and late. Testing the assumptions individually, starting with the riskiest and least-evidenced, is cheaper and earlier. This skill exists to force that decomposition *before* any build-or-test conversation.

Never skip straight to "how do we test this feature." Always surface the assumptions first.

**How this differs from `red-team`:** red-team attacks whether an argument holds — it hunts for logic gaps, biases, and failure modes to see if the case survives. Assumption-mapping is constructive: it breaks a solution into discrete testable beliefs and designs the cheapest experiment for each. If the user wants to know "is this idea wrong?" that's red-team. If they want "what would we have to learn before committing?" that's this skill.

## Interaction Model

This runs **draft-then-refine**, not step-by-step interrogation. PMs want a first artifact fast, then tightened — a blank Socratic march through every rating is slow and annoying.

1. **Confirm the belief statement** (Step 1) with the user before building the table — this is the one place a quick check pays off, because everything downstream hangs on it.
2. **Generate the full first-pass table in one go** (Steps 2–3): every assumption, tagged and scored.
3. **Present it with the scores flagged as proposals**, explicitly inviting correction — something like: *"Here's my first cut. The Evidence scores are my best guess from what we've discussed — correct any that are off, and tell me what I missed."* The real evidence score lives in the team's head, not yours.
4. **Revise, then recommend** the 1–3 gating assumptions to test first (Steps 4–5).

Output lives inline by default. If the map is going to drive real test planning, offer to save it to `drafts/assumption-map-[topic]-[date].md`.

## Process

### Step 1 — Restate the idea as a belief statement

Most of the time this skill runs in reverse: someone already has a proposed solution and the job is to walk backward from it to the assumptions it's quietly resting on — not to start from a clean opportunity tree and work forward. Treat that as the default.

Convert the proposed solution into: *"If we build [X], we believe [outcome Y] will happen, because [Z]."*

This forces the hidden causal chain into view. If the person can't fill in Y and Z, that's itself the finding — the idea isn't decomposable yet and needs more discovery before mapping is useful. Say so rather than manufacturing a plausible chain for them.

### Step 2 — Decompose into assumptions, sorted by Cagan's four risks

Pull out every discrete thing that has to be true for the belief statement to hold, and tag each with one of the four risks. Working through all four is the point — most people surface value risk and stop, and the killer assumption is often hiding in viability or feasibility:

- **Value / desirability** — will the customer actually want and use this, and choose it over the alternatives (including doing nothing)?
- **Usability** — can the customer figure out how to use it?
- **Feasibility** — can we actually build it with the time, tech, and skills we have?
- **Viability** — does it work for the business (unit economics, legal, channel, sales, brand, regulatory, cannibalization)?

Push for specificity. "Users want this" is not an assumption — it's a category. "First-time buyers will trust an automated price estimate enough to check out without contacting sales" is an assumption. The test of a good assumption is that you can imagine data that would prove it false.

### Step 3 — Map by importance × evidence (Torres's assumption map)

For each assumption, rate 1–5 on two axes:

- **Importance**: how much does the idea's success depend on this being true? (5 = if this is false, the whole idea collapses.)
- **Evidence**: how much do we already know — from data, past research, or direct experience — that it's true? (5 = well-established; 1 = pure hope.)

Score Evidence from what the user has told you and the conversation context. Don't invent evidence the user hasn't mentioned — if you don't know, that's a low score, and the test in Step 4 is what resolves it. (If the user wants a score checked against real signal — analytics data, past user research, a research brief — you can go pull it, but don't make that a reflexive step; the map is a thinking tool first.)

Place each assumption conceptually on the 2×2:

- **High importance / low evidence = leap-of-faith assumptions.** These are the whole game — test them first, before building anything.
- **High importance / high evidence** — already de-risked; don't burn test cycles re-proving them.
- **Low importance / either** — deprioritize regardless of evidence.

### Step 4 — Design the smallest test for each leap-of-faith assumption

For each top-right assumption, propose the cheapest method that could resolve it *either way*. Favor, in rough order of speed and cost:

1. **Existing data pull** — do we already have signal in analytics, support tickets, or past research? (Cheapest possible; often the answer is already sitting there.)
2. **Concierge / fake-door / landing-page test** — manufacture the demand signal without building the thing.
3. **Customer interview** (moderated or unmoderated) probing the specific belief.
4. **Prototype test** — only when the cheaper methods can't isolate the assumption.

Name both a **confirm signal** and a **kill signal**: what result would validate the belief, and what result would falsify it. Design the test to surface either — an experiment that can only confirm isn't a test, it's theater. Treat confirmation and disconfirmation as equally valid outcomes.

### Step 5 — Output

Produce a table:

| Assumption | Type | Importance (1–5) | Evidence (1–5) | Leap of faith? | Smallest test | Confirm signal | Kill signal |
| --- | --- | --- | --- | --- | --- | --- | --- |

Follow it with a short recommendation: which **1–3 assumptions to test first**, and why *those* are the gating ones — not the whole list. The recommendation is the deliverable; the table is the reasoning behind it.

## Guardrails

- **Don't let the conversation jump to "how would we build/ship this" until the assumption table exists.** That's the entire discipline the skill enforces.
- **Reframe certainties as testable beliefs.** An assumption phrased as fact ("users need X") hides the risk. Rewrite it as "we believe users will do X when Y," so it can be proven false.
- **Work all four risk categories explicitly**, rather than stopping once a few obvious value-risk assumptions surface. The goal is to leave no assumption unturned — but only surface the ones that actually *gate* the idea.
- **Aim for the vital few.** A 15-row table where 12 rows are low-importance busywork defeats the purpose. Keep it to the assumptions that would actually change the decision.
- **Value-risk-only is a legitimate scope** early in discovery. If that's all the user wants, say so explicitly rather than silently dropping the other three categories.
