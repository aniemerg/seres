# Fix Intelligence: recipe_valve_solenoid_v0

## Files

- **Recipe:** `kb/recipes/recipe_valve_solenoid_v0.yaml`
- **Target item:** `valve_solenoid`
  - File: `kb/items/valve_solenoid.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'assembly_basic_v0') requires input 'valve_body_machined' which is not available

**Location:** Step 0
**Process:** `assembly_basic_v0`
  - File: `kb/processes/assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: valve_body_machined
    qty: 0.4
    unit: kg
  - item_id: solenoid_coil_assembly
    qty: 1.0
    unit: unit
  - item_id: spring_compression_small
    qty: 1.0
    unit: unit
  - item_id: seal_set_high_temp
    qty: 1.0
    unit: unit
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `valve_body_machined` not found

This item doesn't exist in the KB.

#### Problem: Item `solenoid_coil_assembly` not found

This item doesn't exist in the KB.

#### Problem: Item `spring_compression_small` not found

This item doesn't exist in the KB.

#### Problem: Item `seal_set_high_temp` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_valve_solenoid_v0.yaml`
- **BOM available:** No
