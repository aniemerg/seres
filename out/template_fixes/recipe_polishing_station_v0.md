# Fix Intelligence: recipe_polishing_station_v0

## Files

- **Recipe:** `kb/recipes/recipe_polishing_station_v0.yaml`
- **Target item:** `polishing_station`
  - File: `kb/items/polishing_station.yaml`
- **BOM:** None
- **Steps:** 4 total

## Errors (4 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'welding_and_fabrication_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `welding_and_fabrication_v0`
  - File: `kb/processes/welding_and_fabrication_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: welding_and_fabrication_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

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

- Step 0 produces: `welded_fabrications` (9.5 kg)

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'electrical_wiring_and_controls_v0') requires input 'electrical_wire_and_connectors' which is not available

**Location:** Step 2
**Process:** `electrical_wiring_and_controls_v0`
  - File: `kb/processes/electrical_wiring_and_controls_v0.yaml`

**Current step:**
```yaml
- process_id: electrical_wiring_and_controls_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'alignment_and_testing_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
**Process:** `alignment_and_testing_basic_v0`
  - File: `kb/processes/alignment_and_testing_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: alignment_and_testing_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `welded_fabrications` (9.5 kg)
- Step 1 produces: `assembled_equipment` (1.0 kg)
- Step 2 produces: `wired_electrical_system` (1.0 unit)

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_polishing_station_v0.yaml`
- **BOM available:** No
