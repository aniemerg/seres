# Fix Intelligence: recipe_grinding_spindle_assembly_v0

## Files

- **Recipe:** `kb/recipes/recipe_grinding_spindle_assembly_v0.yaml`
- **Target item:** `grinding_spindle_assembly`
  - File: `kb/items/grinding_spindle_assembly.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (2 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'metal_casting_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
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

**Message:** Step 2 uses template process 'precision_grinding_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `precision_grinding_basic_v0`
  - File: `kb/processes/precision_grinding_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: precision_grinding_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 1 produces: `cast_metal_parts` (0.95 kg)

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_grinding_spindle_assembly_v0.yaml`
- **BOM available:** No
