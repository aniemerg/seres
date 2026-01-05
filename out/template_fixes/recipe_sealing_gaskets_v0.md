# Fix Intelligence: recipe_sealing_gaskets_v0

## Files

- **Recipe:** `kb/recipes/recipe_sealing_gaskets_v0.yaml`
- **Target item:** `sealing_gaskets`
  - File: `kb/items/sealing_gaskets.yaml`
- **BOM:** None
- **Steps:** 2 total

## Errors (2 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'cutting_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `cutting_basic_v0`
  - File: `kb/processes/cutting_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: cutting_basic_v0
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

#### Option B: Use previous step outputs

- Step 0 produces: `cut_parts` (9.5 kg)

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_sealing_gaskets_v0.yaml`
- **BOM available:** No
