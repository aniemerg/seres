import json
from pathlib import Path

from src.simulation.provenance import (
    ensure_provenance,
    provenance_mismatches,
    verify_provenance,
)


def _provenance(**overrides):
    data = {
        "format_version": 1,
        "seres_commit": "seres-a",
        "seres_dirty": False,
        "content_commit": "content-a",
        "kb_tree": "tree-a",
        "kb_dirty": False,
    }
    data.update(overrides)
    return data


def test_content_commit_can_change_when_kb_tree_is_unchanged() -> None:
    saved = _provenance(content_commit="content-a")
    current = _provenance(content_commit="content-b")

    assert provenance_mismatches(saved, current) == []


def test_kb_tree_change_is_incompatible() -> None:
    mismatches = provenance_mismatches(
        _provenance(),
        _provenance(kb_tree="tree-b"),
    )

    assert mismatches == ["KB tree changed (tree-a -> tree-b)"]


def test_source_commit_and_cleanliness_are_checked() -> None:
    mismatches = provenance_mismatches(
        _provenance(),
        _provenance(seres_commit="seres-b", kb_dirty=True),
    )

    assert "SERES commit changed (seres-a -> seres-b)" in mismatches
    assert "KB now has uncommitted changes" in mismatches


def test_legacy_simulation_without_provenance_still_loads(tmp_path: Path) -> None:
    verify_provenance(tmp_path, tmp_path / "kb")


def test_ensure_provenance_does_not_replace_existing_file(tmp_path: Path) -> None:
    provenance_path = tmp_path / "provenance.json"
    provenance_path.write_text(json.dumps({"sentinel": True}), encoding="utf-8")

    ensure_provenance(tmp_path, tmp_path / "kb")

    assert json.loads(provenance_path.read_text(encoding="utf-8")) == {
        "sentinel": True
    }
