---
name: simplify-doc
description: Editing pass for a finished local markdown draft - four parallel reviewers (prose, cohesion, reader cost, framing) find what makes the document harder to read or easy to misread, then one editor applies the mechanical fixes to the file and hands judgment calls back to the author. Use this whenever the user wants a document tightened, cleaned up, polished, made readable, given an edit pass, or checked before sharing - "tighten this", "clean up this draft", "make this read well", "edit pass on", "polish before I send", "/simplify-doc" - and whenever a doc is about to be shared, published, or fed into a memory file or skill. Also use it when the user worries a doc will be misread, contains shorthand nobody else will follow, or has phrases that could get taken as rules. Do NOT use for fact-checking numbers, stress-testing the argument (/red-team), summarizing, or Notion pages that have no local file.
---

# Simplify Doc

`/simplify-doc <path> [voice: default|personal] [changed]` -> 4 lens reviewers in parallel -> 1 editor merges and applies -> judgment calls back to the author

You are improving how a finished draft reads, not whether it is right. Four reviewers each read the whole document through one lens and return findings. One editor merges them, applies the mechanical ones to the file, and writes the judgment calls to a flags file for the author. Fact-checking, argument stress-testing (`/red-team`), and summarizing are separate jobs. Leave those alone here.

## Why four lenses instead of one pass

A single editor reading top to bottom catches sentence-level problems and misses document-level ones. By section five it has absorbed the author's shorthand and no longer notices it, and it has accepted the coined phrase from section two as an established fact. Each lens is a different question asked of the same text. Running them as independent agents keeps each reviewer naive to the others, which is what makes the document-level defects visible.

The four questions:

| Lens | Question | Owns | Reviewer |
|------|----------|------|----------|
| **Prose** | Is each sentence saying its thing once, plainly? | Filler, contrast frames, em dashes, fragments, hedging, magnitude words, restatement, term drift, word-level jargon, passive with a named actor | `prose-editor` in `review` mode (its own checklist) |
| **Cohesion** | Does the document hold together section to section, and can a reader who was not in the room take every phrase forward? | Section-to-section logic, shorthand references, coined phrases that harden into rules, summary vs. body agreement | `doc-editor` with `references/cohesion.md` |
| **Reader cost** | How much work does a skimmer do to get the point? | Lede placement, headings as claims, prose that should be a table (or the reverse), section length vs. job, numbers missing their comparison, emphasis | `doc-editor` with `references/reader-cost.md` |
| **Framing** | Who is this written to, and does every section stay addressed to them? | Audience drift, changelog structure, sections doing another section's job, scope drift between summary and body, register mismatch | `doc-editor` with `references/framing.md` |

The partition matters. Each reference file says what it does not own so the same sentence does not come back four times with four rewrites.

## Phase 0 - Scope

1. **Resolve the target.** This skill edits local markdown only. If the user gives a Notion URL or a non-markdown file, say so and offer the nearest path (fetch the page to a local file first, or point at an existing draft).

2. **Pick the register.** A `voice:` argument wins. Otherwise infer: a path under `personal/`, or a document written in the first person with the user as author, gets the personal register, `personal/writing-style.md`. Everything else gets the default register, `docs/writing-style.md`. If the chosen file does not exist, say so and proceed; the reviewers fall back to the standards built into their own checklists. State the inferred register to the user in one line before spawning anything. It is the cheapest thing to correct and the most expensive to get wrong, since every reviewer calibrates against it.

3. **Set the edit scope.** Default is the whole document. With the `changed` argument, run `git diff HEAD -- <path>` (and `git diff @{upstream}...HEAD -- <path>` when an upstream exists) and pass the changed line ranges to the reviewers. Reviewers still read the whole document, because cohesion cannot be judged from a hunk, but they only propose edits inside the changed ranges plus any cohesion break the change introduced.

4. **Set up the working directory.** `tmp/simplify-doc/<parent>-<stem>/` where `<parent>` is the document's immediate folder name and `<stem>` is the filename without extension (`scratch/churn-analysis/findings.md` -> `tmp/simplify-doc/churn-analysis-findings/`). The parent is there because `findings.md` and `README.md` recur across folders, and two runs sharing a directory overwrite each other's findings. Copy the original there as `original.md`. That copy is the undo, so it is not optional.

5. **Check the destination.** If the document contains Notion XML (`<table`, `<callout`, `<mention-page`), mark it Notion-bound so the editor preserves that syntax rather than converting tables to pipes.

## Phase 1 - Review (4 agents in parallel, one message)

Launch all four in a single message so they run concurrently. Each gets the same facts and one lens.

**Every reviewer prompt carries:**
- Document path, and the scope (whole document, or the changed line ranges)
- Register file to read first (or a note that none exists)
- Output path: `tmp/simplify-doc/<parent>-<stem>/<lens>.md`
- Whether the doc is Notion-bound
- The finding format below, verbatim

**Three `doc-editor` spawns** (`subagent_type: doc-editor`), each in `review` mode with its lens reference path: `references/cohesion.md`, `references/reader-cost.md`, `references/framing.md` (all relative to this skill's folder). If the session reports that `doc-editor` is not a registered agent type (agent files added since the session started are not loaded until the next one), spawn `general-purpose` with `model: sonnet` instead and open the prompt with: "You are acting as the `doc-editor` agent. Read `.claude/agents/doc-editor.md` first and follow its Review mode exactly; its finding format is your output contract." The same fallback applies to the apply-mode spawn in Phase 2, and to `prose-editor`.

**One `prose-editor` spawn** (`subagent_type: prose-editor`) in `review` mode with the register file, the output path, and the finding format.

### Finding format

All four reviewers write findings in this shape. The editor parses it, so the quote has to be verbatim; a paraphrased quote is an edit that cannot land.

```
### <LENS>-<n> - L<line> - mechanical | judgment
**Quote:** the exact text from the document, enough to anchor an edit uniquely
**Problem:** one sentence naming what the reader pays
**Rewrite:** the replacement text (mechanical), or the question the author has to answer (judgment)
```

**mechanical** means the rewrite changes wording only. No claim, number, quoted passage, or citation changes, and the reviewer would bet the author accepts it without looking. **judgment** is everything else: the fix needs a fact the document does not contain, would add or remove a claim, or depends on what the author meant. When in doubt, judgment. A wrongly mechanical finding edits the author's meaning; a wrongly judgment finding costs them one glance.

Each findings file ends with a `## Counts` block: mechanical, judgment, and hits per sweep pattern. Zero is a result worth stating.

## Phase 2 - Merge and apply (1 agent)

Wait for all four. Then spawn one `doc-editor` in `apply` mode with:
- Document path and the path to `original.md`
- The four findings paths (and which, if any, is missing because a reviewer failed)
- Register and Notion-bound flag
- Output paths: `tmp/simplify-doc/<parent>-<stem>/edit_log.md` and `tmp/simplify-doc/<parent>-<stem>/flags.md`

The editor dedups findings that anchor on overlapping text, applies the mechanical ones by quote anchor, demotes anything that would touch a claim or number, re-reads the whole document once for breakage its own edits caused, and writes the log and the flags. Its rules live in `.claude/agents/doc-editor.md`. Do not read the four findings files yourself; the editor merges them, and you read what comes out.

## Phase 3 - Hand back

1. Read `flags.md` and the editor's summary. Skip `edit_log.md` unless a flag sends you there.
2. Point the user to the edited document with a clickable path so they can open it directly.
3. Report in under fifteen lines:
   - Edits applied, as a count per lens
   - The judgment calls, as a list the author can answer with a word or a sentence each. Each item carries the quote and the direction the lens proposed.
   - Sections with heavy rewrites (more than about a fifth of the text changed), so the author knows where to actually read
   - Where the original copy lives
4. If another workflow calls for a final `prose-editor` pass on this document, this run satisfies it. Do not spawn it again on the same document.

## Rules

- **NEVER change a number, quoted passage, citation, or claim**, and never let the editor do it. Whether the number is right is a fact-check; whether the claim is right is the author's call.
- **The whole document is always read**, even with `changed`. A cohesion defect is by definition not visible inside one hunk.
- **The orchestrator does not edit the document.** Reviewers find, the editor applies, you decide what to tell the author. Applying twenty edits inline is batchable mechanical volume, and doing it here means the judgment calls get made in the same breath as the typing.
- **Do not add explanatory notes into the document.** A cut is a cut. The reasoning goes in `edit_log.md`, where the author can find it if they want it.
- **Do not stack editing passes.** If the document is mid-way through another workflow that owns its style pass, let that workflow finish; running both produces two conflicting edits per sentence.
