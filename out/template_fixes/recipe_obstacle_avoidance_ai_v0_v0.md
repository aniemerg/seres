# Fix Intelligence: recipe_obstacle_avoidance_ai_v0_v0

## Files

- **Recipe:** `kb/recipes/recipe_obstacle_avoidance_ai_v0_v0.yaml`
- **Target item:** `obstacle_avoidance_ai_v0`
  - File: `kb/items/obstacle_avoidance_ai_v0.yaml`
- **BOM:** None
- **Steps:** 2 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_obstacle_avoidance_ai_v0` → obstacle_avoidance_ai_v0 (3 steps)

## Errors (2 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `assembly_basic_v0`
  - File: `kb/processes/assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'machine_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `machine_assembly_basic_v0`
  - File: `kb/processes/machine_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machine_assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `assembled_equipment` (1.0 kg)

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_obstacle_avoidance_ai_v0_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
