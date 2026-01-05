# Fix Intelligence: recipe_copper_etched_laminate_v0

## Files

- **Recipe:** `kb/recipes/recipe_copper_etched_laminate_v0.yaml`
- **Target item:** `copper_etched_laminate`
  - File: `kb/items/copper_etched_laminate.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'copper_etching_process_v0') requires input 'copper_clad_laminate' which is not available

**Location:** Step 0
**Process:** `copper_etching_process_v0`
  - File: `kb/processes/copper_etching_process_v0.yaml`

**Current step:**
```yaml
- process_id: copper_etching_process_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_copper_etched_laminate_v0.yaml`
- **BOM available:** No
