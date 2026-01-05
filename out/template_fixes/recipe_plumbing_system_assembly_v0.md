# Fix Intelligence: recipe_plumbing_system_assembly_v0

## Files

- **Recipe:** `kb/recipes/recipe_plumbing_system_assembly_v0.yaml`
- **Target item:** `plumbing_system_assembly`
  - File: `kb/items/plumbing_system_assembly.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'assembly_process_general_v0') requires input 'piping_and_valves_set' which is not available

**Location:** Step 0
**Process:** `assembly_process_general_v0`
  - File: `kb/processes/assembly_process_general_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_process_general_v0
  inputs:
  - item_id: piping_and_valves_set
    qty: 1.0
    unit: set
  - item_id: fastener_kit_medium
    qty: 0.2
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `piping_and_valves_set` not found

This item doesn't exist in the KB.

#### Problem: Item `fastener_kit_medium` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_plumbing_system_assembly_v0.yaml`
- **BOM available:** No
