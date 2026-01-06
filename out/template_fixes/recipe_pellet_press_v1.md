# Fix Intelligence: recipe_pellet_press_v1

## Files

- **Recipe:** `kb/recipes/recipe_pellet_press_v1.yaml`
- **Target item:** `pellet_press`
  - File: `kb/items/pellet_press.yaml`
- **BOM:** `kb/boms/bom_pellet_press.yaml` ✓
  - Components: 3
- **Steps:** 3 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_pellet_press_v0` → pellet_press (3 steps)

## Errors (3 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `assembly_basic_v0`
  - File: `kb/processes/assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 3 components:

- `steel_ingot` (qty: 8.0 None)
- `steel_plate_or_sheet` (qty: 4.0 None)
- `steel_sheet_1mm` (qty: 12.0 None)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: steel_ingot
    qty: 8.0
    unit: None
  - item_id: steel_plate_or_sheet
    qty: 4.0
    unit: None
  - item_id: steel_sheet_1mm
    qty: 12.0
    unit: None
```

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'machining_finish_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `machining_finish_basic_v0`
  - File: `kb/processes/machining_finish_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_finish_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 3 components:

- `steel_ingot` (qty: 8.0 None)
- `steel_plate_or_sheet` (qty: 4.0 None)
- `steel_sheet_1mm` (qty: 12.0 None)

Suggested fix:
```yaml
- process_id: machining_finish_basic_v0
  inputs:
  - item_id: steel_ingot
    qty: 8.0
    unit: None
  - item_id: steel_plate_or_sheet
    qty: 4.0
    unit: None
  - item_id: steel_sheet_1mm
    qty: 12.0
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `assembled_equipment` (1.0 kg)

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'welding_brazing_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `welding_brazing_basic_v0`
  - File: `kb/processes/welding_brazing_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: welding_brazing_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 3 components:

- `steel_ingot` (qty: 8.0 None)
- `steel_plate_or_sheet` (qty: 4.0 None)
- `steel_sheet_1mm` (qty: 12.0 None)

Suggested fix:
```yaml
- process_id: welding_brazing_basic_v0
  inputs:
  - item_id: steel_ingot
    qty: 8.0
    unit: None
  - item_id: steel_plate_or_sheet
    qty: 4.0
    unit: None
  - item_id: steel_sheet_1mm
    qty: 12.0
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `assembled_equipment` (1.0 kg)
- Step 1 produces: `machined_part_raw` (1.0 kg)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_pellet_press_v1.yaml`
- **BOM available:** Yes (3 components)
- **Similar recipes:** 1 found
