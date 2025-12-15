"""
Indexer for the v0 KB. Scans kb/**/*.yaml, performs permissive parsing,
and emits:
- out/index.json (entries + refs)
- out/validation_report.md (soft warnings)
- out/unresolved_refs.jsonl (requires_text and other unresolved strings)
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

try:
    import yaml  # type: ignore
except ImportError:  # pragma: no cover
    yaml = None

from . import models

KB_ROOT = Path("kb")
OUT_DIR = Path("out")
WORK_QUEUE = OUT_DIR / "work_queue.jsonl"


def _infer_kind(path: Path, data: dict) -> Optional[str]:
    kind = data.get("kind")
    if kind:
        return kind
    parts = path.parts
    if "processes" in parts:
        return "process"
    if "recipes" in parts:
        return "recipe"
    if "resources" in parts:
        return "resource_type"
    if "materials" in parts:
        return "material"
    if "machines" in parts:
        return "machine"
    if "parts" in parts:
        return "part"
    if "boms" in parts:
        return "bom"
    return None


def _collect_refs(kind: str, data: dict) -> Tuple[Set[str], List[dict]]:
    refs: Set[str] = set()
    unresolved: List[dict] = []

    def add_unresolved(text: str, field_path: str) -> None:
        if not text:
            return
        unresolved.append({"ref_string": text, "field_path": field_path})

    if kind == "process":
        for field_name in ("inputs", "outputs", "byproducts"):
            for entry in data.get(field_name, []) or []:
                item_id = entry.get("item_id") or entry.get("id")
                if item_id:
                    refs.add(str(item_id))
        for rid in data.get("requires_ids", []) or []:
            refs.add(str(rid))
        for rtxt in data.get("requires_text", []) or []:
            add_unresolved(str(rtxt), "requires_text")
        for req in data.get("resource_requirements", []) or []:
            rtype = req.get("resource_type") or req.get("resource")
            if rtype:
                refs.add(str(rtype))
    elif kind == "recipe":
        target = data.get("target_item_id")
        if target:
            refs.add(str(target))
        for step in data.get("steps", []) or []:
            refs.add(str(step))
    elif kind in ("material", "part", "machine"):
        bom = data.get("bom")
        if bom:
            refs.add(str(bom))
    elif kind == "resource_type":
        for alias in data.get("aliases", []) or []:
            add_unresolved(str(alias), "aliases")
    elif kind == "bom":
        owner = data.get("owner_item_id")
        if owner:
            refs.add(str(owner))
        for comp in data.get("components", []) or []:
            item_id = comp.get("item_id") or comp.get("id")
            if item_id:
                refs.add(str(item_id))
    return refs, unresolved


def _collect_nulls(kind: str, data: dict) -> List[dict]:
    """Collect fields with null values that should eventually have data."""
    nulls: List[dict] = []

    if kind == "process":
        for field_name in ("inputs", "outputs", "byproducts"):
            for i, entry in enumerate(data.get(field_name, []) or []):
                if entry.get("qty") is None:
                    item_id = entry.get("item_id") or entry.get("id") or "unknown"
                    nulls.append({"field": f"{field_name}[{i}].qty", "item": item_id})
        for i, req in enumerate(data.get("resource_requirements", []) or []):
            if req.get("amount") is None:
                rtype = req.get("resource_type") or req.get("resource") or "unknown"
                nulls.append({"field": f"resource_requirements[{i}].amount", "resource": rtype})
    elif kind in ("part", "machine"):
        if data.get("mass") is None:
            nulls.append({"field": "mass"})
    elif kind == "bom":
        for i, comp in enumerate(data.get("components", []) or []):
            if comp.get("qty") is None:
                item_id = comp.get("item_id") or comp.get("id") or "unknown"
                nulls.append({"field": f"components[{i}].qty", "item": item_id})

    return nulls


def _load_yaml(path: Path, warnings: List[str]) -> dict:
    try:
        with path.open("r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
        if not isinstance(data, dict):
            warnings.append(f"{path}: expected mapping at top level; got {type(data).__name__}")
            return {}
        return data
    except Exception as exc:  # pragma: no cover
        warnings.append(f"{path}: failed to parse ({exc})")
        return {}


def build_index() -> Dict[str, dict]:
    if yaml is None:
        raise SystemExit("PyYAML is required: pip install pyyaml")
    entries: Dict[str, dict] = {}
    unresolved_refs: List[dict] = []
    null_values: List[dict] = []
    warnings: List[str] = []
    import_stubs: List[dict] = []
    referenced_only: Set[str] = set()
    kb_files = sorted(KB_ROOT.glob("**/*.yaml"))

    for path in kb_files:
        data = _load_yaml(path, warnings)
        kind = _infer_kind(path, data)
        entry_id = data.get("id") or path.stem
        if not kind:
            warnings.append(f"{path}: unknown kind; skipped")
            continue

        if kind == "recipe":
            steps = data.get("steps") or []
            variant_id = str(data.get("variant_id", "") or "")
            if not steps or "import" in variant_id:
                import_stubs.append(
                    {
                        "recipe_id": data.get("id") or path.stem,
                        "target_item_id": data.get("target_item_id"),
                        "variant_id": variant_id or "unknown",
                        "file": str(path),
                        "reason": "empty_steps" if not steps else "import_variant",
                    }
                )

        refs_out, unresolved = _collect_refs(kind, data)
        for u in unresolved:
            u.update({"owner_id": entry_id, "owner_kind": kind, "file": str(path)})
        unresolved_refs.extend(unresolved)

        nulls = _collect_nulls(kind, data)
        for n in nulls:
            n.update({"owner_id": entry_id, "owner_kind": kind, "file": str(path)})
        null_values.extend(nulls)

        entry = {
            "id": entry_id,
            "kind": kind,
            "status": "defined",
            "defined_in": str(path),
            "refs_out": sorted(refs_out),
            "refs_in": [],
            "layer_tags": data.get("layer_tags", []) or [],
            "aliases": data.get("aliases", []) or [],
            "name": data.get("name"),
        }
        entries[entry_id] = entry

    # Add referenced-only nodes
    for entry in list(entries.values()):
        for ref in entry["refs_out"]:
            if ref not in entries:
                entries[ref] = {
                    "id": ref,
                    "kind": "unknown",
                    "status": "referenced_only",
                    "defined_in": None,
                    "refs_out": [],
                    "refs_in": [],
                    "layer_tags": [],
                    "aliases": [],
                    "name": None,
                }
                referenced_only.add(ref)

    # Compute refs_in
    for entry in entries.values():
        for ref in entry["refs_out"]:
            if ref in entries:
                entries[ref]["refs_in"].append(entry["id"])

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with (OUT_DIR / "index.json").open("w", encoding="utf-8") as f:
        json.dump({"entries": entries}, f, indent=2, sort_keys=True)

    with (OUT_DIR / "unresolved_refs.jsonl").open("w", encoding="utf-8") as f:
        for ref in unresolved_refs:
            f.write(json.dumps(ref) + "\n")

    with (OUT_DIR / "import_stubs.jsonl").open("w", encoding="utf-8") as f:
        for stub in import_stubs:
            f.write(json.dumps(stub) + "\n")

    with (OUT_DIR / "null_values.jsonl").open("w", encoding="utf-8") as f:
        for nv in null_values:
            f.write(json.dumps(nv) + "\n")

    _update_work_queue(unresolved_refs, referenced_only, import_stubs)
    _write_report(entries, warnings, null_values)
    return entries


def _update_work_queue(
    unresolved_refs: List[dict], referenced_only: Set[str], import_stubs: List[dict]
) -> None:
    """
    Append new work items to the work queue based on gaps:
    - unresolved_refs: free-text refs needing definition/resolution
    - referenced_only: ids referenced but not defined
    - import_stubs: recipes with empty steps/import variants needing real routes
    """
    existing: Set[str] = set()
    if WORK_QUEUE.exists():
        with WORK_QUEUE.open("r", encoding="utf-8") as f:
            for line in f:
                try:
                    obj = json.loads(line)
                    wid = obj.get("id")
                    reason = obj.get("reason", "")
                    existing.add(f"{wid}:{reason}")
                except Exception:
                    continue

    def append_items(items: List[dict]) -> None:
        if not items:
            return
        with WORK_QUEUE.open("a", encoding="utf-8") as wf:
            for obj in items:
                key = f"{obj['id']}:{obj['reason']}"
                if key in existing:
                    continue
                wf.write(json.dumps(obj) + "\n")
                existing.add(key)

    gap_items: List[dict] = []
    for ref in unresolved_refs:
        gap_items.append(
            {
                "id": ref["ref_string"],
                "kind": "gap",
                "reason": "unresolved_ref",
                "context": {"owner_id": ref["owner_id"], "field_path": ref["field_path"]},
            }
        )
    for ref_id in sorted(referenced_only):
        gap_items.append(
            {"id": ref_id, "kind": "gap", "reason": "referenced_only", "context": {}}
        )
    for stub in import_stubs:
        gap_items.append(
            {
                "id": stub.get("target_item_id") or stub.get("recipe_id"),
                "kind": "recipe",
                "reason": "import_stub",
                "context": {"recipe_id": stub.get("recipe_id"), "variant": stub.get("variant_id")},
            }
        )
    append_items(gap_items)


def _write_report(entries: Dict[str, dict], warnings: List[str], null_values: List[dict]) -> None:
    counts: Dict[str, int] = {}
    for entry in entries.values():
        counts[entry["kind"]] = counts.get(entry["kind"], 0) + 1
    lines = [
        "# Validation Report (v0)",
        "",
        "## Counts by kind",
    ]
    for kind, count in sorted(counts.items()):
        lines.append(f"- {kind}: {count}")

    # Null value summary
    if null_values:
        null_by_kind: Dict[str, int] = {}
        for nv in null_values:
            k = nv.get("owner_kind", "unknown")
            null_by_kind[k] = null_by_kind.get(k, 0) + 1
        lines.append("")
        lines.append("## Missing data (null values)")
        lines.append(f"Total: {len(null_values)} null fields")
        for kind, count in sorted(null_by_kind.items()):
            lines.append(f"- {kind}: {count}")
        lines.append("")
        lines.append("See `out/null_values.jsonl` for details.")

    if warnings:
        lines.append("")
        lines.append("## Warnings")
        for w in warnings:
            lines.append(f"- {w}")
    if not warnings:
        lines.append("")
        lines.append("No warnings.")

    with (OUT_DIR / "validation_report.md").open("w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def main() -> None:
    entries = build_index()
    print(f"Indexed {len(entries)} entries into {OUT_DIR/'index.json'}")


if __name__ == "__main__":  # pragma: no cover
    main()
