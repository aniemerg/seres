# Fix Intelligence: recipe_dicobalt_octacarbonyl_v0

## Files

- **Recipe:** `kb/recipes/recipe_dicobalt_octacarbonyl_v0.yaml`
- **Target item:** `dicobalt_octacarbonyl`
  - File: `kb/items/dicobalt_octacarbonyl.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'dicobalt_octacarbonyl_synthesis_v0') requires input 'carbon_monoxide' which is not available

**Location:** Step 0
**Process:** `dicobalt_octacarbonyl_synthesis_v0`
  - File: `kb/processes/dicobalt_octacarbonyl_synthesis_v0.yaml`

**Current step:**
```yaml
- process_id: dicobalt_octacarbonyl_synthesis_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_dicobalt_octacarbonyl_v0.yaml`
- **BOM available:** No
