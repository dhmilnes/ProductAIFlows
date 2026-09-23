#!/usr/bin/env python3
"""UserPromptSubmit hook for ProductAIFlows.

Re-injects the orchestrator-first delegation reminder on every turn so it does
not decay in long sessions. Whatever this prints to stdout is injected into the
model's context by Claude Code. Pure stdlib, no dependencies, so it runs the
same on Windows (PowerShell) and macOS/Linux (bash).

Full rubric lives in CLAUDE.md -> "Orchestrator-First Working Model".
"""

# ASCII only on purpose: this prints to stdout, which on Windows defaults to
# cp1252 -- non-ASCII (arrows, em-dashes, middot) raise UnicodeEncodeError and
# would crash the hook on every turn. Keep it plain.
REMINDER = (
    "[Delegation check] "
    "(1) Does this leave you? Yes if heavy-in (a large source to digest), "
    "heavy-out (>~a page produced), or parallelizable - and above the boot "
    "threshold. "
    "(2) What tier? Haiku (mechanical/retrieval) | Sonnet (writing/reasoning/"
    "code) | Opus (hard synthesis - still a sub-agent, not inline). "
    "(3) Hand off by file: give the sub-agent an output path; it returns a "
    "pointer + short summary, never a full dump back into your context. "
    "Stay inline only when it's small, conversational, needs this "
    "conversation's live context, or is your own framing/synthesis - not "
    "merely because it's hard. "
    "Full rubric: CLAUDE.md -> Orchestrator-First Working Model."
)


def main() -> None:
    print(REMINDER)


if __name__ == "__main__":
    main()
