"""
Indexer for the v0 KB. Scans kb/**/*.yaml, performs permissive parsing,
and emits:
- out/index.json (entries + refs)
- out/validation_report.md (soft warnings)
- out/unresolved_refs.jsonl (requires_text and other unresolved strings)
- out/work_queue.jsonl (all gaps needing attention)
- out/missing_recipes.jsonl (items without recipes)
- out/missing_fields.jsonl (required fields not populated)
- out/orphan_resources.jsonl (resource_types with no provider machine)
"""
from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

try:
    import yaml  # type: ignore
except ImportError:  # pragma: no cover
    yaml = None

from . import models
from .queue_tool import _locked_queue

KB_ROOT = Path("kb")
OUT_DIR = Path("out")
WORK_QUEUE = OUT_DIR / "work_queue.jsonl"
WORK_QUEUE_LOCK = OUT_DIR / "work_queue.lock"


def _infer_kind(path: Path, data: dict) -> Optional[str]:
    kind = data.get("kind")
    if kind:
        return kind
    parts = path.parts
    if "seeds" in parts:
        return "seed"
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


def _collect_refs(kind: str, data: dict) -> Tuple[Set[str], List[dict], List[dict], Dict[str, dict]]:
    refs: Set[str] = set()
    unresolved: List[dict] = []
    invalid: List[dict] = []
    ref_metadata: Dict[str, dict] = {}

    def add_unresolved(text: str, field_path: str) -> None:
        if not text:
            return
        unresolved.append({"ref_string": text, "field_path": field_path})

    if kind in ("process", "seed"):
        for field_name in ("inputs", "outputs", "byproducts"):
            for entry in data.get(field_name, []) or []:
                item_id = entry.get("item_id") or entry.get("id")
                if item_id:
                    refs.add(str(item_id))
        for rid in data.get("requires_ids", []) or []:
            if isinstance(rid, str):
                # Simple string format (backward compatible)
                refs.add(str(rid))
            elif isinstance(rid, dict):
                # Rich object format with metadata
                item_id = rid.get("id")
                if item_id:
                    refs.add(str(item_id))
                    # Store metadata (everything except 'id')
                    metadata = {k: v for k, v in rid.items() if k != "id"}
                    if metadata:
                        ref_metadata[str(item_id)] = metadata
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
        steps = data.get("steps", []) or []
        for step in steps:
            if isinstance(step, dict):
                pid = step.get("process_id")
                if pid:
                    refs.add(str(pid))
                else:
                    invalid.append({"reason": "missing_process_id", "step": step})
            else:
                invalid.append({"reason": "legacy_step_format", "step": step})
                try:
                    refs.add(str(step))
                except Exception:
                    pass
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
    return refs, unresolved, invalid, ref_metadata


def _collect_nulls(kind: str, data: dict) -> List[dict]:
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


def _collect_missing_fields(kind: str, data: dict) -> List[dict]:
    missing: List[dict] = []

    if kind == "process":
        if not data.get("energy_model"):
            missing.append({"field": "energy_model", "severity": "soft"})
        if not data.get("time_model"):
            missing.append({"field": "time_model", "severity": "soft"})
    elif kind == "part":
        if not data.get("material_class"):
            missing.append({"field": "material_class", "severity": "soft"})
    elif kind == "machine":
        if not data.get("capabilities"):
            missing.append({"field": "capabilities", "severity": "soft"})
        if not data.get("bom"):
            missing.append({"field": "bom", "severity": "soft"})

    return missing


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
    invalid_recipes: List[dict] = []
    null_values: List[dict] = []
    missing_fields: List[dict] = []
    warnings: List[str] = []
    import_stubs: List[dict] = []
    referenced_only: Set[str] = set()
    machine_capabilities: Dict[str, List[str]] = {}  # machine_id -> capabilities
    recipe_targets: Set[str] = set()  # items that have recipes
    invalid_recipes: List[dict] = []
    seed_references: Dict[str, List[str]] = {}  # item_id -> list of seed file ids that reference it
    item_metadata: Dict[str, dict] = {}  # item_id -> metadata from seed requires_ids
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
            target = data.get("target_item_id")
            if target:
                recipe_targets.add(str(target))
            if not steps or "import" in variant_id:
                import_stubs.append(
                    {
                        "recipe_id": data.get("id") or path.stem,
                        "target_item_id": target,
                        "variant_id": variant_id or "unknown",
                        "file": str(path),
                        "reason": "empty_steps" if not steps else "import_variant",
                    }
                )
        elif kind == "machine":
            caps = data.get("capabilities", []) or []
            if caps:
                machine_capabilities[entry_id] = caps

        refs_out, unresolved, invalid_steps, ref_metadata = _collect_refs(kind, data)

        # Track seed file references and metadata for work queue
        if kind == "seed":
            for ref_id in refs_out:
                if ref_id not in seed_references:
                    seed_references[ref_id] = []
                seed_references[ref_id].append(entry_id)
            # Store metadata from this seed file
            for ref_id, metadata in ref_metadata.items():
                if ref_id not in item_metadata:
                    item_metadata[ref_id] = {}
                # Merge metadata (later seeds can add/override)
                item_metadata[ref_id].update(metadata)

        for u in unresolved:
            u.update({"owner_id": entry_id, "owner_kind": kind, "file": str(path)})
        unresolved_refs.extend(unresolved)
        if invalid_steps:
            invalid_recipes.append({"id": entry_id, "file": str(path), "issues": invalid_steps})
        if invalid_steps:
            invalid_recipes.append({"id": entry_id, "file": str(path), "issues": invalid_steps})

        nulls = _collect_nulls(kind, data)
        for n in nulls:
            n.update({"owner_id": entry_id, "owner_kind": kind, "file": str(path)})
        null_values.extend(nulls)

        mfields = _collect_missing_fields(kind, data)
        for m in mfields:
            m.update({"owner_id": entry_id, "owner_kind": kind, "file": str(path)})
        missing_fields.extend(mfields)

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

    # Compute items without recipes (parts/materials/machines that no recipe targets)
    items_without_recipes: List[dict] = []
    for entry in entries.values():
        if entry["kind"] in ("part", "material", "machine") and entry["id"] not in recipe_targets:
            items_without_recipes.append({
                "id": entry["id"],
                "kind": entry["kind"],
                "file": entry["defined_in"],
            })

    # Compute orphan resources (resource_types with no machine providing them)
    all_capabilities: Set[str] = set()
    for caps in machine_capabilities.values():
        all_capabilities.update(caps)
    orphan_resources: List[dict] = []
    for entry in entries.values():
        if entry["kind"] == "resource_type" and entry["status"] == "defined":
            if entry["id"] not in all_capabilities:
                orphan_resources.append({
                    "id": entry["id"],
                    "file": entry["defined_in"],
                    "refs_in": entry["refs_in"],  # processes that need this resource
                })

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

    with (OUT_DIR / "missing_fields.jsonl").open("w", encoding="utf-8") as f:
        for mf in missing_fields:
            f.write(json.dumps(mf) + "\n")

    with (OUT_DIR / "missing_recipes.jsonl").open("w", encoding="utf-8") as f:
        for mr in items_without_recipes:
            f.write(json.dumps(mr) + "\n")

    with (OUT_DIR / "orphan_resources.jsonl").open("w", encoding="utf-8") as f:
        for orph in orphan_resources:
            f.write(json.dumps(orph) + "\n")

    with (OUT_DIR / "invalid_recipes.jsonl").open("w", encoding="utf-8") as f:
        for inv in invalid_recipes:
            f.write(json.dumps(inv) + "\n")

    filter_stats = _update_work_queue(
        unresolved_refs, referenced_only, import_stubs,
        items_without_recipes, missing_fields, orphan_resources, invalid_recipes,
        seed_references, item_metadata
    )
    _write_report(
        entries, warnings, null_values, missing_fields,
        items_without_recipes, orphan_resources, filter_stats
    )
    return entries


# Added helper for missing recipes (backward-compatible stub to satisfy older indexer paths)

def _write_missing_recipes(missing_recipes: List[dict], file_path: Optional[Path] = None) -> None:
    if file_path is None:
        file_path = OUT_DIR / "missing_recipes.jsonl"
    try:
        with file_path.open("w", encoding="utf-8") as f:
            for mr in missing_recipes:
                f.write(json.dumps(mr) + "\n")
    except Exception:
        # Best-effort; do not crash indexing if this fails
        pass


def _update_work_queue(
    unresolved_refs: List[dict],
    referenced_only: Set[str],
    import_stubs: List[dict],
    items_without_recipes: List[dict],
    missing_fields: List[dict],
    orphan_resources: List[dict],
    invalid_recipes: List[dict],
    seed_references: Dict[str, List[str]],
    item_metadata: Dict[str, dict],
) -> Dict[str, int]:
    """
    Rebuild work queue from current gaps (replaces previous queue).
    - unresolved_refs: free-text refs needing definition/resolution
    - referenced_only: ids referenced but not defined
    - import_stubs: recipes with empty steps/import variants needing real routes
    - items_without_recipes: parts/materials/machines with no recipe
    - missing_fields: required fields not populated (energy_model, time_model, etc.)
    - orphan_resources: resource_types with no machine providing them
    - seed_references: item_id -> list of seed file ids that reference it
    - item_metadata: item_id -> freeform metadata from seed requires_ids

    Returns dict of filter statistics.
    """
    from .config import QueueFilterConfig

    gap_items: List[dict] = []

    # Unresolved text references
    for ref in unresolved_refs:
        gap_items.append(
            {
                "id": f"unresolved_ref:{ref['ref_string']}",
                "kind": "gap",
                "reason": "unresolved_ref",
                "context": {"owner_id": ref["owner_id"], "field_path": ref["field_path"]},
                "item_id": ref["ref_string"],
                "gap_type": "unresolved_ref",
            }
        )

    # Referenced but not defined
    for ref_id in sorted(referenced_only):
        context = {}
        if ref_id in seed_references:
            context["seed_files"] = seed_references[ref_id]
        if ref_id in item_metadata:
            context["metadata"] = item_metadata[ref_id]
        gap_items.append(
            {
                "id": f"referenced_only:{ref_id}",
                "kind": "gap",
                "reason": "referenced_only",
                "context": context,
                "item_id": ref_id,
                "gap_type": "referenced_only",
            }
        )

    # Import stubs needing real manufacturing routes
    for stub in import_stubs:
        gap_items.append(
            {
                "id": f"import_stub:{stub.get('target_item_id') or stub.get('recipe_id')}",
                "kind": "recipe",
                "reason": "import_stub",
                "gap_type": "import_stub",
                "item_id": stub.get("target_item_id") or stub.get("recipe_id"),
                "context": {"recipe_id": stub.get("recipe_id"), "variant": stub.get("variant_id")},
            }
        )

    # Items without recipes (will be imports unless recipe added)
    for item in items_without_recipes:
        gap_items.append(
            {
                "id": f"no_recipe:{item['id']}",
                "kind": item["kind"],
                "reason": "no_recipe",
                "gap_type": "no_recipe",
                "item_id": item["id"],
                "context": {"file": item["file"]},
            }
        )

    # Missing required fields (energy_model, time_model, material_class, etc.)
    for mf in missing_fields:
        gap_items.append(
            {
                "id": f"missing_field:{mf['owner_id']}:{mf['field']}",
                "kind": mf["owner_kind"],
                "reason": "missing_field",
                "gap_type": "missing_field",
                "item_id": mf["owner_id"],
                "context": {"field": mf["field"], "file": mf["file"]},
            }
        )

    # Orphan resources (resource_types with no machine providing them)
    for orph in orphan_resources:
        gap_items.append(
            {
                "id": f"no_provider_machine:{orph['id']}",
                "kind": "resource_type",
                "reason": "no_provider_machine",
                "gap_type": "no_provider_machine",
                "item_id": orph["id"],
                "context": {"needed_by": orph.get("refs_in", []), "file": orph["file"]},
            }
        )

    # Invalid recipes (legacy step schema or missing process_id)
    for inv in invalid_recipes:
        gap_items.append(
            {
                "id": f"invalid_recipe_schema:{inv.get('id')}",
                "kind": "recipe",
                "reason": "invalid_recipe_schema",
                "gap_type": "invalid_recipe_schema",
                "item_id": inv.get("id"),
                "context": {"file": inv.get("file")},
            }
        )

    # Apply queue filtering based on config
    config = QueueFilterConfig.load()
    total_gaps = len(gap_items)
    filtered_count = 0

    if config.enabled:
        filtered_items = []
        for gap in gap_items:
            should_exclude, reason = config.should_exclude(gap)
            if should_exclude:
                filtered_items.append(gap)
                filtered_count += 1

        gap_items = [g for g in gap_items if g not in filtered_items]

    filter_stats = {
        "total_gaps": total_gaps,
        "filtered_count": filtered_count,
        "queued_count": len(gap_items),
        "filtering_enabled": config.enabled,
        "current_mode": config.current_mode,
    }

    with _locked_queue():
        existing: Dict[str, dict] = {}
        if WORK_QUEUE.exists():
            with WORK_QUEUE.open("r", encoding="utf-8") as f:
                for line in f:
                    try:
                        obj = json.loads(line)
                        existing[obj.get("id")] = obj
                    except Exception:
                        continue

        merged: List[dict] = []
        now = time.time()
        for obj in gap_items:
            eid = obj["id"]
            if eid in existing:
                prev = existing[eid]
                if prev.get("status") == "done":
                    obj.update({"status": "pending"})
                else:
                    if prev.get("status") == "leased" and prev.get("lease_expires_at", 0) < now:
                        prev["status"] = "pending"
                        prev.pop("lease_id", None)
                        prev.pop("lease_expires_at", None)
                    obj = {**obj, **prev}
            merged.append(obj)

        WORK_QUEUE.parent.mkdir(parents=True, exist_ok=True)
        with WORK_QUEUE.open("w", encoding="utf-8") as wf:
            for obj in merged:
                wf.write(json.dumps(obj) + "\n")

    return filter_stats


def _write_report(
    entries: Dict[str, dict],
    warnings: List[str],
    null_values: List[dict],
    missing_fields: List[dict],
    items_without_recipes: List[dict],
    orphan_resources: List[dict],
    filter_stats: Dict[str, int],
) -> None:
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

    if items_without_recipes:
        by_kind: Dict[str, int] = {}
        for item in items_without_recipes:
            k = item["kind"]
            by_kind[k] = by_kind.get(k, 0) + 1
        lines.append("")
        lines.append("## Items without recipes (will be imports)")
        lines.append(f"Total: {len(items_without_recipes)} items need recipes or import designation")
        for kind, count in sorted(by_kind.items()):
            lines.append(f"- {kind}: {count}")
        lines.append("")
        lines.append("See `out/missing_recipes.jsonl` for details.")

    if missing_fields:
        by_field: Dict[str, int] = {}
        for mf in missing_fields:
            f = mf["field"]
            by_field[f] = by_field.get(f, 0) + 1
        lines.append("")
        lines.append("## Missing required fields")
        lines.append(f"Total: {len(missing_fields)} missing fields")
        for field, count in sorted(by_field.items()):
            lines.append(f"- {field}: {count}")
        lines.append("")
        lines.append("See `out/missing_fields.jsonl` for details.")

    if orphan_resources:
        lines.append("")
        lines.append("## Orphan resources (no machine provides)")
        lines.append(f"Total: {len(orphan_resources)} resource_types have no provider machine")
        for orph in orphan_resources[:10]:
            needed = len(orph.get("refs_in", []))
            lines.append(f"- {orph['id']} (needed by {needed} processes)")
        if len(orphan_resources) > 10:
            lines.append(f"- ... and {len(orphan_resources) - 10} more")
        lines.append("")
        lines.append("See `out/orphan_resources.jsonl` for details.")

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

    if filter_stats.get("filtering_enabled"):
        lines.append("")
        lines.append("## Queue Filtering")
        lines.append(f"**Status**: Enabled")
        if filter_stats.get("current_mode"):
            lines.append(f"**Mode**: {filter_stats['current_mode']}")
        lines.append(f"**Total gaps found**: {filter_stats['total_gaps']}")
        lines.append(f"**Filtered out**: {filter_stats['filtered_count']}")
        lines.append(f"**Added to queue**: {filter_stats['queued_count']}")
        if filter_stats['filtered_count'] > 0:
            pct = (filter_stats['filtered_count'] / filter_stats['total_gaps']) * 100
            lines.append(f"**Filtering rate**: {pct:.1f}%")

    total_gaps = (
        len(items_without_recipes) + len(missing_fields) +
        len(orphan_resources) + len(null_values)
    )
    lines.append("")
    lines.append("## Work queue summary")
    lines.append(f"Total gaps in work queue: see `out/work_queue.jsonl`")

    with (OUT_DIR / "validation_report.md").open("w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def main() -> None:
    entries = build_index()
    print(f"Indexed {len(entries)} entries into {OUT_DIR/'index.json'}")


if __name__ == "__main__":  # pragma: no cover
    main()
