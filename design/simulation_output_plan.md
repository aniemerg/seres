# Simulation Output: Implementation Plan

Audience: decision makers and engineering leads. This plan turns the UX concept into a concrete, low-risk rollout.

## Executive summary

We will upgrade simulator output to a story-driven, low-noise scrolling console for runbooks. The system will preserve raw logs while presenting a curated narrative that surfaces ISRU %, energy, imports, and key outputs per phase. This improves readability without breaking existing runbooks or tools.

## Goals

- Make runbook output readable, structured, and cool.
- Keep raw event logs intact and authoritative.
- Use markdown structure to drive narrative without requiring runbook rewrites.
- Ship an incremental change with minimal risk.

## Non-goals (for this phase)

- No live TUI dashboard yet.
- No mandatory changes to runbook files.
- No breaking changes to existing CLI behavior outside runbooks.

## Proposed approach

1) **Event stream stays authoritative.** We keep JSONL logs as the source of truth.
2) **Add lightweight metadata.** Phase, importance, and deltas are added to events where possible.
3) **Introduce a story renderer.** A new module decides what to show in the CLI and how to group it.
4) **Scroll-first output.** The UI is a narrative scroll with scene headers, summaries, and collapses.

## What users will see

For each runbook phase:

- A scene header derived from markdown headings or `sim.note` milestones.
- A compact telemetry line: ISRU %, energy, time, imports, local mass.
- A short summary of steps and key outputs.
- Optional callouts when runbook authors add markdown story blocks.

## Deliverables

- A formal CLI output spec for runbooks (scroll mode).
- A story renderer that uses runbook structure + event metadata.
- Updated event schema to include phase/importance/delta (minimal additions).
- A small set of example outputs for internal review.

## Implementation phases

### Phase 1: Spec + alignment (1–2 weeks)

Deliver:

- Final CLI output spec (format, grouping rules, telemetry line).
- Decision log on defaults (verbosity, thresholds, always-on metrics).
- Event schema additions defined and approved.

### Phase 2: Story renderer prototype (2–3 weeks)

Deliver:

- Story renderer that groups events by phase.
- Basic summarization rules (collapse repeats, hide skipped imports).
- Telemetry line computed from existing event data.
- Scroll output for runbooks only.

### Phase 3: Markdown-aware upgrades (2–3 weeks)

Deliver:

- Optional parsing for `sim.note` styles and markdown story blocks.
- Callout rendering for `milestone`, `info`, `success`, `warn`.
- Examples in 2–3 runbooks (no breaking changes).

### Phase 4: Stabilization + review (1–2 weeks)

Deliver:

- Consistency and formatting pass.
- Performance check on large runs.
- Internal sign-off with example runbooks.

## Decisions already made

- Scroll-first output (no live TUI yet).
- Focus on runbook CLI output.
- Event stream may be extended with new metadata.
- Default verbosity is low; always show ISRU, energy, imports, local mass.

## Open questions (to decide in Phase 1)

- Thresholds for “large delta” promotion.
- How much provenance detail to show per phase.
- Naming and formatting conventions for telemetry line.

## Risks and mitigations

- Risk: Additional event fields break tooling.
  - Mitigation: Add fields additively; keep existing schema valid.
- Risk: Over-summarization hides important events.
  - Mitigation: Provide `--verbose` and `--debug` modes.
- Risk: Performance impact on large runs.
  - Mitigation: Summarize incrementally, avoid heavy lookbacks.

## Success metrics

- Users can identify phase outcome in under 10 seconds.
- ISRU %, energy, and import mass are visible in every scene.
- No regression in raw event logs or existing CLI tests.

## Recommended next step

Approve Phase 1 spec work and nominate 2–3 representative runbooks for sample output review.

## Visual mock output (scroll mode)

This mock tries to cover the main scenarios plus the “cool stuff”: cyberpunk styling, markdown‑driven callouts, task lists, compact tables/heatmaps, sparklines, split‑pane views (rendered inline), richer provenance, and icon taxonomy.

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ ░░░░░░░░░░░░░░░░░░░░  SIMULATOR // RUNBOOK  ░░░░░░░░░░░░░░░░ ┃
┃ Runbook: reduction_furnace_v0_runbook   Sim: reduction_furnace_v0_v2 ┃
┃ ISRU 62%  ⚡ +0 kWh (0)  ⏱ +0h (0d)  ⇣ +0 kg (0)  ⬡ +0 kg (0)        ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

※ Icon key (taxonomy):
  ⚡ energy  ⏱ time  ⇣ imports  ⬡ local  🧱 materials  🧰 tooling  🧪 process
  📦 inventory  🧭 provenance  ✔ success  ▲ warning  ✖ error  ▷ running

:::note "Runbook intent"
Starting reduction furnace v0 runbook (optimized).
:::

◈ Stage 1: Import fabrication equipment
  ISRU 0%  ⚡ +0 kWh (0)  ⏱ +0h (0d)  ⇣ +980 kg (980)  ⬡ +0 kg (0)
  Imports: 🧰 labor_bot_general_v0, milling_machine_general_v0, welding_power_supply_v0, furnace_basic
  ⓘ Skipped imports hidden (use --verbose to show)

◈ Stage 2: Produce metal feedstock from regolith
  ISRU 58%  ⚡ +18,000 kWh (18,000)  ⏱ +320h (13.3d)  ⇣ +0 kg (980)  ⬡ +1,003 kg (1,003)
  Summary: recipe_metal_alloy_bulk_v0 x44  → metal_alloy_bulk +1003.2 kg
  Collapsed: regolith_mining_simple_v0 x44
  Collapsed: regolith_screening_sieving_v0 x44
  Collapsed: regolith_crushing_grinding_v0 x44
  ✔ oxygen_extraction_molten_regolith_electrolysis_v0 → oxygen_gas +668.8 kg
  Sparkline (energy per batch): ▁▂▃▄▆▇█▆▅▄▃▂▁
  Heatmap (top deltas): metal_alloy_bulk ███████  oxygen_gas █████  tailings ██

◈ Stage 3: Reduction furnace shell (local)
  ISRU 61%  ⚡ +1,400 kWh (19,400)  ⏱ +15h (13.9d)  ⇣ +125 kg (1,105)  ⬡ +375 kg (1,378)
  :::info "Phase note"
  Build reduction_furnace_shell from local metal.
  :::
  ┌─ Steps (collapsed summary) ─────────────────────────────────┐
  │ 🧪 metal_casting_basic_v0             → cast_metal_parts 380 │
  │ 🧪 welding_brazing_basic_v0           → welded_assemblies 375│
  │ 🧪 sintering_and_hot_pressing_v0      → sintered_shapes 95   │
  │ 🧪 assembly_basic_v0                  → reduction_furnace_shell 1 │
  └─────────────────────────────────────────────────────────────┘
  Task list:
    - [x] cast shell parts
    - [x] weld shell assemblies
    - [x] hot press insulation
    - [x] final shell assembly

◈ Stage 4: Gas handling system (local)
  ISRU 61%  ⚡ +770 kWh (20,170)  ⏱ +60h (16.4d)  ⇣ +2 kg (1,107)  ⬡ +145 kg (1,523)
  ✔ recipe_gas_handling_system_v0  → gas_handling_system 1

◈ Stage 5: Power bus (local)
  ISRU 60%  ⚡ +267 kWh (20,437)  ⏱ +30h (17.6d)  ⇣ +0.7 kg (1,108)  ⬡ +52 kg (1,575)
  ▲ Imports used: ceramic_insulators, fastener_kit_small
  ✔ recipe_power_bus_high_current_v0 → power_bus_high_current 50

◈ Stage 6: Insulation pack (regolith-based)
  ISRU 60%  ⚡ +0 kWh (20,437)  ⏱ +6h (17.9d)  ⇣ +120 kg (1,228)  ⬡ +0 kg (1,575)
  ✔ recipe_insulation_pack_high_temp_regolith_v0 → insulation_pack_high_temp 1

◈ Stage 7: Import remaining components
  ISRU 42%  ⚡ +0 kWh (20,437)  ⏱ +0h (17.9d)  ⇣ +320 kg (1,548)  ⬡ +0 kg (1,575)
  Imports: heating_element_set_high_temp, offgas_manifold, control_compute_module_imported

◈ Stage 8: Final assembly
  ISRU 62%  ⚡ +0 kWh (20,437)  ⏱ +3h (18.0d)  ⇣ +0 kg (1,548)  ⬡ +0 kg (1,575)
  ✔ recipe_machine_reduction_furnace_v0 → reduction_furnace_v0 1
  ✔ Success: "Reduction furnace v0 complete with optimized ISRU."

◆ Checkpoint
  ISRU 62%  ⚡ 20,437 kWh  ⏱ 18.0d  ⇣ 1,548 kg  ⬡ 1,575 kg
  📦 Inventory: 114 items  |  ⇣ Imports tracked: 39
  🧭 Provenance: reduction_furnace_v0  (local 62% / imported 38%)

──────────────────────────────────────────────────────────────
Split‑pane (inline) view for context while scrolling
──────────────────────────────────────────────────────────────
┌────────── Timeline ──────────┐┌──────── Context ─────────────┐
│ ◈ Stage 1: Imports           ││ Phase: Power bus (local)      │
│  ◈ Stage 2: Feedstock         ││ Output: power_bus_high_current│
│  ◈ Stage 3: Shell             ││ ΔE: +267 kWh  ΔMass: +52 kg   │
│  ▷ Stage 5: Power bus         ││ Imports used: ceramic_insul. │
│  ◈ Stage 8: Final assembly    ││ ISRU now: 60%                │
├──────────────────────────────┤├───────────────────────────────┤
│ ▽ Live tail (last 5)          ││ 🧭 Provenance lens            │
│  ✔ metal_casting_basic_v0     ││ Local: 60%  Imported: 40%     │
│  ✔ machining_finish_basic_v0  ││ Top local: metal_alloy_bulk   │
│  ✔ assembly_basic_v0          ││ Top import: insulators        │
└──────────────────────────────┴┴───────────────────────────────┘

──────────────────────────────────────────────────────────────
Scenario: warning (resource shortfall)
──────────────────────────────────────────────────────────────
▲ Warning: insufficient carbon_reducing_agent (need 1.6 kg, have 0.8 kg)
  Suggestion: run recipe_carbon_reductant_v0 x2

──────────────────────────────────────────────────────────────
Scenario: error (missing machine)
──────────────────────────────────────────────────────────────
✖ Error: machine 'assembly_station' not found
  Cause: recipe requires assembly_station
  Next steps: import assembly_station or run assembly_station_runbook

──────────────────────────────────────────────────────────────
Scenario: provenance focus (verbose)
──────────────────────────────────────────────────────────────
▶ Provenance: welding_power_supply_v0
  Local: 41% (metal_alloy_bulk, torch_assembly, ground_clamp_and_cables)
  Imported: 59% (electronics, control_compute_module_imported)
```
