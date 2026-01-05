# Fix Intelligence: recipe_insulation_coating_material_v0

## Files

- **Recipe:** `kb/recipes/recipe_insulation_coating_material_v0.yaml`
- **Target item:** `insulation_coating_material`
  - File: `kb/items/insulation_coating_material.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'epoxy_resin_to_insulation_coating_v0') requires input 'epoxy_resin_base' which is not available

**Location:** Step 0
**Process:** `epoxy_resin_to_insulation_coating_v0`
  - File: `kb/processes/epoxy_resin_to_insulation_coating_v0.yaml`

**Current step:**
```yaml
- process_id: epoxy_resin_to_insulation_coating_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_insulation_coating_material_v0.yaml`
- **BOM available:** No
