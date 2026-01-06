# Fix Intelligence: recipe_basalt_molten_v0

## Files

- **Recipe:** `kb/recipes/recipe_basalt_molten_v0.yaml`
- **Target item:** `basalt_molten`
  - File: `kb/items/basalt_molten.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'basalt_melting_v0') requires input 'basalt_aggregate' which is not available

**Location:** Step 0
**Process:** `basalt_melting_v0`
  - File: `kb/processes/basalt_melting_v0.yaml`

**Current step:**
```yaml
- process_id: basalt_melting_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_basalt_molten_v0.yaml`
- **BOM available:** No
