# Fix Intelligence: recipe_molding_press_cylinder_v0

## Files

- **Recipe:** `kb/recipes/recipe_molding_press_cylinder_v0.yaml`
- **Target item:** `molding_press_cylinder`
  - File: `kb/items/molding_press_cylinder.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (2 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'machining_finish_basic_v0') requires input 'steel_bar_stock' which is not available

**Location:** Step 0
**Process:** `machining_finish_basic_v0`
  - File: `kb/processes/machining_finish_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_finish_basic_v0
  inputs:
  - item_id: steel_bar_stock
    qty: 45.0
    unit: kg
  - item_id: hydraulic_seals_set
    qty: 1.0
    unit: kg
  - item_id: fastener_kit_small
    qty: 0.5
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `steel_bar_stock` not found

This item doesn't exist in the KB.

#### Problem: Item `hydraulic_seals_set` not found

This item doesn't exist in the KB.

#### Problem: Item `fastener_kit_small` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'sealing_and_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `sealing_and_assembly_basic_v0`
  - File: `kb/processes/sealing_and_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: sealing_and_assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `molding_press_cylinder` (1.0 unit)

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_molding_press_cylinder_v0.yaml`
- **BOM available:** No
