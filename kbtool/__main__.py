import argparse
import json
from pathlib import Path

from . import indexer, queue_tool, report


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="kbtool CLI")
    sub = parser.add_subparsers(dest="command")
    sub.add_parser("index", help="Build index.json from kb/**/*.yaml")
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
    rel_p = q_sub.add_parser("release", help="Release a lease back to pending")
    rel_p.add_argument("--id", required=True)
    rel_p.add_argument("--agent", required=True)
    gc_p = q_sub.add_parser("gc", help="Revert expired leases; optionally prune old done items")
    gc_p.add_argument("--prune-done-older-than", type=int, default=None, dest="prune_done")
    q_sub.add_parser("ls", help="Show queue counts by status")

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

    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    if args.command in (None, "index"):
        # Compatibility: some environments may expose indexer.main, others may expose run_indexer only
        if hasattr(indexer, "main"):
            indexer.main()
        else:
            json_output = indexer.run_indexer()
            print(json.dumps(json_output, indent=2))
    elif args.command == "queue":
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
            ok = queue_tool.complete(args.id, args.agent)
            if ok:
                print(f"Marked {args.id} done")
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
    else:
        raise SystemExit(f"Unknown command {args.command}")


if __name__ == "__main__":  # pragma: no cover
    main()
