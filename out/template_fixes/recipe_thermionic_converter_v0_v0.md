# Fix Intelligence: recipe_thermionic_converter_v0_v0

## Files

- **Recipe:** `kb/recipes/recipe_thermionic_converter_v0_v0.yaml`
- **Target item:** `thermionic_converter_v0`
  - File: `kb/items/thermionic_converter_v0.yaml`
- **BOM:** `kb/boms/bom_thermionic_converter_v0.yaml` ✓
  - Components: 4
- **Steps:** 8 total

## Similar Recipes

Found 2 recipes producing similar items:

- `recipe_machine_thermionic_converter_v0` → thermionic_converter (3 steps)
- `recipe_thermionic_converter_v0` → thermionic_converter (5 steps)

## Errors (7 found)

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

- `ceramic_tube_body` (qty: 1 unit)
- `refractory_metal_electrodes` (qty: 2 unit)
- `ceramic_insulators` (qty: 4 unit)
- `cesium_ampule` (qty: 1 unit)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: ceramic_tube_body
    qty: 1
    unit: unit
  - item_id: refractory_metal_electrodes
    qty: 2
    unit: unit
  - item_id: ceramic_insulators
    qty: 4
    unit: unit
  - item_id: cesium_ampule
    qty: 1
    unit: unit
```

#### Option C: Pattern from `recipe_machine_thermionic_converter_v0`

Similar recipe uses this process (step 0) with:

```yaml
  inputs:
  - item_id: thermionic_vacuum_tube
    qty: 1.0
    unit: unit
  - item_id: converter_housing_assembly
    qty: 1.0
    unit: unit
  - item_id: vacuum_seal_assembly
    qty: 1.0
    unit: unit
```

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'vacuum_tube_assembly_v0') requires input 'tungsten_cathode_coated' which is not available

**Location:** Step 1
**Process:** `vacuum_tube_assembly_v0`
  - File: `kb/processes/vacuum_tube_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: vacuum_tube_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

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

BOM has 4 components:

- `ceramic_tube_body` (qty: 1 unit)
- `refractory_metal_electrodes` (qty: 2 unit)
- `ceramic_insulators` (qty: 4 unit)
- `cesium_ampule` (qty: 1 unit)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: ceramic_tube_body
    qty: 1
    unit: unit
  - item_id: refractory_metal_electrodes
    qty: 2
    unit: unit
  - item_id: ceramic_insulators
    qty: 4
    unit: unit
  - item_id: cesium_ampule
    qty: 1
    unit: unit
```

#### Option B: Use previous step outputs

- Step 0 produces: `assembled_equipment` (1.0 kg)
- Step 1 produces: `thermionic_vacuum_tube` (1.0 unit)

#### Option C: Pattern from `recipe_machine_thermionic_converter_v0`

Similar recipe uses this process (step 0) with:

```yaml
  inputs:
  - item_id: thermionic_vacuum_tube
    qty: 1.0
    unit: unit
  - item_id: converter_housing_assembly
    qty: 1.0
    unit: unit
  - item_id: vacuum_seal_assembly
    qty: 1.0
    unit: unit
```

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

- `ceramic_tube_body` (qty: 1 unit)
- `refractory_metal_electrodes` (qty: 2 unit)
- `ceramic_insulators` (qty: 4 unit)
- `cesium_ampule` (qty: 1 unit)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: ceramic_tube_body
    qty: 1
    unit: unit
  - item_id: refractory_metal_electrodes
    qty: 2
    unit: unit
  - item_id: ceramic_insulators
    qty: 4
    unit: unit
  - item_id: cesium_ampule
    qty: 1
    unit: unit
```

#### Option B: Use previous step outputs

- Step 0 produces: `assembled_equipment` (1.0 kg)
- Step 1 produces: `thermionic_vacuum_tube` (1.0 unit)
- Step 2 produces: `assembled_equipment` (1.0 kg)

#### Option C: Pattern from `recipe_machine_thermionic_converter_v0`

Similar recipe uses this process (step 0) with:

```yaml
  inputs:
  - item_id: thermionic_vacuum_tube
    qty: 1.0
    unit: unit
  - item_id: converter_housing_assembly
    qty: 1.0
    unit: unit
  - item_id: vacuum_seal_assembly
    qty: 1.0
    unit: unit
```

---

### Error 5: recipe_template_missing_step_inputs

**Message:** Step 4 uses template process 'wiring_and_electronics_integration_v0' but doesn't provide step-level input overrides

**Location:** Step 4
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

BOM has 4 components:

- `ceramic_tube_body` (qty: 1 unit)
- `refractory_metal_electrodes` (qty: 2 unit)
- `ceramic_insulators` (qty: 4 unit)
- `cesium_ampule` (qty: 1 unit)

Suggested fix:
```yaml
- process_id: wiring_and_electronics_integration_v0
  inputs:
  - item_id: ceramic_tube_body
    qty: 1
    unit: unit
  - item_id: refractory_metal_electrodes
    qty: 2
    unit: unit
  - item_id: ceramic_insulators
    qty: 4
    unit: unit
  - item_id: cesium_ampule
    qty: 1
    unit: unit
```

#### Option B: Use previous step outputs

- Step 0 produces: `assembled_equipment` (1.0 kg)
- Step 1 produces: `thermionic_vacuum_tube` (1.0 unit)
- Step 2 produces: `assembled_equipment` (1.0 kg)
- Step 3 produces: `assembled_equipment` (1.0 kg)

---

### Error 6: recipe_template_missing_step_inputs

**Message:** Step 6 uses template process 'integration_test_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 6
**Process:** `integration_test_basic_v0`
  - File: `kb/processes/integration_test_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: integration_test_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 4 components:

- `ceramic_tube_body` (qty: 1 unit)
- `refractory_metal_electrodes` (qty: 2 unit)
- `ceramic_insulators` (qty: 4 unit)
- `cesium_ampule` (qty: 1 unit)

Suggested fix:
```yaml
- process_id: integration_test_basic_v0
  inputs:
  - item_id: ceramic_tube_body
    qty: 1
    unit: unit
  - item_id: refractory_metal_electrodes
    qty: 2
    unit: unit
  - item_id: ceramic_insulators
    qty: 4
    unit: unit
  - item_id: cesium_ampule
    qty: 1
    unit: unit
```

#### Option B: Use previous step outputs

- Step 0 produces: `assembled_equipment` (1.0 kg)
- Step 1 produces: `thermionic_vacuum_tube` (1.0 unit)
- Step 2 produces: `assembled_equipment` (1.0 kg)
- Step 3 produces: `assembled_equipment` (1.0 kg)
- Step 4 produces: `wired_electrical_system` (1.0 unit)

---

### Error 7: recipe_template_missing_step_inputs

**Message:** Step 7 uses template process 'inspection_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 7
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

BOM has 4 components:

- `ceramic_tube_body` (qty: 1 unit)
- `refractory_metal_electrodes` (qty: 2 unit)
- `ceramic_insulators` (qty: 4 unit)
- `cesium_ampule` (qty: 1 unit)

Suggested fix:
```yaml
- process_id: inspection_basic_v0
  inputs:
  - item_id: ceramic_tube_body
    qty: 1
    unit: unit
  - item_id: refractory_metal_electrodes
    qty: 2
    unit: unit
  - item_id: ceramic_insulators
    qty: 4
    unit: unit
  - item_id: cesium_ampule
    qty: 1
    unit: unit
```

#### Option B: Use previous step outputs

- Step 0 produces: `assembled_equipment` (1.0 kg)
- Step 1 produces: `thermionic_vacuum_tube` (1.0 unit)
- Step 2 produces: `assembled_equipment` (1.0 kg)
- Step 3 produces: `assembled_equipment` (1.0 kg)
- Step 4 produces: `wired_electrical_system` (1.0 unit)
- Step 6 produces: `assembled_electronics` (1.0 kg)

---

## Summary

- **Total errors:** 7
- **Recipe file:** `kb/recipes/recipe_thermionic_converter_v0_v0.yaml`
- **BOM available:** Yes (4 components)
- **Similar recipes:** 2 found
