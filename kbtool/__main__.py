import argparse
import json

from . import indexer, queue_tool


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="kbtool CLI")
    sub = parser.add_subparsers(dest="command")
    sub.add_parser("index", help="Build index.json from kb/**/*.yaml")
    q = sub.add_parser("queue", help="Work queue operations")
    q_sub = q.add_subparsers(dest="qcmd")
    q_sub.add_parser("pop", help="Pop and print the next queue item")
    q_sub.add_parser("prune", help="Remove completed items (defined in index) from queue")
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
        else:
            raise SystemExit("Unknown queue subcommand")
    else:
        raise SystemExit(f"Unknown command {args.command}")


if __name__ == "__main__":  # pragma: no cover
    main()
