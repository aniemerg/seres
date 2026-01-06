# Fix Intelligence: recipe_formation_wiring_harness_import_v0

## Files

- **Recipe:** `kb/recipes/recipe_formation_wiring_harness_import_v0.yaml`
- **Target item:** `formation_wiring_harness`
  - File: `kb/items/formation_wiring_harness.yaml`
- **BOM:** None
- **Steps:** 4 total

## Errors (4 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'wire_cutting_and_stripping_v0') requires input 'magnet_wire_copper' which is not available

**Location:** Step 0
**Process:** `wire_cutting_and_stripping_v0`
  - File: `kb/processes/wire_cutting_and_stripping_v0.yaml`

**Current step:**
```yaml
- process_id: wire_cutting_and_stripping_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'crimping_and_termination_v0') requires input 'electrical_wire_and_connectors' which is not available

**Location:** Step 1
**Process:** `crimping_and_termination_v0`
  - File: `kb/processes/crimping_and_termination_v0.yaml`

**Current step:**
```yaml
- process_id: crimping_and_termination_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'cable_harness_assembly_v0') requires input 'electrical_wire_and_connectors' which is not available

**Location:** Step 2
**Process:** `cable_harness_assembly_v0`
  - File: `kb/processes/cable_harness_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: cable_harness_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

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
- **Recipe file:** `kb/recipes/recipe_formation_wiring_harness_import_v0.yaml`
- **BOM available:** No
