from pathlib import Path

from scripts.audit_machines import (
    compile_exclusion_patterns,
    is_excluded,
    merge_trust_tags,
    selection_status,
    update_trust_tags_text,
)


def test_machine_exclusion_patterns_are_explicit_and_case_insensitive():
    patterns = compile_exclusion_patterns([r"^prototype_", r"private project"])

    assert is_excluded("prototype_lathe", {}, Path("items/machines/lathe.yaml"), patterns)
    assert is_excluded(
        "lathe_v0",
        {"name": "Private Project Lathe"},
        Path("items/machines/lathe.yaml"),
        patterns,
    )
    assert not is_excluded("production_lathe", {}, Path("items/machines/lathe.yaml"), patterns)


def test_excluded_machine_has_distinct_selection_status():
    status = selection_status(
        excluded=True,
        audit_tags=[],
        evidence=["functional_notes"],
        mismatches=[],
        resource_use_count=1,
    )

    assert status == "excluded_by_pattern"


def test_update_trust_tags_preserves_non_audit_content():
    original = "id: mill_v0\nnotes: General mill.\ntrust_tags:\n- old_tag\n"

    updated = update_trust_tags_text(original, ["machine_audit_imported"])

    assert "notes: General mill." in updated
    assert "- machine_audit_imported" in updated
    assert "- old_tag" not in updated


def test_excluded_machine_preserves_existing_trust_tags():
    existing = ["owner_reviewed", "machine_audit_placeholder"]

    assert merge_trust_tags(existing, [], excluded=True) == existing
