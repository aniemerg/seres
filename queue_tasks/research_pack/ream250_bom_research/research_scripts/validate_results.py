#!/usr/bin/env python3
"""Validate reAM250 BOM research result files.

This is a one-off task-pack validator, intentionally kept outside the core queue
system. It accepts JSON, YAML, or Markdown files with YAML frontmatter.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any, Dict, Iterable, List

import yaml


REQUIRED_SECTIONS = ("function", "mass", "material", "how_to_make")
SOURCE_FIELDS = ("url_or_path", "cited_fact_or_basis", "confidence")
REQUIRED_LISTS = ("assumptions", "uncertainty_notes", "kb_implications")
CONFIDENCE_VALUES = {"low", "medium", "high", "unknown"}
ASSUMED_MATERIAL_RE = re.compile(
    r"\b(assumed|assumption|guess|guessed|likely|suggests?|conservative)\b",
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
    for section_name in REQUIRED_SECTIONS:
        section = data.get(section_name)
        if not isinstance(section, dict):
            issues.append(f"missing required object section: {section_name}")
            continue
        issues.extend(validate_source(section, section_name))

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
    if not how_to_make.get("summary"):
        issues.append("missing required field: how_to_make.summary")
    if "manufacturing_steps" not in how_to_make:
        issues.append("missing required field: how_to_make.manufacturing_steps")
    elif not isinstance(how_to_make.get("manufacturing_steps"), list):
        issues.append("how_to_make.manufacturing_steps must be a list")

    for field in REQUIRED_LISTS:
        if field not in data:
            issues.append(f"missing required field: {field}")
        elif not isinstance(data.get(field), list):
            issues.append(f"{field} must be a list")

    return issues


def validate_source(section: Dict[str, Any], path: str) -> List[str]:
    source = section.get("source")
    if not isinstance(source, dict):
        return [f"missing required object: {path}.source"]
    issues = []
    for field in SOURCE_FIELDS:
        if source.get(field) in (None, ""):
            issues.append(f"missing required field: {path}.source.{field}")
    confidence = source.get("confidence")
    if isinstance(confidence, str) and confidence.strip().lower() not in CONFIDENCE_VALUES:
        issues.append(
            f"{path}.source.confidence must be one of: "
            f"{', '.join(sorted(CONFIDENCE_VALUES))}"
        )
    return issues


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
