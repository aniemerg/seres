# Fix Intelligence: recipe_path_planning_executable_v0

## Files

- **Recipe:** `kb/recipes/recipe_path_planning_executable_v0.yaml`
- **Target item:** `path_planning_executable`
  - File: `kb/items/path_planning_executable.yaml`
- **BOM:** None
- **Steps:** 2 total

## Errors (2 found)

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

**Message:** Step 1 (process 'software_compilation_v0') requires input 'slam_code_uncompiled' which is not available

**Location:** Step 1
**Process:** `software_compilation_v0`
  - File: `kb/processes/software_compilation_v0.yaml`

**Current step:**
```yaml
- process_id: software_compilation_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_path_planning_executable_v0.yaml`
- **BOM available:** No
