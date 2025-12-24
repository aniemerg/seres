# ADR-007: Explicit Import Items Architecture

## Status
Proposed

## Context

Currently, the knowledge base uses "import placeholder" recipes to indicate items that are imported rather than manufactured locally. This approach has several limitations:

1. **Loss of manufacturing knowledge**: When a recipe is marked as `variant_id: import_placeholder_v0` with empty steps, we lose the information about how the item *could* be manufactured
2. **Data vs. simulation decision**: Whether to import an item should be a simulation/analysis decision, not a permanent KB data decision
3. **Scenario inflexibility**: The same KB can't easily represent different scenarios (lunar base bootstrap vs. mature manufacturing)
4. **Circular dependency handling**: Currently handled by permanently changing recipes to imports, losing the original manufacturing flow

### Current State
- Import detection: Recipes with `"import" in variant_id` or empty `steps: []`
- Location: Mixed throughout `kb/recipes/` folder
- No distinction between temporary bootstrap imports and permanent imports

## Decision

We will implement an **explicit import items architecture** with the following design:

### 1. Import Items as First-Class Entities

**Explicit import field:**
```yaml
# kb/imports/water.yaml
id: import_water
kind: material
is_import: true  # NEW: Explicit field marking this as an import
name: Water (imported)
mass: 1.0
unit: kg
material_class: water
notes: "Imported water for bootstrap. ISRU alternative: water_v0 from regolith processing."
isru_alternative: water_v0  # Optional: links to ISRU version
```

**Naming convention:**
- Import items use `import_` prefix (e.g., `import_water`, `import_copper`)
- This is a **convention**, not a requirement (enforced by `is_import: true` field)
- Helps humans quickly identify imports in references

### 2. Imports Don't Need Recipes

Import items are **intentionally recipe-less**:
- They represent externally sourced materials
- Having no recipe is the correct state
- Indexer will **not** flag `is_import: true` items as "missing recipes"

**Indexer changes:**
```python
# Skip "no recipe" detection for import items
if entry.get("is_import"):
    continue  # Don't flag as missing recipe
```

### 3. Folder Organization

```
kb/
├── imports/           # NEW: Explicit import items
│   ├── water.yaml     # id: import_water, is_import: true
│   ├── copper.yaml    # id: import_copper, is_import: true
│   └── electronics.yaml
├── items/
│   ├── materials/
│   │   └── water_v0.yaml     # ISRU water from regolith
│   │   └── copper_v0.yaml    # ISRU copper from recycling
```

**Indexer support:**
- Scan `kb/imports/**/*.yaml` in addition to `kb/items/**/*.yaml`
- Infer `kind` from subfolder or default to `material` for imports

### 4. BOM and Recipe References

**BOMs can reference import items directly:**
```yaml
# kb/boms/bom_hauler_v0.yaml
components:
  - item_id: import_water  # References import explicitly
    qty: 100
    unit: kg
```

**Closure analysis behavior:**
- When expanding `import_water`, identifies it as imported (via `is_import: true`)
- Reports it in "Imported Items" section
- Analysts review and decide if ISRU alternative exists

**Discovery process:**
1. Run closure analysis on machine
2. See `import_water: 100 kg` in imported items
3. Question: "Can we make water locally?"
4. If yes: Update BOM to reference `water_v0` instead
5. If no: Keep import

### 5. Co-existence of Import and ISRU Versions

Both can exist simultaneously:
- `import_water` - for bootstrap/scenarios without water extraction
- `water_v0` - for ISRU from regolith processing

**Transition path:**
```
Bootstrap phase: BOM → import_water (imported)
                ↓
         (analyze closure, seek alternatives)
                ↓
Mature phase:   BOM → water_v0 (ISRU, from regolith)
```

**If ISRU version doesn't exist:**
- Closure analysis shows `import_water` as imported
- If desired, create `water_v0` item + recipe for ISRU route
- Update BOMs to reference `water_v0`
- Import still exists for other scenarios

### 6. No Automatic Fallbacks

**Rejected approach:** Automatically fallback `water_v0` → `import_water` if ISRU fails

**Chosen approach:** Explicit references only
- If BOM says `water_v0` but recipe is incomplete → shows as unresolved
- Analyst must **manually** decide: fix recipe OR change BOM to `import_water`
- This is intentional: forces conscious decisions about ISRU vs. import

### 7. Variant Linking (Optional Metadata)

Import items can link to ISRU alternatives:
```yaml
id: import_water
is_import: true
isru_alternative: water_v0  # Optional linking
notes: "For bootstrap. ISRU route: water_v0 from lunar regolith."
```

This is **documentation only**, not functional linkage.

### 8. Circular Dependency Resolution

With explicit imports, circular dependencies are handled at **analysis time**:

**Closure analysis logic:**
```python
if item_id in expansion_path:
    # Circular dependency - check if import version exists
    import_id = f"import_{item_id}"
    if kb.get_item(import_id) and kb.get_item(import_id).get("is_import"):
        # Use import version for bootstrap
        accumulate(imported_items, import_id, ...)
    else:
        # Mark second encounter as virtual import
        accumulate(imported_items, item_id, ...)  # Bootstrap import
```

**KB data remains unchanged** - loops represent real manufacturing flows (e.g., copper recycling)

## Consequences

### Positive

1. **Preserved manufacturing knowledge**: All ISRU routes remain in KB
2. **Scenario flexibility**: Same KB works for bootstrap vs. mature manufacturing
3. **Explicit decisions**: `is_import: true` clearly marks intent
4. **Clean separation**: `kb/imports/` folder makes imports visible
5. **Analysis-driven**: Import decisions made during closure analysis, not hardcoded
6. **Transition path**: Can evolve from imports to ISRU by updating BOM references

### Negative

1. **Migration effort**: ~50 existing import placeholder recipes need conversion
2. **Indexer changes**: Need to support `kb/imports/` folder and `is_import` field
3. **Dual items**: Can have both `import_water` and `water_v0` (potential confusion)
4. **Manual BOM updates**: Transitioning from import to ISRU requires manual BOM changes

### Neutral

1. **Convention-based naming**: `import_` prefix helps but isn't enforced
2. **No automatic fallbacks**: Intentional, forces conscious decisions
3. **Documentation linking**: `isru_alternative` field is metadata only

## Implementation Plan

### Phase 1: Indexer Support (Small)
1. Add `kb/imports/` folder scanning
2. Add `is_import` field recognition
3. Skip "no recipe" detection for `is_import: true` items
4. Update kind inference for imports folder

### Phase 2: Closure Analysis Enhancement (Small)
1. Check `is_import` field when classifying items
2. Report import items separately from ISRU
3. Add import ID check for circular dependency resolution

### Phase 3: Migration (Medium)
1. Create `kb/imports/` folder structure
2. Convert existing import placeholder recipes to explicit import items
3. Update BOMs currently referencing placeholder items
4. Document transition paths for common materials

### Phase 4: Documentation (Small)
1. Update KB structure documentation
2. Add import item creation guidelines
3. Document ISRU transition workflow

## Migration Complexity: MEDIUM

**Estimated effort:** 4-8 hours
- ~50 import placeholder recipes to migrate
- Indexer changes: ~50 lines of code
- Closure analysis changes: ~30 lines of code
- Testing and validation: 2-3 hours

## Alternatives Considered

### Alternative 1: Keep Import Placeholders
- **Rejected**: Loses manufacturing knowledge, inflexible for scenarios

### Alternative 2: Import Manifest Files
- Separate `imports.yaml` config file listing imports for each scenario
- **Rejected**: Adds indirection; harder to discover what's imported

### Alternative 3: Automatic Fallbacks
- If `water_v0` fails, automatically try `import_water`
- **Rejected**: Hides dependencies, makes analysis less explicit

### Alternative 4: Recipe Variants Only
- Use `recipe_water_import_v0` and `recipe_water_isru_v0` targeting same item
- **Rejected**: Doesn't solve the "permanent data decision" problem

## References

- Investigation report: `design/indexer_imports_investigation.txt`
- Related: Circular dependency handling (ADR-003, pending)
- Related: Material closure analysis tool

## Decision Makers

- Allan Niemerg (Primary)
- Date: 2024-12-24

## Notes

This ADR represents a significant architectural improvement, moving from "import as data" to "import as explicit entity." The key insight is that **import decisions belong in BOMs and simulation configs**, not in recipes.

The explicit `is_import: true` field makes intent clear, while the `import_` naming convention helps humans. Co-existence of import and ISRU versions enables gradual transitions and scenario flexibility.
