# Fix Intelligence: recipe_impeller_blades_set_v0

## Files

- **Recipe:** `kb/recipes/recipe_impeller_blades_set_v0.yaml`
- **Target item:** `impeller_blades_set`
  - File: `kb/items/impeller_blades_set.yaml`
- **BOM:** None
- **Steps:** 5 total

## Errors (5 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'metal_casting_process_v0') requires input 'steel_scrap_refined' which is not available

**Location:** Step 0
**Process:** `metal_casting_process_v0`
  - File: `kb/processes/metal_casting_process_v0.yaml`

**Current step:**
```yaml
- process_id: metal_casting_process_v0
  inputs:
  - item_id: steel_scrap_refined
    qty: 3.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `steel_scrap_refined` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'sheet_metal_forming_process_v0') requires input 'steel_sheet_3mm' which is not available

**Location:** Step 1
**Process:** `sheet_metal_forming_process_v0`
  - File: `kb/processes/sheet_metal_forming_process_v0.yaml`

**Current step:**
```yaml
- process_id: sheet_metal_forming_process_v0
  inputs:
  - item_id: steel_sheet_3mm
    qty: 1.5
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `steel_sheet_3mm` not found

This item doesn't exist in the KB.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'machining_process_turning_v0') requires input 'steel_bar_stock' which is not available

**Location:** Step 2
**Process:** `machining_process_turning_v0`
  - File: `kb/processes/machining_process_turning_v0.yaml`

**Current step:**
```yaml
- process_id: machining_process_turning_v0
  inputs:
  - item_id: steel_bar_stock
    qty: 2.7
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `steel_bar_stock` not found

This item doesn't exist in the KB.

---

### Error 4: recipe_step_input_not_satisfied

**Message:** Step 3 (process 'welding_process_general_v0') requires input 'steel_bar_stock' which is not available

**Location:** Step 3
**Process:** `welding_process_general_v0`
  - File: `kb/processes/welding_process_general_v0.yaml`

**Current step:**
```yaml
- process_id: welding_process_general_v0
  inputs:
  - item_id: steel_bar_stock
    qty: 2.5
    unit: kg
  - item_id: steel_sheet_3mm
    qty: 1.4
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `steel_bar_stock` not found

This item doesn't exist in the KB.

#### Problem: Item `steel_sheet_3mm` not found

This item doesn't exist in the KB.

---

### Error 5: recipe_step_input_not_satisfied

**Message:** Step 4 (process 'machining_process_milling_v0') requires input 'impeller_assembly_welded' which is not available

**Location:** Step 4
**Process:** `machining_process_milling_v0`
  - File: `kb/processes/machining_process_milling_v0.yaml`

**Current step:**
```yaml
- process_id: machining_process_milling_v0
  inputs:
  - item_id: impeller_assembly_welded
    qty: 3.8
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `impeller_assembly_welded` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 5
- **Recipe file:** `kb/recipes/recipe_impeller_blades_set_v0.yaml`
- **BOM available:** No
