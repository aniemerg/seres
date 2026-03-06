---
id: material_classes
title: Material Classes and the ISRU Material Flow
type: article
---

SERES models materials at a level of abstraction that reflects the real goal: understanding whether in-situ resources can substitute for imported ones. This page explains how the material class system works and what it means for interpreting recipe chains in the simulation.

## The Problem: Specificity vs. Flexibility

A naive model would define every material precisely: `regolith_lunar_mare`, `iron_ore_ilmenite`, `pig_iron_95pct`, and so on, with recipes that exactly specify which material feeds which process. This breaks constantly — a smelter that was designed to accept `iron_ore` cannot accept `iron_ore_ilmenite` even if they are functionally identical for this purpose.

The material class system addresses this by letting items declare a generic *class* they belong to. Recipes can then specify either an exact item or a class, allowing any item of that class to satisfy the requirement.

## How Material Classes Work

Each item in the KB can carry a `material_class` field:

```yaml
id: regolith_lunar_mare
kind: material
material_class: regolith

id: raw_ore_or_regolith
kind: material
material_class: regolith
```

A process that requires `raw_ore_or_regolith` would — when class substitution is enabled — also accept `regolith_lunar_mare`, because both share `material_class: regolith`.

### Common Material Classes in the KB

- **`regolith`** — Various lunar and planetary surface materials (mare, highland, carbonaceous, silicate)
- **`metal`** — Steel, aluminum, copper, iron, and alloys
- **`raw_metal_block`** — Generic metal stock; enables iron → steel substitution for structural purposes
- **`ceramic`** — Alumina, zirconia, silicate ceramics
- **`polymer`** — Silicones, plastics, elastomers
- **`glass`** — Various glass compositions
- **`composite`** — Fiber-reinforced materials

## Current Status: Substitution Is Disabled

Material class substitution is **currently disabled** in the simulation engine. This means:

- Recipe inputs must match the exact `item_id` specified — no automatic class-based substitution occurs
- Even if two items share the same `material_class`, one will not automatically satisfy a recipe that calls for the other
- The `material_class` field is present in the KB for future use and for manual equivalence checking, but does not affect simulation runs today

**Why disabled?** During active KB development, automatic substitution can hide dependency problems. Requiring exact matches makes broken chains immediately visible, which is more valuable at this stage than smooth material flow.

When substitution is eventually enabled, the system will first try an exact item match, then fall back to class-level matching.

## The ISRU Material Flow

The most important material flow in the current simulation is the chain from raw regolith to manufactured metal parts. This is the foundation of any ISRU (In-Situ Resource Utilization) scenario:

```
Regolith (mining)
  → Iron ore / ilmenite (extraction)
    → Pure iron (reduction)
      → Iron powder or sheet (processing)
        → Base metal parts (fabrication)
```

Because substitution is disabled, each step in this chain must use exact item IDs that match what the previous step produces. Small naming mismatches between what a process outputs and what the next process expects are a common source of broken chains in the current model.

See [[supply_chain_patterns]] for the specific recipe chains that have been validated end-to-end in simulation runs.

## What This Means for Recipe Interpretation

When browsing recipes in the KB viewer, you may notice that some inputs seem overly specific (`regolith_lunar_mare`) while a process logically accepts any regolith-type material. This reflects the current state of the model: the KB has the material class infrastructure, but the simulation enforces exact matching. Over time, as the KB matures, substitution rules will be enabled and recipe inputs will become more general.

## Related Articles

- [[parts_and_labor]] — How generic items are used in parts and BOMs
- [[kb_philosophy]] — Why the KB tolerates gaps and approximation
- [[supply_chain_patterns]] — Validated material flow chains from regolith to machines
