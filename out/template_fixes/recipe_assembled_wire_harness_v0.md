# Fix Intelligence: recipe_assembled_wire_harness_v0

## Files

- **Recipe:** `kb/recipes/recipe_assembled_wire_harness_v0.yaml`
- **Target item:** `assembled_wire_harness`
  - File: `kb/items/assembled_wire_harness.yaml`
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

- Step 0 produces: `cut_wire_lengths` (1.0 kg)
- Step 1 produces: `assembled_wire_harness` (1.0 unit)

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'inspection_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
**Process:** `inspection_basic_v0`
  - File: `kb/processes/inspection_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: inspection_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `cut_wire_lengths` (1.0 kg)
- Step 1 produces: `assembled_wire_harness` (1.0 unit)
- Step 2 produces: `assembled_equipment` (1.0 kg)

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_assembled_wire_harness_v0.yaml`
- **BOM available:** No
