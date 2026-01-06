# Fix Intelligence: recipe_silicon_seed_crystal_v0

## Files

- **Recipe:** `kb/recipes/recipe_silicon_seed_crystal_v0.yaml`
- **Target item:** `silicon_seed_crystal`
  - File: `kb/items/silicon_seed_crystal.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'zone_refining_silicon_v0') requires input 'silicon_purified' which is not available

**Location:** Step 0
**Process:** `zone_refining_silicon_v0`
  - File: `kb/processes/zone_refining_silicon_v0.yaml`

**Current step:**
```yaml
- process_id: zone_refining_silicon_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'metal_cutting_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `metal_cutting_basic_v0`
  - File: `kb/processes/metal_cutting_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: metal_cutting_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `silicon_polycrystalline_ultrapure` (0.98 kg)
- Step 0 produces: `silicon_purified` (0.02 kg)

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'inspection_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `inspection_basic_v0`
  - File: `kb/processes/inspection_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: inspection_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `silicon_polycrystalline_ultrapure` (0.98 kg)
- Step 0 produces: `silicon_purified` (0.02 kg)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_silicon_seed_crystal_v0.yaml`
- **BOM available:** No
