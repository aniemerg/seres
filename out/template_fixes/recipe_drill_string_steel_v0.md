# Fix Intelligence: recipe_drill_string_steel_v0

## Files

- **Recipe:** `kb/recipes/recipe_drill_string_steel_v0.yaml`
- **Target item:** `drill_string_steel`
  - File: `kb/items/drill_string_steel.yaml`
- **BOM:** None
- **Steps:** 2 total

## Errors (2 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'tube_bending_and_cutting_v0') requires input 'metal_tubing_stock' which is not available

**Location:** Step 0
**Process:** `tube_bending_and_cutting_v0`
  - File: `kb/processes/tube_bending_and_cutting_v0.yaml`

**Current step:**
```yaml
- process_id: tube_bending_and_cutting_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'machining_precision_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `machining_precision_v0`
  - File: `kb/processes/machining_precision_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_precision_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `bent_tube_sections` (0.92 kg)

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_drill_string_steel_v0.yaml`
- **BOM available:** No
