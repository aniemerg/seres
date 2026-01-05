# Fix Intelligence: recipe_oxygen_collection_system_ffc_v0

## Files

- **Recipe:** `kb/recipes/recipe_oxygen_collection_system_ffc_v0.yaml`
- **Target item:** `oxygen_collection_system_ffc_v0`
  - File: `kb/items/oxygen_collection_system_ffc_v0.yaml`
- **BOM:** `kb/boms/bom_oxygen_collection_system_ffc_v0.yaml` ✓
  - Components: 1
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'oxygen_collection_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `oxygen_collection_v0`
  - File: `kb/processes/oxygen_collection_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: oxygen_collection_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 1 components:

- `import_misc_components_set` (qty: 1.0 None)

Suggested fix:
```yaml
- process_id: oxygen_collection_v0
  inputs:
  - item_id: import_misc_components_set
    qty: 1.0
    unit: None
```

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_oxygen_collection_system_ffc_v0.yaml`
- **BOM available:** Yes (1 components)
