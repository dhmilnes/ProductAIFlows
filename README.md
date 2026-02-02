# ProductAIFlows

AI-powered workflow automation for product management. Connects Notion, analytics, browser tools, and research to automate investigation, writing, and reporting tasks.

## The Idea

Most people think of AI prompts as one-off questions. This repo treats prompts as **shared, versioned documents** — the person who's best at each job writes the prompt, and everyone else benefits.

A data analysis framework written by your strongest analyst. A test design process from your best experimenter. A strategy structure from your sharpest strategic thinker. These live in the repo as skills and agents that anyone can run.

## Quick Start

This repo is designed to work with [Claude Code](https://claude.ai/code). Open it in Claude Code and use the skills below.

1. Clone the repo
2. Edit `personal/aboutme.md` with your role, priorities, and collaborators
3. Ask a question or invoke a skill

## Skills

Skills are workflows Claude runs automatically when relevant, or manually via `/skill-name`.

| Skill | What it does | Invoke with |
|---|---|---|
| **analyze** | Rigorous data investigation with hypotheses, YoY comparisons, and audit trail | Ask a data question, or `/analyze` |
| **test-thinking** | Design meaningful A/B test variations using behavioral science principles | `/test-thinking` |
| **strategy-doc** | Build product strategy documents using Cagan + Playing to Win frameworks | `/strategy-doc` |

## Agents

Agents are specialized sub-processes spawned by skills. They separate concerns — researchers don't write, writers don't search, reviewers poke holes.

| Agent | Purpose |
|---|---|
| `notion-researcher` | Search and synthesize information from Notion |
| `notion-writer` | Publish content to Notion with proper formatting |
| `competitor-researcher` | Research market landscape and competitive positioning |
| `strategy-writer` | Draft strategy documents in executive-focused style |
| `strategy-reviewer` | Critique strategy docs and surface blind spots |
| `py-visualization-writer` | Create data visualizations following Tufte/Knaflic principles |

## Browser Automation

Claude in Chrome lets AI see and interact with web pages — reviewing landing pages, running competitive teardowns, or auditing UX flows. Requires the [Claude in Chrome extension](https://chromewebstore.google.com/detail/claude-in-chrome/).

## Directory Structure

```
ProductAIFlows/
├── .claude/
│   ├── skills/           # Workflow definitions (auto-discovered)
│   ├── agents/           # Sub-agents called by skills
│   └── settings.local.json
├── docs/                 # Reference documentation
├── personal/             # User-specific context (gitignored contents)
│   ├── aboutme.md        # Your role, focus, collaborators
│   └── queries/          # Saved SQL queries for reuse
├── tmp/                  # Ephemeral session files (gitignored)
├── scratch/              # Active working files (gitignored)
├── output/               # Stable outputs (gitignored)
├── research_briefs/      # Agent research outputs (gitignored)
└── CLAUDE.md             # Instructions for Claude
```

## Key Conventions

- **tmp/** files auto-delete — copy to `scratch/` or `output/` before further use
- **scratch/** is for work-in-progress — organized by `{topic}_{date}/`
- **personal/queries/** stores reusable SQL with parameterized defaults
- All Python runs through `poetry run python`

## Customization

### Add your context

Edit `personal/aboutme.md` with your role, current priorities, and key collaborators. Claude reads this at the start of every session to personalize responses.

### Add a skill

Skills are markdown files in `.claude/skills/`. Each needs a `SKILL.md` with YAML frontmatter (`name` and `description` fields). Write the framework, constraints, and anti-patterns — the AI handles implementation.

### Add an agent

Agents live in `.claude/agents/`. Define principles and hard constraints, not step-by-step procedures. The AI already knows common patterns — focus on what makes your team's approach distinctive.

## More Details

See `CLAUDE.md` for full technical documentation and conventions.
