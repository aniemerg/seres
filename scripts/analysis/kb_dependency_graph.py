#!/usr/bin/env python3
"""
Generate a dependency graph of the KB (items, recipes, processes, machines).
Outputs DOT and renders to SVG/PNG if Graphviz is available.
"""
from __future__ import annotations

import argparse
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set, Tuple

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
KB_DIR = REPO_ROOT / "kb"


@dataclass(frozen=True)
class Node:
    node_id: str
    label: str
    ntype: str
    subtype: Optional[str] = None


@dataclass(frozen=True)
class Edge:
    src: str
    dst: str
    etype: str


def _load_yaml(path: Path) -> Optional[dict]:
    try:
        with path.open() as f:
            data = yaml.safe_load(f)
        return data if isinstance(data, dict) else None
    except Exception:
        return None


def _node_id(kind: str, item_id: str) -> str:
    return f"{kind}:{item_id}"


def _collect_items() -> Dict[str, Node]:
    nodes: Dict[str, Node] = {}
    items_dir = KB_DIR / "items"
    for path in items_dir.rglob("*.yaml"):
        data = _load_yaml(path)
        if not data:
            continue
        item_id = data.get("id")
        kind = data.get("kind")
        if not item_id or not kind:
            continue
        subtype = kind
        label = item_id
        nid = _node_id("item", item_id)
        nodes[nid] = Node(node_id=nid, label=label, ntype="item", subtype=subtype)
    return nodes


def _collect_recipes() -> Dict[str, Node]:
    nodes: Dict[str, Node] = {}
    for path in (KB_DIR / "recipes").glob("*.yaml"):
        data = _load_yaml(path)
        if not data:
            continue
        if data.get("kind") not in (None, "recipe"):
            continue
        rid = data.get("id")
        if not rid:
            continue
        nid = _node_id("recipe", rid)
        nodes[nid] = Node(node_id=nid, label=rid, ntype="recipe")
    return nodes


def _collect_processes() -> Dict[str, Node]:
    nodes: Dict[str, Node] = {}
    for path in (KB_DIR / "processes").glob("*.yaml"):
        data = _load_yaml(path)
        if not data:
            continue
        if data.get("kind") not in (None, "process"):
            continue
        pid = data.get("id")
        if not pid:
            continue
        nid = _node_id("process", pid)
        nodes[nid] = Node(node_id=nid, label=pid, ntype="process")
    return nodes


def _iter_quantities(data: dict, key: str) -> Iterable[str]:
    for entry in data.get(key, []) or []:
        item_id = entry.get("item_id")
        if item_id:
            yield item_id


def _collect_edges(recipes: Dict[str, Node], processes: Dict[str, Node]) -> Set[Edge]:
    edges: Set[Edge] = set()

    # Recipe edges
    for path in (KB_DIR / "recipes").glob("*.yaml"):
        data = _load_yaml(path)
        if not data:
            continue
        rid = data.get("id")
        if not rid:
            continue
        recipe_nid = _node_id("recipe", rid)

        for item_id in _iter_quantities(data, "inputs"):
            edges.add(Edge(_node_id("item", item_id), recipe_nid, "recipe_input"))
        for item_id in _iter_quantities(data, "outputs"):
            edges.add(Edge(recipe_nid, _node_id("item", item_id), "recipe_output"))

        for step in data.get("steps", []) or []:
            pid = step.get("process_id")
            if pid:
                edges.add(Edge(recipe_nid, _node_id("process", pid), "recipe_process"))

    # Process edges
    for path in (KB_DIR / "processes").glob("*.yaml"):
        data = _load_yaml(path)
        if not data:
            continue
        pid = data.get("id")
        if not pid:
            continue
        process_nid = _node_id("process", pid)

        for item_id in _iter_quantities(data, "inputs"):
            edges.add(Edge(_node_id("item", item_id), process_nid, "process_input"))
        for item_id in _iter_quantities(data, "outputs"):
            edges.add(Edge(process_nid, _node_id("item", item_id), "process_output"))

        for req in data.get("resource_requirements", []) or []:
            machine_id = req.get("machine_id")
            if machine_id:
                edges.add(Edge(process_nid, _node_id("item", machine_id), "process_machine"))

    return edges


def _dot_attr(attrs: Dict[str, str]) -> str:
    return ",".join(f"{k}={v}" for k, v in attrs.items())


def _render_dot(nodes: Dict[str, Node], edges: Set[Edge], directed: bool) -> str:
    gtype = "digraph" if directed else "graph"
    edge_op = "->" if directed else "--"

    lines: List[str] = []
    lines.append(f"{gtype} kb_deps {{")
    lines.append("  graph [bgcolor=\"#0f172a\", fontname=\"Helvetica\", overlap=false, splines=true];")
    lines.append("  node [style=filled, fontname=\"Helvetica\", fontsize=10];")
    lines.append("  edge [color=\"#64748b\", arrowsize=0.6];")

    # Node styles
    for node in nodes.values():
        if node.ntype == "recipe":
            attrs = {
                "shape": "diamond",
                "fillcolor": "\"#f59e0b\"",
                "fontcolor": "\"#111827\"",
                "label": f"\"{node.label}\"",
            }
        elif node.ntype == "process":
            attrs = {
                "shape": "hexagon",
                "fillcolor": "\"#94a3b8\"",
                "fontcolor": "\"#0f172a\"",
                "label": f"\"{node.label}\"",
            }
        else:
            # item
            if node.subtype == "machine":
                fill = "\"#22c55e\""
                shape = "box"
            elif node.subtype == "part":
                fill = "\"#60a5fa\""
                shape = "ellipse"
            else:
                fill = "\"#fde047\""
                shape = "ellipse"
            attrs = {
                "shape": shape,
                "fillcolor": fill,
                "fontcolor": "\"#111827\"",
                "label": f"\"{node.label}\"",
            }

        lines.append(f"  \"{node.node_id}\" [{_dot_attr(attrs)}];")

    # Edge styles by type
    edge_colors = {
        "recipe_input": "#2563eb",
        "recipe_output": "#16a34a",
        "recipe_process": "#a855f7",
        "process_input": "#1d4ed8",
        "process_output": "#15803d",
        "process_machine": "#f43f5e",
    }

    for edge in sorted(edges, key=lambda e: (e.src, e.dst, e.etype)):
        color = edge_colors.get(edge.etype, "#64748b")
        attrs = {
            "color": f"\"{color}\"",
        }
        if not directed:
            attrs["dir"] = "none"
        lines.append(
            f"  \"{edge.src}\" {edge_op} \"{edge.dst}\" [{_dot_attr(attrs)}];"
        )

    lines.append("}")
    return "\n".join(lines)


def _write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


def _render_graphviz(dot_path: Path, out_path: Path) -> None:
    fmt = out_path.suffix.lstrip(".")
    subprocess.check_call(["dot", f"-T{fmt}", str(dot_path), "-o", str(out_path)])


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate KB dependency graph")
    parser.add_argument("--output", default=str(REPO_ROOT / "out" / "kb_dependency_graph.dot"))
    parser.add_argument("--format", choices=["dot", "svg", "png"], default="svg")
    parser.add_argument("--directed", action="store_true", help="Use directed edges")
    args = parser.parse_args()

    items = _collect_items()
    recipes = _collect_recipes()
    processes = _collect_processes()

    nodes = {**items, **recipes, **processes}
    edges = _collect_edges(recipes, processes)

    dot_path = Path(args.output)
    dot_content = _render_dot(nodes, edges, directed=args.directed)
    _write_file(dot_path, dot_content)

    if args.format != "dot":
        out_path = dot_path.with_suffix(f".{args.format}")
        try:
            _render_graphviz(dot_path, out_path)
            print(f"Wrote {out_path}")
        except FileNotFoundError:
            print("Graphviz 'dot' not found. DOT file generated only:")
            print(dot_path)
    else:
        print(f"Wrote {dot_path}")


if __name__ == "__main__":
    main()
