# Fix Intelligence: recipe_brazing_torch_oxy_fuel_v0

## Files

- **Recipe:** `kb/recipes/recipe_brazing_torch_oxy_fuel_v0.yaml`
- **Target item:** `brazing_torch_oxy_fuel`
  - File: `kb/items/brazing_torch_oxy_fuel.yaml`
- **BOM:** None
- **Steps:** 2 total

## Errors (2 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'machining_process_drilling_v0') requires input 'copper_rod_ingot' which is not available

**Location:** Step 0
**Process:** `machining_process_drilling_v0`
  - File: `kb/processes/machining_process_drilling_v0.yaml`

**Current step:**
```yaml
- process_id: machining_process_drilling_v0
  inputs:
  - item_id: copper_rod_ingot
    qty: 0.2
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `copper_rod_ingot` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'assembly_process_general_v0') requires input 'torch_body_and_valves_machined' which is not available

**Location:** Step 1
**Process:** `assembly_process_general_v0`
  - File: `kb/processes/assembly_process_general_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_process_general_v0
  inputs:
  - item_id: torch_body_and_valves_machined
    qty: 0.45
    unit: kg
  - item_id: copper_rod_ingot
    qty: 0.18
    unit: kg
  - item_id: hydraulic_hose_segment_v0
    qty: 1.0
    unit: kg
  - item_id: valve_needle_precision
    qty: 2.0
    unit: each
  - item_id: valve_set_gas_handling
    qty: 2.0
    unit: each
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `torch_body_and_valves_machined` not found

This item doesn't exist in the KB.

#### Problem: Item `copper_rod_ingot` not found

This item doesn't exist in the KB.

#### Problem: Item `hydraulic_hose_segment_v0` not found

This item doesn't exist in the KB.

#### Problem: Item `valve_needle_precision` not found

This item doesn't exist in the KB.

#### Problem: Item `valve_set_gas_handling` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_brazing_torch_oxy_fuel_v0.yaml`
- **BOM available:** No
