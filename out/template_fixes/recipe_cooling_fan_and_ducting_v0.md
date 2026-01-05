# Fix Intelligence: recipe_cooling_fan_and_ducting_v0

## Files

- **Recipe:** `kb/recipes/recipe_cooling_fan_and_ducting_v0.yaml`
- **Target item:** `cooling_fan_and_ducting`
  - File: `kb/items/cooling_fan_and_ducting.yaml`
- **BOM:** None
- **Steps:** 2 total

## Errors (2 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'machining_finish_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `machining_finish_basic_v0`
  - File: `kb/processes/machining_finish_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_finish_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'assembly_basic_v0') requires input 'cooling_fan_assembly' which is not available

**Location:** Step 1
**Process:** `assembly_basic_v0`
  - File: `kb/processes/assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: cooling_fan_assembly
    qty: 1.0
    unit: unit
  - item_id: sheet_metal_or_structural_steel
    qty: 5.0
    unit: kg
  - item_id: fastener_kit_small
    qty: 1.0
    unit: unit
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `cooling_fan_assembly` not found

This item doesn't exist in the KB.

#### Problem: Generic placeholder `sheet_metal_or_structural_steel`

This is not a real item. Need to replace with specific item.

**Specific items matching pattern:**

- `sheet_metal_or_structural_steel`
- `steel_chassis_sheet_metal`
- `formed_sheet_metal_parts`
- `structural_steel_frame`

#### Problem: Item `fastener_kit_small` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_cooling_fan_and_ducting_v0.yaml`
- **BOM available:** No
