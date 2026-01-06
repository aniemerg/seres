# Fix Intelligence: recipe_solenoid_coil_assembly_v0

## Files

- **Recipe:** `kb/recipes/recipe_solenoid_coil_assembly_v0.yaml`
- **Target item:** `solenoid_coil_assembly`
  - File: `kb/items/solenoid_coil_assembly.yaml`
- **BOM:** None
- **Steps:** 2 total

## Errors (2 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'wire_winding_process_v0') requires input 'copper_wire_magnet' which is not available

**Location:** Step 0
**Process:** `wire_winding_process_v0`
  - File: `kb/processes/wire_winding_process_v0.yaml`

**Current step:**
```yaml
- process_id: wire_winding_process_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
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

- Step 0 produces: `relay_coil_assembly` (0.05 kg)

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_solenoid_coil_assembly_v0.yaml`
- **BOM available:** No
