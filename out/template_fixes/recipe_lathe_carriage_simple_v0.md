# Fix Intelligence: recipe_lathe_carriage_simple_v0

## Files

- **Recipe:** `kb/recipes/recipe_lathe_carriage_simple_v0.yaml`
- **Target item:** `lathe_carriage_simple`
  - File: `kb/items/lathe_carriage_simple.yaml`
- **BOM:** None
- **Steps:** 4 total

## Errors (4 found)

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

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'machining_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `machining_basic_v0`
  - File: `kb/processes/machining_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `lathe_carriage_and_cross_slide` (1.0 unit)

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'precision_grinding_and_scraping_v0') requires input 'rough_part' which is not available

**Location:** Step 2
**Process:** `precision_grinding_and_scraping_v0`
  - File: `kb/processes/precision_grinding_and_scraping_v0.yaml`

**Current step:**
```yaml
- process_id: precision_grinding_and_scraping_v0
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

- Step 0 produces: `lathe_carriage_and_cross_slide` (1.0 unit)
- Step 1 produces: `machined_metal_block_v0` (1.8 kg)
- Step 2 produces: `finished_part` (1.0 kg)

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_lathe_carriage_simple_v0.yaml`
- **BOM available:** No
