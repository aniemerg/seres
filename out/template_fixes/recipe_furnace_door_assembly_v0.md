# Fix Intelligence: recipe_furnace_door_assembly_v0

## Files

- **Recipe:** `kb/recipes/recipe_furnace_door_assembly_v0.yaml`
- **Target item:** `furnace_door_assembly`
  - File: `kb/items/furnace_door_assembly.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'assembly_basic_v0') requires input 'raw_metal_block' which is not available

**Location:** Step 0
**Process:** `assembly_basic_v0`
  - File: `kb/processes/assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: raw_metal_block
    qty: 35.0
    unit: kg
  - item_id: door_hinge_assembly
    qty: 2.0
    unit: unit
  - item_id: sealing_gaskets
    qty: 1.0
    unit: unit
  - item_id: fastener_kit_medium
    qty: 1.0
    unit: unit
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `raw_metal_block` not found

This item doesn't exist in the KB.

#### Problem: Item `door_hinge_assembly` not found

This item doesn't exist in the KB.

#### Problem: Item `sealing_gaskets` not found

This item doesn't exist in the KB.

#### Problem: Item `fastener_kit_medium` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_furnace_door_assembly_v0.yaml`
- **BOM available:** No
