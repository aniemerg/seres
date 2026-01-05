# Fix Intelligence: recipe_green_ceramic_parts_v0

## Files

- **Recipe:** `kb/recipes/recipe_green_ceramic_parts_v0.yaml`
- **Target item:** `green_ceramic_parts`
  - File: `kb/items/green_ceramic_parts.yaml`
- **BOM:** None
- **Steps:** 2 total

## Errors (2 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'powder_processing_v0') requires input 'powder_metal_or_ceramic' which is not available

**Location:** Step 0
**Process:** `powder_processing_v0`
  - File: `kb/processes/powder_processing_v0.yaml`

**Current step:**
```yaml
- process_id: powder_processing_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'pressing_operations_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `pressing_operations_basic_v0`
  - File: `kb/processes/pressing_operations_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: pressing_operations_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `processed_powder_mixture` (1.0 kg)

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_green_ceramic_parts_v0.yaml`
- **BOM available:** No
