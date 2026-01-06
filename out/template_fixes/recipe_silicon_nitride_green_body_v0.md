# Fix Intelligence: recipe_silicon_nitride_green_body_v0

## Files

- **Recipe:** `kb/recipes/recipe_silicon_nitride_green_body_v0.yaml`
- **Target item:** `silicon_nitride_green_body`
  - File: `kb/items/silicon_nitride_green_body.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'powder_compaction_process_v0') requires input 'silicon_nitride_powder_fine' which is not available

**Location:** Step 0
**Process:** `powder_compaction_process_v0`
  - File: `kb/processes/powder_compaction_process_v0.yaml`

**Current step:**
```yaml
- process_id: powder_compaction_process_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_silicon_nitride_green_body_v0.yaml`
- **BOM available:** No
