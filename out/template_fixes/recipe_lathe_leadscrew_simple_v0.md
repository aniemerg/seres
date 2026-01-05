# Fix Intelligence: recipe_lathe_leadscrew_simple_v0

## Files

- **Recipe:** `kb/recipes/recipe_lathe_leadscrew_simple_v0.yaml`
- **Target item:** `lathe_leadscrew_simple`
  - File: `kb/items/lathe_leadscrew_simple.yaml`
- **BOM:** None
- **Steps:** 4 total

## Errors (4 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'machining_process_turning_v0') requires input 'rough_part' which is not available

**Location:** Step 0
**Process:** `machining_process_turning_v0`
  - File: `kb/processes/machining_process_turning_v0.yaml`

**Current step:**
```yaml
- process_id: machining_process_turning_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'lead_screw_fabrication_v0') requires input 'steel_bar_stock' which is not available

**Location:** Step 1
**Process:** `lead_screw_fabrication_v0`
  - File: `kb/processes/lead_screw_fabrication_v0.yaml`

**Current step:**
```yaml
- process_id: lead_screw_fabrication_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'precision_grinding_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `precision_grinding_basic_v0`
  - File: `kb/processes/precision_grinding_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: precision_grinding_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `machined_steel_part_precision` (0.075 kg)
- Step 1 produces: `lead_screw_assembly` (1.0 unit)

---

### Error 4: recipe_step_input_not_satisfied

**Message:** Step 3 (process 'heat_treatment_hardening_v0') requires input 'bearing_rings_machined' which is not available

**Location:** Step 3
**Process:** `heat_treatment_hardening_v0`
  - File: `kb/processes/heat_treatment_hardening_v0.yaml`

**Current step:**
```yaml
- process_id: heat_treatment_hardening_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_lathe_leadscrew_simple_v0.yaml`
- **BOM available:** No
