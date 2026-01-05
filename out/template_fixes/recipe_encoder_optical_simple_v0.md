# Fix Intelligence: recipe_encoder_optical_simple_v0

## Files

- **Recipe:** `kb/recipes/recipe_encoder_optical_simple_v0.yaml`
- **Target item:** `encoder_optical_simple_v0`
  - File: `kb/items/encoder_optical_simple_v0.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (2 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'pcb_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `pcb_assembly_basic_v0`
  - File: `kb/processes/pcb_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: pcb_assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_template_missing_step_inputs

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

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_encoder_optical_simple_v0.yaml`
- **BOM available:** No
