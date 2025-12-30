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
process_type: continuous
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
  - machine_id: crusher_basic_v0
    qty: 2.0
    unit: hr
energy_model:
  type: per_unit
  value: 0.5
  unit: kWh/kg
  scaling_basis: regolith_raw
time_model:
  type: linear_rate
  rate: 50.0
  rate_unit: kg/hr
  scaling_basis: regolith_raw
```

**Energy Model Types:**
- `per_unit` — Energy per unit (e.g., kWh/kg, kWh/unit)
- `fixed_per_batch` — Fixed energy per batch
- `boundary` — Terminal process boundary

**Time Model Types:**
- `linear_rate` — Continuous rate-based time
- `batch` — Fixed time per batch (with optional setup)
- `boundary` — Terminal process boundary

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
  - process_id: crushing_basic_v0
  - process_id: magnetic_separation_v0
  - process_id: hydrogen_reduction_v0
  - process_id: melting_basic_v0
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

**Purpose:** Processes declare resource requirements directly, typically via machine IDs.

**Required Fields:**
```yaml
resource_requirements:
  - machine_id: labor_bot_general_v0
    qty: 1.0
    unit: hr
```

**Note:** Avoid creating new resource definitions unless a schema or tool explicitly requires them.

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

### Standard Units (Preferred)

**Mass:** `kg`
**Energy:** `kWh`
**Time:** `hr`
**Rates:** compound units like `kg/hr`, `unit/hr`, `L/hr` (ADR-012)
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
process_type: batch
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
  - machine_id: reduction_furnace_v0
    qty: 4.0
    unit: hr
energy_model:
  type: fixed_per_batch
  value: 120.0             # Estimate based on similar reductions
  unit: kWh
time_model:
  type: batch
  setup_hr: 0.5
  hr_per_batch: 3.5
notes: "Based on terrestrial Pidgeon process, adapted for lunar"
```

## Example: Creating a Recipe

```yaml
# kb/recipes/recipe_silicon_wafer_v0.yaml
id: recipe_silicon_wafer_v0
kind: recipe
target_item_id: silicon_wafer_basic
steps:
  - process_id: silicon_reduction_v0
  - process_id: silicon_purification_v0
  - process_id: crystal_growth_czochralski_v0
  - process_id: wafer_slicing_v0
assumptions: "Simplified process chain - omits several refinement steps"
notes: "Placeholder recipe for semiconductor manufacturing"
```
