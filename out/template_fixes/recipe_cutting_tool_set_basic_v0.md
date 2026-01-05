# Fix Intelligence: recipe_cutting_tool_set_basic_v0

## Files

- **Recipe:** `kb/recipes/recipe_cutting_tool_set_basic_v0.yaml`
- **Target item:** `cutting_tool_set_basic`
  - File: `kb/items/cutting_tool_set_basic.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'import_receiving_basic_v0') requires input 'bulk_material_or_parts' which is not available

**Location:** Step 0
**Process:** `import_receiving_basic_v0`
  - File: `kb/processes/import_receiving_basic_v0.yaml`

**Current step:**
```yaml
- process_id: import_receiving_basic_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'metal_casting_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `metal_casting_basic_v0`
  - File: `kb/processes/metal_casting_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: metal_casting_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `bulk_material_or_parts` (1.0 kg)

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'machining_finish_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `machining_finish_basic_v0`
  - File: `kb/processes/machining_finish_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_finish_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `bulk_material_or_parts` (1.0 kg)
- Step 1 produces: `cast_metal_parts` (0.95 kg)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_cutting_tool_set_basic_v0.yaml`
- **BOM available:** No
