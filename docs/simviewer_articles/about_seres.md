---
id: about_seres
title: About SERES — Project Overview
type: article
---

SERES is a computational framework for analyzing whether an industrial system can reproduce its own machines using locally available resources. The primary application is space manufacturing — lunar or Martian surface settlement scenarios where resupply from Earth is expensive or impossible.

The project turns informal claims ("we could build everything from regolith") into a computable dependency graph with explicit mass, energy, and time accounting, so tradeoffs and bottlenecks are visible rather than assumed.

## Navigate This Wiki

**New to SERES?** Start here, then follow the links below in order.

| Article | What it covers |
|---|---|
| [[self_reproduction]] | What "self-reproduction" means, how coverage is measured, and what limits it |
| [[minimal_self_reproducing_set]] | The current converged list of machine types the model needs to close |
| [[supply_chain_patterns]] | The validated production chains from raw regolith to finished machines |
| [[material_classes]] | How materials are classified, ISRU substitution, and why exact IDs matter now |
| [[parts_and_labor]] | How parts, BOMs, and labor bots are modeled — why things look generic |
| [[kb_philosophy]] | Why gaps and imports exist and what the warnings mean |
| [[simulation_overview]] | This simulation's live dashboard — timeline, coverage tables, utilization |

---

## What This Simulation Is

Each simulation models a sequence of manufacturing processes. The engine works from a *knowledge base* (KB) of items, processes, and recipes, and executes a *runbook* — a scripted production plan that chains manufacturing steps together to build specified machines.

The central question is: **can the machines we start with produce those same machines locally?** See [[self_reproduction]] for how this is measured and what the coverage metrics mean.

## Modeling Philosophy

Four principles guide how the KB is built and how gaps are handled.

**Structure before precision.** Coarse estimates are acceptable if they preserve dependency relationships. A motor estimated at 2–3 kg rather than a precisely measured 2.4 kg does not change the dependency graph. The accuracy of relationships matters more than the accuracy of individual numbers.

**Processes before machines.** Manufacturing unit operations — smelting, casting, machining, assembly — are modeled first. Machines appear both as tools that run processes and as manufactured products that processes produce. This keeps the model grounded in physical reality: you can't build a machine without the equipment to build it.

**Incompleteness is a feature.** The simulation runs with missing data and surfaces gaps rather than hiding them. Items that cannot yet be manufactured locally are treated as *imports* — a boundary condition that assigns an explicit mass penalty to unknowns. This keeps gaps visible and quantified.

**Iteration is driven by bottlenecks.** Modeling effort is focused on the top contributors to imported mass, energy, and time. The long tail of minor components can remain approximate indefinitely. The system is designed for incremental refinement, not one-shot completeness.

## What Is and Is Not Modeled

**In scope:**
- A computable dependency graph across items, processes, and recipes
- Mass, energy, and time accounting with explicit gaps at every node
- Machine-level self-reproduction coverage analysis
- ISRU (In-Situ Resource Utilization) feasibility at the machine level

**Out of scope (by design):**
- High-fidelity chemistry or precision manufacturing tolerances
- Full logistics, scheduling, or mission planning
- Claims of real-world engineering feasibility — this is a model, not a design

## How the KB Is Organized

The knowledge base has three entity types:

- **Items** — materials (regolith, metals, chemicals), parts (bearings, motors, frames), and machines (mills, furnaces, assembly stations)
- **Processes** — unit operations such as smelting, casting, CNC milling, chemical extraction
- **Recipes** — concrete parameterized instances of processes with specific inputs, outputs, time, and energy requirements

See [[parts_and_labor]] for how parts and manufacturing labor are modeled, and [[kb_philosophy]] for why the KB intentionally uses generic, approximate items rather than precise specifications.
