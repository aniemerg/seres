# Fix Intelligence: recipe_tungsten_cathode_coated_v0

## Files

- **Recipe:** `kb/recipes/recipe_tungsten_cathode_coated_v0.yaml`
- **Target item:** `tungsten_cathode_coated`
  - File: `kb/items/tungsten_cathode_coated.yaml`
- **BOM:** None
- **Steps:** 6 total

## Errors (6 found)

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

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'pressing_operations_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `pressing_operations_basic_v0`
  - File: `kb/processes/pressing_operations_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: pressing_operations_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `processed_powder_mixture` (1.0 kg)

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'tungsten_sintering_high_temp_v0') requires input 'tungsten_powder' which is not available

**Location:** Step 2
**Process:** `tungsten_sintering_high_temp_v0`
  - File: `kb/processes/tungsten_sintering_high_temp_v0.yaml`

**Current step:**
```yaml
- process_id: tungsten_sintering_high_temp_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'machining_finish_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
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
- Step 1 produces: `pressed_component` (9.5 kg)
- Step 2 produces: `sintered_tungsten_part` (0.95 kg)

---

### Error 5: recipe_step_input_not_satisfied

**Message:** Step 4 (process 'cathode_coating_application_v0') requires input 'tungsten_cathode_blank_v0' which is not available

**Location:** Step 4
**Process:** `cathode_coating_application_v0`
  - File: `kb/processes/cathode_coating_application_v0.yaml`

**Current step:**
```yaml
- process_id: cathode_coating_application_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 6: recipe_template_missing_step_inputs

**Message:** Step 5 uses template process 'inspection_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 5
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
- Step 1 produces: `pressed_component` (9.5 kg)
- Step 2 produces: `sintered_tungsten_part` (0.95 kg)
- Step 3 produces: `machined_part_raw` (1.0 kg)
- Step 4 produces: `tungsten_cathode_coated` (1.0 unit)

---

## Summary

- **Total errors:** 6
- **Recipe file:** `kb/recipes/recipe_tungsten_cathode_coated_v0.yaml`
- **BOM available:** No
