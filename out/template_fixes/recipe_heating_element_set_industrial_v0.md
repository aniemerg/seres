# Fix Intelligence: recipe_heating_element_set_industrial_v0

## Files

- **Recipe:** `kb/recipes/recipe_heating_element_set_industrial_v0.yaml`
- **Target item:** `heating_element_set_industrial`
  - File: `kb/items/heating_element_set_industrial.yaml`
- **BOM:** None
- **Steps:** 6 total

## Errors (5 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'wire_drawing_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `wire_drawing_basic_v0`
  - File: `kb/processes/wire_drawing_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: wire_drawing_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'coil_winding_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `coil_winding_basic_v0`
  - File: `kb/processes/coil_winding_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: coil_winding_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `metal_wire_feed` (1.0 kg)

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'ceramic_forming_v0') requires input 'ceramic_powder_mixture' which is not available

**Location:** Step 2
**Process:** `ceramic_forming_v0`
  - File: `kb/processes/ceramic_forming_v0.yaml`

**Current step:**
```yaml
- process_id: ceramic_forming_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 4 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 4
**Process:** `assembly_basic_v0`
  - File: `kb/processes/assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `metal_wire_feed` (1.0 kg)
- Step 1 produces: `motor_coil_wound` (2.0 kg)
- Step 2 produces: `green_ceramic_part` (5.0 kg)

---

### Error 5: recipe_template_missing_step_inputs

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

- Step 0 produces: `metal_wire_feed` (1.0 kg)
- Step 1 produces: `motor_coil_wound` (2.0 kg)
- Step 2 produces: `green_ceramic_part` (5.0 kg)
- Step 4 produces: `assembled_equipment` (1.0 kg)

---

## Summary

- **Total errors:** 5
- **Recipe file:** `kb/recipes/recipe_heating_element_set_industrial_v0.yaml`
- **BOM available:** No
