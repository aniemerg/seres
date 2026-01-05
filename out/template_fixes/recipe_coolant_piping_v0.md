# Fix Intelligence: recipe_coolant_piping_v0

## Files

- **Recipe:** `kb/recipes/recipe_coolant_piping_v0.yaml`
- **Target item:** `coolant_piping`
  - File: `kb/items/coolant_piping.yaml`
- **BOM:** None
- **Steps:** 4 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'tube_bending_and_cutting_v0') requires input 'metal_tubing_stock' which is not available

**Location:** Step 0
**Process:** `tube_bending_and_cutting_v0`
  - File: `kb/processes/tube_bending_and_cutting_v0.yaml`

**Current step:**
```yaml
- process_id: tube_bending_and_cutting_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

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

#### Option B: Use previous step outputs

- Step 0 produces: `bent_tube_sections` (0.92 kg)

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

- Step 0 produces: `bent_tube_sections` (0.92 kg)
- Step 1 produces: `welded_fabrications` (9.5 kg)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_coolant_piping_v0.yaml`
- **BOM available:** No
