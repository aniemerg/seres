# Fix Intelligence: recipe_fastener_kit_medium_v0

## Files

- **Recipe:** `kb/recipes/recipe_fastener_kit_medium_v0.yaml`
- **Target item:** `fastener_kit_medium`
  - File: `kb/items/fastener_kit_medium.yaml`
- **BOM:** None
- **Steps:** 7 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_fastener_kit_medium_assembly_v0` → fastener_kit_medium (1 steps)

## Errors (7 found)

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

**Message:** Step 1 uses template process 'forging_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `forging_basic_v0`
  - File: `kb/processes/forging_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: forging_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `metal_wire_feed` (1.0 kg)

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

- Step 0 produces: `metal_wire_feed` (1.0 kg)
- Step 1 produces: `forged_steel_parts` (1.0 kg)

---

### Error 4: recipe_step_input_not_satisfied

**Message:** Step 3 (process 'sheet_metal_forming_process_v0') requires input 'steel_sheet_3mm' which is not available

**Location:** Step 3
**Process:** `sheet_metal_forming_process_v0`
  - File: `kb/processes/sheet_metal_forming_process_v0.yaml`

**Current step:**
```yaml
- process_id: sheet_metal_forming_process_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 5: recipe_template_missing_step_inputs

**Message:** Step 4 uses template process 'heat_treatment_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 4
**Process:** `heat_treatment_basic_v0`
  - File: `kb/processes/heat_treatment_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: heat_treatment_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `metal_wire_feed` (1.0 kg)
- Step 1 produces: `forged_steel_parts` (1.0 kg)
- Step 2 produces: `machined_part_raw` (1.0 kg)
- Step 3 produces: `steel_chassis_sheet_metal` (1.0 kg)

---

### Error 6: recipe_template_missing_step_inputs

**Message:** Step 5 uses template process 'finishing_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 5
**Process:** `finishing_basic_v0`
  - File: `kb/processes/finishing_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: finishing_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `metal_wire_feed` (1.0 kg)
- Step 1 produces: `forged_steel_parts` (1.0 kg)
- Step 2 produces: `machined_part_raw` (1.0 kg)
- Step 3 produces: `steel_chassis_sheet_metal` (1.0 kg)
- Step 4 produces: `finished_part` (10.0 kg)

---

### Error 7: recipe_template_missing_step_inputs

**Message:** Step 6 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 6
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
- Step 1 produces: `forged_steel_parts` (1.0 kg)
- Step 2 produces: `machined_part_raw` (1.0 kg)
- Step 3 produces: `steel_chassis_sheet_metal` (1.0 kg)
- Step 4 produces: `finished_part` (10.0 kg)
- Step 5 produces: `finished_part` (1.0 unit)

---

## Summary

- **Total errors:** 7
- **Recipe file:** `kb/recipes/recipe_fastener_kit_medium_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
