"""
DEPRECATED: This file is deprecated and should be migrated to src/

Indexer for the v0 KB. Scans kb/**/*.yaml, performs permissive parsing,
and emits:
- out/index.json (entries + refs)
- out/validation_report.md (soft warnings)
- out/unresolved_refs.jsonl (requires_text and other unresolved strings)
- out/work_queue.jsonl (all gaps needing attention)
- out/missing_recipes.jsonl (items without recipes)
- out/missing_fields.jsonl (required fields not populated)
- out/orphan_resources.jsonl (resource_types with no provider machine)
- out/missing_recipe_items.jsonl (items referenced in recipe steps but not defined)

TODO: Migrate to src/kb_core/indexer.py or src/indexer/index_builder.py
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
from base_builder.kb_loader import KBLoader
from src.kb_core.validators import validate_process, validate_recipe, ValidationLevel
from src.kb_core.unit_converter import UnitConverter

KB_ROOT = Path("kb")
OUT_DIR = Path("out")
WORK_QUEUE = OUT_DIR / "work_queue.jsonl"
WORK_QUEUE_LOCK = OUT_DIR / "work_queue.lock"


def _infer_kind(path: Path, data: dict) -> Optional[str]:
    kind = data.get("kind")
    if kind:
        return kind
    parts = path.parts
    if "imports" in parts:
        # Infer kind from data or default to material for import items
        return data.get("kind", "material")
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
                # Collect items from step inputs, outputs, and byproducts
                for inp in step.get("inputs", []) or []:
                    item_id = inp.get("item_id")
                    if item_id:
                        refs.add(str(item_id))
                for out in step.get("outputs", []) or []:
                    item_id = out.get("item_id")
                    if item_id:
                        refs.add(str(item_id))
                for byp in step.get("byproducts", []) or []:
                    item_id = byp.get("item_id")
                    if item_id:
                        refs.add(str(item_id))
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


def _analyze_recipe_items(kb_files: List[Path], entries: Dict[str, dict], warnings: List[str]) -> List[dict]:
    """
    Analyze all recipe items to find missing external inputs and intermediate parts.
    Returns list of missing recipe items with classification and usage context.
    """
    if yaml is None:
        return []

    # Track item usage across all recipes
    item_usage: Dict[str, dict] = {}  # item_id -> {as_input: [recipes], as_output: [recipes], as_target: [recipes]}

    for path in kb_files:
        data = _load_yaml(path, warnings)
        kind = _infer_kind(path, data)

        if kind != "recipe":
            continue

        recipe_id = data.get("id") or path.stem
        target = data.get("target_item_id")

        # Track target
        if target:
            if target not in item_usage:
                item_usage[target] = {"as_input": [], "as_output": [], "as_target": []}
            item_usage[target]["as_target"].append(recipe_id)

        # Track step-level items
        steps = data.get("steps", []) or []
        for step in steps:
            if not isinstance(step, dict):
                continue

            # Track inputs
            for inp in step.get("inputs", []) or []:
                item_id = inp.get("item_id")
                if item_id:
                    if item_id not in item_usage:
                        item_usage[item_id] = {"as_input": [], "as_output": [], "as_target": []}
                    if recipe_id not in item_usage[item_id]["as_input"]:
                        item_usage[item_id]["as_input"].append(recipe_id)

            # Track outputs
            for out in step.get("outputs", []) or []:
                item_id = out.get("item_id")
                if item_id:
                    if item_id not in item_usage:
                        item_usage[item_id] = {"as_input": [], "as_output": [], "as_target": []}
                    if recipe_id not in item_usage[item_id]["as_output"]:
                        item_usage[item_id]["as_output"].append(recipe_id)

            # Track byproducts
            for byp in step.get("byproducts", []) or []:
                item_id = byp.get("item_id")
                if item_id:
                    if item_id not in item_usage:
                        item_usage[item_id] = {"as_input": [], "as_output": [], "as_target": []}
                    if recipe_id not in item_usage[item_id]["as_output"]:
                        item_usage[item_id]["as_output"].append(recipe_id)

    # Classify missing items
    missing_recipe_items: List[dict] = []

    for item_id, usage in item_usage.items():
        # Skip if item is defined in KB
        if item_id in entries and entries[item_id].get("status") == "defined":
            continue

        as_input = usage["as_input"]
        as_output = usage["as_output"]
        as_target = usage["as_target"]

        # Determine classification
        is_target = len(as_target) > 0
        is_produced = len(as_output) > 0
        is_consumed = len(as_input) > 0
        used_in_multiple_recipes = len(set(as_input + as_output + as_target)) > 1

        # Classify
        if is_target:
            classification = "missing_recipe_target"
        elif is_produced and is_consumed and used_in_multiple_recipes:
            classification = "missing_intermediate_part"
        elif is_produced and is_consumed and not used_in_multiple_recipes:
            classification = "pure_intermediate"
        elif is_consumed and not is_produced:
            classification = "missing_recipe_input"
        elif is_produced and not is_consumed:
            classification = "unused_recipe_output"
        else:
            classification = "unknown_recipe_item"

        missing_recipe_items.append({
            "item_id": item_id,
            "classification": classification,
            "used_as_input_in": as_input,
            "used_as_output_in": as_output,
            "used_as_target_in": as_target,
            "total_recipe_count": len(set(as_input + as_output + as_target)),
        })

    return missing_recipe_items


def _validate_recipe_inputs(kb_files: List[Path], warnings: List[str]) -> List[dict]:
    """
    Validate that recipes have inputs defined in their steps.
    Returns list of recipes where ALL steps have no inputs.
    """
    if yaml is None:
        return []

    recipes_no_inputs: List[dict] = []

    for path in kb_files:
        data = _load_yaml(path, warnings)
        kind = _infer_kind(path, data)

        if kind != "recipe":
            continue

        recipe_id = data.get("id") or path.stem
        target_item_id = data.get("target_item_id")
        variant_id = data.get("variant_id", "")

        # Skip import stubs
        if "import" in str(variant_id):
            continue

        steps = data.get("steps", []) or []
        if not steps:
            continue

        # Check if ANY step has inputs
        has_any_inputs = False
        for step in steps:
            if not isinstance(step, dict):
                continue

            inputs = step.get("inputs", []) or []
            if inputs:
                has_any_inputs = True
                break

        # If no steps have inputs, this is incomplete
        if not has_any_inputs:
            recipes_no_inputs.append({
                "recipe_id": recipe_id,
                "target_item_id": target_item_id,
                "file": str(path),
                "step_count": len(steps),
            })

    return recipes_no_inputs


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
    # Skip items marked as imports or scrap (is_import/is_scrap: true)
    items_without_recipes: List[dict] = []
    for entry in entries.values():
        if entry["kind"] in ("part", "material", "machine") and entry["id"] not in recipe_targets:
            # Check if item is marked as import by reading the file
            is_import = False
            is_scrap = False
            if entry.get("defined_in"):
                try:
                    file_path = Path(entry["defined_in"])
                    if file_path.exists():
                        with file_path.open("r", encoding="utf-8") as f:
                            item_data = yaml.safe_load(f) or {}
                            is_import = item_data.get("is_import", False)
                            is_scrap = item_data.get("is_scrap", False)
                except Exception:
                    pass

            # Skip import or scrap items
            if is_import or is_scrap:
                continue

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

    # Analyze recipe items to find missing inputs and intermediate parts
    missing_recipe_items = _analyze_recipe_items(kb_files, entries, warnings)

    # Validate that recipes have inputs defined
    # DISABLED 2025-12-24: Validation moved to closure analyzer which properly
    # checks recipe-level inputs, step-level inputs, AND process-level inputs.
    # See ADR-006 addendum for details.
    recipes_no_inputs = []  # _validate_recipe_inputs(kb_files, warnings)

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

    with (OUT_DIR / "missing_recipe_items.jsonl").open("w", encoding="utf-8") as f:
        for mri in missing_recipe_items:
            f.write(json.dumps(mri) + "\n")

    with (OUT_DIR / "recipes_no_inputs.jsonl").open("w", encoding="utf-8") as f:
        for rni in recipes_no_inputs:
            f.write(json.dumps(rni) + "\n")

    # Load KB for circular dependency detection and closure analysis
    kb_loader = KBLoader(KB_ROOT)
    kb_loader.load_all()

    # Collect closure analysis errors from all machines
    print("Running closure analysis on all machines...")
    closure_errors = _collect_closure_errors(entries, kb_loader)
    print(f"Found {len(closure_errors)} unique closure errors")

    # Collect validation issues (ADR-017)
    validation_issues = _collect_validation_issues(entries, kb_loader)

    filter_stats = _update_work_queue(
        unresolved_refs, referenced_only, import_stubs,
        items_without_recipes, missing_fields, orphan_resources, invalid_recipes,
        missing_recipe_items, recipes_no_inputs, seed_references, item_metadata,
        entries, kb_loader, closure_errors, validation_issues
    )
    _write_report(
        entries, warnings, null_values, missing_fields,
        items_without_recipes, orphan_resources, missing_recipe_items, recipes_no_inputs,
        filter_stats, validation_issues
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


def _detect_circular_dependencies(entries: Dict[str, dict], kb_loader) -> List[dict]:
    """
    Detect circular dependencies and return queue items.

    Args:
        entries: Index entries dict (item_id -> entry data)
        kb_loader: KBLoader instance for dependency analysis

    Returns:
        List of queue items (one per unique normalized loop)
    """
    from .circular_dependency_fixer import CircularDependencyFixer

    fixer = CircularDependencyFixer(kb_loader)
    queue_items = fixer.get_work_queue_items(entries)

    # Write to output file
    circ_dep_path = OUT_DIR / "circular_dependencies.jsonl"
    try:
        with circ_dep_path.open("w", encoding="utf-8") as f:
            for item in queue_items:
                f.write(json.dumps(item) + "\n")
    except Exception:
        # Best-effort; do not crash indexing if this fails
        pass

    return queue_items


def _collect_closure_errors(entries: Dict[str, dict], kb_loader) -> List[dict]:
    """
    Run closure analysis on all machines and collect errors as queue items.

    Args:
        entries: Index entries dict (item_id -> entry data)
        kb_loader: KBLoader instance for closure analysis

    Returns:
        List of unique queue items from closure analysis errors
    """
    from .closure_analysis import ClosureAnalyzer
    import re

    analyzer = ClosureAnalyzer(kb_loader)
    error_map = {}  # Deduplicate by error signature

    # Get all machine IDs
    machine_ids = [eid for eid, entry in entries.items() if entry.get('kind') == 'machine']

    for machine_id in machine_ids:
        result = analyzer.analyze_machine(machine_id)

        for error in result.get('errors', []):
            # Parse error to extract item_id, recipe_id, process_id
            # Create a signature for deduplication

            # Patterns to extract IDs from error messages
            item_match = re.search(r"Item '([^']+)'", error)
            recipe_match = re.search(r"Recipe '([^']+)'", error)
            process_match = re.search(r"Process '([^']+)'", error)
            bom_match = re.search(r"BOM '([^']+)'", error)
            machine_match = re.search(r"Machine '([^']+)'", error)

            item_id = item_match.group(1) if item_match else None
            recipe_id = recipe_match.group(1) if recipe_match else None
            process_id = process_match.group(1) if process_match else None
            bom_id = bom_match.group(1) if bom_match else None
            machine_id_from_error = machine_match.group(1) if machine_match else None

            # Determine gap type from error message
            gap_type = "closure_error"
            reason = "closure_error"

            if "not found in KB" in error:
                gap_type = "item_not_found"
                reason = "item_not_found"
            elif "has no recipe and is not a raw material" in error:
                gap_type = "no_recipe"
                reason = "no_recipe_not_raw"
            elif "Recipe" in error and "not found" in error:
                gap_type = "recipe_not_found"
                reason = "recipe_not_found"
            elif "Process" in error and "not found" in error:
                gap_type = "process_not_found"
                reason = "process_not_found"
            elif "null/zero quantity" in error:
                gap_type = "null_quantity"
                reason = "null_quantity"
            elif "has no inputs" in error:
                gap_type = "recipe_no_inputs"
                reason = "recipe_no_inputs"
            elif "Bootstrap import (circular)" in error:
                # Skip circular import errors - already handled by circular dependency detection
                continue

            # Create unique signature for deduplication
            signature = f"{gap_type}:{item_id or recipe_id or process_id or bom_id or machine_id_from_error or error[:50]}"

            if signature not in error_map:
                # Determine the primary ID for the queue item
                primary_id = item_id or recipe_id or process_id or bom_id or machine_id_from_error or "unknown"

                error_map[signature] = {
                    "id": f"closure:{gap_type}:{primary_id}",
                    "kind": "gap",
                    "reason": reason,
                    "gap_type": gap_type,
                    "item_id": primary_id,
                    "context": {
                        "error_message": error,
                        "detected_in_machine": machine_id,
                        "item_id": item_id,
                        "recipe_id": recipe_id,
                        "process_id": process_id,
                        "bom_id": bom_id,
                        "machine_id": machine_id_from_error,
                    }
                }

    # Write to output file
    closure_errors_path = OUT_DIR / "closure_errors.jsonl"
    queue_items = list(error_map.values())
    try:
        with closure_errors_path.open("w", encoding="utf-8") as f:
            for item in queue_items:
                f.write(json.dumps(item) + "\n")
    except Exception:
        # Best-effort; do not crash indexing if this fails
        pass

    return queue_items


def _collect_validation_issues(entries: Dict[str, dict], kb_loader) -> List[dict]:
    """
    Run ADR-017 validation on all processes and recipes.

    Args:
        entries: Index entries dict (item_id -> entry data)
        kb_loader: KBLoader instance with loaded KB data

    Returns:
        List of validation issue queue items (ERROR and WARNING levels only)
    """
    print("Running ADR-017 validation on processes and recipes...")

    # Create UnitConverter for validation
    converter = UnitConverter(kb_loader)

    all_issues = []
    issue_map = {}  # Deduplicate by signature

    # Validate all processes
    process_ids = [eid for eid, entry in entries.items() if entry.get('kind') == 'process']
    for process_id in process_ids:
        process_data = kb_loader.processes.get(process_id)
        if not process_data:
            continue

        # Run validation
        issues = validate_process(process_data, converter)

        # Filter to ERROR and WARNING only (skip INFO)
        issues = [i for i in issues if i.level in (ValidationLevel.ERROR, ValidationLevel.WARNING)]

        for issue in issues:
            # Create unique signature for deduplication
            signature = f"{issue.entity_type}:{issue.entity_id}:{issue.rule}:{issue.field_path or ''}"

            if signature not in issue_map:
                # Determine if issue is auto-fixable
                auto_fixable_rules = {
                    'process_type_required',
                    'deprecated_field',
                    'setup_hr_in_continuous',
                    'target_item_id_required'
                }
                is_auto_fixable = issue.rule in auto_fixable_rules

                # Determine priority (higher number = higher priority)
                # ERROR validation = 100, WARNING = 50, INFO = 10
                priority = {
                    ValidationLevel.ERROR: 100,
                    ValidationLevel.WARNING: 50,
                    ValidationLevel.INFO: 10
                }.get(issue.level, 0)

                # Boost priority for auto-fixable issues
                if is_auto_fixable:
                    priority += 20

                # Convert ValidationIssue to queue item
                queue_item = {
                    "id": f"validation:{issue.level.value}:{issue.entity_type}:{issue.entity_id}:{issue.rule}",
                    "kind": issue.entity_type,
                    "reason": f"validation_{issue.level.value}",
                    "gap_type": f"validation_{issue.rule}",
                    "item_id": issue.entity_id,
                    "priority": priority,
                    "auto_fixable": is_auto_fixable,
                    "context": {
                        "validation_level": issue.level.value,
                        "category": issue.category,
                        "rule": issue.rule,
                        "message": issue.message,
                        "field_path": issue.field_path,
                        "fix_hint": issue.fix_hint,
                        "file": entries.get(issue.entity_id, {}).get("defined_in"),
                        "auto_fixable": is_auto_fixable,
                    }
                }
                issue_map[signature] = queue_item
                all_issues.append(issue)

    # Validate all recipes
    recipe_ids = [eid for eid, entry in entries.items() if entry.get('kind') == 'recipe']
    for recipe_id in recipe_ids:
        recipe_data = kb_loader.recipes.get(recipe_id)
        if not recipe_data:
            continue

        # Run validation
        issues = validate_recipe(recipe_data)

        # Filter to ERROR and WARNING only (skip INFO)
        issues = [i for i in issues if i.level in (ValidationLevel.ERROR, ValidationLevel.WARNING)]

        for issue in issues:
            # Create unique signature for deduplication
            signature = f"{issue.entity_type}:{issue.entity_id}:{issue.rule}:{issue.field_path or ''}"

            if signature not in issue_map:
                # Determine if issue is auto-fixable
                auto_fixable_rules = {
                    'process_type_required',
                    'deprecated_field',
                    'setup_hr_in_continuous',
                    'target_item_id_required'
                }
                is_auto_fixable = issue.rule in auto_fixable_rules

                # Determine priority (higher number = higher priority)
                # ERROR validation = 100, WARNING = 50, INFO = 10
                priority = {
                    ValidationLevel.ERROR: 100,
                    ValidationLevel.WARNING: 50,
                    ValidationLevel.INFO: 10
                }.get(issue.level, 0)

                # Boost priority for auto-fixable issues
                if is_auto_fixable:
                    priority += 20

                # Convert ValidationIssue to queue item
                queue_item = {
                    "id": f"validation:{issue.level.value}:{issue.entity_type}:{issue.entity_id}:{issue.rule}",
                    "kind": issue.entity_type,
                    "reason": f"validation_{issue.level.value}",
                    "gap_type": f"validation_{issue.rule}",
                    "item_id": issue.entity_id,
                    "priority": priority,
                    "auto_fixable": is_auto_fixable,
                    "context": {
                        "validation_level": issue.level.value,
                        "category": issue.category,
                        "rule": issue.rule,
                        "message": issue.message,
                        "field_path": issue.field_path,
                        "fix_hint": issue.fix_hint,
                        "file": entries.get(issue.entity_id, {}).get("defined_in"),
                        "auto_fixable": is_auto_fixable,
                    }
                }
                issue_map[signature] = queue_item
                all_issues.append(issue)

    # Write to output file
    validation_issues_path = OUT_DIR / "validation_issues.jsonl"
    queue_items = list(issue_map.values())
    try:
        with validation_issues_path.open("w", encoding="utf-8") as f:
            for issue in all_issues:
                # Write full ValidationIssue details for debugging
                f.write(json.dumps({
                    "level": issue.level.value,
                    "category": issue.category,
                    "rule": issue.rule,
                    "entity_type": issue.entity_type,
                    "entity_id": issue.entity_id,
                    "message": issue.message,
                    "field_path": issue.field_path,
                    "fix_hint": issue.fix_hint,
                }) + "\n")
    except Exception:
        # Best-effort; do not crash indexing if this fails
        pass

    print(f"Found {len(all_issues)} validation issues ({len([i for i in all_issues if i.level == ValidationLevel.ERROR])} errors, {len([i for i in all_issues if i.level == ValidationLevel.WARNING])} warnings)")

    return queue_items


def _update_work_queue(
    unresolved_refs: List[dict],
    referenced_only: Set[str],
    import_stubs: List[dict],
    items_without_recipes: List[dict],
    missing_fields: List[dict],
    orphan_resources: List[dict],
    invalid_recipes: List[dict],
    missing_recipe_items: List[dict],
    recipes_no_inputs: List[dict],
    seed_references: Dict[str, List[str]],
    item_metadata: Dict[str, dict],
    entries: Dict[str, dict],
    kb_loader,
    closure_errors: List[dict] = None,
    validation_issues: List[dict] = None,
) -> Dict[str, int]:
    """
    Rebuild work queue from current gaps (replaces previous queue).
    - unresolved_refs: free-text refs needing definition/resolution
    - referenced_only: ids referenced but not defined
    - import_stubs: recipes with empty steps/import variants needing real routes
    - items_without_recipes: parts/materials/machines with no recipe
    - missing_fields: required fields not populated (energy_model, time_model, etc.)
    - orphan_resources: resource_types with no machine providing them
    - invalid_recipes: legacy step schema or missing process_id
    - missing_recipe_items: items referenced in recipe steps but not defined
    - recipes_no_inputs: recipes where all steps have no inputs defined
    - seed_references: item_id -> list of seed file ids that reference it
    - item_metadata: item_id -> freeform metadata from seed requires_ids
    - validation_issues: ADR-017 validation errors and warnings

    Returns dict of filter statistics.
    """
    from .config import QueueFilterConfig

    gap_items: List[dict] = []

    # Detect circular dependencies
    circular_dependencies = _detect_circular_dependencies(entries, kb_loader)
    gap_items.extend(circular_dependencies)

    # Add closure analysis errors
    if closure_errors:
        gap_items.extend(closure_errors)

    # Add validation issues (ADR-017)
    if validation_issues:
        gap_items.extend(validation_issues)

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

    # Missing recipe items (items referenced in recipe steps but not defined)
    for mri in missing_recipe_items:
        classification = mri.get("classification", "unknown")
        gap_items.append(
            {
                "id": f"{classification}:{mri['item_id']}",
                "kind": "item",  # Generic, will be determined during fix
                "reason": classification,
                "gap_type": classification,
                "item_id": mri["item_id"],
                "context": {
                    "used_as_input_in": mri.get("used_as_input_in", []),
                    "used_as_output_in": mri.get("used_as_output_in", []),
                    "used_as_target_in": mri.get("used_as_target_in", []),
                    "total_recipe_count": mri.get("total_recipe_count", 0),
                },
            }
        )

    # Recipes with no inputs (incomplete recipes)
    for rni in recipes_no_inputs:
        gap_items.append(
            {
                "id": f"recipe_no_inputs:{rni['recipe_id']}",
                "kind": "recipe",
                "reason": "recipe_no_inputs",
                "gap_type": "recipe_no_inputs",
                "item_id": rni.get("target_item_id"),
                "recipe_id": rni["recipe_id"],
                "context": {
                    "recipe_id": rni["recipe_id"],
                    "target_item_id": rni.get("target_item_id"),
                    "step_count": rni.get("step_count", 0),
                    "file": rni["file"],
                },
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

        # Preserve leased items that are no longer in gap_items (they were resolved)
        # This allows agents to successfully complete items they fixed
        merged_ids = {obj["id"] for obj in merged}
        for eid, prev in existing.items():
            if eid not in merged_ids and prev.get("status") == "leased":
                # Gap was resolved while leased - mark as resolved so agent can complete it
                if prev.get("lease_expires_at", 0) >= now:
                    # Only preserve if lease is still valid
                    prev["status"] = "resolved"
                    merged.append(prev)

        # Preserve manually-added items that aren't auto-detected by indexer
        # Manual items (source="manual" or source="agent") persist until explicitly completed/released
        for eid, prev in existing.items():
            if eid not in merged_ids and prev.get("source") in ("manual", "agent"):
                # Only preserve if not already done/superseded
                if prev.get("status") not in ("done", "superseded"):
                    merged.append(prev)

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
    missing_recipe_items: List[dict],
    recipes_no_inputs: List[dict],
    filter_stats: Dict[str, int],
    validation_issues: List[dict] = None,
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

    if missing_recipe_items:
        by_classification: Dict[str, List[dict]] = {}
        for mri in missing_recipe_items:
            classification = mri.get("classification", "unknown")
            if classification not in by_classification:
                by_classification[classification] = []
            by_classification[classification].append(mri)

        lines.append("")
        lines.append("## Missing recipe items")
        lines.append(f"Total: {len(missing_recipe_items)} items referenced in recipes but not defined")

        # Show breakdown by classification
        for classification, items in sorted(by_classification.items()):
            lines.append("")
            lines.append(f"### {classification} ({len(items)} items)")
            for mri in items[:10]:
                recipe_count = mri.get("total_recipe_count", 0)
                lines.append(f"- {mri['item_id']} (used in {recipe_count} recipe(s))")
            if len(items) > 10:
                lines.append(f"- ... and {len(items) - 10} more")

        lines.append("")
        lines.append("See `out/missing_recipe_items.jsonl` for details.")

    if recipes_no_inputs:
        lines.append("")
        lines.append("## Recipes with no inputs")
        lines.append(f"Total: {len(recipes_no_inputs)} recipes have steps but no inputs defined")
        for rni in recipes_no_inputs[:10]:
            target = rni.get("target_item_id", "unknown")
            steps = rni.get("step_count", 0)
            lines.append(f"- {rni['recipe_id']} (target: {target}, {steps} step(s))")
        if len(recipes_no_inputs) > 10:
            lines.append(f"- ... and {len(recipes_no_inputs) - 10} more")
        lines.append("")
        lines.append("See `out/recipes_no_inputs.jsonl` for details.")

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

    # Read circular dependencies from output file
    circ_dep_path = OUT_DIR / "circular_dependencies.jsonl"
    circular_deps = []
    if circ_dep_path.exists():
        try:
            with circ_dep_path.open("r", encoding="utf-8") as f:
                for line in f:
                    if line.strip():
                        circular_deps.append(json.loads(line))
        except Exception:
            pass

    if circular_deps:
        # Count by loop type
        by_type: Dict[str, int] = {}
        for cd in circular_deps:
            loop_type = cd.get("loop_type", "unknown")
            by_type[loop_type] = by_type.get(loop_type, 0) + 1

        lines.append("")
        lines.append("## Circular Dependencies")
        lines.append(f"Total: {len(circular_deps)} circular dependency loops detected")
        lines.append("")
        lines.append("By type:")
        for loop_type, count in sorted(by_type.items()):
            lines.append(f"- {loop_type}: {count}")
        lines.append("")
        lines.append("Sample loops:")
        for cd in circular_deps[:5]:
            viz = cd.get("context", {}).get("loop_visualization", "unknown")
            loop_type = cd.get("loop_type", "unknown")
            lines.append(f"- [{loop_type}] {viz}")
        if len(circular_deps) > 5:
            lines.append(f"- ... and {len(circular_deps) - 5} more")
        lines.append("")
        lines.append("See `out/circular_dependencies.jsonl` for details.")

    # Validation issues (ADR-017)
    if validation_issues:
        # Count by level and category
        by_level: Dict[str, int] = {}
        by_category: Dict[str, int] = {}
        by_rule: Dict[str, int] = {}

        for issue in validation_issues:
            level = issue.get("context", {}).get("validation_level", "unknown")
            category = issue.get("context", {}).get("category", "unknown")
            rule = issue.get("context", {}).get("rule", "unknown")

            by_level[level] = by_level.get(level, 0) + 1
            by_category[category] = by_category.get(category, 0) + 1
            by_rule[rule] = by_rule.get(rule, 0) + 1

        lines.append("")
        lines.append("## Validation Issues (ADR-017)")
        lines.append(f"Total: {len(validation_issues)} validation issues found")
        lines.append("")

        lines.append("By severity:")
        for level, count in sorted(by_level.items()):
            lines.append(f"- {level}: {count}")

        lines.append("")
        lines.append("By category:")
        for category, count in sorted(by_category.items()):
            lines.append(f"- {category}: {count}")

        lines.append("")
        lines.append("Top validation rules triggered:")
        # Show top 10 rules by count
        sorted_rules = sorted(by_rule.items(), key=lambda x: x[1], reverse=True)
        for rule, count in sorted_rules[:10]:
            lines.append(f"- {rule}: {count}")
        if len(sorted_rules) > 10:
            lines.append(f"- ... and {len(sorted_rules) - 10} more")

        lines.append("")
        lines.append("See `out/validation_issues.jsonl` for details.")

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
