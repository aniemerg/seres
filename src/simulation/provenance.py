"""Commit-based provenance for reproducible simulation runs."""
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any, Optional

from src.paths import REPO_ROOT


PROVENANCE_FILENAME = "provenance.json"
PROVENANCE_FORMAT_VERSION = 1


class ProvenanceMismatchError(ValueError):
    """Raised when a simulation is opened with incompatible source content."""


def _git(path: Path, *args: str) -> Optional[str]:
    try:
        result = subprocess.run(
            ["git", "-C", str(path), *args],
            check=True,
            capture_output=True,
            text=True,
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        return None
    return result.stdout.strip()


def _git_dirty(repo_root: Path, pathspec: Optional[str] = None) -> Optional[bool]:
    args = ["status", "--porcelain", "--untracked-files=normal"]
    if pathspec:
        args.extend(["--", pathspec])
    status = _git(repo_root, *args)
    return None if status is None else bool(status)


def _repository_url(repo_root: Path) -> Optional[str]:
    return _git(repo_root, "remote", "get-url", "origin")


def _content_metadata(kb_root: Path) -> dict[str, Any]:
    content_repo_text = _git(kb_root, "rev-parse", "--show-toplevel")
    if content_repo_text is None:
        return {
            "content_repository": None,
            "content_commit": None,
            "kb_tree": None,
            "kb_dirty": None,
        }

    content_repo = Path(content_repo_text)
    try:
        kb_relative = kb_root.resolve().relative_to(content_repo.resolve())
    except ValueError:
        kb_relative = Path("kb")

    return {
        "content_repository": _repository_url(content_repo),
        "content_commit": _git(content_repo, "rev-parse", "HEAD"),
        "kb_tree": _git(content_repo, "rev-parse", f"HEAD:{kb_relative.as_posix()}"),
        "kb_dirty": _git_dirty(content_repo, kb_relative.as_posix()),
    }


def capture_provenance(kb_root: Path) -> dict[str, Any]:
    """Capture the engine commit and the selected content/KB commit."""
    data: dict[str, Any] = {
        "format_version": PROVENANCE_FORMAT_VERSION,
        "seres_repository": _repository_url(REPO_ROOT),
        "seres_commit": _git(REPO_ROOT, "rev-parse", "HEAD"),
        # Ignore the submodule worktree here; KB cleanliness is checked below,
        # and simulation output may legitimately make the submodule dirty.
        "seres_dirty": _git_dirty(REPO_ROOT, ":(exclude)content"),
        **_content_metadata(kb_root),
        "runbook": None,
    }
    data["reproducible"] = bool(
        data["seres_commit"]
        and data["content_commit"]
        and data["kb_tree"]
        and data["seres_dirty"] is False
        and data["kb_dirty"] is False
    )
    return data


def provenance_mismatches(saved: dict[str, Any], current: dict[str, Any]) -> list[str]:
    """Return source incompatibilities between saved and current provenance."""
    mismatches: list[str] = []

    saved_seres = saved.get("seres_commit")
    current_seres = current.get("seres_commit")
    if saved_seres and current_seres and saved_seres != current_seres:
        mismatches.append(f"SERES commit changed ({saved_seres} -> {current_seres})")

    saved_tree = saved.get("kb_tree")
    current_tree = current.get("kb_tree")
    if saved_tree and current_tree:
        if saved_tree != current_tree:
            mismatches.append(f"KB tree changed ({saved_tree} -> {current_tree})")
    else:
        saved_content = saved.get("content_commit")
        current_content = current.get("content_commit")
        if saved_content and current_content and saved_content != current_content:
            mismatches.append(
                f"content commit changed ({saved_content} -> {current_content})"
            )

    if saved.get("seres_dirty") is False and current.get("seres_dirty") is True:
        mismatches.append("SERES source now has uncommitted changes")
    if saved.get("kb_dirty") is False and current.get("kb_dirty") is True:
        mismatches.append("KB now has uncommitted changes")

    return mismatches


def ensure_provenance(sim_dir: Path, kb_root: Path) -> Path:
    """Create provenance for a simulation if it does not already exist."""
    provenance_path = sim_dir / PROVENANCE_FILENAME
    if provenance_path.exists():
        return provenance_path

    provenance_path.write_text(
        json.dumps(capture_provenance(kb_root), indent=2) + "\n",
        encoding="utf-8",
    )
    return provenance_path


def verify_provenance(sim_dir: Path, kb_root: Path) -> None:
    """Fail when a recorded simulation is opened with incompatible sources."""
    provenance_path = sim_dir / PROVENANCE_FILENAME
    if not provenance_path.exists():
        return

    saved = json.loads(provenance_path.read_text(encoding="utf-8"))
    mismatches = provenance_mismatches(saved, capture_provenance(kb_root))
    if mismatches:
        details = "; ".join(mismatches)
        raise ProvenanceMismatchError(
            f"Simulation provenance mismatch: {details}. "
            "Check out the recorded commits before resuming this simulation."
        )


def record_runbook(sim_dir: Path, runbook_path: Path) -> None:
    """Attach an exact runbook path and SHA-256 digest to existing provenance."""
    provenance_path = sim_dir / PROVENANCE_FILENAME
    if not provenance_path.exists():
        return

    resolved = runbook_path.resolve()
    try:
        stored_path = str(resolved.relative_to(REPO_ROOT))
    except ValueError:
        stored_path = str(resolved)
    data = json.loads(provenance_path.read_text(encoding="utf-8"))
    data["runbook"] = {
        "path": stored_path,
        "sha256": hashlib.sha256(resolved.read_bytes()).hexdigest(),
    }
    provenance_path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
