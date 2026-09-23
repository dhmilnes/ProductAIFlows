# Framing lens

**The question:** Who is this document written to, and does every section stay addressed to them?

## Why this lens exists

A document is not a discussion thread. It should describe the end state and be addressed to a reader who is not the author or a co-author. Drafts drift from this in predictable ways: a paragraph answers a question a co-author asked in review, a section accretes dated updates, a summary written on Monday no longer matches a body rewritten on Thursday. Each drift costs the outside reader a reconstruction they should not have to do. Sentence-level process phrases ("after reviewing the data, we...") belong to the Prose lens; you take the section-level and audience-level version of the same failure.

Read the register file named in your prompt first, if one exists. The register tells you who the reader is: the default register addresses execs and cross-functional partners; the personal register addresses the author's manager or a peer and is allowed to be blunt and first-person.

## Checks

**1. Audience drift.** Passages addressed to someone other than the end reader: a co-author ("as we discussed", "you asked for", "per your note"), the assistant that drafted it, or the author's future self (notes-to-self, TODO markers, "(check this)", "(verify)"). Also meta-commentary about the document's own drafting ("this section was hard to write", "we chose this framing because"). Mechanical when the passage carries nothing the end reader needs (delete it). Judgment when it carries a real open question or an unverified claim; propose converting it to an explicit item in an Open Questions section rather than deleting the information.

**2. Changelog structure.** A section that reads as accretion: "Update:", "Added 9/17:", dated appends, a paragraph that responds to the paragraph before it, a caveat bolted onto a claim rather than integrated into it. The reader should meet the current state, not replay how it got there. Mechanical when the current state is fully stated somewhere in the section (collapse to it). Judgment when the history is itself the content (a decision log, a timeline), or when collapsing would drop a distinction the author might want.

**3. Sections doing another section's job.** Each heading makes a promise about what is under it. Check that the content keeps it. For PRDs and strategy docs: Summary says what we are doing, Hypothesis states the bet and its theory, Justification argues why now, Metrics say what success looks like, Requirements describe the product change. For other documents, apply the same test loosely: a "Business goals" section that contains roadmap decisions, a "Findings" section that contains recommendations, a "Next steps" section that re-argues the case. Judgment: name the content and the section it belongs in. Do not move it.

**4. Scope agreement between summary and body.** The summary promises a checkout test; the body proposes rebuilding payments. The purpose line says "shared context"; the body ends with a decision request. Always judgment: which one is right is the author's call, and it is usually the most consequential finding this lens produces. Quote both.

(Cohesion owns the adjacent case where the summary and body agree on scope but disagree on *claims*, like three findings promised and four delivered.)

**5. Defensive sections.** A section or paragraph whose purpose is to defend the document rather than inform the reader: a methodology note explaining word choices, a paragraph pre-empting an objection nobody in the audience raised, a "why we framed it this way" aside. The inverted pyramid gives the test: claim, then support, then stop. Judgment: recommend a cut or a move to an appendix, and say which.

**6. Register mismatch.** A default-register document that reads as personal notes (clipped fragments, in-jokes, first names with no role for a reader who does not know them). A personal-voice document that has slid into consultant prose ("the through-line is", balanced-calibration tone, titles instead of names, metrics as structure instead of punctuation); the personal style guide may list more drift markers. Mechanical only when the fix is wording within the same claim. Judgment when the whole passage would need rewriting in a different voice.

**7. Reader's next move.** Does the document tell the reader what to do with it? A PRD or strategy doc without a decision requested, a findings doc without who should act, a context doc that ends on a cliff. Judgment: propose the closing line you infer and let the author confirm.

## What this lens does not own

- Sentence-level process narration and hedging phrases: Prose.
- Where the lede sits, heading wording, table-vs-prose shape, section length: Reader cost.
- Shorthand references, coined phrases, and claim agreement between sections: Cohesion.

## Sweep

Candidates, not verdicts:

```
Co-author address:        (?i)\b(as (we|you) discussed|you asked|per your|as requested|you mentioned|as agreed with you)\b
Notes to self:            (?i)\b(TODO|TBD|FIXME|XXX)\b|\((check|verify|confirm|source\?|cite)\b[^)]*\)
Dated appends:            (?i)^\s*(\*\*)?(update|added|edit|revised|note)(\*\*)?\s*[:(]|\b(added|updated) (on )?\d{1,2}/\d{1,2}\b
Drafting commentary:      (?i)\b(this (doc|document|section) (is|was|tries|attempts)|we (chose|decided) to (frame|word|structure|call))\b
```

Report the count per pattern in your `## Counts` block.
