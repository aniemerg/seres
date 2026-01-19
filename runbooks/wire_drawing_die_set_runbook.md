# Wire Drawing Die Set Runbook

Goal: build `wire_drawing_die_set` using ISRU feedstocks where available.

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: wire_drawing_die_set_runbook
- cmd: sim.reset
  args:
    sim-id: wire_drawing_die_set_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting wire drawing die set runbook."
```

## ISRU equipment imports

Commentary: import equipment and utilities needed for the ISRU path.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Import equipment for ISRU wire_drawing_die_set build."
- cmd: sim.import
  args:
    item: labor_bot_general_v0
    quantity: 2
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
    item: cutting_tools_general
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: heat_treatment_furnace
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: surface_grinder
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: grinding_wheels
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
- cmd: sim.import
  args:
    item: saw_or_cutting_tool
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: hand_tools_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: hand_tools_mechanical
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: deburring_tools
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: hydraulic_press
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: surface_treatment_station
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: blast_furnace_or_smelter
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
    item: reduction_furnace_v0
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
    item: casting_furnace_v0
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
    item: furnace_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: electrical_energy
    quantity: 250
    unit: kWh
    ensure: true
```
## ISRU: tool steel from regolith

Commentary: replace imported tool steel with an ISRU chain using regolith-derived
ilmenite/iron and carbonaceous regolith carbon.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU: produce tool_steel_high_carbon_v0 from regolith."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_lunar_mare_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_iron_ore_or_ilmenite_basic_v0
    quantity: 7
- cmd: sim.advance-time
  args:
    hours: 7
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_carbonaceous_collection_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 7
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reductant_v0
    quantity: 4
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reducing_agent_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_tool_steel_high_carbon_v0
    quantity: 2.1
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.note
  args:
    style: info
    message: "ISRU tool steel ready."
```

## ISRU: steel stock, plates, and cut parts

Commentary: produce steel ingots for plate/sheet stock, then cut and machine parts
for downstream finishing.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU: produce steel ingots, plates, and cut parts."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_lunar_mare_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_iron_ore_or_ilmenite_basic_v0
    quantity: 50
- cmd: sim.advance-time
  args:
    hours: 50
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_carbonaceous_collection_v0
    quantity: 6
- cmd: sim.advance-time
  args:
    hours: 40
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reductant_v0
    quantity: 28
- cmd: sim.advance-time
  args:
    hours: 42
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reducing_agent_v0
    quantity: 8
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.run-recipe
  args:
    recipe: recipe_iron_pig_or_ingot_v0
    quantity: 15
- cmd: sim.advance-time
  args:
    hours: 60
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_ingot_v0
    quantity: 14
- cmd: sim.advance-time
  args:
    hours: 42
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_plate_or_sheet_v0
    quantity: 10
- cmd: sim.advance-time
  args:
    hours: 8
- cmd: sim.run-recipe
  args:
    recipe: recipe_cut_parts_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_machined_part_raw_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 4
- cmd: sim.note
  args:
    style: info
    message: "ISRU steel stock and machined parts ready."
```

## ISRU: finished and surface-treated parts

Commentary: convert machined parts into deburred parts and surface-treated parts
from locally produced steel plate stock.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU: produce finished_part_deburred and metal_part_surface_treated."
- cmd: sim.run-recipe
  args:
    recipe: recipe_finished_part_deburred_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_plate_raw_v0
    quantity: 3
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.run-recipe
  args:
    recipe: recipe_metal_part_surface_treated_v0
    quantity: 2.1
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.note
  args:
    style: info
    message: "ISRU finished and surface-treated parts ready."
```

## ISRU build (expanded)

Commentary: rebuild using local tool steel, finished parts, and surface-treated parts.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU: rebuild wire_drawing_die_set with local feedstocks."
- cmd: sim.run-recipe
  args:
    recipe: recipe_wire_drawing_die_set_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.note
  args:
    style: success
    message: "ISRU (expanded) wire_drawing_die_set build complete."
```

## Next ISRU targets

- Localize the imported machines via their runbooks (surface grinder, plate rolling,
  heat treatment, and surface treatment equipment).
- Replace imported electrical energy with local generation if a power runbook is available.
