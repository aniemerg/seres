# Fix Intelligence: recipe_instrument_mounts_basic_v0

## Files

- **Recipe:** `kb/recipes/recipe_instrument_mounts_basic_v0.yaml`
- **Target item:** `instrument_mounts_basic`
  - File: `kb/items/instrument_mounts_basic.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (3 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'metal_forming_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `metal_forming_basic_v0`
  - File: `kb/processes/metal_forming_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: metal_forming_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'welding_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `welding_basic_v0`
  - File: `kb/processes/welding_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: welding_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `formed_metal_part` (0.95 kg)

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'surface_finishing_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `surface_finishing_basic_v0`
  - File: `kb/processes/surface_finishing_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: surface_finishing_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `formed_metal_part` (0.95 kg)
- Step 1 produces: `welded_assemblies` (1.0 kg)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_instrument_mounts_basic_v0.yaml`
- **BOM available:** No
