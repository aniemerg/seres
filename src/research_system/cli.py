from __future__ import annotations

import json
from pathlib import Path

from src.research_system import core


def add_research_subcommands(subparsers) -> None:
    parser = subparsers.add_parser("research", help="Research mission operations")
    sub = parser.add_subparsers(dest="research_cmd")

    ingest = sub.add_parser("ingest", help="Generate tasks and initialize mission state")
    ingest.add_argument("--mission", type=Path, required=True, help="Research mission directory")
    ingest.add_argument("--reset", action="store_true", help="Replace existing mission tasks")

    lease = sub.add_parser("lease", help="Lease the next pending research task")
    lease.add_argument("--mission", type=Path, required=True, help="Research mission directory")
    lease.add_argument("--agent", required=True, help="Agent name")
    lease.add_argument("--ttl", type=int, default=1800, help="Lease TTL in seconds")

    complete = sub.add_parser("complete", help="Complete a leased research task")
    complete.add_argument("--mission", type=Path, required=True, help="Research mission directory")
    complete.add_argument("--task", required=True, help="Task ID")
    complete.add_argument("--agent", required=True, help="Agent name")
    complete.add_argument("--result", type=Path, required=True, help="Result YAML or JSON path")

    release = sub.add_parser("release", help="Release a leased research task")
    release.add_argument("--mission", type=Path, required=True, help="Research mission directory")
    release.add_argument("--task", required=True, help="Task ID")
    release.add_argument("--agent", required=True, help="Agent name")
    release.add_argument("--failed", action="store_true", help="Move task to needs_review instead of pending")
    release.add_argument("--message", default="", help="Release/failure note")

    validate = sub.add_parser("validate-result", help="Validate a result against the mission schema")
    validate.add_argument("--mission", type=Path, required=True, help="Research mission directory")
    validate.add_argument("--result", type=Path, required=True, help="Result YAML or JSON path")

    status = sub.add_parser("status", help="Show task counts by status")
    status.add_argument("--mission", type=Path, required=True, help="Research mission directory")

    gc = sub.add_parser("gc", help="Expire stale leases")
    gc.add_argument("--mission", type=Path, required=True, help="Research mission directory")

    aggregate = sub.add_parser("aggregate", help="Aggregate completed task results")
    aggregate.add_argument("--mission", type=Path, required=True, help="Research mission directory")


def run_research_command(args) -> int:
    cmd = args.research_cmd
    if not cmd:
        raise core.ResearchMissionError("Missing research subcommand")

    if cmd == "ingest":
        result = core.ingest_mission(args.mission, reset=args.reset)
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0

    if cmd == "lease":
        item = core.lease_task(args.mission, args.agent, ttl=args.ttl)
        if item is None:
            print("research queue empty")
        else:
            print(json.dumps(item, indent=2, sort_keys=True))
        return 0

    if cmd == "complete":
        result_path = core.mission_path(args.mission, args.result)
        result = core.complete_task(args.mission, args.task, args.agent, result_path)
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0

    if cmd == "release":
        result = core.release_task(
            args.mission,
            args.task,
            args.agent,
            failed=args.failed,
            message=args.message,
        )
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0

    if cmd == "validate-result":
        result_path = core.mission_path(args.mission, args.result)
        issues = core.validate_result_file(args.mission, result_path)
        if issues:
            print("Result validation failed:")
            for issue in issues:
                print(f"- {issue}")
            return 1
        print("Result is valid.")
        return 0

    if cmd == "status":
        print(json.dumps(core.status_counts(args.mission), indent=2, sort_keys=True))
        return 0

    if cmd == "gc":
        expired = core.gc_leases(args.mission)
        print(f"Expired {expired} lease(s)")
        return 0

    if cmd == "aggregate":
        result = core.aggregate_mission(args.mission)
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0

    raise core.ResearchMissionError(f"Unknown research subcommand: {cmd}")

