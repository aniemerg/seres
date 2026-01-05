# Fix Intelligence: recipe_hormone_digital_signaling_v0

## Files

- **Recipe:** `kb/recipes/recipe_hormone_digital_signaling_v0.yaml`
- **Target item:** `hormone_digital_signaling_v0`
  - File: `kb/items/hormone_digital_signaling_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'digital_signal_generation_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `digital_signal_generation_v0`
  - File: `kb/processes/digital_signal_generation_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: digital_signal_generation_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_hormone_digital_signaling_v0.yaml`
- **BOM available:** No
