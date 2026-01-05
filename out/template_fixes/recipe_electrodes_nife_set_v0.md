# Fix Intelligence: recipe_electrodes_nife_set_v0

## Files

- **Recipe:** `kb/recipes/recipe_electrodes_nife_set_v0.yaml`
- **Target item:** `electrodes_nife_set`
  - File: `kb/items/electrodes_nife_set.yaml`
- **BOM:** None
- **Steps:** 6 total

## Errors (6 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'powder_milling_process_v0') requires input 'nickel_hydroxide' which is not available

**Location:** Step 0
**Process:** `powder_milling_process_v0`
  - File: `kb/processes/powder_milling_process_v0.yaml`

**Current step:**
```yaml
- process_id: powder_milling_process_v0
  inputs:
  - item_id: nickel_hydroxide
    qty: 2.0
    unit: kg
  - item_id: graphite_powder
    qty: 0.1
    unit: kg
  - item_id: binder_simple
    qty: 0.1
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `nickel_hydroxide` not found

This item doesn't exist in the KB.

#### Problem: Item `graphite_powder` not found

This item doesn't exist in the KB.

#### Problem: Item `binder_simple` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'powder_milling_process_v0') requires input 'iron_powder_v0' which is not available

**Location:** Step 1
**Process:** `powder_milling_process_v0`
  - File: `kb/processes/powder_milling_process_v0.yaml`

**Current step:**
```yaml
- process_id: powder_milling_process_v0
  inputs:
  - item_id: iron_powder_v0
    qty: 2.0
    unit: kg
  - item_id: binder_simple
    qty: 0.1
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `iron_powder_v0` not found

This item doesn't exist in the KB.

#### Problem: Item `binder_simple` not found

This item doesn't exist in the KB.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'metal_stamping_process_v0') requires input 'steel_sheet_1mm' which is not available

**Location:** Step 2
**Process:** `metal_stamping_process_v0`
  - File: `kb/processes/metal_stamping_process_v0.yaml`

**Current step:**
```yaml
- process_id: metal_stamping_process_v0
  inputs:
  - item_id: steel_sheet_1mm
    qty: 1.5
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `steel_sheet_1mm` not found

This item doesn't exist in the KB.

---

### Error 4: recipe_step_input_not_satisfied

**Message:** Step 3 (process 'powder_pressing_process_v0') requires input 'electrode_mix_nife' which is not available

**Location:** Step 3
**Process:** `powder_pressing_process_v0`
  - File: `kb/processes/powder_pressing_process_v0.yaml`

**Current step:**
```yaml
- process_id: powder_pressing_process_v0
  inputs:
  - item_id: electrode_mix_nife
    qty: 2.1
    unit: kg
  - item_id: electrode_grid_set
    qty: 0.7
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `electrode_mix_nife` not found

This item doesn't exist in the KB.

#### Problem: Item `electrode_grid_set` not found

This item doesn't exist in the KB.

---

### Error 5: recipe_step_input_not_satisfied

**Message:** Step 4 (process 'powder_pressing_process_v0') requires input 'electrode_mix_nife' which is not available

**Location:** Step 4
**Process:** `powder_pressing_process_v0`
  - File: `kb/processes/powder_pressing_process_v0.yaml`

**Current step:**
```yaml
- process_id: powder_pressing_process_v0
  inputs:
  - item_id: electrode_mix_nife
    qty: 2.05
    unit: kg
  - item_id: electrode_grid_set
    qty: 0.7
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `electrode_mix_nife` not found

This item doesn't exist in the KB.

#### Problem: Item `electrode_grid_set` not found

This item doesn't exist in the KB.

---

### Error 6: recipe_step_input_not_satisfied

**Message:** Step 5 (process 'drying_process_oven_v0') requires input 'positive_electrode_pressed' which is not available

**Location:** Step 5
**Process:** `drying_process_oven_v0`
  - File: `kb/processes/drying_process_oven_v0.yaml`

**Current step:**
```yaml
- process_id: drying_process_oven_v0
  inputs:
  - item_id: positive_electrode_pressed
    qty: 2.7
    unit: kg
  - item_id: negative_electrode_pressed
    qty: 2.7
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `positive_electrode_pressed` not found

This item doesn't exist in the KB.

#### Problem: Item `negative_electrode_pressed` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 6
- **Recipe file:** `kb/recipes/recipe_electrodes_nife_set_v0.yaml`
- **BOM available:** No
