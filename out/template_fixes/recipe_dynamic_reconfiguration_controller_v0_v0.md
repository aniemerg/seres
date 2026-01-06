# Fix Intelligence: recipe_dynamic_reconfiguration_controller_v0_v0

## Files

- **Recipe:** `kb/recipes/recipe_dynamic_reconfiguration_controller_v0_v0.yaml`
- **Target item:** `dynamic_reconfiguration_controller_v0`
  - File: `kb/items/dynamic_reconfiguration_controller_v0.yaml`
- **BOM:** None
- **Steps:** 4 total

## Errors (4 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'pcb_assembly_v0') requires input 'pcb_bare_board' which is not available

**Location:** Step 0
**Process:** `pcb_assembly_v0`
  - File: `kb/processes/pcb_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: pcb_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'electronic_component_assembly_v0') requires input 'electronic_parts_kit' which is not available

**Location:** Step 1
**Process:** `electronic_component_assembly_v0`
  - File: `kb/processes/electronic_component_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: electronic_component_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'electrical_wiring_and_controls_v0') requires input 'electrical_wire_and_connectors' which is not available

**Location:** Step 2
**Process:** `electrical_wiring_and_controls_v0`
  - File: `kb/processes/electrical_wiring_and_controls_v0.yaml`

**Current step:**
```yaml
- process_id: electrical_wiring_and_controls_v0
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

#### Option B: Use previous step outputs

- Step 0 produces: `pcb_populated` (1.0 unit)
- Step 1 produces: `electronic_component_or_module` (1.0 unit)
- Step 2 produces: `wired_electrical_system` (1.0 unit)

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_dynamic_reconfiguration_controller_v0_v0.yaml`
- **BOM available:** No
