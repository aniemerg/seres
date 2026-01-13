# Test Steel Ingot Recipe

Test a known multi-step recipe.

```sim-runbook
- cmd: sim.use
  args:
    sim-id: test_steel
- cmd: sim.reset
  args:
    sim-id: test_steel
- cmd: sim.import
  args:
    item: iron_pig_or_ingot
    quantity: 30
    unit: kg
- cmd: sim.import
  args:
    item: crucible_refractory
    quantity: 1
    unit: unit
- cmd: sim.import
  args:
    item: casting_furnace_v0
    quantity: 1
    unit: unit
- cmd: sim.import
  args:
    item: casting_mold_set
    quantity: 1
    unit: unit
- cmd: sim.import
  args:
    item: labor_bot_general_v0
    quantity: 2
    unit: unit
- cmd: sim.import
  args:
    item: electrical_energy
    quantity: 100
    unit: kWh
- cmd: sim.note
  args:
    style: milestone
    message: "Testing steel ingot recipe"
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_ingot_v0
    quantity: 25
- cmd: sim.advance-time
  args:
    hours: 50
- cmd: sim.status
  args: {}
```
