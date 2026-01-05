# Fix Intelligence: recipe_silica_purified_v0

## Files

- **Recipe:** `kb/recipes/recipe_silica_purified_v0.yaml`
- **Target item:** `silica_purified`
  - File: `kb/items/silica_purified.yaml`
- **BOM:** None
- **Steps:** 4 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'mineral_processing_basic_v0') requires input 'regolith_lunar_mare' which is not available

**Location:** Step 0
**Process:** `mineral_processing_basic_v0`
  - File: `kb/processes/mineral_processing_basic_v0.yaml`

**Current step:**
```yaml
- process_id: mineral_processing_basic_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'drying_and_curing_v0') requires input 'wet_material' which is not available

**Location:** Step 2
**Process:** `drying_and_curing_v0`
  - File: `kb/processes/drying_and_curing_v0.yaml`

**Current step:**
```yaml
- process_id: drying_and_curing_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'inspection_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
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

- Step 0 produces: `concentrated_mineral` (0.3 kg)
- Step 0 produces: `tailings` (0.7 kg)
- Step 1 produces: `silica_purified` (0.28 kg)
- Step 1 produces: `tailings` (0.02 kg)
- Step 2 produces: `dried_material` (1.0 kg)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_silica_purified_v0.yaml`
- **BOM available:** No
