# Reader cost lens

**The question:** How much work does a skimmer do to get the point, and where is that work wasted?

## Why this lens exists

The reader is an exec scanning ten documents, or a partner deciding in ninety seconds whether to read the whole thing. The skim test applies: headings, first sentences, and bolded text should carry the argument on their own. When they do not, the reader either reads everything (expensive) or reads the wrong thing (worse). This lens measures the structure, not the sentences.

Read the register file named in your prompt first, if one exists. The personal register tolerates fragments and bullets where the default register wants prose; calibrate before you flag shape.

## Procedure: run the skim test literally

Extract, in order, every heading, the first sentence of every section and paragraph, and every bolded phrase. Read that extract alone. Where it fails to carry the argument, you have found the defects. Then read the whole document to classify them.

## Checks

**1. Lede placement.** In each section, where is the claim? If the first sentence is context and the claim arrives in sentence three, propose moving the claim up. Mechanical when it is a reorder within the section with no new words. Judgment when the section has no claim at all, or the claim only exists by implication; say what you think the claim is and let the author confirm.

**2. Headings state claims, not topics.** "Justification" tells the skimmer nothing. "Enterprise is 19% of customers and 42% of support tickets" tells them the section's job. Mechanical when the section's own first sentence supplies the claim (lift it into the heading). Judgment otherwise. Standard template headings that a downstream system depends on (a proposal template's section names, a Notion database's expected structure) stay; note that in the finding rather than proposing a rename.

**3. Shape matches content.** A comparison of three or more items across two or more attributes, written as prose, wants a table. A sequence wants a numbered list. Eight one-line bullets that are really three ideas want three bullets or a paragraph. The reverse also costs: a two-row table, a bulleted list where each bullet is a full paragraph, a callout around a routine sentence. Converting prose to a table is mechanical only when every cell is already stated in the prose; if you would have to fill a cell the author did not, it is judgment. For Notion-bound documents, propose tables in Notion XML, never pipe syntax.

**4. Section length against its job.** A summary over roughly 100 words. A justification past three paragraphs. A background section longer than the argument it supports. A section whose second half is an appendix in disguise. These are judgment findings: name what should move and where (an appendix, a linked doc, a toggle), but do not move content yourself. Moving content changes what the document argues, and that is the author's call.

**5. Numbers without their comparison.** "14.7% of enterprise customers submit a ticket in a month" is a fact waiting for its point. "2.5x the SMB rate" is the point. Every number should arrive with the comparison that makes it mean something: the baseline, the prior period, the other segment, the target. Mechanical when the comparison exists elsewhere in the document (bring it adjacent). Judgment when it does not exist in the document, and never invent one. Whether the number is correct is not your question.

**6. Emphasis.** Bold belongs on key metrics, decisions, and actions. Flag bold on every other phrase (the emphasis stops signaling), and flag a long section with no signposting at all (the skimmer has nowhere to land). Mechanical either way.

**7. Orientation at the top.** A document longer than a page with no statement of what it is, who it is for, and what the reader should do with it. Judgment: propose a one-line purpose drawn from the content and let the author confirm or replace it.

## What this lens does not own

- Wording inside a sentence, filler, contrast frames, magnitude words, undefined acronyms and vocabulary jargon: Prose.
- Whether the document is addressed to the right reader, and whether sections are doing another section's job: Framing.
- Shorthand references to things and events, and phrases that harden into rules: Cohesion.

If a paragraph is both badly placed and badly worded, flag the placement and leave the wording; Prose will get the sentence, and the editor merges.

## Sweep

Candidates, not verdicts:

```
Topic-only headings:      ^#{1,6}\s*(Background|Context|Overview|Justification|Details|Notes|Discussion|Analysis|Summary|Introduction|Approach|Methodology)\s*$
Bare percentages:         \d+(\.\d+)?%   (then, for each hit, check the same sentence for a comparison word: vs, versus, compared, than, up from, down from, x, against, baseline, target, prior, previous, last. Ripgrep has no lookahead without -P, so this is a two-step check.)
Bold density (per para):  \*\*[^*]+\*\*
Long bullets:             ^\s*[-*]\s+.{240,}$
```

Report the count per pattern in your `## Counts` block.
