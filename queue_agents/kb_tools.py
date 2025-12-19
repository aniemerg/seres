"""
kb_tools.py

Tool definitions for the autonomous queue agent:
- rg_search: ripgrep-based search
- read_file: read complete files
- write_file: write/overwrite files with diff output
- run_indexer: validate changes
- queue_release: give up on an item
"""
from __future__ import annotations

import base64
import json
import os
import subprocess
from pathlib import Path
from typing import Any, Dict, List

from agents import function_tool


# Repo root
REPO_ROOT = Path(__file__).parent.parent
KB_ROOT = REPO_ROOT / "kb"
VENV_PYTHON = REPO_ROOT / ".venv" / "bin" / "python"

# Limits to prevent context overflow
MAX_LINE_LENGTH = 500
MAX_TOTAL_OUTPUT_CHARS = 100_000


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


@function_tool
def rg_search(
    pattern: str,
    path: str = ".",
    max_matches: int = 200,
) -> Dict[str, Any]:
    """
    Search the repository using ripgrep.

    Args:
        pattern: The text or regex to search for (e.g., "ball_mill", "material_class")
        path: Path to search within (relative to repo root, default "." for all)
        max_matches: Maximum number of matches to return (default 200)

    Returns:
        {
            "pattern": str,
            "path": str,
            "total_matches_seen": int,
            "hit_max_count": bool,
            "matches": [
                {"file": "kb/items/machines/foo.yaml", "line": 15, "matched_text": "..."},
                ...
            ]
        }
    """
    search_path = REPO_ROOT / path
    if not search_path.exists():
        return {
            "error": f"Path does not exist: {search_path}",
            "pattern": pattern,
            "path": str(search_path),
            "matches": [],
        }

    cmd = [
        "rg",
        "--json",
        "--no-messages",
        "-n",
        f"--max-count={max_matches}",
        pattern,
        str(search_path),
    ]

    try:
        proc = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )
    except FileNotFoundError:
        return {
            "error": "ripgrep (rg) not found. Please install ripgrep.",
            "pattern": pattern,
            "path": str(search_path),
            "matches": [],
        }

    matches: List[Dict[str, Any]] = []
    total_matches_seen = 0
    hit_max_count = False

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
            path_obj = data.get("path", {})
            file_path = _ensure_text(path_obj)
            line_number = data.get("line_number")
            line_text = _ensure_text(data.get("lines", {})).strip()

            if len(line_text) > MAX_LINE_LENGTH:
                line_text = line_text[:MAX_LINE_LENGTH] + "...[truncated]"

            rel_path = os.path.relpath(file_path, REPO_ROOT)
            matches.append({
                "file": rel_path,
                "line": int(line_number) if line_number is not None else None,
                "matched_text": line_text,
            })

        elif typ == "summary":
            stats = data.get("stats", {})
            total_matches_seen = int(stats.get("matches", 0))
            if total_matches_seen >= max_matches:
                hit_max_count = True

    return {
        "pattern": pattern,
        "path": str(search_path.relative_to(REPO_ROOT)),
        "total_matches_seen": total_matches_seen,
        "hit_max_count": hit_max_count,
        "matches_returned": len(matches),
        "matches": matches,
    }


@function_tool
def read_file(path: str) -> Dict[str, Any]:
    """
    Read a file from the repository.

    Args:
        path: Path relative to repo root (e.g., "kb/items/machines/ball_mill_v0.yaml")

    Returns:
        {
            "path": str,
            "exists": bool,
            "content": str,  # File contents (or error message if not found)
            "size": int,     # Size in characters
            "lines": int,    # Number of lines
        }
    """
    file_path = REPO_ROOT / path

    # Security: ensure path is within repo
    try:
        file_path = file_path.resolve()
        file_path.relative_to(REPO_ROOT)
    except (ValueError, RuntimeError):
        return {
            "path": path,
            "exists": False,
            "error": "Path is outside repository",
        }

    if not file_path.exists():
        return {
            "path": path,
            "exists": False,
            "error": "File does not exist",
        }

    try:
        content = file_path.read_text(encoding="utf-8")

        # Cap total output
        if len(content) > MAX_TOTAL_OUTPUT_CHARS:
            content = content[:MAX_TOTAL_OUTPUT_CHARS] + "\n...[truncated at 100KB]"

        return {
            "path": path,
            "exists": True,
            "content": content,
            "size": len(content),
            "lines": content.count("\n") + 1,
        }
    except Exception as e:
        return {
            "path": path,
            "exists": True,
            "error": f"Failed to read file: {e}",
        }


@function_tool
def write_file(path: str, content: str) -> Dict[str, Any]:
    """
    Write or overwrite a file in the repository.

    Args:
        path: Path relative to repo root (e.g., "kb/items/materials/new_material.yaml")
        content: File contents to write

    Returns:
        {
            "path": str,
            "action": "created" | "updated",
            "size": int,
            "diff": str,  # Git-style diff if file existed
        }
    """
    file_path = REPO_ROOT / path

    # Security: ensure path is within repo
    try:
        file_path = file_path.resolve()
        file_path.relative_to(REPO_ROOT)
    except (ValueError, RuntimeError):
        return {
            "path": path,
            "error": "Path is outside repository",
            "success": False,
        }

    # Check if file exists
    existed = file_path.exists()
    old_content = None
    if existed:
        try:
            old_content = file_path.read_text(encoding="utf-8")
        except Exception:
            old_content = None

    # Write file
    try:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(content, encoding="utf-8")
    except Exception as e:
        return {
            "path": path,
            "error": f"Failed to write file: {e}",
            "success": False,
        }

    result = {
        "path": path,
        "action": "updated" if existed else "created",
        "size": len(content),
        "success": True,
    }

    # Generate diff if file existed
    if existed and old_content is not None:
        diff = _generate_diff(path, old_content, content)
        result["diff"] = diff

    return result


def _generate_diff(path: str, old: str, new: str) -> str:
    """Generate a simple unified diff."""
    import difflib

    old_lines = old.splitlines(keepends=True)
    new_lines = new.splitlines(keepends=True)

    diff_lines = difflib.unified_diff(
        old_lines,
        new_lines,
        fromfile=f"a/{path}",
        tofile=f"b/{path}",
        lineterm="",
    )

    return "".join(diff_lines)


@function_tool
def run_indexer() -> Dict[str, Any]:
    """
    Run the KB indexer to validate changes.

    Returns:
        {
            "success": bool,       # True if indexer completed without hard errors
            "exit_code": int,
            "output": str,         # Full stdout
            "errors": [str],       # List of error messages (empty if success)
            "warnings": [str],     # List of warning messages
            "summary": str,        # Brief summary of results
            "gap_count": int,      # Total gaps in work queue
        }
    """
    cmd = [str(VENV_PYTHON), "-m", "kbtool", "index"]

    try:
        proc = subprocess.run(
            cmd,
            cwd=str(REPO_ROOT),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )
    except Exception as e:
        return {
            "success": False,
            "error": f"Failed to run indexer: {e}",
            "exit_code": -1,
            "errors": [str(e)],
            "warnings": [],
        }

    output = proc.stdout
    stderr = proc.stderr

    # Parse output for errors and warnings
    errors = []
    warnings = []
    gap_count = 0

    for line in output.splitlines():
        line_lower = line.lower()
        if "error" in line_lower and "0 errors" not in line_lower:
            errors.append(line.strip())
        if "warning" in line_lower:
            warnings.append(line.strip())
        if "gaps" in line_lower or "gap" in line_lower:
            # Try to extract gap count
            import re
            match = re.search(r'(\d+)\s+gaps?', line)
            if match:
                gap_count = int(match.group(1))

    # Parse stderr for errors
    if stderr:
        for line in stderr.splitlines():
            if line.strip():
                errors.append(line.strip())

    # Determine success
    success = proc.returncode == 0 and len(errors) == 0

    # Generate summary
    summary_lines = []
    for line in output.splitlines():
        if "processed" in line.lower() or "total" in line.lower() or "gaps" in line.lower():
            summary_lines.append(line.strip())
    summary = " | ".join(summary_lines[:3]) if summary_lines else "Indexer completed"

    return {
        "success": success,
        "exit_code": proc.returncode,
        "output": output,
        "errors": errors,
        "warnings": warnings,
        "summary": summary,
        "gap_count": gap_count,
    }


@function_tool
def queue_release(item_id: str, agent_name: str) -> Dict[str, Any]:
    """
    Release a leased queue item back to pending status.

    Use this when you cannot resolve a gap and want to give up.

    Args:
        item_id: The queue item ID (e.g., "missing_field:ball_mill_v0")
        agent_name: Your agent name

    Returns:
        {
            "success": bool,
            "message": str,
        }
    """
    cmd = [
        str(VENV_PYTHON),
        "-m",
        "kbtool",
        "queue",
        "release",
        "--id",
        item_id,
        "--agent",
        agent_name,
    ]

    try:
        proc = subprocess.run(
            cmd,
            cwd=str(REPO_ROOT),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )

        if proc.returncode == 0:
            return {
                "success": True,
                "message": f"Released {item_id}",
                "output": proc.stdout,
            }
        else:
            return {
                "success": False,
                "message": f"Failed to release {item_id}",
                "error": proc.stderr or proc.stdout,
            }
    except Exception as e:
        return {
            "success": False,
            "message": f"Failed to release {item_id}",
            "error": str(e),
        }
