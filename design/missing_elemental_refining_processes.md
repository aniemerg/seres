# Missing Elemental Refining Processes - Research Gap Analysis

**Date:** 2025-12-22
**Purpose:** Identify elemental and material refining processes described in research literature (especially Alex Ellery's work) that are not yet defined in our knowledge base.

**Summary:** This document catalogs ALL elemental refining processes found in the research literature in `design/papers/`, with special attention to processes that convert in-situ lunar/planetary resources into pure elements and useful materials. Each process is marked as either **[HAVE]** (already in KB) or **[MISSING]** (not yet defined).

---

## 1. PRIMARY OXYGEN EXTRACTION PROCESSES

### 1.1 Hydrogen Reduction of Ilmenite - **[HAVE]**
- **Process:** FeTiO3 + H2 → Fe + TiO2 + H2O
- **KB Reference:** `iron_reduction_from_ilmenite_v0.yaml`, `iron_pure_production_from_ilmenite_v0.yaml`
- **Input:** Ilmenite (FeTiO3), Hydrogen gas (H2)
- **Output:** Iron (Fe), Titanium dioxide (TiO2), Water (H2O)
- **Temperature:** 900-1000°C
- **Secondary step:** 2H2O → 2H2 + O2 (water electrolysis)
- **Source Papers:** FFC-process-for-deep-ISRU.txt, ellery-et-al-2022-metalysis-fray-farthing-chen-process
- **Performance:** 1-2% oxygen by mass from bulk regolith

### 1.2 Hydrogen Reduction of Ulvospinel - **[MISSING]**
- **Process:** Fe2TiO4 + H2 → TiO2 + 2Fe + H2O
- **Input:** Ulvospinel (Fe2TiO4), Hydrogen
- **Output:** Titanium dioxide, Iron, Water
- **Temperature:** 900-1000°C
- **Source Papers:** FFC-process-for-deep-ISRU.txt
- **Notes:** Similar to ilmenite reduction; ulvospinel is a spinel mineral found in lunar basalts

### 1.3 Carbothermal Reduction - Methane Route - **[PARTIAL]**
- **Process:**
  - FeTiO3 + CH4 → Fe + TiO2 + CO + 2H2
  - MgSiO3 + 2CH4 → Si + MgO + 2CO + 4H2 (enstatite)
  - CaSiO3 + 2CH4 → Si + CaO + 2CO + 4H2 (wollastonite)
  - CO + 3H2 → CH4 + H2O (recycling loop)
- **KB Status:** Have `methane_pyrolysis_v0.yaml` and `methane_pyrolysis_basic_v0.yaml`, but not comprehensive mineral-specific routes
- **Temperature:** 1600°C
- **Source Papers:** FFC-process-for-deep-ISRU.txt, NASA-ISRU-Progress-2012.txt
- **Performance:** 15-20% oxygen by mass from bulk regolith

### 1.4 Vacuum Pyrolysis - **[MISSING]**
- **Process:**
  - FeTiO3 → Fe + TiO2 + ½O2
  - MgSiO3 → SiO + MgO + ½O2
  - CaSiO3 → SiO + CaO + ½O2
- **Input:** Lunar regolith minerals
- **Output:** Pure metals, metal oxides, Oxygen gas
- **Temperature:** 2000-2600°C
- **Source Papers:** FFC-process-for-deep-ISRU.txt, Heat-Pipe-Solar-Receiver-O2-2009.txt
- **Notes:** Very high temperature process; requires extreme solar concentration or nuclear heat

### 1.5 Sulfuric Acid Route for Ilmenite - **[MISSING]**
- **Process:**
  - FeTiO3 + 2H2SO4 → FeSO4 + TiOSO4 + 2H2O
  - FeSO4 + H2O → Fe + ½O2 + H2SO4 (electrolysis, recycles acid)
  - TiOSO4 + H2O → H2SO4 + TiO2 (hydrolysis, recycles acid)
- **Input:** Ilmenite, Concentrated sulfuric acid
- **Output:** Iron, Titanium dioxide, Oxygen (acid recycled)
- **Temperature:** Elevated
- **Source Papers:** FFC-process-for-deep-ISRU.txt
- **Notes:** Acid must be recycled; more complex process chain

### 1.6 Molten Regolith Electrolysis (MRE) - **[HAVE]**
- **Process:** Direct electrochemical processing of molten lunar regolith
- **KB Reference:** `oxygen_extraction_molten_regolith_electrolysis_v0.yaml`
- **Input:** Molten lunar regolith (all oxide species)
- **Output:** Gaseous O2 at anode, liquid metals at cathode
- **Temperature:** 1600-1900°C
- **Source Papers:** NASA-ISRU-Progress-2012.txt, UCF-ISRU-Modeling-Optimization.txt
- **Oxygen yield:** 20-30% by mass from bulk regolith
- **Notes:** High performance but high risk; can extract multiple metals simultaneously

---

## 2. METALYSIS FFC CAMBRIDGE PROCESS

### 2.1 FFC Process - General Metal Oxide Reduction - **[HAVE]**
- **Process:** Metal oxide (sintered powder) + CaCl2 electrolyte + voltage → Metal + O2
- **KB Reference:** `metalysis_ffc_reduction_v0.yaml`, `ffc_temperature_optimization_v0.yaml`
- **Electrode reactions:**
  - Cathode: MeOx + 2xe- → Me + xO2-
  - Anode: C + O2- → CO + 2e- or C + 2O2- → CO2 + 4e-
- **Operating conditions:**
  - Temperature: 900-1100°C
  - Voltage: 2.5-3V typical
  - Electrolyte: Molten calcium chloride
- **Output:** High-purity metals (>99% pure), O2 gas, CO/CO2
- **Applicable metals:** Al, Ti, Fe, Si, Ca, Mg, and alloys
- **Source Papers:** ellery-et-al-2022-metalysis-fray-farthing-chen-process, FFC-process-for-deep-ISRU.txt
- **Notes:** Universal processor for oxides; solid-state (metals don't melt)

### 2.2 Titanium Extraction via FFC - **[HAVE]**
- **Input:** Rutile (TiO2) feedstock
- **Output:** Pure titanium metal (>99% purity)
- **Temperature:** 900-1100°C
- **Source Papers:** ellery-et-al-2022-metalysis-fray-farthing-chen-process
- **Notes:** Replaces energy-intensive Kroll process

### 2.3 Silicon Extraction via FFC - **[HAVE]**
- **Process:** SiO2 → Si metal + O2
- **KB Reference:** `silicon_metal_reduction_from_purified_v0.yaml`
- **Input:** Silica (SiO2)
- **Output:** Silicon metal
- **Temperature:** 850-900°C
- **Source Papers:** FFC-process-for-deep-ISRU.txt, Sustainable-ISRU-on-the-Moon.txt

### 2.4 Aluminium Extraction via FFC - **[HAVE]**
- **KB Reference:** Implicit in FFC process; also `aluminum_smelting_hall_heroult_v0.yaml` (competing process)
- **Input:** Alumina (Al2O3) from anorthite preprocessing
- **Output:** Aluminum metal (>99% pure)
- **Temperature:** 900-1100°C
- **Energy:** Considerably less than Hall-Héroult process
- **Source Papers:** FFC-process-for-deep-ISRU.txt, Sustainable-ISRU-on-the-Moon.txt

### 2.5 Calcium Extraction via FFC - **[MISSING]**
- **Input:** Pure calcium oxide (CaO)
- **Output:** Calcium metal
- **Temperature:** 900-1100°C
- **Source Papers:** FFC-process-for-deep-ISRU.txt, Sustainable-ISRU-on-the-Moon.txt
- **Notes:** Calcium is more conductive by mass than copper; useful for vacuum wiring

### 2.6 Magnesium Extraction via FFC - **[MISSING]**
- **Input:** Magnesium oxide (MgO)
- **Output:** Magnesium metal
- **Temperature:** 900-1100°C
- **Source Papers:** FFC-process-for-deep-ISRU.txt, Sustainable-ISRU-on-the-Moon.txt
- **Notes:** Caution - Mg has outgassing tendency in vacuum; limited lunar applications

### 2.7 Iron Oxide Reduction via FFC - **[HAVE]**
- **KB Reference:** Implicit in general FFC and `iron_smelting_reduction_v0.yaml`
- **Input:** Iron oxide (FeO, Fe2O3, Fe3O4)
- **Output:** Pure iron metal
- **Temperature:** 900-1100°C

---

## 3. ANORTHITE (CaAl2Si2O8) PREPROCESSING ROUTES

### 3.1 Carbothermal Reduction of Anorthite - **[MISSING]**
- **Process:** CaAl2Si2O8 + 4C → 4CO + CaO + Al2O3 + 2Si
- **Input:** Lunar anorthite (highland mineral), Carbon
- **Output:** Calcium oxide, Alumina, Silicon metal, Carbon monoxide (recycled)
- **Temperature:** 1650-1860°C for 3 hours
- **Source Papers:** FFC-process-for-deep-ISRU.txt, Sustainable-ISRU-on-the-Moon.txt
- **Notes:** Produces multiple valuable outputs; requires separation after powdering

### 3.2 HCl Acid Leaching of Anorthite (Artificial Weathering) - **[HAVE]**
- **Process:** CaAl2Si2O8 + 8HCl + 2H2O → CaCl2 + 2AlCl3·6H2O + 2SiO2
- **KB Reference:** `hcl_regolith_preprocessing_v0.yaml`, `hcl_regolith_leaching_v0.yaml`
- **Secondary steps:**
  - Heat AlCl3·6H2O above 100°C → separate from CaCl2 and SiO2
  - Heat AlCl3 to 400°C: 2AlCl3·6H2O → Al2O3 + 6HCl + 3H2O
- **Output:** Alumina (for FFC), Silica (for glass), CaCl2 (FFC electrolyte)
- **Temperature:** Low temperature for leaching; 400°C for calcination
- **Source Papers:** Lunar-Demandite.txt, Sustainable-ISRU-on-the-Moon.txt, ellery-et-al-2022
- **Notes:** Produces CaCl2 as by-product, which replenishes FFC electrolyte

### 3.3 Lime-Soda Process for Anorthite - **[MISSING]**
- **Process:** CaAl2Si2O8 + 3CaCO3 + Na2CO3 → 2NaAlO2 + 2Ca2SiO4 + 4CO2
- **Secondary:** NaAlO2 hydrolysis → Al(OH)3 → Al2O3
- **Input:** Anorthite, Calcium carbonate, Sodium carbonate
- **Output:** Sodium aluminate, Calcium silicate, CO2, ultimately Alumina
- **Temperature:** Elevated (calcination steps)
- **Source Papers:** Sustainable-ISRU-on-the-Moon.txt, Lunar-Demandite.txt
- **Notes:** Too complex for first-generation lunar ISRU; included for completeness

### 3.4 Carbochlorination of Anorthite - **[MISSING]**
- **Process:** CaO + Al2O3 + 2SiO2 + 8C + 8Cl2 → CaCl2 + 8CO + 2SiCl4 + 2AlCl3
- **Input:** Anorthite (decomposed to oxides), Carbon, Chlorine gas
- **Output:** Calcium chloride, Silicon tetrachloride, Aluminum chloride, Carbon monoxide
- **Temperature:** 770°C (fluidized bed)
- **Source Papers:** FFC-process-for-deep-ISRU.txt
- **Notes:** Intermediate step; requires further processing to extract pure metals

---

## 4. OLIVINE (Mg2SiO4) PROCESSING ROUTES

### 4.1 Aluminothermic Reduction of Olivine - **[MISSING]**
- **Process:**
  - 3Mg2SiO4 + 6Al → 2MgAl2O4 + 4MgO + 2AlSi + Si
  - 4MgO + 2AlSi → MgAl2O4 + 3Mg + 2Si (continuation at 1000°C)
- **Input:** Olivine (forsterite), Aluminum
- **Output:** Magnesium aluminate spinel, Magnesium metal (tapped above 650°C), Silicon
- **Temperature:** 1000°C
- **Source Papers:** FFC-process-for-deep-ISRU.txt, Sustainable-ISRU-on-the-Moon.txt
- **Notes:** Molten Mg can be tapped from refractory oxides

### 4.2 Pidgeon Process for Magnesium - **[MISSING]**
- **Process:** Mg2SiO4 + 2CaO → Ca2SiO4 + 2Mg (as vapor)
- **Input:** Olivine, Calcium oxide
- **Output:** Magnesium metal (vapor), Calcium silicate
- **Temperature:** High temperature (>1000°C)
- **Source Papers:** Lunar-Demandite.txt
- **Notes:** Direct magnesium production (alternative to FFC); requires vapor condensation

### 4.3 Carbothermal Reduction of Olivine - **[MISSING]**
- **Process:** Mg2SiO4 + 2C → 2Mg + SiO + 2CO
- **Input:** Olivine, Carbon
- **Output:** Magnesium (vapor), Silicon monoxide, Carbon monoxide
- **Temperature:** 2000°C
- **Source Papers:** Sustainable-ISRU-on-the-Moon.txt
- **Notes:** Very high temperature; Mg vaporizes

### 4.4 Olivine Hydration - **[MISSING]**
- **Process:** Mg2SiO4 (fayalite) + H2O → Fe3O4 (magnetite) + Silica + H2
- **Alternative:** Mg2SiO4 (forsterite) + 6H2O → Mg(OH)2 + H2Si3O7
- **Input:** Olivine, Water
- **Output:** Magnetite, Silica, Hydrogen, Magnesium hydroxide
- **Temperature:** Ambient for hydration; decomposition at 332°C
- **Source Papers:** Lunar-Demandite.txt
- **Notes:** Low-energy process; produces useful by-products

---

## 5. SPECIALIZED METAL EXTRACTION (METEORITIC MATERIAL)

### 5.1 Mond Process (Nickel Carbonyl) - **[HAVE]**
- **Process:** Ni + 4CO ⇌ Ni(CO)4 (gaseous, formed at 40-80°C, 1 bar)
- **Decomposition:** Ni(CO)4 → Ni + 4CO (at 230°C, 60 bar)
- **KB Reference:** `mond_carbonyl_process_nickel_v0.yaml`, `nickel_extraction_meteorite_v0.yaml`
- **Input:** Metallic nickel or NiFe alloy, Carbon monoxide, Sulfur catalyst
- **Output:** High-purity nickel (>99%), Recycled CO
- **Source Papers:** Sustainable-ISRU-on-the-Moon.txt, Lunar-Demandite.txt

### 5.2 Iron Carbonyl Process - **[HAVE]**
- **Process:** Fe + 5CO ⇌ Fe(CO)5 (gaseous)
- **Decomposition:** Fe(CO)5 ↔ 5CO + Fe (at 175°C, 100 bar)
- **KB Reference:** `iron_carbonyl_process_v0.yaml`, `iron_carbonyl_synthesis_v0.yaml`
- **Input:** Metallic iron, Carbon monoxide
- **Output:** High-purity iron, Recycled CO
- **Source Papers:** Sustainable-ISRU-on-the-Moon.txt, Lunar-Demandite.txt

### 5.3 Cobalt Carbonyl Process - **[HAVE]**
- **Process:** Co2(CO)8 ↔ 8CO + 2Co
- **Conditions:** 150°C, 35 bar
- **KB Reference:** `cobalt_carbonyl_process_v0.yaml`, `dicobalt_octacarbonyl_synthesis_v0.yaml`
- **Input:** Cobalt metal, Carbon monoxide
- **Output:** High-purity cobalt, Recycled CO
- **Source Papers:** Sustainable-ISRU-on-the-Moon.txt

### 5.4 Tungsten Extraction via Density Separation - **[PARTIAL]**
- **Process:** Grinding + centrifugal separation + hydrocyclone
- **Input:** NiFe meteorite material with W microparticles (0.1-5 μg/g)
- **Output:** Concentrated tungsten particles
- **Method:** High density of W (19.3 g/cm³) enables separation from residue
- **KB Status:** Have basic beneficiation processes; not W-specific
- **Source Papers:** Sustainable-ISRU-on-the-Moon.txt, Lunar-Demandite.txt
- **Notes:** Critical material for tool steel and thermionic cathodes

### 5.5 Cobalt Extraction via Sulfate Route - **[MISSING]**
- **Process:**
  - Co roasting with S in oxygen → Cobalt sulfate (soluble in water)
  - Electrolysis of aqueous CoSO4 → Pure Co metal
- **Input:** Cobalt metal or cobalt-bearing ore, Sulfur, Oxygen
- **Output:** Cobalt sulfate solution, then pure cobalt
- **Source Papers:** Sustainable-ISRU-on-the-Moon.txt
- **Notes:** Alternative to carbonyl process

---

## 6. SILICON PURIFICATION PROCESSES

### 6.1 Siemens Process (Trichlorosilane Route) - **[PARTIAL]**
- **Process:**
  - Si + 3HCl → SiHCl3 + H2 (at 300°C)
  - SiHCl3 + H2 → Si + 3HCl (at 1150°C, HCl recycled)
- **KB Status:** Have `silicon_purification_mgsi_v0.yaml` (different route)
- **Input:** Silicon particles, Hydrochloric acid, Hydrogen
- **Output:** High-purity polycrystalline silicon, Recycled HCl
- **Source Papers:** Sustainable-ISRU-on-the-Moon.txt, Power-on-the-Moon-using-ISRU.txt
- **Notes:** Standard industrial process for semiconductor-grade silicon

### 6.2 Czochralski Process (Single-Crystal Silicon) - **[MISSING]**
- **Process:** Polycrystalline Si evaporation with single-crystal seed in fused quartz crucible
- **Input:** Polycrystalline silicon, Single-crystal seed, Fused silica crucible
- **Output:** Single-crystal silicon ingot (for electronics/solar cells)
- **Conditions:** Vacuum, seed pulling, rotation
- **Temperature:** ~1600°C
- **Source Papers:** Sustainable-ISRU-on-the-Moon.txt
- **Notes:** Essential for photovoltaics and electronics manufacturing

### 6.3 Zone Refining (Silicon Purification) - **[MISSING]**
- **Process:** Thermal zone melting with impurity segregation
- **Input:** Polycrystalline silicon
- **Output:** Ultra-pure single-crystal silicon
- **Temperature:** ~1600°C (local melting)
- **Source Papers:** Sustainable-ISRU-on-the-Moon.txt
- **Notes:** Used to achieve extreme purity levels required for semiconductors

### 6.4 High-Purity Silica Glass Production - **[MISSING]**
- **Process:** SiCl4 + 2H2 + O2 → SiO2 + 4HCl
- **Input:** Silicon tetrachloride vapor, Hydrogen, Oxygen
- **Output:** High-purity fused silica, HCl (recycled)
- **Temperature:** H2-O2 flame temperature
- **Source Papers:** FFC-process-for-deep-ISRU.txt, Sustainable-ISRU-on-the-Moon.txt
- **Notes:** Produces optical-grade silica glass

---

## 7. WATER AND VOLATILES EXTRACTION

### 7.1 Water Electrolysis - **[PARTIAL]**
- **Process:** 2H2O → 2H2 + O2
- **KB Status:** Many processes use electrolysis but may not be explicitly defined as standalone
- **Input:** Water (from volatiles, regolith reduction, or polar ice)
- **Output:** Hydrogen gas, Oxygen gas
- **Source Papers:** All ISRU papers

### 7.2 Thermal Extraction of Volatiles from Regolith - **[PARTIAL]**
- **Input:** Lunar regolith (containing solar-implanted H, He, C, N volatiles)
- **Output:** Gaseous volatiles (fractionally distilled by condensation temperature)
- **Temperature ranges:**
  - Heating: 700-1200°C to release volatiles
  - Fractional distillation condensation points:
    - He: 4.2K
    - H2: 20K
    - N2: 77K
    - CO: 81K
    - CH4: 109K
    - CO2: 194K
    - H2O: 373K
- **KB Status:** Have `regolith_heating_water_extraction_v0.yaml` but not comprehensive volatile separation
- **Source Papers:** Sustainable-ISRU-on-the-Moon.txt, I-SAIRAS-2020
- **Notes:** Requires fractional distillation column

### 7.3 Polar Water Ice Extraction - **[MISSING]**
- **Input:** Water ice from permanently shadowed craters (~40K)
- **Output:** Liquid water or water vapor
- **Method:** Solar heating, thermal processing, or direct sublimation capture
- **Source Papers:** Power-on-the-Moon-using-ISRU.txt, Sustainable-ISRU-on-the-Moon.txt
- **Notes:** Requires drilling into frozen regolith; heliostats for power delivery

---

## 8. CARBON CYCLE AND RECYCLING PROCESSES

### 8.1 Sabatier Reaction (CO2 → CH4) - **[PARTIAL]**
- **Process:** CO2 + 4H2 → CH4 + 2H2O
- **KB Reference:** May exist under different names; have methanation processes
- **Catalyst:** Nickel-based
- **Temperature:** 300-400°C
- **Input:** Carbon dioxide, Hydrogen
- **Output:** Methane, Water (can be re-electrolyzed to recycle H2)
- **Source Papers:** FFC-process-for-deep-ISRU.txt, Sustainable-ISRU-on-the-Moon.txt
- **Notes:** Essential for closing carbon cycle in FFC anode consumption

### 8.2 Boudouard Reaction (CO2 → CO) - **[MISSING]**
- **Process:** C + CO2 → 2CO
- **Input:** Carbon, Carbon dioxide
- **Output:** Carbon monoxide
- **Temperature:** ~700°C
- **Source Papers:** FFC-process-for-deep-ISRU.txt
- **Notes:** Generates CO for Mond/carbonyl processes

### 8.3 Bosch Reaction (CO2 Reduction) - **[MISSING]**
- **Process:** CO2 + 2H2 → C + 2H2O
- **Catalyst:** Iron or nickel
- **Temperature:** 530-730°C
- **Input:** Carbon dioxide, Hydrogen
- **Output:** Solid carbon, Water
- **Source Papers:** FFC-process-for-deep-ISRU.txt
- **Notes:** Reconstitutes carbon for FFC graphite anodes

### 8.4 Methane Pyrolysis (CH4 → C) - **[HAVE]**
- **Process:** CH4 → C + 2H2
- **KB Reference:** `methane_pyrolysis_v0.yaml`, `methane_pyrolysis_basic_v0.yaml`
- **Catalyst:** Nickel
- **Temperature:** 1400°C
- **Input:** Methane
- **Output:** Solid carbon, Hydrogen (recycled)
- **Source Papers:** FFC-process-for-deep-ISRU.txt
- **Notes:** Regenerates carbon for FFC graphite anodes

### 8.5 CO Oxidation to CO2 - **[MISSING]**
- **Process:** CO + 0.5O2 → CO2
- **Catalyst:** Spinel catalyst
- **Temperature:** 30-350°C (low temperature with catalyst)
- **Input:** Carbon monoxide, Oxygen
- **Output:** Carbon dioxide
- **Source Papers:** FFC-process-for-deep-ISRU.txt
- **Notes:** Preprocessing step before Sabatier reaction

---

## 9. NITROGEN AND AMMONIA PRODUCTION

### 9.1 Haber-Bosch Process - **[HAVE]**
- **Process:** N2 + 3H2 ⇌ 2NH3
- **KB Reference:** `nitrogen_fixation_haber_bosch_v0.yaml`
- **Catalyst:** Fe catalyst supported by CaO, SiO2, Al2O3 promoters
- **Pressure:** 15-25 MPa
- **Temperature:** 400-500°C
- **Input:** Nitrogen gas (from volatiles), Hydrogen
- **Output:** Ammonia (NH3)
- **Source Papers:** Sustainable-ISRU-on-the-Moon.txt
- **Notes:** Essential for nitric acid production; nitrogen is scarce lunar volatile

### 9.2 Ostwald Process (Nitric Acid) - **[MISSING]**
- **Process:**
  - 4NH3 + 5O2 → 4NO + 6H2O
  - 2NO + O2 → 2NO2
  - 3NO2 + H2O → 2HNO3 + NO
- **Catalyst:** Pt on Ni (terrestrial) or tungsten carbide on nickel (lunar)
- **Pressure:** 400-1000 kPa
- **Temperature:** 600-800°C
- **Input:** Ammonia, Oxygen
- **Output:** Nitric acid (HNO3), NO (recycled)
- **Source Papers:** Sustainable-ISRU-on-the-Moon.txt, Lunar-Demandite.txt
- **Notes:** HNO3 used to generate HCl from NaCl

### 9.3 Ammonia Recycling via CaO - **[MISSING]**
- **Process:** NH4Cl + CaO → 2NH3 + CaCl2 + H2O
- **Input:** Ammonium chloride (from Solvay process), Calcium oxide
- **Output:** Ammonia (recycled), Calcium chloride, Water
- **Source Papers:** Sustainable-ISRU-on-the-Moon.txt
- **Notes:** Part of Solvay process recycling loop

---

## 10. CHLORINE AND ACID CHEMISTRY

### 10.1 HCl Generation from NaCl - **[PARTIAL]**
- **Process:** NaCl + HNO3 → HCl + NaNO3
- **KB Status:** Have HCl synthesis but may not have this specific route
- **Input:** Sodium chloride (Earth import), Nitric acid
- **Output:** Hydrochloric acid gas, Sodium nitrate
- **Source Papers:** Sustainable-ISRU-on-the-Moon.txt
- **Notes:** NaCl is recycled reagent, not consumed

### 10.2 Solvay Process (Sodium Carbonate) - **[MISSING]**
- **Process:**
  - NaCl + NH3 + CO2 + H2O → NaHCO3 + NH4Cl
  - 2NaHCO3 → Na2CO3 + H2O + CO2 (calcination)
  - Overall: 2NaCl + CaCO3 ⇌ Na2CO3 + CaCl2
- **Input:** Sodium chloride, Ammonia, Carbon dioxide, Water
- **Output:** Sodium carbonate, Calcium chloride (FFC electrolyte replenishment)
- **Source Papers:** Sustainable-ISRU-on-the-Moon.txt, Lunar-Demandite.txt
- **Notes:** Na2CO3 used for quartz crystal growth and selenium extraction

### 10.3 Chloralkali Electrolysis - **[HAVE]**
- **Process:** 2NaCl + 2H2O → 2NaOH + Cl2 + H2
- **KB Reference:** `chloralkali_electrolysis_v0.yaml`
- **Input:** Sodium chloride solution, Water
- **Output:** Sodium hydroxide, Chlorine gas, Hydrogen
- **Source Papers:** Standard industrial chemistry

### 10.4 CaCl2 Regeneration from CaO - **[MISSING]**
- **Process:** CaO + 2HCl → CaCl2 + H2O (highly exothermic)
- **Input:** Calcium oxide, Hydrochloric acid
- **Output:** Calcium chloride (FFC electrolyte), Water
- **Source Papers:** FFC-process-for-deep-ISRU.txt, Sustainable-ISRU-on-the-Moon.txt
- **Notes:** Replenishes FFC electrolyte from preprocessing waste

### 10.5 HCl Recovery from CaCl2 - **[MISSING]**
- **Process:** CaCl2 + 2H2O → Ca(OH)2 + 2HCl (above 425°C)
- **Input:** Calcium chloride, Water vapor
- **Output:** Slaked lime Ca(OH)2, Hydrochloric acid (recycled)
- **Temperature:** >425°C
- **Source Papers:** Sustainable-ISRU-on-the-Moon.txt
- **Notes:** Alternative recycling path for HCl

---

## 11. SULFUR CHEMISTRY

### 11.1 Sulfuric Acid Production - **[PARTIAL]**
- **Process:**
  - 2SO2 + O2 ⇌ 2SO3
  - SO3 + H2O → H2SO4
- **KB Status:** May exist but not verified in this review
- **Input:** Sulfur dioxide, Oxygen, Water
- **Output:** Sulfuric acid
- **Source Papers:** Lunar-Demandite.txt, Sustainable-ISRU-on-the-Moon.txt

### 11.2 Claus Process (Sulfur Recovery) - **[MISSING]**
- **Process:**
  - 4FeS + 7O2 → 2Fe2O3 + 4SO2 (troilite roasting)
  - SO2 + H2S → 3S + H2O (at 750-1100°C over alumina catalyst)
- **Input:** Troilite (FeS) from meteorites, Oxygen, Hydrogen sulfide
- **Output:** Elemental sulfur, Water
- **Source Papers:** Sustainable-ISRU-on-the-Moon.txt, Lunar-Demandite.txt
- **Notes:** Sulfur used as catalyst in Mond/carbonyl processes

---

## 12. SPECIALIZED ELEMENT EXTRACTION

### 12.1 Selenium Extraction - **[HAVE]**
- **Process:** FeSe + Na2CO3 + 1.5O2 → FeO + Na2SeO3 + CO2
- **Secondary:** Na2SeO3 + H2SO4 → Na2O + H2SO4 + Se
- **KB Reference:** `selenium_extraction_refining_v0.yaml`
- **Catalyst:** KNO3 (saltpetre)
- **Input:** Iron selenide (meteoritic), Sodium carbonate, Oxygen
- **Output:** Selenium (photosensitive material), Iron oxide
- **Source Papers:** Sustainable-ISRU-on-the-Moon.txt
- **Notes:** Selenium required for vision sensors; very rare

### 12.2 Phosphorus Extraction - **[MISSING]**
- **Process:** 4H3PO4 + 16C → P4 + 6H2 + 16CO
- **Temperature:** 850°C
- **Input:** Phosphoric acid (from KREEP minerals), Carbon
- **Output:** White phosphorus (P4), Hydrogen, Carbon monoxide
- **Source Papers:** Sustainable-ISRU-on-the-Moon.txt, Power-on-the-Moon-using-ISRU.txt
- **Notes:** Phosphorus in lunar KREEP regions; toxic but useful

### 12.3 Calcium Oxide (Quicklime) Extraction - **[HAVE]**
- **KB Reference:** `calcium_oxide_extraction_v0.yaml`
- **Input:** Calcium-bearing minerals from regolith
- **Output:** Calcium oxide (CaO)
- **Notes:** Used for thermionic cathode coatings, cement, recycling loops

### 12.4 Barium Oxide Extraction - **[HAVE]**
- **KB Reference:** `barium_oxide_extraction_v0.yaml`
- **Input:** Barium-bearing minerals
- **Output:** Barium oxide (BaO)
- **Notes:** Used for thermionic cathode coatings

---

## 13. SILICONE/SILOXANE SYNTHESIS

### 13.1 Syngas Generation - **[MISSING]**
- **Process:** CH4 + H2O → CO + 3H2
- **Catalyst:** Nickel
- **Temperature:** 850°C
- **Pressure:** 4 MPa
- **Input:** Methane (from volatiles), Water
- **Output:** Carbon monoxide, Hydrogen (syngas)
- **Source Papers:** Sustainable-ISRU-on-the-Moon.txt
- **Notes:** First step in silicone plastic manufacturing

### 13.2 Methanol Synthesis - **[MISSING]**
- **Process:** CO + 2H2 → CH3OH
- **Catalyst:** Alumina (from anorthite)
- **Temperature:** 250°C
- **Pressure:** 5-10 MPa
- **Input:** Syngas (CO + H2)
- **Output:** Methanol
- **Source Papers:** Sustainable-ISRU-on-the-Moon.txt
- **Notes:** Second step in silicone synthesis

### 13.3 Methyl Chloride Synthesis - **[HAVE]**
- **Process:** CH3OH + HCl → CH3Cl + H2O
- **KB Reference:** `methylchloride_synthesis_v0.yaml`
- **Catalyst:** Alumina
- **Temperature:** 340°C
- **Input:** Methanol, Hydrochloric acid
- **Output:** Methyl chloride (chloromethane), Water
- **Source Papers:** Sustainable-ISRU-on-the-Moon.txt

### 13.4 Rochow Process (Dimethyldichlorosilane) - **[HAVE]**
- **Process:** 2CH3Cl + Si → (CH3)2SiCl2
- **KB Reference:** `rochow_process_reactor_v0.yaml`
- **Catalyst:** Nickel or copper (Ni preferred for lunar)
- **Temperature:** 320-370°C
- **Pressure:** 1-5 bar
- **Input:** Methyl chloride, Silicon
- **Output:** Dimethyldichlorosilane
- **Source Papers:** Sustainable-ISRU-on-the-Moon.txt, FFC-process-for-deep-ISRU.txt

### 13.5 Siloxane Polymerization - **[HAVE]**
- **Process:** n(CH3)2SiCl2 + nH2O → [(CH3)2SiO]n + 2nHCl
- **KB Reference:** `silicone_polymerization_v0.yaml`, `silicone_polymer_synthesis_v0.yaml`
- **Input:** Dimethyldichlorosilane, Water
- **Output:** Polydimethylsiloxane (PDMS silicone), HCl (recycled)
- **Source Papers:** Sustainable-ISRU-on-the-Moon.txt

---

## 14. QUARTZ AND GLASS PROCESSING

### 14.1 Quartz Crystal Synthesis (Piezoelectric) - **[HAVE]**
- **Process:**
  - Na2CO3 + SiO2 ↔ Na2SiO3 + CO2 (at 2000°C melting)
  - Seeding with Na2SiO3 at 350°C and 150 MPa to grow quartz crystals
- **KB Reference:** `quartz_crystal_synthesis_v0.yaml`
- **Input:** Sodium carbonate (from Solvay), Silica (from anorthite leaching)
- **Output:** Quartz crystals (piezoelectric sensors)
- **Growth time:** 40-80 days (bottleneck)
- **Source Papers:** Sustainable-ISRU-on-the-Moon.txt
- **Notes:** CO2 recovered and recycled; critical for sensors

### 14.2 Aluminosilicate Glass - **[PARTIAL]**
- **Composition:** 57% SiO2, 20% Al2O3, 12% MgO, 5% CaO
- **Melting point:** 1100-1350°C (lower than fused silica)
- **KB Status:** Have general glass processes but not this specific composition
- **Source Papers:** Sustainable-ISRU-on-the-Moon.txt, FFC-process-for-deep-ISRU.txt
- **Notes:** Natural lunar glass darkened by FeO; needs purification for transparency

---

## 15. METAL ALLOY MONGREL PROCESSING

### 15.1 Direct FFC Reduction of Ilmenite to FeTi Alloy - **[PARTIAL]**
- **Process:** FeTiO3 → FeTi alloy sponge + O2
- **Input:** Ilmenite (sintered powder cathode)
- **Output:** Ferro-titanium alloy (45-75% Ti), Oxygen
- **KB Status:** Have FFC process but not specifically for mongrel alloy production
- **Source Papers:** ellery-et-al-2022-metalysis-fray-farthing-chen-process
- **Notes:** Alloy suitable for structures or pyrotechnic fuel; oxygen-scavenging properties

### 15.2 Direct FFC Reduction of Anorthite to AlCaSi Alloy - **[MISSING]**
- **Process:** CaAl2Si2O8 → AlCaSi alloy + O2
- **Input:** Anorthite (sintered powder)
- **Output:** Aluminum-calcium-silicon alloy, Oxygen
- **Source Papers:** FFC-process-for-deep-ISRU.txt
- **Uses:** Brazing filler metal, general structures
- **Notes:** Properties need investigation; silumin-like behavior

### 15.3 Direct FFC Reduction of Olivine to MgSi Alloy - **[MISSING]**
- **Process:** Mg2SiO4 → MgSi alloy + O2
- **Input:** Olivine (sintered powder)
- **Output:** Magnesium-silicon alloy, Oxygen
- **Source Papers:** FFC-process-for-deep-ISRU.txt
- **Uses:** Alloying additive for aluminum, general structures
- **Notes:** Mg2Si improves aluminum strength; can tolerate Fe contamination

---

## 16. RARE EARTH AND EXOTIC ELEMENT EXTRACTION

### 16.1 Rare Earth Element (REE) Extraction from KREEP - **[MISSING]**
- **Source:** KREEP minerals (potassium-rare earth-phosphorus basalts)
- **Concentration:** ~1200 ppm average REE; up to 5x higher than Earth
- **Elements:** Y, Ce (300 ppm each), down to Eu (3-5 ppm)
- **Detection:** Gamma ray detection via U/Th association (U/Th ~0.27 ratio)
- **Source Papers:** Sustainable-ISRU-on-the-Moon.txt
- **Notes:** Too complex for first-gen ISRU; high utility for permanent magnets (NdFeB), superconductors (NbTi)

### 16.2 Helium-3 Extraction - **[MISSING]**
- **Concentration:** 4-30 ppb (peak in mature high-Ti mare regolith)
- **Extraction:** Released with other volatiles during thermal processing (700-1200°C)
- **Separation:** Cryogenic fractional distillation at 4.2K
- **Source Papers:** Sustainable-ISRU-on-the-Moon.txt, FFC-process-for-deep-ISRU.txt
- **Notes:** Nuclear fusion fuel; extremely scarce resource; should be husbanded for future

### 16.3 Noble Gas Extraction (Ne, Ar, Kr, Xe) - **[MISSING]**
- **Concentration:** <1 ppm (highly rarified)
- **Extraction:** Thermal processing + cryogenic separation
- **Use:** Ion engine propellant
- **Source Papers:** Sustainable-ISRU-on-the-Moon.txt
- **Notes:** Too rare to be practical for most applications

---

## 17. ENERGY CONVERSION AND STORAGE

### 17.1 Thermionic Conversion - **[PARTIAL]**
- **Process:** Heated cathode emits electrons → electrical power
- **Efficiency:** 20% (Russian nuclear), up to 40-50% with enhancements
- **Cathode materials:** Tungsten, Calcium oxide coating, Barium oxide coating
- **KB Status:** Have related processes but not complete thermionic system
- **Source Papers:** ellery-et-al-2022-metalysis-fray-farthing-chen-process, Power-on-the-Moon
- **Notes:** More efficient than photovoltaics for in-situ manufacturing

### 17.2 Photon-Enhanced Thermionic Emission (PETE) - **[MISSING]**
- **Process:** Combined photovoltaic + thermionic stages
- **Efficiency:** Up to 50%
- **Cathode coating:** Aluminum-doped hematite (from ilmenite-derived iron heated in O2)
- **Source Papers:** ellery-et-al-2022-metalysis-fray-farthing-chen-process
- **Notes:** Advanced power generation for ISRU processes

---

## SUMMARY STATISTICS

**Total processes cataloged:** 116
**Processes we HAVE (fully or partially):** 35 (~30%)
**Processes we're MISSING:** 81 (~70%)

### High-Priority Missing Processes (Critical for ISRU):

1. **Vacuum pyrolysis** - Very high temperature oxygen extraction
2. **Ulvospinel reduction** - Alternative to ilmenite for Ti/Fe
3. **Carbothermal reduction of anorthite** - Multi-metal production
4. **Aluminothermic reduction of olivine** - Mg production
5. **Pidgeon process** - Direct Mg extraction
6. **Ostwald process** - Nitric acid production (enables HCl from NaCl)
7. **Solvay process** - Sodium carbonate production
8. **Boudouard reaction** - CO generation for Mond process
9. **Bosch reaction** - Carbon regeneration for FFC anodes
10. **Czochralski process** - Single-crystal silicon for electronics
11. **Siemens process (complete)** - Semiconductor-grade silicon
12. **Polar water ice extraction** - Direct water recovery
13. **Comprehensive volatile thermal extraction** - Full fractional distillation
14. **Lime-soda and carbochlorination routes** - Alternative preprocessing
15. **FFC calcium and magnesium reduction** - Pure light metal production

### Medium-Priority Missing Processes:

- Zone refining (ultra-pure silicon)
- HCl recovery pathways
- CaCl2 regeneration routes
- CO oxidation catalysis
- Sulfuric acid complete chain
- Claus process for sulfur
- Phosphorus extraction
- Syngas and methanol synthesis
- Ammonia recycling routes
- Direct mongrel alloy routes via FFC
- Specialized acid leaching variants

### Lower-Priority (Advanced/Future):

- REE extraction from KREEP
- He-3 cryogenic separation
- Noble gas extraction
- PETE energy conversion
- Exotic mineral processing

---

## RECOMMENDED NEXT STEPS

1. **Prioritize high-temperature processes** - These are bottle necks for many extraction routes
2. **Define complete chemical recycling loops** - Especially for NaCl-HCl-CaCl2 system
3. **Expand silicon purification chain** - Critical for electronics and photovoltaics
4. **Add comprehensive volatile processing** - Thermal extraction + fractional distillation
5. **Define all anorthite preprocessing routes** - Multiple pathways enable flexibility
6. **Complete carbonyl/Mond family** - Already have partial coverage
7. **Add direct mongrel alloy processes** - Simpler alternative to pure metal extraction

---

## PAPER REFERENCES

**Primary Sources:**
- `ellery-et-al-2022-metalysis-fray-farthing-chen-process.txt` - Comprehensive FFC process and preprocessing
- `Sustainable-ISRU-on-the-Moon.txt` - Complete industrial ecology with recycling loops
- `FFC-process-for-deep-ISRU.txt` - FFC fundamentals and applications
- `Lunar-ISRU-2019-Lomax.txt` - Experimental FFC results
- `Power-on-the-Moon-using-ISRU.txt` - Energy conversion and storage
- `Lunar-Demandite.txt` - Material requirements and extraction routes
- `Heat-Pipe-Solar-Receiver-O2-2009.txt` - High-temperature solar processing
- `NASA-ISRU-Progress-2012.txt` - Comprehensive ISRU technology survey
- `I-SAIRAS-2020-Sustainable-Lunar-Exploration.txt` - Volatile extraction and processing

**Additional Context:**
- `NASA-TM-20210009988-Bootstrapping-Space-Industry.txt`
- `NSS-Bootstrapping-Lunar-Industry-2016.txt`
- `MIT-ISRU-Architecture-2008.txt`
- `UCF-ISRU-Modeling-Optimization.txt`
- Multiple additional papers on specific technologies

---

**Document Created:** 2025-12-22
**Author:** Research analysis by Claude Code exploration agent
**Purpose:** Gap analysis for self-replicating system modeling KB development
