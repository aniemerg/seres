---
row_identity:
  item: "17B"
  cad_file: "17B_dummy_oxygen_sensor_A19N"
  source_row_number: 243
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://sensorsandpower.angst-pfister.com/en/products/gas/product/pza-mc25-n-potentiometric-zirconia-oxygen-o2-gas-sensor-module/"
function:
  summary: "A19-N screw-in potentiometric zirconia oxygen sensor head for measuring oxygen partial pressure in the reAM250 gas/process atmosphere; it connects to the PZA-MC25 electronics module and is used for inline/diffusion-based oxygen measurement."
  source:
    url_or_path: "https://sensorsandpower.angst-pfister.com/fileadmin/products/datasheets/272/A19-Sensor-head_1620-21869-0002-E-0421.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; research/ream250_bom/ream250_bom_row_0243_17B__views_2x2.png"
    cited_fact_or_basis: "BOM row 243 and the manifest identify item 17B as Angst + Pfister 17B_dummy_oxygen_sensor_A19N with one matched vendor-component STEP. The A19-N/P manual identifies the A19 type as an oxygen measurement sensor, states that A19-N can be screw-mounted into the reaction space, and says the sensor connects to a converter module. The rendered CAD preview shows a cylindrical threaded probe/head form matching a screw-in sensor head. official_alternate_route_check: original BOM URL is the official Angst+Pfister PZA-MC25-N oxygen sensor module page; the cited A19 sensor-head PDF is an official Angst+Pfister datasheet/manual for the paired A19-N sensor head used by that module family and matches the row CAD name A19N."
    evidence_basis: "bom_provided"
  assumptions:
    - "The BOM item 17B represents the A19-N sensor head rather than the separate PZA-MC25 electronics unit, because the CAD file name is A19N and the geometry is a threaded sensor head."
  uncertainty_notes:
    - "The BOM row description field is blank; function is resolved from the row CAD filename, official PZA-MC25-N route, and official A19-N/P manual."
mass:
  value_kg: 1.0
  basis: "Per-unit mass for one A19-N oxygen sensor head. The A19-N/P manual lists weight as approximately 1 kg for Sensor A19-N / Sensor A19-P. BOM quantity is 1, so the row total is also about 1.0 kg. FreeCAD measured the row STEP as 1 solid, volume 164216.652 mm^3, surface area 18913.961 mm^2, and bounding box 67.00 x 80.50 x 67.00 mm; the manual weight is preferred over CAD-density calculation because the sensor is a multi-material assembly."
  source:
    url_or_path: "https://sensorsandpower.angst-pfister.com/fileadmin/products/datasheets/272/A19-Sensor-head_1620-21869-0002-E-0421.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17B_dummy_oxygen_sensor_A19N.step"
    cited_fact_or_basis: "The official A19-N/P manual lists Sensor A19-N / Sensor A19-P weight as approximately 1 kg and gives connection-head dimensions diameter 70 mm, height 75 mm including plug, plus A19-N mounting depth 30 mm with M27 x 2 mm screw-in thread. FreeCAD measured the supplied row STEP volume and bounding box. Local assembly STEP material extraction returned only Generic with density 1000.0, which is placeholder metadata and is not used for mass. official_alternate_route_check: original BOM URL is the official Angst+Pfister PZA-MC25-N module page; the cited official A19 sensor-head manual matches the row CAD A19N sensor head identity."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The manual gives an approximate weight and appears to cover both A19-N and A19-P variants; it does not state whether the supplied cable is included in that weight."
    - "The STEP is a single merged solid and does not separate stainless steel, aluminum, ceramic, heater, contacts, connector, or cable volumes."
material:
  primary_material: "stainless steel sensor body with aluminum plug/connection-head housing, stabilized zirconium oxide ceramic sensing element, and platinum contact layer; additional heater, connector, wiring, and sealing materials are present but not grade-resolved"
  source:
    url_or_path: "https://sensorsandpower.angst-pfister.com/fileadmin/products/datasheets/272/A19-Sensor-head_1620-21869-0002-E-0421.pdf"
    cited_fact_or_basis: "The A19-N/P manual states that the sensor is constructed of stabilized zirconium oxide, that the electrically conductive surface is generally platinum, and that the sensor is built into a stainless steel body with an aluminium housing and plug connection serving as the connection head. Local assembly STEP material extraction for 17B_dummy_oxygen_sensor_A19N returned only Generic with density 1000.0, which is placeholder metadata. official_alternate_route_check: original BOM URL is the official Angst+Pfister PZA-MC25-N module page; the official A19 sensor-head manual is the matching sensor-head route for the row CAD name A19N."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "Exact stainless alloy, aluminum alloy, zirconia dopant, heater alloy, connector polymer, cable composition, and seal material are not specified in the extracted official manual text."
how_to_make:
  summary: "Treat as a standard purchased Angst+Pfister/Metrotec A19-N oxygen sensor head for current KB modeling. A plausible local route would fabricate the stainless threaded probe body and aluminum connection head, produce or source the stabilized-zirconia sensing cell with platinum electrodes and heater, assemble the plug/cable interface and seals, then calibrate and test the sensor with its converter electronics."
  manufacturing_steps:
    - "Procurement route: buy the A19-N sensor head as the row-matched oxygen-sensor component for the PZA-MC25-N measurement system."
    - "Local route: machine the stainless steel screw-in body and M27 x 2 mm mounting thread, then make the aluminum connection-head housing and plug interface."
    - "Produce or source the stabilized zirconium oxide ceramic sensor element with conductive platinum contact layers and integrate the heater/temperature sensing elements required for high-temperature zirconia operation."
    - "Assemble internal wiring, connector, seals, and optional cable; leak-check the gas boundary and verify mechanical fit against the CAD/manual dimensions."
    - "Pair, calibrate, and function-test the sensor with the converter electronics over the relevant oxygen ranges before installation."
  source:
    url_or_path: "https://sensorsandpower.angst-pfister.com/fileadmin/products/datasheets/272/A19-Sensor-head_1620-21869-0002-E-0421.pdf; research/ream250_bom/ream250_bom_row_0243_17B__views_2x2.png"
    cited_fact_or_basis: "The official manual establishes the A19-N sensor identity, stainless body, aluminum connection head, stabilized-zirconia oxygen sensor construction, platinum contact layer, A19-N screw-in mounting, M27 x 2 mm thread, and need for a converter module. The rendered CAD preview shows a stepped cylindrical threaded sensor-head geometry. targeted_web_search: queries tried included 'A19-N potentiometric oxygen sensor dimensions weight material', 'A19N potentiometric oxygen sensor Angst Pfister material weight', and 'PZA-MC25-N A19-N oxygen sensor head material weight'; results found official product/manual facts but no source stating the supplier's detailed manufacturing process."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Detailed local fabrication steps are inferred from the sourced material stack, threaded sensor-head geometry, and common zirconia oxygen-sensor construction rather than from an Angst+Pfister manufacturing-process disclosure."
  uncertainty_notes:
    - "Actual supplier production likely uses specialized ceramic processing, electrode deposition, heater integration, sealing, calibration, and quality-control steps not fully specified by the public manual."
kb_implications:
  - "item_granularity: complex_module - Model as one oxygen sensor-head assembly for now; split into ceramic cell, metal body, heater, connector, cable, and calibration electronics only if gas-sensing hardware becomes a modeling bottleneck."
---
