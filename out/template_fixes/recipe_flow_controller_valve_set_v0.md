# Fix Intelligence: recipe_flow_controller_valve_set_v0

## Files

- **Recipe:** `kb/recipes/recipe_flow_controller_valve_set_v0.yaml`
- **Target item:** `flow_controller_valve_set`
  - File: `kb/items/flow_controller_valve_set.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'flow_controller_valve_set_assembly_v0') requires input 'valve_body_machined' which is not available

**Location:** Step 0
**Process:** `flow_controller_valve_set_assembly_v0`
  - File: `kb/processes/flow_controller_valve_set_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: flow_controller_valve_set_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'calibration_and_test_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `calibration_and_test_basic_v0`
  - File: `kb/processes/calibration_and_test_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: calibration_and_test_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `flow_controller_valve_set` (1.0 unit)

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'leak_testing_v0') requires input 'welded_assemblies' which is not available

**Location:** Step 2
**Process:** `leak_testing_v0`
  - File: `kb/processes/leak_testing_v0.yaml`

**Current step:**
```yaml
- process_id: leak_testing_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_flow_controller_valve_set_v0.yaml`
- **BOM available:** No
