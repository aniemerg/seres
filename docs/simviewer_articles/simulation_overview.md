---
id: simulation_overview
title: Runbook Queue Sequential — Scenario Overview
type: article
related_kb_entries:
  - runbook_queue_sequential
  - labor_bot_general_v0
  - recipe_regolith_metal_crude_v0
  - recipe_iron_pig_or_ingot_v0
---

This build is based on the **runbook queue aggregator** scenario: `runbooks/runbook_queue_sequential.md`.

The scenario executes a large queue of machine-focused runbooks in sequence, each aimed at building or improving one machine using a mix of imported inputs and local (ISRU) production where possible.

See `[[runbook_queue_definition]]` for the command structure and queue execution semantics.
You can also jump via Markdown link: [Runbook Queue Definition](runbook_queue_definition).

## Snapshot Metrics

| Metric | Value | Notes |
|---|---:|---|
| Sim ID | `runbook_queue_sequential` | Shared simulation instance for the queue run |
| Total process runs | `1641` | Includes successful and failed process runs |
| Simulated time | `353197.00 h` | Long-horizon aggregate timeline |
| Total energy | `1209372.13 kWh` | Aggregate process energy from completed runs |
| Missing machine categories | `397` | KB hygiene issue highlighted in warnings |

## What This Scenario Is Testing

1. **Breadth of manufacturing coverage**
   The queue touches a wide set of machine families (mining, smelting, machining, tooling, assembly, power, and test equipment).

2. **ISRU feasibility at machine level**
   Many runbooks attempt partial or high ISRU substitutions (for example, using regolith-derived metal for frames, stock, and fasteners).

3. **Robustness under incomplete KB conditions**
   Queue execution is configured to continue on child-runbook failures, so the aggregate run can complete and expose multiple gaps in one pass.

## How to Interpret the Timeline

- The timeline is a **composite workload** from many machine-target runbooks.
- It is best interpreted as a **coverage/regression scenario**, not a single coherent mission plan.
- Use per-process drawer context (recipe + final outputs) to understand whether a process output is intermediate or terminal.

## Typical Flow Pattern

A recurring pattern in this scenario is:

- mine/regolith collection
- material concentration and extraction
- smelting/refining/casting/rolling
- part machining and assembly
- machine-level assembly recipe

You will see this reflected in recipes like `[[recipe_regolith_metal_crude_v0]]`, `[[recipe_iron_pig_or_ingot_v0]]`, and downstream machine assembly recipes.

## Known Caveats

- Some machine entries still lack `category` in KB (shown in warnings).
- Some runbooks still rely on imported items where local recipe chains are incomplete.
- A few process/recipe paths are intentionally tolerant of failure in this queue so the run can continue and expose additional issues.

## Practical Use in Simviewer

- Start with **Timeline** for execution patterns and bottlenecks.
- Use process drawer links to jump into machine/process/recipe KB entries.
- Use **Wiki** pages to inspect full YAML-derived entries, especially recipe steps and process IO definitions.
- Use **KB Search** to quickly find an entity/article by ID or title.
