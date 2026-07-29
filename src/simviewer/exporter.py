from __future__ import annotations

import json
from collections import defaultdict
from dataclasses import asdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple

import yaml

from src.simviewer.articles import discover_article_files, merge_backlinks, parse_articles
from src.simviewer.config import SimviewerConfig
from src.paths import KB_ROOT, REPO_ROOT
from src.simulation.provenance import verify_provenance
from src.simviewer.models import (
    ExportWarnings,
    InventoryCheckpoint,
    InventoryDelta,
    MachineAssignment,
    ProcessRunRecord,
    ReservedMachine,
)


def _read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _load_yaml(path: Path) -> dict | None:
    try:
        payload = yaml.safe_load(path.read_text(encoding="utf-8"))
        return payload if isinstance(payload, dict) else None
    except Exception:
        return None


def _iter_event_lines(path: Path) -> Iterable[dict]:
    with path.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                event = json.loads(line)
                if isinstance(event, dict):
                    yield event
            except json.JSONDecodeError:
                continue


def _primary_machine_from_scheduled(scheduled: dict | None) -> str | None:
    if not scheduled:
        return None
    reservations = scheduled.get("machine_reservations") or []
    if not isinstance(reservations, list):
        return None

    first = None
    for reservation in reservations:
        if not isinstance(reservation, dict):
            continue
        machine_id = reservation.get("machine_id")
        if not machine_id:
            continue
        if first is None:
            first = machine_id
        if machine_id != "labor_bot_general_v0":
            return machine_id
    return first


def _inventory_delta_from_events(scheduled: dict | None, complete: dict | None) -> Dict[str, dict]:
    delta: Dict[str, dict] = {}

    def add(item_id: str, quantity: float, unit: str) -> None:
        slot = delta.get(item_id)
        if slot is None:
            delta[item_id] = {"quantity": quantity, "unit": unit}
            return
        if slot["unit"] == unit:
            slot["quantity"] += quantity
        else:
            # Keep both units separated when unit mismatch appears.
            delta[f"{item_id}::{unit}"] = {"quantity": quantity, "unit": unit}

    if isinstance(scheduled, dict):
        inputs = scheduled.get("inputs_consumed") or {}
        if isinstance(inputs, dict):
            for item_id, payload in inputs.items():
                if not isinstance(payload, dict):
                    continue
                qty = float(payload.get("quantity", 0.0) or 0.0)
                unit = str(payload.get("unit", "unit"))
                add(str(item_id), -qty, unit)

    if isinstance(complete, dict):
        outputs = complete.get("outputs") or {}
        if isinstance(outputs, dict):
            for item_id, payload in outputs.items():
                if not isinstance(payload, dict):
                    continue
                qty = float(payload.get("quantity", 0.0) or 0.0)
                unit = str(payload.get("unit", "unit"))
                add(str(item_id), qty, unit)

    return delta


def _assign_machine_lanes(process_runs: List[ProcessRunRecord]) -> List[dict]:
    by_machine: Dict[str, List[ProcessRunRecord]] = defaultdict(list)
    for run in process_runs:
        if run.machine_type:
            by_machine[run.machine_type].append(run)

    lanes: List[dict] = []
    for machine_id, runs in by_machine.items():
        runs.sort(key=lambda r: ((r.start_time if r.start_time is not None else 0.0), r.process_run_id))
        lane_end_times: List[float] = []

        for run in runs:
            start = run.start_time if run.start_time is not None else 0.0
            end = run.end_time if run.end_time is not None else start
            lane_idx = None
            for idx, lane_end in enumerate(lane_end_times):
                if start >= lane_end:
                    lane_idx = idx
                    break
            if lane_idx is None:
                lane_idx = len(lane_end_times)
                lane_end_times.append(end)
            else:
                lane_end_times[lane_idx] = end

            lane_id = f"{machine_id}#{lane_idx + 1}"
            run.lane_id = lane_id

        for idx in range(len(lane_end_times)):
            lanes.append(
                {
                    "machine_type": machine_id,
                    "lane_id": f"{machine_id}#{idx + 1}",
                    "lane_index": idx,
                }
            )

    lanes.sort(key=lambda x: (x["machine_type"], x["lane_index"]))
    return lanes


def _build_machine_assignments(process_runs: List[ProcessRunRecord]) -> List[MachineAssignment]:
    assignments: List[MachineAssignment] = []
    for run in process_runs:
        for idx, reservation in enumerate(run.reserved_machines):
            start_time = reservation.start_time if reservation.start_time is not None else run.start_time
            end_time = reservation.end_time if reservation.end_time is not None else run.end_time
            duration = None
            if start_time is not None and end_time is not None:
                duration = max(0.0, end_time - start_time)
            instance_ids = reservation.machine_instance_ids or []
            if instance_ids:
                for instance_idx, instance_id in enumerate(instance_ids):
                    assignments.append(
                        MachineAssignment(
                            assignment_id=f"{run.process_run_id}:{reservation.machine_id}:{idx}:{instance_idx}",
                            process_run_id=run.process_run_id,
                            machine_id=reservation.machine_id,
                            machine_instance_id=instance_id,
                            start_time=start_time,
                            end_time=end_time,
                            duration_hours=duration,
                            lane_id=None,
                            lane_index=None,
                        )
                    )
                continue

            assignments.append(
                MachineAssignment(
                    assignment_id=f"{run.process_run_id}:{reservation.machine_id}:{idx}",
                    process_run_id=run.process_run_id,
                    machine_id=reservation.machine_id,
                    machine_instance_id=None,
                    start_time=start_time,
                    end_time=end_time,
                    duration_hours=duration,
                    lane_id=None,
                    lane_index=None,
                )
            )

    return assignments


def _assign_machine_lanes_from_assignments(assignments: List[MachineAssignment]) -> List[dict]:
    # Prefer concrete instance IDs when present.
    lane_rows: List[dict] = []
    rows_with_instance = [a for a in assignments if a.machine_instance_id]
    rows_without_instance = [a for a in assignments if not a.machine_instance_id]

    if rows_with_instance:
        lane_by_instance: Dict[str, Tuple[str, int]] = {}
        for row in sorted(rows_with_instance, key=lambda r: (r.machine_id, r.machine_instance_id or "")):
            instance_id = str(row.machine_instance_id)
            lane = lane_by_instance.get(instance_id)
            if lane is None:
                used_for_machine = sum(1 for m, _ in lane_by_instance.values() if m == row.machine_id)
                lane = (row.machine_id, used_for_machine)
                lane_by_instance[instance_id] = lane
                lane_rows.append(
                    {
                        "machine_type": row.machine_id,
                        "lane_id": instance_id,
                        "lane_index": used_for_machine,
                    }
                )
            row.lane_id = instance_id
            row.lane_index = lane[1]

    # Fallback for legacy data without instance IDs (overlap-based synthetic lanes).
    if not rows_without_instance:
        lane_rows.sort(key=lambda x: (x["machine_type"], x["lane_index"]))
        return lane_rows

    by_machine: Dict[str, List[MachineAssignment]] = defaultdict(list)
    for assignment in rows_without_instance:
        if not assignment.machine_id:
            continue
        by_machine[assignment.machine_id].append(assignment)

    for machine_id, rows in by_machine.items():
        rows.sort(
            key=lambda r: (
                r.start_time if r.start_time is not None else 0.0,
                r.end_time if r.end_time is not None else float("inf"),
                r.process_run_id,
            )
        )
        lane_end_times: List[float] = []
        for row in rows:
            start = row.start_time if row.start_time is not None else 0.0
            end = row.end_time if row.end_time is not None else start
            assigned = False
            for idx, last_end in enumerate(lane_end_times):
                if start <= last_end:
                    continue
                row.lane_index = idx
                row.lane_id = f"{machine_id}#{idx + 1}"
                lane_end_times[idx] = end
                assigned = True
                break
            if assigned:
                continue
            idx = len(lane_end_times)
            lane_end_times.append(end)
            row.lane_index = idx
            row.lane_id = f"{machine_id}#{idx + 1}"

        for idx, _ in enumerate(lane_end_times):
            lane_rows.append(
                {
                    "machine_type": machine_id,
                    "lane_id": f"{machine_id}#{idx + 1}",
                    "lane_index": idx,
                }
            )

    lane_rows.sort(key=lambda x: (x["machine_type"], x["lane_index"]))
    return lane_rows


def _extract_process_runs(
    events: List[dict],
    recipe_id_by_run_id: Dict[str, str],
) -> tuple[List[ProcessRunRecord], List[InventoryDelta], int]:
    scheduled: Dict[str, dict] = {}
    started: Dict[str, dict] = {}
    completed: Dict[str, dict] = {}
    errors_by_run: Dict[str, str] = {}

    for event in events:
        etype = event.get("type")
        run_id = event.get("process_run_id")

        if etype == "process_scheduled" and run_id:
            scheduled[str(run_id)] = event
        elif etype == "process_start" and run_id:
            started[str(run_id)] = event
        elif etype == "process_complete" and run_id:
            completed[str(run_id)] = event
        elif etype == "error":
            details = event.get("details")
            if isinstance(details, dict):
                error_run_id = details.get("process_run_id")
                if error_run_id:
                    errors_by_run[str(error_run_id)] = str(event.get("message", "process error"))

    all_run_ids = sorted(set(scheduled) | set(started) | set(completed) | set(errors_by_run))

    process_runs: List[ProcessRunRecord] = []
    deltas: List[InventoryDelta] = []

    for run_id in all_run_ids:
        sched = scheduled.get(run_id)
        start_ev = started.get(run_id)
        done_ev = completed.get(run_id)

        process_id = None
        for source in (done_ev, sched, start_ev):
            if isinstance(source, dict) and source.get("process_id"):
                process_id = str(source.get("process_id"))
                break
        if process_id is None:
            process_id = "unknown_process"

        start_time = None
        if isinstance(start_ev, dict):
            start_time = start_ev.get("actual_start_time")
        if start_time is None and isinstance(done_ev, dict):
            start_time = done_ev.get("start_time")
        if start_time is None and isinstance(sched, dict):
            start_time = sched.get("scheduled_start_time")
        start_time = float(start_time) if start_time is not None else None

        end_time = None
        if isinstance(done_ev, dict) and done_ev.get("time_hours") is not None:
            end_time = float(done_ev.get("time_hours"))
        elif isinstance(sched, dict) and sched.get("scheduled_end_time") is not None:
            end_time = float(sched.get("scheduled_end_time"))

        duration = None
        if start_time is not None and end_time is not None:
            duration = max(0.0, end_time - start_time)

        energy_kwh = None
        if isinstance(done_ev, dict) and done_ev.get("energy_kwh") is not None:
            energy_kwh = float(done_ev.get("energy_kwh"))
        elif isinstance(sched, dict) and sched.get("energy_kwh") is not None:
            energy_kwh = float(sched.get("energy_kwh"))

        status = "pending"
        error_message = None
        if run_id in errors_by_run:
            status = "failed"
            error_message = errors_by_run[run_id]
        elif done_ev is not None:
            status = "success"

        inputs = sched.get("inputs_consumed", {}) if isinstance(sched, dict) else {}
        outputs = done_ev.get("outputs", {}) if isinstance(done_ev, dict) else {}
        reserved_machines: List[ReservedMachine] = []
        if isinstance(sched, dict):
            for row in sched.get("machine_reservations", []) or []:
                if not isinstance(row, dict):
                    continue
                machine_id = row.get("machine_id")
                if not machine_id:
                    continue
                reserved_machines.append(
                    ReservedMachine(
                        machine_id=str(machine_id),
                        qty=float(row.get("qty", 1.0) or 1.0),
                        unit=str(row.get("unit", "count")),
                        start_time=float(row["start_time"]) if row.get("start_time") is not None else None,
                        end_time=float(row["end_time"]) if row.get("end_time") is not None else None,
                        machine_instance_ids=[
                            str(instance_id)
                            for instance_id in (row.get("machine_instance_ids", []) or [])
                            if instance_id
                        ],
                    )
                )

        recipe_run_id = str(done_ev.get("recipe_run_id")) if isinstance(done_ev, dict) and done_ev.get("recipe_run_id") else (
            str(sched.get("recipe_run_id")) if isinstance(sched, dict) and sched.get("recipe_run_id") else None
        )
        recipe_id = None
        for source in (done_ev, start_ev, sched):
            if isinstance(source, dict) and source.get("recipe_id"):
                recipe_id = str(source.get("recipe_id"))
                break
        if recipe_id is None and recipe_run_id:
            recipe_id = recipe_id_by_run_id.get(recipe_run_id)

        goal_context: Dict[str, Any] = {}
        for source in (done_ev, start_ev, sched):
            if not isinstance(source, dict):
                continue
            raw_goal_context = source.get("goal_context")
            if isinstance(raw_goal_context, dict):
                goal_context = raw_goal_context
                break

        record = ProcessRunRecord(
            process_run_id=run_id,
            process_id=process_id,
            recipe_run_id=recipe_run_id,
            recipe_id=recipe_id,
            start_time=start_time,
            end_time=end_time,
            duration_hours=duration,
            energy_kwh=energy_kwh,
            status=status,
            machine_type=_primary_machine_from_scheduled(sched),
            lane_id=None,
            inputs=inputs if isinstance(inputs, dict) else {},
            outputs=outputs if isinstance(outputs, dict) else {},
            reserved_machines=reserved_machines,
            goal_context=goal_context,
            error_message=error_message,
        )
        process_runs.append(record)

        delta = _inventory_delta_from_events(sched, done_ev)
        deltas.append(
            InventoryDelta(
                process_run_id=run_id,
                time_hours=end_time,
                delta=delta,
            )
        )

    process_runs.sort(key=lambda r: ((r.start_time if r.start_time is not None else 0.0), r.process_run_id))
    deltas.sort(key=lambda d: ((d.time_hours if d.time_hours is not None else 0.0), d.process_run_id))

    return process_runs, deltas, len(completed)


def _select_checkpoints(
    events: List[dict],
    checkpoint_every_processes: int,
    checkpoint_every_hours: float,
) -> List[InventoryCheckpoint]:
    snapshots: List[Tuple[int, dict]] = []
    process_complete_count = 0

    for event in events:
        etype = event.get("type")
        if etype == "process_complete":
            process_complete_count += 1
        if etype == "state_snapshot":
            snapshots.append((process_complete_count, event))

    if not snapshots:
        return []

    selected_indexes = {0, len(snapshots) - 1}

    last_sel_i = 0
    last_sel_count, last_sel_event = snapshots[0]
    last_sel_time = float(last_sel_event.get("time_hours", 0.0) or 0.0)

    for i in range(1, len(snapshots) - 1):
        count, event = snapshots[i]
        t = float(event.get("time_hours", 0.0) or 0.0)
        if (count - last_sel_count) >= checkpoint_every_processes or (t - last_sel_time) >= checkpoint_every_hours:
            selected_indexes.add(i)
            last_sel_i = i
            last_sel_count = count
            last_sel_time = t

    checkpoints: List[InventoryCheckpoint] = []
    idx_counter = 0
    for i in sorted(selected_indexes):
        count, event = snapshots[i]
        inventory = event.get("inventory") or {}
        if not isinstance(inventory, dict):
            inventory = {}
        checkpoints.append(
            InventoryCheckpoint(
                idx=idx_counter,
                time_hours=float(event.get("time_hours", 0.0) or 0.0),
                process_complete_count=int(count),
                inventory=inventory,
            )
        )
        idx_counter += 1

    return checkpoints


def _collect_kb_entities(repo_root: Path) -> tuple[Dict[str, dict], List[str]]:
    entities: Dict[str, dict] = {}
    missing_categories: List[str] = []

    kb_root = repo_root / KB_ROOT.relative_to(REPO_ROOT)
    for section in ("items", "recipes", "processes"):
        root = kb_root / section
        if not root.exists():
            continue
        for path in root.rglob("*.yaml"):
            payload = _load_yaml(path)
            if not payload:
                continue
            entity_id = payload.get("id")
            if not entity_id:
                continue

            kind = str(payload.get("kind") or section.rstrip("s"))
            category = payload.get("category")
            if kind == "machine" and not category:
                missing_categories.append(str(entity_id))

            entities[str(entity_id)] = {
                "id": str(entity_id),
                "kind": kind,
                "category": category,
                "path": str(path.relative_to(repo_root)),
                "name": payload.get("name") or str(entity_id),
                "raw": payload,
            }

    return entities, sorted(set(missing_categories))


def _summarize_simulation(snapshot: dict, process_runs: List[ProcessRunRecord], completed_count: int) -> dict:
    state = snapshot.get("state") if isinstance(snapshot, dict) else {}
    if not isinstance(state, dict):
        state = {}

    total_energy = float(state.get("total_energy_kwh", 0.0) or 0.0)
    time_hours = float(state.get("current_time_hours", 0.0) or 0.0)

    by_status: Dict[str, int] = defaultdict(int)
    for run in process_runs:
        by_status[run.status] += 1

    return {
        "sim_id": state.get("sim_id"),
        "time_hours": time_hours,
        "time_days": time_hours / 24.0,
        "total_energy_kwh": total_energy,
        "process_runs_total": len(process_runs),
        "process_runs_completed": completed_count,
        "process_runs_by_status": dict(sorted(by_status.items())),
        "inventory_items": len(state.get("inventory", {}) if isinstance(state.get("inventory"), dict) else {}),
        "imports_tracked": len(state.get("total_imports", {}) if isinstance(state.get("total_imports"), dict) else {}),
    }


def _augment_kb_entities_with_stats(entities: Dict[str, dict], process_runs: List[ProcessRunRecord]) -> None:
    process_counts: Dict[str, int] = defaultdict(int)
    output_counts: Dict[str, float] = defaultdict(float)

    for run in process_runs:
        process_counts[run.process_id] += 1
        for item_id, payload in run.outputs.items():
            if isinstance(payload, dict):
                qty = float(payload.get("quantity", 0.0) or 0.0)
                output_counts[item_id] += qty

    for entity_id, count in process_counts.items():
        if entity_id in entities:
            entities[entity_id]["sim_stats"] = {
                "process_run_count": count,
            }

    for entity_id, qty in output_counts.items():
        if entity_id in entities:
            bucket = entities[entity_id].setdefault("sim_stats", {})
            bucket["produced_quantity_total"] = qty


def _build_simquery(
    config: SimviewerConfig,
    summary: dict,
    events: List[dict],
    process_runs: List[ProcessRunRecord],
    kb_entities: Dict[str, dict],
) -> dict:
    machine_ids = {eid for eid, entity in kb_entities.items() if entity.get("kind") == "machine"}

    seeded_by_id: Dict[str, dict] = {}
    for event in events:
        if event.get("type") != "import":
            continue
        item_id = str(event.get("item_id") or "")
        if not item_id or item_id not in machine_ids:
            continue
        qty = float(event.get("quantity", 0.0) or 0.0)
        unit = str(event.get("unit", "unit") or "unit")
        sim_time = float(event.get("sim_time_hours", 0.0) or 0.0)
        row = seeded_by_id.get(item_id)
        if row is None:
            seeded_by_id[item_id] = {
                "id": item_id,
                "name": kb_entities.get(item_id, {}).get("name", item_id),
                "imported_quantity": qty,
                "unit": unit,
                "first_seen_time_hours": sim_time,
            }
        else:
            row["imported_quantity"] += qty
            row["first_seen_time_hours"] = min(float(row["first_seen_time_hours"]), sim_time)

    produced_by_id: Dict[str, dict] = {}
    for run in process_runs:
        if run.status != "success":
            continue
        for item_id, payload in run.outputs.items():
            if item_id not in machine_ids or not isinstance(payload, dict):
                continue
            qty = float(payload.get("quantity", 0.0) or 0.0)
            if qty <= 0:
                continue
            unit = str(payload.get("unit", "unit") or "unit")
            sim_time = float(run.end_time or run.start_time or 0.0)
            row = produced_by_id.get(item_id)
            if row is None:
                produced_by_id[item_id] = {
                    "id": item_id,
                    "name": kb_entities.get(item_id, {}).get("name", item_id),
                    "produced_quantity": qty,
                    "unit": unit,
                    "first_seen_time_hours": sim_time,
                }
            else:
                row["produced_quantity"] += qty
                row["first_seen_time_hours"] = min(float(row["first_seen_time_hours"]), sim_time)

    seeded_rows = sorted(seeded_by_id.values(), key=lambda r: str(r["id"]))
    produced_rows = sorted(produced_by_id.values(), key=lambda r: str(r["id"]))

    coverage_rows: List[dict] = []
    covered_count = 0
    for seeded in seeded_rows:
        produced = produced_by_id.get(str(seeded["id"]))
        produced_qty = float(produced["produced_quantity"]) if produced else 0.0
        covered = produced_qty >= 1.0
        if covered:
            covered_count += 1
        coverage_rows.append(
            {
                "id": seeded["id"],
                "name": seeded["name"],
                "imported_quantity": float(seeded["imported_quantity"]),
                "produced_quantity": produced_qty,
                "unit": seeded["unit"],
                "covered": covered,
            }
        )

    annotations: List[dict] = []
    markers: List[dict] = []
    for event in events:
        etype = event.get("type")
        if etype == "sim_annotation":
            annotations.append(
                {
                    "sim_time_hours": float(event.get("sim_time_hours", 0.0) or 0.0),
                    "key": str(event.get("key", "")),
                    "value": event.get("value"),
                    "tags": list(event.get("tags", []) or []),
                    "source": str(event.get("source", "runbook")),
                    "metadata": event.get("metadata") if isinstance(event.get("metadata"), dict) else {},
                }
            )
        elif etype == "sim_marker":
            markers.append(
                {
                    "sim_time_hours": float(event.get("sim_time_hours", 0.0) or 0.0),
                    "name": str(event.get("name", "")),
                    "tags": list(event.get("tags", []) or []),
                    "source": str(event.get("source", "runbook")),
                    "metadata": event.get("metadata") if isinstance(event.get("metadata"), dict) else {},
                }
            )

    annotations.sort(key=lambda row: float(row.get("sim_time_hours", 0.0)))
    markers.sort(key=lambda row: float(row.get("sim_time_hours", 0.0)))

    seed_total = len(seeded_rows)
    coverage_ratio = (covered_count / seed_total) if seed_total > 0 else 0.0

    # Machine utilization by machine type (success runs only).
    # Utilization window is simulation [0, summary.time_hours].
    sim_window_hours = max(0.0, float(summary.get("time_hours", 0.0) or 0.0))
    intervals_by_machine: Dict[str, List[Tuple[float, float]]] = defaultdict(list)
    run_count_by_machine: Dict[str, int] = defaultdict(int)
    energy_by_machine: Dict[str, float] = defaultdict(float)

    for run in process_runs:
        if run.status != "success":
            continue
        if not run.machine_type:
            continue
        if run.start_time is None or run.end_time is None:
            continue
        start = max(0.0, float(run.start_time))
        end = max(start, float(run.end_time))
        intervals_by_machine[run.machine_type].append((start, end))
        run_count_by_machine[run.machine_type] += 1
        energy_by_machine[run.machine_type] += float(run.energy_kwh or 0.0)

    utilization_rows: List[dict] = []
    for machine_id, intervals in intervals_by_machine.items():
        if not intervals:
            continue
        intervals.sort(key=lambda x: (x[0], x[1]))
        merged: List[Tuple[float, float]] = []
        for start, end in intervals:
            if not merged:
                merged.append((start, end))
                continue
            last_start, last_end = merged[-1]
            if start <= last_end:
                merged[-1] = (last_start, max(last_end, end))
            else:
                merged.append((start, end))
        busy_hours = sum(end - start for start, end in merged)
        utilization = (busy_hours / sim_window_hours) if sim_window_hours > 0 else 0.0
        utilization_rows.append(
            {
                "id": machine_id,
                "name": kb_entities.get(machine_id, {}).get("name", machine_id),
                "run_count": int(run_count_by_machine.get(machine_id, 0)),
                "busy_hours": busy_hours,
                "window_hours": sim_window_hours,
                "utilization_ratio": utilization,
                "utilization_percent": utilization * 100.0,
                "total_energy_kwh": float(energy_by_machine.get(machine_id, 0.0)),
            }
        )

    utilization_rows.sort(key=lambda row: (float(row["utilization_ratio"]), float(row["busy_hours"])), reverse=True)
    avg_utilization = (
        sum(float(r["utilization_ratio"]) for r in utilization_rows) / len(utilization_rows)
        if utilization_rows
        else 0.0
    )

    return {
        "version": "simquery.v0",
        "scalars": {
            "sim.id": config.sim_id,
            "sim.summary.time_hours": float(summary.get("time_hours", 0.0) or 0.0),
            "sim.summary.time_days": float(summary.get("time_days", 0.0) or 0.0),
            "sim.summary.total_energy_kwh": float(summary.get("total_energy_kwh", 0.0) or 0.0),
            "sim.summary.process_runs_total": int(summary.get("process_runs_total", 0) or 0),
            "sim.summary.process_runs_completed": int(summary.get("process_runs_completed", 0) or 0),
            "sim.replication.seed_machine_types": seed_total,
            "sim.replication.covered_machine_types": covered_count,
            "sim.replication.coverage_ratio": coverage_ratio,
            "sim.replication.coverage_percent": coverage_ratio * 100.0,
            "sim.machines.avg_utilization_ratio": avg_utilization,
            "sim.machines.avg_utilization_percent": avg_utilization * 100.0,
        },
        "tables": {
            "sim.machines.seeded": seeded_rows,
            "sim.machines.produced": produced_rows,
            "sim.machines.coverage": coverage_rows,
            "sim.machines.utilization": utilization_rows,
            "sim.annotations": annotations,
            "sim.markers": markers,
        },
    }


def export_simviewer(repo_root: Path, config: SimviewerConfig, out_dir: Path) -> dict:
    """Export static data artifacts for the simviewer frontend."""
    sim_dir = repo_root / config.simulation_root / config.sim_id
    kb_root = repo_root / KB_ROOT.relative_to(REPO_ROOT)
    event_log_path = sim_dir / "events.jsonl"
    snapshot_path = sim_dir / "snapshot.json"

    if not snapshot_path.exists():
        raise FileNotFoundError(f"Simulation snapshot not found: {snapshot_path}")
    if not event_log_path.exists():
        raise FileNotFoundError(f"Simulation event log not found: {event_log_path}")

    verify_provenance(sim_dir, kb_root)
    snapshot = _read_json(snapshot_path)
    events = list(_iter_event_lines(event_log_path))

    recipe_id_by_run_id: Dict[str, str] = {}
    orchestrator = snapshot.get("orchestrator")
    if isinstance(orchestrator, dict):
        recipe_runs = orchestrator.get("recipe_runs")
        if isinstance(recipe_runs, dict):
            for run_id, payload in recipe_runs.items():
                if not isinstance(payload, dict):
                    continue
                recipe_id = payload.get("recipe_id")
                if run_id and recipe_id:
                    recipe_id_by_run_id[str(run_id)] = str(recipe_id)

    process_runs, inventory_deltas, completed_count = _extract_process_runs(events, recipe_id_by_run_id)
    machine_assignments = _build_machine_assignments(process_runs)
    machine_lanes = _assign_machine_lanes_from_assignments(machine_assignments)
    lane_by_run_id: Dict[str, str] = {}
    for row in machine_assignments:
        if not row.process_run_id or not row.lane_id:
            continue
        lane_by_run_id.setdefault(row.process_run_id, row.lane_id)
    for run in process_runs:
        if run.process_run_id in lane_by_run_id:
            run.lane_id = lane_by_run_id[run.process_run_id]
    checkpoints = _select_checkpoints(
        events,
        checkpoint_every_processes=config.checkpoint_every_processes,
        checkpoint_every_hours=config.checkpoint_every_hours,
    )

    kb_entities, missing_categories = _collect_kb_entities(repo_root)
    _augment_kb_entities_with_stats(kb_entities, process_runs)

    article_files = discover_article_files(repo_root, config.article_paths)
    articles, article_backlinks = parse_articles(repo_root, article_files)

    article_ids = {a["id"] for a in articles}
    unresolved_links: List[dict] = []
    for article in articles:
        for target in article.get("wiki_links", []):
            if target not in kb_entities and target not in article_ids:
                unresolved_links.append(
                    {
                        "source_article_id": article["id"],
                        "target": target,
                        "message": "Wiki-link target is undefined",
                    }
                )

    warnings = ExportWarnings(
        unresolved_wiki_links=unresolved_links,
        missing_kb_categories=missing_categories,
        undefined_references=sorted({w["target"] for w in unresolved_links}),
    )

    summary = _summarize_simulation(snapshot, process_runs, completed_count)
    simquery = _build_simquery(
        config=config,
        summary=summary,
        events=events,
        process_runs=process_runs,
        kb_entities=kb_entities,
    )

    data_dir = out_dir / "data"
    data_dir.mkdir(parents=True, exist_ok=True)

    sim_data = {
        "sim_id": config.sim_id,
        "summary": summary,
        "machine_lanes": machine_lanes,
        "process_runs": [r.to_dict() for r in process_runs],
        "machine_assignments": [a.to_dict() for a in machine_assignments],
        "inventory_checkpoints": [c.to_dict() for c in checkpoints],
        "inventory_deltas": [d.to_dict() for d in inventory_deltas],
    }

    backlinks = merge_backlinks(article_backlinks)

    (data_dir / "sim_data.json").write_text(json.dumps(sim_data, indent=2), encoding="utf-8")
    (data_dir / "kb_entities.json").write_text(
        json.dumps({"entities": sorted(kb_entities.values(), key=lambda x: (x["kind"], x["id"]))}, indent=2),
        encoding="utf-8",
    )
    (data_dir / "backlinks.json").write_text(json.dumps(backlinks, indent=2), encoding="utf-8")
    (data_dir / "articles.json").write_text(json.dumps({"articles": articles}, indent=2), encoding="utf-8")
    (data_dir / "warnings.json").write_text(json.dumps(warnings.to_dict(), indent=2), encoding="utf-8")
    (data_dir / "simquery.json").write_text(json.dumps(simquery, indent=2), encoding="utf-8")
    def _rel(path: Path) -> str:
        try:
            return str(path.relative_to(repo_root))
        except Exception:
            return str(path)

    (data_dir / "export_meta.json").write_text(
        json.dumps(
            {
                "config": config.to_dict(),
                "paths": {
                    "simulation_dir": _rel(sim_dir),
                    "event_log": _rel(event_log_path),
                    "snapshot": _rel(snapshot_path),
                },
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    return {
        "out_dir": str(out_dir),
        "data_dir": str(data_dir),
        "summary": summary,
        "warnings": warnings.to_dict(),
    }
