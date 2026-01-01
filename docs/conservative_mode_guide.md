# Conservative Mode: Root Cause Analysis for Queue Work

**Status:** Official Policy
**Version:** 1.0
**Date:** 2025-12-22

## Overview

**Conservative Mode** is the default approach for all queue work. Instead of treating queue items as direct fix requests, we treat them as **potential symptoms** that may indicate mistakes elsewhere in the knowledge base.

**Core Principle:** Minimize new creation, maximize reuse and correction.

## Key Philosophy Shift

### OLD Approach (Deprecated)
```
Queue says: "missing reference to water_vapor_v0"
Agent thinks: "I'll create water_vapor_v0"
Result: Unnecessary item proliferation
```

### NEW Approach (Conservative Mode)
```
Queue says: "missing reference to water_vapor_v0"
Agent thinks: "Why is this needed? Does 'water' already exist?
             Can the recipe use 'water' with a boiling step?"
Result: Recipe updated to use existing 'water' item with transformation
```

## Why Conservative Mode?

1. **Queue items are often symptoms, not root causes**
   - A missing reference might indicate a typo in the referencing file
   - A request for a new machine might be better served by labor bot + tools
   - A missing BOM might indicate the item doesn't need one

2. **Part/machine proliferation is the primary threat** to KB tractability
   - Every new item adds to the dependency graph
   - Similar items should be consolidated, not duplicated
   - Generic items are better than specific variants

3. **Phase/state variations should be process steps, not new items**
   - Don't create `water_liquid`, `water_vapor`, `water_ice`
   - Use one `water` item with transformation processes
   - Same for `steel_hot`, `steel_molten`, etc.

4. **Existing equivalents are common**
   - KB already has 800+ items
   - Many "missing" items have functional equivalents
   - Name variations obscure duplicates (`steel_plate` vs `plate_steel`)

---

## Conservative Mode Decision Trees

### For `referenced_only` (Missing References)

**Context:** An ID is referenced but doesn't exist in the KB.

**Decision Tree:**

```
1. Does the exact item exist under a DIFFERENT ID?
   ├─ YES → Update reference to use existing ID
   └─ NO → Continue to #2

2. Does a functionally equivalent item exist (5× magnitude rule)?
   ├─ YES → Update reference to use equivalent, document in notes
   └─ NO → Continue to #3

3. Is this a phase/state variation of an existing item?
   (water→water_vapor, steel→steel_molten, etc.)
   ├─ YES → Update referencing recipe/process to use base item
   │         + add transformation step (boiling, melting, etc.)
   └─ NO → Continue to #4

4. Could this be replaced by labor bot + existing tools?
   (See Labor Bot Decision Guide below)
   ├─ YES → Update to use labor_bot_general_v0 + appropriate tool
   └─ NO → Continue to #5

5. Is the reference itself a mistake?
   (Check git history, similar files, naming patterns)
   ├─ YES → Remove or correct the erroneous reference
   └─ NO → Continue to #6

6. CREATE new item (last resort)
   - Add note: "Created after checking: [list what you checked]"
   - Follow naming conventions
   - Apply equivalence principles for estimated parameters
```

### For `no_recipe` (Items Without Recipes)

**Context:** An item exists but has no manufacturing recipe.

**Decision Tree:**

```
1. Is this item actually referenced/used anywhere?
   Search: grep -r "item_id.*" kb/
   ├─ NO → Mark for potential deletion, investigate further
   └─ YES → Continue to #2

2. Does an equivalent item with a recipe already exist?
   (5× magnitude, same material_class, same function)
   ├─ YES → Replace references to this item with equivalent
   │         Delete this item (consolidation)
   └─ NO → Continue to #3

3. Is this a variant/phase of something with a recipe?
   ├─ YES → Update upstream recipes to produce this as variant
   │         OR merge into base item and use process variations
   └─ NO → Continue to #4

4. Should this be a BOM component rather than manufactured item?
   (Is it always part of a larger assembly?)
   ├─ YES → Remove from standalone production, keep as BOM component only
   └─ NO → Continue to #5

5. Can this be marked as import instead of manufactured?
   (Not in top contributors, high complexity, low mass impact)
   ├─ YES → Add is_import: true to item (per ADR-007), no recipe needed
   └─ NO → Continue to #6

6. CREATE new recipe (last resort)
   - Quick check: is this really needed?
   - Follow existing recipe patterns
   - Reference established processes
   - Document assumptions in notes
```

### For `missing_field` (Required Fields Not Populated)

**Context:** An item is missing required fields like `material_class`, `energy_model`, etc.

**Decision Tree:**

```
1. Is this item a duplicate of something better-defined?
   ├─ YES → Consolidate: replace references with better item, delete this one
   └─ NO → Continue to #2

2. Can the field be populated from similar items?
   (Search by function, material, mass range)
   ├─ YES → Add field value based on similar item, note provenance
   └─ NO → Continue to #3

3. Is the item definition incomplete/unclear?
   (Vague name, no notes, uncertain purpose)
   ├─ YES → Investigate purpose, consider deletion if orphaned
   └─ NO → Continue to #4

4. POPULATE missing field
   - Use conservative estimates (heavier, slower, more energy)
   - Document source: "Based on similar_item_v0"
   - Add confidence tags if available
```

### For Import Items Needing Local Manufacturing

**Context:** Item has `is_import: true` but local manufacturing may be possible (per ADR-007).

**Decision Tree:**

```
1. Is this import in top contributors to imported mass?
   Check: out/validation_report.md
   ├─ NO → Leave as import (low priority)
   └─ YES → Continue to #2

2. Can an existing recipe/process be adapted?
   ├─ YES → Create recipe variant, reference existing processes
   └─ NO → Continue to #3

3. Does local manufacturing make sense given complexity?
   (Electronics, precision optics, exotic materials)
   ├─ NO → Leave as import, add notes explaining why
   └─ YES → Continue to #4

4. CREATE local manufacturing recipe
   - Research papers for process details
   - Reference or create necessary processes
   - May create new gaps (expected and acceptable)
```

### For `no_provider_machine` (Resource Types Without Machines)

**NOTE:** This gap type is being phased out per [ADR-003](../docs/ADRs/003-process-machine-refactor.md). After migration, processes will reference specific `machine_id` instead of abstract `resource_type`.

**Current temporary guidance:**

```
1. Is this resource_type actually needed?
   (Check if it's referenced by any process)
   ├─ NO → Remove from KB
   └─ YES → Continue to #2

2. Does an existing machine already provide this capability?
   ├─ YES → Update machine's `processes_supported` list
   └─ NO → Create machine or wait for ADR-003 migration
```

---

## Labor Bot vs Special Machine Decision Guide

**CRITICAL PRINCIPLE:** Strongly prefer labor bot + tools over special-purpose machines unless high efficiency is required.

### When to Use Labor Bot + Tools

Use `labor_bot_general_v0` with existing tools for:

- **Manual assembly operations**
  - Fitting parts together
  - Fastening bolts/screws
  - Alignment and adjustment
  - Testing and inspection

- **Simple fabrication tasks**
  - Cutting with hand tools
  - Drilling with portable drill
  - Grinding/deburring with portable grinder
  - Measuring with hand tools

- **Material handling**
  - Loading/unloading
  - Positioning workpieces
  - Transferring materials
  - Sorting/organizing

- **One-off or low-volume operations**
  - Prototype assembly
  - Repair work
  - Custom modifications
  - Infrequent tasks

### When to Create Special Machine

Create a dedicated machine only when:

1. **High throughput required**
   - Continuous production (>10 units/day)
   - Automated mass production
   - Time-critical processes

2. **Precision beyond labor bot capability**
   - Tolerances <0.1mm (labor bot: ±0.5mm)
   - Optical alignment
   - Surface finish requirements
   - Automated control loops

3. **Heavy capacity beyond labor bot**
   - Loads >20kg (labor bot payload limit)
   - Forces >200N
   - Large-scale operations

4. **Environmental requirements**
   - High temperature (>200°C)
   - Vacuum operations
   - Hazardous materials
   - Controlled atmosphere

5. **Process physics requires specialized equipment**
   - Melting/casting (furnace)
   - Chemical reactions (reactor)
   - Electrolysis (electrolyzer)
   - Centrifugal forces (separator)

### Examples

**GOOD (Labor Bot + Tools):**
```yaml
# Instead of "hose_crimping_station_v0"
resource_requirements:
  - machine_id: labor_bot_general_v0
    qty: 0.5
    unit: hr
  - machine_id: crimping_tool_manual  # Simple hand tool
    qty: 0.5
    unit: hr
```

**GOOD (Labor Bot + Tools):**
```yaml
# Instead of "deburring_station_v0"
resource_requirements:
  - machine_id: labor_bot_general_v0
    qty: 1.0
    unit: hr
  - machine_id: grinding_tool_portable  # Or even just "hand_tools_general"
    qty: 1.0
    unit: hr
```

**BAD (Unnecessary Special Machine):**
```yaml
# Don't create specialized machines for simple tasks
resource_requirements:
  - machine_id: bolt_tightening_station_automated_v0  # Overkill!
    qty: 0.2
    unit: hr

# Instead use:
  - machine_id: labor_bot_general_v0
    qty: 0.2
    unit: hr
  - machine_id: wrench_torque_adjustable  # Simple tool
    qty: 0.2
    unit: hr
```

**GOOD (Necessary Special Machine):**
```yaml
# High-precision, high-volume operation
resource_requirements:
  - machine_id: cnc_mill_precision_v0  # Can't do this with labor bot
    qty: 2.0
    unit: hr
```

### Tool Reuse Strategy

Common reusable tools (prefer these over specialized machines):

- `hand_tools_general` - Wrenches, screwdrivers, pliers, etc.
- `drill_portable_electric` - For drilling operations
- `grinding_tool_portable` - For deburring, finishing
- `welding_torch_manual` - For small-scale welding
- `cutting_tools_manual` - Saws, shears, cutters
- `measuring_tools_precision` - Calipers, micrometers, gauges

**Before creating a new tool:** Search for existing tools that could work with reasonable adaptation.

---

## Naming Conventions and Equivalence

### Common Naming Variations to Check

When searching for equivalents, check these variations:

**Material/Component Order:**
- `steel_plate` vs `plate_steel`
- `motor_electric` vs `electric_motor`
- `pump_hydraulic` vs `hydraulic_pump`

**Descriptors:**
- `_basic`, `_simple`, `_standard`, `_general`
- `_small`, `_medium`, `_large`
- `_v0`, `_v1`, etc. (mostly v0 in current KB)

**Specificity:**
- `water` vs `water_liquid` vs `water_purified`
- `steel` vs `steel_alloy` vs `steel_structural`

### Search Strategies

```bash
# Search for potential equivalents
grep -i "motor.*5.*kw" kb/items/parts/*.yaml
grep -i "bearing.*steel" kb/items/parts/*.yaml

# Search for usage
grep -r "item_id: motor_general_5kw" kb/

# Search for similar names
fd -i motor kb/items/
```

---

## Documentation Requirements

### When Creating New Items

**REQUIRED in notes field:**
```yaml
notes: |
  Conservative Mode check completed:
  - Searched for: [specific search terms]
  - Checked items: [list of similar items reviewed]
  - No equivalent found within 5× magnitude
  - Created because: [specific reason]
```

### When Reusing/Adapting Existing Items

**OPTIONAL but helpful in notes:**
```yaml
notes: |
  Using existing_item_v0 (originally 3kW, this application ~5kW).
  Within 5× equivalence threshold. Acceptable for approximation.
  Verified no closer match exists.
```

### When Updating References

**Git commit messages should note:**
```
Fix: Update reference from water_vapor_v0 to water

Conservative Mode: water_vapor_v0 doesn't exist. Recipe updated to
use existing 'water' item with boiling step added to process chain.
```

---

## Integration with Existing Guidelines

Conservative Mode **extends and unifies** existing principles:

1. **From parts_and_labor_guidelines.md:**
   - 5× equivalence rule → now applies to ALL items
   - Mandatory inventory check → now for all gap types
   - Material class system → helps identify equivalents

2. **From docs/project_overview.md and docs/kb_schema_reference.md:**
   - "Structure before precision" → reuse preserves structure
   - "Processes before machines" → prefer process adaptation
   - "Incompleteness is acceptable" → don't create just to fill gaps

3. **From docs/knowledge_acquisition_protocol.md:**
   - "Best-guess engineering" → when creating, use similar items
   - "Iterative closure" → don't solve all downstream gaps at once
   - "Import termination rule" → accept imports when appropriate

---

## Exceptions and Edge Cases

### When to Skip Conservative Mode

**Immediate creation is acceptable for:**

1. **Seed file requirements** - Items explicitly listed in `kb/seeds/*.yaml`
   - These are intentional roadmaps from design docs
   - Still check for equivalents, but creation is expected

2. **Obvious gaps from recent work** - You just created item X, now need item Y
   - If tightly coupled and freshly designed
   - Still do quick equivalence check

3. **Terminal/boundary items** - Environment sources, imports
   - `environment_source_v0` for natural inputs (boundary process)
   - `is_import: true` for accepted imports (per ADR-007, no recipe needed)

### When in Doubt

**Default actions:**
- **If 80% sure equivalent exists:** Search harder, ask in notes
- **If 80% sure new item needed:** Create with documentation
- **If 50/50 uncertain:** Bias toward reuse/adaptation over creation

**Confidence calibration:**
- "I've searched thoroughly" → proceed with decision
- "I've done a quick check" → search more before creating
- "I'm not sure" → document uncertainty, use best judgment

---

## Summary Checklist

Before creating any new item, verify:

- [ ] Searched for exact ID under different name
- [ ] Checked for equivalent items (5× rule)
- [ ] Considered phase/state variation of existing item
- [ ] Evaluated labor bot + tools alternative (for machines)
- [ ] Verified reference isn't erroneous
- [ ] Searched common naming variations
- [ ] Checked if item is actually used/needed
- [ ] Reviewed similar items for parameter estimates
- [ ] Documented search in notes field

**Only after all checks:** Create new item with clear justification.

---

## Related Documentation

- **`docs/closure_error_guidance.md`** - Closure analysis error resolution (complements Conservative Mode for material flow gaps)
- **`docs/parts_and_labor_guidelines.md`** - Part reuse policy and equivalence criteria (Conservative Mode started here)
- **`docs/ADRs/003-process-machine-refactor.md`** - Resource type migration (affects `no_provider_machine` gaps)
- **`docs/project_overview.md`** - Project philosophy (minimizing proliferation)
- **`docs/kb_schema_reference.md`** - Specification and design principles
- **`docs/knowledge_acquisition_protocol.md`** - Knowledge acquisition methodology

---

## Questions or Feedback?

Conservative Mode is about using good judgment to minimize KB complexity. If you encounter situations where these guidelines conflict or are unclear:

1. Document the issue in item `notes`
2. Make a conservative choice (prefer reuse)
3. Add comment to work queue item or commit message
4. Patterns will emerge and this document will evolve
