# Fix Intelligence: recipe_basic_fabrication_station_v1

## Files

- **Recipe:** `kb/recipes/recipe_basic_fabrication_station_v1.yaml`
- **Target item:** `basic_fabrication_station`
  - File: `kb/items/basic_fabrication_station.yaml`
- **BOM:** None
- **Steps:** 6 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_basic_fabrication_station_v0` → basic_fabrication_station_v0 (6 steps)

## Errors (6 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'metal_fabrication_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `metal_fabrication_basic_v0`
  - File: `kb/processes/metal_fabrication_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: metal_fabrication_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'frame_fabrication_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `frame_fabrication_basic_v0`
  - File: `kb/processes/frame_fabrication_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: frame_fabrication_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'bearing_installation_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `bearing_installation_basic_v0`
  - File: `kb/processes/bearing_installation_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: bearing_installation_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 1 produces: `structural_frame_medium` (1.0 unit)

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'machine_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
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

- Step 1 produces: `structural_frame_medium` (1.0 unit)
- Step 2 produces: `finished_part` (2.0 kg)

---

### Error 5: recipe_template_missing_step_inputs

**Message:** Step 4 uses template process 'electrical_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 4
**Process:** `electrical_assembly_basic_v0`
  - File: `kb/processes/electrical_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: electrical_assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 1 produces: `structural_frame_medium` (1.0 unit)
- Step 2 produces: `finished_part` (2.0 kg)
- Step 3 produces: `analog_test_bench_neural_circuits_v0` (1.0 unit)

---

### Error 6: recipe_template_missing_step_inputs

**Message:** Step 5 uses template process 'electrical_testing_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 5
**Process:** `electrical_testing_basic_v0`
  - File: `kb/processes/electrical_testing_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: electrical_testing_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 1 produces: `structural_frame_medium` (1.0 unit)
- Step 2 produces: `finished_part` (2.0 kg)
- Step 3 produces: `analog_test_bench_neural_circuits_v0` (1.0 unit)

---

## Summary

- **Total errors:** 6
- **Recipe file:** `kb/recipes/recipe_basic_fabrication_station_v1.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
