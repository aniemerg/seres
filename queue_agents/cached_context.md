# Cached Context for Autonomous Queue Agent

This context is cached and reused across all agent invocations.

---
## 1. Agent Reference

# Agent Reference — KB Creation Guide

## Core Principles

**Import Policy:** Anything that cannot be replicated locally is treated as imported. Items without recipes become imports with mass penalties.

**Design Philosophy:**
1. **Structure before precision** — Coarse, labeled estimates are acceptable. Capture dependency structure first, refine numbers later.
2. **Processes before machines** — Prefer unit operations (crush, sinter, cast). Machines are capacity providers, not the primary abstraction.
3. **Incompleteness is acceptable** — Use placeholders (null values), surface gaps explicitly. The system must run with partial data.

**Best-Guess Engineering:** When uncertain, make conservative assumptions based on similar items. Label estimates with provenance and confidence.

**When to Give Up (Import):**
- No recipe found after researching similar items
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

## Workflow Tips

1. **Research first** — Use `rg_search` to find similar items before creating new ones
2. **Follow patterns** — Copy structure from similar existing items
3. **Start minimal** — Required fields only, add optional fields later
4. **Be explicit about unknowns** — Use `null` + notes rather than omitting fields
5. **Validate early** — Run indexer after each change to catch errors
6. **Conservative assumptions** — When estimating, err on the side of heavier/slower/more energy
7. **One item at a time** — Don't try to anticipate downstream gaps, let the indexer guide you

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
- resource_type: assembly_station
  qty: 1.0
  unit: unit
- resource_type: labor_bot_general
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
# kb/processes/optical_microscope_assembly_v0.yaml
id: optical_microscope_assembly_v0
kind: process
name: Optical microscope assembly v0
layer_tags:
- layer_7
- layer_8
inputs:
- item_id: glass_lens_objective_set
  qty: 4.0
  unit: each
- item_id: glass_lens_eyepiece
  qty: 2.0
  unit: each
- item_id: prism_glass_optical
  qty: 2.0
  unit: each
- item_id: illumination_lamp_led
  qty: 1.0
  unit: each
- item_id: condenser_lens_assembly
  qty: 1.0
  unit: each
- item_id: mechanical_stage_xy
  qty: 1.0
  unit: each
- item_id: focusing_mechanism_coarse_fine
  qty: 1.0
  unit: each
- item_id: steel_frame_microscope_body
  qty: 8.0
  unit: kg
- item_id: mirror_optical_flat
  qty: 1.0
  unit: each
outputs:
- item_id: optical_microscope_v0
  qty: 1.0
  unit: unit
requires_ids:
- assembly_tools_basic
resource_requirements:
- resource_type: assembly_station
  qty: 1.0
  unit: unit
- resource_type: labor_bot_general
  amount: null
  unit: hr
energy_model:
  type: kWh_per_batch
  value: 6.0
  notes: Placeholder energy for optical microscope assembly
time_model:
  type: fixed_time
  hr_per_batch: 5.0
  notes: Placeholder assembly time for microscope
notes: Assembles an optical microscope from provided optical components and a steel
  frame. Placeholder manufacturing step to enable modeling in the KB.
```

```yaml
# kb/processes/surface_treatment_station_assembly_v0.yaml
id: surface_treatment_station_assembly_v0
kind: process
name: Surface treatment station assembly
inputs:
- item_id: chemical_bath_tank_set
  qty: 1.0
  unit: unit
- item_id: agitation_system_basic
  qty: 1.0
  unit: unit
- item_id: chemical_bath_ventilation
  qty: 1.0
  unit: unit
- item_id: circulation_pump_coolant
  qty: 1.0
  unit: unit
- item_id: control_panel_basic
  qty: 1.0
  unit: unit
- item_id: support_frame_welded
  qty: 1.0
  unit: unit
- item_id: fastener_kit_medium
  qty: 1.0
  unit: unit
outputs:
- item_id: surface_treatment_station
  qty: 1.0
  unit: unit
requires_ids: []
resource_requirements:
- resource_type: labor_bot_general
  qty: 4.0
  unit: hr
energy_model:
  type: kWh_per_batch
  value: 5.0
  notes: Approximate energy for assembling surface_treatment_station
time_model:
  type: fixed_time
  hr_per_batch: 6.0
  notes: Approximate assembly time
notes: Local fabrication path for surface_treatment_station; consumes BOM components
  to produce the machine.
```


### Recipe Examples

```yaml
# kb/recipes/recipe_packed_bed_distillation_v0.yaml
id: recipe_packed_bed_distillation_v0
kind: recipe
name: Recipe for packed bed distillation
produces_id: packed_bed_distillation
produces_qty: 1.0
produces_unit: unit
steps:
- process_id: metal_casting_basic_v0
  notes: Cast base frame components for packed bed distillation
- process_id: welding_brazing_basic_v0
  notes: Weld frame components and support structures
- process_id: machining_finish_basic_v0
  notes: Finish machining for interfaces and mounting holes
- process_id: assembly_basic_v0
  notes: Pre-assembly of subcomponents into the machine shell
- process_id: enclosure_assembly_basic_v0
  notes: Assemble enclosure for electronics and control hardware
- process_id: electrical_wiring_and_controls_v0
  notes: Install wiring, control panels, sensors, and interlocks
- process_id: machine_assembly_basic_v0
  notes: 'Final assembly: frame, enclosure, wiring into packed bed distillation machine'
notes: Prototype recipe to manufacture packed bed distillation; BOM details to be
  refined.
```

```yaml
# kb/recipes/recipe_machine_regolith_brick_press_hydraulic_v0.yaml
id: recipe_machine_regolith_brick_press_hydraulic_v0
kind: recipe
name: Recipe for regolith brick hydraulic press
produces_id: regolith_brick_press_hydraulic_v0
produces_qty: 1.0
produces_unit: unit
target_item_id: regolith_brick_press_hydraulic_v0
variant_id: v0
steps:
- process_id: cutting_basic_v0
  est_time_hr: 2.0
  machine_hours: 2.0
  labor_hours: 1.0
  notes: Cut frame members, platens, and mold plates.
- process_id: welded_fabrication_basic_v0
  est_time_hr: 3.0
  machine_hours: 2.5
  labor_hours: 2.5
  notes: Weld press frame and mold housing.
- process_id: machining_finish_basic_v0
  est_time_hr: 2.0
  machine_hours: 1.5
  labor_hours: 1.5
  notes: Machine platen faces, mold cavity surfaces, mounting holes.
- process_id: hydraulic_system_assembly_v0
  est_time_hr: 1.5
  labor_hours: 1.5
  notes: Install cylinder, hoses, valves, and power unit.
- process_id: hydraulic_system_integration_v0
  est_time_hr: 1.0
  labor_hours: 1.0
  notes: Fill/bleed hydraulics; set relief valves.
- process_id: wiring_and_electronics_integration_v0
  est_time_hr: 0.8
  labor_hours: 0.8
  notes: Wire controls, limit switches, safety interlocks.
- process_id: integration_test_basic_v0
  est_time_hr: 0.8
  labor_hours: 0.6
  notes: Cycle press with mold, verify pressure and ejection.
assumptions: Hydraulic press variant for regolith bricks; uses hydraulic system modules
  present in BOM; includes mold set.
notes: Local build route for regolith brick hydraulic press v0.
```

```yaml
# kb/recipes/recipe_press_hydraulic_v1.yaml
id: recipe_press_hydraulic_v1
kind: recipe
name: Recipe for hydraulic press v1
produces_id: press_hydraulic
produces_qty: 1.0
produces_unit: unit
steps:
- process_id: metal_casting_basic_v0
  notes: Cast frame, columns, and base (approx 600 kg)
- process_id: welding_brazing_basic_v0
  notes: Weld hydraulic cylinder mounting, reinforcement gussets
- process_id: machining_finish_basic_v0
  notes: Machine ram guides, platen surfaces, cylinder mounting bores
- process_id: assembly_basic_v0
  notes: Assemble hydraulic cylinders, rams, platens, pressure gauges
- process_id: hydraulic_system_integration_v0
  notes: Install hydraulic pump, valves, hoses, and pressure controls
- process_id: wiring_and_electronics_integration_v0
  notes: Install electrical controls, safety interlocks, pressure sensors
notes: Alternative production route for hydraulic press; provides explicit path for
  indexer.
```


### Bom Examples


### Machine Examples

```yaml
# kb/items/machines/visual_odometry_system_v0.yaml
id: visual_odometry_system_v0
kind: machine
name: Visual odometry system
mass: 6.0
unit: kg
capabilities:
- odometry
- visual_odometry
- slam
- data_logging
bom: bom_visual_odometry_system_v0_v0.yaml
notes: Camera-based dead reckoning system used to estimate motion/pose from onboard
  camera streams. Placeholder mass; refine with actual hardware data.
```

```yaml
# kb/items/machines/ffc_reactor_enhanced_v0.yaml
id: ffc_reactor_enhanced_v0
kind: machine
name: Enhanced FFC Cambridge reactor
mass: 1200.0
unit: kg
bom: bom_ffc_reactor_enhanced_v0
capabilities:
- molten_salt_electrolysis
- high_temperature_processing
- gas_extraction
notes: "Enhanced fluoride-fluoride conversion (FFC) reactor for molten CaCl2 electrolysis\
  \ at ~900\xB0C. Primary outputs: Ca, Al, Si metals and O2 gas from regolith-derived\
  \ feedstock. Energy split typically ~97% thermal and ~3% electrical; integration\
  \ with solar thermal. Dependencies at installation: molten_salt_containment_v0,\
  \ graphite_anode_assembly_v0, temperature_control_system_v0. Seed context: from\
  \ Ellery/Moon ISRU literature; see seeds/paper reviews for provenance."
```

```yaml
# kb/items/machines/plate_rolling_mill.yaml
id: plate_rolling_mill
kind: machine
name: Plate rolling mill
mass: 1500.0
unit: kg
bom: bom_plate_rolling_mill_v0
capabilities:
- rolling
- metal_forming
- plate_production
material_class: steel
notes: Plate rolling mill for producing metal plate from ingots or billets. Heavy
  rollers compress heated metal through multiple passes to achieve desired thickness.
  Used for producing steel plate, sheet metal stock, and structural materials. Includes
  drive motors, roll adjustment, and heating system.
preferred_variant: simple
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
```

```yaml
# kb/items/parts/rectifier_full_bridge_v0.yaml
id: rectifier_full_bridge_v0
kind: part
name: Full-bridge rectifier module
mass: 0.3
unit: unit
material_class: electronic
notes: "Bridge rectifier module for AC\u2192DC conversion; diode pack with heat sink\
  \ and leads."
```


### Material Examples

```yaml
# kb/items/materials/methane_pyrolysis_carbon_v0.yaml
id: methane_pyrolysis_carbon_v0
name: Methane pyrolysis carbon (carbon black)
kind: material
unit: kg
mass: 1.0
material_class: carbon
notes: "Product of methane pyrolysis: CH4 \u2192 C + 2H2 (carbon black).\nSeed material\
  \ referenced in comprehensive paper reviews. Placeholder entry to\nallow closed-loop\
  \ modeling until a dedicated production process for this carbon is defined.\n"
source_tags:
- seed
- paper_reviews_dec2024_comprehensive_v0
```

```yaml
# kb/items/materials/finished_part_deburred.yaml
id: finished_part_deburred
kind: material
name: Finished part (deburred)
mass: 1.0
unit: kg
material_class: metal
notes: 'Generic placeholder for a part after deburring operations.

  Represents any part that has had sharp edges, burrs, and flash removed.

  Used as output in deburring and finishing processes.

  Actual material properties depend on the input part being deburred.

  '
```

```yaml
# kb/items/materials/raw_metal_block.yaml
id: raw_metal_block
name: Raw metal block
kind: material
mass: 3.0
unit: kg
material_class: metal
notes: Placeholder raw metal block used as input for the robot tool quick-change fabrication
  process.
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

# Multi-Agent Queue Usage

## REQUIRED READING FIRST

**Before working on the queue, you MUST read:**
1. `design/meta-memo.md` — Project overview and goals
2. `design/memo_a.md` — Specification and design principles
3. `design/memo_b.md` — Knowledge acquisition methodology

See `docs/README.md` for full onboarding documentation.

## Queue Operations

- IDs are stable: `id = "<gap_type>:<item_id>"` with `gap_type`, `item_id`, `reason`, `context`, `status`, `lease_id`, `lease_expires_at`.
- Always lease before editing:
  - Lease: `.venv/bin/python -m kbtool queue lease --agent <name> [--ttl 900] [--priority gap1,gap2]`
    - Only one lease per `item_id` is allowed; if another entry with the same `item_id` is leased, the request is denied.
  - Complete: `.venv/bin/python -m kbtool queue complete --id <gap_type:item_id> --agent <name>`
  - Release: `.venv/bin/python -m kbtool queue release --id <gap_type:item_id> --agent <name>`
  - GC expired leases: `.venv/bin/python -m kbtool queue gc [--prune-done-older-than N]`
  - List: `.venv/bin/python -m kbtool queue ls`
- Do not edit items you haven’t leased. If you find another agent’s edits, reconcile rather than overwrite; leave context in `notes`.
- Indexer rebuilds the queue each run, preserving leases/done status; gaps resurface if fixes are incomplete.
- Pruning only removes items marked `resolved`/`superseded`; gaps persist until fixes land.


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

The indexer outputs:
- `out/work_queue.jsonl` - All gaps (rebuilt each run)
- `out/validation_report.md` - Detailed validation results
- `out/unresolved_refs.jsonl` - Unresolved references
- `out/missing_fields.jsonl` - Missing required fields


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
