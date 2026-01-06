# Fix Intelligence: recipe_vacuum_pump_station_v0

## Files

- **Recipe:** `kb/recipes/recipe_vacuum_pump_station_v0.yaml`
- **Target item:** `vacuum_pump_station`
  - File: `kb/items/vacuum_pump_station.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'vacuum_pump_station_assembly_v0') requires input 'vacuum_pump_small' which is not available

**Location:** Step 0
**Process:** `vacuum_pump_station_assembly_v0`
  - File: `kb/processes/vacuum_pump_station_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: vacuum_pump_station_assembly_v0
  inputs:
  - item_id: vacuum_pump_small
    qty: 1.0
    unit: unit
  - item_id: motor_electric_small
    qty: 1.0
    unit: unit
  - item_id: shaft_and_bearing_set
    qty: 1.0
    unit: unit
  - item_id: hydraulic_seals_set
    qty: 1.0
    unit: unit
  - item_id: vacuum_gauge_set
    qty: 1.0
    unit: unit
  - item_id: vacuum_pump_system_miniature
    qty: 1.0
    unit: unit
  - item_id: pump_housing_machined
    qty: 1.0
    unit: unit
  - item_id: control_circuit_board_basic
    qty: 1.0
    unit: unit
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `vacuum_pump_small` not found

This item doesn't exist in the KB.

#### Problem: Item `motor_electric_small` not found

This item doesn't exist in the KB.

#### Problem: Item `shaft_and_bearing_set` not found

This item doesn't exist in the KB.

#### Problem: Item `hydraulic_seals_set` not found

This item doesn't exist in the KB.

#### Problem: Item `vacuum_gauge_set` not found

This item doesn't exist in the KB.

#### Problem: Item `vacuum_pump_system_miniature` not found

This item doesn't exist in the KB.

#### Problem: Item `pump_housing_machined` not found

This item doesn't exist in the KB.

#### Problem: Item `control_circuit_board_basic` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_vacuum_pump_station_v0.yaml`
- **BOM available:** No
