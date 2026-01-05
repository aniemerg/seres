# Fix Intelligence: recipe_green_ceramic_part_v0

## Files

- **Recipe:** `kb/recipes/recipe_green_ceramic_part_v0.yaml`
- **Target item:** `green_ceramic_part`
  - File: `kb/items/green_ceramic_part.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (3 found)

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

**Message:** Step 2 uses template process 'inspection_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
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

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_green_ceramic_part_v0.yaml`
- **BOM available:** No
