#!/usr/bin/env python3
"""Generate reAM250 BOM research queue tasks from the gold CSV package."""
from __future__ import annotations

import argparse
import csv
import fcntl
import hashlib
import json
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[4]
TASK_DIR = Path("queue_tasks/research_pack/ream250_bom_research")
PACKAGE_ROOT = Path("design/real-mechanical/reAm250/reAM250_cad_gold_package")
PACKAGE_ABS = REPO_ROOT / PACKAGE_ROOT
DEFAULT_BOM = PACKAGE_ROOT / "reAm250_BOM_gold.csv"
DEFAULT_MANIFEST = PACKAGE_ROOT / "gold_export/manifest.csv"
DEFAULT_OUTPUT = Path("out/ream250_bom_research_tasks.jsonl")
DEFAULT_QUEUE = Path("out/work_queue.jsonl")
DEFAULT_LOCK = Path("out/work_queue.lock")
DEFAULT_REGISTRY = Path("queue/gap_type_registry.json")
TASK_PREFIX = "research_task:ream250_bom_row_"
ITEM_PREFIX = "ream250_bom_row_"
OUTPUT_DIR = Path("research/ream250_bom")
VALIDATOR = TASK_DIR / "research_scripts/validate_results.py"
FREECADCMD = Path(".tools/freecad/freecadcmd")


def safe_token(value: str) -> str:
    token = re.sub(r"[^A-Za-z0-9]+", "_", value.strip()).strip("_")
    return token or "unknown"


def repo_relative(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def manifest_key(row: dict[str, str]) -> tuple[str, str, str]:
    return (
        (row.get("source_row_number") or "").strip(),
        (row.get("item") or "").strip(),
        (row.get("cad_file") or "").strip(),
    )


def bom_key(source_row_number: int, row: dict[str, str]) -> tuple[str, str, str]:
    return (
        str(source_row_number),
        (row.get("Item") or "").strip(),
        (row.get("CAD file") or "").strip(),
    )


def extract_step_metadata(paths: list[Path], freecadcmd: Path) -> dict[str, dict[str, Any]]:
    if not paths:
        return {}
    if not freecadcmd.exists():
        raise FileNotFoundError(f"FreeCADCmd wrapper not found: {freecadcmd}")

    script = r"""
import json
import sys

import Part

input_path = sys.argv[2]
output_path = sys.argv[3]

with open(input_path, "r", encoding="utf-8") as f:
    paths = json.load(f)

result = {}
for path in paths:
    try:
        shape = Part.Shape()
        shape.read(path)
        bb = shape.BoundBox
        result[path] = {
            "read_ok": True,
            "solid_count": len(shape.Solids),
            "volume_mm3": shape.Volume,
            "surface_area_mm2": shape.Area,
            "bbox_mm": {
                "x": bb.XLength,
                "y": bb.YLength,
                "z": bb.ZLength,
            },
        }
    except Exception as exc:
        result[path] = {
            "read_ok": False,
            "error": str(exc),
        }

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(result, f, indent=2, sort_keys=True)
"""
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)
        script_path = tmp / "extract_step_metadata.py"
        input_path = tmp / "paths.json"
        output_path = tmp / "metadata.json"
        script_path.write_text(script, encoding="utf-8")
        input_path.write_text(
            json.dumps([str(path) for path in paths], indent=2),
            encoding="utf-8",
        )
        proc = subprocess.run(
            [str(freecadcmd), str(script_path), str(input_path), str(output_path)],
            cwd=REPO_ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        if proc.returncode != 0:
            raise RuntimeError(
                "FreeCAD metadata extraction failed\n"
                f"stdout:\n{proc.stdout}\n"
                f"stderr:\n{proc.stderr}"
            )
        data = json.loads(output_path.read_text(encoding="utf-8"))
    return {str(Path(path)): value for path, value in data.items()}


def build_tasks(
    bom_path: Path,
    manifest_path: Path,
    extract_cad_metadata: bool,
    freecadcmd: Path,
) -> list[dict[str, Any]]:
    bom_rows = read_csv(bom_path)
    manifest_rows = read_csv(manifest_path)
    manifest = {manifest_key(row): row for row in manifest_rows}

    metadata_by_path: dict[str, dict[str, Any]] = {}
    if extract_cad_metadata:
        paths: list[Path] = []
        seen: set[Path] = set()
        for row in manifest_rows:
            rel = (row.get("canonical_step_path") or "").strip()
            if not rel:
                continue
            step_path = (PACKAGE_ABS / rel).resolve()
            if step_path.exists() and step_path not in seen:
                paths.append(step_path)
                seen.add(step_path)
        metadata_by_path = extract_step_metadata(paths, freecadcmd.resolve())

    tasks: list[dict[str, Any]] = []
    for ordinal, row in enumerate(bom_rows, start=1):
        source_row_number = ordinal + 1
        item = (row.get("Item") or "").strip()
        cad_file = (row.get("CAD file") or "").strip()
        key = bom_key(source_row_number, row)
        manifest_row = manifest.get(key)
        if not manifest_row:
            raise ValueError(f"no manifest match for BOM row {source_row_number}: {key}")

        item_id = f"{ITEM_PREFIX}{source_row_number:04d}_{safe_token(item)}"
        output_path = OUTPUT_DIR / f"{item_id}.md"
        canonical_rel = (manifest_row.get("canonical_step_path") or "").strip()
        canonical_path_abs = (PACKAGE_ABS / canonical_rel).resolve() if canonical_rel else None
        canonical_path = repo_relative(canonical_path_abs) if canonical_path_abs else ""
        canonical_abs = str(canonical_path_abs) if canonical_path_abs else ""
        cad_metadata = metadata_by_path.get(canonical_abs)
        cad_hash = ""
        if canonical_path_abs and canonical_path_abs.exists():
            cad_hash = hashlib.sha256(canonical_path_abs.read_bytes()).hexdigest()

        context: dict[str, Any] = {
            "source_csv": repo_relative(bom_path),
            "manifest_csv": repo_relative(manifest_path),
            "bom_row_number": str(source_row_number),
            "source_row_number": source_row_number,
            "item": item,
            "quantity": (row.get("Qty") or "").strip(),
            "cad_file": cad_file,
            "description_or_product_id": (row.get("Description / Product ID") or "").strip(),
            "manufacturer": (row.get("Manufacturer") or "").strip(),
            "third_party_link_url": (row.get("Link URL") or "").strip(),
            "subsystem_suggested": (row.get("Subsystem (suggested)") or "").strip(),
            "material_family_hint": (row.get("Material family") or "").strip(),
            "specific_material_grade_hint": (row.get("Specific material / grade") or "").strip(),
            "notes_from_gold_csv": (row.get("Notes") or "").strip(),
            "raw_row_text": (row.get("Raw row text") or "").strip(),
            "canonical_step_path": canonical_path,
            "alternate_step_paths": (manifest_row.get("alternate_step_paths") or "").strip(),
            "cad_export_status": (manifest_row.get("export_status") or "").strip(),
            "cad_export_kind": (manifest_row.get("export_kind") or "").strip(),
            "cad_source_object_label": (manifest_row.get("source_object_label") or "").strip(),
            "cad_parent_assembly": (manifest_row.get("parent_assembly") or "").strip(),
            "cad_instance_count_found": (manifest_row.get("instance_count_found") or "").strip(),
            "cad_notes": (manifest_row.get("notes") or "").strip(),
            "cad_sha256": cad_hash,
            "cad_evidence_limited": (manifest_row.get("export_status") or "").strip()
            not in {"matched_existing"},
            "required_outputs": ["function", "mass", "material", "how_to_make"],
            "output_path": str(output_path),
            "output_validator": str(VALIDATOR),
            "done_criteria": (
                "Write the result to output_path. Include YAML frontmatter with "
                "function, mass, material, and how_to_make sections; each section "
                "must include its own source object. Validate the result and complete "
                "the queue task with --require-output --validate-output."
            ),
        }
        if cad_metadata is not None:
            context["cad_metadata"] = cad_metadata

        tasks.append(
            {
                "kind": "research",
                "gap_type": "research_task",
                "item_id": item_id,
                "source": "manual",
                "description": (
                    f"Research reAM250 BOM row {source_row_number} item {item} "
                    f"({cad_file}) for function, mass, material, and manufacturing."
                ),
                "context": context,
            }
        )
    return tasks


def write_jsonl(path: Path, tasks: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for task in tasks:
            f.write(json.dumps(task, ensure_ascii=False, sort_keys=True) + "\n")


def queue_entry_for_task(task: dict[str, Any]) -> dict[str, Any]:
    context = dict(task.get("context") or {})
    context["added_at"] = time.time()
    gap_type = task["gap_type"]
    item_id = task["item_id"]
    if task.get("description") and "description" not in context:
        context["description"] = task["description"]
    return {
        "id": f"{gap_type}:{item_id}",
        "kind": task.get("kind", "gap"),
        "reason": gap_type,
        "gap_type": gap_type,
        "item_id": item_id,
        "source": task.get("source", "manual"),
        "context": context,
        "status": "pending",
    }


def replace_queue_prefix(queue_path: Path, lock_path: Path, tasks: list[dict[str, Any]]) -> int:
    queue_path.parent.mkdir(parents=True, exist_ok=True)
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    with lock_path.open("w") as lockf:
        fcntl.flock(lockf, fcntl.LOCK_EX)
        try:
            existing: list[dict[str, Any]] = []
            if queue_path.exists():
                for line in queue_path.read_text(encoding="utf-8").splitlines():
                    if not line.strip():
                        continue
                    try:
                        obj = json.loads(line)
                    except Exception:
                        continue
                    if not str(obj.get("id", "")).startswith(TASK_PREFIX):
                        existing.append(obj)
            new_entries = [queue_entry_for_task(task) for task in tasks]
            with queue_path.open("w", encoding="utf-8") as f:
                for obj in existing + new_entries:
                    f.write(json.dumps(obj, ensure_ascii=False, sort_keys=True) + "\n")
            return len(new_entries)
        finally:
            fcntl.flock(lockf, fcntl.LOCK_UN)


def ensure_research_task_registry(registry_path: Path, usage_count: int) -> None:
    registry_path.parent.mkdir(parents=True, exist_ok=True)
    if registry_path.exists():
        try:
            registry = json.loads(registry_path.read_text(encoding="utf-8"))
        except Exception:
            registry = {}
    else:
        registry = {}

    entry = registry.setdefault(
        "research_task",
        {
            "description": "Manual research task completed by writing task-specific artifacts.",
            "created_by": "ream250_bom_research_task_pack",
            "created_at": time.time(),
            "usage_count": 0,
            "source": "manual",
        },
    )
    entry["description"] = entry.get("description") or "Manual research task completed by writing task-specific artifacts."
    entry["source"] = entry.get("source") or "manual"
    entry["usage_count"] = usage_count
    registry_path.write_text(json.dumps(registry, indent=2), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bom", type=Path, default=DEFAULT_BOM)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--extract-cad-metadata", action="store_true")
    parser.add_argument("--freecadcmd", type=Path, default=FREECADCMD)
    parser.add_argument(
        "--replace-queue-prefix",
        action="store_true",
        help="Replace existing out/work_queue.jsonl entries with the reAM250 task prefix.",
    )
    parser.add_argument("--queue", type=Path, default=DEFAULT_QUEUE)
    parser.add_argument("--lock", type=Path, default=DEFAULT_LOCK)
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    args = parser.parse_args()

    bom_path = args.bom if args.bom.is_absolute() else REPO_ROOT / args.bom
    manifest_path = args.manifest if args.manifest.is_absolute() else REPO_ROOT / args.manifest
    output_path = args.output if args.output.is_absolute() else REPO_ROOT / args.output
    freecadcmd = args.freecadcmd if args.freecadcmd.is_absolute() else REPO_ROOT / args.freecadcmd
    queue_path = args.queue if args.queue.is_absolute() else REPO_ROOT / args.queue
    lock_path = args.lock if args.lock.is_absolute() else REPO_ROOT / args.lock
    registry_path = args.registry if args.registry.is_absolute() else REPO_ROOT / args.registry

    tasks = build_tasks(
        bom_path,
        manifest_path,
        args.extract_cad_metadata,
        freecadcmd,
    )
    write_jsonl(output_path, tasks)
    print(f"Wrote {len(tasks)} tasks to {repo_relative(output_path)}")

    if args.replace_queue_prefix:
        added = replace_queue_prefix(queue_path, lock_path, tasks)
        ensure_research_task_registry(registry_path, added)
        print(f"Replaced {TASK_PREFIX} entries in {repo_relative(queue_path)} with {added} pending tasks")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
