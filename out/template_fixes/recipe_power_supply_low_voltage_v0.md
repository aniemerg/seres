# Fix Intelligence: recipe_power_supply_low_voltage_v0

## Files

- **Recipe:** `kb/recipes/recipe_power_supply_low_voltage_v0.yaml`
- **Target item:** `power_supply_low_voltage`
  - File: `kb/items/power_supply_low_voltage.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'transformer_winding_v0') requires input 'transformer_core' which is not available

**Location:** Step 0
**Process:** `transformer_winding_v0`
  - File: `kb/processes/transformer_winding_v0.yaml`

**Current step:**
```yaml
- process_id: transformer_winding_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'pcb_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `pcb_assembly_basic_v0`
  - File: `kb/processes/pcb_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: pcb_assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `wound_transformer` (1.0 unit)

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

#### Option B: Use previous step outputs

- Step 0 produces: `wound_transformer` (1.0 unit)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_power_supply_low_voltage_v0.yaml`
- **BOM available:** No
