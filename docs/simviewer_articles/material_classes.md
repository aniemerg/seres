---
id: material_classes
title: Materials and Substitution
type: article
---

SERES models materials at a level of abstraction that reflects the real goal: understanding whether in-situ resources can substitute for imported ones. The current direction separates actual item material from substitution rules.

## The Problem: Specificity vs. Flexibility

A naive model would define every material precisely: `regolith_lunar_mare`, `iron_ore_ilmenite`, `pig_iron_95pct`, and so on, with recipes that exactly specify which material feeds which process. This breaks constantly — a smelter that was designed to accept `iron_ore` cannot accept `iron_ore_ilmenite` even if they are functionally identical for this purpose.

The old material class system addressed this by letting items declare a generic *class* they belong to. That mixed two questions: what an item is made from, and what can substitute for it. The KB is migrating toward `material` for the actual material, with substitution handled by explicit material groups.

## How Materials Work

Parts should carry a `material` field:

```yaml
id: mounting_bracket_steel_v0
kind: part
material: steel
```

Material items may still carry legacy classification fields during migration,
but part material should answer what the part is actually made from.

### Legacy Broad Values

Values such as `metal`, `electronic`, and `composite` are still present in the
KB after migration. Treat them as audit flags, not high-confidence material
specifications.

## Current Status: Substitution Is Disabled

Automatic material substitution is **currently disabled** in the simulation engine. This means:

- Recipe inputs must match the exact `item_id` specified — no automatic class-based substitution occurs
- Even if two items share a legacy `material_class`, one will not automatically satisfy a recipe that calls for the other
- Future substitution should use explicit material groups with allowed contexts

**Why disabled?** During active KB development, automatic substitution can hide dependency problems. Requiring exact matches makes broken chains immediately visible, which is more valuable at this stage than smooth material flow.

When substitution is eventually enabled, the system should first try an exact item match, then consult reviewed material groups.

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
