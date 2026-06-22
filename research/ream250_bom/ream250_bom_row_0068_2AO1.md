---
row_identity:
  item: "2AO1"
  cad_file: "2AO1_flange"
  source_row_number: 68
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Custom square flange or interface frame in the reAM250 2A motion/heating-area assembly; CAD shows a low-profile square ring with an open center, perimeter/corner mounting holes, and diagonal lightening or stiffening features."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AO1_flange.step; research/ream250_bom/ream250_bom_row_0068_2AO1__views_2x2.png"
    cited_fact_or_basis: "BOM row 68 states item 2AO1, quantity 1, CAD file 2AO1_flange. The manifest maps the row to gold_export/parts/2AO1_flange.step as a matched part export. FreeCAD measured one solid with bounding box 368.00 x 368.00 x 28.00 mm. The rendered contact sheet shows a flat square frame/flange with an open center, perimeter/corner holes, and diagonal rib or relief geometry."
    evidence_basis: "bom_provided"
  assumptions:
    - "The BOM name flange and the square bolted frame geometry are interpreted as a mechanical interface or support flange for neighboring 2A-axis or 2AP heating/platform components."
  uncertainty_notes:
    - "The BOM/CAD evidence identifies the local flange role, but not the exact mating parts, sealing function, or load path."
mass:
  value_kg: 4.76
  basis: "FreeCAD volume 1762872.821 mm^3 equals 0.001762873 m^3. Nominal value uses aluminum density 2700 kg/m^3 from kb/materials/properties.yaml, giving 4.76 kg for quantity 1. If the same CAD volume were generic steel at 7850 kg/m^3, mass would be about 13.84 kg; stainless steel at 8000 kg/m^3 would be about 14.10 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AO1_flange.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 1762872.821 mm^3, area 224791.131 mm^2, and bounding box 368.00 x 368.00 x 28.00 mm. The local density table lists aluminum density 2700 kg/m^3, steel density 7850 kg/m^3, and stainless_steel density 8000 kg/m^3. targeted_web_search: searched \"2AO1_flange\", \"2AO1 reAM250 flange\", \"reAM250 2AO1\", and \"reAM250 additive manufacturing machine flange 2AO1\"; found duplicate BOM text but no row-specific mass, drawing, or material source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The STEP solid volume is used as the physical-volume proxy for one manufactured part."
    - "Aluminum is used as the nominal scenario because the row is a large lightened custom machine flange/frame near motion and heating-platform components, where machined aluminum plate is a plausible low-mass structural choice in the absence of a material callout."
  uncertainty_notes:
    - "Mass depends directly on unresolved material; use 4.76 kg as an aluminum-scenario estimate, with steel or stainless construction near 14 kg."
material:
  primary_material: "unknown structural metal/alloy"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AO1_flange.step; research/ream250_bom/ream250_bom_row_0068_2AO1__views_2x2.png"
    cited_fact_or_basis: "BOM row 68 has blank material fields. The assembly STEP material extractor matched 2AO1_flange but returned material Generic and density 1000.0, which the task workflow treats as placeholder rather than resolved material evidence. CAD geometry is a bolted square flange/frame mechanical part. targeted_web_search: searched \"2AO1_flange\", \"2AO1 reAM250 flange\", \"reAM250 2AO1\", and \"reAM250 additive manufacturing machine flange 2AO1\"; found duplicate BOM text but no row-specific material source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A structural metal/alloy family is inferred from the flange name, bolted frame geometry, and placement among shaft, motor mount, guidance, spring plate, assembly plate, and heating plate rows."
  uncertainty_notes:
    - "The specific alloy or grade is not identified; aluminum alloy is plausible for a lightened custom machine frame, while steel or stainless steel remain possible if stiffness, thermal, or sealing requirements dominate."
how_to_make:
  summary: "Fabricate as a custom machined metal flange/frame from plate stock in the resolved alloy, with the open center, lightening pockets or ribs, and mounting-hole pattern cut to the CAD geometry."
  manufacturing_steps:
    - "Select structural metal plate stock in the resolved alloy, sized for the 368 x 368 mm footprint and about 28 mm final thickness."
    - "CNC mill or profile-cut the square outer perimeter, open center, diagonal relief/stiffening geometry, and corner/perimeter features."
    - "Drill and, where required by the mating hardware, countersink or counterbore the mounting holes visible around the frame."
    - "Finish-machine mating faces for flatness, deburr all edges, and inspect hole positions, outer dimensions, and frame flatness."
    - "Apply anodizing, passivation, blackening, or cleaning only if later design evidence specifies the alloy and environment."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AO1_flange.step; research/ream250_bom/ream250_bom_row_0068_2AO1__views_2x2.png"
    cited_fact_or_basis: "CAD and preview show one 368.00 x 368.00 x 28.00 mm solid with a square open-frame flange, perimeter/corner holes, and diagonal relief or stiffening features. targeted_web_search: searched \"2AO1_flange\", \"2AO1 reAM250 flange\", \"reAM250 2AO1\", and \"reAM250 additive manufacturing machine flange 2AO1\"; no row-specific manufacturing drawing, material callout, or process note was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The part is treated as a custom simple part rather than a purchased module because the BOM row has no manufacturer, product ID, or link URL and the CAD name is a machine-specific flange."
    - "Subtractive machining from plate stock is assumed from the large flat flange geometry and expected need for accurate mounting faces and hole positions."
  uncertainty_notes:
    - "The CAD/BOM evidence does not specify tolerances, surface finish, coating, or whether this flange has thermal, vacuum, or sealing requirements."
kb_implications:
  - "item_granularity: simple_part - model as one custom machined structural flange/frame, with material grade unresolved until a drawing or designer note identifies it."
---

Research result for reAM250 BOM row 68.
