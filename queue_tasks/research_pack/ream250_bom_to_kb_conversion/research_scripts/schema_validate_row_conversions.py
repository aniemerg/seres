#!/usr/bin/env python3
"""Validate reAM250 BOM-to-KB conversion task outputs."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any

import yaml


REPO_ROOT = Path(__file__).resolve().parents[4]
ROW_HEADING = "## KB Conversion"
BASELINE_HASHES = Path("research/ream250_bom/kb_conversion/baseline_hashes.json")

CONVERSION_STATUS = {"row_reviewed", "not_applicable", "needs_human"}
DECOMPOSITION_DECISIONS = {
    "simple_part",
    "complex_module",
    "decompose_into_parts",
    "needs_human",
}
SUBSTITUTION_DECISIONS = {
    "keep_original_family",
    "substitute_process_family",
    "add_post_processing",
    "not_applicable",
    "needs_human",
}
CANONICAL_PROCESS_FAMILIES = {
    "general_metal_additive_with_finish_machining",
    "general_subtractive_machining",
    "sheet_plate_cutting_drilling",
    "structural_profile_stock_fabrication_cutting",
    "polymer_elastomer_forming_dispensing",
    "manual_assembly_with_general_tools",
    "fastener_forming_thread_rolling",
    "plumbing_connector_fabrication_testing",
    "precision_component_import_decompose_later",
    "not_applicable",
    "needs_human",
}
SUPPORTING_PROCESS_TYPES = {
    "stock_preparation",
    "cutting",
    "drilling",
    "deburring",
    "precision_machining",
    "thread_forming",
    "gear_tooth_machining",
    "surface_finishing",
    "grinding_lapping",
    "heat_treatment",
    "forming",
    "extrusion",
    "additive_build",
    "support_removal",
    "joining",
    "cleaning",
    "leak_testing",
    "pressure_testing",
    "dimensional_inspection",
    "calibration",
    "coating",
    "curing",
    "elastomer_forming",
    "assembly",
    "ceramic_forming",
    "ceramic_sintering",
    "decomposition_required",
    "import_assumption",
}
CANDIDATE_PROCESS_FITS = {"direct", "partial", "supporting", "poor_fit"}
MERGE_DECISIONS = {"merge", "split", "partial_merge", "needs_human"}
PHASE3_STAGE_STATUS = {"pilot_only", "ready_for_review", "needs_human"}
PHASE3_ACTIONS = {"reuse_existing", "create_new", "defer"}
PHASE3_IMPORT_LOCAL_DECISIONS = {
    "import",
    "local_manufacture",
    "local_manufacture_candidate_with_recipe_gap",
    "local_manufacture_candidate_with_precision_guardrails",
    "reuse_existing_local_recipe",
    "needs_human",
}
FUNCTION_KEY_FORBIDDEN_RE = re.compile(
    r"(^|_)(aluminum|aluminium|steel|stainless|copper|glass|ceramic|polymer|"
    r"silicone|rubber|machining|cutting|extrusion|additive|printing|casting|"
    r"welding|sheet|plate|profile|tube|bar|rod|bracket|flange|gasket|seal|"
    r"tiny|small|medium|large|heavy)(_|$)|\d+\s*x\s*\d+|\d+mm|\d+kg",
    re.IGNORECASE,
)
VACUUM_KEY_RE = re.compile(r"(^|_)(vacuum|iso_k|iso_kf|kf)(_|$)", re.IGNORECASE)
AMBIGUOUS_OR_RE = re.compile(r"(^|_)or(_|$)|\bor\b", re.IGNORECASE)


def repo_relative(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def normalize_pre_section(text: str) -> str:
    return text.rstrip() + "\n"


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_baseline_hashes() -> dict[str, str]:
    path = REPO_ROOT / BASELINE_HASHES
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"baseline hash file must contain a mapping: {path}")
    return {str(k): str(v) for k, v in data.items()}


def load_process_ids() -> set[str]:
    ids: set[str] = set()
    for path in (REPO_ROOT / "kb/processes").glob("*.yaml"):
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        except Exception:
            continue
        if isinstance(data, dict) and data.get("id"):
            ids.add(str(data["id"]))
    return ids


def split_kb_conversion(text: str) -> tuple[str, str]:
    pattern = re.compile(rf"(?m)^{re.escape(ROW_HEADING)}\s*$")
    matches = list(pattern.finditer(text))
    if not matches:
        raise ValueError(f"missing {ROW_HEADING!r} section")
    if len(matches) > 1:
        raise ValueError(f"multiple {ROW_HEADING!r} sections found")
    match = matches[0]
    return text[: match.start()], text[match.start() :]


def parse_fenced_yaml(section: str) -> dict[str, Any]:
    match = re.search(r"```yaml\s*\n(.*?)\n```", section, flags=re.DOTALL)
    if not match:
        raise ValueError("KB Conversion section must contain one fenced ```yaml block")
    data = yaml.safe_load(match.group(1)) or {}
    if not isinstance(data, dict):
        raise ValueError("fenced YAML must be a mapping")
    return data


def load_markdown_frontmatter(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"merge review must start with YAML frontmatter: {path}")
    end = text.find("\n---", 4)
    if end == -1:
        raise ValueError(f"frontmatter is not closed: {path}")
    data = yaml.safe_load(text[4:end]) or {}
    if not isinstance(data, dict):
        raise ValueError("frontmatter must be a mapping")
    return data


def require_mapping(data: dict[str, Any], key: str, issues: list[str]) -> dict[str, Any]:
    value = data.get(key)
    if not isinstance(value, dict):
        issues.append(f"missing required object: {key}")
        return {}
    return value


def require_list(data: dict[str, Any], key: str, issues: list[str]) -> list[Any]:
    value = data.get(key)
    if not isinstance(value, list):
        issues.append(f"missing required list: {key}")
        return []
    return value


def require_nonempty(data: dict[str, Any], key: str, issues: list[str], prefix: str = "") -> Any:
    value = data.get(key)
    if value in (None, ""):
        issues.append(f"missing required field: {prefix}{key}")
    return value


def find_ambiguous_or_values(value: Any, path: str = "") -> list[str]:
    issues: list[str] = []
    if isinstance(value, str):
        if AMBIGUOUS_OR_RE.search(value):
            issues.append(path or "<root>")
    elif isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}" if path else str(key)
            issues.extend(find_ambiguous_or_values(child, child_path))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            child_path = f"{path}[{index}]"
            issues.extend(find_ambiguous_or_values(child, child_path))
    return issues


def validate_conversion_file(path: Path) -> list[str]:
    issues: list[str] = []
    text = path.read_text(encoding="utf-8")
    rel = repo_relative(path)

    try:
        pre, section = split_kb_conversion(text)
        data = parse_fenced_yaml(section)
    except Exception as exc:
        return [str(exc)]

    baselines = load_baseline_hashes()
    expected_hash = baselines.get(rel)
    actual_hash = sha256_text(normalize_pre_section(pre))
    if expected_hash is None:
        issues.append(f"no baseline hash found for {rel}; regenerate row conversion tasks first")
    elif actual_hash != expected_hash:
        issues.append("content before ## KB Conversion changed from baseline")

    required_top = [
        "conversion_status",
        "source_research_file",
        "source_research_sha256",
        "evidence_reviewed",
        "decomposition",
        "process_abstraction",
        "identity_for_merge",
        "merge_pool",
        "downstream_decision_inputs",
        "kb_staging",
        "assumptions",
        "unresolved",
    ]
    for key in required_top:
        if key not in data:
            issues.append(f"missing required top-level field: {key}")
    if "lunarized_process_substitution" in data:
        issues.append("use process_abstraction, not lunarized_process_substitution")

    ambiguous_paths = find_ambiguous_or_values(data)
    if ambiguous_paths:
        issues.append(
            "conversion values must not use standalone 'or' or '_or_': "
            + ", ".join(ambiguous_paths[:12])
            + (" ..." if len(ambiguous_paths) > 12 else "")
        )

    if data.get("conversion_status") not in CONVERSION_STATUS:
        issues.append(f"conversion_status must be one of {sorted(CONVERSION_STATUS)}")
    if data.get("source_research_file") != rel:
        issues.append(f"source_research_file must be {rel!r}")
    if expected_hash and data.get("source_research_sha256") != expected_hash:
        issues.append("source_research_sha256 must match baseline hash")

    evidence = require_mapping(data, "evidence_reviewed", issues)
    if evidence:
        sections = require_list(evidence, "original_research_sections", issues)
        required_sections = {"function", "mass", "material", "how_to_make", "kb_implications"}
        if not required_sections.issubset({str(section) for section in sections}):
            issues.append(
                "evidence_reviewed.original_research_sections must include "
                "function, mass, material, how_to_make, and kb_implications"
            )
        if not isinstance(evidence.get("geometry_evidence_used"), bool):
            issues.append("evidence_reviewed.geometry_evidence_used must be boolean")
        require_nonempty(evidence, "notes", issues, "evidence_reviewed.")

    decomposition = require_mapping(data, "decomposition", issues)
    if decomposition:
        if decomposition.get("decision") not in DECOMPOSITION_DECISIONS:
            issues.append(f"decomposition.decision must be one of {sorted(DECOMPOSITION_DECISIONS)}")
        require_nonempty(decomposition, "rationale", issues, "decomposition.")
        require_list(decomposition, "proposed_subparts", issues)

    process = require_mapping(data, "process_abstraction", issues)
    if process:
        require_nonempty(process, "original_process_family", issues, "process_abstraction.")
        primary_bucket = require_nonempty(
            process,
            "primary_process_bucket",
            issues,
            "process_abstraction.",
        )
        if primary_bucket and primary_bucket not in CANONICAL_PROCESS_FAMILIES:
            issues.append(
                "process_abstraction.primary_process_bucket must be one "
                f"of canonical process buckets: {sorted(CANONICAL_PROCESS_FAMILIES)}"
            )
        if isinstance(primary_bucket, str) and AMBIGUOUS_OR_RE.search(primary_bucket):
            issues.append("process_abstraction.primary_process_bucket must not use 'or'")
        if process.get("abstraction_decision") not in SUBSTITUTION_DECISIONS:
            issues.append(
                "process_abstraction.abstraction_decision must be one of "
                f"{sorted(SUBSTITUTION_DECISIONS)}"
            )
        require_nonempty(process, "rationale", issues, "process_abstraction.")
        supporting = require_list(process, "supporting_processes", issues)
        for index, support in enumerate(supporting):
            if support not in SUPPORTING_PROCESS_TYPES:
                issues.append(
                    f"process_abstraction.supporting_processes[{index}] must be one of "
                    f"{sorted(SUPPORTING_PROCESS_TYPES)}"
                )
        candidates = require_list(process, "candidate_existing_processes", issues)
        process_ids = load_process_ids()
        for index, candidate in enumerate(candidates):
            if not isinstance(candidate, dict):
                issues.append(f"process_abstraction.candidate_existing_processes[{index}] must be an object")
                continue
            process_id = candidate.get("process_id")
            if process_id not in process_ids:
                issues.append(
                    f"process_abstraction.candidate_existing_processes[{index}].process_id "
                    f"must exist in kb/processes: {process_id!r}"
                )
            if candidate.get("fit") not in CANDIDATE_PROCESS_FITS:
                issues.append(
                    f"process_abstraction.candidate_existing_processes[{index}].fit must be one of "
                    f"{sorted(CANDIDATE_PROCESS_FITS)}"
                )
            require_nonempty(candidate, "reason", issues, f"process_abstraction.candidate_existing_processes[{index}].")
        checks = require_mapping(process, "process_guardrails", issues)
        for check in ("tolerance", "surface_finish", "sealing_quality", "alignment_accuracy"):
            if check not in checks:
                issues.append(f"missing process guardrail: {check}")
        if not isinstance(checks.get("blocked_by_precision"), bool):
            issues.append("process_abstraction.process_guardrails.blocked_by_precision must be boolean")

    identity = require_mapping(data, "identity_for_merge", issues)
    if identity:
        require_nonempty(identity, "functional_purpose", issues, "identity_for_merge.")
        require_nonempty(identity, "material", issues, "identity_for_merge.")
        require_nonempty(identity, "geometry_form", issues, "identity_for_merge.")
        scale = require_mapping(identity, "scale_or_capacity", issues)
        if scale:
            mass = scale.get("mass_kg")
            if mass is not None and not isinstance(mass, (int, float)):
                issues.append("identity_for_merge.scale_or_capacity.mass_kg must be numeric or null")
            require_nonempty(scale, "scale_class", issues, "identity_for_merge.scale_or_capacity.")

    merge_pool = require_mapping(data, "merge_pool", issues)
    if merge_pool:
        if not isinstance(merge_pool.get("eligible"), bool):
            issues.append("merge_pool.eligible must be boolean")
        if merge_pool.get("eligible") and not merge_pool.get("functional_purpose_key"):
            issues.append("merge_pool.functional_purpose_key is required when eligible is true")
        key = str(merge_pool.get("functional_purpose_key") or "")
        if key and FUNCTION_KEY_FORBIDDEN_RE.search(key):
            issues.append(
                "merge_pool.functional_purpose_key must be function-only; "
                "do not include material, process, geometry, dimensions, or mass class"
            )
        if key and VACUUM_KEY_RE.search(key):
            issues.append(
                "merge_pool.functional_purpose_key must not use vacuum-specific labels; "
                "use the ordinary function such as plumbing_connection, interface_clamping, "
                "and joint_clamping"
            )
        if key and AMBIGUOUS_OR_RE.search(key):
            issues.append("merge_pool.functional_purpose_key must not use 'or'")
        require_list(merge_pool, "precision_guardrails", issues)

    downstream = require_mapping(data, "downstream_decision_inputs", issues)
    if downstream:
        require_list(downstream, "local_manufacturing_paths_considered", issues)
        require_list(downstream, "import_risk_factors", issues)
        require_nonempty(
            downstream,
            "post_merge_decision_notes",
            issues,
            "downstream_decision_inputs.",
        )

    kb_staging = require_mapping(data, "kb_staging", issues)
    if kb_staging:
        if "proposed_item_id" not in kb_staging:
            issues.append("missing required field: kb_staging.proposed_item_id")
        require_nonempty(kb_staging, "notes", issues, "kb_staging.")

    require_list(data, "assumptions", issues)
    require_list(data, "unresolved", issues)
    return issues


def validate_merge_review_file(path: Path) -> list[str]:
    issues: list[str] = []
    try:
        data = load_markdown_frontmatter(path)
    except Exception as exc:
        return [str(exc)]

    for key in [
        "group_id",
        "candidate_rows",
        "evidence_reviewed",
        "rough_match_basis",
        "merge_decision",
        "material_review",
        "process_review",
        "geometry_review",
        "precision_review",
        "assumptions",
        "unresolved",
    ]:
        if key not in data:
            issues.append(f"missing required top-level field: {key}")

    evidence = require_mapping(data, "evidence_reviewed", issues)
    if evidence:
        files_read = require_list(evidence, "original_research_files_read", issues)
        sections_read = require_list(evidence, "conversion_sections_read", issues)
        if len(files_read) < 2:
            issues.append("evidence_reviewed.original_research_files_read must list every candidate row file")
        if len(sections_read) < 2:
            issues.append("evidence_reviewed.conversion_sections_read must list every candidate row conversion section")
        require_nonempty(evidence, "notes", issues, "evidence_reviewed.")

    rows = require_list(data, "candidate_rows", issues)
    if len(rows) < 2:
        issues.append("candidate_rows must contain at least two rows")
    for idx, row in enumerate(rows):
        if not isinstance(row, dict):
            issues.append(f"candidate_rows[{idx}] must be an object")
            continue
        for field in ("source_row_number", "item", "path", "conversion_section_present"):
            if field not in row:
                issues.append(f"candidate_rows[{idx}] missing {field}")
        if row.get("conversion_section_present") is not True:
            issues.append(f"candidate_rows[{idx}].conversion_section_present must be true")

    basis = require_mapping(data, "rough_match_basis", issues)
    if basis:
        require_nonempty(basis, "functional_purpose_key", issues, "rough_match_basis.")
        window = basis.get("mass_window_kg")
        if not isinstance(window, list) or len(window) != 2:
            issues.append("rough_match_basis.mass_window_kg must be [low, high]")

    decision = require_mapping(data, "merge_decision", issues)
    if decision:
        if decision.get("decision") not in MERGE_DECISIONS:
            issues.append(f"merge_decision.decision must be one of {sorted(MERGE_DECISIONS)}")
        require_nonempty(decision, "rationale", issues, "merge_decision.")
        proposed = require_list(decision, "proposed_closure_items", issues)
        if decision.get("decision") in {"merge", "partial_merge"} and not proposed:
            issues.append("merge or partial_merge decisions require proposed_closure_items")

    for section_name in ("material_review", "process_review", "geometry_review"):
        section = require_mapping(data, section_name, issues)
        if section:
            if not isinstance(section.get("can_unify"), bool):
                issues.append(f"{section_name}.can_unify must be boolean")
            require_nonempty(section, "rationale", issues, f"{section_name}.")

    precision = require_mapping(data, "precision_review", issues)
    if precision:
        if not isinstance(precision.get("blocks_merge"), bool):
            issues.append("precision_review.blocks_merge must be boolean")
        require_nonempty(precision, "rationale", issues, "precision_review.")

    require_list(data, "assumptions", issues)
    require_list(data, "unresolved", issues)
    return issues


def load_yaml_file(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(data, dict):
        raise ValueError("YAML file must contain a mapping")
    return data


def source_rows_from_merge_review(path: Path) -> set[int]:
    data = load_markdown_frontmatter(path)
    rows = data.get("candidate_rows") or []
    source_rows: set[int] = set()
    if isinstance(rows, list):
        for row in rows:
            if isinstance(row, dict) and isinstance(row.get("source_row_number"), int):
                source_rows.add(row["source_row_number"])
    return source_rows


def kb_item_exists(item_id: str) -> bool:
    for root in ("kb/items", "kb/imports"):
        for path in (REPO_ROOT / root).rglob("*.yaml"):
            try:
                data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
            except Exception:
                continue
            if isinstance(data, dict) and data.get("id") == item_id:
                return True
    return False


def validate_phase3_stage_file(path: Path) -> list[str]:
    issues: list[str] = []
    try:
        data = load_yaml_file(path)
    except Exception as exc:
        return [str(exc)]

    for key in [
        "stage_id",
        "stage_status",
        "source_merge_review",
        "source_phase2_decision",
        "evidence_inputs",
        "proposed_items",
        "proposed_bom_mappings",
        "stage_findings",
        "unresolved",
    ]:
        if key not in data:
            issues.append(f"missing required top-level field: {key}")

    if data.get("stage_status") not in PHASE3_STAGE_STATUS:
        issues.append(f"stage_status must be one of {sorted(PHASE3_STAGE_STATUS)}")
    if data.get("source_phase2_decision") not in MERGE_DECISIONS:
        issues.append(f"source_phase2_decision must be one of {sorted(MERGE_DECISIONS)}")

    source_merge = data.get("source_merge_review")
    merge_path: Path | None = None
    expected_rows: set[int] = set()
    if source_merge:
        merge_path = Path(str(source_merge))
        if not merge_path.is_absolute():
            merge_path = REPO_ROOT / merge_path
        if not merge_path.exists():
            issues.append(f"source_merge_review does not exist: {source_merge}")
        else:
            try:
                expected_rows = source_rows_from_merge_review(merge_path)
            except Exception as exc:
                issues.append(f"cannot read source_merge_review candidate rows: {exc}")

    evidence = require_mapping(data, "evidence_inputs", issues)
    if evidence:
        if evidence.get("merge_review_read") is not True:
            issues.append("evidence_inputs.merge_review_read must be true")
        require_list(evidence, "original_rows_read", issues)
        require_mapping(evidence, "existing_kb_checked", issues)

    proposed_items = require_list(data, "proposed_items", issues)
    proposed_ids: set[str] = set()
    for index, item in enumerate(proposed_items):
        if not isinstance(item, dict):
            issues.append(f"proposed_items[{index}] must be an object")
            continue
        action = item.get("action")
        if action not in PHASE3_ACTIONS:
            issues.append(f"proposed_items[{index}].action must be one of {sorted(PHASE3_ACTIONS)}")
        item_id = require_nonempty(item, "proposed_item_id", issues, f"proposed_items[{index}].")
        if item_id:
            proposed_ids.add(str(item_id))
        require_nonempty(item, "reason_for_action", issues, f"proposed_items[{index}].")
        if action == "reuse_existing":
            existing_path = item.get("existing_kb_path")
            if existing_path:
                path_obj = Path(str(existing_path))
                if not path_obj.is_absolute():
                    path_obj = REPO_ROOT / path_obj
                if not path_obj.exists():
                    issues.append(f"proposed_items[{index}].existing_kb_path does not exist: {existing_path}")
            elif item_id and not kb_item_exists(str(item_id)):
                issues.append(
                    f"proposed_items[{index}] reuses {item_id!r}, but no matching KB item was found"
                )
        if action == "create_new":
            kb_like = require_mapping(item, "kb_like_item", issues)
            if kb_like:
                for field in ("id", "kind", "unit", "unit_kind", "material_class", "notes"):
                    require_nonempty(kb_like, field, issues, f"proposed_items[{index}].kb_like_item.")
        decision = require_mapping(item, "import_local_decision", issues)
        if decision:
            if decision.get("decision") not in PHASE3_IMPORT_LOCAL_DECISIONS:
                issues.append(
                    f"proposed_items[{index}].import_local_decision.decision must be one of "
                    f"{sorted(PHASE3_IMPORT_LOCAL_DECISIONS)}"
                )
            if not isinstance(decision.get("is_import"), bool):
                issues.append(f"proposed_items[{index}].import_local_decision.is_import must be boolean")
            require_nonempty(decision, "rationale", issues, f"proposed_items[{index}].import_local_decision.")
            require_list(decision, "import_risk_factors", issues)
            require_list(decision, "local_manufacture_blockers", issues)
        blockers = require_list(item, "promotion_blockers", issues)
        if not blockers:
            issues.append(f"proposed_items[{index}].promotion_blockers must not be empty for pilot staging")

    mappings = require_list(data, "proposed_bom_mappings", issues)
    mapped_rows: set[int] = set()
    for index, mapping in enumerate(mappings):
        if not isinstance(mapping, dict):
            issues.append(f"proposed_bom_mappings[{index}] must be an object")
            continue
        for field in ("source_row", "source_item", "closure_item_id", "quantity", "unit", "row_total_mass_kg"):
            if field not in mapping:
                issues.append(f"proposed_bom_mappings[{index}] missing {field}")
        source_row = mapping.get("source_row")
        if isinstance(source_row, int):
            mapped_rows.add(source_row)
        closure_item_id = mapping.get("closure_item_id")
        if closure_item_id not in proposed_ids:
            issues.append(
                f"proposed_bom_mappings[{index}].closure_item_id must reference a proposed item: {closure_item_id!r}"
            )
        if not isinstance(mapping.get("quantity"), (int, float)) or mapping.get("quantity") <= 0:
            issues.append(f"proposed_bom_mappings[{index}].quantity must be positive numeric")
        if not isinstance(mapping.get("row_total_mass_kg"), (int, float)) or mapping.get("row_total_mass_kg") < 0:
            issues.append(f"proposed_bom_mappings[{index}].row_total_mass_kg must be non-negative numeric")

    if expected_rows and mapped_rows != expected_rows:
        missing = sorted(expected_rows - mapped_rows)
        extra = sorted(mapped_rows - expected_rows)
        if missing:
            issues.append(f"proposed_bom_mappings missing source rows from merge review: {missing}")
        if extra:
            issues.append(f"proposed_bom_mappings includes rows not in merge review: {extra}")

    require_list(data, "stage_findings", issues)
    require_list(data, "unresolved", issues)
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--file", required=True, type=Path)
    parser.add_argument(
        "--kind",
        choices=("auto", "row_conversion", "merge_review", "phase3_stage"),
        default="auto",
    )
    args = parser.parse_args()

    path = args.file if args.file.is_absolute() else REPO_ROOT / args.file
    if not path.exists():
        print(f"missing file: {path}", file=sys.stderr)
        return 1

    kind = args.kind
    if kind == "auto":
        rel = repo_relative(path)
        if rel.startswith("research/ream250_bom/ream250_bom_row_"):
            kind = "row_conversion"
        elif rel.endswith(".stage.yaml"):
            kind = "phase3_stage"
        else:
            kind = "merge_review"

    if kind == "row_conversion":
        issues = validate_conversion_file(path)
    elif kind == "merge_review":
        issues = validate_merge_review_file(path)
    else:
        issues = validate_phase3_stage_file(path)
    if issues:
        for issue in issues:
            print(f"- {issue}", file=sys.stderr)
        return 1
    print(f"OK: {repo_relative(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
