# Fix Intelligence: recipe_cryocooler_core_unit_v0_v0

## Files

- **Recipe:** `kb/recipes/recipe_cryocooler_core_unit_v0_v0.yaml`
- **Target item:** `cryocooler_core_unit_v0`
  - File: `kb/items/cryocooler_core_unit_v0.yaml`
- **BOM:** None
- **Steps:** 2 total

## Errors (2 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'machining_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `machining_basic_v0`
  - File: `kb/processes/machining_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'cryocooler_core_unit_assembly_v0') requires input 'machined_metal_block_v0' which is not available

**Location:** Step 1
**Process:** `cryocooler_core_unit_assembly_v0`
  - File: `kb/processes/cryocooler_core_unit_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: cryocooler_core_unit_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_cryocooler_core_unit_v0_v0.yaml`
- **BOM available:** No
