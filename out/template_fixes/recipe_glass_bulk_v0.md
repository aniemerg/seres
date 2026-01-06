# Fix Intelligence: recipe_glass_bulk_v0

## Files

- **Recipe:** `kb/recipes/recipe_glass_bulk_v0.yaml`
- **Target item:** `glass_bulk`
  - File: `kb/items/glass_bulk.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'glass_melting_and_forming_v0') requires input 'regolith_fine_fraction' which is not available

**Location:** Step 0
**Process:** `glass_melting_and_forming_v0`
  - File: `kb/processes/glass_melting_and_forming_v0.yaml`

**Current step:**
```yaml
- process_id: glass_melting_and_forming_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_glass_bulk_v0.yaml`
- **BOM available:** No
