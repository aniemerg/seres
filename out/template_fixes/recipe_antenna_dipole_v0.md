# Fix Intelligence: recipe_antenna_dipole_v0

## Files

- **Recipe:** `kb/recipes/recipe_antenna_dipole_v0.yaml`
- **Target item:** `antenna_dipole_v0`
  - File: `kb/items/antenna_dipole_v0.yaml`
- **BOM:** None
- **Steps:** 4 total

## Errors (4 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'metal_cutting_process_v0') requires input 'aluminum_tube_stock' which is not available

**Location:** Step 0
**Process:** `metal_cutting_process_v0`
  - File: `kb/processes/metal_cutting_process_v0.yaml`

**Current step:**
```yaml
- process_id: metal_cutting_process_v0
  inputs:
  - item_id: aluminum_tube_stock
    qty: 0.5
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `aluminum_tube_stock` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'ceramic_sintering_process_v0') requires input 'alumina_powder' which is not available

**Location:** Step 1
**Process:** `ceramic_sintering_process_v0`
  - File: `kb/processes/ceramic_sintering_process_v0.yaml`

**Current step:**
```yaml
- process_id: ceramic_sintering_process_v0
  inputs:
  - item_id: alumina_powder
    qty: 0.1
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `alumina_powder` not found

This item doesn't exist in the KB.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'machining_process_drilling_v0') requires input 'center_insulator_ceramic' which is not available

**Location:** Step 2
**Process:** `machining_process_drilling_v0`
  - File: `kb/processes/machining_process_drilling_v0.yaml`

**Current step:**
```yaml
- process_id: machining_process_drilling_v0
  inputs:
  - item_id: center_insulator_ceramic
    qty: 0.08
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `center_insulator_ceramic` not found

This item doesn't exist in the KB.

---

### Error 4: recipe_step_input_not_satisfied

**Message:** Step 3 (process 'assembly_process_general_v0') requires input 'antenna_elements_cut' which is not available

**Location:** Step 3
**Process:** `assembly_process_general_v0`
  - File: `kb/processes/assembly_process_general_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_process_general_v0
  inputs:
  - item_id: antenna_elements_cut
    qty: 0.48
    unit: kg
  - item_id: insulator_drilled
    qty: 0.075
    unit: kg
  - item_id: coaxial_connector_n_type
    qty: 1.0
    unit: each
  - item_id: wire_copper_insulated
    qty: 0.05
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `antenna_elements_cut` not found

This item doesn't exist in the KB.

#### Problem: Item `insulator_drilled` not found

This item doesn't exist in the KB.

#### Problem: Item `coaxial_connector_n_type` not found

This item doesn't exist in the KB.

#### Problem: Item `wire_copper_insulated` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_antenna_dipole_v0.yaml`
- **BOM available:** No
