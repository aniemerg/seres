# Fix Intelligence: recipe_test_leads_insulation_tester_v0

## Files

- **Recipe:** `kb/recipes/recipe_test_leads_insulation_tester_v0.yaml`
- **Target item:** `test_leads_insulation_tester`
  - File: `kb/items/test_leads_insulation_tester.yaml`
- **BOM:** None
- **Steps:** 2 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'cable_harness_assembly_v0') requires input 'electrical_wire_and_connectors' which is not available

**Location:** Step 0
**Process:** `cable_harness_assembly_v0`
  - File: `kb/processes/cable_harness_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: cable_harness_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_test_leads_insulation_tester_v0.yaml`
- **BOM available:** No
