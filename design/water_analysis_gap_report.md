# Water Usage in ISRU Analysis - Gap Analysis

## Current State

### Water Items Found:
- `water` - Pure water material (1 kg)
- `water_isru_train_v0` - Water extraction equipment
- Machines: water_electrolyzer, water_purification, thermal_water_extractor

### Water Extraction:
- **Process:** `polar_water_ice_extraction_v0`
- **Source:** Permanently shadowed craters (polar ice deposits)
- **Yield:** 5.6% H2O by mass from frozen regolith
- **Output:** 56 kg water per 1000 kg regolith
- **Notes:** ~140× higher concentration than regolith volatiles

### Current Water Usage (Found in ~20+ processes):
- Electrolysis (chloralkali, water electrolysis)
- Chemical synthesis (calcium chloride, ammonia recovery, cryolite)
- Cooling/heat transfer
- Ceramic forming (binder)
- Cutting fluid formulation
- Acid/base reactions

### Analytical Equipment Found:
1. `gamma_ray_spectrometer_v0` - KREEP detection, ore prospecting (IMPORT)
2. `microscope_inspection_stereo` - Visual inspection (IMPORT)
3. `optical_microscope_v0` - Visual/optical inspection
4. `spectrometer_simple_prism_v0` - Basic optical spectroscopy

## Major Gaps for In Situ Analysis

### Missing Analytical Instruments:
1. **XRF (X-ray Fluorescence)** - Elemental composition analysis
   - Critical for ore assay, quality control
   - Non-destructive
   - No water needed (dry method)

2. **XRD (X-ray Diffraction)** - Mineralogy/crystal structure
   - Identify mineral phases
   - Process control
   - No water needed (dry method)

3. **ICP-MS/ICP-OES** - High-precision elemental analysis
   - **USES WATER** - Samples dissolved in acid/water
   - Trace element detection
   - Quality control for metals

4. **Gas Chromatograph** - Volatile analysis
   - May use water in some methods
   - Critical for atmosphere monitoring

5. **Wet Chemistry Lab Equipment:**
   - Titration equipment
   - pH meters  
   - Beakers, burettes, pipettes
   - **ALL USE WATER** as solvent/reagent

### Missing Analysis Processes:
1. **Sample preparation:**
   - Dissolution (acid + water)
   - Filtration (water washing)
   - Dilution (water-based)

2. **Wet chemistry assays:**
   - Titration for metal content
   - Gravimetric analysis
   - Precipitation reactions
   - **ALL REQUIRE WATER**

3. **Quality control:**
   - Chemical purity testing
   - Composition verification
   - Contamination detection

4. **Ore characterization:**
   - Grade determination
   - Impurity analysis
   - Recovery optimization

## Why This Matters

### Current Problem:
The KB has extensive **production** processes but minimal **analytical** processes.
You can't optimize ISRU without knowing:
- What's in your ore?
- Is your product pure enough?
- What's contaminating your stream?
- Is your process efficient?

### Water's Role in Analysis:
- **Solvent:** Dissolves samples for analysis
- **Reagent:** pH adjustment, precipitation, complexation
- **Standard preparation:** Diluting reference materials
- **Cleaning:** Equipment between analyses
- **Mobile phase:** Chromatography

### Real-World ISRU Example:
To refine aluminum from regolith:
1. Mine regolith (production ✓)
2. **ANALYZE composition** (MISSING ❌)
3. Optimize beneficiation (production ✓)
4. **VERIFY concentrate grade** (MISSING ❌)
5. Smelt aluminum (production ✓)
6. **TEST purity** (MISSING ❌)
7. Alloy/cast (production ✓)

**Steps 2, 4, 6 all need analytical capabilities using water!**

## Recommendations

### High Priority (Dry Methods):
1. Add XRF spectrometer + analysis process
2. Add XRD diffractometer + mineralogy process
3. Add optical emission spectrometer

### Medium Priority (Wet Chemistry):
4. Add wet chemistry lab equipment
5. Add titration analysis processes
6. Add sample dissolution processes
7. Add filtration/washing processes

### Low Priority (Advanced):
8. Add ICP-MS/ICP-OES equipment
9. Add gas chromatograph
10. Add automated analyzers

### Water Budget Impact:
- Analytical water usage: ~1-10 kg/day for small lab
- Recoverable via distillation: ~80-90%
- Net consumption: ~0.1-1 kg/day
- **Much smaller than production needs (cooling, synthesis)**

## Example Missing Items/Processes

### Items to Create:
- `xrf_spectrometer` (machine)
- `xrd_diffractometer` (machine)
- `wet_chemistry_lab_basic` (machine)
- `titration_equipment_set` (part)
- `ph_meter` (part)
- `analytical_balance` (part)
- `sample_vial_set` (part)
- `analytical_reagent_set` (material, water-based)

### Processes to Create:
- `xrf_analysis_elemental_v0` (outputs: composition_data)
- `xrd_analysis_mineralogy_v0` (outputs: phase_data)
- `sample_dissolution_acid_v0` (**uses water**)
- `titration_analysis_metal_v0` (**uses water**)
- `ore_assay_wet_chemistry_v0` (**uses water**)
- `purity_test_precipitation_v0` (**uses water**)

