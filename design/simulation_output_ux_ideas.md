# Simulation Output UX: Story-Driven, Cyberpunk, Markdown-Aware

Goal: make simulation output feel like a living systems console. The markdown runbook is the script; the simulator output is the live performance.

## Design principles

- Story first: surface milestones, deltas, and outcomes before raw logs.
- Progressive disclosure: show essentials by default; expand for detail.
- Intentional hierarchy: visually encode importance, scope, and state.
- Time-aware: orient users with “where we are” and “what just happened.”
- Multi-viewport: same data supports terminal, web, and notebook views.
- Markdown is a source of truth: the narrative should mirror headings, notes, and structure from the runbook file.

## Markdown-driven storytelling

Treat the runbook markdown as a script with structure:

- Headings become chapters and sections.
- `sim.note` blocks become narrations and callouts.
- `sim.runbook` becomes a nested episode with a collapsible subtree.
- Each recipe/process gets annotated under its nearest heading context.

This unlocks story-first UI:

- **Chapter header**: derived from `#` and `##` headings.
- **Scene cards**: derived from `sim.note` (style: milestone/note/warn).
- **Action rows**: derived from recipe/process start/complete events.

## Always-on telemetry (what users care about)

Make these visible at the top of every scene and at runbook end:

- ISRU % for the **current machine** (not just global sim).
- Energy used (delta + cumulative), time elapsed (delta + total).
- Imports mass (delta + cumulative), local mass produced (delta + cumulative).
- Provenance snapshot: local vs imported ratio for key outputs.
- Active phase name and current recipe/process count.

Example line (compact):

```
ISRU 62%  ⚡ +1,400 kWh (99,014)  ⏱ +15h (1469.3d)  ⇣ +125 kg (56,126)  ⬡ +375 kg (31,220)
```

## Make markdown smarter (structured storytelling)

Add light structure to `sim.note` and headings so the renderer can do more:

- `style`: milestone|info|warn|success|debug (already in use).
- `tags`: `["isru","imports","electronics"]` to drive filters.
- `metrics`: inline mini-table or key/value block to pin.
- `focus`: `item: reduction_furnace_v0` or `recipe: recipe_metal_alloy_bulk_v0`.

Example note block:

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Build reduction_furnace_shell from local metal."
    tags: ["isru","metal","phase:3"]
    focus: "item: reduction_furnace_shell"
```

## Allow structured data in markdown (for better UI)

Runbooks could include optional “story blocks” that the renderer can parse:

```md
```sim-story
title: "Phase 3: Shell Fabrication"
focus: item:reduction_furnace_shell
show: [isru, energy, imports, provenance]
table:
  - step: metal_casting_basic_v0
    output: cast_metal_parts
    delta: "+380 kg"
  - step: welding_brazing_basic_v0
    output: welded_assemblies
    delta: "+375 kg"
```
```

This keeps the runbook readable while giving the UI a richer, explicit map.

## Borrow from existing markdown extensions (cheap power)

We can “steal” common markdown patterns that already map to UI affordances:

- **Admonitions / callouts** (MkDocs Material, Obsidian):
  - `!!! warning "Imports"` → render as neon callout panel.
- **Task lists**: `- [ ] step` / `- [x] step` → progress checklist for phases.
- **Definition lists** (Pandoc): `Term :: Definition` → key/value telemetry blocks.
- **Footnotes**: provenance caveats or assumptions without clutter.
- **Emoji shortcodes**: `:bolt:` `:satellite:` → icon mapping for imports/ISRU.
- **Mermaid blocks**: show DAGs or timelines when available.
- **Tabbed content** (MkDocs): switch between “story / data / raw.”
- **Custom fenced directives** (Markdown-it): `:::phase`, `:::metrics`.

Example (admonition):

```md
!!! info "ISRU milestone"
    Local share hit 62% after shell + gas handling completion.
```

Example (task list for a phase):

```md
- [x] metal_alloy_bulk from regolith
- [x] reduction_furnace_shell
- [x] gas_handling_system
- [ ] final assembly
```

## Off-the-shelf rendering ideas (cool by default)

- **Markdown-it + plugins**: admonitions, containers, emoji, task lists.
- **Rich TUI frameworks**: `rich`/`textual` (Python), `ink` (Node), `blessed`.
- **React-style CLI**: not required, but you can mimic layout with a TUI.
- **Mermaid rendering**: optional exports to SVG for post-run reports.

These let us ship a “cyberpunk console” look quickly without inventing a new format.

## Architecture: event stream → story renderer

We need a clean separation between “what happened” and “what gets shown.” Proposed flow:

1) **Event emitters** (sim core)
   - Every sim action emits structured events with type, metadata, and deltas.
   - Examples: `import`, `recipe_start`, `recipe_end`, `process_end`, `note`.

2) **Event bus / log sink**
   - Append-only JSONL (source of truth).
   - Optional in-memory stream for live UI.

3) **Story engine (filter + summarize)**
   - Applies rules (importance, thresholds, repetition collapse).
   - Groups events by phase (markdown heading path).
   - Computes deltas: time/energy/imports/ISRU/provenance.

4) **Renderers**
   - `scroll` renderer (single-screen, narrative blocks).
   - `live` renderer (TUI dashboard).
   - `json` renderer (agent/automation).

### Event schema (minimal)

- `event_type`: `import|note|recipe_start|recipe_end|process_end|advance_time|status`
- `ts`: simulation time + wall time
- `importance`: `debug|info|milestone|warn|error`
- `phase`: markdown heading path + runbook id
- `delta`: `{time, energy, mass_local, mass_imported}`
- `items`: array of `{item_id, quantity, unit, direction}`
- `links`: `{recipe_id, process_id, runbook_id}`

### Summarization rules (examples)

- Collapse repeated low-value events (e.g., `regolith_mining_simple_v0 x20`).
- Hide “skipped import” unless `--debug`.
- Promote events that:
  - Change ISRU % beyond a threshold (e.g., +2%).
  - Add large mass/energy deltas.
  - Complete a machine or subcomponent.
- If a phase runs >N minutes, emit a periodic heartbeat summary.

### Configurable storytelling

Let users select how aggressive summarization is:

- `--verbosity quiet|normal|verbose`
- `--focus machine:<id> recipe:<id> item:<id>`
- `--collapse imports|repeats|low_energy`

### Why this matters

- Keeps the sim logs as a forensic record.
- Lets UI focus on *meaning* without losing data.
- Enables future “AI narrator” or report generator.

## Decisions (current phase)

- **Output mode**: Scroll-first, no live TUI.
- **Primary scope**: Runbook output (other CLI commands keep simple direct output for now).
- **Data contract**: We can add new event fields (phase, importance, deltas) to the stream.
- **Summarization**: Default is low-verbosity; emphasize ISRU, energy, imports, and key outputs.
- **Runbook compatibility**: Existing runbooks must remain valid; new markdown/story blocks are additive.
- **Deliverable**: Design spec + plan, not heavy implementation yet.

## Design spec (non-technical narrative)

We want simulator output to read like a mission log, not a raw firehose. The runbook already contains the story; our output should surface that story with clarity and style.

When a runbook runs, the system will still record all raw events, but the CLI will show a curated narrative:

- **Each stage becomes a scene.** Headings and milestone notes in the runbook become scene headers, so the user always knows where they are in the story.
- **Every scene has a “status line.”** This line always shows ISRU %, energy, time, imports, and local mass. It gives instant situational awareness without scrolling.
- **Details are summarized, not spammed.** Repeated actions (like many mining steps) collapse into a single line with a count. Big changes rise to the top.
- **Runbook notes become callouts.** If the author includes notes or story blocks, the output becomes more cinematic and intentional.

The result is a scrolling console that is readable, cool, and decisive: high‑signal by default, with optional depth if you need it.

## How this works at a high level

We will introduce a “story renderer” that sits between raw sim events and the terminal output. It uses light heuristics to choose what to show and how to group it. This is not a black box; it is deterministic and aligned with runbook structure.

Key mechanics:

- **Phase mapping**: events inherit the nearest runbook heading or milestone note.
- **Event importance**: errors and large deltas float to the top; routine events get summarized.
- **Telemetry overlay**: ISRU, energy, imports, local mass always visible per scene.

## What does “low‑verbosity” look like?

- Only show milestones, phase summaries, and large deltas.
- Hide “skipped import” lines unless debugging.
- Collapse repetitive process lines.
- Always show: ISRU %, energy, imports, local mass.

## Using markdown to tell the story (without breaking anything)

Runbooks can remain unchanged. If authors want richer output, they can optionally add:

- **Admonitions** (callout blocks)
- **Task lists** (phase checklists)
- **Story blocks** (`sim-story`) that define how a scene should be presented

These are additive; the renderer ignores them if absent.

## Open questions (for later)

- Should the renderer be usable for other CLI commands beyond runbooks?
- What thresholds should trigger a “large delta”?
- How much provenance detail should be visible by default?

## Information architecture (what to show)

1) **Headline summary**
   - Machine built? ISRU %? Energy used? Runtime? Imports mass?
   - Short human sentence: “Built reduction_furnace_v0 with 62% ISRU, 99014 kWh, 1469 days.”

2) **Milestone timeline**
   - Runbook start/end, sub-runbook boundaries, major phases, failures, resets.
   - Each milestone is a compact card with time, outcome, and delta.

3) **Focused phase view**
   - The “chapter” currently running (e.g., “Build gas_handling_system”).
   - Show only relevant steps and inventories touched.

4) **Diagnostics + evidence**
   - Errors, deficits, underflows, missing machines.
   - Links/refs to event IDs or files for deep dive.

5) **Raw log access**
   - Always available, but collapsed by default.
   - Toggle scopes: show only last N events, or only failures.

## CLI output design (what could look cool)

### Visual hierarchy

- Use Unicode glyphs consistently:
  - Chapter: `◈`, Section: `▶`, Success: `✔`, Warning: `▲`, Failure: `✖`
  - Info: `•`, Import: `⇣`, Local: `⬡`, Energy: `⚡`, Time: `⏱`
  - Indent depth with light box-drawing: `│  ├─  └─`
- Color themes (optional):
  - Muted base text; accent for status; dim timestamps.
  - Support `NO_COLOR` and monochrome mode by design.
  - “Cyberpunk” palette: cyan/amber/pink accents with low-contrast base.

### Tables that tell the story

Use compact, high-signal tables instead of long scrolls:

```
┌─ Phase Summary ──────────────────────────────────────────────┐
│ Phase                         Status   ΔMass     ΔEnergy     │
├───────────────────────────────────────────────────────────────┤
│ reduction_furnace_shell       ✔       +375 kg   +1,400 kWh   │
│ gas_handling_system           ✔       +145 kg     +770 kWh   │
│ power_bus_high_current         ✔        +50 u     +267 kWh   │
│ final_assembly                 ✔         1 u        +0 kWh   │
└───────────────────────────────────────────────────────────────┘
```

### Live console (htop/btop inspired)

Instead of endless scroll, use a single screen dashboard that updates:

```
┌───────────────────────── SIM STATUS ─────────────────────────┐
│ Runbook: runbook_queue_sequential         Sim: rqs           │
│ Time: 1469.3d  ⚡ 99,014 kWh  ISRU: 62%  Imports: 56,126 kg  │
├───────────────────────── ACTIVE PHASE ────────────────────────┤
│ ▶ reduction_furnace_v0_runbook                                │
│   ✔ Build shell       Δ +375 kg   ⚡ +1,400 kWh               │
│   ✔ Gas handling      Δ +145 kg   ⚡   +770 kWh               │
│   ✔ Power bus         Δ  +50 u    ⚡   +267 kWh               │
│   ▷ Final assembly    running…                                │
├───────────────────────── TOP DELTAS ─────────────────────────┤
│ + metal_alloy_bulk  +1003.2 kg   - electrical_energy  -3001  │
│ + oxygen_gas        +668.8  kg   - carbon_reducing_agent -? │
├───────────────────────── ALERTS ─────────────────────────────┤
│ ▲ Imports used: temperature_sensing, control_compute_module   │
│ ✔ No deficits                                                │
└───────────────────────────────────────────────────────────────┘
```

### Scrolling mode (single-screen for now)

Keep a normal scroll, but make it readable and story-driven by structuring each phase as a compact “scene” with a summary header, optional table, and a short tail of raw events.

Principles:

- Emit a **scene header** for each markdown heading or `sim.note` milestone.
- Collapse repeated events into a single line with counts.
- Always show a **phase summary row** (time/energy delta, key outputs).
- Keep a **short tail** (last 5–10 events) for immediacy.

Clarify the two layers:

- **Steps**: the structured summary of what ran in this phase, grouped by recipe/process with counts and key outputs. Think “index.” It’s stable, compact, and tells the story at a glance.
- **Tail**: the most recent raw event lines for immediacy (“what just happened?”). It’s ephemeral and scrolls quickly; it is not the canonical record.

Example:

```
◈ Stage 3: Reduction furnace shell (local)
  Note: "Build reduction_furnace_shell from local metal."
  Δt: +15h  ⚡ +1,400 kWh  Δmass: +375 kg  Output: reduction_furnace_shell (1)
  ┌─ Steps ────────────────────────────────────────────────────┐
  │ recipe_reduction_furnace_shell_v0  x1   ✔ completed         │
  │ metal_casting_basic_v0             x1   +380 kg             │
  │ welding_brazing_basic_v0           x1   +375 kg             │
  │ sintering_and_hot_pressing_v0      x1   +95 kg              │
  └─────────────────────────────────────────────────────────────┘
  Tail:
    ✔ metal_casting_basic_v0  → cast_metal_parts 380 kg
    ✔ welding_brazing_basic_v0 → welded_assemblies 375 kg
    ✔ sintering_and_hot_pressing_v0 → sintered_shapes 95 kg
    ✔ assembly_basic_v0 → reduction_furnace_shell 1

◈ Stage 4: Gas handling system (local)
  Note: "Build gas_handling_system from local metal."
  Δt: +60h  ⚡ +770 kWh  Δmass: +145 kg  Output: gas_handling_system (1)
  ┌─ Steps ────────────────────────────────────────────────────┐
  │ recipe_gas_handling_system_v0      x1   ✔ completed         │
  │ metal_casting_basic_v0             x1   +150 kg             │
  │ machining_finish_basic_v0          x1   +145 kg             │
  │ welding_brazing_basic_v0           x1   +145 kg             │
  └─────────────────────────────────────────────────────────────┘
  Tail:
    ✔ metal_casting_basic_v0  → cast_metal_parts 150 kg
    ✔ machining_finish_basic_v0 → machined_part_raw 145 kg
    ✔ welding_brazing_basic_v0 → welded_assemblies 145 kg
    ✔ assembly_basic_v0 → gas_handling_system 1
```

### Split-pane layout (cyberpunk workstation vibe)

- Left: timeline ribbon with milestones and phases.
- Right: context pane showing phase details and item deltas.
- Bottom: live log for last N events (auto-scroll optional).

```
┌────────── Timeline ──────────┐┌──────── Context ───────────┐
│ ◈ Runbook start               ││ Phase: gas_handling_system │
│  ▶ reduction_furnace_v0       ││ Inputs: metal_alloy_bulk   │
│   ✔ shell built               ││ Outputs: gas_handling_sys  │
│   ✔ gas handling              ││ ΔEnergy: +770 kWh          │
│   ▷ final assembly            ││ ΔMass: +145 kg             │
├──────────────────────────────┤├────────────────────────────┤
│ ▼ Live log (last 8 events)    ││ Imports used: 2            │
│  …                            ││ Local share: 62%           │
└──────────────────────────────┴┴────────────────────────────┘
```

### Example: “story” mode

```
◈ Runbook queue: runbook_queue_sequential  (sim-id: runbook_queue_sequential)
  Time: 1469.3d  ⚡ 99,014 kWh  ISRU: 62%  ⇣ Imports: 56,126 kg

▶ Phase: reduction_furnace_v0_runbook
  ✔ Build shell (local metal)    +375 kg welded  +95 kg sintered
  ✔ Gas handling system          +145 kg welded
  ✔ Power bus high current       +50 units
  ✔ Insulation pack              +1 unit (regolith-based)
  ✔ Final assembly               reduction_furnace_v0

▶ Inventory deltas (top 5)
  ⬡ metal_alloy_bulk   +1003.2 kg
  ⬡ oxygen_gas         +668.8 kg
  ⚡ electrical_energy  -3,001 kWh

▶ Diagnostics
  ▲ Imports used: temperature_sensing, control_compute_module_imported
  ✔ No deficits or underflows
```

### Example: “dense” mode for experts

```
◆ reduction_furnace_v0_runbook
  t=35149h  ΔE=+3001kWh  events=17  recipes=5  procs=16
  ├─ recipe_metal_alloy_bulk_v0 x44  → metal_alloy_bulk 1003.2 kg
  ├─ recipe_reduction_furnace_shell_v0
  ├─ recipe_gas_handling_system_v0
  ├─ recipe_power_bus_high_current_v0
  └─ recipe_machine_reduction_furnace_v0  → reduction_furnace_v0 (1)
```

## What to hide by default

- Repeated low-value logs (e.g., dozens of identical mining steps).
- Standard import “skipped” lines unless debugging.
- Full inventory dumps, unless requested.
  - Time advances with no state change.

## Show/hide based on markdown intent

Let runbooks control visibility with light markup:

- `sim.note` with `style: milestone` renders as a banner.
- `sim.note` with `style: debug` stays hidden unless `--debug`.
- `sim.note` with `style: compact` becomes a single-line row.
- `sim.runbook` renders as a collapsible subtree in TUI.

## Glyph and color system (cyberpunk)

- Accent color per phase (cycling palette).
- Status glow: `✔` green, `▲` amber, `✖` red.
- Use halfwidth blocks for gauges: `▁▂▃▄▅▆▇█`

Example gauge line:

```
ISRU 62%   ▓▓▓▓▓▓▓▓░░░░
Energy    99 MWh  ▓▓▓▓▓▓▓░░░░
Imports   56 t    ▓▓▓░░░░░░░░
```

## Rich UI concepts (if we build a GUI)

- **Runbook Map**: DAG-like view with nodes for runbooks and recipes.
- **Phase Lens**: click a phase and see only inputs/outputs touched.
- **Delta Inventory Heatmap**: highlight largest item changes in each phase.
- **Energy + Time overlays**: timeline with stacked process bars by energy.
- **Provenance lens**: “local vs import” stacked bars per machine.
- **Event scrubbing**: drag a time slider to see state snapshots.
- **Markdown storyboard**: a pane that shows the runbook headings and notes; clicking a note jumps to relevant events.

## Interaction patterns

- Filters: `--only failures`, `--only recipe`, `--only item <id>`
- Grouping: `--group-by recipe|process|item|phase`
- Folding: `--collapse repeats`, `--collapse imports`
- Focus: `--focus runbook`, `--focus machine`, `--focus recipe`
- Output modes: `story`, `dense`, `raw`, `json`, `tui`
 - Dashboard: `--ui live` renders a single-screen HUD.

## CLI options worth adding

- `sim runbook --format story|dense|raw`
- `sim runbook --collapse repeats`
- `sim runbook --highlight item:<id> recipe:<id>`
- `sim runbook --only phase:<name>`
- `sim runbook --show-deltas top:N`
- `sim runbook --quiet-imports`
- `sim runbook --ui live|split|scroll`
- `sim runbook --markdown-aware`

## Structural improvements in the event stream

Add metadata so UX can be smart:

- `phase_id`, `phase_name`, `phase_type`
- `event_importance` (info/warn/error/milestone)
- `event_group` (mining batch, recipe step)
- `item_delta` summary for each step
- `link` fields: `recipe_id`, `process_id`, `runbook_id`
- `md_context` fields: `heading_path`, `note_style`, `note_text`

## Visual “cool factor” ideas

- Terminal “glass” layout: thin borders, subtle dim headers, faint grid.
- Neon accent banners for milestones; holographic “glow” via ANSI styles.
- Micro-sparklines for energy/time deltas per phase.
- Pulse glyphs for active processes: `⟲` spinning or alternating frames.
- ASCII/Unicode bar charts for ISRU, imports, and deltas.
- “Scanline” separators to sell the workstation vibe.

## Success metrics

- 90% of users can answer “what happened?” in <10 seconds.
- Failure cause is visible without scrolling.
- Users can drill to raw logs in <2 commands.
