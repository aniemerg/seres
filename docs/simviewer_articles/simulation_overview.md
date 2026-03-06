---
id: simulation_overview
title: Runbook Queue Sequential - Self-Replication Scenario
type: article
related_kb_entries:
  - runbook_queue_sequential
  - labor_bot_general_v0
  - recipe_regolith_metal_crude_v0
  - recipe_iron_pig_or_ingot_v0
---

This build is based on the **runbook queue aggregator** scenario: `runbooks/runbook_queue_sequential.md`.

The core scenario question is: can an initial imported machine seed set be used to produce that same machine set locally over time?

See `[[runbook_queue_definition]]` for the command structure and queue execution semantics.
You can also jump via Markdown link: [Runbook Queue Definition](runbook_queue_definition).

## Live Snapshot

> Sim ID: {{ sim.value key="sim.id" }}  
> Simulated time: {{ sim.value key="sim.summary.time_hours" format="number:2" unit="h" }}  
> Total energy: {{ sim.value key="sim.summary.total_energy_kwh" format="number:2" unit="kWh" }}  
> Process runs: {{ sim.value key="sim.summary.process_runs_total" format="number" }}  
> Seeded machine types: {{ sim.value key="sim.replication.seed_machine_types" format="number" }}  
> Covered machine types: {{ sim.value key="sim.replication.covered_machine_types" format="number" }}  
> Coverage: {{ sim.value key="sim.replication.coverage_percent" format="number:1" unit="%" }}  
> Avg machine utilization: {{ sim.value key="sim.machines.avg_utilization_percent" format="number:1" unit="%" }}

## Seed vs Produced

```sim-query
type: two-table
title: Seeded Imports vs Produced Machines
left_source: sim.machines.seeded
left_title: Imported Seed Machines
left_columns: [id, name, imported_quantity, unit]
right_source: sim.machines.produced
right_title: Machines Produced During Simulation
right_columns: [id, name, produced_quantity, unit]
```

```sim-query
type: table
source: sim.machines.coverage
title: Replication Coverage by Machine
columns: [id, name, imported_quantity, produced_quantity, covered]
```

```sim-query
type: table
source: sim.machines.utilization
title: Machine Utilization (Ranked)
columns: [id, name, run_count, busy_hours, window_hours, utilization_percent, total_energy_kwh]
```

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

## Markers and Annotations (If Present)

```sim-query
type: table
source: sim.markers
title: Scenario Markers
columns: [sim_time_hours, name, tags, source]
```
