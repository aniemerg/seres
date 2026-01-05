# Fix Intelligence: recipe_thermal_storage_media_regolith_v0

## Files

- **Recipe:** `kb/recipes/recipe_thermal_storage_media_regolith_v0.yaml`
- **Target item:** `thermal_storage_media_regolith`
  - File: `kb/items/thermal_storage_media_regolith.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'regolith_collection_and_processing_v0') requires input 'regolith_lunar_highlands' which is not available

**Location:** Step 0
**Process:** `regolith_collection_and_processing_v0`
  - File: `kb/processes/regolith_collection_and_processing_v0.yaml`

**Current step:**
```yaml
- process_id: regolith_collection_and_processing_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_thermal_storage_media_regolith_v0.yaml`
- **BOM available:** No
