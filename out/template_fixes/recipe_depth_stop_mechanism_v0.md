# Fix Intelligence: recipe_depth_stop_mechanism_v0

## Files

- **Recipe:** `kb/recipes/recipe_depth_stop_mechanism_v0.yaml`
- **Target item:** `depth_stop_mechanism`
  - File: `kb/items/depth_stop_mechanism.yaml`
- **BOM:** None
- **Steps:** 6 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_depth_stop_mechanism_import_v0` → depth_stop_mechanism (3 steps)

## Errors (6 found)

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

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'machining_process_turning_v0') requires input 'rough_part' which is not available

**Location:** Step 1
**Process:** `machining_process_turning_v0`
  - File: `kb/processes/machining_process_turning_v0.yaml`

**Current step:**
```yaml
- process_id: machining_process_turning_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'machining_process_drilling_v0') requires input 'center_insulator_ceramic' which is not available

**Location:** Step 2
**Process:** `machining_process_drilling_v0`
  - File: `kb/processes/machining_process_drilling_v0.yaml`

**Current step:**
```yaml
- process_id: machining_process_drilling_v0
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

- Step 0 produces: `cast_metal_parts` (0.95 kg)
- Step 1 produces: `machined_steel_part_precision` (0.075 kg)
- Step 2 produces: `insulator_drilled` (0.075 kg)

---

### Error 5: recipe_template_missing_step_inputs

**Message:** Step 4 uses template process 'machining_precision_v0' but doesn't provide step-level input overrides

**Location:** Step 4
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

- Step 0 produces: `cast_metal_parts` (0.95 kg)
- Step 1 produces: `machined_steel_part_precision` (0.075 kg)
- Step 2 produces: `insulator_drilled` (0.075 kg)
- Step 3 produces: `machined_part_raw` (1.0 kg)

---

### Error 6: recipe_template_missing_step_inputs

**Message:** Step 5 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 5
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

- Step 0 produces: `cast_metal_parts` (0.95 kg)
- Step 1 produces: `machined_steel_part_precision` (0.075 kg)
- Step 2 produces: `insulator_drilled` (0.075 kg)
- Step 3 produces: `machined_part_raw` (1.0 kg)
- Step 4 produces: `machined_steel_part_precision` (7.0 kg)

---

## Summary

- **Total errors:** 6
- **Recipe file:** `kb/recipes/recipe_depth_stop_mechanism_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
