# Fix Intelligence: recipe_slam_algorithm_implementation_v0

## Files

- **Recipe:** `kb/recipes/recipe_slam_algorithm_implementation_v0.yaml`
- **Target item:** `slam_algorithm_implementation_v0`
  - File: `kb/items/slam_algorithm_implementation_v0.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'software_development_programming_v0') requires input 'computing_time_development' which is not available

**Location:** Step 0
**Process:** `software_development_programming_v0`
  - File: `kb/processes/software_development_programming_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: software_development_programming_v0
  inputs:
  - item_id: computing_time_development
    qty: 100.0
    unit: hr
  - item_id: software_source_code_v0
    qty: 1.0
    unit: each
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `computing_time_development` not found

This item doesn't exist in the KB.

#### Problem: Item `software_source_code_v0` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'software_compilation_v0') requires input 'slam_code_uncompiled' which is not available

**Location:** Step 1
**Process:** `software_compilation_v0`
  - File: `kb/processes/software_compilation_v0.yaml`

**Current step:**
```yaml
- process_id: software_compilation_v0
  inputs:
  - item_id: slam_code_uncompiled
    qty: 1.0
    unit: each
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `slam_code_uncompiled` not found

This item doesn't exist in the KB.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'software_testing_simulation_v0') requires input 'sensor_data_test_set' which is not available

**Location:** Step 2
**Process:** `software_testing_simulation_v0`
  - File: `kb/processes/software_testing_simulation_v0.yaml`

**Current step:**
```yaml
- process_id: software_testing_simulation_v0
  inputs:
  - item_id: slam_executable
    qty: 1.0
    unit: each
  - item_id: sensor_data_test_set
    qty: 1.0
    unit: each
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `slam_executable` not found

This item doesn't exist in the KB.

#### Problem: Item `sensor_data_test_set` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_slam_algorithm_implementation_v0.yaml`
- **BOM available:** No
