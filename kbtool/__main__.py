import argparse
import json
import sys
from pathlib import Path

from . import indexer, queue_tool, report, closure_analysis


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="kbtool CLI")
    sub = parser.add_subparsers(dest="command")
    sub.add_parser("index", help="Build index.json from kb/**/*.yaml")
    v = sub.add_parser("validate", help="Rebuild queue and verify gap resolution")
    v.add_argument("--id", action="append", dest="ids", required=True, help="Gap id to verify (repeatable)")
    v.add_argument("--no-index", action="store_true", help="Skip indexer run and use existing queue")
    q = sub.add_parser("queue", help="Work queue operations")
    q_sub = q.add_subparsers(dest="qcmd")
    q_sub.add_parser("pop", help="Pop and print the next queue item (legacy)")
    q_sub.add_parser("prune", help="Remove items marked resolved/superseded from queue")
    lease_p = q_sub.add_parser("lease", help="Lease next pending item")
    lease_p.add_argument("--agent", required=True)
    lease_p.add_argument("--ttl", type=int, default=900)
    lease_p.add_argument("--priority", help="Comma-separated reasons in priority order")
    comp_p = q_sub.add_parser("complete", help="Mark leased item complete")
    comp_p.add_argument("--id", required=True)
    comp_p.add_argument("--agent", required=True)
    comp_p.add_argument(
        "--verify",
        action="store_true",
        help="Rebuild queue and refuse completion if the gap remains",
    )
    comp_p.add_argument(
        "--no-index",
        action="store_true",
        help="Skip indexer run when used with --verify",
    )
    rel_p = q_sub.add_parser("release", help="Release a lease back to pending")
    rel_p.add_argument("--id", required=True)
    rel_p.add_argument("--agent", required=True)
    gc_p = q_sub.add_parser("gc", help="Revert expired leases; optionally prune old done items")
    gc_p.add_argument("--prune-done-older-than", type=int, default=None, dest="prune_done")
    q_sub.add_parser("ls", help="Show queue counts by status")
    add_p = q_sub.add_parser("add", help="Add manual gap to queue")
    add_p.add_argument("--gap-type", required=False, help="Gap type (existing or new)")
    add_p.add_argument("--item-id", required=False, help="Item/recipe/process ID")
    add_p.add_argument("--description", help="Description of the issue")
    add_p.add_argument("--context", help="JSON context string")
    add_p.add_argument("--file", help="JSONL file with gap items to add (alternative to --gap-type)")
    q_sub.add_parser("gap-types", help="List registered gap types")

    r = sub.add_parser("report", help="Generate reports from knowledge base")
    r_sub = r.add_subparsers(dest="rcmd")
    r_sub.add_parser("inventory", help="Generate inventory report of all items")

    d = sub.add_parser("dedupe", help="Dedupe queue operations")
    d_sub = d.add_subparsers(dest="dcmd")
    d_lease = d_sub.add_parser("lease", help="Lease next dedupe task")
    d_lease.add_argument("--agent", required=True)
    d_lease.add_argument("--ttl", type=int, default=900)
    d_add = d_sub.add_parser("add", help="Add dedupe tasks from file (JSON or JSONL)")
    d_add.add_argument("--file", required=True, help="Path to JSON/JSONL with dedupe entries")
    d_complete = d_sub.add_parser("complete", help="Mark dedupe task complete")
    d_complete.add_argument("--id", required=True)
    d_complete.add_argument("--agent", required=True)
    d_release = d_sub.add_parser("release", help="Release a dedupe lease back to pending")
    d_release.add_argument("--id", required=True)
    d_release.add_argument("--agent", required=True)
    d_gc = d_sub.add_parser("gc", help="Revert expired dedupe leases; optionally prune old done items")
    d_gc.add_argument("--prune-done-older-than", type=int, default=None, dest="prune_done")
    d_sub.add_parser("ls", help="Show dedupe queue counts by status")

    c = sub.add_parser("config", help="Queue filtering configuration")
    c_sub = c.add_subparsers(dest="ccmd")
    c_sub.add_parser("show", help="Show current configuration")
    c_sub.add_parser("modes", help="List available filter modes")

    cl = sub.add_parser("mat-closure", help="Analyze material closure for machines")
    cl.add_argument("--machine", type=str, help="Analyze a specific machine")
    cl.add_argument("--all", action="store_true", help="Analyze all machines")
    cl.add_argument("--output", type=str, help="Output file (default: stdout)")

    return parser.parse_args()


def _run_indexer() -> bool:
    if hasattr(indexer, "main"):
        indexer.main()
        return True
    json_output = indexer.run_indexer()
    if isinstance(json_output, dict):
        return bool(json_output.get("success", True))
    return True


def main() -> None:
    args = _parse_args()
    if args.command in (None, "index"):
        # Compatibility: some environments may expose indexer.main, others may expose run_indexer only
        if hasattr(indexer, "main"):
            indexer.main()
        else:
            json_output = indexer.run_indexer()
            print(json.dumps(json_output, indent=2))
    elif args.command == "validate":
        print(
            "WARNING: kbtool validate is deprecated. Use `python -m src.cli queue verify --id <gap_type:item_id>` instead.",
            file=sys.stderr,
        )
        if not args.no_index:
            ok = _run_indexer()
            if not ok:
                raise SystemExit("Indexer failed; cannot validate queue")
        remaining = queue_tool.gap_ids_present(args.ids)
        if remaining:
            print("Unresolved gaps:")
            for gap_id in sorted(remaining):
                print(f"- {gap_id}")
            raise SystemExit(1)
        print("All specified gaps are resolved.")
    elif args.command == "queue":
        print(
            "WARNING: kbtool queue is deprecated. Use `python -m src.cli queue ...` instead.",
            file=sys.stderr,
        )
        if args.qcmd == "pop":
            item = queue_tool.pop_queue()
            if item:
                print(json.dumps(item))
            else:
                print("queue empty")
        elif args.qcmd == "prune":
            removed = queue_tool.prune_queue()
            print(f"Pruned {removed} completed items from queue")
        elif args.qcmd == "lease":
            priorities = args.priority.split(",") if args.priority else None
            item = queue_tool.lease_next(args.agent, ttl=args.ttl, priorities=priorities)
            if item:
                print(json.dumps(item))
            else:
                print("queue empty")
        elif args.qcmd == "complete":
            if args.verify:
                if not args.no_index:
                    ok = _run_indexer()
                    if not ok:
                        raise SystemExit("Indexer failed; refusing to complete")
                remaining = queue_tool.gap_ids_present([args.id])
                if remaining:
                    raise SystemExit(f"Refusing to complete; gap still present: {args.id}")
            ok = queue_tool.complete(args.id, args.agent)
            if ok:
                print(f"Marked {args.id} done")
            else:
                if args.verify and not queue_tool.gap_id_exists(args.id):
                    print(f"Gap {args.id} already resolved; no queue entry to mark done")
                else:
                    print(f"Failed to mark {args.id} done (not leased by {args.agent}?)")
        elif args.qcmd == "release":
            ok = queue_tool.release(args.id, args.agent)
            if ok:
                print(f"Released {args.id} to pending")
            else:
                print(f"Failed to release {args.id} (not leased by {args.agent}?)")
        elif args.qcmd == "gc":
            removed = queue_tool.gc(prune_done_older_than=args.prune_done)
            print(f"GC removed {removed} items")
        elif args.qcmd == "ls":
            counts = queue_tool.list_queue()
            print(json.dumps(counts, indent=2))
        elif args.qcmd == "add":
            if args.file:
                # Batch add from file
                added = queue_tool.add_from_file(Path(args.file))
                print(f"Added {added} items to queue")
            else:
                # Single add - require gap-type and item-id
                if not args.gap_type or not args.item_id:
                    raise SystemExit("Error: --gap-type and --item-id required (or use --file)")
                import json as json_mod
                context = json_mod.loads(args.context) if args.context else {}
                gap_id = queue_tool.add_gap(
                    gap_type=args.gap_type,
                    item_id=args.item_id,
                    description=args.description,
                    context=context,
                    source="manual"
                )
                print(f"Added gap to queue: {gap_id}")
        elif args.qcmd == "gap-types":
            types = queue_tool.list_gap_types()
            if not types:
                print("No gap types registered")
            else:
                # Separate indexer types from agent-created types
                indexer_types = {k: v for k, v in types.items() if v.get("source") == "indexer"}
                agent_types = {k: v for k, v in types.items() if v.get("source") != "indexer"}

                print(f"Registered Gap Types ({len(types)} total)")
                print("=" * 60)

                if indexer_types:
                    print("\nIndexer-Detected Types:")
                    for gap_type, meta in sorted(indexer_types.items()):
                        desc = meta.get("description", "No description")
                        print(f"  {gap_type:25s} - {desc}")

                if agent_types:
                    print("\nAgent-Created Types:")
                    for gap_type, meta in sorted(agent_types.items()):
                        desc = meta.get("description", "No description")
                        usage = meta.get("usage_count", 0)
                        print(f"  {gap_type:25s} - {desc} (used {usage} times)")
        else:
            raise SystemExit("Unknown queue subcommand")
    elif args.command == "report":
        if args.rcmd:
            report.main(args.rcmd)
        else:
            raise SystemExit("No report subcommand specified")
    elif args.command == "dedupe":
        from . import dedupe_tool
        if args.dcmd == "lease":
            item = dedupe_tool.lease_next(args.agent, ttl=args.ttl)
            if item:
                print(json.dumps(item))
            else:
                print("dedupe queue empty")
        elif args.dcmd == "add":
            added = dedupe_tool.add_from_file(Path(args.file))
            print(f"Added {added} dedupe tasks")
        elif args.dcmd == "complete":
            ok = dedupe_tool.complete(args.id, args.agent)
            if ok:
                print(f"Marked {args.id} done")
            else:
                print(f"Failed to mark {args.id} done (not leased by {args.agent}?)")
        elif args.dcmd == "release":
            ok = dedupe_tool.release(args.id, args.agent)
            if ok:
                print(f"Released {args.id} to pending")
            else:
                print(f"Failed to release {args.id} (not leased by {args.agent}?)")
        elif args.dcmd == "gc":
            removed = dedupe_tool.gc(prune_done_older_than=args.prune_done)
            print(f"GC removed {removed} dedupe items")
        elif args.dcmd == "ls":
            counts = dedupe_tool.list_queue()
            print(json.dumps(counts, indent=2))
        else:
            raise SystemExit("Unknown dedupe subcommand")
    elif args.command == "config":
        from . import config as cfg
        if args.ccmd == "show":
            config = cfg.QueueFilterConfig.load()
            stats = config.get_stats()
            print("Queue Filtering Configuration")
            print("=" * 40)
            print(f"Filtering enabled: {stats['enabled']}")
            print(f"Current mode: {stats['current_mode'] or '(none)'}")
            print(f"Available modes: {', '.join(stats['modes_available']) if stats['modes_available'] else '(none)'}")
            if stats['exclude_kinds']:
                print(f"Excluded kinds: {', '.join(stats['exclude_kinds'])}")
            if stats['exclude_gap_types']:
                print(f"Excluded gap types: {', '.join(stats['exclude_gap_types'])}")
        elif args.ccmd == "modes":
            config = cfg.QueueFilterConfig.load()
            if not config.modes:
                print("No modes defined in configuration")
            else:
                print("Available Filter Modes")
                print("=" * 40)
                for name, mode in config.modes.items():
                    active = " (ACTIVE)" if name == config.current_mode else ""
                    print(f"\n{name}{active}")
                    if mode.get("description"):
                        print(f"  {mode['description']}")
                    if mode.get("exclude"):
                        print(f"  Excludes: {len(mode['exclude'])} rules")
                    if mode.get("include"):
                        print(f"  Includes: {len(mode['include'])} rules")
        else:
            raise SystemExit("Unknown config subcommand")
    elif args.command == "mat-closure":
        from base_builder.kb_loader import KBLoader
        import sys

        # Load KB
        print("Loading knowledge base...", file=sys.stderr)
        kb_root = Path("kb")
        kb_loader = KBLoader(kb_root)
        kb_loader.load_all()
        print(f"Loaded {len(kb_loader.items)} items, {len(kb_loader.boms)} BOMs, "
              f"{len(kb_loader.recipes)} recipes", file=sys.stderr)

        analyzer = closure_analysis.ClosureAnalyzer(kb_loader)

        # Determine which machines to analyze
        machines_to_analyze = []

        if args.machine:
            machines_to_analyze.append(args.machine)
        elif args.all:
            # Get all machines
            machines_to_analyze = [
                item_id for item_id, item in kb_loader.items.items()
                if item.get('kind') == 'machine' and item.get('bom')
            ]
        else:
            print("Error: Must specify --machine <machine_id> or --all", file=sys.stderr)
            raise SystemExit(1)

        # Analyze machines
        results = []
        for machine_id in machines_to_analyze:
            print(f"Analyzing {machine_id}...", file=sys.stderr)
            result = analyzer.analyze_machine(machine_id)
            results.append(result)

        # Format output
        output_lines = []

        if args.all:
            # Summary table for all machines
            output_lines.append("=" * 120)
            output_lines.append("MATERIAL CLOSURE ANALYSIS SUMMARY - ALL MACHINES")
            output_lines.append("=" * 120)
            output_lines.append("")
            output_lines.append(f"{'Machine ID':<40} {'Total Mass':>12} {'ISRU %':>10} {'Import %':>10} {'Unres %':>10}")
            output_lines.append("-" * 120)

            for result in sorted(results, key=lambda r: r['imported_percent'], reverse=True):
                output_lines.append(
                    f"{result['machine_id']:<40} "
                    f"{result['total_mass']:>12.1f} kg "
                    f"{result['isru_percent']:>9.1f}% "
                    f"{result['imported_percent']:>9.1f}% "
                    f"{result['unresolved_percent']:>9.1f}%"
                )

            output_lines.append("")
            output_lines.append("=" * 120)
            output_lines.append("")
            output_lines.append("")

        # Detailed reports
        for result in results:
            output_lines.append(closure_analysis.format_closure_report(result))
            output_lines.append("\n")

        # Output
        output_text = "\n".join(output_lines)

        if args.output:
            with open(args.output, 'w') as f:
                f.write(output_text)
            print(f"Report written to {args.output}", file=sys.stderr)
        else:
            print(output_text)
    else:
        raise SystemExit(f"Unknown command {args.command}")


if __name__ == "__main__":  # pragma: no cover
    main()
