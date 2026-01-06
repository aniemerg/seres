# Fix Intelligence: recipe_fused_silica_v0

## Files

- **Recipe:** `kb/recipes/recipe_fused_silica_v0.yaml`
- **Target item:** `fused_silica`
  - File: `kb/items/fused_silica.yaml`
- **BOM:** None
- **Steps:** 2 total

## Errors (2 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'fused_silica_production_v0') requires input 'silica_purified' which is not available

**Location:** Step 0
**Process:** `fused_silica_production_v0`
  - File: `kb/processes/fused_silica_production_v0.yaml`

**Current step:**
```yaml
- process_id: fused_silica_production_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'inspection_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
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

- Step 0 produces: `fused_silica` (9.0 kg)

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_fused_silica_v0.yaml`
- **BOM available:** No
