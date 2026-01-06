# Fix Intelligence: recipe_machined_metal_block_v0

## Files

- **Recipe:** `kb/recipes/recipe_machined_metal_block_v0.yaml`
- **Target item:** `machined_metal_block_v0`
  - File: `kb/items/machined_metal_block_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'machining_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `machining_basic_v0`
  - File: `kb/processes/machining_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_machined_metal_block_v0.yaml`
- **BOM available:** No
