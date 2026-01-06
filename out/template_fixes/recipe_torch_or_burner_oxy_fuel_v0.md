# Fix Intelligence: recipe_torch_or_burner_oxy_fuel_v0

## Files

- **Recipe:** `kb/recipes/recipe_torch_or_burner_oxy_fuel_v0.yaml`
- **Target item:** `torch_or_burner_oxy_fuel`
  - File: `kb/items/torch_or_burner_oxy_fuel.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (3 found)

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

**Message:** Step 1 (process 'machining_process_drilling_v0') requires input 'center_insulator_ceramic' which is not available

**Location:** Step 1
**Process:** `machining_process_drilling_v0`
  - File: `kb/processes/machining_process_drilling_v0.yaml`

**Current step:**
```yaml
- process_id: machining_process_drilling_v0
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

- Step 0 produces: `machined_steel_part_precision` (0.075 kg)
- Step 1 produces: `insulator_drilled` (0.075 kg)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_torch_or_burner_oxy_fuel_v0.yaml`
- **BOM available:** No
