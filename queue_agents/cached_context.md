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
## 2. Knowledge Base Structure


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
## 3. Complex Examples (Templates)


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
- item_id: enclosure_steel_electronics
  qty: 12.0
  unit: kg
  notes: Control panel enclosure cabinet
- item_id: control_plc_basic
  qty: 2.0
  unit: kg
  notes: Programmable logic controller
- item_id: relay_set_industrial
  qty: 2.0
  unit: kg
  notes: Control relays and contactors
- item_id: switch_selector_industrial
  qty: 1.0
  unit: kg
  notes: Selector switches and buttons
- item_id: indicator_light_set
  qty: 0.5
  unit: kg
  notes: Status indicator lights
- item_id: wire_harness_control
  qty: 3.0
  unit: kg
  notes: Control wiring and cable assemblies
- item_id: terminal_block_set
  qty: 2.0
  unit: kg
  notes: Terminal blocks and connectors
- item_id: circuit_breaker_set
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
- item_id: bearing_steel_bar
  qty: 1.2
  unit: kg
  notes: High-carbon bearing steel for races and rolling elements
- item_id: brass_sheet
  qty: 0.15
  unit: kg
  notes: Bearing cage/retainer material
- item_id: lubricant_grease_bearing
  qty: 0.05
  unit: kg
  notes: Bearing grease
- item_id: bearing_seal_rubber
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
- item_id: emergency_stop_system
  qty: 1
  notes: "2\xD7 mushroom buttons, dual-channel safety relay, wiring, 1 kg"
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
# kb/boms/bom_welding_tig_unit_v0_v0.yaml
id: bom_welding_tig_unit_v0_v0
kind: bom
owner_item_id: welding_tig_unit_v0
components:
- item_id: torch_assembly
  qty: 1.0
  unit: unit
  notes: TIG torch assembly
- item_id: welding_power_supply_unit
  qty: 1.0
  unit: unit
  notes: Welding power supply unit
- item_id: gas_supply_regulator
  qty: 1.0
  unit: unit
  notes: Gas regulator for TIG arc shielding gas
- item_id: gas_cylinder_argon_or_nitrogen
  qty: 1.0
  unit: unit
  notes: Inert shielding gas cylinder (argon or nitrogen)
- item_id: gas_flow_controller
  qty: 1.0
  unit: unit
  notes: Gas flow controller for TIG torch
- item_id: gas_inlet_manifold
  qty: 1.0
  unit: unit
- item_id: inert_gas_manifold
  qty: 1.0
  unit: unit
- item_id: coolant_loop_basic
  qty: 1.0
  unit: unit
  notes: Coolant loop for TIG power electronics
- item_id: circulation_pump_coolant
  qty: 1.0
  unit: unit
- item_id: control_panel_basic
  qty: 1.0
  unit: unit
notes: Expanded BOM for TIG welding unit; includes essential subsystems for gas handling
  and cooling.
```

```yaml
# kb/boms/bom_hpht_furnace_v0.yaml
id: bom_hpht_furnace_v0
kind: bom
owner_item_id: hpht_furnace_v0
components:
- item_id: furnace_shell_refractory
  qty: 1
- item_id: heating_element_set_high_temp
  qty: 1
- item_id: insulation_pack_high_temp
  qty: 1
- item_id: temperature_controller_basic
  qty: 1
- item_id: power_conditioning_module
  qty: 1
- item_id: cooling_loop_basic
  qty: 1
- item_id: power_bus_high_current
  qty: 1
- item_id: control_compute_module_imported
  qty: 1
- item_id: fastener_kit_medium
  qty: 4
notes: Placeholder HPHT furnace BOM; refined with complete hardware data.
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
# kb/items/materials/hydrogen_chloride.yaml
id: hydrogen_chloride
name: Hydrogen Chloride
kind: material
mass: 1.0
unit: kg
material_class: gas
state: gas
physical_properties:
  boiling_point_c: -85.05
  notes: Colorless gas at STP. When dissolved in water, forms hydrochloric acid solution.
notes: 'Hydrogen chloride (HCl). Colorless, pungent gas at STP.

  Dissolves in water to form hydrochloric acid (aqueous HCl).

  Product of chlorination and carbochlorination processes.

  Recyclable in closed-loop leaching systems.

  '
recipe: recipe_hydrogen_chloride_v0
```

```yaml
# kb/items/materials/epoxy_precursor_block_v0.yaml
id: epoxy_precursor_block_v0
name: Epoxy resin precursor block
kind: material
mass: 1.0
unit: kg
material_class: polymer
notes: Placeholder precursor material for epoxy resin base synthesis. Represents unreacted
  epoxy monomer or prepolymer stage.
recipe: recipe_epoxy_precursor_block_v0
```

```yaml
# kb/items/materials/silicon_tetrachloride.yaml
id: silicon_tetrachloride
name: Silicon Tetrachloride
kind: material
mass: 1.0
unit: kg
material_class: chemical
state: liquid
physical_properties:
  boiling_point_c: 57.6
  melting_point_c: -68.7
  notes: Colorless fuming liquid at STP. Volatile, reacts with moisture.
notes: 'Silicon tetrachloride (SiCl4). Liquid at room temperature.

  Intermediate in silicon purification via Siemens process.

  Produced via carbochlorination of silicates.

  Highly reactive with water, producing HCl and silicic acid.

  '
recipe: recipe_silicon_tetrachloride_v0
```


---
## 4. Available Papers


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
## 5. Queue Workflow

[Error reading /Users/allanniemerg/dev2/self-replicating-system-modeling/docs/queue_multi_agent.md: [Errno 2] No such file or directory: '/Users/allanniemerg/dev2/self-replicating-system-modeling/docs/queue_multi_agent.md']

---
## 6. Gap Types and Validation


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

7. **missing_recipe_input** - Items used as recipe inputs but not defined
   - Context includes: `used_as_input_in` (list of recipes), `total_recipe_count`
   - These are raw materials or parts consumed by recipes but never produced
   - Fix: Create a material or part definition. Check if it should be:
     - A material (raw inputs like `copper_sheet_2mm`, `brazing_alloy_copper_phosphorus`)
     - A part (manufactured components like `copper_tube_fitting`)
   - Research similar items first (e.g., `aluminum_sheet_2mm` as pattern for `copper_sheet_2mm`)

8. **missing_intermediate_part** - Items produced and consumed across multiple recipes
   - Context includes: `used_as_input_in`, `used_as_output_in`, `total_recipe_count`
   - These are sub-assemblies or intermediate products shared by multiple recipes
   - Fix: Create a part definition with appropriate `mass` and `material_class`
   - Example: `jacket_panels_formed` (used in 3 recipes as intermediate product)

9. **pure_intermediate** - Items only used within a single recipe
   - Context includes: `used_as_input_in`, `used_as_output_in` (both list same recipe)
   - These are internal recipe steps that don't need separate definitions
   - Fix: Usually can be left undefined (acceptable per design). Only create if:
     - The item represents a meaningful sub-assembly that might be reused later
     - It helps with recipe clarity and debugging
   - Consider: Can the recipe be simplified to eliminate this intermediate?

10. **missing_recipe_target** - Recipe targets an item that doesn't exist
    - Context includes: `used_as_target_in` (list of recipes)
    - The recipe produces this item, but the item itself isn't defined
    - Fix: Create the part/material/machine definition that the recipe produces

11. **recipe_no_inputs** - Recipe has process steps but no inputs/outputs defined
    - Context includes: `recipe_id`, `target_item_id`, `step_count`, `file`
    - These are placeholder/incomplete recipes that define process sequence but not material flow
    - Fix: Add `inputs`, `outputs`, and optionally `byproducts` arrays to each step

    **When NO inputs is acceptable:**
    - ONLY for raw material extraction using `environment_source_v0` process
    - The target item should be in `kb/items/raw_materials/` folder
    - Examples: lunar_regolith_in_situ, water (from polar ice), solar_irradiance
    - If this is raw material extraction, move the item to raw_materials folder instead

    **How to fix incomplete recipes:**
    1. Read the recipe file to understand the process sequence
    2. Check `assumptions` and `notes` fields for material hints
    3. For each step, define:
       - `inputs`: What materials/parts go into this step
         - Each input needs: `item_id`, `qty`, `unit`
       - `outputs`: What this step produces
         - Each output needs: `item_id`, `qty`, `unit`
       - `byproducts`: Optional waste/side products
    4. Ensure material balance: outputs should account for most of input mass
    5. Link steps: Step N outputs should be Step N+1 inputs (for multi-step recipes)

    **Example fix:**
    ```yaml
    # BEFORE (incomplete):
    id: recipe_glass_bulk_v0
    target_item_id: glass_bulk
    steps:
      - process_id: glass_melting_and_forming_v0
        est_time_hr: 2.5
    assumptions: Glass melting/forming from regolith fines

    # AFTER (complete):
    id: recipe_glass_bulk_v0
    target_item_id: glass_bulk
    steps:
      - process_id: glass_melting_and_forming_v0
        est_time_hr: 2.5
        inputs:
          - item_id: regolith_fines
            qty: 10
            unit: kg
          - item_id: thermal_energy
            qty: 50
            unit: MJ
        outputs:
          - item_id: glass_bulk
            qty: 8
            unit: kg
        byproducts:
          - item_id: waste_gas
            qty: 0.5
            unit: kg
    ```

    **Multi-step recipe example:**
    ```yaml
    id: recipe_basalt_fiber_v0
    target_item_id: basalt_fiber
    steps:
      - process_id: glass_melting_and_forming_v0
        inputs:
          - item_id: regolith_basalt
            qty: 10
            unit: kg
        outputs:
          - item_id: glass_bulk
            qty: 8
            unit: kg
      - process_id: basalt_fiber_production_v0
        inputs:
          - item_id: glass_bulk  # Output from step 1
            qty: 8
            unit: kg
        outputs:
          - item_id: basalt_fiber_raw
            qty: 7
            unit: kg
      - process_id: spool_winding_basic_v0
        inputs:
          - item_id: basalt_fiber_raw  # Output from step 2
            qty: 7
            unit: kg
        outputs:
          - item_id: basalt_fiber
            qty: 7
            unit: kg
    ```

    **Common patterns:**
    - First step often needs raw materials (regolith, ore, metal ingots)
    - Intermediate steps transform materials (melting, forming, machining)
    - Final step produces the target item
    - Energy inputs (thermal_energy, electrical_energy) are common
    - Tool/machine wear items may be consumed (cutting_fluid, abrasive_media)

The indexer outputs:
- `out/work_queue.jsonl` - All gaps (rebuilt each run)
- `out/validation_report.md` - Detailed validation results
- `out/unresolved_refs.jsonl` - Unresolved references
- `out/missing_fields.jsonl` - Missing required fields
- `out/missing_recipe_items.jsonl` - Items referenced in recipe steps but not defined
- `out/recipes_no_inputs.jsonl` - Recipes with no inputs/outputs defined


---
## 7. Best Practices


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
