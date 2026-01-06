# Fix Intelligence: recipe_relay_coil_assembly_v0

## Files

- **Recipe:** `kb/recipes/recipe_relay_coil_assembly_v0.yaml`
- **Target item:** `relay_coil_assembly`
  - File: `kb/items/relay_coil_assembly.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'wire_winding_process_v0') requires input 'copper_wire_magnet' which is not available

**Location:** Step 0
**Process:** `wire_winding_process_v0`
  - File: `kb/processes/wire_winding_process_v0.yaml`

**Current step:**
```yaml
- process_id: wire_winding_process_v0
  inputs:
  - item_id: copper_wire_magnet
    qty: 0.04
    unit: kg
  - item_id: iron_core_laminated
    qty: 0.01
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `copper_wire_magnet` not found

This item doesn't exist in the KB.

#### Problem: Item `iron_core_laminated` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_relay_coil_assembly_v0.yaml`
- **BOM available:** No
