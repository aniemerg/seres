# Import Architecture Migration Plan

## Executive Summary

**Scope:** Minimal migration - only 2 confirmed import recipes
**Effort:** ~2 hours (much less than estimated 4-8 hours)
**Impact:** Low risk - affects only 2 items directly

## Current State Analysis

### Confirmed Imports (2 items)
Recipes with `variant_id: import_placeholder_v0`:

1. **magnesium_powder_v0**
   - Recipe: `kb/recipes/recipe_magnesium_powder_v0.yaml`
   - Item: `kb/items/materials/magnesium_powder_v0.yaml`
   - Status: Has import placeholder recipe with empty steps

2. **permanent_magnet_neodymium**
   - Recipe: `kb/recipes/recipe_permanent_magnet_neodymium_v0.yaml`
   - Item: `kb/items/materials/permanent_magnet_neodymium.yaml` (likely)
   - Status: Has import placeholder recipe with empty steps

### Items Without Recipes (50 items - Review Needed)
These items have NO `recipe:` field in their definition. They might be:
- Legitimate imports (need to create import items)
- Incomplete items (need ISRU recipes)
- Obsolete items (need cleanup)

Sample items:
- graphite_dry_lubricant_high_temp_v0
- gasket_sheet
- nickel_chromium_alloy
- yn_neuron_bias_circuit_v0
- metal_powder_atomization_v0
- bearing_rings_machined
- ...and 44 more

### False Positives (99 processes)
Processes named `import_placeholder_*` are **NOT imports** - they're historical names for processes that were formerly placeholders but now have real ISRU routes.
- No migration needed for these

## Migration Plan

### Phase 1: Core Infrastructure (1 hour)

#### 1.1 Indexer Changes
**File:** `kbtool/indexer.py`

```python
# Line ~374: Add imports folder scanning
kb_files = sorted(KB_ROOT.glob("**/*.yaml"))

# Line ~39: Update _infer_kind() to handle imports folder
def _infer_kind(path: Path, data: dict) -> Optional[str]:
    # ... existing code ...
    parts = path.parts
    if "imports" in parts:
        # Infer kind from data or default to material
        return data.get("kind", "material")
    # ... rest of existing code ...

# Line ~477: Skip "no recipe" detection for import items
if entry["kind"] in ("part", "material", "machine") and entry["id"] not in recipe_targets:
    # NEW: Skip if item is marked as import
    if entry.get("is_import"):
        continue
    items_without_recipes.append({...})
```

#### 1.2 Closure Analysis Changes
**File:** `kbtool/closure_analysis.py`

```python
# Line ~185: Check is_import field when determining if item is imported
item = self.kb.get_item(item_id)
if not item:
    # ... existing unresolved handling ...
    return

# NEW: Check if item is explicitly marked as import
if item.get("is_import"):
    mass_kg = self._calculate_mass(item, qty, unit)
    self._accumulate(imported_items, item_id, qty, unit, mass_kg)
    return

# ... rest of existing logic for recipes ...
```

### Phase 2: Migrate 2 Confirmed Imports (30 minutes)

#### 2.1 Magnesium Powder

**Create:** `kb/imports/magnesium_powder.yaml`
```yaml
id: import_magnesium_powder
kind: material
is_import: true
name: Magnesium powder (imported)
mass: 1.0
unit: kg
density: 1748
state: powder
material_class: magnesium
notes: |
  Imported magnesium powder for bootstrap. Used as feedstock for silicide formation.

  ISRU alternative: Extract from lunar regolith (MgO reduction) or seawater
  processing. Real ISRU route requires magnesium metal reduction from
  regolith-derived MgO or seawater Mg extraction.
isru_alternative: magnesium_powder_isru  # Future ISRU version
```

**Delete:** `kb/recipes/recipe_magnesium_powder_v0.yaml`

**Update:** `kb/items/materials/magnesium_powder_v0.yaml`
```yaml
# Remove the recipe field OR
# Change: recipe: recipe_magnesium_powder_v0
# To:     (delete the line - no recipe needed)
```

**Update References:** Search for `magnesium_powder_v0` in BOMs/recipes:
```bash
grep -r "magnesium_powder_v0" kb/boms/ kb/recipes/ kb/processes/
```
If BOMs reference it, they'll now correctly identify it as imported via closure analysis.

#### 2.2 Permanent Magnet Neodymium

**Create:** `kb/imports/permanent_magnet_neodymium.yaml`
```yaml
id: import_permanent_magnet_neodymium
kind: material
is_import: true
name: Permanent magnet (neodymium, imported)
mass: 1.0
unit: kg
material_class: neodymium_magnet
notes: |
  Imported NdFeB permanent magnet for bootstrap. Used in motors and generators.

  ISRU alternative: Requires powder metallurgy → sinter NdFeB alloy from Nd/Fe/B
  powders → grind/shape → magnetization. Complex rare earth extraction from
  regolith needed.
isru_alternative: permanent_magnet_neodymium_isru
```

**Delete:** `kb/recipes/recipe_permanent_magnet_neodymium_v0.yaml`

**Update:** Item file (if exists)
**Update References:** Search for usage

### Phase 3: Review 50 Items Without Recipes (2-4 hours)

For each of the 50 items without recipes, decide:

**Decision Tree:**
```
Is this a real item?
├─ NO → Delete item file (obsolete)
└─ YES → Should it be manufactured (ISRU)?
    ├─ YES → Create ISRU recipe
    └─ NO → Convert to import item
```

**Example Review Process:**
```bash
# Get list of items without recipes
python3 << 'EOF'
import yaml
from pathlib import Path

for item_file in Path("kb/items").rglob("*.yaml"):
    with open(item_file) as f:
        data = yaml.safe_load(f)
        if data and not data.get("recipe"):
            print(f"{item_file}\t{data.get('id')}\t{data.get('kind')}")
EOF

# For each item, decide: import, ISRU, or delete
```

**Recommendation:** Create script to assist:
```python
# tools/review_items_without_recipes.py
# Helps systematically review and categorize items
```

### Phase 4: Testing (30 minutes)

1. **Test indexer:**
```bash
python -m kbtool index
# Verify: kb/imports/ items are indexed
# Verify: No "missing recipe" errors for is_import items
```

2. **Test closure analysis:**
```bash
python -m kbtool mat-closure --machine hauler
# Verify: import_magnesium_powder shows in "Imported Items"
# Verify: Correct mass calculations
```

3. **Test circular dependency:**
```bash
# Verify circular dependencies still work with new import detection
```

## Migration Checklist

### Prerequisites
- [ ] Create `kb/imports/` directory
- [ ] Review ADR-007 and confirm approach

### Infrastructure (Phase 1)
- [ ] Update `kbtool/indexer.py` - imports folder support
- [ ] Update `kbtool/indexer.py` - skip "no recipe" for is_import
- [ ] Update `kbtool/closure_analysis.py` - check is_import field
- [ ] Test indexer with empty kb/imports/

### Magnesium Powder (Phase 2.1)
- [ ] Create `kb/imports/magnesium_powder.yaml`
- [ ] Delete `kb/recipes/recipe_magnesium_powder_v0.yaml`
- [ ] Update `kb/items/materials/magnesium_powder_v0.yaml` (remove recipe field)
- [ ] Test closure analysis

### Permanent Magnet (Phase 2.2)
- [ ] Create `kb/imports/permanent_magnet_neodymium.yaml`
- [ ] Delete `kb/recipes/recipe_permanent_magnet_neodymium_v0.yaml`
- [ ] Update item file (if exists)
- [ ] Test closure analysis

### Review Items (Phase 3)
- [ ] Generate list of 50 items without recipes
- [ ] Review each item: Import / ISRU / Delete
- [ ] Create import items as needed
- [ ] Create ISRU recipes as needed
- [ ] Delete obsolete items

### Final Testing (Phase 4)
- [ ] Run full indexer test
- [ ] Run closure analysis on 3+ machines
- [ ] Verify circular dependency handling
- [ ] Check validation report

## File Structure After Migration

```
kb/
├── imports/                              # NEW FOLDER
│   ├── magnesium_powder.yaml            # id: import_magnesium_powder
│   ├── permanent_magnet_neodymium.yaml  # id: import_permanent_magnet_neodymium
│   └── ... (more as Phase 3 progresses)
├── items/
│   └── materials/
│       ├── magnesium_powder_v0.yaml     # recipe field removed
│       └── ... (existing items)
├── recipes/
│   # recipe_magnesium_powder_v0.yaml DELETED
│   # recipe_permanent_magnet_neodymium_v0.yaml DELETED
│   └── ... (remaining recipes)
```

## Rollback Plan

If migration causes issues:

1. **Restore deleted recipes:**
```bash
git checkout kb/recipes/recipe_magnesium_powder_v0.yaml
git checkout kb/recipes/recipe_permanent_magnet_neodymium_v0.yaml
```

2. **Remove kb/imports/ folder:**
```bash
git rm -r kb/imports/
```

3. **Revert indexer/closure changes:**
```bash
git checkout kbtool/indexer.py kbtool/closure_analysis.py
```

## Success Criteria

Migration is successful when:
- [ ] Indexer runs without errors
- [ ] Import items show in index.json with `is_import: true`
- [ ] Closure analysis correctly identifies import items
- [ ] No "missing recipe" warnings for import items
- [ ] Circular dependency detection still works
- [ ] No regression in existing functionality

## Risks and Mitigation

| Risk | Impact | Mitigation |
|------|--------|------------|
| BOMs reference old item IDs | Medium | Update BOM references or use same IDs |
| Processes reference old items | Medium | Search and update all references |
| Indexer breaks with kb/imports/ | High | Test with empty folder first |
| Item ID collisions | Low | Use import_ prefix consistently |
| 50 items review takes longer | Medium | Phase 3 can be done incrementally |

## Timeline

**Immediate (Core Migration):** 2 hours
- Phase 1: 1 hour
- Phase 2: 30 minutes
- Phase 4: 30 minutes

**Extended (Full Review):** +2-4 hours
- Phase 3: Review 50 items without recipes

**Total:** 4-6 hours (vs original estimate of 4-8 hours)

## Notes

- The migration is much smaller than anticipated (only 2 confirmed imports)
- Most complexity is in Phase 3 (reviewing 50 items without recipes)
- Phase 3 can be done incrementally over time
- Core architecture can be deployed with just 2 items migrated
