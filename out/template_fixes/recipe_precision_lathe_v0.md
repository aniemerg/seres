# Fix Intelligence: recipe_precision_lathe_v0

## Files

- **Recipe:** `kb/recipes/recipe_precision_lathe_v0.yaml`
- **Target item:** `precision_lathe`
  - File: `kb/items/precision_lathe.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (3 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'casting_or_fabrication_machine_frame_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `casting_or_fabrication_machine_frame_v0`
  - File: `kb/processes/casting_or_fabrication_machine_frame_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: casting_or_fabrication_machine_frame_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'precision_grinding_and_scraping_v0') requires input 'rough_part' which is not available

**Location:** Step 1
**Process:** `precision_grinding_and_scraping_v0`
  - File: `kb/processes/precision_grinding_and_scraping_v0.yaml`

**Current step:**
```yaml
- process_id: precision_grinding_and_scraping_v0
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

#### Option B: Use previous step outputs

- Step 0 produces: `lathe_carriage_and_cross_slide` (1.0 unit)
- Step 1 produces: `finished_part` (1.0 kg)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_precision_lathe_v0.yaml`
- **BOM available:** No
