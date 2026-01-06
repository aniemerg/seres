# Fix Intelligence: recipe_kiln_ceramic_v0

## Files

- **Recipe:** `kb/recipes/recipe_kiln_ceramic_v0.yaml`
- **Target item:** `kiln_ceramic`
  - File: `kb/items/kiln_ceramic.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'refractory_casting_v0') requires input 'refractory_castable' which is not available

**Location:** Step 0
**Process:** `refractory_casting_v0`
  - File: `kb/processes/refractory_casting_v0.yaml`

**Current step:**
```yaml
- process_id: refractory_casting_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'heating_element_installation_v0') requires input 'heating_element_resistive' which is not available

**Location:** Step 1
**Process:** `heating_element_installation_v0`
  - File: `kb/processes/heating_element_installation_v0.yaml`

**Current step:**
```yaml
- process_id: heating_element_installation_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

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

#### Option B: Use previous step outputs

- Step 0 produces: `acid_resistant_reactor_lining_v0` (1.0 kg)
- Step 1 produces: `furnace_chamber_equipped` (1.0 unit)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_kiln_ceramic_v0.yaml`
- **BOM available:** No
