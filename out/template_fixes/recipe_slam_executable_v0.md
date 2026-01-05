# Fix Intelligence: recipe_slam_executable_v0

## Files

- **Recipe:** `kb/recipes/recipe_slam_executable_v0.yaml`
- **Target item:** `slam_executable`
  - File: `kb/items/slam_executable.yaml`
- **BOM:** None
- **Steps:** 2 total

## Errors (2 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'software_development_programming_v0') requires input 'slam_code_uncompiled' which is not available

**Location:** Step 0
**Process:** `software_development_programming_v0`
  - File: `kb/processes/software_development_programming_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: software_development_programming_v0
  inputs:
  - item_id: slam_code_uncompiled
    qty: 1.0
    unit: each
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `slam_code_uncompiled` not found

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

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_slam_executable_v0.yaml`
- **BOM available:** No
