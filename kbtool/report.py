"""Report generation for knowledge base inventory and analysis."""

import json
from collections import defaultdict
from pathlib import Path
from typing import Dict, List


def generate_inventory_report() -> None:
    """Generate a markdown inventory report of all KB items."""
    index_path = Path("out/index.json")
    if not index_path.exists():
        print("Error: out/index.json not found. Run 'python -m src.cli index' first.")
        return

    with open(index_path, "r", encoding="utf-8") as f:
        index_data = json.load(f)

    entries = index_data.get("entries", {})

    # Group items by kind
    by_kind: Dict[str, List[dict]] = defaultdict(list)
    for entry_id, entry in entries.items():
        kind = entry.get("kind", "unknown")
        name = entry.get("name") or entry_id
        by_kind[kind].append({"id": entry_id, "name": name})

    # Sort items within each kind alphabetically by name
    for kind in by_kind:
        by_kind[kind].sort(key=lambda x: (x["name"] or "").lower())

    # Generate markdown report
    output_path = Path("out/reports/inventory.md")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("# Knowledge Base Inventory\n\n")
        f.write("Auto-generated inventory of all items in the knowledge base.\n\n")

        # Summary statistics
        f.write("## Summary Statistics\n\n")
        f.write(f"- **Total items:** {len(entries)}\n")
        for kind in sorted(by_kind.keys()):
            count = len(by_kind[kind])
            f.write(f"- **{kind.capitalize()}:** {count}\n")
        f.write("\n")

        # Sections by kind
        for kind in sorted(by_kind.keys()):
            items = by_kind[kind]
            f.write(f"## {kind.capitalize()}\n\n")
            for item in items:
                # Format: - Name (id)
                f.write(f"- {item['name']} (`{item['id']}`)\n")
            f.write("\n")

    print(f"Generated inventory report: {output_path}")
    print(f"Total items: {len(entries)}")


def main(subcommand: str) -> None:
    """Entry point for report commands."""
    if subcommand == "inventory":
        generate_inventory_report()
    else:
        raise SystemExit(f"Unknown report subcommand: {subcommand}")
