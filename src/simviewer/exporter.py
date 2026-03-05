from __future__ import annotations

import json
from collections import defaultdict
from dataclasses import asdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple

import yaml

from src.simviewer.articles import discover_article_files, merge_backlinks, parse_articles
from src.simviewer.config import SimviewerConfig
from src.simviewer.models import ExportWarnings, InventoryCheckpoint, InventoryDelta, ProcessRunRecord


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

    kb_root = repo_root / "kb"
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


def export_simviewer(repo_root: Path, config: SimviewerConfig, out_dir: Path) -> dict:
    """Export static data artifacts for the simviewer frontend."""
    sim_dir = repo_root / "simulations" / config.sim_id
    event_log_path = sim_dir / "events.jsonl"
    snapshot_path = sim_dir / "snapshot.json"

    if not snapshot_path.exists():
        raise FileNotFoundError(f"Simulation snapshot not found: {snapshot_path}")
    if not event_log_path.exists():
        raise FileNotFoundError(f"Simulation event log not found: {event_log_path}")

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
    machine_lanes = _assign_machine_lanes(process_runs)
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

    data_dir = out_dir / "data"
    data_dir.mkdir(parents=True, exist_ok=True)

    sim_data = {
        "sim_id": config.sim_id,
        "summary": summary,
        "machine_lanes": machine_lanes,
        "process_runs": [r.to_dict() for r in process_runs],
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
    (data_dir / "export_meta.json").write_text(
        json.dumps(
            {
                "config": config.to_dict(),
                "paths": {
                    "simulation_dir": str(sim_dir.relative_to(repo_root)),
                    "event_log": str(event_log_path.relative_to(repo_root)),
                    "snapshot": str(snapshot_path.relative_to(repo_root)),
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
