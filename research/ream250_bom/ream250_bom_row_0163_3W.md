---
row_identity:
  item: "3W"
  cad_file: "3W_dummy_oxygen_sensor_FCX-TR"
  source_row_number: 163
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://sensorsandpower.angst-pfister.com/de/produkte/gassensoren/produkt/fcx-tr0025-amperometric-oxygen-o2-gas-transmitter/"
function:
  summary: "Angst+Pfister FCX-TR0025 oxygen transmitter module for measuring 0-25% oxygen concentration and converting the zirconia sensor signal to a 4-20 mA industrial output."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3W_dummy_oxygen_sensor_FCX-TR.step; https://sensorsandpower.angst-pfister.com/fileadmin/products/datasheets/272/FCX-TR_1620-21914-0029-E-0821.pdf"
    cited_fact_or_basis: "BOM row 163 identifies item 3W as 3W_dummy_oxygen_sensor_FCX-TR, manufacturer Angst + Pfister, description oxygen (O2) gas transmitter. Manifest row 163 maps the same item to the per-part STEP. FreeCAD measured one solid with volume about 60172.791 mm3, area about 11084.770 mm2, and bounding box about 34.50 x 114.00 x 34.50 mm; the rendered contact sheet shows a cylindrical threaded transmitter body with connector/end features. The FCX-TR manual says the FCX-TR0025 range is 0...25% O2, the sensor and measurement electronics are integrated in a stainless steel transmitter housing, and the electronics outputs 4-20 mA."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The BOM wording includes 'valve sv04_din_cc_dn40_-' after the oxygen-transmitter description, but the CAD filename, manufacturer, URL, dimensions, and manual all match the FCX-TR oxygen transmitter rather than a separate valve."
mass:
  value_kg: 0.25
  basis: "Use the official FCX-TR manual weight of 250 g, or 0.25 kg, per transmitter. BOM quantity is 1, so the row total is also about 0.25 kg. FreeCAD measured volume about 60172.791 mm3 and bounding box about 34.50 x 114.00 x 34.50 mm; the vendor weight is preferred over CAD-density calculation for this mixed stainless-housing, sensor, connector, and electronics module."
  source:
    url_or_path: "https://sensorsandpower.angst-pfister.com/fileadmin/products/datasheets/272/FCX-TR_1620-21914-0029-E-0821.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3W_dummy_oxygen_sensor_FCX-TR.step"
    cited_fact_or_basis: "The FCX-TR manual specifications list dimensions length/diameter 114 mm / Ø34.5 mm and weight 250 g. FreeCAD measured one STEP solid, volume about 60172.791 mm3, area about 11084.770 mm2, and bounding box about 34.50 x 114.00 x 34.50 mm."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The local STEP assembly material extractor returned only Generic with density 1000.0, which is placeholder metadata and was not used for mass."
material:
  primary_material: "Stainless steel transmitter housing with zirconium oxide oxygen sensor, integrated control/amplifier electronics, M8 4-pole electrical connector, and a small PA6.6 plastic protection screw."
  source:
    url_or_path: "https://sensorsandpower.angst-pfister.com/fileadmin/products/datasheets/272/FCX-TR_1620-21914-0029-E-0821.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The FCX-TR manual states the zirconia oxygen sensor is built into a stainless steel transmitter housing, with control electronics integrated into the housing; it also identifies a male M8 4-pole electrical connection and an M3x6 PA6.6 plastic screw protecting the potentiometer. Local assembly STEP material extraction for 3W_dummy_oxygen_sensor_FCX-TR returned only Generic with density 1000.0, so CAD metadata was treated as placeholder."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The source does not provide a full material breakdown for electrodes, connector contacts, PCB, potting, seals, or internal fasteners; treat those as unresolved submaterials inside the purchased transmitter module."
how_to_make:
  summary: "A future Manufacturing route would decompose it into precision stainless housing fabrication, zirconia sensor production, electronics assembly, connector installation, calibration, and functional testing"
  manufacturing_steps:
    - "Integration route: screw-mount the transmitter by its G1/2 process connection, connect the M8 4-pole electrical interface or matching cable, supply 10-28 VDC, and verify output/calibration in dry air or calibration gas per the manual."
    - "Manufacturing route: machine or otherwise fabricate the stainless transmitter housing and process adapter, make or source the zirconium-oxide oxygen sensing element, assemble heater/control/amplifier electronics and connector hardware, install protection screw and seals as required, then calibrate and verify 4-20 mA output response."
  source:
    url_or_path: "https://sensorsandpower.angst-pfister.com/fileadmin/products/datasheets/272/FCX-TR_1620-21914-0029-E-0821.pdf; research/ream250_bom/ream250_bom_row_0163_3W__views_2x2.png; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3W_dummy_oxygen_sensor_FCX-TR.step"
    cited_fact_or_basis: "The FCX-TR manual establishes product identity, sensor range, stainless housing, zirconia sensor, 4-20 mA output, G1/2 process connection, M8 4-pole electrical connection, dimensions, weight, and factory calibration behavior. CAD geometry and preview confirm the compact threaded cylindrical transmitter form. targeted_web_search: queries tried included 'FCX-TR0025 amperometric oxygen O2 gas transmitter Angst Pfister datasheet weight material', 'FCX-TR0025 amperometric oxygen O2 gas transmitter Angst+Pfister', and 'FCX-TR oxygen gas transmitter datasheet FCX-TR0025'; results found official/product/manual data but no row-specific factory manufacturing process."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Near-term KB modeling should treat this as a calibrated external sensor/transmitter module, because zirconia oxygen sensor fabrication and calibration are specialized precision-electronics work"
    - "The a planning decomposition inferred from the sourced product architecture and CAD shape, not a disclosed Angst+Pfister factory route."
  uncertainty_notes:
    - "A concrete self-manufacturing recipe would need sensor ceramic/electrode details, heater design, PCB schematic, connector and seal specifications, calibration procedure limits, and acceptance-test requirements."
kb_implications:
  - "item_granularity: complex_module - Model this row as one calibrated FCX-TR oxygen-transmitter complex module for this pass; split later only if oxygen-sensor/electronics manufacturing becomes a priority."
---
