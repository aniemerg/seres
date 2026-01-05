# Fix Intelligence: recipe_machine_drill_press_v0

## Files

- **Recipe:** `kb/recipes/recipe_machine_drill_press_v0.yaml`
- **Target item:** `drill_press_v0`
  - File: `kb/items/drill_press_v0.yaml`
- **BOM:** `kb/boms/bom_drill_press_v0.yaml` ✓
  - Components: 6
- **Steps:** 5 total

## Similar Recipes

Found 2 recipes producing similar items:

- `recipe_drill_press_v0` → drill_press (4 steps)
- `recipe_drill_press_v1` → drill_press (4 steps)

## Errors (5 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'casting_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `casting_basic_v0`
  - File: `kb/processes/casting_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: casting_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 6 components:

- `machine_column_cast` (qty: 1 unit)
- `spindle_head_basic` (qty: 1 unit)
- `motor_electric_small` (qty: 1 unit)
- `table_top_t_slot` (qty: 1 unit)
- `depth_stop_mechanism` (qty: 1 unit)
- `belt_and_pulley_set` (qty: 1 unit)

Suggested fix:
```yaml
- process_id: casting_basic_v0
  inputs:
  - item_id: machine_column_cast
    qty: 1
    unit: unit
  - item_id: spindle_head_basic
    qty: 1
    unit: unit
  - item_id: motor_electric_small
    qty: 1
    unit: unit
  - item_id: table_top_t_slot
    qty: 1
    unit: unit
  - item_id: depth_stop_mechanism
    qty: 1
    unit: unit
  - item_id: belt_and_pulley_set
    qty: 1
    unit: unit
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

BOM has 6 components:

- `machine_column_cast` (qty: 1 unit)
- `spindle_head_basic` (qty: 1 unit)
- `motor_electric_small` (qty: 1 unit)
- `table_top_t_slot` (qty: 1 unit)
- `depth_stop_mechanism` (qty: 1 unit)
- `belt_and_pulley_set` (qty: 1 unit)

Suggested fix:
```yaml
- process_id: machining_finish_basic_v0
  inputs:
  - item_id: machine_column_cast
    qty: 1
    unit: unit
  - item_id: spindle_head_basic
    qty: 1
    unit: unit
  - item_id: motor_electric_small
    qty: 1
    unit: unit
  - item_id: table_top_t_slot
    qty: 1
    unit: unit
  - item_id: depth_stop_mechanism
    qty: 1
    unit: unit
  - item_id: belt_and_pulley_set
    qty: 1
    unit: unit
```

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
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

BOM has 6 components:

- `machine_column_cast` (qty: 1 unit)
- `spindle_head_basic` (qty: 1 unit)
- `motor_electric_small` (qty: 1 unit)
- `table_top_t_slot` (qty: 1 unit)
- `depth_stop_mechanism` (qty: 1 unit)
- `belt_and_pulley_set` (qty: 1 unit)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: machine_column_cast
    qty: 1
    unit: unit
  - item_id: spindle_head_basic
    qty: 1
    unit: unit
  - item_id: motor_electric_small
    qty: 1
    unit: unit
  - item_id: table_top_t_slot
    qty: 1
    unit: unit
  - item_id: depth_stop_mechanism
    qty: 1
    unit: unit
  - item_id: belt_and_pulley_set
    qty: 1
    unit: unit
```

#### Option B: Use previous step outputs

- Step 1 produces: `machined_part_raw` (1.0 kg)

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'wiring_and_electronics_integration_v0' but doesn't provide step-level input overrides

**Location:** Step 3
**Process:** `wiring_and_electronics_integration_v0`
  - File: `kb/processes/wiring_and_electronics_integration_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: wiring_and_electronics_integration_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 6 components:

- `machine_column_cast` (qty: 1 unit)
- `spindle_head_basic` (qty: 1 unit)
- `motor_electric_small` (qty: 1 unit)
- `table_top_t_slot` (qty: 1 unit)
- `depth_stop_mechanism` (qty: 1 unit)
- `belt_and_pulley_set` (qty: 1 unit)

Suggested fix:
```yaml
- process_id: wiring_and_electronics_integration_v0
  inputs:
  - item_id: machine_column_cast
    qty: 1
    unit: unit
  - item_id: spindle_head_basic
    qty: 1
    unit: unit
  - item_id: motor_electric_small
    qty: 1
    unit: unit
  - item_id: table_top_t_slot
    qty: 1
    unit: unit
  - item_id: depth_stop_mechanism
    qty: 1
    unit: unit
  - item_id: belt_and_pulley_set
    qty: 1
    unit: unit
```

#### Option B: Use previous step outputs

- Step 1 produces: `machined_part_raw` (1.0 kg)
- Step 2 produces: `assembled_equipment` (1.0 kg)

---

### Error 5: recipe_template_missing_step_inputs

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

#### Option A: Use BOM components

BOM has 6 components:

- `machine_column_cast` (qty: 1 unit)
- `spindle_head_basic` (qty: 1 unit)
- `motor_electric_small` (qty: 1 unit)
- `table_top_t_slot` (qty: 1 unit)
- `depth_stop_mechanism` (qty: 1 unit)
- `belt_and_pulley_set` (qty: 1 unit)

Suggested fix:
```yaml
- process_id: inspection_basic_v0
  inputs:
  - item_id: machine_column_cast
    qty: 1
    unit: unit
  - item_id: spindle_head_basic
    qty: 1
    unit: unit
  - item_id: motor_electric_small
    qty: 1
    unit: unit
  - item_id: table_top_t_slot
    qty: 1
    unit: unit
  - item_id: depth_stop_mechanism
    qty: 1
    unit: unit
  - item_id: belt_and_pulley_set
    qty: 1
    unit: unit
```

#### Option B: Use previous step outputs

- Step 1 produces: `machined_part_raw` (1.0 kg)
- Step 2 produces: `assembled_equipment` (1.0 kg)
- Step 3 produces: `wired_electrical_system` (1.0 unit)

---

## Summary

- **Total errors:** 5
- **Recipe file:** `kb/recipes/recipe_machine_drill_press_v0.yaml`
- **BOM available:** Yes (6 components)
- **Similar recipes:** 2 found
