# Fix Intelligence: recipe_uncoated_substrate_material_v0

## Files

- **Recipe:** `kb/recipes/recipe_uncoated_substrate_material_v0.yaml`
- **Target item:** `uncoated_substrate_material_v0`
  - File: `kb/items/uncoated_substrate_material_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'substrate_fabrication_basic_v0') requires input 'regolith_lunar_highlands' which is not available

**Location:** Step 0
**Process:** `substrate_fabrication_basic_v0`
  - File: `kb/processes/substrate_fabrication_basic_v0.yaml`

**Current step:**
```yaml
- process_id: substrate_fabrication_basic_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_uncoated_substrate_material_v0.yaml`
- **BOM available:** No
