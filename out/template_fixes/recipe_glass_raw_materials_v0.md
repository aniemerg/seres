# Fix Intelligence: recipe_glass_raw_materials_v0

## Files

- **Recipe:** `kb/recipes/recipe_glass_raw_materials_v0.yaml`
- **Target item:** `glass_raw_materials`
  - File: `kb/items/glass_raw_materials.yaml`
- **BOM:** None
- **Steps:** 4 total

## Errors (4 found)

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

**Message:** Step 1 (process 'crushing_and_grinding_v0') requires input 'mineral_ore_sulfide' which is not available

**Location:** Step 1
**Process:** `crushing_and_grinding_v0`
  - File: `kb/processes/crushing_and_grinding_v0.yaml`

**Current step:**
```yaml
- process_id: crushing_and_grinding_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'mixing_basic_v0') requires input 'silica_purified' which is not available

**Location:** Step 2
**Process:** `mixing_basic_v0`
  - File: `kb/processes/mixing_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: mixing_basic_v0
  inputs:
  - item_id: silica_purified
    qty: 0.7
    unit: kg
  - item_id: sodium_carbonate
    qty: 0.2
    unit: kg
  - item_id: calcium_carbonate
    qty: 0.1
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `silica_purified` not found

This item doesn't exist in the KB.

#### Problem: Item `sodium_carbonate` not found

This item doesn't exist in the KB.

#### Problem: Item `calcium_carbonate` not found

This item doesn't exist in the KB.

---

### Error 4: recipe_template_missing_step_inputs

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
- Step 1 produces: `crushed_ore` (1.0 kg)
- Step 2 produces: `glass_raw_materials` (1.0 kg)

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_glass_raw_materials_v0.yaml`
- **BOM available:** No
