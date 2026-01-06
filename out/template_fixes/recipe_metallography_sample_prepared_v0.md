# Fix Intelligence: recipe_metallography_sample_prepared_v0

## Files

- **Recipe:** `kb/recipes/recipe_metallography_sample_prepared_v0.yaml`
- **Target item:** `metallography_sample_prepared`
  - File: `kb/items/metallography_sample_prepared.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'metallography_sample_prep_v0') requires input 'metallography_sample_raw' which is not available

**Location:** Step 0
**Process:** `metallography_sample_prep_v0`
  - File: `kb/processes/metallography_sample_prep_v0.yaml`

**Current step:**
```yaml
- process_id: metallography_sample_prep_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_metallography_sample_prepared_v0.yaml`
- **BOM available:** No
