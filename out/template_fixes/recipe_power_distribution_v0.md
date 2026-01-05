# Fix Intelligence: recipe_power_distribution_v0

## Files

- **Recipe:** `kb/recipes/recipe_power_distribution_v0.yaml`
- **Target item:** `power_distribution`
  - File: `kb/items/power_distribution.yaml`
- **BOM:** None
- **Steps:** 4 total

## Errors (4 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'sheet_metal_fabrication_v0') requires input 'sheet_metal_or_structural_steel' which is not available

**Location:** Step 0
**Process:** `sheet_metal_fabrication_v0`
  - File: `kb/processes/sheet_metal_fabrication_v0.yaml`

**Current step:**
```yaml
- process_id: sheet_metal_fabrication_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'cable_harness_assembly_v0') requires input 'electrical_wire_and_connectors' which is not available

**Location:** Step 1
**Process:** `cable_harness_assembly_v0`
  - File: `kb/processes/cable_harness_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: cable_harness_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'electrical_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `electrical_assembly_basic_v0`
  - File: `kb/processes/electrical_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: electrical_assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `formed_sheet_metal_parts` (9.5 kg)
- Step 1 produces: `assembled_cable_harness` (1.0 unit)

---

### Error 4: recipe_step_input_not_satisfied

**Message:** Step 3 (process 'electrical_testing_v0') requires input 'assembled_electrical_system' which is not available

**Location:** Step 3
**Process:** `electrical_testing_v0`
  - File: `kb/processes/electrical_testing_v0.yaml`

**Current step:**
```yaml
- process_id: electrical_testing_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_power_distribution_v0.yaml`
- **BOM available:** No
