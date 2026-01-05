# Fix Intelligence: recipe_fastener_kit_large_v0

## Files

- **Recipe:** `kb/recipes/recipe_fastener_kit_large_v0.yaml`
- **Target item:** `fastener_kit_large_v0`
  - File: `kb/items/fastener_kit_large_v0.yaml`
- **BOM:** `kb/boms/bom_fastener_kit_large_v0.yaml` ✓
  - Components: 4
- **Steps:** 4 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_fastener_kit_large_v1` → fastener_kit_large (4 steps)

## Errors (4 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'metal_casting_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `metal_casting_basic_v0`
  - File: `kb/processes/metal_casting_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: metal_casting_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 4 components:

- `bolt_hex_medium_steel` (qty: 1.44 kg)
- `nut_hex_medium_steel` (qty: 0.28 kg)
- `washer_flat_medium_steel` (qty: 0.18 kg)
- `washer_lock_medium_steel` (qty: 0.14 kg)

Suggested fix:
```yaml
- process_id: metal_casting_basic_v0
  inputs:
  - item_id: bolt_hex_medium_steel
    qty: 1.44
    unit: kg
  - item_id: nut_hex_medium_steel
    qty: 0.28
    unit: kg
  - item_id: washer_flat_medium_steel
    qty: 0.18
    unit: kg
  - item_id: washer_lock_medium_steel
    qty: 0.14
    unit: kg
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

BOM has 4 components:

- `bolt_hex_medium_steel` (qty: 1.44 kg)
- `nut_hex_medium_steel` (qty: 0.28 kg)
- `washer_flat_medium_steel` (qty: 0.18 kg)
- `washer_lock_medium_steel` (qty: 0.14 kg)

Suggested fix:
```yaml
- process_id: machining_finish_basic_v0
  inputs:
  - item_id: bolt_hex_medium_steel
    qty: 1.44
    unit: kg
  - item_id: nut_hex_medium_steel
    qty: 0.28
    unit: kg
  - item_id: washer_flat_medium_steel
    qty: 0.18
    unit: kg
  - item_id: washer_lock_medium_steel
    qty: 0.14
    unit: kg
```

#### Option B: Use previous step outputs

- Step 0 produces: `cast_metal_parts` (0.95 kg)

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'heat_treat_basic_v0') requires input 'machined_part_raw' which is not available

**Location:** Step 2
**Process:** `heat_treat_basic_v0`
  - File: `kb/processes/heat_treat_basic_v0.yaml`

**Current step:**
```yaml
- process_id: heat_treat_basic_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
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

BOM has 4 components:

- `bolt_hex_medium_steel` (qty: 1.44 kg)
- `nut_hex_medium_steel` (qty: 0.28 kg)
- `washer_flat_medium_steel` (qty: 0.18 kg)
- `washer_lock_medium_steel` (qty: 0.14 kg)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: bolt_hex_medium_steel
    qty: 1.44
    unit: kg
  - item_id: nut_hex_medium_steel
    qty: 0.28
    unit: kg
  - item_id: washer_flat_medium_steel
    qty: 0.18
    unit: kg
  - item_id: washer_lock_medium_steel
    qty: 0.14
    unit: kg
```

#### Option B: Use previous step outputs

- Step 0 produces: `cast_metal_parts` (0.95 kg)
- Step 1 produces: `machined_part_raw` (1.0 kg)
- Step 2 produces: `machined_part_raw` (1.0 kg)

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_fastener_kit_large_v0.yaml`
- **BOM available:** Yes (4 components)
- **Similar recipes:** 1 found
