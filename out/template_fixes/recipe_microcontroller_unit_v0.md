# Fix Intelligence: recipe_microcontroller_unit_v0

## Files

- **Recipe:** `kb/recipes/recipe_microcontroller_unit_v0.yaml`
- **Target item:** `microcontroller_unit_v0`
  - File: `kb/items/microcontroller_unit_v0.yaml`
- **BOM:** None
- **Steps:** 4 total

## Errors (4 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'microcontroller_ic_generic_fabrication_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `microcontroller_ic_generic_fabrication_v0`
  - File: `kb/processes/microcontroller_ic_generic_fabrication_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: microcontroller_ic_generic_fabrication_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'pcb_fabrication_v0') requires input 'copper_clad_laminate' which is not available

**Location:** Step 1
**Process:** `pcb_fabrication_v0`
  - File: `kb/processes/pcb_fabrication_v0.yaml`

**Current step:**
```yaml
- process_id: pcb_fabrication_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'pcb_assembly_v0') requires input 'pcb_bare_board' which is not available

**Location:** Step 2
**Process:** `pcb_assembly_v0`
  - File: `kb/processes/pcb_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: pcb_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 4: recipe_step_input_not_satisfied

**Message:** Step 3 (process 'microcontroller_unit_assembly_v0') requires input 'microcontroller_ic_generic' which is not available

**Location:** Step 3
**Process:** `microcontroller_unit_assembly_v0`
  - File: `kb/processes/microcontroller_unit_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: microcontroller_unit_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_microcontroller_unit_v0.yaml`
- **BOM available:** No
