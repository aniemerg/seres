# Fix Intelligence: recipe_insulated_part_or_wire_v0

## Files

- **Recipe:** `kb/recipes/recipe_insulated_part_or_wire_v0.yaml`
- **Target item:** `insulated_part_or_wire`
  - File: `kb/items/insulated_part_or_wire.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (3 found)

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

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'plastic_extrusion_v0') requires input 'plastic_pellets' which is not available

**Location:** Step 1
**Process:** `plastic_extrusion_v0`
  - File: `kb/processes/plastic_extrusion_v0.yaml`

**Current step:**
```yaml
- process_id: plastic_extrusion_v0
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

- Step 0 produces: `metal_wire_feed` (1.0 kg)
- Step 1 produces: `extruded_plastic_profile` (1.0 kg)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_insulated_part_or_wire_v0.yaml`
- **BOM available:** No
