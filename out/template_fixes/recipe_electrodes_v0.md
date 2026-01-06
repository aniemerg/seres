# Fix Intelligence: recipe_electrodes_v0

## Files

- **Recipe:** `kb/recipes/recipe_electrodes_v0.yaml`
- **Target item:** `electrodes`
  - File: `kb/items/electrodes.yaml`
- **BOM:** None
- **Steps:** 4 total

## Errors (4 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'powder_processing_v0') requires input 'powder_metal_or_ceramic' which is not available

**Location:** Step 0
**Process:** `powder_processing_v0`
  - File: `kb/processes/powder_processing_v0.yaml`

**Current step:**
```yaml
- process_id: powder_processing_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'sintering_and_hot_pressing_v0') requires input 'regolith_fine_fraction' which is not available

**Location:** Step 1
**Process:** `sintering_and_hot_pressing_v0`
  - File: `kb/processes/sintering_and_hot_pressing_v0.yaml`

**Current step:**
```yaml
- process_id: sintering_and_hot_pressing_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

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

- Step 0 produces: `processed_powder_mixture` (1.0 kg)
- Step 1 produces: `sintered_shapes` (1.0 kg)

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'inspection_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
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

- Step 0 produces: `processed_powder_mixture` (1.0 kg)
- Step 1 produces: `sintered_shapes` (1.0 kg)
- Step 2 produces: `machined_part_raw` (1.0 kg)

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_electrodes_v0.yaml`
- **BOM available:** No
