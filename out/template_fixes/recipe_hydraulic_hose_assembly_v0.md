# Fix Intelligence: recipe_hydraulic_hose_assembly_v0

## Files

- **Recipe:** `kb/recipes/recipe_hydraulic_hose_assembly_v0.yaml`
- **Target item:** `hydraulic_hose_assembly`
  - File: `kb/items/hydraulic_hose_assembly.yaml`
- **BOM:** None
- **Steps:** 4 total

## Errors (3 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'cutting_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `cutting_basic_v0`
  - File: `kb/processes/cutting_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: cutting_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'hose_crimping_v0') requires input 'hydraulic_hose_segment_v0' which is not available

**Location:** Step 1
**Process:** `hose_crimping_v0`
  - File: `kb/processes/hose_crimping_v0.yaml`

**Current step:**
```yaml
- process_id: hose_crimping_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 3: recipe_template_missing_step_inputs

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

- Step 0 produces: `cut_parts` (9.5 kg)
- Step 1 produces: `crimped_hydraulic_hose_v0` (1.0 unit)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_hydraulic_hose_assembly_v0.yaml`
- **BOM available:** No
