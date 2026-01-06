# Fix Intelligence: recipe_hydraulic_cylinder_small_v0

## Files

- **Recipe:** `kb/recipes/recipe_hydraulic_cylinder_small_v0.yaml`
- **Target item:** `hydraulic_cylinder_small`
  - File: `kb/items/hydraulic_cylinder_small.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (2 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'machining_finish_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `machining_finish_basic_v0`
  - File: `kb/processes/machining_finish_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_finish_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'sealing_and_assembly_basic_v0') requires input 'raw_metal_block' which is not available

**Location:** Step 1
**Process:** `sealing_and_assembly_basic_v0`
  - File: `kb/processes/sealing_and_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: sealing_and_assembly_basic_v0
  inputs:
  - item_id: raw_metal_block
    qty: 12.0
    unit: kg
  - item_id: hydraulic_seals_set
    qty: 1.0
    unit: unit
  - item_id: fastener_kit_small
    qty: 1.0
    unit: unit
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `raw_metal_block` not found

This item doesn't exist in the KB.

#### Problem: Item `hydraulic_seals_set` not found

This item doesn't exist in the KB.

#### Problem: Item `fastener_kit_small` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_hydraulic_cylinder_small_v0.yaml`
- **BOM available:** No
