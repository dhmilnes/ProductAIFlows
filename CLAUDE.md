# CLAUDE.md

ProductAIFlows is an AI-powered workflow automation toolkit. It connects analytics data with documentation systems to automate research, writing, and reporting tasks.

## Meta: How to Evolve Prompts

**To trigger learning:** When I make a mistake, tell me:
> "Reflect on this. Abstract the pattern."

**Where does the rule belong?**

| Scope | Location | Example |
|-------|----------|---------|
| Global (applies everywhere) | CLAUDE.md | Windows Python `-c` fix |
| Skill-specific workflow | `.claude/skills/*/SKILL.md` | "Avoid magnitude words" in analyze |
| Agent behavior | `.claude/agents/*.md` | Tufte styling in py-visualization-writer |
| Reference docs | `docs/*.md` | Notion table syntax in formatting guide |

**Is it a new rule or an edit?** Often the right fix is clarifying an existing rule, not adding a new one. Check if related guidance already exists.

**Rule format (when adding new):**
- Lead with WHY before the rule — context prevents misapplication
- Use NEVER/ALWAYS for hard constraints, "prefer" for soft guidance
- Keep rules under 2 sentences
- Add examples only when the antipattern is subtle

**What belongs in CLAUDE.md specifically:** Cross-cutting patterns that affect multiple workflows, repo-wide conventions, integration quirks.

## Learned Patterns

Rules added through reflection on recurring mistakes.

- **Discovery before design prevents rework.** When building new agents, skills, or features, start with questions about use cases, constraints, and pain points. Understand the problem space before proposing solutions. Ask "What problems are you solving?" not "Here's what I built."

- **Failing to read the personal folder leads to missed context.** ALWAYS check for an `personal/aboutme.md` for user-specific context and saved queries before starting work.

- **Duplicating source docs bloats skill files and creates maintenance burden.** NEVER repeat what a template or external doc already explains. Link to the source for "what to include," only add supplementary value: format specifics, length limits, examples, gotchas.

- **Writing without reading the source leads to drift and rework.** ALWAYS fetch and verify source documents before writing content that depends on them - but only what the current task requires, not "just in case."

- **Skills require exact file structure to be discoverable.** Entry file MUST be named `SKILL.md` (not `prompt.md`). MUST include YAML frontmatter with `name` and `description` fields. Without these, Claude Code won't recognize the skill.

- **Skill instructions specify architecture, not suggestions.** When a skill says "use X agent for Y task" or lists Critical Rules, those define the workflow - not optional guidance. Read the Critical Rules section FIRST and treat agent delegation as constraints. Default behavior is to "just do the work" which violates orchestration patterns.

- **Agent prompts define principles, not procedures.** AI agents already know common libraries and coding patterns. Focus on: domain principles (Few/Knaflic), hard constraints (file paths), preferences (ggplot style), and anti-patterns (no pie charts). Avoid detailed code templates - the agent can implement principles without step-by-step instructions. Over-prescription wastes context and reduces adaptability.

- **Training data confidence causes hallucination.** When documenting external systems (APIs, third-party tools), ALWAYS fetch current docs or test actual behavior. Never write guides from memory alone—training data may be outdated or wrong.

## Notion Formatting

Before writing to Notion, read `docs/notion-formatting-guide.md`. Key gotcha: tables require the API's block format, not Markdown pipes.

## Available Workflows
Always check skills for use cases.

**Skills** (`.claude/skills/`) — Auto-discovered via YAML frontmatter. Claude uses these automatically when user needs apply.

| Skill | Purpose | Invoked By |
|-------|---------|------------|
| `analyze` | Rigorous data investigation | User asks data questions |
| `test-thinking` | A/B test variation design | User designing test variations |
| `strategy-doc` | Product strategy documents using Cagan + P2W frameworks | User wants to develop strategy |
| `red-team` | Adversarial analysis of proposals, arguments, product ideas | `/red-team`, "poke holes in this", "stress test this" |
| `assumption-mapping` | Decompose a proposed solution into testable leap-of-faith assumptions | "what are we assuming", "before we build this", "how do we de-risk this" |
| `simplify-doc` | Four-lens edit pass on a finished markdown draft | "tighten this", "polish before I send", `/simplify-doc` |
| `pm-style` | Writing standards for PM documents (PRDs, strategy docs, briefs) | Drafting or reviewing any PM document |
| `make-my` | Author a new personal runbook in `personal/prompts/` | "save this", "make this reusable", "turn this into a /my" |

**Commands** (`.claude/commands/`) — User-invokable via `/command-name`.

| Command | Purpose |
|---------|---------|
| `my` | Run a saved personal prompt: `/my <name> [extras]` |

**Agents** (`.claude/agents/`) — Sub-agents spawned by skills via Task tool. Not user-invokable directly.

| Agent | Purpose | Used By |
|-------|---------|---------|
| `notion-researcher` | Notion search + synthesis (general or strategy-context format) | strategy-doc, any workflow |
| `notion-writer` | Publishes content to Notion with proper formatting | strategy-doc |
| `competitor-researcher` | Market landscape and competitive positioning | strategy-doc |
| `strategy-writer` | Drafts strategy docs in exec-focused style | strategy-doc |
| `strategy-reviewer` | Critiques strategy docs, surfaces blind spots | strategy-doc |
| `doc-editor` | Lens review (cohesion, reader cost, framing) and merge-and-apply editing | simplify-doc |
| `prose-editor` | Sentence-level de-slop pass: filler, hedging, contrast frames, em dashes | simplify-doc, any workflow |
| `doc-researcher` | Returns raw passages from local files with `path:line` pointers, no verdicts | any workflow |

## Personal Query Library

Users can save SQL queries they run repeatedly in `personal/queries/`. Check there before invoking full data discovery.

**When user asks for data:**
1. Check if `personal/queries/` has a matching query (by name or description)
2. If found: read the file, parse YAML frontmatter for params, substitute values, run directly
3. If not found: proceed with data analysis skills for full field/table discovery

**Query file format:**
```sql
---
name: Weekly Metrics Report
description: 7-day metrics for specific segment
params:
  period_start: "2025-01-01"
  segment: "enterprise"
---
SELECT ... WHERE date >= @period_start AND segment = @segment
```

**Saving new queries:**
When a query works well and seems reusable, offer to save it:
1. Ask: "Want me to save this query for reuse?"
2. If yes: create file in `personal/queries/` with descriptive name (lowercase, underscores)
3. Extract variable parts as params (dates, segments, products)
4. Add YAML frontmatter with name, description, and param defaults


## Working Conventions

**tmp/ has 24-hour TTL.** Use tmp/ for intra-conversation context (e.g., advisors writing files for query agents to read). Files survive overnight for next-morning work, but treat as ephemeral - don't rely on them persisting long-term.

**ALWAYS use `poetry run python` to execute Python.** This repo manages dependencies via Poetry; the system Python lacks required packages. Never use bare `python` or `pip install`.

**Analysis outputs go in a scratch folder.** Each analysis gets a dedicated folder: `scratch/{topic}_{date}/`. All artifacts live together — CSVs, scripts, visualizations. Copy query result CSVs from `tmp/` into this folder before using them in Python.

Example: `scratch/support_tickets_2026-01-31/`

**Check for prior work before starting analysis.** Time-saving pattern for data analysis tasks:
1. Ask user: "Is there prior work on [topic] I should reference?"
2. If user indicates yes, check `scratch/` for relevant folders
3. Reuse queries, data, or analysis structure when applicable

**File naming conventions:**
- Include topic and date: `feature_timeline_2026-01-26.py`
- Use underscores, lowercase
- Version when iterating: `timeline_v2.py`, `timeline_v3.py`

**Subdirectory standards:**

| Path | Contents |
|------|----------|
| `scratch/{topic}_{date}/` | All analysis artifacts (CSVs, scripts, charts) |
| `scratch/uxr-[project]/` | UXR coding aggregation files |
| `personal/queries/` | Saved reusable SQL queries |
| `tmp/context/` | Agent research outputs for intra-session use |

All folders are tracked in git but contents are gitignored (except personal/README.md and templates).

## Agent Orchestration Principles

When workflows spawn sub-agents:
1. **User gates critical actions** - Always get approval before updating Notion or making significant changes
2. **Separation of concerns** - Research agents don't write, writing agents don't search
3. **Parallel execution** - Spawn independent agents simultaneously when possible
4. **Clear handoffs** - Agents return focused briefs, orchestrator decides what to commit
5. **Single writer per page** - The orchestrator owns the *decision* to write and the user's approval for it; the write itself is normally delegated to `notion-writer`, a shared utility agent any workflow can spawn. Only one agent writes a given page in a task, and it re-fetches the page immediately before and after the write.

### Orchestrator-First Working Model

The main session (Opus) is the **orchestrator**: it frames, decides, and delegates — it does not do bulk labor itself. Right-size every delegated task to the cheapest model tier and lowest effort that fits. Goal: control cost and keep the orchestrator's context lean and long-lived.

Delegation is **three orthogonal decisions**:

**1. Locus — inline vs. delegate.**
- **Delegate when** (the heavy-in/heavy-out test): *heavy-in* (a large source to digest — file, page, query results, transcript) · *heavy-out* (more than ~a page produced) · parallelizable fan-out · **batchable mechanical volume** (many small homogeneous edits/lookups — batch into ONE spawn) · context hygiene (would otherwise dump use-once debris into durable context).
- **Keep inline when**: a single small task below the boot threshold and not batchable with siblings · needs this conversation's live, accumulating context · it *is* the orchestration role (weighing results, deciding next steps, user alignment) · trivial or already known.
- The boot threshold (~20k tokens reloaded per spawn: system prompt + this file + tool schemas) is **per-spawn, not per-item** — batch small homogeneous tasks into one spawn to clear it. Conversely, when fanning out *independent* tasks, use the **fewest spawns that preserve useful parallelism** — each spawn re-pays the boot cost, so consolidate (don't over-fan-out) when the work per item is small or latency is cheap. "Hard" is *not* a reason to stay inline: hard + heavy + self-contained → an **Opus sub-agent** (keeps the bulk and intermediate reasoning out of durable context).
- **A definition or schema lookup is heavy-in retrieval — delegate it.** Reading a doc to nail down a field meaning, table name, or definition is the same as digesting any large source: send a Haiku Explore agent and get the ≤5-line conclusion back. Don't pull the source into your context "just to be sure" — "I need to *understand* this first" is the rationalization that smuggles heavy-in reads inline.

**2. Tier — capability** (`model=` per call, or the agent's frontmatter default):
- **Haiku** — retrieval, fetch, mechanical audits, executors. No open-ended reasoning.
- **Sonnet** — reasoning, writing, code (the floor for code generation), citation research, fact-checking.
- **Opus** — hard synthesis/analysis/decomposition; the orchestrator runs here, or a sub-agent for hard + heavy + self-contained work.

**3. Effort — deliberation depth** (config-time only: agent frontmatter `effort:` + session `effortLevel`; no per-call override; Haiku has no effort knob). Tier = capability ceiling; effort = how much of it you spend. Need more capability → up a tier; need more deliberation → up effort.

**File-handoff (always, when delegating):** every delegated task names an output path (`tmp/` for ephemeral inter-agent context, `output/`·`research_briefs/` for keepers); the sub-agent writes there and returns a pointer + ≤5-line summary — never a full dump back into the orchestrator's context. The orchestrator reads the file only when it needs the detail.

**Numbers travel as provenance-tagged data, never as summary prose.** Any figure destined for a deliverable comes back in the handoff *file* as an exact value with its source pointer (CSV path + column, Notion page + the exact figure, query + cell) — never rounded or paraphrased into the ≤5-line summary. The orchestrator reports from the artifact and audits the deliverable; it does NOT transcribe figures out of a sub-agent's summary. This is how delegation and verification reconcile: verification happens at the point of contact (the sub-agent reading the source), and the orchestrator owns auditability, not re-reading.

**Mixed-complexity:** tier the sub-task, not the skill (mechanical → Haiku, hard core → Sonnet/Opus, tests → Sonnet); on uncertain complexity start at the higher tier (try-cheap-then-retry pays twice).

**Pricing rationale (per 1M tokens):** Opus $5/$25 · Sonnet $3/$15 · Haiku $1/$5. Haiku is 5× cheaper than Opus, 3× cheaper than Sonnet (same ratio in/out) — moving a task down one tier buys 3–5× the tokens at equal cost.

## Trust Is Built by Being Cheap to Verify

The way an agent loses a user's trust is by raising their **correction load** — and it compounds. One wrong output isn't one unit of cost; it's a tax on trust in *everything else*, because the user now has to re-check all of it to find which parts are safe. So the target is not "be right" — it's **be cheap to verify**: minimize how much of the output the reader must independently check before they can rely on it. An output that is 90% right but hides which 10% is wrong is *less* trustworthy than one that is 80% right and marks its own uncertain spots — the second lets the reader check two places and move on; the first taxes everything.

Two failure modes raise verification cost, and both erode trust:

- **Hard to parse → high audit cost per claim.** If the reader has to work to follow the output, they can't scan-verify it; errors hide in the density. Lead with the conclusion, keep each claim adjacent to its support, and drop schema names, jargon, and reflexive hedging from reader-facing prose. (Concretely: write full sentences, state the end state not the process, stay with facts, don't conclude on thin data.)
- **Jumps to conclusions → confidence stops carrying information.** The first time a confident assertion turns out to be a leap, the reader learns the confidence was decoration and discounts all of it afterward. The fix is not timidity — it's **calibration**: state confidence at the level the evidence earns, so "true," "probably true," and "couldn't confirm" read as visibly different.

These two pull against each other if handled naively — uniform hedging is *harder* to parse, not safer, because every sentence sounds equally unsure and the reader must re-derive which caveats are load-bearing. Good calibration is **decisive where the evidence is solid and explicit where it's thin**, both stated plainly, neither smeared across the whole thing. A well-calibrated output is easier to audit than a hedged one, because it tells the reader where to spend attention.

## Boundaries

**Never:**
- Commit secrets, credentials, or API keys
- Modify production data or configs without explicit approval
- Include PII (names, emails, user IDs) in outputs shared externally
- Push to main/master without PR review
- Run destructive commands (DROP, DELETE, rm -rf) without confirmation

**Always ask first:**
- Before making changes that affect multiple files
- Before running commands that cost money (large database queries)
- When uncertain about user intent

## Troubleshooting

**Notion update fails silently**: Verify page ID is correct and you have edit access. Use `notion-fetch` first to confirm.

## Repository Structure

```
ProductAgents/
├── .claude/
│   ├── skills/          # Auto-used by Claude when user needs apply
│   ├── commands/        # User-invokable via /command
│   ├── agents/          # Specialized sub-agents (called by skills/commands)
│   └── settings.local.json
├── docs/
│   ├── db/          # Schema docs, example queries, hints
│   └── notion-formatting-guide.md
├── mcp_servers/         # homebrewed mcps
├── scripts/             # Python utilities
├── tmp/                 # Session-only ephemeral files (fully gitignored)
│   ├── context/         # Advisor outputs for query agents
│   ├── csv/       # Query result CSVs (auto-cleaned)
│   └── uxr/             # UXR coding intermediate files
├── personal/            # User-specific context and queries (contents gitignored)
│   └── queries/         # Saved SQL queries for quick reuse
├── research_briefs/     # Agent research outputs (contents gitignored)
├── scratch/             # Active working files (contents gitignored)
├── drafts/              # WIP documents (contents gitignored)
├── output/              # Stable outputs (contents gitignored)
│   └── visualizations/  # Charts from py-visualization-writer
└── CLAUDE.md            # This file
```
