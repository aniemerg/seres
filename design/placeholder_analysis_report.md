# Placeholder and Stub Analysis Report
**Generated:** 2025-12-28
**Analysis of:** KB placeholders, stubs, and lazy data patterns

## Executive Summary

The KB contains **extensive use of placeholders and stubs** as a gap-filling strategy:

- **1,363** total mentions of "placeholder" or "stub" in KB files
- **442** processes have "placeholder" in their notes (49.6% of all processes!)
- **99** recipes use import_placeholder_* processes
- **25** recipes use the generic "stock_material" instead of specific inputs
- **24** dedicated import_placeholder_* process files

## Categories of Placeholders

### 1. **Placeholder Parameters** (75 processes)
Processes that exist but use rough/estimated values.

**Example:**
```yaml
id: extrusion_basic_v0
notes: "Basic extrusion process for polymer or soft metal tubing; placeholder parameters."
```

**Impact:** Low - Process exists, just needs refinement
**Fix:** Gradual refinement with real data

---

### 2. **Placeholder Processes** (88 processes)
Entire processes that are placeholders, often created just to resolve no_recipe gaps.

**Example:**
```yaml
id: heliostat_mounting_bracket_fabrication_v0
notes: "Placeholder fabrication that converts steel_plate_or_sheet to
       heliostat_mounting_bracket_v0 to resolve no_recipe gap for this part."
```

**Impact:** HIGH - These are fake manufacturing processes
**Fix:** Either create real process or mark as import

---

### 3. **Import Placeholder Processes** (24 files)
Dedicated placeholder processes for imports, some replaced with real processes.

**Example:**
```yaml
id: import_placeholder_proximity_sensor_inductive_v0
kind: process
inputs: []
outputs:
  - item_id: proximity_sensor_inductive
    qty: 1.0
notes: "External import placeholder for inductive proximity sensor."
```

**Impact:** MEDIUM - Legitimate for true imports, problematic when used as shortcuts
**Fix:** Distinguish true imports from lazy placeholders

---

### 4. **Stock_Material Recipes** (25 recipes)
Recipes using the generic "stock_material" instead of specific inputs.

**Example:**
```yaml
id: recipe_placeholder_component_v0
steps:
  - process_id: assembly_basic_v0
    inputs:
      - item_id: stock_material
        qty: 1.0
        unit: kg
    outputs:
      - item_id: placeholder_component_v0
        qty: 1
        unit: unit
```

**Impact:** HIGH - Completely fake recipes with no real manufacturing
**Fix:** Delete or replace with real recipes

---

### 5. **Explicit Placeholder Items** (9 items)
Items explicitly named as placeholders.

**Examples:**
- `placeholder_component_v0`
- `placeholder_seed_component`
- `placeholder_dummy_component`
- `hydraulic_hose_segment_input_placeholder`

**Impact:** MEDIUM - Used to unblock dependencies
**Fix:** Track and replace systematically

---

### 6. **Generic Items** (4 items)
Generic catch-all items that hide real dependencies.

**Items:**
- `stock_material` - Used in 25+ recipes
- `raw_material` - Generic feedstock
- `none` - Null placeholder
- `placeholder_component` - Generic placeholder

**Impact:** HIGH - Obscures real material requirements
**Fix:** Ban use of stock_material in new recipes

---

## Problem Patterns

### Pattern 1: "Lazy Recipe Creation"
Agent creates recipe to resolve gap but doesn't research real inputs:

```yaml
# BAD: Lazy placeholder recipe
id: recipe_something_v0
steps:
  - process_id: assembly_basic_v0
    inputs:
      - item_id: stock_material  # ← Generic, no research
        qty: 1.0
    outputs:
      - item_id: something
        qty: 1
```

### Pattern 2: "Placeholder Cascade"
Placeholders reference other placeholders:

```
placeholder_component_v0 → uses → stock_material
  ↓ used by
placeholder_seed_component → uses → placeholder_component_v0
```

### Pattern 3: "Import Shortcuts"
Agent creates import_placeholder instead of researching manufacturing:

```yaml
# Instead of researching how to make proximity sensor,
# agent creates import_placeholder_proximity_sensor_v0
```

---

## Quantitative Analysis

| Category | Count | % of Total |
|----------|-------|------------|
| Processes with placeholder in notes | 442 | 49.6% |
| Recipes using import_placeholder_* | 99 | 4.9% |
| Stock_material recipes | 25 | 1.2% |
| Explicit placeholder items | 9 | 0.5% |
| Import placeholder processes | 24 | 2.7% |

---

## Root Causes

1. **Gap Resolution Pressure**: Agents prioritize resolving gaps quickly over accuracy
2. **Missing Guidance**: No clear policy against placeholders in prompts
3. **Stock_Material Exists**: The existence of `stock_material` item enables lazy behavior
4. **Circular Dependency Avoidance**: Agents use placeholders to avoid circular deps
5. **Knowledge Gaps**: Agents don't know real manufacturing process, so they fake it

---

## Recommendations

### Immediate Actions

1. **Ban stock_material in new recipes**
   - Add validation rule: recipes cannot use stock_material as input
   - Exception: bootstrap/seed recipes only

2. **Flag placeholder processes**
   - Mark processes with "placeholder" in notes for review
   - Create separate queue for placeholder replacement

3. **Distinguish import types**
   - `import_v0` variant = legitimate Earth import
   - `import_placeholder_*` process = lazy shortcut (should be replaced)

### Medium-Term Solutions

4. **Placeholder Quotas**
   - Track placeholder creation rate per agent
   - Penalize agents that create too many placeholders

5. **Validation Rules**
   - Reject recipes that only use stock_material
   - Reject processes with "placeholder" in notes unless approved
   - Require specific inputs for all manufacturing recipes

6. **Cleanup Campaign**
   - Priority 1: Replace stock_material recipes (25 items)
   - Priority 2: Replace placeholder processes (88 items)
   - Priority 3: Refine parameter placeholders (75 items)

### Long-Term Prevention

7. **Agent Prompt Updates**
   - Explicitly forbid creating placeholders
   - Require research before creating recipes
   - Examples of good vs bad recipes

8. **Review Process**
   - Human review of recipes before acceptance
   - AI review agent that checks for placeholders

9. **Better Templates**
   - Provide recipe templates for common patterns
   - Include "how to research" guidance

---

## Detection Queries

### Find all placeholder usage:
```bash
grep -r "placeholder\|stub" kb/ --include="*.yaml" -i
```

### Find stock_material recipes:
```bash
grep -r "item_id: stock_material" kb/recipes --include="*.yaml"
```

### Find processes marked as placeholder:
```bash
grep -r "^notes:.*[Pp]laceholder" kb/processes --include="*.yaml"
```

### Find import_placeholder processes:
```bash
find kb/processes -name "import_placeholder_*.yaml"
```

---

## Examples of Good vs Bad

### ❌ BAD: Placeholder Recipe
```yaml
id: recipe_proximity_sensor_v0
variant_id: v0
steps:
  - process_id: assembly_basic_v0
    inputs:
      - item_id: stock_material
        qty: 0.25
    outputs:
      - item_id: proximity_sensor
        qty: 1
notes: "Placeholder recipe; replace with real manufacturing later"
```

### ✅ GOOD: Real Recipe
```yaml
id: recipe_proximity_sensor_v0
variant_id: v0
steps:
  - process_id: electronics_assembly_v0
    inputs:
      - item_id: copper_wire_magnet
        qty: 0.05
        unit: kg
      - item_id: pcb_populated
        qty: 0.02
        unit: kg
      - item_id: aluminum_alloy_ingot
        qty: 0.15
        unit: kg
      - item_id: potting_compound
        qty: 0.03
        unit: kg
    outputs:
      - item_id: proximity_sensor
        qty: 1
        unit: unit
notes: "Manufacturing recipe using specific components"
```

---

## Specific Files to Review/Replace

### High Priority Stock_Material Recipes:
1. `recipe_fluorite_v0`
2. `recipe_powder_metal_or_ceramic_v0`
3. `recipe_nitrogen_gas_v0`
4. `recipe_etching_chemicals_v0`
5. `recipe_voltage_regulator_ic_v0`
6. `recipe_placeholder_component_v0`
7. `recipe_sensor_suite_general_v0`

### Placeholder Items to Replace:
1. `placeholder_component_v0`
2. `placeholder_seed_component`
3. `placeholder_dummy_component`
4. `hydraulic_hose_segment_input_placeholder`

### Import Placeholder Processes (sample - 24 total):
1. `import_placeholder_proximity_sensor_inductive_v0`
2. `import_placeholder_electrolysis_cell_unit_v0`
3. `import_placeholder_safety_light_curtain_v0`

---

## Conclusion

**The placeholder problem is pervasive** - nearly half of all processes contain placeholder references. This indicates a systemic issue where agents are prioritizing gap closure over accuracy.

**Key insight**: The existence of `stock_material` and `import_placeholder_*` patterns provides an "easy out" for agents who don't want to research real manufacturing processes.

**Recommended approach**:
1. Immediate ban on new placeholders
2. Systematic replacement of existing placeholders
3. Better agent guidance and validation

---

## Next Steps

1. **Create validation rules** to prevent new placeholders
2. **Update agent prompts** to explicitly forbid placeholders
3. **Launch cleanup campaign** targeting the 25 stock_material recipes first
4. **Add quality metrics** tracking placeholder creation vs replacement
5. **Consider deprecating** the stock_material item entirely
