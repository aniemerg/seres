---
id: supply_chain_patterns
title: Supply Chain Patterns — From Regolith to Machines
type: article
---

This page documents the manufacturing chain patterns that have been validated end-to-end in simulation runs. These are chains where every step has a confirmed recipe in the KB, inputs and outputs connect correctly, and the process actually executed successfully.

Understanding these chains helps interpret the timeline — the recurring sequences of processes you see in almost every simulation reflect these fundamental production pathways.

## The Core Regolith-to-Metal Chain

The most foundational supply chain in the model extracts metal from raw surface material and converts it into usable parts. This chain appears repeatedly across simulations because nearly every machine assembly requires structural metal components.

```
regolith_lunar_mare  (mining: ~8 h per 100 kg)
  → ilmenite_extraction_from_regolith_v0  (1 h/kg input, ~60% yield)
iron_ore_or_ilmenite
  → iron_pure_production_from_ilmenite_v0  (1 h/kg)
iron_metal_pure
  → iron_powder_from_pure_iron_v0  (0.5 h/kg)
iron_powder_or_sheet
  → base_metal_parts_from_raw_metal_v0  (0.5 h per 3 kg input)
base_metal_parts
```

**What this chain represents:** Starting from regolith — the loose surface material found on the Moon or Mars — iron oxide minerals are extracted, reduced to pure iron, processed into workable stock, and fabricated into generic structural parts. This is the ISRU backbone: local rock becoming manufactured components.

**Key constraints:** Each step requires exact item ID matching (see [[material_classes]]). The chain breaks if a process outputs `iron_metal_pure` but the next step expects `iron_pure` — names must match exactly until class-based substitution is enabled.

## Motor Manufacturing

A validated chain for producing a general-purpose drive motor, tested in the `motor_build_v2` simulation (~8 hours total):

```
Imports: electrical_steel_sheet, aluminum_wire, bearing_set_heavy, coil_insulation_material
  → recipe_stator_rotor_lamination_set_v0  →  stator_rotor_lamination_set
  → recipe_motor_coil_wound_v0            →  motor_coil_wound
  → recipe_motor_housing_steel_v0         →  motor_housing_steel
  → recipe_motor_shaft_steel_v0           →  motor_shaft_steel
  → recipe_drive_motor_medium_v1          →  drive_motor_medium
```

**What this chain represents:** Assembly of a medium-duty electric motor from subcomponents. Most structural parts are locally producible; the electrical components (windings, insulation) currently remain imports in most simulation configurations.

## Labor Bot Components

Key subcomponents of `[[labor_bot_general_v0]]` that have been successfully manufactured in simulation:

- `robot_arm_link_aluminum` via `recipe_robot_arm_link_aluminum_v0` (1 h, 10 kg aluminum input)
- `robot_wrist_3axis` via `recipe_robot_wrist_3axis_v0`
- `thermal_management_system` via `recipe_thermal_management_system_v0`
- `protective_cover_set` via `recipe_protective_cover_set_v0`
- `electric_parallel_gripper` via `recipe_electric_parallel_gripper_v0`

These chains are significant because the labor bot is itself the primary labor resource. Manufacturing its components is a prerequisite for any scenario that aims to reproduce the labor bot locally.

## Most Commonly Imported Items

Across simulations, these items most frequently remain as imports — meaning local production chains do not yet exist or are not triggered in typical runs:

1. `[[labor_bot_general_v0]]` — the standard starting labor machine
2. `fastener_kit_medium` — used in roughly half of all assembly recipes
3. `coil_insulation_material` — motor manufacturing
4. `aluminum_wire` — motor coils
5. `aluminum_alloy_ingot` — generic metal stock
6. `electrical_steel_sheet` — motor cores
7. `bearing_set_heavy` — mechanical assemblies throughout

These recurring imports represent the current frontier of KB development — the items where adding local production chains would most improve closure.

## Machine Utilization in This Run

The table below shows which machines are running the most in the current simulation. High utilization indicates bottleneck machines — candidates for capacity expansion or for understanding where time is concentrated.

```sim-query
type: table
source: sim.machines.utilization
title: Machine Utilization (Ranked by Utilization)
columns: [id, name, run_count, busy_hours, utilization_percent, total_energy_kwh]
```

## Reading the Timeline

When viewing the simulation timeline:

- **Clusters of mining and extraction processes** early in a run reflect the regolith chain starting up.
- **Long sequential chains** with the same machine type are typically motor or structural component production.
- **Labor bot processes** appear distributed throughout — assembly steps are interspersed with fabrication steps.
- **Short isolated processes** may be final assembly steps or single-run recipes for specific machine outputs.

See [[simulation_overview]] for the full scenario context and [[self_reproduction]] for how these chains contribute to coverage.

## Related Articles

- [[material_classes]] — Why exact item ID matching matters in these chains
- [[parts_and_labor]] — How labor bot hours are accounted for
- [[self_reproduction]] — How chain completeness affects coverage metrics
- [[kb_philosophy]] — What broken chains indicate and how gaps are handled
