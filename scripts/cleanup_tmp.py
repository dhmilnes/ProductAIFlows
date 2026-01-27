#!/usr/bin/env python3
"""
Clean up files in tmp/ older than 24 hours.
Called by Claude Code SessionStart hook.
"""

import os
import time
from pathlib import Path

# Project root is parent of scripts/
PROJECT_ROOT = Path(__file__).parent.parent
TMP_DIR = PROJECT_ROOT / "tmp"

# 24 hours in seconds
MAX_AGE_SECONDS = 24 * 60 * 60


def cleanup():
    if not TMP_DIR.exists():
        return

    now = time.time()
    deleted = 0

    for file_path in TMP_DIR.rglob("*"):
        if file_path.is_file():
            age = now - file_path.stat().st_mtime
            if age > MAX_AGE_SECONDS:
                try:
                    file_path.unlink()
                    deleted += 1
                except Exception:
                    pass  # Skip files that can't be deleted

    if deleted > 0:
        print(f"Cleaned up {deleted} file(s) from tmp/")


if __name__ == "__main__":
    cleanup()
