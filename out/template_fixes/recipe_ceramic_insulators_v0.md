# Fix Intelligence: recipe_ceramic_insulators_v0

## Files

- **Recipe:** `kb/recipes/recipe_ceramic_insulators_v0.yaml`
- **Target item:** `ceramic_insulators`
  - File: `kb/items/ceramic_insulators.yaml`
- **BOM:** None
- **Steps:** 5 total

## Errors (4 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'ceramic_forming_v0') requires input 'ceramic_powder_mixture' which is not available

**Location:** Step 0
**Process:** `ceramic_forming_v0`
  - File: `kb/processes/ceramic_forming_v0.yaml`

**Current step:**
```yaml
- process_id: ceramic_forming_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'drying_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `drying_basic_v0`
  - File: `kb/processes/drying_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: drying_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `green_ceramic_part` (5.0 kg)

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'surface_finishing_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
**Process:** `surface_finishing_basic_v0`
  - File: `kb/processes/surface_finishing_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: surface_finishing_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `green_ceramic_part` (5.0 kg)
- Step 1 produces: `dried_material` (1.0 kg)

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 4 uses template process 'inspection_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 4
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

- Step 0 produces: `green_ceramic_part` (5.0 kg)
- Step 1 produces: `dried_material` (1.0 kg)
- Step 3 produces: `finished_part` (0.95 kg)

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_ceramic_insulators_v0.yaml`
- **BOM available:** No
