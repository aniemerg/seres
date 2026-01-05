# Fix Intelligence: recipe_gas_scrubbing_unit_v0

## Files

- **Recipe:** `kb/recipes/recipe_gas_scrubbing_unit_v0.yaml`
- **Target item:** `gas_scrubbing_unit_v0`
  - File: `kb/items/gas_scrubbing_unit_v0.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'gas_scrubbing_unit_frame_v0') requires input 'steel_stock' which is not available

**Location:** Step 0
**Process:** `gas_scrubbing_unit_frame_v0`
  - File: `kb/processes/gas_scrubbing_unit_frame_v0.yaml`

**Current step:**
```yaml
- process_id: gas_scrubbing_unit_frame_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'gas_scrubbing_unit_filter_v0_v0') requires input 'filter_cartridges_dust' which is not available

**Location:** Step 1
**Process:** `gas_scrubbing_unit_filter_v0_v0`
  - File: `kb/processes/gas_scrubbing_unit_filter_v0_v0.yaml`

**Current step:**
```yaml
- process_id: gas_scrubbing_unit_filter_v0_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'gas_scrubbing_unit_assembly_v0') requires input 'gas_scrubbing_unit_filter_v0' which is not available

**Location:** Step 2
**Process:** `gas_scrubbing_unit_assembly_v0`
  - File: `kb/processes/gas_scrubbing_unit_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: gas_scrubbing_unit_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_gas_scrubbing_unit_v0.yaml`
- **BOM available:** No
