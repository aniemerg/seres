# Fix Intelligence: recipe_metal_part_surface_treated_v0

## Files

- **Recipe:** `kb/recipes/recipe_metal_part_surface_treated_v0.yaml`
- **Target item:** `metal_part_surface_treated`
  - File: `kb/items/metal_part_surface_treated.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (3 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'metal_forming_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `metal_forming_basic_v0`
  - File: `kb/processes/metal_forming_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: metal_forming_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'surface_treatment_basic_v0') requires input 'formed_metal_part' which is not available

**Location:** Step 1
**Process:** `surface_treatment_basic_v0`
  - File: `kb/processes/surface_treatment_basic_v0.yaml`

**Current step:**
```yaml
- process_id: surface_treatment_basic_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'inspection_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
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

- Step 0 produces: `formed_metal_part` (0.95 kg)
- Step 1 produces: `metal_part_surface_treated` (1.0 kg)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_metal_part_surface_treated_v0.yaml`
- **BOM available:** No
