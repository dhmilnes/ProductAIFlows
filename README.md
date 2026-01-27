# ProductAIFlows

AI-powered workflow automation for product management. Connects Notion, analytics, and research tools to automate investigation, writing, and reporting tasks.

## Quick Start

This repo is designed to work with [Claude Code](https://claude.ai/code). Open it in Claude Code and use the skills below.

## Skills

Skills are workflows Claude runs automatically when relevant, or manually via `/skill-name`.

| Skill | What it does | Invoke with |
|-------|--------------|-------------|
| **analyze** | Rigorous data investigation with hypotheses, YoY comparisons, and audit trail | Ask a data question, or `/analyze` |
| **test-thinking** | Design meaningful A/B test variations using behavioral science principles | `/test-thinking` |
| **strategy-doc** | Build product strategy documents using Cagan + Playing to Win frameworks | `/strategy-doc` |

## Agents

Agents are specialized sub-processes spawned by skills. You don't call them directly.

| Agent | Purpose |
|-------|---------|
| `notion-researcher` | Search and synthesize information from Notion |
| `notion-writer` | Publish content to Notion with proper formatting |
| `competitor-researcher` | Research market landscape and competitive positioning |
| `strategy-writer` | Draft strategy documents in executive-focused style |
| `strategy-reviewer` | Critique strategy docs and surface blind spots |

## Directory Structure

```
ProductAIFlows/
├── .claude/
│   ├── skills/           # Workflow definitions (auto-discovered)
│   ├── commands/         # User-invokable commands (planned)
│   └── agents/           # Sub-agents called by skills
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

## Customization

### Add your context

Edit `personal/aboutme.md` with your role, current priorities, and collaborators. Claude reads this to personalize responses.

### Save reusable queries

Put frequently-used SQL in `personal/queries/` with YAML frontmatter:

```sql
---
name: Weekly Metrics
description: 7-day metrics for a segment
params:
  segment: "enterprise"
---
SELECT ... WHERE segment = @segment
```

### Create a new skill

1. Create `.claude/skills/your-skill/SKILL.md`
2. Add YAML frontmatter with `name` and `description`
3. Write instructions Claude should follow

See existing skills for examples.

## Key Conventions

- **tmp/** files auto-delete — copy to `output/` before analysis
- **scratch/** is for work-in-progress — organized by project
- **Human gates** — skills that modify external systems (Notion, etc.) always ask before acting

## More Details

See `CLAUDE.md` for full technical documentation and conventions.
