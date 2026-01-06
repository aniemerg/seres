# Fix Intelligence: recipe_condenser_lens_assembly_v0

## Files

- **Recipe:** `kb/recipes/recipe_condenser_lens_assembly_v0.yaml`
- **Target item:** `condenser_lens_assembly`
  - File: `kb/items/condenser_lens_assembly.yaml`
- **BOM:** None
- **Steps:** 4 total

## Errors (4 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'glass_lens_objective_set_fabrication_v0') requires input 'cast_glass_parts' which is not available

**Location:** Step 0
**Process:** `glass_lens_objective_set_fabrication_v0`
  - File: `kb/processes/glass_lens_objective_set_fabrication_v0.yaml`

**Current step:**
```yaml
- process_id: glass_lens_objective_set_fabrication_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'glass_lens_eyepiece_fabrication_v0') requires input 'cast_glass_parts' which is not available

**Location:** Step 1
**Process:** `glass_lens_eyepiece_fabrication_v0`
  - File: `kb/processes/glass_lens_eyepiece_fabrication_v0.yaml`

**Current step:**
```yaml
- process_id: glass_lens_eyepiece_fabrication_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'lens_machine_lunar_v0_assembly_v0') requires input 'machine_frame_small' which is not available

**Location:** Step 2
**Process:** `lens_machine_lunar_v0_assembly_v0`
  - File: `kb/processes/lens_machine_lunar_v0_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: lens_machine_lunar_v0_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'finishing_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
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

- Step 0 produces: `glass_lens_objective_set` (1.0 unit)
- Step 1 produces: `glass_lens_eyepiece` (1.0 unit)
- Step 2 produces: `lens_machine_lunar_v0` (1.0 unit)

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_condenser_lens_assembly_v0.yaml`
- **BOM available:** No
