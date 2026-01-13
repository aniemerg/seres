# Test Nickel Extraction

Test the nickel extraction recipe in isolation.

```sim-runbook
- cmd: sim.use
  args:
    sim-id: test_nickel
- cmd: sim.reset
  args:
    sim-id: test_nickel
- cmd: sim.import
  args:
    item: regolith_lunar_mare
    quantity: 4000
    unit: kg
- cmd: sim.import
  args:
    item: magnetic_separator_drum_v0
    quantity: 1
    unit: unit
- cmd: sim.import
  args:
    item: vibratory_feeder_v0
    quantity: 1
    unit: unit
- cmd: sim.import
  args:
    item: furnace_high_temp
    quantity: 1
    unit: unit
- cmd: sim.import
  args:
    item: crucible_graphite
    quantity: 1
    unit: unit
- cmd: sim.import
  args:
    item: chemical_separation_equipment
    quantity: 1
    unit: unit
- cmd: sim.import
  args:
    item: labor_bot_general_v0
    quantity: 3
    unit: unit
- cmd: sim.import
  args:
    item: electrical_energy
    quantity: 500
    unit: kWh
- cmd: sim.note
  args:
    style: milestone
    message: "Starting nickel extraction test"
- cmd: sim.run-recipe
  args:
    recipe: recipe_nickel_metal_from_regolith_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 1005
- cmd: sim.status
  args: {}
```
