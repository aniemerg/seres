from __future__ import annotations

import csv
import json
import re
import time
import sqlite3
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

import yaml


MISSION_MANIFEST = "mission_manifest.yaml"
STATE_DB = "state.sqlite"


class ResearchMissionError(RuntimeError):
    """Raised for invalid mission state or user-facing research CLI errors."""


def load_manifest(mission_dir: Path) -> Dict[str, Any]:
    manifest_path = mission_dir / MISSION_MANIFEST
    if not manifest_path.exists():
        raise ResearchMissionError(f"Missing {MISSION_MANIFEST} in {mission_dir}")
    with manifest_path.open(encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    if not isinstance(data, dict):
        raise ResearchMissionError(f"{manifest_path} must contain a YAML mapping")
    if not data.get("id"):
        raise ResearchMissionError(f"{manifest_path} must define id")
    return data


def mission_path(mission_dir: Path, path_value: str | Path) -> Path:
    path = Path(path_value)
    if path.is_absolute():
        return path
    return mission_dir / path


def now_ts() -> float:
    return time.time()


def slugify(value: str, fallback: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "_", value.strip().lower()).strip("_")
    return slug or fallback


def normalize_key(value: str) -> str:
    return re.sub(r"\s+", " ", str(value or "").strip().lower())


def get_first(record: Dict[str, Any], names: Iterable[str], default: str = "") -> str:
    lowered = {str(k).lower(): k for k in record.keys()}
    for name in names:
        key = lowered.get(name.lower())
        if key is not None and record.get(key) not in (None, ""):
            return str(record[key]).strip()
    return default


def parse_float(value: Any) -> Optional[float]:
    if value in (None, ""):
        return None
    try:
        return float(str(value).replace(",", ""))
    except ValueError:
        return None


def read_records(path: Path) -> List[Dict[str, Any]]:
    if not path.exists():
        raise ResearchMissionError(f"Input file not found: {path}")

    suffix = path.suffix.lower()
    if suffix == ".csv":
        with path.open(newline="", encoding="utf-8-sig") as f:
            return [dict(row) for row in csv.DictReader(f)]

    if suffix == ".jsonl":
        records: List[Dict[str, Any]] = []
        with path.open(encoding="utf-8") as f:
            for line_no, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                obj = json.loads(line)
                if not isinstance(obj, dict):
                    raise ResearchMissionError(f"JSONL line {line_no} must be an object")
                records.append(obj)
        return records

    if suffix == ".json":
        with path.open(encoding="utf-8") as f:
            obj = json.load(f)
        if isinstance(obj, list) and all(isinstance(item, dict) for item in obj):
            return list(obj)
        raise ResearchMissionError(f"JSON input must be an array of objects: {path}")

    raise ResearchMissionError(f"Unsupported input file type: {path.suffix}")


def load_source_catalog(mission_dir: Path, manifest: Dict[str, Any]) -> List[Dict[str, Any]]:
    catalog = (manifest.get("input") or {}).get("source_catalog")
    if not catalog:
        return []
    catalog_path = mission_path(mission_dir, catalog)
    if not catalog_path.exists():
        return []
    return read_records(catalog_path)


def source_files_for_part(
    mission_dir: Path,
    primary_file: Path,
    catalog: List[Dict[str, Any]],
    part_number: str,
    part_name: str,
) -> List[str]:
    files = [str(primary_file.relative_to(mission_dir)) if primary_file.is_relative_to(mission_dir) else str(primary_file)]
    number_norm = normalize_key(part_number)
    name_norm = normalize_key(part_name)
    for row in catalog:
        related_number = normalize_key(get_first(row, ["related_part_number", "part_number", "number"]))
        related_name = normalize_key(get_first(row, ["related_part_name", "part_name", "name"]))
        if related_number and number_norm and related_number != number_norm:
            continue
        if related_name and name_norm and related_name != name_norm:
            continue
        if not related_number and not related_name:
            continue
        path_value = get_first(row, ["path", "file", "source_path"])
        if path_value:
            files.append(path_value)
    return sorted(dict.fromkeys(files))


def build_tasks(mission_dir: Path, manifest: Dict[str, Any]) -> List[Dict[str, Any]]:
    input_cfg = manifest.get("input") or {}
    primary = input_cfg.get("primary_file")
    if not primary:
        raise ResearchMissionError("manifest input.primary_file is required")
    primary_path = mission_path(mission_dir, primary)
    records = read_records(primary_path)
    strategy = (manifest.get("task_generation") or {}).get("strategy", "one_record")
    mission_type = manifest.get("mission_type", "research")
    catalog = load_source_catalog(mission_dir, manifest)

    grouped: Dict[str, List[Tuple[int, Dict[str, Any]]]] = {}
    for index, record in enumerate(records, 1):
        row_id = get_first(record, ["row_id", "row", "source_row", "id"], str(index))
        part_number = get_first(record, ["part_number", "number", "mpn", "manufacturer_part_number"])
        part_name = get_first(record, ["part_name", "name", "item", "description", "title"], f"row {row_id}")

        if strategy in {"unique_part_or_part_family", "unique_part"}:
            key_source = part_number or part_name
        elif strategy in {"one_record", "one_row"}:
            key_source = f"row_{row_id}"
        else:
            raise ResearchMissionError(f"Unsupported task_generation.strategy: {strategy}")

        grouped.setdefault(normalize_key(key_source), []).append((index, record))

    tasks: List[Dict[str, Any]] = []
    used_ids: set[str] = set()
    for group_index, (_key, group_rows) in enumerate(grouped.items(), 1):
        records_only = [record for _, record in group_rows]
        first = records_only[0]
        row_ids = [
            get_first(record, ["row_id", "row", "source_row", "id"], str(index))
            for index, record in group_rows
        ]
        part_number = get_first(first, ["part_number", "number", "mpn", "manufacturer_part_number"])
        part_name = get_first(first, ["part_name", "name", "item", "description", "title"], f"task {group_index}")
        qty_total = 0.0
        any_qty = False
        for record in records_only:
            qty = parse_float(get_first(record, ["qty", "quantity", "count"]))
            if qty is not None:
                any_qty = True
                qty_total += qty

        base_id = f"task_{slugify(part_number or part_name, f'{group_index:06d}')}"
        task_id = base_id
        suffix = 2
        while task_id in used_ids:
            task_id = f"{base_id}_{suffix}"
            suffix += 1
        used_ids.add(task_id)

        payload = {
            "part_number": part_number,
            "part_name": part_name,
            "source_rows": row_ids,
            "qty_total": qty_total if any_qty else None,
            "records": records_only,
        }
        source_files = source_files_for_part(mission_dir, primary_path, catalog, part_number, part_name)

        tasks.append(
            {
                "task_id": task_id,
                "task_type": mission_type,
                "title": part_name,
                "payload": payload,
                "source_files": source_files,
            }
        )

    return tasks


def connect_state(mission_dir: Path) -> sqlite3.Connection:
    mission_dir.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(mission_dir / STATE_DB, timeout=30)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA busy_timeout=30000")
    return conn


def init_state(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            task_id TEXT PRIMARY KEY,
            task_type TEXT NOT NULL,
            title TEXT NOT NULL,
            status TEXT NOT NULL,
            lease_owner TEXT,
            lease_expires_at REAL,
            attempts INTEGER NOT NULL DEFAULT 0,
            payload_json TEXT NOT NULL,
            source_files_json TEXT NOT NULL,
            result_path TEXT,
            error TEXT,
            created_at REAL NOT NULL,
            updated_at REAL NOT NULL
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_id TEXT,
            event_type TEXT NOT NULL,
            agent TEXT,
            message TEXT,
            created_at REAL NOT NULL
        )
        """
    )
    conn.commit()


def task_row_to_dict(row: sqlite3.Row) -> Dict[str, Any]:
    return {
        "task_id": row["task_id"],
        "task_type": row["task_type"],
        "title": row["title"],
        "status": row["status"],
        "lease_owner": row["lease_owner"],
        "lease_expires_at": row["lease_expires_at"],
        "attempts": row["attempts"],
        "payload": json.loads(row["payload_json"]),
        "source_files": json.loads(row["source_files_json"]),
        "result_path": row["result_path"],
        "error": row["error"],
        "created_at": row["created_at"],
        "updated_at": row["updated_at"],
    }


def write_task_files(mission_dir: Path, tasks: List[Dict[str, Any]]) -> None:
    tasks_dir = mission_dir / "tasks"
    tasks_dir.mkdir(parents=True, exist_ok=True)
    for task in tasks:
        path = tasks_dir / f"{task['task_id']}.json"
        with path.open("w", encoding="utf-8") as f:
            json.dump(task, f, indent=2, sort_keys=True)
            f.write("\n")


def ingest_mission(mission_dir: Path, reset: bool = False) -> Dict[str, Any]:
    manifest = load_manifest(mission_dir)
    tasks = build_tasks(mission_dir, manifest)
    conn = connect_state(mission_dir)
    try:
        init_state(conn)
        existing = conn.execute("SELECT COUNT(*) FROM tasks").fetchone()[0]
        if existing and not reset:
            raise ResearchMissionError(
                f"Mission already has {existing} tasks. Use --reset to replace them."
            )
        if reset:
            conn.execute("DELETE FROM events")
            conn.execute("DELETE FROM tasks")
        created = now_ts()
        for task in tasks:
            conn.execute(
                """
                INSERT INTO tasks (
                    task_id, task_type, title, status, payload_json, source_files_json,
                    created_at, updated_at
                ) VALUES (?, ?, ?, 'pending', ?, ?, ?, ?)
                """,
                (
                    task["task_id"],
                    task["task_type"],
                    task["title"],
                    json.dumps(task["payload"], sort_keys=True),
                    json.dumps(task["source_files"], sort_keys=True),
                    created,
                    created,
                ),
            )
        conn.commit()
        write_task_files(mission_dir, tasks)
        return {"mission_id": manifest["id"], "task_count": len(tasks)}
    finally:
        conn.close()


def lease_task(mission_dir: Path, agent: str, ttl: int) -> Optional[Dict[str, Any]]:
    expires = now_ts() + ttl
    conn = connect_state(mission_dir)
    try:
        init_state(conn)
        conn.execute("BEGIN IMMEDIATE")
        now = now_ts()
        conn.execute(
            """
            UPDATE tasks
            SET status = 'pending', lease_owner = NULL, lease_expires_at = NULL, updated_at = ?
            WHERE status = 'leased' AND lease_expires_at < ?
            """,
            (now, now),
        )
        row = conn.execute(
            """
            SELECT * FROM tasks
            WHERE status = 'pending'
            ORDER BY attempts ASC, task_id ASC
            LIMIT 1
            """
        ).fetchone()
        if row is None:
            conn.commit()
            return None
        conn.execute(
            """
            UPDATE tasks
            SET status = 'leased', lease_owner = ?, lease_expires_at = ?,
                attempts = attempts + 1, updated_at = ?
            WHERE task_id = ?
            """,
            (agent, expires, now, row["task_id"]),
        )
        conn.execute(
            "INSERT INTO events (task_id, event_type, agent, message, created_at) VALUES (?, 'lease', ?, '', ?)",
            (row["task_id"], agent, now),
        )
        conn.commit()
        leased = conn.execute("SELECT * FROM tasks WHERE task_id = ?", (row["task_id"],)).fetchone()
        return task_row_to_dict(leased)
    finally:
        conn.close()


def load_yaml_or_json(path: Path) -> Dict[str, Any]:
    with path.open(encoding="utf-8") as f:
        if path.suffix.lower() == ".json":
            data = json.load(f)
        else:
            data = yaml.safe_load(f)
    if not isinstance(data, dict):
        raise ResearchMissionError(f"Result must be a mapping: {path}")
    return data


def validate_result_data(data: Dict[str, Any], schema: Dict[str, Any]) -> List[str]:
    issues: List[str] = []
    for field in schema.get("required", []) or []:
        if field not in data or data[field] in (None, ""):
            issues.append(f"Missing required field: {field}")

    for field, spec in (schema.get("fields") or {}).items():
        if field not in data:
            continue
        issues.extend(validate_field(data[field], spec or {}, field))
    return issues


def validate_field(value: Any, spec: Dict[str, Any], path: str) -> List[str]:
    issues: List[str] = []
    expected_type = spec.get("type")
    if expected_type and not type_matches(value, expected_type):
        issues.append(f"{path} must be {expected_type}")
        return issues

    allowed = spec.get("allowed")
    if allowed and value not in allowed:
        issues.append(f"{path} must be one of: {', '.join(map(str, allowed))}")

    required = spec.get("required") or []
    if required:
        if not isinstance(value, dict):
            issues.append(f"{path} must be an object with required fields")
        else:
            for child in required:
                if child not in value or value[child] in (None, ""):
                    issues.append(f"Missing required field: {path}.{child}")

    for child, child_spec in (spec.get("fields") or {}).items():
        if isinstance(value, dict) and child in value:
            issues.extend(validate_field(value[child], child_spec or {}, f"{path}.{child}"))

    item_spec = spec.get("items")
    if item_spec and isinstance(value, list):
        for index, item in enumerate(value):
            issues.extend(validate_field(item, item_spec or {}, f"{path}[{index}]"))
    return issues


def type_matches(value: Any, expected_type: str) -> bool:
    if expected_type == "string":
        return isinstance(value, str)
    if expected_type == "list":
        return isinstance(value, list)
    if expected_type == "object":
        return isinstance(value, dict)
    if expected_type == "boolean":
        return isinstance(value, bool)
    if expected_type == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    return True


def load_result_schema(mission_dir: Path, manifest: Dict[str, Any]) -> Dict[str, Any]:
    schema_path = (manifest.get("worker") or {}).get("output_schema")
    if not schema_path:
        return {}
    path = mission_path(mission_dir, schema_path)
    if not path.exists():
        raise ResearchMissionError(f"Output schema not found: {path}")
    with path.open(encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    if not isinstance(data, dict):
        raise ResearchMissionError(f"Output schema must be a mapping: {path}")
    return data


def validate_result_file(mission_dir: Path, result_path: Path) -> List[str]:
    manifest = load_manifest(mission_dir)
    schema = load_result_schema(mission_dir, manifest)
    data = load_yaml_or_json(result_path)
    return validate_result_data(data, schema)


def complete_task(mission_dir: Path, task_id: str, agent: str, result_path: Path) -> Dict[str, Any]:
    issues = validate_result_file(mission_dir, result_path)
    if issues:
        raise ResearchMissionError("Result failed schema validation: " + "; ".join(issues))

    result_data = load_yaml_or_json(result_path)
    if str(result_data.get("task_id", "")) != task_id:
        raise ResearchMissionError(f"Result task_id does not match leased task: {task_id}")

    rel_result = str(result_path.relative_to(mission_dir)) if result_path.is_relative_to(mission_dir) else str(result_path)
    conn = connect_state(mission_dir)
    try:
        init_state(conn)
        conn.execute("BEGIN IMMEDIATE")
        row = conn.execute("SELECT * FROM tasks WHERE task_id = ?", (task_id,)).fetchone()
        if row is None:
            raise ResearchMissionError(f"Task not found: {task_id}")
        if row["status"] != "leased":
            raise ResearchMissionError(f"Task {task_id} is not leased")
        if row["lease_owner"] != agent:
            raise ResearchMissionError(f"Task {task_id} is leased by {row['lease_owner']}, not {agent}")
        now = now_ts()
        conn.execute(
            """
            UPDATE tasks
            SET status = 'completed', result_path = ?, error = NULL,
                lease_owner = NULL, lease_expires_at = NULL, updated_at = ?
            WHERE task_id = ?
            """,
            (rel_result, now, task_id),
        )
        conn.execute(
            "INSERT INTO events (task_id, event_type, agent, message, created_at) VALUES (?, 'complete', ?, ?, ?)",
            (task_id, agent, rel_result, now),
        )
        conn.commit()
        return {"task_id": task_id, "status": "completed", "result_path": rel_result}
    finally:
        conn.close()


def release_task(
    mission_dir: Path,
    task_id: str,
    agent: str,
    failed: bool = False,
    message: str = "",
) -> Dict[str, Any]:
    conn = connect_state(mission_dir)
    try:
        init_state(conn)
        conn.execute("BEGIN IMMEDIATE")
        row = conn.execute("SELECT * FROM tasks WHERE task_id = ?", (task_id,)).fetchone()
        if row is None:
            raise ResearchMissionError(f"Task not found: {task_id}")
        if row["status"] != "leased":
            raise ResearchMissionError(f"Task {task_id} is not leased")
        if row["lease_owner"] != agent:
            raise ResearchMissionError(f"Task {task_id} is leased by {row['lease_owner']}, not {agent}")
        new_status = "needs_review" if failed else "pending"
        now = now_ts()
        conn.execute(
            """
            UPDATE tasks
            SET status = ?, lease_owner = NULL, lease_expires_at = NULL, error = ?, updated_at = ?
            WHERE task_id = ?
            """,
            (new_status, message or None, now, task_id),
        )
        event_type = "fail" if failed else "release"
        conn.execute(
            "INSERT INTO events (task_id, event_type, agent, message, created_at) VALUES (?, ?, ?, ?, ?)",
            (task_id, event_type, agent, message, now),
        )
        conn.commit()
        return {"task_id": task_id, "status": new_status}
    finally:
        conn.close()


def status_counts(mission_dir: Path) -> Dict[str, int]:
    conn = connect_state(mission_dir)
    try:
        init_state(conn)
        rows = conn.execute("SELECT status, COUNT(*) AS count FROM tasks GROUP BY status").fetchall()
        return {row["status"]: row["count"] for row in rows}
    finally:
        conn.close()


def gc_leases(mission_dir: Path) -> int:
    conn = connect_state(mission_dir)
    try:
        init_state(conn)
        now = now_ts()
        cur = conn.execute(
            """
            UPDATE tasks
            SET status = 'pending', lease_owner = NULL, lease_expires_at = NULL, updated_at = ?
            WHERE status = 'leased' AND lease_expires_at < ?
            """,
            (now, now),
        )
        conn.commit()
        return cur.rowcount
    finally:
        conn.close()


def flatten_for_csv(data: Dict[str, Any]) -> Dict[str, Any]:
    flat: Dict[str, Any] = {}
    for key, value in data.items():
        add_flat_value(flat, key, value)
    return flat


def add_flat_value(flat: Dict[str, Any], prefix: str, value: Any) -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            add_flat_value(flat, f"{prefix}.{key}", child)
        return
    if isinstance(value, list):
        flat[prefix] = format_list_for_csv(value)
        return
    flat[prefix] = value


def format_list_for_csv(values: List[Any]) -> str:
    if not values:
        return ""
    if all(not isinstance(value, (dict, list)) for value in values):
        return "; ".join(str(value) for value in values)
    formatted: List[str] = []
    for value in values:
        if isinstance(value, dict):
            parts = []
            for key, child in value.items():
                if isinstance(child, (dict, list)):
                    child_text = json.dumps(child, sort_keys=True)
                else:
                    child_text = str(child)
                parts.append(f"{key}={child_text}")
            formatted.append(", ".join(parts))
        else:
            formatted.append(json.dumps(value, sort_keys=True))
    return " | ".join(formatted)


def aggregate_mission(mission_dir: Path) -> Dict[str, Any]:
    conn = connect_state(mission_dir)
    try:
        init_state(conn)
        rows = conn.execute(
            "SELECT task_id, title, result_path FROM tasks WHERE status = 'completed' ORDER BY task_id"
        ).fetchall()
    finally:
        conn.close()

    aggregate_dir = mission_dir / "aggregate"
    aggregate_dir.mkdir(parents=True, exist_ok=True)
    output_rows: List[Dict[str, Any]] = []
    needs_review_rows: List[Dict[str, Any]] = []
    material_rows: List[Dict[str, Any]] = []
    evidence_rows: List[Dict[str, Any]] = []
    manufacturing_step_rows: List[Dict[str, Any]] = []

    for row in rows:
        if not row["result_path"]:
            continue
        result_path = mission_path(mission_dir, row["result_path"])
        data = load_yaml_or_json(result_path)
        task_id = str(data.get("task_id") or row["task_id"])
        part_name = str(data.get("part_name") or row["title"])
        summary = summarize_result_for_master(data, row["title"])
        output_rows.append(summary)
        if data.get("needs_human_review") is True:
            needs_review_rows.append(summary)
        material_rows.extend(extract_material_rows(task_id, part_name, data))
        evidence_rows.extend(extract_evidence_rows(task_id, part_name, data))
        manufacturing_step_rows.extend(extract_manufacturing_step_rows(task_id, part_name, data))

    master_path = aggregate_dir / "master_table.csv"
    write_csv(master_path, output_rows)
    needs_review_path = aggregate_dir / "needs_review.csv"
    write_csv(needs_review_path, needs_review_rows)
    materials_path = aggregate_dir / "materials_table.csv"
    write_csv(materials_path, material_rows)
    evidence_path = aggregate_dir / "evidence_table.csv"
    write_csv(evidence_path, evidence_rows)
    manufacturing_steps_path = aggregate_dir / "manufacturing_steps_table.csv"
    write_csv(manufacturing_steps_path, manufacturing_step_rows)

    counts = status_counts(mission_dir)
    summary_path = aggregate_dir / "summary.md"
    with summary_path.open("w", encoding="utf-8") as f:
        f.write("# Research Mission Summary\n\n")
        f.write(f"- Completed results aggregated: {len(output_rows)}\n")
        f.write(f"- Needs human review: {len(needs_review_rows)}\n")
        for status, count in sorted(counts.items()):
            f.write(f"- {status}: {count}\n")
        f.write("\n## Outputs\n\n")
        f.write("- `aggregate/master_table.csv`\n")
        f.write("- `aggregate/needs_review.csv`\n")
        f.write("- `aggregate/materials_table.csv`\n")
        f.write("- `aggregate/evidence_table.csv`\n")
        f.write("- `aggregate/manufacturing_steps_table.csv`\n")

    return {
        "completed_results": len(output_rows),
        "needs_review": len(needs_review_rows),
        "outputs": [
            str(master_path),
            str(needs_review_path),
            str(materials_path),
            str(evidence_path),
            str(manufacturing_steps_path),
            str(summary_path),
        ],
    }


def summarize_result_for_master(data: Dict[str, Any], fallback_title: str) -> Dict[str, Any]:
    mass = data.get("mass") if isinstance(data.get("mass"), dict) else {}
    function = data.get("function") if isinstance(data.get("function"), dict) else {}
    composition = (
        data.get("material_composition")
        if isinstance(data.get("material_composition"), dict)
        else {}
    )
    how_to_make = data.get("how_to_make") if isinstance(data.get("how_to_make"), dict) else {}
    materials = composition.get("materials") if isinstance(composition.get("materials"), list) else []
    material_names = [
        str(item.get("material"))
        for item in materials
        if isinstance(item, dict) and item.get("material")
    ]
    return {
        "task_id": data.get("task_id", ""),
        "part_name": data.get("part_name", fallback_title),
        "source_bom_rows": format_list_for_csv(data.get("source_bom_rows", [])),
        "mass_value": mass.get("value", ""),
        "mass_unit": mass.get("unit", ""),
        "mass_confidence": mass.get("confidence", ""),
        "mass_basis": mass.get("basis", ""),
        "function_summary": function.get("summary", ""),
        "subsystem_role": function.get("subsystem_role", ""),
        "material_confidence": composition.get("confidence", ""),
        "materials": "; ".join(material_names),
        "how_to_make_summary": how_to_make.get("summary", ""),
        "how_to_make_source_file": how_to_make.get("source_file", ""),
        "local_make_assessment": how_to_make.get("local_make_assessment", ""),
        "confidence": data.get("confidence", ""),
        "needs_human_review": data.get("needs_human_review", ""),
        "uncertainty_notes": format_list_for_csv(data.get("uncertainty_notes", [])),
    }


def extract_material_rows(task_id: str, part_name: str, data: Dict[str, Any]) -> List[Dict[str, Any]]:
    composition = data.get("material_composition")
    if not isinstance(composition, dict):
        return []
    materials = composition.get("materials")
    if not isinstance(materials, list):
        return []
    rows: List[Dict[str, Any]] = []
    for index, item in enumerate(materials, 1):
        if not isinstance(item, dict):
            continue
        rows.append(
            {
                "task_id": task_id,
                "part_name": part_name,
                "material_index": index,
                "material": item.get("material", ""),
                "role": item.get("role", ""),
                "estimated_mass_fraction": item.get("estimated_mass_fraction", ""),
                "source_file": item.get("source_file", ""),
            }
        )
    return rows


def extract_evidence_rows(task_id: str, part_name: str, data: Dict[str, Any]) -> List[Dict[str, Any]]:
    evidence = data.get("evidence")
    if not isinstance(evidence, list):
        return []
    rows: List[Dict[str, Any]] = []
    for index, item in enumerate(evidence, 1):
        if not isinstance(item, dict):
            continue
        rows.append(
            {
                "task_id": task_id,
                "part_name": part_name,
                "evidence_index": index,
                "source_file": item.get("source_file", ""),
                "claim": item.get("claim") or item.get("note", ""),
            }
        )
    return rows


def extract_manufacturing_step_rows(
    task_id: str, part_name: str, data: Dict[str, Any]
) -> List[Dict[str, Any]]:
    how_to_make = data.get("how_to_make")
    if not isinstance(how_to_make, dict):
        return []
    steps = how_to_make.get("manufacturing_steps")
    if not isinstance(steps, list):
        return []
    rows: List[Dict[str, Any]] = []
    for index, step in enumerate(steps, 1):
        rows.append(
            {
                "task_id": task_id,
                "part_name": part_name,
                "step_index": index,
                "manufacturing_step": step,
                "source_file": how_to_make.get("source_file", ""),
            }
        )
    return rows


def write_csv(path: Path, rows: List[Dict[str, Any]]) -> None:
    fieldnames: List[str] = []
    seen = set()
    for row in rows:
        for key in row.keys():
            if key not in seen:
                seen.add(key)
                fieldnames.append(key)

    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames or ["task_id"])
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
