# Fix Intelligence: recipe_piping_assembly_small_v3

## Files

- **Recipe:** `kb/recipes/recipe_piping_assembly_small_v3.yaml`
- **Target item:** `piping_assembly_small`
  - File: `kb/items/piping_assembly_small.yaml`
- **BOM:** None
- **Steps:** 3 total

## Similar Recipes

Found 3 recipes producing similar items:

- `recipe_piping_assembly_small_v2` → piping_assembly_small (3 steps)
- `recipe_piping_assembly_small_v1` → piping_assembly_small (3 steps)
- `recipe_piping_assembly_small_v0` → piping_assembly_small_v0 (4 steps)

## Errors (2 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'tube_bending_and_cutting_v0') requires input 'metal_tubing_stock' which is not available

**Location:** Step 0
**Process:** `tube_bending_and_cutting_v0`
  - File: `kb/processes/tube_bending_and_cutting_v0.yaml`

**Current step:**
```yaml
- process_id: tube_bending_and_cutting_v0
  inputs:
  - item_id: metal_tubing_stock
    qty: 1.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `metal_tubing_stock` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'welding_process_tig_v0') requires input 'pipe_bent_sections' which is not available

**Location:** Step 1
**Process:** `welding_process_tig_v0`
  - File: `kb/processes/welding_process_tig_v0.yaml`

**Current step:**
```yaml
- process_id: welding_process_tig_v0
  inputs:
  - item_id: pipe_bent_sections
    qty: 0.92
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

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_piping_assembly_small_v3.yaml`
- **BOM available:** No
- **Similar recipes:** 3 found
