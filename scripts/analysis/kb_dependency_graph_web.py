#!/usr/bin/env python3
"""Generate an interactive HTML graph (Sigma.js) for KB dependencies."""
from __future__ import annotations

import argparse
import json
import random
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set

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
        label = item_id
        nid = _node_id("item", item_id)
        nodes[nid] = Node(node_id=nid, label=label, ntype="item", subtype=kind)
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


def _collect_edges() -> Set[Edge]:
    edges: Set[Edge] = set()

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


def _layout(nodes: Dict[str, Node], seed: int = 42) -> Dict[str, Dict[str, float]]:
    rng = random.Random(seed)
    positions: Dict[str, Dict[str, float]] = {}

    # Top-down layout: machines across the top, materials at the bottom,
    # with other nodes in bands in between.
    bands = {
        "item_machine": (0.0, 6.5),
        "item_part": (-4.0, 3.0),
        "recipe": (0.0, 2.0),
        "process": (4.0, 1.0),
        "item_material": (0.0, -3.0),
        "item_other": (0.0, -2.0),
        "missing": (0.0, -5.0),
    }

    for node in nodes.values():
        key = node.ntype
        if node.ntype == "item":
            if node.subtype == "machine":
                key = "item_machine"
            elif node.subtype == "part":
                key = "item_part"
            elif node.subtype == "missing":
                key = "missing"
            else:
                key = "item_material"
        elif node.subtype == "missing":
            key = "missing"
        elif node.ntype not in ("recipe", "process"):
            key = "item_other"

        cx, cy = bands.get(key, (0.0, 0.0))
        jitter_x = 1.8
        jitter_y = 1.8
        x = cx + rng.uniform(-jitter_x, jitter_x)
        y = cy + rng.uniform(-jitter_y, jitter_y)
        positions[node.node_id] = {"x": x, "y": y}

    # Normalize around the mean so camera centering is stable.
    if positions:
        mean_x = sum(pos["x"] for pos in positions.values()) / len(positions)
        mean_y = sum(pos["y"] for pos in positions.values()) / len(positions)
        max_abs = 0.0
        for pos in positions.values():
            pos["x"] -= mean_x
            pos["y"] -= mean_y
            max_abs = max(max_abs, abs(pos["x"]), abs(pos["y"]))
        if max_abs > 0:
            scale = 10.0 / max_abs
            for pos in positions.values():
                pos["x"] *= scale
                pos["y"] *= scale

    return positions


def _color(node: Node) -> str:
    if node.subtype == "missing":
        return "#ef4444"
    if node.ntype == "recipe":
        return "#f59e0b"
    if node.ntype == "process":
        return "#94a3b8"
    if node.subtype == "machine":
        return "#22c55e"
    if node.subtype == "part":
        return "#60a5fa"
    return "#fde047"


def _edge_color(etype: str) -> str:
    return {
        "recipe_input": "#2563eb",
        "recipe_output": "#16a34a",
        "recipe_process": "#a855f7",
        "process_input": "#1d4ed8",
        "process_output": "#15803d",
        "process_machine": "#f43f5e",
    }.get(etype, "#64748b")


def _build_graph() -> Dict[str, List[dict]]:
    items = _collect_items()
    recipes = _collect_recipes()
    processes = _collect_processes()

    nodes = {**items, **recipes, **processes}
    edges = _collect_edges()
    missing_nodes: Dict[str, Node] = {}
    for edge in edges:
        for node_id in (edge.src, edge.dst):
            if node_id in nodes or node_id in missing_nodes:
                continue
            kind, _, label = node_id.partition(":")
            if kind == "item":
                ntype = "item"
                subtype = "missing"
            elif kind == "recipe":
                ntype = "recipe"
                subtype = "missing"
            elif kind == "process":
                ntype = "process"
                subtype = "missing"
            else:
                ntype = kind or "unknown"
                subtype = "missing"
            missing_nodes[node_id] = Node(
                node_id=node_id,
                label=label or node_id,
                ntype=ntype,
                subtype=subtype,
            )
    if missing_nodes:
        nodes.update(missing_nodes)
    positions = _layout(nodes)

    node_list = []
    for node in nodes.values():
        pos = positions[node.node_id]
        node_list.append({
            "id": node.node_id,
            "label": node.label,
            "x": pos["x"],
            "y": pos["y"],
            "size": 2 if node.ntype != "item" else 1.6,
            "color": _color(node),
            "ntype": node.ntype,
            "subtype": node.subtype,
        })

    edge_list = []
    for i, edge in enumerate(edges):
        edge_list.append({
            "id": f"e{i}",
            "source": edge.src,
            "target": edge.dst,
            "color": _edge_color(edge.etype),
            "etype": edge.etype,
        })

    return {"nodes": node_list, "edges": edge_list}


def _write_html(path: Path, graph_data: dict) -> None:
    html = f"""<!doctype html>
<html>
<head>
  <meta charset=\"utf-8\" />
  <title>Knowledge Base</title>
  <style>
    html, body {{ margin: 0; padding: 0; width: 100%; height: 100%; background: #0f172a; color: #e2e8f0; font-family: system-ui, sans-serif; }}
    #container {{ width: 100%; height: 100%; }}
    #title {{ position: fixed; top: 12px; left: 12px; background: rgba(15,23,42,0.85); padding: 8px 12px; border: 1px solid #334155; border-radius: 10px; font-size: 16px; letter-spacing: 0.5px; font-weight: 600; }}
    #hud {{ position: fixed; bottom: 12px; right: 12px; background: rgba(15,23,42,0.85); padding: 10px 12px; border: 1px solid #334155; border-radius: 8px; font-size: 12px; }}
    #hud span {{ display: block; margin-bottom: 4px; }}
    #hud span:last-child {{ margin-bottom: 0; }}
    #status {{ position: fixed; bottom: 12px; left: 12px; background: rgba(15,23,42,0.85); padding: 8px 10px; border: 1px solid #334155; border-radius: 8px; font-size: 12px; }}
  </style>
</head>
<body>
  <div id=\"container\"></div>
  <div id=\"title\">Knowledge Base</div>
  <div id=\"hud\">
    <span style=\"color:#22c55e\">■ machines</span>
    <span style=\"color:#60a5fa\">■ parts</span>
    <span style=\"color:#fde047\">■ materials</span>
    <span style=\"color:#f59e0b\">■ recipes</span>
    <span style=\"color:#94a3b8\">■ processes</span>
    <span style=\"color:#ef4444\">■ missing refs</span>
  </div>
  <div id=\"status\">Loading graph…</div>

  <script src=\"https://unpkg.com/graphology@0.25.1/dist/graphology.umd.min.js\"></script>
  <script src=\"https://unpkg.com/sigma@2.4.0/build/sigma.min.js\"></script>
  <script>
    const status = document.getElementById('status');
    try {{
      const graphData = {json.dumps(graph_data)};
      const graph = new graphology.Graph();
      graphData.nodes.forEach(n => graph.addNode(n.id, n));
      graphData.edges.forEach(e => graph.addEdge(e.source, e.target, e));

      const container = document.getElementById('container');
      const renderer = new Sigma(graph, container, {{
        renderEdgeLabels: false,
        defaultEdgeType: 'line',
        minCameraRatio: 0.005,
        maxCameraRatio: 15,
      }});

      const camera = renderer.getCamera();
      function fmt(value) {{
        return Number.isFinite(value) ? value.toFixed(2) : "—";
      }}
      let lastFit = null;
      function percentile(sorted, p) {{
        if (!sorted.length) return 0;
        const idx = Math.max(0, Math.min(sorted.length - 1, Math.floor(p * (sorted.length - 1))));
        return sorted[idx];
      }}

      function fitToGraph(mode) {{
        const xs = [];
        const ys = [];
        graph.forEachNode((key, attrs) => {{
          xs.push(attrs.x);
          ys.push(attrs.y);
        }});
        xs.sort((a, b) => a - b);
        ys.sort((a, b) => a - b);
        const pick = (arr, p) => {{
          const idx = Math.max(0, Math.min(arr.length - 1, Math.floor(p * (arr.length - 1))));
          return arr[idx];
        }};
        const useDense = mode === "dense";
        const minX = useDense ? pick(xs, 0.05) : xs[0];
        const maxX = useDense ? pick(xs, 0.95) : xs[xs.length - 1];
        const minY = useDense ? pick(ys, 0.05) : ys[0];
        const maxY = useDense ? pick(ys, 0.95) : ys[ys.length - 1];

        const width = maxX - minX || 1;
        const height = maxY - minY || 1;
        const cx = minX + width / 2;
        const cy = minY + height / 2;
        const ratio = Math.max(width, height) / 12;
        camera.setState({{ x: cx, y: cy, ratio }});
        lastFit = {{ mode, x: cx, y: cy, ratio, minX, maxX, minY, maxY }};
      }}
      function fitToMean(mode) {{
        let sumX = 0;
        let sumY = 0;
        let count = 0;
        const dists = [];
        graph.forEachNode((key, attrs) => {{
          sumX += attrs.x;
          sumY += attrs.y;
          count += 1;
        }});
        const cx = count ? sumX / count : 0;
        const cy = count ? sumY / count : 0;
        graph.forEachNode((key, attrs) => {{
          const dx = attrs.x - cx;
          const dy = attrs.y - cy;
          dists.push(Math.sqrt(dx * dx + dy * dy));
        }});
        dists.sort((a, b) => a - b);
        const percentile = mode === "mean-tight" ? 0.6 : 0.85;
        const radius = dists.length
          ? dists[Math.floor(percentile * (dists.length - 1))]
          : 1;
        const ratio = Math.max(radius / 2, 0.05);
        camera.setState({{ x: cx, y: cy, ratio }});
        lastFit = {{ mode, x: cx, y: cy, ratio, minX: cx - radius, maxX: cx + radius, minY: cy - radius, maxY: cy + radius }};
      }}
      function fitToMedian() {{
        const xs = [];
        const ys = [];
        graph.forEachNode((key, attrs) => {{
          xs.push(attrs.x);
          ys.push(attrs.y);
        }});
        xs.sort((a, b) => a - b);
        ys.sort((a, b) => a - b);
        const mid = Math.floor(xs.length / 2);
        const cx = xs.length ? (xs.length % 2 ? xs[mid] : (xs[mid - 1] + xs[mid]) / 2) : 0;
        const cy = ys.length ? (ys.length % 2 ? ys[mid] : (ys[mid - 1] + ys[mid]) / 2) : 0;
        const dists = [];
        graph.forEachNode((key, attrs) => {{
          const dx = attrs.x - cx;
          const dy = attrs.y - cy;
          dists.push(Math.sqrt(dx * dx + dy * dy));
        }});
        dists.sort((a, b) => a - b);
        const radius = dists.length
          ? dists[Math.floor(0.6 * (dists.length - 1))]
          : 1;
        const ratio = Math.max(radius / 2, 0.05);
        camera.setState({{ x: cx, y: cy, ratio }});
        lastFit = {{ mode: "median", x: cx, y: cy, ratio, minX: cx - radius, maxX: cx + radius, minY: cy - radius, maxY: cy + radius }};
      }}
      const preferredStartRaw = localStorage.getItem("kbGraphPreferred");
      if (preferredStartRaw) {{
        const preferredStart = JSON.parse(preferredStartRaw);
        camera.setState(preferredStart);
        lastFit = {{
          mode: "preferred",
          x: preferredStart.x,
          y: preferredStart.y,
          ratio: preferredStart.ratio,
          minX: preferredStart.x,
          maxX: preferredStart.x,
          minY: preferredStart.y,
          maxY: preferredStart.y,
        }};
        // Preferred camera loaded.
      }} else {{
        fitToMedian();
      }}
      status.textContent = `Nodes: ${{graph.order}} | Edges: ${{graph.size}}`;
    }} catch (err) {{
      status.textContent = `Error loading graph: ${{err}}`;
      console.error(err);
    }}
  </script>
</body>
</html>"""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate interactive KB dependency graph HTML")
    parser.add_argument("--output", default=str(REPO_ROOT / "out" / "kb_dependency_graph.html"))
    args = parser.parse_args()

    graph = _build_graph()
    _write_html(Path(args.output), graph)
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
