---
row_identity:
  item: "1A52"
  cad_file: "1A52_cover"
  source_row_number: 8
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Small cover plate for the inside schlieren-imaging area of the reAM250 chamber/back assembly, likely closing or protecting the adjacent 1A51 seal/interface."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1A52_cover.step; research/ream250_bom/ream250_bom_row_0008_1A52__views_2x2.png; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "BOM row 8 names item 1A52 as 1A52_cover, quantity 1. The manifest maps it to gold_export/parts/1A52_cover.step as a matched_existing part. FreeCAD measured one solid with bounding box 99.00 x 69.00 x 7.00 mm, and the rendered contact sheet shows a shallow rectangular cover with a raised perimeter and four corner holes. The full assembly places 1A52_cover under 1A50_schlieren_imaging_inside next to 1A51_seal."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row name 'cover' and nearby 1A51_seal context identify this as a local closure/protective plate rather than an optical element or active module."
  uncertainty_notes:
    - "The CAD/BOM do not state which opening or mating hardware this cover serves, so the function is limited to the cover role within the 1A50 schlieren-imaging-inside subassembly."
mass:
  value_kg: 0.114
  basis: "Per-unit estimate for quantity 1. CAD volume is 42,334.514 mm^3 = 0.000042334514 m^3. Using aluminum density 2700 kg/m^3 from kb/materials/properties.yaml gives 0.114 kg. If the unresolved metal is steel at 7850 kg/m^3, the same CAD volume would be about 0.332 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1A52_cover.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured one solid with STEP volume 42,334.514 mm^3; local material table gives aluminum density 2700 kg/m^3 and steel density 7850 kg/m^3. targeted_web_search: queries tried: '1A52_cover reAM250', '1A52 schlieren imaging cover', and 'reAM250 1A52 cover'; result: found duplicate BOM text but no row-specific mass or material source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The CAD solid volume is used as the physical volume of one cover."
    - "Aluminum is used as the planning density because this is a small removable-looking cover plate in an optical/chamber subassembly and the BOM provides no material."
  uncertainty_notes:
    - "The exact mass remains material-dependent; the plausible metal range is roughly 0.11 kg for aluminum to 0.33 kg for steel."
material:
  primary_material: "unknown metal/alloy cover-plate material"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1A52_cover.step; https://www.scribd.com/document/888397420/reAm250-BoM-en-v1-1-0-1"
    cited_fact_or_basis: "Assembly STEP material extraction for 1A52_cover reports only Generic with density 1000.0. The CAD preview shows an opaque plate-like part rather than glass or elastomer. The public mirrored BOM text repeats 1A52 1 1A52_cover without a material field. targeted_web_search: queries tried: '1A52_cover reAM250 material', '1A52 schlieren imaging cover material', and 'reAM250 1A52 cover material'; result: no row-specific material source was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The cover is treated as metal/alloy because the geometry is a thin rigid plate with countersunk or counterbored mounting features, not a flexible seal or optical window."
  uncertainty_notes:
    - "No BOM field, STEP metadata, supplier route, or row-specific web source resolves the exact alloy, grade, or finish."
how_to_make:
  summary: "Make as a custom machined cover plate from aluminum or steel plate stock: cut the rectangular blank, mill the raised perimeter/recess geometry, drill and countersink or counterbore the four corner mounting holes, deburr, finish, and inspect fit against the mating seal/interface."
  manufacturing_steps:
    - "Cut a blank slightly larger than the 99.00 x 69.00 x 7.00 mm CAD envelope from selected plate stock."
    - "CNC mill the perimeter lip/recess geometry and the shallow face features visible in the STEP preview."
    - "Drill the four corner mounting holes and machine the visible counterbore or countersink features."
    - "Deburr all edges, clean the cover, and apply anodizing, passivation, or coating appropriate to the final alloy and chamber environment."
    - "Inspect hole positions, flatness, and fit against the adjacent seal or mating flange before installation."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1A52_cover.step; research/ream250_bom/ream250_bom_row_0008_1A52__views_2x2.png; https://www.emachineshop.com/aluminum/"
    cited_fact_or_basis: "CAD geometry shows a shallow rectangular cover plate with raised perimeter and four corner holes; eMachineShop describes custom aluminum parts made by uploading CAD for machining/ordering. targeted_web_search: queries tried: 'custom machined aluminum cover plate four holes manufacturing' and 'custom CNC aluminum plate cover machining'; result: general custom CNC plate machining routes found, but no row-specific manufacturing drawing."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The manufacturing route is inferred from the compact plate geometry and visible machined hole/lip features."
    - "A plate-stock CNC route is preferred over casting or additive manufacturing because the part is thin, simple, and has planar machined features."
  uncertainty_notes:
    - "Exact process details depend on the unresolved alloy, finish requirement, and mating seal geometry."
kb_implications:
  - "item_granularity: simple_part - Model as one custom cover plate with reusable plate-cutting/machining operations; keep material broad until a row-specific drawing or alloy source is recovered."
---
