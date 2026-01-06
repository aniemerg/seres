# Fix Intelligence: recipe_bearing_set_v0

## Files

- **Recipe:** `kb/recipes/recipe_bearing_set_v0.yaml`
- **Target item:** `bearing_set`
  - File: `kb/items/bearing_set.yaml`
- **BOM:** None
- **Steps:** 10 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_bearing_set_v0_v0` → bearing_set_v0 (1 steps)

## Errors (9 found)

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

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'machining_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `machining_basic_v0`
  - File: `kb/processes/machining_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `cast_metal_parts` (0.95 kg)

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'heat_treatment_hardening_v0') requires input 'bearing_rings_machined' which is not available

**Location:** Step 2
**Process:** `heat_treatment_hardening_v0`
  - File: `kb/processes/heat_treatment_hardening_v0.yaml`

**Current step:**
```yaml
- process_id: heat_treatment_hardening_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'precision_grinding_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
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

- Step 0 produces: `cast_metal_parts` (0.95 kg)
- Step 1 produces: `machined_metal_block_v0` (1.8 kg)
- Step 2 produces: `bearing_rings_hardened` (1.05 kg)

---

### Error 5: recipe_step_input_not_satisfied

**Message:** Step 5 (process 'heat_treatment_hardening_v0') requires input 'bearing_rings_machined' which is not available

**Location:** Step 5
**Process:** `heat_treatment_hardening_v0`
  - File: `kb/processes/heat_treatment_hardening_v0.yaml`

**Current step:**
```yaml
- process_id: heat_treatment_hardening_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 6: recipe_step_input_not_satisfied

**Message:** Step 6 (process 'surface_grinding_precision_v0') requires input 'rough_part' which is not available

**Location:** Step 6
**Process:** `surface_grinding_precision_v0`
  - File: `kb/processes/surface_grinding_precision_v0.yaml`

**Current step:**
```yaml
- process_id: surface_grinding_precision_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 7: recipe_template_missing_step_inputs

**Message:** Step 7 uses template process 'metal_casting_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 7
**Process:** `metal_casting_basic_v0`
  - File: `kb/processes/metal_casting_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: metal_casting_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `cast_metal_parts` (0.95 kg)
- Step 1 produces: `machined_metal_block_v0` (1.8 kg)
- Step 2 produces: `bearing_rings_hardened` (1.05 kg)
- Step 3 produces: `finished_part_deburred` (1.0 kg)
- Step 4 produces: `bearing_ring_blanks` (1.3 kg)
- Step 5 produces: `bearing_rings_hardened` (1.05 kg)
- Step 6 produces: `finished_part_deburred` (1.0 kg)

---

### Error 8: recipe_template_missing_step_inputs

**Message:** Step 8 uses template process 'machining_finish_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 8
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
- Step 1 produces: `machined_metal_block_v0` (1.8 kg)
- Step 2 produces: `bearing_rings_hardened` (1.05 kg)
- Step 3 produces: `finished_part_deburred` (1.0 kg)
- Step 4 produces: `bearing_ring_blanks` (1.3 kg)
- Step 5 produces: `bearing_rings_hardened` (1.05 kg)
- Step 6 produces: `finished_part_deburred` (1.0 kg)
- Step 7 produces: `cast_metal_parts` (0.95 kg)

---

### Error 9: recipe_template_missing_step_inputs

**Message:** Step 9 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 9
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
- Step 1 produces: `machined_metal_block_v0` (1.8 kg)
- Step 2 produces: `bearing_rings_hardened` (1.05 kg)
- Step 3 produces: `finished_part_deburred` (1.0 kg)
- Step 4 produces: `bearing_ring_blanks` (1.3 kg)
- Step 5 produces: `bearing_rings_hardened` (1.05 kg)
- Step 6 produces: `finished_part_deburred` (1.0 kg)
- Step 7 produces: `cast_metal_parts` (0.95 kg)
- Step 8 produces: `machined_part_raw` (1.0 kg)

---

## Summary

- **Total errors:** 9
- **Recipe file:** `kb/recipes/recipe_bearing_set_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
