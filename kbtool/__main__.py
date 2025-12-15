import argparse
import json

from . import indexer, queue_tool


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
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    if args.command in (None, "index"):
        indexer.main()
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
    else:
        raise SystemExit(f"Unknown command {args.command}")


if __name__ == "__main__":  # pragma: no cover
    main()
