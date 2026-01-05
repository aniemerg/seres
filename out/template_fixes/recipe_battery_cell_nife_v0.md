# Fix Intelligence: recipe_battery_cell_nife_v0

## Files

- **Recipe:** `kb/recipes/recipe_battery_cell_nife_v0.yaml`
- **Target item:** `battery_cell_nife`
  - File: `kb/items/battery_cell_nife.yaml`
- **BOM:** None
- **Steps:** 3 total

## Similar Recipes

Found 2 recipes producing similar items:

- `recipe_battery_cell_nife_v1` → battery_cell_nife (3 steps)
- `recipe_battery_cell_nife_local_v0` → battery_cell_nife (3 steps)

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'electrode_fabrication_nife') requires input 'electrode_mix_nife' which is not available

**Location:** Step 0
**Process:** `electrode_fabrication_nife`
  - File: `kb/processes/electrode_fabrication_nife.yaml`

**Current step:**
```yaml
- process_id: electrode_fabrication_nife
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'electrolyte_prep_koh') requires input 'potassium_hydroxide' which is not available

**Location:** Step 1
**Process:** `electrolyte_prep_koh`
  - File: `kb/processes/electrolyte_prep_koh.yaml`

**Current step:**
```yaml
- process_id: electrolyte_prep_koh
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'cell_assembly_and_seal_nife') requires input 'electrode_mix_nife' which is not available

**Location:** Step 2
**Process:** `cell_assembly_and_seal_nife`
  - File: `kb/processes/cell_assembly_and_seal_nife.yaml`

**Current step:**
```yaml
- process_id: cell_assembly_and_seal_nife
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_battery_cell_nife_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 2 found
