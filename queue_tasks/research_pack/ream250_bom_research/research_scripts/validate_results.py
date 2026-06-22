#!/usr/bin/env python3
"""Validate reAM250 BOM research result files.

This is a one-off task-pack validator, intentionally kept outside the core queue
system. It accepts JSON, YAML, or Markdown files with YAML frontmatter.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path
from typing import Any, Dict, Iterable, List
from urllib.parse import urlparse

import yaml


REQUIRED_SECTIONS = ("function", "mass", "material", "how_to_make")
REQUIRED_ROW_IDENTITY_FIELDS = (
    "item",
    "cad_file",
    "source_row_number",
    "source_csv",
)
OPTIONAL_ROW_IDENTITY_FIELDS = ("link_url",)
ROW_IDENTITY_ALLOWED_FIELDS = set(REQUIRED_ROW_IDENTITY_FIELDS) | set(OPTIONAL_ROW_IDENTITY_FIELDS)
EXPECTED_SOURCE_CSV = "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
SOURCE_FIELDS = ("url_or_path", "cited_fact_or_basis", "evidence_basis")
SECTION_LIST_FIELDS = ("assumptions", "uncertainty_notes")
TOP_LEVEL_LIST_FIELDS = ("kb_implications",)
ITEM_GRANULARITY_VALUES = (
    "simple_part",
    "assembly",
    "purchased_module",
    "consumable",
    "raw_material_or_stock",
    "unknown",
)
ITEM_GRANULARITY_RE = re.compile(
    r"^item_granularity:\s*([a-z_]+)\s+-\s+.+"
)
REPLACEABLE_CONSUMABLE_CAD_RE = re.compile(
    r"\b(o-?ring|gasket|filter|lubricant|adhesive|seal_iso|seal[_ -]?iso)\b",
    re.IGNORECASE,
)
STANDARD_HARDWARE_NOT_MODULE_RE = re.compile(
    r"\b(claw clamp|fastener|bolt|screw|nut|washer)\b",
    re.IGNORECASE,
)
STANDARD_HARDWARE_CAD_RE = re.compile(
    r"(?:^|[^A-Za-z0-9])(bolt|screw|nut|washer|fastener)(?:$|[^A-Za-z0-9])",
    re.IGNORECASE,
)
NON_PLACEHOLDER_STEP_MATERIAL_RE = re.compile(
    r"\b(?:STEP material extractor|assembly STEP material extraction|local assembly STEP material extractor)"
    r".{0,160}\b(?:returned|reports?|matched|found)\b"
    r".{0,80}\bmaterial\s+['\"]?(?!Generic\b|Default\b|Material\b|None\b|Allgemein\b)"
    r"[A-Za-z][A-Za-z0-9, /+_.-]+",
    re.IGNORECASE | re.DOTALL,
)
EVIDENCE_BASIS_VALUES = (
    "bom_provided",
    "independent_vendor_spec",
    "standard_part_convention",
    "engineering_hypothesis",
    "unresolved",
)
EVIDENCE_BASIS_SET = set(EVIDENCE_BASIS_VALUES)
RELIABILITY_ORDER = (
    "bom_provided",
    "independent_vendor_spec",
    "standard_part_convention",
    "engineering_hypothesis",
)
ASSUMED_MATERIAL_RE = re.compile(
    r"\b(assumed|assumption|guess|guessed|likely|suggests?|conservative)\b",
    re.IGNORECASE,
)
UNRESOLVED_MATERIAL_RE = re.compile(r"\bunresolved\b", re.IGNORECASE)
STANDARD_BASIS_RE = re.compile(
    r"\b(standard|designation|parameter|suffix|class|family|DIN|ISO|SKF|SMC|complete|incomplete)\b",
    re.IGNORECASE,
)
INDEPENDENT_SEARCH_ROUTE_RE = re.compile(
    r"\b(agent-initiated|independent (?:web )?search|searched|search result|found by web search)\b",
    re.IGNORECASE,
)
WEB_SEARCH_AUDIT_RE = re.compile(r"\btargeted_web_search\s*:", re.IGNORECASE)
BOM_URL_ROUTE_AUDIT_RE = re.compile(r"\bbom_url_route_check\s*:", re.IGNORECASE)
OFFICIAL_ALTERNATE_ROUTE_AUDIT_RE = re.compile(
    r"\bofficial_alternate_route_check\s*:",
    re.IGNORECASE,
)


def load_result(path: Path) -> Dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    suffix = path.suffix.lower()
    if suffix == ".json":
        data = json.loads(text)
    elif suffix in {".yaml", ".yml"}:
        data = yaml.safe_load(text)
    else:
        data = load_markdown_frontmatter(text, path)
    if not isinstance(data, dict):
        raise ValueError(f"result must be a mapping: {path}")
    return data


def load_markdown_frontmatter(text: str, path: Path) -> Dict[str, Any]:
    if not text.startswith("---\n"):
        raise ValueError(f"markdown result must start with YAML frontmatter: {path}")
    end = text.find("\n---", 4)
    if end == -1:
        raise ValueError(f"markdown frontmatter is not closed: {path}")
    data = yaml.safe_load(text[4:end]) or {}
    if not isinstance(data, dict):
        raise ValueError(f"frontmatter must be a mapping: {path}")
    return data


def validate_result(data: Dict[str, Any]) -> List[str]:
    issues: List[str] = []
    first_key = next(iter(data), None)
    if first_key != "row_identity":
        issues.append("row_identity must be the first top-level frontmatter key")
    row_identity = data.get("row_identity")
    if not isinstance(row_identity, dict):
        issues.append("missing required object section: row_identity")
    else:
        for field in REQUIRED_ROW_IDENTITY_FIELDS:
            if row_identity.get(field) in (None, ""):
                issues.append(f"missing required field: row_identity.{field}")
        for field in row_identity:
            if field not in ROW_IDENTITY_ALLOWED_FIELDS:
                issues.append(f"unexpected field in row_identity: {field}")
        if "link_url" in row_identity and row_identity.get("link_url") in (None, ""):
            issues.append("row_identity.link_url must be non-empty when present")
        if row_identity.get("source_csv") != EXPECTED_SOURCE_CSV:
            issues.append(
                "row_identity.source_csv must be "
                f"{EXPECTED_SOURCE_CSV!r}"
            )
        issues.extend(validate_row_identity_link_url(row_identity))

    for section_name in REQUIRED_SECTIONS:
        section = data.get(section_name)
        if not isinstance(section, dict):
            issues.append(f"missing required object section: {section_name}")
            continue
        source_row_identity = row_identity if isinstance(row_identity, dict) else {}
        issues.extend(validate_source(section, section_name, source_row_identity))
        issues.extend(validate_web_search_audit(section, section_name))
        issues.extend(validate_section_lists(section, section_name))
        issues.extend(validate_no_duplicate_section_notes(section, section_name))

    mass = data.get("mass") if isinstance(data.get("mass"), dict) else {}
    value_kg = mass.get("value_kg")
    if value_kg in (None, ""):
        issues.append("missing required field: mass.value_kg")
    elif not isinstance(value_kg, (int, float)) or isinstance(value_kg, bool):
        issues.append("mass.value_kg must be a number")

    function = data.get("function") if isinstance(data.get("function"), dict) else {}
    material = data.get("material") if isinstance(data.get("material"), dict) else {}
    how_to_make = data.get("how_to_make") if isinstance(data.get("how_to_make"), dict) else {}

    if not function.get("summary"):
        issues.append("missing required field: function.summary")
    if not mass.get("basis"):
        issues.append("missing required field: mass.basis")
    if not material.get("primary_material"):
        issues.append("missing required field: material.primary_material")
    else:
        primary_material = str(material.get("primary_material"))
        if ASSUMED_MATERIAL_RE.search(primary_material):
            issues.append(
                "material.primary_material must be sourced or broad/unknown; "
                "do not encode assumed specific materials"
            )
        if UNRESOLVED_MATERIAL_RE.search(primary_material):
            issues.append(
                "material.primary_material must not contain 'unresolved'; "
                "use a defensible broad engineering_hypothesis or 'unknown material'"
            )
    if not how_to_make.get("summary"):
        issues.append("missing required field: how_to_make.summary")
    if "manufacturing_steps" not in how_to_make:
        issues.append("missing required field: how_to_make.manufacturing_steps")
    elif not isinstance(how_to_make.get("manufacturing_steps"), list):
        issues.append("how_to_make.manufacturing_steps must be a list")

    for field in TOP_LEVEL_LIST_FIELDS:
        if field not in data:
            issues.append(f"missing required field: {field}")
        elif not isinstance(data.get(field), list):
            issues.append(f"{field} must be a list")
    issues.extend(validate_kb_implications(data))

    return issues


def validate_row_identity_link_url(row_identity: Dict[str, Any]) -> List[str]:
    source_csv = row_identity.get("source_csv")
    source_row_number = row_identity.get("source_row_number")
    if source_csv != EXPECTED_SOURCE_CSV:
        return []
    try:
        row_number = int(source_row_number)
    except (TypeError, ValueError):
        return []

    csv_path = Path(source_csv)
    if not csv_path.exists():
        return []

    try:
        with csv_path.open(newline="", encoding="utf-8") as f:
            for line_number, row in enumerate(csv.DictReader(f), start=2):
                if line_number != row_number:
                    continue
                expected = (row.get("Link URL") or "").strip()
                if not expected:
                    return []
                actual = row_identity.get("link_url")
                if actual != expected:
                    return [
                        "row_identity.link_url must match BOM Link URL "
                        f"{expected!r} when the BOM row has one"
                    ]
                return []
    except OSError as exc:
        return [f"could not read row_identity.source_csv for link_url check: {exc}"]
    return []


def validate_section_lists(section: Dict[str, Any], path: str) -> List[str]:
    issues = []
    for field in SECTION_LIST_FIELDS:
        if field not in section:
            issues.append(f"missing required field: {path}.{field}")
        elif not isinstance(section.get(field), list):
            issues.append(f"{path}.{field} must be a list")
    return issues


def normalize_note_text(value: Any) -> str:
    return " ".join(str(value).strip().lower().split())


def validate_no_duplicate_section_notes(section: Dict[str, Any], path: str) -> List[str]:
    seen: Dict[str, str] = {}
    issues: List[str] = []
    source = section.get("source") if isinstance(section.get("source"), dict) else {}
    cited = source.get("cited_fact_or_basis")
    entries: List[tuple[str, Any]] = [("source.cited_fact_or_basis", cited)]
    for field in SECTION_LIST_FIELDS:
        values = section.get(field)
        if isinstance(values, list):
            entries.extend((f"{field}[]", value) for value in values)

    for label, value in entries:
        if value in (None, ""):
            continue
        normalized = normalize_note_text(value)
        if not normalized:
            continue
        if normalized in seen:
            issues.append(
                f"{path}.{label} duplicates {path}.{seen[normalized]}; "
                "do not repeat the same fact across source, assumptions, and uncertainty_notes"
            )
        else:
            seen[normalized] = label
    return issues


def validate_kb_implications(data: Dict[str, Any]) -> List[str]:
    kb_implications = data.get("kb_implications")
    if not isinstance(kb_implications, list):
        return []

    granularity_entries = [
        str(value).strip()
        for value in kb_implications
        if str(value).strip().startswith("item_granularity:")
    ]
    if len(granularity_entries) != 1:
        return [
            "kb_implications must include exactly one entry starting with "
            "'item_granularity: <value> - '"
        ]

    entry = granularity_entries[0]
    match = ITEM_GRANULARITY_RE.match(entry)
    if not match:
        return [
            "kb_implications item_granularity entry must match "
            "'item_granularity: <value> - <explanation>'"
        ]

    value = match.group(1)
    if value not in ITEM_GRANULARITY_VALUES:
        return [
            "kb_implications item_granularity value must be one of: "
            f"{', '.join(ITEM_GRANULARITY_VALUES)}"
        ]

    row_identity = data.get("row_identity") if isinstance(data.get("row_identity"), dict) else {}
    function = data.get("function") if isinstance(data.get("function"), dict) else {}
    cad_file = str(row_identity.get("cad_file") or "")
    cad_file_lower = cad_file.lower()
    function_summary = str(function.get("summary") or "")
    granularity_context = " ".join([entry, cad_file, function_summary])
    is_belt_item = "belt" in cad_file_lower and "pulley" not in cad_file_lower
    is_replaceable_consumable_item = bool(REPLACEABLE_CONSUMABLE_CAD_RE.search(cad_file))
    if (is_belt_item or is_replaceable_consumable_item) and value != "consumable":
        return [
            "kb_implications item_granularity should be consumable for replaceable "
            "belts, O-rings, gaskets, filter elements, lubricants, adhesives, and "
            "similar maintenance items unless the row is clearly a larger calibrated "
            "vendor subsystem"
        ]
    if value == "purchased_module" and STANDARD_HARDWARE_NOT_MODULE_RE.search(granularity_context):
        return [
            "kb_implications item_granularity should not be purchased_module for "
            "simple standard hardware such as claw clamps, fasteners, bolts, screws, "
            "nuts, or washers; use simple_part unless the row is a calibrated "
            "functional module or a multi-part assembly"
        ]
    if value == "raw_material_or_stock" and STANDARD_HARDWARE_CAD_RE.search(cad_file):
        return [
            "kb_implications item_granularity should not be raw_material_or_stock "
            "for finished standard fasteners such as bolts, screws, nuts, or "
            "washers; use simple_part while noting that later KB work should map "
            "them to reusable standard hardware or a fastener kit"
        ]
    return []


def validate_source(section: Dict[str, Any], path: str, row_identity: Dict[str, Any] | None = None) -> List[str]:
    source = section.get("source")
    if not isinstance(source, dict):
        return [f"missing required object: {path}.source"]
    issues = []
    for field in SOURCE_FIELDS:
        if source.get(field) in (None, ""):
            issues.append(f"missing required field: {path}.source.{field}")
    evidence_basis = source.get("evidence_basis")
    if (
        isinstance(evidence_basis, str)
        and evidence_basis.strip().lower() not in EVIDENCE_BASIS_SET
    ):
        issues.append(
            f"{path}.source.evidence_basis must be one of: "
            f"{', '.join(EVIDENCE_BASIS_VALUES)}"
        )
    if (
        isinstance(evidence_basis, str)
        and evidence_basis.strip().lower() == "standard_part_convention"
    ):
        cited = str(source.get("cited_fact_or_basis") or "")
        if not STANDARD_BASIS_RE.search(cited):
            issues.append(
                f"{path}.source.cited_fact_or_basis must explain standard/designation "
                "parameter completeness when evidence_basis is standard_part_convention"
            )
        if NON_PLACEHOLDER_STEP_MATERIAL_RE.search(cited):
            issues.append(
                f"{path}.source.evidence_basis should be bom_provided when a "
                "non-placeholder row-specific STEP material extraction directly "
                "resolves the claimed material fact; use standard_part_convention "
                "only as a cross-check for standard/designation-derived facts"
            )
    if (
        isinstance(evidence_basis, str)
        and evidence_basis.strip().lower() == "bom_provided"
        and row_identity
    ):
        issues.extend(validate_bom_provided_source_route(section, path, row_identity))
    if (
        isinstance(evidence_basis, str)
        and evidence_basis.strip().lower() == "independent_vendor_spec"
        and row_identity
    ):
        issues.extend(validate_independent_source_route(section, path, row_identity))
    return issues


def section_evidence_text(section: Dict[str, Any]) -> str:
    chunks: List[str] = []
    source = section.get("source")
    if isinstance(source, dict):
        chunks.extend(str(source.get(field) or "") for field in SOURCE_FIELDS)
    for field in SECTION_LIST_FIELDS:
        values = section.get(field)
        if isinstance(values, list):
            chunks.extend(str(value) for value in values)
    return " ".join(chunks)


def validate_web_search_audit(section: Dict[str, Any], path: str) -> List[str]:
    source = section.get("source")
    if not isinstance(source, dict):
        return []
    evidence_basis = source.get("evidence_basis")
    if not isinstance(evidence_basis, str):
        return []
    if evidence_basis.strip().lower() not in {"engineering_hypothesis", "unresolved"}:
        return []

    evidence_text = section_evidence_text(section)
    if WEB_SEARCH_AUDIT_RE.search(evidence_text):
        return []
    return [
        f"{path}.source.evidence_basis is {evidence_basis}; include a "
        "`targeted_web_search:` note in this section listing the web queries "
        "attempted and the result before using engineering_hypothesis or unresolved"
    ]


def extract_urls(text: str) -> List[str]:
    return re.findall(r"https?://[^\s;,\"')]+", text)


def comparable_domain(url: str) -> str:
    host = urlparse(url).hostname or ""
    host = host.lower()
    if host.startswith("www."):
        host = host[4:]
    parts = host.split(".")
    if len(parts) >= 2:
        return ".".join(parts[-2:])
    return host


def validate_independent_source_route(
    section: Dict[str, Any],
    path: str,
    row_identity: Dict[str, Any],
) -> List[str]:
    source = section.get("source")
    if not isinstance(source, dict):
        return []
    link_url = str(row_identity.get("link_url") or "").strip()
    if not link_url:
        return []

    bom_domain = comparable_domain(link_url)
    if not bom_domain:
        return []

    source_text = section_evidence_text(section)
    source_urls = extract_urls(source_text)
    if not source_urls:
        return []

    same_domain_urls = [
        url for url in source_urls
        if comparable_domain(url) == bom_domain
    ]
    if not same_domain_urls:
        if BOM_URL_ROUTE_AUDIT_RE.search(source_text):
            return []
        return [
            f"{path}.source.evidence_basis is independent_vendor_spec and cites "
            "a different domain than row_identity.link_url; include a "
            "`bom_url_route_check:` note explaining the BOM-provided URL, "
            "redirect/canonical, or first-party route checked and why it did not "
            "resolve this section's value before relying on a third-party source"
        ]

    if INDEPENDENT_SEARCH_ROUTE_RE.search(source_text):
        return []

    if link_url in source_text:
        return [
            f"{path}.source.evidence_basis is independent_vendor_spec but cites the "
            "BOM row link_url; use bom_provided for facts obtained through the "
            "BOM-provided URL route"
        ]

    return [
        f"{path}.source.evidence_basis is independent_vendor_spec but cites the same "
        f"vendor domain as row_identity.link_url ({bom_domain}) without documenting "
        "an agent-initiated independent search route; use bom_provided when the fact "
        "came from the BOM-provided URL route"
    ]


def validate_bom_provided_source_route(
    section: Dict[str, Any],
    path: str,
    row_identity: Dict[str, Any],
) -> List[str]:
    source = section.get("source")
    if not isinstance(source, dict):
        return []
    link_url = str(row_identity.get("link_url") or "").strip()
    if not link_url:
        return []

    bom_domain = comparable_domain(link_url)
    if not bom_domain:
        return []

    source_text = section_evidence_text(section)
    source_urls = extract_urls(source_text)
    if not source_urls:
        return []

    different_domain_urls = [
        url for url in source_urls
        if comparable_domain(url) and comparable_domain(url) != bom_domain
    ]
    if not different_domain_urls:
        return []

    if OFFICIAL_ALTERNATE_ROUTE_AUDIT_RE.search(source_text):
        return []

    return [
        f"{path}.source.evidence_basis is bom_provided but cites external URL(s) "
        f"on a different domain than row_identity.link_url ({bom_domain}); include "
        "an `official_alternate_route_check:` note explaining why the alternate "
        "domain is still BOM-side evidence, such as same manufacturer or official "
        "operator, official shop/canonical/domain evidence, and row-matched product "
        "ID or same-row product-family route"
    ]


def iter_paths(files: Iterable[Path], directory: Path | None) -> List[Path]:
    paths = list(files)
    if directory:
        if not directory.exists():
            raise FileNotFoundError(f"result directory does not exist: {directory}")
        if not directory.is_dir():
            raise NotADirectoryError(f"result path is not a directory: {directory}")
        paths.extend(
            sorted(
                path for path in directory.iterdir()
                if path.is_file() and path.suffix.lower() in {".md", ".json", ".yaml", ".yml"}
            )
        )
    return paths


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate reAM250 BOM research result files")
    parser.add_argument("--file", action="append", default=[], type=Path, help="Result file to validate")
    parser.add_argument("--dir", type=Path, help="Directory of result files to validate")
    args = parser.parse_args()

    paths = iter_paths(args.file, args.dir)
    if not paths:
        parser.error("provide --file or --dir")

    failed = False
    for path in paths:
        try:
            issues = validate_result(load_result(path))
        except Exception as exc:
            issues = [str(exc)]
        if issues:
            failed = True
            print(f"{path}: FAIL")
            for issue in issues:
                print(f"  - {issue}")
        else:
            print(f"{path}: OK")

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
