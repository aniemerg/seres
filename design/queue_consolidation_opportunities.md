# Work Queue Consolidation Opportunities

**Generated**: 2025-12-22
**Purpose**: Identify and eliminate unnecessary queue items that are duplicates or state variations

## Summary

Estimated queue reduction: **~30-50 items** through consolidation

## 1. State-Change Materials (14 items → 0)

These materials represent physical states that should be handled in processes, not as separate materials:

### Can Use Base Material + Process Heat

| Queue Item | Should Use | Action |
|------------|------------|--------|
| `calcium_chloride_molten` | `calcium_chloride` | Update processes to reference base material |
| `water_vapor` | `water` | Process heats water; no separate item needed |
| `carbon_monoxide_gas` | `carbon_monoxide` | All CO is gas at STP; redundant suffix |
| `hydrochloric_acid_gas` | `hydrochloric_acid` | HCl is gas at STP; redundant |
| `silicon_monoxide_gas` | `silicon_monoxide` | Gas at process temps |

### Can Use Base Material + Dehydration/Hydration

| Queue Item | Should Use | Action |
|------------|------------|--------|
| `calcium_chloride_anhydrous` | `calcium_chloride` | Specify hydration state in process |
| `aluminum_chloride_anhydrous` | `aluminum_chloride` | Specify hydration state in process |
| `aluminum_chloride_hexahydrate` | `aluminum_chloride` | Specify hydration state in process |

### Can Use Base Material (Already Liquid/Solution)

| Queue Item | Should Use | Action |
|------------|------------|--------|
| `water_liquid` | `water` | Water is already liquid at STP |
| `silicon_tetrachloride_liquid` | `silicon_tetrachloride` | Liquid at STP |
| `iron_sulfate_solution` | `iron_sulfate` | Dissolved state; process detail |
| `sodium_aluminate_solution` | `sodium_aluminate` | Dissolved state; process detail |
| `titanyl_sulfate_solution` | `titanyl_sulfate` | Dissolved state; process detail |

### Special Case

| Queue Item | Issue |
|------------|-------|
| `filter_gas` | Unclear what this is; likely typo or wrong reference |

**Action**: Update all processes referencing these items to use base materials. Physical state is a process parameter, not a material ID.

## 2. Duplicate Items with Version Suffixes (1+ items)

### Carbon Electrode

| Queue Item | Existing Item | Action |
|------------|---------------|--------|
| `carbon_electrode` | `electrodes` (kb/items/parts/electrodes.yaml) | Update FFC processes to use `electrodes` |

**Evidence**:
- `kb/items/parts/electrodes.yaml` exists with "Electrodes for molten regolith electrolysis. Graphite or carbon construction"
- Multiple FFC processes reference `carbon_electrode`
- These are the same thing

## 3. BOM References for Existing Machines (1 confirmed)

| Queue BOM | Existing Machine | Action |
|-----------|------------------|--------|
| `bom_precision_grinding_system_v0.yaml` | `precision_grinding_system_v0.yaml` | Either create BOM or remove BOM reference from machine |

**Context**: The machine exists, queue wants its BOM. Per "incompleteness is a feature", BOM only needed if machine is a bottleneck.

## 4. Potential Machine Duplicates (Need Investigation)

These _v0 suffixed machines in queue might have non-versioned equivalents:

```
acid_resistant_reactor_v0     -> Check for acid_resistant_reactor
calcination_furnace_v0        -> We have multiple calcination processes
chlorine_handling_system_v0   -> Might be generic chlorine_handling
cryogenic_chiller_v0          -> Check for cryogenic_chiller
solar_concentrator_v0         -> Check for solar_concentrator
solar_concentrator_high_temp_v0 -> Might consolidate with above
```

**Action**: Search for non-versioned equivalents before creating these.

## 5. Implementation Plan

### Phase 1: State-Change Materials (Quick Win)

1. **Update processes using state-change materials**:
   - Search for all processes using the 14 state-change materials
   - Update to reference base materials
   - Add notes about physical state if critical

2. **Pattern to follow**:
   ```yaml
   # BEFORE
   inputs:
     - item_id: calcium_chloride_molten
       qty: 1.0
       unit: kg

   # AFTER
   inputs:
     - item_id: calcium_chloride
       qty: 1.0
       unit: kg
   notes: |
     Process operates at 900-1100°C where CaCl2 is molten.
     Electrolyte is recycled; 10% makeup required.
   ```

3. **Verify no material definitions exist** for state-change items (they shouldn't)

### Phase 2: Carbon Electrode Consolidation

1. Update FFC processes:
   - `ffc_calcium_extraction_v0.yaml`
   - `ffc_magnesium_extraction_v0.yaml`
   - And others using `carbon_electrode`

2. Change `carbon_electrode` → `electrodes`

3. Verify `electrodes` material_class and properties match usage

### Phase 3: Review _v0 Duplicates

1. For each _v0 machine in queue, search for non-versioned equivalent
2. If found: update references to use canonical name
3. If not found: determine if _v0 suffix is needed or artifact

### Phase 4: BOM Cleanup

1. Review high-priority BOM references
2. For each, decide:
   - Create BOM if machine is bottleneck
   - Remove BOM reference from machine if not needed
3. Document pattern: "BOMs created on demand for bottleneck analysis"

## Expected Impact

### Queue Reduction
- State-change materials: -14 referenced_only items
- Carbon electrode: -1 referenced_only item
- BOM consolidation: -5 to -10 referenced_only items (estimated)
- _v0 duplicates: -5 to -10 items (after investigation)

**Total estimated reduction**: 25-35 items from 346 → ~310-320

### Code Quality
- More consistent material naming
- Clearer separation of material vs. process state
- Reduced KB bloat
- Easier to understand dependency graphs

## Related Issues

### Why State-Change Items Appear in Queue

Processes were written referencing specific states because:
1. Chemical accuracy (molten CaCl2 vs solid)
2. Process clarity (water vapor vs liquid water)
3. Import from papers that specify states

However, for KB purposes:
- Material ID = chemical identity
- Physical state = process parameter
- Exception: Allotropes (graphite vs diamond) may need separate IDs

### Material vs. Process State Principle

**Material identity**: Chemical composition (CaCl2, H2O, Al2Cl6)
**Process state**: Temperature, pressure, phase, concentration

The material definition can note typical state:
```yaml
id: calcium_chloride
material_class: salt
state: solid
notes: Solid at STP. Melts at 772°C. Used molten in FFC electrolysis.
```

But process should reference base material and specify conditions in notes.

## Next Steps

1. Get user approval for consolidation approach
2. Start with state-change materials (highest impact, lowest risk)
3. Update processes systematically
4. Re-run indexer to verify queue reduction
5. Document pattern for future material additions
