---
row_identity:
  item: "1B1"
  cad_file: "1B1_door_plate"
  source_row_number: 9
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Large aluminum door plate for the reAM250 chamber door-side assembly, providing the main structural plate that carries or interfaces with the adjacent handle, schlieren-imaging flange/window stack, seals, cover hardware, hinges, and clamps."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1B1_door_plate.step; research/ream250_bom/ream250_bom_row_0009_1B1__views_2x2.png"
    cited_fact_or_basis: "BOM row 9 identifies item 1B1, quantity 1, CAD file 1B1_door_plate. Nearby rows list a door-side handle, schlieren-imaging flange, glass, seals, frame, cover, hinge parts, and clamps. The manifest maps row 9 to gold_export/parts/1B1_door_plate.step as a matched part export. FreeCAD measured one solid with bounding box 880.00 x 460.00 x 96.13 mm; the rendered contact sheet shows a broad thin ribbed/relieved plate form with a local aperture or mounting detail near one end."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row is interpreted as the main door plate because the BOM name is door_plate and the neighboring 1B/1D rows are door handle, window/seal/frame, cover, hinge, and clamp components."
  uncertainty_notes:
    - "The local CAD/BOM evidence identifies the structural door-plate role, but not the exact chamber sealing interface, load case, or mating hardware stack."
mass:
  value_kg: 34.96
  basis: "FreeCAD volume 12,949,065.633 mm^3 equals 0.012949066 m^3. The full assembly STEP material metadata identifies Aluminum 6061 with density 2700 kg/m^3 for 1B1_door_plate, giving 34.96 kg per unit. BOM quantity is 1, so the row total is also about 34.96 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1B1_door_plate.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 12,949,065.633 mm^3, area 855,108.207 mm^2, and bounding box 880.00 x 460.00 x 96.13 mm. Local assembly STEP material extraction for product 1B1_door_plate returned material Aluminum 6061 and density 2700.0, with the extractor noting the reAM250 export uses kg/m^3-like material densities."
    evidence_basis: "bom_provided"
  assumptions:
    - "The isolated STEP solid volume is used as the physical-volume proxy for one manufactured door plate."
    - "The assembly STEP density value is used directly for Aluminum 6061 mass calculation."
  uncertainty_notes:
    - "The rendered preview reports an 880.00 x 460.00 x 40.00 mm display bounding box while the raw FreeCAD shape read reports 96.13 mm in Z; the mass estimate uses volume rather than bounding-box thickness."
material:
  primary_material: "Aluminum 6061"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Local assembly STEP material extraction for product 1B1_door_plate returned material Aluminum 6061 and density 2700.0."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The BOM row material fields are blank, so material depends on the assembly STEP metadata rather than the CSV."
how_to_make:
  summary: "Fabricate as a custom machined Aluminum 6061 door plate from thick plate or billet stock, then finish the mounting/sealing and optical-door interface features."
  manufacturing_steps:
    - "Prepare Aluminum 6061 plate or billet large enough for the 880 mm by 460 mm door-plate envelope and the maximum local thickness or boss height"
    - "Rough CNC mill the plate faces, perimeter, ribs, pockets, reliefs, and local aperture or mounting features shown in the CAD."
    - "Drill, tap, countersink, or counterbore the mounting patterns needed for the handle, hinges, clamps, schlieren-imaging frame/window/seal stack, and cover hardware."
    - "Finish-machine sealing and mating faces, then deburr all edges and inspect flatness, hole positions, and interface alignment."
    - "Apply the required surface finish or cleaning route, such as anodizing or vacuum-compatible cleaning, only if later drawings or chamber requirements call for it."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1B1_door_plate.step; research/ream250_bom/ream250_bom_row_0009_1B1__views_2x2.png; web_search"
    cited_fact_or_basis: "The row-specific CAD and preview show one large 880 mm by 460 mm plate-like solid with ribs/reliefs and localized interface geometry; assembly STEP metadata identifies Aluminum 6061. targeted_web_search: queries tried \"1B1_door_plate reAM250\", \"reAM250 1B1 door plate\", and \"reAM250_BOM_gold 1B1\" results found duplicate BOM text and general reAM250 project pages, but no row-specific drawing, tolerance note, or manufacturing process route."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The part is treated as a custom simple machined structural plate because the BOM row has no manufacturer, product ID, or link URL and the CAD file is an assembly-specific door plate"
    - "CNC machining from Aluminum 6061 plate or billet is assumed from the large plate geometry, relieved/ribbed features, and expected need for accurate door, hinge, clamp, and optical-window interfaces."
  uncertainty_notes:
    - "The CAD/BOM evidence does not specify tolerances, surface finish, sealing flatness requirements, heat treatment, or whether the plate is machined from one thick stock piece versus assembled or welded from thinner stock."
kb_implications:
  - "item_granularity: simple_part - model later as one custom Aluminum 6061 machined door plate, not as a vendor module; neighboring handle, hinge, seal, window, frame, clamp, and cover rows should remain separate BOM items."
---

Research result for reAM250 BOM row 9.
