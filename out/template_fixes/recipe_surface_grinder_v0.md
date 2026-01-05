# Fix Intelligence: recipe_surface_grinder_v0

## Files

- **Recipe:** `kb/recipes/recipe_surface_grinder_v0.yaml`
- **Target item:** `surface_grinder`
  - File: `kb/items/surface_grinder.yaml`
- **BOM:** None
- **Steps:** 5 total

## Errors (5 found)

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

**Message:** Step 1 uses template process 'machining_finish_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
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

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
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
- Step 1 produces: `machined_part_raw` (1.0 kg)

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'wiring_and_electronics_integration_v0' but doesn't provide step-level input overrides

**Location:** Step 3
**Process:** `wiring_and_electronics_integration_v0`
  - File: `kb/processes/wiring_and_electronics_integration_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: wiring_and_electronics_integration_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `cast_metal_parts` (0.95 kg)
- Step 1 produces: `machined_part_raw` (1.0 kg)
- Step 2 produces: `assembled_equipment` (1.0 kg)

---

### Error 5: recipe_step_input_not_satisfied

**Message:** Step 4 (process 'precision_alignment_and_leveling_v0') requires input 'machine_frame_small' which is not available

**Location:** Step 4
**Process:** `precision_alignment_and_leveling_v0`
  - File: `kb/processes/precision_alignment_and_leveling_v0.yaml`

**Current step:**
```yaml
- process_id: precision_alignment_and_leveling_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 5
- **Recipe file:** `kb/recipes/recipe_surface_grinder_v0.yaml`
- **BOM available:** No
