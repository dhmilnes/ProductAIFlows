---
description: Run one of the user's saved personal prompts from personal/prompts/
argument-hint: <prompt-name> [extra context...]
---

The user invoked `/my` with arguments: `$ARGUMENTS`

Personal prompts live in `personal/prompts/<name>.md` (gitignored, user-customized). Your job is to load the named prompt and execute it as if the user had typed its contents directly.

## How to handle the arguments

Treat the first whitespace-delimited token as the prompt name. Everything after it is **extra context** the user is layering on top — dates, focus areas, segments, freeform notes, etc. The prompt files do not need placeholders; read the prompt, read the extras, and apply judgment to weave them in. Mention what you're folding in if it materially changes how the prompt runs.

## Steps

1. **Resolve the file.** Read `personal/prompts/<name>.md`. If it doesn't exist, fall through to the not-found path below.
2. **Execute the prompt.** Treat its contents as the user's instructions. Honor any frontmatter the user has added (e.g., default params), then run.
3. **Apply extras.** If the user passed extra arguments after the name, fold them in naturally — as parameters, scoping, or additional asks.

## Not-found path

If `personal/prompts/<name>.md` is missing:
1. List what's actually in `personal/prompts/` (file stems only, no `.md`).
2. Ask which the user meant. If nothing is close, suggest they run the `make-my` skill to create a new one.

## No name given

If `$ARGUMENTS` is empty, list available prompts and ask which to run. Don't guess.

## Why this command exists

Personal prompts are kept out of the repo so the user can iterate on phrasing, defaults, and shortcuts without adding noise to git. `/my` is the runner; `make-my` is the authoring counterpart. Keep the contract simple — name in, prompt body executed, extras folded in.
