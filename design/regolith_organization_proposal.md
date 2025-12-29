# Regolith Organization Proposal

## Current State

### Raw Regolith Types (kb/items/raw_materials/)

| Item ID | Location/Source | Key Composition | Mining Process |
|---------|----------------|-----------------|----------------|
| `regolith_lunar_highlands` | Highland regions | Al-rich (12% Al2O3, 5% FeO) | regolith_mining_lunar_highlands_v0 |
| `regolith_lunar_mare` | Mare regions | Fe-rich (15% FeO, 10% TiO2) | regolith_mining_simple_v0 |
| `regolith_carbonaceous` | Meteorite impacts | C-rich (3% C, 10% H2O) | regolith_mining_carbonaceous_v0 |
| `lunar_regolith_in_situ` | Generic surface | Unspecified | environment_source_v0 |
| **MISSING** | **Polar PSCs** | **Ice-rich (5.6% H2O)** | **None** |

### Intermediate Materials (kb/items/materials/)

- `regolith_excavated` - Generic "screened" regolith made from regolith_lunar_mare
- `regolith_crushed`, `regolith_powder`, `regolith_coarse_fraction`, `regolith_fine_fraction` - Various processed forms
- Construction materials - `regolith_concrete_polymer_v0`, `sulfur_concrete_regolith_v0`, etc.

### Current Pattern Inconsistency

**Pattern A (Direct Use):**
```
regolith_mining_lunar_highlands_v0: [] → regolith_lunar_highlands
alumina_extraction_from_highlands_v0: regolith_lunar_highlands → alumina_powder + tailings
```

**Pattern B (Via Intermediate):**
```
regolith_mining_simple_v0: [] → regolith_lunar_mare
regolith_excavation_processing_v0: regolith_lunar_mare → regolith_excavated
ilmenite_extraction_from_regolith_v0: regolith_excavated → iron_ore_or_ilmenite + tailings
```

**Problem:** 22 processes use `regolith_excavated` but it's only made from mare regolith, creating composition mismatches.

---

## Proposed Unified Pattern

### Principle: Location-Specific Raw Materials

Each distinct lunar location/deposit type should have its own raw regolith material with documented composition.

### Standard Pattern for All Regoliths

```
┌─────────────────────────────────────────────────────────────┐
│ Step 1: Mining (No Inputs)                                  │
│   Mining Process → Raw Regolith Type                        │
│   - Location-specific                                        │
│   - Defined composition                                      │
│   - In kb/items/raw_materials/                              │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ Step 2: Extraction/Processing (Direct Use)                  │
│   Extraction Process: Raw Regolith → Products               │
│   - Uses raw regolith directly                              │
│   - Yields match composition                                │
│   - Clear traceability                                       │
└─────────────────────────────────────────────────────────────┘
```

---

## Complete Regolith Taxonomy

### 1. Highland Regolith
**Item:** `regolith_lunar_highlands`
**Location:** Highland regions (anorthositic crust)
**Mining:** `regolith_mining_lunar_highlands_v0`
**Composition:** Al-rich (12% Al2O3, 5% FeO, 2% TiO2, 45% SiO2, 15% CaO)
**Primary Use:** Alumina extraction
**Example:** `alumina_extraction_from_highlands_v0: regolith_lunar_highlands → alumina_powder`

### 2. Mare Regolith
**Item:** `regolith_lunar_mare`
**Location:** Mare regions (basaltic lowlands)
**Mining:** `regolith_mining_simple_v0`
**Composition:** Fe-rich (15% FeO, 10% TiO2, 8% Al2O3, 20% SiO2)
**Primary Use:** Iron/titanium extraction, general feedstock
**Example:** `ilmenite_extraction_from_regolith_v0: regolith_lunar_mare → iron_ore_or_ilmenite` (should be updated)

### 3. Carbonaceous Regolith
**Item:** `regolith_carbonaceous`
**Location:** Meteorite impact sites
**Mining:** `regolith_mining_carbonaceous_v0`
**Composition:** C-rich (3% C, 10% H2O, 25% FeO, 35% SiO2)
**Primary Use:** Carbon extraction, volatile extraction
**Example:** `carbon_extraction_from_carbonaceous_v0: regolith_carbonaceous → carbon_powder`

### 4. Polar Ice Regolith (NEW)
**Item:** `regolith_polar_psc` ← **CREATE THIS**
**Location:** Permanently shadowed craters (PSCs)
**Mining:** `regolith_mining_polar_psc_v0` ← **CREATE THIS**
**Composition:** Ice-bearing (5.6% H2O ice, remainder similar to local highland/mare)
**Primary Use:** Water extraction
**Example:** `polar_water_ice_extraction_v0: regolith_polar_psc → water + dry_regolith` ← **UPDATE THIS**

### 5. Generic In-Situ Regolith
**Item:** `lunar_regolith_in_situ`
**Location:** Generic surface (no specific composition)
**Mining:** `environment_source_v0` (free source)
**Composition:** Unspecified
**Primary Use:** Placeholder, generic feedstock
**Status:** Consider deprecating in favor of specific types

---

## Migration Plan

### Phase 1: Create Polar Ice Regolith (Immediate)

1. **Create** `kb/items/raw_materials/regolith_polar_psc.yaml`
   - Composition: 5.6% H2O ice, base composition similar to local regolith
   - Mass, density, particle properties

2. **Create** `kb/processes/regolith_mining_polar_psc_v0.yaml`
   - Mining process: [] → regolith_polar_psc
   - Special equipment: drilling_equipment_v0 (ice-cemented regolith harder than loose regolith)
   - Rate: Lower than mare mining (50 kg/hr vs 100 kg/hr) due to hard ice-cement
   - Energy: Higher (drilling concrete-hard frozen regolith)

3. **Create** `kb/recipes/recipe_regolith_polar_psc_v0.yaml`
   - Links recipe to mining process

4. **Update** `kb/processes/polar_water_ice_extraction_v0.yaml`
   - Change input from `regolith_excavated` to `regolith_polar_psc`
   - Composition now matches (5.6% ice input → 5.6% water output)

### Phase 2: Resolve regolith_excavated (Medium Term)

**Option A: Deprecate regolith_excavated** (Most consistent)
- Update all 22 processes to use appropriate raw regolith types
- `ilmenite_extraction_from_regolith_v0`: regolith_lunar_mare → ilmenite
- `silicon_extraction`: regolith_lunar_highlands → silicon (highlands are silica-rich)
- Etc.

**Option B: Make regolith_excavated location-agnostic** (Pragmatic)
- Create multiple recipes:
  - `recipe_regolith_excavated_mare_v0`: regolith_lunar_mare → regolith_excavated
  - `recipe_regolith_excavated_highlands_v0`: regolith_lunar_highlands → regolith_excavated
  - `recipe_regolith_excavated_carbonaceous_v0`: regolith_carbonaceous → regolith_excavated
- Document that regolith_excavated composition varies by source
- Processes using it accept "generic screened regolith" from any source
- Add composition metadata to track source

**Recommendation:** Option A (deprecate) for clarity, but Option B if 22-process update is too disruptive.

### Phase 3: Standardize Extraction Processes (Long Term)

- Review all extraction processes to ensure they use appropriate regolith types
- Verify yields match composition
- Document source assumptions
- Update process notes with compositional rationale

---

## Naming Conventions

### Raw Regolith Items
- Pattern: `regolith_<location>_<variant>`
- Location in: `kb/items/raw_materials/`
- Examples:
  - `regolith_lunar_highlands`
  - `regolith_lunar_mare`
  - `regolith_polar_psc` (permanently shadowed craters)
  - `regolith_carbonaceous` (meteorite sites)

### Mining Processes
- Pattern: `regolith_mining_<location>_v<N>`
- No inputs (free collection)
- Output: Corresponding raw regolith type
- Examples:
  - `regolith_mining_lunar_highlands_v0`
  - `regolith_mining_simple_v0` (mare) ← consider renaming to `regolith_mining_lunar_mare_v0`
  - `regolith_mining_polar_psc_v0` (new)
  - `regolith_mining_carbonaceous_v0`

### Extraction Processes
- Pattern: `<product>_extraction_from_<regolith_type>_v<N>`
- Input: Specific raw regolith type
- Output: Extracted products + tailings
- Examples:
  - `alumina_extraction_from_highlands_v0`
  - `ilmenite_extraction_from_mare_v0` (should rename/update)
  - `water_extraction_from_polar_psc_v0` (consider renaming polar_water_ice_extraction_v0)
  - `carbon_extraction_from_carbonaceous_v0`

---

## Benefits of This Organization

1. **Compositional Integrity:** Input composition matches output yields
2. **Location Traceability:** Clear link from location → composition → products
3. **No Unnecessary Intermediates:** Direct raw regolith → products
4. **Scalable:** Easy to add new regolith types (e.g., regolith_south_pole_aitken)
5. **Simulation Accuracy:** Yields based on actual composition data
6. **Clear Semantics:** Item name tells you where it comes from

---

## Implementation Priority

**High Priority (Do First):**
- Create `regolith_polar_psc` raw material
- Create `regolith_mining_polar_psc_v0` process
- Update `polar_water_ice_extraction_v0` to use polar PSC regolith

**Medium Priority (Next):**
- Decide on regolith_excavated: deprecate or make multi-source
- Update ilmenite_extraction and silicon_extraction to use appropriate sources

**Low Priority (Cleanup):**
- Standardize naming: `regolith_mining_simple_v0` → `regolith_mining_lunar_mare_v0`
- Review all 22 processes using regolith_excavated
- Consolidate or deprecate `lunar_regolith_in_situ` if not needed

---

## Questions to Resolve

1. **regolith_excavated fate:** Deprecate or multi-source?
2. **Composition for regolith_polar_psc:** Should it be highlands-based or mare-based composition (minus ice)?
3. **Process renaming:** Update `regolith_mining_simple_v0` to `regolith_mining_lunar_mare_v0` for consistency?
4. **lunar_regolith_in_situ:** Keep as generic catchall or deprecate?
