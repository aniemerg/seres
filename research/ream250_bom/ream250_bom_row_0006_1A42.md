---
row_identity:
  item: "1A42"
  cad_file: "1A42_flange_schlieren_imaging"
  source_row_number: 6
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Custom schlieren-imaging flange or optical interface bracket for the reAM250 1A-side schlieren imaging assembly; CAD shows a bolted rectangular flange face with a protruding cylindrical/conical optical tube feature."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1A42_flange_schlieren_imaging.step; research/ream250_bom/ream250_bom_row_0006_1A42__views_2x2.png"
    cited_fact_or_basis: "BOM row 6 states item 1A42, quantity 1, CAD file 1A42_flange_schlieren_imaging. The manifest maps the row to gold_export/parts/1A42_flange_schlieren_imaging.step as a matched part export. FreeCAD measured one solid with bounding box 80.00 x 114.40 x 160.00 mm. The rendered contact sheet shows a rectangular bolted frame/flange face and an angled cylindrical/conical tube feature."
    evidence_basis: "bom_provided"
  assumptions:
    - "The name flange_schlieren_imaging and visible tube/flange geometry are interpreted as an optical mount or interface for the schlieren imaging path."
  uncertainty_notes:
    - "The BOM/CAD evidence identifies the local mechanical role, but not the exact mating optic, adapter, or sealing interface."
mass:
  value_kg: 0.39
  basis: "FreeCAD volume 144446.714 mm^3 equals 0.000144447 m^3. Nominal value uses aluminum density 2700 kg/m^3 from kb/materials/properties.yaml, giving 0.390 kg. If the same CAD volume were generic steel at 7850 kg/m^3, mass would be about 1.13 kg; stainless steel at 8000 kg/m^3 would be about 1.16 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1A42_flange_schlieren_imaging.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 144446.714 mm^3, area 51677.320 mm^2, and bounding box 80.00 x 114.40 x 160.00 mm. The local density table lists aluminum density 2700 kg/m^3, steel density 7850 kg/m^3, and stainless_steel density 8000 kg/m^3. targeted_web_search: searched \"1A42_flange_schlieren_imaging material\", \"1A42 flange schlieren imaging material\", \"reAM250 1A42 schlieren\", and \"ream250 flange_schlieren_imaging\"; found duplicate BOM text and general schlieren references but no row-specific mass or material source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The STEP solid volume is used as the physical-volume proxy for one manufactured part."
    - "Aluminum is used as the nominal scenario because optical mounts and custom machine brackets are commonly aluminum, and the part geometry is a lightened custom flange rather than a heavy vacuum clamp."
  uncertainty_notes:
    - "Mass depends directly on unresolved material; use 0.39 kg as an aluminum-scenario estimate, with steel or stainless construction around 1.1-1.2 kg."
material:
  primary_material: "unknown structural metal/alloy"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1A42_flange_schlieren_imaging.step"
    cited_fact_or_basis: "BOM row 6 has blank material fields. The assembly STEP material extractor matched 1A42_flange_schlieren_imaging but returned material Generic and density 1000.0, which the task workflow treats as placeholder rather than resolved material evidence. CAD geometry is a bolted flange/tube mechanical bracket. targeted_web_search: searched \"1A42_flange_schlieren_imaging material\", \"1A42 flange schlieren imaging material\", \"reAM250 1A42 schlieren\", and \"ream250 flange_schlieren_imaging\"; found duplicate BOM text and general schlieren references but no row-specific material source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A structural metal/alloy family is inferred from the flange/bracket role, bolted rectangular face, optical tube feature, and machine-frame context."
  uncertainty_notes:
    - "The specific alloy or grade is not identified; aluminum alloy is plausible for an optical bracket, while steel or stainless steel remain possible if stiffness, vacuum, or thermal requirements dominate."
how_to_make:
  summary: "Fabricate as a machined metal optical flange/bracket from the resolved alloy, using CNC milling/boring for the flange face, bolt pattern, angled tube feature, and mating surfaces."
  manufacturing_steps:
    - "Select structural metal billet, thick plate, or near-net blank in the resolved alloy."
    - "CNC mill the rectangular flange/frame outline, bolt holes, and lightening or relief features visible on the face."
    - "Bore or machine the cylindrical/conical optical tube feature and its angled transition to the flange body."
    - "Finish-machine optical or sealing mating faces, then deburr and inspect hole positions, flatness, and tube alignment."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1A42_flange_schlieren_imaging.step; research/ream250_bom/ream250_bom_row_0006_1A42__views_2x2.png"
    cited_fact_or_basis: "CAD and preview show one 80.00 x 114.40 x 160.00 mm solid with a rectangular bolted flange/frame, diagonal/lightened face members, and a protruding cylindrical/conical tube feature. targeted_web_search: searched \"1A42_flange_schlieren_imaging material\", \"1A42 flange schlieren imaging material\", \"reAM250 1A42 schlieren\", and \"ream250 flange_schlieren_imaging\"; no row-specific manufacturing drawing, material callout, or process note was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The part is treated as a custom machined simple part rather than a purchased module because the BOM row has no manufacturer/product ID and the CAD name is a custom assembly-specific flange."
    - "Subtractive machining is assumed from the visible flange/tube geometry and expected need for accurate optical alignment or mating surfaces."
  uncertainty_notes:
    - "The CAD/BOM evidence does not specify tolerances, surface finish, coating/anodizing, or whether the tube feature is machined from one piece or joined from a separate tube."
kb_implications:
  - "item_granularity: simple_part - custom structural/optical flange likely modeled as one machined metal part, with material grade unresolved until a drawing or designer note identifies it."
---

Research result for reAM250 BOM row 6.
