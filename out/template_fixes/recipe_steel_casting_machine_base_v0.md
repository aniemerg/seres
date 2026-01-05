# Fix Intelligence: recipe_steel_casting_machine_base_v0

## Files

- **Recipe:** `kb/recipes/recipe_steel_casting_machine_base_v0.yaml`
- **Target item:** `steel_casting_machine_base`
  - File: `kb/items/steel_casting_machine_base.yaml`
- **BOM:** None
- **Steps:** 5 total

## Errors (5 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'melting_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `melting_basic_v0`
  - File: `kb/processes/melting_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: melting_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'casting_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `casting_basic_v0`
  - File: `kb/processes/casting_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: casting_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `molten_material_or_preform` (1.0 kg)

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'cooling_solidification_v0') requires input 'molten_material_or_preform' which is not available

**Location:** Step 2
**Process:** `cooling_solidification_v0`
  - File: `kb/processes/cooling_solidification_v0.yaml`

**Current step:**
```yaml
- process_id: cooling_solidification_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'shakeout_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
**Process:** `shakeout_basic_v0`
  - File: `kb/processes/shakeout_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: shakeout_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `molten_material_or_preform` (1.0 kg)
- Step 2 produces: `solidified_casting` (5.0 kg)

---

### Error 5: recipe_template_missing_step_inputs

**Message:** Step 4 uses template process 'machining_finish_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 4
**Process:** `machining_finish_basic_v0`
  - File: `kb/processes/machining_finish_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_finish_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `molten_material_or_preform` (1.0 kg)
- Step 2 produces: `solidified_casting` (5.0 kg)

---

## Summary

- **Total errors:** 5
- **Recipe file:** `kb/recipes/recipe_steel_casting_machine_base_v0.yaml`
- **BOM available:** No
