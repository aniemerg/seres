# Fix Intelligence: recipe_electrode_materials_v0

## Files

- **Recipe:** `kb/recipes/recipe_electrode_materials_v0.yaml`
- **Target item:** `electrode_materials`
  - File: `kb/items/electrode_materials.yaml`
- **BOM:** None
- **Steps:** 2 total

## Errors (2 found)

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

**Message:** Step 1 (process 'cathode_oxide_coating_v0') requires input 'coating_compound' which is not available

**Location:** Step 1
**Process:** `cathode_oxide_coating_v0`
  - File: `kb/processes/cathode_oxide_coating_v0.yaml`

**Current step:**
```yaml
- process_id: cathode_oxide_coating_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_electrode_materials_v0.yaml`
- **BOM available:** No
