# Fix Intelligence: recipe_silicon_purified_v0

## Files

- **Recipe:** `kb/recipes/recipe_silicon_purified_v0.yaml`
- **Target item:** `silicon_purified`
  - File: `kb/items/silicon_purified.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'silicon_purification_mgsi_v0') requires input 'magnesium_silicide' which is not available

**Location:** Step 0
**Process:** `silicon_purification_mgsi_v0`
  - File: `kb/processes/silicon_purification_mgsi_v0.yaml`

**Current step:**
```yaml
- process_id: silicon_purification_mgsi_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_silicon_purified_v0.yaml`
- **BOM available:** No
