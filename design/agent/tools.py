"""
tools.py

Tool definitions for the dependency usage agent:
- rg_search: ripgrep-based code search
- read_file_chunk: read file slices
"""

from __future__ import annotations

import base64
import json
import os
import subprocess
from pathlib import Path
from typing import Any, Dict, List

from agents import function_tool


def _ensure_text(maybe_text_or_bytes: Dict[str, str]) -> str:
    """Decode ripgrep's 'text' or 'bytes' field into a Python str."""
    if "text" in maybe_text_or_bytes and maybe_text_or_bytes["text"] is not None:
        return maybe_text_or_bytes["text"]
    if "bytes" in maybe_text_or_bytes and maybe_text_or_bytes["bytes"] is not None:
        try:
            return base64.b64decode(maybe_text_or_bytes["bytes"]).decode(
                "utf-8", errors="replace"
            )
        except Exception:
            return ""
    return ""


# Limits to prevent context overflow
MAX_LINE_LENGTH = 500  # Truncate individual lines
MAX_TOTAL_OUTPUT_CHARS = 100_000  # ~100KB cap on tool output


@function_tool
def rg_search(
    pattern: str,
    root: str,
    max_matches: int = 200,
    include_hidden: bool = False,
) -> Dict[str, Any]:
    """
    Run ripgrep in JSON mode to find occurrences of `pattern` under `root`.

    Args:
        pattern: The text or regex to search for (e.g. an import path like 'github.com/google/uuid').
        root: Absolute or relative path to the repo root to search in.
        max_matches: Maximum number of match events to surface. This is a hard cap.
        include_hidden: If True, also search hidden files and directories (those starting with '.').
                       Use this when searching for config files, git hooks (.husky/), or other
                       dotfiles that might reference or use the dependency.

    Behavior:
        - Uses `rg --json -n` so we can parse structured events.
        - Returns:
            {
                "pattern": str,
                "root": str,
                "total_matches_seen": int,  # from ripgrep stats
                "hit_max_count": bool,      # True if we likely truncated via --max-count
                "matches": [
                    {
                        "file": "path/to/file.go",
                        "line": 123,
                        "matched_text": "the full line where the match occurred"
                    },
                    ...
                ]
            }

        - The model can use:
            - matches[*].file to understand breadth across directories
            - matches[*].line to call read_file_chunk for more context
            - total_matches_seen + hit_max_count to reason about pervasiveness

    Notes:
        - This tool does NOT hide ripgrep output via summarization. It only caps
          the number of match events returned to prevent unbounded growth.
        - If ripgrep is not installed or fails, we raise a RuntimeError so the
          agent can see an error message.
    """
    root_path = Path(root).expanduser().resolve()
    if not root_path.exists():
        raise RuntimeError(f"rg_search: root path does not exist: {root_path}")

    cmd = [
        "rg",
        "--json",
        "--no-messages",
        "-n",  # show line numbers
        f"--max-count={max_matches}",
    ]

    if include_hidden:
        cmd.append("--hidden")

    cmd.extend([pattern, str(root_path)])

    try:
        proc = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )
    except FileNotFoundError:
        raise RuntimeError(
            "ripgrep (rg) not found on PATH. Please install ripgrep and try again."
        )

    matches: List[Dict[str, Any]] = []
    total_matches_seen = 0
    hit_max_count = False
    output_truncated = False
    estimated_output_size = 0

    for line in proc.stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue

        typ = obj.get("type")
        data = obj.get("data", {})

        if typ == "match":
            # Check if we've exceeded output size limit
            if estimated_output_size >= MAX_TOTAL_OUTPUT_CHARS:
                output_truncated = True
                continue

            # Extract file path, line number, matched line text.
            path_obj = data.get("path", {})
            file_path = _ensure_text(path_obj)

            line_number = data.get("line_number")
            line_text = _ensure_text(data.get("lines", {})).strip()

            # Truncate long lines to prevent context overflow
            if len(line_text) > MAX_LINE_LENGTH:
                line_text = line_text[:MAX_LINE_LENGTH] + "...[truncated]"

            rel_path = os.path.relpath(file_path, root_path)
            match_entry = {
                "file": rel_path,
                "line": int(line_number) if line_number is not None else None,
                "matched_text": line_text,
            }
            matches.append(match_entry)

            # Estimate size contribution of this match
            estimated_output_size += len(rel_path) + len(line_text) + 50  # overhead for JSON structure

        elif typ == "summary":
            stats = data.get("stats", {})
            # 'matches' is the number of matches ripgrep saw before stopping.
            total_matches_seen = int(stats.get("matches", 0))
            # If total_matches_seen equals max_matches, we *probably* hit the cap.
            if total_matches_seen >= max_matches:
                hit_max_count = True

    # In practice, ripgrep may exit with code 0 when matches are found.
    # We tolerate non-zero exit if we still got some matches or a summary.
    return {
        "pattern": pattern,
        "root": str(root_path),
        "total_matches_seen": total_matches_seen,
        "hit_max_count": hit_max_count,
        "output_truncated": output_truncated,
        "matches_returned": len(matches),
        "matches": matches,
        "stderr": proc.stderr.strip() or None,
    }


@function_tool
def read_file_chunk(
    path: str,
    root: str,
    start_line: int,
    end_line: int,
    max_lines: int = 200,
) -> Dict[str, Any]:
    """
    Read a slice of a file as plain text.

    Args:
        path: File path, relative or absolute.
        root: Repo root to resolve relative paths against.
        start_line: 1-based inclusive start line.
        end_line: 1-based inclusive end line.
        max_lines: Hard cap on number of lines returned, to avoid huge chunks.

    Returns:
        {
            "file": str,
            "start_line": int,
            "end_line": int,   # may be clamped by file length or max_lines
            "text": str        # joined lines with newlines
        }
    """
    root_path = Path(root).expanduser().resolve()
    full_path = (root_path / path).resolve() if not os.path.isabs(path) else Path(path)

    if not full_path.exists():
        raise RuntimeError(f"read_file_chunk: file does not exist: {full_path}")

    if start_line < 1:
        start_line = 1
    if end_line < start_line:
        end_line = start_line

    # Clamp by max_lines
    if end_line - start_line + 1 > max_lines:
        end_line = start_line + max_lines - 1

    lines: List[str]
    with full_path.open("r", encoding="utf-8", errors="replace") as f:
        lines = f.readlines()

    # Adjust end_line if file is shorter
    num_lines = len(lines)
    truncated = False
    if start_line > num_lines:
        text = ""
        effective_end = start_line
    else:
        effective_end = min(end_line, num_lines)
        # lines index is 0-based, start_line/end_line are 1-based
        selected_lines = lines[start_line - 1 : effective_end]

        # Truncate individual long lines
        processed_lines = []
        for ln in selected_lines:
            if len(ln) > MAX_LINE_LENGTH:
                processed_lines.append(ln[:MAX_LINE_LENGTH] + "...[truncated]\n")
                truncated = True
            else:
                processed_lines.append(ln)

        text = "".join(processed_lines)

        # Cap total output size
        if len(text) > MAX_TOTAL_OUTPUT_CHARS:
            text = text[:MAX_TOTAL_OUTPUT_CHARS] + "\n...[output truncated at 100KB]"
            truncated = True

    return {
        "file": os.path.relpath(full_path, root_path),
        "start_line": start_line,
        "end_line": effective_end,
        "truncated": truncated,
        "text": text,
    }
