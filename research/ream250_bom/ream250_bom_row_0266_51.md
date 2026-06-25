---
row_identity:
  item: "51"
  cad_file: "51_dummy_scanner"
  source_row_number: 266
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.raylase.de/_Resources/Persistent/4/9/b/7/49b7182a146725d34457ce6b213a228d737e26a8/RAYLASE_AM-MODUL NEXT GEN_en.pdf"
function:
  summary: "Raylase AM-MODULE NEXT GEN fiber-laser scan module for additive manufacturing; it provides fast beam deflection, digitally controlled scan positioning, variable spot size through a zoom axis, and process-monitoring optical outputs for cameras, pyrometers, or photodiodes."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/51_dummy_scanner.step; research/ream250_bom/ream250_bom_row_0266_51__views_2x2.png; https://www.raylase.de/_Resources/Persistent/4/9/b/7/49b7182a146725d34457ce6b213a228d737e26a8/RAYLASE_AM-MODUL NEXT GEN_en.pdf"
    cited_fact_or_basis: "BOM row 266 names item 51, quantity 1, CAD file 51_dummy_scanner, description AM-Module Next Gen, manufacturer Raylase, and the Raylase AM-MODULE NEXT GEN PDF route. Manifest row 266 maps the row to a matched vendor-component STEP. FreeCAD measured 1 solid with volume 34111966.482 mm^3, area 787778.761 mm^2, and bounding box 407.50 x 589.00 x 270.00 mm; the contact sheet shows a large scanner/module envelope with protruding mounting or optical-interface features. The Raylase PDF describes the AM-MODULE NEXT GEN as an additive-manufacturing module for fiber-coupled lasers with beam deflection, flexible spot diameter, digital control, process-control sensor connections, and multi-module operation over one build field."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The local CAD filename says dummy_scanner, so CAD shape is used for envelope/function consistency rather than for exact internal scanner layout."
mass:
  value_kg: 15.0
  basis: "Per unit. BOM quantity is 1, so the row total is about 15 kg if the row is the base module alone. The Raylase PDF gives approximate weights of 15 kg for the BASE-Module and 5 kg for the optional RAYSPECTOR monitoring unit; if this row includes RAYSPECTOR, planning mass would be about 20 kg. CAD volume 34111966.482 mm^3 is not converted by density because the vendor module is a hollow, multi-material calibrated assembly and local STEP material metadata only reports Generic at density 1000."
  source:
    url_or_path: "https://www.raylase.de/_Resources/Persistent/4/9/b/7/49b7182a146725d34457ce6b213a228d737e26a8/RAYLASE_AM-MODUL NEXT GEN_en.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/51_dummy_scanner.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Raylase mechanical data gives approximate weights for the BASE-Module and optional RAYSPECTOR. FreeCAD measured the row STEP as 1 solid, volume 34111966.482 mm^3, area 787778.761 mm^2, and bounding box 407.50 x 589.00 x 270.00 mm. The local assembly STEP material extractor matched 51_dummy_scanner but returned material Generic and density 1000.0."
    evidence_basis: "bom_provided"
  assumptions:
    - "The BOM row description AM-Module Next Gen is treated as the base scanner module, not the optional RAYSPECTOR add-on, because the row does not explicitly name RAYSPECTOR."
  uncertainty_notes:
    - "Mass may be approximately 20 kg instead of 15 kg if the row's CAD/assembly intent includes the optional RAYSPECTOR monitoring unit."
material:
  primary_material: "multi-material optomechatronic module: aluminum cooling-contact parts, silicon-carbide deflection mirrors with coating for 1060-1090 nm fiber lasers, galvanometer scanner/electronics, optical sets, lens/fiber interfaces, water/air-cooling connections, electrical/data connectors, and process-monitoring sensor interfaces"
  source:
    url_or_path: "https://www.raylase.de/_Resources/Persistent/4/9/b/7/49b7182a146725d34457ce6b213a228d737e26a8/RAYLASE_AM-MODUL NEXT GEN_en.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Raylase describes aluminum parts that require cooling-water corrosion protection, silicon-carbide mirror substrate for the 1060-1090 nm laser range, mirror variations, electronic components, galvanometer scanner, deflection mirrors, optical sets for fiber coupling, laser fiber socket, water connection, power/data connection, C-mount camera connection, and process-light outputs. Local assembly STEP material extraction matched the product but returned only Generic material and density 1000.0."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The PDF identifies material families and key optical/electronic components, but it does not provide a full sub-BOM, exact alloy grades, coatings beyond the mirror notation, or material fractions."
how_to_make:
  summary: "Machine integration with the laser fiber, power and RL3-100 data connection, water/air cooling services, and process-monitoring sensor paths. Local self-manufacture should be deferred until a detailed scanner/optics/electronics sub-BOM and calibration process are modeled"
  manufacturing_steps:
    - "Integrate the module mechanically using the CAD envelope and mounting/interface protrusions as layout constraints."
    - "Connect QBH laser fiber, +48 V power, RL3-100 data, water temperature control or air cooling as configured, and process-monitoring camera/pyrometer/photodiode paths."
    - "Commission the module through Raylase-style field setup, software adjustment, focus tracking, and process-monitoring calibration before production use."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; research/ream250_bom/ream250_bom_row_0266_51__views_2x2.png; https://www.raylase.de/_Resources/Persistent/4/9/b/7/49b7182a146725d34457ce6b213a228d737e26a8/RAYLASE_AM-MODUL NEXT GEN_en.pdf"
    cited_fact_or_basis: "BOM row 266 identifies the row as a Raylase AM-Module Next Gen. The Raylase PDF states that Raylase develops, manufactures, and tests its products in-house, and it describes the relevant fiber, power/data, water/air cooling, process-monitoring, setup, and software-adjustment interfaces. The contact sheet shows a simplified module envelope suitable for integration planning, not a local manufacturing sub-BOM."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "A future local-manufacturing model would need scanner motor, mirror, optical coating, electronics, cooling, alignment, and calibration details that are not exposed by the BOM row or PDF."
kb_implications:
  - "item_granularity: complex_module - Treat as a calibrated Raylase laser scan/monitoring subsystem for near-term KB modeling; split into galvo scanner, zoom/focus optics, mirrors, electronics, cooling hardware, and sensor paths only if a detailed optomechatronic scanner manufacturing workflow becomes a target."
---

# reAM250 BOM Row 266 - 51

Research result for the leased reAM250 BOM row.
