# Fix Intelligence: recipe_auger_drill_assembly_v0

## Files

- **Recipe:** `kb/recipes/recipe_auger_drill_assembly_v0.yaml`
- **Target item:** `auger_drill_assembly`
  - File: `kb/items/auger_drill_assembly.yaml`
- **BOM:** None
- **Steps:** 2 total

## Errors (2 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'assembly_basic_v0') requires input 'steel_bar_stock' which is not available

**Location:** Step 0
**Process:** `assembly_basic_v0`
  - File: `kb/processes/assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: steel_bar_stock
    qty: 8.0
    unit: kg
  - item_id: formed_sheet_metal_parts
    qty: 2.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `steel_bar_stock` not found

This item doesn't exist in the KB.

#### Problem: Item `formed_sheet_metal_parts` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'finishing_deburring_v0') requires input 'machined_part_raw' which is not available

**Location:** Step 1
**Process:** `finishing_deburring_v0`
  - File: `kb/processes/finishing_deburring_v0.yaml`

**Current step:**
```yaml
- process_id: finishing_deburring_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_auger_drill_assembly_v0.yaml`
- **BOM available:** No
