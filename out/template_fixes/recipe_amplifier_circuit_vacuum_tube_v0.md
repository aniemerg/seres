# Fix Intelligence: recipe_amplifier_circuit_vacuum_tube_v0

## Files

- **Recipe:** `kb/recipes/recipe_amplifier_circuit_vacuum_tube_v0.yaml`
- **Target item:** `amplifier_circuit_vacuum_tube_v0`
  - File: `kb/items/amplifier_circuit_vacuum_tube_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'assembly_basic_v0') requires input 'vacuum_tube_triode_v0' which is not available

**Location:** Step 0
**Process:** `assembly_basic_v0`
  - File: `kb/processes/assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: vacuum_tube_triode_v0
    qty: 1.0
    unit: unit
  - item_id: electronic_components_set
    qty: 0.05
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `vacuum_tube_triode_v0` not found

This item doesn't exist in the KB.

#### Problem: Item `electronic_components_set` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_amplifier_circuit_vacuum_tube_v0.yaml`
- **BOM available:** No
