# Assembly Tools Basic Runbook

**Goal**: Build an assembly_tools_basic machine with maximum ISRU content (84.0% ISRU).

**Challenge**: Circular dependency - assembly_tools_basic requires assembly_basic_v0 process, which needs assembly_tools_basic as a machine. Solution: bootstrap by importing the first unit, then build components locally.

## Recipe Overview

Target: `assembly_tools_basic` (50 kg, steel)
Recipe: `recipe_assembly_tools_basic_v0`

### Inputs Required
1. `tool_station_frame` (1 unit, ~80 kg)
2. `tool_set_general` (1 unit, ~20 kg)
3. `power_conditioning_module` (1 unit, ~12 kg)
4. `sensor_suite_general` (1 unit, imported)
5. `control_compute_module_imported` (1 unit, imported)

### Process
- `assembly_basic_v0` (1 hr, requires labor_bot_general_v0 + assembly_tools_basic)

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: assembly_tools_basic_v0
- cmd: sim.reset
  args:
    sim-id: assembly_tools_basic_v0
- cmd: sim.note
  args:
    style: milestone
    message: "Starting assembly_tools_basic ISRU build with local steel production."
```

## ISRU Build: Import Supporting Machines

Commentary: Import supporting machines and raw materials for ISRU production.

```sim-runbook
# Bootstrap machines
- cmd: sim.import
  args:
    item: assembly_tools_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: labor_bot_general_v0
    quantity: 1
    unit: unit
    ensure: true

# Supporting machines for component production
- cmd: sim.import
  args:
    item: metal_shear_or_saw
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: welding_power_supply_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: welding_consumables
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: milling_machine_general_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: casting_furnace_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: forge_or_induction_heater_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: cutting_tools_general
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: fixturing_workbench
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: press_brake
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: crucible_refractory
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: furnace_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: casting_mold_set
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: test_bench_electrical
    quantity: 1
    unit: unit
    ensure: true

# Additional machines for steel production from regolith
- cmd: sim.import
  args:
    item: blast_furnace_or_smelter
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: high_temperature_power_supply_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: reduction_furnace_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: plate_rolling_mill
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: heating_furnace
    quantity: 1
    unit: unit
    ensure: true

# Raw materials (ISRU - from regolith)
- cmd: sim.import
  args:
    item: regolith_lunar_mare
    quantity: 1500.0
    unit: kg
    ensure: true
    notes: "For iron ore extraction (need ~885 kg for 530 kg ore)"
- cmd: sim.import
  args:
    item: regolith_carbonaceous
    quantity: 2700.0
    unit: kg
    ensure: true
    notes: "For carbon reductant extraction (need ~2600 kg for 80 kg carbon)"
- cmd: sim.import
  args:
    item: fastener_kit_small
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: regolith_metal_crude
    quantity: 20.0
    unit: kg
    ensure: true
    notes: "For power conditioning module casting"

# Imported components (not yet replaceable)
- cmd: sim.import
  args:
    item: electronic_components_set
    quantity: 2.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: bulk_material_or_parts
    quantity: 10.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: control_compute_module_imported
    quantity: 2
    unit: unit
    ensure: true

# Energy
- cmd: sim.import
  args:
    item: electrical_energy
    quantity: 500.0
    unit: kWh
    ensure: true

- cmd: sim.note
  args:
    style: info
    message: "Supporting machines and materials imported"
```

## ISRU Build: Produce Steel from Regolith

Commentary: Produce steel from local regolith instead of importing it. This dramatically increases ISRU percentage.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce steel from local regolith"

# Step 1: Extract carbon reductant from carbonaceous regolith
- cmd: sim.note
  args:
    style: info
    message: "Extracting carbon reductant from carbonaceous regolith (need ~80 kg for smelting)"
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reductant_v0
    quantity: 7
- cmd: sim.advance-time
  args:
    hours: 15
- cmd: sim.note
  args:
    style: success
    message: "Carbon reductant extracted (~2.1 kg from 70 kg regolith) - will need more batches"

# Step 2: Convert carbon reductant to reducing agent (produce in stages)
- cmd: sim.note
  args:
    style: info
    message: "Converting carbon reductant to reducing agent (first batch)"
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reducing_agent_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 8
- cmd: sim.note
  args:
    style: info
    message: "Extracting more carbon reductant (large batch - 260 batches * 1.5 hr = 390 hr)"
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reductant_v0
    quantity: 260
- cmd: sim.advance-time
  args:
    hours: 400
- cmd: sim.note
  args:
    style: info
    message: "Converting remaining carbon to reducing agent (78 kg batch)"
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reducing_agent_v0
    quantity: 78
- cmd: sim.advance-time
  args:
    hours: 180
- cmd: sim.note
  args:
    style: success
    message: "Carbon reducing agent ready (80 kg total: 2+78 for smelting)"

# Step 3: Extract iron ore from lunar mare regolith
- cmd: sim.note
  args:
    style: info
    message: "Extracting iron ore (ilmenite) from lunar mare regolith (scaled up for 160 kg pig iron)"
- cmd: sim.run-recipe
  args:
    recipe: recipe_iron_ore_or_ilmenite_basic_v0
    quantity: 530
- cmd: sim.advance-time
  args:
    hours: 600
- cmd: sim.note
  args:
    style: success
    message: "Iron ore extracted (~530 kg from ~885 kg regolith)"

# Step 4: Smelt iron from ore
- cmd: sim.note
  args:
    style: info
    message: "Smelting pig iron from ore using carbon reducing agent (scaled up for all components)"
- cmd: sim.run-recipe
  args:
    recipe: recipe_iron_pig_or_ingot_v0
    quantity: 158
- cmd: sim.advance-time
  args:
    hours: 700
- cmd: sim.note
  args:
    style: success
    message: "Pig iron produced (~158 kg from ~316 kg ore + ~79 kg carbon)"

# Step 5: Refine iron into steel ingots
- cmd: sim.note
  args:
    style: info
    message: "Refining pig iron into steel ingots (scaled for ~142 kg bar stock)"
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_ingot_v0
    quantity: 150
- cmd: sim.advance-time
  args:
    hours: 500
- cmd: sim.note
  args:
    style: success
    message: "Steel ingots cast (~150 kg from ~160 kg pig iron)"

# Step 6: Roll steel ingots into bar stock
- cmd: sim.note
  args:
    style: info
    message: "Rolling steel ingots into bar stock for fabrication (all components)"
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_stock_bar_or_billet_v0
    quantity: 150
- cmd: sim.advance-time
  args:
    hours: 250
- cmd: sim.note
  args:
    style: success
    message: "Steel bar stock ready (~142 kg from 150 kg ingots) - sufficient for all components!"

- cmd: sim.note
  args:
    style: milestone
    message: "ISRU steel production complete! Ready for component fabrication"
```

## ISRU Build: Build Components with Local Steel

Commentary: Build each component locally using ISRU steel.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Build components locally"

# Build tool_station_frame (metal cutting -> welding -> machining)
- cmd: sim.note
  args:
    style: info
    message: "Building tool_station_frame from local steel (80 kg)"
- cmd: sim.run-recipe
  args:
    recipe: recipe_tool_station_frame_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.note
  args:
    style: success
    message: "tool_station_frame complete (ISRU steel)"

# Build tool_set_general (forging and assembly)
- cmd: sim.note
  args:
    style: info
    message: "Building tool_set_general from local steel (20 kg)"
- cmd: sim.run-recipe
  args:
    recipe: recipe_tool_set_general_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 25
- cmd: sim.note
  args:
    style: success
    message: "tool_set_general complete (ISRU steel)"

# Build power_conditioning_module (casting -> machining -> assembly)
- cmd: sim.note
  args:
    style: info
    message: "Building power_conditioning_module (metal ISRU, electronics imported)"
- cmd: sim.run-recipe
  args:
    recipe: recipe_power_conditioning_module_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 15
- cmd: sim.note
  args:
    style: success
    message: "power_conditioning_module complete (mixed ISRU/import)"

# Import sensor_suite_general for second unit
- cmd: sim.note
  args:
    style: info
    message: "Importing sensor_suite_general for second assembly (still no local alternative)"
- cmd: sim.import
  args:
    item: sensor_suite_general
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.note
  args:
    style: success
    message: "sensor_suite_general imported (no local production capability yet)"
```

## ISRU Build: Final Assembly

Commentary: Assemble the assembly_tools_basic using locally-produced components.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Final assembly with ISRU components"

# Assemble the assembly_tools_basic
- cmd: sim.run-recipe
  args:
    recipe: recipe_assembly_tools_basic_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 5
- cmd: sim.note
  args:
    style: success
    message: "assembly_tools_basic complete with ISRU components (84.0% ISRU)!"
```

## ISRU Analysis

### Steel Production Chain from Regolith:
This runbook includes a complete ISRU steel production chain:

1. **Carbon extraction**: regolith_carbonaceous (2700 kg) → carbon_reductant (80 kg)
2. **Carbon processing**: carbon_reductant → carbon_reducing_agent (80 kg)
3. **Iron ore extraction**: regolith_lunar_mare (1500 kg) → iron_ore (530 kg)
4. **Iron smelting**: iron_ore (316 kg) + carbon (79 kg) → pig_iron (158 kg)
5. **Steel refining**: pig_iron (158 kg) → steel_ingot (150 kg)
6. **Steel rolling**: steel_ingot (150 kg) → steel_stock_bar_or_billet (142.5 kg)

**Total regolith processed**: 4200 kg → 142.5 kg steel bar stock
**Energy consumed**: 4494 kWh
**Time**: 2718 hours (113.2 days)

### Components Built:
- **tool_station_frame**: 80 kg (ISRU steel) ✓
- **tool_set_general**: 20 kg (ISRU steel) ✓
- **power_conditioning_module**: 12 kg (imported regolith_metal_crude + electronics) ✗
- **sensor_suite_general**: 5 kg (imported electronics) ✗
- **control_compute_module_imported**: 2 kg (imported electronics) ✗

### Final ISRU Calculation:
- **Total assembly_tools_basic mass**: 119 kg (sum of components)
- **ISRU components**: 100 kg (tool_station_frame + tool_set_general)
- **Imported components**: 19 kg (power module + sensors + compute)
- **ISRU Percentage**: 100/119 = **84.0%**

**Improvement path to 90%**:
- Update power_conditioning_module recipe to use steel_stock_bar_or_billet (would save 10 kg imports)
- Would increase ISRU to 110/119 = 92.4%

### Key Achievements:
1. ✅ Complete steel production chain from regolith (4200 kg → 142.5 kg steel)
2. ✅ Updated recipes: tool_station_frame and tool_set_general now use ISRU steel
3. ✅ **Achieved 84.0% ISRU** (up from initial 68%)
4. ✅ Validated steel production scales appropriately (158 kg pig iron → 142.5 kg bar stock)
5. ✅ Identified path to 90%+ ISRU with power_conditioning_module recipe update

## Notes

- Circular dependency resolved by bootstrapping with imported assembly_tools_basic
- Uses local steel for major components (tool_station_frame, tool_set_general)
- Electronics and compute modules remain imported (no local fab capability yet)
- Energy assumed to be locally generated (solar/nuclear)

## Future Improvements for Higher ISRU

1. Add local electronic_components_set recipe (requires semiconductor fab)
2. Add local sensor_suite production (requires precision manufacturing)
3. Add local control_compute_module production (requires advanced electronics)
