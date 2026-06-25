---
row_identity:
  item: "2AD7"
  cad_file: "2AD7_part_7"
  source_row_number: 50
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "One small spherical rolling element in the reAM250 top axis bearing group."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AD7_part_7.step; research/ream250_bom/ream250_bom_row_0050_2AD7__views_2x2.png"
    cited_fact_or_basis: "BOM row 50 lists item 2AD7, quantity 1, CAD file 2AD7_part_7, description 'axis bearing top'. Manifest row 50 maps the item to a matched part STEP. FreeCAD measured one solid with volume 63.506 mm^3 and a 4.95 x 4.95 x 4.95 mm bounding box; the rendered contact sheet shows a near-spherical ball."
    evidence_basis: "bom_provided"
  assumptions:
    - "The supplied per-row STEP represents one physical rolling element from the top axis bearing rather than a placeholder for the whole bearing assembly."
  uncertainty_notes:
    - "The BOM row does not show the full bearing layout, race geometry, or preload arrangement, so the exact bearing type is inferred only at the rolling-element level."
mass:
  value_kg: 0.0005
  basis: "Per-unit estimate for quantity 1. FreeCAD volume is 63.506 mm^3, equal to 6.3506e-8 m^3. Using the local generic steel density constant of 7850 kg/m^3 gives 0.000498 kg, rounded to 0.0005 kg. Generic 5 mm chrome-steel bearing-ball listings found by targeted search report about 0.513 g each, consistent with the CAD-density calculation."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AD7_part_7.step; kb/materials/properties.yaml; https://www.amazon.com/Chrome-Steel-Ball-Bearings-G25-500/dp/B01MSJVDV9; https://simplybearings.co.uk/shop/p35920/5mm-Diameter-Grade-100-Hardened-52100-Chrome-Steel-Ball-Bearings/product_info.html"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 63.506 mm^3 and bounding box about 4.95 mm on each axis. kb/materials/properties.yaml lists generic steel density 7850 kg/m^3. Agent-initiated searches for 5 mm bearing balls found generic chrome-steel examples with AISI 52100 material and about 0.513 g per ball, but no row-specific vendor source. targeted_web_search: tried '\"axis bearing top\" \"2AD7\"', '\"2AD7_part_7\"', '5 mm bearing ball material chrome steel AISI 52100', and '5mm chrome steel ball bearings G25 weight'; results confirmed duplicate BOM identity and generic 5 mm bearing-ball facts only."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The row item is treated as a solid steel-family bearing ball whose CAD volume is the finished physical volume."
    - "Generic steel density is used as the mass calculation constant because the local STEP material metadata is placeholder only."
  uncertainty_notes:
    - "Mass would shift slightly with exact alloy or ceramic substitution; no row-specific catalog mass or material grade was found."
material:
  primary_material: "hardened bearing steel or chrome-steel bearing-ball material family"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; https://www.amazon.com/Chrome-Steel-Ball-Bearings-G25-500/dp/B01MSJVDV9; https://simplybearings.co.uk/shop/p35920/5mm-Diameter-Grade-100-Hardened-52100-Chrome-Steel-Ball-Bearings/product_info.html"
    cited_fact_or_basis: "BOM row 50 gives no manufacturer, product ID, material hint, or link URL. Assembly STEP material extraction for product 2AD7_part_7 returned material 'Generic' with density 1000.0, which is placeholder metadata. Generic 5 mm bearing-ball product pages identify comparable balls as chrome steel or AISI 52100 hardened chrome steel. targeted_web_search: tried '\"axis bearing top\" \"2AD7\"', '\"reAM250\" \"axis bearing top\"', 'bearing balls material hardened chrome steel AISI 52100', and '5 mm bearing ball material chrome steel AISI 52100'; no row-specific material source was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The spherical 4.95 mm rolling-element geometry and 'axis bearing top' row description are most consistent with a hardened steel bearing ball."
  uncertainty_notes:
    - "The material family is not row-sourced; stainless, ceramic, or another bearing-ball material cannot be excluded without the bearing drawing or vendor bill of materials."
how_to_make:
  summary: "Prepare as a standard approximately 5 mm precision bearing ball for KB modeling, or manufacture locally from bearing-steel wire/slug by cold heading, flashing, heat treatment, grinding, lapping, cleaning, and inspection"
  manufacturing_steps:
    - "Cut bearing-steel wire or slug stock for the ball blank."
    - "Cold-head or otherwise form a near-spherical blank."
    - "Remove flash and heat-treat for bearing hardness."
    - "Grind and lap between precision plates to reach roundness, surface finish, and diameter tolerance."
    - "Clean, inspect diameter/roundness/surface quality, and lubricate or package for bearing assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AD7_part_7.step; research/ream250_bom/ream250_bom_row_0050_2AD7__views_2x2.png; https://insights.globalspec.com/article/12349/how-are-bearing-balls-made; https://resources.hartfordtechnologies.com/blog/high-quality-precision-ball-manufacturing-a-process-overview"
    cited_fact_or_basis: "The row STEP and preview show a single about-5 mm sphere. Generic bearing-ball manufacturing references describe grinding/lapping as precision finishing steps for steel balls. targeted_web_search: tried 'ball bearing manufacturing process lapping hardened steel', 'how are bearing balls made grinding lapping', and 'precision ball manufacturing process overview'; results provided generic ball-manufacturing process context but not a row-specific reAM250 manufacturing route."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Machine-specific part"
    - "The inferred from common bearing-ball production practice and the spherical CAD geometry."
  uncertainty_notes:
    - "No row-specific grade, tolerance class, surface finish, or heat-treatment specification is available from the BOM or CAD package."
kb_implications:
  - "item_granularity: simple_part - Model as a reusable small precision bearing ball/rolling element, not as a purchased module or custom axis-bearing subassembly."
---

Research result for the leased reAM250 BOM row.
