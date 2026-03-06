---
id: self_reproduction
title: Self-Reproduction — What It Means and How It's Measured
type: article
---

The central question SERES investigates is whether an industrial system can reproduce itself from local resources. This page explains what that means in the context of this model and how coverage is measured in the simulation data.

## The Concept

A self-replicating industrial system is one where:

1. You start with an initial set of machines — the *seed set* — imported from elsewhere.
2. Those machines manufacture goods using locally available materials.
3. Among the goods they produce are the machines themselves.

If the set of machines you end up producing matches the set you started with, the system is *closed at the machine level*. The seed is no longer needed from outside; it can be regenerated internally.

This is a model-level result, not a real-world feasibility claim. It means: given the current knowledge base assumptions and recipe chains, the dependency graph closes. See [[about_seres]] for what the model does and does not represent.

## Seeded vs. Produced

The simulation tracks two categories of machines:

- **Seeded (imported) machines**: machine types that appear as imports at the start — they are present in the simulation but were not manufactured by it. They represent the founding equipment that must arrive from Earth (or another supply source).
- **Produced machines**: machine types that appear as outputs of process runs during the simulation. These were manufactured on-site from available materials and recipes.

A machine type is *covered* if at least one unit was produced locally during the simulation run.

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

## Coverage Ratio

Coverage is defined as:

> Coverage = machines produced that were also seeded / total seeded machine types

A coverage of 100% means every machine type in the starting seed set was also successfully manufactured during the simulation. This is the self-replication milestone.

```sim-query
type: table
source: sim.machines.coverage
title: Replication Coverage by Machine Type
columns: [id, name, imported_quantity, produced_quantity, covered]
```

> Current coverage: {{ sim.value key="sim.replication.coverage_percent" format="number:1" unit="%" }} of seeded machine types produced locally.

## What Limits Coverage

Coverage below 100% reflects one or more of the following conditions:

**Missing recipes.** Some machines have no manufacturing recipe yet in the KB. They remain imports until a recipe is added and the relevant supply chain is modeled.

**Broken supply chains.** A recipe may exist for a machine but depend on intermediate items or processes that themselves lack recipes. If any step in the chain is unresolvable, the machine cannot be produced locally.

**Material availability.** A recipe may require specific input materials that are not produced by any other process in the current run. This is often an ISRU gap — the local extraction route does not yet exist in the model.

**Conservative modeling.** The simulation does not substitute generic materials for specific ones unless explicitly configured to do so. This can break chains that would work in practice. See [[material_classes]] for details on material substitution.

All of these gaps are visible in the simulation data. Gaps are the model's primary output — they direct where KB development effort should go next.

## The Minimal Self-Reproducing Set

[[minimal_self_reproducing_set]] describes the current converged list of machine types that the model needs to form a closed, self-replicating set. Machines on that list that are not yet produced in a given simulation run represent the remaining open gaps.
