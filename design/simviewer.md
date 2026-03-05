# SERES Simulation Viewer — Design Brief

> For a coding agent familiar with the SERES simulation system.
> Goal: build a React-based simulation viewer, statically exportable, that serves as both an investigation tool and a shareable artifact for a given simulation run.

---

## Core Principles

- **Timeline-first**: the Gantt is the primary view; everything else is secondary or contextual.
- **Static export**: Vite build, no server required. A Python export script produces the data files; `npm run build` produces a self-contained `/dist`.
- **Unified content space**: KB entries (auto-generated from YAML/JSON) and articles (authored Markdown) coexist as pages in the same browser. No distinction in routing or navigation.
- **Aesthetic**: Factorio — dense, industrial, functional. Dark theme. Monospace where appropriate. Information-dense without being chaotic.

---

## App Structure

Three top-level views, accessible via a persistent sidebar or tab bar.

### 1. Home (Simulation Summary)

The landing page for a shared export. Not the raw Gantt.

- **Authored article block**: a Markdown article (e.g. `articles/simulation_overview.md`) rendered at the top. This is where the human narrative lives — what this sim run was, what it demonstrated, key assumptions.
- **Auto-generated stats block**: total energy consumed, machines produced, processes executed, simulation duration (hours), ISRU percentage. Pulled from `sim_data.json`.
- **Navigation links**: into the Gantt and into KB browser top-level categories.

### 2. Gantt (Timeline)

The primary investigation view.

**Layout:**
- Left column: machine list, Y axis. Fixed width, scrolls vertically in sync with chart.
- Right area: scrollable/zoomable Gantt chart. Horizontal axis is simulation time (hours).
- Top: zoom controls, time range display, category filter/collapse controls.

**Machine rows:**
- One row per machine.
- Rows are collapsible by machine category (ISRU, fabrication, assembly, etc.).
- Category headers are clickable links to the category's KB article if one exists.
- Categories should be inferred from YAML tags or naming conventions; agent should determine the best approach given the actual KB structure.

**Process bars:**
- Each bar represents one process run: positioned by start time, width by duration.
- Color-coded by process type or category (agent's discretion, should be legible at density).
- At low zoom, bars may be 1–2px wide; color density is still useful. Labels appear as zoom increases.
- Hover: lightweight tooltip showing process name, duration, energy.
- Click: opens the sliding detail drawer (see below).

**Rendering approach:**
- Row virtualization via `react-virtual` — only render visible rows.
- Bars rendered as SVG within each virtualized row.
- If performance degrades at extreme zoom-out, the SVG layer can be swapped for canvas per-row without touching the rest of the architecture.

**Zoom/pan:**
- Horizontal zoom and pan on the time axis.
- A minimap / overview strip at the bottom showing the full sim duration with energy consumption as a background shape (from the energy-over-time data). The viewport window is draggable on the minimap.

### 3. KB Browser

A Wikipedia-style content browser. All entity types and articles coexist here.

**Navigation:**
- Left sidebar: navigable index. Filterable by type (machine, process, material, recipe, article), searchable by name.
- Main area: renders the selected page using the appropriate template.
- Hash-based routing: `#/kb/machine/regolith_crusher_v0`, `#/kb/article/isru-assumptions`, etc.

**Page templates** (one React component per type):

- **Machine**: name, specs, power draw, process types it can run, parts it's made of, sim stats (how many process runs, total energy consumed in this sim), links to all its process runs (each clickable back to Gantt at that timestamp).
- **Process**: duration, energy per run, required machines, input/output materials, list of every execution in the sim with timestamps (each clickable back to Gantt).
- **Material/Item**: what produces it, what consumes it, inventory level chart over sim time (sparkline or small chart).
- **Recipe/BOM**: indented hierarchy of sub-processes and parts.
- **Article**: Markdown rendered with wiki-link support (see below). Frontmatter: `title`, `type: article`, optional `related_kb_entries`.

**Wiki-links:**
- Syntax: `[[machine:regolith_crusher_v0]]` or `[[process:iron_smelting_reduction_v0]]` etc.
- Rendered as inline links within article prose.
- Optionally rendered as inline KB cards (compact summary of the entity) — agent's discretion on which is cleaner.
- Backlinks are computed at export time and surfaced at the bottom of each page ("Referenced by: ...").

**Entries with no sim activity:**
- KB entries that exist but never appeared in the simulation are still shown, clearly marked as "not active in this simulation run."

---

## Sliding Detail Drawer

Appears when a process bar is clicked in the Gantt. Slides in from the right, does not replace the Gantt (which remains visible and pannable behind it).

**Contents:**
- Process name, machine that ran it.
- Start time, end time, duration.
- Energy consumed.
- Inputs consumed (item name, quantity).
- Outputs produced (item name, quantity).
- Inventory snapshot at the moment this process completed: all inventory items, quantities, and delta from before the process ran (what changed as a result).
- Link to the process's KB page (opens in KB Browser tab).

**Compact KB drawer:**
- The same drawer is reused for contextual KB lookups — clicking a wiki-link or a machine name anywhere in the interface opens a compact version of the KB page in the drawer, with a "Open full page" link to navigate to the KB Browser tab.

---

## Data Pipeline

The agent should write (or adapt) a Python export script on the SERES side that produces:

```
dist_data/
  sim_data.json        # event log: all process runs with timestamps, energy, inventory deltas
  kb_entities.json     # all YAML KB entries as JSON, joined with per-entity sim stats
  backlinks.json       # computed at export time by scanning wiki-links across all content
  articles/            # directory of .md files with frontmatter
    simulation_overview.md
    ...
```

**`sim_data.json` shape (suggested):**
```json
{
  "meta": {
    "sim_id": "...",
    "total_energy_kwh": 1200000,
    "total_processes": 2787,
    "machines_produced": 135,
    "sim_duration_hours": 350000
  },
  "process_runs": [
    {
      "id": "run_001",
      "process_id": "iron_smelting_reduction_v0",
      "machine_id": "electric_arc_furnace_v0",
      "start_hour": 1200,
      "end_hour": 1248,
      "energy_kwh": 450,
      "inputs": [{"item_id": "iron_ore", "qty": 100, "unit": "kg"}],
      "outputs": [{"item_id": "steel_ingot", "qty": 80, "unit": "kg"}],
      "inventory_before": {"iron_ore": 500, "steel_ingot": 20},
      "inventory_after": {"iron_ore": 400, "steel_ingot": 100}
    }
  ],
  "inventory_timeline": [
    {"hour": 0, "snapshot": {"iron_ore": 600, "steel_ingot": 0}},
    ...
  ]
}
```

**`kb_entities.json` shape (suggested):**
```json
{
  "machines": {
    "electric_arc_furnace_v0": {
      "sim_stats": {
        "total_runs": 47,
        "total_energy_kwh": 12400,
        "run_ids": ["run_001", "..."]
      }
    }
  },
  "processes": {},
  "materials": {},
  "recipes": {}
}
```

The export script should review the actual JSON already produced by SERES and adapt these shapes to match reality rather than inventing structure.

---

## Tech Stack

| Layer | Choice |
|---|---|
| Framework | React 18 |
| Build | Vite |
| Routing | React Router v6, hash mode |
| Row virtualization | TanStack Virtual (`react-virtual`) |
| Gantt bars | SVG per virtualized row |
| Markdown | `react-markdown` + custom wiki-link plugin |
| Styling | Tailwind CSS utility classes |
| Charts (sparklines, energy minimap) | Recharts or lightweight Canvas — agent's discretion |
| State | Zustand for selected process, active drawer, sim data |

---

## Aesthetic Direction: Factorio-Industrial

- Dark background (`#1a1a1a` range), not pure black.
- Accent colors: amber/orange for energy, teal/cyan for inventory, muted steel-blue for process bars. Category colors should be distinct but desaturated.
- Monospace font for IDs, timestamps, quantities. Sans-serif for prose and labels.
- Borders: visible, thin, `1px solid` slightly lighter than background. No rounded corners on data elements; small radius (2–4px) on interactive controls only.
- Hover states: brightness increase, not color change.
- Drawer: slides in from right with a subtle dark overlay, `2px` left border in the accent color matching the process category.
- Category collapse controls: chevron inline with the category label row, styled like a Factorio submenu header.
- Minimap: dark strip at bottom with energy consumption as a filled amber area, viewport indicator as a semi-transparent lighter rectangle that is draggable.

---

## Build Order (Suggested)

1. Vite + React scaffold with routing and dummy data shape.
2. Data loading layer — imports `sim_data.json` and `kb_entities.json`, exposes via Zustand store.
3. Gantt shell — machine list column + scrollable time axis + zoom/pan, no bars yet.
4. Process bars — SVG bars in virtualized rows, hover tooltip.
5. Click → sliding drawer with process details + inventory snapshot + delta.
6. Minimap strip with energy shape and draggable viewport.
7. KB Browser shell — sidebar index + hash routing.
8. Page templates — Machine, Process, Material, Recipe, Article.
9. Wiki-link rendering in articles + backlinks.
10. Home / simulation summary page.
11. Polish — aesthetic pass, category colors, typography, transitions.

---

## Open Questions for the Agent

- Review the actual SERES JSON output and adapt the suggested data shapes to match reality.
- Determine the best approach for machine categories given the actual KB YAML structure (tags, naming conventions, or explicit category field).
- Decide whether wiki-links render as inline links or inline entity cards — whichever is cleaner given the template designs.
- Confirm that `inventory_before` / `inventory_after` per process run is available in the event log, or determine how to reconstruct it from the inventory timeline.
- Determine whether the Python export script needs to be written from scratch or whether existing SERES output scripts can be adapted.
