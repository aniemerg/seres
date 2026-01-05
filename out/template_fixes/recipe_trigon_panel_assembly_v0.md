# Fix Intelligence: recipe_trigon_panel_assembly_v0

## Files

- **Recipe:** `kb/recipes/recipe_trigon_panel_assembly_v0.yaml`
- **Target item:** `trigon_panel_assembly_v0`
  - File: `kb/items/trigon_panel_assembly_v0.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'composite_panel_fabrication_v0') requires input 'trigon_panel_structure_v0' which is not available

**Location:** Step 0
**Process:** `composite_panel_fabrication_v0`
  - File: `kb/processes/composite_panel_fabrication_v0.yaml`

**Current step:**
```yaml
- process_id: composite_panel_fabrication_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'motor_assembly_3d_printed_v0') requires input 'sma_motor_components' which is not available

**Location:** Step 1
**Process:** `motor_assembly_3d_printed_v0`
  - File: `kb/processes/motor_assembly_3d_printed_v0.yaml`

**Current step:**
```yaml
- process_id: motor_assembly_3d_printed_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

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

- Step 0 produces: `composite_panel_substrate_v0` (1.0 unit)
- Step 1 produces: `3d_printed_motor_ironpla_v0` (1.0 unit)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_trigon_panel_assembly_v0.yaml`
- **BOM available:** No
