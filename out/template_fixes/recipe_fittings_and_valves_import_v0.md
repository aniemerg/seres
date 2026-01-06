# Fix Intelligence: recipe_fittings_and_valves_import_v0

## Files

- **Recipe:** `kb/recipes/recipe_fittings_and_valves_import_v0.yaml`
- **Target item:** `fittings_and_valves`
  - File: `kb/items/fittings_and_valves.yaml`
- **BOM:** None
- **Steps:** 5 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_fittings_and_valves_v0` → fittings_and_valves (5 steps)

## Errors (4 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'metal_casting_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `metal_casting_basic_v0`
  - File: `kb/processes/metal_casting_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: metal_casting_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'valve_body_boring_v0') requires input 'valve_body_cast_rough' which is not available

**Location:** Step 1
**Process:** `valve_body_boring_v0`
  - File: `kb/processes/valve_body_boring_v0.yaml`

**Current step:**
```yaml
- process_id: valve_body_boring_v0
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

**Message:** Step 4 (process 'leak_testing_v0') requires input 'welded_assemblies' which is not available

**Location:** Step 4
**Process:** `leak_testing_v0`
  - File: `kb/processes/leak_testing_v0.yaml`

**Current step:**
```yaml
- process_id: leak_testing_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_fittings_and_valves_import_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
