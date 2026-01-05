# Fix Intelligence: recipe_laminated_silicon_steel_core_v0

## Files

- **Recipe:** `kb/recipes/recipe_laminated_silicon_steel_core_v0.yaml`
- **Target item:** `laminated_silicon_steel_core_v0`
  - File: `kb/items/laminated_silicon_steel_core_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'lamination_stamping_v0') requires input 'electrical_steel_sheet' which is not available

**Location:** Step 0
**Process:** `lamination_stamping_v0`
  - File: `kb/processes/lamination_stamping_v0.yaml`

**Current step:**
```yaml
- process_id: lamination_stamping_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_laminated_silicon_steel_core_v0.yaml`
- **BOM available:** No
