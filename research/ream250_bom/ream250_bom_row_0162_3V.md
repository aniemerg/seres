---
row_identity:
  item: "3V"
  cad_file: "3V_gas_in_top"
  source_row_number: 162
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Stationary oxygen gas transmitter for measuring O2 concentration at the top gas inlet, using an FCX-TR0025 zirconia/amperometric transmitter with a 4-20 mA output."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; https://sensorsandpower.angst-pfister.com/fileadmin/products/datasheets/272/FCX-TR_1620-21914-0029-E-0821.pdf; https://www.digikey.com/en/products/detail/angst-pfister-sensors-and-power-ag/FCX-TR0025-7-5-Q08-112-500/26236819"
    cited_fact_or_basis: "BOM row 162 identifies item 3V, CAD file 3V_gas_in_top, and description FCX-TR0025 amperometric. The Angst+Pfister manual describes the FCX-TR0025 range as an oxygen transmitter for 0...25% O2 with integrated sensor/electronics and 4-20 mA output. DigiKey lists FCX-TR0025-7-5-Q08-112-500 as an Oxygen (O2) Sensor 4mA ~ 20mA."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The BOM description maps row 3V to the FCX-TR0025 transmitter identity even though the local CAD filename emphasizes the gas-in-top mounting geometry."
  uncertainty_notes:
    - "The rendered CAD preview is a manifold or top gas inlet shape rather than the full cylindrical catalog transmitter, so CAD is treated as installation context rather than the sole function definition."
mass:
  value_kg: 0.25
  basis: "Per-unit mass is the vendor manual weight of 250 g for one FCX-TR transmitter. BOM quantity is 1, so the row total is also about 0.25 kg. Local FreeCAD measurement for 3V_gas_in_top.step found 1 solid, volume 70143.365 mm^3, area 45909.183 mm^2, and bounding box 129.90 x 120.26 x 52.00 mm, but the catalog/manual mass is used because the CAD preview does not represent the complete cylindrical transmitter envelope."
  source:
    url_or_path: "https://sensorsandpower.angst-pfister.com/fileadmin/products/datasheets/272/FCX-TR_1620-21914-0029-E-0821.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3V_gas_in_top.step"
    cited_fact_or_basis: "The Angst+Pfister FCX-TR operating manual lists transmitter dimensions Length/diameter 114 mm/Ø34.5 mm and Weight 250 g. FreeCAD measured the supplied row STEP geometry as 70143.365 mm^3 with a 129.90 x 120.26 x 52.00 mm bounding box."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The manual weight applies to one physical FCX-TR0025 transmitter represented by this BOM row."
  uncertainty_notes:
    - "The CAD-derived volume would give a different mass if treated as solid stainless steel; that disagreement is attributed to the CAD file representing gas-inlet installation geometry or a simplified body rather than the complete catalog transmitter."
material:
  primary_material: "stainless steel transmitter housing with zirconia oxygen sensing element and integrated control electronics"
  source:
    url_or_path: "https://sensorsandpower.angst-pfister.com/fileadmin/products/datasheets/272/FCX-TR_1620-21914-0029-E-0821.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The Angst+Pfister manual states the zirconia oxygen sensor is built into a stainless steel transmitter housing with control electronics integrated into the housing. Local assembly STEP material extraction for product 3V_gas_in_top returned only Generic material with density 1000.0."
    evidence_basis: "independent_vendor_spec"
  assumptions: []
  uncertainty_notes:
    - "The specific stainless grade and detailed electronics submaterials are not stated in the available row-matched sources."
how_to_make:
  summary: "Defer local self-manufacture until a sensor-cell, electronics, pressure housing, and calibration workflow are modeled"
  manufacturing_steps:
    - "Install the transmitter into the gas-in-top interface using the appropriate process adapter and cable connection."
    - "Commission or periodically check calibration against dry air according to the operating manual."
    - "For future local manufacture, model stainless pressure housing fabrication, zirconia sensor production, electronics assembly, heater/control tuning, and factory calibration as separate specialist work."
  source:
    url_or_path: "https://sensorsandpower.angst-pfister.com/fileadmin/products/datasheets/272/FCX-TR_1620-21914-0029-E-0821.pdf; https://www.digikey.com/en/products/detail/angst-pfister-sensors-and-power-ag/FCX-TR0025-7-5-Q08-112-500/26236819"
    cited_fact_or_basis: "The operating manual says the sensor and measurement electronics are integrated in the stainless transmitter housing, the transmitter is calibrated as one unit at the factory, the sensor is not directly replaceable, and the FCX-TR0025 calibration check can be done in dry air. DigiKey lists the FCX-TR0025-7-5-Q08-112-500 as an orderable oxygen sensor/transmitter product."
    evidence_basis: "independent_vendor_spec"
  assumptions: []
  uncertainty_notes:
    - "Local manufacture remains unresolved at subcomponent level because no source in this row provides a sensor-cell BOM, electronics design, heater calibration data, or pressure-housing manufacturing drawing."
kb_implications:
  - "item_granularity: complex_module - Model 3V as a calibrated oxygen transmitter complex module for this pass; split into housing, zirconia cell, electronics, and calibration processes only if oxygen-sensor self-manufacture becomes a priority."
---

