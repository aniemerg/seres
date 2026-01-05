# Fix Intelligence: recipe_robot_arm_6dof_v0

## Files

- **Recipe:** `kb/recipes/recipe_robot_arm_6dof_v0.yaml`
- **Target item:** `robot_arm_6dof_v0`
  - File: `kb/items/robot_arm_6dof_v0.yaml`
- **BOM:** None
- **Steps:** 5 total

## Errors (5 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'metal_cutting_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `metal_cutting_basic_v0`
  - File: `kb/processes/metal_cutting_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: metal_cutting_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'machining_finish_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `machining_finish_basic_v0`
  - File: `kb/processes/machining_finish_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_finish_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'finishing_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `finishing_basic_v0`
  - File: `kb/processes/finishing_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: finishing_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 1 produces: `machined_part_raw` (1.0 kg)

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
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

- Step 1 produces: `machined_part_raw` (1.0 kg)
- Step 2 produces: `finished_part` (1.0 unit)

---

### Error 5: recipe_template_missing_step_inputs

**Message:** Step 4 uses template process 'machine_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 4
**Process:** `machine_assembly_basic_v0`
  - File: `kb/processes/machine_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machine_assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 1 produces: `machined_part_raw` (1.0 kg)
- Step 2 produces: `finished_part` (1.0 unit)
- Step 3 produces: `assembled_equipment` (1.0 kg)

---

## Summary

- **Total errors:** 5
- **Recipe file:** `kb/recipes/recipe_robot_arm_6dof_v0.yaml`
- **BOM available:** No
