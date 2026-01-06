# Fix Intelligence: recipe_information_closure_verification_v0

## Files

- **Recipe:** `kb/recipes/recipe_information_closure_verification_v0.yaml`
- **Target item:** `information_closure_verification_v0`
  - File: `kb/items/information_closure_verification_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'information_verification_unit_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `information_verification_unit_v0`
  - File: `kb/processes/information_verification_unit_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: information_verification_unit_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_information_closure_verification_v0.yaml`
- **BOM available:** No
