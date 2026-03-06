---
id: parts_and_labor
title: How Parts and Labor Are Modeled
type: article
---

This page explains the conventions the SERES knowledge base uses for modeling manufactured parts and manufacturing labor. Understanding these conventions helps interpret what you see in the KB browser and timeline.

## Parts Philosophy

### One Part = One Identifiable Thing

Each item in the KB represents a specific, nameable component. Vague groupings ("miscellaneous hardware") are avoided. The exception is *kits* — bundled collections of near-substitutable items like fasteners or gaskets that would otherwise generate hundreds of nearly identical entries.

### The 5× Equivalence Rule

Because this is a dependency graph model — not a precision manufacturing specification — parts are consolidated aggressively. Two parts are treated as the same KB entry if they are within roughly 5× of each other in mass, size, or capability and serve the same functional purpose.

Examples of what this means in practice:
- A 5 kW motor and a 10 kW motor → same entry (`motor_general_5kw`)
- A support frame with cross-beams and one without → same entry
- A 2 kg bracket and an 8 kg bracket → same entry

This is intentional. The goal is to model *dependency structure*, not to plan a precision bill of materials. Proliferating near-identical parts makes the graph harder to analyze without adding useful information.

When a specific application needs a slightly different size than the canonical entry, the difference is noted in the recipe rather than creating a new part.

### Mass Estimates

Every part should have a mass estimate. Estimates within 5× of reality are acceptable. The mass field enables the model to track total imported mass — one of the primary bottleneck metrics.

## Bills of Materials (BOMs)

A BOM lists the parts and materials that make up a machine, with quantities. BOMs drive the recursive dependency graph: building a machine requires its parts, which may require their own sub-processes and materials.

BOMs intentionally omit items that are negligible contributors to mass or complexity. An incomplete BOM is acceptable — the gap is surfaced by the model, not hidden. Over time, BOMs are refined toward higher completeness starting with the items that matter most (top contributors to imported mass or time).

Software and digital artifacts are not BOM components. BOMs track physical mass flow.

## Labor Modeling

### Labor Bots, Not Abstract Labor Hours

Labor in SERES is modeled as machine-hours from *replicable robots* — labor bots — rather than as abstract human labor. This is a deliberate architectural choice: in a self-replicating system, labor capacity must itself be manufactured. By treating labor as a machine resource, the model can:

- Make labor capacity explicit in the dependency graph
- Account for the cost of manufacturing the labor bots themselves
- Schedule and identify labor bottlenecks

### The Primary Labor Bot

`[[labor_bot_general_v0]]` is the default labor resource for assembly and manufacturing tasks. It represents a general-purpose 6-DOF industrial manipulator (~120 kg, 2m reach, 20 kg payload, ±0.5 mm repeatability).

You will see this machine appear frequently in the timeline because almost every assembly operation requires it. Its high utilization is expected — it is the primary bottleneck resource for labor-intensive manufacturing.

```sim-query
type: table
source: sim.machines.utilization
title: Machine Utilization (All Machines)
columns: [id, name, run_count, busy_hours, utilization_percent, total_energy_kwh]
```

### When Specialized Labor Bots Are Used

Specialized labor bots are only introduced when capability requirements differ by more than 5× from the general bot — for example, heavy-lift operations (>100 kg payload), ultra-precise operations (<0.05 mm tolerance), or operations in extreme environments (vacuum, high temperature).

Most assembly, fitting, fastening, and inspection tasks are handled by `[[labor_bot_general_v0]]`.

## Material Classes

Parts and materials carry a `material_class` field that enables generic substitution — for example, allowing an iron sheet to satisfy a recipe that calls for generic metal sheet stock. This is covered in detail in [[material_classes]].

## Related Articles

- [[about_seres]] — Project overview and modeling principles
- [[kb_philosophy]] — Why the KB uses generic items and what gaps mean
- [[material_classes]] — Material types and substitution system
- [[supply_chain_patterns]] — Known validated production chains
