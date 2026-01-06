# Fix Intelligence: recipe_compound_applicator_v0

## Files

- **Recipe:** `kb/recipes/recipe_compound_applicator_v0.yaml`
- **Target item:** `compound_applicator`
  - File: `kb/items/compound_applicator.yaml`
- **BOM:** None
- **Steps:** 5 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_compound_applicator_import_v0` → compound_applicator (5 steps)

## Errors (5 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'machining_process_turning_v0') requires input 'steel_bar_stock' which is not available

**Location:** Step 0
**Process:** `machining_process_turning_v0`
  - File: `kb/processes/machining_process_turning_v0.yaml`

**Current step:**
```yaml
- process_id: machining_process_turning_v0
  inputs:
  - item_id: steel_bar_stock
    qty: 0.3
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `steel_bar_stock` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'machining_process_milling_v0') requires input 'valve_body_machined' which is not available

**Location:** Step 1
**Process:** `machining_process_milling_v0`
  - File: `kb/processes/machining_process_milling_v0.yaml`

**Current step:**
```yaml
- process_id: machining_process_milling_v0
  inputs:
  - item_id: valve_body_machined
    qty: 0.25
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `valve_body_machined` not found

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
    qty: 0.1
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `steel_bar_stock` not found

This item doesn't exist in the KB.

---

### Error 4: recipe_step_input_not_satisfied

**Message:** Step 3 (process 'machining_process_drilling_v0') requires input 'steel_bar_stock' which is not available

**Location:** Step 3
**Process:** `machining_process_drilling_v0`
  - File: `kb/processes/machining_process_drilling_v0.yaml`

**Current step:**
```yaml
- process_id: machining_process_drilling_v0
  inputs:
  - item_id: steel_bar_stock
    qty: 0.05
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `steel_bar_stock` not found

This item doesn't exist in the KB.

---

### Error 5: recipe_step_input_not_satisfied

**Message:** Step 4 (process 'assembly_process_general_v0') requires input 'valve_body_machined' which is not available

**Location:** Step 4
**Process:** `assembly_process_general_v0`
  - File: `kb/processes/assembly_process_general_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_process_general_v0
  inputs:
  - item_id: valve_body_machined
    qty: 0.23
    unit: kg
  - item_id: applicator_plunger
    qty: 0.08
    unit: kg
  - item_id: applicator_nozzle
    qty: 0.04
    unit: kg
  - item_id: seal_o_ring_rubber
    qty: 2.0
    unit: each
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `valve_body_machined` not found

This item doesn't exist in the KB.

#### Problem: Item `applicator_plunger` not found

This item doesn't exist in the KB.

#### Problem: Item `applicator_nozzle` not found

This item doesn't exist in the KB.

#### Problem: Item `seal_o_ring_rubber` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 5
- **Recipe file:** `kb/recipes/recipe_compound_applicator_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
