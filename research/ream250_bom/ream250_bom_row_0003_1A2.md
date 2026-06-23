---
row_identity:
  item: "1A2"
  cad_file: "1A2_flange_schlieren_imaging"
  source_row_number: 3
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Custom schlieren-imaging flange or optical interface frame for the reAM250 1A-side schlieren imaging assembly; CAD shows a thin rectangular bolted frame/plate with diagonal lightening or stiffening features."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1A2_flange_schlieren_imaging.step; research/ream250_bom/ream250_bom_row_0003_1A2__views_2x2.png"
    cited_fact_or_basis: "BOM row 3 states item 1A2, quantity 1, CAD file 1A2_flange_schlieren_imaging. The manifest maps the row to gold_export/parts/1A2_flange_schlieren_imaging.step as a matched part export. FreeCAD measured one solid with bounding box 80.00 x 10.00 x 160.00 mm. The rendered contact sheet shows a thin rectangular frame or flange face with corner fastener holes and diagonal rib/lightening geometry."
    evidence_basis: "bom_provided"
  assumptions:
    - "The name flange_schlieren_imaging and the thin bolted rectangular geometry are interpreted as a mechanical interface for the schlieren imaging optical path or cover assembly."
  uncertainty_notes:
    - "The BOM/CAD evidence identifies the local mechanical role, but not the exact mating optic, window, seal, or neighboring plate interface."
mass:
  value_kg: 0.33
  basis: "FreeCAD volume 122504.602 mm^3 equals 0.000122505 m^3. Nominal value uses aluminum density 2700 kg/m^3 from kb/materials/properties.yaml, giving 0.331 kg. If the same CAD volume were generic steel at 7850 kg/m^3, mass would be about 0.96 kg; stainless steel at 8000 kg/m^3 would be about 0.98 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1A2_flange_schlieren_imaging.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 122504.602 mm^3, area 31198.586 mm^2, and bounding box 80.00 x 10.00 x 160.00 mm. The local density table lists aluminum density 2700 kg/m^3, steel density 7850 kg/m^3, and stainless_steel density 8000 kg/m^3. targeted_web_search: searched \"1A2_flange_schlieren_imaging\", \"flange schlieren imaging material\", \"reAM250 flange_schlieren_imaging\", and \"schlieren imaging flange material additive manufacturing machine\"; found duplicate BOM text and general schlieren references but no row-specific mass or material source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The STEP solid volume is used as the physical-volume proxy for one manufactured part."
    - "Aluminum is used as the nominal scenario because custom optical mounts, plates, and lightened machine brackets are commonly aluminum when no vacuum, thermal, or high-load material requirement is specified."
  uncertainty_notes:
    - "Mass depends directly on unresolved material; use 0.33 kg as an aluminum-scenario estimate, with steel or stainless construction near 1.0 kg."
material:
  primary_material: "unknown structural metal/alloy"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1A2_flange_schlieren_imaging.step; research/ream250_bom/ream250_bom_row_0003_1A2__views_2x2.png"
    cited_fact_or_basis: "BOM row 3 has blank material fields. The assembly STEP material extractor matched 1A2_flange_schlieren_imaging but returned material Generic and density 1000.0, which the task workflow treats as placeholder rather than resolved material evidence. CAD geometry is a bolted thin flange/frame mechanical part. targeted_web_search: searched \"1A2_flange_schlieren_imaging\", \"flange schlieren imaging material\", \"reAM250 flange_schlieren_imaging\", and \"schlieren imaging flange material additive manufacturing machine\"; found duplicate BOM text and general schlieren references but no row-specific material source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A structural metal/alloy family is inferred from the flange/frame role, bolted corners, thin machined-plate geometry, and machine optical-interface context."
  uncertainty_notes:
    - "The specific alloy or grade is not identified; aluminum alloy is plausible for a custom optical frame, while steel or stainless steel remain possible if stiffness, thermal stability, vacuum compatibility, or sealing requirements dominate."
how_to_make:
  summary: "Fabricate as a machined metal schlieren-imaging flange/frame from the resolved alloy, most likely by CNC milling a plate blank and drilling/countersinking the mounting pattern."
  manufacturing_steps:
    - "Select structural metal plate stock in the resolved alloy, nominally about 10 mm thick before finish machining."
    - "CNC mill or profile-cut the rectangular outer frame, inner relief/lightening geometry, and diagonal rib-like features visible in the CAD."
    - "Drill and, if required by the mating fasteners, countersink or counterbore the corner and edge mounting holes."
    - "Finish-machine mating faces for flatness, then deburr edges and inspect hole positions, frame flatness, and optical-interface alignment."
    - "Apply surface finish or coating only if later design evidence requires anodizing, passivation, blackening, or vacuum-compatible cleaning."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1A2_flange_schlieren_imaging.step; research/ream250_bom/ream250_bom_row_0003_1A2__views_2x2.png"
    cited_fact_or_basis: "CAD and preview show one 80.00 x 10.00 x 160.00 mm solid with a thin rectangular frame/flange, corner fastener holes, and diagonal relief/stiffening geometry. targeted_web_search: searched \"1A2_flange_schlieren_imaging\", \"flange schlieren imaging material\", \"reAM250 flange_schlieren_imaging\", and \"schlieren imaging flange material additive manufacturing machine\"; no row-specific manufacturing drawing, material callout, or process note was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The part is treated as a custom machined simple part rather than a purchased module because the BOM row has no manufacturer/product ID and the CAD name is a custom assembly-specific flange."
    - "Subtractive machining from plate stock is assumed from the thin rectangular flange geometry and expected need for accurate mounting-hole and optical-interface alignment."
  uncertainty_notes:
    - "The CAD/BOM evidence does not specify tolerances, surface finish, coating, or whether any sealing groove or optical aperture detail is hidden by the exported solid representation."
kb_implications:
  - "item_granularity: simple_part - custom structural/optical flange likely modeled as one machined metal plate/frame, with material grade unresolved until a drawing or designer note identifies it."
---

Research result for reAM250 BOM row 3.
