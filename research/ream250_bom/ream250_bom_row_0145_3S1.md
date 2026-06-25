---
row_identity:
  item: "3S1"
  cad_file: "3S1_flange"
  source_row_number: 145
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Custom flange or interface plate for the reAM250 3S gas-outlet area; CAD shows a thin round/square flange-like plate with a central square opening, radial webbing, and small mounting holes."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3S1_flange.step; research/ream250_bom/ream250_bom_row_0145_3S1__views_2x2.png"
    cited_fact_or_basis: "BOM row 145 states item 3S1, quantity 1, CAD file 3S1_flange. Neighboring BOM rows 147-159 are labeled gas outlet pipe/parts. The manifest maps row 145 to gold_export/parts/3S1_flange.step as a matched part export. FreeCAD measured one solid with bounding box 130.00 x 8.00 x 130.00 mm. The rendered contact sheet shows a thin flange/interface plate with a central square aperture, radial triangular webs, and small mounting holes around the perimeter."
    evidence_basis: "bom_provided"
  assumptions:
    - "The 3S grouping and adjacent gas-outlet rows are interpreted as local assembly context for this otherwise unlabeled flange."
  uncertainty_notes:
    - "The BOM/CAD evidence identifies a flange-like interface role, but not the exact mating gas outlet part, seal, or fastener pattern standard."
mass:
  value_kg: 0.48
  basis: "FreeCAD volume 59802.285 mm^3 equals 0.000059802 m^3. Nominal value uses stainless_steel density 8000 kg/m^3 from kb/materials/properties.yaml, giving 0.478 kg per unit. Quantity is 1, so the row total is also about 0.48 kg. If the same CAD volume were aluminum at 2700 kg/m^3, mass would be about 0.16 kg; generic steel at 7850 kg/m^3 would be about 0.47 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3S1_flange.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 59802.285 mm^3, area 24214.494 mm^2, and bounding box 130.00 x 8.00 x 130.00 mm. The local density table lists stainless_steel density 8000 kg/m^3, steel density 7850 kg/m^3, and aluminum density 2700 kg/m^3. targeted_web_search: searched \"3S1_flange\", \"reAM250 3S1 flange\", \"3S1 flange reAM250\", and \"reAM250 gas outlet flange material\"; found duplicate BOM/project references but no row-specific material, drawing mass, or vendor specification."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The STEP solid volume is used as the physical-volume proxy for one manufactured item."
    - "Stainless steel is used as the nominal mass scenario because the part sits among gas/vacuum outlet hardware and has flange geometry, but the exact alloy is not sourced."
  uncertainty_notes:
    - "Mass depends directly on unresolved material; use 0.48 kg as a stainless/steel scenario estimate, with aluminum construction closer to 0.16 kg."
material:
  primary_material: "unknown structural metal/alloy"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3S1_flange.step; research/ream250_bom/ream250_bom_row_0145_3S1__views_2x2.png"
    cited_fact_or_basis: "BOM row 145 has blank manufacturer, product ID, material family, and material grade fields. The assembly STEP material extractor matched 3S1_flange but returned material Generic and density 1000.0, which is placeholder metadata under the task criteria. CAD geometry is a thin bolted flange/interface plate in the gas-outlet row group. targeted_web_search: searched \"3S1_flange\", \"reAM250 3S1 flange\", \"3S1 flange reAM250\", and \"reAM250 gas outlet flange material\"; found duplicate BOM/project references but no row-specific material callout."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A structural metal/alloy family is inferred from the flange role, bolted geometry, and adjacent gas/vacuum outlet hardware."
  uncertainty_notes:
    - "The specific alloy or grade is not identified; stainless steel is plausible for gas/vacuum compatibility, but aluminum or another structural alloy cannot be ruled out from the available row evidence."
how_to_make:
  summary: "Fabricate as a custom machined or profile-cut metal flange plate from the resolved alloy, then finish the mating faces and mounting holes."
  manufacturing_steps:
    - "Select structural metal plate stock in the resolved alloy, nominally slightly thicker than the 8 mm finished part."
    - "Profile-cut or CNC mill the outside round/square contour, central square aperture, and radial web/lightening geometry shown in CAD."
    - "Drill, ream, countersink, or counterbore the small mounting holes as required by the mating gas-outlet assembly."
    - "Finish-machine sealing or mating faces for flatness, then deburr the web and aperture edges."
    - "Clean and passivate, anodize, or otherwise finish only after the final material and gas/vacuum compatibility requirements are resolved."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3S1_flange.step; research/ream250_bom/ream250_bom_row_0145_3S1__views_2x2.png"
    cited_fact_or_basis: "CAD and preview show one 130.00 x 8.00 x 130.00 mm solid with a thin flange/interface plate, central square aperture, radial webbing, and small perimeter mounting holes. targeted_web_search: searched \"3S1_flange\", \"reAM250 3S1 flange\", \"3S1 flange reAM250\", and \"reAM250 gas outlet flange material\" no row-specific manufacturing drawing, material callout, or process note was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The part is treated as a custom simple part because the BOM row has no manufacturer/product ID and the CAD file is a custom-named flange"
    - "Subtractive machining or plate profile-cutting is assumed from the thin plate geometry and need for controlled aperture, hole placement, and mating-face flatness."
  uncertainty_notes:
    - "The CAD/BOM evidence does not specify tolerances, surface finish, sealing features, or whether post-machining vacuum cleaning/passivation is required."
kb_implications:
  - "item_granularity: simple_part - custom gas-outlet flange/interface plate should be modeled as one reusable machined metal part once material grade and mating interface are resolved."
---

Research result for reAM250 BOM row 145.
