# Fix Intelligence: recipe_steel_block_raw_v0

## Files

- **Recipe:** `kb/recipes/recipe_steel_block_raw_v0.yaml`
- **Target item:** `steel_block_raw_v0`
  - File: `kb/items/steel_block_raw_v0.yaml`
- **BOM:** None
- **Steps:** 2 total

## Errors (2 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'sawing_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `sawing_basic_v0`
  - File: `kb/processes/sawing_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: sawing_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'inspection_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `inspection_basic_v0`
  - File: `kb/processes/inspection_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: inspection_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_steel_block_raw_v0.yaml`
- **BOM available:** No
