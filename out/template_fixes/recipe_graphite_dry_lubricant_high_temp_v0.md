# Fix Intelligence: recipe_graphite_dry_lubricant_high_temp_v0

## Files

- **Recipe:** `kb/recipes/recipe_graphite_dry_lubricant_high_temp_v0.yaml`
- **Target item:** `graphite_dry_lubricant_high_temp_v0`
  - File: `kb/items/graphite_dry_lubricant_high_temp_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'graphite_dry_lubricant_high_temp_v0') requires input 'graphite_powder' which is not available

**Location:** Step 0
**Process:** `graphite_dry_lubricant_high_temp_v0`
  - File: `kb/processes/graphite_dry_lubricant_high_temp_v0.yaml`

**Current step:**
```yaml
- process_id: graphite_dry_lubricant_high_temp_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_graphite_dry_lubricant_high_temp_v0.yaml`
- **BOM available:** No
