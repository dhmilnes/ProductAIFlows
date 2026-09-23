# Cohesion lens

**The question:** Does the document hold together from section to section, and can a reader who was not in the room take every phrase forward?

## Why this lens exists

Documents in this repo are read twice. A person reads them once. Then models read them many times: memory files distill them, skills and later documents pull premises from them. A phrase the author coined for emphasis in one paragraph becomes a premise in the next reader's reasoning, and a shorthand reference the author could resolve from memory becomes an unresolvable pointer for everyone else. This lens protects the second reading.

Read the register file named in your prompt first, if one exists. Then read the whole document twice: once for the three checks below, once to run the sweep.

## Check 1 - Section-to-section logic

Read only the first sentence of every section, in order. It should tell a continuous story on its own. Where it does not, the break is usually one of these:

- **A claim changes shape between sections.** A target stated as a range in the summary and a point in the body. A population defined as "enterprise customers" in one section and "all customers" two sections later with no signal that the scope widened. A term that means one thing on page one and a wider thing on page three.
- **The summary says more than the body supports.** The body has three findings and the summary names four, or leads with a different one. The conclusion introduces a recommendation no section argued for.
- **A section opens on a premise no earlier section established.** "Given the annual-first default..." when the default was never described.
- **Recurring figures disagree.** The same metric appears as 14.7% in one place and 15% in another. Flag the mismatch as **judgment** and name both locations. Never decide which is right; that is a fact-check, not an edit.

Fixes that only reconcile wording (the same claim, said consistently) are mechanical. Fixes that require knowing which version the author meant are judgment.

## Check 2 - Shorthand a reader cannot take forward

The test: could a new teammate, or a model reading only this document, resolve the reference to one specific thing and act on it? If they would have to ask, expand it once with a name, a date, a link, or a one-clause description.

What to look for:

- **References that assume the reader was there.** "The Jordan conversation." "The earlier doc." "Per the April session." "The Q3 plan." A test or initiative nickname with no expansion. "The pilot" when three pilots exist in the same quarter.
- **Demonstratives whose antecedent is a section away.** A section that opens with "This means...", "That approach...", "The change..." when the referent last appeared two headings ago.
- **Implied comparisons.** "Lower than expected" with no statement of what was expected. "The other segment" when four have been named.

Mechanical when the referent is named elsewhere in the document (bring the name to the reference). Judgment when it is not; propose the expansion you think the author meant and let them confirm.

Word-level vocabulary jargon (schema names, undefined acronyms, internal codenames used as common nouns) belongs to the Prose lens. You take references to things, events, and documents.

## Check 3 - Coined phrases that harden into rules

This is the check the other lenses cannot make.

**The pattern.** The author compresses a generalization into a memorable phrase for impact: "X is the gate." "Y is the binding constraint." "The only lever is Z." "Everything routes through W." "If it isn't A, it doesn't count." Stated once, in context, it reads as emphasis. A later reader, and especially a model reading the document as source material, takes it literally: a hard rule, an invariant, a filter that excludes cases the author never considered. The author decided on a description of behavior. The downstream reader inherits a constraint.

**How to spot it:**

- A definite noun phrase with "is the" and a singular role word: gate, lever, constraint, bottleneck, bar, test, line, rule, filter, driver, engine.
- Absolutes not attached to a number or a source: only, always, never, every, all, nothing, no one.
- A memorable phrase that appears once as rhetoric and again later as if it were an established fact ("since X is the gate, ...").
- A metaphor doing the work of a claim, with no literal statement of the claim nearby.
- A sentence you can imagine being copied verbatim into a CLAUDE.md rule, a memory file, or a skill.

**The test.** Ask two questions. What is the actual scope and condition? And would the author be comfortable if a skill or memory file quoted this sentence as a rule? If the honest version has a scope ("in H1", "for enterprise customers", "in the cases we looked at") or a mechanism the phrase is hiding, the compression is costing the reader.

**The fix.** Restate the claim with its scope and its evidence class attached. If the scope and evidence are stated elsewhere in the document, the fix is mechanical: bring them to the sentence. If they are stated nowhere, the finding is judgment: propose the scoped version you infer and ask the author what they meant. If the author intended a rule, make that explicit and name its source: "Rule, agreed with the VP of Product on 2026-08-12: ...". A rule with a source is fine. A rule that arrived by rhetoric is the defect.

**What not to flag.** A vivid sentence whose scope is obvious from the same paragraph. A rule that names its source. A claim with its number attached ("Annual plans are 71% of new signups" is not a coined phrase, it is a figure). Do not strip every strong sentence; the cost you are protecting against is specific.

### Examples

| Before | Why it hardens | After |
|--------|----------------|-------|
| "Onboarding completion is the gate to retention." | Read later as: nothing else affects retention; filter analyses to completers. | "In the 2025 cohorts, customers who finished onboarding had 2.1x the 12-month retention of those who did not, so onboarding is where we look first." |
| "The Basic plan is the growth engine." | Read later as: invest only in Basic; Premium growth is out of scope. | "The Basic plan drove 84% of net customer growth in H1 2026. Premium was flat." |
| "If it doesn't move the North Star, it doesn't count." | Read later as: a scoring rule for every initiative, including ones with no North Star mapping yet. | "The 2026 priorities are ranked by expected North Star impact." (If it is a rule: "Rule, set at the 2026 planning offsite: initiatives without a North Star line are not staffed.") |
| "The cart was the problem." | Read later as: the new default plan was fine; never revisit it. | "The checkout test lost on the cart step itself; the new default plan was not tested in isolation." |

## Sweep

Run these before the close read. They produce candidates, not verdicts; look at every hit.

```
Coined role phrases:      (?i)\bis the (gate|lever|constraint|bottleneck|bar|test|line|rule|filter|driver|engine|key|answer|problem)\b
Absolutes without anchor: (?i)\b(only|always|never|every|all|nothing|no one|everything|entirely)\b
Was-there references:     (?i)\bthe (earlier|previous|prior|last|other) (doc|document|conversation|meeting|session|thread|call|version)\b|\bper (the|our) \w+ (session|conversation|meeting|thread)\b
Section-opening pointers: ^#{1,6}[^\n]*\n+\s*(This|That|These|Those|It) \b
Nickname candidates:      \bthe [A-Z][a-z]+ (test|pilot|plan|deck|doc|proposal)\b
```

Report the count per pattern in your `## Counts` block. For the coined-phrase and absolutes patterns, also list every hit you dismissed with a three-to-six-word reason ("L61: absolute has its number"). A dismissed hit that is not listed is indistinguishable from a hit you never looked at, and silent dismissals are exactly how unscoped rules reach the author unflagged. The list is what lets the editor and the author see where the bar was set.

Verdict phrasings count as coined phrases even without a role noun. "X cannot explain it." "It is not a Y effect." "Raw comparisons are meaningless." "Nothing else." Each closes a question with no scope attached, and each will be quoted as settled by the next reader. Treat them exactly like "X is the gate."

## What this lens does not own

- Sentence-level restatement inside or between adjacent paragraphs: Prose.
- Where the lede sits, heading wording, table-vs-prose shape: Reader cost.
- Whether the document is addressed to the right reader, changelog structure, summary-vs-body scope: Framing. (You own summary-vs-body *claims*; Framing owns summary-vs-body *scope*. If a summary promises a test and the body proposes a rebuild, that is Framing. If a summary says "three findings" and the body has four, that is you.)
