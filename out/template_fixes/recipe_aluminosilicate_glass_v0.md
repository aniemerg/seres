# Fix Intelligence: recipe_aluminosilicate_glass_v0

## Files

- **Recipe:** `kb/recipes/recipe_aluminosilicate_glass_v0.yaml`
- **Target item:** `aluminosilicate_glass`
  - File: `kb/items/aluminosilicate_glass.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'aluminosilicate_glass_production_v0') requires input 'silica_purified' which is not available

**Location:** Step 0
**Process:** `aluminosilicate_glass_production_v0`
  - File: `kb/processes/aluminosilicate_glass_production_v0.yaml`

**Current step:**
```yaml
- process_id: aluminosilicate_glass_production_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_aluminosilicate_glass_v0.yaml`
- **BOM available:** No
