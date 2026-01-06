# Fix Intelligence: recipe_path_planning_algorithm_v0

## Files

- **Recipe:** `kb/recipes/recipe_path_planning_algorithm_v0.yaml`
- **Target item:** `path_planning_algorithm_v0`
  - File: `kb/items/path_planning_algorithm_v0.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (3 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'software_development_programming_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `software_development_programming_v0`
  - File: `kb/processes/software_development_programming_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: software_development_programming_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'software_compilation_v0') requires input 'path_planning_code_uncompiled' which is not available

**Location:** Step 1
**Process:** `software_compilation_v0`
  - File: `kb/processes/software_compilation_v0.yaml`

**Current step:**
```yaml
- process_id: software_compilation_v0
  inputs:
  - item_id: path_planning_code_uncompiled
    qty: 1.0
    unit: unit
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `path_planning_code_uncompiled` not found

This item doesn't exist in the KB.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'software_testing_simulation_v0') requires input 'path_planning_executable' which is not available

**Location:** Step 2
**Process:** `software_testing_simulation_v0`
  - File: `kb/processes/software_testing_simulation_v0.yaml`

**Current step:**
```yaml
- process_id: software_testing_simulation_v0
  inputs:
  - item_id: path_planning_executable
    qty: 1.0
    unit: unit
  - item_id: sensor_data_test_set
    qty: 1.0
    unit: unit
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `path_planning_executable` not found

This item doesn't exist in the KB.

#### Problem: Item `sensor_data_test_set` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_path_planning_algorithm_v0.yaml`
- **BOM available:** No
