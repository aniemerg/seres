# Regolith Pattern Analysis

## Pattern Inconsistency Found

### Standard Regolith Pattern

**Raw Material Items:**
- `regolith_lunar_mare` - Iron-rich mare regolith
- `regolith_lunar_highlands` - Aluminum-rich highland regolith
- `lunar_regolith_in_situ` - Generic in-place regolith

**Acquisition Pattern:**
```
Mining Process (no inputs) → Raw Regolith
```

**Examples:**
- `regolith_mining_simple_v0`: [] → regolith_lunar_mare (100 kg/hr)
- `regolith_mining_lunar_highlands_v0`: [] → regolith_lunar_highlands (100 kg/hr)
- `environment_source_v0`: [] → lunar_regolith_in_situ (free)

**Processing Pattern:**
```
Raw Regolith → Processing → Derived Materials
```

**Examples:**
- `alumina_extraction_from_highlands_v0`: regolith_lunar_highlands → alumina_powder + tailings
- (But see issue below)

---

## Polar Ice Extraction Pattern (INCONSISTENT)

**Current Pattern:**
```
regolith_lunar_mare (raw)
  ↓ [regolith_excavation_processing_v0]
regolith_excavated (intermediate)
  ↓ [polar_water_ice_extraction_v0]
water + regolith_crushed
```

**Why Inconsistent:**
1. Polar ice extraction uses `regolith_excavated` (intermediate processed material)
2. Other extractions should use raw regolith directly but many use `regolith_excavated`
3. Creates extra processing step not needed for other regolith types

---

## Widespread Use of regolith_excavated

**22 processes use `regolith_excavated` as input:**
- polar_water_ice_extraction_v0
- ilmenite_extraction_from_regolith_v0
- silicon_extraction_from_regolith_carbothermic_v0
- silicon_extraction_from_regolith_magnesiothermic_v0
- forsterite_extraction_from_regolith_v0
- mineral_ore_sulfide_extraction_v0
- regolith_heating_water_extraction_v0
- And 15 more...

**This suggests:**
- `regolith_excavated` may be *intentionally* used as a common intermediate
- Represents "processed/screened" regolith ready for chemical processing
- But conflicts with direct use of regolith_lunar_highlands in alumina_extraction

---

## Two Possible Interpretations

### Interpretation A: regolith_excavated is Wrong Pattern

**Should be:**
- Create specific raw regolith types for each source
- Example: `regolith_polar_ice` as a raw material
- Mining process: [] → regolith_polar_ice
- Extraction: regolith_polar_ice → water + dry_regolith

**Pros:**
- Matches pattern of regolith_lunar_highlands/mare
- Each regolith type represents distinct composition
- Mining processes output raw materials directly

**Cons:**
- 22 processes would need updating
- Loses common intermediate abstraction

### Interpretation B: regolith_excavated is Correct Pattern

**Should be:**
- `regolith_excavated` represents generic "screened/prepared" regolith
- Derived from whichever raw type is available (mare, highlands, etc.)
- Extraction processes use generic excavated regolith as input
- Composition varies based on source location

**Pros:**
- Already used by 22 processes
- Provides common abstraction for "prepared regolith"
- Mirrors real ISRU where location determines composition

**Cons:**
- alumina_extraction_from_highlands_v0 breaks pattern (uses raw highlands directly)
- Polar ice should be location-specific (PSC regolith, not generic)
- Loses compositional specificity

---

## Polar Ice Specific Issue

**Real-world consideration:**
- Polar ice is found in permanently shadowed craters (PSCs)
- PSC regolith is NOT the same as mare or highlands regolith
- Contains 5.6% water ice (vs. <0.05% in normal regolith)
- Should probably be its own distinct regolith type

**Current behavior:**
- `regolith_excavated` is made from `regolith_lunar_mare` (0% ice content)
- Used as input to `polar_water_ice_extraction_v0` (5.6% yield)
- Compositional mismatch: where does the ice come from?

---

## Recommendation

**Option 1 (Most Consistent):** Create location-specific raw regoliths
- `regolith_polar_psc` - Permanently shadowed crater regolith (5.6% H2O ice)
- Mining: [] → regolith_polar_psc
- Extraction: regolith_polar_psc → water + dry_regolith

**Option 2 (Medium Effort):** Fix composition assumption
- Keep `regolith_excavated` intermediate
- Document that excavated regolith composition depends on location
- `recipe_regolith_excavated_v0` should have variants for different sources
- Polar variant would source from PSC locations (with ice content)

**Option 3 (Minimal Change):** Document inconsistency
- Accept that regolith_excavated is a generic intermediate
- Note that actual yields vary by location
- Process notes explain compositional assumptions

---

## Files Referenced

**Raw Regolith Items:**
- kb/items/raw_materials/regolith_lunar_highlands.yaml
- kb/items/raw_materials/regolith_lunar_mare.yaml
- kb/items/raw_materials/lunar_regolith_in_situ.yaml

**Intermediate Materials:**
- kb/items/materials/regolith_excavated.yaml

**Recipes:**
- kb/recipes/recipe_regolith_lunar_highlands_v0.yaml (mining)
- kb/recipes/recipe_regolith_lunar_mare_v0.yaml (mining)
- kb/recipes/recipe_lunar_regolith_in_situ_v0.yaml (free source)
- kb/recipes/recipe_regolith_excavated_v0.yaml (mare → excavated)

**Processes:**
- kb/processes/regolith_mining_simple_v0.yaml ([] → mare)
- kb/processes/regolith_mining_lunar_highlands_v0.yaml ([] → highlands)
- kb/processes/alumina_extraction_from_highlands_v0.yaml (highlands → alumina)
- kb/processes/ilmenite_extraction_from_regolith_v0.yaml (excavated → ilmenite)
- kb/processes/polar_water_ice_extraction_v0.yaml (excavated → water)

**Analysis:**
- simulation_learnings.md shows ilmenite_extraction_from_regolith_v0 is heavily used
- 22 processes depend on regolith_excavated pattern
