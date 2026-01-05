# Fix Intelligence: recipe_magnetic_core_memory_array_v0

## Files

- **Recipe:** `kb/recipes/recipe_magnetic_core_memory_array_v0.yaml`
- **Target item:** `magnetic_core_memory_array_v0`
  - File: `kb/items/magnetic_core_memory_array_v0.yaml`
- **BOM:** None
- **Steps:** 4 total

## Errors (4 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'ferrite_toroid_sintering_v0') requires input 'powder_metal_or_ceramic' which is not available

**Location:** Step 0
**Process:** `ferrite_toroid_sintering_v0`
  - File: `kb/processes/ferrite_toroid_sintering_v0.yaml`

**Current step:**
```yaml
- process_id: ferrite_toroid_sintering_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'core_memory_threading_machine_v0') requires input 'ferrite_toroid_core_v0' which is not available

**Location:** Step 1
**Process:** `core_memory_threading_machine_v0`
  - File: `kb/processes/core_memory_threading_machine_v0.yaml`

**Current step:**
```yaml
- process_id: core_memory_threading_machine_v0
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

- Step 0 produces: `powder_metal_or_ceramic` (1.0 kg)
- Step 1 produces: `ferrite_toroid_core_v0` (1.0 kg)

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
- **Recipe file:** `kb/recipes/recipe_magnetic_core_memory_array_v0.yaml`
- **BOM available:** No
