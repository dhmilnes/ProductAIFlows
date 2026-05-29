---
name: make-my
description: |
  Capture a reusable personal prompt as a markdown runbook in `personal/prompts/` so the user can rerun it later via `/my <name>`. Trigger ANY time the user has just finished an ad-hoc workflow and wants to keep it, save it, rerun it later, or use it again — even without saying "/my" or "personal prompt" explicitly. Catch all of these phrasings: "save this", "save it for next time", "keep it", "name it X", "let's save it", "I want to rerun this", "do this every [week/month/quarter]", "let's templatize this", "turn this into a /my", "make this reusable", "capture this workflow", "save it as <name>", "save this as a personal prompt", "alright that worked, let's keep it". The intent is always the same: turn what we just did into a saved runbook. Do NOT trigger for shared repo-level commands (use draft-command), skills (use skill-creator), saving non-prompt artifacts like PDFs or query results or CSVs, reminders or scheduling, or running an existing prompt — make-my is only for AUTHORING a new entry in the user's gitignored `personal/prompts/` folder.
---

# Make-My

Authoring counterpart to the `/my` command. Produces a markdown runbook at `personal/prompts/<name>.md` plus, when needed, supporting artifacts (Python scripts, SQL queries, templates) in dedicated `personal/` subfolders.

The runbook is always the single entry point: `/my <name>` only ever resolves to the `.md` file, which then orchestrates whatever else is needed.

## Why this skill exists

The user keeps personal, customized prompts out of the repo (`personal/` is gitignored). Without a structured authoring flow, those files drift toward terse one-liners that don't survive being rerun weeks later by a fresh model session with no memory of the conversation that produced them. This skill enforces just enough structure — clear goal, expected inputs, expected output, constraints — for each saved prompt to keep working cold.

## The artifact layout

A `/my` invocation always loads the runbook. The runbook may instruct the runtime model to run other files. Keep them separated by type:

| Folder | Holds | Referenced from runbook how |
|---|---|---|
| `personal/prompts/<name>.md` | The runbook itself (always required) | This is what `/my <name>` loads |
| `personal/scripts/<name>.py` | Python scripts the runbook executes | `poetry run python personal/scripts/<name>.py` |
| `personal/queries/<name>.sql` | Saved SQL queries (YAML-frontmatter format documented in CLAUDE.md) | Loaded and run via `bibot_query` with param substitution |
| `personal/<other>/` | Templates, CSVs, doc references | Read by path |

A runbook can name files with the same stem as itself (e.g., `weekly-report.md` referencing `weekly-report.py`) or pull from shared artifacts. Match what's natural for the workflow — don't force a 1:1 pairing.

## The flow

### Step 1 — Capture intent

**Interview vs. infer.** If the current conversation already contains the workflow being captured (the user just finished doing the thing), pull as much as possible from history — steps taken, tools used, inputs, the output format that landed well, corrections the user made. Only ask to fill genuine gaps. If there's no prior context (cold start: "make me a /my that does X"), do the full interview.

Get clear on:
1. **What should this prompt do?** One or two sentences. Push back if it's vague — "summarize stuff" is not a prompt; "summarize last week's experiment results into a ranked list with effect sizes and confidence intervals" is.
2. **What's the name?** Lowercase, hyphens, no extension (e.g., `weekly-report`, `experiment-summary`, `morning-standup`). Suggest one based on the intent; let the user override.
3. **Will it take extras?** `/my <name>` accepts trailing context. Decide whether this prompt expects extras (a date, a focus area, a Notion URL) or stands alone. If extras are expected, name them in the prompt body so the runtime model knows what to do with them.

### Step 2 — Identify inputs, tools, and supporting artifacts

Determine (asking or inferring from history):
- **Data sources.** BigQuery via cinco? Notion? MySQL? Web search? Local files? None?
- **Required context the user must supply.** If the prompt always needs a date range, week number, or topic, document it.
- **Optional context.** Things that change behavior if provided — segments, products, focus pages.
- **Supporting artifacts.** Does this workflow need a Python script (data transform, chart generation, multi-step analysis), a parameterized SQL query, a template, or a CSV? Decide upfront so the runbook can point at them by path.

**When to spin off a supporting file:**
- Logic is deterministic and would be tedious for the model to rewrite each run → Python script in `personal/scripts/`
- The same SQL gets run with different params → SQL file in `personal/queries/` with YAML frontmatter
- The output uses a fixed structure → template/example file in `personal/`
- Logic is simple enough for the model to do inline → keep it in the runbook, no extra file

If the prompt depends on an existing artifact, name it explicitly. Don't duplicate.

### Step 3 — Define the output

Be opinionated. Vague output specs produce drifty results. Pin down:
- **Format** — table, bullets, prose, Notion page, file in `output/`?
- **Length / shape** — three themes, top five quotes, one-page memo?
- **Required sections** — what must always appear? What's optional?
- **Where it lands** — printed in chat? Written to a file? Posted to Notion (with user approval)?

### Step 4 — Draft the runbook

Write it as a self-contained instruction the runtime model will execute cold. Use this skeleton — adapt freely, don't be rigid:

```markdown
# [Prompt Title]

[One-sentence statement of what this prompt does.]

## Inputs
- **Required:** [what the user must supply, e.g., date range]
- **Optional extras** (passed after `/my <name>`): [what they mean and how to apply them]

## Steps
1. [First action — typically gather data or read a source]
2. [Second action — the analysis or transformation]
3. [Third action — produce the output in the specified format]

## Output format
[Exact structure. Include a tiny example if it clarifies.]

## Constraints
- [What to include / exclude]
- [Length, tone, defaults]
- [Fallback behavior if data is missing]

## Notes
- [Edge cases, gotchas, references to other files]
```

#### Writing principles

- **Stand-alone.** The runbook will be read cold by a model that has zero memory of the conversation that produced it. No "as we discussed", no "the workflow we just walked through", no references to this skill or to other ad-hoc artifacts that aren't actually saved. A reader opening the file fresh should be able to execute it without context. Test this by re-reading the draft and asking: "Would I know what to do if this were the only thing on my screen?"
- **Imperative form.** "Pull the last 7 days of experiment results." not "You should pull..."
- **Explain why** when a constraint is non-obvious. A model running this cold will follow rules better when it understands them.
- **Lean.** Cut anything that doesn't change output. No ceremonial preamble.
- **Avoid heavy-handed MUSTs.** Reframe as guidance with a reason.

#### Universal patterns

- **Reference external files; don't inline them.** Long SQL, Python, or templates belong in `personal/scripts/` or `personal/queries/`. The runbook orchestrates, it doesn't contain.
- **Pin a concrete output template at the bottom.** Exact section names, exact table shapes, example values. Vague output specs drift between runs.
- **Surface the load-bearing step.** If one step is the whole point of the workflow (e.g., "compare to last run"), put it where it can't be missed — early, numbered, named clearly.

#### Patterns for recurring data reports

Skip these if the runbook isn't a periodic data report.

- **State the date math explicitly.** If the prompt computes windows (recent N days, YoY, etc.), have it print the absolute dates in the output so the reader can sanity-check. Hidden date arithmetic produces confidently-wrong numbers.
- **Use 364-day lookback, not 365, for YoY.** 52 × 7 keeps weekdays aligned.
- **Critical-invariants callouts.** When the SQL has gotchas that have actually burned past runs (wrong join key, wrong segment field, missing partition filter), name them in a dedicated section with the *reason*. Theoretical risks aren't worth listing; lived ones are.
- **Design for comparability.** Write to a dated folder and read the most recent prior output to produce a delta. A snapshot becomes a trend.

#### Antipatterns

- **Conditional sections without a detection rule.** "Skip on the first run" isn't actionable unless the prompt also says how to detect "first run."
- **Invariant caveats stuck under conditional Limitations sections.** A caveat that's *always* true belongs in the body where it shapes the analysis; only situational caveats belong under Limitations.
- **No failure-mode guidance.** If the prompt fans out queries or steps in parallel, say what to do when one fails — continue with partial data, halt, or retry once.
- **Trigger phrasings stranded inside a "When to invoke" section.** The opening one-liner of the runbook serves that purpose; don't duplicate.

### Step 5 — Self-review the draft, then show the user

Before showing the user, run a self-review pass against the draft. The goal is to catch the things a fresh-session reader will trip on, not to nitpick wording. Read the runbook as if you have never seen this conversation and walk through each check:

- **Stand-alone test.** Are there any references to "the workflow we discussed", "as we did earlier", "the conversation above", or to ad-hoc files that aren't actually being saved? If yes, rewrite or remove. The runbook must be self-contained.
  - *Bad:* "Use the same query approach we did earlier."
  - *Good:* "Run the SQL in `personal/queries/weekly-metrics.sql`."
- **Cold-execute test.** If the only thing on screen were this runbook, could a model produce the right output? Step through the instructions mentally. Anywhere it would have to guess is a gap to fill.
- **Reference integrity.** Every file the runbook names — Python script, SQL query, template — either already exists or is being authored alongside in this same save. No dangling pointers.
- **Inputs check.** Every "required input" has a clear way to be supplied (frontmatter param, position in `extras`, or a prompt-time question). No required input that has no path in.
- **Output template specificity.** Is the output section concrete (named sections, table shapes, example values), or vague enough that two runs could land in different formats? Tighten if vague.
- **Failure modes.** If the prompt fans out queries or external calls, is there guidance for what to do when one fails?
- **Trigger phrasings.** Are they in the opening one-liner, not stranded inside a "When to invoke" section that duplicates the lead?

Fix anything the self-review surfaces. Then show the user the cleaned draft and briefly call out:
- What was pulled from conversation history vs. invented.
- Which parts encode opinions (format, defaults, constraints) the user might want to tweak.
- What the user can pass as `extras` to vary behavior at runtime.
- Anything the self-review changed and why.

Ask: "Want me to save this to `personal/prompts/<name>.md`, or adjust first?"

### Step 6 — Save

On approval, write all files at once:
1. The runbook → `personal/prompts/<name>.md`
2. Any supporting Python → `personal/scripts/<name>.py` (or a stem that fits)
3. Any supporting SQL → `personal/queries/<name>.sql` with YAML frontmatter per CLAUDE.md
4. Any other artifacts the runbook references

Confirm with the exact invocation and list what was written:

> Saved. Run it with `/my <name>` (or `/my <name> <extras>` to scope it).
> Files: `personal/prompts/<name>.md`, `personal/scripts/<name>.py`

If any target already exists, do not silently overwrite. Show the diff or ask whether to replace, version (`<name>-v2`), or merge. Apply this to every file, not just the runbook.

## Existing conventions

Scan `personal/prompts/` for any existing runbooks and match the style the user has already established — but those are gitignored, so don't assume any specific one exists. Good runbooks share these traits: parallel data gathering fired in a single turn, thresholds explained inline with the reason (not just the number), empty sections dropped from output, and the most important finding leading rather than buried.

## Edge cases

- **The user wants something the repo already has as a command or skill.** Point them at it instead of creating a duplicate. Personal prompts are for things that don't merit committing.
- **The prompt is sensitive (credentials, internal URLs, PII).** Save anyway — `personal/` is gitignored — but flag it so the user knows not to share the file.
- **The user describes a recurring task with a schedule** (e.g., "every Monday morning"). Save the prompt, then suggest pairing with `/schedule` or `/loop` to automate the run.
- **The "prompt" is really a workflow with branching logic and broad reuse.** That's a skill, not a personal prompt. Suggest creating it as a skill instead.
- **The user says "save this" but it's not clear what kind of artifact they mean.** A `/my` runbook is the default; if the conversation produced a script, query, or doc that doesn't need an orchestrating runbook, ask whether they want a standalone artifact in `personal/scripts/` or `personal/queries/` instead — sometimes a runbook is over-structured for what they actually want.

## Files this skill touches

- **Creates:** `personal/prompts/<name>.md` (always); plus `personal/scripts/<name>.py`, `personal/queries/<name>.sql`, or other artifacts as the workflow demands
- **Reads (for context, optional):** `personal/aboutme.md`, prior `personal/prompts/*.md`, existing `personal/scripts/` and `personal/queries/` to match conventions the user has established
- **Never touches:** anything outside `personal/`
