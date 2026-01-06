# Fix Intelligence: recipe_power_electronics_module_v1

## Files

- **Recipe:** `kb/recipes/recipe_power_electronics_module_v1.yaml`
- **Target item:** `power_electronics_module`
  - File: `kb/items/power_electronics_module.yaml`
- **BOM:** None
- **Steps:** 5 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_power_electronics_module_v0` → power_electronics_module_v0 (5 steps)

## Errors (4 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'pcb_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `pcb_assembly_basic_v0`
  - File: `kb/processes/pcb_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: pcb_assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'heat_sink_installation_v0') requires input 'heat_sink' which is not available

**Location:** Step 2
**Process:** `heat_sink_installation_v0`
  - File: `kb/processes/heat_sink_installation_v0.yaml`

**Current step:**
```yaml
- process_id: heat_sink_installation_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 3: recipe_template_missing_step_inputs

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

#### Option B: Use previous step outputs

- Step 1 produces: `electronic_component_or_module` (1.0 unit)
- Step 2 produces: `component_with_heat_sink` (1.0 unit)

---

### Error 4: recipe_step_input_not_satisfied

**Message:** Step 4 (process 'electrical_testing_v0') requires input 'assembled_electrical_system' which is not available

**Location:** Step 4
**Process:** `electrical_testing_v0`
  - File: `kb/processes/electrical_testing_v0.yaml`

**Current step:**
```yaml
- process_id: electrical_testing_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_power_electronics_module_v1.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
