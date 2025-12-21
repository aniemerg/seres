# Research Question: Regolith Type Compatibility in KB

**Date:** 2024-12-20
**Context:** Base Builder Simulation - KB Gap Discovery
**Priority:** High - Blocks simulation progress

## Problem Statement

The knowledge base has a type compatibility issue between regolith collection and refining processes:

### Current Situation

**Mining outputs specific types:**
- `regolith_lunar_mare` (iron-rich)
- `regolith_lunar_highlands` (aluminum-rich)
- `regolith_carbonaceous` (carbon-rich)
- `regolith_silicate` (silicon-rich)

**Refining expects generic types:**
- `raw_ore_or_regolith`
- `lunar_regolith_raw`
- `regolith_excavated`

### The Gap

There's no defined relationship between:
1. Specific regolith types (output from mining)
2. Generic regolith types (input to refining)

This prevents building production chains: Mine → Refine → Produce

## Research Questions

### Primary Question

**How should we model material type compatibility in a self-replicating system knowledge base?**

Options to consider:
1. **Subtyping**: Are specific types (mare) subtypes of generic (regolith)?
2. **Conversion processes**: Need explicit conversion step?
3. **Material properties**: Track composition, use property-based matching?
4. **Aliasing**: Are they just different names for the same thing?

### Secondary Questions

1. **In real lunar ISRU, would different regolith types matter?**
   - Does mare vs highland regolith affect extraction processes?
   - Should we model this distinction?

2. **What's the best KB design pattern?**
   - Option A: All processes accept generic `regolith`, properties stored in item definitions
   - Option B: Type-specific processes (iron_extract_from_mare, iron_extract_from_highland)
   - Option C: Explicit conversion layer (regolith_mare → regolith_generic)

3. **How do we handle this at scale?**
   - Will every material have specific types?
   - Steel alloys? Aluminum grades?
   - How to prevent combinatorial explosion?

## Current KB State

### Items that exist:
- kb/items/materials/regolith_lunar_mare.yaml (if it exists?)
- kb/items/materials/regolith_excavated.yaml (if it exists?)

### Processes referencing regolith:
- 40+ processes found with "regolith" in name
- Examples:
  - `ilmenite_extraction_from_regolith_v0` - wants `raw_ore_or_regolith`
  - `regolith_mining_simple_v0` - produces `regolith_lunar_mare`

### Current mismatch example:
```yaml
# Process: regolith_mining_simple_v0
outputs:
  - item_id: regolith_lunar_mare
    quantity: 100
    unit: kg

# Process: ilmenite_extraction_from_regolith_v0
inputs:
  - item_id: raw_ore_or_regolith
    qty: 1.0
    unit: kg
```

These don't connect!

## Proposed Solutions (need research/validation)

### Option 1: Material Class System
Add a `material_class` field to items:
```yaml
# regolith_lunar_mare.yaml
id: regolith_lunar_mare
material_class: regolith
composition:
  iron: 0.15
  aluminum: 0.08
  silicon: 0.20
```

Processes can accept by class:
```yaml
inputs:
  - material_class: regolith
    quantity: 100
    unit: kg
```

### Option 2: Conversion Processes
Create explicit converters:
```yaml
# Process: regolith_type_normalization_v0
inputs:
  - item_id: regolith_lunar_mare
    quantity: 100
    unit: kg
outputs:
  - item_id: raw_ore_or_regolith
    quantity: 100
    unit: kg
```

### Option 3: Process Variants
Create specific versions:
```yaml
# ilmenite_extraction_from_mare_regolith_v0
inputs:
  - item_id: regolith_lunar_mare
    qty: 1.0
    unit: kg
outputs:
  - item_id: iron_ore_or_ilmenite
    qty: 0.8  # Higher yield due to iron-rich source
    unit: kg
```

### Option 4: Aliasing
Define that specific types are aliases:
```yaml
# kb/materials/aliases.yaml
aliases:
  - canonical: raw_ore_or_regolith
    aliases:
      - regolith_lunar_mare
      - regolith_lunar_highlands
      - regolith_carbonaceous
      - regolith_silicate
```

## What We Need from ChatGPT

1. **Best practices** for material type systems in knowledge bases
2. **Real-world ISRU knowledge**: Do regolith types actually matter for extraction?
3. **Ontology design**: How to model material hierarchies?
4. **Trade-offs analysis**: Pros/cons of each option
5. **Recommendation**: Which approach fits a self-replicating system KB best?

## Success Criteria

The solution should:
- ✅ Allow mining → refining chains to work
- ✅ Preserve type information where it matters (iron-rich vs aluminum-rich)
- ✅ Be simple enough to maintain at scale
- ✅ Work with simulation engine's unit converter
- ✅ Support future material types (alloys, composites, etc.)

## Additional Context

This KB is for modeling a self-replicating lunar base. It needs to:
- Track what can be made from local resources
- Understand dependencies between processes
- Support mission planning (what to import vs make locally)
- Be extensible as we add more materials/processes

The simulation agent discovered this gap autonomously by trying to build a production chain.

## References

- Base Builder Simulation: /base_builder/
- KB Processes: /kb/processes/
- KB Items: /kb/items/materials/
- ADR-004: Base Builder Simulation architecture
