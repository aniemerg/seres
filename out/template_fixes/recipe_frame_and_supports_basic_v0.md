# Fix Intelligence: recipe_frame_and_supports_basic_v0

## Files

- **Recipe:** `kb/recipes/recipe_frame_and_supports_basic_v0.yaml`
- **Target item:** `frame_and_supports_basic`
  - File: `kb/items/frame_and_supports_basic.yaml`
- **BOM:** None
- **Steps:** 4 total

## Errors (4 found)

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

**Message:** Step 1 uses template process 'welding_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `welding_basic_v0`
  - File: `kb/processes/welding_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: welding_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `cut_parts` (9.5 kg)

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'drilling_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `drilling_basic_v0`
  - File: `kb/processes/drilling_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: drilling_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `cut_parts` (9.5 kg)
- Step 1 produces: `welded_assemblies` (1.0 kg)

---

### Error 4: recipe_step_input_not_satisfied

**Message:** Step 3 (process 'surface_treatment_basic_v0') requires input 'formed_metal_part' which is not available

**Location:** Step 3
**Process:** `surface_treatment_basic_v0`
  - File: `kb/processes/surface_treatment_basic_v0.yaml`

**Current step:**
```yaml
- process_id: surface_treatment_basic_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_frame_and_supports_basic_v0.yaml`
- **BOM available:** No
