# Cached Context for Autonomous Queue Agent

This context is cached and reused across all agent invocations.

---
## 1. Agent Reference

# Agent Reference — KB Gap Analysis and Root Cause Resolution

## CONSERVATIVE MODE: Default Approach (CRITICAL)

**All queue work follows Conservative Mode** - treat queue items as potential symptoms, not direct fixes.

### Core Principle
**Minimize new creation, maximize reuse and correction.**

Before creating ANY new item:
1. **Check if it exists under a different name** (search variations: `steel_plate` vs `plate_steel`)
2. **Check for functional equivalents** (5× magnitude rule from parts_and_labor_guidelines.md)
3. **Consider phase/state variations** (don't create `water_vapor`, use `water` + boiling step)
4. **Evaluate labor bot + tools** instead of special machines (strongly preferred unless high efficiency needed)
5. **Verify the reference isn't erroneous** (check git history, similar files)

**See `docs/conservative_mode_guide.md` for complete decision trees.**

### Quick Examples

❌ **DON'T CREATE:**
- `water_vapor_v0` → ✅ Use `water` + add boiling/evaporation process step
- `hose_crimping_station_v0` → ✅ Use `labor_bot_general_v0` + `crimping_tool_manual`
- `steel_plate_large` when `steel_plate` exists → ✅ Reuse, document size variation in notes
- `deburring_machine_automated` → ✅ Use `labor_bot_general_v0` + `grinding_tool_portable`

❌ **DON'T CREATE WITHOUT CHECKING:**
- Any machine that could be labor bot + simple tool
- Any material that's a state variation (solid/liquid/gas/hot/cold)
- Any part within 5× magnitude of existing part (mass, size, function)

## Core Principles

**Import Policy:** Anything that cannot be replicated locally is treated as imported. Items without recipes become imports with mass penalties.

**Design Philosophy:**
1. **Structure before precision** — Coarse, labeled estimates are acceptable. Capture dependency structure first, refine numbers later.
2. **Processes before machines** — Prefer unit operations (crush, sinter, cast). Machines are capacity providers, not the primary abstraction.
3. **Incompleteness is acceptable** — Use placeholders (null values), surface gaps explicitly. The system must run with partial data.
4. **Labor bot + tools over special machines** — STRONGLY prefer `labor_bot_general_v0` with simple tools unless high precision/throughput/capacity required.

**Best-Guess Engineering:** When uncertain, make conservative assumptions based on similar items. Label estimates with provenance and confidence.

**When to Give Up (Import):**
- No recipe found after researching similar items AND no equivalent exists
- Modeling effort exceeds likely mass/energy impact
- Item not in top contributors to imported mass, energy, or time

---

## Schema Reference

### Materials

**Purpose:** Raw and processed materials (regolith, metals, glass, gases, intermediates).

**Required Fields:**
```yaml
id: iron_powder_v0          # lowercase_snake_case
name: Iron Powder
kind: material
unit: kg                    # typically kg; sometimes m3, mol
```

**Optional but Recommended:**
```yaml
density: 7850              # kg/m3
composition: "Fe 98%, impurities 2%"
state: powder              # solid/powder/liquid/gas
notes: "From carbothermal reduction of ilmenite"
```

**Examples:** `regolith_raw`, `oxygen_gas`, `iron_ingot`, `glass_bulk`, `slag_tailings`

---

### Parts

**Purpose:** Components and subassemblies (bearings, electrodes, crucibles, housings).

**Required Fields:**
```yaml
id: crucible_graphite_v0
name: Graphite Crucible
kind: part
mass: 15.0                 # kg (required)
material_class: ceramic    # steel/ceramic/glass/polymer/etc
```

**Optional but Recommended:**
```yaml
dimensions: "300mm dia x 400mm H"
notes: "Based on typical MRE reactor size"
```

**Examples:** `motor_stator`, `electrode_graphite_rod`, `bearing_set`, `gearbox_housing`

---

### Machines

**Purpose:** Equipment that provides manufacturing capacity.

**Required Fields:**
```yaml
id: ball_mill_v0
name: Ball Mill
kind: machine
mass: 850.0                # kg
bom: bom_ball_mill_v0      # reference to BOM (can be null early)
capabilities:
  - grinding
  - comminution
```

**Optional but Recommended:**
```yaml
power_draw_kW: 5.0
notes: "Processes regolith and mineral concentrates"
```

**Examples:** `ball_mill_v0`, `casting_furnace_v0`, `mre_reactor_v0`, `excavator_v0`

---

### BOMs (Bill of Materials)

**Purpose:** Defines what a machine or part is made of.

**Required Fields:**
```yaml
id: bom_ball_mill_v0
kind: bom
owner_item_id: ball_mill_v0
components:
  - item_id: steel_drum
    qty: 1
  - item_id: motor_assembly
    qty: 1
  - item_id: bearing_set
    qty: 2
  - item_id: grinding_media_steel
    qty: 50.0
```

**Optional:**
```yaml
scrap_rate: 0.05           # 5% material loss during assembly
notes: "Minimal BOM - full expansion deferred"
```

**Note:** Incomplete BOMs are acceptable early. Missing components reduce mass closure but don't block the model.

---

### Processes

**Purpose:** Unit operations that transform inputs to outputs using resources and energy.

**Required Fields:**
```yaml
id: crushing_basic_v0
name: Crushing (Basic)
kind: process
inputs:
  - item_id: regolith_raw
    qty: 100.0
    unit: kg
outputs:
  - item_id: regolith_crushed
    qty: 95.0
    unit: kg
byproducts:                # Optional but recommended
  - item_id: dust_fines
    qty: 5.0
    unit: kg
resource_requirements:
  - resource_type: crusher
    amount: 2.0
    unit: hr
energy_model:
  type: kWh_per_kg_input
  value: 0.5
time_model:
  type: linear_rate
  setup_hr: 0.1
  rate_kg_per_hr: 50.0
```

**Energy Model Types:**
- `kWh_per_kg_input` — Energy per kg of input material
- `kWh_per_unit_output` — Energy per unit of output
- `kW_times_time` — Power draw × time duration

**Time Model Types:**
- `fixed_time` — Constant duration regardless of quantity
- `linear_rate` — Time = setup + (qty / rate)

**Conservation:** Mass should balance (inputs ≈ outputs + byproducts). Losses to waste/byproducts are acceptable if declared.

**Examples:** `crushing_basic_v0`, `hydrogen_reduction_v0`, `casting_basic_v0`, `sintering_basic_v0`

---

### Recipes

**Purpose:** Defines how to manufacture an item (ordered list of processes).

**Required Fields:**
```yaml
id: recipe_iron_ingot_v0
kind: recipe
target_item_id: iron_ingot
steps:
  - crushing_basic_v0
  - magnetic_separation_v0
  - hydrogen_reduction_v0
  - melting_basic_v0
```

**Optional:**
```yaml
variant_id: carbothermal   # If multiple recipes exist for same item
assumptions: "Uses H2 reduction instead of carbothermal"
notes: "Based on Ellery 2018 process chain"
```

**Policy:** If multiple recipes exist, the system chooses one. If none exist, the item becomes an import.

**Examples:** `recipe_steel_sheet_v0`, `recipe_oxygen_gas_v0`, `recipe_motor_assembly_v0`

---

### Resources

**Purpose:** Resource types that constrain throughput (referenced by processes).

**Required Fields:**
```yaml
id: crusher
kind: resource
resource_type: machine_type
```

**Note:** Agents rarely create resources directly. Most are inferred from machine capabilities or process requirements.

---

## Normalization Guide

### Naming Conventions

**All IDs:** `lowercase_snake_case` with optional version suffix

**Materials:** Descriptive, no special suffix
- `regolith_raw`, `regolith_powder`, `iron_ingot`, `oxygen_gas`, `glass_bulk`

**Parts:** Component name + material/type when helpful
- `crucible_graphite`, `electrode_carbon_rod`, `bearing_steel_sealed`

**Machines:** Function + variant
- `ball_mill_v0`, `casting_furnace_v0`, `mre_reactor_v0`

**Processes:** `verb_target_variant`
- `crushing_basic_v0`, `grinding_fine_v0`, `hydrogen_reduction_ilmenite_v0`

**Recipes:** `recipe_targetitem_variant`
- `recipe_iron_ingot_v0`, `recipe_steel_sheet_basic_v0`

**BOMs:** `bom_owneritem_variant`
- `bom_ball_mill_v0`, `bom_motor_assembly_v0`

---

### Standard Units (Required)

**Mass:** `kg`
**Energy:** `kWh`
**Time:** `hr`
**Rates:** `kg/hr`
**Distance:** `km`
**Power:** `kW`

All numeric values must use these units. No conversions needed.

---

### Provenance & Uncertainty

**When possible, tag estimates:**

```yaml
mass: 125.0
mass_source: ai_estimate
mass_confidence: medium
```

**For unknowns:**

```yaml
energy_model: null
energy_confidence: unknown
```

**Source Types:** `ellery_2018`, `nasa_report`, `ai_estimate`, `hand_assumption`, `similar_to_X`

**Confidence:** `low`, `medium`, `high`, `unknown`

---

### Common Process Patterns

**Regolith Handling:**
- `excavate` → `haul` → `crush` → `grind` → `sieve` → `beneficiate`

**Oxygen Extraction:**
- `hydrogen_reduction` (ilmenite + H₂ → Fe + TiO₂ + H₂O)
- `carbothermal` (ilmenite + C → Fe + CO₂)
- `molten_regolith_electrolysis` (regolith → O₂ + metal alloy + slag)

**Metal Processing:**
- `reduction` → `melting` → `casting` → `cooling` → `machining`

**Manufacturing:**
- `casting` (pour molten metal into molds)
- `sintering` (compress powder + heat below melting point)
- `machining` (cut, drill, grind to shape)
- `assembly` (join parts into machines)

**Material Flows (Typical):**
- regolith_raw → regolith_powder → mineral_concentrate → metal + oxygen + slag
- metal → ingot → sheet/rod/tube → part → subassembly → machine

---

### Validation Rules

**Hard Errors (Must Fix):**
- Unknown or inconsistent units
- Negative quantities
- Dangling references (item_id that doesn't exist) used in active recipes

**Soft Warnings (Flag but Allow):**
- Mass imbalance in processes (unless waste/byproducts declared)
- Missing `mass` for parts (blocks mass calculations but doesn't fail)
- Missing recipe for item (becomes import, flagged in reports)
- Missing `energy_model` or `time_model` (totals will be partial)

---

## Directory Structure

```
kb/
├── items/
│   ├── materials/       # *.yaml (one per material)
│   ├── parts/           # *.yaml (one per part)
│   └── machines/        # *.yaml (one per machine)
├── processes/           # *.yaml (can group related processes)
├── recipes/             # *.yaml (one per recipe variant)
├── boms/                # *.yaml (one per complex item)
├── resources/           # *.yaml (resource type definitions)
└── seeds/               # *.yaml (seed configurations)
```

**File Naming:**
- Items: `{name}_v{N}.yaml` (e.g., `ball_mill_v0.yaml`)
- Processes: `{action}_{variant}_v{N}.yaml` (e.g., `crushing_basic_v0.yaml`)
- Recipes: `recipe_{target}_v{N}.yaml` (e.g., `recipe_steel_ingot_v0.yaml`)
- BOMs: `bom_{owner}_v{N}.yaml` (e.g., `bom_ball_mill_v0.yaml`)

---

## Conservative Mode Workflow

**REQUIRED workflow for all gap types:**

1. **Research FIRST (mandatory):**
   - Search exact ID: `grep -r "id: item_name" kb/`
   - Search variations: `grep -ri "motor.*5.*kw" kb/items/`
   - Check equivalents: review similar items for 5× magnitude match
   - Check if exists under different ID

2. **Evaluate alternatives (before creating):**
   - For machines: Could labor bot + tool do this?
   - For materials: Is this a phase variation? (water→vapor, steel→molten)
   - For parts: Is there equivalent within 5× size/mass?
   - For references: Is the reference itself a mistake?

3. **Create ONLY as last resort:**
   - Document search in notes: "Checked: X, Y, Z - no equivalents"
   - Follow existing patterns
   - Use conservative estimates
   - Apply 5× equivalence for parameters

4. **Labor Bot Decision:**
   - **Default:** Use `labor_bot_general_v0` + simple tools
   - **Special machine ONLY if:**
     - High throughput (>10 units/day continuous)
     - Precision <0.1mm (labor bot: ±0.5mm)
     - Heavy loads >20kg (labor bot payload limit)
     - Environmental (high temp, vacuum, hazardous)
     - Process physics requires it (furnace, reactor, etc.)

## Workflow Tips

1. **Research first** — Use `rg_search` to find similar items before creating new ones (MANDATORY)
2. **Follow patterns** — Copy structure from similar existing items
3. **Start minimal** — Required fields only, add optional fields later
4. **Be explicit about unknowns** — Use `null` + notes rather than omitting fields
5. **Validate early** — Run indexer after each change to catch errors
6. **Conservative assumptions** — When estimating, err on the side of heavier/slower/more energy
7. **One item at a time** — Don't try to anticipate downstream gaps, let the indexer guide you
8. **Document reuse decisions** — Note when you've checked and chosen to reuse vs create

---

## Example: Creating a New Material

```yaml
# kb/items/materials/silicon_powder_v0.yaml
id: silicon_powder_v0
name: Silicon Powder
kind: material
unit: kg
density: 2330              # kg/m3 - from literature
state: powder
notes: "Refined from lunar regolith via Mg reduction of SiO2"
```

## Example: Creating a New Process

```yaml
# kb/processes/silicon_reduction_v0.yaml
id: silicon_reduction_v0
name: Magnesium Reduction of Silica
kind: process
inputs:
  - item_id: silica_powder
    qty: 60.0
    unit: kg
  - item_id: magnesium_powder
    qty: 48.0
    unit: kg
outputs:
  - item_id: silicon_powder_v0
    qty: 28.0
    unit: kg
  - item_id: magnesium_oxide
    qty: 40.0
    unit: kg
byproducts:
  - item_id: slag_silicate
    qty: 40.0
    unit: kg
resource_requirements:
  - resource_type: reduction_furnace
    amount: 4.0
    unit: hr
energy_model:
  type: kWh_per_kg_output
  value: 15.0              # Estimate based on similar reductions
time_model:
  type: linear_rate
  setup_hr: 0.5
  rate_kg_per_hr: 7.0
notes: "Based on terrestrial Pidgeon process, adapted for lunar"
```

## Example: Creating a Recipe

```yaml
# kb/recipes/recipe_silicon_wafer_v0.yaml
id: recipe_silicon_wafer_v0
kind: recipe
target_item_id: silicon_wafer_basic
steps:
  - silicon_reduction_v0
  - silicon_purification_v0
  - crystal_growth_czochralski_v0
  - wafer_slicing_v0
assumptions: "Simplified process chain - omits several refinement steps"
notes: "Placeholder recipe for semiconductor manufacturing"
```


---
## 2. Gap Resolution Guidance


Agents MUST follow these guides when fixing queue items:


### 2.1 Conservative Mode (Default Approach)

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
   ├─ YES → Create import_placeholder recipe, mark as import
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

### For `import_stub` (Import Recipes Needing Local Manufacturing)

**Context:** Recipe uses `import_placeholder_v0` but local manufacturing may be possible.

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

2. **From memo_a.md:**
   - "Structure before precision" → reuse preserves structure
   - "Processes before machines" → prefer process adaptation
   - "Incompleteness is acceptable" → don't create just to fill gaps

3. **From memo_b.md:**
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
   - `environment_source_v0` for natural inputs
   - `import_placeholder_v0` for accepted imports

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
- **`design/meta-memo.md`** - Project philosophy (minimizing proliferation)
- **`design/memo_a.md`** - Specification and design principles
- **`design/memo_b.md`** - Knowledge acquisition methodology

---

## Questions or Feedback?

Conservative Mode is about using good judgment to minimize KB complexity. If you encounter situations where these guidelines conflict or are unclear:

1. Document the issue in item `notes`
2. Make a conservative choice (prefer reuse)
3. Add comment to work queue item or commit message
4. Patterns will emerge and this document will evolve


### 2.2 Closure Error Resolution

# Closure Error Resolution Guide

**Status:** Official Policy
**Version:** 1.0
**Date:** 2024-12-24
**Complements:** [Conservative Mode Guide](conservative_mode_guide.md)

## Overview

This guide provides decision trees for resolving closure analysis errors - material flow problems detected when tracing recipes and processes down to raw materials.

**Core Principle:** Closure errors indicate incomplete or inconsistent material flow definitions. Fix root causes, not symptoms.

---

## Error Types and Decision Trees

### 1. `null_quantity` (Process Inputs/Outputs with Null Quantities)

**Context:** A process has `qty: null` or `qty: 0` for an input or output, breaking material flow tracing.

**Example Error:**
```
Process 'welding_brazing_basic_v0' (in recipe 'recipe_printer_frame_v0')
input 'cast_metal_parts' has null/zero quantity
```

**Decision Tree:**

```
1. Is this a GENERIC process used by multiple recipes?
   (Check: grep "process_id.*{process_name}" kb/recipes/*.yaml)
   ├─ YES → Process should have null quantities
   │         → SOLUTION: Add explicit inputs/outputs to RECIPES that use it
   │         → See "Adding Recipe-Level Inputs" below
   └─ NO → Continue to #2

2. Is there a SIMILAR process with quantities defined?
   (Search: find kb/processes -name "*{function}*.yaml")
   ├─ YES → Copy quantity structure from similar process
   │         → Document: "Based on {similar_process_id}"
   └─ NO → Continue to #3

3. Can quantities be calculated from the TARGET ITEM?
   (If recipe produces X kg of item, inputs ≈ X kg + waste)
   ├─ YES → Calculate quantities based on:
   │         - Target item mass
   │         - Typical material waste (5-20%)
   │         - Material density conversions
   │         → Document assumptions in notes
   └─ NO → Continue to #4

4. Should this process be DELETED?
   (Is it unreferenced, redundant, or obsolete?)
   ├─ YES → Remove process, update referencing recipes
   └─ NO → Continue to #5

5. ESTIMATE quantities conservatively
   - Use 1 kg as default unit quantity
   - Assume 10% waste unless specific process indicates otherwise
   - Document: "Placeholder quantities, refine with research"
   - Add to queue for future refinement
```

**Adding Recipe-Level Inputs (for generic processes):**

```yaml
# BEFORE (generic process with null quantities)
id: recipe_frame_v0
target_item_id: frame_structural
steps:
  - process_id: welding_basic_v0  # Has null quantities

# AFTER (explicit recipe inputs)
id: recipe_frame_v0
target_item_id: frame_structural
inputs:
  - item_id: steel_tube_set
    qty: 5.0
    unit: kg
  - item_id: welding_rod
    qty: 0.5
    unit: kg
outputs:
  - item_id: frame_structural
    qty: 5.0
    unit: kg
steps:
  - process_id: welding_basic_v0
```

---

### 2. `recipe_no_inputs` (Recipes with No Material Flow)

**Context:** A recipe has steps but no material inputs are defined (not at recipe level, not in process steps).

**Example Error:**
```
Recipe 'recipe_motor_assembly_v0' for 'motor_electric_small' has no inputs
```

**Decision Tree:**

```
1. Does this recipe have EXPLICIT inputs/outputs at recipe level?
   (Check: recipe has 'inputs:' and 'outputs:' fields)
   ├─ YES → Check if inputs are empty or have null quantities
   │         → Fix quantities (see null_quantity guidance above)
   └─ NO → Continue to #2

2. Do the process steps have DEFINED inputs?
   (Check each process referenced in steps)
   ├─ YES (all processes have inputs) → Re-index, should resolve automatically
   └─ SOME/NONE → Continue to #3

3. Is there a BOM for the target item that shows components?
   (Check: grep "id.*bom_{target_item}" kb/boms/*.yaml)
   ├─ YES → Convert BOM components to recipe inputs
   │         → Add transformation processes as needed
   └─ NO → Continue to #4

4. Is there a SIMILAR RECIPE for reference?
   (Search for recipes producing similar items)
   ├─ YES → Copy input structure, adapt quantities
   │         → Document: "Based on {similar_recipe_id}"
   └─ NO → Continue to #5

5. Can inputs be INFERRED from the target item?
   ├─ YES → Create inputs based on:
   │         - Target item material_class
   │         - Target item mass
   │         - Typical process inputs for that material
   └─ NO → Continue to #6

6. Should this recipe be DELETED?
   (Is it redundant, obsolete, or import-only?)
   ├─ YES → Mark item as import or use different recipe
   └─ NO → Continue to #7

7. RESEARCH and create minimal inputs
   - Check papers: docs/papers/
   - Use Conservative Mode principles (prefer existing items)
   - Document assumptions clearly
   - Start with major components only
```

---

### 3. `recipe_not_found` (Referenced Recipe Doesn't Exist)

**Context:** An item references a recipe that doesn't exist in the KB.

**Example Error:**
```
Recipe 'recipe_special_alloy_v0' not found for item 'alloy_special_v0'
```

**Decision Tree:**

```
1. Is this a TYPO in the item's recipe field?
   (Check for similarly-named recipes)
   ├─ YES → Fix item's recipe field to point to correct recipe
   └─ NO → Continue to #2

2. Does the recipe exist under a DIFFERENT NAME?
   (Search: find kb/recipes -name "*{keyword}*.yaml")
   ├─ YES → Update item to reference correct recipe ID
   └─ NO → Continue to #3

3. Does the item NEED a recipe?
   (Is it used anywhere? Is it imported?)
   ├─ NO (unused/imported) → Remove recipe reference or mark as import
   └─ YES → Continue to #4

4. Can an EXISTING recipe be adapted?
   (Search for recipes producing similar items)
   ├─ YES → Create recipe variant or update item to use existing recipe
   └─ NO → Continue to #5

5. Should this be consolidated with an EQUIVALENT item?
   (Check Conservative Mode 5× equivalence rule)
   ├─ YES → Replace with equivalent item, delete this one
   └─ NO → Continue to #6

6. CREATE the recipe
   - Follow existing recipe patterns
   - Use Conservative Mode principles
   - Reference existing processes where possible
   - Document assumptions
```

---

### 4. `process_not_found` (Referenced Process Doesn't Exist)

**Context:** A recipe step references a process that doesn't exist in the KB.

**Example Error:**
```
Process 'special_welding_v0' referenced in recipe 'recipe_frame_v0' not found
```

**Decision Tree:**

```
1. Is this a TYPO in the recipe's process_id?
   (Check for similarly-named processes)
   ├─ YES → Fix recipe step to point to correct process
   └─ NO → Continue to #2

2. Does the process exist under a DIFFERENT NAME?
   (Search: find kb/processes -name "*{keyword}*.yaml")
   ├─ YES → Update recipe to reference correct process ID
   └─ NO → Continue to #3

3. Can an EXISTING process be used instead?
   (Search for processes with similar function)
   ├─ YES → Update recipe to use existing process
   │         → Document: "Using {process_id} for {operation}"
   └─ NO → Continue to #4

4. Can this be replaced with LABOR_BOT + TOOLS?
   (See Conservative Mode: Labor Bot Decision Guide)
   ├─ YES → Update recipe to use labor_bot_general_v0 + tool
   └─ NO → Continue to #5

5. Is this process truly UNIQUE and necessary?
   ├─ NO → Simplify recipe, use generic process
   └─ YES → Continue to #6

6. CREATE the process
   - Follow existing process patterns
   - Define inputs and outputs with quantities
   - Reference required machines/tools
   - Document assumptions
```

---

### 5. `item_not_found` (Item Referenced But Not Defined)

**Context:** A process or recipe references an item that doesn't exist in the KB.

**See:** Conservative Mode Guide - `referenced_only` decision tree

**Additional Closure-Specific Considerations:**

```
If detected through closure analysis:
1. Check WHICH MACHINE needs this item
   → High-priority machines → higher urgency to fix
   → Rarely-used machines → lower priority

2. Check QUANTITY needed
   → Large mass impact → create/define item
   → Small mass impact → consider consolidation/deletion

3. Follow standard referenced_only guidance with priority weighting
```

---

## Common Patterns and Solutions

### Pattern 1: Generic Process with Null Quantities

**Problem:** Process is reused across many recipes, can't have fixed quantities.

**Solution:** Add explicit inputs/outputs to recipes, keep process generic.

```yaml
# Process (generic, null quantities)
id: assembly_basic_v0
inputs: []  # Or inputs with qty: null
outputs: []

# Recipe (explicit inputs/outputs)
id: recipe_motor_v0
inputs:
  - item_id: motor_housing
    qty: 1
  - item_id: motor_rotor
    qty: 1
outputs:
  - item_id: motor_electric_small
    qty: 1
steps:
  - process_id: assembly_basic_v0  # Generic process
```

### Pattern 2: Process Chain with Intermediate Items

**Problem:** Recipe references items that aren't explicitly defined but are intermediate products.

**Solution:** Either:
- Define intermediate items as parts
- OR Inline the process chain and skip intermediate items

```yaml
# Option A: Define intermediate
id: recipe_wire_v0
inputs:
  - item_id: copper_rod
    qty: 1.0
outputs:
  - item_id: copper_wire
    qty: 0.95
steps:
  - process_id: wire_drawing_v0

# Option B: Inline (if intermediate not reused)
id: recipe_wire_v0
inputs:
  - item_id: copper_scrap
    qty: 1.1
outputs:
  - item_id: copper_wire
    qty: 0.95
steps:
  - process_id: copper_refining_v0  # scrap → rod (inlined)
  - process_id: wire_drawing_v0     # rod → wire
```

### Pattern 3: Mass Balance Issues

**Problem:** Recipe inputs total mass doesn't match outputs.

**Solution:** Add waste/loss items or adjust quantities.

```yaml
id: recipe_part_machined_v0
inputs:
  - item_id: steel_bar
    qty: 2.0
    unit: kg
outputs:
  - item_id: part_machined
    qty: 1.5
    unit: kg
  - item_id: metal_swarf  # Waste from machining
    qty: 0.5
    unit: kg
```

---

## Conservative Mode Integration

All closure error fixes MUST follow Conservative Mode principles:

1. **Check for equivalents** before creating new items/processes/recipes
2. **Prefer reuse** over creation
3. **Document assumptions** in notes fields
4. **Use 5× magnitude rule** for equivalence
5. **Minimize KB growth** - consolidate when possible

## Research Resources

When quantities or process details are unknown:

1. **Check existing KB patterns**
   ```bash
   grep -r "similar_process" kb/processes/
   ```

2. **Review papers directory**
   ```bash
   ls docs/papers/ | grep -i {topic}
   ```

3. **Use parts and labor guidelines**
   - Mass estimation guidelines
   - Material class system
   - Equivalence criteria

4. **Conservative estimates**
   - Heavier rather than lighter
   - More energy rather than less
   - More waste rather than less

---

## Validation

After fixing closure errors:

1. **Run indexer**
   ```bash
   .venv/bin/python -m kbtool index
   ```

2. **Check if error resolved**
   ```bash
   grep "{item_id}" out/closure_errors.jsonl
   ```

3. **Verify material flow**
   ```bash
   .venv/bin/python -m kbtool mat-closure --machine {machine_id}
   ```

4. **Check for new gaps**
   - Expect some new gaps when filling closure errors
   - Each fix should resolve more than it creates

---

## Agent Workflow

For autonomous queue agents processing closure errors:

```
1. Lease closure error from queue
2. Read error context (machine, recipe, process, item)
3. Apply decision tree for error type
4. Make minimal necessary changes
5. Run indexer to validate
6. Check closure error resolved
7. Complete if resolved, iterate if not
```

## Questions to Ask Yourself

Before fixing a closure error, ask:

- [ ] Have I checked for existing equivalents?
- [ ] Is this error a symptom of a deeper issue?
- [ ] Am I creating new items unnecessarily?
- [ ] Are my quantity estimates conservative?
- [ ] Have I documented my assumptions?
- [ ] Does this fix follow Conservative Mode?
- [ ] Will this create circular dependencies?

---

## Examples

### Example 1: Fixing Null Quantity

**Error:**
```
Process 'welding_basic_v0' input 'metal_parts' has null quantity
```

**Investigation:**
```bash
# Check how many recipes use this process
grep "welding_basic_v0" kb/recipes/*.yaml | wc -l
# Output: 45 recipes

# This is a generic process - don't fix the process, fix recipes
```

**Fix:** Add inputs to specific recipes that use this process

### Example 2: Fixing Recipe No Inputs

**Error:**
```
Recipe 'recipe_bracket_v0' has no inputs
```

**Investigation:**
```bash
# Read the recipe
cat kb/recipes/recipe_bracket_v0.yaml
# Shows: Only has steps, no inputs

# Check if BOM exists
grep "bracket" kb/boms/*.yaml
# Found: bom_bracket_v0 shows steel_plate component
```

**Fix:** Add inputs based on BOM
```yaml
inputs:
  - item_id: steel_plate
    qty: 0.5
    unit: kg
```

---

## Summary

**Key Takeaways:**

1. Closure errors indicate **incomplete material flow definitions**
2. Fix **root causes**, not symptoms
3. Follow **Conservative Mode** principles
4. **Document assumptions** clearly
5. **Validate** with indexer and closure analysis
6. Expect **some new gaps** - each fix should net positive

Closure errors are normal and expected. They help us systematically complete the material flow graph.


---
## 3. Knowledge Base Structure


The KB is organized as:

```
kb/
├── items/
│   ├── materials/    # Raw and processed materials (regolith, metals, glass, etc.)
│   ├── parts/        # Components (bearings, gears, electrodes, etc.)
│   └── machines/     # Equipment that provides manufacturing capacity
├── processes/        # Unit operations (crush, grind, cast, sinter, etc.)
├── recipes/          # How to make items (chains of processes)
├── boms/            # Bill of materials (item composition trees)
├── resources/       # Resource types (machine capabilities)
└── seeds/           # Seed configurations for analysis

Each YAML file defines one entity with:
- Unique `id` (lowercase snake_case)
- Required fields per kind (see memo_a.md)
- Optional provenance, notes, source_tags
```


---
## 4. Complex Examples (Templates)


Use these as templates when creating new KB entries.


### Process Examples

```yaml
# kb/processes/flywheel_motor_generator_assembly_v0.yaml
id: flywheel_motor_generator_assembly_v0
kind: process
name: Flywheel motor generator assembly v0
layer_tags:
- layer_5
- layer_6
inputs:
- item_id: machine_frame_medium
  qty: 1.0
  unit: unit
- item_id: flywheel_medium
  qty: 1.0
  unit: unit
- item_id: flywheel_vacuum_housing_v0
  qty: 1.0
  unit: unit
- item_id: magnetic_bearing_passive_v0
  qty: 1.0
  unit: unit
- item_id: bearing_race_set
  qty: 1.0
  unit: unit
- item_id: rolling_elements_set
  qty: 1.0
  unit: unit
- item_id: bearing_cage_set
  qty: 1.0
  unit: unit
- item_id: shaft_and_bearing_set
  qty: 1.0
  unit: unit
- item_id: roller_bearing_cylindrical_v0
  qty: 1.0
  unit: unit
- item_id: plain_bearing_graphite_v0
  qty: 1.0
  unit: unit
- item_id: lubrication_pack_basic
  qty: 1.0
  unit: unit
- item_id: fastener_kit_large
  qty: 1.0
  unit: unit
- item_id: power_electronics_module
  qty: 1.0
  unit: unit
outputs:
- item_id: flywheel_motor_generator_v0
  qty: 1.0
  unit: unit
requires_ids:
- assembly_station
resource_requirements:
- machine_id: assembly_station
  amount: 1.0
  unit: unit
- machine_id: labor_bot_general_v0
  qty: 1.0
  unit: hr
energy_model:
  type: kWh_per_unit_output
  value: 15.0
  notes: Placeholder energy for final assembly of flywheel_motor_generator_v0
time_model:
  type: fixed_time
  hr_per_batch: 2.0
  notes: Placeholder assembly time for flywheel_motor_generator_v0
notes: Assemble flywheel_motor_generator_v0 from BOM components; placeholder timing/energy.
```

```yaml
# kb/processes/pete_photon_enhanced_thermionic_v0_assembly_v0.yaml
id: pete_photon_enhanced_thermionic_v0_assembly_v0
kind: process
name: Assemble PETE photon-enhanced thermionic converter v0
layer_tags:
- layer_7
- layer_8
inputs:
- item_id: cathode_low_work_function_v0
  qty: 10.0
  unit: kg
- item_id: anode_collector_electrode_v0
  qty: 8.0
  unit: kg
- item_id: vacuum_envelope_quartz
  qty: 15.0
  unit: kg
- item_id: vacuum_pump_system_miniature
  qty: 1.0
  unit: unit
- item_id: electrical_feedthrough_vacuum
  qty: 20.0
  unit: unit
- item_id: thermal_insulation_high_temp
  qty: 5.0
  unit: kg
- item_id: concentrating_mirror_set
  qty: 20.0
  unit: kg
- item_id: cooling_radiator_anode
  qty: 15.0
  unit: kg
- item_id: structural_frame_steel
  qty: 25.0
  unit: kg
outputs:
- item_id: pete_photon_enhanced_thermionic_v0
  qty: 1.0
  unit: unit
requires_ids:
- assembly_station
resource_requirements:
- machine_id: assembly_station
  qty: 1.0
  unit: unit
- machine_id: labor_bot_general_v0
  qty: 4.0
  unit: hr
energy_model:
  type: kWh_per_unit_output
  value: 40.0
  notes: Preliminary energy for PETE converter assembly
time_model:
  type: fixed_time
  hr_per_batch: 12.0
  notes: Assembly time including alignment and testing
notes: Assemble PETE photon-enhanced thermionic converter from BOM components.
```

```yaml
# kb/processes/control_panel_assembly_v0.yaml
id: control_panel_assembly_v0
kind: process
name: Control panel assembly
layer_tags:
- layer_7
inputs:
- item_id: enclosure_electrical_medium
  qty: 12.0
  unit: kg
  notes: Control panel enclosure cabinet
- item_id: control_circuit_board_basic
  qty: 2.0
  unit: kg
  notes: Programmable logic controller
- item_id: relay_electromagnetic_v0
  qty: 2.0
  unit: kg
  notes: Control relays and contactors
- item_id: control_components
  qty: 1.0
  unit: kg
  notes: Selector switches and buttons
- item_id: control_components
  qty: 0.5
  unit: kg
  notes: Status indicator lights
- item_id: assembled_wire_harness
  qty: 3.0
  unit: kg
  notes: Control wiring and cable assemblies
- item_id: terminal_block_set
  qty: 2.0
  unit: kg
  notes: Terminal blocks and connectors
- item_id: control_components
  qty: 1.5
  unit: kg
  notes: Circuit protection devices
- item_id: fastener_kit_small
  qty: 0.5
  unit: kg
  notes: Mounting hardware
- item_id: din_rail_steel
  qty: 0.5
  unit: kg
  notes: Component mounting rails
outputs:
- item_id: control_panel_assembly_v0
  qty: 25.0
  unit: kg
requires_ids:
- assembly_tools_basic
- test_equipment_basic
resource_requirements:
- machine_id: labor_bot_general_v0
  qty: 1.0
  unit: hr
energy_model:
  type: kWh_per_kg
  value: 0.5
  notes: Bench assembly and test power draw.
time_model:
  type: linear_rate
  hr_per_kg: 0.4
  setup_hr: 0.2
  notes: Wiring, mounting, labeling, and functional checkout.
notes: 'Assemble control panels or control units: mount switches, indicators, wiring
  harnesses, and controllers into enclosures; includes continuity checks and basic
  functional test.

  '
```


### Recipe Examples

```yaml
# kb/recipes/recipe_bearing_set_v0.yaml
id: recipe_bearing_set_v0
name: Bearing set fabrication v0
kind: recipe
target_item_id: bearing_set
variant_id: v0
inputs:
- item_id: steel_bar_stock
  qty: 1.2
  unit: kg
  notes: High-carbon bearing steel for races and rolling elements
- item_id: brass_sheet
  qty: 0.15
  unit: kg
  notes: Bearing cage/retainer material
- item_id: grease_bearing_high_temp
  qty: 0.05
  unit: kg
  notes: Bearing grease
- item_id: seal_rubber_bearing
  qty: 0.1
  unit: kg
  notes: Optional seals
outputs:
- item_id: bearing_set
  qty: 1.5
  unit: kg
steps:
- process_id: metal_casting_basic_v0
  est_time_hr: 1.0
  machine_hours: 1.0
  notes: Cast inner and outer bearing race blanks from bearing steel
- process_id: machining_basic_v0
  est_time_hr: 1.5
  machine_hours: 1.5
  notes: Rough machine race blanks to near-net shape
- process_id: heat_treatment_hardening_v0
  est_time_hr: 3.0
  machine_hours: 3.0
  notes: Harden bearing races to HRC 58-62
- process_id: precision_grinding_basic_v0
  est_time_hr: 2.0
  machine_hours: 2.0
  notes: Precision grind race surfaces to tight tolerances
- process_id: metal_forging_process_v0
  est_time_hr: 1.0
  machine_hours: 1.0
  notes: Hot forge ball blanks from bearing steel
- process_id: heat_treatment_hardening_v0
  est_time_hr: 2.5
  machine_hours: 2.5
  notes: Harden rolling elements to HRC 60-64
- process_id: surface_grinding_precision_v0
  est_time_hr: 1.5
  machine_hours: 1.5
  notes: Precision grind balls to spherical form
- process_id: metal_casting_basic_v0
  est_time_hr: 0.3
  machine_hours: 0.3
  notes: Cast or stamp bearing cage blanks
- process_id: machining_finish_basic_v0
  est_time_hr: 0.8
  machine_hours: 0.8
  notes: Machine cage pockets
- process_id: assembly_basic_v0
  est_time_hr: 1.0
  labor_hours: 1.0
  notes: Assemble races, balls, and cage; pack with grease; install seals
assumptions: Medium bearing set (1.5 kg) for general machinery. Precision ground races
  and balls, heat-treated to bearing-grade hardness, includes lubrication and seals.
notes: Ten-step recipe covering bearing race and ball production, heat treatment,
  precision grinding, cage fabrication, and final assembly with lubrication for 35-45mm
  bore bearings.
```

```yaml
# kb/recipes/recipe_vacuum_furnace_v0_v0.yaml
id: recipe_vacuum_furnace_v0_v0
kind: recipe
target_item_id: vacuum_furnace_v0
variant_id: v0
steps:
- process_id: cutting_basic_v0
- process_id: metal_forming_basic_v0
- process_id: welded_fabrication_basic_v0
- process_id: machining_finish_basic_v0
- process_id: enclosure_assembly_basic_v0
- process_id: heating_element_installation_v0
- process_id: lamination_basic_v0
- process_id: wiring_and_electronics_integration_v0
- process_id: integration_test_basic_v0
notes: Prototype vacuum furnace v0 assembled from basic stock, welding, assembly,
  heating elements, insulation, wiring; placeholder timing/energy to be refined.
```

```yaml
# kb/recipes/recipe_machine_coordinate_measuring_machine_v0.yaml
id: recipe_machine_coordinate_measuring_machine_v0
kind: recipe
target_item_id: coordinate_measuring_machine_v0
variant_id: v0
steps:
- process_id: precision_grinding_basic_v0
  est_time_hr: 40.0
  machine_hours: 40.0
  labor_hours: 20.0
  notes: "Grind and lap granite base to extreme flatness (\xB10.001 mm)"
- process_id: machining_precision_v0
  est_time_hr: 30.0
  machine_hours: 30.0
  labor_hours: 15.0
  notes: Machine linear motion stages, guide rails, and mounting components to tight
    tolerances
- process_id: assembly_basic_v0
  est_time_hr: 20.0
  labor_hours: 20.0
  notes: Assemble X-Y-Z motion stages on granite base, install linear encoders and
    bearings
- process_id: precision_alignment_and_leveling_v0
  est_time_hr: 16.0
  labor_hours: 16.0
  notes: Align and level all axes to extreme accuracy using laser interferometer
- process_id: wiring_and_electronics_integration_v0
  est_time_hr: 8.0
  labor_hours: 8.0
  notes: Install touch probe, motion controllers, and measurement computer
- process_id: calibration_basic_v0
  est_time_hr: 12.0
  labor_hours: 12.0
  notes: Calibrate CMM using precision reference standards
- process_id: integration_test_basic_v0
  est_time_hr: 8.0
  labor_hours: 6.0
  notes: Test measurement accuracy and repeatability
- process_id: inspection_basic_v0
  est_time_hr: 2.0
  labor_hours: 2.0
  notes: "Verify CMM performance meets \xB10.005 mm tolerance specification"
assumptions: "Precision 3D coordinate measuring machine with granite base, X-Y-Z linear\
  \ stages, and touch probe. 800 kg system for dimensional inspection to \xB10.005\
  \ mm accuracy. Critical for quality control of precision parts."
notes: Manufacturing of coordinate measuring machine. Total assembly time ~136 hours.
  Requires extreme precision in grinding, machining, alignment, and calibration. Essential
  for precision manufacturing quality control.
```


### Bom Examples

```yaml
# kb/boms/bom_labor_bot_general_v0.yaml
id: bom_labor_bot_general_v0
kind: bom
owner_item_id: labor_bot_general_v0
components:
- item_id: machine_frame_small
  qty: 1
  notes: "Robot base frame, 10 kg, cast/welded steel, 600\xD7600\xD7400mm, houses\
    \ J1 rotation"
- item_id: robot_arm_link_aluminum
  qty: 1
  notes: Upper arm link, 1.0m aluminum box beam, 8 kg, houses J2 motor
- item_id: robot_arm_link_aluminum
  qty: 1
  notes: Forearm link, 0.8m aluminum tapered beam, 7 kg, houses J3 motor
- item_id: robot_wrist_3axis
  qty: 1
  notes: 3-axis wrist module (J4-J5-J6), aluminum housing with steel shafts, 5 kg
- item_id: motor_housing_cast
  qty: 6
  notes: Joint housings, aluminum castings, enclose motors/gearboxes, sealed bearings
- item_id: motor_electric_medium
  qty: 3
  notes: 400W BLDC motors for joints 1-2 (base, shoulder), 3000 rpm, integrated 20-bit
    encoders, 4 kg each
- item_id: motor_electric_medium
  qty: 1
  notes: 300W BLDC motor for joint 3 (elbow), 3000 rpm, 3 kg
- item_id: motor_electric_small
  qty: 2
  notes: 200W BLDC motors for wrist joints 4-6, 4000 rpm, 2.5 kg each
- item_id: harmonic_drive_reducer_medium
  qty: 3
  notes: 100:1 ratio, 50mm diameter, for joints 1-3 (base, shoulder, elbow), 2 kg
    each
- item_id: harmonic_drive_reducer_medium
  qty: 3
  notes: 80:1 ratio, 40mm diameter, for wrist joints 4-6, 2 kg each
- item_id: power_supply_small_imported
  qty: 1
  notes: 48V DC output, 2.5 kW continuous, from 240V 3-phase AC input, 5 kg
- item_id: power_distribution_board
  qty: 1
  notes: "PCB with bus bars, 6\xD7 circuit breakers, routes 48V to motor controllers,\
    \ 2 kg"
- item_id: battery_backup_small
  qty: 1
  notes: Li-ion 48V 100Wh emergency backup for brake holding on power loss, 1 kg
- item_id: computer_core_imported
  qty: 1
  notes: 'Industrial PC: ARM/x86 4-core, 8GB RAM, real-time Linux, EtherCAT master,
    kinematics, 3 kg'
- item_id: servo_drive_controller
  qty: 6
  notes: FOC servo drives, EtherCAT communication, 1kHz update, position/velocity/torque
    modes, 0.3 kg each
- item_id: safety_controller_plc
  qty: 1
  notes: SIL 2 safety PLC, monitors E-stop/limits, triggers Safe Torque Off, 1 kg
- item_id: sensor_suite_general
  qty: 1
  notes: "Stereo camera pair, 2\xD7 5MP cameras for pose estimation and inspection,\
    \ 30fps, 2 kg"
- item_id: force_torque_sensor_6axis
  qty: 1
  notes: "6-axis F/T sensor, \xB1200N/\xB120Nm, strain gauge on aluminum flexure,\
    \ 2 kg"
- item_id: touch_sensor_capacitive
  qty: 2
  notes: Capacitive touch sensors for gripper collision detection, 0.25 kg each
- item_id: proximity_sensor_inductive
  qty: 4
  notes: Inductive proximity sensors for workspace boundaries and homing, 0.25 kg
    each
- item_id: instrument_mounts_basic
  qty: 1
  notes: Camera mounting bracket, aluminum, 2 kg
- item_id: led_ring_light
  qty: 2
  notes: LED ring lights (12W each) for camera illumination, with diffusers, 1 kg
    each
- item_id: electric_parallel_gripper
  qty: 1
  notes: 2-finger 120mm stroke, 200N force, interchangeable jaws, aluminum body, 4
    kg
- item_id: stepper_motor_precision
  qty: 1
  notes: NEMA 23 stepper with ball screw for gripper actuation, 2 kg
- item_id: quick_change_tool_interface
  qty: 1
  notes: ISO 9409-1-50-4-M6 coupling, 8-pin connector, pneumatic/manual lock, 2 kg
- item_id: assembled_cable_harness
  qty: 6
  notes: 'Motor cables: 3m shielded 3-phase + encoder, M12/M23 connectors, 1 kg each'
- item_id: assembled_cable_harness
  qty: 1
  notes: 'Signal bundle: EtherCAT, USB3, force sensor, safety, ~25m total, 2 kg'
- item_id: cable_drag_chain
  qty: 2
  notes: Polymer energy chains for base and shoulder cable routing, 2m each, 1.5 kg
    each
- item_id: electrical_wire_and_connectors
  qty: 1
  notes: 'Connector set: M12, M23, RJ45, USB-C, terminal blocks, ~40 units, 2 kg'
- item_id: thermal_management_system
  qty: 1
  notes: "6\xD7 copper heat pipes from motors, aluminum radiator fins (0.3m\xB2),\
    \ thermal pads, 2 kg"
- item_id: control_components
  qty: 1
  notes: Includes emergency stop buttons, safety relay, and control wiring
- item_id: safety_light_curtain
  qty: 1
  notes: "Optical safety curtain, 2m\xD72m coverage, IEC 61496 Type 4, <100ms response,\
    \ 2 kg"
- item_id: protective_cover_set
  qty: 1
  notes: Polycarbonate/aluminum covers for motors, gears, pinch points, 3 kg
notes: 'Complete bill of materials for labor_bot_general_v0 - a 6-DOF industrial

  robotic manipulator for lunar manufacturing.


  Design basis: docs/labor_bot_design_memo.md

  Parts mapping: docs/labor_bot_parts_mapping.md


  Total mass: 120 kg

  - Mechanical structure: 35 kg

  - Actuation (motors + gearboxes): 30 kg

  - Power system: 8 kg

  - Control system: 6 kg

  - Sensing system: 12 kg

  - End effector: 8 kg

  - Wiring and integration: 15 kg

  - Safety and enclosure: 6 kg


  Component reuse strategy (per parts_and_labor_guidelines.md):

  - 14 existing parts reused (motors, frames, cables, sensors)

  - 18 new parts created (precision mechanisms, safety, robot-specific)


  Lunar manufacturability:

  - Structures, cables, thermal systems: ~55 kg (46%) - lunar Al/Fe/Cu

  - Motors, gearboxes, sensors: ~35 kg (29%) - partial (need magnets, precision)

  - Electronics, magnets, optics: ~30 kg (25%) - Earth import required


  Assembly time: ~140 hours (8 phases from base to testing/calibration)


  This BOM replaces the previous stub (assembly_tools_basic) with a realistic

  breakdown of robot subsystems based on industrial manipulator architecture.

  '
```

```yaml
# kb/boms/bom_labor_bot_basic_v0.yaml
id: bom_labor_bot_basic_v0
kind: bom
owner_item_id: labor_bot_basic_v0
components:
- item_id: machine_frame_small
  qty: 1
  notes: Base frame for lightweight labor bot.
- item_id: robot_arm_link_aluminum
  qty: 2
  notes: Upper arm and forearm links.
- item_id: robot_wrist_3axis
  qty: 1
  notes: Basic 3-axis wrist module.
- item_id: motor_electric_small
  qty: 4
  notes: Small motors for joints and wrist.
- item_id: harmonic_drive_reducer_medium
  qty: 4
  notes: Gear reducers for joint actuation.
- item_id: power_distribution_board
  qty: 1
  notes: Power distribution for control electronics.
- item_id: computer_core_imported
  qty: 1
  notes: Embedded controller for basic motion and coordination.
- item_id: sensor_suite_general
  qty: 1
  notes: Basic sensing package.
- item_id: led_ring_light
  qty: 1
  notes: Illumination for inspection tasks.
- item_id: electric_parallel_gripper
  qty: 1
  notes: Simple end effector for handling parts.
- item_id: assembled_cable_harness
  qty: 3
  notes: Motor and signal cabling.
- item_id: cable_drag_chain
  qty: 1
  notes: Cable routing chain.
- item_id: protective_cover_set
  qty: 1
  notes: Safety covers for moving components.
notes: Placeholder BOM; to be refined as design progresses.
```

```yaml
# kb/boms/bom_resource_3d_printer_basic_v0.yaml
id: bom_resource_3d_printer_basic_v0
kind: bom
owner_item_id: resource_3d_printer_basic_v0
components:
- item_id: printer_frame_generic
  qty: 1
- item_id: gantry_axes_set
  qty: 1
- item_id: extruder_head_basic
  qty: 1
- item_id: drive_motor_medium
  qty: 3
- item_id: gearbox_reducer_medium
  qty: 3
- item_id: bearing_set_heavy
  qty: 3
- item_id: printer_control_module
  qty: 1
- item_id: power_conditioning_module
  qty: 1
- item_id: sensor_suite_general
  qty: 1
- item_id: control_compute_module_imported
  qty: 1
- item_id: fastener_kit_medium
  qty: 1
notes: Coarse BOM for resource_3d_printer_basic_v0; matches cartesian 3D printer baseline.
```


### Machine Examples

```yaml
# kb/items/machines/basic_fabrication_station_v0.yaml
id: basic_fabrication_station_v0
name: Basic fabrication station
kind: machine
mass: 500.0
unit: kg
bom: bom_basic_fabrication_station_v0
notes: Generic fabrication station used in early-stage KB modeling. Placeholder; extend
  BOMs later.
capabilities:
- fabrication
- fixturing_table
- cutting
- drilling
- milling
- welding
- assembly
recipe: recipe_basic_fabrication_station_v0
```

```yaml
# kb/items/machines/universal_constructor_system_v0.yaml
id: universal_constructor_system_v0
kind: machine
name: Universal constructor system
mass: 1000.0
unit: kg
notes: 'Placeholder universal constructor system (v0) intended to manufacture and
  assemble other machines and parts.

  This entry resolves the queue gap for a referenced-butundefined item found in the
  seed paper_reviews_dec2024_comprehensive_v0.

  '
bom: bom_universal_constructor_system_v0
capabilities:
- assembly
- fabrication
- machining
- welding
- testing
recipe: recipe_universal_constructor_system_v0
```

```yaml
# kb/items/machines/basic_fabrication_station.yaml
id: basic_fabrication_station
name: Basic fabrication station
kind: machine
mass: 450.0
unit: kg
bom: bom_basic_fabrication_station_v0
notes: Base fabrication station (unversioned) referenced by KB gaps; extended in v0
  as needed.
capabilities:
- fabrication
- assembly
- machining
- welding
- deburring
processes_supported:
- tension_gauge_fabrication_v0
recipe: recipe_basic_fabrication_station_v1
```


### Part Examples

```yaml
# kb/items/parts/hydraulic_hose_assembly.yaml
id: hydraulic_hose_assembly
kind: part
name: Hydraulic hose assembly
mass: 3.0
unit: kg
material_class: composite
notes: Complete hydraulic hose assembly with reinforced rubber or thermoplastic hose,
  crimp fittings, and protective covering. Rated for high pressure (200-400 bar).
  Used for hydraulic power transmission in presses, cylinders, and mobile equipment.
  Includes both flexible hose and metal end fittings.
recipe: recipe_hydraulic_hose_assembly_v0
```

```yaml
# kb/items/parts/mount_frame_bearing_bores.yaml
id: mount_frame_bearing_bores
kind: part
name: Mount frame bearing bores
mass: 0.1
unit: kg
material_class: steel
notes: Mock bore features produced during bore installation on a mount frame.
recipe: recipe_mount_frame_bearing_bores_v0
```

```yaml
# kb/items/parts/antenna_matching_network.yaml
id: antenna_matching_network
name: Antenna Matching Network
kind: part
mass: 0.25
unit: kg
material_class: electronic
notes: Alias placeholder bridging to antenna_matching_network_v0; replace with a versioned
  entry later.
recipe: recipe_antenna_matching_network_unversioned_v0
```


### Material Examples

```yaml
# kb/imports/permanent_magnet_neodymium.yaml
id: import_permanent_magnet_neodymium
kind: material
is_import: true
name: Permanent magnet (neodymium, imported)
mass: 1.0
unit: kg
density: 7500
composition: Nd2Fe14B (neodymium iron boron)
state: solid
material_class: neodymium_magnet
notes: "Imported NdFeB permanent magnet for bootstrap. Used in motors and generators.\n\
  \nISRU alternative: Requires powder metallurgy \u2192 sinter NdFeB alloy from Nd/Fe/B\n\
  powders \u2192 grind/shape \u2192 magnetization. Complex rare earth extraction from\n\
  regolith needed.\n"
isru_alternative: permanent_magnet_neodymium
```

```yaml
# kb/imports/magnesium_powder.yaml
id: import_magnesium_powder
kind: material
is_import: true
name: Magnesium powder (imported)
mass: 1.0
unit: kg
density: 1748
state: powder
material_class: magnesium
notes: 'Imported magnesium powder for bootstrap. Used as feedstock for silicide formation.


  ISRU alternative: Extract from lunar regolith (MgO reduction) or seawater

  processing. Real ISRU route requires magnesium metal reduction from

  regolith-derived MgO or seawater Mg extraction.

  '
isru_alternative: magnesium_powder_v0
```

```yaml
# kb/items/materials/aluminum_metal_pure.yaml
id: aluminum_metal_pure
kind: material
name: Aluminum metal (pure)
mass: 1.0
unit: kg
density: 2700
material_class: aluminum
notes: 'Pure aluminum metal feedstock for alloying and metallurgical processes.

  Used in synthesis of aluminum-containing alloys (e.g., AlNiCo magnets).

  Produced via electrolytic reduction or purification processes.

  '
recipe: recipe_aluminum_metal_pure_v0
```


---
## 5. Available Papers


Papers are located in `design/papers/`. Use `rg_search` to search extracted text.


Available papers:

- ✓ `3-D-Printed-motors-2.pdf` → `3-D-Printed-motors-2.txt`
- ✓ `3D-Printed-Motor.pdf` → `3D-Printed-Motor.txt`
- ✓ `Affordable-rapid-bootstrapping-of-space-industry-and-solar-system-civilization.pdf` → `Affordable-rapid-bootstrapping-of-space-industry-and-solar-system-civilization.txt`
- ✓ `Alex-Ellery-CV-2023.pdf` → `Alex-Ellery-CV-2023.txt`
- ✓ `An-architecture-for-self-replicating-lunar-factories-Chirikjian.pdf` → `An-architecture-for-self-replicating-lunar-factories-Chirikjian.txt`
- ✓ `Bootstrapping-neural-electronics-from-lunar-resources.pdf` → `Bootstrapping-neural-electronics-from-lunar-resources.txt`
- ✓ `Control-of-Shape-Memory-Alloy.pdf` → `Control-of-Shape-Memory-Alloy.txt`
- ✓ `Ellery-Neural-Electronics-Lunar-2022.pdf` → `Ellery-Neural-Electronics-Lunar-2022.txt`
- ✓ `Ellery-Self-Replicating-Machines-Feasible.pdf` → `Ellery-Self-Replicating-Machines-Feasible.txt`
- ✓ `Engineering-a-lunar-photolithoautotroph-on-the-moon.pdf` → `Engineering-a-lunar-photolithoautotroph-on-the-moon.txt`
- ✓ `FFC-process-for-deep-ISRU.pdf` → `FFC-process-for-deep-ISRU.txt`
- ✓ `Heat-Pipe-Solar-Receiver-O2-2009.pdf` → `Heat-Pipe-Solar-Receiver-O2-2009.txt`
- ✓ `I-SAIRAS-2020-Sustainable-Lunar-Exploration.pdf` → `I-SAIRAS-2020-Sustainable-Lunar-Exploration.txt`
- ✓ `ISRU-Neural-Computing.pdf` → `ISRU-Neural-Computing.txt`
- ✓ `ISRU-Sensors.pdf` → `ISRU-Sensors.txt`
- ✓ `JHU-Self-Replicating-Robots-2002.pdf` → `JHU-Self-Replicating-Robots-2002.txt`
- ✓ `Lunar-Demandite.pdf` → `Lunar-Demandite.txt`
- ✓ `Lunar-ISRU-2019-Lomax.pdf` → `Lunar-ISRU-2019-Lomax.txt`
- ✓ `MIT-ISRU-Architecture-2008.pdf` → `MIT-ISRU-Architecture-2008.txt`
- ✓ `NASA-ICES-2024-ISRU-Modeling.pdf` → `NASA-ICES-2024-ISRU-Modeling.txt`
- ✓ `NASA-ISRU-Progress-2012.pdf` → `NASA-ISRU-Progress-2012.txt`
- ✓ `NASA-Lunar-Polar-Illumination-2008.pdf` → `NASA-Lunar-Polar-Illumination-2008.txt`
- ✓ `NASA-TM-20210009988-Bootstrapping-Space-Industry.pdf` → `NASA-TM-20210009988-Bootstrapping-Space-Industry.txt`
- ✓ `NIAC-Chirikjian-Self-Replicating-Lunar-Factories.pdf` → `NIAC-Chirikjian-Self-Replicating-Lunar-Factories.txt`
- ✓ `NPV-cost-benefit-analysis-of-self-replication.pdf` → `NPV-cost-benefit-analysis-of-self-replication.txt`
- ✓ `NSS-Bootstrapping-Lunar-Industry-2016.pdf` → `NSS-Bootstrapping-Lunar-Industry-2016.txt`
- ✓ `Power-on-the-Moon-using-ISRU.pdf` → `Power-on-the-Moon-using-ISRU.txt`
- ✓ `RepRap-Robotica-2011.pdf` → `RepRap-Robotica-2011.txt`
- ✓ `Rover-Prospecting-and-Mining.pdf` → `Rover-Prospecting-and-Mining.txt`
- ✓ `Self-Assembling-Structures.pdf` → `Self-Assembling-Structures.txt`
- ✓ `Self-Replicating-Machines-on-the-Moon.pdf` → `Self-Replicating-Machines-on-the-Moon.txt`
- ✓ `Sustainable-ISRU-on-the-Moon.pdf` → `Sustainable-ISRU-on-the-Moon.txt`
- ✓ `TTU-Thermal-Design-ISRU.pdf` → `TTU-Thermal-Design-ISRU.txt`
- ✓ `UCF-ISRU-Modeling-Optimization.pdf` → `UCF-ISRU-Modeling-Optimization.txt`
- ✓ `building-physical-self-replicating-machines.pdf` → `building-physical-self-replicating-machines.txt`
- ✓ `ceramics-08-00107.pdf` → `ceramics-08-00107.txt`
- ✓ `ellery-2021-generating-and-storing-power-on-the-moon-using-in-situ-resources.pdf` → `ellery-2021-generating-and-storing-power-on-the-moon-using-in-situ-resources.txt`
- ✓ `ellery-2021-leveraging-in-situ-resources-for-lunar-base-construction.pdf` → `ellery-2021-leveraging-in-situ-resources-for-lunar-base-construction.txt`
- ✓ `ellery-et-al-2022-metalysis-fray-farthing-chen-process-as-a-strategic-lunar-in-situ-resource-utilization-technology.pdf` → `ellery-et-al-2022-metalysis-fray-farthing-chen-process-as-a-strategic-lunar-in-situ-resource-utilization-technology.txt`
- ✓ `sustainable-lunar-exploration-through-self-replicating-robots.pdf` → `sustainable-lunar-exploration-through-self-replicating-robots.txt`


Key papers from Alex Ellery:
- Ellery's work on self-replicating lunar systems is canonical
- Focus on processes, ISRU methods, and manufacturable actuation
- Papers describe chemical reaction families and machine classes
- Use as primary source for process parameters and material flows


---
## 6. Queue Workflow


When working on queue items, you'll use these tools:

**Available tools (defined in queue_agents/kb_tools.py):**

- **rg_search**: Search repository using ripgrep
- **read_file**: Read file contents
- **write_file**: Write/overwrite files with diff output
- **run_indexer**: Validate changes by running the indexer
- **queue_release**: Give up on an item and release it back to pending
- **queue_add_gap**: Add discovered issues to the queue for another agent

**queue_add_gap - Reporting Discovered Issues:**

**IMPORTANT: When to fix directly vs. queue:**
- **Fix directly** if the issue is in the file you're currently editing AND you have sufficient information to make the change
- **Queue the work** if it requires special research, working in other files, or is outside your current task scope

Use this tool when you discover problems that need separate attention:

```python
queue_add_gap(
    gap_type="quality_concern",
    item_id="steel_melting_v0",
    description="Energy model shows 1.2 kWh/kg but Ellery 2023 paper indicates 3.5 kWh/kg",
    context={"paper_ref": "ellery_2023.pdf", "section": "Table 4"}
)
```

Common gap types:
- `quality_concern` - Incorrect data, unrealistic estimates, conflicts with papers
- `needs_consolidation` - Multiple similar items should be merged
- `needs_review` - Requires domain expertise or verification
- `missing_dependency` - Found reference to undefined item not caught by indexer
- `data_inconsistency` - Values don't match across related items

You can create new gap types by using descriptive names (e.g., `energy_model_mismatch`).

**Workflow:**
1. Lease next task with your agent name
2. Research the gap using rg_search and read_file
3. Fix the issue by creating/updating YAML files with write_file
4. Validate with run_indexer to ensure the gap is resolved
5. If you discover other issues, use queue_add_gap to report them
6. The system will mark your task complete automatically if validation succeeds


---
## 7. Gap Types and Validation


The indexer identifies several gap types:

1. **missing_field** - Required fields not populated
   - Examples: `material_class` for parts, `energy_model` for processes
   - Fix: Research similar items and add the missing field

2. **no_recipe** - Items without manufacturing recipes
   - These will be treated as imports unless a recipe is created
   - Fix: Create a recipe referencing appropriate processes

3. **unresolved_ref** - Free-text requirements needing definition
   - Example: `requires_text: ["ball mill or grinder"]`
   - Fix: Replace with structured `requires_ids` or create the missing item

4. **referenced_only** - IDs referenced but not defined
   - Fix: Create the missing item definition

5. **import_stub** - Recipes marked as imports needing local manufacturing
   - Fix: Replace import recipe with actual manufacturing steps

6. **no_provider_machine** - Resource types with no machine providing them
   - Fix: Add capability to an existing machine or create a new machine

The indexer outputs:
- `out/work_queue.jsonl` - All gaps (rebuilt each run)
- `out/validation_report.md` - Detailed validation results
- `out/unresolved_refs.jsonl` - Unresolved references
- `out/missing_fields.jsonl` - Missing required fields


---
## 8. Best Practices


When filling gaps:

1. **Research first**: Use `rg_search` to find similar items in the KB
2. **Follow patterns**: Use the complex examples above as templates
3. **Be specific**: Use proper IDs, units, and structure
4. **Add context**: Include notes explaining assumptions or sources
5. **One item well**: Focus on quality over quantity
6. **Let indexer guide**: Don't try to anticipate downstream gaps
7. **Conservative assumptions**: When uncertain, use reasonable defaults from similar items
8. **Provenance**: Note sources in comments (e.g., "Based on ball_mill_v0")

File naming conventions:
- Items: `{category}_{description}_v{N}.yaml` (e.g., `ball_mill_v0.yaml`)
- Processes: `{action}_{target}_{variant}.yaml` (e.g., `crushing_basic_v0.yaml`)
- Recipes: `recipe_{target}_v{N}.yaml` (e.g., `recipe_steel_ingot_v0.yaml`)
- BOMs: `bom_{owner_item}_v{N}.yaml` (e.g., `bom_ball_mill_v0.yaml`)

Required fields by kind:
- **Material**: id, name, kind: material, unit (usually kg)
- **Part**: id, name, kind: part, mass, material_class
- **Machine**: id, name, kind: machine, mass, capabilities (optional: bom)
- **Process**: id, name, inputs, outputs, resource_requirements, energy_model, time_model
- **Recipe**: id, target_item_id, steps (list of process_ids)
- **BOM**: id, owner_item_id, components (list of {item_id, qty})
