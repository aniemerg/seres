# Fix Intelligence: recipe_resource_holon_v0

## Files

- **Recipe:** `kb/recipes/recipe_resource_holon_v0.yaml`
- **Target item:** `resource_holon_v0`
  - File: `kb/items/resource_holon_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'software_deployment_v0') requires input 'software_source_code_v0' which is not available

**Location:** Step 0
**Process:** `software_deployment_v0`
  - File: `kb/processes/software_deployment_v0.yaml`

**Current step:**
```yaml
- process_id: software_deployment_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_resource_holon_v0.yaml`
- **BOM available:** No
