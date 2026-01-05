# Fix Intelligence: recipe_microstructure_analysis_system_v0_v0

## Files

- **Recipe:** `kb/recipes/recipe_microstructure_analysis_system_v0_v0.yaml`
- **Target item:** `microstructure_analysis_system_v0`
  - File: `kb/items/microstructure_analysis_system_v0.yaml`
- **BOM:** None
- **Steps:** 4 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_microstructure_analysis_system_v0_v1` → microstructure_analysis_system_v0 (4 steps)

## Errors (4 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'machine_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `machine_assembly_basic_v0`
  - File: `kb/processes/machine_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machine_assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option C: Pattern from `recipe_microstructure_analysis_system_v0_v1`

Similar recipe uses this process (step 0) with:

```yaml
  inputs:
  - item_id: optical_microscope_v0
    qty: 1.0
    unit: unit
  - item_id: computer_workstation
    qty: 1.0
    unit: unit
  - item_id: lab
    qty: 1.0
    unit: unit
```

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'enclosure_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `enclosure_assembly_basic_v0`
  - File: `kb/processes/enclosure_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: enclosure_assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `analog_test_bench_neural_circuits_v0` (1.0 unit)

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'electronic_assembly_v0') requires input 'pcb_populated' which is not available

**Location:** Step 2
**Process:** `electronic_assembly_v0`
  - File: `kb/processes/electronic_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: electronic_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 4: recipe_step_input_not_satisfied

**Message:** Step 3 (process 'electrical_wiring_assembly_v0') requires input 'sensor_element_with_gauges' which is not available

**Location:** Step 3
**Process:** `electrical_wiring_assembly_v0`
  - File: `kb/processes/electrical_wiring_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: electrical_wiring_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_microstructure_analysis_system_v0_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
