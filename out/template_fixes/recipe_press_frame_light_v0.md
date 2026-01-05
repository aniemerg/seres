# Fix Intelligence: recipe_press_frame_light_v0

## Files

- **Recipe:** `kb/recipes/recipe_press_frame_light_v0.yaml`
- **Target item:** `press_frame_light`
  - File: `kb/items/press_frame_light.yaml`
- **BOM:** None
- **Steps:** 4 total

## Errors (4 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'metal_cutting_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `metal_cutting_basic_v0`
  - File: `kb/processes/metal_cutting_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: metal_cutting_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'welding_and_fabrication_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `welding_and_fabrication_v0`
  - File: `kb/processes/welding_and_fabrication_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: welding_and_fabrication_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'machining_finish_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `machining_finish_basic_v0`
  - File: `kb/processes/machining_finish_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_finish_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 1 produces: `welded_fabrications` (9.5 kg)

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'stress_relief_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
**Process:** `stress_relief_basic_v0`
  - File: `kb/processes/stress_relief_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: stress_relief_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 1 produces: `welded_fabrications` (9.5 kg)
- Step 2 produces: `machined_part_raw` (1.0 kg)

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_press_frame_light_v0.yaml`
- **BOM available:** No
