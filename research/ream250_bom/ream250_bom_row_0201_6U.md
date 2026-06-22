---
row_identity:
  item: "6U"
  cad_file: "6U_belt_pulley_motor_GT2_Bore6p35_20_teeth"
  source_row_number: 201
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.3vbelt.com/product/gt2-6mm-timing-belt-pulley-20-teeth/"
function:
  summary: "20-tooth GT2 timing pulley for a 6 mm timing belt, mounted on a 6.35 mm motor shaft to transmit synchronous belt motion without slip."
  source:
    url_or_path: "https://www.3vbelt.com/product/gt2-6mm-timing-belt-pulley-20-teeth/; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6U_belt_pulley_motor_GT2_Bore6p35_20_teeth.step; research/ream250_bom/ream250_bom_row_0201_6U__views_2x2.png"
    cited_fact_or_basis: "BOM row 201 identifies item 6U as manufacturer 3VBELT with CAD file 6U_belt_pulley_motor_GT2_Bore6p35_20_teeth and quantity 1. The 3VBELT row URL identifies the row-matched product as a GT2 timing pulley with 20 teeth, 6 mm belt width, and available 6.35 mm bore. FreeCAD measured one solid with about 14.94 x 14.94 x 18.00 mm bounding box, and the rendered preview shows a flanged toothed pulley with a central bore and side set-screw hole."
    evidence_basis: "bom_provided"
  assumptions:
    - "The BOM CAD filename's Bore6p35 and the vendor option list's 6.35 mm bore identify the selected motor-shaft variant."
  uncertainty_notes: []
mass:
  value_kg: 0.00426
  basis: "FreeCAD measured the row STEP volume as 1577.728 mm^3, equal to 1.577728e-6 m^3. The local assembly STEP material extractor returned Aluminum 6061 with density 2700 kg/m^3, matching the local aluminum density constant in kb/materials/properties.yaml. 1.577728e-6 m^3 * 2700 kg/m^3 = 0.0042609 kg per pulley. BOM quantity is 1, so the row total is also about 0.00426 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6U_belt_pulley_motor_GT2_Bore6p35_20_teeth.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured one solid, volume 1577.728 mm^3, surface area 1642.181 mm^2, and bounding box 14.94 x 14.94 x 18.00 mm. The local assembly STEP material extractor matched product 6U_belt_pulley_motor_GT2_Bore6p35_20_teeth to Aluminum 6061 with density 2700.0. kb/materials/properties.yaml lists aluminum density as 2700 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The single row STEP solid volume represents one physical pulley, including flanges and hub features, and is suitable for per-unit BOM mass."
    - "The Aluminum 6061 STEP material is represented by the repo's aluminum density constant for mass calculation."
  uncertainty_notes:
    - "The CAD model may omit tiny fastener/set-screw mass if the pulley is supplied with a separate screw; this is small relative to the pulley mass for KB planning."
material:
  primary_material: "Aluminum 6061 / aluminum alloy pulley body"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; https://www.3vbelt.com/product/gt2-6mm-timing-belt-pulley-20-teeth/"
    cited_fact_or_basis: "The local assembly STEP material extractor matched this product to Aluminum 6061 with density 2700.0. The row-matched 3VBELT product page lists the pulley material as aluminum alloy."
    evidence_basis: "bom_provided"
  assumptions:
    - "Any small set screw or finish/coating is not treated as a separate material for this BOM row because the row CAD and vendor page define the pulley body material."
  uncertainty_notes:
    - "The vendor page gives only aluminum alloy; the more specific Aluminum 6061 grade comes from local STEP material metadata rather than the public product page."
how_to_make:
  summary: "Procure as a standard 3VBELT GT2 20-tooth, 6 mm belt-width, 6.35 mm bore timing pulley; a plausible local route is to machine an Aluminum 6061 pulley blank, cut the GT2 tooth profile and flanges/hub, drill/bore the 6.35 mm shaft hole and set-screw hole, then deburr and inspect belt/shaft fit."
  manufacturing_steps:
    - "Procurement route: buy the row-matched 3VBELT GT2-6mm-20T pulley variant with 6.35 mm bore."
    - "Local route: start from aluminum alloy bar or a near-net pulley blank sized for about 15 mm outside diameter and 18 mm length."
    - "Turn the OD, hub, bore, and flanges; cut or hob the 20-tooth GT2 belt profile; drill and tap the radial set-screw hole visible in the CAD preview."
    - "Deburr/anodize or finish if required, then inspect tooth count, 6 mm belt-width interface, 6.35 mm bore fit, and pulley runout."
  source:
    url_or_path: "https://www.3vbelt.com/product/gt2-6mm-timing-belt-pulley-20-teeth/; research/ream250_bom/ream250_bom_row_0201_6U__views_2x2.png"
    cited_fact_or_basis: "The 3VBELT product route establishes the standard purchased product identity, tooth count, belt width, material family, and bore variants. The rendered CAD contact sheet shows a flanged toothed pulley with central bore and side set-screw hole. targeted_web_search: queries tried included 'GT2 6mm timing belt pulley 20 teeth aluminum alloy 6.35mm bore manufacturing machined hobbing' and 'GT2 20 tooth timing pulley aluminum set screw hobbing machining'; results found matching aluminum GT2 pulley product/spec listings but no row-specific supplier manufacturing process, so detailed local operations are inferred from geometry and standard pulley fabrication practice."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "For current KB planning, procurement as a commodity timing pulley is the preferred route unless local small-pulley machining becomes a modeled capability."
    - "The local manufacturing path assumes a one-piece aluminum pulley body with a set-screw hole, consistent with the CAD preview."
  uncertainty_notes:
    - "Exact factory process, surface treatment, tooth-profile tolerance, and whether a separate set screw is included are not specified by the row evidence."
kb_implications:
  - "item_granularity: simple_part - model as reusable standard GT2 aluminum timing pulley hardware with bore/tooth/belt-width parameters, not as a reAM250-specific purchased module."
---
