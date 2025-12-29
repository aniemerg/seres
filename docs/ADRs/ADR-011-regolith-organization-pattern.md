# ADR-011: Regolith Organization Pattern

**Status:** Accepted
**Date:** 2025-12-28
**Decision Makers:** Allan Niemerg

## Context

The knowledge base contains multiple regolith types representing different lunar locations and compositions (highlands, mare, carbonaceous meteorite sites, polar ice deposits). However, the current organization is inconsistent:

1. **Inconsistent Patterns:**
   - Some extraction processes use raw regolith types directly (e.g., `alumina_extraction_from_highlands_v0` uses `regolith_lunar_highlands`)
   - Other processes use a generic intermediate (`regolith_excavated`) made only from mare regolith
   - 22 processes use `regolith_excavated` as input, creating composition mismatches

2. **Compositional Mismatches:**
   - `regolith_excavated` is made from `regolith_lunar_mare` (0% ice content)
   - `polar_water_ice_extraction_v0` uses `regolith_excavated` as input but yields 5.6% water
   - Where does the ice come from? The input doesn't contain ice.

3. **Missing Regolith Type:**
   - Polar permanently shadowed crater (PSC) regolith is compositionally distinct (5.6% H2O ice)
   - No dedicated raw material for PSC regolith
   - Water extraction process uses wrong input material

4. **Unclear Semantics:**
   - `regolith_mining_simple_v0` outputs `regolith_lunar_mare` (not obvious from name)
   - Generic `lunar_regolith_in_situ` has unspecified composition
   - Difficult to trace location → composition → products

## Decision

**Adopt a unified location-specific regolith pattern across all regolith types.**

### Standard Pattern

Every distinct lunar location/deposit type shall follow this pattern:

```
┌─────────────────────────────────────────┐
│ Step 1: Mining Process                 │
│   Input: None (free collection)        │
│   Output: Raw Regolith Type            │
│   Location: kb/processes/              │
│   Naming: regolith_mining_<location>   │
└─────────────────────────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│ Raw Regolith Material                   │
│   Location: kb/items/raw_materials/    │
│   Naming: regolith_<location>          │
│   Properties: Defined composition       │
└─────────────────────────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│ Step 2: Extraction Process             │
│   Input: Specific raw regolith         │
│   Output: Products + tailings          │
│   Yields match input composition       │
└─────────────────────────────────────────┘
```

### Complete Regolith Taxonomy

| Regolith Type | Location | Key Composition | Mining Process | Primary Use |
|---------------|----------|-----------------|----------------|-------------|
| `regolith_lunar_highlands` | Highland regions | Al-rich (12% Al2O3) | `regolith_mining_lunar_highlands_v0` | Alumina extraction |
| `regolith_lunar_mare` | Mare regions | Fe-rich (15% FeO, 10% TiO2) | `regolith_mining_simple_v0` | Iron/titanium extraction |
| `regolith_carbonaceous` | Meteorite impacts | C-rich (3% C, 10% H2O) | `regolith_mining_carbonaceous_v0` | Carbon extraction |
| `regolith_polar_psc` | Polar PSCs | Ice-rich (5.6% H2O) | `regolith_mining_polar_psc_v0` | Water extraction |

### Deprecation

- **Deprecate:** `regolith_excavated` intermediate material
- **Rationale:** Unnecessary abstraction that obscures composition and creates mismatches
- **Migration:** Update all 22 processes using `regolith_excavated` to use appropriate raw regolith types based on their extraction chemistry

## Consequences

### Positive

1. **Compositional Integrity:** Input composition matches output yields
2. **Clear Traceability:** Direct link from location → composition → products
3. **No Unnecessary Intermediates:** Simpler material flow
4. **Scalable:** Easy to add new location-specific regolith types
5. **Simulation Accuracy:** Yields based on documented composition
6. **Semantic Clarity:** Item names clearly indicate source location

### Negative

1. **Breaking Change:** 22 processes must be updated
2. **Migration Effort:** All references to `regolith_excavated` must be resolved
3. **Less Generic:** Cannot write "accepts any regolith" processes (but this was false abstraction anyway)

### Neutral

1. **Recipe Complexity:** Similar number of recipes (replace 1 generic with 4 specific)
2. **Item Count:** Net change minimal (add 1 PSC regolith, deprecate 1 excavated)

## Implementation Plan

### Phase 1: Create Polar Ice Regolith (Immediate)

1. Create `kb/items/raw_materials/regolith_polar_psc.yaml`
2. Create `kb/processes/regolith_mining_polar_psc_v0.yaml`
3. Create `kb/recipes/recipe_regolith_polar_psc_v0.yaml`
4. Update `kb/processes/polar_water_ice_extraction_v0.yaml` to use `regolith_polar_psc`

### Phase 2: Migrate Processes from regolith_excavated (Immediate)

1. Identify all 22 processes using `regolith_excavated` as input
2. For each process, determine appropriate raw regolith type:
   - Iron/titanium extraction → `regolith_lunar_mare`
   - Aluminum/calcium extraction → `regolith_lunar_highlands`
   - Carbon extraction → `regolith_carbonaceous`
   - Silicon extraction → context-dependent (highlands are silica-rich)
3. Update process inputs to use specific regolith types
4. Verify yields match updated input compositions

### Phase 3: Deprecate regolith_excavated (Immediate)

1. Move `kb/items/materials/regolith_excavated.yaml` to `kb/deprecated/`
2. Move `kb/processes/regolith_excavation_processing_v0.yaml` to `kb/deprecated/`
3. Move `kb/recipes/recipe_regolith_excavated_v0.yaml` to `kb/deprecated/`
4. Add deprecation notes explaining migration path

### Phase 4: Validation (Immediate)

1. Run closure analysis to verify no broken dependencies
2. Run KB validation
3. Test simulation with new pattern
4. Update documentation

## Naming Conventions

### Raw Regolith Items
- **Pattern:** `regolith_<location>_<variant>`
- **Location:** `kb/items/raw_materials/`
- **Examples:** `regolith_lunar_highlands`, `regolith_polar_psc`

### Mining Processes
- **Pattern:** `regolith_mining_<location>_v<N>`
- **Inputs:** None (free collection)
- **Outputs:** Corresponding raw regolith type
- **Examples:** `regolith_mining_lunar_highlands_v0`, `regolith_mining_polar_psc_v0`

### Extraction Processes
- **Pattern:** `<product>_extraction_from_<regolith_type>_v<N>`
- **Inputs:** Specific raw regolith type
- **Outputs:** Extracted products + tailings
- **Examples:** `alumina_extraction_from_highlands_v0`, `water_extraction_from_polar_psc_v0`

## Related ADRs

- **ADR-007:** Import Items Organization (establishes pattern for kb/imports/ vs kb/items/)
- This ADR establishes pattern for regolith organization within raw_materials

## References

- `design/regolith_pattern_analysis.md` - Initial pattern inconsistency analysis
- `design/regolith_organization_proposal.md` - Detailed proposal with options
- Polar water ice data: LCROSS impact (5.6% ± 2.9% H2O concentration in PSCs)
- Lunar regolith compositions: Apollo samples, orbital spectroscopy

## Notes

- `lunar_regolith_in_situ` remains as generic placeholder but should be avoided in favor of specific types
- Consider renaming `regolith_mining_simple_v0` to `regolith_mining_lunar_mare_v0` for clarity (future work)
- Polar PSC regolith composition (excluding ice) assumed similar to local highland/mare mixture
