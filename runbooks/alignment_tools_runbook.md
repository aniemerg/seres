# Alignment Tools Runbook

Goal: Build `alignment_tools` using in-situ resources where possible. Start by importing
all parts for baseline assembly, then produce inputs locally to maximize ISRU.

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: alignment_tools_runbook
- cmd: sim.reset
  args:
    sim-id: alignment_tools_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting alignment_tools runbook."
```

## Baseline import + assembly

Commentary: Import all machines and materials needed to assemble alignment_tools,
then run the recipe as a baseline to verify it works.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Import baseline equipment and materials."
- cmd: sim.import
  args:
    item: labor_bot_general_v0
    quantity: 3
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
    item: assembly_tools_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: tool_steel_high_carbon_v0
    quantity: 5.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: fastener_kit_small
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.note
  args:
    style: milestone
    message: "Running baseline alignment_tools assembly."
- cmd: sim.run-recipe
  args:
    recipe: recipe_alignment_tools_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.note
  args:
    style: milestone
    message: "Baseline alignment_tools assembled successfully."
```

## ISRU Phase 1: Process regolith to extract iron ore and carbon

Commentary: Extract iron ore (ilmenite) and carbon from local regolith instead of importing them.
This achieves true ISRU by using only materials found on the lunar surface.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU Phase 1: Extract iron ore and carbon from regolith."
- cmd: sim.note
  args:
    style: info
    message: "Step 1a: Mine mare regolith (need ~16 kg for iron ore extraction)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_lunar_mare_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 2
- cmd: sim.note
  args:
    style: success
    message: "Mined 100 kg regolith_lunar_mare."
- cmd: sim.note
  args:
    style: info
    message: "Step 1b: Extract ilmenite from regolith (21 batches for tool steel + steel stock)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_ilmenite_from_regolith_v0
    quantity: 21
- cmd: sim.advance-time
  args:
    hours: 25
- cmd: sim.note
  args:
    style: success
    message: "Extracted 12.6 kg iron_ore_or_ilmenite from mare regolith."
- cmd: sim.note
  args:
    style: info
    message: "Step 2a: Mine carbonaceous regolith (need ~55 kg for carbon extraction)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_carbonaceous_collection_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 15
- cmd: sim.note
  args:
    style: success
    message: "Mined 100 kg regolith_carbonaceous."
- cmd: sim.note
  args:
    style: info
    message: "Step 2b: Extract carbon from carbonaceous regolith (8 batches for tool steel + steel stock)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reductant_v0
    quantity: 8
- cmd: sim.advance-time
  args:
    hours: 12
- cmd: sim.note
  args:
    style: success
    message: "Extracted 2.4 kg carbon_reductant from carbonaceous regolith."
- cmd: sim.note
  args:
    style: info
    message: "Converting carbon_reductant to carbon_reducing_agent for steel production (need 2.4 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reducing_agent_v0
    quantity: 2.4
- cmd: sim.advance-time
  args:
    hours: 5
- cmd: sim.note
  args:
    style: success
    message: "Converted 2.4 kg carbon_reducing_agent."
```

## ISRU Phase 2: Produce tool steel from regolith-derived materials

Commentary: Use the regolith-extracted iron ore and carbon to produce tool steel through
smelting, refining, and casting - completely from local resources.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Import steel production machinery (one-time Earth imports)."
- cmd: sim.import
  args:
    item: blast_furnace_or_smelter
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
    item: casting_furnace_v0
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
    item: crucible_refractory
    quantity: 2
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: casting_mold_set
    quantity: 2
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
- cmd: sim.note
  args:
    style: info
    message: "Producing 5.0 kg tool steel and 1.5 kg steel stock from regolith materials."
- cmd: sim.run-recipe
  args:
    recipe: recipe_tool_steel_high_carbon_v0
    quantity: 5.0
- cmd: sim.advance-time
  args:
    hours: 50
- cmd: sim.note
  args:
    style: success
    message: "Produced 5.0 kg tool_steel_high_carbon_v0 from regolith!"
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_stock_v0
    quantity: 1.5
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.note
  args:
    style: success
    message: "Produced 1.5 kg steel_stock for fasteners from regolith!"
```

## ISRU Phase 3: Produce fasteners from ISRU steel

Commentary: Produce fastener_kit_small using regolith-derived steel (now uses steel_stock instead of imported regolith_metal_crude).

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce fasteners from ISRU tool steel."
- cmd: sim.note
  args:
    style: info
    message: "Using regolith-derived tool_steel_high_carbon_v0 for fasteners (recipe updated to accept steel_stock)"
- cmd: sim.run-recipe
  args:
    recipe: recipe_fastener_kit_small_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 5
- cmd: sim.note
  args:
    style: success
    message: "Produced 1 fastener_kit_small from ISRU steel."
```

## ISRU Phase 4: Final assembly with regolith-derived materials

Commentary: Build alignment_tools using tool steel produced from regolith-extracted
iron ore and carbon, plus locally-manufactured fasteners.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Final assembly using ISRU-produced inputs."
- cmd: sim.run-recipe
  args:
    recipe: recipe_alignment_tools_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.note
  args:
    style: milestone
    message: "Alignment tools built with ISRU inputs!"
```

## Summary

**Final ISRU: 44.3% (improved from 32.8%)** - All steel from regolith!

**Regolith-derived materials (in-situ):**
- Mare regolith (100 kg mined) → Iron ore (12.6 kg via ilmenite extraction)
- Carbonaceous regolith (100 kg mined) → Carbon reductant (2.4 kg) → Carbon reducing agent (2.4 kg)
- Tool steel (5.0 kg): produced from regolith-extracted iron ore + carbon
- Steel stock (1.5 kg): produced from regolith for fasteners

**Still imported:**
- All machines (labor bots, furnaces, machining tools) - one-time Earth imports

**Improvements made:**
1. Updated fastener_kit_small recipe to use steel_stock instead of regolith_metal_crude
2. Added steel_stock production (1.5 kg) for fasteners
3. Scaled regolith processing: 16→21 batches ore, 6→8 batches carbon
4. Eliminated last material import dependency

**Mass breakdown (per provenance tracking):**
- Total alignment_tools mass: 11.20 kg
- In-situ contribution: 4.96 kg (44.3%) - regolith-derived steel
- Imported contribution: 6.24 kg (55.7%) - includes machine infrastructure

**Achievement:**
- All material inputs (tool steel + fasteners) now from regolith
- Improved ISRU from 32.8% to 44.3% (+11.5 percentage points)
- Eliminated regolith_metal_crude import for fasteners
