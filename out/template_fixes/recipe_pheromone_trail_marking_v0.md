# Fix Intelligence: recipe_pheromone_trail_marking_v0

## Files

- **Recipe:** `kb/recipes/recipe_pheromone_trail_marking_v0.yaml`
- **Target item:** `pheromone_trail_marking_v0`
  - File: `kb/items/pheromone_trail_marking_v0.yaml`
- **BOM:** `kb/boms/bom_pheromone_trail_marking_v0.yaml` ✓
  - Components: 0
- **Steps:** 1 total

## Errors (1 found)

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

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_pheromone_trail_marking_v0.yaml`
- **BOM available:** Yes (0 components)
