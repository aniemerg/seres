# Fix Intelligence: recipe_chemical_reactor_heated_v0

## Files

- **Recipe:** `kb/recipes/recipe_chemical_reactor_heated_v0.yaml`
- **Target item:** `chemical_reactor_heated_v0`
  - File: `kb/items/chemical_reactor_heated_v0.yaml`
- **BOM:** `kb/boms/bom_chemical_reactor_heated_v0.yaml` ✓
  - Components: 4
- **Steps:** 4 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_chemical_reactor_heated_v1` → chemical_reactor_heated (4 steps)

## Errors (4 found)

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

BOM has 4 components:

- `chemical_reactor_heated_body` (qty: 1.0 None)
- `reactor_shell_steel_v0` (qty: 1.0 None)
- `pressure_vessel_steel` (qty: 1.0 None)
- `heating_element_set_basic` (qty: 1.0 None)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: chemical_reactor_heated_body
    qty: 1.0
    unit: None
  - item_id: reactor_shell_steel_v0
    qty: 1.0
    unit: None
  - item_id: pressure_vessel_steel
    qty: 1.0
    unit: None
  - item_id: heating_element_set_basic
    qty: 1.0
    unit: None
```

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'enclosure_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `enclosure_assembly_basic_v0`
  - File: `kb/processes/enclosure_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: enclosure_assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 4 components:

- `chemical_reactor_heated_body` (qty: 1.0 None)
- `reactor_shell_steel_v0` (qty: 1.0 None)
- `pressure_vessel_steel` (qty: 1.0 None)
- `heating_element_set_basic` (qty: 1.0 None)

Suggested fix:
```yaml
- process_id: enclosure_assembly_basic_v0
  inputs:
  - item_id: chemical_reactor_heated_body
    qty: 1.0
    unit: None
  - item_id: reactor_shell_steel_v0
    qty: 1.0
    unit: None
  - item_id: pressure_vessel_steel
    qty: 1.0
    unit: None
  - item_id: heating_element_set_basic
    qty: 1.0
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `assembled_equipment` (1.0 kg)

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'electrical_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `electrical_assembly_basic_v0`
  - File: `kb/processes/electrical_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: electrical_assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 4 components:

- `chemical_reactor_heated_body` (qty: 1.0 None)
- `reactor_shell_steel_v0` (qty: 1.0 None)
- `pressure_vessel_steel` (qty: 1.0 None)
- `heating_element_set_basic` (qty: 1.0 None)

Suggested fix:
```yaml
- process_id: electrical_assembly_basic_v0
  inputs:
  - item_id: chemical_reactor_heated_body
    qty: 1.0
    unit: None
  - item_id: reactor_shell_steel_v0
    qty: 1.0
    unit: None
  - item_id: pressure_vessel_steel
    qty: 1.0
    unit: None
  - item_id: heating_element_set_basic
    qty: 1.0
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `assembled_equipment` (1.0 kg)
- Step 1 produces: `enclosure_electrical_medium` (1.0 kg)

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'sealing_and_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
**Process:** `sealing_and_assembly_basic_v0`
  - File: `kb/processes/sealing_and_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: sealing_and_assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 4 components:

- `chemical_reactor_heated_body` (qty: 1.0 None)
- `reactor_shell_steel_v0` (qty: 1.0 None)
- `pressure_vessel_steel` (qty: 1.0 None)
- `heating_element_set_basic` (qty: 1.0 None)

Suggested fix:
```yaml
- process_id: sealing_and_assembly_basic_v0
  inputs:
  - item_id: chemical_reactor_heated_body
    qty: 1.0
    unit: None
  - item_id: reactor_shell_steel_v0
    qty: 1.0
    unit: None
  - item_id: pressure_vessel_steel
    qty: 1.0
    unit: None
  - item_id: heating_element_set_basic
    qty: 1.0
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `assembled_equipment` (1.0 kg)
- Step 1 produces: `enclosure_electrical_medium` (1.0 kg)

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_chemical_reactor_heated_v0.yaml`
- **BOM available:** Yes (4 components)
- **Similar recipes:** 1 found
