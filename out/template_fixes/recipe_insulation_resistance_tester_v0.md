# Fix Intelligence: recipe_insulation_resistance_tester_v0

## Files

- **Recipe:** `kb/recipes/recipe_insulation_resistance_tester_v0.yaml`
- **Target item:** `insulation_resistance_tester`
  - File: `kb/items/insulation_resistance_tester.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'control_panel_assembly_v0') requires input 'enclosure_electrical_medium' which is not available

**Location:** Step 0
**Process:** `control_panel_assembly_v0`
  - File: `kb/processes/control_panel_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: control_panel_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'electrical_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
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

- Step 0 produces: `control_panel_assembly_v0` (25.0 kg)

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'integration_test_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `integration_test_basic_v0`
  - File: `kb/processes/integration_test_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: integration_test_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `control_panel_assembly_v0` (25.0 kg)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_insulation_resistance_tester_v0.yaml`
- **BOM available:** No
