# Fix Intelligence: recipe_piping_and_valves_set_v0

## Files

- **Recipe:** `kb/recipes/recipe_piping_and_valves_set_v0.yaml`
- **Target item:** `piping_and_valves_set`
  - File: `kb/items/piping_and_valves_set.yaml`
- **BOM:** None
- **Steps:** 4 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_piping_and_valves_set_import_v0` → piping_and_valves_set (4 steps)

## Errors (4 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'metal_casting_process_v0') requires input 'aluminum_alloy_ingot' which is not available

**Location:** Step 0
**Process:** `metal_casting_process_v0`
  - File: `kb/processes/metal_casting_process_v0.yaml`

**Current step:**
```yaml
- process_id: metal_casting_process_v0
  inputs:
  - item_id: aluminum_alloy_ingot
    qty: 5.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `aluminum_alloy_ingot` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'machining_process_turning_v0') requires input 'valve_body_cast_rough' which is not available

**Location:** Step 1
**Process:** `machining_process_turning_v0`
  - File: `kb/processes/machining_process_turning_v0.yaml`

**Current step:**
```yaml
- process_id: machining_process_turning_v0
  inputs:
  - item_id: valve_body_cast_rough
    qty: 4.5
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `valve_body_cast_rough` not found

This item doesn't exist in the KB.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'tube_bending_process_v0') requires input 'aluminum_tube_stock' which is not available

**Location:** Step 2
**Process:** `tube_bending_process_v0`
  - File: `kb/processes/tube_bending_process_v0.yaml`

**Current step:**
```yaml
- process_id: tube_bending_process_v0
  inputs:
  - item_id: aluminum_tube_stock
    qty: 3.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `aluminum_tube_stock` not found

This item doesn't exist in the KB.

---

### Error 4: recipe_step_input_not_satisfied

**Message:** Step 3 (process 'welding_process_tig_v0') requires input 'valve_body_machined' which is not available

**Location:** Step 3
**Process:** `welding_process_tig_v0`
  - File: `kb/processes/welding_process_tig_v0.yaml`

**Current step:**
```yaml
- process_id: welding_process_tig_v0
  inputs:
  - item_id: pipe_bent_sections
    qty: 2.8
    unit: kg
  - item_id: valve_body_machined
    qty: 4.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `pipe_bent_sections` not found

This item doesn't exist in the KB.

#### Problem: Item `valve_body_machined` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_piping_and_valves_set_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
