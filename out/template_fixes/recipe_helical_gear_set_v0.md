# Fix Intelligence: recipe_helical_gear_set_v0

## Files

- **Recipe:** `kb/recipes/recipe_helical_gear_set_v0.yaml`
- **Target item:** `helical_gear_set_v0`
  - File: `kb/items/helical_gear_set_v0.yaml`
- **BOM:** None
- **Steps:** 2 total

## Errors (2 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'metal_casting_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `metal_casting_basic_v0`
  - File: `kb/processes/metal_casting_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: metal_casting_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'helical_gear_cutting_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `helical_gear_cutting_basic_v0`
  - File: `kb/processes/helical_gear_cutting_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: helical_gear_cutting_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `cast_metal_parts` (0.95 kg)

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_helical_gear_set_v0.yaml`
- **BOM available:** No
